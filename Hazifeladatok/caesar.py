def main():
    s = "kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    key = 3
    print(encrypt(s,key))

def encrypt(s, k):
    ns = ""
    for x in s:
        ns += chr(ord(x)-k)
    return ns

if __name__ == "__main__":
    main()