import meumodulo

numero_de_saques_restantes = 3
saldo = 10000
limite_de_saque = 500

while True:
    print(f'''
          {"1 - Visualizar o extrato".center(50)}
          {"2 - Depositar".center(50)}
          {"3 - Sacar".center(50)}
          {"4 - Sair".center(50)}
          ''')
    op = input("Escolha uma opção:\n --->  ".center(50))
    match op:
        case "1":
            print(f"Seu saldo é de R${saldo:.2f}".center(50))
        case "2":
            a = float(meumodulo.Validação_número("Digite o valor que deseja depositar:\n ---> ".center(50)))
            saldo += a
            print(f'{saldo:.2f}'.center(50))
        case "3":
            if numero_de_saques_restantes > 0:
                if saldo >= limite_de_saque:
                    a = float(meumodulo.Validação_número("Digite o valor que deseja sacar:\n ---> ".center(50)))
                    if a <= limite_de_saque:
                        saldo -= a
                        numero_de_saques_restantes -= 1
                        print(f"Você tem restante R${saldo:.2f}".center(50))
                        print(f"Você possui {numero_de_saques_restantes} saques restantes!".center(50))
                    else:
                        saldo -= limite_de_saque
                        numero_de_saques_restantes -= 1
                        print(f"Limite de saque excedido! Sacando apenas o limite de saque de R${limite_de_saque:.2f}".center(50))
                        print(f"Você tem restante R${saldo:.2f}".center(50))
                        print(f"Você possui {numero_de_saques_restantes} saques restantes!".center(50))
                else:
                    print("Saldo insuficiente!".center(50))
            else:
                print("Você não tem saques restantes!".center(50))
        case "4":
            print('Opção 4 selecionada!')
            print("Fim do Programa")
            break
        case _:
            print("Opção inválida!")
