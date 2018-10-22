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

def bubleSort(list):
    while

    

liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]
print(selectionSort(liste))