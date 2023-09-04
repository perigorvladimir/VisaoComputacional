import cv2
import numpy

imagem = cv2.imread("entrada.jpeg")

kernel = numpy.array([[0,0,0],
                           [0,1,0],
                           [0,0,0]])

# cv2.imshow("imagem", imagem)
imagemMaior = cv2.resize(imagem, (1366,768))
imagemMaior = cv2.filter2D(kernel = kernel, ddepth=-1, src=imagemMaior)
cv2.imshow("imagemGrande", imagemMaior)
cv2.waitKey(0)