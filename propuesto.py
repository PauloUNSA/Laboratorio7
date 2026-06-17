import cv2
import numpy as np
# Crear lienzo blanco
canvas = np.ones((600, 800, 3), dtype=np.uint8) * 255
historial = [canvas.copy()]
modo = "RECTANGULO"
dibujando = False
x0, y0 = -1, -1
# Mostrar menú
def mostrar_menu():

    print("\n" + "="*50)
    print("      PROGRAMA DE DIBUJO")
    print("="*50)

    print("TECLAS DISPONIBLES")
    print()
    print("R -> Dibujar RECTANGULO")
    print("C -> Dibujar CIRCULO")
    print("L -> Dibujar LINEA")
    print("U -> Deshacer ultimo cambio")
    print("S -> Guardar dibujo")
    print("Q -> Salir")
    print("ESC -> Salir")
    print()

    print("Modo actual:", modo)
    print("="*50)

mostrar_menu()

# Evento Mouse
def mouse(event, x, y, flags, param):

    global x0, y0
    global dibujando
    global canvas
    global historial
    global modo

    if event == cv2.EVENT_LBUTTONDOWN:

        dibujando = True
        x0, y0 = x, y

    elif event == cv2.EVENT_LBUTTONUP:

        dibujando = False

        if modo == "RECTANGULO":

            cv2.rectangle(
                canvas,
                (x0, y0),
                (x, y),
                (0, 0, 255),
                2
            )

        elif modo == "CIRCULO":

            radio = int(
                np.sqrt(
                    (x - x0)**2 +
                    (y - y0)**2
                )
            )

            cv2.circle(
                canvas,
                (x0, y0),
                radio,
                (255, 0, 0),
                2
            )

        elif modo == "LINEA":

            cv2.line(
                canvas,
                (x0, y0),
                (x, y),
                (0, 255, 0),
                2
            )

        historial.append(canvas.copy())

# Configurar ventana
cv2.namedWindow("Dibujo")
cv2.setMouseCallback("Dibujo", mouse)

while True:

    # Crear copia temporal
    vista = canvas.copy()

    # Mostrar modo actual dentro de la ventana

    cv2.putText(
        vista,
        f"Modo: {modo}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 0),
        2
    )

    cv2.putText(
        vista,
        "R=Rect C=Circulo L=Linea U=Deshacer S=Guardar Q=Salir",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 0),
        1
    )

    cv2.imshow("Dibujo", vista)

    tecla = cv2.waitKey(1) & 0xFF

    # Rectángulo
    if tecla == ord('r'):

        modo = "RECTANGULO"
        print("Modo cambiado a RECTANGULO")

    # Círculo
    elif tecla == ord('c'):

        modo = "CIRCULO"
        print("Modo cambiado a CIRCULO")

    # Línea
    elif tecla == ord('l'):

        modo = "LINEA"
        print("Modo cambiado a LINEA")

    # Deshacer
    elif tecla == ord('u'):

        if len(historial) > 1:

            historial.pop()
            canvas = historial[-1].copy()

            print("Ultima accion deshecha")

        else:

            print("No hay acciones para deshacer")

    elif tecla == ord('s'):#guardar

        cv2.imwrite(
            "dibujo_final.png",
            canvas
        )

        print("Dibujo guardado como dibujo_final.png")

    elif tecla == ord('q') or tecla == 27:#salir con q o esc

        print("Programa finalizado")
        break

cv2.destroyAllWindows()