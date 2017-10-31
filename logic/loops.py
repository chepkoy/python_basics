# For loops

greetings = ['Hello', 'how', 'are', 'you']

for word in greetings:
    print(word)

# For strings
letters ="abcdefghijklmnopqrstuvwxyz"

for letter in letters:
    print(letter.upper())

# combining with conditionals

numbers = [0,1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    if num % 2 ==0:
        print(num)

# While loops

start = 10

while start:
    print(start)
    start -= 1



# Loops with conditions

names = ['allan','naomi','kevin','QUIT','brian']

for name in names:
    if name == 'QUIT':
        break
    print(name)


# Continue

for name in names:
    if name == 'QUIT':
        continue
    print(name)