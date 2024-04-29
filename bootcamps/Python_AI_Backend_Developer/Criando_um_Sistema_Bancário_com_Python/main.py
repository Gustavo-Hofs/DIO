menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE_POR_SAQUE = 500
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
        
    elif opcao == "q":
        print("Saindo.")
        break

    else:
        print("Opção inválida.")
