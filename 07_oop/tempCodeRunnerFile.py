class Car:

#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#         Car.total_car += 1

#     def get_brand(self):
#         return self.__brand + "!"

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Petrol or Diesel"
    
#     def general_description(self):
#         return "Cars are means of transport"

    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size

#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Battery"


# Curvv = Car("Tata","Curvv")
# Car("Tata", "Nexon")
# print(Curvv.general_description())
# print(Car.general_description())