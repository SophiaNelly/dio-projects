# Dicionário para armazenar contas bancárias simuladas
contas = {}

# Função para exibir o menu e obter a opção do usuário
def exibir_menu():
    menu = """
    === Menu ===
    [1] Criar Nova Conta
    [2] Acessar Conta Existente
    [3] Depositar
    [4] Sacar
    [5] Transferir
    [6] Consultar Saldo
    [7] Extrato
    [8] Sair
    
    => """
    print(menu)
    return input().strip()


def criar_nova_conta():
    numero_conta = input("Digite o número da nova conta: ").strip()
    senha = input("Digite a senha para a nova conta: ")
    saldo_inicial = float(input("Informe o saldo inicial da conta: "))

    if numero_conta in contas:
        print("Conta já existe!")
        return
    
    contas[numero_conta] = {
        'senha': senha,
        'saldo': saldo_inicial,
        'extrato': [],
        'limite': 500,
        'saques': 0
    }
    print(f"Conta {numero_conta} criada com sucesso!")


def acessar_conta_existente():
    numero_conta = input("Digite o número da conta: ").strip()
    senha = input("Digite a senha: ")

    if numero_conta in contas and contas[numero_conta]['senha'] == senha:
        print(f"Acesso autorizado! Bem-vindo, conta {numero_conta}!")
        return numero_conta
    else:
        print("Número de conta ou senha incorretos.")
        return None


def realizar_deposito(numero_conta):
    valor_deposito = float(input("Informe o valor do depósito: "))
    if valor_deposito > 0:
        contas[numero_conta]['saldo'] += valor_deposito
        contas[numero_conta]['extrato'].append(f"Depósito: +R$ {valor_deposito:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")


def realizar_saque(numero_conta):
    valor_saque = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor_saque > contas[numero_conta]['saldo']
    excedeu_limite = valor_saque > contas[numero_conta]['limite']
    excedeu_saques = contas[numero_conta]['saques'] >= 3

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor_saque > 0:
        contas[numero_conta]['saldo'] -= valor_saque
        contas[numero_conta]['extrato'].append(f"Saque: -R$ {valor_saque:.2f}")
        contas[numero_conta]['saques'] += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")


def realizar_transferencia(numero_conta):
    conta_destino = input("Informe o número da conta de destino: ").strip()
    if conta_destino not in contas:
        print("Conta de destino não encontrada.")
        return
    
    valor_transferencia = float(input("Informe o valor da transferência: "))

    excedeu_saldo = valor_transferencia > contas[numero_conta]['saldo']
    excedeu_limite = valor_transferencia > contas[numero_conta]['limite']

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor da transferência excede o limite.")
    elif valor_transferencia > 0:
        contas[numero_conta]['saldo'] -= valor_transferencia
        contas[conta_destino]['saldo'] += valor_transferencia
        contas[numero_conta]['extrato'].append(f"Transferência enviada para {conta_destino}: -R$ {valor_transferencia:.2f}")
        contas[conta_destino]['extrato'].append(f"Transferência recebida de {numero_conta}: +R$ {valor_transferencia:.2f}")
        print("Transferência realizada com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")


def consultar_saldo(numero_conta):
    print(f"Saldo disponível: R$ {contas[numero_conta]['saldo']:.2f}")


def exibir_extrato(numero_conta):
    print("\n=== Extrato ===")
    if not contas[numero_conta]['extrato']:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in contas[numero_conta]['extrato']:
            print(movimentacao)
    print(f"\nSaldo: R$ {contas[numero_conta]['saldo']:.2f}")
    print("===============")


def main():
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            criar_nova_conta()

        elif opcao == "2":
            numero_conta = acessar_conta_existente()
            if numero_conta:
                operar_conta(numero_conta)

        elif opcao == "3":
            realizar_deposito(numero_conta)

        elif opcao == "4":
            realizar_saque(numero_conta)

        elif opcao == "5":
            realizar_transferencia(numero_conta)

        elif opcao == "6":
            consultar_saldo(numero_conta)

        elif opcao == "7":
            exibir_extrato(numero_conta)

        elif opcao == "8":
            print("Sessão encerrada. Obrigado!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


def operar_conta(numero_conta):
    print(f"Bem-vindo, conta {numero_conta}!")



if __name__ == "__main__":
    main()
