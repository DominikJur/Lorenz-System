# Lorenz System

## Overview
This repository provides an implementation and analysis of the **Lorenz System**, a system of ordinary differential equations used to model chaotic systems. The Lorenz system is famous for its role in illustrating chaotic behavior, commonly known as the "butterfly effect," and is widely studied in the field of dynamical systems and chaos theory.

The Lorenz equations were derived by **Edward Lorenz** in 1963 while studying atmospheric convection, and they are defined by the following three coupled, non-linear differential equations:

$$
\begin{cases}
\frac{dx}{dt} = \sigma (y - x) \\
\frac{dy}{dt} = x (\rho - z) - y \\
\frac{dz}{dt} = x y - \beta z
\end{cases}
$$

where:
-  $x$ ,  $y$ , and  $z$ are the state variables.
-  $$\sigma $$ ,  $$\rho $$ , and $$\beta $$ are parameters that control the system's behavior.

For the classic Lorenz attractor, the values of these parameters are typically:

$$
\begin{cases}
\sigma = 10 \\
\rho = 28  \\
\beta = \frac{8}{3} 
\end{cases}
$$

## Features
- Numerical simulation of the Lorenz system using Python.
- Visualization of the Lorenz attractor.
- Exploration of how different parameter values impact system behavior.
- Analysis of the chaotic properties of the system.
