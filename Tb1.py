import re

# Baca input dimensi
N, M = map(int, input().split())

# Baca baris matriks
matrix = [input() for _ in range(N)]

# Dekode script dengan membaca kolom demi kolom
decoded_script = ""
for col in range(M):
    for row in range(N):
        decoded_script += matrix[row][col]

# Gunakan regular expression untuk mengganti urutan karakter non-alfanumerik dengan satu spasi
decoded_script = re.sub(r'\b[^a-zA-Z0-9]+\b', ' ', decoded_script)

# Cetak hasil decoded script
print(decoded_script)
