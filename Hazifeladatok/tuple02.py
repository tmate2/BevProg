#https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20120818a
#!/usr/bin/env python3

from cmath import sqrt
import math


def distance(p1, p2):
    # TODO...
    a=p1[0]-p2[0]
    b=p1[1]-p2[1]
    c=sqrt(a**2+b**2)
    return c


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()
