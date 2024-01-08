sez = []
file = open("koda.txt", "w")

note = [("A4", 440), ("B4", 494), ("C4", 262), ("D4", 294), ("E4", 330), ("F4", 349), ("G4", 392), ("CS4", 277), 
        ("FS4", 370), ("A5", 880), ("B5", 988), ("C5", 523), ("D5", 587), ("E5", 659), ("F5", 698), ("G5", 784), 
        ("CS5", 554), ("FS5", 740), ("GS5", 831), ("DS5", 622), ("GS4", 415) ]

r17 = 0
r16 = 0


for i in note:

    ime = i[0]
    freq = i[1]

    if 1000000/freq/8 > 255:
        r17 = 1000000/freq/16
        r16 = 8
    
    else:
        r17 = 1000000/freq/8
        r16 = 4
    

    sez.append(ime + ":")
    sez.append("")
    sez.append("    ldi r18, " + str(int(freq/10)))
    sez.append("    ldi r19, 7")
    sez.append("")
    sez.append("    loopanje" + ime + ":")
    sez.append("")
    sez.append("        ldi r17, " + str(int(r17)))
    sez.append("        ldi r16, " + str(r16))
    sez.append("        sbi DDRB, 5")
    sez.append("")
    sez.append("        delayon" + ime + ":")
    sez.append("            dec r17")
    sez.append("            brne delayon" + ime)
    sez.append("            ldi r17, " + str(int(r17)))
    sez.append("            dec r16")
    sez.append("            brne delayon" + ime)
    sez.append("")
    sez.append("        ldi r17, " + str(int(r17)))
    sez.append("        ldi r16, " + str(r16))
    sez.append("        cbi DDRB, 5")
    sez.append("")
    sez.append("        delayoff" + ime + ":")
    sez.append("            dec r17")
    sez.append("            brne delayoff" + ime)
    sez.append("            ldi r17, " + str(int(r17)))
    sez.append("            dec r16")
    sez.append("            brne delayoff" + ime)
    sez.append("")
    sez.append("    dec r18")
    sez.append("    brne loopanje" + ime)
    sez.append("    ldi r18, " + str(int(freq/10)))
    sez.append("    dec r19")
    sez.append("    brne loopanje" + ime)
    sez.append("")
    sez.append("    ldi r18, " + str(int(freq/10)))
    sez.append("")
    sez.append("    loopanje2" + ime + ":")
    sez.append("")
    sez.append("        ldi r17, " + str(int(r17)))
    sez.append("        ldi r16, " + str(r16))
    sez.append("        sbi DDRB, 5")
    sez.append("")
    sez.append("        delayon2" + ime + ":")
    sez.append("            dec r17")
    sez.append("            brne delayon2" + ime)
    sez.append("            ldi r17, " + str(int(r17)))
    sez.append("            dec r16")
    sez.append("            brne delayon2" + ime)
    sez.append("")
    sez.append("        ldi r17, " + str(int(r17)))
    sez.append("        ldi r16, " + str(r16))
    sez.append("        cbi DDRB, 5")
    sez.append("")
    sez.append("        delayoff2" + ime + ":")
    sez.append("            dec r17")
    sez.append("            brne delayoff2" + ime)
    sez.append("            ldi r17, " + str(int(r17)))
    sez.append("            dec r16")
    sez.append("            brne delayoff2" + ime)
    sez.append("")
    sez.append("    dec r18")
    sez.append("    brne loopanje2" + ime)
    sez.append("    ret")
    sez.append("")


file.write('\n'.join(sez))