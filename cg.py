import matplotlib.pyplot as plt


def normalize_coordinates(x, y, resolution):
  normalized_x = int(x / resolution[0] * (resolution[0] - 1))
  normalized_y = int(y / resolution[1] * (resolution[1] - 1))
  return normalized_x, normalized_y


def draw_line(x_start, y_start, x_end, y_end, resolution):
  x_start, y_start = normalize_coordinates(x_start, y_start, resolution)
  x_end, y_end = normalize_coordinates(x_end, y_end, resolution)

  delta_x = abs(x_end - x_start)
  delta_y = abs(y_end - y_start)
  steep = delta_y > delta_x

  if steep:
    x_start, y_start = y_start, x_start
    x_end, y_end = y_end, x_end

  if x_start > x_end:
    x_start, x_end = x_end, x_start
    y_start, y_end = y_end, y_start

  delta_x = abs(x_end - x_start)
  delta_y = abs(y_end - y_start)
  error = 0
  delta_error = delta_y / delta_x if delta_x != 0 else 0
  y = y_start

  for x in range(x_start, x_end + 1):
    if steep:
      plt.scatter(y, x, color='black')
    else:
      plt.scatter(x, y, color='black')

    error += delta_error
    if error >= 0.5:
      y += 1 if y_end > y_start else -1
      error -= 1

  plt.show()


# Exemplo de uso para diferentes resoluções
draw_line(10, 10, 90, 90, (100, 100))
draw_line(50, 50, 250, 250, (300, 300))
draw_line(100, 100, 700, 500, (800, 600))
draw_line(100, 100, 1820, 980, (1920, 1080))