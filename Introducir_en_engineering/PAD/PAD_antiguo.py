import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.transforms import Affine2D
import numpy as np
from matplotlib.patches import Polygon

##### -------------------------------------------------
##### script para desarrollar todo el PAD de la tulipa
##### -------------------------------------------------

%matplotlib qt


L = 25
D = 15
d = 5

translate_l = 0
angle = 0   # grados

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

### --- Geometría fija ---
### rectangle ---> Primer valor es la esquina inferior izquierda, luego ancho y alto
ax1.add_patch(plt.Rectangle((-L*.5, D*0.5), L, 2, color='b'))
ax1.add_patch(plt.Rectangle((-L*.5, -D*0.5), L, -2, color='b'))
## fin de la tulipa
ax1.add_patch(plt.Rectangle((L*.5, -D*0.5-2), 2, D+4, color='b'))

### --- Parte móvil ---
width = L+L*.1
rect_move = plt.Rectangle((-width, -d/2), width, d, color='k')
ax1.add_patch(rect_move)

line, = ax1.plot([0, 0], [D*0.5, -D*0.5], color='r')

extremo_derecho_L = L*.5
angulo_max_derecho = np.arctan(((D/2)-d*0.5)/ extremo_derecho_L*0.5) * 180 / np.pi

print(f"Longitud máxima derecha: {extremo_derecho_L:.2f}")
print(f"Ángulo máximo derecho: {angulo_max_derecho:.2f} grados")

ax1.axis('equal')
ax1.set_xlim(-20, 20)
ax1.set_ylim(-10, 10)
ax1.axis('off')

########################
poly = Polygon([[-12.5, 0], [0, 75], [10, 60], [12.5, 0]], facecolor='0.9', edgecolor='0.5')
ax2.add_patch(poly)
ax2.autoscale_view()

# punto inicial
point, = ax2.plot(5, 5, 'ro', markersize=10)

# configurar ejes centrados en (0,0)
ax2.spines['left'].set_position('zero')
ax2.spines['bottom'].set_position('zero')
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')

ax2.xaxis.set_ticks_position('bottom')
ax2.yaxis.set_ticks_position('left')

ax2.set_xlabel('Plunge (mm)')
ax2.set_ylabel(r'$\theta$ (degrees)', rotation=0)

ax2.xaxis.set_label_coords(1, -0.05)   # derecha
ax2.yaxis.set_label_coords(0.5, 1)  # arriba del centro   

dragging = False

def on_press(event):
    global dragging
    if event.inaxes != ax2:
        return
    
    x, y = point.get_data()
    
    # comprobar si el click está cerca del punto
    if np.hypot(event.xdata - x[0], event.ydata - y[0]) < 0.5:
        dragging = True

def on_release(event):
    global dragging
    dragging = False

def update_motion(x, theta):

    transform = (
        Affine2D()
        .rotate_deg(theta)
        .translate(x, 0)
        + ax1.transData
    )

    rect_move.set_transform(transform)
    line.set_transform(transform)

    fig.canvas.draw_idle()


def on_move(event):
    if not dragging or event.inaxes != ax2:
        return

    x = event.xdata
    y = event.ydata

    # comprobar si está dentro del polígono
    if poly.get_path().contains_point((x, y)):
        point.set_data([x], [y])

        update_motion(x, y)   # ← aquí está la clave

        fig.canvas.draw_idle()

fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()
