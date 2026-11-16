import math
import numpy as np

# MODIFIED CASE: rounding error when a shop adds up many small payments.
# 1,000,000 payments of KES 0.10 should total exactly KES 100,000.00
n = 1_000_000
payment = 0.10

# 1. Naive floating-point running total
total_float = 0.0
for _ in range(n):
    total_float += payment

# 2. Compensated summation (math.fsum)
total_fsum = math.fsum([payment] * n)

# 3. Integer cents (how real accounting systems store money)
total_cents = n * 10
total_int = total_cents / 100

expected = 100_000.00
for name, value in [("Running float total", total_float),
                    ("math.fsum total", total_fsum),
                    ("Integer cents total", total_int)]:
    abs_err = abs(value - expected)
    print(f"{name:20s}: {value:.10f}  absolute error = {abs_err:.3e}  "
          f"relative error = {abs_err/expected:.3e}")

print("Exact comparison of running total:", total_float == expected)
print("Tolerance comparison of running total:", np.isclose(total_float, expected))
print("Machine epsilon for float64:", np.finfo(float).eps)
