n1 = 1
n2 = 2
total = 0
while n1 <= 4000000 and n2 <= 4000000:
    n1 += n2
    if not n1%2:
        total += n1
    n2 += n1
    if not n2%2:
        total += n2
print total

#I have left out the recursive version as it is very uneffective as it adds tons
#of uneeded steps in order to achieve the answer