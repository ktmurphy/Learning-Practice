from fpdf import FPDF
import webbrowser
import os

class PdfReport:
    """
    Creates PdfReport based on the amount owed by each flatmate for the period.
    """
    def __init__(self, filename):
        self.filename = filename
    
    def create(self, flatmate1, flatmate2, bill):
        flatmate1owes = str(round(flatmate1.owes(bill, flatmate2)))
        flatmate2owes = str(round(flatmate2.owes(bill, flatmate1)))
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add Icon
        pdf.image("files\house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        # Insert Period Label and Value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=150, h=48, txt="Period: ", border=0)
        pdf.cell(w=150, h=48, txt=bill.period, border=0, ln=1)

        #Insert name and amount owed for first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=150, h=25, txt=flatmate1.name + " owes: ", border=0)
        pdf.cell(w=150, h=25, txt=flatmate1owes, border=0, ln=1)

        #Insert name and amount owed for second flatmate
        pdf.cell(w=150, h=25, txt=flatmate2.name + " owes: ", border=0)
        pdf.cell(w=150, h=25, txt=flatmate2owes, border=0, ln=1)

        pdf.output(f"files\{self.filename}")
        
        # Change directory and open file
        os.chdir("files")
        webbrowser.open(self.filename)