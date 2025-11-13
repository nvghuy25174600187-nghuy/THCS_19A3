# Nhập dữ liệu
tien_goc = float(input("Nhập số tiền gửi ban đầu (VNĐ): "))
lai_suat_nam = float(input("Nhập lãi suất năm (%): "))

# Đổi phần trăm sang số thập phân
lai_suat = lai_suat_nam / 100

# Tính lãi đơn
lai_1_thang = tien_goc * lai_suat * (1/12)
lai_2_quy = tien_goc * lai_suat * (6/12)
lai_3_nam = tien_goc * lai_suat * 3

# In kết quả
print("Tiền lãi sau 1 tháng:", round(lai_1_thang, 2), "VNĐ")
print("Tiền lãi sau 2 quý:", round(lai_2_quy, 2), "VNĐ")
print("Tiền lãi sau 3 năm:", round(lai_3_nam, 2), "VNĐ")
