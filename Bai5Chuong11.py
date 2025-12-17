a = list(map(int, input().split()))
b = []

for x in a:
    found = False
    for y in b:
        if x == y:
            found = True
            break
    if not found:
        b.append(x)

print(b)
