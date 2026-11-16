import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# MODIFIED CASE: monthly active users of a new campus app (illustrative data).
# Early growth looks exponential, so fit N(t) = N0 * exp(r t).
month = np.arange(1, 9, dtype=float)
users = np.array([120, 165, 228, 300, 410, 560, 740, 1010], dtype=float)

def model(t, N0, r):
    return N0*np.exp(r*t)

params, cov = curve_fit(model, month, users, p0=[100, 0.3])
N0, r = params
err = np.sqrt(np.diag(cov))
pred = model(month, N0, r)
rmse = np.sqrt(np.mean((users - pred)**2))

print(f"Fitted model: N(t) = {N0:.2f} * exp({r:.4f} t)")
print(f"Growth rate per month: {np.exp(r) - 1:.2%}  (+/- {err[1]:.4f} on r)")
print(f"Doubling time: {np.log(2)/r:.2f} months")
print(f"RMSE: {rmse:.2f} users")
print(f"Forecast for month 12: {model(12, N0, r):.0f} users")

t_plot = np.linspace(1, 12, 300)
plt.scatter(month, users, label="Measured users")
plt.plot(t_plot, model(t_plot, N0, r), label="Exponential fit")
plt.xlabel("Month")
plt.ylabel("Active users")
plt.title("Exponential growth fit for app users")
plt.legend()
plt.grid(True)
plt.show()
