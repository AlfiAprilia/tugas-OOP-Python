from abc import ABC, abstractmethod
# 1. Interface / Abstract Class
# Ini adalah KONTRAK. Semua turunan wajib punya method di bawah ini.

class GameUnit(ABC):

 @abstractmethod
 def serang(self, target):
    pass
 @abstractmethod
 def info(self):
    pass
# 2. Implementasi pada Class Konkret
class Hero(GameUnit):
 def __init__(self, nama):
    self.nama = nama

 # Kita WAJIB membuat method serang, kalau tidak akan Error
 def serang(self, target):
    print(f"Hero {self.nama} menebas {target}!")

 def info(self):
    print(f"Saya adalah Hero: {self.nama}")
    
class Monster(GameUnit):
 def __init__(self, jenis):
    self.jenis = jenis
 # Implementasi serang versi Monster
 def serang(self, target):
    print(f"Monster {self.jenis} menggigit {target}!")

 def info(self):
    print(f"Saya adalah Monster: {self.jenis}")

# Parent Class
class Hero:
 def __init__(self, nama):
    self.nama = nama

 def serang(self):
    print("Hero menyerang dengan tangan kosong.")
# Child Class 1
class Mage(Hero):
 def serang(self):
    print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")
# Child Class 2
class Archer(Hero):
 def serang(self):
    print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")
# Child Class 3
class Fighter(Hero):
 def serang(self):
    print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")

 # -- Penerapan Polymorphism --
# Kita punya daftar hero campuran
pasukan = [
 Mage("Eudora"),
 Archer("Miya"),
 Fighter("Zilong"),
 Mage("Gord")
]
print("--- PERANG DIMULAI ---")
# Satu perintah loop, tapi respon berbeda-beda (Polymorphism)
for pahlawan in pasukan:
 pahlawan.serang()
# -- Uji Coba --
# unit = GameUnit() # ERROR! Abstract class tidak bisa jadi objek.
h = Hero("Alucard")
m = Monster("Serigala")
h.info()
m.info()