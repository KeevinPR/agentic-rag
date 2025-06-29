# Optimizing Continuous Problems Using Estimation of Distribution Algorithm Based on Histogram Model ${ }^{*}$ 

Nan Ding ${ }^{1}$, Shude Zhou ${ }^{2}$, and Zengqi Sun ${ }^{2}$<br>${ }^{1}$ Department of Electronic Engineering, Tsinghua University, Beijing, China ding-n04@mails.tsinghua.edu.cn<br>${ }^{2}$ Department of Computer Science and Technology, Tsinghua University, Beijing, China zsd03@mails.tsinghua.edu.cn, szq-dcs@tsinghua.edu.cn


#### Abstract

In the field of estimation of distribution algorithms, choosing probabilistic model for optimizing continuous problems is still a challenging task. This paper proposes an improved estimation of distribution algorithm (HEDA) based on histogram probabilistic model. By utilizing both historical and current population information, a novel learning method - accumulation strategy - is introduced to update the histogram model. In the sampling phase, mutation strategy is used to increase the diversity of population. In solving some wellknown hard continuous problems, experimental results support that HEDA behaves much better than the conventional histogram-based implementation both in convergence speed and scalability. Compared with UMDA-Gaussian, SGA and CMA-ES, the proposed algorithms exhibit excellent performance in the test functions.


## 1 Introduction

Recently, estimation of distribution algorithms have become the hot topic in the field of evolutionary computation [1]. The contribution of EDAs not only lies in its ability to explicitly learn the linkage relationship among variables, but also provides a novel macroscopical evolutionary paradigm, in which without any conventional operators, the population evolves by iteratively learning and sampling the probabilistic distribution model that describes the movements of population. Theoretical and empirical researches have shown that EDAs are a class of efficient black-box optimization algorithms.

The core of EDAs is the probabilistic model.
For $0-1$ domain problem, the basic probabilistic model is very simple: $P(0)=p$ and $P(1)=1-p$, where $0 \leq p \leq 1$. All the existent $0-1$ EDAs are based on the basic model. During the last decade, large amounts of different versions of $0-1$ EDAs were developed, which can be classified into three categories [1]: without interaction, pairwise interaction and multi-interaction. PBIL, UMDA and cGA are estimation of distribu-

[^0]
[^0]:    * The work is funded by National Key Project for Basic Research of China (G2002cb312205).

tion algorithms which do not take the interaction among variables into account; BMDA and MIMIC use probabilistic model that can represent the relationship between two variables; BOA and FDA can describe the distribution of solutions by Bayesian Network, which can model complex interaction among variables [1-3]. The amazing success in discrete domain attracts people to design efficient EDAs for continuous problems.

However, choosing probabilistic model for continuous domain is still a challenging problem, even though several attempts have been made to extend the research results from discrete to continuous problems. The complexity of continuous fitness landscape makes it impossible to choose an almighty probabilistic model that fits any problem. In general, continuous EDAs can be classified into two approaches - indirect and direct. The former employs transform methods such as discretization [4] and the latter estimates the parameters of the predefined distribution [3,6-9]. It should be noted that the "direct" approach occupies a predominant position because the "indirect" approach fails to scale with problem size and solution precision [12]. According to the probabilistic model employed in "direct" approach, continuous EDAs can be further classified into two categories: Gaus-sian-based EDAs[1,3,6-9] and Histogram-based EDAs [5]. Most of the work concentrates on Gaussian probabilistic model. These include $\mathrm{PBIL}_{\mathrm{C}}, \mathrm{UMDA}_{\mathrm{C}}$, EMNA, EGNA, IDEA and so on [1,3]. Histogram-based EDAs mainly refer to the work by Tsutsui, S. et al.[5], in which marginal histogram model was used to model the population in continuous domain for the first time.

The purpose of the paper is to further study the continuous EDAs based on histogram model. A novel estimation of distribution algorithm (HEDA) based on histogram model is developed. Accumulation strategy is used to update the probabilistic model. In sampling phase, mutation strategy is designed to enhance the population diversity. Experimental analyses will show the performance of HEDA compared with FWH, SGA, UMDA-Gaussian[7] and CMA-ES[11].

The present paper is organized as follows. Next section will give the detailed description of HEDA. In Section 3, numerical experiments of HEDA, FWH, CMA-ES, UMDA-Gaussian and SGA are described. The paper is concluded in Section 4.

# 2 HEDA - Histogram-Based Estimation of Distribution Algorithm 

### 2.1 The General Description of HEDA

(1) Set the generation counter $t:=1$
(2) Divide the searching space of each variable into a certain number of bins. These bins should be of the same width and do not overlap with each other.
(3) Initialize the histogram model in which the height of each bin is same. The histogram generated should be normalized.
(4) Generate population $P(t)$ using sampling method described in subsection 2.3.
(5) Evaluate and rank the population $P(t)$. Save the elitist.
(6) Update the histogram model using accumulation learning strategy.

(7) Update the generation counter $t:=t+1$.
(8) If the termination conditions have not been satisfied, go to step 4.
(9) HEDA is finished and solutions are obtained in $P(t)$.

# 2.2 Learning Method in HEDA 

Accumulation learning strategy is proposed to update the histogram model. The histogram model is updated according to two kinds of information: historical and current information. In each generation, for each variable $i$, the selected individuals will be used to construct a histogram model $H_{c}^{i}$. The old histogram for variable $i$ is denoted as $H_{H}^{i}$. The height of a certain bin $j$ of the renewed histogram for variable $i$ is:

$$
H^{i}(j)=\alpha H_{H}^{i}(j)+(1-\alpha) \cdot H_{C}^{i}(j)
$$

where $H_{H}^{i}(j)$ is the height of bin $j$ in the old model, $\alpha(0 \leq \alpha \leq 1)$ is the accumulation factor which determines the effect of the old model on the new model, $H_{c}^{i}(j)$ is the height of the bin $j$ in model $H_{c}^{i}(j)$, and $\sum_{j} H_{c}^{i}(j)=1$. It is clear that new histogram $H^{i}$ has been normalized. Accumulation strategy used in HEDA is a method to reserve the information of historical model. In comparison with FWH [5] which reserves some good individuals in each generation, HEDA emphasizes the importance of the model building. The reservation of the historical model also reserves the information of the good individuals in the past generations. If $\alpha=0$, HEDA is reduced to the FWH [5].

In addition, the contribution of different individuals with different fitness values is considered in the learning process. The histogram model is learned according to relative ranking among different individuals. The height of each bin is modified according to the ranking and the position of each individual. Different rankings of the individuals lead to different increments of the bins. In the paper, the relationship is linear. If $N$ best individuals of the population are selected, the $k$-th best individual $(k \leq N)$ will make an increment of the corresponding bin which it belongs to by:

$$
\Delta h_{k}^{i}=(N-k+1) / \sum_{i=1}^{N} l=\frac{2(N-k+1)}{N(N+1)}
$$

So,

$$
H_{c}^{i}(j)=\sum_{k=1}^{N} \Delta h_{k}^{i} \cdot \delta_{j k}^{i}
$$

where $\delta_{j k}^{i}=1$ for $\left\{\delta_{j k}^{i} \mid k \in\{1,2, \ldots, N\} \wedge \min _{j}^{i} \leq v_{k}^{i}<\max _{j}^{i}\right\}$, and $\delta_{j k}^{i}=0$ otherwise. $v_{k}^{i}$ denotes the value of variable $i$ of the $k$-th best individual, $\min _{j}^{i}$ and $\max _{j}^{i}$ denote the lower and upper bound of bin $j$ of variable $i$. The better individuals will have more effect on the new model. Updating $H_{c}^{i}$ based on the ranking information helps improve the convergence property of HEDA.

# 2.3 Sampling Method in HEDA 

In HEDA, the population is sampled according to the model as follows: First, the bin $j$ is selected according to the probability of $H^{\prime}(j)$; then an individual is generated in the searching space of the bin $j$ with uniform distribution.

In order to enhance the diversity of population, mutation strategy is used. In HEDA, the mutation strategy means that each variable of an individual has a probability to be generated randomly. Here "randomly" means that the variable of an individual is generated with uniform distribution in the whole searching space. If the mutation rate is set $p_{m}$, that means there is a possibility of $p_{m}$ for each variable of each individual to be generated randomly and a possibility of $1-p_{m}$ for it to be generated according to the histogram model.

## 3 Numerical Experiments

### 3.1 Experimental Settings

Several well-known continuous test functions, which include the 20 -variable twopeak function, the 20 -variable Rastrigin function, the 10 -variable Griewank function and the 5 -variable Schfewel function, are used to verify the performance of HEDA. Table 1 lists these experimental functions and their respective optimal solutions.

Table 1. Test functions

In the experiments, the proposed HEDA has been compared with several wellknown continuous evolutionary algorithms including FWH, UMDA-Gaussian, SGA and CMA-ES. FWH is the original proposed continuous EDA based on histogram probability model [5]. The objective of comparison with FWH is to show that HEDA is a superior optimization method based on histogram model. UMDA-Gaussian is an EDA based on Gaussian probability model [7]; SGA refers to simple genetic algorithm; CMA-ES is an advanced evolution strategy with covariance matrix adaptation [11]. The objective of the comparison with UMDA-Gaussian, SGA and CMA-ES is to show that, among many kinds of continuous evolutionary algorithms, HEDA hold an outstanding position in solving the above test functions.

To evaluate the performance of HEDA, two criteria are used: convergence property and scalability. The convergence property is to measure the ability of the algorithm to reach the global optimum. In our experiments, we evaluate the convergence property by measuring the number of runs in which algorithm succeeds in finding the global optimum and the mean number of function evaluations (MNE) to find the global optimum in those successful runs. We define the successful detection of the solution as being within $\pm \varepsilon$ of the actual optimum point $(\varepsilon=0.1)$. The scalability of HEDA in solving two-peak problem is used to see how the behavior of algorithms changes when the dimension of the problem increases.

All the algorithms run 20 independent times on each problem. The termination condition for the 5 algorithms is detection of optimal solution or maximum 100,000 function evaluations. In all the algorithms, the initial population is generated uniformly. The parameter settings HEDA, FWH, SGA, UMDA-Gaussian and CMA-ES are as follows.

HEDA: the width of bin is set 0.1 , mutation rate is set 0.05 , and accumulation rate $0.2 .50 \%$ of population is selected for model updating. Elitist strategy is used.

FWH: we directly use the results obtained by FWH published in [5].
SGA: crossover probability 0.8 and mutation probability 0.05 . Selection method is tournament selection. Elitist strategy is used.

UMDA-Gaussian: the Gaussian probability model is updated using method introduced in [9]. 50\% of parent population is selected for model updating. Elitist strategy is used.

CMA-ES: $\mu=\lambda / 4$, where is $\lambda$ is the size of parent population and $\mu$ is the number of descendants. The Matlab code of CMA-ES in [13] is used in the experiments.

# 3.2 Convergence Property 

Table 2 illustrates the convergence property of HEDA, UMDA-Gaussian, FWH, SGA, and CMA-ES in solving the above test functions.

Firstly, we compare the performance of HEDA and FWH, both of which have the common feature: estimation of distribution algorithms based on marginal histogram probability model. The results of FWH have been published in [1]. From table 2, it is obvious that HEDA performs much better than FWH. For example, in solving Griewank function, with population size 100, HEDA can always obtain the optimal solution in the 20 runs, while FWH fails in all the 20 runs. Excellent behavior in solving the 4 problems shows the effectiveness of accumulation learning strategy and mutation strategy in HEDA.

And then, let's see the comparison with SGA, UMDA-Gaussian and CMA-ES. As shown in Table 2, for Schwefel functions, CMA-ES exhibits very good performance. For example, with population size 100, CMA-ES can obtain optimal solution in all the 20 runs with less MNE 1205.6. UMDA-Gaussian performs very well in solving Griewank function and it can always succeed in converging to optimum in all the 20 runs. However, UMDA-Gaussian and CMA-ES performs worse than HEDA in solving other test functions. It can be observed that the convergence property of HEDA

![img-0.jpeg](img-0.jpeg)

is consistently good in solving all the 4 functions. CMA-ES often fails in solving Two-peak function and Rastrigin function; UMDA-Gaussian often fails in solving Two-peak function, Schwefel function and Rastrigin function. Compared with SGA, HEDA performs much better both in MNE and \#OPT. Experimental results show that HEDA is a stable, robust and efficient algorithm in solving the test functions.

# 3.3 Scalability of HEDA 

The scalability of HEDA is tested on Two-peak function. The problem dimension starts at 10 , increased to 100 with step 10 . For each dimension, 20 independent runs are executed. Fig. 1 shows the mean number of fitness evaluations until HEDA finds the optimal solution. The number of fitness evaluations can be approximated by $O\left(n^{1.256}\right)$. Therefore, the results indicate that HEDA can solve Two-peak function in sub-quadratic number of evaluations.
![img-1.jpeg](img-1.jpeg)

Fig. 1. Scalability of HEDA for Two-peak problem

### 3.4 Drawback of HEDA

In the previous subsections, experiments demonstrate that HEDA can efficiently solve the test functions and performs much better than some of well-known continuous evolutionary algorithms. However, in the procedure of HEDA, the relationship among variables is not taken into consideration. This will limit the ability of HEDA in solving complicated problems with strong linkage information. Here, 20-variable Rosenbrock function with optimum $[1,1, \ldots, 1]$ is used to test the limited performance of HEDA:

$$
f(x)=\sum_{i=2}^{n} 100\left(x_{i}-x_{i-1}^{2}\right)^{2}+\left(1-x_{i-1}\right)^{2}
$$

There are strongly correlated variables in Rosenbrock function. In the experiment, 10 runs are executed for each population setting. The experimental results in Table 3 demonstrate it is hard to find optimal solution using HEDA. The drawback of HEDA is due to the fact that HEDA does not encode the linkage information.

Table 3. Convergence property of HEDA in solving Rosenbrock function

# 4 Conclusion 

In this paper, we have proposed an improved estimation of distribution algorithm (HEDA) based on histogram probabilistic model. In the algorithm, a novel learning strategy named accumulation strategy is proposed, which considers the historical and current information of population at the same time. Mutation strategy is brought into the sampling phase to enhance the population diversity. HEDA is tested to solve a class of well-known continuous problems. Experimental results demonstrate that HEDA significantly outperforms FWH, and exhibits excellent capability compared to other evolutionary algorithms, e.g. CMA-ES, SGA and UMDA-Gaussian.

It is also noted that the capability of HEDA is limited by the fact that HEDA does not take the relationship among variables into account. Future work will focus on extensions of HEDA that can model the relationship among variables.
