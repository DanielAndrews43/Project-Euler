ans = 1

for n in range(11,100):
    for d in range(n+1,100):
        frac = 1.0*n/d
        if d%10:
            nn = str(n)
            dd= str(d)
            if float(nn[0]) / float(dd[1]) == frac or float(nn[1]) / float(dd[0]) == frac:
                if nn[0] == dd[1] or nn[1] == dd[0]:
                    ans *= frac
print(1 / ans)