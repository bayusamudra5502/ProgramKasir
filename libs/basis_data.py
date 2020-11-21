"""PUSTAKA BASIS DATA

File ini untuk menyambungkan program dengan database."""

# Impor Library
import sqlite3

def connect():
    """Menghasilkan Koneksi terhadap database
    
    Output : Objek Koneksi"""
    objDB = None

    # Mencegah error karena koneksi.
    try:
        objDB = sqlite3.connect("database.db")
    except sqlite3.Error as err:
        # Bila error, tuliskan penyebabnya
        print(err)
    
    return objDB