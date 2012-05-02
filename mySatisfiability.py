# -*- coding: utf-8 -*-
from copy import deepcopy
def satisfiblity(A):
    """ CNFリスト A の充足可能性を調べる """
    vrblList = restructure(A)
    termNum = len(A)
    vrblNum =len(vrblList)
    values = [0 for k in range(vrblNum)]
    flag = 0
    while 1:
        Test = deepcopy(A)
        flag += 1
        if countSats(Test, values) == termNum:
            print values
            return True
        if nextVal(values,flag) == False:
            return False
    return False

def countSats(A, values):
    """ A に値 values を適用したとき充足する和項数を返す """
    count = 0 # count の初期化

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < 0: # not だった場合の処理
                if values[abs(A[i][j])-1] == 0: # 0だったら
                    A[i][j] = 1 # not 0 = 1を入れる
                else:
                    A[i][j] = 0
            else:
                A[i][j] = values[abs(A[i][j])-1]

    for i in range(len(A)):
        dammy = 0
        for j in range(len(A[i])):
            dammy = dammy or A[i][j]
        if dammy: # dammy が 1 (真)ならば
            count += 1
    return count

def nextVal(value,flag):
    """ 値のリスト values を次の値にする """
    bitValue = format(flag,'0%(hoge)db' %{'hoge':len(value)})

    for i in range(len(value)):
        value[i] = int(bitValue[i])

    if flag == (2 ** len(value)):
        return False
    else:
        return True

def restructure(A):
    """ A で使われている変数名を 1 からに再構成する """
    vrblList = []
    for term in A: # term はリテラルの和
        for vrbl in term:
            if vrbl < 0:
                vrbl = -vrbl
            if vrbl not in vrblList:
                vrblList.append(vrbl)
    vrblList.sort()
    for term in A:
        for k in range(len(term)):
            if term[k] < 0:
                sign, vrbl = (-1, -term[k])
            else:
                sign, vrbl = (1, term[k])
            term[k] = (vrblList.index(vrbl) + 1) * sign
    return vrblList

#A = [[1, -2, 4], [3, -4, 8], [-2, -4, -8], [1, 8]]
A = [[1,2],[-1,-2,3],[2,3]]
satisfiblity(A)
