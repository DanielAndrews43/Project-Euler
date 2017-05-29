index = 1
exp = 0
while True:
    s = str(index)
    if len(s) < len(str(index*6)):
        exp += 1
        index = 10**exp
        continue
    nums = {}
    for i in s:
        nums[i] = nums.get(i,0) + 1
    flag = True
    for i in range(1,7):
        temp = i * index
        if not flag:
            break
        for j in range(10):
            if str(temp).count(str(j)) != nums.get(str(j),0):
                flag = False
                break
    if flag:
        print(index)
        break
    index += 1
