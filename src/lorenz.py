import numpy as np
from scipy.integrate import solve_ivp
import plotly.graph_objects as go
import plotly.express as px


def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


def lorenz_attractor(
    sigma: float = 10.0,
    rho: float = 28.0,
    beta: float = 8.0 / 3.0,
    initial_state: np.ndarray = np.array([1.0, 0.0, 0.0]),
    t_start: float = 0.0,
    t_end: float = 400.0,
    plots: int = 1,
    ERROR: float = 0.001,
    cmap: str = "GnBu",
    plot_thickness: int = 2,
    color_offset: float = 0.1,
    fig_size: tuple = (1350, 900),
):
    plots = int(plots)
    if plots < 1:
        raise ValueError("Number of plots must be at least 1")

    t_eval = np.linspace(t_start, t_end, 1000 * int(t_end - t_start))

    fig = go.Figure()
    color_values = np.linspace(color_offset, 1- color_offset, plots)

    for plot_num in range(plots):
        perturbed_state = initial_state * (1 + (ERROR * plot_num))  # Small perturbation

        solution = solve_ivp(
            lorenz,
            [t_start, t_end],
            perturbed_state,
            args=(sigma, rho, beta),
            t_eval=t_eval,
        )
        color_value = 0.5 if plots==1 else color_values[plot_num]  # Map plot_num to a value between 0 and 1

        # Get the corresponding color from the colorscale
        color = px.colors.sample_colorscale(cmap, [color_value])[0]

        x, y, z = solution.y

        fig.add_trace(
            go.Scatter3d(
                x=x,
                y=y,
                z=z,
                mode="lines",
                line=dict(
                    color=color,
                    width=plot_thickness,
                ),
                name=f"Initial Condition {plot_num + 1}",
            )
        )

    fig.update_traces(opacity=0.4)

    fig.update_layout(
        title=(
            f"Lorenz Attractor - Two Initial Conditions (ERROR:{ERROR*100}%)"
            if plots > 1
            else "Lorenz Attractor - One Initial Condition"
        ),
        scene=dict(
            xaxis=dict(
                backgroundcolor="black",
                gridcolor="white",
                showbackground=True,
                zerolinecolor="white",
            ),
            yaxis=dict(
                backgroundcolor="black",
                gridcolor="white",
                showbackground=True,
                zerolinecolor="white",
            ),
            zaxis=dict(
                backgroundcolor="black",
                gridcolor="white",
                showbackground=True,
                zerolinecolor="white",
            ),
            camera=dict(
                up=dict(x=0, y=0, z=1),
                center=dict(x=0, y=0, z=0),
                eye=dict(x=2.5, y=0.1, z=0.1),
            ),
        ),
        margin=dict(r=10, l=10, b=10, t=10),
        paper_bgcolor="black",
        plot_bgcolor="black",
        width=fig_size[0],
        height=fig_size[1],
        font=dict(color="white"),
        showlegend=True,
    )

    fig.show()