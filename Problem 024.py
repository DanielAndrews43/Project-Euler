def generate(s):
    if len(s) <= 1:
        yield [s]
    else:
        for perm in generate(s[1:]):
            for i in range(len(s)):
                yield perm[:i] + [s[0:1]] + perm[i:]

a = list(generate('0123456789'))

a.sort()

print(''.join(a[999999]))
