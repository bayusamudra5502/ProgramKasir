## PROGRAM KASIR
""" 
      _              __    _   __                      _    ___  ____                  _           
     / \            [  |  (_) [  |  _                 (_)  |_  ||_  _|                (_)          
    / _ \    _ .--.  | |  __   | | / ]  ,--.   .--.   __     | |_/ /    ,--.   .--.   __   _ .--.  
   / ___ \  [ '/'`\ \| | [  |  | '' <  `'_\ : ( (`\] [  |    |  __'.   `'_\ : ( (`\] [  | [ `/'`\] 
 _/ /   \ \_ | \__/ || |  | |  | |`\ \ // | |, `'.'.  | |   _| |  \ \_ // | |, `'.'.  | |  | |     
|____| |____|| ;.__/[___][___][__|  \_]\'-;__/[\__) )[___] |____||____|\'-;__/[\__) )[___][___]    
            [__|                                                                                   
        
        Versi Alpha
"""

# Impor library
from forms.login import *
from forms.loading import *

def main():
    # Fungsi utama dari program
    formLogin()

# Mencegah error karena KeyboardIntterupt (CTRL+C)
try:
    if __name__ == "__main__":
        # Buka form loading
        formLoading()

        # Jalankan prosedur main
        main()
except KeyboardInterrupt as err:
    pass
finally:
    # Langkah saat menutup program
    hapusLayar()

    print(warnai("Menutup program...", Warna.kuning))
    print(warnai("Program Selesai", Warna.hijau))
    print()