#https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20130218b
def main():
    print(valid("Barking!", "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))

def valid(text,chars):
    ns = ""
    for x in text:
        if x in chars:
            ns+=x
    return ns

if __name__ == "__main__":
    main()