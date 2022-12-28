def l_persegi(s):
    return s*s
def k_persegi(s):
    return 4*s

print("=== Menghitung Luas dan Keliling Persegi ===")
print("1. Luas Persegi")
print("2. Keliling Persegi")
pil = int(input("Masukkan pilihan : "))
sisi = int(input("Masukkan sisi : "))

if pil == 1:
    print(f"Luas Persegi adalah : {l_persegi(sisi)}")
elif pil == 2:
    print(f"Keliling Persegi adalah : {k_persegi(sisi)}")