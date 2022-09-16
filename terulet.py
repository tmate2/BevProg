#globális változó:
#a=2

def main():
    a=int(input('A oldal: '))
    b=int(input('B oldal: '))

    print('Terület: {t}'.format(t = a*b),end=';\n')

if __name__ == "__main__":
    main()
