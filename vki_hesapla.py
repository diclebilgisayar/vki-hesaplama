def vki_hesapla():
    print("--- Vucut Kitle İndeksi (VKİ)  HESAPLAMA ---")
    try:
        kilo = float(input("Kilonuzu girin (kg): "))
        boy = float(input("Boyunuzu girin (metre, örn: 1.75): "))
        
        vki = kilo / (boy ** 2)
        print(f"Vücut Kitle İndeksiniz: {vki:.2f}")
        
        if vki < 18.5:
            print("Durum: Zayıf")
        elif 18.5 <= vki < 25:
            print("Durum: Normal")
        elif 25 <= vki < 30:
            print("Durum: Kilolu")
        else:
            print("Durum: Obez")
    except ValueError:
        print("Lütfen sayısal değerler giriniz!")

vki_hesapla()

