start, end = 2, 5

array = []
temp = "A"

for firstDigit in range(start, end+1):   # "end+1" for "end" get involved
    for secondDigit in range(1, firstDigit+1):
        array.append(f"{firstDigit}{secondDigit}")

for i in range(len(array)):
    if array[i][0] == array[i][1]:
        print(f"{temp}"+array[i], end="\n")
    else:
        print(f"{temp}"+array[i], end=" ")
