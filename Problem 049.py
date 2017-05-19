primes = []
for i in range(0,10000):
    primes.append(True)

for i in range(2,len(primes)):
    if primes[i]:
        index = i * 2
        while index < len(primes):
            primes[index] = False
            index += i

for i in range(1000,len(primes)-6660):
    a,b,c = i,i+3330,i+6660
    if primes[i] and primes[i+3330] and primes[i+6660] and i != 1487:
        aset,bset,cset = set(),set(),set()
        for l in range(0,4):
            aset.add(str(a)[l])
            bset.add(str(b)[l])
            cset.add(str(c)[l])
        if aset == bset and bset == cset:
            print(str(a)+str(b)+str(c))
