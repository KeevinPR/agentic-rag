# Estimation of Distribution Algorithm Based on Lévy Flight for Solving the Set-Union Knapsack Problem 

XUE-JING LIU ${ }^{\oplus}$ AND YI-CHAO HE<br>College of Information and Engineering, Hebei GEO University, Shijiazhuang 050031, China<br>Corresponding author: Xue-Jing Liu (lxjpass@163.com)

This work was supported in part by the National Natural Science Foundation of China under Grant 61806069, in part by the Scientific Research Project Program of Colleges and Universities in Hebei Province under Grant QN2019075, in part by the Scientific Research Project Program of Colleges and Universities in Hebei Province under Grant ZD2016005, and in part by the Natural Science Foundation of Hebei Province under Grant F2016403055.


#### Abstract

This article investigates how to use the estimation of distribution algorithm based on Lévy flight to solve the set-union knapsack problem (SUKP). First, the mathematical model of the SUKP is introduced. Then, a quadratic greedy repair and optimization algorithm (Q-GROA), which deals with infeasible solutions, is proposed. Thereby, a new approach, the estimation of distribution algorithm based on Lévy flight (LFEDA) combined with the Q-GROA is also proposed to solve the SUKP. A number of experiments are performed on the SUKP datasets to evaluate the performance of our proposed model. The results verify that the proposed method is significantly better than other algorithms with respect to the solution's performance.


#### Abstract

INDEX TERMS Set-union knapsack problem, estimation of distribution algorithm, Lévy flight, repair and optimization.


## I. INTRODUCTION

The $0-1$ knapsack problem ( $0-1 \mathrm{KP}$ ) [1] is a classic NP-hard problem; it has important applications in project selection, cargo loading, investment decision-making and so on. The $0-1 \mathrm{KP}$ is as follows: given $n$ items, where the item $i(1 \leq i \leq n)$ has weight $w_{i}$ and profit $p_{i}$, and a knapsack with capability $C$, the $0-1 \mathrm{KP}$ describes packing a number of items into the knapsack without exceeding the capability $C$, so that the items in it have the maximal value among all possible combinations.

The set-union knapsack problem (SUKP) [2]-[5], which is a variation of the $0-1 \mathrm{KP}$ [1], is an NP-complete problem, and it has important applications in many fields such as machine loading in flexible manufacturing systems [2]-[4], the allocation of storage to fields in a database [4], data stream compression and smart cities. First, Goldschmidt et al. [2] studied the SUKP and proposed a dynamic program running in exponential time to solve it exactly, but the dynamic program is not applicable to this problem. Arulselvan and

[^0]Ashwin [4] presented an approximation algorithm named the A-SUKP for solving the SUKP with the additional restriction that the A-SUKP approximates a special case of the SUKP within a constant factor, and the A-SUKP greatly improved the speed for solving the SUKP. Then, He et al. [5] proposed a novel binary artificial bee colony algorithm (BABC) with the greedy repair and optimization algorithm (S-GROA) for solving the SUKP, and the BABC provides a new idea for solving the SUKP using evolutionary algorithms (EAs). Baykasoğlu et al. [6] used the binary weighted superposition attraction algorithm (bWSA) to solve the SUKP. At present, the SUKP is a hotspot of KP problems, and there are fewer EAs to solve it. Therefore, estimation of distribution algorithms (EDAs) [7]-[9] are a trending research topic in the field of evolutionary computations and will be explored to solve the SUKP.

EDAs are new stochastic optimization algorithms based on statistical principles, which explore the space of potential solutions by establishing a probabilistic model and sampling the candidate solutions based on the model. The explicit application of probabilistic models in optimization provides more important advantages than other types of


[^0]:    The associate editor coordinating the review of this manuscript and approving it for publication was Hisao Ishibuchi.

metaheuristics. At present, the related theoretical research of EDAs has achieved many results, and EDAs have good optimization performance in many fields, including combinatorial problems, pattern matching, secondary distributions, mechanical structure design, numerical optimization problems and so on. Population-based incremental learning (PBIL) is the earliest EDA model [10]. EDAs were first proposed in 1996 [7] and had been rapidly developed over the following years. Hauschild and Pelikan [11] discussed the advantages of EDAs using probability models over other types of metaheuristics and outlined many different types of EDAs. Pelikan et al. [12] proposed a Bayesian optimization algorithm based on EDAs. Aickelin et al. [13] used EDAs to implement the explicit learning of rule-based nurse scheduling, and an ant-miner method was used to improve each solution that was generated in each generation. Zhang et al. [14] proposed multi-objective EDAs based on the rule model for the variable links of continuous multi-objective optimization problems. Chang et al. [15] used three mechanisms to effectively combine particle swarm optimization with EDAs, and proposed a new particle swarm EDA framework that retained the original unique functions of the two algorithms. A new type of EDA was proposed to solve a special kind of nonlinear bilevel programming problem [16]. Ceberio et al. [17] proposed a hybrid method consisting of an EDA and a variable neighborhood search to solve the problem of flow shop scheduling. Inspired by the organization and division of the bee colony, Novais et al.[18] used a clustering method in the target space and combined the EDAs to propose a hybrid multi-objective estimation distribution algorithm based on an artificial bee colony and clustering to solve continuous variables. Luo et al. [19] divided the particle swarm into several subgroups and built a probability model for each subgroup based on the EDAs to solve the complex multi-objective optimization problem of reservoir flood control operations. Alden and Miikkulainen [20] introduced a Markovian learning EDA by employing a Markov random field model, and applied it in computational biology and autonomous agent design. PérezRodríguez and Hernández-Aguirre [21] combined EDAs and the Mallows distribution in order to build better sequences for flexible job shop scheduling problems with process plan flexibility. Min et al.[22] used the Monte Carlo method and transfer learning technique to propose a domain EDA based on domain adaptation and nonparametric estimation to solve the dynamic multi-objective optimization problem. Based on Pareto EDAs, Shao et al. [23] constructed three probability models to solve the multi-objective distributed no-wait flow shop scheduling problem with the sequence correlation setup time and achieved better results. While EDA applications have been very extensive and achieved certain results, they are less frequently applied to the knapsack problem; therefore, this paper will study EDAs to solve the SUKP problem.

The remainder of this paper is organized as follows. In section II, the definition and the mathematical model of the SUKP are introduced. Section III introduces EDAs. In the following section, Lévy flight is reviewed, and an efficient quadratic greedy repairing and optimization algorithm (Q-GROA) that can deal with the infeasible solution of the SUKP is presented. Subsequently, we applied Lévy flight and the Q-GROA to EDAs (named LFEDAs) to form a new approach for solving the SUKP. In section V, a large-scale comparison between LFEDAs and other methods including the A-SUKP, binary differential evolution (binDE) [24], BABC [5], binary weighted superposition attraction (bWSA) [6] and EDAs for solving three real-world problems is conducted, and the experimental results show that LFEDAs are superior to other algorithms with respect to efficiency and performance. We summarize our results and suggest future research directions in section VI.

## II. DEFINITION AND MATHEMATICAL MODELS

The SUKP [2],[3],[5] contains a set of items $S=\{1,2, \ldots, m\}$ and a set of elements $U=\{1,2, \ldots, n\}$. Each item $i(i=1,2, \ldots, m)$ has a nonnegative value $p_{i}$ corresponding to a subset of elements, and each element $j(j=1,2, \ldots, n)$ has a nonnegative weight $w_{j}$. For a nonempty set $A \subseteq S$, the weight of set $A$ is $W(A)=\sum_{j \in \bigcup_{i \in A} U_{i}} w_{j}$ and the profit of set $A$ is $P(A)=\sum_{i \in A} p_{i}$. Finding a subset $S^{*} \subseteq S$ is the purpose of the SUKP, which will maximize $P\left(S^{*}\right)$ and meet the conditions $W\left(S^{*}\right) \leq C$, where $C$ is a nonnegative value and is the given capacity of the knapsack. Without loss of generality, the SUKP can be expressed as follows:

$$
\begin{array}{ll}
\text { maximize } & P(A)=\sum_{i \in A} p_{i} \\
\text { subject to } & W(A)=\sum_{j \in \bigcup_{i \in A} U_{i}} w_{j} \leq C, \quad A \subseteq S
\end{array}
$$

The above mathematical model cannot be solved using EAs. Therefore, an integer model based on the above model is introduced, which is easier for EAs.

Let $A_{X}=\left[i \mid x_{i} \in \boldsymbol{X}, x_{i}=1, i=1,2, \ldots, m\right] \subseteq S$, where $\boldsymbol{X}=\left[x_{1}\right.$, $\left.x_{2}, \ldots, x_{m}\right] \in\{0,1\}^{m}$ is an $m$-dimension $0-1$ vector. Obviously, the relationship between $\boldsymbol{X}$ and $A_{X} \subseteq S$ is a one-toone mapping. Through this one-to-one mapping relationship, the SUKP can be modeled as follows:

$$
\begin{gathered}
\operatorname{maximize} f(\boldsymbol{X})=\sum_{i=1}^{m} x_{i} p_{i} \\
\text { subject to } W\left(A_{X}\right)=\sum_{j \in \bigcup_{i \in A} U_{i}} w_{j} \leq C \\
X=\left[x_{1}, x_{2}, \ldots, x_{m}\right] \in\{0,1\}^{m}
\end{gathered}
$$

According to the model above, all $0-1$ vectors of $\boldsymbol{X}$ are the only potential solutions of the SUKP, and only the solutions that satisfy the limit condition (4) and (5) are the feasible solutions.

## III. ESTIMATION OF DISTRIBUTION ALGORITHMS

EDAs are EAs that are stochastic optimization algorithms. They explore the space of potential solutions by using the constructed explicit probabilistic model to find the most promising solution. In EDAs, there is no traditional crossover or mutation. Usually, EDAs start with the initial population that is generated based on a uniform distribution in the

solution space. Then, the population is evaluated using the fitness function, and the population is sorted according to the fitness function. For example, from the sorted population, when we use $60 \%$ as the selection operator, the subset of the top $60 \%$ best solutions is selected. The probabilistic model is constructed using the selected solution method in order to estimate the probability distribution of the solution. Once a probabilistic model has been established, some new solutions can be sampled based on this probabilistic model and a new population can be generated. Until the termination conditions are met, we repeat this process, and each iteration is usually called a generation of the EDAs. The basic procedure of EDAs is shown in Algorithm 1. Here, $N P$ is the population size, $\boldsymbol{X}$ is the $n$-dimensional vector, Miter is the maximum number of iterations, $P_{m}$ is the selection factor, $\boldsymbol{B}$ is the optimal solution, and the function $f$ is the fitness value.

```
Algorithm 1 EDAs Pseudocode
    Input: parameters \(N P\), Miter, \(P_{m}, t\)
    Output: \(\boldsymbol{B}\) and \(f(\boldsymbol{B})\)
    1) generate initial population \(P(0)=\left\{X_{k}(0) \mid 1 \leq k \leq N P\right\}\)
    randomly;
    2) compute fitness \(f(P(0))\);
    3) for \(t \leftarrow 1\) to Miter
    4) \(\operatorname{sort} P(t)\) by \(f(P(t))\);
    5) generate the selection population \(S(t)\) from \(P(t)\) using
        the selection operator \(P_{m}\);
    6) build probabilistic model \(M(t)\) from \(S(t)\);
    7) generate new feasible solutions \(P^{\prime}(t)\) by sampling
        \(M(t)\);
    8) generate new \(P(t)\) by \(P^{\prime}(t)\) and \(P(t)\);
    9) calculate \(\boldsymbol{B}\) and \(f(\boldsymbol{B})\);
    10) end for
    11) return \(\boldsymbol{B}\) and \(f(\boldsymbol{B})\).
```

An important step in distinguishing EDAs from many other metaheuristic methods is the construction of the model and the attempt to capture the probability distribution of a promising solution. This task is not trivial because the goal is not a perfect representation of a promising solution for the population, but rather a more general distribution that captures the functionality of the chosen solution and makes it better than any other candidate. In addition, we must ensure that models are efficiently built and sampled.

## IV. EDAS BASED ON LÉVY FLIGHT

## A. LÉVY FLIGHT

The Lévy distribution is a probability distribution [25] that was proposed by the French mathematician Lévy in the 1930s. As a random movement, Lévy flight is an alternate way of walking with a short distance search combined with occasional longer distance walking [26], which is a random search path that obeys a Lévy distribution. So far, scholars have proven that the foraging trajectory of many animals and insects in nature, such as albatrosses, bees and fruit flies,
conform to a Lévy distribution (Lévy flights) pattern. Lévy flight can increase the diversity of the population and broaden the scope of the search, which makes it is easier to jump out of local optimal points in the intelligent optimization algorithm.

The Lévy flight location update formula is as follows [27]:

$$
\boldsymbol{X}_{i}^{t+1}=\boldsymbol{X}_{i}^{t}+\alpha \oplus \operatorname{Levy}(\lambda), \quad i=1,2, \ldots, n
$$

where $\boldsymbol{X}_{i}$ is the position of the $i$-th individual, $\boldsymbol{X}_{i}^{t}$ represents $\boldsymbol{X}_{i}$ 's t generation position, $\oplus$ is point-to-point multiplication, $\alpha$ represents the step control amount, and Lévy $(\lambda)$ is a random search path. The latter satisfies the following:

$$
\text { Lévy } \sim u=t^{-\lambda}, \quad 1<\lambda \leq 3
$$

At present, Lévy flight has been applied to firefly algorithms (FAs) [27], [28], moth search algorithms (MSAs) [29], cuckoo search (CS) [30] and many state-of-the-art algorithms because Lévy flight significantly improves the search ability of metaheuristic algorithms.

## B. QUADRATIC GREEDY REPAIRING AND OPTIMIZATION

The SUKP is a constrained optimization problem that will definitely generate infeasible solutions when metaheuristic algorithms are used to solve it. Because infeasible solutions reduce the effectiveness of the algorithm, how to deal with infeasible solutions is the key problem that needs to be solved. The most common methods for dealing with infeasible solutions are the repair approach, the penalty function approach, the purist approach, the separation method and the hybrid approach [31], [32]. They have their own advantages and disadvantages for the general constrained optimization problem, but for the $0-1 \mathrm{KP}$, Michalewicz [33] showed that the repair approach is more suitable than any other approach to address nonfeasible solutions. He et al. [5], [34] proposed a repair and optimization algorithm for solving the infeasible solutions of randomized time varying knapsack problems, the discount $\{0-1\}$ knapsack problem (D $[0-1] \mathrm{KP}$ ) and the SUKP. On the basis of the S-GROA [5], Q-GROA is proposed to handle the infeasible solutions of the SUKP.

According to the SUKP, suppose that $c_{i}(0<=c_{i}<=m)$ $(i=1,2, \ldots, n)$ counts the number of occurrences of the element $i(i \in U)$ in the subsets $U_{1}, U_{2}, \ldots, U_{m}$. Let $W_{-} N_{j}=\sum_{i \in U_{j}}\left(w_{i} / c_{i}\right)(j=1,2, \ldots, m)$. Let $H[1 \ldots m]$ be the descending subscript order in which the Quicksort algorithm is employed to sort all items in $S$ in descending order according to $p_{j} / W_{-} N_{j}(j=1,2, \ldots, m)$. For an arbitrary $m$ dimensional $0-1$ vector $\boldsymbol{Y}=\left[y_{1}, y_{2}, \ldots, y_{m}\right] \in\{0,1\}^{m}$, we simplify the notation as $\boldsymbol{A}_{\boldsymbol{Y}}=\left\{i \mid y_{i} \in \boldsymbol{Y} \&\& y_{i}=1,1 \leq i \leq m\right\}$. The detailed steps of the Q-GROA are shown in Algorithm 2.

In the Q-GROA, the Quicksort algorithm's time complexity is $O(m \log m)$, where step 1 calculates the parameters $c_{i}(i=1,2, \ldots, n), W_{-} N_{j}(j=1,2, \ldots, m)$ and $H[1 \ldots m]$, and the time complexity is $O(m \log m)+O(m n)$. Step 2 assigns 0 to the potential solution $Y$, and the time complexity is $O(m)$. A repair stage (steps 3 to 7 ) is used to obtain a preliminary feasible solution, and the time complexity is $O(m n)$. Without considering the elements that have been

## Algorithm 2 Q-GROA

Input: $\boldsymbol{X}=\left[x_{1}, x_{2}, \ldots, x_{m}\right] \in\{0,1\}^{m}$
Output: $\boldsymbol{Y}=\left[y_{1}, y_{2}, \ldots, y_{m}\right] \in\{0,1\}^{m}, f(\boldsymbol{Y})$

1) calculate $c_{i}(i=1,2, \ldots, n), W_{-} N_{j}(j=1,2, \ldots, m)$ and $H[1 \ldots m]$
2) for $i=1$ to $m$ do $y_{i}=0$ endfor
3) for $i=1$ to $m$ do
4) if $\left(x_{H[i]}=1 \& \& W\left(A_{Y} \cup\{H[i]\}\right) \leq C\right)$ then
5) $y_{H[i]}=1, A_{Y}=A_{Y} \cup\{H[i]\}$
6) endif
7) endfor
8) do not consider the elements that have been added to the knapsack, recalculate $c_{i}(i=$ $1,2, \ldots, n), W_{-} N_{j}(j=1,2, \ldots, m)$ and $H[1 \ldots m]$
9) for $i=1$ to $m$ do
10) if $\left(x_{H[i]}=0 \& \& W\left(A_{Y} \cup\{H[i]\right\} \leq C\right)$ then
11) $y_{H[i]}=1, A_{Y}=A_{Y} \cup\{H[i]\}$
12) endif
13) endfor
14) $\operatorname{return}(\boldsymbol{Y}, f(\boldsymbol{Y}))$
added to the knapsack (step 8), the frequencies of the items that are not included in the knapsack and the weight of each item after the correction are recalculated, and quicksort is used to reassign $H[1 \ldots m]$ with a time complexity of $O(m \log m)+O(m n)$. In the optimization phase (steps 9 to 13), the feasible solution $\boldsymbol{Y}$ is further optimized and the feasible solution is obtained with a time complexity of $O(m n)$. Therefore, the total time complexity is $O(m \log m)+O(m n)+O(m)+$ $O(m n)+O(m \log m)+O(m n)+O(m n)=O(m n)$. Obviously, the Q-GROA is an efficient method for handling the infeasible solutions of the SUKP.

## C. APPLICATION OF EDAS BASED ON LÉVY FLIGHT TO SUKP

In this section, the Q-GROA and Lévy flights are applied to EDAs for the SUKP in order to deal with infeasible solutions and increase the diversity of solutions. Therefore, Algorithm 1 needs to be further modified in the following three aspects.
(1) Before generating the initial population, according to $p_{j} / W_{-} N_{j}(j=1,2, \ldots, m)$, all items in $S$ are sorted in descending order, and the index of each ordering item is stored in array $H[1 \ldots m]$.
(2) To increase the diversity of the population, the Lévy flight strategy is introduced with a flight probability of $\alpha$ when generating new populations.
(3) The Q-GROA is used to repair and optimize the potential solutions that are generated in every iteration, and the output of the objective function of the feasible solutions is considered the fitness.

The detailed steps of the EDAs based on Lévy flight (LFEDAs) for the SUKP are shown in Algorithm 3.

To show the LFEDAs more clearly, a flowchart is shown in Fig. 1.

## Algorithm 3 LFEDAs Pseudo-Code

input: knapsack parameter $P, W, C, m, n$
output: approximate solution $\boldsymbol{Y}$ and the objective function $f(\boldsymbol{Y})$

1) initialize parameter: maxiteration MaxIter, iteration $t$, the population size $N P$, flight probability $\alpha$, selection operator $p_{m}$
2) $H[1 \ldots m] \leftarrow \operatorname{Quicksort}\left(p_{j} / W_{-} N_{j}\right)(j=1,2, \ldots, m)$
3) generate initial population $P(0)$ of $N P$ individuals randomly, and apply the Q-GROA to $P(0)$
evaluate $f(P(0))$
while $t<$ MaxIter do
sort $P(t)$ by $f(P(t))$
generate selection population $S(t)$ from $P(t)$ by $p_{m}$
build probabilistic model $M(t)$ from $S(t)$
for $i=1$ to $N P$ do
if $\operatorname{rand}(1>\alpha$ then
generate new individual $i$ by sampling $M(t)$
else
generate new individual $i$ by Lévy flights
end if
apply the Q-GROA on individual $i$
recalculate $f(P(t))$ and probabilistic model $M(t)$
end for
$t=t+1$
find the best individual $Y$ and $f(Y)$
end while
return $Y$ and $f(Y)$

Let MaxIter and $N P$ be the constant times of $\max \{m, n\}$, where $N=\max \{m, n\}$. In step 2 , the time complexity of the quicksort algorithm is $O(m \log m)=O(N \log N)$. The time complexity of the Q-GROA is $O(m n)=O\left(N^{2}\right)$. In step 3 , the time complexity is $O(m n)+O\left(N P^{*} m\right)=O\left(N^{2}\right)+$ $O\left(N^{2}\right)=O\left(N^{2}\right)$. In steps 5-20, the time complexity is $O\left(\operatorname{MaxIter}^{*} N P^{*} m^{*} n\right)=O\left(N^{4}\right)$. Therefore, the total time complexity of the LFEDAs is $O(N \log N)+O\left(N^{2}\right)+O\left(N^{2}\right)+$ $O\left(N^{4}\right)=O\left(N^{4}\right)$. In other words, it is a random approximation algorithm with polynomial time complexity for solving the SUKP.

## V. EXPERIMENTAL RESULTS

We use three types of large-scale SUKP instances to verify the performance of the EDAs and LFEDAs, and the SUKP instances can be downloaded from http://sncet.com/ThreekindsofSUKPinstances(EAs).rar. An $m \times n 0-1$ matrix $M=\left(r_{i j}\right)(i=1,2, \ldots, m ; j=1,2, \ldots, n)$ denotes the subsets $U=\left\{U_{1}, U_{2}, \ldots, U_{m}\right\}$, and when $r_{i j}=1$, it denotes $j \in U_{i}$. The name of the three types of SUKP instances is unified as $\operatorname{ukp} m_{-} n_{-} \alpha_{-} \beta$, where $m$ is the number of items, $n$ is the number of elements, $\alpha=$ $\left(\sum_{i=1}^{m} \sum_{j=1}^{n} r_{i j}\right) /(m n), \alpha$ represents the density of element 1 in matrix $M, \beta=C / \sum_{j=1}^{n} w_{j}$, and $\beta$ is the ratio of $C$ to the sum of all elements. As shown in Table 1, when

![img-0.jpeg](img-0.jpeg)

FIGURE 1. The flowchart of LFEDAs.
$m>n$, Fir1-Fir10 are the first kind of SUKP instances; when $m=n, \operatorname{Sec} 1 \sim \operatorname{Sec} 10$ are the second kind of SUKP instances; and when $m<n$, Thi1 Thi10 are the third kind of SUKP instances. The experimental platform is a 1.7 GHz Intel (R) Core (TM) i3-4005U CPU with 4 GB of RAM ( 3.75 GB available). The operating system is Microsoft Windows 7. All algorithms are written with C language in the CodeBlocks environment, and the line charts are implemented by MATLAB7.14.0.739 (R2012A).

## A. PARAMETER SETTINGS

The value of the parameter flight probability $\alpha$ for the LFEDAs is determined experimentally. Assume that $\alpha$ is $0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8$, and 0.9 . Due to space limitations, we conducted experiments by LFEDAs on only 6 instances, Fir1, Fir5, Sec1, Sec5, Thi1 and Thi5, after being independently run 100 times each. In Table 2 and Figs. 2-7, the results of the Kruskal-Wallis test of different $\alpha$ value are given. In Table 2, the $p$ value of the Kruskal-Wallis test is given; if the $p$ value is near zero, this casts doubt on the null hypothesis and suggests that at least one sample median is significantly different from the others. Fig. 2 to Fig. 7 show box plots of the 100 best results.

It can be seen from Table 2 and Fig. 2 - Fig. 7 that when $\alpha=0.5$, the best solutions that are obtained by the six cases are the largest, and the median is the largest or the second largest; therefore, $\alpha=0.5$ is a suitable choice.

The parameter settings of the LFEDAs are as follows: a population size of $N P=100$, a selection operator of $P_{m}=0.6$,
![img-1.jpeg](img-1.jpeg)

FIGURE 2. Experimental results for Fir1.
![img-2.jpeg](img-2.jpeg)

FIGURE 3. Experimental results for Fir5.
![img-3.jpeg](img-3.jpeg)

FIGURE 4. Experimental results for Sec1.
![img-4.jpeg](img-4.jpeg)

FIGURE 5. Experimental results for Sec5.
a flight probability of $\alpha=0.5$, and the maxiteration is MaxIter $=\operatorname{Max}\{m, n\}$ for all SUKP instances, where $m$ is the number of items and $n$ is the number of elements in the instances.

## B. COMPARISON OF EXPERIMENTAL RESULTS

To study the performance of the LFEDAs for solving the SUKP, the results are compared with those of the A-SUKP, BABC [5], binDE [24], bWSA [6] and EDAs for the three kinds of SUKP instances.

In Table 3-5, Chest is the best result that is currently known for the instance. Best, Mean, and Std are the best value, the mean value and the standard deviation that are achieved by

TABLE 1. The id of three kinds of SUKP instances.


![img-5.jpeg](img-5.jpeg)

FIGURE 6. Experimental results for Thi1.
![img-6.jpeg](img-6.jpeg)

FIGURE 7. Experimental results for Thi5.
TABLE 2. The results of Kruskal-Wallis test.

all algorithms over 100 times independently. In the A-SUKP approximation algorithm, Best is the same as Mean, and they are approximate results.

It can be seen from Fig. 8(a), Fig. 9(a), and Fig. 10(a) that in terms of the best solution, the LFEDAs are inferior to the EDAs only in Thi1, and the LFEDAs are better or equal to the EDAs in other cases. It can be seen from Fig. 8(b), Fig. 9(b), and Fig. 10(b) that the LFEDAs are superior to the EDAs in terms of the mean performance for the three kinds of SUKP instances. Therefore, the Lévy flight strategy is feasible for solving the SUKP because Lévy flight increases the diversity of the solutions and it helps us find a better
solution. Therefore, we only compare the LFEDAs with other algorithms in the following text.

Since the EA is a stochastic approximation algorithm, in order to evaluate its performance, it is also necessary to consider the average statistical performance. The gap fitting curve can be used to compare the average performances of all algorithms, where the Gap measure is the relative difference between the optimal value Opt and the mean value Mean, and the formula is given in (8). The closer the gap curve is to the transverse axis, the smaller its value is, and the better the average performance of the algorithm.

$$
\text { Gap }=\frac{|\text { Opt }- \text { Mean }|}{O p t} * 100(\%)
$$

The Opt of the SUKP instances is unknown, so Opt is replaced by Cbest when calculating the Gap among the ASUKP, BABC, binDE and LFEDAs. The Gap curve of each algorithm is given in Fig. 11- Fig. 13.

It can be seen from Fig. 11 to Fig. 13 that the Gap value of the LFEDAs is closest to the X axis; therefore, the average performance of the LFEDAs is the best, the A-SUKP is the worst, the bWSA ranks second in most instances, and the BABC is superior to binDE in most cases. Obviously, when solving the first type of SUKP instance, the Gap value of the LFEDAs is less than $5 \%$ except for Fir10. When solving the second and third kinds of instances, the Gap values of the LFEDAs are no more than $10 \%$, while the Gap values of the other algorithms are nearly $25 \%$.

Tables 6-8 show the comparison of LDEDAs with other algorithms in the optimal solution of three types of instances. " + " represents LFEDAs are poor, "-" denotes LFEDAs are better, and " $=$ " represents the same optimal solution for both algorithms. In addition, the total number of " + ", "-", " $=$ " is listed in the last three lines of the table. Obviously, it can be seen that LFEDAs are superior to other algorithms in terms of optimal solutions.

From Fig. 14, we observe that the Stds of the BABC and binDE are less than 300 in most cases, and the Stds of the LFEDAs are smaller than those of the bWSA in most cases; therefore, we conclude that the BABC and binDE are more robust algorithms than the LFEDAs and bWSA for the first

![img-7.jpeg](img-7.jpeg)

FIGURE 8. Comparison between EDAs and LFEDAs for Fir1-Fir10.
![img-8.jpeg](img-8.jpeg)

FIGURE 9. Comparison between EDAs and LFEDAs for Sec1-Sec10.
![img-9.jpeg](img-9.jpeg)

FIGURE 10. Comparison between EDAs and LFEDAs for Thi1-Thi10.
![img-10.jpeg](img-10.jpeg)

FIGURE 11. The Gap fitting curves for Fir1-Fir10.
kind of SUKP instances. From Fig. 15, we find that the Stds of the LFEDAs are less than 100 in 7 cases, the Stds of the LFEDAs are larger than those of the binDE and BABC only
![img-11.jpeg](img-11.jpeg)

FIGURE 12. The Gap fitting curves for Sec1-Sec10.
for the Sec 5 instance, and the Stds of the LFEDAs are smaller than those of the other three algorithms on all other examples. Therefore, the LFEDAs are the most robust algorithm for

TABLE 3. The results of the first kind of SUKP instances.

TABLE 4. The results of the second kind of SUKP instances.

the second kind of SUKP instances. From Fig. 16, the Stds of the LFEDAs are less than 200 in all cases, the Stds of the LFEDAs are slightly larger than the BABC only for the Thi10 instance and slightly larger than the BABC and binDE for the Thi4 instance, and the Stds of the LFEDAs are smaller
than those of the other three algorithms for all other examples. There is no doubt that the LFEDAs are the most robust of all algorithms in the third categories of SUKP cases.

Based on the above analysis, we draw the following two conclusions.

TABLE 5. The results of the third kind of SUKP instances.

![img-12.jpeg](img-12.jpeg)

FIGURE 13. The Gap fitting curves for Thi1-Thi10.
TABLE 6. Comparison of LFEDAs with other algorithms on Fir1-Fir10.

(1) Among all the algorithms, LFEDAs provide better solutions than EDAs, which obviously shows that the Lévy flight strategy for EDAs is an effective way to solve the SUKP.

TABLE 7. Comparison of LFEDAs with other algorithms on Sec1-Sec10.

TABLE 8. Comparison of LFEDAs with other algorithms on Thi1-Thi10.

(2) When using LFEDAs to solve the SUKP, the calculation results are better than those of other algorithms. The results show that the algorithm based on the probability model is more suitable for solving SUKP than other algorithms.

![img-13.jpeg](img-13.jpeg)

FIGURE 14. The Stds for Firi1-Firi10.
![img-14.jpeg](img-14.jpeg)

FIGURE 15. The Stds for Sec1-Sec10.
![img-15.jpeg](img-15.jpeg)

FIGURE 16. The Stds for Firi1-Thi10.

## VI. CONCLUSION

In this paper, EDAs based on Lévy flight are proposed to solve the SUKP problem. To apply the LFEDAs to solve the SUKP, we propose the Q-GROA to solve the infeasible solutions. Compared with the BABC and binDE using the S-GROA, LFEDAs are more effective than the BABC and binDE, and the average solution performance is better. In fact, the Q-GROA is a general-purpose algorithm that can be applied to other EAs (e.g., the artificial algae algorithm (AAA) [35], the fireworks algorithm (FWA) [36], brainstorming optimization (BSO) [37], particle swarm optimization (PSO) [38] and the moth flame optimization algorithm (MFO) [39] to solve the infeasible solutions of the SUKP. Since the SUKP is an NP-complete problem and there is no pseudopolynomial to solve it, it is necessary to find an efficient and fast approximation algorithm. The research results in this paper show that using LFEDAs to design
approximation algorithms is a feasible research direction. In our future research, we will continue to solve the SUKP by developing EDAs and EAs such as the AAA, FWA, BSO, PSO and MFO and will find the best performing EAs. The other two research directions are (i) using more accurate discriminators to consolidate recent machine learning methods [40], and (ii) using adaptive frameworks to improve the robustness and accuracy.
