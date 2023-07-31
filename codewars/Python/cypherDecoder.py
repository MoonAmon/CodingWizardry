def sortingArray(array):
    for i in range(i,len(array)-1,1):
        for j in range(i+1,len(array),1):
            if array[i]%2 != 0 and array[j]%2 != 0:
                if array[j]<array[i]:
                    x = array[i]
                    array[i]=array[j]
                    array[j] = x
    return array