menu = """
   *******************
  
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

   *******************
    """


nome = ""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


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
    if(valor_a_sacar<=limite and valor_a_sacar<saldo and numero_saques <LIMITE_SAQUES):
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
    global saldo
    if (extrato==""):
        print(f"Nenhum processo foi realizado até o momento...\n Seu saldo atual é de R${saldo:.2f}")
    else:
        print(extrato)


while (True):
    opcao = input(menu)
    if (opcao == "d"):
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
