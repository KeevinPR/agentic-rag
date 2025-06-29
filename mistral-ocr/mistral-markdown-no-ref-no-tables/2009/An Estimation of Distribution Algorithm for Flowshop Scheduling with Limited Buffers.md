# An Estimation of Distribution Algorithm for Flowshop Scheduling with Limited Buffers 

Mansour Eddaly, Bassem Jarboui, Patrick Siarry, and Abdelwaheb Rebaï


#### Abstract

Most of the works that address the flowshop scheduling problem presume unlimited buffers between successive machines. However, with the advent of new technologies in the manufacturing systems, limited capacity storage between machines has become profitable. Aimed at makespan minimization, the flowshop scheduling problem with buffer constraints is NP-hard in the strong sense. Therefore, several approximate algorithms have been proposed in the literature. In this chapter, we propose an Estimation of Distribution Algorithm for solving a flowshop scheduling problem with buffer constraints. The main characteristics of the problem, such as the order of jobs and similar blocks of jobs in the sequence, are taken into account while building the probabilistic model. In order to enrich the search procedure of the algorithm, a skewed variable neighbourhood search algorithm is embedded into it, restricted by a calculated probability which depends on the quality of the created offspring. The computational results show that our algorithm outperforms genetic algorithm and particle swarm algorithm, and can obtain several optimal solutions in a short time.


## 1 Introduction

In a classical flowshop scheduling problem (FSP), each job $j(j=1,2, \ldots, n)$ must be processed on every machine $i(i=1,2, \ldots, m)$ and all the jobs have to pass through all the machines following the same route. In such problems, an infinite buffer size between every two successive machines is assumed. Due to the modernization of

[^0]
[^0]:    Mansour Eddaly, Bassem Jarboui, and Abdelwaheb Rebaï
    FSEGS, route de l'aéroport km 4.5, B.P. No. 1088, Sfax 3018, Tunisie
    e-mail: eddaly.mansour@gmail.com, bassem_jarboui@yahoo.fr, abdelwaheb.rebai@fsegs.rnu.tn
    Patrick Siarry
    LiSSi, Université de Paris 12, 61 avenue du Général de Gaulle, 94010 Créteil, France
    e-mail: siarry@univ-paris12.fr

manufacturing technologies and the emergence of just-in-time manufacturing and Kanban control systems, which maintain a limited in-process inventory, the constraint of intermediate buffers with a limited capacity between every two successive machines is introduced. Therefore, the study of flowshop scheduling with limited buffer storage has become attractive for many researchers [28]. In real world applications, the FSP with limited buffers may occur in industrial production, e.g. petrochemical processing industries and cell manufacturing [31], as well as in computer architecture [13]. Papadimitriou and Kanellakis [21] have proved that this problem is strongly NP-hard with respect to the makespan criterion. Therefore, many approximate algorithms have been developed in the literature for solving the FSP with limited buffers.

With the makespan criterion, Dutta and Cunningham [5] and Reddi [26] have proposed a dynamic programming technique aimed at finding an optimal solution for the problem with two or more machines successively. Leisten [13] has analysed the importance of the limited storage restrictions on the performance of the production systems. Moreover, he has presented several constructive heuristics to solve this variant of FSP. Nowicki [20] has proposed a tabu search approach (TS) by using a non-trivial generalization of the block elimination properties known for the classical FSP. Qian et al. [25] have proposed a differential evolution algorithm (DE) where they developed a rule to convert the continuous version of DE individuals to job permutations. Also, they applied a local search procedure based on the insertion of a part of individuals at each generation. In [31] a genetic algorithm (GA) is adapted to solve the problem where multiple crossover and mutation operators are used simultaneously. Moreover, a decision probability is used to control the utilization of genetic mutation and local search. Liu et al. [14] have presented a particle swarm optimization (PSO) algorithm. They have proposed a new encoding scheme allowing the transition from the continuous values of the PSO to job permutations. A local search procedure and a simulated annealing algorithm (SA) are introduced into the algorithm in order to enrich the search procedure and obtain solutions with good diversity.

In 1996, a new class of evolutionary algorithms was introduced by Mühlenbein and Paaß [19], called Estimation of Distribution Algorithm (EDA). In order to generate a new individual, EDA uses a probabilistic model learned from a population of individuals. Therefore, a distribution of probability is estimated from the selected candidates of the initial population and then new offspring are generated according to this distribution. Finally, according to the quality of the new individual, it is decided whether it will survive in the next generation. Concerning its applications, EDA was devoted to solving several combinatorial optimization problems. A detailed survey of these applications can be found in Larrañaga and Lozano [12], Pelikan [22], and Lozano et al. [15].

In this chapter, we propose an EDA for solving the FSP with limited buffers while minimizing the makespan criterion. Aimed at enhancing the quality of the solution of EDA, it is recommended to use a local search algorithm [15]. The Skewed Variable Neighborhood Search (SVNS) [7] is embedded to the EDA for improving its performance.

# 2 Problem Definition 

In a FSP with limited buffers, there is a set of $n$ jobs to be processed through a set of $m$ machines with the same sequence on all machines and without interruption in the processing (no pre-emption). Let $p_{i[j]}$ be the processing time for the job at position $j$ in the sequence $s$ on the machine $i$, where $j=1,2, \ldots, n, i=1,2, \ldots, m$, $s=\left\{s_{1}, s_{2}, \ldots, s_{n}\right\}$ and $p_{i j}$ are fixed, known in advance and have non-negative values. The intermediate storage constraint implies that between each successive pair of machines $(i-1, i)$ a buffer with limited size $B_{i}$ of unfinished jobs can temporarily stay. Let $D_{i[j]}$ denotes the departure time (starting time) of the job at the $j^{\text {th }}$ position in the sequence on the machine $i$.

The completion time of the last executed job, also known as the makespan $\left(C_{\max }\right)$ can be found through the recursive expression of the departure time as follows:

$$
\begin{aligned}
& D_{1[1]}=0 \\
& D_{1[j]}=D_{1[j-1]}+p_{1[j-1]}, j=2,3, \ldots, n \\
& D_{i[j]}=\max \left(D_{i-1[j]}+p_{i-1[j]}, D_{i[j-1]}+p_{i[j-1]}, D_{i+1[j-B_{i+1}-1]}\right) i=2, \ldots, m, j=2, \ldots, n
\end{aligned}
$$

Thus,
$C_{\max }=D_{n[m]}+p_{n[m]}$
Following this definition, two cases can be discussed. If $B_{i}=0$, the limited buffer constraint disappears and the problem will be transformed into the blocking flowshop scheduling problem [28]. Otherwise, if $B_{i} \geq n-1$, the problem under consideration becomes the classical FSP. Nowicki [20] has presented a detailed analysis of the limited buffer FSP based on a graph representation model.

## 3 An Overview of Estimation of Distribution Algorithms (EDAs)

The framework of the basic EDA [19] can be presented as follows: starting with a randomly generated initial population, one selects a subpopulation of $M$ parent individuals through a selection method based on the fitness function. Next, one estimates the probability of distribution of the selected parents with a probabilistic model. Then, one generates new offspring, according to the estimated probability distribution. Finally, some individuals in the current population are replaced with newly generated offspring. These steps are repeated until a stopping criterion is met.

Three classes of EDA were developed, according to the chosen probabilistic model. The first class consists of models which do not take into account the dependencies between variables of candidate solutions, i.e. all variables are independent. The second class assumes at most two-order dependencies between these variables and the last class assumes multiple dependencies between the variables.

# 3.1 EDAs with No Dependencies 

### 3.1.1 Population-Based Incremental Learning Algorithm (PBIL)

The PBIL algorithm was introduced by Baluja [1]. It involves transforming the population of candidate solutions into a probability vector $p(x)=\left\{p\left(x_{1}\right), p\left(x_{2}\right), \ldots\right.$, $\left.p\left(x_{n}\right)\right\}$ where $p\left(x_{i}\right)$ denotes the probability of a " 1 " in the $i^{\text {th }}$ position of solution bits. In other words, this algorithm checks the proportion of ones in each individual chromosome. All positions are initially equally likely, that is all the probability values are set to 0.5 . In this way, the highest level of diversity will be found [1]. In each iteration, after transforming the population into a probability vector, the PBIL algorithm generates $P_{1}$ solutions according to the current probability. Then, each component of probability vector, $p\left(x_{i}\right)$, is updated according to the following:

$$
p\left(x_{i}\right)=p\left(x_{i}\right)+\alpha\left(x_{i}^{\text {best }}-p\left(x_{i}\right)\right)
$$

where $\alpha \in[0,1]$ is the so-called learning rate and $x_{i}^{\text {best }}$ is the $i^{\text {th }}$ bit in the best solution found so far. Using this update rule, the value of $p\left(x_{i}\right)$ increases when $x_{i}^{\text {best }}$ is equal to " 1 " and decreases otherwise. Furthermore, the values in the probability vector move towards the fittest of the generated solutions. The aim of PBIL is to actively create a probability vector which, with high probability, represents a population of highly evaluated solution vectors. It is worthy to note that each bit is examined independently and thus no interaction is considered.

### 3.1.2 Compact Genetic Algorithm (CGA)

CGA was proposed by Harik et al. [8]. Similar to PBIL algorithm, CGA creates a probability vector from the population of solutions and all vector values are initialized to 0.5 . The update rule used in this algorithm is equivalent to a steady-state tournament selection. So, the procedure is as follows: at each iteration, two individuals are selected at random from the population. These individuals are compared with respect to the fitness values. Then, the probability vector is updated, following this formula:

$$
p\left(x_{i}\right)= \begin{cases}p\left(x_{i}\right)+\frac{1}{p} & \text { if } x_{i}^{\text {best }}=1 \text { and } x_{i}^{\text {worst }}=0 \\ p\left(x_{i}\right)-\frac{1}{p} & \text { if } x_{i}^{\text {best }}=0 \text { and } x_{i}^{\text {worst }}=1 \\ p\left(x_{i}\right) & \text { otherwise }\end{cases}
$$

where $x_{i}^{\text {best }}$ and $x_{i}^{\text {worst }}$ denote the $i^{\text {th }}$ bit in the best and the worst solutions respectively, among the two selected solutions and $P$ is the population size. According to this method of updating the probability, the CGA replaces one candidate solution by another one using a population of size $P$.

Two points of difference between PBIL and CGA can be found. Firstly, the update rule used by CGA depends only on the size of the population. Secondly, the CGA is more profitable in terms of memory requirements. The update phase in CGA requires a constant size of $\frac{1}{p}$ whereas the update rule values in PBIL can take

an arbitrary value in the range $[0,1]$ and the number of values that can be stored in an element of the vector is infinite.

# 3.1.3 Univariate Marginal Distribution Algorithm (UMDA) 

The UMDA was proposed by Mühlenbein et al. [19]. This algorithm works differently compared to PBIL and CGA. The UMDA does not transform the population into a population vector. After generating a population of individuals, UMDA selects some individuals according to their fitness values. Then, it constructs a probability vector through the selected solution. Formally, the probabilistic model used in UMDA can be written as follows:

$$
p(x)=\prod_{i=1}^{n} p\left(x_{i}\right)
$$

Finally, it generates new solutions based on the built probabilistic model. The process is repeated until a termination criterion is met. Although UMDA has different framework than CGA and PBIL, the performances of these algorithms are similar [22].

### 3.2 EDAs with Two-Order Dependencies

### 3.2.1 Mutual Information Maximization for Input Clustering (MIMIC)

MIMIC was proposed by De Bonet et al. [4]. It considers pairwise interactions between the variables in its distribution of probability.

Let $p(x)=p\left(x_{1} / x_{2}, \ldots, x_{n}\right) p\left(x_{2} / x_{3}, \ldots, x_{n}\right) \ldots p\left(x_{n-1} / x_{n}\right) p\left(x_{n}\right)$ denote the true joint probability, and $\hat{p}_{\pi}(x)=p\left(x_{i 1} / x_{i 2}\right) p\left(x_{i 2} / x_{i 3}\right) \ldots p\left(x_{i n-1} / x_{i n}\right) p\left(x_{i n}\right)$ where $\pi\left\{i_{1}, i_{2}, \ldots, n\right\}$ is a permutation of the numbers between 1 and $n$ and $\hat{p}_{\pi}(x)$ is estimated by the marginal and conditional relative frequencies of the corresponding variables within the subset of selected individuals. The aim of MIMIC algorithm is to generate a permutation $\pi^{*}$ that minimizes the divergence between $\hat{p}_{\pi}(x)$ and $p(x)$. This probabilistic model has the framework of a chain. In a sequential way, all positions, except for the first position of the chain, are conditionally dependent on the previous position in the chain. Starting with an initial random population, the MIMIC algorithm selects a set of promising solutions. After that, it computes the marginal and conditional probabilities. Next, MIMIC uses a greedy algorithm, based on Kullback-Leibler information divergence, to maximize mutual information between the adjacent positions in the chain.

### 3.2.2 Combining Optimizers with Mutual Information Trees (COMIT)

COMIT algorithm, proposed by Baluja and Davies [2], also considers pairwise interactions between variables of the problem. Instead of using the shape of a chain in

the probabilistic model, as in MIMIC, this algorithm attempts to present the probability vector through a tree distribution. The probabilistic model, constructed here, can be written as follows:

$$
p(x)=\prod_{i=1}^{n} p\left(x_{i} / x_{j}\right)
$$

where $i$ is a descendant node from $j$. If $i$ is a root node then $p\left(x_{i} / x_{j}\right)=p\left(x_{i}\right)$. The objective is to find a tree that maximizes mutual information between parent nodes and their descendants. In [2], it is shown that COMIT outperforms MIMIC algorithm.

# 3.2.3 Bivariate Marginal Distribution Algorithm (BMDA) 

BMDA was introduced by Pelikan and Mühlenbein [24]. It constitutes a kind of a generalization of both the previous algorithms and UMDA. For constructing the probability distribution, this algorithm uses a set of disjoint tree distributions. The criterion used for measuring the dependencies between variables is Pearson's chisquare statistics using the following:

$$
\chi_{i j}^{2}=M \times \sum_{x_{i}, x_{j}} \frac{\left(p\left(x_{i}, x_{j}\right)-p\left(x_{i}\right) p\left(x_{j}\right)\right)^{2}}{p\left(x_{i}\right) p\left(x_{j}\right)}
$$

### 3.3 EDAs with Multiple Dependencies

### 3.3.1 Factorized Distribution Algorithm (FDA)

FDA was proposed by Mühlenbein and Mahnig [17]. The method involves using an additive decomposition of function (ADF), to decompose the fitness function of the problem and a factorization method, based on Boltzmann distribution which is used to factor the distribution into consistent, conditional and marginal distributions. In such a way, $N$ individuals are generated according to uniform distribution as in UMDA. Then, the Boltzmann selection is used to select $M$ individuals from those generated previously. In addition, the conditional probabilities are estimated from the selected individuals. Finally, $M$ new individuals are generated according to these probabilities. The process is repeated until a termination criterion is met.

### 3.3.2 The Extended Compact Genetic Algorithm (ECGA)

The ECGA [8] is an extension inspired from CGA. It works by partitioning the variables into different partitions by using the so called Marginal Product Model (MPM). This model does not estimate the conditional probabilities as in FDA. However, it includes both univariate marginal distribution as well as multivariate marginal distribution. The form of probability distribution used in MPM can be presented as:

$$
p(x)=\sum_{i \in \Omega} p\left(x_{i}\right)
$$

where $\Omega$ is the set of alleles included in the same partitions. Based on MPM, ECGA uses a greedy procedure in order to obtain the best partitions. At the beginning, MPM assumes that all variables are independent, i.e. all partitions are composed of one element. Then, at each iteration, it merges two partitions together with respect to the Bayesian Information criterion. Finally, when no further possible improvement is obtained, the model used is retained.

# 3.3.3 Bayesian Optimization Algorithm (BOA) 

In [23], the BOA was developed. This algorithm considers multiple interactions among the variables. At first, an initial random population is generated. Secondly, a selected method is chosen to select the promising solutions. Thirdly, a Bayesian Network is constructed from a probabilistic model based on the selected individuals. Formally, an acyclic Bayesian network with directed edges is used in this algorithm. The estimated joint probability can be written as follows:

$$
p(x)=\prod_{i=0}^{n-1} p\left(x_{i} / \Phi_{x_{i}}\right)
$$

where $\Phi_{x_{i}}$ is the set of nodes from which there exists an edge to $x_{i}$. In such way, a variable is sampled after all its parents have already been sampled. In order to evaluate the quality of the constructed network, a metric named Bayesian Dirichlet metric is used by Pelikan et al. [23]. Finally, new offspring are generated according to this network.

### 3.3.4 Learning Factorised Distribution Algorithm (LFDA)

LFDA [18] extends the FDA by using the Bayesian network. Instead of using the ADF structure, as in FDA, LFDA uses the Bayesian network framework to build the probabilistic model. In fact, this algorithm does not need a priori information about the structure of the problem. Therefore, LFDA performs similarly to BOA with the exception of the metric used. In this context, LFDA uses a Bayesian Information Criterion (BIC) in order to assess the network's quality.

### 3.3.5 Estimation of Bayesian Network Algorithm (EBNA)

EBNA was proposed by Etxeberria and Larrañaga [6]. Also, these authors exploit the Bayesian network structure in estimating the joint probability. This algorithm follows the same process as BOA and LFDA. In [11] three different variants of EBNA have been proposed where they differ in the metrics used in the evaluation step. The first one, called $\mathrm{EBNA}_{P} C$, uses Chi square tests to detect the conditional independencies. The BIC criterion is devoted to the second variant $\mathrm{EBNA}_{B I C}$. The last one is called $\mathrm{EBNA}_{k_{2}+p e n}$ which uses the marginal likelihood in order to construct the Bayesian network and a penalty is added to the metric for reducing the complexity of the algorithm.

# 4 Estimation of Distribution Algorithm (EDA) for the Flowshop Scheduling Problem with Limited Buffer 

EDA is a new evolutionary algorithm proposed by Mühlenbein and Paaß in 1996 [19]. Instead of recombination and mutation, EDA generates new individuals with respect to a probabilistic model, learned from the population of parents. To the best of our knowledge, in the literature, there is no application of this algorithm in the scheduling context, with the exception of the work of Jarboui et al. [10]. In this section, we discuss, in detail, our proposed EDA for solving the FSP with respect to makespan criterion.

### 4.1 Encoding Solutions and Initial Population

For encoding the solution, we use the well-known representation scheme for the permutation FSP, which is the permutation of $n$ jobs, where the $j^{\text {th }}$ number in the permutation denotes the job located at position $j$. For the purpose of diversity, the initial population of $P$ individuals is generated randomly.

### 4.2 Selection

The selection procedure adopted in our algorithm consists of two phases. First, the individuals of the initial population are sorted according to their objective function value. Second, $M$ individuals are selected from the subset of $20 \%$ of the best individuals from the sorted list.

### 4.3 Probabilistic Model: Construction of New Solution

The choice of the probabilistic model is closely related to the performance of the EDA [15]. So, it is recommended to carefully construct this model. In this chapter, the probabilistic model is built while taking into account the specific characteristics of the problem under consideration, as in [10]. Therefore, both the order of jobs in the sequence and the similar blocks of jobs presented in the selected parents are considered. In order to construct a new sequence, Jarboui et al. [10] have proposed a probability $\pi_{j k}$ for selecting a job $j$ at position $k$ :

$$
\pi_{j k}=\frac{\eta_{j k} \times \mu_{j[k-1]}}{\sum_{l \in \Omega_{k}} \eta_{l k} \times \mu_{l[k-1]}}
$$

with $\eta_{j k}$ denotes the number of times job $j$ that appears before or at the position $k$ in the subset of the selected sequences plus a given constant $\delta_{1}$. This parameter indicates the importance of the order of jobs in the sequence. $\mu_{j[k-1]}$ denotes the

# EDA Algorithm 

```
Initialize the population \(P\) using random permutation;
loop
    select \(M\) individuals from \(20 \%\) of the best individuals in the population;
    select \(s_{0}\) at random from the \(M\) selected individuals;
    for \(k=1,2, \ldots, n\)
        update \(\Omega_{k}\) using the \(q\) first job not already scheduled from \(s_{0}\);
        compute the probability \(\pi_{j k}\) for each job \(j \in \Omega_{k}\);
        \(s_{\text {current }, k}\) receives the job selected from \(\Omega_{k}\) following the computed probability;
    end for
    if (the fitness of newly created induvidual \(s_{\text {current }}\) is better than the worst individual in the
        population) then
        replace the latter by \(s_{\text {current }}\);
    end if
until (stopping criterion is reached)
```

Fig. 1 EDA procedure
number of times job $j$ comes immediately after the job at the position $k-1$ in the new individual from the sequences of the selected parents. This parameter is used to highlight the importance of similar blocks in the sequence. $\Omega_{k}$ represents the set of jobs not already scheduled until position $k$. According to this model, the task of constructing new offspring has a complexity order of $O\left(n^{2}\right)$. Although this model provides a good solution quality, it consumes high CPU times, especially when the size of the problem increases. In this work, we propose an improvement to the model of Jarboui et al. [10] by reducing its complexity. First, a sequence of jobs $s_{0}$ is selected, at random, among the $M$ selected parents. Then, the probabilistic model is built like the one described above while modifying the set $\Omega_{k}$ into $\Omega_{k q}$. The latter set is composed of $q$ jobs not already scheduled, following their order in $s_{0}$, until position $k$. So, while comparing the model proposed here and the one proposed by Jarboui al. [10], we find that the phase of construction of new individual requires a linear time $O(n)$ in this proposed model. Moreover, this formulation grants more intensification to the algorithm. The pseudo-code of the EDA is given in Fig. 1.

### 4.4 Skewed Variable Neighborhood Search (SVNS) Algorithm

SVNS algorithm is an extension inspired by the original variable neighborhood search algorithm proposed by Hansen and Mladenovic [7]. In order to escape from the local optima, this algorithm is added to our EDA after creating a new solution. Firstly, to increase the performance of the SVNS, we restrict the application of the algorithm to only a part of the individuals [29]. To do this, we define a calculated probability $p^{c}$, as in [10], which decides if the new individual will be subject to an application of the SVNS algorithm. This probability depends on the quality of the created individual, as follows:

$$
p^{c}=\max \left\{\exp \left(\frac{R D}{\alpha}\right), \varepsilon\right\}
$$

where

$$
R D=\left(\frac{f\left(s_{\text {current }})-f\left(s_{\text {best }}\right)\right.}{f\left(s_{\text {best }}\right)}\right)
$$

and $s_{\text {current }}$ and $s_{\text {best }}$ denote the sequences of the new offspring and the best individual found so far, respectively. This probability depends on the distance separating the current solution and the best solution. Therefore, the best obtained solutions have a high probability of being subject to an application of SVNS algorithm.

A random number in the range $[0,1]$ is drawn for each individual. If this number is less than or equal to $p^{c}$, then the considered individual will be eligible to be subjected to the SVNS algorithm. This algorithm consists of two structures of neighbourhood $(k=1,2)$. The first structure leads to the selection of two distinct positions at random from $s_{\text {current }}$ and the permutation of the jobs located on those positions. The second one consists of selecting, randomly, a job $j$ from $s_{\text {current }}$ and inserting it at a randomly selected position. After setting $k$ to 1 , the shaking phase generates a sequence $s_{1}$ according to the $k^{\text {th }}$ neighborhood. This phase is introduced into the SVNS algorithm in order to avoid cycling which might occur if any deterministic rule was used.

Then, two local search methods are employed. The first procedure performs all possible swap moves in the sequence $s_{1}$. The obtained local optimum is denoted by $s_{2}$ (see Fig. 2). After that, the second local search procedure starts performing all insertion moves to $s_{2}$. Let $s_{3}$ be the resulting local optimum (see Fig. 3). If $f\left(s_{3}\right)<$ $f\left(s_{2}\right)$, we replace $s_{1}$ by $s_{3}$, and we return to the first local search procedure. The process is repeated until no improvement is possible. Then we compare the objective

```
Swap Local Search
swap_local_search()
Let \(s_{0}\) be the input solution
Let \(s_{\text {best }}\) be the output solution
\(s_{\text {best }}=s_{0}\);
set \(i=1\);
loop
    for \(j=i+1, i+2, \ldots, n\)
        create a new solution by exchanging the jobs at position \(i\) and \(j\) in the best sequence;
        if (the fitness of the new solution is better than the \(s_{\text {best }}\) ) then
            update \(s_{\text {best }}\);
            break;
        end if
    endfor
    \(i=i+1\)
    if \((i>n-1)\) set \(i=1\);
until (no possible improvement)
```

Fig. 2 Swap local search procedure

function values of $s_{3}$ (the local optimum) and $s_{\text {current }}$ (the incumbent solution). If $s_{3}$ is better than $s_{\text {current }}$, then the latter is updated and we go to the shaking phase with $k=1$. Else, we define a distance function $\rho\left(s_{3}, s_{\text {current }}\right)$ as a discrete function, as follows:

$$
\rho\left(s_{3}, s_{\text {current }}\right)=\frac{\sum_{j=1}^{n}\left|\operatorname{pos}_{3}^{j}-\operatorname{pos}_{\text {current }}^{j}\right|}{n}
$$

where $\operatorname{pos}_{3}^{j}$ denotes the position of the job $j$ in $s_{3}$ and $\operatorname{pos}_{\text {current }}^{j}$ denotes the position of the job $j$ in the incumbent sequence $s_{\text {current }}$. So, $\rho\left(s_{3}, s^{\text {current }}\right)$ represents the position lags between the obtained local optimum and the incumbent solution. The calculation of this distance function is illustrated by the example below. Let $s_{3}=\{6,4,3,1,2,5\}$ and $s_{\text {current }}=\{3,1,6,4,2,5\}$, we define by $\operatorname{pos}_{3}$ and pos $_{\text {current }}$ two $n$-dimensional vectors, where $\operatorname{pos}_{3}^{j}$ and $\operatorname{pos}_{\text {current }}^{j}$ indicate the positions of the job $j$ in $s_{3}$ and $s_{\text {current }}$, respectively. So, $\operatorname{pos}_{3}=\{4,5,3,2,6,1\}$ and $\operatorname{pos}_{\text {current }}=\{2,5,1,4,6,3\}$ and consequently:

$$
\rho\left(s_{3}, s^{\text {current }}\right)=\frac{|4-2|+|5-5|+|3-1|+|2-4|+|6-6|+|1-3|}{6}=1.33
$$

Also, we define a parameter $\beta$ : when $f\left(s_{3}\right)-f\left(s_{\text {current }}\right)<\beta \times \rho\left(s_{3}, s_{\text {current }}\right)$, then we accept the deterioration of the current solution and we replace $s_{\text {current }}$ by $s_{3}$ and thereafter $k$ is reinitialized to 1 . Otherwise, $k$ is incremented to 2 and we return to the shaking process. Finally, the whole procedure is repeated until a maximum number of iterations (iter ${ }_{\max }$ ) is reached. Fig. 4 describes the pseudo-code of the SVNS algorithm.

# Insert Local Search 

Let $s_{0}$ be the input solution
Let $s_{\text {best }}$ be the output solution
$s_{\text {best }}=s_{0}$
set $i=1$
loop
for $j=1,2, \ldots, n$ and $j \neq i$
create a new solution by inserting the job at position $i$ into position $j$ in the best sequence;
if (the fitness of the new solution is better than the $s_{\text {best }}$ ) then
update $s_{\text {best }}$
break;
end if
endfor
$i=i+1$
if $(i>n)$ set $i=1$
until (no possible improvement)

Fig. 3 Insert local search procedure

# SVNS Algorithm 

Let $s_{0}$ be the input solution
Let $s_{\text {best }}$ be the output solution
$s_{\text {best }}=s_{0}$
$s_{\text {current }}=s_{0}$
loop
set $k=1$
do
$s_{1}=s_{\text {current }}$
if $(k=1)$ then
select $i$ and $j$ at random and insert the job at position $i$ into position $j$ in $s_{1}$;
else
select $i$ and $j$ at random and exchange the jobs at position $i$ and $j$ in $s_{1}$;
endif
do
find the optimum local $s_{2}$ by applying swap local search to $s_{1}$;
find the optimum local $s_{3}$ by applying insert local search to $s_{2}$;
if ( $s_{3}$ is better than $s_{2}$ ) then
$s_{1}=s_{3}$
endif
while ( $s_{3}$ is better than $s_{2}$ )
if ( $s_{3}$ is better than $s_{\text {best }}$ ) then
$s_{\text {best }}=s_{3}$
$s_{\text {current }}=s_{3}$
$k=1$
else if $\left(f\left(s_{3}\right)-f\left(s_{\text {current }}\right)<\beta \times \rho\left(s_{3}, s_{\text {current }}\right)\right)$ then
$s_{\text {current }}=s_{3}$
$k=1$
else
$k=k+1$
endif
while $(k \leq 2)$
until(stopping criterion is reached)

Fig. 4 SVNS procedure

### 4.5 Replacement and Stopping Criterion

In our algorithm, we compare the new individual with the worst individual in the current population. If the first one is better than the latter and the sequence of the offspring is unique, then the worst individual is removed from the population and is replaced by the new individual. In the literature, various stopping criteria have been proposed, such as the maximum number of generations, bound of time, the maximum number of iterations without improvement, etc. In our work, we set a maximal computational time. The pseudo-code of the whole hybrid algorithm is provided in Fig. 5.

# Hybrid EDA 

Initialize the population $P$ using random permutation;
loop
select $M$ individuals from $20 \%$ of best individuals in the population;
select $s_{0}$ at random from the $M$ selected individuals;
for $k=1, \ldots, n$
update $\Omega_{k}$ using the $q$ first job not already scheduled from $s_{0}$;
compute the probability $\pi_{j k}$ for each job $j \in \Omega_{k}$;
$s_{\text {current }, k}$ receives the job selected from $\Omega_{k}$ following the computed probability;
end for
compute $p^{c}$;
if (rand $\leq p^{c}$ ) then // rand denotes a random value uniformly distributed in the range $[0,1]$
Apply the SVNS procedure to improve $s_{\text {current }}$;
end if
if (the fitness of new created induvidual $s_{\text {current }}$ is better than the worst individual in the population) then
replace the latter by $s_{\text {current }}$;
end if
until (stopping criterion is reached)

Fig. 5 EDA with SVNS procedure

## 5 Experimental Results and Comparative Study

The algorithm was coded in C++ programming language. All experiments with EDA for FSP with limited buffers, with respect to the makespan criterion, were run in Windows XP on a desktop PC with Intel Pentium IV, 3.2 GHz processor and 512 MB memory. EDA was tested for 29 instances distributed as follows: 8 instances of Carlier [3] and 21 instances of Reeves [27]. All results were obtained after 20 replications for each instance.

The corresponding parameters of EDA were set, experimentally, to the following values: $P=20, \delta_{1}=\delta_{2}=4 / n$, the number of the selected parents $M=3$, the number of generated offspring $O=3$. Numerically, $p^{c}=0.5$ leads to the acceptance of a sequence with a makespan relatively superior by $1 \%$ to the best value of the makespan found so far. So, thereafter we determined $p^{c}$ according to this formula: $p^{c}=\max \left\{\exp \left(\frac{B D}{\alpha}\right), \varepsilon\right\}$, with $\varepsilon=0.01$. The maximum number of iterations of VNS algorithm (iter ${ }_{\max }$ ) was set at 3 and the coefficient $\beta$ was fixed to 2 . The performance measure employed in our numerical study was the average relative percentage deviation in the makespan:

$$
\Delta_{\text {avg }}=\frac{\sum_{i=1}^{R}\left(\frac{H e u_{i}-L B}{L B}\right)}{R} \times 100
$$

$\mathrm{Heu}_{i}$ is the objective value of the solution found by our algorithm at the $i^{\text {th }}$ replication and $L B$ (Lower Bound) is the best known value of makespan when the size of the buffer is infinite.

The comparative approaches used in this study consist of the representative methods employed for solving this problem in the literature, including Hybrid Genetic Algorithm (HGA) of Wang et al. [31], Hybrid Particle Swarm Optimization (HPSO) of Liu et al. [14] and (PSOvns) of Tasgetiren al. [30] .

# 5.1 Results of the Proposed EDA under Zero and Infinite Buffer Sizes 

Table 1 and Table 2 summarize the results obtained by our EDA against HGA and HPSO for the extreme cases of the problem. In Table 1, the problem with no buffer,

Table 1 Computational results under $B_{i}=0$

Table 2 Computational results under $B_{i}=$ infinite
i.e. the blocking flowshop scheduling problem, is addressed. It is clear that EDA is better than HGA and HPSO with respect to both $\delta_{\text {avg }}$ and the minimum relative percentage deviations of best found solutions, $\delta_{\min }$. Therefore, we observe that, in average for all instances, $\delta_{\text {avg }}$ provided by our algorithm $(12,46 \%)$ is less than $\delta_{\min }$ provided by the compared algorithms ( $14,17 \%$ for HGA and $12,75 \%$ for HPSO). When the size of the buffer is infinite, i.e. for the classical FSP, the EDA again outperforms the other approaches in terms of $\delta_{\text {avg }}$ and $\delta_{\min }$ (Table 2). Moreover, for Carlier instances [3], our EDA seems to be able to reach all $L B$ values for all replications in short CPU times (Table 6). Globally, the EDA reaches 17 LB values out of 29 and $14 L B$ values are obtained by HGA and HPSO.

Table 3 Computational results under $B_{i}=1$
# 5.2 Results of the Proposed EDA under Different Buffer Sizes 

Even for the buffer sizes of 1,2 and 4 where the results are depicted in Tables 3, 4 and 5 respectively, our proposed algorithm remains the best one in terms of the quality of the solutions. Moreover, it is shown that while the buffer sizes increase the deviations become close to zero. Therefore, the performance of the EDA increases when the problem presents fewer constraints and approaches the classical FSP. Also, it can be seen that the differences between $\delta_{\min }$ and $\delta_{\text {avg }}$ are very small, which implies the high robustness of our algorithm in a consistent manner (Table 6).

Table 4 Computational results under $B_{i}=2$
# 5.3 Comparative Results Based on Unilateral Paired t-Test 

In order to compare the performance of our algorithms, we have used the unilateral paired t-test procedure [16] at the $99 \%$ significance level. This procedure consists of testing the differences in two samples of observations within pairs. Let $\mu_{A}$ and $\mu_{B}$ denote the true average relative percent deviations of the algorithms $A$ and $B$ respectively. The tested hypotheses are:

$$
\left\{\begin{array}{l}
H_{0}: \mu_{A}-\mu_{B}=0 \\
H_{1}: \mu_{A}-\mu_{B}<0
\end{array}\right.
$$

Table 5 Computational results under $B_{i}=4$
$H_{0}$ implies that the average relative percent deviations of the two algorithms are similar, while $H_{1}$ implies that the average relative percent deviations of the algorithm $A$ are lower than the ones for the algorithm $B$. The obtained results are given in Table 7.

For different buffer sizes, the statistical tests prove that the negative difference between EDA and all other algorithms is meaningful at the significance level of 0.99 . Therefore, the effectiveness of our algorithm against the representative approaches from the literature for this problem is proved.

Table 6 Average CPU times of EDA over 20 replications (in seconds)

Table 7 Comparative results based on unilateral paired t-test

# 6 Conclusion 

This chapter presented an application of EDA to a FSP under limited buffer with respect to makespan criterion. Therefore, we developed a probabilistic model based on the main characteristics of the problem. After constructing new sequence of jobs through the EDA, a SVNS was added to improve the quality of the solution. The computational results show that our algorithm outperforms the approaches it was compared with in terms of the solution quality and gives good results in short CPU times. Moreover, the performance of our algorithm is proved by using the unilateral paired t-test procedure.
