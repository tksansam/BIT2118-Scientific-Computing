# Task 7: Gaussian Elimination and LU Decomposition

Files: code/original/Task_07_gaussian_lu.py, code/parameter_change/Task_07_gaussian_lu_param.py, code/modified/Task_07_modified_mesh_circuit.py

## B. Input values and operation

There is one 3 by 3 matrix A and three different measurement vectors b. The program factors A into L and U once using lu_factor, which is Gaussian elimination with pivoting. Then it uses lu_solve to get the answer for each b. The first answer is checked against np.linalg.solve.

## C. Changing an input

I changed the bottom right value of A from 3 to 5.

| Set | Original answer | After change |
|---|---|---|
| 1 | [5, 5, 5] | [4.859, 4.437, 2.887] |
| 2 | [5.317, 5.268, 4.756] | [5.183, 4.732, 2.746] |
| 3 | [4.902, 5.610, 5.537] | [4.746, 4.986, 3.197] |

The third unknown dropped the most. Its coefficient is now bigger, so a smaller value is needed to give the same measurement. The other two unknowns also dropped a little because they are linked to it. The residuals stayed around 1e-15.

## D. Meaning of the output

All the answers satisfy their equations almost exactly, and the LU answer matches np.linalg.solve. The main point is that the matrix only has to be factored once. After that, each new b can be solved quickly. This saves time when the same system is solved many times.

## E. Modified program: electric circuit with three loops

Assumptions: a circuit has three loops. Using Kirchhoff's voltage law, the resistances give the matrix [[15, -5, 0], [-5, 20, -10], [0, -10, 25]] in ohms. The battery voltages change for three different tests.

Input data: the resistance matrix and three sets of battery voltages.

Output:
- Test 1 (12 V, 0 V, 6 V): currents 0.949, 0.447 and 0.419 A, using 13.9 W.
- Test 2 (9 V, 0 V, 9 V): currents 0.754, 0.461 and 0.544 A, using 11.7 W.
- Test 3 (24 V, 5 V, 0 V): currents 1.902, 0.907 and 0.363 A, using 50.2 W.

Interpretation: the circuit is factored once and then solved for each test. Test 3 uses about 4 times the power of Test 1, so the resistors need to handle at least about 50 W.
