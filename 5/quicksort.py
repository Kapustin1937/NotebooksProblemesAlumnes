def quicksort(llista):

    if len(llista) < 2:
        return llista
    
    if len(llista) == 2:
        if llista[0] > llista [1]:
            return llista[::-1]
        else:
            return llista
    else:
        pivot = llista[-1]
        rightlist = []
        leftlist = []
        for i in llista[:-1]:
            if i < pivot:
                leftlist.append(i)
            if i >= pivot:
                rightlist.append(i)
        return quicksort(leftlist) + [pivot] + quicksort(rightlist)

llist = [1000,9,9,9,94,2,2,3,5,7,9,3,9,8,7,6,5,4,3,2,1]
print(quicksort(llist))