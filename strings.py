# put in between single and double quotes

first_name = 'allan'
last_name = "chepkoy"
print(first_name)
print(last_name)

#Forgeting a string throws an error

# school = 'kitale"

# Handling apostrophees

sentance = "He's right"
print(sentance)

#Ignoring and escaping a sequence

second_sentance = "He\'s right again"
print(second_sentance)

#Using multiple lines with  tripple quotes

long_string = """ Here is the first paragraph
here comes the second

snd the third after a tab"""

print(long_string)

# Creating strings from the str function

market_size = str(750000)
print(market_size)

# Confirming the type of the converted  market size
print(type(market_size))

# Making strings from other strings

greeting_one = "Hello "
greeting_two = 'There'
combined_greeting = greeting_one + greeting_two
print(combined_greeting)

# Using place holders inside strings

message = "Hey we have {} {} using the site right now"
print(message.format(5, "People"))

