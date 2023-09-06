import cv2
import numpy

imagem = cv2.imread('entrada.jpeg')
cv2.imshow("imagem normal", imagem);

#GAUSSIAN BLUR (blur com peso diferente para pixel distante)
imagemGaussian = cv2.GaussianBlur(imagem, (7,7), 0)
cv2.imshow("gaussian blur", imagemGaussian)

#MEDIAN BLUR (diminuir ruido da imagem)
imagemMedian = cv2.medianBlur(imagem, 3)
cv2.imshow("mediam blur", imagemMedian)

#FILTRAGEM BILATERAL (fazer tipo um median blur mas manter as bordas)
imagemBilateral = cv2.bilateralFilter(imagem, 9, 75, 75)
cv2.imshow("Bilateral blur", imagemBilateral)

#Brilho e Contraste
alpha = 1 #contraste
beta = 50 #brilho
imagemBrilhoContraste = numpy.zeros_like(imagem) #inicializar a nova imagem

for y in range(imagem.shape[0]):
    for x in range(imagem.shape[1]):
        for z in range(imagem.shape[2]):
            imagemBrilhoContraste[y,x,z] = numpy.clip(alpha*imagem[y,x,z] + beta, 0, 255)
cv2.imshow("brilho e contraste", imagemBrilhoContraste)
cv2.waitKey(0)
