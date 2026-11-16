# Task 16: Numerical Integration

Files: code/original/Task_16_numerical_integration.py, code/parameter_change/Task_16_numerical_integration_param.py, code/modified/Task_16_modified_land_area.py

## B. Input values and operation

A smart meter records power (kW) every 2 hours for 12 hours. Energy is the area under the power curve. The program finds this area with the trapezoidal rule, which joins the points with straight lines, and with Simpson's rule, which uses curves.

## C. Changing an input

I used readings every 4 hours instead of every 2 hours.

| Result | Every 2 hours | Every 4 hours |
|---|---|---|
| Trapezoidal | 15.700 kWh | 15.400 kWh |
| Simpson | 15.800 kWh | 15.967 kWh |
| Difference | 0.100 kWh | 0.567 kWh |

With fewer readings, the two methods disagree much more, because we know less about what happened between readings. More frequent readings give a more reliable answer.

## D. Meaning of the output

The house used about 15.7 to 15.8 kWh of electricity in 12 hours. The two methods are only 0.1 kWh apart, so the answer can be trusted. At an example price of KES 25 per kWh, this would cost about KES 395.

## E. Modified program: area of a piece of land

Assumptions: a surveyor measures the width of a plot that runs along a river every 10 m along a 120 m straight line.

Input data: 13 widths, from 0 m to 31 m.

Output: the trapezoidal rule gave 2,663.0 square metres (0.658 acres). Simpson's rule gave 2,695.3 square metres (0.666 acres). The difference is 1.2%.

Interpretation: the plot is about two thirds of an acre. Simpson's rule follows the curved river side better, so I would use its answer.
