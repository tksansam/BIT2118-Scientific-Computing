import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# MODIFIED CASE: flu outbreak in a boarding school of 1,200 students (SIR model).
#   dS/dt = -beta S I / N
#   dI/dt =  beta S I / N - gamma I
#   dR/dt =  gamma I
N = 1200
beta = 0.6      # infections per infected student per day
gamma = 0.2     # recovery rate (about 5 days sick)
I0 = 3
y0 = [N - I0, I0, 0]

def sir(t, y):
    S, I, R = y
    return [-beta*S*I/N, beta*S*I/N - gamma*I, gamma*I]

t_eval = np.linspace(0, 60, 601)
sol = solve_ivp(sir, (0, 60), y0, t_eval=t_eval, rtol=1e-9, atol=1e-9)
S, I, R = sol.y

peak = np.argmax(I)
print("Solver success:", sol.success)
print(f"Basic reproduction number R0 = {beta/gamma:.1f}")
print(f"Peak number sick: {I[peak]:.0f} students on day {sol.t[peak]:.1f}")
print(f"Students never infected by day 60: {S[-1]:.0f}")
print(f"Total ever infected: {R[-1] + I[-1]:.0f} ({(R[-1] + I[-1])/N:.1%})")
print(f"Population conservation error: {np.max(np.abs(S + I + R - N)):.2e}")

plt.plot(sol.t, S, label="Susceptible")
plt.plot(sol.t, I, label="Infected")
plt.plot(sol.t, R, label="Recovered")
plt.xlabel("Day")
plt.ylabel("Students")
plt.title("SIR model of a school flu outbreak")
plt.legend()
plt.grid(True)
plt.show()
