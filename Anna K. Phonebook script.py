def phonefunction():
    action = ""
    while action != "exit":
        action = input("what would you like to do?")
        if action == "add":
            add()
        elif action == "delete":
            delete()
        elif action == "update":
            update()
        elif action == "search":
            search()
        elif action == "exit":
            print("good bye.")
            pass
        else:
            print("Please write 'add' , 'update' , 'delete' , 'search' or 'exit'")        

def add():
    phonebook = open("phonebook.txt","a")
    additions=((input("first name?")) + " " + (input("last name?")) + ", " + (input("phone number")))
    moreadd = input("would you like to add another phone number?")
    while moreadd == "yes":
        additions= additions + (", " + (input("add a phone number")))
        moreadd = input("would you like to add another phone number?")
    if moreadd == "no":
        pass
    else:
        print("type 'yes' to add. returning to main menu.")
    phonebooklist = open("phonebook.txt", "r")
    num_added = len((phonebooklist).readlines(  ))  #if there are existing lines 
    num_added += 1
    phonebook.write((str(num_added)) + ". " + additions + "\n") 
    phonebook.close()

def search():
    with open("phonebook.txt", "r") as f:
        searchlines = f.readlines()
    notfound=True
    search = input("search by name or number")
    for line in searchlines:    
        if search in line:
            print(line)
            notfound=False
    if notfound:
        print("entry not found")
    
def delete():
    with open("phonebook.txt", "r") as f:
        updatelines = f.readlines()
    updatesearch = input("search by name or number to delete")
    any_found = False
    for y,line in enumerate(updatelines):   
        if updatesearch in line:
            any_found = True
            print(line)
            confirmdelete = input("would you like to delete this entry?")
            if confirmdelete == "yes":
                updatelines[y] = "delete"
            elif confirmdelete == "no":
                pass
            else:
                print("type 'yes' or 'no'")
    if not any_found:
       print("entry not found")
    with open("phonebook.txt", "w") as f:
        x=1
        for line in updatelines:
            if line != "delete":
                f.write((str(x) +'. '+ line.split(' ',1)[1]))
                x+=1
def update():
    with open("phonebook.txt", "r") as f:
        updatelines = f.readlines()
    updatesearch = input("search by name or number to update")
    any_found = False
    for y,line in enumerate(updatelines):   
        if updatesearch in line:
            any_found = True
            print(line)
            confirmupdate = input("would you like to update this entry?")
            if confirmupdate == "yes":
                newline = ((input("first name?")) + " " + (input("last name?")) + ", " + (input("phone number")))           
                moreadd = input("would you like to add another phone number?")
                while moreadd == "yes":
                    newline += (", " + (input("add a phone number")))
                    moreadd = input("would you like to add another phone number?")
                    if moreadd == "no":
                        pass
                    else:
                        print("type 'yes' to add. returning to main menu.")
                updatelines[y] = str(y+1) +". " + newline + "\n" 
            elif confirmupdate == "no":
                pass
            else:
                print("type 'yes' or 'no'")
    if not any_found:
       print("entry not found")
    
    with open("phonebook.txt", "w") as f:
        for line in updatelines:
            f.write(line)

phonefunction()
