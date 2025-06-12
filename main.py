# Projeto desenvolvido por Walter Soares Costa Neto, para o Lab Project "Criando um Sistema Bancário com Python" da DIO.

menu = """

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

=> """

saldo, limite, num_saques, LIMITE_SAQUES = (0, 500, 0, 3)
extrato = ""

while True:
    opcao = input(menu)

    # Depositar
    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\nOperação falhou! Valor inválido.")
    
    # Sacar
    elif opcao == "s":
        if num_saques >= LIMITE_SAQUES:
            print("\nOperação falhou! Limite de saques diários foi atingido.")
            continue

        valor = float(input("Informe o valor que deseja sacar: "))

        if valor > saldo:
            print("\nOperação falhou! Saldo insuficiente.")
        elif valor > limite:
            print("\nOperação falhou! Saque desejado ultrapassou o limite.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saques += 1
        else:
            print("\nOperação falhou! Valor inválido.")

    # Extrato
    elif opcao == "e":
        print("\n")
        print("EXTRATO".center(41, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("FIM".center(41, "="))

    # Sair
    elif opcao == "q":
        print("\nAté logo!")
        break

    # Opção inválida
    else:
        print("\nOperação falhou! Por favor selecione uma opção válida.")
