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

user_choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ^_^\n"))
computer_choice= random.randint(0,2)
rps=[rock, paper, scissors]
print(rps[user_choice])
print("Computer chose:")
print(rps[computer_choice])
if user_choice == computer_choice:
    print("tie -_-")
elif user_choice == 0:
    if computer_choice==1:
        print("you lost T.T")
    elif computer_choice==2:
        print("you won ^_^")
elif user_choice == 1:
    if computer_choice==2:
        print("you lost T.T")
    elif computer_choice==0:
        print("you won ^_^")
elif user_choice == 2:
    if computer_choice==0:
        print("you lost T.T")
    elif computer_choice==1:
        print("you won ^_^")
