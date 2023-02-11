from art import logo
from random import randint
import os

HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 10


def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def check_guess(guess, answer, attempts):
    if guess > answer:
        print("Too high!")
        return attempts - 1
    elif guess < answer:
        print("Too low!")
        return attempts - 1
    elif guess == answer:
        print(f"You got it! The answer was {answer}.")


def game():
    os.system('cls')
    print(logo)
    print ("Welcome to the Number Guessing Game!\nI'm thinking of number between 1 and 100.")

    answer = randint(1, 100)
    guess = 0
    attempts = choose_difficulty()

    while guess != answer:
        print (f"\nYou have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_guess(guess, answer, attempts)

        if attempts == 0:
            print("You`ve run out of guesses, you lose.")
            return
        elif guess != answer: 
            print("Guess again.")


game()
