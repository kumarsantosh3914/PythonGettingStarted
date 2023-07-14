# Python Object Oriented Programming

# Classes - Class is a template/blue-print for real-world entities

# Objects - Objects are specific instances of a class
# Creating the first Class

class Phone:

    def make_call(self):
        print("Making phone call")
    
    def play_game(self):
        print("Playing Game")

p1 = Phone()     # Instantiating the 'p1' object

# Invoking methods through object
p1.make_call()
p1.play_game()


# Adding parameters to the class

class Phone:
    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color
    
    def show_cost(self):
        return self.cost
    
    def make_call(self):
        print("Making phone call")

    def play_game(self):
        print("Playing Game")


# Creating a class with Constructor
class Employee:
    def __init__(self, name, age, salary, gender):

        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of employee is ", self.name)
        print("Age of employee is ", self.age)
        print("Salary of employee is ", self.salary)
        print("Gender of employee is ", self.gender)

# Instantiating Object
e1 = Employee('Santosh', 20, 90000, 'Male')

# Invoking the 'employee_details' method
e1.employee_details()

# Inheritance in Python - With inheritance one class can derive the properties of another class
# Example - Man inheriting features from his father

class Vehicle:

    def __init__(self, mileage, cost):             # Creating the base class
        self.mileage = mileage
        self.cost = cost

    def show_details(self):             
        print("I am a Vehicle")
        print("Mileage of Vehicle is ", self.mileage)
        print("Cost of Vehicle is ", self.cost)


v1 = Vehicle(500, 500)      # Instantiating the object for base class
v1.show_details()

# Inheritance Examle
class Car(Vehicle):               # Creating the child class
    def show_car(self):
        print("I am a car")


# Instantiating the object for child class
c1 = Car(200, 1200)
c1.show_details()

# Invoking the child class  method
c1.show_car()


# Over-riding init method
class Car(Vehicle):

    def __init__(self, mileage, cost, tyres, hp):
        super().__init__(mileage, cost)
        self.tyres = tyres
        self.hp = hp

    def show_car_details(self):
        print("I am a car")
        print("Number of tyres are ", self.tyres)
        print("Value of horse power is ", self.hp)


# Invoking show_details() method from parent class
c1 = Car(20, 12000, 4, 300)
c1.show_details()


# Invoking show_car_details()
c1.show_car_details()


# Types of Inheritance - Single Inheritance, Multiple Inheritance, Multilevel Inheritance, Hybrid Inheritance

# Multiple Inheritance in Python

class Parent1():
    def assign_string_one(self, str1):
        self.str1 = str1

    def show_string_one(self):
        return self.str1

# Parent Class Two
class Parent2():
    def assign_string_two(self, str2):
        self.str2 = str2

    def show_string_two(self):
        return self.str2

# Child Class
class Derived(Parent1, Parent2):
    def assign_string_three(self, str3):
        self.str3 = str3

    def show_string_three(self):
        return self.str3

# Instantiating object of child class
d1 = Derived()
d1.assign_string_one("one")
d1.assign_string_two("two")
d1.assign_string_three("three")

# Invoking methods
d1.show_string_one()
d1.show_string_two()
d1.show_string_three()


# Multilevel Inheritance - In multi-level Inheritance, we have parent, child, grand-child relationship

# Multi-Level Inheritance in Python

# Parent Class
class Parent():
    def assign_name(self, name):
        self.name = name

    def show_name(self):
        return self.name

# Child Class
class Child(Parent):
    def assign_age(self, age):
        self.age = age

    def show_age(self):
        return self.age

# Grand-Child Class
class GrandChild(Child):
    def assign_gender(self, gender):
        self.gender = gender 

    def show_gender(self):
        return self.gender

# Instantiating object of GrandChild class
g1 = GrandChild()
g1.assign_name("Santosh")
g1.assign_age(20)
g1.assign_gender("Male")

# invoking class methods
g1.show_name()
g1.show_age()
g1.show_gender()