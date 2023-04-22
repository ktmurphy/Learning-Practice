import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

wb = openpyxl.load_workbook("example.xlsx")
sheet = wb["Sheet1"]

print(tuple(sheet["A1":"C3"]))

for rowOfCellObjects in sheet["A1":"C3"]:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print("End of row")


print(list(sheet.columns)[1])
