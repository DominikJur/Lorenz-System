import numpy as np


# Unused

def forward_euler(f, x0, t0, tf, dt):
    t = np.arange(t0, tf, dt)
    n = len(t)
    x = np.zeros((n, len(x0)))
    x[0] = x0
    for i in range(n - 1):
        x[i + 1] = x[i] + dt * f(t[i], x[i])
    return x

def backward_euler(f, x0, t0, tf, dt):
    t = np.arange(t0, tf, dt)
    n = len(t)
    x = np.zeros((n, len(x0)))
    x[0] = x0
    for i in range(n - 1):
        x[i + 1] = x[i] + dt * f(t[i + 1], x[i + 1])
    return x

def RK2(f, x0, t0, tf, dt):
    t = np.arange(t0, tf, dt)
    n = len(t)
    x = np.zeros((n, len(x0)))
    x[0] = x0
    for i in range(n - 1):
        k1 = f(t[i], x[i])
        k2 = f(t[i] + dt, x[i] + dt * k1)
        x[i + 1] = x[i] + dt / 2 * (k1 + k2)
    return x
 



# Used

def RK4(f, initial_state, t0, tf, dt):
    t = np.arange(t0, tf, dt)
    n = len(t)
    states = np.zeros((n, len(initial_state)))
    states[0] = initial_state
    for i in range(n - 1):
        state= states[i]
        k1 = f(t[i], state)
        k2 = f(t[i] + dt / 2, state + dt / 2 * k1)
        k3 = f(t[i] + dt / 2, state + dt / 2 * k2)
        k4 = f(t[i] + dt, state + dt * k3)
        states[i + 1] = states[i] + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return states

def solve_ivp(f, t_span, y0, t_eval):
    t0, tf = t_span 
    dt = t_eval[1] - t_eval[0]
    return RK4(f, y0, t0, tf, dt)

def lorenz_system(t, state, sigma=10, rho=28, beta=8 / 3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return np.array([dxdt, dydt, dzdt])

def ode_solution_points(function, state0, time, dt=0.01):   
    solution = solve_ivp(
        function,
        t_span=(0, time),
        y0=state0,
        t_eval=np.arange(0, time, dt)
    )
    return solution

if __name__ == "__main__":
    state0 = [10, 10, 10]
    time = 30
    dt = 0.01
    solution = ode_solution_points(lorenz_system, state0, time, dt)
    print(solution)
    
    import matplotlib.pyplot as plt 
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(solution[:,0], solution[:,1], solution[:,2])
    plt.show()