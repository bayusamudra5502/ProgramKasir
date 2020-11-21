## FORM LOGIN
""" Form yang mengatur mengenai segala yang berkaitan dengan
proses login
"""
from libs.library import *
from forms.menu import formMenu

## MODEL
def cekLogin(username, password):
    global PenggunaLogin
    """ Memeriksa apakah pasangan username dan password ada dalam
    database.
    """
    matPengguna = lihatPengguna()

    for i in matPengguna:
        if(i[0] == username and i[1] == password):
            PenggunaLogin[0] = username
            return True
    
    return False

## VIEW
def cetakTampilan(boolKeadaanError = False):
    """ Fungsi ini akan mencetak tampilan dari form login menghasilkan posisi baris terakhir"""

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
    """Mengambil input pengguna"""
    listStrPesan = """-----------------------------------------------------
⚠️ Perhatian!
Isilah Username dan Password yang sudah terdaftar
-----------------------------------------------------""".split("\n")

    printRataTengah(posisi_baris, listStrPesan, True)
    pindahkanKursor(posisi_baris + 5, (get_terminal_size().columns)// 4)
    strUname = input("Username : ")
    pindahkanKursor(posisi_baris + 6, (get_terminal_size().columns)// 4)
    strPasswd = inputPassword("Password : ")
    return cekLogin(strUname,strPasswd)

## CONTROLLER
def formLogin():
    boolSudahLogin = False
    boolSalah = False

    while(not boolSudahLogin):
        boolSudahLogin = inputPengguna(cetakTampilan(boolSalah))
        boolSalah = not boolSudahLogin
    
    formMenu()