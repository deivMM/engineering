from shapely.geometry import box, Point
from shapely.ops import unary_union
import matplotlib.pyplot as plt

# Parámetros
ancho_centro = 35
alto_centro = 55

ancho_extremo = 42
alto_extremo = 30

radio = alto_extremo / 2

# -------------------------
# Parte central
# -------------------------

cuerpo = box(
    -ancho_centro / 2,
    -alto_centro / 2,
    ancho_centro / 2,
    alto_centro / 2
)

# -------------------------
# TOP
# -------------------------

# Centro vertical del top
y_top = alto_centro / 2

# Rectángulo central del top
top_rect = box(
    -ancho_extremo / 2,
    y_top - alto_extremo / 2,
    ancho_extremo / 2,
    y_top + alto_extremo / 2
)

# Círculo izquierdo
left_circle = Point(
    -ancho_extremo / 2,
    y_top
).buffer(radio)

# Círculo derecho
right_circle = Point(
    ancho_extremo / 2,
    y_top
).buffer(radio)

# Unión top
top = unary_union([
    top_rect,
    left_circle,
    right_circle
])

# -------------------------
# BOTTOM
# -------------------------

y_bottom = -alto_centro / 2

bottom_rect = box(
    -ancho_extremo / 2,
    y_bottom - alto_extremo / 2,
    ancho_extremo / 2,
    y_bottom + alto_extremo / 2
)

left_circle_b = Point(
    -ancho_extremo / 2,
    y_bottom
).buffer(radio)

right_circle_b = Point(
    ancho_extremo / 2,
    y_bottom
).buffer(radio)

bottom = unary_union([
    bottom_rect,
    left_circle_b,
    right_circle_b
])

# -------------------------
# Unión final
# -------------------------

pieza = unary_union([cuerpo, top, bottom])

# Redondeo suave entre piezas
pieza = pieza.buffer(2).buffer(-10)

# -------------------------
# Dibujar
# -------------------------

x, y = pieza.exterior.xy

plt.figure(figsize=(5, 8))
plt.fill(x, y)
plt.axis("equal")
plt.show()