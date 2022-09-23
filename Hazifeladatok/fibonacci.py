def main():
    n = int(input("Adjon meg egy szamot: "))

    if n == 0:
        print(0)
        exit(0)

    i=0
    fib1 = 0
    fib2 = 1
    while(i<n-1):
        fib1, fib2=fib2, fib1+fib2
        i+=1

    print(fib2)



if __name__ == "__main__":
    main()

#0 1 1 2 3 5 8 13