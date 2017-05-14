for n in range(1000):
    for m in range(1000):
        a = n*n - m*m
        b = 2*n*m
        c = n*n + m*m
        if a + b + c == 1000:
            print(a*b*c)
            break

