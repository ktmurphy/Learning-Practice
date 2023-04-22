#! python3
# go through all files, find pdfs, encrypt copies
# go through all encrypted copies and write a decrpyted copy using password in command line
# if password incorrect, print message and continue to next pdf


import os
import PyPDF2 as pdf
from pathlib import Path

pdfsList = []
for file in os.listdir("."):
    if file.endswith(".pdf"):
        pdfsList.append(file)
pdfWriter = pdf.PdfFileWriter()

for file in pdfsList:
    try:
        pdfFile = open(file, "rb")
        pdfReader = pdf.PdfFileReader(pdfFile)
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
