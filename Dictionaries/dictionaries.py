# A dictionary is a mutable data type.
# A dictionary stores data in key-value pairs.
# A dictionary is also a container, which means it can hold other dictionaries.
# The value of a key-value pair can be any data type.


# a dictionary of people and their ages
ages = {"Salim": 45, "Zainab": 42, "Khalid": 17, "Hassana": 15}

print(ages)

# access a value by its key
print(ages["Salim"])

# delete a key-value pair
del ages["Zainab"]

print(ages)

# change a value by its key
ages["Salim"] = 46

# add a new key-value pair
ages["Muhammad"] = 20

print(ages)
