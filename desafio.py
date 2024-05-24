limite = 500
LIMITE_SAQUE = 3
saldo = 0
extrato = ""
numero_saques = 0


menu = """
[1] DEPOSITAR 
[2] SACAR
[3] EXTRATO
[4] SAIR

"""

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: \n"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque\n"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("operação falhou! O valor informado é inválido.")

    elif opcao == "3":

        print("\n============ EXTRATO =========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "4":
        break

    else: ("Operação inválida, por favor selecione novamente a operação desejada.")

