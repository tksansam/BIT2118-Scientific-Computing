import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# MODIFIED CASE: a spherical water tank of radius r = 1.5 m.
# Volume of water at depth h:  V(h) = pi*h^2*(3r - h)/3
# Find the depth that holds 6.0 m^3 (6000 litres) so a level gauge can be marked.
r = 1.5
V_target = 6.0

def f(h):
    return np.pi*h**2*(3*r - h)/3 - V_target

solution = root_scalar(f, bracket=[0, 2*r], method="bisect", xtol=1e-10)

# Fixed-point form: h = sqrt(3V / (pi(3r - h)))
def g(h):
    return np.sqrt(3*V_target / (np.pi*(3*r - h)))

h = 1.0
history = [h]
for _ in range(200):
    h_new = g(h)
    history.append(h_new)
    if abs(h_new - h) < 1e-10:
        break
    h = h_new

print(f"Bisection depth:   {solution.root:.6f} m ({solution.iterations} iterations)")
print(f"Fixed-point depth: {history[-1]:.6f} m ({len(history)-1} iterations)")
print(f"Full tank volume:  {4/3*np.pi*r**3:.3f} m^3")

depths = np.linspace(0, 2*r, 300)
plt.plot(depths, f(depths) + V_target, label="Volume V(h)")
plt.axhline(V_target, linestyle=":", label="6.0 m^3 target")
plt.axvline(solution.root, linestyle="--", label=f"h = {solution.root:.3f} m")
plt.xlabel("Water depth h (m)")
plt.ylabel("Volume (m^3)")
plt.title("Depth of water in a spherical tank")
plt.legend()
plt.grid(True)
plt.show()
