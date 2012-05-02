# -*- coding: utf-8 -*-
# ナップサック設定
KNAP_SIZE = 3000
Length = 1000

def GeneticAlgorithm():
    items = knapItems(Length)
    print "items = ",items
    Times, Npop, Seed = parameter()
    probX = 0.6
    probM = 0.2
    group = initialize(Length, Npop)
    for k in range(Times):
        evaluate(group,items)
        eliteChr = elite(group)
        prntAll(group, k)
        group = roulette(group)
        crossover(group, probX)
        mutation(group, probM)
        elitePrs(group, eliteChr, 2)
    prntBest(group,items)
    return

def parameter(paras = ""):
    """ パラメータを読む """
    Times, Npop, Seed = (100, 30, 109) #default値
    if paras == "":
        paras = []
    else:
        paras = paras.aplit("-")
    for p in paras:
        if   p[0] == "t":
            Times = int(p[1:])
        elif p[0] == "p":
            Npop  = int(p[1:])
        elif p[0] == "s":
            Seed  = int(p[1:])
    return(Times, Npop, Seed)
# paras の例: "t200-p30-s29" "p50" "s91-t200"
# 実際はパラメータの数はもっと増える

import random # 乱数に関するモジュール

def initialize(Length, Npop):
    """ 初期集団生成:ランダムな順列を Npop 個 """
    group = []
    for k in range(Npop):
        chromo = range(Length)  # chromo = [0, 1, ... Length-1]
        random.shuffle(chromo)  # chromo = [3, 9, ... 1, 0, 5]
        chromo.append(0)        # chromo[-1] には適応度を入れる
        group.append(chromo)
    return group

def prntAll(group, time):
    """ 全染色体を出力 """
    print "%4d - " % time,
    for chromo in group:
        # print "{%d} %s" % (chromo[-1], chromo[:-1])
        print chromo[-1]['price'],
    print
    return

def prntBest(group,items):
    """ 全染色体を出力 """
    price_list = []
    for chromo in group:
        price_list.append(chromo[-1]['price'])
    for chromo in group:
        if chromo[-1]['price'] == max(price_list):
            items_list = chromo[-1]['list']
            print "Best : ",chromo[-1]['list']
            for k in range(len(items_list)):
                x = items_list[k]
                print x,": ",items[x]
            print "KnapMaxSize :",KNAP_SIZE,", MaxSize : ",chromo[-1]['size'],
            print ", MaxPrice : ",chromo[-1]['price']
            break
    return

# list[:-1] = list[0] ~ list[-2] = list[0:-1]

def evaluate(group, items):
    for chromo in group:
        fitness(chromo, items)
    return

def fitness(chromo, items):  # 問題ごとに作成
    max_size = 0
    max_price = 0
    greed_list = []
    for k in range(len(items)):
       # サイズオーバーしないかchromo先頭から調べる
        max_size += items[chromo[k]]['size']
        max_price += items[chromo[k]]['price']
        if (max_size > KNAP_SIZE):
            max_size -= items[chromo[k]]['size']
            max_price -= items[chromo[k]]['price']
        else:
            greed_list.append(k) # サイズオーバーしない値の列を作成

    chromo[-1] = {'price': max_price, 'list':greed_list, 'size':max_size}
    return

def elite(group):
    """ 生物集団 group 中のエリートを返す """
    largestPos, largestVal = (0, group[0][-1]['price'])
    for k in range(1, len(group)):
        if largestVal < group[k][-1]['price']:
            largestPos, largestVal = (k, group[k][-1]['price'])
    return group[largestPos][:]

def roulette(oldGrp):
    """ ルーレット選択 """
    strip = [oldGrp[0][-1]] # 要素1つのリスト

    for k in range(len(oldGrp) -1):
        strip.append({'price':strip[-1]['price'] + oldGrp[k + 1][-1]['price']})
        # 布切れの最後に k + 1 番目の評価値を布を加える
    newGrp = []
    while len(newGrp) < len(oldGrp):
        newGrp.append(oldGrp[rotate(strip)][:])
    return newGrp

def rotate(strip):
    """ ルーレットを回す """
    value = random.random() * strip[-1]['price']
    left, right = (0, len(strip) - 1)
    while left < right:
        middle = (left + right) / 2
        if strip[middle] < value:
            left = middle + 1
        else:
            right = middle
    return right

def crossover(group, probX):
    """ 交叉確率 probX """
    genes = group[0][:-1]  # 遺伝子の集合, 順序はランダム
    for k in range(0, len(group), 2):
        if (len(group) % 2 == 1) and ( k == len(group) -1):
            return
        if random.random() > probX:  # 0 <= random() < 1
            continue
        pos2 = random.sample(genes, 2)
        posL = range(min(pos2), max(pos2))
        group[k]     = PMXbasic(group[k], group[k + 1], posL)
        group[k + 1] = PMXbasic(group[k + 1], group[k], posL)
    return

def PMXbasic(papa, mama, posL):
    """ partial mapped crossover """
    child = papa[:]
    for pos in posL:
        swap(child, pos, child.index(mama[pos]))
    return child

def swap(List, left, right):
    List[left], List[right] = (List[right], List[left])
    return

def mutation(group, probM):
    """ 突然変異確率 """
    genes = group[0][:-1]
    for chromo in group:
        if random.random() > probM:
            continue
        pos2 = random.sample(genes, 2)
        swap(chromo, pos2[0], pos2[1])
    return

def elitePrs(group, eliteChr, num):
    deleteS = random.sample(range(len(group)), num)
    for k in deleteS:
        group[k] = eliteChr[:]
    return

def knapItems(Length):
    """ 商品作成 """
    items = []
    for k in range(Length):
        #items[size,price]
        items.append({'size':random.randint(10,100),'price':random.randint(1,20)})
    return items

print GeneticAlgorithm()
