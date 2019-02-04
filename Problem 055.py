count = 0
for i in range(10000):
  num = i
  flag = True
  for i in range(50):
    num_str = str(num)
    if num_str[::-1] == num_str:
      flag = False
      break
    else:
      num += int(num_str[::-1])
  if flag:
    count += 1


print(count)