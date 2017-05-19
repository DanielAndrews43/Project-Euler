primes = []
for i in range(0,1000000):
    primes.append(True)

prime = []
for i in range(2,len(primes)):
    if primes[i]:
        prime.append(i)
        index = i * 2
        while index < len(primes):
            primes[index] = False
            index += i
memo = {}
cons = 1
largest = 2
for ind,p in enumerate(prime):
    start = 0
    while start < 20 and prime[start] * (cons+1) < p:
        index = start
        total = 0
        if memo.get(start,0):
            a = memo.get(start)
            index = start + a[0]
            total = a[1]
        while total + prime[index] <= p and index < len(prime):
            total += prime[index]
            index += 1
        if total == p and index - start > cons:
            cons = index - start
            largest = p
            memo[start] = (cons,total)
        else:
            memo[start] = (index-start,total)
        start += 1
print(largest)