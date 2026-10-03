#FOR
alunos = [
    {"nome": "Ana", "notas": [8, 7, 9]},
    {"nome": "Bruno", "notas": [5, 6, 4]},
    {"nome": "Carla", "notas": [10, 9, 8]},
]

for aluno in alunos:
    soma = 0

    for nota in aluno["notas"]:
        soma += nota

    media = soma / len(aluno["notas"])

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f'{aluno["nome"]}: média {media:.1f} — {situacao}')

#While
saldo = 1000.00
opcao = ""

while opcao != "4":
    print("\n=== Caixa eletrônico ===")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Seu saldo é R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("Quanto deseja depositar? R$ "))

        if valor > 0:
            saldo += valor
            print(f"Depósito feito. Novo saldo: R$ {saldo:.2f}")
        else:
            print("Digite um valor maior que zero.")

    elif opcao == "3":
        valor = float(input("Quanto deseja sacar? R$ "))

        if valor <= 0:
            print("Digite um valor maior que zero.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            print(f"Saque feito. Novo saldo: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Obrigado por usar o caixa eletrônico!")

    else:
        print("Opção inválida. Escolha de 1 a 4.")
       