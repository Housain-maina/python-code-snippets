# A list is a collection of items that can be of different data types. Its numbering starts from 0.
numbers = [5, 6, 7, 8, 9]  # list of integers

names = ["Hussaini", "Maina", "Usman", "Khalid"]  # list of strings

floating_numbers = [1.23, 2.34, 3.45, 4.56]  # list of floats

mixed_list = [5, "Ali", 1.23, "Mustapha"]  # list of mixed data types

list_of_lists = [numbers, names, floating_numbers, mixed_list]  # list of lists

print(numbers, names, floating_numbers, mixed_list, list_of_lists, sep="\n\n")

# The length of a list is the sum of the total number of items in the list
print(len(numbers))  # prints 5 since there are 5 items in the list
