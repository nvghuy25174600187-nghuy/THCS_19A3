with open("vanban.txt", "w", encoding="utf-8") as f:
    f.write("Python là một ngôn ngữ lập trình mạnh mẽ...")

with open("vanban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

print("Số từ:", len(noi_dung.split()))
