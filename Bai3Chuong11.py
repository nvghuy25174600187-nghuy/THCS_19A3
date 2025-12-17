s = input("Nhập chuỗi: ")

result = ""
space = False

for ch in s:
    if ch != " ":
        result += ch
        space = False
    else:
        if not space:
            result += " "
            space = True

print(result)
