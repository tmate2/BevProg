from cmath import pi

def main():
    print("Valassza ki, hogy mit szeretne kiszamolni:\n\t1) Teglalap terulete\n\t2) Kor terulete\n\t3) Gula terfogata\n\t4) Kup terfogata")
    valasz = int(input("Feladat: "))
 
    if(valasz == 1):
        print("Az on altal beirt teglalap terulete {} m^2".format(teglalapTerulet()))
    elif(valasz == 2):
        print("Az on altal beirt kor terulete {} m^2".format(korTerulet()))
    elif(valasz == 3):
        print("Az on altal beirt gula terfogata {} m^3".format(gulaTerfogat()))
    elif(valasz == 4):
        print("Az on altal beirt kup terfogata {} m^3".format(kupTerfogat()))
    else:
        print("Ilyen valasztasi lehetoseg nincs.")


###fuggvenyek###


def magassag():
    return float(input("Adja meg a magassagot: "))

def teglalapTerulet():
    a = float(input("Adja meg a teglalap 'a' oldalat: "))
    b = float(input("Adja meg a teglalap 'b' oldalat: "))
    return a*b

def korTerulet():
    r = float(input("Adja meg a kor sugarat: "))
    return r**2 * pi

def gulaTerfogat():
    terfogat = (teglalapTerulet()*magassag())/3
    return terfogat

def kupTerfogat():
    terfogat = (korTerulet()*magassag())/3
    return terfogat


if __name__ == "__main__":
    main()
