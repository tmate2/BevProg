# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120815l
def caesar(c, k):
    if not c.isalpha(): return c
    elif chr(ord(c)+k).isalpha(): return chr(ord(c)+k)
    elif (c.islower() and ord(c)+k>ord('z')): return chr(ord(c)+k-26)
    elif (c.islower() and ord(c)+k<ord('a')): return chr(ord(c)+k+26)
    elif (c.isupper() and ord(c)+k>ord('Z')): return chr(ord(c)+k-26)
    return chr(ord(c)+k+26)


def main():

    titok = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""

    key = ord('G')-ord('E')
    uzenet = ""
    for x in titok:
        uzenet += caesar(x, key)
    print(uzenet)

if __name__ == "__main__":
    main()