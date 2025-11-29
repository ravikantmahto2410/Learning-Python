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

######Example - 01 : this code will print output as Car are means of transport but we dont want ki isss tarah se ho
#############################################################################################

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


#### Example -02
######################################################################################################
#### to create the static method in python we simply write @ see below code for bette understanding

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
    
    @staticmethod                     ### To create the static method we simply use @staticmethod      
    def general_description():
        return "Cars are means of transport"

    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_Size):
        super().__init__(brand,model)
        self.battery_size  = battery_Size

    def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
        return "Battery"


Curvv = Car("Tata","Curvv")
Car("Tata", "Nexon")

print(Car.general_description())


###Example -03 : this is the example  where static method is actally working 


#### What are @staticmethod: 
   ##ans : inko bola jataaa hai decorators. In python the decorators are very interesting things. because they enhance the functionality of your method
          