import matplotlib.pyplot as plt
import numpy as np


def plot_temperature_field(T, L=1.0):
    N = T.shape[0]
    x = np.linspace(0, L, N)
    y = np.linspace(L, 0, N)
    X, Y = np.meshgrid(x, y)

    plt.figure(figsize=(6, 5))
    contour = plt.contourf(X, Y, T, levels=50, cmap="jet")
    plt.colorbar(contour, label="Temperature $T(x,y)$")
    plt.title("Steady-State Temperature Field")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()

def plot_convergence(residuals):
    plt.figure(figsize=(6, 4))
    plt.semilogy(range(1, len(residuals) + 1), residuals, color="black", lw=1.2)
    plt.title("Convergence History (Max $\\Delta T$)")
    plt.xlabel("Iteration")
    plt.ylabel("Residual (Log scale)")
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
