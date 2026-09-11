import sqlite3

def register_user(username, password):
    try:
        conn = sqlite3.connect("database_fungsi.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return "Registrasi berhasil!"
    except sqlite3.IntegrityError:
        return "Username kamu sudah terdaftar!"

def login_user(username, password):
    conn = sqlite3.connect("database_fungsi.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user is not None:
        return True  
    else:
        return False
def cek_ganjil_genap(angka):
            # Menggunakan pembagian bulat (//) dan perkalian (*)
            if (angka // 2) * 2 == angka:
                return "GENAP"
            else:
                return "GANJIL"

def cek_huruf_vokal(huruf):
            if huruf.lower() in ['a', 'e', 'i', 'o', 'u']:
                return "huruf vokal"
            else:
                return "bukan huruf vokal"

def cek_huruf_konsonan(huruf):
            if huruf.lower() not in ['a', 'e', 'i', 'o', 'u'] and huruf.isalpha():
                return "huruf konsonan"
            else:
                return "bukan huruf konsonan"

def cek_merubah_capslock(teks):
            if teks.isupper():
                return teks.lower()
            else:
                return teks.upper()
                
