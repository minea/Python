# -*- coding: utf-8 -*-
def powBinary(g,k,N):
    """ Binary version """
    ans = 1
    while k != 0:
        if k % 2 == 1:
            ans = (ans * g) % N
        k /= 2
        g = (g * g ) % N
    return ans

def powNormal(g,k,N):
    """ Normal version """
    ans = 1
    for i in range(k):
        ans = (ans * g) % N
    return ans

import time
def powBinaryT(g,k,N,times):
    start = time.time()
    for i in range(times):
        ans = powBinary(g,k,N)
#    print "powBinary g: ",g," k: ",k," N: ",N," times : ",datetime.datetime.now() - start
    print "powBinary ,g, ",g,",",time.time() - start
    return ans

def powNormalT(g,k,N,times):
    start = time.time()
    for i in range(times):
        ans = powNormal(g,k,N)
#    print "powNormal g: ",g," k: ",k," N: ",N," times : ",datetime.datetime.now() - start
    print "powNormal ,g, ",g,",",time.time() - start
    return ans

#powNormalT(2,10,1,1000)
#powBinaryT(2,10,1,1000)
powNormalT(1,10,7,1000)
powBinaryT(1,10,7,1000)

for i in range(5,1005,5):
    powNormalT(i,10,7,100)

for i in range(5,1005,5):
    powBinaryT(i,10,7,100)
