def tri():
    n = 286
    while True:
        yield n*(n+1) / 2
        n += 1
def pent():
    n = 166
    while True:
        yield n*(3*n - 1) / 2
        n += 1
def hex():
    n = 144
    while True:
        yield n * (2*n - 1)
        n += 1

t,p,h = tri(),pent(),hex()
tt,pp,hh = t.next(),p.next(),h.next()

while tt != pp and pp != hh:
    while tt < pp or tt < hh:
        tt = t.next()
    while pp < tt or  pp < hh:
        pp = p.next()
    while hh < tt or hh < pp:
        hh = h.next()

print(tt)
