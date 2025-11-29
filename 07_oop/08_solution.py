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
    
#     @staticmethod                     ### To create the static method we simply use @staticmethod      
#     def general_description():
#         return "Cars are means of transport"

    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size

#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Battery"


# my_car = Car("Tata","Safari")
# my_car.model = "Sierra"
# Car("Tata", "Nexon")

# print(my_car.model)

#### Example-01 : In this we try to overwrite the model whether the model  can be overwrite or not
          ###Ans : The ans is Yes the Safari is written to sierra . and we have to prevent this

############################################################################################


## the first thing we have to do is  to stop anybody from accessing the model, to do that refer example-02

# class Car:

#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model     #### here __ add karte hi model ho gya inaccessible directly
#         Car.total_car += 1

#     def get_brand(self):
#         return self.__brand + "!"

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"
    
#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Petrol or Diesel"
    
#     @staticmethod                     ### To create the static method we simply use @staticmethod      
#     def general_description():
#         return "Cars are means of transport"

    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size

#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Battery"


# my_car = Car("Tata","Safari")
# my_car.model = "Sierra"
# Car("Tata", "Nexon")

# print(my_car.model)

####### Example -02  ::: in this example we just made the model inaccessible, but we don't only have to do this we are supposed to make it read only, for that refer example -03 

###########################################################################
#### to make the model readonly we can do that by making a method, and through this model , we can say that whether you can do readonly as well as can do some other task

# class Car:

#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model     #### here __ add karte hi model ho gya inaccessible directly
#         Car.total_car += 1

#     def get_brand(self):
#         return self.__brand + "!"

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"
    
#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Petrol or Diesel"
    
#     @staticmethod                     ### To create the static method we simply use @staticmethod      
#     def general_description():
#         return "Cars are means of transport"
    
#     def model(self):
#         return self.__model

    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size

#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Battery"


# my_car = Car("Tata","Safari")
# my_car.model = "Sierra"
# Car("Tata", "Nexon")

# print(my_car.model)


#### example -03 :
###############################################################################

## in the example -03 even though we have made  a method model so that we can make the model readonly but then also we can see that the Safari is changed to sierra 

# class Car:

#     total_car = 0

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model     #### here __ add karte hi model ho gya inaccessible directly
#         Car.total_car += 1

#     def get_brand(self):
#         return self.__brand + "!"

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"
    
#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Petrol or Diesel"
    
#     @staticmethod                     ### To create the static method we simply use @staticmethod      
#     def general_description():
#         return "Cars are means of transport"
    
#     @property                    ### ye ban gya hamara decorator
#     def model(self):
#         return self.__model

    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_Size):
#         super().__init__(brand,model)
#         self.battery_size  = battery_Size

#     def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
#         return "Battery"


# my_car = Car("Tata","Safari")
# Car("Tata", "Nexon")

# print(my_car.model())

###### Here we are getting a error 
#### example-04

########################################################################################
class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model     #### here __ add karte hi model ho gya inaccessible directly
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
        return "Petrol or Diesel"
    
    @staticmethod                     ### To create the static method we simply use @staticmethod      
    def general_description():
        return "Cars are means of transport"
    
    @property                    ### ye ban gya hamara decorator
    def model(self):
        return self.__model

    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_Size):
        super().__init__(brand,model)
        self.battery_size  = battery_Size

    def fuel_type(self): ###3 python mein context to dena hi padta hai , so we are writing the self
        return "Battery"


my_car = Car("Tata","Safari")
Car("Tata", "Nexon")

print(my_car.model)   #### actually the decorators has allowed to access that method model as property, so we can simply write my_car.model, and when we write like this we are getting the safari only


#### Example -04

#### Pointe to be notted
   ## 1.) whenever we use @property decorator ,that indicates that we want to do somthiing intentionally , that says that there is a property , which I want to hide , and can't be accessed by eceryone. and if any body wants to access , then they can do so through my method only
   ## 2.) Once our brand is set up during the constructor call , that can't be overwritten

 ## at any time we want that we don't want to change certain value or any value then in that case we must have to use @property decorator