rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

list = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print(list[choice])

  computer = random.randint(0,2)
  print("Computer chose:")
  print(list[computer])
  
  
  if choice == 0 and computer == 2:
    print("You win!")
  elif computer == 0 and choice == 2:
    print("You lose")
  elif choice > computer:
    print("You win!")
  elif computer > choice:
    print("You lose")
  elif choice == computer:
    print("It's a draw")