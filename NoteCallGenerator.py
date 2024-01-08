sez = []
c = 1
file = open("NoteCalls.txt", "w")
note=""
string = str(input("Input string here: "))

for i in string:

    if i == "-":
        for i in range(int(16/int(string[c])*1.5)):
                sez.append("call " + note)
        note = ""

    elif i.isdigit() == True and string[c].isdigit()==True and string[c] != "6" or string[c]=="-":
        note += i

    elif i.isdigit() == True and string[c].isdigit()==True and string[c] == "6":
        
        sez.append("call " + note)
        note = ""

    elif i.isdigit() == True and string[c].isdigit()!=True and string[c] != "-" and note != "":    
        
            for i in range(int(16/int(i))):
                sez.append("call " + note)
            note = ""
    elif i.isdigit() != True:
        note += i
    
    c += 1
    if c == len(string):
        c = 0

file.write('\n'.join(sez))