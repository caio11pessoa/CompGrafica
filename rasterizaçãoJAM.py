import matplotlib.pyplot as plt
import numpy as np


def create_image(width, height):
    return np.zeros((height, width), dtype=np.uint8)


def draw_line(image, x0, y0, x1, y1):
    # Garantir que x0 <= x1
    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0

    delta_x = x1 - x0
    delta_y = y1 - y0
    # Lidar com caso de linha vertical
    if delta_x == 0:
        for y in range(y0, y1 + 1):
            image[y, x0] = 255  # 255 representa o branco
        return
    elif delta_x > delta_y:
        m = delta_y / delta_x
        # Desenhar a linha
        for x in range(x0, x1 + 1):
            y = int(y0 + m * (x - x0))
            image[y, x] = 255  # 255 representa o branco
    else:
        m = delta_x / delta_y
        # Desenhar a linha
        for y in range(y0, y1 + 1):
            x = int(x0 + m * (y - y0))
            image[y, x] = 255  # 255 representa o branco

    # Calcular inclinação da reta
    


# Ajuste a resolução alterando a largura e a altura
width, height = 100, 100
image = create_image(width, height)

x0, y0 = 20, 50
x1, y1 = 18, 40

draw_line(image, x0, y0, x1, y1)

# Exibindo a imagem
plt.imshow(image, cmap="gray", origin="lower", extent=[0, width, 0, height])
plt.title("Rasterização de Linha")
plt.show()
