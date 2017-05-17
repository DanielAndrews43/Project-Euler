total = 0
for n in range(1,1000000):
    if str(n) == str(n)[::-1] and str(bin(n)[2:]) == str(bin(n)[2:][::-1]):
        total += n

print(total)