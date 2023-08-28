import sqlite3
import seat
import card
import attendee 


seats_database = "cinema.db"
banking_database = "banking.db"

def main():
    #Gather attendee name and seat choice
    attendee_name = (input("What is the name of the cinema attendee? "))
    seat_choice = seat.Seat(gather_seat_choice())
    attendee_obj = attendee.Attendee(attendee_name, seat_choice)

    #Pull up card from database based on card number.
    stored_card = input("What is your credit card number? ")
    while validate_card_number(stored_card) == False:
        print("Card info not found. Please check your card number or use another card: ")
        stored_card = input("What is your credit card number? ")

    stored_card = card.Card(stored_card)

    #Confirm card info from attendee:
    card_type_entered = input("Please enter the card type (Visa, Mastercard, etc.): ")
    card_holder_entered = input("Please enter the name of the card holder on the card: ")
    cvc_entered = input("please enter your cvc number: ")

    #Validate card with banking info
    if card_type_entered != stored_card.card_type:
        print("Incorrect card type. Please try again.")
        return

    if card_holder_entered != stored_card.card_holder:
        print("Incorrect card holder name. Please try again.")
        return

    if cvc_entered != stored_card.card_cvc:
        print("Incorrect cvc. Please try again.")
        return
    
    #check if price in range
    if stored_card.validate_can_afford(seat_choice.seat_price):
        #complete purchse
        attendee_obj.buy(stored_card)

    else:
        print("Insufficient funds.")
        return  





def list_available_seats():

    connection = sqlite3.connect(seats_database)
    cursor = connection.cursor()
    available_seats_tuple_list = cursor.execute("SELECT seat_id FROM Seat WHERE taken=0").fetchall()
    seats = []
    for seat in available_seats_tuple_list:
        seats.append(seat[0])
    connection.commit()
    connection.close()
    return seats


def gather_seat_choice():
    available_seats = list_available_seats()
    print("These seats are available: ", ", ".join(available_seats))

    seat_choice = input("Which seat would you like? ")

    while seat_choice not in available_seats:
        print("Seat Choice not available")
        seat_choice = input("Which seat would you like? ")

    return seat_choice

def validate_card_number(stored_card):
    connection = sqlite3.connect(banking_database)
    cursor = connection.cursor()
    numbers = cursor.execute("""
    SELECT "number" FROM "Card"
    """).fetchall()
    valid_nums = []
    for number in numbers:
        valid_nums.append(number[0])
    connection.close()
    if stored_card in valid_nums:
        return True
    else:
        return False
    

main()