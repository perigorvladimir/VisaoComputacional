import cv2
import numpy
import matplotlib.pyplot as pyplot

min_HSV = numpy.array([0,58,30], dtype= "uint8")
max_HSV =numpy.array([33,255,255], dtype = "uint8")

imagem = cv2.imread('gatoPreto.jpeg')
imagemHSV = cv2.cvtColor (imagem, cv2.COLOR_BGR2HSV)
peleHSV = cv2.inRange(imagemHSV, min_HSV, max_HSV)

mesclagemHSV = cv2.bitwise_and(imagem, imagem, mask = peleHSV)
 
cv2.imshow("imagem normal", imagem)
cv2.imshow("imagem HSV", imagemHSV)
cv2.imshow("pele hsv", peleHSV)
cv2.imshow("resultado da opera", mesclagemHSV)
cv2.waitKey(0)

