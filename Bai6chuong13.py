import csv

with open("nhan_vien.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["Lương"]) > 50000:
            print(row)
