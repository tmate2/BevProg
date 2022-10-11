class Developers():

    def __init__(self, name, payment, level="junior", years=0):
        self.name = name
        self.payment = payment
        self.level = level
        self.years = years

    def payRaise(self, pluss=10000):
        self.payment+=pluss

    def nextYear(self):
        self.years+=1

    def devLevel(self):
        levelstr = "{}'s recommended level is {} and he/she is {}"
        if self.years == 0:
            print(levelstr.format(self.name,"intern",self.level))
        elif self.years in range(1,3):
            print(levelstr.format(self.name,"junior",self.level))
        elif self.years in range(3,6):
            print(levelstr.format(self.name,"medior",self.level))
        else:
            print(levelstr.format(self.name,"senior",self.level))

    def __str__(self):
         return "Name: {}, level: {}, years: {}, payment: {} Ft.".format(self.name,self.level,self.years,self.payment)


def main():
    gyula = Developers("Gyula", 250000)
    bela = Developers("Bela", 450000, "medior", 7)
    kristof = Developers("Kristof", 200000, "intern")
    gergo = Developers("Gergo", 500000,"senior",7)

    kristof.payRaise()
    gergo.payRaise(50000)
    gyula.nextYear()

    kristof.devLevel()
    gyula.devLevel()
    bela.devLevel()
    gergo.devLevel()

    print()

    print(kristof)
    print(gyula)
    print(bela)
    print(gergo)


if __name__ == "__main__":
    main()