def perms(s):
    if len(s) <= 1:
        yield [s]
    else:
        for perm in perms(s[1:]):
            for i in range(len(s)):
                yield perm[:i] + [s[0:1]] + perm[i:]

biggest = 0
number = "9876543210"
for p in perms(number):
    num = int(''.join(p))
    flag = True
    for i in range(2, 5):
        if num % i == 0:
            flag = False
            break
    if flag:
        if num > biggest:
            biggest = num
            print(num)
