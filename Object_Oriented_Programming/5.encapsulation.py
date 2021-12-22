

class User:
    """
    a class that encapsulates both the variables the methods to manipulate the
    variables in a single unit whilst hiding the variables from the user
    """

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def login(self, username, password):

        if (self.__username == username) and (self.__password == password):
            return "Access Granted"
        else:
            return "Invalid Credentials"


user1 = User("Hussaini", "1234")
print(user1.login("Hussaini", "1234"))

