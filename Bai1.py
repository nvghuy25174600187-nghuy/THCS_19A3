# BAI 1: TINH TONG CHI PHI VA THUE VAT (10%)

# Nhập giá sản phẩm từ bàn phím
gia_san_pham = float(input("Nhập giá sản phẩm (VNĐ): "))

# Nhập số lượng mua từ bàn phím
so_luong = int(input("Nhập số lượng mua: "))

# Tính tổng chi phí
tong_chi_phi = gia_san_pham * so_luong

# Tính thuế VAT (10%)
thue_vat = tong_chi_phi * 0.1

# Tính tổng tiền phải trả
tong_tien = tong_chi_phi + thue_vat

# In kết quả, làm tròn đến 2 chữ số thập phân
print("Tổng chi phí:", round(tong_chi_phi, 2), "VNĐ")
print("Thuế VAT (10%):", round(thue_vat, 2), "VNĐ")
print("Tổng tiền phải trả:", round(tong_tien, 2), "VNĐ")
