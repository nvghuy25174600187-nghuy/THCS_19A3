d = eval(input())
x = int(input())

new_d = {}
for k in d:
    if d[k] > x:
        new_d[k] = d[k]

print(new_d)
