import numpy as np
from scipy.optimize import minimize

# MODIFIED CASE: a farmer has 10 acres and decides how many acres of
# maize (x) and beans (y) to plant to MAXIMISE profit.
# Profit per acre (KES): maize 30,000, beans 42,000
# Labour per acre (days): maize 10, beans 20, available 160 days
# Fertiliser budget (KES): maize 6,000/acre, beans 4,000/acre, budget 52,000
# Contract: at least 3 acres of maize for a school feeding programme.
# Money is scaled to KES thousands so all constraints have similar size
# (badly scaled numbers made SLSQP report failure in the first test run).

def neg_profit(z):
    x, y = z
    return -(30*x + 42*y)   # profit in KES thousands; minimise the negative = maximise

constraints = [
    {"type": "ineq", "fun": lambda z: 10 - z[0] - z[1]},              # land
    {"type": "ineq", "fun": lambda z: 160 - 10*z[0] - 20*z[1]},       # labour
    {"type": "ineq", "fun": lambda z: 52 - 6*z[0] - 4*z[1]},          # fertiliser (KES 000)
    {"type": "ineq", "fun": lambda z: z[0] - 3},                       # contract
]
sol = minimize(neg_profit, x0=[3, 3], method="SLSQP",
               bounds=[(0, None), (0, None)], constraints=constraints)
x, y = sol.x
print("Optimization success:", sol.success)
print(f"Maize: {x:.3f} acres, Beans: {y:.3f} acres")
print(f"Maximum profit: KES {-sol.fun*1000:,.0f}")
print(f"Land used {x+y:.2f}/10, labour {10*x+20*y:.1f}/160 days, "
      f"fertiliser KES {6000*x+4000*y:,.0f}/52,000")

# Whole and half acres only
best = None
for a in np.arange(0, 10.5, 0.5):
    for b in np.arange(0, 10.5, 0.5):
        if a + b <= 10 and 10*a + 20*b <= 160 and 6000*a + 4000*b <= 52000 and a >= 3:
            p = 30_000*a + 42_000*b
            if best is None or p > best[0]:
                best = (p, a, b)
print(f"Best half-acre plan: maize {best[1]}, beans {best[2]}, profit KES {best[0]:,.0f}")
