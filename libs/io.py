import msvcrt
from termcolor import *
import colorama
from os import system, get_terminal_size

def inputPassword(prompt="Kata Sandi : ", char="•"):
    """ Fungsi yang membuat inputan user tidak terlihat 
    Cara kerjanya mirip fungsi input pada umumnya hanya
    karakternya tidak terlihat saja.
    """

    # Tampilkan prompt satu karakter demi satu karakter
    for i in prompt:
        msvcrt.putwch(i)

    inputUser = ""
    while True:
        inputChar = msvcrt.getwch()
        if(inputChar == "\n" or inputChar == "\r"):
            break
        elif(inputChar == "\003"): # CTRL+C
            # Keluar dari program dengan error KeyboardInterrupt
            raise KeyboardInterrupt
        elif(inputChar == "\b"):
            # Jika user menekan backspace
            if(len(inputUser) > 0):
                # Hapus satu karakter di layar
                msvcrt.putwch("\b")
                msvcrt.putwch(" ")
                msvcrt.putwch("\b")
            
            # Hapus satu karakter di inputUser
            inputUser = inputUser[:-1] 
        elif(str(inputChar).isalnum()):
            inputUser += inputChar
            msvcrt.putwch(char)
    
    msvcrt.putwch("\r")
    msvcrt.putwch("\n")
    return inputUser

class Warna(object):
    """Daftar Warna yang tersedia"""
    abu_abu = "grey"
    merah = "red"
    hijau = "green"
    kuning = "yellow"
    biru = "blue"
    magenta = "magenta"
    cyan = "cyan"
    putih = "white"

class Atribut(object):
    """Daftar Atribut"""
    garis_bawah = ["underline"]
    tebal = ["bold"]
    reverse = ["reverse"]

def warnai(text, warna_teks = None, warna_belakang = None, atribut=[]):
    """Memberi warna pada output."""
    if warna_teks != None and warna_belakang == None:
        return colored(text, warna_teks, attrs=atribut)
    elif warna_teks == None and warna_belakang != None:
        return colored(text, on_color="on_" + warna_belakang, attrs=atribut)
    elif warna_teks != None and warna_belakang != None:
        return colored(text, warna_teks, "on_" + warna_belakang, attrs=atribut)
    else:
        return colored(text, attrs=atribut)

def hapusLayar():
    """Membersihkan Layar"""
    system("cls")

def pindahkanKursor(baris,kolom):
    """Pindahkan kursor ke posisi (kolom, baris)"""
    print(colorama.Cursor.POS(kolom, baris), end="") 

def printRataTengah(baris, listOutput, mode_block = False):
    """Mencetak ke layar dengan Rata Tengah"""
    i = 0
    if not mode_block: # Buat menjadi ditengah untuk tiap baris
        for text in listOutput:
            pindahkanKursor(baris + i, (get_terminal_size().columns \
                        - len(text)) // 2)
            print(text)
            i += 1
    else: # Buat menjadi ditengah berdasarkan baris yg terpanjang
        intMax = -1
        for text in listOutput: # Mencari string perpanjang
            intMax = max([intMax, len(text)]) 
        
        for text in listOutput:
            pindahkanKursor(baris + i, (get_terminal_size().columns \
                        - intMax) // 2)
            print(text)
            i += 1

def cetakFrame(karakter_frame = "#"):
    """Mencetak Frame"""
    for i in range(1, get_terminal_size().lines + 1): # Mencetak pinggiran
        if i == 1 or i == get_terminal_size().lines:
            for j in range(1,get_terminal_size().columns + 1):
                print(karakter_frame, end="")
        else:
            pindahkanKursor(i,1)
            print(karakter_frame, end="")
            pindahkanKursor(i, get_terminal_size().columns)
            print(karakter_frame, end="")

def printTabel(judul_kolom, data):
    pass