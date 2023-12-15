# Dynamic Programming Algorithms
## Problem Definition 
<div align="justify">
The project focuses on developing an algorithm to optimize tree planting in the town of Greenvale, where each plot of land has a minimum tree requirement assigned by the Parks and Recreation Department. The goal is to find the largest possible square-shaped area of plots within the town that meets specific tree planting criteria.
<p></p>
<b> Problem 1: Maximum Square Area for Minimum Tree Requirement </b>
<p>Given a matrix p of dimensions m × n, representing the minimum number of trees required on each plot, and an integer h (positive), the algorithm aims to find the bounding indices of a square area where each plot enclosed requires a minimum of h trees to be planted.</p>

<b> Problem 2: Maximum Square Area with Corner Plot Flexibility </b>
<p>Similar to Problem 1, but with the additional flexibility that corner plots can have any number of trees required. The goal is to find the bounding indices of a square area where all but the corner plots enclosed require a minimum of h trees to be planted.</p>

<b> Problem 3: Limited Exception for Minimum Tree Requirement </b>
<p>Given the matrix p, an integer h (positive), and an additional parameter k (positive) representing the maximum number of plots that can have a minimum tree requirement of less than h, the algorithm aims to find the bounding indices of a square area meeting these criteria.</p>
</div>

## Steps to run
To execute algorithm use python3 main.py ALG#, where # is algorithm no.

For example, to execute ALG3
```
$ python3 main.py ALG3
```
## Algorithms Included

<b> For Problem 1 </b>

| Algorithm | Time Complexity | Space Complexity |
| ------- | ------- | ------- |
| ALG1 (Brute Force)   | O(m^3n^3)   | O(1)   |
| ALG2   | O(m^2n^2)   | O(1)   |
| ALG3 (Dynamic Programming)   | O(mn)   | O(mn)   |

<b> For Problem 2 </b>
| Algorithm | Time Complexity | Space Complexity |
| ------- | ------- | ------- |
| ALG4 (Dynamic Programming)   | O(mn^2)   | O(mn^2)   |
| ALG5A (Recursive)   | O(mn)  | O(mn)  |
| ALG5B (Iterative)   | O(mn)   | O(mn)   |


