import numpy as np
from scipy.interpolate import interp1d, CubicSpline
from scipy.optimize import brentq
import matplotlib.pyplot as plt

# MODIFIED CASE: a phone battery's voltage is logged every 30 minutes.
# Estimate the voltage at any minute and the time it reaches the 3.50 V
# low-battery warning level.
minutes = np.array([0, 30, 60, 90, 120, 150, 180, 210], dtype=float)
voltage = np.array([4.20, 4.05, 3.95, 3.87, 3.80, 3.71, 3.58, 3.40])

linear = interp1d(minutes, voltage, kind="linear")
cubic = CubicSpline(minutes, voltage)

t = 100.0
print(f"Linear estimate at {t:.0f} min: {float(linear(t)):.3f} V")
print(f"Cubic  estimate at {t:.0f} min: {float(cubic(t)):.3f} V")

warning = 3.50
t_lin = brentq(lambda x: linear(x) - warning, 180, 210)
t_cub = brentq(lambda x: cubic(x) - warning, 180, 210)
print(f"Time to {warning} V (linear): {t_lin:.1f} min")
print(f"Time to {warning} V (cubic):  {t_cub:.1f} min")

fine = np.linspace(0, 210, 400)
plt.scatter(minutes, voltage, label="Logged voltage", zorder=3)
plt.plot(fine, linear(fine), label="Linear")
plt.plot(fine, cubic(fine), label="Cubic spline")
plt.axhline(warning, linestyle=":", label="Low-battery warning")
plt.xlabel("Time (minutes)")
plt.ylabel("Voltage (V)")
plt.title("Battery discharge interpolation")
plt.legend()
plt.grid(True)
plt.show()
