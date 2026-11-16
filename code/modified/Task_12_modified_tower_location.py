import numpy as np
from scipy.optimize import root

# MODIFIED CASE: locate a phone from two cell towers.
# Tower 1 at (0, 0) km measures a distance of 5.0 km.
# Tower 2 at (8, 0) km measures a distance of 6.0 km.
towers = np.array([[0.0, 0.0], [8.0, 0.0]])
dist = np.array([5.0, 6.0])

def equations(z):
    x, y = z
    return [(x - towers[0, 0])**2 + (y - towers[0, 1])**2 - dist[0]**2,
            (x - towers[1, 0])**2 + (y - towers[1, 1])**2 - dist[1]**2]

# Two circles meet in two places: one north and one south of the towers.
for guess in ([3.0, 3.0], [3.0, -3.0]):
    sol = root(equations, guess)
    print("Initial guess:", guess)
    print("Possible location (km):", np.round(sol.x, 4))
    print("Residuals:", np.round(equations(sol.x), 10))
    print("Converged:", sol.success)
    print()

# A third tower removes the ambiguity
tower3, d3 = np.array([4.0, 6.0]), 2.4
for guess in ([3.0, 3.0], [3.0, -3.0]):
    p = root(equations, guess).x
    print(f"Candidate {np.round(p, 3)} is {np.linalg.norm(p - tower3):.2f} km "
          f"from tower 3 (measured {d3} km)")
