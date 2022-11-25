# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20140314a
def main():
    oldalak = input("nyomtatando oldalak: ").split(",")
    oldallist = []
    for x in oldalak:
        if(x.find("-") > 0):
            tmpl = x.split("-")
            for y in range(int(tmpl[0]),int(tmpl[1])+1):
                oldallist.append(y)
        else: oldallist.append(int(x))

    print(oldallist)

if __name__ == "__main__":
    main()