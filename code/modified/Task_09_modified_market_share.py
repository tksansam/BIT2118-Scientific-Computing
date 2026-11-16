import numpy as np

# MODIFIED CASE: long-run market share of three mobile networks.
# P[i, j] = probability that a customer on network j this month is on
# network i next month (columns sum to 1). Rates are hypothetical.
P = np.array([
    [0.90, 0.07, 0.10],   # to Network X
    [0.06, 0.88, 0.05],   # to Network Y
    [0.04, 0.05, 0.85],   # to Network Z
])
networks = ["Network X", "Network Y", "Network Z"]
assert np.allclose(P.sum(axis=0), 1)

eigenvalues, eigenvectors = np.linalg.eig(P)
index = np.argmin(np.abs(eigenvalues - 1))     # eigenvalue 1 = steady state
steady = np.real(eigenvectors[:, index])
steady = steady / steady.sum()

print("Eigenvalues:", np.round(np.real(eigenvalues), 4))
print("Long-run market share:")
for name, share in zip(networks, steady):
    print(f"  {name}: {share:.2%}")

# Check by simulating 60 months from today's shares
share = np.array([0.30, 0.40, 0.30])
for month in range(60):
    share = P @ share
print("Shares after 60 months from (30%, 40%, 30%):", np.round(share, 4))
print("Verification error ||Pv - v||:", np.linalg.norm(P @ steady - steady))
