phone_book = {}
choice = 0


print "===Electronic Phone Book==="
print "==========================="
print "1. Look up a phone number"
print "2. Set an entry"
print "3. Delete an entry"
print "4. List all entries"
print "5. Search by phone number"
print "6. Quit"


while (choice <7 ):    
    choice = input("What do you want to do (1-5)?")

    if(choice ==1):
        select_name = raw_input("Name: ")
        if select_name in phone_book:
            print "Found entry for " + select_name +": " +phone_book[select_name]
        else:
            print "No one by that name here."

    if(choice == 2):
        name = raw_input("Name: ")
        phone_number = str(input("Phone Number: "))
        phone_book[name] = phone_number
        print "Entry saved for %s" % name

    if(choice ==3):
        del_Name = raw_input("Who would you like to delete: ")
        if del_Name in phone_book.keys():
            del phone_book[del_Name]
            print "%s has been removed" % del_Name

    if(choice ==4):
            print phone_book

    if (choice == 5):
        select_number = str(raw_input("Phone Number: "))
        if select_number in phone_book.values():
            print "Found entry for " + select_number +": " + phone_book.keys()[phone_book.values().index(select_number)]
        else:
            print "No one by with that number here."

    if (choice == 6):
        print "Later Gator!"
        break

    

  


                
