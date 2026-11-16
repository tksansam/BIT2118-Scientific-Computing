# Task 12: Nonlinear Systems of Equations

Files: code/original/Task_12_nonlinear_equations.py, code/parameter_change/Task_12_nonlinear_equations_param.py, code/modified/Task_12_modified_tower_location.py

## B. Input values and operation

The program finds where the circle x^2 + y^2 = 4 meets the parabola y = x^2 - 1. scipy.optimize.root solves the two equations together, starting from the guesses (1, 1) and (-1, 1). It prints the answer and the residuals.

## C. Changing an input

I changed the circle to x^2 + y^2 = 9, so the radius is 3.

| Result | Original | After change |
|---|---|---|
| Intersection points | (1.5175, 1.3028) and (-1.5175, 1.3028) | (1.8364, 2.3723) and (-1.8364, 2.3723) |

I checked this by hand: y^2 + y - 8 = 0 gives y = 2.3723, which is the same. A bigger circle meets the parabola higher up.

## D. Meaning of the output

The two curves cross at two points that mirror each other, because both shapes are symmetrical about the y-axis. The residuals are very small and Converged is True, so the answers are accurate. Different starting guesses give different crossing points.

## E. Modified program: finding a phone using cell towers

Assumptions: tower 1 is at (0, 0) km and the phone is 5 km away from it. Tower 2 is at (8, 0) km and the phone is 6 km away from it. A third tower at (4, 6) km measures 2.4 km.

Input data: the tower positions and the distances.

Output: two possible positions were found, (3.31, 3.75) km and (3.31, -3.75) km. The first is 2.36 km from tower 3 and the second is 9.77 km away.

Interpretation: two towers leave two possible places. Only the first point agrees with tower 3, so the phone is at about (3.31, 3.75) km. This is why location systems need at least three towers or satellites.
