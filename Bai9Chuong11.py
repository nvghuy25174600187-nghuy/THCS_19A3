n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

tong = 0
for i in range(n):
    tong += a[i][n - 1 - i]

print(tong)
