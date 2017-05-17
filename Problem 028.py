total = 1
current = 1
scaler = 2
for _ in range(500):
    for __ in range(4):
        current += scaler
        total += current
    scaler += 2

print(total)