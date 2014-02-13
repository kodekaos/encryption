import json


def save(i):
    try:
        fout = open("storage.json", "w")
        try:
            json.dump(i,fout)
        finally:
            fout.close()
    except IOError:
        print "Couldn't open file %s for writing" % fout.name
        pass

def load():
    try:
        fin = open("storage.json", "r")
        try:
            jsonObj = json.load(fin)
            return jsonObj
        finally:
            fin.close()
    except IOError:
        print "Couldn't open file %s for reading" % fin.name
        pass
def printmenu():
    print ""
    print "1. Print menu"
    print "2. Display current values"
    print "3. Add new value"
    print "4. Remove value"
    print "5. Load values from file"
    print "6. Save values to file"
    print "7. Quit"
    print "-"*30

def menu():
    choice = 0
    values = []
    printmenu()
    while choice != 7:
            try:
                choice = int(input("Please select an option > "))
                print ""
            except (ValueError, NameError, SyntaxError, TypeError):
                print "Please selct a valid number"    
            if choice == 1:
                printmenu()
            elif choice == 2:
                counter = 0
                print "Current content:"
                for value in values:
                    counter += 1
                    print "%s.\t%s" % (counter, value)
            elif choice == 3:
                values.append(raw_input("Input > "))
            elif choice == 4:
                try:
                    delete = int(input("Enter item to delete > ")) -1
                    if delete <= len(values):
                        print "Deleting %s" % values[delete]
                        values.pop(delete)
                    else:
                        print "Item does not exist"
                except (NameError, SyntaxError, TypeError):
                    print "Please selct a valid number"    
            elif choice == 5:
                print "Loading values from file..."
                values = load()
            elif choice == 6:
                print "Saving values to file..."
                save(values)
            elif choice > 7:
                print "Please select a valid option"
    print "Tata!"

menu()