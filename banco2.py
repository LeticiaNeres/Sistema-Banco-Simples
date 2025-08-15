import textwrap

def menu():
    menu = """\n
    ==================== MENU ====================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    ==> """
    return input(textwrap.dedent(menu))
    
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Saldo insuficiente para saque.")
    
    elif excedeu_limite:
        print("Valor excede o limite de R$500.00 por saque.")
        
    elif excedeu_saques:
        print("Número máximo de saques diários atingido.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}.\n"
        numero_saques += 1
        print(f"Valor de R${valor:.2f} sacado com sucesso!")
    
    else:
        print("Valor inválido para saque. Tente novamente.")
    
    return saldo, extrato
    
    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}.\n"
        print(f"Valor de R${valor:.2f} depositado com sucesso!")
    else:
        print("Valor inválido para depósito. Tente novamente.")
        
    return saldo, extrato
   
   
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Já existe um usuário com esse CPF.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-yyyy): ")  
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")    
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário castrado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Conta criada com suscesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado. Conta não criada.")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia: \t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']} 
        """
        print("-" * 100)
        print(textwrap.dedent(linha))
    
    
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    agencia = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: R$"))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: R$"))

            saldo, extrato = sacar(
                saldo=saldo,    
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas (contas)
            
        elif opcao == "q":
            break
        
        else: 
            print("Operação inválida, por favor selecione novamente a operação desejada.")
                
           
main()