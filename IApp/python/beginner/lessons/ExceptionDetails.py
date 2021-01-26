
def ayriAyriHata():
    try:
        print(*"***HOŞ GELDİNİZ!***",sep=" ",end="\n\n")
        sayi = int(input("Birinci sayıyı giriniz!\n"))
        sayi=hataFırlatmaOrnek(sayi,0)

        result = sayi ** 2
        print("result",result,sep=":",end="\n")

    except ValueError as hata:
        print("Lütfen rakam giriniz! Detay:",hata,sep="\n")
    except ZeroDivisionError as hata:
        print("Sıfıra bölünme hatası! Detay:", hata, sep="\n")
    except Exception as hatamVar:
        print("Hata fırlatma örneği çalıştı. Detay:", hatamVar, sep="\n")

def hataFırlatmaOrnek(sayi1, sayi2):
    try:
      result=sayi1/sayi2
      return result
    except ZeroDivisionError as hata:
        raise Exception("Sıfıra bölme hatası")


ayriAyriHata()


