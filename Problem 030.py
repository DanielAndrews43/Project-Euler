a = []
for i in range(2,354294): #9^5 * 6 is 6 digits, so sum of 7 of these will definitely not be 7 digits
    s = str(i)
    temp = 0
    for j in s:
        temp += int(j)**5
    if temp == i:
        a.append(i)
print(sum(a))