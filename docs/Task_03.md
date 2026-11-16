# Task 3: Vectorisation

Files: code/original/Task_03_vectorization.py, code/parameter_change/Task_03_vectorization_param.py, code/modified/Task_03_modified_mobile_money_fees.py

## B. Input values and operation

The input is one million random network latency readings between 5 and 250 ms. The random seed is 42, so the same numbers come out every time. Each reading is changed to seconds (divided by 1000) and then squared. This is done once with a normal Python for loop and once with a NumPy array operation, and timeit measures how long each takes.

## C. Changing an input

I reduced the number of readings from 1,000,000 to 100,000.

| Result | 1,000,000 readings | 100,000 readings |
|---|---|---|
| Loop time | about 0.15 to 0.22 s | 0.020 s |
| Vectorised time | about 0.003 to 0.004 s | 0.0008 s |
| Speed-up | about 46x to 54x | about 26x |

The loop became about 10 times faster, which matches having 10 times less data. The vectorised version did not speed up as much, because NumPy has a small fixed cost every time it is called. This means vectorising helps more when the data is large. The times change a little each time the program runs.

## D. Meaning of the output

The loop and NumPy give exactly the same answers, but NumPy is around 50 times faster. This is because NumPy does the work in compiled C code instead of going through Python one value at a time. For big data like network logs, vectorised code is the better choice.

## E. Modified program: mobile money transfer fees

I used vectorisation to work out a fee for one million money transfers.

Assumptions: transfer amounts are between KES 10 and KES 70,000, with many small transfers and a few big ones. The fee bands are ones I made up for the exercise and are not a real company's charges.

Input data: one million random amounts and seven fee bands.

Output: total fees were KES 29,066,566, and the average fee was KES 29.07. The loop took 0.32 s and the vectorised version took 0.008 s, about 39 times faster. Both methods gave the same fees.

Interpretation: even a calculation that has if-statements, like choosing a fee band, can be vectorised with np.searchsorted. For a company with millions of transfers every day, this saves a lot of time.
