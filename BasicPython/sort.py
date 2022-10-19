
dizi = [35,46,17,99,85,57,12,5,84,46]
n = len(dizi)

def selectionSort():
    copyDizi = dizi.copy()
    i = 0
    while(i < n):
        minX = copyDizi[i]
        minIndex = i
        j = i+1
        while(j < n):
            if(minX > copyDizi[j]):
                minX = copyDizi[j]
                minIndex = j
            j+=1
        temp = copyDizi[i]
        copyDizi[i] = minX
        copyDizi[minIndex] = temp
        i+=1
    return copyDizi

def insertionSort():
    copyDizi = dizi.copy()
    i = 0
    while(i < n):
        temp = copyDizi[i]
        j = i-1
        while(j >= 0 and temp < copyDizi[j]):
            copyDizi[j+1] = copyDizi[j]
            j-=1
        copyDizi[j+1] = temp
        i+=1
    return copyDizi

print(f"Dizi:\t\t{dizi}\nS.Sort:\t\t{selectionSort()}\nI.Sort:\t\t{insertionSort()}")
