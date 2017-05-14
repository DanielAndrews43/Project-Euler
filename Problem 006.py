squareSum = ((101 * 100) / 2)**2

sumSquare = 0
for i in range(1,101):
    sumSquare += i**2

print(squareSum - sumSquare)