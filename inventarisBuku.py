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
    --------------- Sistem Inventasris Buku Toko 'Sukses' ---------------
    =====================================================================
        1. Tampilkan Semua Buku
        2. Tambah Buku Baru
        3. Cari Buku
        4. Keluar
    ---------------------------------------------------------------------
    ''')

    # mengambil input pilihan
    pilihan = input("masukan pilihan anda (1-4) : ") 

    # kondisi setiap pilihan
    if pilihan == "1":
        # akan loop list inventaris dan mengambil semua data
        for keterangan_buku in inventaris:
            print(f"judul buku  : {keterangan_buku[0]}")
            print(f"jumlah buku : {keterangan_buku[1]}")
            print(f"harga buku  : {keterangan_buku[2]}")
            print("--------------------------------")

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

    elif pilihan == "4":
        break

    else:
        print(f"{WARNA_MERAH}pilihan {pilihan} tidak ada di menu{WARNA_RESET}")

# program selesai