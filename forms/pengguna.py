## FORM PENGGUNA
""" Form yang mengatur mengenai pengguna
"""

from libs.library import *

# Gunakan fungsi berikut untuk memudahkan:
# editPassword(username, password_lama, password_baru)
#    Mengedit password pengguna. Password_lama adalah password
#    pengguna yg dimaksud sebelum diubah. password_baru adalah
#    password pengguna setelah diubah
#
# hapusPengguna(username)
#   Mengapus pengguna dengan username tertentu. Pastikan pengguna
#   yang dihapus bukanlah pengguna yang aktif saat ini. Cek dengan
#   melihat apakan username yang hedak dihapus sama dengan 
#   strPenggunaLogin?
#
# tambahPengguna(username, password)
#   Menambah pengguna baru, dengan username dan password  tertentu
#
# inputPassword(prompt)
#   Seperti input biasa, hanya saja seperti kita menginput password
#   di browser, sehingga hasil inputannya tidak terlihat.

def formPengguna():
    """Fungsi untuk menampilkan form pengguna.
    
    Form pengguna akan berisi komponen untuk melihat semua
    pengguna yang ada, mengedit kata sandi pengguna, dan
    menghapus pengguna."""

    boolInfo = False
    boolError = False
    strErrorMsg = ""
    strMsg = ""
    menu_utama = False
    while (menu_utama == False) :
        try:
                intPosBaris = cetakHeader("FORM PENGGUNA")

                # Daftar username yang ada
                listUsername = [i[0] for i in lihatPengguna()]
                pindahkanKursor(3,3)
                print(warnai(" Login sebagai " + PenggunaLogin[0], Warna.kuning))

                if boolInfo:
                    pindahkanKursor(4,3)
                    print(" " * 50)
                    pindahkanKursor(4,4)
                    print(warnai(strMsg, Warna.hijau))
                    
                elif boolError:
                    pindahkanKursor(4,3)
                    print(" " * 50)
                    pindahkanKursor(4,4)
                    print(warnai(strErrorMsg, Warna.merah))
                
                # Reset notifikasi
                boolInfo = False
                boolError = False
                
                printRataTengah(intPosBaris + 1, ["Opsi Pilihan Aksi", "1. Tambah Pengguna",
                                "2. Hapus Pengguna", "3. Edit Password", "4. Kembali ke Menu Utama"], True)
                intPerEmpat = get_terminal_size().columns // 3
                pindahkanKursor(intPosBaris + 7, intPerEmpat)
                Act = input('Masukkan Opsi : ')

                if Act == "1" :
                    hapusLayar()
                    cetakFrame()
                    printRataTengah(3 ,[warnai("TAMBAH PENGGUNA", Warna.cyan)])
                    print()
                    pindahkanKursor(5,3)
                    print("Masukkan data user yang akan ditambahkan")
                    pindahkanKursor(6,3)
                    print(warnai("Info : Tekan CTRL+C untuk membatalkan aksi ini.", Warna.biru))
                    boolUserValid = False
                    while not boolUserValid:
                        # Bersihkan input sebelumnya
                        pindahkanKursor(8,3)
                        print(" " * 75)
                        pindahkanKursor(8,3)

                        Username = input("Username: ")

                        pindahkanKursor(9,3)
                        print(" "*50)
                        # Cek apakah username kosong atau tidak
                        if Username != "":
                            boolUserValid = True
                        else:
                            pindahkanKursor(9,3)
                            print(warnai("Kesalahan : Username tidak boleh kosong", Warna.merah))

                        # Cek apakah username ada
                        for x in listUsername:
                            if Username == x:
                                pindahkanKursor(9,3)
                                print(warnai("Peringatan : Username sudah terdaftar. Silahkan masukan username lain.", Warna.kuning))
                                boolUserValid = False
                                break
                    Pass = False
                    while (Pass == False) :
                        # Membersihkan layar dari input sebelumnya
                        pindahkanKursor(9,3)
                        print(" " * 75)
                        pindahkanKursor(10,3)
                        print(" " * 75)

                        pindahkanKursor(9,3)
                        Password = inputPassword("Password: ")
                        pindahkanKursor(10,3)
                        KonfirmasiPassword = inputPassword("Konfirmasi Password: ")

                        if (Password == KonfirmasiPassword) :
                            if (Password != ""):
                                pindahkanKursor(11,3)
                                print(warnai("Menambahkan pengguna..", Warna.hijau))
                                tambahPengguna(Username,Password)
                                Pass = True
                                boolInfo = True
                                strMsg = f"Pengguna {Username} berhasil ditambah."
                            else:
                                pindahkanKursor(11,3)
                                print(warnai("Kesalahan : Password tidak boleh kosong", Warna.merah))
                        else :
                            pindahkanKursor(11,3)
                            print(warnai("Kesalahan : Ulangi, password dan Konfirmasi Password tidak sama", Warna.merah))

                if Act == "2" :
                    hapusLayar()
                    boolSelesai = False
                    while not boolSelesai:
                        printRataTengah(2,[warnai("MENGHAPUS USER", Warna.cyan)])
                        pindahkanKursor(4,1)
                        print("Berikut ini adalah daftar username yang terdaftar")
                        for x in range(len(listUsername)) :
                            if listUsername[x] == PenggunaLogin[0]:
                                print(f"{x+1}. ", warnai(f"{listUsername[x]} (Aktif)", Warna.hijau))
                            else:
                                print(f"{x+1}. {listUsername[x]}")
                        print()
                        print("Masukkan username pengguna yang akan dihapus. Pastikan pengguna tidak aktif saat ini.")
                        print(warnai("Info : Tekan CTRL+C untuk membatalkan aksi ini.", Warna.biru))
                        print()
                        username = input("Username : ")

                        if username == PenggunaLogin[0]:
                            print(warnai("Kesalahan : Anda tidak boleh menghapus pengguna yang sedang aktif.", Warna.merah))
                            continue

                        # Cek apakah username ada, jika ada, hapus username tersebut
                        for x in listUsername:
                            if username == x:
                                hapusPengguna(username)
                                boolSelesai = True
                                boolInfo = True
                                strMsg = f"Pengguna {Username} berhasil dihapus."
                                break
                            
                        if not boolSelesai:
                            print(warnai("Kesalahan : Pengguna tidak ditemukan", Warna.merah))
                        else:
                            print(warnai("Info : Pengguna berhasil dihapus.", Warna.hijau))

                if Act == "3" :
                    hapusLayar()
                    cetakFrame()
                    boolUserAda = False
                    while not boolUserAda:
                        printRataTengah(3,[warnai("EDIT PASSWORD USER", Warna.cyan)])
                        pindahkanKursor(4,3)
                        print("Masukkan username yang akan diubah passwordnya:")
                        pindahkanKursor(5,3)
                        print(warnai("Info : Tekan CTRL+C untuk membatalkan aksi ini.", Warna.biru))
                        pindahkanKursor(7,3)
                        username = input("Username: ")

                        # Cek apakah username ada, jika ada, hapus username tersebut
                        for x in listUsername:
                            if username == x:
                                boolUserAda = True
                                break
                        if not boolUserAda:
                            pindahkanKursor(8,3)
                            print(warnai("Kesalahan : Pengguna tidak ditemukan", Warna.merah))

                    # Bersihkan pemberitahuan error
                    pindahkanKursor(8,3)
                    print(" " * 50)

                    Pass = False
                    while (Pass == False) :
                        # Bersihkan input yang lama
                        pindahkanKursor(8,3)
                        print(" " * 75)
                        pindahkanKursor(9,3)
                        print(" " * 75)
                        pindahkanKursor(10,3)
                        print(" " * 75)
                        pindahkanKursor(8,3)
                        passwordLama = inputPassword("Password Lama: ")
                        pindahkanKursor(9,3)
                        passwordBaru = inputPassword("Password Baru: ")
                        pindahkanKursor(10,3)
                        passwordBaruVerify = inputPassword("Verifikasi Password Baru: ")

                        if passwordBaruVerify == passwordBaru :
                            if editPassword(username,passwordLama,passwordBaru):
                                Pass = True
                                boolInfo = True
                                strMsg = f"Password pengguna {username} berhasil diubah."
                            else:
                                pindahkanKursor(11,3)
                                print(warnai("Ulangi, password lama salah", Warna.merah))
                        else :
                            pindahkanKursor(11,3)
                            print(warnai("Ulangi, password baru dan verifikasi password baru tidak sama", Warna.merah))
                elif Act == "4":
                    menu_utama = True
                else:
                    boolError = True
                    strErrorMsg = warnai("Kesalahan : Masukan hanya integer 1 s.d. 4 saja", Warna.merah)
        except KeyboardInterrupt:
            boolInfo = True
            strMsg = "Info : Aksi dibatalkan.."
