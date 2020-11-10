import lib.basis_data as db
import sqlite3

def lihatPengguna():
    """Mendapatkan semua data pengguna dari database"""
    conn = db.connect()
    cmdPengguna = "SELECT * FROM pengguna"
    dataPengguna = conn.execute(cmdPengguna)
    res = []

    for i in dataPengguna:
        res.append(list(i))

    conn.close()

    return res

def editPassword(username, password_lama, password_baru):
    """Mengedit kata sandi pengguna.

    Username : Username pengguna yang akan diedit;
    password_lama : Password sebelum diedit;
    password_baru : Password setelah diedit;
    
    return True bila berhasil mengubah password"""

    conn = db.connect()
    cmdEdit = f'UPDATE pengguna SET Password = "{password_baru}" WHERE'+\
              f' Username="{username}" and Password="{password_lama}"'
    conn.execute(cmdEdit)
    conn.commit()
    res = conn.total_changes

    conn.close()
    return (res != 0)

def hapusPengguna(username):
    """Menghapus Pengguna

    Username : Nama pengguna yang akan dihapus;

    return True bila berhasil menghapus pengguna"""
    conn = db.connect()
    cmdHapus = f"DELETE FROM pengguna WHERE Username='{username}'"
    conn.execute(cmdHapus)
    conn.commit()
    res = conn.total_changes

    conn.close()
    return (res != 0)

def tambahPengguna(username, password):
    """Menambah pengguna
    
    Username : Nama pengguna yang akan ditambahkan (Pastikan belum ada);
    Password : Kata Sandi pengguna yang akan ditambahkan;
    
    return True bila berhasil menambah pengguna"""

    try:
        conn = db.connect()
        cmdTambah = f"INSERT INTO pengguna (Username, Password) VALUES \
                     ('{username}','{password}')"
        conn.execute(cmdTambah)
        conn.commit()
        res = conn.total_changes
    except sqlite3.Error as err:
        res = 0
    else: 
        conn.close()
    
    return (res != 0)