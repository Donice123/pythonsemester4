class Karyawan:
    def __init__(self, nama, jam_lembur):
        self.__nama = nama
        self.__jam_lembur = jam_lembur
        self.__gaji_pokok = 3500000
        self.__gaji_lembur = 300000

    def __hitung_gaji(self):
        upah_lembur = self.__gaji_lembur * self.__jam_lembur
        return upah_lembur + self.__gaji_pokok

    def cetak_gaji(self):
        gaji = self.__hitung_gaji()
        print(f"Gaji {self.__nama}: Rp. {gaji}")


if __name__ == "__main__":
    while True:
        nama = input("Masukkan nama karyawan: ")
        jam_lembur = int(input("Masukkan jumlah jam lembur: "))

        karyawan = Karyawan(nama, jam_lembur)
        karyawan.cetak_gaji()

        ulang = input("Hitung gaji karyawan lain? (y/n): ")
        if ulang.lower() != 'y':
            break
