menu = """

    Selecione a opção desejada:

    [1] Depositar
    [2] Sacar
    [3] Consultar extrato
    [4] Sair

=> """

saldo = 0 # Saldo inicial = 0
limite = 500
extrato = "" # String que regista as movimentações de saque e depósito
numero_saques = 0 # Conta quantos saques foram realizados (Inicialmente = 0)
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("------- Depósito -------")
        valor = float(input("Informe o valor para depósito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n" #Registra no extrato

        else:
            print("Operação inválida.")
            
    elif opcao == "2":
        print("------- Saque -------")
        valor = float(input("Informe o valor para saque: \n"))

        # Validações:

        limite_saldo = valor > saldo # Valor do saque não pode ser maior que o saldo disponível.
        limite = valor > limite # Valor do saque não pode ser maior que o limite estabelecido.
        acima_saques = numero_saques >= LIMITE_SAQUE # Não exceder o limite diário de saques.

        if limite_saldo:
            print("Você não possui saldo suficiente para concluir esta operação.")

        elif limite:
            print("O valor do saque excede o limite disponível.")

        elif acima_saques:
            print("Você excedeu o limite de saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1 # Aumenta o número de saques realizados.

        else:
            print("Operação inválida.")

    elif opcao == "3":
        print("------- Extrato -------")
        print("Não há movimentações.") if not extrato else extrato
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        
    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

