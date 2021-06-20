import random

ex1 = [
    [ 0, -1,  0,  -1,  -1,  0, -1, 0],
    [ 0, 0,  0,  0, -1,  0, 0, 0],
    [ 0,  0,  -1,  -1, 0,  0, -1, 0],
    [-1, 0, 0 ,  0,  0,  -1, 0,  0],
    [ 0,  0,  -1,  0,  0,  0, -1, -1]
]

def matrizAleatoria():
    lin = random.randint(1, 10)
    col = random.randint(1,10)
    M = []
    for i in range (lin):
        linha = []
        for j in range (col):
            num = random.randint(-1,0)
            linha.append(num)
        M.append(linha)
    return M

