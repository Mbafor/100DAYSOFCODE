import math
#Python Tricks
name = input("what is your name: ")
color = input("What is your favorite color: ")

print(f"{name} likes {color}")

year = int(input("What year where you born: "))
age = 2025 - year
print(f"your are {age} years old")

courses = "Pythonnaiers, This is mb bad"
print(courses[::-1])
print(len(courses))

print(math.fabs(-2.9))

price = 1_000_000
good_credit = True

if good_credit:
    price = price + (0.1 * price)
    print(f"Your payment is: ${price}")
else:
      price = price + (0.2 * price)
      print(f"Your payment is: ${price}")



name = input("Enter your name: ")
while len(name) < 3 or len(name) > 50:
  name = input("Please enter another name: ")
  if len(name) < 3:
    print("Name must be at least 3 characters")
  elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
  
print("Name looks good")

weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
if unit == 'K' or 'k':
    new_weight = weight / 0.45
    print(f"You are {new_weight} pounds")
elif unit == 'L' or 'l':
    new_weight = weight * 0.45
    print(f"You are {new_weight} pounds")
else:
    print("You entered an invalid unit")

secrete_number = 9
attempt = 0
limit = 3

while attempt < limit:
    guess = int(input("Guess: "))
    if guess == secrete_number:
        print("Yon won")
        break
    else: 
        attempt += 1
    
print("You lost")
command = ""
while command.lower() != "quit":
    command = input(">")
    if command == 'help':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif command == "start":
        print("Car started...Ready to go!")
    elif command == "stop":
        print("Car stopped")
    else:
        print("You entered an invalid command")

names = ["Joe", "Mary", "Jonathan"]
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print(i*2)
    if i == 3:
        continue

for i in names:
    print(i)

print(min(numbers))
print(min(names, key=len))

for item in range(2, 10, 2):
    print(item)

prices = [10, 20, 30, 40, 50]

total = 0
for price in prices:
    total = total + price
print(total)

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print("x" * item)
    
names = ["Joe", "Mary", "Jonathan"]
numbers = [1, 2, 3, 4, 5, 6]

numbers.append(7) 
print(numbers.count(2))
print(numbers)  

numbers.reverse()
print(numbers)


# Swap two numbers
a = 5
b = 3

a, b = b, a
print(a, b)

# a = 3
# b = 2

# c = a
# a = b
# b = c

# print(a)
# print(b)

numbers1 = [1, 4, 3]
for num in numbers1:
    print(num*2)

Matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

# print(Matrix[1][2])
for row in Matrix:
    for item in row:
          print(item)


# Basics
numbers = [10, 20, 30, 40]

print(numbers[0])   # first item
print(numbers[-1])  # last item
print(numbers[1:3]) # slice
print(numbers[::-1]) # reverse

list.append(x)


list.remove(x)
list.pop()        # removes last
list.pop(2)       # remove by index
list.clear()      # empty list

len(numbers)
min(numbers)
max(numbers)
sum(numbers)



#Example 1: Printing items in a list

numbers = [1,2,3,4,5]

for i in numbers:
    print(i)

#Example 2: summing items

prices = [10, 20, 30, 40, 50]

total = 0
for price in prices:
    total = total + price
print(total)

#Example 3: Combining two list

numbers1 = [1, 4, 3]
numbers2 = [4, 5, 6]

combined = numbers1 + numbers2
print(combined)


# Example 4: Sorting items in a list

numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers) 

numbers.sort(reverse=True)
print(numbers) 

#Example 4: Checking if an item is in a list

fruits = ["apple", "banana", "orange"]

if "banana" in fruits:
    print("Yes, it's in the list!")
else:
    print("No, it's not there.")

# Example 5: Removing duplicates

numbers = [1,2,2,3,4,4,5]

unique =[]

for num in numbers:
    if num not in unique:
        unique.append(num) 

print(unique)


# CHeck for pale

word= "level"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# Nested List:

Matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

# print(Matrix[1][2])
for row in Matrix:
    for item in row:
          print(item)



def greet_user():
    print("Hi, this is my first function")
    print("Welcome on board")

greet_user()
greet_user()

def greet(first_name, last_name):
    print(f"Hi, {first_name} {last_name}")
greet("John", "Smith")

def square():
    num = int(input())
    return num * num

result = square()
print(result)

def area():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    return length * width

print(area())

def volume(l, w, h):
    return l*w*h

vol = volume(3,4,5)
print(f"The volume is:{vol}")



