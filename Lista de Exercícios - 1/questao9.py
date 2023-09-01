quantidade = int(input("Digite a quantidade de nomes na lista: "))

nomes = []
for _ in range(quantidade):
    nome = input("Digite um nome: ")
    nomes.append(nome)

nomes_com_a = [nome for nome in nomes if nome.startswith('A') or nome.startswith('a')]

print("Nomes que começam com 'A':")
print(nomes_com_a)
