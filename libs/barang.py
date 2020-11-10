import libs.basis_data as db
import sqlite3

def lihatBarang():
    """Mendapatkan semua data pengguna dari database"""
    conn = db.connect()
    cmdPengguna = "SELECT * FROM barang"
    dataPengguna = conn.execute(cmdPengguna)
    res = []

    for i in dataPengguna:
        res.append(list(i))

    conn.close()

    return res

def editBarang(Kode_Barang, Nama_Barang = None,\
               Stock = None, Harga = None):
    """Mengedit data barang.

    Kode_Barang : Kode barang yang akan diedit;
    Nama_Barang : Nama barang baru dari barang yang akan diedit (Opsional);
    Stock: Jumlah stok barang yang baru dari barang yang diedit (Opsional);
    Harga : Harga baru dari barang yang akan diedit (Opsional);

    return True bila berhasil mengedit barang"""

    conn = db.connect()
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
    conn.commit()
    res = conn.total_changes

    conn.close()
    return (res != 0)

def hapusBarang(Kode_Barang):
    """Menghapus Barang

    Kode_Barang : Kode Barang yang akan dihapus;

    return True bila berhasil menghapus barang"""
    conn = db.connect()
    cmdHapus = f"DELETE FROM barang WHERE Kode_Barang='{Kode_Barang}'"
    conn.execute(cmdHapus)
    conn.commit()
    res = conn.total_changes

    conn.close()
    return (res != 0)

def tambahBarang(Kode_Barang, Nama_Barang, Jumlah_Stock, Harga):
    """Menambah barang
    
    Kode_Barang : Kode barang yang akan ditambahkan;
    Nama_Barang : Nama barang yang akan ditambahkan;
    Jumlah_Stock: Jumlah stok barang yang akan ditambahkan;
    Harga : Harga dari barang yang akan dtambahkan;
    
    return True bila berhasil menambah barang"""
    
    try:
        conn = db.connect()
        cmdTambah = f"INSERT INTO barang (Kode_Barang, Nama_Barang,Stok,Harga) VALUES \
                     ('{Kode_Barang}','{Nama_Barang}','{Jumlah_Stock}','{Harga}')"
        conn.execute(cmdTambah)
        conn.commit()
        res = conn.total_changes
    except sqlite3.Error as err:
        res = 0
    else: 
        conn.close()
    
    return (res != 0)