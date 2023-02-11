import art
import game_data
import random
import os

def choose_random_person(data):
    '''Returns random person from data list.'''
    return random.choice(data)

def compare(first_person, second_person):
    '''Prints data for first and second person. Returns user choice who has more followers.'''
    print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}.")
    print(art.vs)
    print(f"Compare B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}.")

    return input("Who has more followers? Type 'A' or 'B': ")

def check_the_answer(first_person, second_person, answer):
    '''Checks user answer. If it's correct, adds a point to the SCORE, and reassign the first_person value(if necessary). Returns True(continue the game) and first_person value. 
    If answer is wrong, returns False(stop the game) and first person value(without changing).'''

    global SCORE

    if first_person['follower_count'] >= second_person['follower_count'] and answer == 'A':
        SCORE += 1
        return True, first_person
    elif first_person['follower_count'] <= second_person['follower_count'] and answer == 'B':
        first_person = second_person
        SCORE += 1
        return True, first_person
    else:
        return False, first_person

def game_over():
    """When the game is over, prints a message with the final score."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {SCORE}.")

def game():
    answer_is_right = True

    first_person = choose_random_person(game_data.data)
    second_person = choose_random_person(game_data.data)
    
    while answer_is_right: # while answer is right, game runs
        os.system('cls' if os.name == 'nt' else 'clear') # cleans the console
        print(art.logo)

        if SCORE > 0:
            print(f"You're right! Current score: {SCORE}.")

        user_answer = compare(first_person, second_person)
        answer_is_right, first_person = check_the_answer(first_person, second_person, user_answer)

        if answer_is_right:
            second_person = choose_random_person(game_data.data)

    game_over()

    
SCORE = 0

game()