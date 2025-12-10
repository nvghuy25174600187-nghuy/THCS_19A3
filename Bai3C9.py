def kiem_tra_so_armstrong(n):
    s = str(n)
    tong = sum(int(x)**3 for x in s)
    return tong == n

# Ví dụ:
print(kiem_tra_so_armstrong(153))
