# Task 4: Numerical Errors

Files: code/original/Task_04_numerical_errors.py, code/parameter_change/Task_04_numerical_errors_param.py, code/modified/Task_04_modified_money_rounding.py

## B. Input values and operation

The program has three parts:

1. It adds 0.1 and 0.2 and compares the answer with 0.3, first with == and then with np.isclose.
2. It finds the absolute and relative error when the square root of 2 is approximated as 1.414.
3. It compares two formulas that should give the same answer, (sqrt(1+x) - 1)/x and 1/(sqrt(1+x) + 1), for x = 1e-4, 1e-8 and 1e-12.

## C. Changing an input

I changed the approximation of the square root of 2 to 1.41421 and added x = 1e-15 to the list.

| Result | Original | After change |
|---|---|---|
| Absolute error | 0.00021356 | 0.00000356 |
| Relative error | 0.0151% | 0.00025% |
| Direct formula at x = 1e-15 | not tested | 0.4441 |
| Stable formula at x = 1e-15 | not tested | 0.5000 |

With two more decimal places, the error became about 60 times smaller. At x = 1e-15 the first formula gives 0.444 when the answer should be about 0.5. The computer cannot store 1 + 1e-15 exactly, and subtracting 1 removes most of the correct digits. This is called catastrophic cancellation. The second formula has no subtraction, so it stays correct.

## D. Meaning of the output

0.1 + 0.2 gives 0.30000000000000004 because these numbers cannot be stored exactly in binary. That is why == says False and isclose says True. Decimal numbers should be compared with a tolerance and not with ==. The last part shows that the way a formula is written can affect how accurate the answer is.

## E. Modified program: adding up small payments

I used the same idea for money.

Assumptions: a shop gets 1,000,000 payments of KES 0.10, so the correct total is exactly KES 100,000.

Input data: the payment amount (0.10) and the number of payments (1,000,000).

Output: adding the payments one by one in a float variable gave 100000.0000013329, which is wrong by about 0.0000013. Using math.fsum, or counting in whole cents, both gave exactly 100000.0.

Interpretation: the error is tiny here, but it grows as more numbers are added, and it can make an exact balance check fail. This is why banking systems store money as whole cents or use decimal types.
