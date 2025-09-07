# Project - Rock , Paper , Scissors
# We are going to play with computer
# Rules :
# Rock wins against Scissors
# Scissors win against Paper
# Paper wins against Rock
# Let's be 0 for Rock , 1 for paper , 2 for scissors
# Total there can be 9 choices
# users_choice       computer_choice        winner
#     0                   0                   tie
#     0                   1                   c
#     0                   2                   u
#     1                   0                   u
#     1                   1                   tie
#     1                   2                   c
#     2                   0                   c
#     2                   1                   u
#     2                   2                   tie
import random
print("Come on , Lets start the game !!")
print("The choices are 0 for rock , 1 for paper , 2 for scissors ...")
choice = int(input("Enter your choice : "))
computer = random.randint(0,2)
if choice == 0:
    print("You chose rock")
elif choice == 1:
    print("You chose paper")
elif choice == 2:
    print("You chose scissors")

if computer == 0:
    print("Computer chose rock")
elif computer == 1:
    print("Computer chose paper")
elif computer == 2:
    print("Computer chose scissors")

if choice>=3 :
    print("You please Enter valid choice")
else :
    if choice==computer :
        print("Oh noo, Its tie ")
    elif choice==0 and computer==2 :
        print("You won the game : )")
    elif choice==2 and computer==0 :
        print("Sorry, you lose . Try again")
    elif computer>choice :
        print("Sorry, you lose . Try again")
    elif choice>computer :
        print("You won the game : )")