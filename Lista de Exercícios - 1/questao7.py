limite = int(input("Digite um valor limite para a sequência de Fibonacci: "))

fibonacci = [0, 1]

while fibonacci[-1] + fibonacci[-2] <= limite:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print("Sequência de Fibonacci até", limite, ":")
print(fibonacci)
