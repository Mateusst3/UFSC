from TestaMatrizQ2 import ex1, matrizAleatoria

def contar(m):
    mat = []
    c = 0
    linha = len(m)
    coluna = len(m[0])

    for i in range(linha):
        l1 = []
        for j in range(coluna):
            if m[i][j] == 0:
                v = False
                if i + 1 <= linha - 1:
                    if m[i + 1][j] == 0:
                        if i - 1 > -1:
                            if m[i - 1][j] != 0:
                                c += 1
                                l1.append(c)
                                v = True
                        else:
                            c += 1
                            l1.append(c)
                            v = True
                if not v:
                    if j + 1 <= coluna - 1:
                        if m[i][j + 1] == 0:
                            if j - 1 > -1:
                                if m[i][j - 1] != 0:
                                    c += 1
                                    l1.append(c)
                                else:
                                    l1.append(m[i][j])
                            else:
                                c += 1
                                l1.append(c)
                        else:
                            l1.append(m[i][j])
                    else:
                        l1.append(m[i][j])
            else:
                l1.append(m[i][j])
        mat.append(l1)
    return mat

def escreveMatriz(m):
    col = 4
    coluna = len(m)
    for i in range(coluna):
        print("".join(str(j).rjust(col) for j in m[i]), end=' ')
        print()

def main():
    matrizes = [ex1, matrizAleatoria()]
    for i in range(len(matrizes)):
        print("Matriz {}:\n".format(i))
        escreveMatriz(matrizes[i])

        print("\nComo ficou: \n")
        escreveMatriz(contar(matrizes[i]))
        print("\n")

main()
