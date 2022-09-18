# 2. het 3. hazifeladat
#2*Na + Clˇ2 = 2*NaCl

def main():
    natrium = int(input('Natrium: '))
    klor = int(input('Klor: '))
    so = 0
    excessNatrium = 0
    excessKlor = 0

    if natrium == klor*2:
        so = natrium
    elif natrium > klor*2:
        so = klor
        excessNatrium = natrium-klor*2
    else:
        so = natrium
        excessKlor = klor*2-natrium

    print('Letrejott konyhaso: {0}\nmaradek natriumatom: {1}\nmaradek kloratom: {2}'.format(so,excessNatrium,excessKlor))

if __name__ == "__main__":
    main()