# Optimal decoding and minimal length for the non-unique oligonucleotide probe selection problem 

Laleh Soltan Ghoraie ${ }^{\text {a,* }}$, Robin Gras ${ }^{\text {a }}$, Lili Wang ${ }^{\text {b }}$, Alioune Ngom ${ }^{\text {a }}$<br>${ }^{a}$ School of Computer Science, 5115 Lambton Tower, University of Windsor, 401 Sunset Avenue, Windsor, Ontario, Canada N9B 3P4<br>${ }^{\mathrm{b}}$ School of Computing, 556 Goodwin Hall, Queen's University, Kingston, Ontario, Canada K7L 3N6

## A R T I C L E I N F O

Available online 29 June 2010
Keywords:
Microarray
Probe selection
Target
Estimation of distribution algorithm
Bayesian optimization algorithm
Heuristic
Multiobjective optimization
Decoding
Markov chain Monte Carlo

## A B S T R A C T

One of the applications of DNA microarrays is recognizing the presence or absence of different biological components (targets) in a sample. Hence, the quality of the microarrays design which includes selecting short Oligonucleotide sequences (probes) to be affixed on the surface of the microarray becomes a major issue. A good design is the one that contains the minimum possible number of probes while having an acceptable ability in identifying the targets existing in the sample. This paper focuses on the problem of computing the minimal set of probes which is able to identify each target of a sample, referred to as non-unique oligonucleotide probe selection. We present the application of an estimation of distribution algorithm (EDA) named Bayesian optimization algorithm (BOA) to this problem, for the first time. The proposed approach considers integration of BOA and one simple heuristic introduced for the non-unique probe selection problem. The results provided by this approach compare favorably with the state-of-the-art methods in the single target case. While most of the recent research works on this problem has been focusing on the single target case only, we present the application of our method in integration with decoding approach in a multiobjective optimization framework for solving the problem in the case of multiple targets.

Crown Copyright © 2010 Published by Elsevier B.V. All rights reserved.

## 1. Introduction

Microarrays are tools used for performing many hybridization experiments in parallel. As noted by Schliep et al. [18], two main applications are considered for microarrays. A first application is measuring the expression levels of thousands of genes simultaneously. Gene expression level is measured based on the amount of mRNA sequences bound or hybridized to their complementary sequences affixed on the surface of the microarray. The complementary sequences are called probes which are typically short DNA strands about $8-30 \mathrm{bp}$ [24]. The second important application of miocroarrays is the identification of unknown biological components in a sample [9]. Knowing the sequences affixed on the microarray and considering the hybridization pattern of a sample, one can infer which targets exist in the sample by observing appropriate hybridization reactions [18]. Finding an appropriate set of probes to be affixed on the surface of microarray, or in other words, finding a good design for microarray is a crucial task. The appropriate design should lead to costefficient experiments. Therefore, while the quality of the probe set

[^0]is important, the objective of finding the minimal set of probes also should be considered. The quality of the probe set is discussed in terms of its ability to identify the unknown targets in the sample.

Two approaches are considered for the probe selection problem, namely, unique and non-unique probe selection. In the unique probe selection, for each single target there is one unique probe designed to hybridize only to the target. In this case, in specified experimental conditions, the probe should not hybridize to other targets except for its intended target. However, due to high levels of similarity in families of closely related gene sequences, finding unique probes for each target is almost impossible [9,10,13,16,18,22-24]. When many targets are similar, experimental errors increase. In these cases, an alternative approach is applying non-unique probes.

The non-unique probes are designed to hybridize to more than one target. The non-unique probe selection problem is to find the smallest probe set that is able to uniquely identify a set of targets in the sample [24]. Minimizing the probe set is a reasonable objective. Smaller microarray designs occupy less space on the surface of microarray. This leads to use smaller chips, and reduce the costs considerably [18].

Our focus in this paper is on the non-unique probe selection. We propose a method for solving the non-unique probe selection problem. Given a design containing candidate non-unique probes,


[^0]:    * Corresponding author.

    E-mail addresses: soltan@uwindsor.ca (L.S. Ghoraiie), rgras@cs.uwindsor.ca (R. Gras), lili@cs.queensu.ca (L. Wang), angom@cs.uwindsor.ca (A. Ngom).

our task is to analyze and minimize the design in order to select the best possible probe set. The initial design is presented as a target-probe incidence matrix. Target-probe incidence matrices contain the targets and probes and their hybridization patterns. The included probes are the high quality ones selected among all possible non-unique probes [9]. Computing the initial targetprobe incidence matrix in not a trivial task [10].

Many parameters such as secondary structure, salt concentration, GC content, hybridization energy, etc., influence the quality of the probes hybridization [18], and should be considered carefully in selecting the candidate probes. For instance, at a given temperature and salt concentration, all probes should exhibit the same hybridization affinity [10]. Moreover, hybridization errors such as cross-hybridization, self-hybridization, and non-sensitive hybridization should also be taken into account in computing the set of candidate probes for the Oligonucleotide probe selection [23]. Candidate probes should neither be selfcomplementary nor should cross-hybridize [10].

It should be noted that we assume that the problem of computing the target-probe incidence matrix has been solved, and our focus is minimizing the design given by this matrix.

This paper is organized as follows. Section 2 provides a detailed description of the non-unique probe selection problem. Related work on non-unique probe selection is reviewed in Section 3. In Section 4, we present our approach for solving the non-unique probe selection problem. A review of the main concepts of Bayesian optimization algorithm (BOA) is presented in Section 5, and its advantages over the genetic algorithms (GA) are discussed. Also, the heuristic which we have integrated into the BOA is discussed in Section 6. At the end of this section, we explain how and why we integrate the heuristic into the BOA. The multiobjective optimization technique and decoding idea applied in this work are discussed in Sections 7 and 8, respectively. We discuss the results of our experiments in Section 9. In Section 10, complexity of the components of the approach is discussed. Finally, we conclude this research work with discussion of possible future research directions and open problems appears in Section 11.

## 2. Non-unique probe selection problem

We illustrate the probe selection problem with an example. Assume that we have a target-probe incidence matrix $H=\left(h_{i j}\right)$ of a set of three targets $\left(t_{1}, \ldots, t_{3}\right)$ and five probes $\left(p_{1}, \ldots, p_{5}\right)$, where $h_{i j}=1$, if probe $j$ hybridizes to target $i$, and 0 otherwise (see Table 1). The problem is to find the minimal set of probes which identifies all targets in the sample. First, we assume that the sample contains a single target. Using a probe set of $\left\{p_{1}, p_{2}\right\}$, we can recognize the four different situations of 'no target present in the sample', ' $t_{1}$ is present', ' $t_{2}$ is present', and ' $t_{3}$ is present' in the sample. The minimal set of probes in this case is $\left\{p_{1}, p_{2}\right\}$ since $\left\{p_{1}\right\}$ or $\left\{p_{2}\right\}$ cannot detect these four situations.

Consider the case that multiple targets are present in the sample. In this case, the chosen probe set should be able to distinguish between the events in which all subsets (of all possible cardinalities) of the target set may occur. The probe set

Table 1
Sample target-probe incidence matrix.
$\left\{p_{1}, p_{2}\right\}$ is not good enough for this purpose. With this probe set, we cannot recognize between the case of having subset $\left\{t_{1}, t_{2}\right\}$ and $\left\{t_{2}, t_{3}\right\}$ in the sample. However, the probe set $\left\{p_{3}, p_{4}, p_{5}\right\}$ can distinguish between all events in this case. It should be noted that the incidence matrix presented here is an unreal example, and its dimensions (number of probes and targets) are not representative of the real datasets of non-unique probe selection problem. For instance, the smallest incidence matrix in the literature contains about 256 targets and 2786 probes. For more information on the datasets properties, see Table 5.

Now, a more formal definition of the probe selection problem is presented.

Given the target-probe incidence matrix $H$, and parameters $s_{\min } \in \mathbb{N}$ and $c_{\min } \in \mathbb{N}$, the goal is to select a minimal probe set such that each target is hybridized by at least $c_{\min }$ probes (minimum coverage constraint), and any two subsets of targets are separated by means of at least $s_{\min }$ probes (minimum separation constraint) $[9,10]$.

A probe separates two subsets of targets if it hybridizes to exactly one of them. We say that a probe hybridizes to a set of targets when it hybridizes to at least one of the targets in the target set [18]. In other words, assume two target sets of $S$ and $T$. If $P(S)$ and $P(T)$ are the set of probes hybridizing to $S$ and $T$, respectively, a probe $p$ separates these two sets of targets if $p \in P(S) \Delta P(T)[18] . \Delta$ denotes symmetric set difference. Moreover, target sets $S$ and $T$ are $s_{\min }$-separable if at least $s_{\min }$ probes separates them, that is $\left|P(S) \Delta P(T)\right| \geq s_{\min }$.

The probe selection is proven to be a NP-hard problem [5], and is considered as a variation of the combinatorial optimization problem minimal set covering problem. We consider the problem in both cases of single target and multiple targets in the sample. The focus of the literature has mostly been on the problem in case of single target, although multiple targets in the sample are more realistic. In most of the real experiments of target-probe hybridization, several targets exist simultaneously in the sample, and in general, the identity of targets in the sample is unknown in advance. Therefore, it is crucial for the selected probe set of the final design to have the ability to identify several targets in the sample.

As mentioned, the problem can be approached as an optimization problem. The search space of the problem consists of $2^{p}$ ( $p=$ number of probes) possible solutions which makes this problem very difficult to solve exhaustively, even with powerful computers [16]. We propose a method based on an estimation distribution algorithms (EDA), named Bayesian optimization algorithm (BOA) integrated with a simple probe selection heuristic for both cases of single target and multiple targets in sample. This work is the first one which considers the ability of the probes to recognize multiple targets in the sample explicitly as an objective of the optimization algorithm.

## 3. Previous work

Most of the research works dedicated to the non-unique probe selection problem have focused on the case of single target in sample. As mentioned, this case is a simplified version of the nonunique probe selection problem. Rash and Gusfield [17] considered genes as strings and the probes as substrings of these original strings. They used suffix tree to identify the critical substrings and integer linear programming in order to solve the optimization problem. They applied CPLEX (an ILP solver) to solve the ILP problem. Schliep et al. [18] introduced a fast heuristic for minimizing the size of the probe set. Since guaranteeing the separation of all possible subsets of the original target set was computationally impossible by their heuristic, they could only

guarantee the separation of up to a randomly chosen number $N$ (e.g. $N=500,000$ ) of pairs of target subsets. In this work, for the first time the idea of decoding was proposed. They presented a Bayesian method in order to evaluate the ability of the obtained probe set by their fast heuristic in identifying multiple targets. In this work, cross-hybridization and experimental errors were explicitly taken into account for the first time. Klau et al. [10] extended this work. CPLEX was applied to solve the ILP.

The ILP formulation extended to a more general version which also includes the group separation [9] in which groups correspond to multiple targets. They proposed a branch-and-cut algorithm to solve the ILP. By this extension, the assumption of the multiple targets was realized. Focusing on the single target case, Meneses et al. [13] used a two-phase heuristic including, first, construction of a feasible solution containing enough probes able to satisfy the constraints, and second, reducing the size of the probe set. Ragle et al. [16] applied a cutting-plane approach with reasonable computation time, and achieved the best results for some of the benchmark datasets in case of single target. Without using any a priori method to decrease the number of initial probes, the cutting-place algorithm relaxes a constraint set in order to find the lower bounds on the number of the required probes for an optimal solution. Then it improves the lower bound till an optimal solution is obtained. Wang and Ngom [23] presented deterministic heuristics in order to solve the ILP formulation, and reduce the size of final probe set. They applied their heuristic in order to introduce a population-based approach (without learning phase) for coverage and separation in order to guide the search for the appropriate probe set in case of single target in the sample. Recently, Wang et al. [22] presented a combination of the genetic algorithm and the selection functions used in [23], and obtained results which are in most cases better than results of Ragle et al. [16]. Finally, Soltan Ghoraie et al. [20], focusing on the single target case, proposed a compound method of Bayesian optimization algorithm (BOA) and a simple heuristic of Wang and Ngom [23] to solve the optimization problem of non-unique probe selection. This paper extends the mentioned approach to be able to solve the more realistic problem in case of presence of multiple targets in the sample.

## 4. Our approach

Our approach is based on integration of Bayesian optimization algorithm (BOA) (see Section 5) and a heuristic named dominated row covering (DRC) which was proposed in [23] for solving the problem of non-unique probe selection (see Section 6). The nonunique probe selection problem has been considered as an optimization problem for the cases of single target and multiple targets in the sample. We approach the problem in case of single target in the sample as a one-objective optimization problem. The objective is minimizing the number of selected probes.

The case of multiple targets in the sample is considered as a twoobjective optimization problem. While first objective is minimizing the probe set, the other one is the ability of the selected set in identifying a predetermined number of targets in the sample. Several methods have been proposed to solve multiobjective optimization problems efficiently by means of evolutionary-based algorithms such as BOA (see Section 7). We have applied one of the most efficient methods proposed in the literature.

The definition of the non-unique probe selection problem is realistic when the possibility of presence of a set of targets in the sample is considered. Only in this case, the obtained solutions are practical solutions. Therefore, evaluating the ability of the selected (by means of any method) probe sets in identifying targets of the sample is a critical task. Our work is the first one
that explicitly seeks to maximize the ability of a probe set in identifying multiple targets in the sample, along with the goal of minimizing the probe set. In order to measure the ability of selected probe set in identifying multiple targets, we have applied decoding idea proposed by Schliep et al. [18] (see Section 8).

## 5. Bayesian optimization algorithm

Estimation of distribution algorithm (EDA) method was introduced by Larranaga and Lozano [12] and Mühlenbein and Paaß [14]. EDAs are also called probabilistic model-building genetic algorithms (PM-BGA) which extend the concept of classical GAs. Targeting more efficient exploration of the search space, EDA approach has been proposed. In EDA optimization methods, a sample of the search space is generated and the information extracted from that sample is used in order to explore the search space more efficiently.

The EDA (Algorithm 1) is an iterative approach. In initialization (1), a set of random solutions is generated which is the first sample of search space (2); the quality of solutions is evaluated (3); a subset of high quality solutions that have more probability to be chosen is selected (4); a probabilistic model of the sample is constructed, and the model is used to generate a new set of solutions (5). The algorithm is repeated from evaluation step.

## Algorithm 1. EDA

1. (Random) initialization of set of solutions $S_{0}$
2. $S=S_{0}$
3. Evaluation of $S$
4. Select set of promising solutions $S_{i}$
5. Build probabilistic model $M$ of $S_{i}$
6. Sample from the Model $M$ and generate new set of solutions $S$
7. Repeat from 3.

In BOA, which was first proposed by Pelikan [15], the constructed probabilistic model is a Bayesian network. A Bayesian network can be considered as a directed acyclic graph in which the nodes represent the variables of the problem, and the directed edges introduced between some nodes represent the dependencies among the variables. The important advantage of constructing a Bayesian network is discovering and representing the possible dependencies between the variables of the problem. The discovered dependencies which are extracted from the sample of search space, are used to accomplish the target of BOA to explore the search space more efficiently.

Based on the generic algorithm of EDA, in BOA, a probabilistic model which is a Bayesian network is constructed in step (5). Learning a Bayesian network is basically a two-step process. First the dependencies should be discovered which means an appropriate network structure should be found, and second, the conditional probabilities between the variables should be estimated. A local search algorithm is used for the problem of building the best network from the sample in each iteration of BOA. A metric to measure the quality of the built network directs the local search. For further information on building Bayesian networks, see [8]. After constructing the network, the joint probabilities should be estimated. These probabilities can be estimated based on the frequency of occurrences of the variables in the sample.

In optimization problems, there is a difficult class of problems which contain dependencies among variables, and classical GAs has been shown not to be able to solve these problems properly [6]. On the other hand, BOA approach has been more successful in solving such problems. We are interested in applying BOA

approach for the complex problem of nonunique probe selection optimization problem. In this problem, we considered that each binary variable represents the presence or absence of a particular probe in the final design matrix. The dependencies among variables represent the fact that choosing a particular probe have a consequence on the choice of other probes in an optimal solution. Pelikan and Goldberg [4], [15] have proven that when the number of variables and the number of dependencies are $n$ and $k$, respectively, the size of the sample should be about of $O\left(2^{k} \cdot n^{1.05}\right)$ to guarantee convergence.

There are several advantages in applying this new approach. First, BOA is known as an efficient way to solve complex optimization problems. Therefore, it is interesting to compare it with other methods applied to the non-unique probe selection problem. Second, EDA methods, by working on the samples of the search space and deducing the properties of dependencies among the variables of the problem, are able to reveal new knowledge about the biological mechanisms involved. Finally, with the study of the results obtained from experimenting different values of the parameter $k$, BOA provides the ability to evaluate the level of complexity of the non-unique probe selection in general, and the specific complexity of the classical set of problems applied to evaluate the algorithms used for solving this problem in particular.

## 6. Dominated row covering heuristic

As mentioned above, our algorithm integrates a simple heuristic to the BOA. The heuristic dominated row covering (DRC) was proposed by Wang and Ngom [23]. Given the target-probe incidence matrix $H$, probe set $P=\left\{p_{1}, \ldots, p_{n}\right\}$, and the target set $T=\left\{t_{1}, \ldots, t_{m}\right\}$, two main functions $C\left(p_{j}\right)$ (coverage function) and $S\left(p_{j}\right)$ (separation function) have been defined for this heuristic as follows:
$C\left(p_{j}\right)=\max _{t_{1} \in T_{p_{j}}}\left(\operatorname{cov}\left(p_{j}, t_{i}\right) \mid 1 \leq j \leq n\right)$
where $T_{p_{j}}$ is the set of targets covered by $p_{j}$
$S\left(p_{j}\right)=\max _{t_{i k} \in T_{p_{j}}}\left(\operatorname{sep}\left(p_{j}, t_{i k}\right) \mid 1 \leq j \leq n\right)$
where $T_{p_{j}}^{2}$ is the set of target pairs separated by probe $p_{j}$.
Function $C$ favors the selection of probes that $c_{\min }$-cover dominated targets. Target $t_{i}$ dominates target $t_{j}$, if $P_{t_{i}} \subset P_{t_{j}}$. Function $S$ favors the selection of the probes that $s_{\min }$-separate dominated target pairs. Target pair $t_{i j}$ dominates target pair $t_{k k}$, if $P_{t_{i j}} \subset P_{t_{k i}}$. The functions $C\left(p_{j}\right)$ and $S\left(p_{j}\right)$ have been defined as the maximum between the values of the function cov and sep, respectively.

The functions cov and sep have been defined over $P \times T$ and $P \times T^{2}$, respectively, as follows:
$\operatorname{sep}\left(p_{j}, t_{i k}\right)=\left|h_{i j}-h_{k j}\right| \frac{s_{\min }}{\left|P_{t_{i k}}\right|}, \quad p_{j} \in P_{t_{k}}, \quad t_{i k} \in T^{2}$
$\operatorname{cov}\left(p_{j}, t_{i}\right)=h_{i j} \frac{c_{\min }}{\left|P_{t_{i}}\right|}, \quad p_{j} \in P_{t_{i}}, \quad t_{i} \in T$
where $P_{t j}$ is the set of probes hybridizing to target $t_{i}$, and $P_{t i k}$ is the set of probes separating target-pair $t_{i k}$.

Value of $\operatorname{sep}\left(p_{j}, t_{i k}\right)$ is what $p_{j}$ can contribute to satisfy the separation constraint for target-pair $t_{i k}$. Value of $\operatorname{cov}\left(p_{j}, t_{i}\right)$ is the amount that $p_{j}$ contributes to satisfy the coverage constraint for target $t_{i}$. Hence, $S$ and $C$ are the maximum values that $p_{j}$ can contribute to satisfy the minimum separation and coverage constraints, respectively.

The selection function $D\left(p_{j}\right)$ which has been defined as follows will indicate the degree of contribution of $p_{j}$ to the minimal solutions
$D\left(p_{j}\right)=\max \left(C\left(p_{j}\right), S\left(p_{j}\right) \mid 1 \leq j \leq n\right)$
The probes with high value of $D\left(p_{j}\right)$ are good probes that will be selected for the solution probe set. The coverage and separation functions of DRC have been calculated for the target-probe incidence matrix of Table 2, in Tables 3 and 4, respectively [23].

The DRC algorithm consists of three phases of: Initialization, Construction, and Reduction (see Algorithm 2).

In the initialization phase, the $D(p)$ value is computed for each probe of the original probe set. The probes for which $D(p)=1$ are added to an initial probe set $\left(P_{\text {ini }}\right)$. This probe set is most probably a non-feasible solution. Therefore, in the construction phase (Algorithm 2), high-degree (high-value in $D$ ) probes are added to the initial probe set repeatedly until we obtain a feasible solution $\left(P_{\text {cow }}\right)$. In the Reduction phase (Algorithm 2), the low-degree (lowvalue in $D$ ) probes are removed repeatedly, as long as, the feasibility of the solution is not disturbed. At the end of this phase, we may obtain a minimal feasible solution $\left(P_{\text {red }}\right)$.

Algorithm 2. Dominated row covering heuristic
Input: $T=\left\{t_{1}, \ldots, t_{m}\right\}, P=\left\{p_{1}, \ldots, p_{n}\right\}$, and $H=\left\{h_{i j}\right\}$
Output: Near-minimal solution $P_{\min }$

## Begin

## ["Initialization Phase"]

Compute $D(p)$ for all $p \in P$ using Eqs. (8)-(10)
$P_{\text {ini }} \leftarrow\left\{p \in P\left[D(p)=1\right]\right\}^{\star}$ essential probes only* $/$
["Construction Phase"]
$P_{\text {red }} \rightarrow P_{\text {ini }}$
Sort $P \backslash P_{\text {red }}$ in decreasing order of $D(\nu)$
for each target $t_{i}$ not $c_{\min }$-covered by $P_{\text {red }}$ do
$n_{i} \leftarrow \#$ probes needed to complete $c_{\min }$-coverage of $t_{i}$
$P_{\text {red }} \leftarrow P_{\text {red } \sim} / L_{i=1}^{i=n_{i}}$ \{next highest-degree probe $p_{j} \in P \backslash P_{\text {red }}$ that covers $t_{i}\}$

Table 2
Target-probe incidence matrix.

Table 3
Coverage function table: $C$ has been calculated based on the DRC definition.
Table 4
Separation function table: $S$ has been calculated based on the DRC definition.
## end

for each target-pair $t_{t k}$ not $s_{\text {min }}$-separated by $P_{\text {sol }}$ do
$n_{\mathrm{tk}} \leftarrow \#$ probes needed to complete $s_{\text {min }}$-separation of $t_{t k}$
$P_{\text {sol }} \leftarrow P_{\text {sol }} / / U_{t=1}^{t \rightarrow n_{\mathrm{k}}}\{$ next highest-degree probe $p_{\mathrm{t}} \in P \backslash P_{\text {sol }}$ that
separates $\left.t_{t k}\right\}$
end
['Reduction Phase' $]$
$P_{\min } \leftarrow P_{\text {sol }}$
$H \leftarrow H / p_{\text {sol }} ; \quad{ }^{\prime}$ restriction of $H$ to probes in $P_{\min }{ }^{\prime}$ /
Compute $D(p)$ for all $p \in P_{\text {min }}$.
Sort $P_{\text {del }} \leftarrow\left\{p \in P_{\min }\right\} D(p)<1\}$ in increasing $D(p)$
if $P_{\min } \backslash\{p\}$ is feasible for each $p \in P_{\text {del }}$ then
$P_{\min } \leftarrow P_{\min }\{p\}$
end
Return final $P_{\text {min }}$
end

### 6.1. The combination of BOA and DRC

As mentioned, we have applied the modified version of BOA to the non-unique probe selection problem. In this version, we have integrated BOA with the DRC heuristic described above. The minimum set of probe should satisfy the coverage and separation constraints. Since the probe set found by BOA does not guarantee the constraints satisfaction, we have applied DRC heuristic in order to guarantee this issue. As mentioned, in each iterative step of BOA, a sample of solutions is generated. Each solution is a string of 0 and 1 which represents a set of probes. Each position in the string represents the presence or absence of a probe in the solution which is noted by 1 or 0 , respectively.

After generating the sample of solutions, the feasibility of each solution should be guaranteed by computing the DRC heuristic. Hence, every solution generated by BOA in the current sample, is transformed by applying the heuristic, in order to respect the coverage and separation constraints.

In order to apply the Bayesian optimization algorithm, the objective(s) to be optimized should be determined. An objective is a function that measures the quality of the solutions for the given problem, and this measure will help explore the search space efficiently in order to find good solutions that optimize the objective. In single target case, the goal is minimization of the probe set. In multiple targets case, in addition to this goal, we want to maximize the ability of the found probe set in identifying several targets in the sample. These can be defined as the objective(s) for the BOA. Therefore, for the first goal, we use inverse of the length of a solution as our objective function. The length of a solution corresponds to the cardinality of probe set, and it is given by the number of ones in the solution. For the second goal, in the multiple targets case, we use a modified version of the decoding idea (see Section 8).

## 7. Multiobjective optimization

Multiobjective optimization refers to optimization problems with several separate objectives [1]. In these problems, each solution has a value for each objective. In other words, each solution has several objective values. The immediate problem caused by this property is how to judge about the overall fitness of solutions. For instance, a solution may have good values for some of the objectives, and have weak values for other objectives. Another solution may have average values for all the objectives. Which of these solutions is better? This major problem, especially
cause the evolutionary-based optimization algorithms to be confused in convergence to the optimal solution [1]. There is no clear way to compare the quality of the solutions in this case. In such cases, a classical approach is to make a weighted sum over all the objectives and try to make a single compound objective to be able to judge about the overall fitness of the solutions. There are two major problems for this approach. First, finding the appropriate weights for each objective is not a trivial problem itself. Assigning wrong weights may cause the evolutionary-based algorithm to converge to an unacceptable solution. Second, sometimes assigning weights to separate objectives and combining them is as meaningless as comparing very different criteria and trying to judge which is better than the other. The literature approach this problem as a ranking problem, and different methods are proposed and examined in order to solve this problem.

In solving the non-unique probe selection problem in multiple targets case, we consider two major objectives. First objective is minimizing the cardinality of the probe set. Second one is maximizing the ability of recognizing multiple targets existing in the sample by selecting the most appropriate probes. These two objectives are somewhat contradictory. We know that in case of selecting more probes, the ability of probe set in recognizing the targets in the sample increases. Therefore, we decided to use one of the multiobjective optimization approaches for solving this problem, instead of combining these two objectives and making one single objective.

Bentley and Wakefield [1] have mentioned an important property for an appropriate ranking method for evaluating the solutions in multiobjective optimization problems. This property is range-independent. In most of the complex multiobjective problems, each objective has an effective range, and the function ranges is non-commensurable [19]. As a result, in case of combining different objectives and making one single objective from them, it is possible that the compound fitness is influenced by the values of the objectives of a larger range more than the objectives of smaller ranges. Hence, in order to ensure that all the objectives are treated equally, either all the objective ranges should be the same in order to make them commensurable, or the method should ensure that objectives are not directly compared with each other.

Bentley and Wakefield [1] have proposed six ranking methods for multiobjective optimization problems: three range-dependent and three range-independent. The most important one is weighted average ranking (WAR). In this method, the fitness values of the solutions for each objective are extracted and listed separately. The lists are sorted, and based on the position of each fitness value, a rank is assigned to the fitness value of the solution. For each solution, different ranks obtained by sorting each list of objectives is averaged. Since each objective has been treated separately, this method is range-independent.

Corne and Knowles [2] have evaluated seven ranking methods using a multiobjective evolutionary algorithm in cases of having $5,10,15$, and 20 objectives. They have shown that the method of average ranking AR (modified version of the WAR of Bentley and Wakefield) outperforms the other algorithms in most cases. Based on their results, they recommended using this method for the 2-5 objectives problem.

We have applied this method in our experiments of twoobjective problem for solving the non-unique probe selection problem in the multiple targets case. By applying multiobjective optimization technique with BOA, we have provided a framework for the problem of non-unique probe selection. New objectives for the problem which result from further studies based on the nature of the problem can be added to the framework easily.

## 8. Decoding

The decoding method proposed by Schliep et al. [18], uses a Bayesian framework to infer the presence of the targets in the sample. The method is based on Monte Carlo Markov Chain sampling and it explicitly allows for experimental errors. Assume a probe set of $\left[p_{1}, \ldots, p_{n}\right]$ as the solution of non-unique probe selection, and a result vector $r=\left(r_{1}, \ldots, r_{n}\right)$ in which each $r_{i}$ corresponds to the result of hybridization ( 0 or 1 ) of the current sample of targets to the probe $p_{i}$. Given the mentioned result vector, the posterior probability that a set of targets $S$ includes all the targets present in the sample is calculated by

Bayes formula as follows:
$P[S \mid r]=\frac{P[r \mid S] P[S]}{P[r]}$
$P[r \mid S]$ is the probability of observing the result vector $r$, while all and only targets of set $S$ are present in the sample. In order to formulate the $P[r \mid S]$, two assumptions were made. First, the probability of observing a specific result is only related to the number of targets from the set $S$ that a probe binds to. Second, the observed binding results of probes are independent from each other. Based on these assumptions, Schliep et al. [18] have defined the $P[r \mid S]$ as
$P[r \mid S]=\prod_{p_{i}} f\left(r_{j},(S \mid j) \cap S\right))$
where $S(j)$ is the set of targets probes $p_{i}$ hybridizes to and $[S(j) \cap S]$ is the number of targets probe $p_{j}$ hybridizes to and also are in the target set $S$. Note that $r_{j}$ is either 0 or $1 . f(0,0), f(0, \geq 1), f(1,0)$, and $f(1, \geq 1)$ are different cases that this function will have. Considering $f_{p}$ and $f_{n}$ as false positive and false negative rates of the targetprobe hybridization experiments, four cases of $f_{r}$ mentioned above, were set to $1-f_{p}, f_{n}, f_{p}$, and $1-f_{n}$, respectively.

A prior probability $(P[S])$ is assigned to every set $S$ from the set of all subsets of the original targets set. This is the probability of finding only the targets of set $S$ in the sample. The prior probability of observing $k$ different targets in a sample is denoted by $c_{k}$, and the abundance of each target $t_{i}$ in samples including more than one target is denoted by $f_{r}$. Hence, the prior probability has been defined as
$P[S] \times c_{S} ; \prod_{t_{i}<S} f_{t_{i}}\left(f_{r} \mid t_{i}-f_{r}\right)$
In the non-unique probe selection, we are interested in calculating the probability of presence of target $t$ in the sample, given the result vector $r$. This can be shown by the marginal $p\left[t_{i} \mid r\right]$ which can be calculated by the posterior of set $S$ over all sets $T$ that include targets $t$
$P\left[t_{i} \mid r\right] \propto \sum_{s, t>S} P[S \mid r]$
Since $P[r]$ is not available, the posterior cannot be computed directly. On the other hand, computing the above equation requires an exponential time in terms of the number of targets. Therefore, the proposed method for this problem by Schliep et al. [18] is Markov Chain Monte Carlo. By sampling a sufficient number of sets $S_{k}$, the marginal $P\left[t_{i} \mid r\right]$ can be estimated as the frequency of observing $t$ in the sets $S_{k}$. A Markov chain is constructed over all possible sets $S$, which is the space of all subsets of the original target set. By choosing $P[S \mid r]$ as the stationary distribution, Gibbs sampling is applied in this approach. The Markov chain is guaranteed to converge to a stationary distribution. After convergence, the relative frequency of the targets $t_{i}$ in the states $S_{k}$ that chain visited is used in estimation of the marginals $P\left[t_{i} \mid r\right]$.

The decoding software was provided to us by Dr. Schliep. We changed the software in order to use the decoding as one of our objectives in the optimization problem. In order to measure the ability of each probe set, obtained by BOA, in identifying a set of targets in the sample, we select a set of true targets. We introduce the experimental errors to the model. This also helps in solving the non-unique probe selection problem more realistically. The probes that hybridize to the true targets are assumed to be true positives. In experiments, we considered $f_{n}=0.05$ and $f_{p}=0.05$. We removed probes from the positive true probes according to the false positive rate, and also add probes to the positive probes set according to the false negative rate.

The obtained design (probe set) is the input for the decoding software, and the output is a ranked list of targets based on the probability of their presence in the sample. We examine the ranked list in order to find the true targets among them. We assume that a given set of targets are carefully identified if in the ranked list of all targets predicted by the decoding algorithm, the true targets existing in the sample are the only ones ranked in the first top positions. Based on this, we defined the decoding related objective for BOA.

In our experiments, we randomly select a subset of the original target set as the true targets set. For $l$ randomly selected targets, there are $l$ possible top positions of $0,1,2, \ldots, l-1$. We search the sorted list of targets produced by the decoding algorithm for the $l$ true targets, and their positions. Hence, we will obtain a list of positions: $p o s_{1}, p o s_{2}, \ldots, p o s_{l}$. The objective $O b j_{\text {dec }}$ is defined as following:
$O b j_{\text {dec }}=\frac{1}{\sum_{l=1}^{l} p o s_{l}}$
Hence, the maximum value for this objective happens when all the true targets are ranked in the top $l$ position of the list. In this case, the summation is calculated as: $((l-1) \times l) / 2$. We examine at most 100 targets of the sorted list. In case of not finding the true targets in the sorted list, their position value is set to 100 . Therefore, the maximum value for the positions summation, which corresponds to the minimum value for the objective, is equal to: $1 \times 100$. In this case, none of the initial true targets are found in the ranked list of the targets.

## 9. Results of computational experiments

We combined BOA with DRC heuristic for solving the nonunique probe selection problem for both cases of single target and multiple targets in the sample. In the single target case, as presented in [20], the results of applying our method indicated that we are able to improve the results obtained by the best methods in literature.

We have extended our method, using a multiobjective optimization technique, in order to cover the multiple targets case which is a more realistic problem. Since our method is basically a time-consuming one, we have applied message passing interface (MPI) technique [7] in order to decrease the execution time of the program. The MPI is a library of methods for distributed computing. It should be noted that since microarray design is not a repetitive task, the execution time of the method used for obtaining a good design is not important. Hence, different methods applied for the problem have been compared based on the cardinality of the final obtained probe set, and not the computational time. The experiments were written in $\mathrm{c}^{\star \star}$ and conducted on Sharcnet systems [26].

The parameters of coverage and separation constraints ( $c_{\min }$ and $s_{\min }$ ) were set to ten and five, respectively. We calculated the appropriate sample size by applying the condition of convergence

for the BOA which was mentioned in Section 5. While $n$ is the number of variables, the sample size should be of $O\left(2^{n} n^{105}\right)$. The number of variables is equal to the number of real and virtual probes for each dataset in this problem. The virtual probes are added to the datasets to guarantee the feasibility of the original probe set. The feasibility is defined in terms of satisfying the coverage and separation constraints.

In all the experiments, we set the variable $k$ to two. This parameter is equal to the maximum number of incoming edges to each node of the Bayesian Network used in the BOA software [27] to model every sample of the search space. Other parameters of BOA software have been set to their default values. For instance, the percentage of the offspring and parents in the sample was set to 50 .

### 9.1. Data sets

We have performed the experiments on ten artificial datasets called $a_{1}, \ldots, a_{5}, b_{1}, \ldots, b_{5}$, and two real datasets HIV1 and HIV2. All previous studies mentioned in Section 3 have been conducted on the same datasets, except for the HIV1, and HIV2 that have not been used in [9], [10]. As mentioned, the datasets are the targetprobe incidence matrices. Properties of the datasets are presented in Table 5. Along with this information, the number of virtual probes required for each dataset has been noted.

Single target in sample the results of applying this approach for the case of single target are presented in Table 6. For this case,

Table 5
Properties of the datasets used for experiments.

The first ten are artificial, and the last two ones are real. Number of targets, probes, and virtual probes are noted by ([T]), ([P]), and ([V]), respectively.

Table 6
Comparison of the cardinality of the minimal probe set for different approaches: Performance of various algorithms evaluated using ten datasets with different number of targets ([T]), probes ([P]), and virtual probes ([V]).

Column DRC-GA and BOA+DRC contain the least obtained cardinalities in several runs.
as mentioned in the [20], BOA was executed for 100 iterations. We have noted our approach by BOA+DRC, and compared it to the other methods in literature. Comparison is based on the number of probes in the final solution obtained by each method. Three columns have been included related to experiments performed by state-of-the-art approaches integer linear programming (ILP) [9], [10], optimal cutting plane algorithm (OCP) [16], and genetic algorithm (DRC-GA) [22].

The illustrated results in Table 6 for algorithms DRC-GA and BOA+DRC are the best obtained results among several runs of the program. Since these optimization methods are evolutionarybased ones, and randomization is used in construction of the first sample of solutions, the programs should be run several times.

Table 7 contains information regarding five runs of BOA+DRC on the non-unique probe selection problem in case of single targets in the sample, and the minimum, average, and the maximum of the obtained results are noted by min, ave, and max in the table, respectively.

As shown in Table 6, the results obtained by the Ragle et al. [16] (noted as OCP) are considered as the best ones in the literature for the non-unique probe selection problem. On the other hand, the results of Wang et al. [22] (noted as DRC-GA) are comparable to (and in most cases better than) [16].

We have been able to improve the result of non-unique probe selection for dataset HIV2, and obtain the shortest solution length of 474. The results we obtained for datasets $a_{1}, a_{2}, a_{4}$, and HIV1 are also equal to the best results calculated for these datasets in the literature. Table 8 summarizes and presents comparison between our method and each of the three mentioned.

### 9.2. Multiple targets in sample

As mentioned, we have extended our method to cover the case of multiple targets for the non-unique probe selection problem. We applied the multiobjective optimization technique presented in Section 7, and measured the ability of the probe set in

Table 7
Minimum, average and maximum cardinality of obtained probe sets by optimization algorithm over five runs of program.
Table 8
Comparison between BOA+DRC and ILP, OCP, and DRC-GA: Number of datasets for which our approach has obtained results better or worse than or equal to methods ILP, OCP, and DRC-GA.
identifying a predetermined number of random targets in the sample as the second objective for our optimization problem. This ability was measured by applying the decoding idea described in Section 8.

The experiments were conducted in two main series of identification of five and ten targets, and identification of 15 and 20 targets in the sample. All experiments were performed while the number of generations for BOA was set to 40 , and the BOA was combined with only the DRC heuristic in these experiments. Regarding the decoding program, we have set the number of warm-up steps and total steps 5000 and 50,000, respectively [18].

### 9.2.1. Identification of five and ten targets

In the first series of experiments, the goal was set to measure the ability of the solutions in identifying five and ten targets in the sample. The results are presented in Table 9. It should be mentioned that the cardinality of probe sets presented in this table are the best ones in three runs of the program for each dataset.

In the first step of experiments, we chose to measure the ability of the solutions in identifying five random targets in the sample. Investigating the obtained results, we realized that the identification ability of the solutions are higher than the expectation, and a randomly selected probe set (in first iteration of BOA) is able to identify five targets in the sample for all the datasets.

As presented in Table 9, the length of the minimal solutions (or number of probes in final probe sets) for all datasets are greater than what we achieved in one-objective optimization problem (Table 6). This is expected in multiobjective optimization. The optimization algorithm should compromise between optimizing each of the two objectives. Therefore, this is natural that objective length has not been minimized as before, especially while the two objectives are in contradiction with each other. As mentioned, a larger set of probes results in better decoding ability.

In next step, we decided to increase the number of the targets to ten in order to make a more difficult optimization problem. Even in this case, our observation was similar to the previous step regarding objectives length (cardinality of the probe sets) and decoding ability.

As mentioned before, we have set the separation constraint ( $s_{\text {min }}$ ) to five. By applying the DRC heuristic (6) in our method, we guarantee the separation of all pairs of targets by at least five probes. Enforcing this constraint improves the decoding ability of the obtained probe sets by our method; But the number of targets that can be identified by the probe sets is not known and should be investigated. Therefore, by performing the mentioned experi-

Table 9
Cardinality of minimum probe set obtained by applying the BOA+DRC in case of multiple targets in the sample-two cases of five and ten targets in the sample were considered.

ments in case of five and ten targets in the sample, in fact, we determined the number of targets that can be identified by the probe sets obtained by our method.

We assumed that the problem of decoding could be modified to discovering a threshold for the difficulty of decoding for each dataset. That is, we can examine further in order to find the maximum number of multiple targets that can exist in the sample, and the solutions generated by our method can identify them properly. Finding this threshold and increasing it will make difficult enough optimization problems. We expect to obtain larger sets of probes by solving these optimization problems, as the reason was explained; But the obtained probe sets will have the ability of identifying larger numbers of targets in the sample which will be more realistic. We conducted another series of experiments to investigate our assumption more carefully (see Section 9.2.2).

### 9.2.2. Identification of 15 and 20 targets

Since the obtained probe sets by our method had a high ability to identify multiple targets in the sample, we tried to increase the number of targets in the sample, make a more difficult optimization problem and find the difficulty threshold of decoding problem for each dataset. Therefore, we examined the problem in case of 15 and 20 targets in the sample.

We conducted new experiments for all the datasets. Our observation about the cardinality of the obtained probe set in these two cases (of 15 and 20 targets) was the same as the cases of five and ten targets, that is, here, the obtained probe sets by multiobjective optimization are larger than the obtained probe sets by one-objective optimization problem, too.

Tables 10 and 11 contain the maximum, minimum, and average decoding scores obtained by three runs of our optimization program for all the datasets in cases of 15 and 20 targets in the sample, respectively.

Our observations of decoding ability of the probe sets were interesting. We realized that our attempt to find a difficulty threshold for the decoding problem was right. Not only we could find this threshold for some datasets, but also, by applying our proposed multiobjective framework, we could improve the decoding ability of the probe sets significantly. For instance, the improvements of the decoding score (in case of 15 targets) in 40 iterations of BOA for dataset $a_{3}$ is shown in Fig. 1.

In this figure, the maximum decoding score obtained in each iteration of BOA is presented. The maximum possible decoding score for the case of 15 targets is obtained when all the targets are identified by the probe set as the top 15 positions. Therefore, the value of the maximum score is $(1 / 105) \approx 0.009524$. As shown in

Table 10
Minimum, average, and maximum of decoding score obtained by three runs of the optimization program for the case of 15 targets in the sample.
Table 11
Minimum, average and maximum cardinality of obtained probe sets by optimization algorithm over three runs of program for the case of 20 targets in the sample.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Maximum decoding score for dataset a3 in 40 iterations of multiobjective optimization in case of 15 targets in the sample.
the figure, the maximum decoding score in iterations has been improved from 0.005235 to the maximum possible decoding score 0.009523 . This indicates that our method has been able to solve this optimization problem quiet efficiently.

As described in Section 8, the inverse of the maximum decoding score in case of 15 targets $\left(\frac{0.009523}{0.009524} \approx 105\right)$ is the summation of the targets positions. Therefore, $\left(\frac{105}{15} \approx 7\right)$ indicates the average targets positions in the optimal case. By inversing the decoding score, and dividing it by the number of targets in the sample, we calculate the average targets position corresponding to the decoding score

$$
\text { Average targets position }=\frac{\sum_{i=1}^{i} p o s_{t_{i}}}{l}, \quad 1 \leq i \leq l
$$

where $t_{i}$ is the target existing in the sample, and $l$ is the number of targets in the sample.

The average targets position can be used for comparing the obtained results by different experiments. In order to show the targets identification improvements obtained by the multiobject-
Table 12
Comparing the average decoding score (ave. decoding score) of the optimal probe set obtained by one-objective optimization with the maximum decoding score (max. decoding score) obtained by the multiobjective optimization in case of 15 targets in the sample.

The average target position (ave. target position) corresponding to each score is also presented. Maximum possible decoding score ( 0.009523 ) has been obtained for almost all the datasets except for a1 and HIV1.
tive method, we calculated the decoding score for the optimal probe sets obtained by one-objective optimization problem (see Section 9.1), and averaged the score over 50 runs for each of the five datasets $\left(a_{1}, \ldots, a_{5}\right)$. We compared the calculated score with the maximum score obtained by multiobjective optimization. In all cases, considerable improvements were noticed. The scores and their associated average target position are demonstrated in Table 12. For instance, the average target position identified by the optimal probe set obtained in case of single target in sample, for dataset $a_{3}$, is 49.93 . By applying multiobjective optimization method, we have improved this value to its best possible value (7) in case of 15 targets in the sample.

It should be noted that although the decoding ability of the probe sets has been significantly improved comparing with the probe sets obtained in single target case, the decoding score has not been improved considerably, during 40 iterations, for the dataset a1. The problem of identifying 15 targets in the sample can be considered a difficult problem for this dataset, and further attempts are required in order to solve this problem more efficiently.

The same calculations can be conducted for the case of 20 targets in the sample (see Table 13). The maximum decoding score in this case is $\frac{1}{190} \approx 0.005263$. 190 which is the summation of 20 targets positions results in $\frac{190}{15} \approx 12.67$ average target position for this case.

As presented in Table 13, comparing with the optimal probe set obtained by the one-objective optimization, probe set obtained by two-objective framework has higher ability in identification of targets. The maximum decoding score after 40 iterations of two-objective method is always greater than the average score calculated for the optimal solution obtained by oneobjective optimization.

Since the optimization problem in case of 20 targets is a difficult problem, we did not notice a significant improvement in the value of decoding objective during the 40 iterations of our method for any of the datasets. It means that the current configuration of BOA is not able to solve this problem efficiently. Therefore, we should try to find a better BOA configuration to solve this case more efficiently. The possible modifications can be performed on the number of iterations of BOA.

On the other hand, we think that we should investigate the impact of the parameter 'maximum incoming edges' on the decoding objective. The maximum incoming edges (see Section 5), determines the level of dependency among variables in BOA.

Table 13
Comparing the average decoding score (ave. decoding score) of the optimal probe set obtained by one-objective optimization with the maximum decoding score (max. decoding score) obtained by the multiobjective optimization in case of 20 targets in the sample.

The average target position (ave. target position) corresponding to each score is also presented. The maximum possible decoding score (0.005263) has been obtained for dataset $b 4$ and almost $b 1$ and $b 3$.

Table 14
Comparing cardinality of the minimum probe set obtained by one-objective optimization problem and the cardinality of the solution with the maximum decoding score in case of 20 targets in the sample.

### 9.2.3. Comparison between optimized and random solutions of same length

Following the experiments illustrated in Section 9.2.2, we performed another series of interesting experiments on the dataset $a_{3}$, all the datasets of $b$-series, and HIV-datasets.

As mentioned before, the minimal length of solutions or the cardinality of the minimal probe set obtained by our multiobjective optimization framework is more than the minimal length obtained by the one-objective optimization approach. Furthermore, the solution with the minimal number of probes is not necessarily the one with the best decoding score.

In Table 14, the minimum length obtained in case of single target in the sample (experiments of Section 9.1 and Table 6) for some datasets are demonstrated. Along with these, the length of the solution with the maximum decoding value in case of 20 targets in the sample is indicated for mentioned datasets in Table 14. It should be mentioned that for both cases of single and multiple targets in the sample, the best (minimum) obtained probe set cardinality among several experiments has been provided.

We conducted a new comparison to illustrate the efficiency of our approach, as follows. We chose the minimum set of probes obtained by the one-objective optimization approach for each dataset, and added random probes to this set as far as constructing a set of the same cardinality mentioned in the third column of Table 14. Then, the decoding score of the resulted probe set, for each dataset, was compared with the obtained maximum decoding score in the case of 20 targets. The result is illustrated in Table 15.

Table 15
Comparing the decoding ability of the optimized solution in case of 20 targets in the sample to the decoding ability of a random solution of the same length.

As noted in Table 15, in the second column, decoding score of a random solution of the same length of the optimal solution obtained by our two-objective framework is illustrated. In the third column, the maximum decoding value obtained for the case of 20 targets in the sample is shown. Comparing these two values for each dataset, it can be noticed that a considerable increase has been obtained by applying the optimization algorithm.

As mentioned before, by increasing the number of the probes, the decoding ability of the probe set also increases; We noticed that by increasing the cardinality of the probe set, the decoding ability did not increase as much as when we apply our optimization algorithm. This proved the efficiency of our algorithm from another aspect.

## 10. Complexity

Among the works on the non-unique probe selection problem in the literature, we notice [3], [21] which have discussed the problem complexity theoretically, and do not contain and illustrate any results obtained by an implementation of a specific method.

The three mentioned works have been focusing on the minimization problem resulted from investigating the nonunique probe selection problem, and applying group testing approach in order to solve it. In this case, the minimization problem is considered as finding a $d$-disjunct submatrix of a given binary matrix. The submatrix should contain the same number of the columns, but the minimum number of rows.

According to the group testing approach, the columns of the matrix are same as the targets in non-unique probe selection problem, and the rows are the pools which are same as the probes

which hybridize to the targets. The definition of this binary matrix corresponds to the definition of the target-probe incidence matrix.

In a binary $d$-disjunct matrix, any union of the $d$ columns cannot contain the $(d+1)$ th column. Wang et al. in [21] have proved and concluded that, first, minimum $d$-disjunct submatrix problem (MIN-d-DS) is polynomial-time solvable in the case that all pools have size two, and second, this problem is MAX SNPcomplete in the case that all pools have size at most two, and there is a polynomial-time approximation with performance ratio $1+2 /(d+1)$ for $d \geq 1$.

Wang et al. also prove that if the all pools are of size of more than two, MIN-d-DS is still NP-hard, approximations with better performance may exist.

Cheng et al. also in [3] discusses the complexity of the nonunique probe selection based on the minimal $d$-separable matrix problem, which is proven to be $D P$-complete. A generalized decision version of the minimum $d$-separable submatrix problem is the $d$-separable submatrix with reserved rows, and can be solved by a nondeterministic machine. This problem is $\sum_{d}^{d}$-complete.

The base of our optimization framework is the EDA of BOA. The other major components of the presented framework in this paper are: the DRC heuristic and the decoding program. These include the time-consuming parts of the framework. Regarding determining the complexity of the whole framework, complexity of all the components are discussed.

Pelikan [15] discusses the complexity of BOA. The most dominant and time-consuming part of the algorithm is its network construction. As mentioned before, we have always performed the experiments with the parameter maximum incoming edges $k \geq 1$. In this case, the overall complexity of constructing Bayesian network is $O\left(k 2^{k} n^{2} N+k n^{3}\right)$ in which $n$ is number of variables of the problem or the number of probes, and $N$ is the number of the instances of solutions (sample) generated in each iteration of the algorithm. The value of this parameter was discussed in Section 5, based on the convergence condition of BOA. Assuming that $k$ is a constant, the complexity can be rewritten as: $O\left(n^{2} N+n^{3}\right)$.

The complexity of the DRC heuristic has been discussed by Wang et al. in [25]. The dominant part of this algorithms is the Construction phase, and results in complexity of $O\left(n^{2} m^{2}\right)$ in which $m$ is the number of targets and $n \geq m$.

Knill et al. have analyzed the decoding idea based on the Markov Chain Monte Carlo method in [11]. The described software in this work is the base of the decoding program we have applied in our framework. The complexity of decoding a result is proportional to number of steps $\times m \times d . d$ is the average number of pools or probes each target hybridize to. As a routine in the MCMC methods, user can choose the number of warm-up steps and also the number of steps between states that are used for marginals calculations [18].

This analysis indicates that the most dominant component of our framework from running-time aspect is related to the BOA algorithm.

## 11. Conclusions (and future research)

In this paper, we extended the new approach proposed in [20] in order to solve the non-unique probe selection in multiple targets in the sample. In case of single target, our method which is a combination of an EDA named BOA and the heuristic DRC obtains results which compare favorably with the state-of-theart. This method has proved its efficiency compared with other methods.

The case of multiple targets in the sample was specifically the subject of discussion in this paper. Most recent works have been focusing on the single target case in the sample, and ignoring the assumption of multiple targets in the sample. For this case, we applied an extended version of the combination of BOA and DRC [20], and considered a second objective for the problem which was ability of identification of multiple targets in the sample. By applying a modified version of the decoding, we tried to measure the second objective for solutions. We approached this problem as a two-objective optimization problem. Our method is the first one which proposes a multi-objective optimization framework which considers the decoding ability of the obtained probe sets along with the objective of cardinality of the probe sets.

Experiments in case of five and ten targets in the sample were conducted. Examining the results, we realized that identification of five or ten targets is not a difficult problem for the obtained probe sets. The separation constraint ( $s_{\min }$ ) in the non-unique probe selection problem improves the decoding ability of the obtained solutions (probe sets) by our method. Even in first iteration of the algorithm, we can find probe sets that are able to identify five or ten targets in the sample properly.

Since the ability of the solutions obtained by BOA+DRC in identifying the five and ten targets in the sample was already high, we investigated this problem for finding the maximum number of targets that can be identified by the solutions obtained by our method, and improving the ability of decoding. Assumption of 15 and 20 targets in the sample constructed difficult optimization problems. Our method was successful in solving the optimization problem for the case of 15 targets for almost all the datasets except for $a_{1}$ and HIV1, and for the case of 20 targets for dataset $M$ and almost $b_{3}$ and $b_{1}$. Optimization led to obtaining maximum possible decoding ability for the probe sets after 40 iterations.

On the other hand, comparing the decoding ability of the probe sets obtained by one-objective and two-objective optimization, we noticed a significant improvement by applying two-objective framework for both cases of 15 and 20 targets in the sample. Also comparison between the decoding ability of the optimized probe sets and random probe sets of the same length also illustrated the efficiency of this method.

Our experiments were conducted while the parameter $k$ of BOA software was set to two. In future, the experiments can be performed to investigate the impact of increase in parameters such as number of iterations of BOA and level of dependency among variables $(k)$.

Moreover, we believe that our multiobjective-based method makes a flexible framework for the problem of non-unique probe selection. In further studies, it will be interesting to consider new objectives for this problem. For instance, the cost associated to adding a probe to a microarray chip may differ for several probes. Therefore, a third objective of obtaining the least expensive design can be considered for the problem. By applying our proposed approach, it will be possible to embed the new objectives to the problem by using current flexible structure proposed in this paper.

## Acknowledgments

This work is supported by the NSERC grant ORGPIN 341854, the CRC grant 950-2-3617 and the CFI grant 203617. The authors gratefully acknowledge the comments and software TCPD (a modified version of MCPD [28]) provided by Dr. Alexander Schliep and Mr. Ole Schulz-Trieglaff that resulted in improvement of this investigation. We are also thankful of Dr. Pardalos and Dr.

Ragle who kindly provided us the data required for the experiments of the paper.
