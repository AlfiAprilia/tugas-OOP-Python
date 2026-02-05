from abc import ABC, abstractmethod

# ABSTRACT CLASS (ABSTRACTION)

class BarangElektronik(ABC):
    def __init__(self, nama, stok, harga_dasar):
        self.nama = nama
        self.__stok = stok              # Private attribute
        self.__harga_dasar = harga_dasar  # Private attribute

    # GETTER (Encapsulation)
    def get_stok(self):
        return self.__stok

    def get_harga_dasar(self):
        return self.__harga_dasar

    # SETTER / METHOD UBAH STOK (Encapsulation)
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print("❌ Stok tidak boleh negatif!")
        else:
            self.__stok += jumlah
            print(f"✅ Stok {self.nama} bertambah menjadi {self.__stok}")

    # ABSTRACT METHODS (Kontrak)
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

# INHERITANCE + POLYMORPHISM

class Laptop(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, processor):
        super().__init__(nama, stok, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        print(f"Laptop: {self.nama} | Processor: {self.processor} | Stok: {self.get_stok()}")

    def hitung_harga_total(self, jumlah):
        pajak = 0.10
        total = jumlah * self.get_harga_dasar()
        return total + (total * pajak)


class Smartphone(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, kamera):
        super().__init__(nama, stok, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        print(f"Smartphone: {self.nama} | Kamera: {self.kamera} | Stok: {self.get_stok()}")

    def hitung_harga_total(self, jumlah):
        pajak = 0.05
        total = jumlah * self.get_harga_dasar()
        return total + (total * pajak)

# POLYMORPHISM (FUNGSI LUAR)

def proses_transaksi(daftar_barang):
    total_belanja = 0
    print("\n🛒 Detail Pembelian:")
    for barang, jumlah in daftar_barang:
        barang.tampilkan_detail()
        harga = barang.hitung_harga_total(jumlah)
        print(f"Jumlah beli: {jumlah} | Subtotal: Rp{harga:,.0f}")
        total_belanja += harga

    print(f"\n💰 Total Belanja Akhir: Rp{total_belanja:,.0f}")
    return total_belanja

# MAIN PROGRAM (USER STORY)

print("=== SISTEM INVENTARIS TECHMASTER ===")

# 1) Admin membuat produk
laptop1 = Laptop("ASUS ROG", 10, 15000000, "Intel i7")
hp1 = Smartphone("Samsung Galaxy", 20, 8000000, "64MP")

# 2) Admin mencoba menambah stok negatif
laptop1.tambah_stok(-5)

# 3) User membeli barang
keranjang = [
    (laptop1, 2),
    (hp1, 1)
]

# 4) Proses transaksi
proses_transaksi(keranjang)
