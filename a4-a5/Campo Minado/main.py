# Aluno: Mateus Silva Teixeira, Matrícula: 20200361
# Link da a5: https://youtu.be/Hu_3Ay97ioY


from CampoMinado import CampoMinado

c1 = CampoMinado(int(input("Quantas Linhas terá o campo minado? \n")), int(input("Quantas colunas terá o campo minado? \n")))
c2 = CampoMinado(c1.lin, c1.col)
c1.adicionaLinha()
c1.adicionaCol()
c1.contaDiagonal()
c1.escreve_matriz()
c2.transformarJogo()
c2.escreve_matriz()
c1.conta_matriz()

while (c1.jogo(c2.M) == True ):
    if (c2.verificaGanho(c1.M) == True):
        print("Você ganhou!")
        break
    c1.jogo(c2.M)
    if (c2.verificaGanho(c1.M) == True):
        print("Você ganhou!")
        break
    if c2.verifica2() == False:
        print("Você perdeu")
        break

print("\n")
print("fim de jogo, seu campo minado era: ")
print(c1.escreve_matriz())