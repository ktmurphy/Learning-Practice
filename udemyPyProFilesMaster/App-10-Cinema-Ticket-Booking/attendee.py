import sqlite3
import ticket
import seat
import card

class Attendee:

    def __init__(self, name, seat_choice):
        self.name = name
        self.seat_choice = seat_choice
    
    def buy(self, stored_card):
        try: 
            stored_card.charge_card(self.seat_choice.seat_price)
        except: 
            print("Failed to run card.")
            return
        try:
            self.seat_choice.occupy()
        except: 
            print("Failed to occupy seat.")
            return
        ticket_pdf = ticket.Ticket(self).generate_pdf()
        return ticket_pdf