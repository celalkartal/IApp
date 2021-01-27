def ayriAyriHata():
    try:
        print(*"HOŞ GELDİNİZ!", sep=" ", end="\n\n")
        sayi = int(input("Birinci sayıyı giriniz!\n"))
        sayi = hataFırlatmaOrnek(sayi, 0)

        result = sayi ** 2
        print("result", result, sep=":", end="\n")

    except ValueError as hata:
        print("Lütfen rakam giriniz! Detay:", hata, sep="\n", end="\n")
    except ZeroDivisionError as hata:
        print("Sıfıra bölünme hatası! Detay:", hata, sep="\n", end="\n")
    except Exception as hatamVar:
        print("Hata yakalandı. Detay:", hatamVar, sep="\n", end="\n\n")
    finally:
        print(*"Hoşça Kalın!", sep=" ")


def hataFırlatmaOrnek(sayi1, sayi2):
    try:
        result = sayi1 / sayi2
        return result
    except ZeroDivisionError as hata:
        print("Hata alındı,şimdi fırlatılacak!...\n")
        raise Exception("Sıfıra bölme hatası")


ayriAyriHata()
