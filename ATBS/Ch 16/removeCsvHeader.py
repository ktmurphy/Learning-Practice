# Write your code here :-)
#! python3
# removeCsvHeader.py - removes header from all CSV files in current working directory

import csv, os

os.makedirs("headerRemoved", exist_ok=True)
for csvFileName in os.listdir("."):
    if not csvFileName.endswith(".csv"):
        continue
    print("Removing header from " + csvFileName + " ...")
    csvRows = []
    csvFileObj = open(csvFileName)
    csvReader = csv.reader(csvFileObj)
    for row in csvReader:
        if csvReader.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(os.path.join("headerRemoved", csvFileName), "w", newline="")
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
