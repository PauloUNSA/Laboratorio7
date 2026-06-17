# 1. Carga tres imágenes.
# 2. Redimensiona las imágenes al tamaño de la más grande.
# 3. Combina canales de color de las tres imágenes.
# 4. Genera el negativo de la imagen combinada.
# 5. Convierte la imagen negativa a escala de grises.
# 6. Guarda todos los resultados obtenidos.

# IMPORTAR LIBRERÍAS

import cv2
import numpy as np

# ABRIR IMÁGENES

# Cargar las tres imágenes desde el disco
img1 = cv2.imread("imagen1.jpg")
img2 = cv2.imread("imagen2.jpg")
img3 = cv2.imread("imagen3.jpg")

# Verificar que las imágenes fueron cargadas correctamente
if img1 is None or img2 is None or img3 is None:
    print("Error: No se pudieron cargar una o más imágenes.")
    exit()

print("Imágenes cargadas correctamente.")

# OBTENER DIMENSIONES DE LAS IMÁGENES

# shape devuelve (alto, ancho, canales)
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]
h3, w3 = img3.shape[:2]

print("\nDimensiones originales:")
print(f"Imagen 1: {w1} x {h1}")
print(f"Imagen 2: {w2} x {h2}")
print(f"Imagen 3: {w3} x {h3}")

# BUSCAR LA IMAGEN MÁS GRANDE

alto_max = max(h1, h2, h3)
ancho_max = max(w1, w2, w3)

print(f"\nNuevo tamaño para todas las imágenes:")
print(f"Ancho: {ancho_max}")
print(f"Alto : {alto_max}")

# REDIMENSIONAR IMÁGENES

img1_resize = cv2.resize(img1, (ancho_max, alto_max))
img2_resize = cv2.resize(img2, (ancho_max, alto_max))
img3_resize = cv2.resize(img3, (ancho_max, alto_max))

# GUARDAR IMÁGENES REDIMENSIONADAS

cv2.imwrite("img1_redimensionada.jpg", img1_resize)
cv2.imwrite("img2_redimensionada.jpg", img2_resize)
cv2.imwrite("img3_redimensionada.jpg", img3_resize)

print("\nImágenes redimensionadas guardadas.")

# CREAR NUEVA IMAGEN CON CANALES COMBINADOS

# OpenCV utiliza el formato BGR:
# B = Azul
# G = Verde
# R = Rojo

# Separar los canales de cada imagen
b1, g1, r1 = cv2.split(img1_resize)
b2, g2, r2 = cv2.split(img2_resize)
b3, g3, r3 = cv2.split(img3_resize)

# Crear nueva imagen usando:
# Canal Azul  -> Imagen 3
# Canal Verde -> Imagen 2
# Canal Rojo  -> Imagen 1

imagen_combinada = cv2.merge([b3, g2, r1])

# Guardar resultado
cv2.imwrite("imagen_combinada.jpg", imagen_combinada)

print("Imagen con canales combinados guardada.")

# CONVERSIÓN A NEGATIVO

# El negativo se obtiene restando cada píxel a 255
negativo = 255 - imagen_combinada

# Guardar resultado
cv2.imwrite("imagen_negativa.jpg", negativo)

print("Imagen negativa guardada.")

# CONVERSIÓN A ESCALA DE GRISES

gris = cv2.cvtColor(
    negativo,
    cv2.COLOR_BGR2GRAY
)

# Guardar resultado
cv2.imwrite("imagen_gris.jpg", gris)

print("Imagen en escala de grises guardada.")

# MOSTRAR RESULTADOS

cv2.imshow("Imagen 1 Redimensionada", img1_resize)
cv2.imshow("Imagen 2 Redimensionada", img2_resize)
cv2.imshow("Imagen 3 Redimensionada", img3_resize)

cv2.imshow("Imagen Combinada", imagen_combinada)
cv2.imshow("Imagen Negativa", negativo)
cv2.imshow("Imagen Escala de Grises", gris)

print("\nPresione cualquier tecla para cerrar las ventanas.")

cv2.waitKey(0)
cv2.destroyAllWindows()
