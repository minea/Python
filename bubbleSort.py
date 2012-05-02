def bubbleSort(a):
    for i in range(len(a) -1):
        for j in range(len(a) -a, i, -1):
            if a[j -1] > a[j]:
                a[j -1], a[j] = (a[j], a[j -1])
    return
