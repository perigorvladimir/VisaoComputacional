# Importação das bibliotecas
import cv2
import numpy
# Leitura da imagem com a função imread()
imagem = cv2.imread('entrada.jpg')
kernel = numpy.ones((5,5))
kernelIgual = numpy.array([[1,1,1],
                           [1,1,1],
                           [1,1,1]])/3
print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])

imagem2 = cv2.filter2D(imagem, -1, kernelIgual)
imagem3 = cv2.resize(imagem2, 2)
imagem3 = cv2.filter2D(imagem3, -1 ,kernelIgual)
cv2.imshow("fiiixa", imagem2)
cv2.waitKey(0)
cv2.imshow("fiiixa", imagem3)
cv2.waitKey(0)

cv2.imwrite("saida.jpg", imagem)
cv2.filter2D()