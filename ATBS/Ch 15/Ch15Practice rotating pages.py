# Write your code here :-)
import PyPDF2 as pdf

minutesFile = open("meetingminutes.pdf", "rb")
pdfReader = pdf.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter = pdf.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open("rotatedPage.pdf", "wb")
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
