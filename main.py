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


def depositar():
    global saldo
    valor_a_depositar = float(input("Digite o valor que você deseja depositar...\n "))
    if (valor_a_depositar > 0):
        saldo += valor_a_depositar
        print(f"O valor foi depositado com sucesso, seu saldo é de R${saldo:.2f}")
        registrar_processo(processo="Depósito", valor=valor_a_depositar, saldo_momento=saldo)


def sacar():
    global limite
    global LIMITE_SAQUES
    global saldo
    global numero_saques
    observacao="Para fazer saques, temos um limte por saque de R$500,00 e podendo ser feito apenas 3 saques por dia.\n"
    print(f"{observacao}")
    valor_a_sacar= float(input("Digite o valor que deseja sacar...\n"))
    if(valor_a_sacar<limite and valor_a_sacar<saldo and numero_saques <LIMITE_SAQUES):
        saldo-=valor_a_sacar
        numero_saques+=1
        qtd_restante_saques= LIMITE_SAQUES-numero_saques
        print(f"Saque realizado com sucesso, seu saldo atual é de R${saldo:.2f} e você tem ainda pode realizar {qtd_restante_saques} saques hoje...\n")
        registrar_processo(processo="Saque", valor=valor_a_sacar, saldo_momento=saldo)
    elif(numero_saques == LIMITE_SAQUES):
        print("Você chegou ao limite de saques por hoje...")
    elif(valor_a_sacar>saldo):
        print("O valor ao qual você deseja sacar é maior do que o saldo presente na sua conta. ")
    elif(valor_a_sacar> limite):
        print(f"Valor de saque desejado é maior que R${limite:.2f},sendo esse o limite por saque.")
    else:
        print("Algo deu errado no processo de saque...")


def registrar_processo(*,processo,valor, saldo_momento):
    global extrato
    extrato +=f"Foi realizado um {processo} no valor R${valor:.2f} sendo assim o seu saldo de momento é:{saldo_momento:.2f}\n"

def extrato_conta():
    global extrato
    print(extrato)

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
        depositar()
    elif (opcao == "s"):
        sacar()
    elif (opcao == "e"):
        extrato_conta()
    elif (opcao == "q"):
        print("Você saiu do sistema")
        break
    else:
        print("Opção inválida...")
