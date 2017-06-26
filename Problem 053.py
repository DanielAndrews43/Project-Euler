facts = [1]
index = 0
for i in range(1,101):
    facts.append(facts[i-1]*i)
count = 0
for n in range(23,101):
    for r in range(1,n):
        if facts[n]/(facts[r]*facts[n-r]) > 1e6:
            count += 1
print(count)
