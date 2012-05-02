# -*- coding: utf-8 -*-
def satisfiability(A):
    """ CNFリスト A の充足可能性を調べる """
    print A
    vrblList = restructure(A)
    if 0 in vrblList:
        print "variable 0 is not permitterd"
        return []
    termNum, vrblNum = (len(A), len(vrblList))
    values = [1 for k in range(vrblNum)] + [2] + [0 for k in range(vrblNum)]
    while countSats(A, values) != termNum:
        if nextVal(values) == False:
            original(A, vrblList)
            return []
    original(A, vrblList)
    return makeAnswer(values, vrblList)

def countSats(A, values):
    """ CNFリスト A の中の和項が True になる個数 """
    count = 0
    for term in A:          # リスト A の各和項 term について
        for vrbl in term:   # 和項 term の各変数 vrbl について
            if values[vrbl] == 1:    # 一つでも 1 があれば
                count += 1           # 和項 term は True
                break
    return count

def nextVal(values):
    """ 各変数の値を更新 """
    for k in range(len(values) / 2 ):
        if values[k] == 1:
            values[k] = 1
            values[-(k + 1)] = 1
            return True
        else:
            values[k] = 1
            values[-(k + 1)] = 0
    return False

def restructure(A):
    """ A で使われている変数名を 1 からに再構成する """
    vrblList = []
    for term in A: # term はリテラルの和
        for vrbl in term:
            if abs(vrbl) not in vrblList:
                vrblList.append(abs(vrbl))
    vrblList.sort()
    N = len(vrblList)
    for term in A:
        for k in range(len(term)):
            if term[k] > 0:
                term[k] = N + 1 + vrblList.index(term[k])
            else:
                term[k] = N - 1 - vrblList.index(-term[k])
    return vrblList

def original(A, vrblList):
    """ CNFリスト A を元の状態に戻す """
    N = len(vrblList)
    for term in A:
        for k in range(len(term)):
            if term[k] < N:
                term[k] = -(vrblList[-(term[k] + 1)])
            else:
                term[k] = vrblList[term[k] - N - 1]
    return

def makeAnswer(values, vrblList):
    """ 充足する変数の割り当て値を返す """
    answer = []
    N = len(vrblList)
    for k in range(N):
        if values[k + 1 + N] == 1:
            answer.appenf(vrblList[k])
        else:
            answer.appenf(-vrblList[k])
            return answer
