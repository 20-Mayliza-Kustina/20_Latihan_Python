from fungsi import register_user, login_user, cek_ganjil_genap, cek_huruf_vokal, cek_huruf_konsonan, cek_merubah_capslock

while True:
    import fungsi
    
    print("PROGRAM UTAMA")
    print("1.register \n2.login")
    user_input = input("Masukkan pilihan (1/2): ")
    print()
    
    if user_input == "1":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print(register_user(username, password))
    elif user_input == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if login_user(username, password):
            print("Login berhasil!")
        else:
            print("Login gagal!")
    if user_input == "3":
        angka = int(input("Ganjil Genap\nMasukkan angka = "))
        print(fungsi.cek_ganjil_genap(angka))
    if user_input == "4":
        huruf = input("huruf vokal\nMasukkan huruf = ")
        print(fungsi.cek_huruf_vokal(huruf))
    if user_input == "5":
        huruf = input("huruf konsonan\nMasukkan huruf = ")
        print(fungsi.cek_huruf_konsonan(huruf))
    if user_input == "6":
        teks = input("merubah capslock\nMasukkan teks = ")
        print(fungsi.cek_merubah_capslock(teks))
    pilihan = input("Lajut atau Sudah? (oke/selesai): ")
 
    if pilihan == "selesai":
        print("okeee program selesai, terimakasih, semangatt")
        break
