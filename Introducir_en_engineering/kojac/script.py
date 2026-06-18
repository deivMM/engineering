import re
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons


%matplotlib qt
# %matplotlib inline

def get_tab_df(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    init_line = False
    
    data = []
    
    for line in lines:
        # if line.startswith('Angle_Rot_Tulip'):
        if line.startswith('Angle_Rot_Spider'):
            columns_names = line.strip().split()
            init_line = True
            
        if init_line:
            try:
                parts = line.strip().split()
                row = [float(p) for p in parts]
                data.append(row)
            
            except ValueError:
                        continue
        
    
    data_filled = [ row + [np.nan] * (len(columns_names) - len(row)) for row in data]
                               
    return pd.DataFrame(data_filled, columns=columns_names)

TU_tab_files = [f for f in os.listdir('Output_AAR3_46_Calc1_Output') if f.endswith('Tu.tab')]
TU_tab_files_dict = {}

for TU_tab_f in TU_tab_files:
    search = re.search('a(\d+)d', TU_tab_f)
    if search:
        angle = int(search.group(1)) // 10
    
        TU_tab_files_dict[angle] = get_tab_df( f'Output_AAR3_46_Calc1_Output/{TU_tab_f}')
    else:
        print('na')

df = TU_tab_files_dict[2]

current_df = df

#######################################################
#######################################################

# Crear orden
df["order"] = df.groupby("Angle_Rot_Spider.Last_Rot").cumcount()

df["Force_xy"] = np.sqrt(df["Normal_Force_x"]**2+df["Normal_Force_y"]**2)
df["Force_yz"] = np.sqrt(df["Normal_Force_y"]**2+df["Normal_Force_z"]**2)


CF_max = round(1.05*df[["Force_xy", "Force_yz"]].max().max(), -2)
CF_min = round(-1.05*df[["Force_xy", "Force_yz"]].min().min(), -2)


# Figura 2x2
fig, axs = plt.subplots(2, 2, figsize=(16, 10), facecolor='.85')
plt.subplots_adjust(bottom=0.2)

ax1, ax2 = axs[0]
ax3, ax4 = axs[1]

# ===================== LINEAS BASE =====================
for order, group in df.groupby("order"):
    ax1.plot(group["CPoint_x"], group["CPoint_y"], alpha=0.5)
    ax2.plot(group["CPoint_z"], group["CPoint_y"], alpha=0.5)

# ===================== GRAFICAS FUERZA =====================
# Ejemplo: magnitud fuerza o componente Y (puedes cambiarlo)
for order, group in df.groupby("order"):
    ax3.plot(group["Angle_Rot_Spider.Last_Rot"], group["Force_xy"], label=f"order {order}")
    ax4.plot(group["Angle_Rot_Spider.Last_Rot"], group["Force_yz"], label=f"order {order}")

ax3.set_title("Fuerza vs Ángulo (X-Y)")
ax4.set_title("Fuerza vs Ángulo (Y-Z)")

# ===================== CONFIG EJES =====================
ax1.set_xlim([0, 50])
ax1.set_ylim([0, 50])
ax1.set_title("Plano X-Y")

ax2.set_xlim([15, 40])
ax2.set_ylim([0, 50])
ax2.set_title("Plano Y-Z")


ax3.axhline(0, color='k', alpha=.2)
ax4.axhline(0, color='k', alpha=.2)


ax3.set_ylim([CF_min,CF_max])
ax3.set_xlim([0, 360])
ax4.set_ylim([CF_min,CF_max])
ax4.set_xlim([0, 360])



rax = plt.axes([.95, 0.4, 0.1, 0.3])  # posición en la figura

angles_available = sorted(TU_tab_files_dict.keys())
radio = RadioButtons(rax, [str(a) for a in angles_available])



# ===================== INICIAL =====================
angulo_init = 0
df_angle = df[df["Angle_Rot_Spider.Last_Rot"] == angulo_init]

# Scatter dinámico
sc1 = ax1.scatter(df_angle["CPoint_x"], df_angle["CPoint_y"], color="red")
sc2 = ax2.scatter(df_angle["CPoint_z"], df_angle["CPoint_y"], color="red")

# Línea vertical en gráficos de fuerza
vline3 = ax3.axvline(angulo_init, color='red')
vline4 = ax4.axvline(angulo_init, color='red')

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']


def change_tab(label):
    global current_df, arrows1, arrows2

    angle_key = int(label)
    current_df = TU_tab_files_dict[angle_key]
    

    # recalcular orden y fuerzas
    current_df["order"] = current_df.groupby("Angle_Rot_Spider.Last_Rot").cumcount()
    current_df["Force_xy"] = np.sqrt(current_df["Normal_Force_x"]**2 + current_df["Normal_Force_y"]**2)
    current_df["Force_yz"] = np.sqrt(current_df["Normal_Force_y"]**2 + current_df["Normal_Force_z"]**2)

    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()

    # volver a dibujar todo
    for order, group in current_df.groupby("order"):
        ax1.plot(group["CPoint_x"], group["CPoint_y"], alpha=0.5)
        ax2.plot(group["CPoint_z"], group["CPoint_y"], alpha=0.5)
        ax3.plot(group["Angle_Rot_Spider.Last_Rot"], group["Force_xy"])
        ax4.plot(group["Angle_Rot_Spider.Last_Rot"], group["Force_yz"])

    update(slider.val)  # refresca con el ángulo actual
    # fig.canvas.draw_idle()
    print(angle_key)

radio.on_clicked(change_tab)


def draw_arrows(df_angle, L=10):
    global q1, q2
    
    # borrar anterior si existe
    if 'q1' in globals() and q1:
        q1.remove()
    if 'q2' in globals() and q2:
        q2.remove()
    
    X1 = df_angle["CPoint_x"].values
    Y1 = df_angle["CPoint_y"].values
    
    X2 = df_angle["CPoint_z"].values
    Y2 = df_angle["CPoint_y"].values
    
    U1, V1 = [], []
    U2, V2 = [], []
    
    for _, row in df_angle.iterrows():
        vec_xy = np.array([row["Normal_Force_x"], row["Normal_Force_y"]])
        vec_yz = np.array([row["Normal_Force_z"], row["Normal_Force_y"]])
        
        norm_xy = np.linalg.norm(vec_xy)
        norm_yz = np.linalg.norm(vec_yz)
        
        dir_xy = vec_xy / norm_xy if norm_xy != 0 else vec_xy
        dir_yz = vec_yz / norm_yz if norm_yz != 0 else vec_yz
        
        U1.append(-dir_xy[0] * L)
        V1.append(-dir_xy[1] * L)
        
        U2.append(-dir_yz[0] * L)
        V2.append(-dir_yz[1] * L)
    
    q1 = ax1.quiver(X1, Y1, U1, V1)
    q2 = ax2.quiver(X2, Y2, U2, V2)


q1, q2 = None, None
draw_arrows(df_angle)


# ===================== SLIDER =====================
ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
slider = Slider(ax_slider, "Angle", 0, 360, valinit=angulo_init, valstep=1)

# ===================== UPDATE =====================

def update(val):
    global q1, q2
    
    angle = int(slider.val)
    df_angle = current_df[current_df["Angle_Rot_Spider.Last_Rot"] == angle]

    # Scatter
    sc1.set_offsets(df_angle[["CPoint_x", "CPoint_y"]].values)
    sc2.set_offsets(df_angle[["CPoint_z", "CPoint_y"]].values)
    
    # Flechas con quiver
    draw_arrows(df_angle)
    
    # Línea vertical
    vline3.set_xdata([angle])
    vline4.set_xdata([angle])
    
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()

