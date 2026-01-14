class Kutuphane:
    def __init__(self):
        self.kitaplar = {
        "Sefiller": {"yazar":"Victor Hugo","durum":"Rafta"},
        "Nutuk": {"yazar":"Mustafa Kemal Atatürk","durum":"Rafta"},
        "1984": {"yazar":"George Orwell","durum":"Rafta vs"},
        "kürk mantolu madonna": {"yazar":"Sabahattin Ali","durum":"Rafta"}
    }
    
    def kitaplari_listele(self): #a
            print("---KÜTÜPHANE ARŞİVİ---")
            for ad, bilgi in self.kitaplar.items():
                durum_ikonu = "✅" if bilgi["durum"] == "Rafta" else "❌"
                print(f"{durum_ikonu}{ad}-yazar: {bilgi['yazar']}({bilgi['durum']})") # değişiklik
                
    def kitap_ekle(self):
        kitap_ad = input("Eklenecek kitap adını giriniz: ")
        yazar_ad = input("Eklenecek kitabın yazarını giriniz: ")
        self.kitaplar[kitap_ad] = {"yazar": yazar_ad , "durum": "Rafta"}
        print(f">>> '{kitap_ad}' Başarıyla sisteme eklendi ✅\n")
    
    def kitap_odunc_al(self):
        self.kitaplari_listele()
        secim = input("Ödünç almak istediğiniz kitabın adını giriniz: ")
        if secim in self.kitaplar:
            if self.kitaplar[secim]["durum"] == "Rafta":
                self.kitaplar[secim]["durum"] == "Ödünç verildi"
                print(f"Başarılı! '{secim}' kitabını aldınız")
            else:
                print("Kitap şu an Başkasında ")
        else:
            print("Sistemimizde böyle bir kitap bulunmamaktadır")
            
    
    def kitap_iade_et(self):
        self.kitaplari_listele()
        secim = input("\nİade etmek istediğiniz kitabın adını giriniz: ")
        
        if secim in self.kitaplar:
            if self.kitaplar[secim]["durum"] == "Ödünç Verildi":
                self.kitaplar[secim]["durum"] = "Rafta"
                print(f">>> Teşekkürler! '{secim}' kitabı iade alındı. ✅")
            else:
                print(">>> Bu kitap zaten kütüphanede (Rafta).")
        else:
            print(">>> Bu kitap bizim kütüphaneye ait değil.")
            

kutuphane = Kutuphane()
while True:
    print("1. Listele\n2. Ekle\n3. Ödünç Al\n4. İade Et\n5. Çıkış Yap\n")
    secim = input("Lütfen yapmak istediğiniz işlemi tuşlayınız: ")
    if secim == '1':
        kutuphane.kitaplari_listele()
    elif secim == '2':
        kutuphane.kitap_ekle()
    elif secim == '3':
        kutuphane.kitap_odunc_al()
    elif secim == '4':
        kutuphane.kitap_iade_et() #yeni eklediğimiz
    elif secim == '5':
        break
    else:
        print("Hatalı değer tuşladınız...")
        
        
        
        
    
    
