from kar import Karyawan

if __name__ == "__main__":
    while True:
        nama = input("Masukkan nama karyawan: ")
        jam_lembur = int(input("Masukkan jumlah jam lembur: "))

        karyawan = Karyawan(nama, jam_lembur)
        karyawan.cetak_gaji()

        ulang = input("Hitung gaji karyawan lain? (y/n): ")
        if ulang.lower() != 'y':
            break
