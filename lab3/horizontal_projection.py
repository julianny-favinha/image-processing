from skimage import io
import numpy as np

""" 
Algoritmo de detecção de inclinação baseada em projeção horizontal.

Entrada:
F, imagem de entrada

Saída: 
m, ângulo de inclinação

****************************************
n = número de linhas da imagem(F)

para i = 1 até n faça
	Perfil[i] = soma(F.linhas[i])

# de um angulo até outro ângulo
para m = m1 até m2 faça
	valor[m] = função_objetivo(Perfil)

m = max(valor)

devolva m
****************************************
"""

"""
FUNÇÃO OBJETIVO: soma dos quadrados das diferenças dos valores em células adjacentes do perfil de projeção
"""

"""
Perfil[i] = quantidade de pixels pretos da linha i
"""



def horizontal_projection(img):
	print("horizontal")	
	
	# número de linhas da imagem	
	n = img.shape[0]

	# binarizar imagem (?)

	perfil = np.zeros((img.shape[0],), dtype=int)


	
