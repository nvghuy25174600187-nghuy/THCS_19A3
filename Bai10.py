# Nhập dữ liệu
luong_co_ban = float(input("Nhập lương cơ bản (VNĐ): "))
so_ngay_cong = int(input("Nhập số ngày công trong tháng: "))

# Tính lương một ngày
luong_mot_ngay = luong_co_ban / 22

# Tính tiền thưởng hoặc tiền phạt
tien_thuong = 0
tien_phat = 0

if so_ngay_cong > 22:
    tien_thuong = 0.1 * luong_co_ban
elif so_ngay_cong < 22:
    tien_phat = 0.05 * luong_co_ban

# Tính tổng lương thực nhận
tong_luong = luong_mot_ngay * so_ngay_cong + tien_thuong - tien_phat

# In kết quả, làm tròn 2 chữ số thập phân
print("Tổng lương thực nhận:", round(tong_luong, 2), "VNĐ")
