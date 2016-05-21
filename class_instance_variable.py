class Teste():
    i = 0

    def met1(self):
        self.i = self.i + 1

    def pi(self):
        print(self.i)

    @staticmethod
    def met2():
        Teste.i = Teste.i + 5

    @staticmethod
    def pi2():
        print (Teste.i)

# obj = Teste()
# obj.met1()
# obj.pi() #1

# Teste.met2()
# Teste.pi2() #5


# obj.pi() #1

#//////



Teste.met2()
Teste.pi2() #10

obj = Teste()
obj.met1()
obj.pi() #11

obj.pi() #11