num = 1
index = 2

while True:
    num += index
    index += 1
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 2
    print(count,num)
    if count >= 500:
        print(num)
        break