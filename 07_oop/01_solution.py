# class Car:
#     brand = None
#     model = None

# ### Class ban gaya

# my_Car = Car()
# print(my_Car)



##### Class Banane ka best tarika

# class Car:
#     def __init__(userbrand, usermodel):
#         brand = userbrand
#         model = usermodel


# my_car = Car("Toyota", "Fortuner")
# print(my_car.brand)   ### my_car.brand attribute ko access karne ka tarika hai



##### Abhi bhi ek problem hai 
# class Car:
#     def __init__(self,brand, model):
#         self.brand = brand      ### self.brand means class ke ander ke variable and the only brand that is written at the very right hand side is parameter  jo user nae diye hai ab ho object bana raha tha Car class se
#         self.model = model


# my_car = Car("Toyota", "Fortuner")
# print(my_car.brand)   ### my_car.brand attribute ko access karne ka tarika hai
# print(my_car.model)

## abhi tak my_car aur Car class ka koi linkage nhi hai abhi tak, dono abhi baat nahin kar paa rahe , to establish the connection between these two 
    # we use a special keyword self . As soon as we write self , it means jisne bhi call kiya

    ## after writing the self keyword , whenever we want to access these two varibales brand and model , that we can do so by writing .(dot) after self like this-> self. 



#########yahan tak  to apni aa gayi hai

####Example - 02 :

class Car:
    def __init__(self,brand, model):
        self.brand = brand      ### self.brand means class ke ander ke variable and the only brand that is written at the very right hand side is parameter  jo user nae diye hai jab ho object bana raha tha Car class se
        self.model = model


my_car = Car("Toyota", "Fortuner")
print(my_car.brand)   ### my_car.brand attribute ko access karne ka tarika hai
print(my_car.model)

my_new_car = Car("Tata Motors", "Harrier")
print(my_new_car.brand)
print(my_new_car.model)

    

####Note __init__ , this is also called as constructor, 


