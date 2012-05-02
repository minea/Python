def binarySearch(A, key):
    left, right = (0, len(A))
    while left < right:
        middle = (left + right) / 2
        if A[middle] == key:
            return middle
        if A[middle] < key:
            left = middle + 1
        else:
            right = middle
    return -1

def  binarySR(A,key):
    return binerySRAux(A,0,len(A),key)

def binarySRAux(A,left,right, key):
    if left >= right:
        return -1
    middle = (left + right) / 2
    if A[middle] == key:
        return middle
    if A[middle] < key:
        return binarySRAux(A, middle+1, right, key)
    else:
        return binarySRAux(A, left, middle, key)
