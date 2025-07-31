# main.py

# evcil_hayvan.py dosyasından EvcilHayvan sınıfını içe aktarıyoruz
from evcil_hayvan import EvcilHayvan

def ana_menu():
    """Kullanıcıya menüyü gösterir ve geçerli bir seçim alana kadar bekler."""
    print("\n--- Evcil Hayvan Menüsü ---")
    print("1. Evcil Hayvanı Besle")
    print("2. Evcil Hayvanla Oyna")
    print("3. Evcil Hayvanı Uyut")
    print("4. Durumu Göster")
    print("5. Çıkış")
    print("----------------------------")
    while True:
        try:
            secim = int(input("Seçiminizi yapın (1-5): "))
            if 1 <= secim <= 5:
                return secim
            else:
                print("Geçersiz seçim. Lütfen 1 ile 5 arasında bir sayı girin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

def main():
    """Programın ana başlangıç noktasını ve oyun döngüsünü yönetir."""
    print("Sanal Evcil Hayvanınız Uygulamasına Hoş Geldiniz!")

    # Evcil hayvanın adını ve türünü kullanıcıdan al
    evcil_hayvan_adi = input("Evcil hayvanınızın adını girin: ")
    evcil_hayvan_turu = input("Evcil hayvanınızın türünü girin (örn: Köpek, Kedi, Kuş): ")

    # EvcilHayvan sınıfından bir nesne (instance) oluşturuyoruz
    benim_evcil_hayvanim = EvcilHayvan(evcil_hayvan_adi, evcil_hayvan_turu)

    while True:
        secim = ana_menu()

        if secim == 1:
            benim_evcil_hayvanim.besle()
        elif secim == 2:
            benim_evcil_hayvanim.oynat()
        elif secim == 3:
            benim_evcil_hayvanim.uyut()
        elif secim == 4:
            benim_evcil_hayvanim.durum_goster()
        elif secim == 5:
            print(f"Hoşça kalın, {benim_evcil_hayvanim.isim} sizi özleyecek!")
            break # Döngüden çıkış

        # Her eylemden sonra evcil hayvanın durumunu biraz değiştir
        # Durum gösterme eylemi için zaman geçirmeye gerek yok
        if secim != 4:
            benim_evcil_hayvanim.zaman_gecir()

# Programın doğrudan çalıştırıldığında 'main()' fonksiyonunu çağırmasını sağlar.
if __name__ == "__main__":
    main()

# Main.py çalışıyor ama evcil_hayvan.py çalışmıyor.
# Import la olmaz bunların birleşmesi lazım. 
# Birden çok class ı moduler yapı olarak ayrı dosyalara bölüp from modul_adi import ClassAdi. (ClassAdi Pascal case den snakecase a dönüşür.) 