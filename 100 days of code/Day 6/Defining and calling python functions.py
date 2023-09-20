# python functions
# https://docs.python.org/3/library/functions.html
print("hello")

num_char = len("hello")
print(num_char)

# creating your own functions
# to call the function do my_function()
def my_function():
    print("Hello")
    print("Bye")
    
my_function()

# reeborg's world
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

# for vs while loops
# for is for itterating i.e. doing something for every item in a list
fruits = ["Apple", "Pear", "Orange"]
for fruit in fruits:
    print(fruit)

for n in range(1, 6):
    print(n)

# while dont care what number in sequence or item and just want to carry out a function until the contion is met
# they keep running until it becomes false i.e. an infinate loop when gone wrong