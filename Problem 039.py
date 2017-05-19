tris = {}
for a in range(3,300):
    for b in range(a,400):
        for c in range(b,500):
            if a*a + b*b == c*c:
                size = a+b+c
                num = tris.get(size,0)
                tris[size] = num + 1
        

biggest = 0
num = 0
for size in tris:
    if tris[size] > biggest:
        biggest = tris[size]
        num = size
print(num)