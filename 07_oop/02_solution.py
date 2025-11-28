class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    

my_car = Car("Toyota", "Fortuner")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())   ### here full_name is not a variable ,its not a attribute , we have added a function, so to run this we must have to write paranthesis also

my_new_car = Car("Tata","Harrier")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())

