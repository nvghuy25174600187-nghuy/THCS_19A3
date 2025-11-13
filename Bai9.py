# Nhập số kWh
so_kwh = float(input("Nhập số kWh điện đã tiêu thụ: "))

# Tính tiền điện theo bậc
if so_kwh <= 100:
    tien_dien = so_kwh * 1678
elif so_kwh <= 200:
    tien_dien = 100 * 1678 + (so_kwh - 100) * 1734
elif so_kwh <= 300:
    tien_dien = 100 * 1678 + 100 * 1734 + (so_kwh - 200) * 2014
else:
    # Nếu muốn xử lý >300 kWh
    tien_dien = 100 * 1678 + 100 * 1734 + 100 * 2014 + (so_kwh - 300) * 2500

# In kết quả làm tròn 2 chữ số thập phân
print("Tổng tiền điện phải trả:", round(tien_dien, 2), "VNĐ")
