
class Person:
    def __init__(self, first_name, last_name, births=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birth = births

    def full_name(self):
        return self.first_name + " " + self.last_name

    # a method that can be implemented to have many forms
    def get_births(self):
        pass


class Man(Person):
    gender = "Male"

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    # overrides the parents class get_birth to have a different form
    def get_births(self):
        return super().full_name() + " is a man, therefore cannot give birth."


class Woman(Person):
    gender = "Female"

    def __init__(self, first_name, last_name, births=0):
        super().__init__(first_name, last_name, births)

    # overrides the parents class get_birth to have a different form
    def get_births(self):
        return super().full_name() + " has given birth " + str(self.birth) + " times."


man = Man("Hussaini", "Usman")
print(man.get_births())

woman = Woman("Khadija", "Musa", 5)
print(woman.get_births())
