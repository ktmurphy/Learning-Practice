import PyPDF2 as pdf

pdf1File = open("meetingminutes.pdf", "rb")
pdf2File = open("meetingminutes2.pdf", "rb")
pdf1Reader = pdf.PdfFileReader(pdf1File)
pdf2Reader = pdf.PdfFileReader(pdf2File)
pdfWriter = pdf.PdfFileWriter()
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open("combinedminutes.pdf", "wb")
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
