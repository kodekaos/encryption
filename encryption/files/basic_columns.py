def save(i):
    a = i.split()
    try:
        f = open("storage.csv", "w")
        try:
            for word in a:
                f.write("%s," % word)
        finally:
            f.close()
    except IOError:
        print "IO-Error"
        pass

def read():
    try:
        f = open("storage.csv", "r")
        try:
            for line in f:
                a = line.split(",")
            return a
        finally:
            f.close()
    except IOError:
        pass
        
i = raw_input("Input, please >")
save(i)
a = read()
for word in a:
    print "%s" % word,
    