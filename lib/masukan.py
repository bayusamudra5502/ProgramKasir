import msvcrt
from termcolor import *
import colorama

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
        else:
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
    garis_bawah = "underline"
    tebal = "bold"
    reverse = "reverse"

def warna(text, warna_teks = None, warna_belakang = None, attrs=[]):
    if warna_teks != None and warna_belakang == None:
        return colored(text, warna_teks, attrs=attrs)
    elif warna_teks == None and warna_belakang != None:
        return colored(text, on_color="on_" + warna_belakang, attrs=attrs)
    elif warna_teks != None and warna_belakang != None:
        return colored(text, warna_teks, "on_" + warna_belakang, attrs=attrs)
    else:
        return colored(text, attrs=attrs)