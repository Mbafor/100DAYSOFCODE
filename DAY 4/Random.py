import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.uniform(1, 10)
print(random_float)

random_num = random.randint(0, 1)
if random_num == 0:
    print("Tails")
else:
    print("Heads")

country = ["English", "French", "Germany", "Ethopia"]

#printing items in a list
print(country[0])
print(country[-2])
print(country)
print(country[0,2])

country[2] = "Brazil"
country.append("Cameroon")

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1 Option
random_friends = random.choice(friends)
print(random_friends)

# 2 Option
random_index = random.randint(0,4)
print(friends[random_index])


print(len(friends))