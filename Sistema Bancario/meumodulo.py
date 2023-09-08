def Validação_número(texto):
    while True:
        n = input(f"{texto}")
        if n.isdigit() or float(n) > 0:
                return n
        else:
            print("Digite um número valido!")
