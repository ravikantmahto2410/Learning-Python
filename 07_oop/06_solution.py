# class Car:

#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#         self.total_car    ####  aise bhi humlog kar sakte hai kam use hota hai aisa

#     def get_brand(self):
#         return self.__brand + "!"

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Petrol or Diesel"

    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size

#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Battery"



# my_electric_car = ElectricCar("Tata","Harrier.ev", "79kWh")
# # print(my_electric_car.__brand)   ##### Ye to nahi chalega as direct access is not allowed
# print(my_electric_car.fuel_type())



# Curvv = Car("Tata","Curvv")
# Nexon = Car("Tata", "Nexon")
# print(Curvv.fuel_type())

###### Example -01 (above)

############################################################################################################

# class Car:

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

    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size

#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Battery"



# myHarrier = ElectricCar("Tata","Harrier.ev", "79kWh")
# # print(my_electric_car.__brand)   ##### Ye to nahi chalega as direct access is not allowed
# print(myHarrier.fuel_type())

# Curvv = Car("Tata","Curvv")
# Nexon = Car("Tata", "Nexon")
# print(Curvv.fuel_type())


# ##now how to access the total_car

# #####note that we can't take the access of total_car from an object , here's why
# print(Nexon.total_car)

# ###### Example -02 (above)
##############################################################################################################
# class Car:

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

    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size

#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Battery"



# myHarrier = ElectricCar("Tata","Harrier.ev", "79kWh")
# # print(my_electric_car.__brand)   ##### Ye to nahi chalega as direct access is not allowed
# print(myHarrier.fuel_type())

# Curvv = Car("Tata","Curvv")
# Nexon = Car("Tata", "Nexon")
# print(Curvv.fuel_type())


# ##now how to access the total_car

# #####note : Do we have to always have to use the object to access the totalCar

# test = Car("test", "test")
# print(test.total_car) #### yahan par 4 ho jaayega 

###### Example -03 (above)

################
#### Whenever we want to access these types of variables , then this is not the appropriate way for doing this
    ### to take the access of total car refer example -04
#############################################################################################################

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
        return "Petrol or Diesel"

    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_Size):
        super().__init__(brand,model)
        self.battery_size  = battery_Size

    def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
        return "Battery"



myHarrier = ElectricCar("Tata","Harrier.ev", "79kWh")
# print(my_electric_car.__brand)   ##### Ye to nahi chalega as direct access is not allowed
print(myHarrier.fuel_type())

Curvv = Car("Tata","Curvv")
Nexon = Car("Tata", "Nexon")
print(Curvv.fuel_type())


##now how to access the total_car
print(Car.total_car)  ##note that we can take direct access of that of variables from the class like this


####Example -04 
##########################################################################################




