###########################################################################
## This is our Python 'Code Editor'. Write your code in this file! ##
###########################################################################

## Exercise - Rock Paper Scissors ##

import random

#code
player_score = 0
computer_score = 0
ties = 0

approved_moves = ["r","p","s"]
winning_moves = ["pr","sp","rs"]

while True: 
  player_move = input("r,p,s ? oe enter q to quit" )

  if player_move == 'q':
    print("Thanks for playing")
    break

  else:

    computer_move = random.choice(approved_moves)
    print(player_move)
    print(computer_move)
    if player_move == computer_move: 
      ties += 1
      print("Game is a draw !")
    elif player_move + computer_move in winning_moves:
      player_score += 1
      print ("Player wins")
    elif computer_move + player_move in winning_moves:
      computer_score += 1
      print ("Computer wins")
    else :
      print("Invalid move. Please try again")

    print(f"Scoreboard - Player:{player_score},Computer:{computer_score},Ties:{ties}")