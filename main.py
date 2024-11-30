import cv2
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