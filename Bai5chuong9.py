def kiem_tra_so_doi_xung(n):
    return str(n) == str(n)[::-1]

# Test
n = int(input("Nhập n: "))
print(kiem_tra_so_doi_xung(n))
