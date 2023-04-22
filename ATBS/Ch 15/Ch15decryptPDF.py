#! python3
# goes through encrypted copies and writes a decrypted copy based on password. Moves on if password isn't entered.


# needs work - need to figure out how to see if they are encrypted before opening them
import os, sys
import PyPDF2 as pdf
from pathlib import Path

pdfList = []
for file in os.listdir("."):
    if file.isEncrypted:
        pdfList.append(file)
pdfWriter = pdf.PdfFileWriter()

for file in pdfList:
    try:
        pdfFile = open(file, "rb")
        pdfReader = pdf.PdfFileReader(pdfFile)
        pdfReader.decrypt(input())
        pdfWriter = pdf.PdfFileWriter()
        for page in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(page))

        pdfWriter.encrypt("swordfish")
        p = Path(file)
        base = p.stem + "_encrypted.pdf"
        resultPdf = open(base, "wb")
        pdfWriter.write(resultPdf)
        resultPdf.close()
    except:
        print(file)
print("Done")
