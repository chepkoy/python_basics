# Strings are iterable
string = list('hello')
print(string)

# Splits by default breaks on white space

split =  "Hello there students"
print(split.split())

# Spliting on something

colors = "Red:Blue:Green"
print(colors.split(':'))

# Changing lists into strings

drinks = ['milk', 'soda','coffee']
print(', '.join(drinks))

#print("My favourite drinks are: " ', '.join(drinks))

print("My favourite drinks are: {}".format(', '.join(drinks)))