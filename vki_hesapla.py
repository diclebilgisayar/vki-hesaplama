def vki_hesapla():
    # Kullanıcıya programın ne yaptığını anlatan başlık
    print("--- Vücut Kitle İndeksi (VKİ) HESAPLAMA ---")
    
    try:
        # Kullanıcıdan kilo bilgisi alınır (kg cinsinden)
        kilo = float(input("Kilonuzu girin (kg): "))
        
        # Kullanıcıdan boy bilgisi alınır (metre cinsinden)
        boy = float(input("Boyunuzu girin (metre, örn: 1.75): "))
        
        # VKİ hesaplama formülü: kilo / (boy * boy)
        vki = kilo / (boy ** 2)
        
        # Hesaplanan VKİ değeri ekrana yazdırılır (2 ondalık basamakla)
        print(f"Vücut Kitle İndeksiniz: {vki:.2f}")
        
        # VKİ değerine göre kullanıcının durumu belirlenir
        if vki < 18.5:
            print("Durum: Zayıf")
        elif 18.5 <= vki < 25:
            print("Durum: Normal")
        elif 25 <= vki < 30:
            print("Durum: Kilolu")
        else:
            print("Durum: Obez")
    
    # Kullanıcı sayı yerine harf vb. girerse bu hata yakalanır
    except ValueError:
        print("Lütfen sayısal değerler giriniz!")

# Fonksiyon çağrılır ve program çalıştırılır
vki_hesapla()
