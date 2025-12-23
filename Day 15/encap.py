# Python Encapsulation

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # private attribute

 # Getter method
    def get_age(self):
        return self.__age

    # Setter method
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

p1 = Person("Emil", 25)
print(p1.get_age())   # Access age safely
p1.set_age(30)        # Modify age safely
print(p1.get_age())







