def main():
    s = "Az egy bogre. Az meg egy masik bogre?"
    x = Beszur(s)
    print(x.foo("bogre","piros"))

########

class Beszur:
    def __init__(self, s):
        self.s = s

    def foo(abc,s1,s2):
        li = abc.s.split()
        ns = ""
        for x in li:
            tmp = ""
            if not x[len(x)-1].isalpha():
                tmp = x[len(x)-1]
                x=x[0:len(x)-1]
                
            if x == s1:
                ns+=s2+" "
            ns+=x+tmp+" "
        return ns    

if __name__ == "__main__":
    main()
