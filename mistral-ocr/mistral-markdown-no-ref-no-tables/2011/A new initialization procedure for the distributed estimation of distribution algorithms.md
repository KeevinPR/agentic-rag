# A new initialization procedure for the distributed estimation of distribution algorithms 

Santiago Muelas $\cdot$ José-María Peña $\cdot$ Antonio LaTorre $\cdot$ Víctor Robles

Published online: 9 April 2010
(c) Springer-Verlag 2010


#### Abstract

Estimation of distribution algorithms (EDAs) are one of the most promising paradigms in today's evolutionary computation. In this field, there has been an incipient activity in the so-called parallel estimation of distribution algorithms (pEDAs). One of these approaches is the distributed estimation of distribution algorithms (dEDAs). This paper introduces a new initialization mechanism for each of the populations of the islands based on the Voronoi cells. To analyze the results, a series of different experiments using the benchmark suite for the special session on Real-parameter Optimization of the IEEE CEC 2005 conference has been carried out. The results obtained suggest that the Voronoi initialization method considerably improves the performance obtained from a traditional uniform initialization.


Keywords Estimation of distribution algorithms $\cdot$ Distributed evolutionary algorithms $\cdot$ Initialization $\cdot$ Continuous optimization

## 1 Introduction

Currently, there is a wide range of optimization tools to deal with many complex problems in very different fields, such as

[^0]engineering, bioinformatics or scheduling. Evolutionary techniques are receiving more and more attention in these complex optimization scenarios. Their exploratory characteristics play a significant role in problems with difficult fitness landscapes. On the other hand, the use of populationbased evolutionary algorithms (EAs) has the drawback of the number of evaluations required to guide the search.

Because EAs are inherently parallel, the so-called parallel evolutionary algorithms (pEAs) have been studied as an alternative to tackle one of the aspects of this drawback (Alba 2002). A successful example of parallel evolutionary algorithms is the model called distributed evolutionary algorithms (dEAs) or island model. In this model, independent nodes execute a local EA, exchanging information under given conditions. The information exchanged provides the mechanism to enhance the local population with the improvements already achieved in other nodes (populations). This kind of EAs seems to improve the numerical and runtime behavior of the basic algorithm in many cases (Alba and Troya 2002; Risco-Martín et al. 2008).

Estimation of distribution algorithms (EDAs) (Mühlenbein and Paass 1996; Larrañaga and Lozano 2002), which have become a fruitful new paradigm for population-based evolutionary computation, have not been an exception. Parallel estimation of distribution algorithms (pEDAs) have been proposed with a broad range of possible parallel approaches (Ocenasek 2001; Bengoetxea 2002; delaOssa et al. 2004).

A relevant aspect in EAs is the initialization of the starting population. This issue is important to provide a good supply of initial individuals to start up the stochastic search. When there is more than one population, the influence of the initial individuals on each of the subpopulations should also be considered.

This paper proposes a new initialization procedure based on a topological tool (Voronoi diagrams) to restrict the


[^0]:    S. Muelas ( $\boxtimes) \cdot$ J.-M. Peña $\cdot$ A. LaTorre $\cdot$ V. Robles

    Department of Computer Systems Architecture and Technology, Facultad de Informática, Universidad Politécnica de Madrid, Madrid, Spain
    e-mail: smuelas@fi.upm.es
    J.-M. Peña
    e-mail: jmpena@fi.upm.es
    A. LaTorre
    e-mail: atorre@fi.upm.es
    V. Robles
    e-mail: vrobles@fi.upm.es

initial search space of the different nodes of the island model. Within each island, the initialization method applies the D2 method (Glover et al. 1998), an heuristic used for the maximum diversity problem, for generating a diverse set of individuals which tries to maximize the coverage of the solutions space. For analyzing the effects of the proposed mechanism, an experiment with 108 distributed EDA configurations has been conducted over the benchmark suite of the special session on Real-Parameter Optimization of the IEEE CEC 2005 conference (Suganthan et al. 2005). The results have been validated using a statistical non-parametric test.

The rest of the paper is organized as follows: Sect. 2 presents an overview of the parallel evolutionary and initialization techniques. Section 3 details the proposed technique and the rationale behind it. In Sect. 4, the experimental scenario is described in detail. Section 5 presents and comments on the results obtained and lists the most relevant facts extracted from this analysis. Finally, Sect. 6 contains the concluding remarks obtained from this study.

## 2 Related work

### 2.1 Estimation of distribution algorithms

Estimation of distribution algorithms are non-deterministic, stochastic heuristic search strategies that are part of the evolutionary computation paradigm (Mühlenbein and Paass 1996; Larrañaga and Lozano 2002). In EDAs, multiple solutions or individuals are created every generation, evolving successively until a satisfactory solution is achieved. In brief, the characteristic that most differentiates EDAs from other evolutionary search strategies, such as genetic algorithms (GAs) is that the evolution from one generation to the next one is achieved by estimating the joint probability distribution of a set of individuals followed by sampling the induced model. This avoids the use of crossing and mutation operators, thus reducing the number of parameters that are required by EDAs. The general schema of the algorithm is described in Algorithm 1.

```
Algorithm 1 EDA schema
    Create initial population (popSize individuals) \(D_{0}\)
    \(i=0\)
    repeat
        Evaluate population \(D_{i}\)
        \(D_{i}^{*}=\operatorname{Select} N \leq \operatorname{popSize}\) individuals from \(D_{i}\)
        Estimate a new model \(M\) from \(D_{i}^{*}\)
        \(D^{\prime}=\) Sample popSize individuals from \(M\)
        Evaluate \(D^{\prime}\)
        \(D_{i+1}=\) Select popSize individuals from \(D_{i} \cup D^{\prime}\)
        \(i=i+1\)
    until stop criterion
```

Graphical models have been commonly used for estimating the joint probability distribution. Some authors have proposed Bayesian networks to represent the probability distribution for discrete domains, whereas Gaussian networks are usually employed for continuous domains. Based on the probabilistic model considered, three main groups of EDAs can be distinguished: univariate models, which assume that variables are marginally independent; bivariate models, which accept dependences between pairs of variables; and multivariate models, in which there is no limitation on the number of dependences. In this study, we are going to focus on the univariate marginal distribution algorithm for Gaussian models $\left(\mathrm{UMDA}_{g}\right)$ (Larrañaga and Lozano 2002) because it has usually been considered as baseline for comparison. In addition, as a result of its simplicity, it is easier to identify and analyze the benefits coming from the proposal. $\mathrm{UMDA}_{g}$ uses the normal distribution to model the density of each variable. Therefore, the induction of the model is reduced to the estimation of $\mu$ and $\sigma^{2}$ of each variable.

### 2.2 Distributed estimation of distribution algorithms

In the distributed evolutionary algorithm, ${ }^{1}$ the overall population is distributed over multiple subpopulations and occasionally allows the migration or exchange of some individuals among the different islands. Therefore, each node executes an independent algorithm on an independent population. An important aspect of the performance of dEAs is the migration strategy. This is configured through different parameters (Cantú-Paz 2001): (1) Migration frequency: How often (in generations) is information sent? (2) Migration rate: How many individuals migrate each time? (3) Information selection: What information is selected to migrate? (4) Acceptance policy: How are the incoming information and the local algorithm state combined? and (5) Migration topology: Which island sends information to which other?

Close scrutiny of migration parameters (Petty and Leuze 1989) has verified that, even though EAs with small populations risk being trapped in a local optimum, an appropriate migration strategy can avoid a suboptimal solution from dominating all the populations. This appropriate strategy must be adjusted between the limits of a low interaction (which would practically imply the execution of $N$ independent algorithms) and an excessive interaction (that would lead to the predominance of only one solution). A correct configuration can help in obtaining better results with fewer evaluations, but configuring these optimal parameters is not a simple issue (Whitley et al. 1999; Alba and Troya 2000; Muelas et al. 2007).

[^0]
[^0]:    ${ }^{1}$ Also known as coarse-grained, multiple-deme or island models.

### 2.3 Initialization

The initialization of population-based evolutionary algorithms is hardly addressed in the literature (Kallel and Schoenauer 1997). Nevertheless, every expert in the field agrees that a bad initialization can make evolution to converge prematurely at suboptimal solutions.

In many cases, the initialization process depends on the application field if an approximate solution to the problem is known. In Ramsey and Grefenstette (1993), Ramsey concluded that, initializing the population with members of previously seen states, accelerated the learning in a changing environment. Otherwise, if the individuals of the population can be built through certain heuristic techniques, these could be a good starting point to reach the optimum (Schwarz and Očenášek 2000). However, this strategy has general drawbacks: (1) it completely depends on the field of application and (2) it may involve biasing the search process towards certain kinds of solutions (possibly others than the optimal ones). Another approach is to use other metaheuristic algorithms (with different fitness functions) for initializing the population (de Garis 1991). In Ahuja and Orlin (1997), it was proposed to develop the initial population with a good randomized heuristic. In Ahuja et al. (2000), this recommendation was followed using the construction phase of a GRASP algorithm as the initial population of a genetic algorithm.

Island models are especially sensitive to initialization, not only for the aforementioned reasons, but also because of the possible mutual dependence between the different populations of the islands. There is very little literature on this topic and, therefore, this is one of the aspects to be studied in depth.

## 3 Contribution

In this paper, a new initialization mechanism for dEDAs is presented. The main idea of this procedure is to use a Voronoi tessellation (Aurenhammer 1991) to define a partition set of the solution space in which each island or node will start its own exploration. The proposal applies several steps as presented in Fig. 1.

To create the tesselation, a set of reference points $\left(r_{i}\right)$ need to be created and assigned to each of the $n$ islands. The initial population of island $i$ will be a set of diverse
points in the solution space which are closer to the $i$ th reference point than to any other reference point.

To avoid the generation of small partitions, we have applied two methods for selecting a good set of diverse reference points. The first method uses a controlled randomization and frequency memory procedure for generating a set $S=\left\{s_{1}, s_{2}, \ldots, s_{N}\right\}, N>n$ of initial diverse individuals. This method is influenced by the work in Duarte et al. (2009) for a Scatter Search algorithm. The procedure starts with the division of the range of each dimension into $s r$ subranges of equal size. Then, for each generated individual, a subrange for each dimension is selected based on the inverse probability value of the frequency count associated with the sub-range. Finally, a value is uniformly generated within the selected interval and the frequency count associated with the subrange is incremented.

The second method takes the set of $N$ points and extracts the $N-n$ individuals with the minimum distance between any pair of points. This procedure is based on the $D 2$ Method presented in Glover et al. (1998) for the maximum diversity problem. This method was chosen because it provides a good balance between the diversity of the individuals and the speed of computation. The general schema of the algorithm is described in Algorithm 2.

```
Algorithm 2 D2 Method
    \(S e l=S\)
    while \(\mid S e l \mid>n\) do
        \(s_{i}^{*}=\operatorname{argmin}_{s_{i} \in S e l}\left\{d\left(s_{i}, S e l\right)\right\}\)
        \(S e l=S e l-\left\{s_{i}^{*}\right\}\)
    end while
```

The distance between an individual $s_{i}$ and a set $X=$ $\left\{s_{j}: j \in I\right\}$ is defined as follows:
$d\left(s_{i}, X\right)=\min \left\{d\left(s_{i}, s_{j}\right) / s_{j} \in X\right\}$
For our experiments with continuous problems, the Euclidean distance has been considered between every pair of individuals.

Once the reference points are created, the next action to execute is the generation of the population of each island. For this task, two steps are applied one after another. First, $k *$ popSize individuals are created and distributed uniformly among the islands, i.e, each island is assigned $k *$ popSize $/ n$ individuals. Each new individual is assigned to
![img-0.jpeg](img-0.jpeg)

Fig. 1 Initialization procedure

the island which distance to its reference point is minimum. This procedure is described by the pseudocode of Algorithm 3. Then the $D 2$ Method is applied to each set of individuals so that the final island set contains the most diverse popSize $/ n$ solutions.

```
Algorithm 3 Population initialization
    for \(i=0\) to \(n\) do
        Population \(_{i}=\emptyset\)
    end for
    while \(\left|\bigcup_{i=0}^{i=n}\right.\) Population \(\left._{i}\right|<k *\) PopSize do
        newindividual \(=\) GenerateARandomIndividual
        Let \(i^{*} / d\left(\right.\) newindividual, \(\left.\left.s_{i^{*}}\right)=d\) (newindividual, \(S\) )
        if |Population \(\left._{i^{*}}\right|<k *\) PopSize \(\left./ n\right\) then
            Population \(\left._{i^{*}}=\right.\) Population \(\left._{i^{*}} \cup\right.\) newindividual
        end if
    end while
```

For the purpose of clarifying the effects of the procedure, a simple example is provided. Figure 2 details the results of initializing a two-dimensional function with the new method and with the traditional uniform approach. The cell lines in the new method diagram delimit the individuals that would be assigned to each island.

Rationale: our approach carries out a systematic initialization procedure following two criteria: (1) homogeneous coverage of the whole solution space, (2) no overlap of the solution space explored by each island.
![img-2.jpeg](img-2.jpeg)
(a)
![img-2.jpeg](img-2.jpeg)
(b)

Fig. 2 Initialization comparison. a Voronoi initialization. b Random uniform initialization

Table 1 Parameters chosen for the experiments

Table 2 \# $N$ of configurations in 10D with significant differences
A $>\mathrm{B}$ represent that the results of A were statistically better than those of B
populations (64, 100, 200, 512, 800 and 1,600) were also executed.

The number of islands was fixed to 8 . The proposed procedure obtains better results with a high number of islands but, because of the maximum number of evaluations of the benchmark, a higher number would imply a reduced number of individuals per island (not appropriate for EDAs) or a considerably reduced number of iterations. Therefore, the selected number offers a good trade-off between the number of islands and the number of iterations.

## 5 Analyzing the results

As mentioned in the previous section, 108 uniformly initialized configurations were compared against their equivalent Voronoi configurations. For each problem, each pair of uniform and Voronoi configurations were compared with a non-parametric Wilcoxon's rank sum test with a significance level of $\alpha=0.01$.Tables 2 and 3 present the number of comparisons per function in which the results were statistically significant as well as the aggregated number for all the functions. It can be seen that Voronoi configurations clearly obtain a higher number of significant

Table 3 \# $N$ of configurations in 30D with significant differences
A $>\mathrm{B}$ represent that the results of A were statistically better than those of B
results than their uniform counterparts, this number being higher with the 10 dimensional functions and with the hardest 8 functions of the benchmark (18-25). Because the number of partitions is the same for both the 10 and the 30 dimensional functions, each island is less affected by the local optima in the 10 dimensional scenario and therefore obtains better results.

A global comparison of the best configurations of both types of initializations per population size and the sequential EDAs was also carried out. The criterion used for selecting the best configurations was: for each population size, select the configuration with the minimum sum of average errors over all the functions in both 10 and 30 dimensions. Similarly to the analysis used in the CEC'05 special session, each algorithm was ranked at each function according to its average error. Although the objective of this study was not to tune an EDA algorithm to obtain the best results in the benchmark, the best algorithm from the special session, G-CMA-ES, has also been included in the analyses. Table 4 presents the average ranking of all the algorithms. Here, Voronoi configurations also obtain better results than their equivalent uniform ones being the Voronoi configuration of 512 individuals the best EDA algorithm. For the purpose of determining the significance

Table 4 Average ranking of the best algorithms

Table $5 p$-Values of the comparisons of the best configurations
$\sqrt{ }$ represents that the $p$-value is $\alpha=0.01$ significant
$\times$ represents that the $p$-value is not significant
of these results, a non-parametric paired Wilcoxon's ranksum test was applied. Table 5 shows the $p$-values of the comparisons of the best EDA configuration (Voronoi with 512 individuals) against the rest of the algorithms. It can be observed that the best Voronoi configuration is $\alpha=0.01$ significantly better in each comparison to the rest of the EDAs algorithms in both 10 and 30 dimensions except against the uniform initialized configuration of 512 individuals in 30 dimensions and the Voronoi configuration of 800 individuals.

It can also be seen that this configuration is clearly superior to any of the sequential EDAs executed. In addition, it can be observed that the dEDA configurations with the fewer number of individuals tend to obtain better results. This is partially due to the constraint in the maximum number of fitness evaluations imposed by the benchmark, which allows them to execute for more iterations. Finally, when analyzing the comparison against a
specially tuned algorithm for the session, the G-CMA-ES algorithm, it can be seen that although the G-CMA-ES is significantly better than the best dEDA configuration in 10 dimensions $p$-value $=0.05$, with the 30 dimensional functions, the G-CMA-ES has worse rank and its results are not significantly better.

Figure 3 shows the evolution of the average score for the 10 dimensional $f 20$ function. ${ }^{2}$ The evolution of the score of the algorithms on the next generations is almost the same for both methods but the influence of the first generations clearly increases the performance of the Voronoi configurations.

Finally, an analysis of the influence of the initialization in the migration schemes was also carried out. For this task, the total number of individuals that are exchanged throughout the evolution for each distributed configuration was measured, i.e.:

$$
\frac{\text { @iterations }}{\text { Migration }_{\text {period }}} \times \text { Migration }_{\text {rate }} \times \text { Topology }_{\text {degree }}
$$

Table 6 presents the average of this number for the 10 distributed configurations with the minimum average error for all the functions. This number represents the total number of individuals that are exchanged along the execution. For obtaining the number of individuals that were actually accepted on each island, the acceptance criterion needs to be taken into account and averaged through all the executions. In general, Voronoi configurations need to exchange fewer individuals than the uniform configurations. This effect is much clearer for the 10 dimensional functions and with bigger population sizes (which, because of the benchmark constraints, have also a smaller number of iterations). It seems that, to obtain the best results, the Voronoi initialized islands need less interaction with their neighboring islands, so they can intensify the exploration on their isolated region (in particular, in their earlier iterations).

## 6 Conclusions

This paper presents a new initialization method for the distributed estimation of distribution algorithms. The proposed initialization is based on Voronoi cells that isolate the initial search space of each island and uses a heuristic method for uniformly covering each region of the search space. Several parameter values have been tested on the standard CEC'05 continuous benchmark suite. To analyze the results, non-parametrical tests were applied. The obtained results show that the best overall performance is

[^0]
[^0]:    ${ }^{2}$ The evolution of the average scores in most of the other functions follows a similar pattern.

Fig. 3 Evolution of the average score for the $f 20$ function
![img-3.jpeg](img-3.jpeg)

Table 6 Number of individuals exchanged between the best configurations

obtained with Voronoi configurations and that, in general, the Voronoi configurations tend to improve the results of the traditional initialization method. The partition of the search space reduces the modality of the constrained regions and offers the possibility, at least in the earliest generations, to emphasize the search in the starting regions. Thus, the search for the optimal solutions is more effective. The analysis also discovered that the best Voronoi configurations need less interaction between the islands than the best uniform configuration. With a greater exchange of individuals, the beneficial properties of the proposed initialization get diluted. The Voronoi configurations also outperformed their equivalent population-sized (both global and island population sizes) sequential EDAs. This approach has been proposed for EDAs, since they are more influentiated by the initial population than other evolutionary algorithms with more explorative mechanisms. However, this procedure could also improve the performance of other evolutionary algorithms by reaching a higher score or helping them to improve their convergence speed.

Acknowledgments This work was supported by the Madrid Regional Education Ministry and the European Social Fund and financed by the Spanish Ministry of Science TIN2007-67148. The authors thankfully acknowledge the computer resources, technical expertise and assistance provided by the Centro de Supercomputación y Visualización de Madrid (CeSViMa) and the Spanish Supercomputing Network. We would also like to thank the reviewers for their suggestions.
