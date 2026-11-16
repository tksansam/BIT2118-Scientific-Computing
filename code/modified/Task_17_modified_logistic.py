import numpy as np
import matplotlib.pyplot as plt

# MODIFIED CASE: logistic growth of fish in a pond.
# dP/dt = r P (1 - P/K)
r = 0.4       # growth rate per week
K = 2000.0    # carrying capacity of the pond (fish)
P0 = 100.0    # fish stocked at week 0
end = 20.0    # weeks

def rate(P):
    return r*P*(1 - P/K)

def exact(t):
    return K / (1 + (K/P0 - 1)*np.exp(-r*t))

for h in [1.0, 0.5, 0.1]:
    t = np.arange(0, end + h/2, h)
    P = np.zeros_like(t); P[0] = P0
    for i in range(len(t) - 1):
        P[i+1] = P[i] + h*rate(P[i])
    err = np.max(np.abs(P - exact(t)))
    print(f"h = {h:4.2f} weeks: P(20) = {P[-1]:8.2f}, max error = {err:7.3f} fish")
    if h == 1.0:
        t1, P1 = t, P

print(f"Exact P(20) = {exact(end):.2f} fish")

tt = np.linspace(0, end, 300)
plt.plot(t1, P1, marker="o", label="Euler (h = 1 week)")
plt.plot(tt, exact(tt), label="Exact solution")
plt.axhline(K, linestyle=":", label="Carrying capacity")
plt.xlabel("Time (weeks)")
plt.ylabel("Fish population")
plt.title("Logistic growth of a fish population")
plt.legend()
plt.grid(True)
plt.show()
