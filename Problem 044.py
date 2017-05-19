pents = {}

def pent():
    n = 1
    while True:
        yield n*(3*n - 1) / 2
        n += 1

foundIt = ''
p = pent()
b = 0
while b < 100000:
    b = p.next()
    for i in pents:
        if pents.get(b - i,False):
            if foundIt:
                if b-i < foundIt[2]:
                    foundIt = (b,i,b-i)
            else:
                foundIt = (b,i,b-i)
    pents[b] = True
print(foundIt[2])