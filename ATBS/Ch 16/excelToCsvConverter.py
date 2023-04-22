#! python3
# excelToCsvConverter.py - converts all excel files in current working directory to csvs
# using the naming of Excel File Name, Sheet Title

"""
1. Loop over all files in CWD and find excel files - os, path
2. For each Excel File, needs to open and read that, saving the information in rows - openpyxl
3. Needs to open a new csv file with the name of the file and sheet. - csv
4. Needs to write excel data to new csv file
"""
import os, openpyxl, csv
from pathlib import Path


for filename in os.listdir("."):
    if not filename.endswith(".xlsx"):
        print("skipping: " + filename)
        continue
    print("opening " + filename)
    wb = openpyxl.load_workbook(filename)
    sheets = wb.sheetnames

    for sheet in sheets:
        csvname = filename.split(".")[0] + "_" + sheet + ".csv"
        print(csvname)
        csvFile = open(csvname, "w", newline="")

        csvWriter = csv.writer(csvFile)
        rows = list(wb[sheet].rows)
        for row in rows:
            rowValues = []
            for cell in row:
                rowValues.append(cell.value)
            csvWriter.writerow(rowValues)
    csvFile.close()
    wb.close()
