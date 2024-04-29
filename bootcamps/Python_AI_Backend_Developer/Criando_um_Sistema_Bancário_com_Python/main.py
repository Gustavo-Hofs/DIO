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

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito.")

    elif opcao == "s":
        print("Saque.")

    elif opcao == "e":
        print("Extrato.")
        extrato = "{:0.2f}".format(saldo)
        print(f"O valor atual em saldo: R$ {extrato}")
        
    elif opcao == "q":
        print("Saindo.")
        break

    else:
        print("Opção inválida.")
