def day():
    day = 3
    while True:
        yield day%7
        day += 1

def numDays(m, y):
    if m == 1:
        if y%4 == 0 and (y%100 != 0 or y%400 == 0):
            return 29
        return 28

    if m > 6:
        m -= 1
    return 30 if m%2 else 31

count = 0
d = day()
currDay = 2
for y in range(1901, 2001):
    for m in range(0,12):
        if currDay == 0:
            count += 1
        for _ in range(numDays(m, y)):
            currDay = d.next()

print(count)

        