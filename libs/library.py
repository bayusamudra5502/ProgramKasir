# File Library
"""
    Kumpulan pustaka yang akan digunakan dalam program
    Kasir
"""

from libs.io import *
from libs.barang import *
from libs.user import *
import re

# Konstanta
listDeveloper = ["A","B","C","D"]
strVersi = "Program Versi Alpha"
listStrJudul = warnai("""
      _              __    _   __                      _    ___  ____                  _           
     / \            [  |  (_) [  |  _                 (_)  |_  ||_  _|                (_)          
    / _ \    _ .--.  | |  __   | | / ]  ,--.   .--.   __     | |_/ /    ,--.   .--.   __   _ .--.  
   / ___ \  [ '/'`\ \| | [  |  | '' <  `'_\ : ( (`\] [  |    |  __'.   `'_\ : ( (`\] [  | [ `/'`\] 
 _/ /   \ \_ | \__/ || |  | |  | |`\ \ // | |, `'.'.  | |   _| |  \ \_ // | |, `'.'.  | |  | |     
|____| |____|| ;.__/[___][___][__|  \_]\'-;__/[\__) )[___] |____||____|\'-;__/[\__) )[___][___]    
            [__|                                                                                   """, Warna.cyan).split("\n")


# Inisiasi Program
colorama.init()
system("echo off")

# Variabel Global
strPenggunaLogin = ""

def cariRegex(Kunci, Data, Index):
  """"Mencari baris pada Data yang sesuai dengan Kunci.
  Pencarian berdasarkan pola Regular Expression pada kolom Index. 
  Hasil dari fungsi ini akan mengeluarkan matriks yang sesuai dengan
  kunci.
  
  Input : 
  Kunci = string
  Data  = matriks
  Index = int
  
  Output : Matriks yang sesuai pola"""
  matResult = []
  for i in Data:
    if re.findall(Kunci, i[Index]) != []:
      matResult.append(i)
  
  return matResult