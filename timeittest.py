import timeit
t = timeit.Timer("pow.powNormal(5,10,7)","import pow")
print "k,",t.timeit(1000)
#for i in range(5,305,5):
#    t = timeit.Timer("pow.powNormal(i,10,7)","import pow")
#    print "k,",t.timeit(1000)
