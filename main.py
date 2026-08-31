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
        
        # Logika pembagian bulat dan perkalian milikmu
        if (angka // 2) * 2 == angka:
            print("-> GENAP")
        else:
            print("-> GANJIL")
            
    except ValueError:
        print("Input tidak valid! Harap masukkan angka bulat.\n")
print("========================== FUNGSI OLAH KATA ================================")
def cek_ganjil_genap(angka):
            # Menggunakan pembagian bulat (//) dan perkalian (*)
            if (angka // 2) * 2 == angka:
                print("GENAP")
            else:
                print("GANJIL")
                
def cek_huruf_vokal(huruf):
            if huruf.lower() in ['a', 'e', 'i', 'o', 'u']:
                print("huruf vokal")
            else:
                print("bukan huruf vokal")
                
def cek_huruf_konsonan(huruf):
            if huruf.lower() not in ['a', 'e', 'i', 'o', 'u'] and huruf.isalpha():
                print("huruf konsonan")
            else:
                print("bukan huruf konsonan")
def cek_merubah_capslock(teks):
            if teks.isupper():
                print(teks.lower())
            else:
                print(teks.upper())
                
while True:
    import fungsi
    
    print("Menu Modul")
    print("1.ganjil genap\n2.huruf vokal\n3.huruf konsonan\n4. merubah capslock")
    print()
    a = int(input("No = "))
    if a == 1:
        print(fungsi.cek_ganjil_genap(print("ganjil genap /nMasukkan angka = ")))
    if a == 2:
        print(fungsi.cek_huruf_vokal(print("huruf vokal /nMasukkan huruf = ")))
    if a == 3:
        print(fungsi.cek_huruf_konsonan(print("huruf konsonan /nMasukkan huruf = ")))
    if a == 4:
        print(fungsi.cek_merubah_capslock(print("merubah capslock /nMasukkan teks = ")))
    pilihan = input("terus atau berhenti? (terus/berhenti): ")
 
    if pilihan == "berhenti":
        print("program selesai, terimakasih")
        break
