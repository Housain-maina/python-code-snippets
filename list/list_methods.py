names = ["Hassan", "Umar", "Abbas", "Muhammad"]
print(names, end="\n\n")

# The append method adds an item to the end of a list.
# It takes one argument, which is the item to be added.
names.append("Abubakar")
print(names, end="\n\n")

# The insert method adds an item to a specific index of a list.
# It takes two arguments, the index to insert the item at and the item to be inserted.
names.insert(2, "Jabir")
print(names, end="\n\n")


numbers = [5, 3, 2, 8, 11]
numbers.sort()
print("sorted numbers: ", numbers)  # outputs [2, 3, 5, 8, 11]

numbers.sort(reverse=True)
print("reversed sorted numbers: ", numbers)  # outputs [11, 8, 5, 3, 2]
