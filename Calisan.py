from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.kontrol_sektor(sektor)
        self.__tecrube = tecrube
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = self.kontrol_sektor(sektor)

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        try:
            if self.__tecrube <= 24:
                return 0
            elif 24 < self.__tecrube <= 48 and self.__maas < 15000:
                return (self.__maas * self.__tecrube) / 100
            elif self.__tecrube > 48 and self.__maas < 25000:
                return (self.__maas * self.__tecrube) / 200
            else:
                return 0
        except TypeError:
            return 0
    
    def yeni_maas(self):
        return self.get_maas()+self.zam_hakki()
    
    def __str__(self,):
        
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.__tecrube}\nYeni Maaş: {self.yeni_maas()}"

    @staticmethod
    def kontrol_sektor(sektor):
        sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        if sektor in sektorler:
            return sektor
        else:
            return "diğer"
