import random

def secim_al():

    secenekler = ["taş", "kağıt", "makas"]
    secim = input("Lütfen taş, kağıt veya makas seçin: ").lower()
    while secim not in secenekler:
        secim = input("Geçersiz seçim. Lütfen taş, kağıt veya makas seçin: ").lower()
    return secim

def kazanan_belirle(oyuncu_secim, bilgisayar_secim):

    if oyuncu_secim == bilgisayar_secim:
        return "Berabere"
    elif (oyuncu_secim == "taş" and bilgisayar_secim == "makas") or \
         (oyuncu_secim == "makas" and bilgisayar_secim == "kağıt") or \
         (oyuncu_secim == "kağıt" and bilgisayar_secim == "taş"):
        return "Oyuncu"
    else:
        return "Bilgisayar"

def tur_oyna():

    oyuncu_secim = secim_al()
    bilgisayar_secim = random.choice(["taş", "kağıt", "makas"])
    print(f"Bilgisayarın seçimi: {bilgisayar_secim}")
    return kazanan_belirle(oyuncu_secim, bilgisayar_secim)

def oyunu_baslat():

    print("Taş, Kağıt, Makas oyununa hoş geldiniz!"
          "\n Kurallar: Taş makası, makas kağıdı, kağıt taşı yener."
          "\n İlk iki turu kazanan oyunu kazanır. İyi şanslar!")

    oyuncu_galibiyet = 0
    bilgisayar_galibiyet = 0

    while oyuncu_galibiyet < 2 and bilgisayar_galibiyet < 2:
        sonuc = tur_oyna()
        if sonuc == "Oyuncu":
            print("Bu turu siz kazandınız!")
            oyuncu_galibiyet += 1
        elif sonuc == "Bilgisayar":
            print("Bu turu bilgisayar kazandı!")
            bilgisayar_galibiyet += 1
        else:
            print("Berabere!")

        print(f"Skor: Siz {oyuncu_galibiyet} - {bilgisayar_galibiyet} Bilgisayar")

    if oyuncu_galibiyet == 2:
        print("Tebrikler, oyunu kazandınız!")
    else:
        print("Bilgisayar oyunu kazandı.")

def tas_kagit_makas_MehmetEren_Erdemir():

    while True:
        oyunu_baslat()
        devam = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        bilgisayar_devam = random.choice(["evet", "hayır"])
        print(f"Bilgisayarın devam etme isteği: {bilgisayar_devam}")

        if devam != "evet" or bilgisayar_devam != "evet":
            print("Oyun sona erdi. Teşekkürler!")
            break

tas_kagit_makas_MehmetEren_Erdemir()
