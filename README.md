# Lorenz System: Chaos Theory & Dynamical Systems Analysis

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

A comprehensive implementation and analysis of the **Lorenz System**, demonstrating chaotic behavior, fractal dimensions, and the famous "butterfly effect" in dynamical systems.

## 📐 Overview

The Lorenz equations were derived by **Edward Lorenz** in 1963 while studying atmospheric convection. This repository provides an in-depth exploration of these coupled, non-linear differential equations:

$$
\begin{cases}
\frac{dx}{dt} = \sigma (y - x) \\
\frac{dy}{dt} = x (\rho - z) - y \\
\frac{dz}{dt} = x y - \beta z
\end{cases}
$$

For the classic Lorenz attractor, the parameter values are:

$$
\begin{cases}
\sigma = 10 \\
\rho = 28 \\
\beta = \frac{8}{3}
\end{cases}
$$

## ✨ Features

- **Numerical Simulations**: Multiple integration methods (Forward Euler, Backward Euler, RK2, RK4)
- **3D Visualizations**: Interactive plots using Plotly and Matplotlib
- **Bifurcation Analysis**: Comprehensive bifurcation diagrams showing system transitions
- **Chaos Characterization**: Lyapunov exponents and fractal dimension calculations
- **Sensitivity Analysis**: Demonstration of the butterfly effect with multiple initial conditions
- **Animations**: Beautiful Manim animations showing trajectory evolution
- **Mathematical Rigor**: Detailed theoretical analysis including stability, attractors, and ergodic theory

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lorenz-system.git
cd lorenz-system
```

2. Install required packages:
```bash
pip install numpy matplotlib scipy seaborn plotly
```

3. For animations (optional):
```bash
# Follow Manim installation guide: https://docs.manim.community/en/stable/installation.html
pip install manim
```

### Quick Start

Open and run the Jupyter notebook:
```bash
jupyter notebook lorenz_system.ipynb
```

Or generate animations:
```bash
manim -pqh animation.py LorenzAttractor
```

## 📊 What's Inside

### 1. **Theoretical Foundation**
- Dynamical systems theory
- Equilibrium points and stability analysis
- Jacobian matrices and eigenvalue analysis
- Attractor types (fixed points, limit cycles, strange attractors)
- Lyapunov exponents and chaos theory

### 2. **Numerical Methods**
Four integration methods with comparison:
- **Forward Euler**: Simple but less accurate
- **Backward Euler**: Better stability for stiff systems
- **RK2**: Second-order Runge-Kutta
- **RK4**: Fourth-order Runge-Kutta (most accurate)

### 3. **Visualizations**

#### Interactive 3D Plots
```python
plot_lorenz_attractor(
    sigma=10.0,
    rho=28.0,
    beta=8.0/3.0,
    plots=2,  # Number of trajectories
    ERROR=0.001,  # Initial condition perturbation
    method="RK4"
)
```

#### Bifurcation Diagrams
Explore how system behavior changes with parameter $\rho$:
- Stable equilibria ($\rho < 1$)
- Period doubling
- Transition to chaos ($\rho \approx 24$)

### 4. **Key Results**

**Fractal Dimension**: The Lorenz attractor has a Kaplan-Yorke dimension of approximately:
$$D \approx 2.06$$

**Lyapunov Exponents** (for $\sigma=10, \rho=28, \beta=8/3$):
$$\lambda_1 \approx 0.905, \quad \lambda_2 \approx 0.0, \quad \lambda_3 \approx -14.57$$

## 🎬 Animations

The included animation demonstrates the **butterfly effect**:
- Three trajectories with tiny initial differences ($0.01$ units apart)
- Rapid divergence showing sensitive dependence on initial conditions
- Full phase space exploration over 40 seconds

### Watch the Animation

![Lorenz Attractor Animation](LorenzAttractor.mp4)

The animation shows three trajectories starting at:
- **Red**: $P_0 = \hat{i}$
- **Orange**: $P_1 = \hat{i} + 0.01\hat{j}$
- **Blue**: $P_2 = \hat{i} + 0.01\hat{k}$

Despite starting only $0.01$ units apart, they rapidly diverge into completely different regions of phase space!

### Generate Your Own

```bash
manim -pqh animation.py LorenzAttractor
```

## 📁 Repository Structure

```
lorenz-system/
├── README.md                    # This file
├── lorenz_system.ipynb         # Main Jupyter notebook with analysis
├── animation.py                # Manim animation script
├── runge-kutta.py             # Numerical integration methods
├── .gitignore                 # Git ignore rules
└── media/                     # Generated animations (gitignored)
```

## 🔬 Research & Applications

The Lorenz system is fundamental to:
- **Meteorology**: Weather prediction limitations
- **Chaos Theory**: Understanding deterministic chaos
- **Nonlinear Dynamics**: Studying complex systems
- **Fractal Geometry**: Analyzing strange attractors
- **Engineering**: Control theory and stability analysis

## 📚 Bibliography

### Books
- Strogatz, S. H. (2014). *Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering*. CRC Press.

### Papers
- Lorenz, E. N. (1963). Deterministic nonperiodic flow. *Journal of the Atmospheric Sciences*, 20(2), 130-141.
- Kaplan, J.L. & Yorke, J.A. (1979). Chaotic behavior of multidimensional difference equations.
- Jamie Budai (2014). Calculating Fractal Dimension of Attracting Sets of the Lorenz System. *Dynamics at the Horsetooth*, Volume 6.

### Videos
- [Chaos: The Science of the Butterfly Effect - Veritasium](https://www.youtube.com/watch?v=fDek6cYijxI)
- [Chaos Theory: the language of (in)stability - Gonkee](https://www.youtube.com/watch?v=uzJXeluCKMs)

## 👥 Authors

- **Albert Janik** - Faculty of Mathematics, Wrocław University of Science and Technology
- **Dominik Jur** - Faculty of Mathematics, Wrocław University of Science and Technology

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 🌟 Acknowledgments

- Edward Lorenz for discovering this fascinating system
- The chaos theory and dynamical systems community
- Manim Community for the animation library

## 📞 Contact

For questions or collaboration opportunities, please open an issue on GitHub.

---

**Made with ❤️ and chaos**
