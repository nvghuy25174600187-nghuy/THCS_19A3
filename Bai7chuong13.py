import os

os.makedirs("test/child", exist_ok=True)
open("test/file1.txt", "w").close()

print(os.listdir("test"))
