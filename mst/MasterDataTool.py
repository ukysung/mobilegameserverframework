
import sys
import json

from os import listdir
from os.path import isfile, join

import xml.etree.cElementTree as cET

def is_int(type_):
    return type_ in ['int(11)', 'bigint(20)']

def is_float(type_):
    return type_ == 'double'

def default_value(type_):
    if is_int(type_) or is_float(type_):
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
        print(f + ' : ' + name)

        mst_dict = {}
        column_visibilities.clear()
        column_names.clear()
        column_types.clear()

        row_index = 0
        column_idx = 0
        column_len = 0

        table = worksheet.find(NS_TABLE)
        for row in table.iter(tag=NS_ROW):

            if row_index == 0: # colum_visibility
                for cell in row.iter(tag=NS_CELL):
                    data = cell.find(NS_DATA)
                    if data is not None and data.text is not None:
                        if data.text == 'END_OF_COLUMNS':
                            break
                        column_visibilities.append(data.text)

                column_len = len(column_visibilities)

            elif row_index == 1: # colum_name
                column_idx = 0
                for cell in row.iter(tag=NS_CELL):
                    if column_idx == column_len:
                        break

                    data = cell.find(NS_DATA)
                    if data is not None:
                        if data.text is not None:
                            column_names.append(data.text)
                        else:
                            column_names.append(''.join([c.text for c in data.getchildren()]))

                    column_idx += 1

                if len(column_visibilities) != len(column_names):
                    print('error : column_visibility_count and column_name_count mismatch')
                    sys.exit()

            elif row_index == 2: # colum_type
                column_idx = 0
                for cell in row.iter(tag=NS_CELL):
                    if column_idx == column_len:
                        break

                    data = cell.find(NS_DATA)
                    if data is not None and data.text is not None:
                        column_types.append(data.text)

                    column_idx += 1

                if len(column_visibilities) != len(column_types):
                    print('error : column_visibility_count and column_type_count mismatch')
                    sys.exit()

            elif row_index == 3: # colum_description
                row_index += 1
                continue

            else: # data
                column_idx = 0
                data_mid = None
                for cell in row.iter(tag=NS_CELL):
                    if data_mid is not None and NS_INDEX in cell.attrib:
                        cell_attrib_index = int(cell.attrib[NS_INDEX]) - 1
                        while column_idx < cell_attrib_index and column_idx < column_len:
                            mst_dict[data_mid] = {
                                column_names[column_idx]:default_value(column_types[column_idx])
                            }
                            column_idx += 1

                    if column_idx == column_len:
                        break

                    data = cell.find(NS_DATA)
                    if data is not None:
                        data_text = None

                        if data.text is not None:
                            data_text = data.text
                        else:
                            data_text = ''.join([c.text for c in data.getchildren()])

                        if data_text == 'END_OF_DATA':
                            break

                        visible = column_visibilities[column_idx] != 'unlisted'

                        if column_idx == 0:
                            data_mid = data_text
                            mst_dict[data_mid] = {}

                        elif visible and 'list' in column_types[column_idx]:
                            mst_dict[data_mid][column_names[column_idx]] = data_text.split(';')

                        elif visible:
                            if is_int(column_types[column_idx]):
                                mst_dict[data_mid][column_names[column_idx]] = int(data_text)

                            elif is_float(column_types[column_idx]):
                                mst_dict[data_mid][column_names[column_idx]] = float(data_text)

                            else:
                                mst_dict[data_mid][column_names[column_idx]] = data_text

                    column_idx += 1

            row_index += 1

        with open('./' + PHASE + '_json/' + name + '.json', 'w') as fh:
            json.dump(mst_dict, fh)

