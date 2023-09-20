# for loop: give it a key word and then say in condition
# e.g. for fruit in fruits
# if you print the new key it assigns the keyword to every word in the list, loops and prints them seperate

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# print(fruit + " Pie") modifies the variable

# range(1, 10) only goes to 9, to get 10 you'd need to do range(1, 11)
# adding a third number is called the step, e.g. 3 gives you every third number
# think of it like 3+1=4, 3+4=7 3+7=10
for number in range(1, 11, 3):
  print(number)

# every number from 1 to 100 added would be
total = 0

for number in range(1, 101):
  total += number
print(total)