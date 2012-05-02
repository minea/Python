def Max1and2(A):
    A = tournament(A)
    print A
    max1 = A[0]
    max2 = number2(A[1:len(A) /2], A[len(A) /2])
    print "max1 = ", max1, " max2 = ", max2
    return

def tournament(A):
    if len(A) % 2 == 1:
        A.append(0)
    if len(A) == 2:
        if A[0] < A[1]:
            A[0], A[1] = (A[1], A[0])
        return A
    halfL = tournament(A[:len(A) /2])
    halfR = tournament(A[len(A)/2:])
    if halfL[0] < halfR[0]:
        return halfR + halfL
    else:
        return halfL + halfR

def number2(A, max2):
    if len(A) == 1:
        return max2
    else:
        if A[len(A)-1] > max2:
            max2 = A[len(A)-1]
        A.pop()
        return number2(A,max2)

A = [3,9,8,6,1,5,7,2,10,4,11,30]
print Max1and2(A)

