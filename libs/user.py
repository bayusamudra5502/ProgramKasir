"""PUSTAKA USER
Digunakan untuk menambah, menghapus, melihat pengguna, dan 
mengubah password pengguna."""

# Impor Pustaka
import libs.basis_data as db
import sqlite3

def lihatPengguna():
    """Mendapatkan semua data pengguna dari database.
    
    Output:
    Fungsi ini mengeluarkan sebuah list yang setiap
    itemnya merupakan list dengan format [username, password]"""
    # Menyambung dengan database
    conn = db.connect()

    # Mengambil data pengguna dari database
    cmdPengguna = "SELECT * FROM pengguna"
    dataPengguna = conn.execute(cmdPengguna)
    res = []

    # Simpan semua data yang diambil pada list res
    for i in dataPengguna:
        res.append(list(i))

    # Tutup koneksi
    conn.close()

    return res

def editPassword(username, password_lama, password_baru):
    """Mengedit kata sandi pengguna.

    Input:
    Username (string) : Username pengguna yang akan diedit;
    password_lama (string) : Password sebelum diedit;
    password_baru (string) : Password setelah diedit;
    
    return True bila berhasil mengubah password"""
    # Menyambung dengan database
    conn = db.connect()

    # Update password pengguna
    # Jangan terapkan perubahan bila pasangan username dan
    # password lama tidak dditemukan
    cmdEdit = f'UPDATE pengguna SET Password = "{password_baru}" WHERE'+\
              f' Username="{username}" and Password="{password_lama}"'
    conn.execute(cmdEdit)

    # Memeriksa jumlah baris pada database yang berubah.
    conn.commit()
    res = conn.total_changes

    # Tutup koneksi
    conn.close()
    return (res != 0)

def hapusPengguna(username):
    """Menghapus Pengguna

    Username (string) : Nama pengguna yang akan dihapus;

    return True bila berhasil menghapus pengguna"""
    # Menyambung dengan database
    conn = db.connect()

    # Hapus pengguna dengan username sesuai input
    cmdHapus = f"DELETE FROM pengguna WHERE Username='{username}'"
    conn.execute(cmdHapus)

    # Memeriksa jumlah baris pada database yang berubah.
    conn.commit()
    res = conn.total_changes

    # Tutup koneksi
    conn.close()
    return (res != 0)

def tambahPengguna(username, password):
    """Menambah pengguna
    
    Username : Nama pengguna yang akan ditambahkan (Pastikan belum ada);
    Password : Kata Sandi pengguna yang akan ditambahkan;
    
    return True bila berhasil menambah pengguna"""
    # Antisipasi error agar tidak keluar dari program
    try:
        # Menyambbung dengan database
        conn = db.connect()

        # Menambah user baru pada database
        cmdTambah = f"INSERT INTO pengguna (Username, Password) VALUES \
                     ('{username}','{password}')"
        conn.execute(cmdTambah)

        # Melihat perubahan jumlah baris pada database
        conn.commit()
        res = conn.total_changes
    except sqlite3.Error as err:
        # Bila terjadi kesalahan, buatlah output False
        res = 0
    else: 
        # Tutup koneksi database
        conn.close()
    
    return (res != 0)