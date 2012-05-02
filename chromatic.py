# -*- coding: utf-8 -*-
def colorable(G,k):
    """ グラフ彩色判定問題 """
    return (G[1] <= k)

def chromatic(G):
    """ 2分探索：最基板 """
    return chromaticAux(G,0,G[0])

def chromaticAux(G,left,right):
    """ chromatic の補助関数 (auciliary) """
    middle = (left + right) / 2
    if colorable(G,middle):
        return middle
    else: # folaseだったら右半分を見る
        return chromaticAux(G,middle +1, right)

A = [5,4]
print chromatic(A)
