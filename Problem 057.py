# new_denom = denom + num
# new_num = new_denom + denom

count = 0
num = 3
denom = 2
for i in range(1000):
  if len(str(num)) > len(str(denom)):
    count += 1

  temp = denom + num
  num = temp + denom
  denom = temp

print(count)