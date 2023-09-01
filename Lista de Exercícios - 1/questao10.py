import random

escolhas = ['Pedra', 'Papel', 'Tesoura']

print("Escolha uma opção:")
print("1. Pedra")
print("2. Papel")
print("3. Tesoura")

escolha_usuario = int(input("Digite o número correspondente à sua escolha: ")) - 1

if escolha_usuario < 0 or escolha_usuario >= len(escolhas):
    print("Escolha inválida.")
else:
    escolha_computador = random.randint(0, 2)

    print("Você escolheu:", escolhas[escolha_usuario])
    print("O computador escolheu:", escolhas[escolha_computador])

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 0 and escolha_computador == 2) or \
            (escolha_usuario == 1 and escolha_computador == 0) or \
            (escolha_usuario == 2 and escolha_computador == 1):
        print("Você venceu!")
    else:
        print("O computador venceu!")
