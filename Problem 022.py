file = open('p022_names.txt', 'r')
names = file.read().replace('"','').split(',')

names.sort()

print(sum([sum([ord(x) - ord('A') + 1 for x in y])*(index+1) for index,y in enumerate(names)]))