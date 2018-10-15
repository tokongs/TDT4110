import random
numbers = []
myGuess = [1, 2, 3, 4, 5, 6, 7]

def createList():
    numbers.clear()
    for x in reversed(range(1, 35)):
        numbers.insert(0, x)


def drawNumbers(tall, n):
    result = []
    for x in range(0, n):
        rand = random.randint(0, len(tall)-1)
        y = tall[rand]
        while tall in result and tall != 0:
            rand = random.randint(0, len(tall)-1)
            y = tall[rand]
        result.insert(0, y)
        tall[rand] = 0
        numbers[rand] = 0

    
    return result

def compList(liste1, liste2):
    like = 0
    for x in liste1 :
        if x in liste2:
            like += 1
    return like

def Winnings(like, tillegg):
    if like == 7:
        return 2749455
    elif like == 6 and tillegg >= 1:
        return 102110
    elif like == 6:
        return 3385
    elif like == 5:
        return 95
    elif like == 4 and tillegg >= 1:
        return 45
    else:
        return 0


def main():
    createList()
    lottotall = drawNumbers(numbers, 7)
    tilleggstall = drawNumbers(numbers, 3)
    createList()
    like = compList(lottotall, myGuess)
    like_tilleg = compList(tilleggstall, myGuess)
    return Winnings(like, like_tilleg) - 5

print(main())