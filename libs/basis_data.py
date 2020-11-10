import sqlite3

def connect():
    """Menghasilkan Koneksi terhadap database """
    objDB = None
    try:
        objDB = sqlite3.connect("database.db")
    except sqlite3.Error as err:
        print(err)
    
    return objDB