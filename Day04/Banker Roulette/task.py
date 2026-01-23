import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = random.randint(0,4)

# 1 Option
print(friends[random_number])
# 2nd Option
print(random.choice(friends))
