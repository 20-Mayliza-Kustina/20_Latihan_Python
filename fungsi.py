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
                
