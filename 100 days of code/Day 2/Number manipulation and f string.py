# Rounding decimals
# Use round(). To round to a certain number of places use , after equation

print(round(2.66666666, 2))
print(round(8 / 3, 2))

# Round using floor devision 
# // for whole number no decimal places
print(8 // 3)


# Continue on calculations

result = 4 / 2
result /= 2
print(result)

# You can manipulate values based on previus set value e.g.
# +=, -+, *=, /+

score = 0

# User scores a point

score += 1
print(score)

# f-strings
# You can print different types without having to convert

score = 0 #int
height = 1.8 #float
isWinning = True #bool

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")