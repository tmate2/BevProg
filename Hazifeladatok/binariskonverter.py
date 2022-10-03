#https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120820b
def main():
    a = 156
    print(binConvert(a))
    # print(3%2)

def binConvert(a):
    binar=""
    while(a!=0):
        b=a//2
        binar=str(a%2)+binar
        a=b
    return binar

if __name__ == "__main__":
    main()