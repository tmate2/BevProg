# https://arato.inf.unideb.hu/szathmary.laszlo/python-solution-checker/check.php?id=20170522a
def kulonbseg(a, b):
    if a>b: return a-b
    if a<b: return b-a
    return 0

def main():
    felhokarcolok = [ord(x) for x in str(2**1024)]
    osszkulonbseg = 0
    i = 0
    while i<len(felhokarcolok)-1:
        osszkulonbseg += kulonbseg(felhokarcolok[i],felhokarcolok[i+1])
        i+=1
    print(osszkulonbseg)


if __name__ == "__main__":
    main()