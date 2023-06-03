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

    except Exception as e:
        print("Hata olustu:", str(e))
        
main()
