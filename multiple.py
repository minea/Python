# -*- coding: utf-8 -*-
def multiple(a, b): # A と B は同じサイズ
    """ A と B の積を返す """
    size = len(a) # len(a) はリスト A の長さ
    C = [] # C はリスト(初期値はnull)と宣言
    for i in range(size): # range(size) は [0,1,...,size-1]
        row = [] # row はリスト. C の i 行目を作る準備
        for j in range(size): # j = 0, 1,..., size-1
            val = 0 # C の i行 j列目の計算準備
            for k in range(size):
                val += a[i][k] * b[k][j]
            row.append(val)
        C.append(row)
    return C

import datetime
def multipleT(a, b, times):
    """ multiple を times 買い実行する """
    start = datetime.datetime.now()
    for i in range(times):
        ans = multiple(a, b)
    print datetime.datetime.now() -start
    return ans

def multipleAdv(a, b):
    """ A の列数と B の行数が同じである場合に計算を実行する """
    if len(a[0]) != len(b): # 違う場合はエラーをだして終了
        return "Error"
    elif len(a[0]) == len(b):
        m_size = len(a) # a の行数
        n_size = len(a[0]) # a の列数　かつ b の行数
        p_size = len(b[0]) # b の列数
        C = []
        for i in range(m_size):
            row = []
            for j in range(p_size):
                val = 0
                for k in range(n_size):
                    val += a[i][k] * b[k][j]
                row.append(val)
            C.append(row)
        return C

import datetime
def multipleAdvT(a, b, times):
    """ multipleAdv を times 買い実行する """
    start = datetime.datetime.now()
    for i in range(times):
        ans = multipleAdv(a, b)
    print datetime.datetime.now() -start
    return ans


