# INICIALIZANDO VARIÁVEIS
saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

def menu():
    print("\n=== MENU ===")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Cadastrar cliente")

    print("[0] Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(" Depósito realizado com sucesso.")
        else:
            print(" Valor inválido para depósito.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

        if excedeu_saldo:
            print(" Saldo insuficiente.")
        elif excedeu_limite:
            print(f" O valor excede o limite de R$ {limite_saque:.2f} por saque.")
        elif excedeu_saques:
            print(" Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(" Saque realizado com sucesso.")
        else:
            print(" Valor inválido para saque.")

    elif opcao == "3":
        print("\n=== EXTRATO ===")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "0":
        print(" Saindo do sistema.  Continue Aprendendo com o  prof:Guilherme!")
        break

    else:
        print(" Opção inválida. Tente novamente.")


