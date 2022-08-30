try:
    number = int(input("Enter a natural number: "))
    print("The reciprocal of ", number, " is ", 1 / number)

except ValueError:
    print("The value you entered is not a natural number.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except:
    print("An unknown error occurred.")


try:
    number = int(input("Enter a natural number: "))
    print("The reciprocal of ", number, " is ", 1 / number)

except (ValueError, ZeroDivisionError):
    print("The value you entered is not a natural number or the number is zero.")
