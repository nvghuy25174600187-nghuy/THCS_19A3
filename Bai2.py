# BAI 2: CHIA KEO CHO HOC SINH

# Nhập tổng số kẹo
tong_keo = int(input("Nhập tổng số kẹo: "))

# Nhập số học sinh
so_hoc_sinh = int(input("Nhập số học sinh: "))

# Tính số kẹo mỗi học sinh nhận
keo_moi_hs = tong_keo // so_hoc_sinh  # chia lấy nguyên

# Tính số kẹo còn thừa
keo_con_thua = tong_keo % so_hoc_sinh  # chia lấy dư

# In kết quả
print("Mỗi học sinh nhận được:", keo_moi_hs, "kẹo")
print("Số kẹo còn thừa:", keo_con_thua, "kẹo")

