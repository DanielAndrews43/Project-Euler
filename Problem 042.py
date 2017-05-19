file = open('p042_words.txt', 'r')
words = file.read().replace('"','').split(',')

tris = [(x*x+x)/2 for x in range(1,50)]

count = 0
for w in words:
    total = 0
    for l in w:
        total += ord(l)-ord('A')+1
    if total in tris:
        count += 1
print(count)