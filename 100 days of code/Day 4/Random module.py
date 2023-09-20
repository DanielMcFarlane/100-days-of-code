# you can import user created modules by creatinga new file with something like pi = 3.14159246
# then import it by -  import my_module
# you can then print it by doing. File name.variable name
# print(my_module.pi)

import random

random_int = random.randint(1, 10)
print(random_int)

# 0.000000 - 0.9999999....
random_float = random.random()
print(random_float)


# to get a float between 0 and a number do
random_float * 5
# that gets you 0.000000 - 4.999999

# you can use it for things like

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# random.choice() gives you a random item from the lsit
random.choice() 

i.e.

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
length = len(chosen_word)
for _ in range(length):
    display += "_"
print(display)