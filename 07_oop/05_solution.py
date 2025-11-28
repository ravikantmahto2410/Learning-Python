class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

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



my_electric_car = ElectricCar("Tata","Harrier.ev", "79kWh")
# print(my_electric_car.__brand)   ##### Ye to nahi chalega as direct access is not allowed
print(my_electric_car.fuel_type())

Curvv = Car("Tata","Curvv")
print(Curvv.fuel_type())


###### Polymorphism means ek hi method hai , lekin do anek room le sakte hai
