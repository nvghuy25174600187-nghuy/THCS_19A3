# Bài 5: Tính S1, S2, S3, S4

def tinh_s1(n):
    return (n * (n + 1)) // 2

def tinh_s2(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n):
        result *= i
    return result

def tinh_s3(n):
    S3 = 0
    for k in range(1, n + 1):
        S3 += ((-1) ** (k + 1)) / k
    return S3

def tinh_s4(n):
    S4 = 0
    for k in range(0, n + 1):
        S4 += k / (k + 2)
    return S4

# Nhập n từ người dùng
n = int(input("Nhập n: "))
print(f"S1 = {tinh_s1(n)}")
print(f"S2 = {tinh_s2(n)}")
print(f"S3 = {tinh_s3(n)}")
print(f"S4 = {tinh_s4(n)}")