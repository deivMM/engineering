from shapely.geometry import box, Point
from shapely.ops import unary_union
import matplotlib.pyplot as plt

from shapely.affinity import scale


# %matplotlib  qt
# %matplotlib  inline


##############################################################################
### Parámetros tripode
### cuerpo
altura_cuerpo = 16.35
espesor_cuerpo = 22.3

PCD_medios = 26.6
espesor_cuello = 22.3

### cuello
PCD = 26.6
espesor_cuello = 20.2

### trunion
altura_trunion = 9.22
radio_trunion = 13

### **************************************
### Parámetros tulipa

plunge = 78.34
espesor_tulipa = 4
altura_hombro = 35.5

### **************************************
### Parámetros eje
diametro = 28.1
diametro_reces = 26.6
longitud_total = 140

longitud_reces = 10
distancia_reces_final = 43.6
L2 = 13.1

### **************************************
### Parámetros roller
diametro_exterior = 44
espesor_roller = 16.3
diametro_interior = 33.878
radio_exterior = 16

diametro_ext_inner = 29.861
diametro_int_inner = 22.9
espesor_inner = 10

##############################################################################
### **************************************
### Modelo_tripode
### cuerpo
cuerpo = box(-espesor_cuerpo / 2, 0,                # bottom left cornet
             espesor_cuerpo / 2,altura_cuerpo)      # upper rigth cornet

### cuello
cuello = box(-espesor_cuello / 2, 0,                # bottom left cornet
             espesor_cuello / 2,PCD)      # upper rigth cornet

### trunion
centro_trunion = (0, PCD)
circulo_trunion = Point(centro_trunion).buffer(radio_trunion)


recorte_sup_circ = box(-radio_trunion*1.5, PCD+altura_trunion*0.5, radio_trunion*1.5, PCD+altura_trunion*1.5)  # mitad izquierda
recorte_inf_circ = box(-radio_trunion*1.5, PCD-altura_trunion*0.5, radio_trunion*1.5, PCD-altura_trunion*1.5)  # mitad izquierda

recortes = unary_union([recorte_sup_circ, recorte_inf_circ])
trunion = circulo_trunion.difference(recortes)

### union

radio_fillet = 1.5  # el radio de redondeo que quieras

tripod = (
    unary_union([
        cuerpo.buffer(radio_fillet),
        cuello.buffer(radio_fillet),
        trunion.buffer(radio_fillet)
    ])
).buffer(-radio_fillet)


# tripod_mirror = scale(tripod, xfact=1, yfact=-1, origin=(0, 0))
# tripod = unary_union([tripod, tripod_mirror])

### **************************************
### Modelo_tulipa

superior_tulipa = box(-plunge*0.5, altura_hombro-espesor_tulipa*0.5, plunge*0.5, altura_hombro+espesor_tulipa*0.5)  # mitad izquierda
vertical_tulipa = box(plunge*0.5-espesor_tulipa*0.5, -altura_hombro-espesor_tulipa*0.5, plunge*0.5+espesor_tulipa*0.5, altura_hombro+espesor_tulipa*0.5)
inferior_tulipa = box(-plunge*0.5, -altura_hombro-espesor_tulipa*0.5, plunge*0.5, -altura_hombro+espesor_tulipa*0.5)  # mitad izquierda


tulipa = unary_union([superior_tulipa, inferior_tulipa, vertical_tulipa])
### **************************************
### Modelo_eje

distancia_centrojunta_reces = (distancia_reces_final+longitud_reces)-L2

eje_izq = box(-longitud_total, -diametro*0.5, -distancia_centrojunta_reces, diametro*0.5)
eje_der = box(-distancia_reces_final+L2, -diametro*0.5, L2, diametro*0.5)
eje_reces = box(-(distancia_reces_final+longitud_reces)+L2-2, -diametro_reces*0.5, -distancia_reces_final+L2+2, diametro_reces*0.5)

radio_fillet = 2  # el radio de redondeo que quieras

eje = (
    unary_union([
        eje_izq.buffer(radio_fillet),
        eje_der.buffer(radio_fillet),
        eje_reces.buffer(radio_fillet)
    ])
).buffer(-radio_fillet)

### **************************************
### Modelo_roller

centro_circulo_izq = (-diametro_exterior*0.5+radio_exterior, PCD)
circulo_izq = Point(centro_circulo_izq).buffer(radio_exterior)


centro_circulo_der = (diametro_exterior*0.5-radio_exterior, PCD)
circulo_der = Point(centro_circulo_der).buffer(radio_exterior)


union_circulos = unary_union([circulo_izq, circulo_der])


recorte_sup_circ = box(-diametro_exterior*1.5, PCD+espesor_roller*0.5, diametro_exterior*1.5, PCD+espesor_roller*1.5)  # mitad izquierda
recorte_inf_circ = box(-diametro_exterior*1.5, PCD-espesor_roller*0.5, diametro_exterior*1.5, PCD-espesor_roller*1.5)  # mitad izquierda

recortes = unary_union([recorte_sup_circ, recorte_inf_circ])

roller = union_circulos.difference(recortes)


inner_izq = box(-diametro_ext_inner*0.5, PCD-espesor_inner*0.5, -diametro_int_inner*0.5, PCD+espesor_inner*0.5) 
inner_der = box(diametro_ext_inner*0.5, PCD-espesor_inner*0.5, diametro_int_inner*0.5, PCD+espesor_inner*0.5)  

unary_union([inner_izq, inner_der])
### **************************************

x_tulipa, y_tulipa = tulipa.exterior.xy


x_tripod, y_tripod = tripod.exterior.xy

x_eje, y_eje = eje.exterior.xy

x_roller, y_roller = roller.exterior.xy

x_inner_izq, y_inner_izq = inner_izq.exterior.xy
x_inner_der, y_inner_der = inner_der.exterior.xy


##############################################################################

f, ax = plt.subplots(figsize=(12,12))

ax.fill(x_roller, y_roller, color='blue')
ax.fill(x_inner_izq, y_inner_izq, color='green')
ax.fill(x_inner_der, y_inner_der, color='green')

ax.fill(x_tulipa, y_tulipa, color='grey')
ax.fill(x_eje, y_eje, color='lightgrey')
ax.fill(x_tripod, y_tripod, color='darkgrey')

ax.set_aspect('equal', adjustable='box')

ax.set_xlim(-80, 50)
ax.set_ylim(-80, 80)

plt.show()

