# Object Oriented Programming
# Food delivery program

menu = {
    "Chickwizz": 2650,
    "Pizza": 3000,
    "Burger": 2000,
    "Fries": 1000
}

class CustomerOrder:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item_name):
        if item_name in menu:
            self.items.append(item_name)
            print(f"{item_name} added to {self.name}")

        else:
            print(f"Sorry, {item_name} is not on the menue")


    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            print(f"{item_name} removed from {self.name}'s order.")
        
        else:
            print(f"{item_name} not found in order")

    def get_total(self):
        total = 0
        for item in self.items:
            total += menu[item]
        return total
        
    def show_order(self):
        if not self.items:
            print("Order is empty. ")

        else:
            print(f"\n{self.name}'s Order:")
            for item in self.items:
                print(f"- {item} : {menu[item]}")


order = CustomerOrder("Josh")


order.add_item("Pizza")
order.add_item("burger")
order.add_item("Fries")
order.add_item("ice cream") # not in the 


order.remove_item("burger")
order.show_order()
print(f"\nTotal: {order.get_total()}")