# File Library
"""LIBRARY
    Kumpulan pustaka yang akan digunakan dalam program
    Kasir
"""

# Impor semua library yang dibutuhkan
# Menyambungkan dengan semua pustaka pada program ini
from libs.io import *
from libs.barang import *
from libs.user import *
from math import log10 # Logaritma basis 10
import re # Regular Expression

# Konstanta
listDeveloper = ["Bayu Samudra (16520420)", "Daniel Salim (16520410)", "Dion Timotius Daeli (16520390)"]
strVersi = "Program Versi Alpha"

# Memecah string dari judul program agar tiap baris menjadi item dari list
listStrJudul = warnai("""
      _              __    _   __                      _    ___  ____                  _           
     / \            [  |  (_) [  |  _                 (_)  |_  ||_  _|                (_)          
    / _ \    _ .--.  | |  __   | | / ]  ,--.   .--.   __     | |_/ /    ,--.   .--.   __   _ .--.  
   / ___ \  [ '/'`\ \| | [  |  | '' <  `'_\ : ( (`\] [  |    |  __'.   `'_\ : ( (`\] [  | [ `/'`\] 
 _/ /   \ \_ | \__/ || |  | |  | |`\ \ // | |, `'.'.  | |   _| |  \ \_ // | |, `'.'.  | |  | |     
|____| |____|| ;.__/[___][___][__|  \_]\'-;__/[\__) )[___] |____||____|\'-;__/[\__) )[___][___]    
            [__|                                                                                   """, Warna.cyan).split("\n")


# Inisiasi Program
# Mengaktifkan warna pada program
colorama.init() 
# Mencegah command prompt menuliskan path selama program berjalan
system("echo off")

# Variabel Global
# PenggunaLogin : list untuk menyimpan pengguna yang aktif pada
# sesi aplikasi ini berjalan
PenggunaLogin = [None]

def cariRegex(Kunci, Data, Index):
  """"Mencari baris pada Data yang sesuai dengan Kunci.
  Pencarian berdasarkan pola Regular Expression pada kolom Index. 
  Hasil dari fungsi ini akan mengeluarkan matriks yang sesuai dengan
  kunci.
  
  Input : 
  Kunci = string
  Data  = matriks
  Index = int
  
  Output : Matriks dari Data yang sesuai pola"""
  # Matriks hasil yang esuai dengan pola
  matResult = []

  # Mencari setiap item di Data yang sesuai dengan pola
  # Regex Kunci
  for i in Data:
    if re.findall(Kunci, i[Index]) != []:
      matResult.append(i)
  
  return matResult

def cetakHeader(Judul = "Menu Utama"):
    """Mencetak Judul program dan judul form.
    
    Output : Posisi kursor terakhir."""
    hapusLayar()
    cetakFrame()

    # Cetak pengguna yang aktif saat ini
    pindahkanKursor(3, 3)
    print(warnai(f" Login sebagai {PenggunaLogin[0]}", Warna.kuning))

    # Cetak nama program pada liststrJudul
    printRataTengah((get_terminal_size().lines)// 4, listStrJudul, True)
    printRataTengah((get_terminal_size().lines)// 4 + 9, [colored(Judul ,Warna.cyan)])

    # Mencetak perintah pada user
    printRataTengah((get_terminal_size().lines)// 4 + 11, [colored("Pilihlah aksi yang akan anda lakukan:",Warna.putih)])
    return (get_terminal_size().lines)// 4 + 12