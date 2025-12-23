# Inheritance
# Building a school management system

class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def greet(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old")


class Student(Person):
    def __init__(self, name, age, id_number, program, level):
        super(). __init__(name, age, id_number)
        self.program = program
        self.level = level
        self.courses = []

    def add_courses(self, course):
        self.courses.append(course)
        print(f"Added: {course}")

    def display_courses(self):
        print(f"Student courses for {self.name}:")
        for course in self.courses:
            print(f"- {course}")


class Teacher(Person):
    def __init__(self, name, age, id_number, subject, salary):
        super(). __init__(name, age, id_number)
        self.salary = salary
        self.subject = subject
        self.student_grades = {}
    
    def assign_grade(self, student, grade):
        self.student_grades[student.name] = grade
        print(f"{student.name} got {grade} in {self.subject}")


    def display_grade(self, student):
        grade = self.student_grades.get(student.name, "No grade assigned")
        print(f"{student.name} got {grade} in {self.subject}")


# Testing

p1 = Person("Mbafor", 21, "2138")
p1.greet()

s1 = Student("Joshua",  23, "21470997", "Computer Engineering", 200)
s1.add_courses("DSA")
s1.add_courses("Programming")
s1.display_courses()
s1.greet()

