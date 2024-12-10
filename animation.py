from manim import *
import numpy as np

def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return np.array([dxdt, dydt, dzdt])

def RK4(f, initial_state, t0, tf, dt, args):
    def f_(t,state, args=args):
        return f(t, state, *args)
    t = np.arange(t0, tf, dt)
    n = len(t)
    states = np.zeros((n, len(initial_state)))
    states[0] = initial_state
    for i in range(n - 1):
        state= states[i]
        k1 = f_(t[i], state)
        k2 = f_(t[i] + dt / 2, state + dt / 2 * k1)
        k3 = f_(t[i] + dt / 2, state + dt / 2 * k2)
        k4 = f_(t[i] + dt, state + dt * k3)
        states[i + 1] = states[i] + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return states

def solve_ivp(f, t_span, y0, args, t_eval):
    t0, tf = t_span 
    dt = t_eval[1] - t_eval[0]
    return RK4(f, y0, t0, tf, dt, args)

class LorenzAttractor(ThreeDScene):
    def construct(self):
        # Lorenz system parameters
        sigma = 10
        rho = 28
        beta = 8 / 3
        initial_states = np.array([[1, 0, 0],
                                   [1, 0.01, 0],
                                   [1, 0, 0.01]])

        # Create the 3D axes with wider ranges
        axes = ThreeDAxes(
            x_range=[-1, 1, 0.5],
            y_range=[-1, 1, 0.5],
            z_range=[-1, 1, 0.5]
            )
        
        t0, tf = 0, 40
        t_eval = np.linspace(t0, tf, (tf - t0) * 100)
        t_span = [t0, tf]
        curves = VGroup()
        # Iterate over initial states to create 3 curves
        for initial_state, color in zip(initial_states, [RED, ORANGE, BLUE]):
            # Solve the system using RK4
            states = solve_ivp(lorenz, t_span, initial_state, args=(sigma, rho, beta), t_eval=t_eval)
            states = states / 50
            
            # Convert the states to 3D points
            curve = [axes.c2p(x, y, z) for x, y, z in states]
            curve_obj = VMobject(stroke_width=2, stroke_opacity=0.4, color=color).set_points_smoothly(curve).set_color(color)
            curves.add(curve_obj)
            
        dots = VGroup(
            *(Dot3D(color=color) for color in [RED, ORANGE, BLUE])
        )
        
        def update_dots(dots):
            for dot, curve_obj in zip(dots, curves):
                dot.move_to(curve_obj.get_end())
           
        dots.add_updater(update_dots)
        
        # Set up camera angle

        self.wait(1)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        # Add the axes and curves to the scene
        self.add(axes, dots)
        self.play(
            
            *[Create(curve_obj, rate_func=linear) for curve_obj in curves],
            run_time=tf - t0
        )
        # Begin ambient camera rotation to visualize the attractor from different angles
        self.begin_ambient_camera_rotation(rate=0.2)

        # # Wait for a few seconds at the end to view the final attractor
        self.wait(15)