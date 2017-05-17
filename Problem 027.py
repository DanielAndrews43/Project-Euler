primes = []
for i in range(0,2000000):
    primes.append(True)

for i in range(2,2000000):
    if primes[i]:
        index = i * 2
        while index < 2000000:
            primes[index] = False
            index += i

p = set()
for i in range(2,len(primes)):
    if primes[i]:
        p.add(i)

tops = 0
maxA = 0
maxB = 0
for a in range(-1000,1000):
    for b in range(-1000,1000):
        count = 0
        n = 0
        while n*n + a*n + b in p:
            n += 1
            count += 1
        if count > tops:
            maxA = a
            maxB = b
            tops = count
print(maxA*maxB)
