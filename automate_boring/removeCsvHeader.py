#! python3
#removeCsvHeader.py - Removes the header from all CSV files in the current
#working directory.

import csv, os

os.makedirs('headerRemoved',exist_ok=True)

# Loop through every file in the current working directory
for csvFilename is os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue # skip non-csv files
	
	print('Removing header from ' + csvFilename + '...')

	csvRows = []
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue # skip first row
		csvRows.append(row)
	csvFileObj.close()



