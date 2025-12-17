n = int(input())
m = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

max_sum = -10**18
row = 0

for i in range(n):
    s = 0
    for j in range(m):
        s += a[i][j]
    if s > max_sum:
        max_sum = s
        row = i

print("Hàng:", row)
