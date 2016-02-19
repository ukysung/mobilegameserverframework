
import sys
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

def main():
	if len(sys.argv) < 2:
		print('Usage: python3 ./GameMasterData.py develop')
		sys.exit()

	phase = sys.argv[1]
	path = '../mst/' + phase
	files = [f for f in listdir(path) if isfile(join(path, f))]

	ns = '{urn:schemas-microsoft-com:office:spreadsheet}'

	for f in files:
		print(f)
		print()
	
		tree = ET.parse(join(path, f))
		root = tree.getroot()
	
		column_names = []
		column_types = []
		column_visibilities = []
		for worksheet in root.findall(ns + 'Worksheet'):
			name = worksheet.attrib[ns + 'Name']
			print('\t' + name)
		
			table = worksheet.find(ns + 'Table')
			#print('\t\t' + table.tag)
		
			row_index = 0
			for row in table.findall(ns + 'Row'):
				#print('\t\t\t' + row.tag)
			
				if row_index == 0: # colum_name
					for cell in row.findall(ns + 'Cell'):
						data = cell.find(ns + 'Data')
						print('\t\t\t\t' + data.text)
						#print('\t\t\t\t' + cell.tag)
					
			elif row_index == 1: # colum_type
				for cell in row.findall(ns + 'Cell'):
					data = cell.find(ns + 'Data')
					print('\t\t\t\t' + data.text)
					#print('\t\t\t\t' + cell.tag)
					
			elif row_index == 2: # colum_visibility
				for cell in row.findall(ns + 'Cell'):
					data = cell.find(ns + 'Data')
					print('\t\t\t\t' + data.text)
					#print('\t\t\t\t' + cell.tag)
					
					if date == 'none':
						
					
			elif row_index == 3: # colum_description
				for cell in row.findall(ns + 'Cell'):
					data = cell.find(ns + 'Data')
					print('\t\t\t\t' + data.text)
					#print('\t\t\t\t' + cell.tag)
					
			#else: # data
				
			print()
			row_index += 1
			if row_index == 3:
				break
			
		break
		
	print()

if __name__ == '__main__':
	main()

