# -*- coding: utf-8 -*-
INF = 999999

def Dijkstra(adjL, s):
    queue = range(len(adjL))
    dist = [INF for k in queue]
    prev = [ -1 for k in queue]
    dist[s] = 0
    while queue != []:
        u = popMin(queue, dist)
        for v, weight in adjL[u]:
            if v not in queue:
                continue
            if dist[v] > dist[u] + weight:
                dist[v], prev[v] = (dist[u] + weight, u)
    return (dist, prev)

def edge2adj(edgeG):
    """ グラフの枝情報 G から隣接リスト adjL を作成する """
    vrtxL = []
    for u, v, w in edgeG:
        if u not in vrtxL:
            vrtxL.append(u)
        if v not in vrtxL:
            vrtxL.append(v)
    vrtxL.sort()
    adjL = [[] for k in range(len(vrtxL))]
    for u, v, weight in edgeG:
        adjL[vrtxL.index(u)].append([vrtxL.index(v),weight])
    return (adjL, vrtxL)

def popMin(queue, dist):
    indMin, distMin = (0, dist[queue[0]])
    for k in range(1, len(queue)):
        if distMin > dist[queue[k]]:
            indMin, distMin = (k, dist[queue[k]])
    return queue.pop(indMin)

def BellmanFord(edgeln, adjL,s):
    N = len(adjL)
    dist = [INF for k in range(N)]
    prev = [ -1 for k in range(N)]
    dist[s] = 0
    for k in range(N - 1):
        for u, v, weight in edgeln:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                prev[v] = u
    for u, v, weight in edgeln:
        if dist[v] > dist[u] + weight:
            return ([], [])
    return (dist, prev)

def edge2edgeln(edgeG):
    """ グラフの枝情報 G から隣接リスト adjL を作成する """
    vrtxL = []
    for u, v, w in edgeG:
        if u not in vrtxL:
            vrtxL.append(u)
        if v not in vrtxL:
            vrtxL.append(v)
    vrtxL.sort()
    adjL = [[] for k in range(len(vrtxL))]
    for u, v, weight in edgeG:
        adjL[vrtxL.index(u)].append([vrtxL.index(v),weight])
    edgeln = []
    for u, v, weight in edgeG:
        edgeln.append([vrtxL.index(u), vrtxL.index(v), weight])
    return (edgeln, adjL, vrtxL)

def pathPrint(prevL):
    last = prevL[t]
    path = [vrtxL[last]]
    while last != s:
        last = prevL[last]
        path.append(vrtxL[last])
    path.reverse()
    path.append(vrtxL[t])
    return path


def DijkOrBell(edgeG, s):
    edgeln, adjL, vrtxL = edge2edgeln(edgeG)
    start = vrtxL.index(s)
    for k in range(len(adjL)):
        if (edgeG[k][2] < 0):
            flag = 1
            break
        else:
            flag = 0
    if (flag == 1):
        dist, prev = BellmanFord(edgeln, adjL, start)
        print "BellmanFord : dist = ",dist, ", prev = ",prev
    else:
        dist, prev = Dijkstra(adjL, start)
        print "Dijkstra : dist = ",dist, ", prev = ",prev
    return (dist, prev)

def howFar(edgeG, s, e):
    edgeln, adjL, vrtxL = edge2edgeln(edgeG)
    dist, prevL = DijkOrBell(edgeG,s)

    start = vrtxL.index(s)
    t = vrtxL.index(e)
    last = prevL[t]
    path = [vrtxL[last]]
    while last != start:
        last = prevL[last]
        path.append(vrtxL[last])
    path.reverse()
    path.append(vrtxL[t])
    print "(",dist[vrtxL.index(e)], ",",path,")"
    return

G2 = [['s','u',10],['s','x',-5],['u','v',1],
      ['u','x',2],['v','y',4],['x','u',3],
      ['x','v',9],['x','y',2],['y','s',7],
      ['y','v',6]]

DijkOrBell(G2, 'x')
howFar(G2, 's', 'v')

def twoSAT(G):

    return


A = [[10], [21, -3], [-21, 3],[ -10, 3]]
