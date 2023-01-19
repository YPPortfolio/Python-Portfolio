
### program ###

import random
from replit import clear
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def restart():
  restart_choice = input("Would you like to restart? 'Y' or 'N':\n").lower()
  if restart_choice == 'y':
    clear()
    blackjack()
  else:
    print("Thank you for playing.")
    
def blackjack():
  def player_draw():
    new_card = random.choice(cards)
    player_cards.append(new_card)  
  
  def dealer_draw():
    new_card = random.choice(cards)
    print(f"Dealer drew {new_card}.")
    dealer_cards.append(new_card)
  
  print(logo)
  
  player_cards = random.choices(cards, k=2)                 
  dealer_cards = random.choices(cards, k=2)
  
  ### first round ###
  player_total = sum(player_cards)
  dealer_total = sum(dealer_cards)
   
  if player_total > 21:
    if player_cards[0] == 11:
      player_cards[0] = 1
    if player_cards[1] == 11:
      player_cards[1] == 1
    player_total = sum(player_cards)
  
  if dealer_total > 21:
    if dealer_cards[0] == 11:
      dealer_cards[0] = 1
    if dealer_cards[1] == 11:
      dealer_cards[1] == 1  
    dealer_total = sum(dealer_cards)
  
  ### After the first round, ace would only be used for 1 ###
  cards[0] = 1
  
  ### initial card open ###
  print(f"Player has {player_cards}, totalling {player_total}.")
  
  if player_total == 21 and dealer_total == 21:
    print(f"You have {player_total} and dealer has {dealer_total}. It is a draw.")
    restart()
  elif dealer_total == 21:
    print(f"Dealer has {dealer_cards}, totalling {dealer_total}. Blackjack! Dealer Wins!")
    restart()
  elif player_total == 21:
    print(f"Your total is {player_total}, Blackjack! You Win!")
    restart()
  
  if player_total > 21:
    print(f"Your total is {player_total}, Bust! You Lose.")
    restart()
  
  print(f"Dealer has a {dealer_cards[0]}.")
  
  ### player draws additional cards ###
  continue_game = True
  while continue_game:
    player_call = input("Would you like to draw another card? 'Y' or 'N':\n").lower()
    
    if player_call == 'y':    
      player_draw()
      player_total = sum(player_cards)
      if player_total > 21:
        print(f"You now have {player_cards}. Total is {player_total}, Bust! You Lose.")
        continue_game = False
        restart()
      elif player_total == 21:
        print(f"You now have {player_cards}. Total is {player_total}.")
        continue_game = False
      else:
        print(f"You now have {player_cards}. Total is {player_total}.") 
    else:
      continue_game = False
  
  ### player has 21. Dealer draws ###
  if player_total == 21:
    while dealer_total <= 21:
      dealer_draw()
      dealer_total = sum(dealer_cards)
      if dealer_total > 21:
        print(f"Dealer has {dealer_cards}, totalling {dealer_total}. Bust! You Win!") 
        restart()
      elif dealer_total == 21:
        print(f"You have {player_total} and dealer has {dealer_total}. It is a draw.")
        restart()
      else:
        print(f"Dealer has {dealer_cards}, totalling {dealer_total}.")
  
  ### player stops drawing ###
  print("Dealer opens the second card.")
  print(f"Dealer has {dealer_cards}.")
  
  if dealer_total >= 17 and dealer_total > player_total:
    print(f"You have {player_total} and dealer has {dealer_total}. You Lose.")
    restart()
  elif dealer_total >= 17 and dealer_total < player_total:
    print(f"You have {player_total} and dealer has {dealer_total}. You Win!")
    restart()
  elif dealer_total >= 17 and dealer_total == player_total:
    print(f"You have {player_total} and dealer has {dealer_total}. It's a draw.")
    restart()
    
  while dealer_total <= 17:
    dealer_draw()
    dealer_total = sum(dealer_cards)
    if dealer_total > 21:
      print(f"Dealer has {dealer_cards}, totalling {dealer_total}. Bust! You Win!") 
      restart()
    elif dealer_total > 17 and dealer_total > player_total:
      print(f"You have {player_total} and dealer has {dealer_total}. You Lose.")
      restart()
    elif dealer_total > 17 and dealer_total == player_total:
      print(f"You have {player_total} and dealer has {dealer_total}. It is a draw.")
      restart()
    else:
      print(f"Dealer has {dealer_cards}, totalling {dealer_total}.")

### End of Blackjack program ###
      
blackjack()
