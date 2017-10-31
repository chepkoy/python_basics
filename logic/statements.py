# Working with if else and elif statements

if 5 > 2:
    print("Well, Yeah 5 is greater than 2")

age = 34 * 365

if age > 10000:
    print("You are over 10,000 days old")

# using else

age = 5000
if age > 10000:
    print("You are over 10,000 years old")

else:
    print("Keep going you will get there")


# using the elif

age = 9000

if age > 20000:
    print("Time to retire")

elif age > 10000:
    print("Lots of time left")

else:
    print("Keep going you will get there")


age = 22000

if not age > 30000:
    print("No present")

    