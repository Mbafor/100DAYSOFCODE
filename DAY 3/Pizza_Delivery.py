print("Welcome to Python Pizza Deliveries")
bill = 0

# 1. Determine the base price based on size
size = input("What size do you want? S, M or L: ")

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25  
else:
    print("Invalid size selected.")

# 2. Add Pepperoni
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

if pepperoni == 'Y':
    if size == 'S':
        bill += 2  
    else:
        bill += 3

# 3. Add Cheese 
cheese = input("Do you want cheese on your pizza? Y or N: ")

if cheese == 'Y':
        bill += 1  

# 3. Print final result
print(f"Your total bill is: ${bill}")