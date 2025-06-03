import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.image("lorenz.png", use_container_width=True)

st.markdown("""
# Bienvenido al Simulador del Atractor de Lorenz

Esta aplicación interactiva permite visualizar el famoso **atractor de Lorenz** y explorar cómo sus parámetros pueden interpretarse en el contexto del **desempeño de equipos**.

### 🎯 ¿Qué puedes hacer con esta app?

- Ajustar los parámetros del sistema de Lorenz:
  - **Sigma (σ)**: Positividad emocional del equipo.
  - **Rho (ρ)**: Nivel de conectividad y colaboración.
  - **Beta (β)**: Presencia de emociones negativas o pérdida de energía.
- Observar cómo estos valores afectan la dinámica del equipo:
  - Bajo desempeño (atractor de punto)
  - Desempeño medio (ciclo límite)
  - Alto desempeño (atractor caótico)

### 🧠 Inspirado en:
- El modelo de Edward Lorenz (1963)
- Aplicaciones organizacionales de Marcial Losada y Emily Heaphy sobre dinámica de equipos y meta-aprendizaje.

### 🧠 Interpretación de los parámetros:
###         Sigma - Positividad
   Representa la rapidez con la que un equipo responde emocionalmente a las interacciones.
   - Valores bajos (2 - 5): Respuesta lenta o poca energía.
   - Valores medios (8 - 12): Respuesta emocional saludable.
   - Valores altos (15 - 30): Muy entusiasta, pero puede ser inestable.

###         Rho - Conectividad
   Representa el nivel de apertura y complejidad de las interacciones dentro del equipo.
   - Valores bajos (5 - 15): Equipo cerrado, poca colaboración.
   - Valores medios (20 - 30): Buena conectividad, comunicación fluida.
   - Valores altos (35 - 50): Muy abiertos y creativos, pero pueden volverse caóticos.

###         Beta - Negatividad
   Representa la tasa de pérdida de energía o motivación en el sistema.
   - Valores bajos (1 - 2): Retiene energía, pero puede acumular tensión.
   - Valores medios (2.5 - 3.5): Equilibrio entre crítica constructiva y motivación.
   - Valores altos (4 - 6): Pierde energía rápidamente, puede llevar a bajo desempeño.
""")

def lorenz(x, y, z, s, r, b):
    dx = s * (y - x)
    dy = x * (r - z) - y
    dz = x * y - b * z
    return dx, dy, dz

st.title("Simulación del Atractor de Lorenz")

st.sidebar.header("Parámetros")
sigma = st.sidebar.slider("Sigma (σ)", 0.0, 30.0, 10.0)
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

st.markdown("""
---
*Desarrollado con el apoyo de Microsoft Copilot, una IA basada en GPT-4.*
""")
