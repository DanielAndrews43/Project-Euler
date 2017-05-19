primes = []
for i in range(0,1000000):
    primes.append(True)
primes[0] = False
primes[1] = False

for i in range(2,1000000):
    if primes[i]:
        index = i * 2
        while index < 1000000:
            primes[index] = False
            index += i

count = 0
for i in range(10,len(primes)):
    if primes[i]:
        s = str(i)
        index = 1
        flag = True
        while index < len(s):
            if not primes[int(s[index:])]:
                flag = False
                break
            index += 1
        index = len(s) - 1
        while index > 0:
            if not primes[int(s[:index])]:
                flag = False
                break
            index -= 1
        if flag:
            count += i
print(count)
