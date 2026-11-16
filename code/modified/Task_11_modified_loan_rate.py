from scipy.optimize import root_scalar

# MODIFIED CASE: a lender offers KES 100,000 repaid in 12 monthly
# instalments of KES 9,500. What monthly interest rate is hidden in the offer?
# Annuity equation:  P = A*(1 - (1+i)^-n)/i   ->  solve f(i) = 0
P, A, n = 100_000.0, 9_500.0, 12

def f(i):
    return A*(1 - (1 + i)**-n)/i - P

def df(i):
    return A*(n*i*(1 + i)**(-n - 1) - (1 - (1 + i)**-n)) / i**2

newton = root_scalar(f, fprime=df, x0=0.02, method="newton", xtol=1e-12)
secant = root_scalar(f, x0=0.01, x1=0.03, method="secant", xtol=1e-12)

i = newton.root
print(f"Monthly rate (Newton): {newton.root:.6%} in {newton.iterations} iterations")
print(f"Monthly rate (Secant): {secant.root:.6%} in {secant.iterations} iterations")
print(f"Effective annual rate: {(1 + i)**12 - 1:.2%}")
print(f"Total repaid: KES {A*n:,.0f}; total interest: KES {A*n - P:,.0f}")
print(f"Check f(i): {f(i):.6f}")
