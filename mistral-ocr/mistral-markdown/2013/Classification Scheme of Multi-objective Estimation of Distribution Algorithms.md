# Classification Scheme of Multi-objective Estimation of Distribution Algorithms 

Alfredo Mendoza-Gonzalez<br>Intelligent Computing Department<br>Autonomous University of<br>Aguascalientes<br>Aguascalientes, Ags. Mexico

Eunice Ponce-de-Leon<br>Intelligent Computing Department<br>Autonomous University of<br>Aguascalientes<br>Aguascalientes, Ags. Mexico

Elva Diaz-Diaz<br>Intelligent Computing Department<br>Autonomous University of<br>Aguascalientes<br>Aguascalientes, Ags. Mexico


#### Abstract

A variety of Estimation of Distribution Algorithms for multi-objective optimization (MOEDAs) has been reported, each of them with its own characteristics and techniques in their optimization process. In this research we present a classification scheme for these algorithms, based on ten characteristics: domain of the variables, relationships between the variables, probabilistic graphical model, estimation approach, restriction support, problem handling, sorting method, individuals' handling, selection approach, and replacement approach. These characteristics were extracted by analyzing all the 24 MOEDAs reported in the literature. The scheme presented here helps to identify the methods and techniques used in each algorithm, also, a useful method for the analysis of the optimization process of an EDA is proposed. This paper includes a brief analysis of the influence in the results of applying different selection/replacement percentages.


Keywords- Estimation of Distribution Algorithms; Evolutionary Algorithms; Multi-objective optimization.

## I. INTRODUCTION

Applying Evolutionary Algorithms over optimization problems has been an interesting case of study for many researchers. Creativity has been the key to create new kind of algorithms. Estimation of Distribution Algorithms (EDAs) incorporate statistical knowledge into the basis of Genetic Algorithms (GA). The creative minds that work on EDAs have strengthened them, designing a variety of new algorithms. In this paper, a classification scheme for the Multi-objective Estimation of Distribution Algorithms (MOEDAs) based on ten criteria is presented. First of all, a deep analysis for all MOEDAs reported in the literature was made: 24 different algorithms were found. Afterwards, the techniques and methods used in their optimization process were identified by following a method described in this paper. The strategy of each algorithm were categorized in: domain of the variables, relationships between the variables, probabilistic graphical model, estimation approach, restriction support, problem handling, sorting method, individuals' handling, selection approach, and replacement approach.

The main contributions of this paper can be summarized as follows:

- A useful method of decomposition of an EDA.
- The presentation of a classification scheme of MOEDAs ruled by ten criteria.
- A useful tool to design, compare, and modify MOEDAs.
- The identification of the methods and techniques already applied in MOEDAs' optimization process.

This paper is presented as follows: Part 2 introduces the Estimation of Distribution Algorithms their basis and their general optimization process. Also, presents the basic concepts of multi-objective optimization. Following, in Part 3 an EDA analysis method is presented, including a proposal of EDA decomposition; the ten criteria of the classification scheme are explained in Part 4: their definitions, methods and techniques. Part 5 presents three useful applications for the taxonomic system. Finally, in Part 6 our conclusions are presented.

## II. BASIC CONCEPTS

## A. Multi-objective Optimization Problem

Multi-objective Optimization Problems (MOPs) have attracted plenty of interest of several areas, due to many realworld problems contain multiple competing objectives; i. e. not a single solution can optimize all the objectives simultaneously.

A general MOP can be expressed as:

$$
\begin{gathered}
\minimize F(x)=\left[f_{1}(x), \ldots, f_{m}(x)\right] \\
\text { subject to } c_{1}(x), \ldots, c_{r}(x) \leq 0 \\
\text { with } x \in D
\end{gathered}
$$

Where D is known as the decision space; the functions $f_{1}(x), \ldots, f_{m}(x)$ are objective functions; the inequalities $c_{1}(x), \ldots, c_{r}(x) \leq 0$ express the restrictions imposed to the values of $x$. Solving a MOP is the process of finding the Pareto-optimal front, which is defined as the set of solutions that can be improved with respect to any objective only at the expense of their quality with respect to at least one other objective. One of the approaches to multi-objective optimization is to solve it through evolutionary algorithms,

due to their capability of working with populations of solutions; this fact has prompted the creation of Multiobjective Evolutionary Algorithms (MOEAs).

TABLE 1
MOEDAs REPORTED IN LITERATURE

| MOEDA | Original EDA |
| :--: | :--: |
| MIDEA | IDEA |
| MO-COIN | COIN |
| MhBOA | hBOA |
| MrBOA | rBOA |
| MBOA | BOA |
| MO-PBIL | PBIL |
| MO-CMA-ES | CMA-ES |
| mMARLEDA | MARLEDA |

## B. Estimation of Distribution Algorithms

Estimation of Distribution Algorithms (EDAs) are Evolutionary Algorithms for optimization that, at each iteration, explore the space of promising solutions by sampling the model of their distribution [1]. The general process of EDAs involves, at least, 8 operators: initialization, evaluation, sorting, selection, learning, sampling, replacement, and finalization.

The EDAs' optimization process begins generating $N$ random solutions (individuals), the fitness is calculated for each one; after all the individuals in the population have been sorted by their adaptability (i. e. their fitness), a subset $K$ of individuals, with $|K|=\tau(N)$ and $\tau=\{\mathbf{0}, \mathbf{1}\}$, is selected. Afterwards, the model of the distribution of the selected individuals is learnt and offspring is created by sampling this model. The set of parents and the set of offspring are joined in order to form a new population. The process is repeated until a stopping condition is met; when this occurs, the algorithm returns the current best individual as the solution of the problem. A pseudocode of this process is presented in figure 1.

## C. Multi-objective Estimation of Distribution Algorithms

Recently EDAs have been successfully implemented on optimizing problems that includes more than one objective, showing a good performance and comparable results with other Multi-objective-implemented Metaheuristics [2-4]. Most of these MOEDAs have their basis in single-objective EDAs; the table 1 shows the cases.

A MOEDA optimization process, also follows the 8 operator shown above, implementing strategies in each made for Multi-objective optimization: evaluates all the objectives, sorts the population according the Pareto dominance (see II, A), return the best approximation to the Pareto front, to name a few. A generic process of a MOEDA is pretty much the same
as the one shown in figure 1, but returns the current-best approximation of the true Pareto front. The literature indicates that there currently there are 24 MOEDAs, table 2 shows them by order of appearance.

```
t \leftarrow 0
generate population P of size N
evaluation and fitness assignment of P
While(stopping condition is not met)\{
S }\leftarrow\mathrm{ select }K\mathrm{ individuals from P with K \leq N
M }\leftarrow \text { learn the probability model of } \mathrm{S}_{t}\mathrm{~S}_{t}
sample M to create a set }\mathrm{Q}\mathrm{ of new solution
    evaluation and fitness assignment of Q
    create P P with best_of }\mp@subsup{}{}{\mathrm{S}}{\mathrm{ }\leftarrow}\mathrm{ Q }\leftarrow\mathrm{ ( }\right.
\ 1 t \leftarrow t+1
\ return (best individual)
```

Figure 1 Single-objective EDA

## III. AlGORITHMS ANALYSIS

In order to analyze each of the 24 state-of-the-art MOEDAs, a carefully study of them most be made; a useful way to accomplish this task is to decompose each algorithm in its 8 basic operators (see II, $B$ ) and identify the strategy that follows in each one.

## A. Decomposition of an EDA

An easy way to analyze an EDA is to see its generic process as independent blocks, each of them develops a defined task; the figure 2 shows this fact. Each block can be seen as a function or a procedure that accepts input-parameters and returns output-values, the hard-work of the analyzer is to identify where the algorithm develops the corresponding task of each block. Identify the main task for each block is the key:

- Initialization: A strategy to construct the first population.
- Evaluation: A strategy to evaluate the fitness function.
- Sorting: A strategy to sort the population.
- Selection: A strategy to select a part of the population that will be considered to build the probabilistic model.
- Learning: A strategy to build the probabilistic model.
- Sampling: A strategy to create new individuals from the probabilistic model.
- Replacement: A strategy to create the new population for the next generation.
- Finalization: A strategy to return the best approximation to the optima.

The result of applying this analysis over the 24 state-of-the-art MOEDAs, is a data base with the strategy that each algorithm follows for each operator. The size of the data base is considerably big; since the goal is to construct a classification scheme, a reduction of this information to the significant data must be done. In the next part, the classification scheme will be constructed and the significant data will be extracted.

TABLE 2
REPORTED MOEDAS

| MOEDA | YR | MOEDA | YR | MOEDA | YR |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $\begin{gathered} \text { MIDEA- } \\ \text { D.C } \end{gathered}$ | 2001 | MhBOA | 2005 | MONEDA | 2008 |
| P-BOA | 2001 | $\begin{gathered} \text { Naive } \\ \text { MIDEA } \end{gathered}$ | 2005 | RM-MEDA | 2008 |
| BMOA | 2002 | MrBOA | 2006 | MMEA | 2009 |
| MBOA | 2002 | mMARLEDA | 2007 | MO-COIN | 2009 |
| MOPED | 2003 | MOCMAES | 2007 | JGBN-EDA | 2011 |
| MOHEDA | 2004 | MO-PBIL | 2007 | MARTEDA | 2011 |
| VEDA | 2004 | RCMEDA | 2007 | MEDA/D | 2012 |
| MASO | 2005 | DT-MEDA | 2007 | $\begin{gathered} \text { MOEA- } \\ \text { HCEDA } \end{gathered}$ | 2012 |

![img-0.jpeg](img-0.jpeg)

Figure 2 Blocks of the process of an EDA

## IV. CLASSIFICATION SCHEME FOR MOEDAS

After the information of all the MOEDAs is collected, a research for the classification schemes for general EDAs must be done (i. e. not only for MOEDAs), literature shows that there are two common ways to classify EDAs.

## A. Classification of EDAs

Some authors have made a useful classification of EDAs [1], [5], that have been adopted by others, these classifications were taken as a base for the extended to multi-objective scheme presented in this article.

Hauschild and Pelikan, categorize EDAs in a first level as: Discrete, Permutations and real-valued vectors. Larrañaga amd Lozano groups them in two ways: EDAs for combinatorial optimization and EDas for countinuos domain. In both researches, it is considered the type of distribution they are able to encode: Discrete and Continuous, being the first one more specific in the Permutation category.

Then as a second level, the authors match by considering the complexity of the probabilistic model used to learn the interdependencies betweeen the variables dividing each category of the first level: Without dependencies, multivariate dependencies and mixture models in [5]; and Univariate, treebased models and multi-variate in [1].

The scheme of classification here proposed contains a more generalized criteria, that involves both approches mentioned above:
$1^{\text {th }}$ criterion: Considering the domain of the variables

- Discrete (DIS)
- Continuous (CNT)
- Mixed (MIX)
$5^{\text {th }}$ criterion ${ }^{1}$ : Considering the relationships between variables
- Univariate (UNI)
- Bivariate (BIV)
- Multivariate (MUL)


## B. Construction of the classification scheme criteria

$2^{\text {th }}$ criterion: Restriction support. This criterion arranges the algorithms that support constraint problems in one group (CON) and those do not in another group (NOC).
$3^{\text {th }}$ criterion: Problem handling. In [5], is shown how the combination of data clustering and evolutionary algorithms has some benefits, this idea was been taken by some authors, consequently, some MOEDAs cluster the objective space, some others do not, depending if the problem is decomposable or not. This criterion classifies the algorithms in two groups: those that implement clustering (CLT) and those do not (NCL).

In [11] it is mentioned another way to classify EDAs, but only applied to those EDAs that involves probabilistic graphical models (PGM) in its process, never the less, there are cases in the 24 state-of-the-art algorithms, that do not involves (PGM) [6-9], so that, a new category must be added in order to include this kind of algorithms:
$4^{\text {th }}$ criterion: Considering the PGM

- Independent (IND)
- Markovian (MK)
- Bayesian (BN)
- No graphical model (NG)

In this section, it will be specify the constitution of the rest of the eleven classification criteria that involves the whole scheme. All of them were extracted from the analysis shown in III applied to the 24 state-of-the-art MOEDAs shown in table 2. The reader can visualize the complete classification scheme in table 3.
$6^{\text {th }}$ criterion: Estimation approach. Larrañaga in [5], mentions that the learning process can be separated in two

[^0]
[^0]:    ${ }^{1}$ Please refer sec. IV,C for the explanation of why this is the $5^{\text {th }}$

sub-tasks structure learning and parametric learning; this criterion classifies MOEDAs considering how they learn the distribution: changing the structure (STR) at each iteration; changing only the parameters (PAR) or changing both.
$7^{\text {th }}$ criterion: Sorting method. There are several methods for sorting individuals in MOEDAs, nevertheless, we have group all of them in three categories: NSGA, Pareto dominance and specialized methods.
a) NSGA-II Sorting (NSG). The algorithms of this class, use the sorting method of NSGA-II [10]. It ranks the population considering the front where they belong, plus evaluating how crowded they are [11].
b) Pareto Dominance sorting (PDS). These algorithms use methods that sort the population considering the number of individuals dominated or that dominate each individual.
c) Specialized Sorting Methods (SSM). In this category Specialized must be understood as those methods that involve more complex theory than the traditional methods mentioned above, e. g. Hypervolume, Parzen sorting, Voronoi sorting, etc.
$8^{\text {th }}$ criterion: Individuals' Handling. MOEDAs evolve a set of individuals which are the possible solutions of the optimization problem. The algorithms of table 2 handle the individuals in two ways: evolving a set of solutions (population) [12] or using an external elitist file where the
non-dominated individuals are stored[13]; the category file is applied to the algorithms that use an Elitist File, and pop is applied to those that use only a population.
$9^{\text {th }}$ criterion: Selection approach. This criterion arranges the algorithms by the part of the population that is considered to estimate the probability distribution; i.e. the subset of the population that is selected.
a) All individuals (ALL). It means that the algorithms select the whole population to learn the model.
b) Best- $\tau$ individuals ( $B-\tau$ ). This class corresponds to the algorithms that selects only a percentile $\tau=[0,1]$ of the population from the learning operator will be applied.
c) Non-Dominated individuals (NDI). The part of the population selected, in these algorithms, for learning operator is only the current non-dominated individuals.
d) Best+Worst individuals ( $B+\mathrm{W}$ ). These algorithms select a part of the best individuals plus a part of the worst.
$10^{\text {th }}$ criterion: Replacement approach. This criterion refers of how the new solutions would be added to the next population. This process is commonly called replacement; this means that the algorithms are classified by the replacement methods that use: Full replacement (FULL). These algorithms replace all the old population by the offspring generated.
a) $\omega$ - Replacement $(\omega-\mathrm{REP})$. These algorithms replace a predefined percentile $\omega=[0,1]$ of the old population

TABLE 3
TASONOMIC SYSTEM FOR MOEDAS

|  | Problem-related |  |  | Learning-related |  |  | Solutions-related |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| MOEDA | $1 \mathrm{~m}$ | $2^{\mathrm{m}}$ | $3^{\mathrm{m}}$ | $4^{\mathrm{m}}$ | $5^{\mathrm{m}}$ | $6^{\mathrm{m}}$ | $7^{\mathrm{m}}$ | $8^{\mathrm{m}}$ | $9^{\mathrm{m}}$ | $10^{\mathrm{m}}$ |
| BMOA | DIS | NOC | NCL | BN | MUL | STR | SSM | FILE | B- $\tau$ | $\omega$-REP |
| DT-MEDA | CNT | NOC | NCL | NG | MUL | STR | NSG | FILE | B- $\tau$ | $\omega$-REP |
| IGRN-EDA | CNT | NOC | NCL | BN | MUL | STR | NSG | POP | B- $\tau$ | $\omega$-REP |
| MARTEDA | CNT | NOC | NCL | NG | MUL | STR | SSM | POP | B- $\tau$ | $\omega$-REP |
| MASO | DIS | CON | NCL | IND | UNI | STR | SSM | FILE | NDI | FULL |
| MBOA | DIS | NOC | NCL | BN | MUL | STR | NSG | POP | ALL | ALL-W |
| MEDA/D | DIS | CON | CLT | NG | UNI | PAR | NSG | FILE | NDI | ALL-W |
| MbBOA | DIS | NOC | CLT | BN | MUL | STR | NSG | POP | B- $\tau$ | ALL-W |
| MIDEA-C | CNT | NOC | CLT | IND | UNI | PAR | PDS | POP | B- $\tau$ | ALL-W |
| MIDEA-D | DIS | NOC | CLT | IND | UNI | PAR | PDS | POP | B- $\tau$ | ALL-W |
| mMARLEDA | DIS | CON | NCL | MK | MUL | PAR | NSG | POP | B- $\tau$ | $\omega$-REP |
| MMEA | CNT | NOC | CLT | IND | UNI | PAR | NSG | POP | NDI | $\omega$-REP |
| MOCMAES | CNT | CON | NCL | NG | MUL | PAR | NSG | POP | B- $\tau$ | ALL-W |
| MO-COIN | DIS | NOC | NCL | NG | BIV | STR | NSG | POP | B+W | ALL |
| MOEAHCEDA | DIS | NOC | NCL | IND | UNI | PAR | PDS | FILE | NDI | $\omega$-REP |
| MOHEDA | DIS | CON | CLT | IND | UNI | PAR | SSM | FILE | B- $\tau$ | FULL |
| MONEDA | CNT | NOC | CLT | NG | MUL | STR | NSG | POP | B- $\tau$ | $\omega$-REP |
| MO-PBIL | DIS | NOC | NCL | IND | UNI | PAR | NSG | FILE | NDI | FULL |
| MOPED | CNT | NOC | NCL | NG | MUL | PAR | SSM | POP | ALL | $\omega$-REP |
| MrBOA | CNT | NOC | NCL | BN | MUL | STR | PDS | POP | B- $\tau$ | $\omega$-REP |
| P-BOA | DIS | NOC | NCL | BN | MUL | STR | PDS | FILE | B- $\tau$ | ALL-W |
| RCMEDA | CNT | CON | NCL | NG | MUL | PAR | NSG | POP | B- $\tau$ | $\omega$-REP |
| RM-MEDA | CNT | NOC | CLT | IND | UNI | PAR | NSG | POP | ALL | FULL |
| VEDA | CNT | NOC | CLT | NG | MUL | STR | NSG | FILE | B+W | ALL-W |

by the offspring.
b) All- worst replacement ( $A L L-W$ ). This class of algorithms replaces all the non-selected individuals by the new ones.
c) Random-worst ( $R-W$ ). These algorithms replace randomly the worst individuals in the old population by the new ones.

## C. Groups of Criteria

With the purpose of maintain an order in the classification scheme; the 10 criteria have been group in categories: Learning-related, Problem-related and Solutions-related.
a) Problem-related. Involves the criteria that concern characteristics of the problem to be optimized.
b) Learning-related. Involves the criteria that concern (in some way) the task related with the process of learning the distribution.
c) Solutions-Related. Groups the criteria that involve how the algorithm manages the solutions in the whole process of optimization.

## V. APPLYING THE CLASSIFICATION SCHEME

Besides the compendium of the methods and techniques already used in MOEDAs, and the radiography of the state-of-the-art MOEDAs, three possible applications of the Classification Scheme here proposed were found:

- The design of a MOEDA
- An easy way to select algorithms that will be part of a comparison.
- The improvement of an already-tested algorithm


## A. Design of a MOEDA

The scheme of the table 3 can be used as a guide to select the characteristics of a new algorithm. The function to be optimized is shown in equation 2 ; this is a continuous multiobjective problem. The algorithm will use a Univariate Gaussian distribution.

$$
\begin{gathered}
f_{1}=f_{1}\left(x_{1}\right)=x_{1} \\
g=g\left(x_{2}, x_{3}, \ldots, x_{n}\right)=1+\frac{9}{n-1} \cdot \sum_{i=2}^{n} x_{i} \\
h\left(f_{i}, g\right)=1-\sqrt{\frac{f_{1} f_{g}}{g}} \\
\text { with } n=30 \text { and } x_{i} \in[0,1]
\end{gathered}
$$

The classification scheme will be used in order to know what other characteristics would be consider in this design, for this purpose, the focus will be in the algorithms that match in this characteristics: continuous domain of the variables, univariate relationships between the variables, independent probabilistic graphical model. The analysis helps to select the next characteristics, due that the combination has not already tried, the values in to the scheme for this algorithm called GIMOEDA (Gaussian Independent Multi-objective Estimation of Distribution Algorithm), are shown in table 4.

TABLE 4
CLASSIFICATION CRITERIA FOR GI-MOEDA

| GI-MOEDA |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
| $1^{\text {th }}$ | $2^{\text {th }}$ | $3^{\text {th }}$ | $4^{\text {th }}$ | $5^{\text {th }}$ |
| IND | UNI | PAR | CNT | NOC |
| $6^{\text {th }}$ | $7^{\text {th }}$ | $8^{\text {th }}$ | $9^{\text {th }}$ | $10^{\text {th }}$ |
| NCL | NSG | FILE | B- $\tau$ | $\omega$-REP |

## B. Modification of a MOEDA ${ }^{2}$

The characteristics of the GI-MOEDA still can be changed, in order to have a better combination, without altering neither the learning strategy nor the kind of problem optimizing; i. e. by the modification of the Solutions-Related characteristics. Note that this modification does not guarantee the improvement of the algorithm; this is only shown as a good design practice.

This modification would consist in testing the algorithm with all the possible combination in criteria $7^{\text {th }}, 8^{\text {th }}, 9^{\text {th }}, 10^{\text {th }}$, generate at least 96 different algorithms, since this is not the main goal of this research, the test will try the combinations with the next values (which are the most common values) generating 16 algorithms:

- Criterion 7: NSG
- Criterion 8: FILE, POP
- Criterion 9: B- $\tau$, NDI, ALL, B+W
- Criterion 10: $\omega$-REP, FULL

There are three combinations that approximate in a better way to the optimum, (the four nearest to the $(0,0)$ in figure 3 ), these correspond to:
![img-1.jpeg](img-1.jpeg)

Figure 3: Pareto fronts of combinations for IG-MOEDA

1. Combination (NSG, POP, B- $\tau, \omega$-REP)
2. Combination (NSG, POP, NDI, $\omega$-REP)
${ }^{2}$ This algorithm is only shown as an example for the application of the classification scheme

## 3. Combination (NSG, FILE, B- $\tau, \omega$-REP)

4. Combination (NSG, FILE, NDI, $\omega$-REP)

The combination 3 is chosen (in this paper), because is the one that best covers the objective space.

## C. Comparison of MOEDAs

The third application shown in this research of the Classification Scheme of MOEDAs is to compare the GIMOEDA with other algorithms; the scheme helps to choose those algorithms.

The algorithms chosen to this test is going to be those that have the most coincidences in the scheme with GI-MOEDA: MIDEA-C and MMEA; they match in criteria $1^{\circ}, 2^{\circ}, 4^{\circ}, 5^{\circ}$, $6^{\circ}$, and $7^{\circ}$.

The function to optimize is the one of equation 2 , and for all the algorithms the next initial parameters were fixed:

- Maximum of generation: 100
- Population size: 100
- 20 independent runs of each algorithms

In figure 4, the average Pareto fronts (the average of all Pareto approximations of all generations), after the 100 generations of the 20 runs, of each algorithm, are shown. This test is only shown as an application of the scheme, since the objective of this paper was not the design of an algorithm, the conclusion of this test is not focused on the quality of GIMOEDA; nevertheless, good results were obtain with it.

## CONCLUSIONS

A Classification Scheme for Multi-objective Estimation of Distribution Algorithms was presented in this paper; it involves the traditional classification criteria plus 7 new-added ones, which complement the comparable-characteristics of the algorithms. Due to the design of the scheme was made by a wide analysis of the state-of-the-art MOEDAs, the reader can obtain information of the methods and techniques that are currently applied. Finally, three ways of its application were analyzed: A design of a new MOEDA called GI-MOEDA guided by the scheme, a modification of the parameters of this algorithms that shown some improvement on it (also guided by the scheme), and a comparison of this algorithm with two of the reported ones in literature (chosen using the scheme).

## ACKNOWLEDGMENT

The authors of this paper appreciate the designers of all the algorithms mentioned here, each of them has enriched the research in Multi-objective Estimation of Distribution Algorithms, and their work became the main motivation of this research.
![img-2.jpeg](img-2.jpeg)

Figure 4: Comparison of Pareto Fronts
The complete list of algorithms and their reference is shown next: BMOA [14], DT-MEDA [15], JGBN-EDA [4], MARTEDA [9], MASO [16], MBOA [17], MEDA/D [3], MhBOA [11], MIDEA [19], mMARLEDA [20], MMEA [21], MO-CMA-ES [22], MO-COIN [23], MOEA-HCEDA [24], [8], MOHEDA [18], MONEDA [7], MO-PBIL [25], MOPED [8], MrBOA [26], P-BOA [27], RCMEDA [28], RM-MEDA [29], and VEDA [6].

## REFERENCES

[1] M. Hauschild and M. Pelikan, "A Survey on Estimation of Distribution Algorithms," MEDAL Report No. 2011004, p. 0113, 2011.
[2] Y. Li, A. Zhou, and G. Zhang, "A Decomposition based estimation of distribution algorithm for multiobjective knapsack problems," 2012 8th International Conference on Natural Computation, no. Icnc, pp. 803-807, May 2012.
[3] F. Gao, A. Zhou, and G. Zhang, "An estimation of distribution algorithm based on decomposition for the multiobjective TSP," 2012 8th International Conference on Natural Computation, no. ICNC, pp. 817-821, May 2012.
[4] H. Karshenas, R. Santana, C. Bielza, and Larrañaga "Multiobjective optimization with joint probabilistic modeling of objectives and variables," Lecture Notes in Computer Science Vol. 6576, pp. 298-312, Springer, 2011.
[5] P. Larrañaga and J. A. Lozano, "Estimation of Distribution Algorithms: A new tool for Evolutionary Computation," 2002.
[6] T. Okabe, Y. Jin, B. Sendhoff, and M. Olhofer, "Voronoi-based Estimation of Distribution Algorithm for Multi-objective Optimization," In Proceedings of the 2004 Congress on Evolutionary Computation CEC-2004, 2004.
[7] L. Marti, J. Garcia, A. Berlanga, and J. M. Molina, "Introducing MONEDA: scalable multiobjective optimization with a neural estimation of distribution algorithm," Proceeding GECCO '08 Proceedings of the 10th annual conference on Genetic and evolutionary computation ACM New York, NY, USA 02008, 2008.

[8] M. Costa and E. Minisci, "MOPED: a multi-objective parzen-based estimation of distribution algorithm for continuous problems," Evolutionary MultiCriterion Optimization Second International Conference EMO 2003 Faro Portugal April 811 2003 Proceedings (2003), vol. 2632, Publ, 2003.
[9] L. Martí, J. García, A. Berlanga, and J. M. Molina, "MultiObjective Optimization with an Adaptive Resonance Theory-Based Estimation of Distribution Algorithm: A Comparative Study," LION'05 Proceedings of the 5th international conference on Learning and Intelligent Optimization. Springer-Verlag, Berlin, Heidelberg, 2011.
[10] K. Deb, S. Agrawal, A. Pratap, and T. Meyarivan, "A Fast Elitist Non-Dominated Sorting Genetic Algorithm for Multi-Objective Optimization: NSGA-II," PPSN VI Proceedings of the 6th International Conference on Parallel Problem Solving from Nature, no. Springer-Verlag London, 2000.
[11] M. Pelikan, K. Sastry, and D. E. Goldberg, "Multiobjective hBOA, Clustering, and Scalability," GECCO'05, June 25-29, 2005, Washington, DC, USA, vol. ACM 1-5959, 2005.
[12] S. Baluja, "Population-Based Incremental Learning: A Method for Integrating Genetic Search Based Function Optimization and Competitive Learning," Pittsburgh, Pennsylvania, 1994.
[13] E. Zitzler, M. Laumanns, and L. Thiele, "SPEA2: Improving the Strength Pareto Evolutionary Algorithm," Eidgenössische Technische Hochschule Zürich (ETH), Institut für Technische Informatik und Kommunikationsnetze (TIK), vol. TIK-Report, 2001.
[14] M. Laumanns and J. Očenašek, "Bayesian Optimization Algorithms for Multi-Objective Optimization," PPSN VII Proceedings of the 7th International Conference on Parallel Problem Solving from Nature. Springer-Verlag, London, 2002.
[15] X. Zhong and W. Li, "A Decision-Tree-Based Multi-objective Estimation of Distribution Algorithm," 2007 International Conference on Computational Intelligence and Security (CIS 2007), pp. 114-118, Dec. 2007.
[16] S. I. Valdez, S. R. Botello, and A. Hernández, "Multiobjective shape optimization using estimation distribution algorithms and correlated information," Proceeding EMO'05 Proceedings of the Third international conference on Evolutionary Multi-Criterion Optimization Springer-Verlag Berlin, Heidelberg ©(2005, 2005.
[17] N. Khan, D. E. Goldberg, and M. Pelikan, "Multi-Objective Bayesian Optimization Algorithm," Proceedings of the Genetic and Evolutionary Computation Conference, 2002.
[18] H. Li, Q. Zhang, E. Tsang, and J. A. Ford, "Hybrid Estimation of Distribution Algorithm for Multiobjective Knapsack," In Evolutionary Computation in Combinatorial Optimization, pp. 145154, 2004.
[19] D. Thierens and P. A. N. Bosman, "Multi-Objective Mixture-based Iterated Density Estimation Evolutionary Algorithms," Proceedings of the Genetic and Evolutionary Computation Conference. San Francisco,California, 2001.
[20] M. E. Alden, "MARLEDA : Effective Distribution Estimation Through Markov Random Fields," The University of Texas at Austin, 2007.
[21] A. Zhou, Q. Zhang, and Y. Jin, "Approximating the Set of ParetoOptimal Solutions in Both the Decision and Objective Spaces by an Estimation of Distribution Algorithm," Journal IEEE Transactions on Evolutionary Computation, vol. Volume 13, 2009.
[22] C. Igel, N. Hansen, and S. Roth, "Covariance matrix adaptation for multi-objective optimization.," Evolutionary Computation, vol. 15, no. 1, pp. 1-28, 2007.
[23] W. Wattanapornprom, P. Olanvivitchai, P. Chutima, and P. Chongstivatana, "Multi-objective Combinatorial Optimisation with Coincidence Algorithm," Proceeding CEC'09 Proceedings of the Eleventh conference on Congress on Evolutionary Computation IEEE Press Piscataway, NJ, USA, 2009.
[24] S. Enriquez-Aranda, E. E. Ponce de León, E. D. Díaz, and C. A. Ochoa-Ortiz-Zezzatti, "An Evolutionary Algorithm for Graph Drawing with a Multiobjective Approach," in Logistics Management and Optimization through Hybrid Artificial Intelligence Systems, C. A. O. O. Zezzatti, C. Chira, A. Hernandez, and M. Basurto, Eds. IGI Global, 2012.
[25] S. Burzerat and K. Srivoramas, "Population-Based Incremental Learning for Multiobjective Optimisation," Soft Computing in Industrial Applications Publisher: Springer. Advances in Soft Computing, Vol. 39, Pages: 223-232, 2007.
[26] C. W. Ahn, "Multiobjective Real-coded Bayesian Optimization Algorithm," Advances in Evolutionary Algorithms: Theory, Design and Practice, Studies in Computational Intelligence. Springer Berlin / Heidelberg, 2006.
[27] J. Schwarz and J. Očenašek, "Multiobjective Bayesian Optimization Algorithm for Combinatorial Problems: Theory and practice," NEURAL NETWORK WORLD, vol. Vol. 11, N, pp. 423-441, 2001.
[28] X. Zhong and W. Li, "A Real-Coded Multi-objective Estimation of Distribution Algorithm," SMO' 97 Proceedings of the 7th WSEAS International Conference on Simulation, Modelling and Optimization, 2007.
[29] Q. Zhang, A. Zhou, and Y. Jin, "RM-MEDA: A Regularity Model Based Multiobjective Estimation of Distribution Algorithm," Evolutionary Computation, IEEE Transactions on In Evolutionary Computation, IEEE Transactions on, Vol. 12, No. 1., 2008.