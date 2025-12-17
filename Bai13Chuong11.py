n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

don_vi = True
for i in range(n):
    for j in range(n):
        if (i == j and a[i][j] != 1) or (i != j and a[i][j] != 0):
            don_vi = False

print(don_vi)
