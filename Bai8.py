# Nhập cân nặng và chiều cao
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

# Tính BMI
bmi = can_nang / (chieu_cao ** 2)

# In kết quả làm tròn 2 chữ số thập phân
print("Chỉ số BMI của bạn là:", round(bmi, 2))
