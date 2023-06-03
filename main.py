import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

def main():
    try:
        # İnsan sınıfı için 2 nesne oluşturulması
        insan1 = Insan("11111111111", "Ahmet", "Yilmaz", 30, "Erkek", "Turk")
        insan2 = Insan("22222222222", "Ayse", "Demir", 25, "Kadin", "Turk")

        # İşsiz sınıfı için 3 nesne oluşturulması
        issiz1 = Issiz("33333333333", "Mehmet", "Kara", 28, "Erkek", "Turk", {"mavi yaka": 2, "beyaz yaka": 4, "yonetici": 6})
        issiz2 = Issiz("44444444444", "Fatma", "Ak", 32, "Kadin", "Turk", {"mavi yaka": 3, "beyaz yaka": 5, "yonetici": 7})
        issiz3 = Issiz("55555555555", "Ali", "Beyaz", 29, "Erkek", "Turk", {"mavi yaka": 1, "beyaz yaka": 6, "yonetici": 8})

        # Çalışan sınıfı için 3 nesne oluşturulması
        calisan1 = Calisan("66666666666", "Zeynep", "Kaya", 35, "Kadin", "Turk", "teknoloji", 36, 20000)
        calisan2 = Calisan("77777777777", "Mustafa", "Arslan", 40, "Erkek", "Turk", "muhaasebe", 48, 12000)
        calisan3 = Calisan("88888888888", "Ebru", "Yildirim", 27, "Kadin", "Turk", "insaat", 60, 25000)

        # Mavi Yaka sınıfı için 3 nesne oluşturulması
        mavi_yaka1 = MaviYaka("99999999999", "Deniz", "Demir", 33, "Erkek", "Turk", "teknoloji", 24, 15000, 0.2)
        mavi_yaka2 = MaviYaka("10101010101", "Elif", "Yilmaz", 38, "Kadin", "Turk", "insaat", 42, 18000, 0.5)
        mavi_yaka3 = MaviYaka("12121212121", "Ayhan", "Aktas", 31, "Erkek", "Turk", "teknoloji", 30, 14000, 0.3)

        # Beyaz Yaka sınıfı için 3 nesne oluşturulması
        beyaz_yaka1 = BeyazYaka("14141414141", "Eren", "Aydin", 36, "Erkek", "Turk", "teknoloji", 12, 18000, 500)
        beyaz_yaka2 = BeyazYaka("16161616161", "Gizem", "Kara", 42, "Kadin", "Turk", "finans", 20, 22000, 2500)
        beyaz_yaka3 = BeyazYaka("18181818181", "Ahmet", "Yilmaz", 39, "Erkek", "Turk", "muhaasebe", 18, 19000, 1500)


    except Exception as e:
        print("Hata olustu:", str(e))
        
main()
