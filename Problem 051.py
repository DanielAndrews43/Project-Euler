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
primes[0] = False
primes[1] = False


seen = set()
flag = False
for p in prime:
    if flag:
        break
    for n in range(10):
        arr = str(p).split(str(n))
        if len(arr) > 1:
            count = 0
            for i in range(10):
                new_p = str(i).join(arr)
                if new_p[0] == '0':
                    continue
                if primes[int(new_p)]:
                    count += 1
                if count == 8:
                    flag = True
                    print(p)
                    break