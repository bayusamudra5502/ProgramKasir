## FORM MAIN
""" Form yang mengatur mengenai segala yang berkaitan dengan
menu utama dari program
"""

from libs.library import *
from forms.barang import *
from forms.loading import *
from forms.pembelanjaan import *
from forms.pengguna import *

# Gunakan fungsi ini untuk memudahkan anda:
# hapusLayar() : Untuk membersihkan layar
# formBarang() : Membuka form barang
# formPembelanjaan() : Membuka form pembelanjaan
# formPengguna() : Membuka form pengguna

def formMenu():
    global PenggunaLogin
    """Fungsi ini akan form Menu.
    
    Form menu berperan untuk menjadi perantara antara berbagai
    form yang ada pada program, seperti form barang, form pengguna,
    dan form penjualan.
    """
    cetakHeader()

    intPos = 1
    boolSelesai = False
    while not boolSelesai:
        printRataTengah((get_terminal_size().lines)// 4 + 13, [" " * 50])
        if intPos == 1:
            printRataTengah((get_terminal_size().lines)// 4 + 13, [colored("• Buka Form Barang", Warna.cyan)])
        else:
            printRataTengah((get_terminal_size().lines)// 4 + 13, [colored("Buka Form Barang", Warna.putih)])
        printRataTengah((get_terminal_size().lines)// 4 + 14, [" " * 50])
        if intPos == 2:
            printRataTengah((get_terminal_size().lines)// 4 + 14, [colored("• Buka Form Kasir", Warna.cyan)])
        else:
            printRataTengah((get_terminal_size().lines)// 4 + 14, [colored("Buka Form Kasir", Warna.putih)])
        printRataTengah((get_terminal_size().lines)// 4 + 15, [" " * 50])
        if intPos == 3:
            printRataTengah((get_terminal_size().lines)// 4 + 15, [colored("• Buka Form Pengguna", Warna.cyan)])
        else:
            printRataTengah((get_terminal_size().lines)// 4 + 15, [colored("Buka Form Pengguna", Warna.putih)])
        printRataTengah((get_terminal_size().lines)// 4 + 16, [" " * 50])
        if intPos == 4:
            printRataTengah((get_terminal_size().lines)// 4 + 16, [colored("• Keluar", Warna.cyan)])
        else:
            printRataTengah((get_terminal_size().lines)// 4 + 16, [colored("Keluar", Warna.putih)])
        
        printRataTengah((get_terminal_size().lines)// 4 + 18, ["Tekan " + colored("KEYUP", Warna.kuning) 
                            + " dan " + colored("KEYDOWN ", Warna.kuning) +"untuk menggerakan pilihan"])
        printRataTengah((get_terminal_size().lines)// 4 + 19, ["Tekan " + colored("ENTER", Warna.kuning) + " untuk memilih pilihan"])

        x = msvcrt.getch()
        if(x == b'\x00' or x == b'\xe0'):
            y = msvcrt.getch()
            if y == b'H':
                if intPos > 1:
                    intPos -= 1
            elif y == b"P":
                if intPos < 4:
                    intPos += 1
        elif(x == b"\r" or x == b"\n"):
            if (intPos == 1) :
                formBarang()
                cetakHeader()
            elif (intPos == 2) :
                formPembelanjaan()
                cetakHeader()
            elif (intPos == 3) :
                formPengguna()
                cetakHeader()
            elif (intPos == 4) :
                hapusLayar()
                boolSelesai = True


    