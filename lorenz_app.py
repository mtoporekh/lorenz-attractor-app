import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.image("lorenz.png", use_column_width= True)

def lorenz(x, y, z, s, r, b):
    dx = s * (y - x)
    dy = x * (r - z) - y
    dz = x * y - b * z
    return dx, dy, dz

st.title("Simulación del Atractor de Lorenz")

st.sidebar.header("Parámetros")
sigma = st.sidebar.slider("Sigma (σ)", 0.0, 50.0, 10.0)
rho = st.sidebar.slider("Rho (ρ)", 0.0, 50.0, 28.0)
beta = st.sidebar.slider("Beta (β)", 0.0, 10.0, 8/3)

x, y, z = 0.0, 1.0, 1.05
dt = 0.01
num_steps = 10000

xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)
xs[0], ys[0], zs[0] = x, y, z

for i in range(num_steps):
    dx, dy, dz = lorenz(x, y, z, sigma, rho, beta)
    x += dx * dt
    y += dy * dt
    z += dz * dt
    xs[i + 1] = x
    ys[i + 1] = y
    zs[i + 1] = z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Atractor de Lorenz")

st.pyplot(fig)
