# 5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método 
# chamado “falar” que imprime uma mensagem com o nome da pessoa

class Pessoa:
    def falar(self, nome, idade):
        print(f"Olá, {nome}. Você tem {idade} mesmo??")

falar = Pessoa()
falar.falar("Paulo Renan", 20)
    