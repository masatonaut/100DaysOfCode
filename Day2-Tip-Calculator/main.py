# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
bill_as_float = float(bill)
tip_as_float = float(tip)
people_as_int = int(people)
tip_as_float = tip_as_float / 100
tip_as_float = tip_as_float + 1
total_bill = bill_as_float * tip_as_float
each_person = total_bill / people_as_int
each_person_rounded = round(each_person, 2)
each_person_rounded = "{:.2f}".format(each_person)
print(f"Each person should pay: ${each_person_rounded}")
