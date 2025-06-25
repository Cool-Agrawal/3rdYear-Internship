import random

choice = ["Rock","Paper","Scissor"]
while True:
<<<<<<< HEAD
    print("Rock Paper Scissor game\n")
=======
    print("\nRock Paper Scissor game")
>>>>>>> a9e740445df3aafb6b8ce9e5e6f170108e776f10
    print("Enter your choice: Rock/Paper/Scissor/Quit")
    user = input().title()
    if user == "Quit":
        break
<<<<<<< HEAD
=======
    if user not in choice:
        user = "Invalid"

>>>>>>> a9e740445df3aafb6b8ce9e5e6f170108e776f10
    computer = random.choice(choice)
    print(computer)
    if user ==  computer:
        print("tie")
<<<<<<< HEAD
    elif (user == "Rock" and computer == "Scissor")or (user == "Scissor" and computer == "Paper") or (user == "Paper" and computer == "Rock" ):
        print("You Won")
    else:
        print("You lose")
=======
    elif user == "Invalid":
         print("invalid")
    elif (user == "Rock" and computer == "Scissor")or (user == "Scissor" and computer == "Paper") or (user == "Paper" and computer == "Rock" ):
        print("You Won\n")
    else:
        print("You lose\n")
>>>>>>> a9e740445df3aafb6b8ce9e5e6f170108e776f10

