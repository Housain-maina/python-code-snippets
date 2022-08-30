

# while loop is used to repeat a block of code until a condition is false
# this is useful for loops that don't know how many times they should run
# this while loop checks if you are hungry and if you are, it will print "Okay, here's a snack" until you are not hungry

hungry = input('Are you hungry? y/n ')

while hungry == 'y':
    print("Okay here's a snack")
    hungry = input('Are you still hungry? y/n ')

print("Okay, bye")
    