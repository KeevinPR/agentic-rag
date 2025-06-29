# AN ESTIMATION OF DISTRIBUTION ALGORITHM FOR THE CHANNEL ASSIGNMENT PROBLEM 

Jayrani Cheeneebash<br>Department of Mathematics, University of Mauritius, Reduit, Mauritius

Harry C. S. Rughooputh<br>Department of Electrical and Electronic Engineering, University of Mauritius, Reduit, Mauritius

Keywords: Channel Assignment problem, Estimation of Distribution Algorithm.

Abstract: The channel assignment problem in cellular radio networks is known to belong to the class of NP-complete optimisation problems. In this paper we present a new algorithm to solve the Channel Assignment Problem using Estimation of Distribution Algorithm. The convergence rate of this new method is shown to be very much faster than other methods such as simulated annealing, neural networks and genetic algorithm.

## 1 INTRODUCTION

During the recent years, it has been observed that the improved portability and widespread of communication systems has accentuated the demand for mobile users. However, since the number of usable frequencies, which are necessary for the communication between mobile users and the base stations of cellular radio networks, is very limited, an efficient use of the frequency spectrum or channels is crucial to meet the increasing demands. Therefore while assigning the frequencies to different base stations, it is desirable to reuse the same frequency as much as possible. On the other hand, it is important to avoid possible interferences between different mobile users, at the same time, the number of frequencies assigned to each base station must be chosen large enough to satisfy the given demand in the corresponding cell. Regarding the above requirements, one can formulate the frequency assignment, problem as a discrete optimisation problem.

The channel assignment problem (CAP) is defined as an NP-complete problem. The channel assignment must fulfil the following three constraints:(Sivaranjan, McElliece and Ketchum, 1986)

1. The Co-Channel Constraint (CCC): The same channel cannot be assigned to a pair of cells within a specified distance simultaneously.
2. The Adjacent Channel Constraint (ACC): Adjacent Channels cannot be assigned to cells simultaneously.
3. The Co-site Constraint (CSC): The distance by an $n \times n$ symmetric matrix called the compatibility matrix between any pair of channels used in the same cell must be larger than a specified distance.
In 1982, Gamst and Rave defined the general form of the channel assignment problem in an arbitrary inhomogeneous cellular radio network (Gamst, 1982). In their definition, compatibility constraints in an $n$-cell network are described $C=\left[c_{i j}\right]$. Each non-diagonal element $c_{i j}$ in $C$ represents the minimum separation distance in the frequency domain between a frequency assigned to cell $i$ and a frequency to cell $j$. The Co-Channel constraint is represented by $c_{i j}=1$, the adjacent channel constraint is represented by $c_{i j}=2$ and $c_{i j}=0$ indicates that cells $i$ and $j$ are allowed to use the same frequency. Each diagonal element $c_{i i}$ in $C$ represents the minimum separation distance between any two frequencies assigned to cell $i$, which is the co-site constraint, where $c_{i i} \geq 1$ is always satisfied.

The channel requirements for each cell in an $n$-cell network are described by an $n$ element vector which is called the demand vector $D$. Each element $d_{i}$ in $D$ represents the number of frequencies to be assigned to cell $i$. When $f_{i k}$ indicates the $k^{\text {th }}$ frequency assigned to cell $i$, the compatibility constraints are represented by:

$$
\left|f_{i k}-f_{j l}\right| \geq c_{i j} \quad \text { for } i, j=1, \ldots, n
$$

$k=1, \ldots, d_{i}, l=1, \ldots, d_{j}$ except for $i=j, k=l$.
Many researchers have investigated the channel assignment problem using non-iterative algorithms (Gamst and Rave, 1982), (Sivaranjan, McElliece and Ketchum1981) and iterative algorithms (Funabiki and Takefyi, 1992), (Kunz, 1991). Neural Networks Algorithms and Genetic Algorithms are among the iterative algorithms in which an energy or cost function representing frequency separation constraints and channel demand is formulated and is then minimised. Unfortunately, the minimisation of the cost function is quite a difficult problem because of the danger of getting stuck in local minima constitutes a major problem. A much more powerful approach to cope with the problem of local minima has been considered in (Beckmann and Killat, 1999), (Fu, Pan and Bourgeois, 2003).

This paper is organised as follows: section 2 gives a brief exposé on Estimation of Distribution Algorithms and section 3 presents the new method that we propose in this paper. In section 4 we show the performance of our algorithms in solving some benchmark problems and finally we conclude in section 5 .

## 2 SEARCH AND OPTIMISATION ALGORITHMS

Genetic Algorithm (GA) depends to a large extent on associated parameters like operators and probabilities of crossing and mutation, size of population, rate of generational reproduction, and the number of generations. The researcher requires experience in the resolution and use of those algorithms in order to choose suitable values for these parameters. All these reasons have motivated the creation of a new class of evolutionary algorithms classified under the name of Estimation of Distribution Algorithms (EDAs) (Larranaga and Lozano, 2002), which attempts to ease the prediction the movements of the population in the search space as well as to avoid the need of so many parameters. EDAs are population based search algorithms based
on probabilistic modelling. The new individuals are sampled starting from a probability distribution estimated from the database containing only selected individuals from the previous generation. The interrelations between the different variables representing the individuals are expressed explicitly through the joint probability, associated with the individuals selected at each iteration.

Given the population of the $l$ th generation, $P_{l}$, the $N$ selected individuals, $P_{l}^{S e}$, constitute a data set of $N$ cases of $X=\left(X_{1}, X_{2}, \ldots, X_{n}\right)$. Denoting the joint probability distribution of $X$ by $\rho(x)=\rho(X=x)$. EDAs estimate $\rho(x)$ from $P_{l}^{S e}$. The pseudo-code of EDA is as follows (Larranaga and Lozano, 2002):

1. $P_{0} \leftarrow$ Generate $M$ individuals (the initial population) randomly.
Repeat for $l=1,2, \ldots$ until a stopping criteria is met.
2. $P_{l-1}^{S e} \leftarrow$ Select $N \leq M$ individuals from $P_{l-1}$ according to a selection method.
3. $\rho_{l}(x)=\rho\left(x \mid P_{l-1}^{S e}\right) \leftarrow$ Estimate the probability distribution of an individual being among the selected individuals.
4. $P_{l} \leftarrow$ Sample $M$ individuals (the new population from $\rho_{l}(x)$.
In the above pseudo-code of EDA there are four main steps:
(i) The first population $P_{0}$ of M individuals is generated, usually by assuming a uniform distribution (either discrete or continuous) on each variable, and evaluating each of the individuals.
(ii) A number $N(N \leq M)$ of individuals are selected, usually the fittest.
(iii) Thirdly, the $n$-dimensional probabilistic model that better expresses the interdependencies between the $n$ variables is induced.
(iv) The new population of $M$ new
individuals is obtained by simulating the probability distribution learnt in the previous step.
Steps (ii), (iii) and (iv) are repeated until a stopping condition is verified. The most important step is to find the interdependencies between the variables (step (iii)), and this is

done using techniques from probabilistic graphical models.

## 3 A NEW APPROACH

From literature review, it is known that call orderings and minimisation of cost functions have been used in solving the frequency assignment problem (Kunz, 1991), (Sivaranjan, McElliece and Ketchum,1986). It has been noticed that the advantages of the method using call orderings correspond to the disadvantages of the cost minimising approaches and vice-versa. Using the idea of Beckmann in (Beckmann and Killat, 1999), we combine the two methods so as to gain their advantages. We propose to use EDA to solve combinatorial optimisation problems for the determination of an optimal satisfying call list $L$ and assign the frequencies using FEA (Beckmann and Killat, 1999); this assures that in contrast to all existing cost-minimising methods, we only get legal frequencies without any interferences. This strategy derives only channel allocations which do not violate any of the interference constraints during the search process which leads to a desirable reduction of the search space. In our method the main optimisation work with EDA is done to search for an optimal frequency assignment.
![img-0.jpeg](img-0.jpeg)

Figure 1: New Method.
Our method is summarised in Figure 1. It can be seen that new call lists are generated by the EDA. The FEA strategy is used to evaluate the quality of the generated call list $L$. This means that for each single call list $L$ we apply the FEA strategy in order to determine the number of calls without an allocated frequency; in other words we check how many calls have been assigned a proper frequency without violating the interference constraints; such calls are known as blocked calls denoted by $b$. A
low value of $b$ then corresponds to a high solution quality. Then EDA is used to generate new, hopefully better call lists during the next iteration. This process is then repeated until the application of the FEA strategy to a proper call list leads to a frequency assignment with the desired minimum frequencies.

We now describe how EDA is applied to solve the channel assignment problem. First, an initial population of randomised solution vectors are generated. Each vector is then evaluated using FEA. The solution vector is then sorted out with respect to the number of blocked calls and half of the best solutions is retained. We then estimate the probability distribution of an individual being among the selected individuals and then sample a new population with the same number of individuals so as to keep the number of individuals in the population same. The described procedure is repeated until we get a solution of the desired quality or the maximum number of iterations is reached.

## 4 SIMULATION RESULTS

The algorithm described in section 3 has been applied to the well known benchmark problem, that is, the 21-cell system shown in Figure 2. This special example which has been dealt by many researchers working in the field of frequency assignment, allows us to compare the results obtained from the new algorithm with published results. Different set of problems have been considered by choosing different demand vectors
$D 1$ and $D 2$ as shown in Table 1 and different interference conditions summarised in Table 2.
![img-1.jpeg](img-1.jpeg)

Figure 2: Cells Layout.

Table 1: Frequency Demand Vectors D1 and D2.

|  | $\mathrm{d}_{1}$ | $\mathrm{~d}_{1}$ | $\mathrm{~d}_{2}$ | $\mathrm{~d}_{3}$ | $\mathrm{~d}_{4}$ | $\mathrm{~d}_{5}$ | $\mathrm{~d}_{6}$ | $\mathrm{~d}_{7}$ | $\mathrm{~d}_{8}$ | $\mathrm{~d}_{9}$ | $\mathrm{~d}_{10}$ | $\mathrm{~d}_{11}$ | $\mathrm{~d}_{12}$ | $\mathrm{~d}_{13}$ | $\mathrm{~d}_{14}$ | $\mathrm{~d}_{15}$ | $\mathrm{~d}_{16}$ | $\mathrm{~d}_{17}$ | $\mathrm{~d}_{18}$ | $\mathrm{~d}_{19}$ | $\mathrm{~d}_{20}$ | $\mathrm{~d}_{21}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| D1 | 8 | 25 | 8 | 8 | 8 | 15 | 18 | 52 | 77 | 28 | 13 | 15 | 31 | 15 | 36 | 57 | 28 | 8 | 10 | 13 | 8 |  |
| D2 | 5 | 5 | 5 | 8 | 12 | 25 | 30 | 25 | 30 | 40 | 40 | 45 | 20 | 30 | 25 | 15 | 15 | 30 | 20 | 20 | 25 |  |

Table 2: Interference Conditions.

| Problem Case | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $\mathrm{~N}_{\mathrm{c}}$ | 7 | 7 | 7 | 12 | 12 | 7 | 7 | 7 | 7 | 12 | 12 | 7 |
| ACC | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 2 |
| $\mathrm{c}_{\mathrm{u}}$ | 5 | 7 | 7 | 5 | 7 | 5 | 5 | 7 | 7 | 5 | 7 | 5 |

To evaluate the performance of the new algorithm, we solve the problem with 50 different seed values. We choose a maximum of 25 iterations to stop the algorithm if no solution is obtained. At each iteration only half of the best solutions are retained and a new population is sampled. Each problem case was run 20 times from the different initial seed values from random generators and the average generation number is shown in Table 3. To evaluate the performance of the new algorithm, we solve the above mentioned problem with 50 different seed values. Convergence rate is an important factor to compare the efficiency of a method which is shown in Table 3. Problems 3 and 9, converge in only one generation, this result is comparable to that obtained in (Beckmann and Killat, 1999). The other problem cases converge in average of two iterations.

Table 3: Average Number of Generations.

| Problem Case | Ave Gen Num |
| :-- | :-- |
| 1,5 | 1.7 |
| $2,4,6,7$ | 1.6 |
| 3,9 | 1 |
| 8,10 | 1.55 |
| 11 | 1.75 |
| 12 | 1.6 |

## 5 CONCLUSION

In this paper we have presented a new method to solve the frequency assignment problem, which is a blend of the frequency exhaustive strategy and EDA. Our results show that EDA can be applied for solving the channel assignment problem in mobile cellular environment. EDA has an advantage over other methods like Neural Networks and Genetic Algorithms in terms of rapid convergence to the optimal solution. Hence the new algorithm presented in this paper seems promising in solving the CAP problem.

## REFERENCES

Beckmann, D. and Killat, U., 1999. A new strategy for the application of genetic algorithms to the channel assignment problem, IEEE Trans Veh Tech. Vol. 48, No. 4, , pp. 1262-1269.
Funabiki, N. and Takefyi, Y., 1992. A neural network parallel algorithm for channel assignment in cellular radio networks, IEEE Trans Veh Tech. Vol. 41, , pp. 430-437.
Gamst, A. and Rave, W., 1982. On frequency assignment in mobile automatic telephone systems, Proceedings of GLOBECOM'82. IEEE, pp. 309-315.
Gamst, A., 1986. Some Lower bounds for a class of frequency assignment problems, IEEE Trans Veh Tech. Vol. 35, , pp. 8 - 14.
Kim, J. S., Park, S., Dowd, P. and Nasrabadi, N., 1996. Channel Assignment in Cellular Radio using Genetic Algorithm, Wireless Personnel Communications. Vol. 3, , pp. 273-286.
Kunz, D., 1991, Channel Assignment for cellular radio using neural networks, IEEE Trans Veh Tech. Vol. 40, , pp. 188-193.
Larranaga, P. and J. A. Lozano., 2002. Estimation of Distribution Algorithms; A new tool for Evolutionary Computation, Kluwer Academic.
Sivaranjan, K. N., McEllieee, R. J and Ketchum, J. W., 1986. Channel Assignment in cellular radio. Proceedings $39^{\text {th }}$ IEEE Veh Tech Conference., pp. 846-850.
Fu, X., Pan, Y. and Bourgeois, A., 2003. A three stage Heuristic combined Genetic Algorithm Strategy to the channel assignment problem. Proceedings of the International Parallel and Distributed Processing Symposium., pp. 145b.