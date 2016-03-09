
import sys
from os import listdir
from os.path import isfile, join
import xml.etree.cElementTree as cET

def is_number(type_):
    return type_ in ['int(11)', 'bigint(20)', 'double']

def default_value(type_):
    if is_number(type_):
        return 0
    elif type_ == 'datetime':
        return '1970-01-01 00:00:00'
    else:
        return ''

if len(sys.argv) < 2:
    print('Usage: python3 ./MasterDataTool.py develop')
    sys.exit()

T = '    '
PHASE = sys.argv[1]

PATH = './' + PHASE
FILES = [f for f in listdir(PATH) if isfile(join(PATH, f))]

NS = '{urn:schemas-microsoft-com:office:spreadsheet}'
NS_WORKSHEET = NS + 'Worksheet'
NS_NAME = NS + 'Name'
NS_TABLE = NS + 'Table'
NS_ROW = NS + 'Row'
NS_CELL = NS + 'Cell'
NS_INDEX = NS + 'Index'
NS_DATA = NS + 'Data'

for f in FILES:
    column_visibilities = []
    column_names = []
    column_types = []

    tree = cET.parse(join(PATH, f))
    root = tree.getroot()

    for worksheet in root.iter(tag=NS_WORKSHEET):
        name = worksheet.attrib[NS_NAME]
        fh = open('../src/mst_' + name + '.py', 'w')
        fh.write('\n# ' + f + '\n\ndata = {\n')

        column_visibilities.clear()
        column_names.clear()
        column_types.clear()

        row_index = 0
        column_idx = 0
        column_len = 0

        table = worksheet.find(NS_TABLE)
        for row in table.iter(tag=NS_ROW):

            if row_index == 0: # colum_visibility
                fh.write(T + '# column_visibility\n')
                for cell in row.iter(tag=NS_CELL):
                    data = cell.find(NS_DATA)
                    if data is not None and data.text is not None:
                        if data.text == 'END_OF_COLUMNS':
                            break
                        column_visibilities.append(data.text)
                        fh.write(T + '# ' + T + data.text + '\n')

                column_len = len(column_visibilities)

            elif row_index == 1: # colum_name
                fh.write(T + '# column_name\n')
                column_idx = 0
                for cell in row.iter(tag=NS_CELL):
                    if column_idx == column_len:
                        break

                    data = cell.find(NS_DATA)
                    if data is not None and data.text is not None:
                        column_names.append(data.text)
                        fh.write(T + '# ' + T + data.text + '\n')

                    column_idx += 1

                if len(column_visibilities) != len(column_names):
                    print('error : column_visibility_count and column_name_count mismatch')
                    sys.exit()

            elif row_index == 2: # colum_type
                fh.write(T + '# column_type\n')
                column_idx = 0
                for cell in row.iter(tag=NS_CELL):
                    if column_idx == column_len:
                        break

                    data = cell.find(NS_DATA)
                    if data is not None and data.text is not None:
                        column_types.append(data.text)
                        fh.write(T + '# ' + T + data.text + '\n')

                    column_idx += 1

                if len(column_visibilities) != len(column_types):
                    print('error : column_visibility_count and column_type_count mismatch')
                    sys.exit()

            elif row_index == 3: # colum_description
                row_index += 1
                continue

            else: # data
                #fh.write(T + '# data')
                column_idx = 0
                data_mid = None
                for cell in row.iter(tag=NS_CELL):
                    if data_mid is not None and NS_INDEX in cell.attrib:
                        #fh.write(cell.attrib[NS_INDEX])
                        cell_attrib_index = int(cell.attrib[NS_INDEX]) - 1
                        while column_idx < cell_attrib_index and column_idx < column_len:
                            fh.write(T + T + "'" + column_names[column_idx] + "':" +
                                  str(default_value(column_types[column_idx])) + ',\n')
                            column_idx += 1

                    if column_idx == column_len:
                        break

                    data = cell.find(NS_DATA)
                    if data is not None and data.text is not None:
                        if data.text == 'END_OF_DATA':
                            break

                        visible = column_visibilities[column_idx] != 'unlisted'

                        if column_idx == 0:
                            data_mid = data.text
                            fh.write(T + data.text + ':{\n')

                        elif visible and column_types[column_idx] == 'list<varchar(50)>':
                            fh.write(T + T + "'" + column_names[column_idx] + "':['" +
                                  data.text.replace(';', "', '") + "'],\n")

                        elif visible and 'list' in column_types[column_idx]:
                            fh.write(T + T + "'" + column_names[column_idx] + "':[" +
                                  data.text.replace(';', ', ') + '],\n')

                        elif visible:
                            if is_number(column_types[column_idx]):
                                fh.write(T + T + "'" + column_names[column_idx] + "':" +
                                      data.text + ',\n')

                            else:
                                fh.write(T + T + "'" + column_names[column_idx] + "':'" +
                                      data.text + "',\n")

                    column_idx += 1

                if column_idx == column_len:
                    fh.write(T + '},\n')

            row_index += 1

        fh.write('}\n')
        fh.close()

