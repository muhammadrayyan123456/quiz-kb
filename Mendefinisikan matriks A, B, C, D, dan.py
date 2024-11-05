# Versi menggunakan pustaka NumPy
import numpy as np

# Definisikan matriks A, B, C, D, dan E
A = np.array([[3, 0], [-1, 2], [1, 1]])
B = np.array([[4, -1], [0, 2]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

# Perkalian Matriks A * C
hasil_A_C = np.dot(A, C)

# Modifikasi A menjadi matriks 3x3 dengan menambahkan kolom nol agar dapat dikalikan dengan D
A_modifikasi = np.hstack((A, np.zeros((3, 1), dtype=int)))
hasil_A_D = np.dot(A_modifikasi, D)

# Penjumlahan dan Pengurangan Matriks D + E dan D - E
hasil_D_plus_E = D + E
hasil_D_minus_E = D - E

print("Hasil A * C:\n", hasil_A_C)
print("Hasil A * D (dengan modifikasi):\n", hasil_A_D)
print("Hasil D + E:\n", hasil_D_plus_E)
print("Hasil D - E:\n", hasil_D_minus_E)


# Versi tanpa pustaka (NumPy)
# Fungsi untuk melakukan perkalian matriks
def perkalian_matriks(X, Y):
    baris_X = len(X)
    kolom_X = len(X[0])
    kolom_Y = len(Y[0])
    hasil = [[0 for _ in range(kolom_Y)] for _ in range(baris_X)]
    for i in range(baris_X):
        for j in range(kolom_Y):
            for k in range(kolom_X):
                hasil[i][j] += X[i][k] * Y[k][j]
    return hasil

# Fungsi untuk menambahkan dua matriks
def tambah_matriks(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Fungsi untuk mengurangi dua matriks
def kurang_matriks(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

# Matriks A dengan kolom tambahan untuk perkalian dengan D
A_modifikasi = [row + [0] for row in A]

# Hitung hasil operasi
hasil_A_C_no_numpy = perkalian_matriks(A, C)
hasil_A_D_no_numpy = perkalian_matriks(A_modifikasi, D)
hasil_D_plus_E_no_numpy = tambah_matriks(D, E)
hasil_D_minus_E_no_numpy = kurang_matriks(D, E)

print("\nHasil A * C tanpa NumPy:\n", hasil_A_C_no_numpy)
print("Hasil A * D (dengan modifikasi) tanpa NumPy:\n", hasil_A_D_no_numpy)
print("Hasil D + E tanpa NumPy:\n", hasil_D_plus_E_no_numpy)
print("Hasil D - E tanpa NumPy:\n", hasil_D_minus_E_no_numpy)