# Task 9: Eigenvalues

Files: code/original/Task_09_eigenvalues.py, code/parameter_change/Task_09_eigenvalues_param.py, code/modified/Task_09_modified_market_share.py

## B. Input values and operation

The input is the adjacency matrix of a small network with nodes A, B, C and D, where 1 means two nodes are connected. np.linalg.eig finds the eigenvalues and eigenvectors. The eigenvector of the largest eigenvalue is scaled so that it adds up to 1, and it is used as the importance score of each node. The program checks the result using Av - lambda v.

## C. Changing an input

I added a new link between A and D.

| Result | Original | After change |
|---|---|---|
| Largest eigenvalue | 2.5616 | 3.0 |
| Importance A, B, C, D | 0.219, 0.281, 0.281, 0.219 | 0.25 for all |

After the change every node has 3 connections. When all nodes have the same number of links, the largest eigenvalue equals that number (3), and all the nodes are equally important.

## D. Meaning of the output

B and C are the most important nodes because they connect to every other node. A and D only have 2 links each. The very small verification error shows the eigenvalue and eigenvector are correct. If B or C failed, the network would be affected the most.

## E. Modified program: market share of mobile networks

Assumptions: three mobile networks (X, Y and Z) lose and gain customers each month. For example, 90% of X's customers stay with X each month. These rates are made up. The long-term market share is the eigenvector for eigenvalue 1.

Input data: a 3 by 3 switching matrix whose columns each add up to 1.

Output: the eigenvalues are 1, 0.815 and 0.815. In the long run X has 45.19%, Y has 32.07% and Z has 22.74%. Running the model for 60 months from 30%, 40% and 30% gave the same shares.

Interpretation: if customers keep switching at these rates, X will end up with about 45% of the market whatever the starting shares are. The second eigenvalue (0.815) shows how fast the market settles. It is small enough that 60 months is plenty.
