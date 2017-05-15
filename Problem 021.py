divs = {}

for n in range(2, 10001):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n / i != i and i != 1:
                divisors.append(n / i)
    divs[n] = divisors

count = 0
for num in divs:
    total = sum(divs.get(num))
    reverse = sum(divs.get(total, []))
    if reverse == num and num != total:
        count += num

print(count)
