class Vehicel:
    def __init__(self,brand, model, year, rental_price):
        self.brand = brand
        self.model =model
        self.year = year
        self.rental_price = rental_price


    def display_info(self):
        print(f'You rent {self.brand} brand {self.model} model  and {self.year} year vehciel and your total rent is {self.total_rent}')        

    def calculate_rent(self,days,insurance_fees):
        self.total_rent = self.rental_price * days + insurance_fees 
        return self.total_rent

class Car (Vehicel):
    def __init__(self, brand, model, year, rental_price):
        super().__init__(brand, model, year, rental_price)


    def calculate_rent(self, days,insurance_fees=200):
        return super().calculate_rent(days,insurance_fees)   
        
class Bike(Vehicel):
    def __init__(self, brand, model, year, rental_price):
        super().__init__(brand, model, year, rental_price)

    def calculate_rent(self, days, insurance_fees=100):
        return super().calculate_rent(days, insurance_fees)    
    
class Truck(Vehicel):
    def __init__(self, brand, model, year, rental_price):
        super().__init__(brand, model, year, rental_price)

    def calculate_rent(self, days, insurance_fees=250):
        return super().calculate_rent(days, insurance_fees)


car1 = Car('Honda','sedan',2026,1000)
car2 = Car('BMW iX3','SUV',2026,1200)
car1.calculate_rent(4)
car2.calculate_rent(5)
car1.display_info()
car2.display_info()
bike1 = Bike('BMW R 1300 RS','sport_tour',2026,800)
bike2 = Bike('Ducati Monster','Naked_Bike',2026,900)
bike1.calculate_rent(10)
bike2.calculate_rent(8)
bike1.display_info()
bike2.display_info()
truck1 = Truck('Ford','F_150',2026,1500)
truck2 = Truck('Toyota','Tcoma',2026,1400)
truck1.calculate_rent(4)
truck2.calculate_rent(5)
truck1.display_info()
truck2.display_info()



