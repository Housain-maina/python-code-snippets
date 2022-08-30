
# Defining a Vehicle class
class Vehicle:

    # creating a constructor method and instantiating 3 instance variables
    def __init__(self, manufacturer, year, model):
        self.manufacturer = manufacturer    # instance variable
        self.year = year    # instance variable
        self.model = model    # instance variable

    # creaing a method
    def printDetails(self):
        print("Manufacturer: ", self.manufacturer)
        print("Year: ", self.year)
        print("model: ", self.model)


# creating an object of the Vehicle class
v1 = Vehicle("Honda", 2017, "DC")

# calling a method of the Vehcile class using the reference variable of the Vehicle object created
v1.printDetails()

print("")

# calling an instance variable of the Vehicle class using the reference variable of the Vehicle object created
print(v1.manufacturer)
