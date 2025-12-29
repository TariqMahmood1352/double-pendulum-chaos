import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation, FFMpegWriter

# 1. PHYSICAL CONSTANTS
G = 9.81    # Gravity (m/s^2)
L1 = 1.0    # Length of first rod (m)
L2 = 1.0    # Length of second rod (m)
M1 = 1.0    # Mass of first bob (kg)
M2 = 1.0    # Mass of second bob (kg)

# 2. EQUATIONS OF MOTION (Differential Equations)
def derivatives(state, t):
    theta1, z1, theta2, z2 = state
    
    delta = theta2 - theta1
    
    # Denominator terms for the Lagrangian mechanics formula
    den1 = (M1 + M2) * L1 - M2 * L1 * np.cos(delta)**2
    den2 = (L2 / L1) * den1
    
    # Angular accelerations
    d_z1 = (M2 * L1 * z1**2 * np.sin(delta) * np.cos(delta) +
            M2 * G * np.sin(theta2) * np.cos(delta) +
            M2 * L2 * z2**2 * np.sin(delta) -
            (M1 + M2) * G * np.sin(theta1)) / den1

    d_z2 = (-M2 * L2 * z2**2 * np.sin(delta) * np.cos(delta) +
            (M1 + M2) * G * np.sin(theta1) * np.cos(delta) -
            (M1 + M2) * L1 * z1**2 * np.sin(delta) -
            (M1 + M2) * G * np.sin(theta2)) / den2
            
    return [z1, d_z1, z2, d_z2]

# 3. SETUP INITIAL CONDITIONS AND SOLVE
# Initial state: [angle1, angular_velocity1, angle2, angular_velocity2]
# We start at 90 degrees (pi/2) for both
initial_state = [np.pi/2, 0, np.pi/2, 0]
t = np.linspace(0, 20, 600)  # 20 seconds, 600 frames (30fps)

# Integrate the equations
solution = odeint(derivatives, initial_state, t)

# Convert Polar (angles) to Cartesian (x, y) for plotting
x1 = L1 * np.sin(solution[:, 0])
y1 = -L1 * np.cos(solution[:, 0])
x2 = x1 + L2 * np.sin(solution[:, 2])
y2 = y1 - L2 * np.cos(solution[:, 2])

# 4. ANIMATION SETUP
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)
plt.title("Scientific Phenomenon: Double Pendulum (Chaos Theory)")

line, = ax.plot([], [], 'o-', lw=2, color='#1f77b4', markersize=10) # The rods/bobs
trace, = ax.plot([], [], '-', lw=1, color='#d62728', alpha=0.6)     # The path trail

def init():
    line.set_data([], [])
    trace.set_data([], [])
    return line, trace

def animate(i):
    # Update main pendulum
    this_x = [0, x1[i], x2[i]]
    this_y = [0, y1[i], y2[i]]
    line.set_data(this_x, this_y)
    
    # Update trail (showing the last 60 points for a "tail" effect)
    start_trail = max(0, i - 60)
    trace.set_data(x2[start_trail:i], y2[start_trail:i])
    
    return line, trace

# Create animation object
# frames=len(t) prevents the IndexError 
ani = FuncAnimation(fig, animate, frames=len(t), init_func=init, interval=33, blit=True)

# 5. SAVE AS MP4
# Change 'fps' to match your 't' vector density
# Change 'bitrate' if you want higher quality (larger file size)
mp4_writer = FFMpegWriter(fps=30, metadata=dict(artist='Scientific Sim'), bitrate=2000)

print("Starting save process... this may take a moment.")
ani.save("double_pendulum_chaos.mp4", writer=mp4_writer)
print("Success! File saved as 'double_pendulum_chaos.mp4'")

# Optional: Show the plot at the end if running locally
# plt.show()
