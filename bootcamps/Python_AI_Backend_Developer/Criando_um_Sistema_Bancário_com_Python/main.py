menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
LIMITE_POR_SAQUE = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor = 0.0

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito.")
        try:
            valor = float(input("Digite o valor que tu deseja depositar: ")) 
            if valor >= 0:
                saldo += valor
                print("O valor foi depositado com sucesso.")
            else:
                print("O valor precisa ser maior que  zero.")
        except:
            print("Entrada inválida.")

    elif opcao == "s":
        print("Saque.")
        if numero_saques < LIMITE_SAQUES:
            try:
                valor = float(input("Digite o valor que tu deseja sacar: ")) 
                if valor >= 0:
                    if valor > saldo:
                        print("Só é possivel sacar um valor menor ou igual ao valor em saldo.")
                    else:
                        if valor <= LIMITE_POR_SAQUE:
                            numero_saques += 1
                            saldo -= valor
                            print("O valor foi sacado com sucesso.")
                        else:
                            print(f"O limite máximo por saque é de R$ {LIMITE_POR_SAQUE:0.2f}.")
                else:
                    print("O valor precisa ser maior que  zero.")
            except:
                print("Entrada inválida.")
        else:
            print("Numero de saques diário foi excedido.")

    elif opcao == "e":
        print("Extrato.")
        extrato = "{:0.2f}".format(saldo)
        print(f"O valor atual em saldo: R$ {extrato}")
        
    elif opcao == "q":
        print("Saindo.")
        break

    else:
        print("Opção inválida.")
