def main():
    f = open("pivers.txt",'r')
    li = str(f.readline()).split(sep=" ")
    f.close

    f = open("pinum.txt","w")
    for x in li:
        print(len(x),end="", file=f)
        if(x == li[0]):
            print(".",end="", file=f)
    f.close

if __name__ == "__main__":
    main()