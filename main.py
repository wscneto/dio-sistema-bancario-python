# Projeto desenvolvido por Walter Soares Costa Neto, para o Lab Project "Criando um Sistema Bancário com Python" da DIO.

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("\nOperação falhou! Valor inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, num_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("\nOperação falhou! Saldo insuficiente.")
    elif num_saques >= LIMITE_SAQUES:
        print("\nOperação falhou! Limite de saques diários foi atingido.")
    elif valor > limite:
        print("\nOperação falhou! Saque desejado ultrapassou o limite.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saques += 1
    else:
        print("\nOperação falhou! Valor inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n")
    print("EXTRATO".center(41, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("FIM".center(41, "="))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somento números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Operação falhou! Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Operação falhou! Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    menu = """

    [d] = Depositar
    [s] = Sacar
    [e] = Extrato
    [nu] = Novo Usuário
    [nc] = Nova Conta
    [q] = Sair

    => """

    extrato, saldo, limite, num_saques, LIMITE_SAQUES = ("", 0, 500, 0, 3)
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = input(menu)

        # Depositar
        if opcao == "d":
            valor = float(input("Informe o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        # Sacar
        elif opcao == "s":
            valor = float(input("Informe o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                LIMITE_SAQUES=LIMITE_SAQUES
                )

        # Extrato
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        # Sair
        elif opcao == "q":
            print("\nAté logo!")
            break

        # Criar usuário
        elif opcao == "nu":
            criar_usuario(usuarios)

        # Criar conta
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        # Opção inválida
        else:
            print("\nOperação falhou! Por favor selecione uma opção válida.")

main()