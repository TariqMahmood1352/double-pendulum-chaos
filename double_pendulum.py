import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# 1. Physics Parameters
G, L1, L2, M1, M2 = 9.81, 1.0, 1.0, 1.0, 1.0

def equations(state, t):
    theta1, z1, theta2, z2 = state
    delta = theta2 - theta1
    den1 = (M1 + M2) * L1 - M2 * L1 * np.cos(delta)**2
    den2 = (L2 / L1) * den1
    d_z1 = (M2 * L1 * z1**2 * np.sin(delta) * np.cos(delta) + M2 * G * np.sin(theta2) * np.cos(delta) + M2 * L2 * z2**2 * np.sin(delta) - (M1 + M2) * G * np.sin(theta1)) / den1
    d_z2 = (-M2 * L2 * z2**2 * np.sin(delta) * np.cos(delta) + (M1 + M2) * G * np.sin(theta1) * np.cos(delta) - (M1 + M2) * L1 * z1**2 * np.sin(delta) - (M1 + M2) * G * np.sin(theta2)) / den2
    return [z1, d_z1, z2, d_z2]

# 2. Solve the Physics
t = np.linspace(0, 20, 500) # 500 points
initial_state = [np.pi/2, 0, np.pi/2, 0]
sol = odeint(equations, initial_state, t)

x1 = L1 * np.sin(sol[:, 0])
y1 = -L1 * np.cos(sol[:, 0])
x2 = x1 + L2 * np.sin(sol[:, 2])
y2 = y1 - L2 * np.cos(sol[:, 2])

# 3. Setup Animation Plot
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

line, = ax.plot([], [], 'o-', lw=2, color='#1f77b4', markersize=8)
trace, = ax.plot([], [], '-', lw=1, color='#d62728', alpha=0.4)

def init():
    line.set_data([], [])
    trace.set_data([], [])
    return line, trace

def animate(i):
    # The 'i' comes from 'frames', we ensure it stays within bounds
    this_x = [0, x1[i], x2[i]]
    this_y = [0, y1[i], y2[i]]
    
    line.set_data(this_x, this_y)
    trace.set_data(x2[max(0, i-50):i], y2[max(0, i-50):i]) # Trail of last 50 points
    return line, trace

# We explicitly set frames to len(t) so it never goes out of bounds
ani = FuncAnimation(fig, animate, frames=len(t), 
                    init_func=init, interval=30, blit=True)

# Close the plot so it doesn't show an empty static image
plt.close()

# 4. Display as HTML5 Video
HTML(ani.to_jshtml())
