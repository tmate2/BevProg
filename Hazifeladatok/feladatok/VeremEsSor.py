# https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.20141125a
class Verem():
    
    def __init__(self):
        self.verem = ""

    def betesz(self, num):
        self.verem += str(num)+" "

    def kivesz(self):
        if (self.verem == ""): return None
        tmpl = self.verem.split(" ")
        self.verem = self.verem[0:len(self.verem)-1-len(tmpl[len(tmpl)-2])]
        return int(tmpl[len(tmpl)-2])

    def meret(self):
        return len(self.verem.split(" "))

    def ures(self):
        if(self.verem == ""): return True
        return False

    def __str__(self):
        return "["+self.verem

class Sor():

    def __init__(self):
        self.sor = ""

    def beall(self, num):
        self.sor += str(num)+" "

    def kiall(self):
        if (self.sor == ""): return None
        tmpl = self.sor.split(" ")
        self.sor = ""
        for i in range(1,len(tmpl)-1):
            self.sor += tmpl[i]+" "
        return int(tmpl[0])

    def meret(self):
        return len(self.sor.split(" "))-1

    def ures(self):
        if(self.sor == ""): return True
        return False

    def __str__(self):
        return "["+self.sor

    

def main():

    v = Verem()
    print(v)
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)

    print("#"*10)

    s = Sor()
    print(s)
    print(s.ures())
    s.beall(1)
    s.beall(4)
    s.beall(5)
    print(s)
    print(s.meret())
    print(s.ures())
    x = s.kiall()
    print(x)
    print(s)
    s.kiall()
    s.kiall()
    x = s.kiall()
    print(x)


if __name__ == "__main__":
    main()