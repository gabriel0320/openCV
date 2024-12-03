import cv2
import numpy as np

#cargamos imagen
image1 = cv2.imread('1.jpg')
cv2.imshow('Image', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#obtener dimensiones de la imagen
hight, width = image1.shape[:2]
center = (width/2, hight/2)

#rotar la imagen
image2 = cv2.imread('2.jpg')
angulo = 45
matrix = cv2.getRotationMatrix2D(center, angulo, 1.0)
rotated = cv2.warpAffine(image2, matrix, (width, hight))
cv2.imshow('Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Definir la matriz de traslacion
tx, ty = 100, 50
M = np.float32([[1, 0, tx], [0, 1, ty]])

# Aplicar la matriz de traslacion a la imagen
image3 = cv2.imread('3.jpg')
translated = cv2.warpAffine(image3, M, (image3.shape  [1], image3.shape[0]))

# Mostrar la imagen trasladada
cv2.imshow('Image', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Escala
# Definir la nueva altura y acho de la imágen
new_height, new_width = 300, 400

# Aplicar la escala de la imágen
image4 = cv2.imread('4.jpg')
scaled = cv2.resize(image4, (new_width, new_height))

# Mostrar la imágen escalada
cv2.imshow('Image', scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Recorte
# Definir las coordenadas de interes ROI
x, y, w, h = 100, 100, 200, 150

# Recortar la region de interes
image5 = cv2.imread('5.jpg')
cropped = image5[y:y+h, x:x+w]

# Mostrar la imágen recortada
cv2.imshow('Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Suavizado (aplicar un filro a la imagen)
# Aplicar el filtro Gauciano para suavizar la imagen (tecnica de procesamiento de imas)
image6 = cv2.imread('6.jpg')
smoothed = cv2.GaussianBlur(image6, (5, 5), 0)

# Mostrar la imágen suavizada
cv2.imshow('Image', smoothed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Realce
# Definir el kernel para el filtro de afilado
image7 = cv2.imread('7.jpg')
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# Aplicar el filtro de afilado para realzar los detalles
sharpened = cv2.filter2D(image7, -1, kernel)
# Mostrar la imágen realzada
cv2.imshow('Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Deteccion de bordes
# Cargar la imagen en escala de grises
image8 = cv2.imread('8.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el operados Sovbl para detectar bordes
sobelx = cv2.Sobel(image8, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image8, cv2.CV_64F, 0, 1, ksize=3)

# Combinar las respuestas en magnitud
edges = cv2.magnitude(sobelx, sobely)

# Normalizar los valores para mostrar la imagen correctamente
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Mostrar la imágen con los bordes detectados
cv2.imshow('Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()