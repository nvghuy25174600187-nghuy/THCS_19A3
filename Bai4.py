so_tien_VND = float(input("Nhập số tiền bằng VNĐ: "))
ty_gia = 24500

so_tien_USD = so_tien_VND / ty_gia

# Làm tròn đến 2 chữ số thập phân
so_tien_USD_lam_tron = round(so_tien_USD, 2)

print(f"Số tiền sau khi chuyển đổi sang USD (đã làm tròn): {so_tien_USD_lam_tron} USD")