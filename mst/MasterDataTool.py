
import sys
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

if len(sys.argv) < 2:
    print('Usage: python3 ./GameMasterData.py develop')
    sys.exit()

PHASE = sys.argv[1]

PATH = '../mst/' + PHASE
FILES = [f for f in listdir(PATH) if isfile(join(PATH, f))]

NS = '{urn:schemas-microsoft-com:office:spreadsheet}'

for f in FILES:
    print(f)
    print()

    tree = ET.parse(join(PATH, f))
    root = tree.getroot()

    column_names = []
    column_types = []
    column_visibilities = []
    for worksheet in root.findall(NS + 'Worksheet'):
        name = worksheet.attrib[NS + 'Name']
        print('\t' + name)

        table = worksheet.find(NS + 'Table')
        #print('\t\t' + table.tag)

        row_index = 0
        for row in table.findall(NS + 'Row'):
            #print('\t\t\t' + row.tag)

            if row_index == 0: # colum_name
                for cell in row.findall(NS + 'Cell'):
                    data = cell.find(NS + 'Data')
                    if data is not None and data.text is not None:
                        print('\t\t\t\t' + data.text)
                        #print('\t\t\t\t' + cell.tag)

            elif row_index == 1: # colum_type
                for cell in row.findall(NS + 'Cell'):
                    data = cell.find(NS + 'Data')
                    if data is not None and data.text is not None:
                        print('\t\t\t\t' + data.text)
                        #print('\t\t\t\t' + cell.tag)

            elif row_index == 2: # colum_visibility
                for cell in row.findall(NS + 'Cell'):
                    data = cell.find(NS + 'Data')
                    if data is not None and data.text is not None:
                        print('\t\t\t\t' + data.text)
                        #print('\t\t\t\t' + cell.tag)

                if data == 'none':
                    pass

            elif row_index == 3: # colum_description
                for cell in row.findall(NS + 'Cell'):
                    data = cell.find(NS + 'Data')
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

