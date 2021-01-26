def SayiBul():
    while True:
        sayi = int(input("sayi giriniz\n"))
        if sayi > 10:
            print("büyük\n")
        elif sayi < 10:
            print("kucuk\n")
        else:
            print("bulundu!\n")
            break;


def sayiYazdir():
    sayi = int(input("sayi giriniz\n"))
    for i in range(3, sayi + 1):
        print(i, end="\n")


def UnsuzHarfileriBul():
    karakterler = "aeıioöuü";
    name = input("isminizi giriniz\n")
    for i in name:
        if i not in karakterler:
            if i == "k":
                break;
            else:
                print("Ünsüz harf", i, sep=":", end="\n")
    else:  # else ifadesi dongülerle bir anlamı var. eğer break olmuşsa,
        # else çalışmaz. break olmamışsa, normal program akışı gibidir. yani çalışır
        print("Bu isimde K harfi yoktur!")



    # SayiBul()


# sayiYazdir()
UnsuzHarfileriBul()
