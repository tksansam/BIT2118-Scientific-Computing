# Task 19: Optimisation

Files: code/original/Task_19_optimization.py, code/parameter_change/Task_19_optimization_param.py, code/modified/Task_19_modified_farm_plan.py

## B. Input values and operation

A Type A server unit costs 12 and gives 100 capacity. A Type B unit costs 18 and gives 170 capacity. At least 1000 capacity is needed. The program uses minimize (SLSQP) to find the lowest cost 12x + 18y that still meets the capacity. It also checks whole-number combinations of servers.

## C. Changing an input

I changed the cost of Type B from 18 to 22.

| Result | Original | After change |
|---|---|---|
| Best plan | 0 A and 5.882 B | 10 A and 0 B |
| Lowest cost | 105.88 | 120.00 |
| Best whole-number plan | 6 B, cost 108 | 10 A, cost 120 |

What matters is the cost per unit of capacity. Before the change, B cost 0.106 per unit and A cost 0.120, so B was cheaper. Now B costs 0.129, so A is cheaper. The answer jumped from all B to all A.

## D. Meaning of the output

The cheapest choice is to use only Type B. Since servers come in whole numbers, the real plan is 6 Type B servers, costing 108 and giving 1020 capacity.

## E. Modified program: farm plan for maize and beans

Assumptions:
- A farmer has 10 acres. Each acre of maize makes KES 30,000 profit and each acre of beans makes KES 42,000.
- Maize needs 10 days of labour per acre and beans need 20. There are 160 days of labour.
- The fertiliser budget is KES 52,000.
- At least 3 acres must be maize.

I scaled the money to thousands of shillings because the first run failed when the numbers were very different in size.

Input data: profits, labour, fertiliser cost and the land limit.

Output: plant 4 acres of maize and 6 acres of beans, for a profit of KES 372,000. All the land and all the labour are used. Only KES 48,000 of the fertiliser budget is used.

Interpretation: land and labour are what limit the profit, not fertiliser. Getting more workers would help more than buying more fertiliser.
