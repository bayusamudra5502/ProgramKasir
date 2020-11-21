## FORM LOGIN
""" Form yang mengatur mengenai segala yang berkaitan dengan
proses login
"""
# Impor pustaka yang digunakan
from libs.library import *
from forms.menu import formMenu

## MODEL
def cekLogin(username, password):
    global PenggunaLogin
    """ Memeriksa apakah pasangan username dan password ada dalam
    database.

    Input:
    Username (string) : Username pengguna
    Password (String) : Kata sandi pengguna

    Output : True bila pasangan username dan password ditemukan
    """
    # Mengambil data pengguna
    matPengguna = lihatPengguna()
    
    # Memeriksa apakah ada data pengguna yang sesuai dengan input
    for i in matPengguna:
        if(i[0] == username and i[1] == password):
            PenggunaLogin[0] = username
            return True
    
    return False

## VIEW
def cetakTampilan(boolKeadaanError = False):
    """ Fungsi ini akan mencetak tampilan dari form login
    Input : boolKeadaanError untuk mengetahui apakah hasil login terakhir 
            error atau tidak.
    Output : Posisi baris terakhir"""

    # Mempersiapkan list errors
    listStrError = warnai("""#########################################################
# ❌ LOGIN GAGAL                                        #
# Oops.. Pasangan Username dan password tidak ditemukan #
#########################################################""", Warna.merah).split("\n")
    
    hapusLayar()
    cetakFrame()
    
    # Mencetak Judul Program
    if not boolKeadaanError:
        printRataTengah((get_terminal_size().lines)// 3, listStrJudul, True)
        return (get_terminal_size().lines)// 3 + 8
    else: # Keadaan error
        printRataTengah((get_terminal_size().lines)// 4, listStrJudul, True)
        printRataTengah((get_terminal_size().lines)// 4 + 8, listStrError, True)
        return (get_terminal_size().lines)// 4 + 13

def inputPengguna(posisi_baris):
    """Mengambil input pengguna.

    Input : Posisi baris memulai pengambilan input
    Output : Bila login berhasil, cetak True"""

    listStrPesan = """-----------------------------------------------------
⚠️ Perhatian!
Isilah Username dan Password yang sudah terdaftar
-----------------------------------------------------""".split("\n")

    # Mencetak pesan
    printRataTengah(posisi_baris, listStrPesan, True)

    # Mengambil data username
    pindahkanKursor(posisi_baris + 5, (get_terminal_size().columns)// 4)
    strUname = input("Username : ")

    # Mengambil data password
    pindahkanKursor(posisi_baris + 6, (get_terminal_size().columns)// 4)
    strPasswd = inputPassword("Password : ")
    
    return cekLogin(strUname,strPasswd)

## CONTROLLER
def formLogin():
    boolSudahLogin = False
    boolSalah = False

    # Lakukan proses login selama belum berhasil
    while(not boolSudahLogin):
        boolSudahLogin = inputPengguna(cetakTampilan(boolSalah))
        boolSalah = not boolSudahLogin
    
    # Bila login berhasil, buka menu utama
    formMenu()