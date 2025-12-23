# Polymorphism
# Restaurant Payment Processing System

class Payment:
    def __init__(self, name):
        self.name = name

class Cash(Payment):
    def pay(self, amount):
        print(f"{self.name} paid {amount} in cash")

class Card(Payment):
    def pay(self, amount):
        print(f"{self.name} paid {amount} by card")


class MobileMoney(Payment):
    def pay(self, amount):
        print(f"{self.name} paid {amount} via mobile money")


def process_payment(payment, amount):
    payment.pay(amount)

# Main program

name = input("Enter your name: ")
amount = float(input("Enter amount to pay: "))

print("\nChoose payment method:")
print("1. Cash")
print("2. Card")
print("3. Mobile Money")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    payment = Cash(name)
elif choice == "2":
    payment = Card(name)
elif choice == "3":
    payment = MobileMoney(name)
else:
    print("Invalid payment option")
    exit()

process_payment(payment, amount)
