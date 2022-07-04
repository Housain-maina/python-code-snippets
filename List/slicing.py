list_a = [2, 3, 4, 5]
list_b = list_a

print(list_a)  # outputs [2, 3, 4, 5]
print(list_b)  # outputs [2, 3, 4, 5]

list_a[0] = 1

print(list_a)  # outputs [1, 3, 4, 5]
print(list_b)  # outputs [1, 3, 4, 5]

"""
list_b will always contain the same values as list_a because list_b is not copying the
content of list_a, rather it is copying the memory location of the content of list_a.
"""

"""
Slicing is used used to copy the content of a list so that changes to the original list 
will not affect the copied list
"""

list_1 = [10, 20, 30, 40, 50]
list_2 = list_1[:]  # copies the entire content of list_1 to list_2

print(list_1)  # outputs [10, 20, 30, 40, 50]
print(list_2)  # outputs [10, 20, 30, 40, 50]

list_1[0] = 11

print(list_1)  # outputs [11, 20, 30, 40, 50]
print(list_2)  # outputs [10, 20, 30, 40, 50]

list_3 = list_2[:2]  # copies the content of list_2 from the beginning to index 2-1

print(list_3)  # outputs [10, 20]

list_4 = list_2[1:3]  # copies the content of list_2 from the beginning to index 3-1

print(list_4)  # outputs [20, 30]

# You will get an empty list if the first number in the slice is greater than the second number
print(list_2[3:1])
