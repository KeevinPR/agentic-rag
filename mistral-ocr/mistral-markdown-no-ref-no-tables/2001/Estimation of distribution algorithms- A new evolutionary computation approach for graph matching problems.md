# Estimation of Distribution Algorithms: A New Evolutionary Computation Approach for Graph Matching Problems 

Endika Bengoetxea ${ }^{1}$, Pedro Larrañaga ${ }^{2}$, Isabelle Bloch ${ }^{3}$, and Aymeric Perchant ${ }^{3}$<br>${ }^{1}$ Department of Computer Architecture and Technology, University of the Basque Country, San Sebastian, Spain endika@si.ehu.es<br>${ }^{2}$ Department of Computer Science and Artificial Intelligence, University of the Basque Country, San Sebastian, Spain pedro@si.ehu.es<br>${ }^{3}$ Department of Signal and Image Processing<br>Ecole Nationale Supérieure des Télécommunications, CNRS URA 820, Paris, France<br>\{Isabelle.Bloch,Aymeric.Perchant\}@enst.fr


#### Abstract

The interest of graph matching techniques in the pattern recognition field is increasing due to the versatility of representing knowledge in the form of graphs. However, the size of the graphs as well as the number of attributes they contain can be too high for optimization algorithms. This happens for instance in image recognition, where structures of an image to be recognized need to be matched with a model defined as a graph. In order to face this complexity problem, graph matching can be regarded as a combinatorial optimization problem with constraints and it therefore it can be solved with evolutionary computation techniques such as Genetic Algorithms (GAs) and Estimation Distribution Algorithms (EDAs). This work proposes the use of EDAs, both in the discrete and continuous domains, in order to solve the graph matching problem. As an example, a particular inexact graph matching problem applied to recognition of brain structures is shown. This paper compares the performance of these two paradigms for their use in graph matching.


## 1 Introduction

Many articles about representation of structural information by graphs in domains such as image interpretation and pattern recognition can be found in the literature [1]. In those, graph matching is used for structural recognition of images: the model (which can be an atlas or a map depending on the application) is represented in the form of a graph, where each node contains information for a particular structure and arcs contain information about relationships between

structures; a data graph is generated from the images to be analyzed and contains similar information. Graph matching techniques are then used to determine which structure in the model corresponds to each of the structures in a given image.

Most existing problems and methods in the graph matching domain assume graph isomorphism, where both graphs being matched have the same number of nodes and links. In some cases this bijective condition between the two graphs is too strong and it is necessary to weaken it and to express the correspondence as an inexact graph matching problem.

When the generation of the data graph from an original image is done without the aid of an expert, it is difficult to segment accurately the image into meaningful entities, that is why over-segmentation techniques need to be applied $[1,2,3]$. As a result, the number of nodes in the data graph increases and isomorphism condition between the model and data graphs cannot be assumed. Such problems call for inexact graph matching, and similar examples can be found in other fields.

Several techniques have been applied to inexact graph matching, including combinatorial optimization [4,5,6], relaxation [7,8,9,10,11], EM algorithm [12,13], and evolutionary computation techniques such as Genetic Algorithms (GAs) [14,15].

This work proposes the use of Estimation Distribution Algorithm (EDA) techniques in both the discrete and continuous domains, showing the potential of this new evolutionary computation approach among traditional ones such as GAs.

The outline of this work is as follows: Section 2 is a review of the EDA approach. Section 3 illustrates the inexact graph matching problem and shows how to face it with EDAs. Section 4 describes the experiment carried out and the results obtained. Finally, Section 5 gives the conclusions and suggests further work.

# 2 Estimation Distribution Algorithms 

### 2.1 Introduction

EDAs [16,17,18] are non-deterministic, stochastic heuristic search strategies that form part of the evolutionary computation approaches, where number of solutions or individuals are created every generation, evolving once and again until a satisfactory solution is achieved. In brief, the characteristic that most differentiates EDAs from other evolutionary search strategies such as GAs is that the evolution from a generation to the next one is done by estimating the probability distribution of the fittest individuals, and afterwards by sampling the induced model. This avoids the use of crossing or mutation operators, and the number of parameters that EDAs require is reduced considerably.

In EDAs, the individuals are not said to contain genes, but variables which dependencies have to be analyzed. Also, while in other heuristics from evolutionary computation the interrelations between the different variables representing the individuals are kept in mind implicitly (e.g. building block hypothesis), in

```
EDA
    \(D_{0} \leftarrow\) Generate \(N\) individuals (the initial population) randomly
    Repeat for \(l=1,2, \ldots\) until a stopping criterion is met
        \(D_{l-1}^{S e} \leftarrow\) Select \(S e \leq N\) individuals from \(D_{l-1}\) according to
        a selection method
    \(\rho_{l}(\boldsymbol{x})=\rho\left(\boldsymbol{x} \mid D_{l-1}^{S e}\right) \leftarrow\) Estimate the probability distribution
        of an individual being among the selected individuals
    \(D_{l} \leftarrow\) Sample \(N\) individuals (the new population) from \(\rho_{l}(\boldsymbol{x})\)
```

Fig. 1. Pseudocode for EDA approach.

EDAs the interrelations are expressed explicitly through the joint probability distribution associated with the individuals selected at each iteration. The task of estimating the joint probability distribution associated with the database of the selected individuals from the previous generation constitutes the hardest work to perform, as this requires the adaptation of methods to learn models from data developed in the domain of probabilistic graphical models.

Figure 1 shows the pseudocode of EDA, in which we distinguish four main steps in this approach:

1. At the beginning, the first population $D_{0}$ of $N$ individuals is generated, usually by assuming an uniform distribution (either discrete or continuous) on each variable, and evaluating each of the individuals.
2. Secondly, a number $S e(S e \leq N)$ of individuals are selected, usually the fittest ones.
3. Thirdly, the $n$-dimensional probabilistic model that better expresses the interdependencies between the $n$ variables is induced.
4. Next, the new population of $N$ new individuals is obtained by simulating the probability distribution learned in the previous step.

Steps 2, 3 and 4 are repeated until a stopping condition is verified. The most important step of this new paradigm is to find the interdependencies between the variables (step 3). This task will be done using techniques from the field of probabilistic graphical models.

Next, some notation is introduced. Let $\boldsymbol{X}=\left(X_{1}, \ldots, X_{n}\right)$ be a set of random variables, and let $x_{i}$ be a value of $X_{i}$, the $i^{\text {th }}$ component of $\boldsymbol{X}$. Let $\boldsymbol{y}=\left(x_{i}\right)_{X_{i} \in \boldsymbol{Y}}$ be a value of $\boldsymbol{Y} \subseteq \boldsymbol{X}$. Then, a probabilistic graphical model for $\boldsymbol{X}$ is a graphical factorization of the joint generalized probability density function, $\rho(\boldsymbol{X}=\boldsymbol{x})$ (or simply $\rho(\boldsymbol{x})$ ). The representation of this model is given by two components: a structure and a set of local generalized probability densities.

With regard to the structure of the model, the structure $S$ for $\boldsymbol{X}$ is a directed acyclic graph (DAG) that describes a set of conditional independences between the variables on $\boldsymbol{X} . \boldsymbol{P} \boldsymbol{a}_{i}^{S}$ represents the set of parents -variables from which

an arrow is coming out in $S$ - of the variable $X_{i}$ in the probabilistic graphical model, the structure of which is given by $S$. The structure $S$ for $\boldsymbol{X}$ assumes that $X_{i}$ and its non descendants are independent given $\boldsymbol{P} \boldsymbol{a}_{i}^{S}, i=2, \ldots, n$. Therefore, the factorization can be written as follows:

$$
\rho(\boldsymbol{x})=\rho\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} \rho\left(x_{i} \mid \boldsymbol{p} \boldsymbol{a}_{i}^{S}\right)
$$

Furthermore, regarding the local generalized probability densities associated with the probabilistic graphical model, these are precisely the ones appearing in Equation 1

A representation of the models of the characteristics described above assumes that the local generalized probability densities depend on a finite set of parameters $\boldsymbol{\theta}_{S} \in \boldsymbol{\Theta}_{S}$, and as a result the previous equation can be rewritten as follows:

$$
\rho\left(\boldsymbol{x} \mid \boldsymbol{\theta}_{S}\right)=\prod_{i=1}^{n} \rho\left(x_{i} \mid \boldsymbol{p} \boldsymbol{a}_{i}^{S}, \boldsymbol{\theta}_{i}\right)
$$

where $\boldsymbol{\theta}_{S}=\left(\boldsymbol{\theta}_{1}, \ldots, \boldsymbol{\theta}_{n}\right)$.
After having defined both components of the probabilistic graphical model, the model itself will be represented by $M=\left(S, \boldsymbol{\theta}_{S}\right)$.

# 2.2 EDAs in Discrete Domains 

In the particular case where every variable $X_{i} \in \boldsymbol{X}$ is discrete, the probabilistic graphical model is called Bayesian network [19]. If the variable $X_{i}$ has $r_{i}$ possible values, $x_{i}^{1}, \ldots, x_{i}^{r_{i}}$, the local distribution, $p\left(x_{i} \mid \boldsymbol{p} \boldsymbol{a}_{i}^{j, S}, \boldsymbol{\theta}_{i}\right)$ is:

$$
p\left(x_{i}{ }^{k} \mid \boldsymbol{p} \boldsymbol{a}_{i}^{j, S}, \boldsymbol{\theta}_{i}\right)=\theta_{x_{i}^{k} \mid \boldsymbol{p} \boldsymbol{a}_{i}^{j}} \equiv \theta_{i j k}
$$

where $\boldsymbol{p} \boldsymbol{a}_{i}^{1, S}, \ldots, \boldsymbol{p} \boldsymbol{a}_{i}^{q_{i}, S}$ denotes the values of $\boldsymbol{P} \boldsymbol{a}_{i}^{S}$, that is the set of parents of the variable $X_{i}$ in the structure $S ; q_{i}$ is the number of different possible instantiations of the parent variables of $X_{i}$. Thus, $q_{i}=\prod_{X_{g} \in} \boldsymbol{P} \boldsymbol{a}_{i} r_{g}$. The local parameters are given by $\boldsymbol{\theta}_{i}=\left(\left(\theta_{i j k}\right)_{k=1}^{r_{i}}\right)_{j=1}^{q_{i}}$. In other words, the parameter $\theta_{i j k}$ represents the conditional probability that variable $X_{i}$ takes its $k^{t h}$ value, knowing that the set of its parent variables take its $j^{t h}$ value. We assume that every $\theta_{i j k}$ is greater than zero.

All the EDAs are classified depending on the maximum number of dependencies between variables that they accept (maximum number of parents that a variable $X_{i}$ can have in the probabilistic graphical model).

Without Interdependencies. The Univariate Marginal Distribution Algorithm (UMDA) [20] is a representative example of this category, which can be

written as:

$$
p_{l}\left(\boldsymbol{x} ; \boldsymbol{\theta}^{l}\right)=\prod_{i=1}^{n} p_{l}\left(x_{i} ; \boldsymbol{\theta}_{i}^{l}\right)
$$

where $\boldsymbol{\theta}^{l}=\left\{\theta_{i j k}^{l}\right\}$ is recalculated every generation by its maximum likelihood estimation, i.e. $\widehat{\theta}_{i j k}^{l}=\frac{N_{i j k}^{l-1}}{N_{i j}^{l-1}} . N_{i j k}^{l}$ is the number of cases on which the variable $X_{i}$ takes the value $x_{i}^{k}$ when its parents are on their $j^{\text {th }}$ combination of values for the $l^{\text {th }}$ generation, and $N_{i j}^{l-1}=\sum_{k} N_{i j k}^{l-1}$.

Pairwise Dependencies. An example of this second category is the greedy algorithm called MIMIC (Mutual Information Maximization for Input Clustering) [21]. The main idea in MIMIC is to describe the true mass joint probability as closely as possible by using only one univariate marginal probability and $n-1$ pairwise conditional probability functions.

Multiple Interdependencies. We will use EBNA (Estimation of Bayesian Network Algorithm) [22] as an example of this category. The EBNA approach was introduced for the first time in [23], where the authors use the Bayesian Information Criterion (BIC) [24] as the score to evaluate the goodness of each structure found during the search. Following this criterion, the corresponding BIC score $-B I C(S, D)$ - for a Bayesian network structure $S$ constructed from a database $D$ and containing $N$ cases can be proved to be as follows:

$$
B I C(S, D)=\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k} \log \frac{N_{i j k}}{N_{i j}}-\frac{\log N}{2} \sum_{i=1}^{n}\left(r_{i}-1\right) q_{i}
$$

where $N_{i j k}$ denotes the number of cases in $D$ in which the variable $X_{i}$ has the value $x_{i}^{k}$ and $\boldsymbol{P} \boldsymbol{a}_{i}$ is instantiated as its $j^{\text {th }}$ value, and $N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$.

Unfortunately, to obtain the best model all possible structures must be searched through, which has been proved to be NP-hard [25]. Even if promising results have been obtained through global search techniques [26|27|28], their computation cost makes them impractical for our problem. As the aim is to find a model as good as possible -even if not the optimal- in a reasonable period of time, a simpler algorithm is preferred. An example of the latter is the so called Algorithm B [29], which is a greedy search heuristic that begins with an arc-less structure and adds iteratively the arcs that produce maximum improvement according to the BIC approximation -but other measures can also be applied. The algorithm stops when adding another arc would not increase the score of the structure.

Local search strategies are another way of obtaining good models. These begin with a given structure, and every step the addition or deletion of an arc that improves most the scoring measure is performed. Local search strategies stop when no modification of the structure improves the scoring measure. The

main drawback of local search strategies is their strong dependence on the initial structure. Nevertheless, since it has been shown in [30] that local search strategies perform quite well when the initial structure is reasonably good, the model of the previous generation could be used as the initial structure.

The initial model $M_{0}$ in EBNA, is formed by its structure $S_{0}$ which is an arcless DAG and the local probability distributions given by the $n$ unidimensional marginal probabilities $p\left(X_{i}=x_{i}\right)=\frac{1}{r_{i}}, i=1, \ldots, n$-that is, $M_{0}$ assigns the same probability to all individuals. The model of the first generation $-M_{1}-$ is learned using Algorithm B, while the rest of the models are learned following a local search strategy that received the model of the previous generation as the initial structure.

Simulation in Bayesian Networks. In EDAs, the simulation of Bayesian networks is used merely as a tool to generate new individuals for the next population based on the structure learned previously. The method used in this work is the Probabilistic Logic Sampling (PLS) proposed in [31]. Following this method, the instantiations are done one variable at a time in a forward way, that is, a variable is not sampled until all its parents have already been so.

# 2.3 EDAs in Continuous Domains 

In this section we introduce an example of the probabilistic graphical model paradigm that assumes the joint density function to be a multivariate Gaussian density.

The local density function for the $i^{t h}$ variable is computed as the linearregression model

$$
f\left(x_{i} \mid \boldsymbol{p a}_{i}^{S}, \boldsymbol{\theta}_{i}\right) \equiv \mathcal{N}\left(x_{i} ; m_{i}+\sum_{x_{j} \in \boldsymbol{p} \boldsymbol{a}_{i}} b_{j i}\left(x_{j}-m_{j}\right), v_{i}\right)
$$

where $\mathcal{N}\left(x ; \mu, \sigma^{2}\right)$ is a univariate normal distribution with mean $\mu$ and variance $\sigma^{2}$.

Local parameters are given by $\boldsymbol{\theta}_{i}=\left(m_{i}, \boldsymbol{b}_{i}, v_{i}\right)$, where $\boldsymbol{b}_{i}=\left(b_{1 i}, \ldots, b_{i-1 i}\right)^{t}$ is a column vector. Local parameters are as follows: $m_{i}$ is the unconditional mean of $X_{i}, v_{i}$ is the conditional variance of $X_{i}$ given $\boldsymbol{P} \boldsymbol{a}_{i}$, and $b_{j i}$ is a linear coefficient that measures the strength of the relationship between $X_{j}$ and $X_{i}$. A probabilistic graphical model built from these local density functions is known as a Gaussian network [32]. Gaussian networks are of interest in continuous EDAs because the number of parameters needed to specify a multivariate Gaussian density is smaller.

Next, an analogous classification of continuous EDAs as for the discrete domain is done, in which these continuous EDAs are also classified depending on the number of dependencies they take into account.

Without Dependencies. In this case, the joint density function is assumed to follow a $n$-dimensional normal distribution, and thus it is factorized as a product

of n unidimensional and independent normal densities. Using the mathematical notation $\boldsymbol{X} \equiv \boldsymbol{\mathcal { N }}(\boldsymbol{x} ; \boldsymbol{\mu}, \sum)$, this assumption can be expressed as:

$$
f_{\boldsymbol{\mathcal { N }}}(\boldsymbol{x} ; \boldsymbol{\mu}, \sum)=\prod_{i=1}^{n} f_{\mathcal{N}}\left(x_{i} ; \mu_{i}, \sigma_{i}\right)=\prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi} \sigma_{i}} e^{-\frac{1}{2}\left(\frac{x_{i}-\mu_{i}}{\sigma_{i}}\right)^{2}}
$$

An example of continuous EDAs in this category is UMDA $_{c}$ [33].

Bivariate Dependencies. An example of this category is MIMIC ${ }_{c}^{G}$ [33], which is basically an adaptation of the MIMIC algorithm [21] to the continuous domain.

Multiple Dependencies. Algorithms in this section are approaches of EDAs for continuous domains in which there is no restriction in the learning of the density function every generation. An example of this category is EGNA $_{B G e}$ (Estimation of Gaussian Network Algorithm) [33]. The method used to find the Gaussian network structure is a Bayesian score+search. In EGNA $_{B G e}$ a local search is used to search for good structures.

Simulation of Gaussian Networks. A general approach for sampling from multivariate normal distributions is known as the conditioning method, which generates instances of $\boldsymbol{X}$ by sampling $X_{1}$, then $X_{2}$ conditionally to $X_{1}$, and so on. The simulation of a univariate normal distribution can be done with a simple method based on the sum of 12 uniform variables.

# 3 Graph Matching as a Combinatorial Optimization Problem with Constraints 

### 3.1 Traditional Representation of Individuals

The choice of an adequate individual representation is a very important step in any problem to be solved with heuristics that will determine the behavior of the search. An individual represents a point in the search space that has to be evaluated, and therefore is a solution. For a graph matching problem, each solution represents a match between the nodes of a data graph $G_{2}$ and those of model graph $G_{1}$.

A possible representation that has already been used either in GAs or discrete EDAs [34] consists of individuals with $\left|V_{2}\right|$ variables, where each variable can take any value between 1 and $\left|V_{1}\right|$. More formally, the individual as well as the solution it represents could be defined as follows: for $1 \leq k \leq\left|V_{1}\right|$ and $1 \leq i \leq\left|V_{2}\right|, X_{i}=k$ means that the $i^{t h}$ node of $G_{2}$ is matched with the $k^{t h}$ node of $G_{1}$.

### 3.2 Representing a Matching as a Permutation

Permutation-based representations have been typically applied to problems such as the Travelling Salesman Problem (TSP), but they can also be used for inexact

graph matching. In this case the meaning of the individual is completely different, as an individual does not show directly which node of $G_{2}$ is matched with each node of $G_{1}$. In fact, what we obtain from each individual is the order in which nodes will be analyzed and treated so as to compute the matching solution that it is representing.

For the individuals to contain a permutation, the individuals will have the same size as the traditional ones described in Section 3.1 (i.e. $\left|V_{2}\right|$ variables long). However, the number of values that each variable can take will be $\left|V_{2}\right|$, and not $\left|V_{1}\right|$ as in that representation. In fact, it is important to note that a permutation is a list of numbers in which all the values from 1 to $n$ have to appear in an individual of size $n$. In other words, our new representation of individuals needs to satisfy a strong constraint in order to be considered as correct, that is, they all have to contain every value from 1 to $n$, where $n=\left|V_{2}\right|$.

More formally, for $1 \leq k \leq\left|V_{2}\right|$ and $1 \leq i \leq\left|V_{2}\right|, X_{i}=k$ means that the $k^{t h}$ node of $G_{2}$ will be the $i^{\text {th }}$ node that is analyzed for its most appropriate match.

Now it is important to define a procedure to obtain the solution that each permutation symbolizes. As this procedure will be done for each individual, it is important that this translation is performed by a fast and simple algorithm. A way of doing this is introduced next.

A solution for the inexact graph matching problem can be calculated by comparing the nodes to each other and deciding which is more similar to which using a similarity function $\varpi(i, j)$ defined to compute the similarity between nodes $i$ and $j$. The similarity measures used so far in the literature have been applied to two nodes, one from each graph, and their aim was to help in the computation of the fitness of a solution, that is, the final value of a fitness function. However, the similarity measure $\varpi(i, j)$ proposed in this work is quite different, as these two nodes to be evaluated are both in the data graph $\left(i, j \in V_{2}\right)$ -see Section 4.3 for more details. With these new similarity values we will identify for each particular node of $G_{2}$ which other nodes in the data graph are most similar to it, and try to group it with the best set of already matched nodes.

Given an individual $\boldsymbol{x}=\left(x_{1}, \ldots, x_{\left|V_{1}\right|}, x_{\left|V_{1}\right|+1}, \ldots, x_{\left|V_{2}\right|}\right)$, the procedure to do the translation is performed in two phases as follows:

1. The first $\left|V_{1}\right|$ values $\left(x_{1}, \ldots, x_{\left|V_{1}\right|}\right)$ that directly represent nodes of $V_{2}$ will be matched to nodes $1,2 \ldots,\left|V_{1}\right|$ (that is, the node $x_{1} \in V_{2}$ is matched with the node $1 \in V_{1}$, the node $x_{2} \in V_{2}$ is matched with the node $2 \in V_{1}$, and so on, until the node $x_{\left|V_{1}\right|} \in V_{2}$ is matched with the node $\left|V_{1}\right| \in V_{1}$ ).
2. For each of the following values of the individual, $\left(x_{\left|V_{1}\right|+1}, \ldots, x_{\left|V_{2}\right|}\right)$, and following their order of appearance in the individual, the most similar node will be chosen from all the previous values in the individual by means of the similarity measure $\varpi$. For each of these nodes of $G_{2}$, we assign the matched node of $G_{1}$ that is matched to the most similar node of $G_{2}$.

The first phase is very important in the generation of the individual, as this is also the one that ensures the correctness of the solution represented by the permutation: all the values of $V_{1}$ are assigned from the beginning, and as we

assumed $\left|V_{2}\right|>\left|V_{1}\right|$, we conclude that all the nodes of $G_{1}$ will have at least a occurrence in the solution represented by any permutation.

# Looking for correct individuals 

As explained in Section 2.2, the simulation process is PLS 31. But a simple PLS algorithm will not take into account any restriction the individuals must have for a particular problem. The interested reader can find a more exhaustive review of this topic in [34], where the authors propose different methods to obtain only correct individuals that satisfy the particular constraints of the problem.

### 3.3 Obtaining a Permutation with Continuous EDAs

Continuous EDAs provide the search with other types of EDA algorithms that can be more suitable for some problems. But again, the main goal is to find a representation of individuals and a procedure to obtain an univocal solution to the matching from each of the possible permutations.

In this case we propose a strategy based on the previous section, trying to translate the individual in the continuous domain to a correct permutation in the discrete one, evaluating it as explained in Section 3.2. This procedure has to be performed for each individual in order to be evaluated. Again, this process has to be fast enough in order to reduce computation time.

With all these aspects in mind, individuals of the same size $\left(n=\left|V_{2}\right|\right)$ will be defined, where each of the variables of the individual can take any value following a Gaussian distribution. This new representation of individuals is a continuous value in $\mathbb{R}^{n}$ that does not provide directly the solution it symbolizes: the values for each of the variables only show the way to translate from the continuous world to a permutation, and it does not contain similarity values between nodes of both graphs. This new type of representation can also be regarded as a way to focus the search from the continuous world, where the techniques that can be applied to the estimation of densities are completely different.

In order to obtain a translation to a discrete permutation individual, we propose to order the continuous values of the individual, and to set its corresponding discrete values by assigning to each $x_{i} \in\left\{1, \ldots,\left|V_{2}\right|\right\}$ the respective order in the continuous individual. The procedure described in this section is further described in 35 .

## 4 Experimental Results. The Human Brain Example

### 4.1 Overview of the Human Brain Example

The example chosen to test the performance of the different EDAs for permutat-ion-based representations in inexact graph matching is a problem of recognition of regions in 3D Magnetic Resonance Images (MRI) of the brain. The data graph $G_{2}=\left(V_{2}, E_{2}\right)$ is generated after over-segmenting an image and contains a node for each segmented region (subset of a brain structure). The model graph

$G_{1}=\left(V_{1}, E_{1}\right)$ contains a node for each of the brain regions to be recognized. The experiments carried out in this chapter are focused on this type of graphs, but could similarly be adapted to any other inexact graph matching problem.

More specifically, the model graph was obtained from the main structures of the the inner part of the brain (the brainstem). This example is a reduced version of the brain images recognition problem in [1]. In our case the number of nodes of $G_{2}$ (number of structures of the image to be recognized) is 94 , and contains 2868 arcs. The model graph contains 13 nodes and 84 arcs.

# 4.2 Description of the Experiment 

This section compares EDA algorithms each other and to a broadly known GA, the GENITOR [36], which is a steady state type algorithm (ssGA).

Both EDAs and GENITOR were implemented in ANSI C++ language, and the experiment was executed on a two processor Ultra 80 Sun computer under Solaris version 7 with 1 GByte of RAM.

The initial population for all the algorithms was created using the same random generation procedure based on a uniform distribution. The fitness function used is described later in Section 4.4.

In the discrete case, all the algorithms were set to finish the search when a maximum of 100 generations or when uniformity in the population was reached. GENITOR, as it is a ssGA algorithm, only generates two individuals at each iteration, but it was also programmed in order to generate the same number of individuals as in discrete EDAs by allowing more iterations (201900 individuals). In the continuous case, the ending criterion was to reach 301850 evaluations (i.e. number of individuals generated).

In EDAs, the following parameters were used: a population of 2000 individuals $(N=2000)$, from which a subset of the best 1000 are selected $\left(S_{e}=1000\right)$ to estimate the probability, and the elitist approach was chosen (that is, always the best individual is included for the next population and 1999 individuals are simulated). In GENITOR a population of 2000 individuals was also set, with a mutation rate of $p_{m}=\frac{1}{\left|V_{2}\right|}$ and a crossover probability of $p_{c}=1$. The operators used in GENITOR where CX [37] and EM [38].

### 4.3 Definition of the Similarity Function

Speaking about the similarity concept, we have used only a similarity measure based on the grey level distribution, so that the function $\varpi$ returns a higher value for two nodes when the grey level distribution over two segments of the data image is more similar. In addition, no clustering process is performed, and therefore the similarity measure $\varpi$ is kept constant during the generation of individuals. These decisions have been made knowing the nature and properties of an MRI image. More formally, the function $\varpi$ can be defined as the set of functions that measure the correspondence between the two nodes of the data graph $G_{2}: \varpi=\left\{\rho_{\sigma}^{u_{2}}: V_{2} \rightarrow[0,1], u_{2} \in V_{2}\right\}$.

# 4.4 Definition of the Fitness Function 

We have chosen a function proposed in [1] as an example. Following this function, an individual $\boldsymbol{x}=\left(x_{1}, \ldots, x_{\left|V_{2}\right|}\right)$ will be evaluated as follows:

$$
\begin{gathered}
f\left(\boldsymbol{x} ; \rho_{\sigma}, \rho_{\mu}, \alpha\right)=\alpha\left[\frac{1}{\left|V_{2}\right|\left|V_{1}\right|} \sum_{i=1}^{\left|V_{2}\right|} \sum_{j=1}^{\left|V_{1}\right|} \sum_{i}\left(1-\left|c_{i j}-\rho_{\sigma}^{u_{1}^{i}}\left(u_{2}^{j}\right)\right|\right)\right]+ \\
(1-\alpha)\left[\frac{1}{\left|E_{2}\right|\left|E_{1}\right|} \sum_{e_{1}^{i}=\left(u_{1}^{i}, v_{1}^{i}\right) \in E_{1}} \sum_{e_{2}^{k}=\left(u_{2}^{j}, v_{2}^{j}\right) \in E_{2}}\left(1-\left|c_{i j} c_{i^{\prime} j^{\prime}}-\rho_{\mu}^{e_{1}^{i}}\left(e_{2}^{k}\right)\right|\right)\right]
\end{gathered}
$$

where

$$
c_{i j}= \begin{cases}1 & \text { if } X_{i}=j \\ 0 & \text { otherwise }\end{cases}
$$

$\alpha$ is a parameter used to adapt the weight of node and arc correspondences in $f$. For each $u_{1}^{i} \in V_{1}, \rho_{\sigma}^{u_{1}^{i}}$ is a function from $V_{2}$ into $[0,1]$ that measures the correspondence between $u_{1}^{i}$ and each node of $V_{2}$. Similarly, for each $e_{1} \in E_{1}$, $\rho_{\mu}$ is the set of functions from $E_{2}$ into $[0,1]$ that measure the correspondence between the arcs of both graphs $G_{1}$ and $G_{2}$. The value of $f$ associated for each variable returns the goodness of the matching. Typically $\rho_{\sigma}$ and $\rho_{\mu}$ are related to the similarities between node and arc properties respectively.

Node properties are described as attributes on grey level and size, while edge properties correspond to spatial relationships between nodes.

### 4.5 Experimental Results

Results such as the best individual obtained, the computation time, and the number of evaluations to reach the final solution were recorded for each of the experiments. The computation time obtained is the CPU time of the process for each execution, and therefore it is not dependent on the load of the system. The latter is given as a measure to illustrate the different computation complexity of all the algorithms.

Each algorithm was executed 10 times. The non-parametric tests of KruskalWallis and Mann-Whitney were used to test the null hypothesis of the same distribution densities for all -or some- of them. This task was done with the statistical package S.P.S.S. release 9.00. The results for the tests applied to all the algorithms are shown in Table 1. The study of particular algorithms gives the following results:

- Between algorithms of similar complexity only:
- UMDA vs. UMDA $_{c}$. Fitness value: $p<0.001$; CPU time: $p<0.001$; Evaluations: $p<0.001$.

Table 1. Mean values of experimental results after 10 executions for each algorithm of the inexact graph matching problem of the Human Brain example.

- MIMIC vs. MIMIC ${ }_{c}$. Fitness value: $p<0.001$; CPU time: $p<0.001$; Evaluations: $p<0.001$.
- EBNA vs. EGNA. Fitness value: $p<0.001$; CPU time: $p<0.001$; Evaluations: $p<0.001$.
These results show that the differences between EDAs in the discrete and continuous domains are significant in all the cases analyzed, meaning that the behavior of selecting a discrete learning algorithm or its equivalent in the continuous domain is very different. It is important to note that the number of evaluations was expected to be different, as the ending criteria for the discrete and continuous domains were also different. In all the cases, continuous EDAs obtained a fitter individual, but the CPU time and number of individuals created was also bigger.
- Between discrete algorithms only:
- Fitness value: $p<0.001$. CPU time: $p<0.001$. Evaluations: $p<0.001$.

In this case significant results are also obtained in fitness value, CPU time, and number of evaluations. The discrete algorithm that obtained the best result was UMDA, closely followed by EBNA. The differences in the CPU time are also according to the complexity of the learning algorithm they apply. Finally, the results show that MIMIC required significantly less individuals to converge (to reach the uniformity in the population), whereas the other two EDA algorithms require nearly the same number of evaluations to converge. The genetic algorithm GENITOR is far behind the performance of EDAs. The computation time is also a factor to consider: the fact that GENITOR requires about 7 hours for each execution shows the complexity of the graph matching problem.

- Between continuous algorithms only:
- Fitness value: $p=0.342$. CPU time: $p<0.001$. Evaluations: $p=1.000$.

Differences between all the continuous EDAs appear to be not significant. As expected, the CPU time required for each of them is according to the complexity of the learning algorithm. On the other hand, the fact of having the same number of evaluations is due to the same ending criterion. Speaking about the differences in computation time between discrete and continuous EDA algorithms, it is important to note that the latter ones require all the

300000 individuals to be generated before they finish the search. The computation time for the continuous algorithms is also longer than the discrete equivalents as a result of several factors: firstly, due to the higher number of evaluations they perform each execution, secondly because of the longer individual-to-solution translation procedure that has to be done for each of the individuals generated, and lastly, as a result of the longer time required to learn the model in continuous spaces.

We can conclude from the results that generally speaking continuous algorithms perform better than discrete ones, either when comparing all of them in general or only with algorithms of equivalent complexity.

# 5 Conclusions and Further Work 

This work describes the application of the EDA approach to graph matching. Different individual representations have been shown in order to allow the use of discrete and continuous representation and algorithms.

In an experiment with real data a comparison of the performance of this new approach between the discrete and continuous domains has been done, and continuous EDAs have shown a better performance looking at the fittest individual obtained, however a longer execution time and more evaluations were required. Additionally, other fitness functions should be tested with this new approach. Techniques such as $[39,40]$ could also help to introduce better similarity measures and therefore improve the results obtained considerably.

For the near future there are several tasks to be done. The most important is to perform more experiments with more data images (more data graphs) in order to evaluate the effectiveness of the proposed matching heuristic with more examples. In addition, a deeper study on the influence of node and arc correspondences requires also to be done. These new experiments are expected to highlight the importance of the structural aspects (the edges) as appreciated in our recent work.

## Acknowledgments

This work has been partially supported by the University of the Basque Country, the Spanish Ministry for Science and Education, and the French Ministry for Education, Research and Technology with the projects 9/UPV/EHU 00140.226-12084/2000, HF1999-0107, and Picasso-00773TE respectively. The authors would also like to thank Ramon Etxeberria, Iñaki Inza and Jose A. Lozano for their useful advice and contributions to this work.
