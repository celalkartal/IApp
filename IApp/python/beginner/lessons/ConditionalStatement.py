
def definePlayer(yas,kilo):
    define: str
    if yas > 34 and kilo>90:
        define = "Yaşlı"
    elif yas > 25 and not kilo > 100:
        define = "Deneyimli"
    else:
        define = "Genç"
    define += " futbolcu"
    print(define)

##################################

futbolcununYasi = int(input("Futbolcunun yaşını giriniz!\n"))
futbolcununKilosu = int(input("Futbolcunun kilosunu giriniz!\n"))
definePlayer(futbolcununYasi,futbolcununKilosu)
