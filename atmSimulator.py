# atm simulator

# keterangan saldo
saldo = 50000

# banner
while True:
    print(f'''
    =======================================================
    ----------- SELAMAT DATANG DI ATM SIMULATOR -----------
    =======================================================
    1. Cek Saldo Anda
    2. Setor Turnai
    3. Tarik Tunai
    4. Keluar
    =======================================================
    ''')

    # input pilihan
    pilihan = input("\tSilahkan masukan pilihan anda (1-4) : ")
    # kondisi pilihan
    if pilihan == "1":
        print(f"\tSaldo anda saat ini adalah : Rp{saldo}")
    elif pilihan == "2":
        setor = int(input("\tmasukan nominal yang ingin anda setorkan : "))
        saldo += setor
    elif pilihan == "3":
        if saldo < 50000:
            print("\tmohon maaf saldo anda kurang dari 50000")
        elif saldo >= 50000:
            tarik = int(input("\tmasukan nominal penarikan : "))
            saldo -= tarik
    elif pilihan == "4":
        break
    else:
        print("\tmohon masukan pilihan dengan benar")