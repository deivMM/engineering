import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# %matplotlib qt
# %matplotlib inline


art_angle = 20
PCD_tripode = 53.2

rot_angles = np.linspace(0,360,361)


z2 = PCD_tripode / 4 * np.sin(np.radians(art_angle))*np.cos(np.radians(rot_angles))
HI = (1/4) * PCD_tripode * (1 - np.cos(np.radians(art_angle))) * np.cos(2 * np.radians(rot_angles))



f, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8), facecolor='.85')



ax1.plot(z2, HI)
dot, = ax1.plot([], [], 'ro')  # red dot
ax1.axis('equal')


ax2.plot(rot_angles, z2)
ax2.plot(rot_angles, HI)


vline = ax2.axvline(color='k', lw=2, alpha=.3)

def init():
    dot.set_data([], [])
    vline.set_xdata([])
    return dot, vline,


def update(frame):
    x_val = z2[frame]
    y_val = HI[frame]

    dot.set_data([x_val], [y_val])
    vline.set_xdata([rot_angles[frame], rot_angles[frame]])

    return dot, vline,


ani = FuncAnimation(
    f, update, frames=len(rot_angles),
    init_func=init, blit=True, interval=50, repeat=False
)


plt.show()





