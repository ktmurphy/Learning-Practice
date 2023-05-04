class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
    

class Flatmate:
    """
    Create a flatmate who lives in the flat and pays a share of the bill.
    """    
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
    
    def owes(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        amountOwed = weight * bill.amount
        return amountOwed
