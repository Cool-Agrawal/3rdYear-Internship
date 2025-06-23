import random

choice = ["Rock","Paper","Scissor"]
while True:
    print("Rock Paper Scissor game\n")
    print("Enter your choice: Rock/Paper/Scissor/Quit")
    user = input().title()
    if user == "Quit":
        break
    computer = random.choice(choice)
    print(computer)
    if user ==  computer:
        print("tie")
    elif (user == "Rock" and computer == "Scissor")or (user == "Scissor" and computer == "Paper") or (user == "Paper" and computer == "Rock" ):
        print("You Won")
    else:
        print("You lose")

