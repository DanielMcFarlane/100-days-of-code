#Write your code below this row 👇
total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

# a simpler way would be to just start at 2 and use a step of 2

total = 0

for number in range(2, 101, 2):
    total += number
print(total)