print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

S_pizza = 15
M_pizza = 20
L_pizza = 25

total_pay = 0

if size == "S":
    total_pay += S_pizza
elif size == "M":
    total_pay += M_pizza
elif size == "L":
    total_pay += L_pizza
else:
    print("You typed an unknown size.")

if pepperoni == "Y":
    if size == "S":
        total_pay += 2
    else:
        total_pay += 3

if extra_cheese == "Y":
    total_pay += 1

print(f"Your final bill is: ${total_pay}.")