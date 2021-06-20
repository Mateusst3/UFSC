

def concatena(l1, l2):
    LC = []
    for i in l1:
        LC.append(i)
    for j in l2:
        LC.append(j)
    return LC

def main():
    TL1 = int(input("Quantos elementos terá a primeira lista?"))
    TL2 = int(input("Quantos elementos terá a segunda lista?"))
    L1 = []
    for i in range(0, TL1):
        z = input("Adicione um elemento a primeira lista: ")
        L1.append(z)
    print("L1 é: ", L1, "\n")

    L2 = []
    for j in range(0, TL2):
        x = input("Adicione um elemento a segunda lista: ")
        L2.append(x)
    print("L2 é: ", L2, "\n")


    print("L1 é: ", L1)
    print("L2 é: ", L2)
    print("L1 concatenado com L2 é L3 =", concatena(L1,L2))
    print("L2 concatenado com L1 é L3 =", concatena(L2,L1))

main()