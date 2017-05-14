primes = []

index = 2
while len(primes) != 10001:
    flag = True
    for p in primes:
        if index % p == 0:
            index += 1
            flag = False
            break
    if not flag:
        continue
    primes.append(index)
    index += 1

print(primes[-1])
