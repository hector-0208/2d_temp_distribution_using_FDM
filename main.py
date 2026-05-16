from src.solver import solve_2d_heat
from src.visualize import plot_convergence, plot_temperature_field


def main():
    N = 51
    L = 1.0
    tol = 1e-8

    print(f"Running Gauss-Seidel solver on a {N}x{N} grid...")
    T, iters, residuals = solve_2d_heat(N=N, L=L, epsilon=tol)
    print(f"Converged after {iters} iterations (Tolerance: {tol}).")

    plot_convergence(residuals)
    plot_temperature_field(T, L=L)

if __name__ == "__main__":
    main()
