print sum([x for x in range(1000) if not x % 3 or not x % 5]) #One lined

total = 0
for x in range(1000):
    if x%3 == 0 or x%5 == 0:
        total += x
print total