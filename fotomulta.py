import cv2
import pytesseract
import numpy as np

# Configura la ruta de Tesseract-OCR en tu sistema
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Cambia esta ruta según tu instalación

def detect_yellow_plate(image_path):
    # Leer la imagen
    image = cv2.imread(image_path)
    # Convertir a espacio de color HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Definir el rango del color amarillo en HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # Crear una máscara para el color amarillo
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Encontrar contornos en la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    plate_text = None
    for contour in contours:
        # Aproximar el contorno
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 15:  # Ajustar estos valores según sea necesario
            # Extraer la región de la placa
            plate_region = image[y:y+h, x:x+w]
            # Convertir la región de la placa a escala de grises
            gray_plate = cv2.cvtColor(plate_region, cv2.COLOR_BGR2GRAY)
            # Aplicar OCR en la región de la placa
            plate_text = pytesseract.image_to_string(gray_plate, config='--psm 8')
            print("Texto de la placa:", plate_text.strip())
            # Dibujar el contorno de la placa en la imagen original
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    # Mostrar la imagen con el contorno
    cv2.imshow("Deteccion de Placas", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    if plate_text is not None:
        return plate_text.strip()
    else:
        print("No se detectó ninguna placa de carro.")
        return None

# Ejemplo de uso
texto_placa = detect_yellow_plate('static/fotomulta2.jpg')
print("Texto de la placa extraída:", texto_placa)


