#ESSE É MEU NOVO CODIGO


# === Sistema de Caixa Eletrônico com Cadastro de Clientes ===

# Configurações
limite_saque = 500
LIMITE_SAQUES_DIARIOS = 3

# Base de dados simulada
clientes = {}

# Função para exibir o menu
def menu():
    print("\n=== MENU ===")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Cadastrar cliente")
    print("[0] Sair")

# Função para cadastrar cliente
def cadastrar_cliente():
    cpf = input("Digite o CPF do cliente: ")
    nome = input("Digite o nome do cliente: ")

    if cpf in clientes:
        print(" Cliente já cadastrado.")
    else:
        clientes[cpf] = {
            "nome": nome,
            "saldo": 0,
            "extrato": "",
            "numero_saques": 0
        }
        print(f" Cliente {nome} cadastrado com sucesso!")

# Função para selecionar cliente
def selecionar_cliente():
    cpf = input("Digite o CPF do cliente: ")
    if cpf in clientes:
        return cpf
    else:
        print(" Cliente não encontrado.")
        return None

# Função de depósito
def depositar():
    cpf = selecionar_cliente()
    if cpf:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            clientes[cpf]["saldo"] += valor
            clientes[cpf]["extrato"] += f"Depósito: R$ {valor:.2f}\n"
            print(" Depósito realizado com sucesso.")
        else:
            print(" Valor inválido para depósito.")

# Função de saque
def sacar():
    cpf = selecionar_cliente()
    if cpf:
        valor = float(input("Informe o valor do saque: "))
        cliente = clientes[cpf]

        excedeu_saldo = valor > cliente["saldo"]
        excedeu_limite = valor > limite_saque
        excedeu_saques = cliente["numero_saques"] >= LIMITE_SAQUES_DIARIOS

        if excedeu_saldo:
            print(" Saldo insuficiente.")
        elif excedeu_limite:
            print(f" O valor excede o limite de R$ {limite_saque:.2f} por saque.")
        elif excedeu_saques:
            print(" Número máximo de saques diários atingido.")
        elif valor > 0:
            cliente["saldo"] -= valor
            cliente["extrato"] += f"Saque: R$ {valor:.2f}\n"
            cliente["numero_saques"] += 1
            print(" Saque realizado com sucesso.")
        else:
            print(" Valor inválido para saque.")

# Função de extrato
def ver_extrato():
    cpf = selecionar_cliente()
    if cpf:
        cliente = clientes[cpf]
        print(f"\n=== EXTRATO de {cliente['nome']} ===")
        print(cliente["extrato"] if cliente["extrato"] else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {cliente['saldo']:.2f}")

# Loop principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        depositar()
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        ver_extrato()
    elif opcao == "4":
        cadastrar_cliente()
    elif opcao == "0":
        print(" Saindo do sistema. Continue aprendendo com o prof: Guilherme!")
        break
    else:
        print(" Opção inválida. Tente novamente.")
