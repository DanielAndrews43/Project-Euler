answer = 1
for i in xrange(999,900,-1):
    for ii in xrange(999,900,-1):
        temp = str(i*ii)
        if temp[::-1] == temp and i*ii > answer:
            answer = i*ii
print answer