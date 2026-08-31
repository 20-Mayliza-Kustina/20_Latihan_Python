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
