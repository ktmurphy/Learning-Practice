#! python3
import win32com.client
import docx

wordFileName = "helloworldpractice.docx"
pdfFileName = "helloworldpracticePdf.pdf"
doc = doc.Document()
doc.save(wordFileName)
