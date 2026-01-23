# TODO-0: Minha versão é funcional, contudo, não é elegante. Uso desnecessário de listas!

# from art import *
#
# print(logo)
#
# bidders = []
# highest_bid = 0
# highest_bidder = ""
# should_continue = True
# while should_continue:
# 	# TODO-1: Ask the user for input
# 	name = input("What is your name? ").lower()
# 	price = int(input("What is your bid? $"))
#
# 	# TODO-2: Save data into dictionary {name: price}
# 	auction = {"name": name, "bid": price}
# 	bidders.append(auction)
#
# 	print(auction)
# 	# TODO-3: Whether if new bids need to be added
# 	answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
# 	if answer == 'no':
# 		should_continue = False
#
# # TODO-4: Compare bids in dictionary
# for bidder in bidders:
# 	if bidder["bid"] > highest_bid:
# 		highest_bid = bidder["bid"]
# 		highest_bidder = bidder["name"]
#
# print(f"The winner is {highest_bidder} with a bid of${highest_bid}")


from art import logo
print(logo)

def find_highest_bidder(bids):
	highest_bid = 0
	winner = ""
	for bidder in bids:
		bid_amount = bids[bidder] # Guarda o valor que está armazenado na chave atual
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner} with a bid of ${highest_bid}")


bid = {}
continue_bidding = True
while continue_bidding:
	name = input("What is your name? ")
	price = int(input("What is your bid? $"))
	bid[name] = price
	should_continue = input("Would you like to continue (yes/no)? \n")
	if should_continue == "no":
		continue_bidding = False
		find_highest_bidder(bid)
	elif should_continue == "yes":
		print("\n" * 20)