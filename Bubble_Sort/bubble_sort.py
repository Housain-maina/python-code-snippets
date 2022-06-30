import random

my_list = [i + random.randint(1, 10) for i in range(100)]
swapped = True
swapped_times = 0

print('my unsorted list: ', my_list)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            swapped = True
            swapped_times += 1

print('my sorted list: ', my_list)
print("{} swaps made.".format(swapped_times))
