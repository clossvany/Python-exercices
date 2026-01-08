print("Welcome to my own calculator!")
bill = float(input("What is a total of bill? "))
percentage = int(input("How many of percentage you're willing to give? 10, 12, 20 "))
people = int(input("How many people going to split this bill? ") )
tip_percentage = percentage / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_total = round(bill_per_person, 2)
print(f"Total to pay each person is: {final_total}")

#just another day run :D3

print("Welcome to Rollercoaster")
hight = int(input("What is your hight? "))

if hight >= 120:
    print("You can ride the Rollercoaster.")
else:
    print("Sorry! You have to grow taller before you can ride, maybe next year.")
