def tim_so_le_lon_nhat(a, b, c):
    le = [x for x in (a, b, c) if x % 2 != 0]
    return max(le) if le else -1

# Ví dụ:
print(tim_so_le_lon_nhat(2, 11, 7))
