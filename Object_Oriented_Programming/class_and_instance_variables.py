
from abc import abstractmethod


class Male:

    gender = "Male"     # class variable

    def __init__(self, age, weight):
        self.age = age      # instance variable
        self.weigth = weight      # instance variable


male = Male(19, 30)

print(male.age)     # calling an instance variable

print(Male.gender)      # calling a class variable
