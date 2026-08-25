# 2D Steady-State Heat Conduction Solver (FDM)

A finite difference solver for 2D steady-state heat conduction on a square domain without internal heat generation, solved using the Gauss-Seidel iterative method.

---

## Governing Equation

Steady-state 2D conduction in an isotropic, homogeneous medium with constant thermal conductivity $k$ and zero internal generation is governed by Laplace's equation:

$$\nabla^2 T = \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0$$

### Discretization

Applying a second-order central difference scheme on a uniform Cartesian grid ($\Delta x = \Delta y = h$):

$$\frac{\partial^2 T}{\partial x^2} \approx \frac{T_{i, j+1} - 2T_{i,j} + T_{i, j-1}}{h^2}$$

$$\frac{\partial^2 T}{\partial y^2} \approx \frac{T_{i+1, j} - 2T_{i,j} + T_{i-1, j}}{h^2}$$

Substituting these approximations into Laplace's equation gives the standard 5-point stencil:

$$\frac{T_{i+1, j} + T_{i-1, j} + T_{i, j+1} + T_{i, j-1} - 4T_{i,j}}{h^2} = 0$$

Rearranging for the nodal temperature $T_{i,j}$:

$$T_{i,j} = \frac{1}{4} \left( T_{i+1, j} + T_{i-1, j} + T_{i, j+1} + T_{i, j-1} \right)$$

---

## Numerical Method: Gauss-Seidel

The Gauss-Seidel method updates nodal values sequentially in-place. As the loop sweeps row-by-row and column-by-column, it immediately uses the newly calculated values from the current iteration $(k+1)$ for the left and top neighbors, rather than waiting for the entire grid to finish:

$$T_{i,j}^{(k+1)} = \frac{1}{4} \left( T_{i-1, j}^{(k+1)} + T_{i+1, j}^{(k)} + T_{i, j-1}^{(k+1)} + T_{i, j+1}^{(k)} \right)$$

This cuts memory overhead and typically halves the iteration count compared to standard Jacobi iteration.

### Convergence Criterion

Convergence is reached when the maximum absolute change across any node drops below the tolerance $\epsilon$:

$$\max_{i,j} \left| T_{i,j}^{(k+1)} - T_{i,j}^{(k)} \right| < \epsilon$$

---

## Boundary Conditions

The domain is a unit square $[0, 1] \times [0, 1]$ subjected to Dirichlet boundary conditions:

* **Top ($y = L$):** $T = 1.0$
* **Bottom ($y = 0$):** $T = 0.0$
* **Left ($x = 0$):** $T = 0.0$
* **Right ($x = L$):** $T = 0.0$

---

## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/hector-0208/2d_temp_distribution_using_FDM.git
cd 2d_temp_distribution_using_FDM
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run
```bash
python main.py
```
## Sample Output

* Grid Resolution: $51 \times 51$ ($h = 0.02$)
* Convergence Criterion: $\epsilon = 10^{-8}$
* Iterations to Convergence: ~2,330 iterations
### Running main.py generates two plots:
1. Semi-log convergence plot showing residual decay $\max |\Delta T|$ per iteration.
2. Filled contour plot (contourf) of the steady-state thermal distribution $T(x,y)$.
