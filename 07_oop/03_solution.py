# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    

# Class ElectricCar(Car):


# my_car = Car("Toyota", "Fortuner")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Fortuner")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())


################# Itna karte hi hamare Car ki sarii properties ElectricCar mein aa gayi

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_Size):
        super().__init__(brand,model)
        self.battery_size  = battery_Size



my_electric_car = ElectricCar("Tata","Harrier.ev", "79kWh")
# print(my_electric_car.brand)
# print(my_electric_car.model)
# print(my_electric_car.battery_size)
print(my_electric_car.full_name())


# my_car = Car("Toyota", "Fortuner")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Fortuner")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())

