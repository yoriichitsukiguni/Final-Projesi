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

    except Exception as e:
        print("Hata olustu:", str(e))
        
main()
