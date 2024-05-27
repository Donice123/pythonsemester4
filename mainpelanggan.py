# main.py

from customer import Customer


def main():
    customers = []  # List untuk menyimpan objek pelanggan

    # Loop untuk memasukkan data pelanggan
    while True:
        nama = input("Masukkan nama pelanggan: ")
        nomor_hp = input("Masukkan nomor HP pelanggan: ")
        jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))

        # Membuat objek pelanggan baru
        customer = Customer(nama, nomor_hp, jumlah_pesanan)

        customers.append(customer)  # Menambahkan objek pelanggan ke dalam list

        lanjut = input("Apakah ada pelanggan lain? (y/n): ")
        if lanjut.lower() != 'y':
            break

    # Looping untuk menghitung pesanan pelanggan lain
    for customer in customers:
        customer.count_other_orders(customers)


if __name__ == "__main__":
    main()
