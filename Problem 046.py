squares = [2*x*x for x in range(1,100000)]

primes = []
for i in range(0,1000000):
    primes.append(True)
primes[0] = False
primes[1] = False

for i in range(2,len(primes)):
    if primes[i]:
        index = i * 2
        while index < len(primes):
            primes[index] = False
            index += i

def finder():
    for i in range(2,len(primes)):
        flag = True
        if i % 2 and not primes[i]:
            for j in range(2,i):
                if primes[j]:
                    index = 0
                    while j + squares[index] <= i:
                        if j + squares[index] == i:
                            flag = False
                            break
                        index += 1
                elif not flag:
                    break
            if flag:
                return i
print(finder())
