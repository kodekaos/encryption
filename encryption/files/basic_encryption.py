# -*- coding: utf8 -*- 
import os
def insert():
    array = []
    row = []
    col = 0
    i = ""
    print "Avslutt med !!"
    while i != "!!":
        i = raw_input("Input, please >")
        if i == "!!":               # Sjekk om input er !!, så den ikke tas med som input
            break
        if col < 2:
            col += 1
            row.append(i)       # legg til inputelementet i rad-elementet dersom det ikke er fullt
        else:
            row.append(i)
            array.append(row)   # Legg raden til i listen når raden er full
            row = []            # tøm rad-listen
            col = 0             # Resett kolonnetelleren
    array.append(row)              # Legg til siste rad i listen etter at !! er sendt
    return array

def save(out_file, content):
    with open(out_file, 'w') as f:
        f.writelines(";separator;".join(map(str,i))+'\n' % i for i in content)
        print 'Content saved successfully to', ''.join(os.path.splitext(out_file))
    # Loop tar ut hver liste i lista til variablen i
    # Variablen i blir konvertert til string object av map(str, i)
    # hvert strengelement i variabelen i blir slått sammen til en string med %separator% mellom elementene
    # Hver liste i content skrives til fil og avsluttes med \n

def read(in_file):
    with open(in_file, "r") as f:
        array = [i.rstrip().split(";separator;") for i in f.readlines()]
        print 'Content loaded from', ''.join(os.path.splitext(in_file))
        return array
            # Hver linje i fila hentes inn som elementet i
            # i blir strippet for \n med .rstrip.
            # Hvert element i linjen blir separert av .split(%separator%)
            # i blir laget som et listeelement i listen array

def print_columns(content):
    col_width = max(len(item) for row in content for item in row) + 1
    # Finner lengden på det lengste elementet i lista, legg til 1 som buffer.
    total_width = (col_width *3) +5
    print ""
    print "Skriver ut innhold i kolonner:"
    print "-" * total_width
    for row in content:
        print "".join(item.ljust(col_width) + "| " for item in row)
    print "-" * total_width

def sort_content(content):
        print ""
        print "Skriver ut alt innhold sortert:"
        combined = sorted(item for row in content for item in row)
        # Tar ut alle elementene i hver liste og legger det til i en ny liste sortert
        print "\n".join(word for word in combined)
        # Slår sammen elementene i listen med newline mellom hvert element

