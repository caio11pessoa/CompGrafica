import matplotlib.pyplot as plt
import numpy as np

def draw_polygon(image, vertices):
  # Implementação simples de rasterização de polígonos
  num_vertices = len(vertices)

  for i in range(num_vertices):
      x0, y0 = vertices[i]
      x1, y1 = vertices[(i + 1) % num_vertices]  # Aresta do vértice atual para o próximo

      draw_line(image, x0, y0, x1, y1)

def create_image(width, height):
    return np.zeros((height, width), dtype=np.uint8)

def draw_line(image, x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steep = dy > dx

    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    error = 0
    delta_error = dy / dx if dx != 0 else 0
    y = y0
    y_step = 1 if y0 < y1 else -1

    for x in range(x0, x1 + 1):
        if steep:
            image[x, y] = 255  # 255 representa o branco
        else:
            image[y, x] = 255

        error += delta_error
        while error >= 0.5:
            y += y_step
            error -= 1

# Exemplo de uso
resolucaoX = 16
resolucaoY = 8

#width, height = 100*resolucaoX, 100*resolucaoY
#image = create_image(width, height)

# Resoluções para testar
resolutions = [(100, 100 ), (300, 300)]

# Rasterizar triângulos, quadrados e hexágonos para cada resolução
for resolucaoX, resolucaoY in resolutions:
    width, height = resolucaoX, resolucaoY
    image = create_image(width, height)
    # Triângulo equilátero
    triangle_vertices = [
      (3*int((resolucaoX/10)), 8*int((resolucaoY/10))),
      (5*int((resolucaoX/10)), 2*int((resolucaoY/10))),
      (7*int((resolucaoX/10)), 8*int((resolucaoY/10)))
    ]
    draw_polygon(image, triangle_vertices)

    # Quadrado
    square_vertices = [(10, 10), (10, 30), (30, 30), (30, 10)]
    draw_polygon(image, square_vertices)

    # Hexágono
    hexagon_vertices = [(80, 70), (90, 50), (80, 30), (70, 30), (60, 50), (70, 70)]
    draw_polygon(image, hexagon_vertices)

    # Exibindo a imagem
    plt.imshow(image, cmap='gray', origin='lower', extent=[0, width, 0, height])
    plt.title(f'Rasterização de Polígonos - Resolução ')
    plt.show()

    # Limpar a imagem para o próximo teste
    image.fill(0)
