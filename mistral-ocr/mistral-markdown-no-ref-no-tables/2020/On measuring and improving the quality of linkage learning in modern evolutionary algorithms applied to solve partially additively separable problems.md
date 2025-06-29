# On measuring and improving the quality of linkage learning in modern evolutionary algorithms applied to solve partially additively separable problems 

Michal W. Przewozniczek<br>Dep. of Computational Intelligence<br>Wroclaw Univ. of Science and Techn. Wroclaw, Poland<br>michal.przewozniczek@pwr.edu.pl

Bartosz Frej<br>Fac. of Pure and Applied Mathematics<br>Wroclaw Univ. of Science and Techn.<br>Wroclaw, Poland<br>bartosz.frej@pwr.edu.pl

## Marcin M. Komarnicki

Dep. of Computational Intelligence Wroclaw Univ. of Science and Techn. Wroclaw, Poland
marcin.komarnicki@pwr.edu.pl

## ABSTRACT

Linkage learning is frequently employed in modern evolutionary algorithms. High linkage quality may be the key to an evolutionary method's effectiveness. Similarly, the faulty linkage may be the reason for its poor performance. Many state-of-the-art evolutionary methods use a Dependency Structure Matrix (DSM) to obtain linkage. In this paper, we propose a quality measure for DSM. Based on this measure, we analyze the behavior of modern evolutionary methods. We show the dependency between the linkage and the effectiveness of the considered methods. Finally, we propose a framework that improves the quality of the linkage.

## CCS CONCEPTS

- Computing methodologies $\rightarrow$ Artificial intelligence;


## KEYWORDS

Linkage Quality Measurement, Genetic Algorithm, Estimation-ofDistribution Algorithm, Linkage Learning, Model Building

## ACM Reference Format:

Michal W. Przewozniczek, Bartosz Frej, and Marcin M. Komarnicki. 2020. On measuring and improving the quality of linkage learning in modern evolutionary algorithms applied to solve partially additively separable problems. In Genetic and Evolutionary Computation Conference (GECCO '20), July8-12, 2020, Cancún, Mexico. ACM, New York, NY, USA, 9 pages. https://doi.org/10.1145/3377930.3390242

## 1 INTRODUCTION

Linkage learning techniques are used by evolutionary methods to detect dependencies between genes encoding a solution to an optimized problem. Such knowledge, if it is precise, allows for the detection of the problem structure, and, if used properly, may significantly increase the effectiveness of an evolutionary method. For instance, if an optimizer is given an accurate knowledge about the problem nature, the number of expected fitness function evaluations (FFE) necessary to find an optimal solution may scale linearly

[^0]with the problem size [16]. Therefore, in black-box optimization, it is important to obtain a high-quality linkage that may be decisive for the effectiveness of a method [15]. Thus, linkage quality measures are necessary to gather knowledge about the quality of linkage obtained by an evolutionary method. Such measures are also necessary to better understand an evolutionary method behavior and analyze the reasons lying behind the successful runs as well as behind the failures. In [10], authors propose linkage quality measures that allow telling if each independent subcomponent of a problem is completely detected or not. To the best of our knowledge, these are the only linkage quality measures proposed that far. Such measures inform only if a perfect linkage was found or not [13]. Therefore, they are not enough - there is a significant difference between the correct detection of $90 \%$ of the subcomponent and detecting only $10 \%$ of it.

This paper concentrates on solving partially additively separable problems defined as follows. The problem is partially additively separable if it has a following general form [9]:

$$
f(\vec{x})=\sum_{i=1}^{r} f_{i}\left(\vec{x}_{i}\right)
$$

where $\vec{x}=\left[x_{1}, \ldots, x_{n}\right]$ is a global decision vector of $n$ dimensions, $\vec{x}_{i}$ are mutually exclusive decision vectors of $f_{i}$, and $r$ is the number of independent subcomponents.

Many of the typical benchmark problems are partially additively separable. However, such problems also conveniently represent the modular nature of many real-world problems [9]. Therefore, optimization methods that successfully solve such problems are valuable in both: theory and practice.

The objectives of this paper are as follows. We propose a linkage quality measure that allows checking how precise is a particular set of linkage information even if it is not perfect. We define what is the perfect linkage stored in the Dependency Structure Matrix (DSM) that is frequently employed to represent linkage [4, 6, 14]. For one of the types of considered optimization problems, we formally estimate the population size necessary to obtain a perfect linkage. Using a set of state-of-the-art methods and the proposed technique of artificial linkage creation, we empirically check what is the minimum linkage quality to successfully solve different types of partially additively separable problems. We measure and present the linkage quality obtained by state-of-the-art evolutionary methods on the set of considered problems. On this basis, we analyze the behavior of the considered methods and identify the premises of their success or failure. Finally, we propose the Unbiased Linkage Improver (ULI)


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
    GECCO '20, July8-12, 2020, Cancún, Mexico
    (c) 2020 Association for Computing Machinery.

    ACM ISBN 978-1-4503-7128-5/20/07... $\$ 15.00$
    https://doi.org/10.1145/3377930.3390242

framework to improve linkage that is obtained on the evolutionary method run. ULI may be applied to any evolutionary method. We show that despite its simplicity, it may significantly improve the effectiveness of an evolutionary method on the problems for which a high-quality linkage is hard to find.

The rest of the paper is organized as follows. In the next section, we briefly present related work. In Section 3, we present the formal estimation of the minimum population size necessary to obtain a perfect linkage. In the fourth section, we give a formal definition of the proposed linkage quality measure. In Section 5, we propose the ULI framework. The results and analysis of all performed experiments are presented in Section 6. Finally, in the last section, we conclude this paper and highlight the main future work directions.

## 2 RELATED WORK

One of the important advances in the domain of single-objective black-box optimization was employing the Dependency Structure Matrix (DSM) to obtain linkage in the evolutionary methods [6, 15]. The concept of DSM is derived from the organization theory. DSM is a square matrix, and its entries indicate the dependencies between some components. The single DSM entry $d_{i, j} \in R$, denotes the relationship between the $i^{t h}$ and $j^{t h}$ components. The higher value of the entry indicates the higher dependency between the components related to the entry. When DSM is employed to obtain linkage in evolutionary methods, a single component is represented as a single gene. Many measures were used that far to measure pairwise dependencies between genes [4, 6, 15]. Here, we use the mutual information measure [6] to illustrate the process of DSM creation.

$$
I(X ; Y)=\sum_{x \in X} \sum_{y \in Y} p(x, y) \log _{2} \frac{p(x, y)}{p(x) p(y)}
$$

where both $X$ and $Y$ are random variables. Note that $\forall_{X, Y} I(X ; Y) \geq$ 0 and $I(X ; Y)$ equals 0 when $X$ and $Y$ are independent, because then $p(x, y)=p(x) p(y)$.

To compute DSM values for a given population, the gene value frequencies are counted. The main goal of creating DSM is to extract some useful information about groups of genes that are dependent on one another. Since DSM contains only pairwise dependency values, a clustering algorithm is necessary to merge pairs of genes into larger groups. There are different algorithms [2, 4, 6, 14] that can meet this objective. Here, we describe a hierarchical clustering algorithm that frequently used. In [4, 14] hierarchical clustering algorithm uses the $D\left(G_{i}, G_{j}\right)$ distance measure. For the $i^{t h}$ and $j^{t h}$ genes, it is calculated using the mutual information and joint entropy:

$$
D\left(G_{i}, G_{j}\right)=\frac{H\left(G_{i}, G_{j}\right)-I\left(G_{i}, G_{j}\right)}{H\left(G_{i}, G_{j}\right)}
$$

where

$$
H\left(G_{i}, G_{j}\right)=-\sum_{g_{i} \in G_{i}} \sum_{g_{j} \in G_{j}} p_{i, j}\left(g_{i}, g_{j}\right) \ln p_{i, j}\left(g_{i}, g_{j}\right)
$$

The hierarchical clustering algorithm creates the linkage tree. The linkage tree consists of nodes (i.e., clusters), which are the groups of genes that are considered to be related. The linkage tree creation procedure is greedy because, during its every step, two
nearest clusters (according to the distance measure) are merged. Initially, clusters containing only a single gene are created. Then, the merging operation is repeated until only one cluster consisting of all genes remains.

One of the methods that employ linkage trees is the Linkage Tree Gene-pool Optimal Mixing Evolutionary Algorithm (LT-GOMEA), which was proposed in [1]. To exchange information between individuals, LT-GOMEA uses the optimal mixing (OM) operator. In OM, the genes from the donor individual, marked by the cluster, replace genes in the source individual. If the fitness of the source decreases, then the operation is reversed. Otherwise, the source remains modified. LT-GOMEA uses the population-sizing scheme [5], which makes it parameter-less (otherwise, the only parameter would be the population size). LT-GOMEA maintains its multiple instances, each with different population size. It starts with a population containing only one individual. Then, the instance with a doubled population is executed at each $4^{t h}$ iteration. The instances are found useless if all of its individuals are the same, or its average population fitness is worse than the average fitness of at least one instance with a larger population size. If an instance is found useless, then all instances with a smaller population are found useless as well.

Parameter-less Population Pyramid (P3) [4] also employs OM and linkage tree. The population of P3 has a pyramid-like structure, where each level is a separate subpopulation with its own DSM. At each iteration, P3 creates a new random individual and optimizes it with the First Improvement Hill Climber (FIHC). For an individual $\vec{x}$ that is a vector of $n$ decision variables $\left[x_{1}, \ldots, x_{n}\right]$ FIHC works as follows. Considering all genes in a random order, it checks all available values for each gene. The first value that leads to fitness improvement over the original $x_{i}$ value replaces the original one. This procedure is executed until the iteration of FIHC will not change any gene. After FIHC, the new individual is mixed with OM with all individuals in the pyramid, starting from the lowest level. If this operation improves an individual, then it is added to an upper pyramid level (the new pyramid level is created if necessary).

Dependency Structure Matrix Genetic Algorithm II (DSMGAII) [6] employs DSM differently to LT-GOMEA and P3. It creates the incremental linkage set that is a sequence of dependent genes. The first gene is selected randomly. The next gene is the one that is not in the sequence yet and is the most linked to the gene that is the last in the sequence, and so on. To improve an individual, the genes marked by an incremental linkage set are flipped (this operation is called restricted mixing). If restricted mixing decreases the fitness, then the changes are reverted. Otherwise, the change made by restricted mixing is injected to the other individuals in a population (this operation is called the back mixing). Recently, the population-sizing DSMGA-II (psDSMGA-II) [8] was proposed. psDSMGA-II uses a similar population-sizing technique as LT-GOMEA [1].

## 3 OBTAINING THE PERFECT LINKAGE FOR DECEPTIVE TRAP FUNCTIONS CONCATENATIONS

In this section, we consider the problems built from the concatenation of $m$ deceptive trap functions. The single deceptive order- $k$ trap function is defined as follows.

$$
\operatorname{dec}(u)= \begin{cases}k-1-u & \text { if } u<k \\ k & \text { if } u=k\end{cases}
$$

where $u$ is the sum of gene values (so called unitation) and $k$ is the deceptive function size.

We estimate the probability of obtaining the DSM containing the perfect linkage for a population of a given size, where each individual was optimized by FIHC. The perfect linkage is a linkage that points true gene dependencies without any genes missing. Let us consider the 6 -bit problem built from two order-3 trap functions. The first three genes refer to the first trap function, while the latter three genes refer to the second trap function. Note that these two blocks of genes are separable (i.e., to find the optimal value of the considered problem, we can optimize both blocks separately). Since the blocks are separable, then there are two groups of dependent genes (genes 1, 2, and 3 form the first group, while genes 4, 5, and 6 from the second one). The DSM that contains the perfect linkage for such a problem points that the most dependent genes of the first gene are genes 2 and 3 (the order is not important). Similarly, for the second gene, the most dependent genes should be 1 and 3 , while for the fifth gene, the most dependent genes should be 4 and 6 , and so on. Note that if the perfect linkage is supported to the evolutionary method, then (if the linkage is used properly), the evolutionary method is expected to solve the problem effectively [16]. Thus, estimating a chance for obtaining the perfect linkage is important for the field of evolutionary computation.

Consider a concatenation of $r$ deceptive trap functions of order $k$. By a block we will understand the domain of a single deceptive function. Let us randomly (with equal probabilities) choose a population of $s$ individuals, where individual $\vec{x}=\left[x_{1}, \ldots, x_{n}\right]$ is a vector of $n=r k$ binary variables. To each individual we apply FIHC. Denote by $X_{i}$ a random variable with values in $(0,1)$, whose probability distribution $\left(p_{i}(0), p_{i}(1)\right)$ is obtained by taking frequencies of zeros and ones at position $i$, respectively. Fix any positions $i, j$ and $m$, so that $i$ and $j$ lie in the same block, meaning that these genes are dependent, while $m$ lies in a different block, i.e., $m^{t h}$ gene is independent of $i^{t h}$ and $j^{t h}$ genes. We want to estimate $P\left(I\left(X_{i} ; X_{j}\right)>I\left(X_{i} ; X_{m}\right)\right)$. Using a well-known equality $I(X ; Y)=H(X)-H(X \mid Y)$ we get

$$
I\left(X_{i} ; X_{j}\right)-I\left(X_{i} ; X_{m}\right)=H\left(X_{i} \mid X_{m}\right)-H\left(X_{i} \mid X_{j}\right)
$$

After applying FIHC, all genes in a block have the same value, hence $H\left(X_{i} \mid X_{j}\right)=0$. Thus,

$$
\begin{aligned}
& P\left(I\left(X_{i} ; X_{j}\right)>I\left(X_{i} ; X_{m}\right)\right) \\
& \quad=P\left(H\left(X_{i} \mid X_{m}\right)-H\left(X_{i} \mid X_{j}\right)>0\right) \\
& \quad=P\left(H\left(X_{i} \mid X_{m}\right)>0\right)
\end{aligned}
$$

Clearly, $H\left(X_{i} \mid X_{m}\right)$ is non-negative and $H\left(X_{i} \mid X_{m}\right)=0$ only if all non-zero values of $p_{i, m}(a, b)=P\left(X_{i}=a, X_{m}=b\right)$ are equal to $p_{m}(b)$, i.e., if in each individual from the population the value of the $m^{t h}$ gene determines the value of the $i^{t h}$ gene. This gives the following possibilities for genes $x_{i}$ and $x_{m}$ : either all individuals in
the population share only one combination of values, namely,

$$
\begin{aligned}
& \left(\sqrt{x^{t}} x_{i} x_{m}=00\right) \quad \text { or } \quad\left(\sqrt{x^{t}} x_{i} x_{m}=01\right) \quad \text { or } \\
& \left(\sqrt{x^{t}} x_{i} x_{m}=10\right) \quad \text { or } \quad\left(\sqrt{x^{t}} x_{i} x_{m}=11\right)
\end{aligned}
$$

or exactly two combinations occur throughout the population, except for cases

$$
\begin{aligned}
& \sqrt{x^{t}}\left(x_{i} x_{m}=00 \text { or } x_{i} x_{m}=10\right) \text { and } \\
& \sqrt{x^{t}}\left(x_{i} x_{m}=01 \text { or } x_{i} x_{m}=11\right)
\end{aligned}
$$

Using the classical definition of probability we derive the probability that an individual has 0 at $i$ th gene and either 0 or 1 at $m$ th gene as equal to $\frac{\left(2^{k}-2\right) 2^{(i-1) k}}{2^{i k}}=1-\frac{1}{2^{k-1}}$. Since the starting population is chosen by $s$ independent drawings, the probability of choosing the population containing only such individuals (including populations with all individuals sharing only one combination of values, 00 or 01 ) is equal to $\left(1-\frac{1}{2^{k-1}}\right)^{s}$. Similarly, the probability that an individual has 1 at $i$ th gene is $\frac{1}{4^{k-1}}$ and the probability that all population has 1 at $i^{t h}$ gene is equal to $\frac{1}{2^{k(4-1)}}$. The probability that zeros or ones occur simultaneously at both genes is equal to $\frac{\left(12^{k}-2\right)^{s}+2^{k} 12^{(i-1) k}}{2^{i k}}=1-\frac{1}{2^{k-2}}+\frac{1}{2^{(k-1)}}$. Finally, the probability that an individual has 0 at $i$, while 1 at $m$ or vice versa is equal to $\frac{2 \cdot 2 \cdot\left(2^{k}-2\right) 2^{(i-2) k}}{2^{i k}}=\frac{1}{2^{k-2}}-\frac{1}{2^{(k-1)}}$. Note that each of the four situations when all individuals share only one combination of values falls into exactly two of considered cases. Therefore,

$$
\begin{aligned}
& P\left(H\left(X_{i} \mid X_{m}\right)=0\right)=\left(1-\frac{1}{2^{k-1}}\right)^{s}+\left(\frac{1}{2^{k-1}}\right)^{s}+ \\
& +\left(1-\frac{1}{2^{k-2}}+\frac{1}{2^{2 k-3}}\right)^{s}+\left(\frac{1}{2^{k-2}}-\frac{1}{2^{2 k-3}}\right)^{s}-\frac{4}{2^{k} r s}
\end{aligned}
$$

Clearly,

$$
P\left(H\left(X_{i} \mid X_{m}\right)=0\right) \leq 4 \cdot\left(1-\frac{1}{2^{k-2}}+\frac{1}{2^{2 k-3}}\right)^{s}
$$

because the third summand majorizes all other terms.
The mutual information function $(i, j) \mapsto I\left(X_{i} ; X_{j}\right)$, treated as a function on a Cartesian product $\{1, \ldots, n\} \times\{1, \ldots, n\}$, is constant on blocks. The probability that there is a triple $i, j, m$ such that $i$ and $j$ belong to one block, while $m$ belongs to another one and $I\left(X_{i} ; X_{j}\right) \leq I\left(X_{i} ; X_{m}\right)$ is smaller than $P\left(H\left(X_{i} \mid X_{m}\right)=0\right)$ multiplied by the number of all blocks (which may contain $i$ and $j$ ) and the number of all blocks decreased by one (which then may contain $m$ ). By (6) and (7), mutual information between $i^{t h}$ and $j^{t h}$ genes belonging to the same block majorizes mutual information between $i^{t h}$ and $m^{t h}$ genes lying in independent blocks for all triples of genes with probability greater than

$$
1-4 r(r-1)\left(1-\frac{1}{2^{k-2}}+\frac{1}{2^{2 k-3}}\right)^{s}
$$

To ensure that mutual information supports a correct linkage for all genes with probability $q$, it suffices to take a population of size

$$
s>\log _{a} \frac{1-q}{4 r(r-1)}
$$

where $a=1-\frac{1}{2^{k-1}}+\frac{1}{2^{2 k-3}}$. For instance, consider a concatenation of 100 deceptive trap functions of order 3 , which gives a variety of $2^{300}$

individuals. The above formula yields that to obtain correct linkage with probability 0.99 one needs $s>32$. The above estimation was verified empirically, the results are presented in Section 6.2.

The obtained formula shows that the population sizes necessary to obtain a perfect linkage for trap function concatenations seem low. This statement is not necessarily true for other commonly used test problems, though by choosing a population in a sequence of independence drawings, we will always make the strong law of large numbers play on our side. However, even if the perfect linkage is hard to find by DSM-based linkage learning techniques, the imperfect linkage information may be sufficient to find the optimum as well. Therefore, in the next section, we define a linkage quality measure. With this measure, we can check what was the linkage quality at the end of the run when the optimal solution was found. Moreover, we can also generate an artificial linkage of the desired quality and check if such a linkage is sufficient to find the optimal result.

## 4 PROPOSED LINKAGE QUALITY MEASURE

In this section, we propose the quality measure for a linkage stored in DSM. We assume that if we possess a high-quality linkage, then for each gene $x_{i}$, the genes that are truly dependent on it shall correspond to higher entries in DSM. Based on it, we may create a ranking of dependencies between genes. For instance, let us assume that the first gene is truly dependent on genes $2,3,4$, and 5 , and is not dependent on any other genes. If linkage points at genes $5,3,4$, and 2 as the most dependent on the first gene, then such a linkage is perfect. If linkage points out genes $3,6,4,7$, and 2 , then such a linkage is imprecise but may still be useful.

Below, we define the Fill measure. Its value is defined for a particular position in a genotype, but one may as well understand it as a measure of the quality of the content of a single DSM row that refers to a particular gene.

Let BlockSize $(i)$ be the number of genes that depend on the $i^{\text {th }}$ gene (i.e., the size of the block the $i^{\text {th }}$ gene belongs to). Let TrueDep $(i, M, n)$ be the number of genes that are correctly pointed by the matrix $M$ to be among $n$ genes, most dependent on the $i^{\text {th }}$ gene. We then set

$$
\operatorname{Fill}(i, M)=\frac{\operatorname{TrueDep}(i, M, \operatorname{BlockSize}(i))}{\operatorname{BlockSize}(i)}
$$

where $i$ is the position in the genotype and $M$ is a DSM for some population. Clearly, the best quality of linkage corresponds to $\operatorname{Fill}(i, M)$ being equal to 1 , while the worst quality corresponds to 0 .

The proposed Fill measure is only applicable to problems that are additively separable. Proposing the linkage quality measures for problems with overlapping blocks is future work.

## 5 LINKAGE-IMPROVING FRAMEWORK

In this section, we define a framework that may be applied to any evolutionary method. The motivation behind our proposition is supporting an evolutionary method, a linkage that is not biased by the evolutionary process. Let us consider the following example. $\vec{x}$ is a solution to the problem that is a concatenation of 100 order-3 deceptive trap functions. The linkage information points that all genes from the first and second block and two genes (first and third) from the third block are dependent. The linkage does not
allow a separation of the first block neither from the second block nor from the two genes from the third block. The first blocks of $\vec{x}$ are as follows $\vec{x}=[000000111 \ldots]$. Consider a mixing operation, using linkage described above, in which $\vec{x}$ is a source and $\vec{x}=$ [111 111 000...] is a donor. After such an operation, the genotype of the donor will be $\overrightarrow{x_{\text {mixed }}}=[111111101 \ldots]$, because $f i t\left(\overrightarrow{x_{\text {mixed }}}\right)>$ fit $(\vec{x})$. Note that although the fitness of $\vec{x}$ has risen, the imprecise linkage information may be strengthened (for instance, if in most of the population, the first three blocks contain only ' 0 's, which would be typical for deceptive trap functions). If so, then such a corrupted linkage may prevent an evolutionary method from finding an optimal solution.

The above example shows that for some of the problems, it may be favorable to obtain linkage without bias caused by an evolutionary process. Therefore, we propose a framework denoted as Unbiased Linkage Improver (ULI). ULI overview is given in Pseudocode 1.

```
Pseudocode 1 Unbiased Linkage Improver Overview
    ImprPop \(\leftarrow\) empty; ImprDSM \(\leftarrow\) random;
    ImprFFE \(\leftarrow 0 ;\) OptFFE \(\leftarrow 0 ;\)
    while \(\neg\) stopCondition do
        StartFFE \(\leftarrow\) GetFFE();
        if ImprFFE \(\leq\) OptFFE then
            NewInd \(\leftarrow\) GetRandomGenotype();
            NewInd \(\leftarrow\) FIHC(NewInd);
            GenesToFlip \(\leftarrow\) GenSize(NewInd);
            while GenesToFlip \(>1\) do
                IndBackup \(\leftarrow\) NewInd;
            FlipGenes(NewInd, GenesToFlip);
            NewInd \(\leftarrow\) FIHC(NewInd);
            if fitness(NewInd) \(\leq\) fitness(IndBackup) then
                NewInd \(\leftarrow\) IndBackup;
                GenesToFlip \(\leftarrow\) GenesToFlip/2;
            ImprPop \(\leftarrow\) ImprPop + NewInd;
            ImprDSM \(\leftarrow\) GetDSM(ImprPop);
            ImprFFE \(\leftarrow\) ImprFFE + GetFFE() - StartFFE;
        else
            RunOptIter();
            RunOptIterExternalLinkage(ImprDSM);
            OptFFE \(\leftarrow\) OptFFE + GetFFE() - StartFFE;
```

ULI is built from two parts: the evolutionary optimizer (eg., P3, LT-GOMEA, or DSMGA-2) and the separate part supposed to support additional linkage information (denoted as linkage improver). At each iteration, ULI executes a single iteration of linkage improver or two iterations of an optimizer. ULI chooses the one that has consumed a smaller number of FFE that far. A single iteration of linkage improver is as follows. First, a new individual is randomly generated and optimized by FIHC. Then, half of the genotype of a new individual is flipped, and the resulting genotype is optimized by FIHC. If this operation improves an individual, the operation is repeated. Otherwise, the genotype changes are reverted, and the number of genes to flip is decreased by half. The operation is performed until the number of genes to flip is higher than one. After such an optimization procedure, the new individual is added

On measuring and improving the quality of linkage learning in modern evolutionary algorithms applied to solve partially additively separable problems

GECCO '20, July8-12, 2020, Cancún, Mexico
to the linkage improver population, and DSM is generated for this population.

If ULI decides to execute an optimizer, then it executes two iterations of it. The first iteration of an optimizer is executed in a regular way. However, in the second iteration, an optimizer is given a linkage gathered by the linkage improver (in the form of the DSM matrix generated on the base of linkage improver's population).

Despite its simplicity, ULI has some important advantages. It is parameter-less, and the individuals added to the linkage improver's population do not influence each other optimization processes. ULI was designed to improve linkage quality on the first dependency level. Thus, it may help to solve problems with overlapping blocks or a high level of the hierarchy. On the other hand, it may improve the effectiveness of evolutionary methods applied to solve problems for which the linkage is poorly detected by the DSM-using linkage learning techniques. Moreover, if an optimizer is capable of solving a particular overlapping problem, then it may still solve when used inside ULI.

## 6 THE RESULTS

In the research presented in this paper, we consider LT-GOMEA, P3, and psDSMGA-II because they are all the state-of-the-art methods in the field of single-objective optimization. Additionally, they are all parameter-less. All methods were coded in C++. LT-GOMEA source codes were published by its authors. ${ }^{1}$. For P3 and psDSMGAII, we use the source code pointed in [4] and [6], respectively. All the source codes we have used and the detailed results of the runs are available at https://github.com/przewooz/LinkageQuality.

For the considered test problem set, and the considered methods, the stop condition based on FFE does not seem reliable [11, 12]. Therefore, we use the time-based stop condition. The time limit was set on 12 hours that should give all methods enough computation resources to reach the convergence. All experiments were executed on PowerEdge R7425 Dell server AMD Epyc 7601 2.2GHz 256GB RAM, with Windows 2019 Server installed. Each experiment was single-threaded, and the number of computation process was always the same and lower than the number of available processor cores. Such an execution procedure shall assure the fairness of the comparison. Unless stated otherwise, the number of experiments per test case was 30 .

All considered methods employ a multi-population scheme and dynamically add new populations during the run (LT-GOMEA and psDSMGA-II also delete the populations during the run). In all methods, each population has a separate linkage. Therefore, when we report linkage quality for the whole method run, we report the highest linkage quality among all populations created by a method.

### 6.1 Test Problems

In this paper, we concentrate on measuring the linkage quality for additively separable problems. To show differences in linkage learning difficulties, we consider different types of deceptive functions. The first considered function is deceptive trap function defined in Section 3. We use order-3 and order-5 deceptive trap functions. Note that if FIHC is used, each block that refers to a single deceptive trap function may contain either only ' 0 's or only ' 1 's. This feature

[^0]makes if relatively easy to find a perfect linkage with the use of DSM. Therefore, we also use deceptive step trap functions defined by formula (10). Deceptive step trap function is a modification of a deceptive trap function, which introduces plateaus of size $s$.

$$
\operatorname{step} \_ \operatorname{trap}(u)=\frac{(k-s) \bmod s+d e c(u)}{s}
$$

We use order-3 and order-5 deceptive step trap functions $s=2$. Note that such order-3 deceptive step trap function is 7-bit long (the same function was use in [4]). The order-5 deceptive step trap is 11-bit long.

Another type of deceptive functions considered in this paper are the bimodal deceptive function [3], defined as follows

$$
\operatorname{bimodal} \_ \operatorname{trap}(u)= \begin{cases}k / 2-|u-k / 2|-1 & , u \neq k \wedge u \neq 0 \\ k / 2 & , u=k \vee u=0\end{cases}
$$

Bimodal deceptive functions are significantly different from deceptive step traps because they have two optima and $\binom{k}{k / 2}$ local optima. As we show in the results section, it is harder to detect a high-quality linkage with the use of DSM when a problem has many suboptima. We also use bimodal noised deceptive functions [7, 17]. The noised bimodal functions increase the number of suboptima and make these suboptima different concerning the unitation. The values for order-10 function are in Table 1. Both bimodal deceptive function types are considered in the order-10 version.

Table 1: The values of bimodal noised deceptive function of order-10

The problems considered in this paper are built from deceptive functions concatenations. Except for mixed bimodal functions concatenation, all problems use only one function type. In mixed bimodal functions concatenation, half of the problem is built from the bimodal functions, and the other half is built from the bimodal noised functions.

### 6.2 The Resistance to Low Linkage Quality

In this paper, we propose a measure to determine the quality of the linkage. All considered methods use linkage learning. Therefore, it is important to check how high linkage quality is a must to find an optimal solution. To this end, we introduce an artificial linkage into the competing methods. The procedure of the artificial linkage creation creates an artificial DSM and is as follows. To generate a perfect linkage, for all DSM entries that represent a true gene dependencies for a given problem, the value of each entry is randomly chosen from range $[0.6,1.0]$, while the value of the entries that refer to gene pairs without true dependency is randomly chosen from range $[0,0.4]$. Note that for DSM generated in such a way, for the additively separable problems, the value of the fill measure will be 1 (i.e., optimal). If we wish to generate the linkage of the lower quality, for instance, we wish to obtain a DSM for which the expected average fill value will be 0.6 , then for each entry that represents a true dependency between two genes, we perform a


[^0]:    ${ }^{1}$ https://homepages.cwi.nl/ bosman/source_code.php, downloaded at 2018.08.30

Table 2: Artificial linkage quality sufficient to solve the problem*
*Results obtained for 30 independent runs
random check with a probability 0.6 . If the check is passed, then the value of the entry is generated in a regular way. Otherwise, the value of the entry is randomly chosen from the range $[0,0.4]$.

Surprisingly, when psDSMGA-II was supported with a perfect linkage, it was unable to find an optimal solution for 1200-bit problems. Such an observation was unexpected. The detailed results analysis has shown that when psDSMGA-II is supported a perfect linkage right from the beginning of the run, then it tends to delete all populations except the currently largest one. Such behavior leads to increasing the size of the largest population almost at every method iteration. The reason for this phenomenon is as follows. When psDSMGA-II is supported with a perfect linkage right at the beginning of the run, any population it creates quickly converges. Thus, larger populations can dominate smaller ones as they execute the backpropagation frequently. Each population is close to finding an optimal solution, but it requires more iterations to improve its best individuals. In effect, when psDSMGA-II is supported with a perfect linkage at the beginning of the run, its behavior is close to continuously doubling the size of the single population that is initialized randomly. The size of this population quickly rises to hundreds of thousands, preventing the method from converging to the optimal solution. In a regular psDSMGA-II run, the above phenomenon does not take place because every population must first evolve and improve the quality of its DSM before it can dominate the smaller populations. Therefore, an important future work direction is to find a population-sizing schema that would be more suitable for DSMGA-II. Due to the above phenomenon, the results for psDSMGA-II will avoid in this subsection.

In Table 2, we present the lowest linkage quality for which LTGOMEA and P3 were able to find an optimal solution. The test procedure was as follows. Each method, for each problem, was first supported with an optimal linkage (of average fill quality 1). Then, the artificial linkage quality was lowered by 0.1 until a method failed to find an optimal solution in all of the 30 runs. The obtained results show that for 400 -bit, the linkage quality sufficient to find an optimal solution is slightly lower than for 1200-bit problems. The results are the same or close for both methods except for 1200-bit order-5 deceptive step functions concatenation. For this problem, when P3 was supported with a perfect linkage, it was able to find an optimal solution only in $40 \%$ of the runs. This is much more than in the case of regular P3 run in which it was only $3 \%$, but still, this result is unexpected. The reason for the fail was similar as in psDSMGA-II case - P3 was creating a very tall pyramid containing many individuals. Such a population structure was limiting the convergence and preventing P3 from finding an optimal solution. It seems that an important future work direction is to propose a P3 modification that would limit its pyramid size and introduce a selection pressure.

The results presented in Table 2 show that the highest quality linkage is required to solve problems built from deceptive trap functions. Such an observation may be surprising because this kind of problem seems to be the easiest to solve for all considered methods. Based on the calculations presented in Section 3, for the DSM-using linkage learning techniques, it seems easy to find a linkage of high quality. Therefore, for the method employing such techniques, it seems easy to solve the concatenations of deceptive trap functions. However, it seems easy because it is easy to find a high-quality linkage, not because the problem itself is easy to solve.
![img-0.jpeg](img-0.jpeg)

Figure 1: The influence of linkage quality on the percentage of optimal solutions found and the median amount of FFE necessary to reach the best-found solution by LT-GOMEA on the chosen optimization problems

In Figure 1, we present the dependency between the quality of linkage and the percentage of optimal solutions found and the median FFE necessary to obtain the best-found solution in a run. As long as the linkage quality is high enough, an optimal solution is found in all runs at a very low cost. However, when the linkage quality drops down to some critical value (different for all three problems presented in Figure 1), then the percentage of successful runs drops down immediately as well. At the same time, the FFE necessary to find the best results in a run (no matter optimal or not) rises significantly as well.

### 6.3 Main Results

In this section, we empirically verify the accuracy of the estimation presented in Section 3, and present the comparison between the competing methods in their standard versions and when ULI framework is used. Finally, we support some additional data to show the influence of linkage quality on considered evolutionary methods.

Table 3: Population* necessary to get perfect linkage**
*Results obtained for 100 independent runs
**Estimation made for probability 0.99

Table 3 presents the population sizes that were necessary to obtain a perfect linkage for given deceptive trap concatenations. The population sizes are given for two cases. In the first individuals were optimized by a procedure proposed in ULI, while in the second one, each individual was only processed by FIHC. Finally, in the last column, we report the value of the estimation proposed in formula 8 . The calculation is made for probability 0.99 . Note that the estimation is made for the populations where individuals were only updated by FIHC.

As presented in Table 3the maximum population size obtained in 100 runs is slightly lower than the estimation. Thus, the estimation proposed in formula 8 seems reliable. Note that the population size values obtained when ULI procedure was employed are lower than in the case of using only FIHC. We have verified the medians equality with Sign Test, the $p$-value for the null hypothesis that the medians are equal was lower than 0.003 for four cases. Thus, we may state that the differences are statistically significant. Such a result is expected because the ULI procedure is more sophisticated than FIHC, and the optimization results of its work shall be of higher quality than in the case of FIHC.

In Table 4, we present the summarized results for the highest considered problem length (1200 bits). Except of the percentage of the optimal solution found, we present the resource cost of finding the best solution (for FFE and computation time) and the linkage quality at the end of the run. For both deceptive trap functions concatenation ULI slightly delays finding the optimal result (for both considered measures - FFE and computation time). Such a result is expected because, as shown in Section 3, for deceptive trap functions, DSM can quickly find the perfect linkage. Thus, the linkage improver only slows down the computation. For deceptive step functions, the influence of ULI does not seem significant - the percentage of optimal solutions found and the resources necessary to find them remain similar. Note that for deceptive step traps, the linkage quality gathered by all considered optimizers is relatively high or even close to perfect (LT-GOMEA). Thus, if a method was unable to find an optimal solution, the reason for the failure is in the method procedure rather than in missing the linkage of reasonably high quality.

The significant influence of ULI is the most visible for all problems built from bimodal functions. For LT-GOMEA applied to bimodal functions concatenation, the FFE and computation time costs of finding the optimal solution are significantly reduced (up to about 8 times). Moreover, ULI-LT-GOMEA successfully finds an optimal solution for bimodal mixed and bimodal noised concatenations, while LT-GOMEA does not. Note that for all these problems, the
quality of linkage found by ULI-LT-GOMEA is close to perfect. Surprisingly, when ULI is used, for all methods, the linkage supported by the linkage improver is of lower quality than the linkage found by an optimizer, but the linkage found by an optimizer using ULI is higher (sometimes significantly) than for the same methods that do not use ULI. The reasonable explanation of this fact is as follows. Most probably, Linkage the Improver can successfully mark some of the blocks. When an optimizer uses such an external linkage can successfully process these correctly marked building blocks. The result of this situation is twofold. The fitness of the population rises, and the appropriate dependencies are strengthened in the DSM matrix leading to a fast increase of the overall DSM quality of the optimizer.

The influence of ULI on P3 is even more significant than in the case of LT-GOMEA. ULI-P3 can find a significantly higher percentage of optimal solutions for bimodal functions than P3. Surprisingly, for the bimodal deceptive functions concatenation the quality of linkage found by P3 is close to optimal. The situation is similar to the problem built from step deceptive functions of order 5. In both cases P3 has found a high-quality linkage but was unable to find the optimal result in almost all of the runs despite the fact it was given a high amount of computation resources. The reason for this fact is the P3 algorithm itself. During the run, at each P3 iteration, the pyramid grows. In consequence, each P3 iteration is more expensive, and additionally, the selection pressure is low - the individuals of the higher quality do not replace those of the lower quality but coexist with them in the same pyramid. Therefore, if P3 will not find the high-quality linkage in the early stages of the run, and if it will not converge quickly, then finding an optimal solution may be hardly likely for this method. Such a reasoning is confirmed by both - results reported in other papers and results reported by ULI-P3. In $[7,17]$ the improved P3 versions are proposed. These modified P3s, under some circumstances, add the current bestfound individual to the lowest level of the pyramid. Thanks to this, the convergence is improved. A similar effect (although achieved differently) takes place for ULI-P3. In ULI-P3, the convergence of P3 is improved by a quick finding linkage of reasonably high quality. Note that ULI-P3 successfully solves bimodal deceptive functions concatenation with a lower linkage quality than the linkage quality gathered by P3 (note that the P3 success rate on this problem was only 3\%).

Unfortunately, the influence of ULI on psDSMGA-II was either neutral or negative. In Section 3, we have described a phenomenon that if psDSMGA-II was supported with a perfect linkage at the beginning of the run, then it was unable to find an optimal solution. Similarly to the psDSMGA-II behavior described in Section 3, ULI-psDSMGA-II tends to quickly create large populations (up to hundreds of thousands of individuals). Therefore, it is unable to find the optimal solution. Since ULI is not beneficial for psDSMGA-II, this method will be avoided in the rest of this section.

It is important to check if the size of the population with the highest quality is somehow influenced by ULI. These results are reported in Table 5. Except for the deceptive trap functions, for all problems, the best linkage is found for the significantly lower population sizes when ULI is used. For some of the problems, this linkage is sufficient to solve the problem. Moreover, based on the results presented in Tables 4 and 5, for ULI-LT-GOMEA and for

Table 4: Main results for the considered problems with $n=1200$



Table 5: The median population size with the highest DSM quality for the considered problems with $n=1200$

![img-1.jpeg](img-1.jpeg)

Figure 2: Scalability analysis for median FFE necessary to find an optimal solution for bimodal-based problems
mixed bimodal and bimodal noised concatenations, the linkage quality found by these smaller populations is higher than the linkage quality found by significantly larger populations in LT-GOMEA.

In Figure 2, we present the scalability analysis for the two chosen bimodal problems. For these problems, it is clear that if LT-GOMEA or P3 uses the ULI framework, then it scales significantly better.

## 7 CONCLUSION

In this paper, we have proposed a linkage quality measure for partially additively separable problems. Using the proposed measure, we have investigated the dependency between the linkage quality and the effectiveness of the evolutionary methods. Finally, we have proposed the ULI framework that allows improving the linkage quality. The results analysis indicates many interesting phenomena. The main future work directions are as follows. The linkage quality measures shall be proposed for problems with overlapping blocks. A population-sizing schema that is more suitable for DSMGA-II should be proposed. Another interesting future research direction is the modification of P3 that would improve its convergence. Finally, the population size that is sufficient to obtain a perfect linkage shall be analytically found for other types of deceptive functions.

## ACKNOWLEDGMENTS

This work of Michal Przewozniczek and Marcin Komarnicki was supported by the Polish National Science Centre (NCN) under Grant 2015/19/D/ST6/03115 and the statutory funds of the Department of Computational Intelligence, Wroclaw University of Science and Technology. The work of Bartosz Frej was supported by the statutory funds of the Faculty of Pure and Applied Mathematics, Wroclaw University of Science and Technology.

On measuring and improving the quality of linkage learning in modern evolutionary algorithms applied to solve partially additively separable problems

GECCO '20, July8-12, 2020, Cancún, Mexico
