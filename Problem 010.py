primes = []
for i in range(0,2000000):
    primes.append(True)

for i in range(2,2000000):
    if primes[i]:
        index = i * 2
        while index < 2000000:
            primes[index] = False
            index += i

total = 0
index = 2
while index < len(primes):
    if primes[index]:
        total += index
    index += 1

print(total)
