import sqlite3

class Seat: 

    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id
        connection = sqlite3.connect(self.database)
        connection.row_factory = sqlite3.Row
        seat_data = connection.execute("SELECT taken, price FROM Seat WHERE seat_id = ?", (self.seat_id,),).fetchone()
        connection.commit()
        connection.close()
        self.seat_taken = seat_data["taken"]
        self.seat_price = seat_data["price"]

    def occupy(self):
        connection = sqlite3.connect(self.database)
        connection.execute("""
        UPDATE "Seat" SET "taken"=1 WHERE "seat_id" =?
        """, [self.seat_id])
        connection.commit()
        connection.close()