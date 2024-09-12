def menu():
    menu = """

    ============ MENU ============
    Selecione a opção desejada:

    [1] Depositar
    [2] Sacar
    [3] Consultar extrato
    [4] Novo usuário
    [5] Criar conta
    [6] Listar contas
    [x] Sair

    => """

    return input(menu)

def depositar(saldo, valor, extrato, /):
    # Barra para passar de forma posicional.
    # A função depositar atualiza o saldo e o extrato de uma conta simulada ao realizar um depósito válido (ou seja, maior que zero). 
    # Se o valor do depósito for inválido, ela informa o usuário sem alterar o saldo ou o extrato.

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")

    else:
        print("\n[!} O valor informado é invalido.")

    # Retorna o saldo e o extrato atualizado após a operação.
    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Asterisco para passar de forma nomeada.

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("[!] Você não possui saldo suficiente para concluir esta transação.")
        
    elif excedeu_limite:
        print("[!] O valor do saque excede o limite transacional.")

    elif excedeu_saques:
        print("[!] Você excedeu o limite de saques diários.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    # Definido saldo como posicional e extrato como nomeado.

    print("============ Extrato ============")
    print("Não foram realizadas movimentações nesta conta" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("[!] Já existe um usuário cadastrado com esse CPF.")

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input ("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})

    print("@@@ Usuário criado com sucesso! @@@")

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    # Percorre a lista usuarios e seleciona apenas os dicionários (usuários) cujo campo "cpf" seja igual ao cpf fornecido como argumento para a função.
    
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("@@@ Conta criada com sucesso! @@@ ")

        return {"agencia": agencia, "numero_conta": numero_conta, "usuarios": usuario}
    
    print("[!] Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\

            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuarios']['nome']}
        
        """
        print("=" * 100)
        print(linha)

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

            # Aqui está o saldo atual, o valor que eu quero depositar, e o extrato atual. 
            # Faça o depósito e me devolva o novo saldo e extrato.
            # Esses novos valores (saldo e extrato atualizados) são então armazenados novamente nas variáveis saldo e extrato, substituindo os valores antigos.

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                # A função sacar deve retornar dois valores: saldo e extrato atualizados após o saque.
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "x":
            break

        else:
            print("[!] Opção inválida. Insira novamente a opção desejada.")

main()