total = 0

for n in range(2, 10000):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a = str(n) + str(i) + str(n/i)
            if len(a) > 9:
                continue
            flag = True
            for j in range(1,10):
                if str(j) not in a:
                    flag = False
            if flag:
                print(a,n,i,n/i)
                total += n
                break

print(total)
    