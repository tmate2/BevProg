# 2. het 2. hazifeladat

from math import sqrt

def main():
    print('Valasszon az alabbi kepletek kozul:\n\t(1) Pitagorasz\n\t(2) Masodfoku megoldo keplet\n\t(3) Haromszog terulete (Heron-keplet)\n')
    k = int(input('Adja meg a keplet sorszamat (1,2,3): '))

    if(k == 1):
        pitagorasz()
    elif(k == 2):
        masodfoku()
    elif(k == 3):
        heron()
    else:
        print('Ha nem, hát nem...')


###Fuggvenyek###


def pitagorasz():
    print('\n(1) Pitagorasz\n')

    a = float(input('Adja meg az egyik befogo meretet: '))
    b = float(input('Adja meg a masik befogo meretet: '))
    c = sqrt((a**2)+(b**2))

    print('Az atfogo merete: {}'.format(c))


def masodfoku():
    print('\n(2) Masodfoku megoldo keplet\n')

    print('A kovetkezo minta alapjan adja meg az ertekeket: ax^2+bx+c=0')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))

    x1 = ((-1)*b+sqrt((b**2)-4*a*c))/(2*a)
    x2 = ((-1)*b-sqrt((b**2)-4*a*c))/(2*a)

    print('x1 = {0}\nx2 = {1}'.format(x1,x2))


def heron():
    print('\n(3) Haromszog terulete (Heron-keplet)\n')

    a = float(input('Adja meg az a oldal meretet: '))
    b = float(input('Adja meg a b oldal meretet: '))
    c = float(input('Adja meg a c oldal meretet: '))

    if a+b<=c or a+c<=b or b+c<=a:
        print('Ez egy nem megszerkesztheto haromszog...')
        exit()
    
    s = (a+b+c)/2

    terulet = sqrt(s*(s-a)*(s-b)*(s-c))

    print('A haromszog terulete: {}'.format(terulet))

if __name__ == "__main__":
    main()