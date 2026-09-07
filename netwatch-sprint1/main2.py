while True:
    import fungsi
    
    print("Menu Modul")
    print("1.ganjil genap\n2.huruf vokal\n3.huruf konsonan\n4. merubah capslock")
    print()
    
    a = int(input("No = "))
    
    if a == 1:
        angka = int(input("Ganjil Genap\nMasukkan angka = "))
        print(fungsi.cek_ganjil_genap(angka))
    if a == 2:
        huruf = input("huruf vokal\nMasukkan huruf = ")
        print(fungsi.cek_huruf_vokal(huruf))
    if a == 3:
        huruf = input("huruf konsonan\nMasukkan huruf = ")
        print(fungsi.cek_huruf_konsonan(huruf))
    if a == 4:
        teks = input("merubah capslock\nMasukkan teks = ")
        print(fungsi.cek_merubah_capslock(teks))
    pilihan = input("Lajut atau Sudah? (oke/selesai): ")
 
    if pilihan == "selesai":
        print("okeee program selesai, terimakasih, semangatt")
        break

    
     


