import PyPDF2 as pdf

minutesFile = open("meetingminutes.pdf", "rb")
pdfReader = pdf.PdfFileReader(minutesFile)
pdfWriter = pdf.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt("swordfish")
resultPdf = open("encryptedminutes.pdf", "wb")
pdfWriter.write(resultPdf)
minutesFile.close()
resultPdf.close()
