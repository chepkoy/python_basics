# Have a help command
# Have a show command
# Make a list to hold on to items

shopping_list = []

def show_help():
    # Print instructions on how to use the app
    print("What should we pick at the store? ")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this Help.
Enter 'SHOW' to see your current list.
""")
def show_list():
    # Print out the list
    print("here is your shopping list: ")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # Add new items to our list
    shopping_list.append(new_item)
    print("Added {}. list now has {} items. ".format(new_item, len(shopping_list)))



show_help()

while True:
    # Ask for new items
    new_item = input("> ")

    # Be able to quit the app
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()