class Kullanici:
    def __init__(self,adi,soyadi,numara):
        print("Kullanıcı sınıfı fonksyonu")
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara

    def giris(self):
        print("Giriş Yapıldı")

    def cikis(self):
        print("Çıkış yapıldı")



class Akademisyen(Kullanici):
    pass
class Personel(Kullanici):
    pass
class Ogrenci(Kullanici):
    pass

akademisyen = Akademisyen("Mustafa","Kaya",1236521)
personel = Personel("Mehmet","Yıldız",1539527)
ogrenci = Ogrenci("Can","Demir",1436589)

print("Akademisyen")
print(akademisyen.adi)
print(akademisyen.soyadi)
print(akademisyen.numara)

print("Personel")
print(personel.adi)
print(personel.soyadi)
print(personel.numara)

print("Öğrenci")
print(ogrenci.adi)
print(ogrenci.soyadi)
print(ogrenci.numara)