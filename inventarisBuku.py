# just color
WARNA_MERAH = '\033[31m'
WARNA_HIJAU = '\033[32m' # Nanti bisa dipakai untuk "input berhasil"
WARNA_RESET = '\033[0m'

# List utama untuk menyimpan semua data buku
inventaris = [
    ["Laskar Pelangi", 15, 85000],
    ["Atomic Habits", 5, 90000],
    ["Filosofi Teras", 20, 75000],
    ["Python Crash Course", 12, 250000],
    ["Bumi Manusia", 8, 110000],
    ["The Alchemist", 18, 65000],
    ["Rich Dad Poor Dad", 25, 88000],
    ["Dune", 7, 140000],
    ["Ronggeng Dukuh Paruk", 10, 70000],
    ["Sebuah Seni untuk Bersikap Bodo Amat", 30, 95000],
    ["Hujan Bulan Juni", 14, 60000],
    ["One Piece Vol. 100", 50, 45000],
    ["Clean Code", 9, 350000],
    ["Resep Warisan Nenek", 22, 125000]
]

# loop untuk mengulang program
while True:
    # banner
    print(f'''
    =====================================================================
    --------------- Sistem Inventaris Buku Toko 'Sukses' ---------------
    =====================================================================
        1. Tampilkan Semua Buku
        2. Tambah Buku Baru
        3. Hapus Buku
        4. Cari Buku
        5. Ubah Data
        6. Keluar
    ---------------------------------------------------------------------
    ''')

    inventaris.sort()

    # mengambil input pilihan
    pilihan = input("masukan pilihan anda (1-6) : ") 

    # kondisi setiap pilihan
    if pilihan == "1":
        # akan loop list inventaris dan mengambil semua data
        for keterangan_buku in inventaris:
            print(f"{inventaris.index(keterangan_buku)+1} | Judul Buku : {keterangan_buku[0]} | Jumlah Buku : {keterangan_buku[1]} | Harga Buku : {keterangan_buku[2]}")
            # print(f"judul buku  : {keterangan_buku[0]}")
            # print(f"jumlah buku : {keterangan_buku[1]}")
            # print(f"harga buku  : {keterangan_buku[2]}")
            # print("--------------------------------")

    elif pilihan == "2":
        # mengambil input
        judul = input("masukan judul \t\t: ").title()
        jumlah_buku = int(input("masukan jumlah buku \t: "))
        harga_buku = int(input("masukan harga buku \t: "))

        # membuat list baru
        buku_baru = [judul, jumlah_buku, harga_buku]

        # memasukan ke list utama
        inventaris.append(buku_baru)
        print(f"{WARNA_HIJAU}input berhasil✅{WARNA_RESET}")
    
    elif pilihan == "3":
        buku_hapus = input("masukan judul buku yang mau dihapus : ").title()

        # cari buku
        buku_ditemukan = None

        # cari buku
        for buku in inventaris:
            if buku[0] == buku_hapus:
                buku_ditemukan = buku
                break

        if buku_ditemukan:
            inventaris.remove(buku_ditemukan)
            print(f"buku berjudul {buku_ditemukan[0]} berhasil dihapus")
        else:
            print(f"buku berjudul {buku_ditemukan[0]} tidak ditemukan")

    elif pilihan == "4":
        # input buku yang dicari
        cari_buku = input("masukan judul yang dicari : ").title()
        
        ditemukan = False

        # looping semua data di inventaris dan mengambil indeks 0 atau judul
        for buku in inventaris:
            if buku[0] == cari_buku:
                print(f"Judul : {buku[0]}")
                print(f"Stok : {buku[1]}")
                print(f"Harga : {buku[2]}")
                ditemukan = True
                break

        if not ditemukan:
                print("buku tidak ditemukan")
        
    elif pilihan == "5":
            for data_buku in inventaris:
                print(f"{inventaris.index(data_buku)+1} | Judul Buku : {data_buku[0]} | Jumlah Buku : {data_buku[1]} | Harga Buku : {data_buku[2]}")

            data_number = int(input("\ndata nomor berapa yang ingin ada ubah : "))
            print(inventaris[data_number-1])
            
            perubahan = input("apa yang mau ada ubah (judul/stok/harga)? : ").lower()

            if perubahan == "judul":
                judul_baru = input("masukan judul baru : ").title()
                inventaris[data_number-1][0] = judul_baru
                print(f"{WARNA_HIJAU} judul berhasil diubah ✅{WARNA_RESET}")
            elif perubahan == "stok":
                stok_baru = int(input("masukan stok baru : "))
                inventaris[data_number-1][1] = stok_baru
                print(f"{WARNA_HIJAU} stok berhasil diubah ✅{WARNA_RESET}")
            elif perubahan == "harga":
                harga_baru = int(input("masukan harga baru : "))
                inventaris[data_number-1][2] = harga_baru
                print(f"{WARNA_HIJAU} harga berhasil diubah ✅{WARNA_RESET}")
            else:
                print(f"pilihan {perubahan} tidak ada")


    elif pilihan == "6":
        break

    else:
        print(f"{WARNA_MERAH}pilihan {pilihan} tidak ada di menu{WARNA_RESET}")

# program selesai