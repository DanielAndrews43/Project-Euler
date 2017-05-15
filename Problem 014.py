def even(n):
    return n/2
def odd(n):
    return n*3 + 1

lens = {1:1}

for i in range(1,1000000):
    num = i
    count = 0
    while True:
        if lens.get(num):
            lens[i] = count + lens.get(num)
            break
        elif num % 2:
            num = odd(num)
            count += 1
        else:
            num = even(num)
            count += 1

best = (0,0)
for i in lens:
    if lens.get(i) > best[1]:
        best = (i, lens.get(i))

print(best)