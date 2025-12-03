import random

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

computer = [scissors, rock, paper]

print("Welcome to Rock, Paper, Scissors!")
user_input = input("Will you choose Scissors, Paper, or Rock?\n").lower()

if user_input == "rock":
  print(rock)
elif user_input == "paper":
  print(paper)
elif user_input == "scissors":
  print(scissors)

computer_choices = random.randint(0, 2)
print("Computer chose: ")
print(computer[computer_choices])

if user_input == computer_choices:
    print ("It's a draw!")
elif user_input == "rock":
  if computer_choices == 2:
    print ("You lose!")
  else: 
    print("You win!")
elif user_input == "paper":
  if computer_choices == 0:
    print("You lose!")
  else: 
    print("You win!")
elif user_input == "scissors":
  if computer_choices == 1:
    print("You lose!")
  else: 
    print("You win!")
