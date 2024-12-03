import cv2
import numpy as np
#cargamos imagen
image = cv2.imread('static/brainia.jpg')

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#obtener dimensiones de la imagen
hight, width = image.shape[:2]

center = (width/2, hight/2)

#rotar la imagen
angulo = 45
matrix = cv2.getRotationMatrix2D(center, angulo, 1.0)
rotated = cv2.warpAffine(image, matrix, (width, hight))

cv2.imshow('Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

tx, ty = 100, 50
M = np.float32([[1, 0, tx], [0, 1, ty]])

translated = cv2.warpAffine(image, M, (width, hight))

cv2.imshow('Image', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

#escalar la imagen
scale_percent = 50
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

cv2.imshow('Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Definir las coordenadas de la región de interés
x1, y1, x2, y2 = 100, 100, 400, 400

# Extraer la región de interés
roi = image[y1:y2, x1:x2]

# Mostrar la región de interés
cv2.imshow('Región de interés', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
# suavizar 
# Aplicar un filtro Gaussiano
blur = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imshow('Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

