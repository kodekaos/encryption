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

def read():
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
        
i = raw_input("Input, please >")
save(i)
print read()
    