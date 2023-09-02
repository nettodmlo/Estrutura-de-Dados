class IMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.imc = (self.peso/self.altura**2)

    def imprime(self):
        print(self.imc)

p1=CalculaIMC(90, 1.78)
p1.imprime()
