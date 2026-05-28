# class Vehicel:
#     def __init__(self,brand, model, year, rental_price):
#         self.brand = brand
#         self.model =model
#         self.year = year
#         self.rental_price = rental_price


#     def display_info(self):
#         print(f'You rent {self.brand} brand {self.model} model  and {self.year} year vehciel and your total rent is {self.total_rent}')        

#     def calculate_rent(self,days,insurance_fees):
#         self.total_rent = self.rental_price * days + insurance_fees 
#         return self.total_rent

# class Car (Vehicel):
#     def __init__(self, brand, model, year, rental_price):
#         super().__init__(brand, model, year, rental_price)


#     def calculate_rent(self, days,insurance_fees=200):
#         return super().calculate_rent(days,insurance_fees)   
        
# class Bike(Vehicel):
#     def __init__(self, brand, model, year, rental_price):
#         super().__init__(brand, model, year, rental_price)

#     def calculate_rent(self, days, insurance_fees=100):
#         return super().calculate_rent(days, insurance_fees)    
    
# class Truck(Vehicel):
#     def __init__(self, brand, model, year, rental_price):
#         super().__init__(brand, model, year, rental_price)

#     def calculate_rent(self, days, insurance_fees=250):
#         return super().calculate_rent(days, insurance_fees)


# car1 = Car('Honda','sedan',2026,1000)
# car2 = Car('BMW iX3','SUV',2026,1200)
# car1.calculate_rent(4)
# car2.calculate_rent(5)
# car1.display_info()
# car2.display_info()
# bike1 = Bike('BMW R 1300 RS','sport_tour',2026,800)
# bike2 = Bike('Ducati Monster','Naked_Bike',2026,900)
# bike1.calculate_rent(10)
# bike2.calculate_rent(8)
# bike1.display_info()
# bike2.display_info()
# truck1 = Truck('Ford','F_150',2026,1500)
# truck2 = Truck('Toyota','Tcoma',2026,1400)
# truck1.calculate_rent(4)
# truck2.calculate_rent(5)
# truck1.display_info()
# truck2.display_info()


# class Book:
#     def __init__(self,title,author,copies):
#         self.title = title
#         self.author = author
#         self.__copies = copies

#     def borrow_book(self):
#         pass


#     def return_book(self):
#         pass    

# class LibrarySystem():
#     def __init__(self):
#         pass

#     def add_book(self):
#         pass    

#     def search_book(self):
#         pass

#     def issue_book(self):
#         pass    


# class User:
#     def __init__(self,name,borrow_limit):
#         self.name = name
#         self.borrow_limit = borrow_limit
        

# class Teacher(User):
#     def __init__(self, name, borrow_limit = 5):
#         super().__init__(name, borrow_limit)



# class Students(User):
#     def __init__(self, name, borrow_limit = 3):
#         super().__init__(name, borrow_limit)


# class Guest(User):
#     def __init__(self, name, borrow_limit = 1):
#         super().__init__(name, borrow_limit)


# class UserDetails:
#     def __init__(self,firstname,lastname,middlename=None):
#         self.firstname = first_name
#         self.middlename = middlename
#         self.lastname = lastname
        
#     def details(self):
#         if self.middlename != None :
#             print(f'First_Name : {self.firstname}\nMiddle_name : {self.middlename}\nLast_name : {self.lastname}')
#         else:    
#             print(f'First_Name : {self.firstname}\nLast_name : {self.lastname}')

# first_name = input('enter 1st name : ')
# second_name = input('enter 2nd name : ')
# user1 = UserDetails(first_name,second_name,'king')
# user1.details()
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):   # + operator
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __str__(self):
#         return f"({self.x}, {self.y})"

# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# print(v1 + v2)   # (6, 8)

# dict = {'name' : 'Usama','age' : 24 , 'hobby' : 'cricket'}
# dict1 =['a','b','c']
# print(dict.fromkeys(dict1,1,2,3))


# users = {
#     "user_01": {
#         "name": "Alice",
#         "email": "alice@example.com",
#         "roles": ["Admin", "Editor"]
#     },
#     "user_02": {
#         "name": "Bob",
#         "email": "bob@example.com",
#         "roles": ["Guest"]
#     }
# }
# print(users.get("user_01").get('name'))

# for user_id, info in users.items():
#     print(f"ID: {user_id}")
#     print(f"Name: {info['name']}")
#     print(f"Role: {info['roles']}")

# list = [1,'usama',7,'khan']
# it = iter(list)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# dict1 =['a','b','c']
# dict2 =[1,2,3]
# a = dict(zip(dict1,dict2))
# print(a)

# a = [1,2,3,4,5]
# b = [6,7,8,9,0]
# c = dict(zip(a,b))
# print(c)

# def logger(func):
#     def wrapper(*args, **kwargs):
#         print('Welcome Sir')
#         print(f'Welcome {args}')
#         return func(*args, **kwargs)
#     return wrapper

# @logger
# def greet(name):
#     return f"Hello {name}"

# print(greet("Usama"))

#  import time
# def decor(func):
#     values = {}
#     def wrapper(*args):
#         if args in values:
#             return values [args]  
#         result = func(*args)
#         values [args] = result
#         return result
#     return wrapper    

# @decor
# def add(a,b):
#     time.sleep(5)
#     return a + b


# print(add(4,5))
# print(add(4,5))
# print(add(5,5))


 
# # views.py
# def fibonacci(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))  # Output: 55


# def factorial(n):
#     if n == 0:   # Base case
#         return 1
#     else:        # Recursive case
#         return factorial(n-1) * factorial(n - 1)

# print(factorial(5))  # Output: 120

# def countdown(n):
#     if n <= 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n - 1)

# countdown(5)

# def string_reverse(n):
#     # for i in n:
#         # a+=i
#     # print(a)
#     if len(n) == 1:
#         return n
#     return string_reverse(n[1:] ) + string_reverse(n[:-1]) + n[0]

# s =string_reverse('hello')
# print(s)

# def recursion(n):
#     if n == 0:
#         return 1
#     elif n < 1:
#         return 1
#     print(n)
#     a = recursion(n-1) + recursion(n-2)
#     return a
# q = recursion(6)
# print(q)


# Hotel menu


# class Order:
#     hotel_menu = {
#     "burger": 10,
#     "pizza": 15,
#     "pasta": 12,
#     'cold drinks':20
#     }
#     def __init__(self,):
#         pass

#     def order (self):
#         print("Welcome to our hotel! Here's our menu:")
#         for item, price in self.hotel_menu.items():
#             print(f"{item}: ${price}")
#         total_bill = 0
#         while True:
#             user_choice = input("Please enter the item you want to order: ")
#             user_ammount = int(input("Please enter the quantity: "))
#             if user_choice in self.hotel_menu:
#                 print(f"You have ordered {user_ammount} {user_choice}\'s which costs ${self.hotel_menu[user_choice] * user_ammount}.")
#                 total_bill += self.hotel_menu[user_choice] * user_ammount
#             else:
#                 print("Sorry, we don't have that item on the menu.")
#             next_order =input('Do you want to order anything else? (yes/no): ')
#             if next_order.lower() == 'yes':
#                 continue
#             else:
#                 print(f"Your total bill is ${total_bill}.")
#                 break
# user_order = Order()
# user_order.order()


# from dataclasses import dataclass, field
# from datetime import datetime

# @dataclass(order=True)
# class Expense:
#     amount: float
#     category: str
#     description: str
#     date: datetime = field(default_factory=datetime.now)

# class ExpenseManager:
#     def __init__(self):
#         self.expenses = []

#     def add_expense(self, amount, category, description):
#         new_expense = Expense(amount, category, description)
#         self.expenses.append(new_expense)
#         print(f"Added: {new_expense}")

#     def show_total(self):
#         total = sum(e.amount for e in self.expenses)
#         print(f"\nTotal Spending: ${total:.2f}")

#     def filter_by_category(self, category):
#         return [e for e in self.expenses if e.category.lower() == category.lower()]

# e1 = Expense(10.0, "Misc", "Pen")
# e2 = Expense(10.0, "Misc", "Pen")
# b = ExpenseManager()
# b.add_expense(10.0, "Food", "Lunch")
# b.show_total()
# print(e1 = e2)  # True

# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
    
#     def __str__(self):
#         return f"Book: {self.title}"
    
#     def __len__(self):
#         return len(self.title)

# b = Book("Python Mastery", 350)
# print(str(b))   # Book: Python Mastery
# print(len(b))   # 350
# class metaclass(type):
#     def __new__(cls, name, bases, attrs):
#         print(f"Creating class {name} with metaclass {cls.__name__}")
#         bases = tuple(base for base in bases)  # Ensure bases is a tuple        
#         # Add a custom method to all classes that use this metaclass
#         attrs['custom_method'] = lambda self: f"This is a custom method for {name}"
#         return super().__new__(cls, name, bases, attrs)


# class Student(metaclass=metaclass):
#     def __init__(self, name, marks):
#         self._name = name
#         self._marks = marks
    
#     @property
#     def marks(self):
#         return self._marks
    
#     @marks.setter
#     def marks(self, value):
#         if value < 0:
#             raise ValueError("Marks cannot be negative")
#         self._marks = value

# s = Student("Usama", 85)
# print(s.marks)   # 85
# s.marks = 23
#      # updates safely
# print(s.marks)   # 85
# print(s.custom_method())  # This is a custom method for Student
dict={
        'name':'Usama',
        'age': 24,
        'city': 'Hirpur',
        'country': 'Pakistan',
        'hobbies': ['coding', 'gaming', 'traveling']
}
print("<br>".join(f'{key}: {value}' for key, value in dict.items()))
