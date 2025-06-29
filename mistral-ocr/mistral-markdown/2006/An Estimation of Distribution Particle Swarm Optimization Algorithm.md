# An Estimation of Distribution Particle Swarm Optimization Algorithm 

Mudassar Iqbal ${ }^{1}$ and Marco A. Montes de Oca ${ }^{2}$<br>${ }^{1}$ Computing Laboratory, University of Kent, Canterbury, United Kingdom<br>mi26@kent.ac.uk<br>${ }^{2}$ IRIDIA, CoDE, Université Libre de Bruxelles, Brussels, Belgium<br>mmontes@ulb.ac.be


#### Abstract

In this paper we present an estimation of distribution particle swarm optimization algorithm that borrows ideas from recent developments in ant colony optimization which can be considered an estimation of distribution algorithm. In the classical particle swarm optimization algorithm, particles exploit their individual memory to explore the search space. However, the swarm as a whole has no means to exploit its collective memory (represented by the array of previous best positions or pbests) to guide its search. This causes a re-exploration of already known bad regions of the search space, wasting costly function evaluations. In our approach, we use the swarm's collective memory to probabilistically guide the particles' movement towards the estimated promising regions in the search space. Our experiments show that this approach is able to find similar or better solutions than the canonical particle swarm optimizer with fewer function evaluations.


## 1 Introduction

The first Particle Swarm Optimization (PSO) algorithm was introduced by Kennedy and Eberhart [12]. It is a population-based optimization algorithm inspired by the social behavior of birds and, like other algorithms of its kind, it is initialized with a population of complete solutions (called particles) randomly located in a $d$-dimensional solution space. An objective function $f: S \rightarrow \Re$ where $S \subset \Re^{d}$, determines the quality of a particle's position, that is, a particle's position represents a solution to the problem being solved. A particle $i$ at time step $t$ has a position vector $\boldsymbol{x}_{i}^{t}$ and a velocity vector $\boldsymbol{v}_{i}^{t}$. Another vector $\boldsymbol{p b e s t}_{i}$ stores the position in which it has received the best evaluation of the objective function. This vector is updated every time the particle finds a better position. Finally, the best vector $\boldsymbol{p b e s t}$ (i.e., the one with the best objective function value) of any particle belonging to the "neighborhood" of particle $i$ is stored in vector $\boldsymbol{s}_{i}$. If the neighborhood of particle $i$ is the whole swarm, then $\boldsymbol{s}_{i}$ is the best solution found so far.

The algorithm iterates updating particles' velocity and position until a stopping criterion is met, usually a sufficiently good solution value or a maximum number of iterations or function evaluations. The update rules are:

$$
\begin{gathered}
\boldsymbol{v}_{i}^{t+1}=\boldsymbol{v}_{i}^{t}+\varphi_{1} \boldsymbol{U}_{1}(0,1) *\left(\boldsymbol{p b e s t _ { i }}-\boldsymbol{x}_{i}^{t}\right)+\varphi_{2} \boldsymbol{U}_{2}(0,1) *\left(\boldsymbol{s}_{i}-\boldsymbol{x}_{i}^{t}\right) \\
\boldsymbol{x}_{i}^{t+1}=\boldsymbol{x}_{i}^{t}+\boldsymbol{v}_{i}^{t+1}
\end{gathered}
$$

where $\varphi_{1}$ and $\varphi_{2}$ are two constants called the cognitive and social coefficients respectively, $\boldsymbol{U}_{1}(0,1)$ and $\boldsymbol{U}_{2}(0,1)$ are two $d$-dimensional uniformly distributed random vectors (generated every iteration) in which each component goes from zero to one, and $*$ is an element-by-element vector multiplication operator.

Clerc and Kennedy [3] introduced the concept of constriction in PSO. Since it is based on a rigorous analysis of the dynamics of a simplified model of the original PSO, it became highly influential in the field to the point that it is now referred to as the canonical PSO. The difference with respect to the original PSO is the addition of a constriction factor in Equation 1. The modified velocity update rule becomes

$$
\boldsymbol{v}_{i}^{t+1}=\chi\left(\boldsymbol{v}_{i}^{t}+\varphi_{1} \boldsymbol{U}_{1}(0,1) *\left(\boldsymbol{p b e s t _ { i }}-\boldsymbol{x}_{i}^{t}\right)+\varphi_{2} \boldsymbol{U}_{2}(0,1) *\left(\boldsymbol{s}_{i}-\boldsymbol{x}_{i}^{t}\right)\right)
$$

with

$$
\chi=\frac{2 k}{\left|2-\varphi-\sqrt{\varphi^{2}-4 \varphi}\right|}
$$

where $k \in[0,1], \varphi=\varphi_{1}+\varphi_{2}$ and $\varphi>4$. Usually, $k$ is set to 1 and both $\varphi_{1}$ and $\varphi_{2}$ are set to 2.05 , giving as a result $\chi$ equal to $0.729[4,5]$. This is the PSO version we use in our comparisons ${ }^{1}$.

From Equations 1 and 3, it is clear that the behavior of every particle is partially determined by its previous experience (through vector $\boldsymbol{p b e s t}_{i}$ ). This memory allows a particle to search somewhere around its own previous best position and the best position ever found by a particle in its neighborhood. However, during a search different particles move and test (i.e., evaluate the objective function) over and over again the same, or approximately the same, region in the search space without any individual improvement. While this is part of the search process and allows the swarm to explore the search space, it is also a waste of computing power when the explored regions have been visited before by the swarm without success. This happens because the swarm as a single entity does not learn.

In this paper, we present a generic extension to the PSO paradigm that allows a particle swarm to estimate the distribution of promising regions-and thus "learn" from previous experience-of the fitness landscape by exploiting the information it gains during the optimization process. This distribution is in turn used to try to keep the particles within the promising regions. It is a modular extension that can be used in any PSO variant that uses a position update rule based on previously found solutions. The estimation of the distribution is done by means of a mixture of normal distributions taking into account the set of pbest vectors. It borrows some ideas from recent developments in Ant

[^0]
[^0]:    ${ }^{1}$ Since there is no agreement about which algorithmic variant can be considered the state-of-the-art in the PSO field, we decided to use this version as our reference.

Colony Optimization (ACO) 6] in which an archive of solutions is used to select the next point to explore in the search space. The underlying assumption of independence between variables common to many Estimation of Distribution Algorithms (EDAs) for continuous optimization problems (see [7) is also present in this work.

The rest of the paper is organized as follows. Section 2 presents some background information on the class of estimation of distribution optimization algorithms to which our proposed algorithm belongs. Section 3 presents in detail the estimation of distribution particle swarm optimizer proposed in this paper. In section 4 we describe the experimental setup we used to assess the performance of our proposed algorithm. Section 5 presents our empirical results along with some discussion and finally, in section 6, we conclude.

# 2 Estimation of Distribution Optimization Algorithms 

Evolutionary Algorithms that use information obtained during the optimization process to build probabilistic models of the distribution of good regions in the search space and that use these models to generate new solutions are called Estimation of Distribution Algorithms (EDAs) 7. The fully joint probability distribution characterizes the problem being solved. Depending on whether there is a priori knowledge about the underlying distribution or not, one can either use a suitable parameterization to get fast convergence rates or use machine learning methods to approximate this unknown distribution, respectively. The latter case is the most commonly found in practice.

EDAs differ in three aspects: (i) in the way they gather information during the optimization process, (ii) in the way they use the gathered information to build probabilistic models, and (iii) in the way they use these models to generate new solutions. An experimental comparison of some of the best known EDAs has been done by Kern et al. 8].

A pseudo-code view of the algorithmic structure behind most EDAs can be seen in Algorithm 1. An EDA starts with a solution population $\mathbf{X}^{0}$ and a solution distribution model $\mathcal{P}^{0}$. The main loop consists of four principal stages. The first stage is to select the best individuals (according to some fitness criteria $f$ ) from the population. These individuals are used in a second stage in which the solution distribution model $\mathcal{P}^{t}$ is updated or recreated. The third stage consists of sampling the updated solution distribution model $\mathcal{P}^{t+1}$ to generate new solutions $\mathbf{X}_{\text {offspring }}^{t+1}$. The last stage involves the base population $\mathbf{X}_{\text {base }}^{t}$, the new solutions and the fitness criteria. The end result is a new base population and the process starts over again until the stopping criteria are satisfied.

There has been a growing interest for EDAs in the last years and there are now some hybrid approaches. One of them is our proposed algorithm. It works as a canonical PSO but uses information gathered during the optimization process to keep the particles within the promising regions so that it does not waste function evaluations. We detail our algorithm in the next section. For a comprehensive presentation of the EDA field see the work of Larrañaga and Lozano 9.

```
Algorithm 1. Algorithmic structure of EDAs.
    /* Initialization */
    Initialize population of solutions \(\mathbf{X}_{\text {base }}^{0}\) and solution distribution model \(\mathcal{P}^{0}\)
    /* Main Loop */
    while Stopping criteria are not satisfied do
        \(\mathbf{X}_{\text {parent }}^{t}=\operatorname{select}\left(\mathbf{X}_{\text {base }}^{t}, f\right) / *\) Selection */
        \(\mathcal{P}^{t+1}=\operatorname{estimate}\left(\mathbf{X}_{\text {parent }}^{t}, \mathcal{P}^{t}\right) / *\) Estimation */
        \(\mathbf{X}_{\text {offspring }}^{t+1}=\operatorname{sample}\left(\mathcal{P}^{t+1}\right) / *\) Sampling */
        \(\mathbf{X}_{\text {base }}^{t+1}=\operatorname{replacement}\left(\mathbf{X}_{\text {offspring }}^{t+1}, \mathbf{X}_{\text {base }}^{t}, f\right) / *\) Replacement */
        \(t=t+1\)
    end while
```


# 3 Estimation of Distribution Particle Swarm Optimization Algorithm 

PSO algorithms are considered to be part of the emerging field of Swarm Intelligence $[10,11]$. Swarm Intelligence is the discipline that studies natural and artificial systems comprised of multiple simple entities that collectively exhibit adaptive behaviors. Some examples of natural swarm intelligent systems are ant colonies, slime molds, bee and wasp swarms.

Besides PSO, the other prominent representative of artificial swarm intelligent systems is Ant Colony Optimization (ACO) [6]. ACO is usually used for solving combinatorial optimization problems. In ACO, artificial ants build solutions incrementally selecting one solution component at a time. The probabilistic selection is biased by a trail of "pheromone" deposited by other ants in previous iterations of the algorithm. The amount of pheromone is proportional to the quality of the complete solutions, so that ants will prefer to choose solution components that are known to yield good solutions. In fact, the role of the so-called pheromone matrix is to approximate the distribution of good solutions in the search space. Seen from this point of view, ACO is an EDA.

A recent development of ACO that extends it to continuous optimization is called $\mathrm{ACO}_{R}[12,13] . \mathrm{ACO}_{R}$ approximates the joint probability distribution, one dimension at a time, by using mixtures of weighted Gaussian functions. The weights try to represent the quality of different search regions. This allows the algorithm to deal with multimodal functions. Figure 1 illustrates the idea of approximating the distribution of good regions in a single dimension using a mixture of weighted Gaussian functions.

The source of information to parameterize these univariate distributions is an archive of solutions of size $k$. The $i$-th component of the $l$-th solution is denoted by $s_{l}^{i}$. For an n-dimensional problem, $1 \leq i \leq n$ and $1 \leq l \leq k$. For each

![img-0.jpeg](img-0.jpeg)

Fig. 1. Mixture of weighted one-dimensional Gaussian functions used to approximate two promising (but in a different degree) search regions
dimension $i$, the vector $\boldsymbol{\mu}_{i}=<s_{1}^{i}, \ldots, s_{k}^{i}>$ is the vector of means that is used to model the univariate probability distribution of the $i$-th dimension. The vector of weights $\boldsymbol{w}=<w_{1}, \ldots, w_{k}>$ is the same across all dimensions because it is based on the relative quality of the complete solutions. Every iteration, after the solutions are ranked, the weights are determined by

$$
w_{l}=\frac{1}{q k \sqrt{2 \pi}} e^{-\frac{(l-1)^{2}}{2(q k)^{2}}}
$$

where $q$ is a parameter that determines the degree of preferability of good solutions. With a small $q$ the best solutions are strongly preferred to guide the search.

Since $\mathrm{ACO}_{R}$ samples the mixture of Gaussians, it has to first select one of the Gaussian functions from the kernel. The selection is done probabilistically. The probability of choosing the $l$-th Gaussian function is proportional to its weight and it is computed using

$$
p_{l}=\frac{w_{l}}{\sum_{j=1}^{k} w_{j}}
$$

Then, $\mathrm{ACO}_{R}$ computes the standard deviation of the chosen Gaussian function as

$$
\sigma_{l}^{i}=\xi \sum_{j=1}^{k} \frac{\left|s_{j}^{i}-s_{l}^{i}\right|}{k-1}
$$

where $\xi$ is a parameter that allows the algorithm to balance its exploration-exploitation behaviors. $\xi$ has the same value for all the dimensions. Having computed all the needed parameters, $\mathrm{ACO}_{R}$ samples the Gaussian function to generate a new solution component. The process is repeated for every dimension, for every ant until a stopping criterion is met.

This fast presentation of $\mathrm{ACO}_{R}$ was needed to introduce our Estimation of Distribution Particle Swarm Optimization (EDPSO) algorithm. The reason is that EDPSO borrows some ideas from $\mathrm{ACO}_{R}$. First, the set of pbest vectors plays the role of the solution archive in $\mathrm{ACO}_{R}$. In EDPSO, $k$ (i.e., the size of the solution archive) is equal to the number of particles. The dynamics of the algorithm, however, is somewhat different. EDPSO works as a canonical PSO as described in section 1 but with some modifications: after the execution of the velocity update rule shown in Equation 3, EDPSO selects one Gaussian function just as $\mathrm{ACO}_{R}$ does. Then, the selected Gaussian function is evaluated (not sampled) to probabilistically move the particle to its new position. If the movement is successful, the algorithm continues as usual, but if the movement is unsuccessful, then the selected Gaussian function is sampled in the same way as in $\mathrm{ACO}_{R}$. The result is a "hybrid" algorithm that explores the search space using the PSO dynamics but when this approach fails (i.e., when a particle's tendency is to move far away from good solutions) a direct sampling of the probability distribution is used instead. It is important to mention that when the selected Gaussian function is evaluated, we use an unscaled version of it, so that its range is $[0,1]$ (i.e., a true probability). A pseudo-code version of EDPSO can be seen in Algorithm 2.

# 4 Experimental Setup 

To evaluate the performance of EDPSO we used the most commonly used benchmark functions in the PSO literature (see [14] for details). We have compared our algorithm with the canonical PSO as described in section 1 Table 1 shows the initialization ranges and the goals that had to be achieved by the algorithms in terms of solution quality, although this goal was not used as a stopping criterion. We ran 30 independent runs for each function in 30,40 and 50 dimensions for a maximum of 120000,160000 , and 200000 function evaluations respectively. The number of particles was equal to 40 .

Table 1. Parameters for the test functions

| Function | Initialization range | Goal |
| :--: | :--: | :-- |
| Sphere | $[-100,100]^{D}$ | 0.01 |
| Rosenbrock | $[-30,30]^{D}$ | 100 |
| Rastrigin | $[-5.12,5.12]^{D}$ | 100 |
| Griewank | $[-600,600]^{D}$ | 0.1 |
| Ackley | $[-32,32]^{D}$ | 0.1 |

```
Algorithm 2. Pseudocode version of the EDPSO algorithm
    /* Initialization. \(k\) is the number of particles,
    and \(n\) is the dimension of the problem */
    for \(i=1\) to \(k\) do
        Create particle \(i\) with random position and velocity
    end for
    Initialize \(g b e s t\) and all \(p b e s t_{i}\) to some sensible values \(/ *\) To a sufficiently large number,
    for example, if we want to minimize a function */
    /* Main Loop */
    \(t=0\)
    while \(g b e s t\) is not good enough or \(t<t_{\max }\) do
        /* Evaluation Loop */
        for \(i=1\) to \(k\) do
            if \(f\left(\boldsymbol{x}_{i}\right)\) is better than \(p b e s t_{i}\) then
                \(\boldsymbol{p}_{i}=\boldsymbol{x}_{i}\)
                \(p b e s t_{i}=f\left(\boldsymbol{x}_{i}\right)\)
            end if
            if \(p b e s t_{i}\) is better than \(g b e s t\) then
                \(g b e s t=p b e s t_{i}\)
                \(\boldsymbol{s}=\boldsymbol{p}_{i}\)
            end if
    end for
    /* Update Loop */
    Rank all \(p b e s t_{i}\) according to their quality
    Compute \(\boldsymbol{w}=<w_{1}, \ldots, w_{k}>\) using Equation 5
    Compute all \(p_{l}\) using Equation 6
    for \(i=1\) to \(k\) do
        for \(j=1\) to \(n\) do
            \(v_{i j}=\chi\left(v_{i j}+\varphi_{1} U_{1}(0,1)\left(p_{i j}-x_{i j}\right)+\varphi_{2} U_{2}(0,1)\left(s_{i j}-x_{i j}\right)\right)\)
            \(x_{i j}^{\text {candidate }}=x_{i j}+v_{i j}\)
            Select a Gaussian function from the kernel according to \(p_{l}\), name it \(g_{l}^{i}\).
            Compute \(\sigma_{l}^{i}\) using Equation 7
            \(p r o b_{\text {move }}=\sigma_{l}^{i} \sqrt{2 \pi} g_{l}^{i}\left(x_{i j}^{\text {candidate }}\right) / * \sigma_{l}^{i} \sqrt{2 \pi}\) unscales the function */
            if \(U_{3}(0,1)<\) proh \(_{\text {move }}\) then
                \(x_{i j}=x_{i j}^{\text {candidate }} / *\) The particle moves normally */
            else
                \(x_{i j}=\operatorname{sample}\left(g_{l}^{i}\right) / *\) New position is a sample from the chosen function */
            end if
            end for
    end for
    \(t=t+1\)
    end while
```

All the benchmark functions we used have the global optimum at or very near the origin, i.e., at the center of the search domain and hence a symmetric uniform initialization would induce a possible bias [15]. To avoid this problem, all functions were shifted to a random location within the search range. This

Table 2. Parameters used by the algorithms

| Algorithm | Parameter | Value |
| :--: | :--: | :--: |
| Canonical PSO | $\varphi_{1}$ | 2.05 |
|  | $\varphi_{2}$ | 2.05 |
|  | $\chi$ | 0.729 |
| EDPSO | $\varphi_{1}$ | 2.05 |
|  | $\varphi_{2}$ | 2.05 |
|  | $\chi$ | 0.729 |
|  | $q$ | 0.1 |
|  | $\xi$ | 0.85 |

approach has been used before and does not confine the swarm to a small region of the search space as is usually done with asymmetrical initializations [16].

Table 2 shows the parameter settings for the algorithms used in our experiments.

# 5 Results 

The benefits of estimating the probability distribution of good regions in the search space and to guide the swarm to search them are reflected (in general) in the quality of the solutions achieved, as well as in the number of function evaluations needed to achieve a solution of certain quality. Table 3 shows the average fitness value (of the best particle in the swarm) after the maximum number of allowed function evaluations.

Table 3. Average fitness value after the maximum number of allowed function evaluations over 30 runs

| Algorithm | Dimension | Sphere | Rosenbrock | Rastrigin | Griewank | Ackley |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Canonical PSO | 30 | 0.0 | 37.48 | 73.52 | 0.023 | 13.35 |
|  | 40 | 0.0 | 55.06 | 133.15 | 0.037 | 18.78 |
|  | 50 | 0.0 | 102.4 | 203.8 | 0.1 | 18.3 |
| EDPSO | 30 | 0.0 | 22.3 | 25.6 | 0.0012 | 0.000019 |
|  | 40 | 0.0 | 37.3 | 33.43 | 0.00098 | 0.00004 |
|  | 50 | 0.0 | 48.12 | 56.18 | 0.0029 | 0.7 |

Table 4. Average number of function evaluations needed to achieve the solution qualities defined in Table 1 and the probability of achieving them

| Algorithm | Dimension | Sphere | Rosenbrock | Rastrigin | Griewank | Ackley |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Canonical PSO | 30 | 13049,1.0 | 20969,0.86 | 7880,0.9 | 11907,0.93 | 13980,0.06 |
|  | 40 | 19365,1.0 | 38442,0.83 | 13296,0.16 | 17563,0.93 | - |
|  | 50 | 27451,1.0 | 61124,0.66 | - | 24584,0.76 | - |
| EDPSO | 30 | 5988,1.0 | 20921,0.96 | 18549,1.0 | 5520,1.0 | 5656,1.0 |
|  | 40 | 8717,1.0 | 24896,0.9 | 28045,1.0 | 7866,1.0 | 8437,1.0 |
|  | 50 | 11971,1.0 | 50442,0.86 | 41659,1.0 | 10741,1.0 | 20284,0.96 |

![img-1.jpeg](img-1.jpeg)

Fig. 2. Solution quality over time. Lines represent the average solution value.
In all benchmark functions, except in the case of the Sphere function, a tendency can be immediately recognized: EDPSO can find better solution qualities after the same number of function evaluations. This is particularly true in the case of the Rastrigin and Ackley functions.

Regarding the issues of speed and reliability, Table 4 shows the average number of function evaluations needed to achieve the solution qualities defined in Table 1 and the probability of achieving them, defined as the success rate (a successful run is one that achieves the specified goal). The average was computed over the successful runs only and rounded off to the nearest integer number greater than the actual number.

From Table 4, it can be seen that EDPSO is faster than the Canonical PSO in getting to the desired objective function value in all functions except in Rastrigin. Entries marked with "-" specify cases in which the goal was not reached in any run. From our experiments, it can be observed that EDPSO shows a significant improvement in terms of the number of function evaluations it needs to get to a certain solution quality. It should also be noted that the behavior of the Canonical PSO is not robust as we go into higher dimensions. In contrast, EDPSO is quite consistent. The Rastrigin case is better explained after examining Figure 2 which shows how the solution quality improves over time for the benchmark problems in 30 dimensions.

The data in Tables 3 and 4 give only a partial view of the behavior of the algorithms. Specifically, they do not show how the solution quality evolves over time. Knowing this is particularly useful to identify which algorithm is best suited for real-time applications in which there are hard time limits or for applications in which we are interested in the solution quality only. In Figure 2(c) it can be seen how the goal defined in Table 1 was reached first by the Canonical PSO but it can also be seen how it stagnates and cannot find better solutions after some more iterations.

# 6 Conclusions 

In this paper we have introduced an Estimation of Distribution Particle Swarm Optimization (EDPSO) algorithm. It is in fact a modular extension that can be used in any other PSO variant that uses a position update rule based on previously found solutions. In effect, it is a learning mechanism that helps the particle swarm explore potentially good regions of the search space. It benefits from the information gathered during the optimization process that is encoded in the array of pbests. The end result is a PSO variant that not only finds better solutions than the Canonical PSO, but also does it with fewer function evaluations. There are some cases, however in which speed is sacrificed for the sake of finding better solutions.

EDPSO is not a pure Estimation of Distribution Algorithm (EDA). It explores the search space in the same way as the Canonical PSO but becomes an EDA whenever particles are pushed further away from good regions (so learnt by the whole swarm). It remains a research issue the problem of handling interactions between variables and the correct parameterization of the probability distributions. The results reported here are encouraging enough to continue looking for ways to allow the particle swarm learn from its past experience.

Acknowledgments. Mudassar lqbal acknowledges support from the Computing Laboratory, University of Kent and the EPSRC grant GR/T11265/01 (eXtended Particle Swarms). Marco A. Montes de Oca acknowledges support from the Programme Aljan, the European Union Programme of High Level Scholarships for Latin America, scholarship No. E05D054889MX. His work was also supported by the ANTS project, an Action de Recherche Concertée funded by the Scientific Research Directorate of the French Community of Belgium.

# References 

1. Kennedy, J., Eberhart, R.: Particle swarm optimization. In: Proceedings of the IEEE International Conference on Neural Networks, Piscataway, NJ, IEEE Press (1995) $1942-1948$
2. Eberhart, R., Kennedy, J.: A new optimizer using particle swarm theory. In: Proceedings of the 6th International Symposium on Micro Machine and Human Science, Piscataway, NJ, IEEE Press (1995) 39-43
3. Clerc, M., Kennedy, J.: The particle swarm-explosion, stability, and convergence in a multidimensional complex space. IEEE Transactions on Evolutionary Computation 6(1) (2002) $58-73$
4. Eberhart, R., Shi, Y.: Comparing inertia weights and constriction factors in particle swarm optimization. In: Proceedings of the 2000 IEEE Congress on Evolutionary Computation. (2000) $84-88$
5. Trelea, I.C.: The particle swarm optimization algorithm: Convergence analysis and parameter selection. Information Processing Letters 85(6) (2003) 317-325
6. Dorigo, M., Stützle, T.: Ant Colony Optimization. The MIT Press (2004)
7. Pelikan, M., Goldberg, D.E., Lobo, F.: A survey of optimization by building and using probabilistic models. Computational Optimization and Applications 21(1) (2002) $5-20$
8. Kern, S., Müller, S.D., Hansen, N., Büche, D., Ocenasek, J., Koumoutsakos, P.: Learning probability distributions in continuous evolutionary algorithms-a comparative review. Natural Computing 3(1) (2004) 77-112
9. Larrañaga, P., Lozano, J.: Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. Genetic Algorithms and Evolutionary Computation, Vol. 2. Springer (2001)
10. Kennedy, J., Eberhart, R., Shi, Y.: Swarm Intelligence. Morgan Kaufmann Publishers, San Francisco, CA, USA (2001)
11. Bonabeau, E., Dorigo, M., Theraulaz, G.: Swarm Intelligence: From Natural to Artificial Systems. Santa Fe Institute Studies on the Sciences of Complexity. Oxford University Press, USA (1999)
12. Socha, K.: ACO for Continuous and Mixed-Variable Optimization. In Dorigo, M., Birattari, M., Blum, C., eds.: Proceedings of ANTS 2004 - Fourth International Workshop on Ant Colony Optimization and Swarm Intelligence. Volume 3172 of LNCS., Springer-Verlag, Berlin, Germany (2004) 25-36
13. Socha, K., Dorigo, M.: Ant colony optimization for continuous domains. Technical Report TR/IRIDIA/2005-037, IRIDIA, Université Libre de Bruxelles (2005)
14. Janson, S., Middendorf, M.: A hierarchical particle swarm optimizer and its adaptive variant. IEEE Transactions on Systems, Man and Cybernetics-Part B 35(6) (2005) $1272-1282$

15. Monson, C.K., Seppi, K.D.: Exposing origin-seeking bias in PSO. In et al., H.G.B., ed.: Proceedings of the Genetic and Evolutionary Computation Conference (GECCO), New York, NY, ACM Press (2005) 241-248
16. Suganthan, P.N., Hansen, N., Liang, J.J., Deb, K., Chen, Y.P., Auger, A., Tiwari, S.: Problem definitions and evaluation criteria for the CEC 2005 special session on real-parameter optimization. Technical Report 2005005, Nanyang Technological University, Singapore and IIT Kanpur, India (2005)