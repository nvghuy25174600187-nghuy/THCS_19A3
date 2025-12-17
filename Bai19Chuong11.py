d = eval(input())
result = {}

for name in d:
    score = d[name]
    if score not in result:
        result[score] = [name]
    else:
        result[score].append(name)

print(result)
