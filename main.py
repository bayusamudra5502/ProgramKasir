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

from forms.login import *
from forms.loading import *

def main():
    # Fungsi utama dari program
    formLogin()

try:
    if __name__ == "__main__":
        formLoading()
        main()
except KeyboardInterrupt as err:
    print("Menutup program...")
finally:
    hapusLayar()