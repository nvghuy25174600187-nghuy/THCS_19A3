ds = [1, 2, 3, 4, 5]

with open("so_nguyen.txt", "w") as f:
    for so in ds:
        f.write(str(so) + "\n")
