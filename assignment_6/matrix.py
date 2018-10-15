import random

def random_matrise(bredde, høyde):
    result = []
    for x in range(bredde):
        result.insert(len(result),[])
        for y in range(høyde):
            result[x].insert(0, random.randint(0, 10))
    return result

def print_matrise(matrise, navn):
    print(navn, "=[")
    for x in range(len(matrise)):
        print(matrise[x])
    print(']')

def matrise_addisjon(a, b):
    result = a
    if len(a) != len(b):
        print("Matrisene er ikke av samme dimensjon")
        return
    for x in range(len(a)):
        if len(a[x]) != len(b[x]):
            print("Matrisene er ikke av samme dimensjon")
            return
        for y in range(len(a[x])):
            result[x][y] = a[x][y] + b[x][y]
    return result

def main():
    A = random_matrise(4,3)
    print_matrise(A, 'A')
    B = random_matrise(3,4)
    print_matrise(B, 'B')
    C = random_matrise(3,4)
    print_matrise(C, 'C')
    D = matrise_addisjon(A,B)
    E = matrise_addisjon(B,C)
    print_matrise(E, 'B+C' )

main()