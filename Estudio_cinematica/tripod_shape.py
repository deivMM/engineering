import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 10
H = 4
R = 3

# Arc angle
theta = np.linspace(-60*np.pi/180, 60*np.pi/180, 100)

# Right arc
xc_r = L - R
yc_r = H/2

xr = xc_r + R*np.cos(theta)
yr = yc_r + R*np.sin(theta)

# Left arc
xc_l = R
yc_l = H/2

xl = xc_l - R*np.cos(theta)
yl = yc_l + R*np.sin(theta)

# Build contour
x = np.concatenate([
    [xl[0], xr[0]],
    xr,
    [xr[-1], xl[-1]],
    xl[::-1]
])

y = np.concatenate([
    [yl[0], yr[0]],
    yr,
    [yr[-1], yl[-1]],
    yl[::-1]
])

plt.figure(figsize=(8,4))
plt.fill(x, y, alpha=0.5)
plt.plot(x, y, 'k')

plt.axis('equal')
plt.show()