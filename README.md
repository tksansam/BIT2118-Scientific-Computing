# BIT 2118 Scientific Computing Group Work

Name: Samwel Abuga Manono
Reg No: BSCCS/2024/56213
Unit: BIT 2118 Scientific Computing

This repository has my individual work for the group tasks 2 to 20. For each task I did the following:

- B. Identified the input values and the mathematical operation.
- C. Changed at least one input and explained how the result changed.
- D. Explained what the output means and what the graph shows.
- E. Changed the program to solve a different real-world problem and wrote down the assumptions, input data, output and interpretation.

## Folders

- code/original - the programs as given in the solution code
- code/parameter_change - the same programs with an input changed (part C)
- code/modified - my new real-world programs (part E)
- outputs - what each program printed
- figures - the graphs
- docs - my findings for each task

## How to run

pip install -r requirements.txt

python code/original/Task_02_numpy_arrays.py

I used Python 3 with NumPy, SciPy and Matplotlib. In Task 16 and Task 18 one print line was split across two lines in the PDF. I joined these lines so the programs would run.

## Tasks

| Task | Topic | What I changed (C) | New problem (E) |
|---|---|---|---|
| 2 | NumPy arrays | all temperatures +2.5 C | monthly rainfall |
| 3 | Vectorisation | 100,000 readings | mobile money fees |
| 4 | Numerical errors | sqrt(2) = 1.41421, x = 1e-15 | adding small payments |
| 5 | Matrix algebra | 90 degrees, y scale 0.5 | shear and reflection |
| 6 | Linear systems | memory 80 GB | fertiliser mixing |
| 7 | Gaussian elimination and LU | A[2,2] = 5 | three-loop circuit |
| 8 | Jacobi and Gauss-Seidel | left end 60 C | hot rod with SOR |
| 9 | Eigenvalues | new link A-D | network market share |
| 10 | Bisection and fixed point | room temperature 30 C | water tank depth |
| 11 | Newton and secant | last cash flow 5,000 | loan interest rate |
| 12 | Nonlinear systems | radius 3 | phone location |
| 13 | Interpolation | 11:00 reading removed | phone battery |
| 14 | Curve fitting | one bad reading | app user growth |
| 15 | Numerical differentiation | GPS error at 3 s | matatu acceleration |
| 16 | Numerical integration | readings every 4 hours | land area |
| 17 | Euler's method | step 0.25 min | fish population |
| 18 | SciPy ODE solver | R = 2000 ohms | flu outbreak (SIR) |
| 19 | Optimisation | Type B cost 22 | farm plan |
| 20 | Monte Carlo | capacity 1100 | project deadline |

The details for each task are in the docs folder. The data in my modified programs is sample data I made up to be realistic. It is not official data.
