divs = {}

for n in range(2, 28123):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n / i != i and i != 1:
                divisors.append(n / i)
    divs[n] = divisors

abundants = []
for div in divs:
    if sum(divs[div]) > div:
        abundants.append(div)

nums = []
for i in range(28124):
    nums.append(False)

for n in abundants:
    for m in abundants:
        if n+m > 28123:
            break
        nums[n+m] = True

count = 0
for index,num in enumerate(nums):
    if index > 28123:
        break
    if not num:
        count += index
print(count)