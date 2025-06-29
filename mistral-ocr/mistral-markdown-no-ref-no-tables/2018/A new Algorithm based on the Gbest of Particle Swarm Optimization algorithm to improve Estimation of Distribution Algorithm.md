# A new Algorithm based on the Gbest of Particle Swarm Optimization algorithm to improve Estimation of Distribution Algorithm 

Qiuyue Zhao<br>Computer science and education software institute<br>Guangzhou University<br>China<br>zhaoqiuyueyue@163.com


#### Abstract

Abstract- Abstract- In recent years, with the rise of artificial intelligence and deep learning, as an evolutionary algorithm based on probability model, estimation of distribution algorithm has been widely research and development. The estimation of distribution algorithm without the traditional genetic operation such as crossover and mutation, is a new kind of evolution model. As an algorithm based on probabilistic mode, the estimation of distribution algorithm establishes a probabilistic model describing the solution space of optimization problems. With the emergence for big data, the convergence of the algorithm and the requirements for solving precision are also increasing. This paper attempts to improve the distribution estimation algorithm. The optimal population of each iteration is found through the location update of each iteration of the Particle Swarm Optimization (PSO) algorithm. The simulation test was carried out with ten benchmark test function. The proposed algorithm was compared with the GA_EDA9improved genetic algorithm) and the basic distribution estimation (EDA) algorithm. Experimental results show that the new algorithm is superior to GA_EDA and basic EDA in terms of convergence and accuracy.


Keywords- Estimation of distribution algorithm; particle Swarm Optimization algorithm; simulation

## I. INTRODUCTION

Evolutionary algorithms are a class of intelligent algorithm that simulate the evolution of "survival of the fittest "in nature. With the development of evolutionary algorithm they are widely used in the fields of artificial intelligence, optimal scheduling, combinatorial optimization and image processing. In recent years, with the emergence of artificial intelligence, intelligent algorithms once again cited the craze of experts and scholars. Although intelligent algorithms are widely used, they still have some shortcomings in theoretical research, which deserves further study.

Estimation of distribution algorithm is a kind of intelligent optimization algorithm based on probability model, which is based on genetic algorithm but developed from genetic algorithm recent years, EDA is widely used in engineering[1][2][3]. In China, a number of experts and scholars have made some improvements to the algorithm. For example, Zhencheng Ye, Xuequn Cao and others combined the cloud model in to the estimation of distribution algorithm [4].

Ting Liu and Liyi Zhang et al. combined the distribution estimation algorithm with the artificial swarm algorithm [5]. Junzhong J, Yufan Quin et al. used chaos optimization and grid filtering strategy to optimize the distribution estimation of distribution algorithm [6]. Based on the existing research, this paper explores a new algorithm. The particle swarm optimization algorithm is used to improve the distribution estimation of distribution algorithm. We try to model the population optimal individual as the estimation of distribution algorithm for each iteration of particle swarm algorithm. The algorithm combining particle swarm optimization algorithm in the characteristics of slow convergence speed quickly before they improving the convergence of the algorithm, at the same time, which can ensure the distribution estimation algorithm achieved through modeling operation such as sampling precision.

This paper is arranged as follows: the first section introduces the back ground and significance of this research. The second section introduces the algorithm principles of estimation of distribution algorithm and its development status. The third section introduces the idea of particle swarm algorithm steps of the simulation experiment. Section 5 compares the convergence and numerical accuracy of the simulation experiment. And then the finally is the conclusion.

## II. Estimation of Distribution Algorithm

Balaja proposed the PBIL algorithm, which is the earliest recognized "Estimation of Distribution Algorithm (EDA)" model[7] in 1994.However, the concept of this algorithm was not yet available in academia at that time until it was first proposed by Larranaga P and Lozano J A in 1996[8].EDA shares many similarities with evolutionary computation techniques such as Genetic Algorithms (GA).However, unlike GA, EDA has no evolution operators such as crossover and mutation. In other word, using the probabilistic model to describe the spatial distribution of candidate solutions, researchers construct a model that describes the distribution from a macroscopic perspective through the use of statistical learning methods, and then randomly sample the model to generate new populations. At the same time, the experimenter achieved the evolution of the population through repeated iterations until the conditions were terminated.

![img-0.jpeg](img-0.jpeg)

Fig 1 Genetic algorithm and estimation of distribution algorithm steps shown
Since 2000, the annual meeting of GECCO has focused on the topic of EDA and the topic has also been opened at other international conferences as follows.It is noteworthy that Larranaga P and Lozano J A published monographs for EDA. And evolutionary computing field authoritative journal "Evolutionary Computation" on the distribution of the estimated algorithm of the special issue in 2002 and 2005 respectively. Most of scholars, especially in the domestic experts and scholars, constantly study on the EDA, including performance analysis [9][10], algorithm improvement [11][12], algorithm application [13][14].Shang Gao and Qinbin Zhang have also published a monograph on EDA and its application [15][16]. The core of EDA is the choice of probabilistic model learning and sampling methods. DEA not only can divided into three categories, including variable-independent, variable-twocorrelation and multivariate correlation, according to the complexity of probability model, but also it can be divided into discrete distribution estimation algorithm, which mostly uses Bayesian network and Markov network as probabilistic model,and continuous distribution, which using Bayesian network and Markov network as a probability model, according to solution vector distribution.

## III. PARTICLE SwARM OptimIZATION

The concept of Particle Swarm Optimization (PSO) is a population based stochastic optimization technique developed by Dr. Eberhart and Dr. Kennedy in 1995, inspired by social behavior of bird flocking or fish schooling[17].In POS,the population is called "particle swarm, " and each individual in the swarm is called a "particle, " which corresponds to a solution to each optimization problem. Each particle keeps track of its coordinates in the problem space which are associated with the best solution (fitness) it has achieved so far.

In a D-dimensional search space, n particles form a particle swarm, and the position of the ith particle is denoted as xi ( $\mathrm{i}=$ $1,2, \ldots, \mathrm{n})$. The velocity of the ith particle is denoted as vi ( $\mathrm{i}=$ $1,2, \ldots, \mathrm{n})$. Particles update their velocity and location by the following formula:

$$
\begin{gathered}
v_{i}(t+1)=w v_{i}(t)+c_{i} r_{i}\left(p b e s t_{i}(t)-x_{i}(t)\right)+c_{2} r_{2}\left(g b e b s t(t)-x_{i}(t)\right) \\
x_{i}(t+1)=x_{i}(t)+v_{i}(t+1)
\end{gathered}
$$

Among them, pbes(i) ( $\mathrm{i}=1,2, \ldots, \mathrm{n}$ ) is the best of individuals, which means the optimal position of the ith particle when it is evolved to the the generation. Determined by the following formula:

$$
\operatorname{phest}_{i}(t)\left\{\begin{array}{lc}
p b e s t_{i}(t-1), & f\left(x_{i}(t)\right) \geq f\left(p b e s t_{i}(t-1)\right) \\
x_{i}(t), & f\left(x_{i}(t)\right)<f\left(p b e s t_{i}(t-1)\right)
\end{array}\right.
$$

Gbest (t) is the optimal population, which refers to the optimal location experienced by all the particles in the population at the time of evolution to the generation, and is determined by the following formula:

$$
\operatorname{gbest}(t)=\min \left\{\operatorname{phest}_{1}(t), \operatorname{phest}_{2}(t), \ldots, \operatorname{phest}_{n}(t)\right\}
$$

In the velocity updating formula (1), w is the inertia weight, $\mathrm{c} 1, \mathrm{c} 2$ is the acceleration factor or learning factor, $\mathrm{r} 1, \mathrm{r} 2$ is a random number that is uniformly distributed on $[0,1]$.

$$
c_{i} r_{i}\left(p b e s t_{i}(t)-x_{i}(t)\right)
$$

belongs to the "cognitive" part, reflecting the particle's memory of their own historical experience and representing the tendency of the particle to the best position in history.

$$
c_{2} r_{2}\left(g b e b s t(t)-x_{i}(t)\right)
$$

Belongs to the "cognitive "part, reflecting the particles memory of their own historical experience and representing the tendency of the particle to the best position in history.

$$
c_{2} r_{2}\left(g b e b s t(t)-x_{i}(t)\right)
$$

belongs to the "society "part, which reflects the tendency of information sharing and cooperation among particles and represents the best historical position in particle directed groups.

## IV. IMPROVED ESTIMATION OF DISTRIBUTION ALGORITHM

This paper mainly introduces an improved estimation of distribution algorithm. The main idea of this algorithm is to apply particle swarm optimization in the "selection" operation of the estimation of distribution algorithm. Different from the parallel hybrid evolutionary algorithm of PSO and EDA[18] introduced in paper [18], this paper introduces the optimization of the population of each iteration through the location update of each iteration of PSO, The optimal individuals of generation are selected as the objects of the estimation of distribution algorithm. The optimal population of individuals generated by each iteration can quickly locate the optimal solution range, so as to speed up the optimization and improve the convergence of the algorithm. Particle swarm optimization (PSO) is to optimize the "micro" level of the optimal solution by updating the position and velocity of each individual in the

population. The estimation of distribution algorithm is based on the probability model and random sampling of the evolutionary trend of the entire population. The "macro"level describes the optimization algorithm. Through the effective combination of the two algorithms, not only the numerical accuracy at the microscopic level can be guaranteed, but also the convergence at the macroscopic level can be realized quickly, and the optimization of the distribution estimation algorithm can be realized. Particle swarm optimization algorithm in the selection of outstanding groups in the process, this article only to update the location of the individual, do not take the velocity update into account. Specific steps are as follows:

Step 1 Initialize the population and randomly generates N individuals ( $\mathrm{i}=1,2 \ldots \mathrm{~N}$ ) In the range of $[-1,1]$;

Step 2 Calculate the fitness of the population, find the optimal individual optimal pbest and optimal population gbest using formulas (3) and (4), and update the individual's position with formula (5):

Step 3 Iterate k times $(\mathrm{k}<\mathrm{T})$ and saves gbest (i), $(\mathrm{i}=$ $1,2, \ldots, \mathrm{k})$.

Step 4 Establish the normal distribution model by calculating the mean $\mathrm{E}(\mathrm{x})=$ and the variance $\mathrm{D}(\mathrm{x})=$ of k excellent individuals through formula (6)and formula(7).

$$
\begin{gathered}
\hat{\mu}=\frac{1}{n} \sum_{i=1}^{n} x_{i} \\
\hat{\sigma}=\sqrt{\frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
\end{gathered}
$$

Step 5 Use formula (8) to randomly sample from the constructed normal distribution to generate a new population.

$$
x=\mu+\sigma\left(-2 \ln u_{1}\right)^{1 / 2} \cos 2 \pi u_{2}
$$

Step 6 If the algorithm reaches the termination condition, end it, otherwise, return to Step2.

The pseudo code is as follows:
$\mathrm{T}=0$;
For $\mathrm{I}=1$ to N
Initialize $\mathrm{X}_{\mathrm{i}}(\mathrm{t})$ and $\mathrm{V}_{\mathrm{i}}(\mathrm{t})$;
Initialize pbest and g best;
FOR $i=1$ to K
Select gbest(i), (i=1,2,...k)
END FOR

$$
\begin{aligned}
& \hat{\mu}=\frac{1}{n} \sum_{i=1}^{n} x_{i} \\
& \hat{\sigma}=\sqrt{\frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}} \\
& x_{k}: \mu(t), \sigma_{k}(t)=\mu+\sigma\left(-2 L n u_{1}\right)^{1 / 2} \cos 2 \pi u_{2}
\end{aligned}
$$

END FOR
If meet the condition
END IF

## V. SIMULATION COMPARISON

In reference [11], we propose an estimation of distribution algorithm that uses crossover operations in genetic algorithms to improve the normal distribution. Through the crossover operation, the search capability of the improved algorithm (GA_EDA) is greatly improved. This section mainly compares the algorithm introduced in this paper (PSO_EDA) with the GA_EDA (improved genetic algorithm) and the improved EDA (non-improved distribution estimation algorithm). Ten computer experiments in Table 1 are used to simulate the commonly used benchmark functions to objectively evaluate the three algorithms in convergence and solution accuracy. In the parameter setting, the parameters of the three algorithms are with the same setting, the size of the initial population 1000 , iteration 100 times, the learning factors c 1 and c 2 are all setting to 2 , the selection probability is 0.4 . The test results of the ten test functions correspond to the following Fig 2 to 11 respectively.

TABLE 1 TEN BENCHMARK FUNCTIONS
![img-1.jpeg](img-1.jpeg)

Fig. 2. Simulation Results of F1

![img-8.jpeg](img-8.jpeg)

Fig. 3. simulation results of F2
![img-9.jpeg](img-9.jpeg)

Fig 4 simulation results of F3
![img-8.jpeg](img-8.jpeg)

Fig. 5. Simulation Results of F4
![img-9.jpeg](img-9.jpeg)

Fig 6. simulation results of F5
![img-8.jpeg](img-8.jpeg)

Fig. 7 simulation results of F6
![img-9.jpeg](img-9.jpeg)

Fig 8 simulation results of $F 7$
![img-8.jpeg](img-8.jpeg)

Fig 9 simulation results of F8
![img-9.jpeg](img-9.jpeg)

Fig.10. Simulation Results of F9

![img-10.jpeg](img-10.jpeg)

Fig.11. simulation results of F10

## VI. CONCLUSION

This paper improves the estimation of distribution algorithm and tries a new fusion method on the basis of previous researchers' fusion of estimation of distribution algorithm and other algorithm; it is bold to propose the fusion of particle swarm algorithm and distribution estimation algorithm that has not been tried before. This paper proposes to optimize the estimation of distribution algorithm by optimizing the population generated by each iteration of particle swarm optimization as elected objects for modeling the estimation of distribution algorithm. The simulation test results of ten benchmark test functions show that the proposed algorithm is superior to the GA_EDA (Improved generic algorithm is) and the basic distribution estimation (EDA) algorithm both in convergence and accuracy. Preliminary excremental results can proves the feasibility of the attempt, but the algorithm parameter settings, optimization and application remain to be further research, such as the subsequent will continue to focus on this problem for a bigger breakthrough

## ACKNOWLEDGMENT

This work is supported by science and technology project of Guangdong Province, China, under Grant No 2016B10127001, and science and technology project of Guangzhou under Grant Nos. 20160710191 and 201604016045.

The template will number citations consecutively within brackets [1]. The sentence punctuation follows the bracket [2]. Refer simply to the reference number, as in [3]-do not use "Ref. [3]" or "reference [3]" except at the beginning of a sentence: "Reference [3] was the first ..."

Number footnotes separately in superscripts. Place the actual footnote at the bottom of the column in which it was cited. Do not put footnotes in the reference list. Use letters for table footnotes.

Unless there are six authors or more give all authors' names; do not use "et al.". Papers that have not been published, even if they have been submitted for publication, should be cited as "unpublished" [4]. Papers that have been accepted for publication should be cited as "in press" [5]. Capitalize only the first word in a paper title, except for proper nouns and element symbols. For papers published in translation journals, please give the English citation first, followed by the original foreign-language citation [6].
