from TestaMatrizQ3 import ex1, ex2, exProva

def pmt(m):
    for i in range(len(m[0])):
        lista = []
        C = 0
        for j in m:
            lista.append(j[i])
        for i in lista:
            if i not in [0, 1]:
                return False
            elif i == 1:
                C += 1
        if C != 1:
            return False
    for i in m:
        C = 0
        for j in i:
            if j == 1:
                C += 1
        if C != 1:
            return False
    return True

def escreveMatriz(m):
    linha = len(m)
    coluna = len(m[0])
    for i in range(linha):
        for j in range(coluna):
            print(m[i][j], end=" ")
        print()

def main():
    testaMatriz = [ex1, ex2, exProva]
    for matriz in testaMatriz:
        print('Matriz: \n')
        escreveMatriz(matriz)
        print('\n', pmt(matriz), '\n')

main()