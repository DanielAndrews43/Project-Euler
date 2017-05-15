f = lambda x: x * f(x-1) if x > 1 else 1
print(sum([int(x) for x in str(f(100))]))