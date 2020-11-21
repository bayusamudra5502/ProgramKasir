"""PUSTAKA IO

Pustaka yang berisi semua hal yang berkaitan dengan Input dan
Output pada program"""

# Impor Library
import msvcrt
from termcolor import *
import colorama
from os import system, get_terminal_size
import datetime

def inputPassword(prompt="Kata Sandi : ", char="•"):
    """ Fungsi yang membuat inputan user tidak terlihat 
    Cara kerjanya mirip fungsi input pada umumnya hanya
    karakternya tidak terlihat saja.
    
    Output : Hasil input user"""

    # DISCLAIMER : Fungsi ini terinspirasi oleh library python
    # vanilla. Anda dapat lihat versi asli dari fungsi ini pada
    # modul getpass untuk fungsi win_getpass().

    # Terima kasih kepada Guido van Rossum yang telah memberikan
    # Inspirasi untuk pembuatan fungsi ini.

    # Lisensi : Lisensi Python Software Foundation Versi 2

    # Print prompt pada layar
    for i in prompt:
        msvcrt.putwch(i)

    inputUser = ""
    while True:
        inputChar = msvcrt.getwch()
        if(inputChar == "\n" or inputChar == "\r"):
            # Bila enter ditekan, input sudah selesai
            break
        elif(inputChar == "\003"): # CTRL+C
            # Keluarkan KeyboardInterrupt
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
            # Apabila karakter yang diinput adalah
            #  angka atau huruf, simpan.
            inputUser += inputChar
            msvcrt.putwch(char)
    
    # Cetak baris baru agar rapi
    msvcrt.putwch("\r")
    msvcrt.putwch("\n")
    return inputUser

class Warna(object):
    """Daftar Warna yang tersedia.
    Digunakan untuk memberi warna pada
    program"""
    abu_abu = "grey"
    merah = "red"
    hijau = "green"
    kuning = "yellow"
    biru = "blue"
    magenta = "magenta"
    cyan = "cyan"
    putih = "white"

class Atribut(object):
    """Daftar Atribut text yang dapat digunakan"""
    garis_bawah = ["underline"]
    tebal = ["bold"]
    reverse = ["reverse"]

def warnai(text, warna_teks = None, warna_belakang = None, atribut=[]):
    """Memberi warna pada string. Efek ini akan terlihat
    saat string yang diwarnai dicetak pada layar.
    
    Input :
    text : string
    warna_text : Warna (Warna Foreground)
    warna_belakang : Warna (Warna Background)
    atribut : Atribut
    
    Output : String yang sudah diformat"""
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
    """Mencetak ke layar dengan Rata Tengah
    
    Input:
    baris : int -> Baris pencetakan string yang rata tengah
    listOutput : list -> list yang berisi string tiap baris
    mode_block : bool -> True akan menyebabkan semua baris pada string
    dianggap menjadi satu. 
    
    Output : Mencetak di tengah pada layar"""
    i = 0
    if not mode_block: 
        # Buat menjadi ditengah untuk tiap baris
        for text in listOutput:
            # Pindahkan kursor agar hasil print tepat ditengah
            pindahkanKursor(baris + i, (get_terminal_size().columns \
                        - len(text)) // 2)
            print(text)
            i += 1
    else: 
        # Buat menjadi ditengah berdasarkan baris yg terpanjang
        intMax = -1
        for text in listOutput: # Mencari string perpanjang
            intMax = max([intMax, len(text)]) 
        
        for text in listOutput:
            # Pindahkan kursor agar hasil print tepat ditengah
            pindahkanKursor(baris + i, (get_terminal_size().columns \
                        - intMax) // 2)
            print(text)
            i += 1

def cetakFrame(karakter_frame = "#"):
    """Mencetak Frame sesuai dengan karakter yang diinginkan
    
    Input : 
    Karakter_frame : char -> Karakter yang diinginkan
    
    Output :
    Karakter yang diprint sepanjang pinggir dari terminal"""

    for i in range(1, get_terminal_size().lines + 1): # Tranvere tiap baris
        if i == 1 or i == get_terminal_size().lines:
            # Bila berada di baris pertama dan terakhir, cetak
            # karakter selebar jendela pada terminal.
            for j in range(1,get_terminal_size().columns + 1):
                print(karakter_frame, end="")
        else:
            # Cetak karakter hanya pinggir kiri dan kanan saja
            pindahkanKursor(i,1)
            print(karakter_frame, end="")
            pindahkanKursor(i, get_terminal_size().columns)
            print(karakter_frame, end="")