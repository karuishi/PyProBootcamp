try:
	age = int(input("How old are you? "))
except ValueError:
	print("You have typed in an invalid number. Try again with a numerical type.")
	age = int(input("How old are you? "))

if age > 18:
	print(f"You can drive at age {age}.")
