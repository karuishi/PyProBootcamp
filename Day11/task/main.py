from random import choice
from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []

blackjack = 21
ace = 11

should_continue = True

def add_card(hand):
	random_card = choice(cards)
	hand.append(random_card)
	return hand

def calculate_score(hand):
	sum_cards = sum(hand)
	return sum_cards

def initialize_hands():
	global player_score, dealer_score
	for x in range(0, 2):
		add_card(player_hand)
		add_card(dealer_hand)

	player_score = calculate_score(player_hand)
	dealer_score = calculate_score(dealer_hand)

	print(f"Player hand: {player_hand}, current player score: {player_score}")
	print(f"Dealer hand: {dealer_hand[0]}")

	return player_score, dealer_score  # Returns a tuple

def is_blackjack():
	global should_continue
	if player_score == blackjack:
		print("Blackjack! You win!")
		should_continue = False
	elif dealer_score == blackjack:
		print("Blackjack! Computer wins!")
		should_continue = False

def is_busted():
	global player_score, dealer_score, should_continue
	if player_score > blackjack and 11 in player_hand:
		ace_index = player_hand.index(11)
		player_hand[ace_index] = 1
		player_score = calculate_score(player_hand)
		if player_score > blackjack:
			print("You lose!")
			should_continue = False
	elif player_score > blackjack:
		print("You lose!")
		should_continue = False

	if dealer_score > blackjack and 11 in dealer_hand:
		ace_index = dealer_hand.index(11)
		dealer_hand[ace_index] = 1
		dealer_score = calculate_score(dealer_hand)
		if dealer_score > blackjack:
			print("You win!")
			should_continue = False
	elif dealer_score > blackjack:
		print("You win!")
		should_continue = False

"""
If a function returns 2 values, 
you can place the 2 variables on the left side of the equals sign, 
in the same order in which they are returned .
"""
player_score, dealer_score = initialize_hands() # Receives player_score first, then dealer_score
is_blackjack()
is_busted()

while should_continue:
	hit = input("Do you want another card? Type 'yes' or 'no': ")
	if hit == "no":
		should_continue = False
		while dealer_score < 17:
			add_card(dealer_hand)
			dealer_score = calculate_score(dealer_hand)
			print(f"Dealer hand: {dealer_hand}, current dealer score: {dealer_score}")

		if dealer_score > blackjack:
			print(f"you win! dealer score: {dealer_score}")
		elif dealer_score > player_score:
			print(f"you lose! dealer score: {dealer_score}")
		elif dealer_score < player_score:
			print(f"you win!dealer score: {dealer_score}")
		else:
			print(f"Draw! dealer score: {dealer_score}")

	if hit == "yes":
		add_card(player_hand)
		player_score = calculate_score(player_hand)
		print(f"player hand: {player_hand}, current player score: {player_score}")
		if player_score == blackjack:
			print("You win!")
			should_continue = False
		is_busted()