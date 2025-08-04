menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$"))       
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}.\n"
            print(f"Valor de R${valor:.2f} depositado com sucesso!")
            
        else: print("Valor inválido para depósito. Tente novamente.")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$"))

        if limite <= 0:
            print("Valor limite diário de R$500.00 para saques foi atingido.")
        elif valor <= 0:
            print("Valor inválido para saque. Tente novamente.")
        elif valor > saldo:
            print("Saldo insuficiente para saque.")
        elif valor > limite:
            print(f"Valor excede o limite disponível para saque. Limite restante: R${limite:.2f}")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}.\n"
            numero_saques += 1
            limite -= valor
            print(f"Valor de R${valor:.2f} sacado com sucesso!")
            if limite <= 0:
                print("Valor limite diário de R$500.00 para saques foi atingido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            print(extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==========================================")
        
    elif opcao == "q":
        print("Saindo do sistema...")
        break
    
    else: 
        print("Opção inválida. Tente novamente.")
