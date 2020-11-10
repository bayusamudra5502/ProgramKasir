import msvcrt

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
            
            inputUser = inputUser[:-1] # Hapus satu karakter di inputUser
        else:
            inputUser += inputChar
            msvcrt.putwch(char)
    
    msvcrt.putwch("\r")
    msvcrt.putwch("\n")
    return inputUser