print("Welcome to the rollercoaster!")

height = int(input("Please what is your height in cm: "))
age = int(input("Enter your age: "))
bill = 0

if height > 120:
    print("You can ride")
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif 12<age<18:
        print("Youth tickets are $7")
        bill = 7
    else:
        bill = 12
        print("Adult tickets are $12")
    choice = input("Do you want a photo taken. Type Y for yes and N for no")
    if choice == 'Y':
        bill += 3
        print(f"Your final bill is: {bill}")
    else:
        print(f"Your final bill is: {bill}")
else:
    print("Sorry, you can't ride")