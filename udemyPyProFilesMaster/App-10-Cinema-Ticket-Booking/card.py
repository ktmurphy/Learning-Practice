import sqlite3

class Card: 

    database = "banking.db"
    
    def __init__(self, card_number):
        self.card_number = card_number
        connection = sqlite3.connect(self.database)
        connection.row_factory = sqlite3.Row
        card_data = connection.execute("SELECT type, cvc, holder, balance FROM Card WHERE number = ?", (self.card_number,),).fetchone()
        connection.commit()
        connection.close()
        self.card_type = card_data["type"]
        self.card_cvc = card_data["cvc"]
        self.card_holder = card_data["holder"]
        self.card_balance = card_data["balance"]

    def validate_can_afford(self, price):
        if self.card_balance > price:
            return True
        else: 
            return False
        
    def charge_card(self, price):
        connection = sqlite3.connect(self.database)
        new_balance = self.card_balance - price
        connection.execute("""
        UPDATE "Card" SET "balance"=? WHERE "number" =?
        """, [new_balance, self.card_number])
        connection.commit()
        connection.close()
        


        
    