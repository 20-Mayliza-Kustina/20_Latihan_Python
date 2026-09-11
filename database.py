import sqlite3

def database():
    conn = sqlite3.connect("database_fungsi.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database dan tabel 'users' berhasil disiapkan!")

database()
