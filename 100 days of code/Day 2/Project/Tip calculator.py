#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome ot the tip calculator.")
bill = float(input("What was the toatal bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = bill * (percentage / 100)
total = tip + bill
each = round(total / people, 2)
# if not rounding a 0 you can manually force it by using "{:.2f}" .format()
each = "{:.2f}" .format(each)

print(f"Each person should pay: ${each}")