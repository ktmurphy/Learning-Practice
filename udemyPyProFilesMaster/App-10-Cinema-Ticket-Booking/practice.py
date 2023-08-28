import sqlite3

'''
database = "banking.db"
number="12345678"
connection = sqlite3.connect(database)
connection.row_factory = sqlite3.Row

card_data = connection.execute("SELECT type, cvc, holder, balance FROM Card WHERE number = ?", (number,),).fetchone()



print(card_data.keys())
'''

def list_available_seats():

    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    available_seats_tuple_list = cursor.execute("SELECT seat_id FROM Seat WHERE taken=0").fetchall()
    seats = []
    for seat in available_seats_tuple_list:
        seats.append(seat[0])
    connection.commit()
    connection.close()
    return seats

seats = list_available_seats()
print(seats)