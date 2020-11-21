"""LIBRARY BARANG

Library ini akan digunakan dalam mengambil, mengubah, 
menghapus, menambah data barang"""

# Impor library
import libs.basis_data as db
import sqlite3

def lihatBarang():
    """Mendapatkan semua data pengguna dari database
    
    Output: List yang tiap itemnya memiliki pola
    Indeks 0 = Kode Barang
    Indeks 1 = Nama Barang
    Indeks 2 = Stock
    Indeks 3 = Harga"""
    # Meyambungkan ke database
    conn = db.connect()

    # Mengambil data dari database
    cmdPengguna = "SELECT * FROM barang"
    dataPengguna = conn.execute(cmdPengguna)
    res = []

    # Menyimpan hasil dari pengambilan data dalam list
    for i in dataPengguna:
        res.append(list(i))

    # Menutup koneksi
    conn.close()
    return res

def editBarang(Kode_Barang, Nama_Barang = None,\
               Stock = None, Harga = None):
    """Mengedit data barang.

    Input :
    Kode_Barang : Kode barang yang akan diedit;
    Nama_Barang : Nama barang baru dari barang yang akan diedit (Opsional);
    Stock: Jumlah stok barang yang baru dari barang yang diedit (Opsional);
    Harga : Harga baru dari barang yang akan diedit (Opsional);

    OUTPUT: True bila berhasil mengedit barang"""
    # Membuat koneksi terhadap database
    conn = db.connect()

    # Mengedit data yang dibutuhkan pada database
    cmdEdit = f"UPDATE barang SET "
    cmdList = []
    if Nama_Barang != None:
        cmdList.append(f"Nama_Barang = '{Nama_Barang}'")
    if Stock != None:
        cmdList.append(f"Stok = {Stock}")
    if  Harga != None:
        cmdList.append(f"Harga = {Harga} ")
    
    cmdEdit += ",".join(cmdList) + f" WHERE Kode_Barang = '{Kode_Barang}'"

    conn.execute(cmdEdit)

    # Memeriksa jumlah baris pada database yang berubah.
    # Simpan perubahan jumlah baris pada res.
    conn.commit()
    res = conn.total_changes

    # Tutup koneksi
    conn.close()
    return (res != 0)

def hapusBarang(Kode_Barang):
    """Menghapus Barang

    Input:
    Kode_Barang : Kode Barang yang akan dihapus;

    Output : True bila berhasil menghapus barang"""
    # Menyambungkan dengan database
    conn = db.connect()

    # Menghapus data pada database
    cmdHapus = f"DELETE FROM barang WHERE Kode_Barang='{Kode_Barang}'"
    conn.execute(cmdHapus)

    # Memeriksa jumlah baris pada database yang berubah.
    # Simpan perubahan jumlah baris pada res.
    conn.commit()
    res = conn.total_changes

    # Tutup koneksi
    conn.close()
    return (res != 0)

def tambahBarang(Kode_Barang, Nama_Barang, Jumlah_Stock, Harga):
    """Menambah barang
    
    Input :
    Kode_Barang : Kode barang yang akan ditambahkan;
    Nama_Barang : Nama barang yang akan ditambahkan;
    Jumlah_Stock: Jumlah stok barang yang akan ditambahkan;
    Harga : Harga dari barang yang akan dtambahkan;
    
    Output : True bila berhasil menambah barang.
    Jika gagal keluarkan False"""
    
    # Jaga-jaga jika gagal menambah data pada database
    try:
        # Membuat koneksi dengan database
        conn = db.connect()

        # Mennambahkan data pada database
        cmdTambah = f"INSERT INTO barang (Kode_Barang, Nama_Barang,Stok,Harga) VALUES \
                     ('{Kode_Barang}','{Nama_Barang}','{Jumlah_Stock}','{Harga}')"
        conn.execute(cmdTambah)

        # Ambil perubahan jumlah baris
        conn.commit()
        res = conn.total_changes
    except sqlite3.Error as err:
        res = 0
    else: 
        conn.close()
    
    return (res != 0)
