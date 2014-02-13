# -*- coding: utf8 -*- 
import basic_encryption
import crypt

def print_menu():
    print ''
    print '1. Insert values'
    print '2. Save values to file'
    print '3. Load values from file'
    print '4. Encrypt file'
    print '5. Decrypt file'
    print '6. Show content in file'
    print '7. Print menu'
    print '8. Quit'
    print '-' *30

def menu():
    print_menu()
    choice = 0
    in_array = []
    filename = 'content.csv'
    while choice != 8:
        try:
            choice = int(input("Please select an option > "))
            print ""
        except (ValueError, NameError, SyntaxError, TypeError):
            print 'Please select a valid option'
        if choice == 1:
            in_array = basic_encryption.insert()
        elif choice == 2:
            basic_encryption.save(filename, in_array)
        elif choice == 3:
            in_array = basic_encryption.read(filename)
        elif choice == 4:
            key = raw_input('---> Select passphrase > ')
            crypt.encrypt_file(key, filename, filename + '.enc') 
        elif choice == 5:
            tries = 0
            while tries < 3:
                key = (raw_input('---> Decryption key > '))
                if crypt.decrypt_file(key, filename + '.enc', filename+'.decrypted'):
                    break
                tries += 1
                if tries == 3:
                    print "Too many tries"
            tries = 0
        elif choice == 6:
            filetoread = (raw_input('---> Filename > '))
            try:
                with open(filetoread, 'r') as f:
                    print ' '.join(f.readlines())
            except IOError:
                print "Invalid file name"
        elif choice == 7:
            print_menu()
        elif choice > 8:
            print 'Please select a valid option'
menu()