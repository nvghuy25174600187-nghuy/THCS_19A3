a = list(map(int, input().split()))

max1 = -10**18
max2 = -10**18

for x in a:
    if x > max1:
        max2 = max1
        max1 = x
    elif x != max1 and x > max2:
        max2 = x

print(max2)
