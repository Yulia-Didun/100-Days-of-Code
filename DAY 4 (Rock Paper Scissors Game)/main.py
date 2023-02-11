import random

print("\t\t\tWelcome to 'The Rock Paper Scissors' game")
repeat = int(input('How many times do you want to play?\n'))

while repeat != 0:
    user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

    lst = ['✊', '✋', '✌️']
    print(f"You chose {lst[user_choice]}")

    computer_choice_num = random.randint(0, 2)

    computer_choice = lst[computer_choice_num]

    print(f"Computer chose {computer_choice}.")

    if user_choice == 0:
        if computer_choice_num == 0:
            print("Draw!")
        elif computer_choice_num == 1:
            print("You Lose!")
        elif computer_choice_num == 2:
            print("You Win!")

    elif user_choice == 1:
        if computer_choice_num == 0:
            print("You Win!")
        elif computer_choice_num == 1:
            print("Draw!")
        elif computer_choice_num == 2:
            print("You Lose!")

    elif user_choice == 2:
        if computer_choice_num == 0:
            print("You Lose!")
        elif computer_choice_num == 1:
            print("You Win!")
        elif computer_choice_num == 2:
            print("Draw!")

    repeat -= 1