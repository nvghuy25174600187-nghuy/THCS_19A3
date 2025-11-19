# Bài 3: Tối giản phân số

def ucln(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

# Nhập tử số và mẫu số
tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
if mau_so == 0:
    print("Phân số không xác định (mẫu số bằng 0).")
else:
    gcd = ucln(abs(tu_so), abs(mau_so))
    tu_so_toi_gian = tu_so // gcd
    mau_so_toi_gian = mau_so // gcd
    if mau_so_toi_gian < 0:
        tu_so_toi_gian = -tu_so_toi_gian
        mau_so_toi_gian = -mau_so_toi_gian
    print(f"Phân số tối giản là: {tu_so_toi_gian}/{mau_so_toi_gian}")