# Optimising Cancer Chemotherapy Using an Estimation of Distribution Algorithm and Genetic Algorithms 

Andrei Petrovski<br>School of Computing<br>The Robert Gordon University<br>Aberdeen, UK<br>ap@comp.rgu.ac.uk

Siddhartha Shakya<br>School of Computing<br>The Robert Gordon University<br>Aberdeen, UK<br>ss@comp.rgu.ac.uk

John McCall<br>School of Computing<br>The Robert Gordon University<br>Aberdeen, UK<br>jm@comp.rgu.ac.uk

## ABSTRACT

This paper presents a methodology for using heuristic search methods to optimise cancer chemotherapy. Specifically, two evolutionary algorithms - Population Based Incremental Learning (PBIL), which is an Estimation of Distribution Algorithm (EDA), and Genetic Algorithms (GAs) have been applied to the problem of finding effective chemotherapeutic treatments. To our knowledge, EDAs have been applied to fewer real world problems compared to GAs, and the aim of the present paper is to expand the application domain of this technique.

We compare and analyse the performance of both algorithms and draw a conclusion as to which approach to cancer chemotherapy optimisation is more efficient and helpful in the decision-making activity led by the oncologists.

## Categories and Subject Descriptors

I.2.8 [Artificial Intelligence]: Problem Solving, Control Methods, and Search
; G. 3 [Probability and statistics]: Probabilistic algorithms, Stochastic processes
; J. 3 [Life and Medical Sciences]: Health

## General Terms

Algorithms, Performance, Theory

## Keywords

Estimation of Distribution Algorithms, Evolutionary Computation, Probabilistic Modelling

## 1. INTRODUCTION

Many decision-making activities involve searching through a large space of possible solutions. In the chemotherapy problem we have studied [17], [19], [20], the size of the solution space increases exponentially with the number of de-

[^0]cision variables, the values of which need to satisfy certain feasibility criteria.

The requirements imposed on decision variables often make the structure of a solution space quite intricate - regions of feasible solutions are scattered irregularly throughout the solution space, and only one of these regions contains the optimal solution. To find the optimal solution in such situations becomes a difficult task for conventional optimisation methods (gradient-based or simple heuristics). Similarly, the methods of mathematical programming cannot easily deal with multiplicity of feasible regions in the solution space or complementary constraints. Although a number of advances have been made in the area of solving nonlinear optimisation problems using numerical methods [6], they cannot guarantee finding a feasible solution - let alone the optimal one.

It has been found [14], [19], [25], [26] that Genetic Algorithms show a good and robust performance on a class of non-linear, multi-constrained chemotherapy design problems. However, the field of evolutionary computation is growing, and alternative techniques of computational optimisation are being developed. The advent of probabilistic models for evolutionary computation has led to the development of more efficient algorithms that are able to resolve some of the limitations exhibited by conventional Genetic Algorithms [8]. One such technique that uses probabilistic models is the Estimation of Distribution Algorithm (EDA) [15], which replaces the traditional crossover and mutation operators used by GAs with the estimation and sampling from probabilistic models of each generation [21]. In EDAs, the important patterns or building blocks are identified from the population of promising solutions. A model of the probability distribution is used to preserve those patterns and is explicitly sampled to generate a better population. EDAs are reported to solve problems that are known to be GAhard [16].

Various implementations of EDAs have been proposed in the literature. They can be categorised into three groups: a) univariate b) bivariate and c) multivariate (see [12] for more information). For the purpose of this paper, we will concentrate on an algorithm called Population Based Incremental Learning (PBIL), proposed by Baluja et al. [2], [3]. PBIL is a univariate EDA that uses binary representation of the chromosome. Other univariate EDA include Univariate Marginal Distribution Algorithm (UMDA)[15], compact Genetic Algorithm (cGA) [9], and a recently proposed EDA called Distribution Estimation using Markov Random Fields (DEUM) [24, 23]. Amongst other EDAs, PBIL is one of the


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. To copy otherwise, to republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee.
    GECCO'06, July 8-12, 2006, Seattle, Washington, USA.
    Copyright 2006 ACM 1-59593-186-4/06/0007 ... $\$ 5.00$.

most frequently-occurring algorithm used for solving real life optimisation problems $[7,11]$.

Although studied extensively in theory, only a few realworld applications of EDAs have been reported [1, 22]. The purpose of this paper is to ascertain the applicability of the PBIL to the problem of finding effective chemotherapeutic treatments and to compare its performance with that of the known method, in particular with that of GAs.

The paper is structured as follows. Section 2 introduces the problem of cancer chemotherapy. Section 3 describes the methodology of solving this problem by transforming a chemotherapeutic treatment into a GA/PBIL chromosome. Section 4 presents the experimental results; the final Section 5 discusses the results and concludes the paper.

## 2. OPTIMIZATION PROBLEM OF CANCER CHEMOTHERAPY

Amongst the modalities of cancer treatment, chemotherapy is often considered as inherently the most complex [27]. As a consequence of this, it is extremely difficult to find effective chemotherapy treatments without a systematic approach. In order to realise such an approach, we need to take into account the medical aspects of cancer treatment.

### 2.1 Medical aspects of Chemotherapy

Drugs used in cancer chemotherapy all have narrow therapeutic indices. This means that the dose levels at which these drugs significantly affect a tumour are close to those levels at which unacceptable toxic side-effects occur. Therefore, more effective treatments result from balancing the beneficial and adverse effects of a combination of different drugs, administered at various dosages over a treatment period [19].

The beneficial effects of cancer chemotherapy correspond to treatment objectives which oncologists want to achieve by means of administering anti-cancer drugs. A cancer chemotherapy treatment may be either curative or palliative. Curative treatments attempt to eradicate the tumour; palliative treatments, on the other hand, are applied only when a tumour is deemed to be incurable with the objective to maintain a reasonable quality of life for as long as possible.

The adverse effects of cancer chemotherapy stem from the systemic nature of this treatment: drugs are delivered via the bloodstream and therefore affect all body tissues. Since most anti-cancer drugs are highly toxic, they inevitably cause damage to sensitive tissues elsewhere in the body. In order to limit this damage, toxicity constraints need to be placed on the amount of drug applied at any time interval, on the cumulative drug dosage over the treatment period, and on the damage caused to various sensitive tissues [27]. In addition to toxicity constraints, the tumour size (i.e. the number of cancerous cells) must be maintained below a lethal level during the whole treatment period for obvious reasons.

The goal of cancer chemotherapy therefore is to achieve the beneficial effects of treatment objectives without violating any of the above mentioned constraints.

### 2.2 Problem formulation

In order to solve the optimisation problem of cancer chemotherapy, we need to find a set of treatment schedules, which satisfies toxicity and tumour size constraints yielding at the same time acceptable values of treatment objectives. This
set will allow the oncologist to make a decision on which treatment schedule to use, given his/her preferences or certain priorities. In the remainder of this section we will define the decision vectors and the search space for the cancer chemotherapy optimisation problem, specify the constraints, and particularise the optimisation objectives.

Anti-cancer drugs are usually delivered according to a discrete dosage program in which there are $s$ doses given at times $t_{1}, t_{2}, \ldots, t_{s}[13]$. In the case of multi-drug chemotherapy, each dose is a cocktail of $d$ drugs characterised by the concentration levels $C_{i j}, i \in \overline{1, s}, j \in \overline{1, d}$ of anti-cancer drugs in the bloodplasma. Optimisation of chemotherapeutic treatment is achieved by modification of these variables. Therefore, the solution space $\Omega$ of the chemotherapy optimisation problem is the set of control vectors $\mathbf{c}=\left(C_{i j}\right)$ representing the drug concentration profiles.

However, not all of these profiles will be feasible as chemotherapy treatment must be constrained in a number of ways. Although the constraint sets of chemotherapeutic treatment vary from drug to drug as well as with cancer type, they have the following general form.

1. Maximum instantaneous dose $C_{\max }$ for each drug acting as a single agent:

$$
g_{1}(\mathbf{c})=\left\{C_{\max j}-C_{i j} \geq 0 \vdots \forall i \in \overline{1, s}, \forall j \in \overline{1, d}\right\}
$$

2. Maximum cumulative $C_{\text {cum }}$ dose for drug acting as a single agent:

$$
g_{2}(\mathbf{c})=\left\{C_{c u m j}-\sum_{i=1}^{s} C_{i j} \geq 0 \vdots \forall j \in \overline{1, d}\right\}
$$

3. Maximum permissible size of the tumour:

$$
g_{3}(\mathbf{c})=\left\{N_{\max }-N\left(t_{i}\right) \geq 0 \vdots \forall i \in \overline{1, s}\right\}
$$

4. Restriction on the toxic side-effects of multi-drug chemotherapy:

$$
g_{4}(\mathbf{c})=\left\{C_{s-c f f k}-\sum_{j=1}^{d} \eta_{k j} C_{i j} \geq 0 \vdots \forall i \in \overline{1, s}, \forall k \in \overline{1, m}\right\}
$$

The factors $\eta_{k j}$ in the last constraint represent the risk of damaging the $k^{\text {th }}$ organ or tissue (such as heart, bone marrow, lung etc.) by administering the $j^{\text {th }}$ drug. Estimates of these factors for the drugs most commonly used in treatment of breast cancer, as well as the values of maximum instantaneous and cumulative doses, can be found in [4], [5].

Regarding the objectives of cancer chemotherapy, we focus our study on the primary objective of cancer treatment - tumour eradication. We define eradication to mean a reduction of the tumour from an initial size of around $10^{9}$ cells (minimum detectable tumour size) to below $10^{3}$ cells.

In order to simulate the response of a tumour to chemotherapy, a number of mathematical models can be used [13]. The most popular is the Gompertz growth model with a linear cell-loss effect [27]:

$$
\frac{d N}{d t}=N(t) \cdot\left[\lambda \ln \left(\frac{\Theta}{N(t)}\right)-\right.
$$

$$
\left.\sum_{j=1}^{d} K_{j} \sum_{i=1}^{s} C_{i j}\left\{H\left(t-t_{i}\right)-H\left(t-t_{i+1}\right)\right\}\right]
$$

where $N(t)$ represents the number of tumour cells at time $t ; \lambda, \Theta$ are the parameters of tumour growth, $H(t)$ is the Heaviside step function; $k_{j}$ are the quantities representing the efficacy of anti-cancer drugs, and $C i j$ denote the concentration levels of these drugs. One advantage of the Gompertz model from the computational optimisation point of view is that the equation (5) yields an analytical solution after the substitution $u(t)=\ln (\Theta / N(t))$ [13]. Since $u(t)$ increases when $N(t)$ decreases, the primary optimisation objective of tumour eradication can be formulated as follows [17]:

$$
\underset{c}{\operatorname{minimize}} F(\mathbf{c})=\sum_{i=1}^{s} N\left(t_{i}\right)
$$

subject to the state equation (5) and the constraints (1)(4).

## 3. METHODOLOGY

In this section we are going to explain how the optimisation problem of cancer chemotherapy can be addressed by applying GA and PBIL. In order to make the comparison fair, the binary representation of solutions for both algorithms was used. It has been reported that integer encoding of GA solutions can improve the algorithm's performance [18], but for the purpose of the present study we have implemented Genetic Algorithms using binary representation to make the analysis of comparative results valid.

### 3.1 Binary string representation of the problem

Multi-drug chemotherapy schedules, represented by decision vectors $\mathbf{c}=\left(C_{i j}\right), i \in \overline{1, s}, j \in \overline{1, d}$, are encoded as binary strings known as chromosomes. The representation space $\mathbf{I}$ (a discretized version of $\Omega$ ) can then be expressed as a Cartesian product
$\mathbf{I}=A_{1}^{1} \times A_{1}^{2} \times \ldots \times A_{1}^{d} \times A_{2}^{1} \times A_{2}^{2} \times \ldots \times A_{2}^{d} \times \ldots \times A_{s}^{1} \times A_{s}^{2} \times \ldots \times A_{s}^{d}$
of allele sets $A_{i}^{j}$. Each allele set uses a 4 -bit representation scheme

$$
A_{i}^{j}=\left\{x_{1} x_{2} x_{3} x_{4}: x_{k} \in\{0,1\} \forall k \in \overline{1,4}\right\}
$$

so that each concentration level $C_{i j}$ takes an integer value in the range of 0 to 15 concentration units [19]. In general, with $s$ treatment intervals and up to $2^{p}$ concentration levels for $d$ drugs, there are up to $2^{\text {spd }}$ individual elements. Henceforth we assume that $s=10$ and that the number of available drugs in restricted to ten [17]. These drugs are delivered sequentially - one after another - to form a multi-drug dose, which is administered periodically over the treatment period that consists of up to $s$ cycles. The values $s=10$ and $d=10$ result in the individual (search) space of power $|\mathbf{I}|=2^{400}$ individuals, referred to as chromosomes.

Thus, a chromosome $x \in \mathbf{I}$ can be expressed as

$$
x=\left\{x_{1} x_{2} x_{3} \ldots x_{4 s d}: x_{k} \in\{0,1\} \forall k \in \overline{1,4 s d}\right\}
$$

and the mapping function $m: \mathbf{I} \rightarrow \mathbf{C}$ between the individual $\mathbf{I}$ and the decision vector $\mathbf{C}$ spaces can be defined as

$$
C_{i j}=\Delta C_{j} \sum_{k=1}^{4} 2^{4-k} x_{4 d(i-1)+4(j-1)+k}, \quad \forall i \in \overline{1, s}, j \in \overline{1, d}
$$

where $\Delta C_{j}$ represents the concentration unit for drug $j$. This function symbolizes the decoding algorithm to derive a decision vector from a chromosome $x$. Applying the evaluation function $F$ to $\mathbf{c}$ yields the value of the fitness function for both algorithms.

$$
F(c)=\sum_{p=1}^{n} \sum_{j=1}^{d} \kappa_{j} \sum_{i=1}^{p} C_{i j} e^{\lambda\left(t_{i-1}-t_{p}\right)}-\sum_{s=1}^{4} P_{s} d_{s}
$$

where $d_{s}$ are the distance measures specifying how seriously the constrains (1)-(4) are violated, and $P_{s}$ are the corresponding penalty coefficients. If all constraints are satisfied (i.e. a treatment regimen is feasible), then the second term in (7) will be zero, significantly increasing the value of the fitness function.

### 3.2 Genetic Algorithms

A general GA starts by randomly generating $M$ number of chromosomes to form a population $P$ (also known as parent population). As stated above, each chromosome $x=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$, where $n=4 s d$, is a binary string representing a chemotherapy schedule. $N$ chromosomes are then selected from $P$ according to the quality/fitness of those chromosomes. Various selection mechanisms can be applied for this purpose. In our case we use fitness proportionate selection [8].

Other GA parameters have been chosen on the basis of the previous work, presented in [18], aimed at tuning the GA factors in order to improve the algorithm's performance.

### 3.3 Population Based Incremental Learning

Similarly to a binary GA, PBIL solutions are also bitstring chromosomes. So, in our case, a chromosome $x=$ $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ represents a candidate chemotherapeutic treatment, where $n=4 s d$ is the chromosome length, and each $x_{i}$ is either 0 or 1 .

PBIL starts by initializing a probability vector $p=\left\{p_{1}, p_{2}\right.$, $\ldots, p_{n}$ ] where, each $p_{i}=0.5$. Each $p_{i}$ represents, the probability of 1 being presented in $i^{\text {th }}$ position of a chromosome. $p$ is then sampled $M$ times to create a population $P$ of chromosomes. $N$ chromosomes are then selected from $P$ according to the quality/fitness of that chromosome. As with GA, a number of selection mechanisms can be applied for this purpose. In our case we use truncation selection [12] which is to select the best $N$ solutions from $P$. After selection, the marginal probability $\rho_{i}$ for each $i^{\text {th }}$ allele position is calculated from the selected $N$ solutions. ( $\rho_{i}$ can be simply calculated by dividing the frequency of 1 in $i^{\text {th }}$ position of allele in selected set by $N$ ). $\rho_{i}$ is then used to update the probability vector $p$ (see workflow of PBIL for more detail). This updated probability vector replaces the initial probability vector. This process continues until termination criteria are satisfied.

Workflow of PBIL is shown below:

1. Initialise a probability vector $p=\left\{p_{1}, p_{2}, \ldots, p_{n}\right\}$ where, each $p_{i}=0.5$
2. Sample $p$ to generate an initial population, $P$, of size $M$. 3. Select the $N$ fittest solutions from $P$, where $N \leq M$.
3. For each allele $x_{i}$, calculate the marginal probability $\rho_{i}$ from selected $N$ solutions.
4. Update $p$ using following updating rule:

$$
\begin{gathered}
\text { for } i=1 \text { to } n \text { do } \\
p_{i}=p_{i} *(1-\lambda)+\rho_{i} * \lambda
\end{gathered}
$$

where, $0 \leq \lambda \leq 1 . \lambda$ is known as learning rate parameter [2] chosen by the user.
6. Go to Step 2 until the termination criterion is satisfied.

## 4. EXPERIMENTAL RESULTS

We compare the performance of GA and PBIL on the problem of multi-drug cancer chemotherapy optimization addressed in [14], [19]. Two different measures were adopted to evaluate the performance of each algorithm:

1. Effeicency / Speed: The efficiency of an algorithm can be measured in terms of computational time it takes to find a solution. In the case of evolutionary algorithms, the calculation of the fitness of a particular chromosome (fitness evaluation) is the most computationally expensive task. Therefore, we measure the efficiency in terms of number of fitness evaluations taken by the algorithm to find a solution. In our case, finding a solution means to find at least one feasible solution (i.e. satisfying all the constraints (1)-(4)).
2. The quality of solution: A solution's quality in our case is the value of the fitness function (7) that indicates how successful a particular chemotherapy schedule is in reducing the overall tumour burden. Therefore, the quality of solution is measured in terms of the best fitness, i.e the best chromosome (best schedule that minimises the tumour burden) found by the algorithms.

### 4.1 Efficiency comparison

In the efficiency comparison experiment, each algorithm was run 1000 times and for each run the number of fitness evaluations taken to find at least one feasible solution (i.e. satisfying all the constraints (1)-(4)) was recorded. Run Length Distribution (RLD)[10] curves were plotted to measure the performance (Figure 1). RLD shows, for each algorithm, the cumulative percentage of successful runs that terminated within a certain number of function evaluations.

The parameters for each of the algorithms were chosen either on the basis of the previous work [18] (for Genetic Algorithms) or empirically (for PBIL), taking into consideration the fairness of the comparison.

In accordance with the best GA parameter settings found in [18] for the cancer chemotherapy problem, we used a GA population of 100 chromosomes, one-point crossover with the probability of 0.614 , uniform mutation with probability of 0.075 , and the elitism of two best chromosomes. The algorithm terminates when it finds a feasible solution.

Similarly, PBIL population consisted of 100 chromosomes, the selection size $N$ was 20 , and the learning rate $\lambda$ was 0.3 .

Figure 1 shows that the performance of PBIL was better than the performance of GA. We can see that, for PBIL $90 \%$
![img-0.jpeg](img-0.jpeg)

Figure 1: Experimental results in the form of RLD showing, for each algorithm running on chemotherapy optimization problem, the cumulative percentage of successful runs that terminated within a certain number of function evaluations.
of the runs found feasible solutions within 6,700 function evaluation in comparison with 32,900 function evaluations for GA ${ }^{1}$. Also, the steepness of the RLD curve for PBIL shows that this algorithm is very reliable and finds solutions within a predictable number of function evaluations. At the same time, the gradual slope of the RLD curve for Genetic Algorithms shows that the number of GA fitness evaluations required to find a feasible solution varies for almost every individual run and cannot be predicted accurately.

Table 1: Mean and stdev of the number of fitness evaluations

The mean value and the standard deviation of the number of function evaluations taken by the algorithms over 1000 runs is presented in the Table 1. These results are analyzed by applying a one-tailed t-test that yields the p-value of $<<0.05$ (Table 2), indicating statistical significance of the difference in speed for PBIL and GA.

Table 2: T-test analysis of PBIL and GA mean values
### 4.2 Comparison of Treatment Quality

The goal of the second experiment was to find the best chemotherapeutic regimen within a specified number of function evaluations, which was set to 200,000 . In order to better achieve this goal, the population size of both GA and PBIL was increased to 200 chromosomes. Also, to encourage

[^0]
[^0]:    ${ }^{1}$ A smaller number of function evaluations indicates the ability of an algorithm to find a feasible solution faster.

more thorough exploration of the solution space, the mutation probability of GA was adjusted in accordance with the strategies suggested in [18]. Also, the learning rate of PBIL was decreased to 0.05 .

The results of the treatment quality experiment are presented in Table 3, which shows the mean and the standard deviation of the fitness values found by the algorithms.

Table 3: mean and stdev of fitness

It is evident that the PBIL solution is better than that of GA ${ }^{2}$. This conclusion is supported by a one-tailed t-test applied to the fitness values found by the algorithms and presented in Table 4.

Table 4: Significance test of results on quality of fitness
The p-value in Table 4 indicates that the difference in the best fitness values for PBIL and GA is highly significant. This means that PBIL outperforms GA on the chemotherapy optimisation problem not only with respect to the computational speed of finding a feasible treatment, but with respect to the quality of the found solution as well.

## 5. CONCLUSION

In this paper we have examined the problem of designing efficient chemotherapeutic treatments that satisfy toxicity and tumour size constraints. This problem has been formulated in terms of exploring a vast search space of possible treatment schedules using two computational heuristic algorithms - Estimation of Distribution Algorithm (in the form of PBIL) and Genetic Algorithm.

The heuristic algorithms proposed have been successfully applied to the chemotherapy optimisation problem and were able to find feasible solutions to this problem in a reasonable computational time. Our experimental results show that PBIL outperforms Genetic Algorithms in both the speed of finding a feasible treatment schedule and in the quality of the final solution.

This result can have practical implications. The better quality of the drug schedules found by PBIL can lead to more effective chemotherapeutic treatments. On the other hand, the ability of PBIL to explore the solution space of possible treatments more efficiently, enables us to provide a more helpful decision-support tool using OWCH - the online decision support system described in [14].

Also, a successful application of PBIL in the present context opens the possibility of using multivariate EDAs for designing chemotherapeutic treatments. Multivariate EDAs

[^0]have been shown to perform better on a wider range of optimization problems as they are able to capture the interactions between variables in their probabilistic model. This is particular important in the context of cancer chemotherapy optimisation, where interactions between drugs play a vital role in the overall success of a treatment regimen [5]. We intend to address this issue in the future.
