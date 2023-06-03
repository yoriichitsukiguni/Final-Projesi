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

        # DataFrame oluşturma
        data = {
            "nesne degeri": ["calisan", "calisan", "calisan", "mavi yaka", "mavi yaka", "mavi yaka",
                             "beyaz yaka", "beyaz yaka", "beyaz yaka"],
            "tc_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(),
                      beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
            "ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(),
                   beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
            "soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(),
                      beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
            "yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(),
                    beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
            "cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(),
                         beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
            "uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(),
                      beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
            "sektor": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(),
                       beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
            "tecrube": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(),
                        beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
            "maas": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(),
                     beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
            "yipranma payi": [0, 0, 0 , mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi() ,0 ,0 ,0],
            "tesvik primi": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],    
            "yeni maas": [calisan1.yeni_maas(), calisan2.yeni_maas(), calisan3.yeni_maas(), mavi_yaka1.yeni_maas(), mavi_yaka2.yeni_maas(), mavi_yaka3.yeni_maas(),
                           beyaz_yaka1.yeni_maas(), beyaz_yaka2.yeni_maas(), beyaz_yaka3.yeni_maas()]
                           }
    
        df = pd.DataFrame(data)

         # a) Boş değerleri 0 atama
        df.fillna(0, inplace=True)

         # b) Tecrübe ve yeni maaş ortalamalarını gruplayarak hesaplama ve yazdırma
        tecrube_ortalamalari = df.groupby("nesne degeri")["tecrube"].mean()
        yeni_maas_ortalamalari = df.groupby("nesne degeri")["yeni maas"].mean()
        print("Tecrube Ortalamalari:\n", tecrube_ortalamalari)
        print("Yeni maas Ortalamalari:\n", yeni_maas_ortalamalari)

        # c) Maaşı 15000 TL üzerinde olanların toplam sayısını bulma
        yuksek_maasli_sayisi = len(df[df["maas"] > 15000])
        print("Maasi 15000 TL üzerinde olanlarin toplam sayisi:", yuksek_maasli_sayisi)

        # d) Yeni maaşa göre DataFrame'i küçükten büyüğe sıralama ve yazdırma
        sirali_df = df.sort_values("yeni maas")
        print("Siralanmis DataFrame:\n", sirali_df)

         # e) Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulma ve yazdırma
        tecrube_filtre = df[(df["nesne degeri"] == "beyaz yaka") & (df["tecrube"] > 3)]
        print("Tecrubesi 3 seneden fazla olan Beyaz Yakalilar:\n", tecrube_filtre)

        # f) Yeni maaşı 10000 TL üzerinde olanlar için 2-5 satır arasındakileri seçme ve yazdırma
        yuksek_maas_filtre = df[df["yeni maas"] > 10000]
        satir_araligi_filtre = yuksek_maas_filtre.iloc[2:5, [1, 12]]
        print("Yeni maasi 10000 TL üzerinde olan 2-5 satirlar arasi veriler:\n", satir_araligi_filtre)

         # g) Ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame oluşturma ve yazdırma
        yeni_df = df[["ad", "soyad", "sektor", "yeni maas"]]
        print("Yeni DataFrame:\n", yeni_df)


    except Exception as e:
        print("Hata olustu:", str(e))
        
main()
