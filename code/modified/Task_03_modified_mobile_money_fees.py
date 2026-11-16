import numpy as np
import timeit

# MODIFIED CASE: compute a tiered transaction fee for one million
# mobile-money transfers. Fee bands are illustrative, not an official tariff.
rng = np.random.default_rng(7)
# Most transfers are small and a few are large, so a log-normal shape is used
amounts = np.clip(rng.lognormal(7.0, 1.3, 1_000_000), 10, 70_000).astype(int)  # KES

bands = [(100, 0), (500, 7), (1_000, 13), (2_500, 25),
         (5_000, 52), (20_000, 87), (70_000, 108)]

def loop_version():
    fees = []
    for a in amounts:
        for upper, fee in bands:
            if a <= upper:
                fees.append(fee)
                break
    return np.array(fees)

def vectorized_version():
    uppers = np.array([u for u, _ in bands])
    fees = np.array([f for _, f in bands])
    return fees[np.searchsorted(uppers, amounts)]

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

fees = vectorized_version()
assert np.array_equal(fees, loop_version()[:len(fees)]), "methods disagree"

print("First five amounts:", amounts[:5])
print("First five fees:   ", fees[:5])
print(f"Total fees collected: KES {fees.sum():,}")
print(f"Average fee per transfer: KES {fees.mean():.2f}")
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")
