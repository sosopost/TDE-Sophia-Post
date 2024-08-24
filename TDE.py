matriz = []

with open('teste.txt', 'r') as arquivo:
    for linha in arquivo:
        x = linha.split()
        matriz.append(x)

def formatar(conjunto):
    return ', '.join(conjunto)

for i in range(len(matriz)):
    if len(matriz[i]) == 1:
        operacao = matriz[i][0]
        if i + 2 < len(matriz):
            conjunto1 = set(matriz[i + 1][0].split(','))
            conjunto2 = set(matriz[i + 2][0].split(','))

            if operacao == 'U':
                resultado = conjunto1 | conjunto2
                print(f"\nOperação: União")
                print(f"\nConjunto 1: {{{formatar(conjunto1)}}}")
                print(f"Conjunto 2: {{{formatar(conjunto2)}}}")
                print(f"\nResultado da operação: \n{{{formatar(resultado)}}}")

            elif operacao == 'I':
                resultado = conjunto1 & conjunto2
                print(f"\nOperação: Intersecção")
                print(f"\nConjunto 1: {{{formatar(conjunto1)}}}")
                print(f"Conjunto 2: {{{formatar(conjunto2)}}}")
                print(f"\nResultado da operação: \n{{{formatar(resultado)}}}")

            elif operacao == 'D':
                resultado = conjunto1 - conjunto2
                print(f"\nOperação: Diferença")
                print(f"\nConjunto 1: {{{formatar(conjunto1)}}}")
                print(f"Conjunto 2: {{{formatar(conjunto2)}}}")
                print(f"\nResultado da operação: \n{{{formatar(resultado)}}}")

            elif operacao == 'C':
                resultado = [(a, b) for a in conjunto1 for b in conjunto2]
                cartesiano = ', '.join([f"({a}, {b})"for a, b in resultado])
                print(f"\nOperação: Produto Cartesiano")
                print(f"\nConjunto 1: {{{formatar(conjunto1)}}}")
                print(f"Conjunto 2: {{{formatar(conjunto2)}}}")
                print(f"\nResultado da operação: \n{cartesiano}")
