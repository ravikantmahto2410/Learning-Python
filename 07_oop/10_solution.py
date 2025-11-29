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



class Battery:
    def battery_info(self):
        return " This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass

my_tata_ev = ElectricCarTwo("Tata", "Curvv.ev")
print(my_tata_ev.battery_info())
print(my_tata_ev.engine_info())

