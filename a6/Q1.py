#Aluno: Mateus Silva Teixeira
#Matrícula: 20200631


from abc import ABC, abstractmethod


class InstrumentoMusical(ABC):
    def __init__(self,):
        self.__fabricante = ""
        self.__material = " "
        self.__acorde = True

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante = str):
        self.__fabricante = fabricante

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material = str):
        self.__material = material

    @property
    def acorde(self):
        return self.__acorde

    @acorde.setter
    def acorde(self, acorde = bool):
        self.__acorde = acorde

    @abstractmethod
    def tocar(self, notas = []):
        self.__notas = notas
        pass


class Violao(InstrumentoMusical):
    def __init__(self, quantidade_de_cordas: int, cordas_de_aco: bool):
        super().__init__()
        self.__quantidade_de_cordas = quantidade_de_cordas
        self.__cordas_de_aco = cordas_de_aco

    def tocar(self, notas = []):
        if len(notas) <= 7:
            for i in notas:
                print(i)
            pass
        else:
            print("Não foi possível tocar, número excedente de notas.")

    def afinarCorda(self, x = int):
        print("afinando corda ", x, "do violão ")

class Flauta(InstrumentoMusical):
    def __init__(self, quantidade_de_notas: int):
        super().__init__()
        self.__quantidade_de_notas = quantidade_de_notas

    def tocar(self, notas = []):
        if len(notas) == 1:
            for i in notas:
                print(i)
            pass
        else:
            print("Não foi possível tocar, número excedente de notas.")

    def afinar(self, x = int):
        print("afinando nota ", x)

def main():
    v1 = Violao(5, True)
    v1.tocar([1,2,3,4,5,6,7])
    v1.afinarCorda(2)
    v1.material = "Madeira"
    v1.fabricante = "Flinstons"
    v1.acorde = True

    v2 = Violao(6, False)
    v2.tocar([3, 4, 5, 8, 4, 3, 1])
    v2.afinarCorda(5)
    v2.material = "Aluminio"
    v2.fabricante = "Samsung"
    v2.acorde = False

    f1 = Flauta(5)
    f1.tocar([5])
    f1.afinar(5)
    f1.material = "Plástico"
    f1.fabricante = "LG"
    f1.acorde = True

    f2 = Flauta(3)
    f2.tocar([3])
    f2.afinar(3)
    f2.material = "Plástico"
    f2.fabricante = "LG"
    f2.acorde = True


main()