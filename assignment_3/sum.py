n = int(input("Skriv inn et heltall "))
result = 0
for x in range (0, n + 1):
    if(x % 2 == 0):
        result -= x**2
    elif(x % 2 != 0):
        result += x**2

print("Summen av tallserien er", result)

k = int(input("Skriv inn et nytt heltall "))
result = 0
it = 0
for x in range(0, n + 1):
    if(x % 2 == 0):
        result -= x**2
        if(result > k):
            result += x**2
            break
    elif(x % 2 != 0):
        result += x**2
        if(result > k):
            result -= x**2
            break
    it+=1

print("Summen av tallene før summen blir større en k er", result, ". Antall iterasjoner:", it)
    

