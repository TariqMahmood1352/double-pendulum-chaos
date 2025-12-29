# double-pendulum-chaos
Deterministic chaos simulation using Lagrangian mechanics

# Double Pendulum – Deterministic Chaos Simulation

This repository contains a numerical simulation and animation of a **double pendulum**, a classical mechanical system known for exhibiting **deterministic chaos** due to its non-linear, coupled dynamics.

## Physical Model
The system consists of two point masses connected by massless rods and evolving under gravity.  
The dynamics are derived using **Lagrangian mechanics**, where:

L = T − V

The resulting equations of motion are **coupled, second-order, non-linear ordinary differential equations**.

## Numerical Method
The equations are solved using `scipy.integrate.odeint`, and the angular variables are converted to Cartesian coordinates for visualization.

Key features:
- Fully non-linear dynamics
- Sensitivity to initial conditions
- Real-time animation with trajectory tracing

## Parameters
- Gravity: 9.81 m/s²  
- Rod lengths: L₁ = L₂ = 1.0 m  
- Masses: M₁ = M₂ = 1.0 kg  
- Initial angles: θ₁ = θ₂ = π/2  

## Output
The simulation generates:
- A real-time animation of the double pendulum
- A trajectory trail showing chaotic motion
- An exported MP4 video (`double_pendulum_chaos.mp4`)

## How to Run
```bash
pip install numpy scipy matplotlib
python double_pendulum.py

