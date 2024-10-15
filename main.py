menu = """
   *******************
    [c] Criar conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

   *******************
    """

agencia = ""
nome = ""
conta = ""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def criar_conta():
    agencia_usu = input("Digite a agência:")
    conta_usu = input("Digite a conta:")
    nome_usu = input("Digite como você quer ser chamado...\n")
    conta(agencia_usuario=agencia_usu,
          conta_usuario=conta_usu, nome_usuario=nome_usu)
    print("Conta criada com sucesso!")


def get_saldo():
    global saldo
    saldo_conta = saldo
    return saldo_conta


def depositar(*, saldo):
    valor = float(input("Digite o valor que você deseja depositar...\n "))
    if (valor > 0):
        saldo += valor
        print("O valor foi depositado com sucesso!")


def conta(*, agencia_usuario, conta_usuario, nome_usuario):
    global agencia
    global nome
    global conta
    global saldo
    agencia = agencia_usuario
    conta = conta_usuario
    nome = nome_usuario
    return {"agencia": agencia, "conta": conta, "nome": nome, "saldo": saldo}


while (True):
    opcao = input(menu)
    if (opcao == "c"):
        criar_conta()
    elif (opcao == "d"):
        depositar(saldo=get_saldo())
    elif (opcao == "s"):
        print("Sacou")
    elif (opcao == "Extrato"):
        print("Extrato")
    elif (opcao == "q"):
        print("Você saiu do sistema")
        break
    else:
        print("Opção inválida...")
