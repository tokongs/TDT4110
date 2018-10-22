def selectionSort(list):
    result = []

    while(list):
        max = list[0]
        for x in list:
            if x > max:
                max = x
        result.insert(0, max)
        list.remove(max)
    return result

def bubbleSort(list):
    while not isSorted(list):
        for x in range(len(list)-1):
            if(list[x] > list[x+1]):
                tmp = list[x]
                list[x] = list[x + 1]
                list[x + 1] = tmp
    return list

def isSorted(list):
    for x in range(1, len(list)):
        if list[x] < list[x-1]:
            return False
    return True
    

liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]
print(selectionSort(liste))

liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]
print(bubbleSort(liste))