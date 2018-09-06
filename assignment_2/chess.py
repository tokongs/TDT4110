translation = {}

translation["a"] = 1
translation["b"] = 2
translation["c"] = 3
translation["d"] = 4
translation["e"] = 5
translation["f"] = 6
translation["g"] = 7
translation["h"] = 8

position = input("Posisjon: ")
if(translation[position[0]]-1 % 2 == 0):
    if(int(position[1]) % 2 == 0):
        print("white")
    else:
        print("black")
else:
    if(int(position[1]) % 2 == 0):
       print("black")
    else:
        print("white")

 

