angka = int(input("Masukkan angka: "))
# Menggunakan pembagian bulat (//) dan perkalian (*)
if (angka // 2) * 2 == angka:
    print("GENAP")
else:
    print("GANJIL")
    
while True:
    print("\n--- Program Cek Genap/Ganjil ---")
    input_user = input("Masukkan angka (ketik 'exit' untuk keluar): ")

    # Cek apakah pengguna ingin menghentikan program
    if input_user.lower() == 'exit':
        print("yeyyyy! program selesai.")
        break

    # Memastikan input berupa angka bulat
    try:
        angka = int(input_user)
        
        # Logika pembagian bulat dan perkalian
        if (angka // 2) * 2 == angka:
            print("-> GENAP")
        else:
            print("-> GANJIL")
            
    except ValueError:
        print("Input tidak valid! Harap masukkan angka bulat.\n")
        
print("-----------------------------fungsi----------------------------------")

def cek_ganjil_genap(angka):
            # Menggunakan pembagian bulat (//) dan perkalian (*)
            if (angka // 2) * 2 == angka:
                print("GENAP")
            else:
                print("GANJIL")
        
print("------------------------------------------------------------------------")

def cek_bilangan_prima (angka):
            if angka < 2:
                print("Bukan bilangan prima")
                return
            for i in range(2, int(angka**0.5) + 1):
                if angka % i == 0:
                    print("Bukan bilangan prima")
                    return
                print ("Bilangan prima")