import numpy as np
import matplotlib.pyplot as plt

# MODIFIED CASE: a student software project has three stages in sequence.
# Each duration (days) is uncertain and modelled with a triangular
# distribution (minimum, most likely, maximum). Deadline = 60 days.
rng = np.random.default_rng(42)
N = 100_000
stages = {
    "Requirements & design": (8, 12, 20),
    "Coding":                (20, 28, 45),
    "Testing & report":      (7, 10, 18),
}
deadline = 60

total = np.zeros(N)
for name, (lo, mode, hi) in stages.items():
    d = rng.triangular(lo, mode, hi, N)
    total += d
    print(f"{name:22s}: mean {d.mean():5.2f} days")

late = total > deadline
print(f"Mean total duration: {total.mean():.2f} days")
print(f"Probability of missing the {deadline}-day deadline: {late.mean():.2%}")
print(f"Deadline needed for 90% confidence: {np.percentile(total, 90):.1f} days")
print(f"95% CI of the miss probability: +/- {1.96*np.sqrt(late.mean()*(1-late.mean())/N):.3%}")

plt.hist(total, bins=80, density=True, alpha=0.7)
plt.axvline(deadline, color="red", linestyle="--", label=f"Deadline ({deadline} days)")
plt.axvline(np.percentile(total, 90), color="black", linestyle=":", label="90th percentile")
plt.xlabel("Total project duration (days)")
plt.ylabel("Probability density")
plt.title("Monte Carlo simulation of project completion time")
plt.legend()
plt.grid(True)
plt.show()
