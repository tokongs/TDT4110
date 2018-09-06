#a)
thing1 = input("Matvare 1: ").lower()
thing2 = input("Matvare 2: ").lower()

print("Sammenligner", thing1, "og", thing2)
if(thing1 == thing2):
    print("Dette er samme matvare")
else:
    print("Dette er to forskjellige matvarer")

name1 = input("Første navn: ")
name2 = input("Andre navn: ")

print("Under følger navnene i alfabetisk rekkefølge:")
if(name1 >= name1):
    print(name2)
    print(name1)
else:
    print(name1)
    print(name2)

#c)
if 'k' < 'b':
    print('k er mindre enn b')
else:
    print('k er større enn b')
  
  
#Kodesnutt 2:
ny = "New York"
la = "Los Angeles"
  
if ny < la:
    print(ny)
    print(la)
else:
    print(la)
    print(ny)
  
  
#Kodesnutt 3:
d1 = "DRuEr"
d2 = "drUer"
if d1.lower() < d2.lower():
    print(d1)
    print(d2)
else:
    print(d2.lower())