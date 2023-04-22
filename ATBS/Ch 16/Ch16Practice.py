# Write your code here :-)
import csv

exampleFile = open("example.csv")
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
    print("Row #" + str(exampleReader.line_num) + " " + str(row))

outputFile = open("output.csv", "w", newline="")

outputWriter = csv.writer(outputFile, delimiter="\t", lineterminator="\n\n")

outputWriter.writerow(["spam", "eggs", "milk"])
outputFile.close()
exampleFile.close()

exampleFile = open("exampleWithHeader.csv")
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row["Timestamp"], row["Fruit"], row["Quantity"])
exampleFile.close()

exampleFile = open("example.csv")
exampleDictReader = csv.DictReader(exampleFile, ["time", "name", "amount"])
for row in exampleDictReader:
    print(row["time"], row["name"], row["amount"])
exampleFile.close()

outputFile = open("output.csv", "w", newline="")
outputDictWriter = csv.DictWriter(outputFile, ["Name", "Pet", "Phone"])
outputDictWriter.writeheader()
outputDictWriter.writerow({"Name": "Alice", "Pet": "Cat", "Phone": "555-1234"})
outputFile.close()

import json

strOfJsonData = '{"name": "zophie", "isCat" : true, "miceCaught":0, "felineIQ": null}'
jsonDataAsPython = json.loads(strOfJsonData)
pythonDataAsJson = json.dumps(jsonDataAsPython)
