id_can_sua = input("Nhập ID: ")
gia_moi = input("Nhập giá mới: ")

with open("san_pham.txt", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith(id_can_sua + ","):
        parts = line.strip().split(", ")
        parts[2] = gia_moi
        line = ", ".join(parts) + "\n"
    new_lines.append(line)

with open("san_pham.txt", "w") as f:
    f.writelines(new_lines)
