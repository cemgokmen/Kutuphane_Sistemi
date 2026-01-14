import time
from uye_islemleri import uye_kayit, uye_giris

def ana_menu():
    while True:
        print("\n" + "="*30) 
        print("📚 KÜTÜPHANE SİSTEMİ - GİRİŞ")
        print("="*30)
        print("1. Üye Ol")
        print("2. Giriş Yap")
        print("3. Çıkış yap")
        
        secim = input("Seçiminiz (1-3): ")

        if secim == "1":
            print("\n--- ÜYE KAYIT ---")
            k_adi = input("Kullanıcı Adı: ")
            sifre = input("Şifre: ")
            uye_kayit(k_adi, sifre)

        elif secim == "2":
            print("\n--- ÜYE GİRİŞ ---")
            k_adi = input("Kullanıcı Adı: ")
            sifre = input("Şifre: ")
            basarili = uye_giris(k_adi, sifre)
            
            if basarili:
                print(">> Kütüphane ana menüsüne yönlendiriliyorsunuz...")
                # Buraya ileride kitap listeleme vs. gelecek
                break

        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Lütfen geçerli bir seçim yapın.")
        
        time.sleep(1) # Okumak için biraz beklet

if __name__ == "__main__":
    ana_menu()
