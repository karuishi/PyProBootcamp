"""
Mine: Lazy version
"""

# import random
# from art import logo
#
# print(logo)
#
# attempts = 0
# number = random.randint(1, 100)
#
# print("Welcome to the Number Guessing Game!")
# print("I am thinking of a number between 1 and 100.")
# level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
#
# if level == "easy":
# 	attempts = 10
# elif level == "hard":
# 	attempts = 5
#
# for _ in range(attempts):
# 	print(f"You have {attempts} attempts remaining to guess the number.")
# 	guess = int(input("Make a guess: "))
# 	if guess == number:
# 		print("You guessed the number!")
# 		break
# 	elif guess > number:
# 		print("Too high!")
# 	elif guess < number:
# 		print("Too low!")
#
# 	if attempts == 0:
# 		print("You've run out of guesses, you lose!")
# 	attempts -= 1


import random, art


EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_guess(guess, number, attempts):
	if guess == number:
		print(f"You guessed the number! The answer was {number}")
	elif guess > number:
		print("Too high!")
		return attempts - 1
	else:
		print("Too low!")
		return attempts -1

def set_difficulty():
	level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
	if level == "easy":
		return EASY_LEVEL_ATTEMPTS
	else:
		return HARD_LEVEL_ATTEMPTS

def game():
	print(art.logo)
	print("Welcome to the Number Guessing Game!")
	print("I am thinking of a number between 1 and 100.")
	number = random.randint(1, 100)

	attempts = set_difficulty()

	guess = 0
	while guess != number:
		print(f"You have {attempts} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))

		attempts = check_guess(guess, number, attempts)
		if attempts == 0:
			print("You've run out of guesses, you lose!")

game()