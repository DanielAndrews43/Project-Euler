pents = {}


for n in range(1,10000):
    pents[n*(3*n - 1) / 2] = True
    n += 1

foundIt = ''
for i in pents:
    for j in pents:
        if j < i:
            continue
        if pents.get(j-i, False) and pents.get(j+i, False):
            if foundIt:
                if j-i < foundIt[2]:
                    foundIt = (j,i,j-i)
            else:
                foundIt = (j,i,j-i)

print(foundIt[2])