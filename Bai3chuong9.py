def kiem_tra_so_armstrong(n):
    s = sum(int(ch)**3 for ch in str(n))
    return s == n

# Test
n = int(input("Nhập n: "))
print(kiem_tra_so_armstrong(n))
