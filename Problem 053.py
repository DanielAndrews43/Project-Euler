facts = []
index = 0
facts.append(1)
for i in range(1,101):
    facts.append(facts[i-1]*i)
count = 0
for n in range(1,101):
    for r in range(1,n):
        if facts[n]/(facts[r]*facts[n-r]):
            count += 1
print(count)
