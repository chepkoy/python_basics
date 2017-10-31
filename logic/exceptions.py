# Working with exceptions in python

try:
    number = int(input("Give me a number: "))
except ValueError:
    print("Thats not a number ")

else:
    print("Hi" * number)