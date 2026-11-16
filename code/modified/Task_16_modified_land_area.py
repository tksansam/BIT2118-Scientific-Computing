import numpy as np
from scipy.integrate import simpson

# MODIFIED CASE: a surveyor measures the width of an irregular plot of
# land (bounded by a river) every 10 m along a 120 m baseline.
distance_m = np.arange(0, 130, 10, dtype=float)
width_m = np.array([0.0, 14.5, 21.0, 25.8, 28.4, 30.1, 31.0,
                    30.2, 28.0, 24.6, 19.9, 12.8, 0.0])

area_trap = np.trapezoid(width_m, distance_m)
area_simp = simpson(width_m, x=distance_m)

for name, a in [("Trapezoidal rule", area_trap), ("Simpson's rule", area_simp)]:
    print(f"{name:17s}: {a:8.1f} m^2 = {a/4046.86:.3f} acres = {a/10000:.4f} ha")
print(f"Difference: {abs(area_simp - area_trap):.1f} m^2 "
      f"({abs(area_simp - area_trap)/area_simp:.2%})")
