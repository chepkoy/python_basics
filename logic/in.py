# In is used Containment or inclusion

# Checking for letters in words

letters = "cheeseshop"

print('cheese' in letters)

# Checking if values is in a list

list = ['cheeseshop']

print('cheeseshop' in list)

# using in with if

days_open = ['monday', 'tuesday', 'wednesday', 'thursday','friday']
today = "Saturday"
if today in days_open:
    print("Come in we are open")
else:
    print('We do not open on weekends')

# using the not

if today not in days_open:
    print("Sorry we are closed")