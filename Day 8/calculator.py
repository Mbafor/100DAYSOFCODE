
# function definitions
def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        print("Error! cannot divide by zero")
    else:
        return a - b
    
# Main program

def calculator():
    print("Welcome to the mini Calculator")
    while True:
        print("\nSelect operator:")
        print("1. Add.")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                print(f"Result: {add(num1, num2)}")
        
            elif choice == "2":
                print(f"Result: {substract(num1, num2)}")

            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
        
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")

        else: 
            print("Invalid input! Please enter a number between 1 and 5")

# Run the calculator
calculator()


