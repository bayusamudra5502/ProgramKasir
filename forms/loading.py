## FORM LOADING
""" Form awal tempat program loading"""

from time import sleep
from libs.library import *

def loading(baris, max = 50, time = 5):
    for i in range(0,100):
        strLoadingBar = warnai("█" * int(i/100 * max), warna_teks=Warna.hijau)
        strLoadingBar +=  "-" * int((1-i/100) * max)
        printRataTengah(baris,[strLoadingBar, f"Memuat Program - {i}%"])
        sleep(time / 100)

def formLoading():
    hapusLayar()
    cetakFrame("*")  
    listTampil = listStrJudul + [strVersi + " Oleh : " + " - ".join(listDeveloper)]
    printRataTengah((get_terminal_size().lines)// 3, listTampil, True)

    loading((get_terminal_size().lines)// 3 + 10)

    return True

