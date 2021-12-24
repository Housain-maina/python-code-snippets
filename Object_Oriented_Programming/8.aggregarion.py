

class Class:
    def __init__(self, name, teacher, no_students=0):
        self.name = name.upper()
        self.teacher = teacher.capitalize()
        self.no_students = no_students

    def get_info(self):
        return self.name + " has " + str(self.no_students) + " students and " + self.teacher + " is the class teacher."


class Student:
    """
    the student_class attribute accepts a class instance,
    therefore deleting the Student class instance will not have any effect on the class instance passed to it.
    """
    def __init__(self, full_name, student_class):
        self.full_name = full_name
        self.student_class = student_class

    def student_info(self):
        return self.full_name + " is in " + self.student_class.name

    def class_info(self):
        return self.student_class.get_info()


student_class1 = Class("jss1", "Muhammad Sani", 20)

student1 = Student("Hussaini Maina Usman", student_class1)
print(student1.class_info())
print(student1.student_info())
