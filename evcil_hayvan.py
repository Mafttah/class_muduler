# evcil_hayvan.py

class EvcilHayvan:
    """
    Bu sınıf, sanal bir evcil hayvanın özelliklerini ve davranışlarını tanımlar.
    """
    def __init__(self, isim, tur):
        """
        Evcil hayvan nesnesini başlatır.
        Parametreler:
            isim (str): Evcil hayvanın adı.
            tur (str): Evcil hayvanın türü.
        """
        self.isim = isim
        self.tur = tur
        self.enerji = 100 # Maksimum 100
        self.aclik = 0   # Maksimum 100 (0 = tok, 100 = çok aç)
        self.mutluluk = 80 # Maksimum 100
        print(f"\n{self.isim} adında bir {self.tur} aramıza katıldı!")

    def besle(self):
        """Evcil hayvanı besler, açlığını azaltır."""
        if self.aclik == 0:
            print(f"{self.isim} zaten tok. Daha fazla yiyemez.")
        else:
            self.aclik = max(0, self.aclik - 30)
            print(f"{self.isim} beslendi. Açlığı şimdi {self.aclik}.")

    def oynat(self):
        """Evcil hayvanla oynar, enerjisini azaltır, mutluluğunu artırır."""
        if self.enerji < 20:
            print(f"{self.isim} çok yorgun! Onunla oynayamazsın. Uyutmalısın.")
        else:
            self.enerji = max(0, self.enerji - 20)
            self.mutluluk = min(100, self.mutluluk + 15)
            print(f"{self.isim} ile oynandı. Enerjisi {self.enerji}, Mutluluğu {self.mutluluk}.")

    def uyut(self):
        """Evcil hayvanı uyutur, enerjisini artırır."""
        if self.enerji == 100:
            print(f"{self.isim} zaten dinlenmiş durumda.")
        else:
            self.enerji = min(100, self.enerji + 40)
            print(f"{self.isim} uyudu ve dinlendi. Enerjisi şimdi {self.enerji}.")

    def durum_goster(self):
        """Evcil hayvanın mevcut durumunu görüntüler."""
        print(f"\n--- {self.isim} ({self.tur}) Durumu ---")
        print(f"Enerji: {self.enerji}/100")
        print(f"Açlık: {self.aclik}/100")
        print(f"Mutluluk: {self.mutluluk}/100")
        print("------------------------------")

    def zaman_gecir(self):
        """Her eylemden sonra evcil hayvanın durumunu biraz değiştirir (hayatı simüle eder)."""
        self.aclik = min(100, self.aclik + 10) # Zamanla acıkır
        self.enerji = max(0, self.enerji - 5) # Zamanla yorulur
        self.mutluluk = max(0, self.mutluluk - 5) # Zamanla sıkılır

        # Durum uyarıları
        if self.aclik >= 70:
            print(f"Uyarı: {self.isim} çok aç! Onu beslemelisin.")
        if self.enerji <= 20 and self.enerji > 0:
            print(f"Uyarı: {self.isim} yoruluyor! Onu uyutmalısın.")
        if self.mutluluk <= 30 and self.mutluluk > 0:
            print(f"Uyarı: {self.isim} mutsuz! Onunla oynamalısın.")
        if self.enerji == 0:
            print(f"Uyarı: {self.isim} bitkin düştü! Hemen uyutmalısın.")
        if self.mutluluk == 0:
            print(f"Uyarı: {self.isim} çok mutsuz! Acilen onunla oynamalısın.")
    
    # evcil_hayvan.py dosyasındaki EvcilHayvan sınıfının içine ekle

    def isim_degistir(self, yeni_isim):
        """Evcil hayvanın adını değiştirir."""
        eski_isim = self.isim
        self.isim = yeni_isim
        print(f"{eski_isim} artık {self.isim} olarak bilinecek!")