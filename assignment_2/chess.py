trans = {}

trans["a"] = 1
trans["b"] = 2
trans["c"] = 3
trans["d"] = 4
trans["e"] = 5
trans["f"] = 6
trans["g"] = 7
trans["h"] = 8
board = [[0 for x in range(8)] for y in range(8)] 

for x in trans:
    for y in range(8):
        if(trans[x] % 2 == 0):
            if(y % 2 == 0):
                board[trans[x] - 1][y] = "white"
            else:
                board[trans[x] - 1][y] = "black"
        else:
            if(y % 2 == 0):
                board[trans[x] - 1][y] = "black"
            else:
                board[trans[x] - 1][y] = "white"
        
 
position = input("Posisjon: ")
print(board[trans[position[0]]-1][int(position[1]) -1])