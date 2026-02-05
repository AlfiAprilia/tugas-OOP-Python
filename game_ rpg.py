class Hero:
 # Constructor: Dijalankan saat Hero baru dibuat
    def __init__(self, name, hp_awal, attack_power):
        self.name = name # Nama Hero
        self._hp = hp_awal # Nyawa (Health Point)
        self.attack_power = attack_power # Kekuatan Serangan
    # GETTER: Cara resmi melihat HP
    def get_hp(self):
        return self._hp
    # SETTER: Cara resmi mengubah HP (dengan validasi)
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self._hp = 0 # HP tidak boleh negatif
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self._hp = 1000
        else:
            self._hp = nilai_baru

    def diserang(self, damage):
        #kita pakai setter/getter bahkan di class sendiri agar aman
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.name} terkena damage {damage}. Sisa HP:{self.get_hp()}")

 # Method untuk menampilkan info hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self._hp} | Power: {self.attack_power}")

# Method menyerang: Objek ini (self) menyerang objek lain (lawan)
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

 # Method diserang: Menerima damage
    def diserang(self, damage):
        self._hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self._hp}")

    # Class Mage adalah anak dari class Hero
class Mage(Hero):
 def __init__(self, name, hp, attack_power, mana):
 # Memanggil constructor milik Parent (Hero)
    super().__init__(name, hp, attack_power)
    self.mana = mana
 def info(self):
    print(f"{self.name} [Mage] | HP: {self._hp} | Mana: {self.mana}")

 # Mage punya skill khusus
 def skill_fireball(self, lawan):
    if self.mana >= 20:
        print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
        self.mana -= 20
        lawan.diserang(self.attack_power * 2) # Damage 2x lipat
    else:
        print(f"{self.name} gagal skill! Mana tidak cukup.")

# -- Main Program --
# Membuat Object (Instansiasi)
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)
# Memanggil Method
hero1.info()
hero2.info()

# -- Main Program Baru --
print("\n--- Update Class Hero ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond) # Serangan biasa (warisan dari Hero)
eudora.skill_fireball(balmond) # Skill khusus Mage

 # Tambah kode Output di akhir program
print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2) # Layla menyerang Zilong
hero2.serang(hero1) # Zilong membalas

# -- Uji Coba --
hero1 = Hero("Layla", 100, 20)
# hero1.__hp = 9999 # GAGAL (Tidak akan mengubah hp asli)
# print(hero1.__hp) # ERROR (Tidak bisa dibaca langsung)
hero1.set_hp(-50) # Coba set negatif
print(hero1.get_hp()) # Output: 0 (Karena dicegat oleh logika Setter)