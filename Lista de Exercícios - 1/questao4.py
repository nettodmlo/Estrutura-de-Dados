numeros = []

quantidade = int(input("Digite a quantidade de números na lista: "))

for _ in range(quantidade):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print("O maior valor da lista é:", maior)
print("O menor valor da lista é:", menor)
