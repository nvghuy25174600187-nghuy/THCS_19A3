n = int(input())
m = int(input())
p = int(input())

A = []
B = []

for i in range(n):
    A.append(list(map(int, input().split())))

for i in range(m):
    B.append(list(map(int, input().split())))

C = [[0]*p for _ in range(n)]

for i in range(n):
    for j in range(p):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)
