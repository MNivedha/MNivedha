#6. Write a Python program to get the difference between the two lists.
list_1 = [5, 10, 15, 20, 25, 30]
list_2 = [10, 20, 30, 40, 50, 60]

set_difference = set(list_1).symmetric_difference(set(list_2))
list_difference = list(set_difference)

print(list_difference)