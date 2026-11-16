import numpy as np
from scipy.linalg import lu_factor, lu_solve

# MODIFIED CASE: three-loop resistor circuit solved by mesh analysis.
# The resistor network (matrix A) is fixed; the battery voltages change
# during a test, so LU factorisation is done once and reused.
# Resistances in ohms -> A, voltages in volts -> b, unknowns are loop currents (A)
A = np.array([
    [ 15.0, -5.0,   0.0],
    [ -5.0, 20.0, -10.0],
    [  0.0, -10.0, 25.0]
])

voltage_tests = {
    "Test 1 (12 V, 0 V, 6 V)": np.array([12.0, 0.0, 6.0]),
    "Test 2 (9 V, 0 V, 9 V)":  np.array([9.0, 0.0, 9.0]),
    "Test 3 (24 V, 5 V, 0 V)": np.array([24.0, 5.0, 0.0]),
}

lu, piv = lu_factor(A)

for name, b in voltage_tests.items():
    I = lu_solve((lu, piv), b)
    power = np.sum(I * (A @ I))  # total power dissipated I^T R I
    print(name)
    print("  Loop currents (A):", np.round(I, 4))
    print(f"  Power dissipated: {power:.3f} W")
    print("  Residual norm:", np.linalg.norm(b - A @ I))
