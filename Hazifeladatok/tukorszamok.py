def main():
    szam = input("Adjon meg egy szamot: ")
    
    szamok=['0','1','2','3','4','5','6','7','8','9']

    for i in szam:
        if not i in szamok:
            print("Ez nem egy szam.")
            exit(0)
    
    tukor = True
    i=0
    j=len(szam)-1
    while( i<len(szam) and tukor):
        if(szam[i]!=szam[j]):
            tukor = False
        i+=1
        j-=1
    
    if tukor:
        print("Tukorszam")
    else:
        print("Nem tukorszam")



if __name__ == "__main__":
    main()