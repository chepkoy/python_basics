# Creating a list

my_list = [1, 2, 3]
print(my_list)

# Cant do addition of a list with something that isnt a list

error_list = [4, 7, 0]
#error_list + 3
print(error_list)

# Adding a list onto a list
adding_list = [1, 2, 3, 4]
adding_list = adding_list + [5, 6]
print(adding_list)

# You cant use division and subtraction on list but we can do multiplication

multiply_list = [1,2,3,4,5]
multiply_list = multiply_list * 6
print(multiply_list)

# Adding a single item into a list

appending_list = [1,2,3,4,5]
appending_list.append(6)
print(appending_list)

# Adding multiple items onto a list

extending_list = [1,2,3,4]
extending_list.extend([5,6,7])
print(extending_list)

# Removing items from a list

list_in_list = [1,2,3,4,[5,6]]
print(list_in_list)
list_in_list.remove([5,6])
print(list_in_list)


