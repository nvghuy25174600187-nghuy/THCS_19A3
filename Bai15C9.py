def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def kiem_tra_nguyen_to(n):
    return la_so_nguyen_to(n)

def in_nguyen_to_100_500():
    for i in range(100, 500):
        if la_so_nguyen_to(i):
            print(i, end=" ")

# Ví dụ:
print(kiem_tra_nguyen_to(17))
in_nguyen_to_100_500()
