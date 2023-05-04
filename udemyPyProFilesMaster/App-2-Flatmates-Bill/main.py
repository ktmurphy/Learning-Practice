from flat import Bill, Flatmate
from reports import PdfReport

# Gather bill information
amount = float(input("Please enter the bill amount: "))
period = input("Please enter the period (Example: March 2021): ")
the_bill = Bill(amount, period)

# Gather flatmate information
flatmate1_name = input("Please enter your name: ")
flatmate1_days_in_house = int(input(f"How many days did {flatmate1_name} stay in the house? "))
flatmate2_name = input("What is your flatmate's name? ")
flatmate2_days_in_house = int(input(f"How many days was {flatmate2_name} in the house in this period? "))
flatmate1 = Flatmate(flatmate1_name, flatmate1_days_in_house)
flatmate2 = Flatmate(flatmate2_name, flatmate2_days_in_house)

# Print results and generate report
print(f"{flatmate1.name} owes: ", flatmate1.owes(the_bill, flatmate2))
print(f"{flatmate2.name} owes: ", flatmate2.owes(the_bill, flatmate1))

pdf = PdfReport(filename=f"{the_bill.period}.pdf")
pdf.create(flatmate1, flatmate2, bill=the_bill)