import os
from art import logo

print(logo)
print("\nWelcome to the secret auction program.\n")

bids = {}
should_continue = True

def find_highest_bidder(bidders):
  highest_bid = 0
  for person in bidders:
      if bidders[person] > highest_bid:
        highest_bidder_name = person
        highest_bid = bidders[person]
  print(f"The winner is {highest_bidder_name} with a bid of ${highest_bid}. Congratulations!")
  

while should_continue:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  
  bids[name] = bid
  
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  os.system("cls")
  
  if more_bidders == 'no':
    should_continue = False
    find_highest_bidder(bids)