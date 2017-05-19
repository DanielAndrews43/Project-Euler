primes = []
for i in range(0,1000):
    primes.append(True)

prime = []
for i in range(2,len(primes)):
    if primes[i]:
        prime.append(i)
        index = i * 2
        while index < len(primes):
            primes[index] = False
            index += i

consecutive = 0
val = 0
for n in range(2, 200000):
    divisors = []
    for i in prime:
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 4:
        consecutive += 1
        val = n
    else:
        consecutive = 0

    if consecutive == 4:
        print val - 3