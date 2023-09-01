numeros = []

quantidade = int(input("Digite a quantidade de números na lista: "))

for _ in range(quantidade):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

numeros_pares = [numero for numero in numeros if numero % 2 == 0]

if numeros_pares:
    media = sum(numeros_pares) / len(numeros_pares)
    print("A média dos números pares é:", media)
else:
    print("Não há números pares na lista.")
