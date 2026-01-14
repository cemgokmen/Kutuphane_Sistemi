import json
import os

# Veri tabanı dosyamızın adı
DB_DOSYASI = "uyeler.json"

def verileri_yukle():
    """JSON dosyasından üyeleri okur, dosya yoksa boş liste döner."""
    if not os.path.exists(DB_DOSYASI):
        return []
    try:
        with open(DB_DOSYASI, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except:
        return []

def verileri_kaydet(uyeler):
    """Üye listesini JSON dosyasına yazar."""
    with open(DB_DOSYASI, "w", encoding="utf-8") as dosya:
        json.dump(uyeler, dosya, indent=4)

def uye_kayit(kullanici_adi, sifre):
    """Yeni üye kaydeder. Başarılıysa True, değilse False döner."""
    uyeler = verileri_yukle()

    # Kullanıcı adı daha önce alınmış mı kontrol et
    for uye in uyeler:
        if uye["kullanici_adi"] == kullanici_adi:
            print("❌ HATA: Bu kullanıcı adı zaten alınmış!")
            return False

    # Yeni üyeyi oluştur
    yeni_uye = {
        "kullanici_adi": kullanici_adi,
        "sifre": sifre
    }
    
    uyeler.append(yeni_uye)
    verileri_kaydet(uyeler)
    print(f"✅ Başarılı: {kullanici_adi} aramıza katıldı!")
    return True

def uye_giris(kullanici_adi, sifre):
    """Giriş kontrolü yapar. Başarılıysa True döner."""
    uyeler = verileri_yukle()

    for uye in uyeler:
        if uye["kullanici_adi"] == kullanici_adi and uye["sifre"] == sifre:
            print(f"👋 Hoş geldin, {kullanici_adi}!")
            return True
    
    print("❌ HATA: Kullanıcı adı veya şifre hatalı.")
    return False
