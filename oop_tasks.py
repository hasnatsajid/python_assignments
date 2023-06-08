# Python Classes and Objects:
# Write a Python class called BankAccount that represents a bank account. The class should have attributes like account_number, balance, and account_holder_name. Implement methods to deposit money, withdraw money, and display the current balance.
# SOLUTION -----------
# class BankAccount:
#     def __init__(self, account_number, balance, account_holder_name):
#         self.account_number = account_number
#         self.balance = balance
#         self.account_holder_name = account_holder_name

#     def deposit_money(self, amount):
#         self.balance += amount
#         print(f"You have deposited : {amount}")

#     def withdraw_money(self, amount):
#         self.balance -= amount
#         print(f"You have withdrawn : {amount}")

#     def display_balance(self):
#         print(f"Your current balance is : {self.balance}")

# state_bank = BankAccount('12345', 10000, 'Hasnat')
# state_bank.display_balance()
# state_bank.deposit_money(500)
# state_bank.display_balance()
# state_bank.withdraw_money(250)
# state_bank.display_balance()

# Inheritance:
# Create a base class called Shape with methods calculate_area and calculate_perimeter. Create derived classes Rectangle and Circle that inherit from the Shape class. Implement the necessary methods in the derived classes to calculate the area and perimeter of rectangles and circles.
# SOLUTION ----------------------
# import math

# class Shape:
#     def __init__(self):
#         pass

#     def calculate_area(self):
#         pass

#     def calculate_perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         print(f"Area of rectangle : {self.length * self.width}")

#     def calculate_perimeter(self):
#         print(f"Perimeter of circle : {2 * (self.length + self.width)}")
        
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         print(f"Area of circle : {math.pi * self.radius**2}")

#     def calculate_perimeter(self):
#         print(f"Perimeter of circle : {2 * math.pi * self.radius}")
        

# circle1 = Circle(2)
# rectangle1 = Rectangle(3,4)
# circle1.calculate_area()
# circle1.calculate_perimeter()
# rectangle1.calculate_area()
# rectangle1.calculate_perimeter()

# Polymorphism:
# Write a Python function called calculate_total_area that accepts a list of shapes (instances of the Shape class from the previous question) and calculates the total area of all shapes. The function should be able to handle different types of shapes in the list.
# SOLUTION ------------------------
# import math

# class Shape:
#     def __init__(self):
#         pass

#     def calculate_area(self):
#         pass

#     def calculate_perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)
        
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return math.pi * self.radius**2

#     def calculate_perimeter(self):
#         return 2 * math.pi * self.radius

# def calculate_total_area(shapes):
#     total=0
    
#     for shape in shapes:
#         if isinstance(shape, Shape):
#             total += shape.calculate_area()
#     return total

# rectangle = Rectangle(3, 4)
# circle = Circle(2)
# shapes = [rectangle, circle]
# total_area = calculate_total_area(shapes)
# print(total_area)

# Association:
# Create a class called Author with attributes like name, age, and nationality. Create another class called Book with attributes like title, year, and an instance of the Author class. Implement methods to get the author's details from a book object and vice versa.
# class Author:
#     def __init__(self, name=None, age=None, nationality=None):
#         self.name = name
#         self.age = age
#         self.nationality = nationality


# class Book:
#     def __init__(self, title, year, author):
#         self.title = title
#         self.year = year
#         self.author = author # Composition

#     def get_author(self):
#         print(f"The author of book '{self.title}' is {self.author.name} with age {self.author.age} and having nationality {self.author.nationality}")

# author1 = Author('Junaid', 26, 'India')
# book1 = Book('Little dog', 1991, author1)
# # book1.author = Author('Junaid', 26, 'India')
# book1.get_author()

# Composition:
# Implement a class called Address with attributes like street, city, state, and zip_code. Create a class called Person with attributes like name and an instance of the Address class. Implement methods to get a person's address details and change their address.
# class Address:
#     def __init__(self, street, city, state, zip_code):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.zip_code = zip_code

# class Person:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

#     def get_address(self):
#         print(f"The address of {self.name} is : \n street:{self.address.street}, city:{self.address.city}, state:{self.address.state}, zip_code:{self.address.zip_code}")

#     def change_address(self, street, city, state, zip_code):
#         self.address.street = street
#         self.address.city = city
#         self.address.state = state
#         self.address.zip_code = zip_code

# address = Address('10', 'lahore', 'punjab', 123)
# person_1 = Person('Hasnaat', address)
# person_1.get_address()
# person_1.change_address('25', 'karachi', 'sindh', 456)
# person_1.get_address()

# Aggregation:
# Create a class called University with attributes like name and a list of student objects. The student class should have attributes like name, age, and major. Implement methods to add a student to the university and display all the students in a university object.
# class University:
#     def __init__(self, name):
#         self.name = name
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def display_students(self):
#         for student in self.students:
#             print(f"Student details -> name: {student.name}, age: {student.age}, major: {student.major}")


# class Student:
#     def __init__(self, name, age, major):
#         self.name = name
#         self.age = age
#         self.major = major

# student1 = Student("Hasnaat", 28, 'Computer')
# student2 = Student("Junaid", 26, 'AI')
# student3 = Student("Ahmad", 30, 'NLP')

# my_university = University("UET")
# my_university.add_student(student1)
# my_university.add_student(student2)
# my_university.add_student(student3)
# my_university.display_students()

# Python lists and loops
# def filter_even_numbers(numbers):
#     even_numbers = []

#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
    
#     return even_numbers
    
# print(filter_even_numbers([1,2,3,4,5,6,7]))

# Conditional statements
# class GradeCalculator:
#     def __init__(self, score):
#         self.score = score
    
#     def calculate_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score <= 89 and self.score >= 80:
#             return 'B'
#         elif self.score <= 79 and self.score >= 70:
#             return 'C'
#         elif self.score <= 69 and self.score >= 60:
#             return 'D'
#         else:
#             return 'F'

# my_grade = GradeCalculator(91)
# print(my_grade.calculate_grade())

# Python Dictionaries
# def count_word_frequency(input):
#     checker = []
#     count_dict = {}
#     for word in input:
#         if word not in checker and word != ' ':
#             checker.append(word)
#             count_dict[word] = 1
#         elif count_dict.get(word) != None:
#             count_dict[word] += 1
        
#     return count_dict
# print(count_word_frequency('hello hasnaat HHH'))

# Functions
# def calculate_discount(price, discount_percentage=10.0):
#     new_price = price - price * ( discount_percentage / 100 )
#     return round(new_price, 2)
# print(calculate_discount(1650, 18.551))

# Abstraction
# from abc import ABC, abstractmethod
# import math
# class Shape(ABC):

#     @abstractmethod
#     def calculate_area(self):
#         pass

#     def display_shape_info(self):
#         print(f"Type of shape : {type(self).__name__}")

# class Rectangle(Shape):

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def calculate_area(self):
#         print(f"Area of rectangle : {self.length * self.width}")

# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius
    
#     def calculate_area(self):
#         print(f"Area of cirlcle : {math.pi * self.radius**2}")

# rectangle1 = Rectangle(5, 6)
# rectangle1.calculate_area()
# rectangle1.display_shape_info()
# circle1 = Circle(2)
# circle1.calculate_area()
# circle1.display_shape_info()