

huge_list = list(range(0, 1000000))

# print(len(huge_list))

# print(huge_list)

# inserting at earlier indexes, makes this a
# costly operation as all the elements after that
# index needs to be shifted to new memory address.
huge_list.insert(2, 200)

print(huge_list[0:500])

