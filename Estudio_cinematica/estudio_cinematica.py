import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


art_angle = 20
PCD_tripode = 53.2

rot_angles = np.linspace(0,360,361)


z2 = PCD_tripode / 4 * np.sin(np.radians(art_angle))*np.cos(np.radians(rot_angles))
HI = (1/4) * PCD_tripode * (1 - np.cos(np.radians(art_angle))) * np.cos(2 * np.radians(rot_angles))


f, ax = plt.subplots()

ax.plot(rot_angles, z2)
ax.plot(rot_angles, HI)


plt.show()









