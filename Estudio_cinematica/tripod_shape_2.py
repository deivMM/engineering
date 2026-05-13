from shapely.geometry import LineString
import matplotlib.pyplot as plt

# Center line
line = LineString([(0, 0), (42, 0)]) #It is only a 1D object.
# start point → (0,0)
# end point → (20,0)

# Buffer creates smooth geometry
shape = line.buffer(
    21,
    cap_style=1  # round ends
)

# Extract coordinates
x, y = shape.exterior.xy

# Plot
fig, ax = plt.subplots()

ax.fill(x, y, alpha=0.5)
ax.plot(x, y, color='black')

ax.set_aspect('equal')
plt.show()

