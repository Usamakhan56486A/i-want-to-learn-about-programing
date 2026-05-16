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



# views.py
from django.shortcuts import render

def home(request):
    posts = [
        {"title": "My First Post", "author": "Usama"},
        {"title": "Learning Django", "author": "Copilot"},
    ]
    return render(request, "home.html", {"posts": posts})
