import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',  ';', ':', "'", '"', ',', '.', '/', '<', '>', '?', '`', '~']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# Pick random letters
for char in range(nr_letters):
    password_list.append(random.choice(letters))

# Pick random symbols
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Pick random numbers
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the list
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

print(f"Your password is: {password}")
