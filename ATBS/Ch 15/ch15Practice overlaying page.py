import PyPDF2 as pdf

minutesFile = open("meetingminutes.pdf", "rb")
pdfReader = pdf.PdfFileReader(minutesFile)

minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = pdf.PdfFileReader(open("watermark.pdf", "rb"))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = pdf.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)
for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open("watermarkedCover.pdf", "wb")
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
