largest = 0
theNum = 0
for i in range(1,1000):
    if len(str(1.0/i)) > 10:
        a = set()
        num = 10**(len(str(i)))
        while num%i not in a:
            num = num%i
            a.add(num%i)
            if num == 0:
                break
            while num < i:
                num *= 10
        if len(a) > largest:
            largest = len(a)
            theNum = i
print(theNum)
