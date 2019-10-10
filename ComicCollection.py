# Declare variables
collection = []
choice = " "


# Create a function that prints menu for user
def menu():
    print("\t\t*************Comic Collection**************"
          + "\n\t\t*1. Look at comics currently in collection*\n\t\t*2. Add new comic\t\t\t  *"
            "\n\t\t*3. Remove comic\t\t\t  *\n\t\t*4. Remove most recent comic before sort  *"
            "\n\t\t*5. Sort collection alphabetically A-Z\t  *\n\t\t*6. Save collection to file\t\t  *"
            "\n\t\t*7. Save to file\t\t\t  *\n\t\t*8. Read file\t\t\t\t  *"
            "\n\t\t*******************************************")


# Create while loop that is terminated once user enters q
while choice != "q":

    # Print menu
    menu()
    # Save users choice
    choice = input("\t\t\tWhat would you like to do? ")
    # Create while loop that is terminated once user enters q

    # Make if else if state to handle users choice
    if choice == "1":
        print("\nCurrent collection consists of: ")
        for x in collection:
            print("\t" + x)
            print()
    elif choice == "2":
        new_comic = input("\nWhat is the name of the new comic? ")
        collection.append(new_comic.title())   # .append() adds comic to end of list,
                                                    # .capitalize() capitalizes first character
        print("Comic successfully added!\n")
    elif choice == "3":
        comic_being_removed = input("\nWhat comic would you like to remove? ")
        if collection.count(comic_being_removed) != 0:
            collection.remove(comic_being_removed)
            print("Comic successfully removed.\n")
        else:
            print("You do not own that comic.\n")
    elif choice == "4":
        collection.pop(-1)
        print("\nMost recent comic successfully removed.\n")
    elif choice == "5":
        collection.sort()
        print("\nCOLLECTION SORTED!\n")
    elif choice == "6":
        # Create a file that saves collection, if file exists overwrite
        file_name = input("What would you like to name the file?\n")
        collection_file = open(file_name, 'w')
        f.close()
        print("File " + file_name + " successfully created.\n")
    elif choice == "7":
        # Open existing file and append new content to it
        file_to_open = input("What file would you like to open?\n")
        with open(file_to_open, 'a') as f:
            for item in collection:
                f.write("%s\n" % item)
        print("\nNew content appended.\n")
    elif choice == "8":
        file_read = input("What file would you like read?\n")
        f = open(file_read, "r")
        print(f.read())
    elif choice == "q":
        print("\nGoodbye.")
    else:
        print("\nInvalid choice. Choose again.\n")
