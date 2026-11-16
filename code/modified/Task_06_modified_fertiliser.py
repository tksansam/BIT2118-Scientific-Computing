import numpy as np

# MODIFIED CASE: a farmer blends three fertilisers to meet the exact
# nutrient need of one hectare of maize.
# Nutrient fraction per kg of product (N, P2O5, K2O):
#   DAP 18-46-0, CAN 26-0-0, MOP 0-0-60
# Target per hectare: 60 kg N, 46 kg P2O5, 30 kg K2O (illustrative recommendation)
A = np.array([
    [0.18, 0.26, 0.00],   # nitrogen
    [0.46, 0.00, 0.00],   # phosphate
    [0.00, 0.00, 0.60],   # potash
])
b = np.array([60.0, 46.0, 30.0])

kg = np.linalg.solve(A, b)
residual = b - A @ kg

for name, value in zip(["DAP", "CAN", "MOP"], kg):
    print(f"{name}: {value:.2f} kg  ({value/50:.2f} bags of 50 kg)")
print("Nutrients supplied (N, P, K):", A @ kg)
print("Residual norm:", np.linalg.norm(residual))
print("Condition number of A:", round(np.linalg.cond(A), 2))
