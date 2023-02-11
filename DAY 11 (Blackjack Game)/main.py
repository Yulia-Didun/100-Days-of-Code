## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
##########################################
import random
from art import logo
import os

def deal_card():
  """
  Chooses random card number and return its value.
  """
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  """Take a list of cards and return the score calculated from the score."""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)


def compare(user, computer):
  """Takes user's and computer's scores and return wether user lose or win"""
  if user == computer:
    return "Draw!"
  elif computer == 0 :
    return "Lose, opponent has Blackjack 😱"
  elif user == 0:
    return "Win with a Blackjack 😎"
  elif user > 21:
    return "You went over. You lose 😭"
  elif computer > 21:
    return "Opponent went over. You win 😁"
  elif user > computer:
    return "You win 😃"
  else:
    return "You lose 😤"


def play_game():
  os.system('cls')
  print(logo)
  user_cards = []
  computer_cards = []
  game_over = False
  
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_over:
    
    user_cards_score = calculate_score(user_cards)
    computer_cards_score = calculate_score(computer_cards)
    
    print(f"\n\tYour cards: {user_cards}. Current score: {user_cards_score}.")
    print(f"\tComputer card: {computer_cards[0]}.")
    
    if user_cards_score == 0 or computer_cards_score == 0 or user_cards_score > 21:
      game_over = True
    
    else:
      get_another_card = input("\nType 'y' to get another card, type 'n' to pass: ")
      
      if get_another_card == 'y':
        user_cards.append(deal_card())
        
      else:
        game_over = True
  
  
  while computer_cards_score != 0 and computer_cards_score < 17:
    computer_cards.append(deal_card())
    computer_cards_score = calculate_score(computer_cards)
  
  print(f"\nYour final hand: {user_cards} , final score: {user_cards_score}. \nComputer final hand: {computer_cards}, final score: {computer_cards_score}.\n\n{compare(user = user_cards_score, computer = computer_cards_score)}")
  

  

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('cls')
  play_game()
