# Object Oriented Programming
# Building a basic student management system

class StudentManager:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added: {student}")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Removed: {student}")

    def show_student(self):
        print(f"Student List '{self.name}':")
        for student in self.students:
            print(f"- {student}")

    
my_class = StudentManager("Computer Engineering")

my_class.add_student("Emily")
my_class.add_student("Josh")
my_class.add_student("Daniel")

my_class.show_student()
my_class.remove_student("Josh")

my_class.show_student()
