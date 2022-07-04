numbers_a = [x for x in range(10)]
print(numbers_a)  # outputs a list of numbers from 0 to 9

numbers_b = [x * 2 for x in range(10)]
# outputs a list containing the multiplication of each number from 0 t0 9
print(numbers_b)

numbers_c = [x**2 for x in range(10)]
# outputs a list containing each number from 0 t0 9 raised to the power of 2
print(numbers_c)

numbers_d = [x for x in range(10) if x % 2 == 0]
print(numbers_d)  # outputs a list containing even numbers from 0 t0 9

numbers_e = [x for x in range(10) if x % 2 != 0]
print(numbers_e)  # outputs a list containing odd numbers from 0 t0 9
