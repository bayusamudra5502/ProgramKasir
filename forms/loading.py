## FORM LOADING
""" Form awal untuk menampilkan loading"""
# Impor pustaka yang digunakan
from time import sleep
from libs.library import *

def loading(baris, max = 50, time = 5):
    """Mencetak progress bar dan persen loading"""
    for i in range(0,100):
        # Cetak progess bar
        strLoadingBar = warnai("█" * int(i/100 * max), warna_teks=Warna.hijau)
        strLoadingBar +=  "-" * int((1-i/100) * max)

        # Cetak persen loading
        printRataTengah(baris,[strLoadingBar, f"Memuat Program - {i}%"])

        # Tahan sebentar eksekusi program
        sleep(time / 100)

def formLoading():
    # Cetak judul program, frame, dan pembuat program
    hapusLayar()
    cetakFrame("*")  
    listTampil = listStrJudul + [strVersi + " Oleh : " + " - ".join(listDeveloper)]
    printRataTengah((get_terminal_size().lines)// 3, listTampil, True)

    # Tampilkan progress bar loading
    loading((get_terminal_size().lines)// 3 + 10)

    return True

