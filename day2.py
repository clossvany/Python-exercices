print("Welcome to my own calculator!")
bill = float(input("What is a total of bill? "))
percentage = int(input("How many of percentage you're willing to give? 10, 12, 20 "))
people = int(input("How many people going to split this bill? ") )
tip_percentage = percentage / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_total = round(bill_per_person, 2)
print(f"Total to pay each is: {final_total}")
