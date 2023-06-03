from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi
    
    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi
        
    def get_tecrube(self):
        return super().get_tecrube()
    
    def set_tecrube(self, tecrube):
        return super().set_tecrube(tecrube)

    def zam_hakki(self):
        try:
            if self.get_tecrube() <= 24:
                return self.__tesvik_primi
            elif 24 < self.get_tecrube() <= 48 and self.get_maas() < 15000:
                return (self.get_maas() % self.get_tecrube()) * 5 + self.__tesvik_primi
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:
                return (self.get_maas() % self.get_tecrube()) * 4 + self.__tesvik_primi
            else:
                return 0
        except TypeError:
            return 0
    
    def yeni_maas(self):
        return self.get_maas()+self.zam_hakki()

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrube: {self.get_tecrube()}\nYeni Maas: {self.yeni_maas()}"
