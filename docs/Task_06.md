# Task 6: Linear Systems

Files: code/original/Task_06_linear_systems.py, code/parameter_change/Task_06_linear_systems_param.py, code/modified/Task_06_modified_fertiliser.py

## B. Input values and operation

A Type A server uses 4 CPU units and 8 GB of memory, and a Type B server uses 2 CPU units and 12 GB. The total use is 20 CPU units and 72 GB. This gives two equations with two unknowns, which the program solves with np.linalg.solve. It then checks the residual (b - Ax).

## C. Changing an input

I changed the memory total from 72 GB to 80 GB. I also changed the print format from .0f to .2f so that decimals would show.

| Result | Original | After change |
|---|---|---|
| Type A servers | 3 | 2.50 |
| Type B servers | 4 | 5.00 |
| Residual | 0 | 0 |

The equations still solve, but 2.5 servers is not possible in real life. This tells us that either the measurement is wrong or something else is using memory. With the original .0f format the program would have printed 2 and hidden this problem.

## D. Meaning of the output

The data centre has 3 Type A servers and 4 Type B servers. A residual of 0 means these numbers give back the exact CPU and memory totals.

## E. Modified program: mixing fertiliser

I used a 3 by 3 system for a farming problem.

Assumptions: a farmer uses DAP (18-46-0), CAN (26-0-0) and MOP (0-0-60). One hectare of maize needs 60 kg of nitrogen, 46 kg of phosphate and 30 kg of potash. These targets are example values.

Input data: the nutrient percentages of each fertiliser make up the matrix, and the targets make up the right-hand side.

Output: 100 kg of DAP (2 bags), 161.54 kg of CAN (about 3.2 bags) and 50 kg of MOP (1 bag). The residual is about 7e-15 and the condition number is 2.54.

Interpretation: with these amounts the farmer gets exactly the nutrients needed. The condition number is small, so small mistakes in the fertiliser labels will not change the answer much.
