import random

pontos_usuario = 0
pontos_pc = 0
options = ['pedra','papel','tesoura']

#alteração para commitar no git

while True:
    print("\n--------------------------------------------------")
    print("Escolha uma das opções ou digite Sair para sair ")
    opcao_usuario = input("\nPedra | Papel | Tesoura ").lower()
    if opcao_usuario == "sair":
        break
    if opcao_usuario not in options:
        print("Por favor, digite uma opção válida!")
        continue

    random_number = random.randint(0,2)
    # pedra: 0, papel: 1, tesoura: 2
    escolha_pc = options[random_number]
    print(f"\nPC escolheu: {escolha_pc}.")

    if opcao_usuario == "pedra" and escolha_pc == "tesoura":
            print("Você venceu!")
            pontos_usuario += 1
    elif opcao_usuario == "papel" and escolha_pc == "pedra":
            print("Você venceu!")
            pontos_usuario += 1
    elif opcao_usuario == "tesoura" and escolha_pc == "papel":
            print("Você venceu!")
            pontos_usuario += 1
    elif opcao_usuario == escolha_pc:
        print("Empate!")
        pontos_usuario += 1
    else:
        print("Você perdeu!")
        pontos_pc += 1

print(f"\nVocê ganhou: {pontos_usuario} pontos")
print(f"O PC ganhou: {pontos_pc} pontos")
print("\nObrigado por jogar!")
print("--------------------------------------------------\n")