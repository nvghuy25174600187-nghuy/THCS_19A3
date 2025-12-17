t = tuple(map(int, input().split()))

chan = []
le = []

for x in t:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

print(tuple(chan), sum(chan))
print(tuple(le), sum(le))
