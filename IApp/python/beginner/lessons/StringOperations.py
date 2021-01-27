veri = "celal kartal"
print(veri[4])
veri2 = veri
print(veri2)
print(veri[::-1])
print(len(veri2))
print(veri[2:-3])
print(veri[-4:-3])
i = 3
print("isminizin {}.harfi {} harfidir".format(i + 1, veri[i]))

site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"
toplam = site1, site2, site3, site4
print(toplam)
for isim in toplam:
    print(toplam.index(isim) + 1, ".site: ", isim[4:-4], sep="")
print("---------------------------------------------------------")

veri3 = "Benim için tek yol çalışmak"
veri4 = {i: veri3.index(i) for i in veri3}
print(veri4)

veri5 = {i: toplam.index(i) for i in toplam}
print(veri5)

veri6 = {str(toplam.index(i) + 1) + ".site: " + str(i[4:-4]) for i in toplam}

for s,m in enumerate(veri6):
    print(s+1,m)

print(veri)
veri7=veri.replace("c","d")
print(veri7)
