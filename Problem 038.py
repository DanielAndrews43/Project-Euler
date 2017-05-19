largest = '0'
for i in range(1,10000):
    a = ''
    index = 1
    while len(a) < 9:
        a += str(i * index)
        index += 1

    if len(a) != 9:
        continue

    flag = True
    for i in range(1,10):
        if str(i) not in a:
            flag = False
    if flag and int(largest) < int(a):
        largest = a
print(largest)
