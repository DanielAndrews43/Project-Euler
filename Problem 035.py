primes = []
for i in range(0,1000000):
    primes.append(True)

for i in range(2,1000000):
    if primes[i]:
        index = i * 2
        while index < 1000000:
            primes[index] = False
            index += i

circulars = set()
for i in range(2,1000000):
    if primes[i]:
        n = str(i)
        flag = True
        for _ in range(len(n)):
            n = n[1:len(n)] + n[0]
            if not primes[int(n)]:
                flag = False
        if flag:
            circulars.add(i)
print(len(circulars))