
import sys
from os import listdir
from os.path import isfile, join
import xml.etree.cElementTree as cET

if len(sys.argv) < 2:
    print('Usage: python3 ./MasterDataTool.py develop')
    sys.exit()

PHASE = sys.argv[1]

PATH = './' + PHASE
FILES = [f for f in listdir(PATH) if isfile(join(PATH, f))]

NS = '{urn:schemas-microsoft-com:office:spreadsheet}'
NS_WORKSHEET = NS + 'Worksheet'
NS_NAME = NS + 'Name'
NS_TABLE = NS + 'Table'
NS_ROW = NS + 'Row'
NS_CELL = NS + 'Cell'
NS_DATA = NS + 'Data'

for f in FILES:
    print(f)
    print()

    tree = cET.parse(join(PATH, f))
    root = tree.getroot()

    column_visibilities = []
    column_names = []
    column_types = []
    for worksheet in root.iter(tag=NS_WORKSHEET):
        name = worksheet.attrib[NS_NAME]
        print('\t' + name)

        table = worksheet.find(NS_TABLE)
        #print('\t\t' + table.tag)

        row_index = 0
        for row in table.iter(tag=NS_ROW):
            #print('\t\t\t' + row.tag)

            if row_index == 0: # colum_visibility
                for cell in row.iter(tag=NS_CELL):
                    data = cell.find(NS_DATA)
                    if data is not None and data.text is not None:
                        print('\t\t\t\t' + data.text)
                        #print('\t\t\t\t' + cell.tag)

            elif row_index == 1: # colum_name
                for cell in row.iter(tag=NS_CELL):
                    data = cell.find(NS_DATA)
                    if data is not None and data.text is not None:
                        print('\t\t\t\t' + data.text)
                        #print('\t\t\t\t' + cell.tag)

            elif row_index == 2: # colum_type
                for cell in row.iter(tag=NS_CELL):
                    data = cell.find(NS_DATA)
                    if data is not None and data.text is not None:
                        print('\t\t\t\t' + data.text)
                        #print('\t\t\t\t' + cell.tag)

                if data == 'none':
                    pass

            elif row_index == 3: # colum_description
                for cell in row.iter(tag=NS_CELL):
                    data = cell.find(NS_DATA)
                    if data is not None and data.text is not None:
                        print('\t\t\t\t' + data.text)
                        #print('\t\t\t\t' + cell.tag)

            #else: # data

        print()
        row_index += 1
        if row_index == 3:
            break

        break

    print()

