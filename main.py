# ATIVIDADE PRÁTICA T1 – M2

# 03)   Faça um programa que crie uma matriz quadrada de ordem 3,
#       que deve ser preenchida com números aleatórios entre 1 e 25.

#       Após o preenchimento da matriz o programa deve exibir:
#           a. A matriz gerada no formato (mxn)
#           b. A soma dos elementos da diagonal principal
#           c. A soma de todos os elementos múltiplos de 5.
#           d. O produto dos elementos da 2ª coluna.

import random

if __name__ == '__main__':
    matriz = []
    soma = 0
    somaMultiplos = 0
    produto = 1
    separacao = '=' * 50

    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(random.randint(1, 25))
        matriz.append(linha)


    for i in range(3):
        soma += matriz[i][i]


    for linha in matriz:
        for elemento in linha:
            if elemento % 5 == 0:
                somaMultiplos += elemento


    for linha in matriz:
        produto *= linha[1]

    print(separacao)
    print(" - A matriz gerada: ")
    for linha in matriz:
        print(f"[ {' ] [ '.join(map(str, linha))} ]")

    print(separacao)
    print(f" - A soma da diagonal principal é: {soma}")
    print(f" - A soma dos múltiplos de 5 é: {somaMultiplos}")
    print(f" - O produto dos elementos da 2° coluna é: {produto}")
    print(separacao)
