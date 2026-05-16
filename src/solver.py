import numpy as np


def solve_2d_heat(N=51, L=1.0, epsilon=1e-8, max_iter=20000):
    """
    Solves steady-state 2D heat conduction on a square domain using Gauss-Seidel.
    Boundary conditions:
        - Top: T = 1.0
        - Bottom, Left, Right: T = 0.0
    """
    h = L / (N - 1)  # noqa: F841
    T = np.zeros((N, N))
    T[0, :] = 1.0  # Dirichlet BC: Top boundary heated

    iterations = 0
    residuals = []

    while iterations < max_iter:
        max_change = 0.0

        for i in range(1, N - 1):
            for j in range(1, N - 1):
                T_old = T[i, j]
                # 5-point Laplacian stencil (Gauss-Seidel update)
                T[i, j] = 0.25 * (T[i + 1, j] + T[i - 1, j] + T[i, j + 1] + T[i, j - 1])
                
                change = abs(T[i, j] - T_old)
                max_change = max(max_change, change)

        residuals.append(max_change)
        iterations += 1

        if max_change < epsilon:
            break

    return T, iterations, residuals
