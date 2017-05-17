coins = [1,2,5,10,20,50,100,200]

def count(index, total):
    if index < 0:
        return 0
    elif total == 0:
        return 1
    else:
        a = 0
        if not coins[index] > total:
            a = count(index, total - coins[index])
        b = count(index - 1, total)

        return a+b

print(count(len(coins)-1, 200))