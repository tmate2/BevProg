# 2. het 1. hazifeladat

def main():
    age = int(input('Adja meg az eletkorat: '))

    if(age>20):
        print('On ihat alkoholt Amerikaban, vehet dohanytermeket Magyarorszagon, szerezhet jogositvanyt es a Shrek 2-t mar reg latnia kellett volna...')
    elif(age>17):
        print('On vehet dohanytermeket Magyarorszagon, szerzhet jogositvanyt es megnezheti a Shrek 2-t is.')
    elif(age>15):
        print('On szerzhet jogositvanyt es megnezheti a Shrek 2-t is.')
    elif(age>11):
        print('On megnezheti a Shrek 2-t.')
    else:
        print('Meg {0} evet varnod kell, hogy megnezhesd a Shrek 2-t.'.format(12-age))

if __name__ == "__main__":
    main()
