# -*- coding: utf-8 -*-
import math
def fastProduct(A, B):
    if len(A) != len(B): # 正方行列ではない場合
        print "impossible! [len(A) != len(B)]"
        return
    if (len(A) & 1) != 0: # N == 2 ** n でない場合
        print "impossible! [ N != 2 ** n]"
        return
    else:
        N = int(math.log(len(A),2))
        print "P : ",product(A, B, N)
        return product(A, B, N)

def product(A, B, N):
    """ サイズ N (= 2 ** n) の行列 A と B の値を出力 """
    if N == 2:
        return strassen(A, B)
    #elif N > 2:
    A0, A1, A2, A3 = divide4(A,N) # 行列 A を4分割
    B0, B1, B2, B3 = divide4(B,N) # 行列 B を4分割
    
    N = int(math.log(len(A0),2))
    p1 = product(difM(A1, A3), sumM(B2, B3), N)
    p2 = product(sumM(A0, A3), sumM(B0, B3), N)
    p3 = product(difM(A0, A2), sumM(B0, B1), N)
    p4 = product(sumM(A0, A1), B3, N)
    p5 = product(A0, difM(B1, B3), N)
    p6 = product(A3, difM(B2, B0), N)
    p7 = product(sumM(A2, A3), B0, N)
    
    C0 = sumM(difM(sumM(p1, p2), p4), p6)
    C1 = sumM(p4, p5)
    C2 = sumM(p6, p7)
    C3 = difM(sumM(difM(p2, p3), p5), p7)

    return conquer(C0, C1, C2, C3, N) # C0 〜 C3 をまとめる

def sumM(A, B):
    """ 行列の足し算 A + B を出力 """
    return [a + b for a, b in zip(A,B)]

def difM(A, B):
    """ 行列の引き算 A + B を出力 """
    return [a - b for a, b in zip(A,B)]

def divide4(A, N):
    """ サイズ N の行列 A を 4つの部分行列に分ける """
    A0, A1, A2, A3 = ([], [], [], [])








    A0.extend(A[ : len(A)/8 ])
    A1.extend(A[ len(A)/8 : len(A)/4 ])
    A0.extend(A[ len(A)/4 : len(A)/4 + len(A)/8 ])
    A1.extend(A[ len(A)/4 + len(A)/8 : ])

    A2.extend(A[ len(A)/2 : len(A)/2 + len(A)/8 ])
    A3.extend(A[ len(A)/2 + len(A)/8 : len(A) - len(A)/4 ])
    A2.extend(A[ len(A) - len(A)/4 : len(A) - len(A)/8 ])
    A3.extend(A[ len(A) - len(A)/8 : ])

    return (A0, A1, A2, A3)

def conquer(C0, C1, C2, C3, N):
    """ 4つの部分行列から行列 C を作る """
    C = []

    C.extend(C0[ : len(C0)/2])
    C.extend(C1[ : len(C1)/2])
    C.extend(C0[ len(C0)/2 : ])
    C.extend(C1[ len(C1)/2 : ])

    C.extend(C2[ : len(C2)/2])
    C.extend(C3[ : len(C3)/2])
    C.extend(C2[ len(C2)/2 : ])
    C.extend(C3[ len(C3)/2 : ])
    return C

def strassen(A,B):
    """ Strassen's の方法, A と B のサイズは2 """
    p1 = (A[1] - A[3]) * (B[2] + B[3])
    p2 = (A[0] + A[3]) * (B[0] + B[3])
    p3 = (A[0] - A[2]) * (B[0] + B[1])
    p4 = (A[0] + A[1]) * B[3]
    p5 = A[0] * (B[1] - B[3])
    p6 = A[3] * (B[2] - B[0])
    p7 = (A[2] + A[3]) * B[0]
    return [p1 + p2 - p4 + p6,
            p4 + p5,
            p6 + p7,
            p2 - p3 + p5 - p7]

def multiple(a, b, sizes): # A と B は同じサイズ
    """ A と B の積を返す (行列1次元vertion) """
    C = [] # C はリスト(初期値はnull)と宣言
    for i in range(sizes):
        for j in range(sizes):
            val = 0
            for k in range(sizes):
                val += a[i * sizes + k] * b[ k * sizes + j]
            C.append(val)
    print "M : ",C
    return C

import datetime
def experiment(sizes, values, fileN):
    """ 計算結果をファイルに出力 """
    f = open(fileN, "w")
    print >>f, datetime.datetime.now()
    for n in sizes:
        print "n : ",n
        print >>f, "size = 2**%d = %d" % (n, 2**n)
        A = randM(2 ** n, values)
        B = A[:]
        random.shuffle(B)
        print >>f, "simple: ", simplePT(A,B,2**n),"sec"
        print >>f, " fast : ", fastPT(A,B),"sec"
        return
    f.close()
    return
# usage: experiment([6, 7, 8, 9], [-1, 0, 1], "experiment.out")

import random
def randM(size, values):
    A = []
    for k in range(size * size):
        A.append(random.choice(values))
    return A

import timeit
def simplePT(A,B,N):
    """ multiple の実行時間をtimeit関数で計測 """
    # 別ファイルである multiple モジュールをインポートしテスト対象に指定
    t = timeit.Timer("multiple( %s, %s, %s)" % (A,B,N), "from fastProduct import multiple")
    # テスト回数を1回としてして実行時間を計測し、出力する
    return t.timeit(1)

def fastPT(A,B):
    """ fastProduct の実行時間をtimeit関数で計測 """
    t = timeit.Timer("fastProduct( %s, %s)" % (A,B), "from fastProduct import fastProduct")
    # テスト回数を1回としてして実行時間を計測し、出力する
    return t.timeit(1)

experiment([3], [0, 1], "experiment.out")
