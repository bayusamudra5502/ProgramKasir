## FORM PENGGUNA
""" Form yang mengatur mengenai pengguna
"""

from libs.library import *

# Daftar username pengguna yang ada
listUsername = [i[0] for i in lihatPengguna()]

# Gunakan fungsi berikut untuk memudahkan:
# editPassword(username, password_lama, password_baru)
#    Mengedit password pengguna. Password_lama adalah password
#    pengguna yg dimaksud sebelum diubah. password_baru adalah
#    password pengguna setelah diubah
#
# hapusPengguna(username)
#   Mengapus pengguna dengan username tertentu. Pastikan pengguna
#   yang dihapus bukanlah pengguna yang aktif saat ini. Cek dengan
#   melihat apakan username yang hedak dihapus sama dengan 
#   strPenggunaLogin?
#
# tambahPengguna(username, password)
#   Menambah pengguna baru, dengan username dan password  tertentu
#
# inputPassword(prompt)
#   Seperti input biasa, hanya saja seperti kita menginput password
#   di browser, sehingga hasil inputannya tidak terlihat.

def formPengguna():
    """Fungsi untuk menampilkan form pengguna.
    
    Form pengguna akan berisi komponen untuk melihat semua
    pengguna yang ada, mengedit kata sandi pengguna, dan
    menghapus pengguna."""
    hapusLayar()
    pass