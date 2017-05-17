def fact(n):
    if n==0: 
        return 1
    return n * fact(n-1)
facts = [fact(x) for x in range(3,9)]

total = 0
for i in range(3,200000):
    n = str(i)
    if sum([fact(int(x)) for x in n]) == i:
        print(i)
        total += i

print(total)