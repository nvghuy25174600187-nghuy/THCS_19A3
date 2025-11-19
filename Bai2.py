# Bài 2: Tìm ước chung lớn nhất

def ucln(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

# Nhập hai số từ người dùng
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
print(f"ƯCLN của {a} và {b} là: {ucln(a, b)}")