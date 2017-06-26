total = 0
for a in range(1,100):
    for b in range(1,100):
        temp = pow(a,b)
        val = 0
        while temp != 0:
            val += temp % 10
            temp /= 10
        if val > total:
            total = val
            print(total)
print(total)