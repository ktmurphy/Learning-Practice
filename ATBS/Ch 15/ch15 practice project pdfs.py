#! python3
# combinePdfs.py - combines all PDFs in the current working directory into a single PDFs without cover pages
import PyPDF2 as pdf
import os

pdfFileNames = []
for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        pdfFileNames.append(filename)

pdfFileNames.sort(key=str.lower)

pdfWriter = pdf.PdfFileWriter()
for file in pdfFileNames:
    pdfFileObj = open(filename, "rb")
    pdfReader = pdf.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfOutput = open("allminutes.pdf", "wb")
pdfWriter.write(pdfOutput)
pdfOutput.close()
