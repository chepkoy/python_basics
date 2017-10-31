import random

# Generate a number between 1 and 10
secret_num = random.randint(1, 10)

while True:
    # Get a number guess from the player
    guess = int(input("Guess a number between 1 and 10: "))

    # Compare guess to secret number
    if guess == secret_num:
        print("You got it! My number was {}".format(secret_num))
        break
    else:
        print("That's not it")
    # print hit or miss
