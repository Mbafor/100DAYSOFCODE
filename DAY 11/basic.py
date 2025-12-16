# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hell, my name is {self.name}")

    
# p1 = Person("Emily", 25)
# p1.greet()

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     def display_info(self):
#         print(f"{self.year}, {self.brand}, {self.model}")


# car1 = Car("Toyota", "Corola", 2020)
# car1.display_info()


# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

# car1 = Car("Toyota", "Corolla")

# print(car1.brand)
# print(car1.model)

# class calculator():
#     def add(self, a, b):
#         return a + b
#     def multiply(self, a, b):
#         return a * b
    

# cal = calculator()
# print(cal.add(5,3))
# print(cal.multiply(4,7))


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def get_info(self):
#     print(f"{self.name} is {self.age} years old")

# p1 = Person("Tobias", 28)
# p1.get_info()

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         self.age += 1
#         print(f"Happy birthday, you are now {self.age}")

# P1 = Person("Emily", 24)
# P1.greet()
# P1.greet()

class Person:
      def __init__(self, name):
            self.name = name
        
      def talk(self):
           print(f"Hello, {self.name}")

P1 = Person("John")
P1.talk()