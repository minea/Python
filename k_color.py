# -*- coding: utf-8 -*-
from satisfiability import satisfiability
from copy import deepcopy
def k_color(G,k):
    vrtxList = checkGraph(G)
    CNF = []
    for vrtx in vrtxList:
        C = []
        for i in range(k): # 頂点に色は少なくとも1つ
            C.append((vrtx * 10) + (i + 1))
        CNF.append(C)

        elem = range(k)
        for i in range(k):
            elem[i] = elem[i] + 1

        for i, v in enumerate(elem):
            for v2 in elem[i+1:]:
                C = []
                C.append(-1 * ((vrtx * 10) + v))
                C.append(-1 * ((vrtx * 10) + v2))
                CNF.append(C)

    for edge in G:
        edge[0] = -1 * (edge[0] * 10)
        edge[1] = -1 * (edge[1] * 10)
        for i in range(k):
            C = deepcopy(edge)
            C[0] = C[0] - (i + 1)
            C[1] = C[1] - (i + 1)
            CNF.append(C)
    vrblList = satisfiability(CNF)
    if vrblList == []:
        print "impossible"
    else:
        print vrblList
    return

def checkGraph(G):
    """ グラフ情報 G から超店名のリストを作る """
    vrtxList = []
    for edge in G:
        if edge[0] not in vrtxList:
            vrtxList.append(edge[0])
        if edge[1] not in vrtxList:
            vrtxList.append(edge[1])
    vrtxList.sort()
    return vrtxList

def combination(n):
    """ 組み合わせの生成 """
    COMB = []
    for i, v in enumerate(n):
        C = []
        for v2 in n[i+1:]:
            C.append(v, v2)
        COMB.append(C)
    return COMB

A = [[1,2],[1,4],[2,3],[3,4],[4,2]]
k_color(A,3)
