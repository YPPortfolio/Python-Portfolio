from replit import clear
from art import logo
from art import vs 
from game_data import data
import random

### randomly pull two dictionaries from game_data.data ###
def random_data():
  """Input list then random output from the list"""
  return random.choice(data)

def format_data(rand):
  """ format the comparison statement based on the rand generation """
  name = rand["name"]
  desc = rand["description"]
  country = rand["country"]
  return f"{name}, a {desc}, from {country}."

def check_answers(guess, rand1_count, rand2_count):
  """check if the guess results in correct, 'True', or incorrect, 'False'"""
  if rand1_count > rand2_count:
    return guess == "a"
  else:
    return guess == "b"

def game():    
  print(logo)

  ### score set ###
  score = 0

  ### random generation ###
  rand1 = random_data()
  rand2 = random_data()
  while rand2 == rand1:
    rand2 = random.choice(data)

  ### loop the game to continue ###
  game_over = False
  while not game_over:
    
   
    
    ### print the two dictionary one above "vs" logo and one below the logo ### 
    print(f"Compare A: {format_data(rand1)}")
    print(vs)
    print(f"Against B: {format_data(rand2)}")

    ### user guess ###
    guess = input("Which has more followers? A or B?\n").lower()
    rand1_count = rand1["follower_count"]
    rand2_count = rand2["follower_count"]
    is_correct = check_answers(guess, rand1_count, rand2_count)
  
    clear()
    print(logo)
    if is_correct:
      score += 1
      if guess == "b":
        rand1 = rand2
        rand2 = random_data()
        while rand2 == rand1:
          rand2 = random.choice(data)
      elif guess == "a":
        rand2 = random_data()
        while rand2 == rand1:
          rand2 = random.choice(data)
      print(f"You are Correct! Current Score: {score}.")
    else:
      game_over = True
      print(f"Incorrect! Final Score: {score}.")

  ### if incorrect then ask to play again ###
  play_again = input("Would you like to play again? 'Y' or 'N':\n").lower()
  if play_again == "y":
    clear()
    game()  
  else:
    clear()
    print("Thanks for playing. Goodbye!")

### game function end ###

game()
