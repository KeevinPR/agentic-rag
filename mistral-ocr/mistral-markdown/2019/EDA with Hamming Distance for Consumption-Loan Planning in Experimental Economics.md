# EDA with Hamming Distance for Consumption-Loan Planning in Experimental Economics 

Yukiko Orito<br>Hiroshima University<br>Hiroshima, Japan<br>orito@hiroshima-u.ac.jp

## ABSTRACT

For the consumption-loan planning in the experimental economics, this paper proposes the EDA (Estimation of Distribution Algorithm) using Hamming distance in order to avoid convergence on a local solution. The EDA with Hamming distance restrains the quantitative change in a solution structure on the processes of EDA.

## CCS CONCEPTS

- Theory of computation $\rightarrow$ Evolutionary algorithms;


## KEYWORDS

EDA, Hamming distance, consumption-loan planning

## ACM Reference Format:

Yukiko Orito and Tomoko Kashima. 2019. EDA with Hamming Distance for Consumption-Loan Planning in Experimental Economics. In Genetic and Evolutionary Computation Conference Companion (GECCO '19 Companion), July 13-17, 2019, Prague, Czech Republic. ACM, New York, NY, USA, 2 pages.
https://doi.org/10.1145/3319619.3326788

## 1 INTRODUCTION

Consumption-loan planning is the combinatorial optimization problem which maximizes the household's utility function consisting of two kinds of decision variables, consumption variables and loan variables, under budget limitation. Izawa and Mardyla [1] designed the consumption-loan planning including various and complicated consumption items and loans as a real world application. They conducted the real effort experiment and then clarified the consumption and borrowing behaviors of subjects through the experiment. Orito et al. [2] optimized this consumption-loan planning by using the EDA. They analyzed the differences between the solutions obtained by the EDA and the behaviors obtained by the subjects on the experiment. However, some of solutions obtained by their EDA were the local solutions, not the global optimal solution. In order to improve this problem, we expand their EDA so that the quantitative change in a solution structure may be restrained.

[^0]
## Tomoko Kashima <br> Kindai University <br> Hiroshima, Japan <br> kashima@hiro.kindai.ac.jp

## 2 CONSUMPTION-LOAN PLANNING

The consumption-loan planning determines the consumption items and the loans such that the household's one-year utility maximizes. The details of the consumption-loan planning are described below.

The length of one year is set to 12 months $(t=1, \cdots, 12)$.
Income consists of monthly salaries of 160,000M (M: the experimental currency unit) and three bonus payments of 80,000 M awarded three times $(t=3,7,11)$.

Required consumption items are automatically consumed and paid every month: Rent (45,000M), Utilities (10,000M), Food \& Clothing (40,000M), and Tuition (50,000M).

Four optional consumption items are freely purchased whenever the consumer has enough currency M. Each item has the prescribed value, MU (marginal utility), according to its price. Four consumption quantity at $t$ are represented as $C_{t}^{1}$ (Movie: $3,000 \mathrm{M} / 50 \mathrm{MU}$ ), $C_{t}^{2}$ (Sports: $6,000 \mathrm{M} / 125 \mathrm{MU}$ ), $C_{t}^{3}$ (Hobby: $12,000 \mathrm{M} / 375 \mathrm{MU}$ ), and $C_{t}^{4}$ (Travel: 100,000M/ $4,500 \mathrm{MU}$ ), respectively.

The consumer can borrow three specific and one emergency rescue loan options. Three specific loans are Loan 1 (20,000M loan with $10 \%$ interest paid back on the following month), Loan 2 (30,000M loan with $13 \%$ interest paid back during the following three months), and Loan 3 (60,000M bonus loan with $18 \%$ interest paid back on the following bonus premium payday). Loan 4 (the emergency rescue loan with $23 \%$ interest paid back on the following month) automatically occurs if the consumer cannot repay the Loans 1 , 2 , and 3 by the due date. We define the following combination of binary arrays as the solution of borrowing behavior for the consumption-loan planning.

$$
\begin{aligned}
L_{t}^{j}= \begin{cases}0 & \text { Consumer does not borrow Loan } j \text { at } t \\
1 & \text { Consumer borrows Loan } j \text { at } t\end{cases} \\
\text { ( } j=1, \cdots, 4 t=1, \cdots, 12)
\end{aligned}
$$

The household's one-year utility becomes high when the consumer purchases the expensive items much. If the consumer cannot repay the loans plus interest in full by the end of the year, he/she goes bankrupt and its household's one-year utility falls to zero.

In these settings, the household's one-year utility function is defined as follows.

$$
\begin{aligned}
& \max W=\sum_{t=1}^{12}\left(\sqrt[12]{1-\gamma}\right)^{t-1} u_{t}+0.01 s_{12} \\
& u_{t}=50 C_{t}^{1}+125 C_{t}^{2}+375 C_{t}^{3}+4500 C_{t}^{4}
\end{aligned}
$$


[^0]:    Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s).
    GECCO '19 Companion, July 13-17, 2019, Prague, Czech Republic (c) 2019 Copyright held by the owner/author(s). ACM ISBN 978-1-4503-6748-6/19/07.
    https://doi.org/10.1145/3319619.3326788

![img-0.jpeg](img-0.jpeg)

Figure 1: Evaluation function obtained by the EDA with/without Hamming distance
with regard to $C_{t}^{j}$ and $L_{t}^{j} \quad(i=1 \cdots, 4, j=1, \cdots, 4)$
subject to $s_{12} \geq 0$,
where $\gamma$ is the time preference of consumer ${ }^{1}$ and $s_{t}$ is the savings at $t$. Note that the consumption quantity $C_{t}^{j}$ depends on the income and the borrowing loan $L_{t}^{j}$.

## 3 EDA WITH HAMMING DISTANCE

The consumption-loan planning given by Eq. (2) is viewed as the two-stage optimization problem for determining the consumption plan and the borrowing plan. In this paper, we optimize the borrowing plan given by Eq. (1) on the first stage of this problem. The consumption plan is optimized by the same method as [2] on the second stage. We propose the following EDA with Hamming distance so that the quantitative change in a solution structure may be restrained.

## 1. Initial State

On the initial generation, the $N_{\mathrm{p}}$ individuals (borrowing plans) are randomly generated in the population.

## 2. Making Offspring

As the offspring, the $N_{\mathrm{o}}$ individuals are randomly generated from the current population according to the probability distributions. We employ the histogram of each binarycoded variable in the individual as the probability distribution of EDA.

In addition, the $N_{\mathrm{o}}$ individuals are generated again by using the local search to keep diversity of variable values of individuals. As the operation of the local search, the selected variable in the individual changes from 0 (1) to 1 (0).

## 3. Selection Using Hamming Distance

In the operations of the selection, we adopt the evaluation function given by Eq. (2) to maximize the household's one-year utility and the Hamming distance to restrain the quantitative change in the solution structure, respectively.

It is well known that the Hamming distance measures the number of different positions between two strings of equal length. In this paper, we define the distance function which uses the Hamming distance between the current best and
each of all individuals as follows.

$$
D=\sum_{j=1}^{2} \sum_{t=1}^{12}\left|L_{t}^{j \text {,best }}-L_{t}^{j}\right|
$$

[^0]where $L_{t}^{j \text {,best }}$ is the current best in the parents' population.
We change the following two individuals, Individuals 1 and 2 , to two individuals randomly selected from parents' population except the current best.

- Individual 1

In the offspring's population, we select the individual having the smallest distance function from individuals having higher evaluation function than the current best. If there are no individuals satisfying the above conditions, we select the individual having the highest evaluation function in the offspring's population.

- Individual 2

We randomly select one individual except Individual 1 in the offspring's population.
By using this operation, we expect that the best solution on each generation is improved by the structural change as small as possible.

## 4. Termination Criterion

The operations of the EDA with Hamming distance are repeated until the maximum number of the repetitions is satisfied.

## 4 NUMERICAL EXPERIMENTS

We applied the EDA with Hamming distance to find optimal borrowing plan. We set to the parameters; Parents' population size 200; Offspring's population size 400; Generation size 100; Algorithm run 10.

For $\gamma=0.01$ in Eq. (2), the evaluation function of the optimal solution obtained by the EDA with/without Hamming distance is shown in Fig. 1.

From Fig. 1, the evaluation function obtained by the EDA with Hamming distance rises gradually. On the other hand, the evaluation function of the EDA without Hamming distance suddenly raises from the initial generation, however it converges to a local solution on the latter part of generations.

## 5 CONCLUSION

In this paper, we proposed the EDA using Hamming distance. This EDA searches the better solutions so that the quantitative change in a solution structure may be restrained. The numerical experiments showed that this EDA works well for optimizing the consumption-loan plans as compared with the conventional EDA.

## ACKNOWLEDGMENT

This work was supported by JSPS KAKENHI Grant Number \#18K11469.

## REFERENCES

[1] Hiroshi Izawa and Grzegorz Mardyla. 2011. Borrowing Behavior and Attitudes towards Risk and Time - Experimental Approach. Journal of International Finance and Economics. 11, 1 (2011), $45-54$.
[2] Yukiko Orito, Hiroshi Izawa, Grzegorz Mardyla, and Makoto Okamura. 2017. Consumption Loan Planning by Using Memetic Algorithm. Proceedings of 2017 International Conference on Intelligent Systems, Metaheuristics and Swarm Intelligence. (2017), $6-10$.


[^0]:    ${ }^{1}$ The relative value placed on a good at an earlier date compared with its value at a later date