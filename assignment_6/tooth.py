mynter = [20, 10, 5, 1]

teeth = [95,103,71,99,114,64,95,53,97,114,109,11,2,21,45,2,26,81,54,14,118,108,117,27,115,43,70,58,107]
result = []
for tooth in teeth:
    twenty = 0
    ten = 0
    five = 0
    one = 0
    while tooth > 0:
        if tooth >= 20:
            tooth -= 20
            twenty +=1
        elif tooth >= 10:
            tooth -= 10
            ten += 1
        elif tooth >= 5:
            tooth -= 5
            five += 1
        elif tooth >= 1:
            tooth -= 1
            one += 1
    result.insert(len(result), [twenty, ten, five, one])

print(result)
            

    