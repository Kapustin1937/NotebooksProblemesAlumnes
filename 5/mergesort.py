def merge(x,y):
    if len(x) < 1:
        return y
    if len(y) < 1:
        return x
    else:
        if x[0] < y[0]:
            return [x[0]] + merge(x[1:], y)
        else:
            return [y[0]] + merge(x,y[1:])
def mergesort(llista):

    if len(llista) < 2:
        return llista
    
    else:
        mid = len(llista) // 2
        left = mergesort(llista[:mid])
        right = mergesort(llista[mid:])
        return merge(left,right)
llist = [1,4,5,4,3,2,5,7,8,4,5,6,2]
print(mergesort(llist))