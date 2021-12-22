
class Vehicle:

    # parent class
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer

    def get_vehicle_details(self):
        return self.name + " was manufactured by " + self.manufacturer


class Car(Vehicle):

    # child class (Car) inherits all the public variables and methods of the parent class (Vehicle)
    def __init__(self, name, manufacturer, car_type):
        super().__init__(name, manufacturer)        # super() function used to access the instance of the parent class
        self.car_type = car_type

    def get_car_details(self):
        return super().get_vehicle_details() + " and is a " + self.car_type


car1 = Car("DC", "Honda", "Sedan")
print(car1.get_car_details())
