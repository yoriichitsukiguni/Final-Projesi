from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = tecrube
        self.__statu = self.statu_bul()

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube
        self.__statu = self.statu_bul()

    def get_statu(self):
        return self.__statu

    def statu_bul(self):
        try:
            mavi_yaka_etkisi = self.__tecrube * 0.20
            beyaz_yaka_etkisi = self.__tecrube * 0.35
            yonetici_etkisi = self.__tecrube * 0.45

            statuler = {
                "mavi yaka": mavi_yaka_etkisi,
                "beyaz yaka": beyaz_yaka_etkisi,
                "yonetici": yonetici_etkisi
            }

            en_uygun_statu = max(statuler, key=statuler.get)
            return en_uygun_statu
        except TypeError:
            return None

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nEn Uygun Statü: {self.__statu}"
