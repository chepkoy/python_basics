# Make a list to hold on to items

shopping_list = []
# Print instructins on how to use the app

print("What should we pick at the store? ")
print("Enter 'DONE' to stop adding items.")

while True:
    # Ask for new items
    new_item = input("> ")
    
    # Be able to quit the app
    if new_item == "DONE":
        break

    # Add new items to our list
    shopping_list.append(new_item)

# Print out the list
print("here is your shopping list: ")


for item in shopping_list:
    print(item)