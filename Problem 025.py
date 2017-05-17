n = 1
m = 1
count = 2
while len(str(m)) != 1000:
    count += 1
    n,m = m,n+m
print(count)
