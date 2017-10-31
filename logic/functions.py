# Functions syntax

def hows_the_parrot():
    print("He is okay and singing")
hows_the_parrot()

# Functions with arguments

def lumberjack(name):
    if name.lower() == 'allan':
        print("Allan is a lumber and he is OK!")
    else:
        print("{} sleeps all night and {} works all day!".format(name, name))
lumberjack("Kevin")

# Working with multiple arguments

def lumberjack(name, pronoun):
        print("{} is a lumberjack and {} Ok!".format(name, pronoun))

lumberjack("Kevin","He's")
lumberjack("Kevin","He's")
lumberjack("Naomi","She's")

# Using return in functions

def average(num1, num2):
    return (num1 + num2) / 2

avg = average(2,14)

print(avg)