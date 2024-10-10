from blackjack_helper import *

#GETTING USERS

num_play = int(input("Welcome to Blackjack! How many players? "))
player_score = {}


for i in range(1,num_play+1):
  player = input(f"What is player {i}'s name? ")
  player_score[player] = 3

cont = 'y'

while cont == 'y':
    player_hand = {}

    # USER'S TURN
    for key in player_score:
      hand = user_game(key)
      player_hand[key] = hand
 
    # DEALER'S TURN
    dealer_hand = draw_starting_hand("DEALER")
    while dealer_hand < 17:
      print("Dealer has {}.".format(dealer_hand))
      dealer_hand = dealer_hand + draw_card()
    print_end_turn_status(dealer_hand)

    print_header('GAME RESULT')
    
    eliminated_players = []

    for key in player_score:
      print_end_game_status(key,player_hand[key],dealer_hand,player_score )
      if player_score[key] == 0:
        eliminated_players.append(key)

    for player in eliminated_players:
      print(f'{player} eliminated!')
      player_score.pop(player)

    if not player_score:
      print("All players eliminated!")
      break

    cont = input ("Do you want to play another hand (y/n)? ")





    
