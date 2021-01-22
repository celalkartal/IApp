##################################
def definePlayer(yas):
    define: str
    if yas > 34:
        define = "Yaşlı"
    elif yas > 25:
        define = "Deneyimli"
    else:
        define = "Genç"
    define += " futbolcu"
    print(define)


##################################

futbolcununYasi = int(input("Futbolcunun yaşını giriniz!\n"))
definePlayer(futbolcununYasi)
