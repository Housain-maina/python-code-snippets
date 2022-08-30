def factorial(number):

    if number < 1:
        return None

    total = 1

    for i in range(1, number + 1):
        total *= i
    return total


for n in range(1, 10):
    print(n, " -> ", factorial(n))
