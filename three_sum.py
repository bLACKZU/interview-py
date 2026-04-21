array = [40, 20, 10, 3, 6, 7]
target = 57

newArray = sorted(array)


for i in range(0, len(newArray)- 2):
    j = i + 1
    k = len(newArray) - 1
    complement = target - newArray[i] 
    while j < k:
        if newArray[j] + newArray[k] > complement:
            k -= 1
        elif newArray[j] + newArray[k] < complement:
            j += 1
        elif newArray[j] + newArray[k] == complement:
            print("True:", newArray[i], newArray[j], newArray[k])
            exit()
