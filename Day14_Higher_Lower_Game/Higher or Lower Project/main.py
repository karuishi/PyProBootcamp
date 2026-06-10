import art, random, game_data

dictionary = game_data.data

def compare_followers(option_a, option_b):
	if option_a['follower_count'] > option_b['follower_count']:
		return option_a
	else:
		return option_b

def game():
	print(art.logo)
	score = 0
	option_a = random.choice(dictionary)
	option_b = random.choice(dictionary)

	game_over = False
	while not game_over:
		while option_a == option_b:
			option_b = random.choice(dictionary)

		answer = compare_followers(option_a, option_b)

		print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
		print(art.vs)
		print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

		guess = input("Who has more followers? Type 'A' or 'B': ").lower()
		if guess == 'a':
			guess = option_a
		else:
			guess = option_b

		if guess == answer:
			score += 1
			option_a = guess
			option_b = random.choice(dictionary)
		else:
			game_over = True
			print(f"You guessed the wrong answer. Final score: {score}")

game()