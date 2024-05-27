# customer.py
#Polimorfisme
class Customer:
    def __init__(self, nama, nomor_hp, jumlah_pesanan):
        self.nama = nama
        self.nomor_hp = nomor_hp
        self.jumlah_pesanan = jumlah_pesanan

#Contoh Override yang di inisialisasi pada fungsi count_other_orders
    def count_other_orders(self, customers):
        total_pesanan_lain = 0
        for other_customer in customers:
            if other_customer != self:  # Menyaring pelanggan lain
                total_pesanan_lain += other_customer.jumlah_pesanan

        print(f"Total pesanan pelanggan lain dari  {self.nama}: {total_pesanan_lain}")
