
days = int(input("Dager til du skal reise? "))

#a)

if(days >= 14):
    print("Du kan få minipris til:", 199, ",-")
else:
    print("For sent for minipris; fullpris", 499, ",-")


#b)
if(days >= 14):
    print("Minipris", 199, ",- kan ikke refunderes/endres")
    want = input("Ønskes dette (J/N)?")
    if(want == "J" or want == "j"):
        print("Takk for pengene, god reise!")
    else:
        print("Da tilbyr vi fullpris:", 440, ",-" )
else:
    print("For sent for minipris; fullpris", 499, ",-")

#c)
full = False
if(days >= 14):
    print("Minipris", 199, ",- kan ikke refunderes/endres")
    want = input("Ønskes dette (J/n)?")
    if(want == "J" or want == "j"):
        print("Takk for pengene, god reise!")
    else:
        full = True
        
else:
    full = True

if(full):
    pris = 440
    age = int(input("Skriv inn din alder: "))
    if(age < 16):
        pris = pris * 0.5
    elif(age >= 60):
        pris = pris * 0.75
    else:
     discount = input("Er du militær i uniform eller student (J/n)")
     if(discount == "J" or discount == "j"):
         pris = pris * 0.75
    print("Prisen på biletten blir:", pris, ",-")
    