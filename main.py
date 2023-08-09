import math
from collections import Counter

data = [
    ("Richard", 175, 75, "L"),
    ("Deby", 165, 60, "M"),
    ("Mike", 166, 77, "L"),
    ("Tom", 178, 73, "L"),
    ("Bella", 174, 62, "M"),
    ("Jhon", 169, 68, "M"),
    ("Ann", 168, 64, "M"),
    ("Jack", 170, 70, "L"),
    ("Alea", 160, 65, "?"),
]

def euclidean_distance(titik1, titik2):
    return math.sqrt((titik1[0] - titik2[0])**2 + (titik1[1] - titik2[1])**2)

def cari_tetangga(k, data, target):
    jarak = []
    for item in data:
        jarak.append((euclidean_distance((item[1], item[2]), target), item[3]))
    jarak.sort()
    tetangga = jarak[:k]
    return tetangga

def mayoritas_pilih(tetangga):
    vote_count = Counter(tetangga[1] for tetangga in tetangga)
    return vote_count.most_common(1)[0][0]

alea_data = (160, 65)

K = 3
tetangga_terdekat = cari_tetangga(K, data, alea_data)

alea_size = mayoritas_pilih(tetangga_terdekat)

print(f"Ukuran baju Alea: {alea_size}")