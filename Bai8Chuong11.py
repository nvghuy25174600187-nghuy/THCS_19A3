a = list(map(int, input().split()))
k = int(input())

n = len(a)
k = k % n
b = [0] * n

for i in range(n):
    b[(i + k) % n] = a[i]

print(b)
