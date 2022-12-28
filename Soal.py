angka = int(input('Masukkan angka : '))
 
hit = 1
for i in range(angka):
    for j in range(i+1):
        print(hit,' ',end='')
    hit+=1
    print()