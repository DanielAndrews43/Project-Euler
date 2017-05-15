p = {}

def findPath(i, j):
    if p.get((i,j)):
        return p.get((i,j))
    if i == 20:
        p[(i,j)] = 1
        return 1
    elif j == 20:
        p[(i,j)] = 1
        return 1
    else:
        p[(i+1,j)] = findPath(i+1,j)
        p[(i,j+1)] = findPath(i,j+1)
        return p.get((i+1,j)) + p.get((i,j+1))

print(findPath(0,0))
