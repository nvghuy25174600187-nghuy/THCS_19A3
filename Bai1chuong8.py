# Bài 1: Kiểm tra số chính phương

def kiem_tra_so_chinh_phuong(num):
    if num < 0:
        return False
    sqrt_num = int(num**0.5)
    return sqrt_num * sqrt_num == num

# Nhập số từ người dùng
n = int(input("Nhập số nguyên dương: "))
if kiem_tra_so_chinh_phuong(n):
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")