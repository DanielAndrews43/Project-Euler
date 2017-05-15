ones  = [0,3,3,5,4,4,3,5,5,4]
teens = [3,6,6,8,8,7,7,9,8,8]
tens  = [0,3,6,6,5,5,5,7,6,6]
hundreds = 7
land = 3

total = 0
total += ones[1] + len("thousand")

for i in range(1, 1000):
    one = i % 10
    i /= 10
    ten = i%10
    i /= 10
    hundred = i%10

    if ten == 1:
        total += teens[one]
    else:
        total += ones[one]
        total += tens[ten]

    if hundred != 0:
        total += hundreds + ones[hundred]

        if ten != 0 or one != 0:
            total += land

print(total)