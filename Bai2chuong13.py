from collections import Counter

with open("vanban.txt", "r", encoding="utf-8") as f:
    words = f.read().split()

tan_suat = Counter(words)

for tu, so_lan in tan_suat.items():
    print(tu, ":", so_lan)
