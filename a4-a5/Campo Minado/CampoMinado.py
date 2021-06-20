import random

class CampoMinado:
	def __init__(self,lin, col):
		self.lin = lin
		self.col = col
		if lin > 0 and col > 0:
			M = []
			for i in range(lin):
				linha = []
				for j in range(col):
					num = random.randint(-1, 0)
					linha.append(num)
				M.append(linha)
		self.M = M

	def escreve_matriz(object):
		mat = object.M
		m = len(mat)
		n = len(mat[0])
		for i in range (m):
			for j in range (n):
				if (mat[i][j] == -1):
					print(mat[i][j], end= '  ')
				else:
					print(mat[i][j], end= '   ')

			print()

	def escreve_matriz2(mat):
		m = len(mat)
		n = len(mat[0])
		for i in range (m):
			for j in range (n):
				if (mat[i][j] == -1):
					print(mat[i][j], end= '  ')
				else:
					print(mat[i][j], end= '   ')

			print()

	def conta_matriz(object):
		mat = object.M
		num_ele = len(mat)
		c = 0
		bombas = 0
		posLivres = 0
		while(c < num_ele):
			z = mat[c]
			len_z= len(z)
			c2 = 0
			while (c2 < len_z):
				x = z[c2]
				if (x > -1):
					posLivres +=1
				if(x == -1):
					bombas+=1
				c2+=1
			c+=1
		print("são: ",bombas, " bombas")
		print("são: ", posLivres, " posições livres")
		return posLivres

	def conta_matriz2(mat):
		num_ele = len(mat)
		c = 0
		bombas = 0
		posLivres = 0
		while(c < num_ele):
			z = mat[c]
			len_z= len(z)
			c2 = 0
			while (c2 < len_z):
				x = z[c2]
				if (x > -1):
					posLivres +=1
				if(x == -1):
					bombas+=1
				c2+=1
			c+=1
		print("são: ",bombas, " bombas")
		print("são: ", posLivres, " posições livres")
		return posLivres

	def adicionaCol(object):
		mat = object.M
		m = len(mat)
		n = len(mat[0])
		for i in range(m):
			for j in range(n):
				x = mat[i][j]
				if (x > -1 and m - 1 > i > 0):
					if (mat[i + 1][j] == -1 and mat[i - 1][j] == -1):
						mat[i][j] += 2
					elif (mat[i + 1][j] == -1 or mat[i - 1][j] == -1):
						mat[i][j]+= 1
				if(i == 0 and x > -1):
					if (mat[i + 1][j] == -1):
						mat[i][j]+= 1
				elif(i == m-1 and x > -1 and mat[i - 1][j] == -1):
					mat[i][j] += 1

	def contaDiagonal(object):
		mat = object.M
		m = len(mat)
		n = len(mat[0])
		for i in range(m):
			for j in range(n):
				x = mat[i][j]
				if (x > -1 and m - 1 > i > 0 and n - 1 > j > 0):
					if (mat[i + 1][j + 1] == -1 ):
						mat[i][j] += 1
					if (mat[i + 1][j - 1] == -1 ):
						mat[i][j] += 1
					if (mat[i - 1][j + 1] == -1):
						mat[i][j] += 1
					if (mat[i -1][j - 1] == -1):
						mat[i][j] += 1
				if(i == 0 and j == 0):
					if (x > -1):
						if(mat[i + 1][j + 1] == -1):
							mat[i][j] += 1
				if(i == 0 and j == n - 1 ):
					if(x > -1):
						if(mat[i + 1][j - 1] == -1):
							mat[i][j] += 1
				if(i == m - 1 and j == 0):
					if(x > -1):
						if(mat[i - 1][j + 1] == -1):
							mat[i][j] += 1
				if(i == m - 1 and j == n-1):
					if(x > -1):
						if(mat[i - 1][j - 1] == -1):
							mat[i][j] += 1
				if(i == 0 and j != 0 and j != n - 1 and x > -1):
					if(mat[i + 1] [j + 1] == -1):
						mat[i][j] += 1
				if (i == 0 and j != 0 and j != n - 1 and x > -1):
					if (mat[i + 1][j - 1] == -1):
						mat[i][j] += 1
				if (i == m - 1 and j != 0 and j != n - 1 and x > -1):
					if (mat[i - 1][j - 1] == -1):
						mat[i][j] += 1
				if (i == m - 1 and j != 0 and j != n - 1 and x > -1):
					if (mat[i - 1][j + 1] == -1):
						mat[i][j] += 1
				if (j == 0 and i != 0 and i != m - 1 and x > -1):
					if (mat[i - 1][j + 1] == -1):
						mat[i][j] += 1
				if (j == 0 and i != 0 and i != m - 1 and x > -1):
					if (mat[i + 1][j + 1] == -1):
						mat[i][j] += 1
				if (j == n - 1 and i != 0 and i != m - 1 and x > -1):
					if (mat[i - 1][j - 1] == -1):
						mat[i][j] += 1
				if (j == n - 1 and i != 0 and i != m - 1 and x > -1):
					if (mat[i + 1][j - 1] == -1):
						mat[i][j] += 1

	def transformarJogo(object):
		mat = object.M
		m = len(mat)
		n = len(mat[0])
		for i in range(m):
			for j in range(n):
					object.M[i][j] = "-"


	def jogo(object, mat2):
		mat = object.M
		x = int(input("Qual o número da linha? ")) - 1
		y = int(input("Qual o número da coluna? ")) - 1
		m = len(mat)
		n = len(mat[0])
		for i in range(m):
			for j in range(n):
				if (i == x and j == y):
					mat2[i][j] = mat[i][j]
		print("\n")
		CampoMinado.escreve_matriz2(mat2)
		if CampoMinado.verifica(mat2) == False:
			return False
			print("Você perdeu!")
		else:
			return True

	def adicionaLinha(object):
		mat = object.M
		num_ele = len(mat)
		c = 0
		while (c < num_ele):
			z = mat[c]
			len_z = len(z)
			c2 = 0
			while (c2 < len_z):
				x = z[c2]
				if ((len_z - 1)> c2 > 0):
					if (x == 0):
						if (z[c2 + 1] == -1 and z[c2 - 1] == -1):
							mat[c][c2] += 2
						elif (z[c2 + 1 ] == -1 or z[c2 - 1] == -1):
							mat[c][c2] += 1
				if(c2 == 0):
					if(x == 0):
						if (z[c2 + 1] == -1):
							mat[c][c2] +=1
				elif (c2 == len_z - 1 and x > -1 and z[c2 - 1 ] == -1):
					mat[c][c2] += 1
				c2 += 1
			c += 1


	def verifica(mat):
		m = len(mat)
		n = len(mat[0])
		for i in range(m):
			for j in range(n):
				if (mat[i][j] == -1):
					return False

	def verifica2(objeto):
		mat = objeto.M
		m = len(mat)
		n = len(mat[0])
		for i in range(m):
			for j in range(n):
				if (mat[i][j] == -1):
					return False

	def verificaGanho(objeto, mat2):
		mat = objeto.M
		m = len(mat)
		n = len(mat[0])
		x = []
		for i in range(m):
			for j in range(n):
				if (mat[i][j] != "-"):
					x.append(mat[i][j])
		if len(x) == CampoMinado.conta_matriz2(mat2):
			return True