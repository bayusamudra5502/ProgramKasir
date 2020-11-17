# File Library
"""
    Kumpulan pustaka yang akan digunakan dalam program
    Kasir
"""

from libs.io import *
from libs.barang import *
from libs.user import *

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