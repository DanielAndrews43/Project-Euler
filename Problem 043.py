def perms(s):
    if len(s) <= 1:
        yield [s]
    else:
        for perm in perms(s[1:]):
            for i in range(len(s)):
                yield perm[:i] + [s[0:1]] + perm[i:]

total = 0
number = "0123456789"
for p in perms(number):
    p = ''.join(p)
    if int(p[1:4]) % 2 == 0:
        if int(p[2:5]) % 3 == 0:
            if int(p[3:6]) % 5 == 0:
                if int(p[4:7]) % 7 == 0:
                    if int(p[5:8]) % 11 == 0:
                        if int(p[6:9]) % 13 == 0:
                            if int(p[7:10]) % 17 == 0:
                                total += int(p)
print(total)