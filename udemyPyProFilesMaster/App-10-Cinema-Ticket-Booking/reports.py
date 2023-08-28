from fpdf import FPDF
import webbrowser
import os


class PdfTicket:
    """
    Creates Pdf Ticket
    """
    def __init__(self, filename):
        self.filename = filename
    
    def create(self, ticket):
        #Create PDF
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert Title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Cinema Ticket", border=0, align="C", ln=1)
        
        # Insert Ticket ID
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=150, h=48, txt="Ticket_Number: ", border=0)
        pdf.cell(w=150, h=48, txt=ticket.id, border=0, ln=1)

        #Insert Seat
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=150, h=25, txt="Attendee: ", border=0)
        pdf.cell(w=150, h=25, txt=ticket.name, border=0, ln=1)

        #Insert name and amount owed for second flatmate
        pdf.cell(w=150, h=25, txt=flatmate2.name + " owes: ", border=0)
        pdf.cell(w=150, h=25, txt=flatmate2owes, border=0, ln=1)

        pdf.output(f"files\{self.filename}")
        
        # Change directory and open file
        os.chdir("files")
        webbrowser.open(self.filename)