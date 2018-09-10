tid = int(input("Hvor mange minutt har kaken stått i ovnen? "))
if(tid >= 50):
    print("Kaken kan tas ut av ovnen.")
print("Tips til servering: vaniljeis.")

epler = int(input("Hvor mange epler har du? "))
barn = int(input("Hvor mange barn passer du? "))
if(barn != 0):
    print("Da blir det", epler // barn, "epler til hvert barn")
    print("og", epler % barn, "epler til overs til deg selv.")
print("Takk for i dag!")

age = int(input("Skriv inn din alder: "))
if(age >= 18):
    print("Du kan stemme:)")
else:
    print("Du kan ikke stemme ennå")

age = int(input("Skriv inn din alder: "))

if(age >= 18):
    print("Du kan stemme både ved lokalvalg og Stortingsvalg")
elif( age >= 16):
    print("Du kan stemme ved lokalvalg, men ikke ved Stortingsvalg")
else:
    print("Du kan ikke stemme ennå")

age = int(input("Din alder: "))

pris = 0
if(age >= 3 and age <= 11):
    pris = 30
elif(age >= 12 and age <= 25):
    pris = 50
elif(age >= 26 and age <= 66):
    pris = 80
elif(age >= 67):
    pris = 40

print("Billettpris:", pris, "kr")
