import cv2
import numpy
import matplotlib.pyplot as pyplot

min_HSV = numpy.array([0,58,30], dtype= "uint8")
max_HSV =numpy.array([33,255,255], dtype = "uint8")

imagem = cv2.imread('entradaHumano4.jpeg')
imagemHSV = cv2.cvtColor (imagem, cv2.COLOR_BGR2HSV)
peleHoldBinario = cv2.inRange(imagemHSV, min_HSV, max_HSV)
cv2.imshow("saa", peleHoldBinario)

kernel = numpy.ones((3,3), numpy.uint8)
resultado = numpy.zeros_like(peleHoldBinario)
while(cv2.countNonZero(peleHoldBinario)):
    peleHoldBinario = cv2.erode(peleHoldBinario, kernel, iterations = 1)

    imagemAbertura = cv2.morphologyEx(peleHoldBinario, cv2.MORPH_OPEN, kernel)
 
    imagemSubtracao = cv2.subtract(peleHoldBinario, imagemAbertura)

    cv2.bitwise_or(resultado, imagemSubtracao, resultado)


cv2.imshow("erosao", resultado)

cv2.waitKey(0)



