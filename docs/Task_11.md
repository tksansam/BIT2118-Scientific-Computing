# Task 11: Newton-Raphson and Secant Methods

Files: code/original/Task_11_newton_secant.py, code/parameter_change/Task_11_newton_secant_param.py, code/modified/Task_11_modified_loan_rate.py

## B. Input values and operation

The cash flows are -10,000 at the start, then 3,000, 3,500, 4,000 and 2,500 in the following years. NPV is the sum of each cash flow divided by (1 + r) to the power of its year. The internal rate of return (IRR) is the rate r that makes NPV = 0.

- Newton's method starts from 0.10 and uses the derivative of NPV.
- The secant method starts with 0.05 and 0.20 and does not need a derivative.

## C. Changing an input

I changed the last cash flow from 2,500 to 5,000.

| Result | Original | After change |
|---|---|---|
| IRR | 11.542% | 18.327% |

A bigger payment at the end makes the investment earn more, so the IRR went up. Both methods still gave the same answer.

## D. Meaning of the output

The project gives a return of about 11.5% per year. It is worth doing if money can be borrowed at less than 11.5%. NPV comes out as 0 at this rate, which shows the root is correct.

## E. Modified program: interest rate of a loan

Assumptions: someone borrows KES 100,000 and pays KES 9,500 per month for 12 months. I used the loan (annuity) formula P = A(1 - (1+i)^-n)/i and solved it for the monthly rate i.

Input data: P = 100,000, A = 9,500, n = 12.

Output: the monthly rate is 2.076%. Newton took 4 iterations and secant took 6. Over a year this comes to 27.96%. The total interest is KES 14,000.

Interpretation: KES 14,000 of interest sounds small, but it is about 28% per year. Newton was faster because it uses the exact derivative.
