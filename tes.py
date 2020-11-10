from libs.library import *

hapusLayar()
ukuran = lihatUkuranLayar()
for i in range(1, ukuran["baris"]+1):
    if i == 1 or i == ukuran["baris"]:
        for j in range(1,ukuran["kolom"]+1):
            print("#", end="")
    else:
        pindahkanKursor(i,1)
        print("#", end="")
        pindahkanKursor(i,ukuran["kolom"])
        print("#", end="")

pindahkanKursor(ukuran["baris"] // 2 - 23 // 2, ukuran["kolom"] // 2 - 99 // 2)
strs = """
      _              __    _   __                      _    ___  ____                  _           
     / \            [  |  (_) [  |  _                 (_)  |_  ||_  _|                (_)          
    / _ \    _ .--.  | |  __   | | / ]  ,--.   .--.   __     | |_/ /    ,--.   .--.   __   _ .--.  
   / ___ \  [ '/'`\ \| | [  |  | '' <  `'_\ : ( (`\] [  |    |  __'.   `'_\ : ( (`\] [  | [ `/'`\] 
 _/ /   \ \_ | \__/ || |  | |  | |`\ \ // | |, `'.'.  | |   _| |  \ \_ // | |, `'.'.  | |  | |     
|____| |____|| ;.__/[___][___][__|  \_]\'-;__/[\__) )[___] |____||____|\'-;__/[\__) )[___][___]    
            [__|                                                                                   """.split("\n")

for i in range(len(strs)):
    pindahkanKursor(ukuran["baris"] // 2 - 23 // 2 + i, ukuran["kolom"] // 2 - 99 // 2)
    print(strs[i])

pindahkanKursor(ukuran["baris"] // 2 - 23 // 2 + len(strs), ukuran["kolom"] // 2 - 27 // 2)  
print("Ayo login dulu yok.")
pindahkanKursor(ukuran["baris"] // 2, ukuran["kolom"] // 2 - 16)  
input("Username : ")
pindahkanKursor(ukuran["baris"] // 2 + 1, ukuran["kolom"] // 2 - 16)  
print(inputPassword("Password : "))
