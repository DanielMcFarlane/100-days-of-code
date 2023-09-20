# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined = name1 + name2
lowercase = combined.lower()

t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")
true = t + r + u + e

l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")
love = l + o + v + e

# having true + love as a string creates 5 + 5 = 55 instead of 10
score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")