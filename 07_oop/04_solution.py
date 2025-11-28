# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
#     def get_brand(self):
#         return self.brand + "!"
    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size



# my_electric_car = ElectricCar("Tata","Harrier.ev", "79kWh")
# print(my_electric_car.brand)
# print(my_electric_car.get_brand())


##### Till now the brand is easily accessible as previously we used to access
############################################################################################################
#####Now we want whenever we want to acces the car brand we can access using the getbrand method only
# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.__brand + "!"

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size



# my_electric_car = ElectricCar("Tata","Harrier.ev", "79kWh")
# print(my_electric_car.__brand)
# print(my_electric_car.get_brand())


##### The moment we put two underscore just behind the any variable then that variable becomes private,  private means , we can access that variable inside the class only , but if agar koi object bana to object uss private ko access nahi kar payega
     ## and if we want that log usko access kare to humein methods banane padenge like  get_brand 





# example  : 03
# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.__brand + "!"

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size



# my_electric_car = ElectricCar("Tata","Harrier.ev", "79kWh")
# # print(my_electric_car.__brand)   ##### Ye to nahi chalega as direct access is not allowed
# print(my_electric_car.get_brand())


##### The moment we put two underscore just behind the any variable then that variable becomes private,  private means , we can access that variable inside the class only , but if agar koi object bana to object uss private ko access nahi kar payega
     ## and if we want that log usko access kare to humein methods banane padenge like  get_brand




##### What will happen if we write chai_brand insteas of get_brand
# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def chai_brand(self):
#         return self.__brand + "!"

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    
    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size



# my_electric_car = ElectricCar("Tata","Harrier.ev", "79kWh")
# # print(my_electric_car.__brand)   ##### Ye to nahi chalega as direct access is not allowed
# print(my_electric_car.chai_brand())

##### COnclusion : chai_brand likhne se bhi kaam ho rha but aisa karna nahi chahiye , because we are breaking convention for getter get and for setter set


##### Hw: Learn setter