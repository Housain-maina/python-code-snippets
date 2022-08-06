def welcome_user(username):  # with 1 parameter
    print("Hello", username)


welcome_user("Hussaini")
welcome_user("Sadiq")


def sum_numbers(num_1, num_2, num_3):  # with multiple parameters
    print(num_1 + num_2 + num_3)


sum_numbers(10, 20, 30.5)


def is_year_leap(year):  # returns true if year is leap year
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False


def days_in_month(year, month):  # returns number of days in a month
    february = 29 if is_year_leap(year) else 28
    month_and_days = {
        "1": 31,
        "2": february,
        "3": 31,
        "4": 30,
        "5": 31,
        "6": 30,
        "7": 31,
        "8": 31,
        "9": 30,
        "10": 31,
        "11": 30,
        "12": 31,
    }
    return month_and_days[str(month)]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
