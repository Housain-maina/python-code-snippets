
class User:

    __person = True     # private variable, can only be accessed from within the class
    animal = False      # public variable can be accessed from within and outside the class
    

    def __init__(self, username, password):
        self.username = username        # public variable can be accessed from within and outside the class
        self.__password = password      # private variable, can only be accessed from within the class

    # public method can be accessed from within and outside the class
    def authenticate(self):
        if self.username == "username" and self.__password == "123":
            return "Autheticated"
        return "Invalid Authentication Credentials"

    # private method, can only be accessed from within the class
    def __get_password(self):
        return self.__password


user = User("username", "123")

# accessign a public method
print(user.authenticate())

# accessing a public variable
print(user.username)

