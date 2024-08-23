matriz = []

with open('teste.txt', 'r') as arquivo:
    for linha in arquivo:
        x = linha.split()
        matriz.append(x)

for i in range(len(matriz)):
    for operacao in matriz[i]:
        if len(matriz[i]) == 1:
            if operacao == 'U':
                print("\nOperação:", operacao)
                print()
                if i + 2 < len(matriz):
                    print(f"União: Conjunto 1 {set(matriz[i + 1])} Conjunto 2 {set(matriz[i + 2])}. \nResultado da operação: {set(matriz[i + 1]) | set(matriz[i + 2])}")
                    print()
            elif operacao == 'I':
                print("\nOperação:", operacao)
                print()
                if i + 2 < len(matriz):
                    print(f"Intersecção: Conjunto 1 {set(matriz[i + 1])}, Conjunto 2 {set(matriz[i + 2])}. \nResultado da operação: {set(matriz[i + 1]) & set(matriz[i + 2])}")
                    print()
            elif operacao == 'D':
                print("\nOperação:", operacao)
                print()
                if i + 2 < len(matriz):
                    print(f"Diferença: Conjunto 1 {set(matriz[i + 1])}, Conjunto 2 {set(matriz[i + 2])}. \nResultado da operação: {set(matriz[i + 1]) - set(matriz[i + 2])}")
                    print()
            elif operacao == 'C':
                print("\nOperação:", operacao)
                print()
                if i + 2 < len(matriz):
                    cartesiano = [(a, b) for a in set(matriz[i + 1]) for b in set(matriz[i + 2])]
                    print(f"Produto Cartesiano: Conjunto 1 {set(matriz[i + 1])}, Conjunto 2 {set(matriz[i + 2])}. \nResultado da operacão: {cartesiano}")
