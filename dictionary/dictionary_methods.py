# a dictionary  of people and their last names
last_names = {"Mike": "Smith", "John": "Doe", "Jane": "Doe"}

# get all the keys in the dictionary
print(last_names.keys())

# get all the values in the dictionary
print(last_names.values())

# get all the key-value pairs as tuples
for first_name, last_name in last_names.items():
    print(first_name, " -> ", last_name)

# add a new key-value pair to the dictionary
last_names.update({"Ned": "Stark"})

print(last_names)

""" remove last item from the dictionary. before python 3.6.7, 
this method removes a random item from a dictionary. """
last_names.popitem()

print(last_names)
