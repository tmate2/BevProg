#https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20121006d
def main():

    f = open("string1.py", 'r')
    f2 = open('string1_clean.py','w')
    f3 = open('string1_clean2.py','w')
    
    s = f.readline()
    while(s):
        if not s.startswith('#'):
            print(s, end="", file=f2)
            if not s.find('#')>-1:
                print(s, end="", file=f3)
             #else:
                #print(s.replace(s[s.find('#'): ], ""), file=f3)
        s = f.readline()

    f.close
    f2.close
    f3.close

if __name__ == "__main__":
    main()