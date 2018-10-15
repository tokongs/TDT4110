from math import *
from random import *

for x in range (1, 6):
    for y in range(1, x+1):
        print(y, end=" ")
    print("\n", end ="")

for x in range(0, 5):
    print("# ", end="")
    for y in range(1,   x+1):
        print(" ", end="")
    print("#")


tall = int(input("Skriv inn et positvt heltall "))
orginal = tall
is_prime = True
for x in range(2, ceil(sqrt(tall))):
    if(tall % x == 0):
        is_prime = False
        break

factors = []
if(is_prime != True):
    for x in range(2, tall):
        exit_condition = False
        while exit_condition == False:
            if(tall % x == 0):
                factors.insert(len(factors) -1, x)
                print(x)
                tall /= x
            else:
                exit_condition = True
    print(orginal, "=", end=" ")
    for x in range(len(factors)):
        if(x != len(factors) - 1):
            print(factors[x], "*",end=" ")
        else:
            print(factors[x])
    print("")
else:
    print(tall, "Er et primtall")
        

cont = True
while cont == True:
    tall1 = randint(0, 9)
    tall2 = randint(0, 9)
    result = tall1*tall2
    for x in reversed(range(1, 4)):
        prompt = "Hva blir " + str(tall1) + "*" + str(tall2) + "? "
        answer = int(input(prompt))
        if(answer == result):
            print("Gratulerer, det er helt riktig")
            break
        else:
            print("Desverre ikke riktig. Du har", x-1, "forsøk igjen.")
    cont = int(input("Er det ønskelig med flere spørsmål? Skriv 1 for ja og 0 for nei "))        

