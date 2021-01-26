import math
cap=input("Dairenin çapını giriniz?\n")

# inputtan alınan değer bir string oldugundan,
# bu stringin önce float tipine dönüştürüp,
# sonra da bölme işlemi gerekiyor

yaricap=float(cap)/2

alan=  math.pi*(yaricap**2)
print("Alan:",alan,end="\n")
alan=round(alan,2)
print("Alan:", alan, end="\n")
beklenti=input("sizin beklentiniz nedir?\n")#67*34-45
# eval() fonksiyonun görevi, kendisine verilen
# KARAKTER yani string dizilerini değerlendirmeye
# tabi tutmak ya da işlemektir.

beklenti=eval(beklenti)

print("beklenti:",type(beklenti), beklenti, end="\n")

name=input("isminiz nedir?\n")
surname=input("soyadınız nedir?\n")

#format konsiyonu kullanmak
print("Adı: {}\nSoyadı:{}".format(name,surname))