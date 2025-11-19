# Bài 4: Tìm tất cả số nguyên tố nhỏ hơn n

def kiem_tra_ngto(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Nhập số từ người dùng
n = int(input("Nhập số nguyên dương n: "))
print(f"Các số nguyên tố nhỏ hơn {n} là:")
for i in range(2, n):
    if kiem_tra_ngto(i):
        print(i, end=' ')
print()