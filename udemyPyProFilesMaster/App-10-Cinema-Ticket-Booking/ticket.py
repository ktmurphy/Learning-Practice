import sqlite3

from fpdf import FPDF
import webbrowser
import os

class Ticket: 

    def __init__(self, attendee):
        self.attendee = attendee
        self.seat = self.attendee.seat_choice
        self.id = f'{self.attendee.name}-{self.seat.seat_id}'
        self.path = f'tickets\{self.id}'

    def generate_pdf(self):
        #Create PDF
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert Title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Cinema Ticket", border=0, align="C", ln=1)
        
        # Insert Ticket ID
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=150, h=48, txt="Ticket ID: ", border=0)
        pdf.cell(w=150, h=48, txt=self.id, border=0, ln=1)

        #Insert Seat
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=150, h=25, txt="Attendee: ", border=0)
        pdf.cell(w=150, h=25, txt=self.attendee.name, border=0, ln=1)

        #Insert name and amount owed for second flatmate
        pdf.cell(w=150, h=25, txt="Seat: ", border=0)
        pdf.cell(w=150, h=25, txt=self.seat.seat_id, border=0, ln=1)

        pdf.output(self.path)
        '''
        # Change directory and open file
        os.chdir("tickets")
        webbrowser.open(self.filename)
        '''
