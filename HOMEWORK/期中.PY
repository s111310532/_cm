import numpy as np
import matplotlib.pyplot as plt

def solve_pendulum(theta0, omega0, t_max, dt, L=1.0, g=9.81):
    """
    使用 RK4 求解單擺運動： d^2(theta)/dt^2 + (g/L)sin(theta) = 0
    將其拆解為兩個一階方程：
    1. d(theta)/dt = omega
    2. d(omega)/dt = -(g/L) * sin(theta)
    """
    def derivatives(state):
        theta, omega = state
        d_theta = omega
        d_omega = -(g / L) * np.sin(theta)
        return np.array([d_theta, d_omega])

    # 初始化
    t_steps = np.arange(0, t_max, dt)
    history = np.zeros((len(t_steps), 2))
    state = np.array([theta0, omega0])

    # RK4 主迴圈
    for i in range(len(t_steps)):
        history[i] = state
        
        k1 = dt * derivatives(state)
        k2 = dt * derivatives(state + 0.5 * k1)
        k3 = dt * derivatives(state + 0.5 * k2)
        k4 = dt * derivatives(state + k3)
        
        state = state + (k1 + 2*k2 + 2*k3 + k4) / 6

    return t_steps, history[:, 0]

# 設定初始條件：從 45 度 (pi/4) 釋放，初始角速度為 0
t, theta = solve_pendulum(theta0=np.pi/4, omega0=0.0, t_max=10, dt=0.05)

# 繪圖
plt.figure(figsize=(10, 4))
plt.plot(t, np.degrees(theta), label='Theta (degrees)')
plt.title("Simple Pendulum Motion (RK4 Solver)")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.grid(True)
plt.show()
