import numpy as np
import matplotlib.pyplot as plt

# MODIFIED CASE: a 9-point metal rod; one end sits in a jiko at 250 C,
# the other end is held at room temperature 25 C.
# Compare Jacobi, Gauss-Seidel and Successive Over-Relaxation (SOR).
n = 9
A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
b = np.zeros(n)
b[0], b[-1] = 250.0, 25.0

def sor(A, b, omega, tol=1e-8, max_iter=5000):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            gs = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
            x[i] = (1 - omega)*old[i] + omega*gs
        errors.append(np.linalg.norm(x - old, ord=np.inf))
        if errors[-1] < tol:
            break
    return x, errors

def jacobi(A, b, tol=1e-8, max_iter=5000):
    D = np.diag(A); R = A - np.diagflat(D)
    x = np.zeros_like(b); errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        errors.append(np.linalg.norm(x_new - x, ord=np.inf))
        x = x_new
        if errors[-1] < tol:
            break
    return x, errors

x_j, e_j = jacobi(A, b)
x_gs, e_gs = sor(A, b, 1.0)          # omega = 1 is Gauss-Seidel
omega_opt = 2 / (1 + np.sin(np.pi/(n+1)))
x_sor, e_sor = sor(A, b, omega_opt)
x_exact = np.linalg.solve(A, b)

print("Temperatures (C):", np.round(x_exact, 2))
print(f"Jacobi iterations:        {len(e_j)}")
print(f"Gauss-Seidel iterations:  {len(e_gs)}")
print(f"SOR iterations (w={omega_opt:.3f}): {len(e_sor)}")
print("Max difference SOR vs direct:", np.max(np.abs(x_sor - x_exact)))

plt.semilogy(e_j, label="Jacobi")
plt.semilogy(e_gs, label="Gauss-Seidel")
plt.semilogy(e_sor, label=f"SOR (w={omega_opt:.2f})")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Rod temperature: convergence of three iterative methods")
plt.legend()
plt.grid(True)
plt.show()
