# CONTROLLING CHAOS BY AN IMPROVED ESTIMATION OF DISTRIBUTION ALGORITHM 

Xingli Huang ${ }^{1}$, Peifa Jia ${ }^{1}$, Bo Liu ${ }^{2}$<br>${ }^{1}$ Department of Computer Science \& Technology<br>Tsinghua University, 100084, Beijing, P. R. China<br>${ }^{2}$ Center for Forecasting Science, Academy of Mathematics and Systems Science<br>Chinese Academy of Sciences, 100190, Beijing, P. R. China<br>liub01@mails.tsinghua.edu.cn


#### Abstract

Control and synchronization of chaotic systems are important issues in nonlinear sciences. This paper proposes an effective estimation of distribution algorithm (EDA)-based memetic algorithm (MA) to direct the orbits of discrete chaotic dynamical systems as well as to synchronize chaotic systems, which could be formulated as complex multi-modal numerical optimization problems. In EDA-based MA (EDAMA), both EDA-based searching operators and simulated annealing (SA)-based local searching operators are designed to balance the exploration and exploitation abilities. On the other hand, global information provided by EDA is combined with local information from SA to create better solutions. In particular, to enrich the searching behaviors and to avoid premature convergence, SA-based local search is designed and incorporated into EDAMA. To balance the exploration and exploitation abilities, after the standard EDA-based searching operation, SA-based local search is probabilistically applied to some good solutions selected by using a roulette wheel mechanism with a specified probability. Numerical simulations based on Hénon Map demonstrate the effectiveness and efficiency of EDAMA, and the effects of some parameters are investigated as well.


Keywords- Estimation of Distribution Algorithm, Chaotic dynamics

## 1. INTRODUCTION

Since the pioneering work of Huber's on chaos control in 1989 [1] and work of Pecora and Carroll's on chaos synchronization [2] in 1990, control and synchronization of chaotic systems have been important issues in nonlinear science and attracting increased interests from various fields [3]. Nowadays, a wide variety of approaches have been proposed for control and synchronization of chaotic systems [4-8].

Recently, a new population-based evolutionary technique, estimation of distribution algorithm (EDA), has been proposed [9] as an alternative to genetic algorithm (GA) [10] and particle swarm optimization (PSO) [11] for continuous or discrete optimization problems. In EDA, a population of solutions is initialized randomly, which is evolved to find optimal solutions through selection, modeling, sampling, and replacement operation procedures. Compared with GA and PSO, EDA has some attractive characteristics. It samples new solutions from a probability model which approximates the distribution of promising solutions, and avoids premature

convergence and selection pressure exhibited by GA's crossover and mutation operation. Additionally, the priori information about the problem structure can be captured by the probability model estimated during the search, which facilitating a more efficient global search. This paper proposes an effective estimation of distribution algorithm (EDA) based memetic algorithm (MA) to direct the orbits of chaotic dynamical systems as well as to synchronize chaotic systems, which could be formulated as multimodal numerical optimization problems. Simulations based on Hénon Map demonstrate the effectiveness and efficiency of EDAMA, and the effects of some parameters are investigated as well.

# 2. PROBLEM FORMULATION 

Consider the following discrete chaotic dynamical system:

$$
\mathbf{x}(k+1)=\mathbf{f}(\mathbf{x}(k)), \quad k=1,2, \ldots, N
$$

where state $\mathbf{x}(k) \in R^{\times}$, and $\mathbf{f}: R^{\times} \rightarrow R^{\times}$is continuously differentiable.
Let $\mathbf{x}_{0} \in R^{\times}$be an initial state of the system. If small perturbation $\mathbf{u}(k) \in R^{\times}$is added to the chaotic system, then

$$
\mathbf{x}(k+1)=\mathbf{f}(\mathbf{x}(k))+\mathbf{u}(k), k=0,1, \cdots, N-1
$$

where $\|\mathbf{u}(k)\| \leq \mu$, and $\mu$ is a positive real constant.
The goal is to determine suitable $\mathbf{u}(k)$ so as to make $\mathbf{x}(N)$ in the $\varepsilon$-neighborhood of the target $\mathbf{x}_{i}$, i.e., $\left\|\mathbf{x}(N)-\mathbf{x}_{i}\right\|<\varepsilon$, where a local controller is effective for chaos control. Without loss of generality, assume that $\mathbf{u}(k)$ acts only on the first component of $\mathbf{f}$, then the problem can be re-formulated as follows.
(P1):
$\min \left\|\mathbf{x}(N)-\mathbf{x}_{i}\right\|$ by choosing suitable $u(k), k=0,1, \ldots, N-1$

$$
\text { s.t. } \quad\left\{\begin{array}{l}
x_{1}(k+1)=f_{1}(\mathbf{x}(k))+u(k) \\
x_{i}(k+1)=f_{i}(\mathbf{x}(k)), i=2, \cdots, n
\end{array}, \quad \mid u(k) \mid \leq \mu, \quad \mathbf{x}(0)=\mathbf{x}_{0}\right.
$$

Let $\mathbf{x}(k+1)=\mathbf{f}(\mathbf{x}(k))$ and $\mathbf{y}(k+1)=\mathbf{f}(\mathbf{y}(k))$ be two given chaotic dynamical systems with the same structure but different initial state. Chaotic synchronization by feedback is to select the feedback matrix $\mathbf{K}(k) \in R^{\times \times x}$ such that $\|\mathbf{x}(N)-\mathbf{y}(N)\| \rightarrow 0$, where $\mathbf{x}(0)=\mathbf{x}_{0} \neq \mathbf{y}(0)=\mathbf{y}_{0}$ and

$$
\left\{\begin{array}{l}
\mathbf{x}(k+1)=\mathbf{f}(\mathbf{x}(k)) \\
\mathbf{y}(k+1))=\mathbf{f}(\mathbf{y}(k))+\mathbf{K}(k) \cdot(\mathbf{y}(k)-\mathbf{x}(k))
\end{array}\right.
$$

It was regarded that chaos synchronization also can be formulated as the above problem [4]. Similarly, assume that feedback only acts on the first component, i.e., $K_{11}(k) \neq 0$ and all other components of $\mathbf{K}(k)$ are zeros. For convenience, denote $K_{11}(k)=K(k)$. Then the problem can be formulated as follows.
(P2):
$\min \left\|\mathbf{x}(N)-\mathbf{y}(N)\right\|$ by choosing suitable $K(k), k=0,1, \cdots, N-1$
s.t. $\left\{\begin{array}{l}\mathbf{x}(k+1)=\mathbf{f}(\mathbf{x}(k)) \\ y_{1}(k+1)=f_{1}(\mathbf{y}(k))+K(k) \cdot\left(y_{1}(k)-x_{1}(k)\right), \quad|K(k)| \leq \kappa, \quad \mathbf{x}(0)=\mathbf{x}_{0} \neq \mathbf{y}(0)=\mathbf{y}_{0} \\ y_{i}(k+1)=f_{i}(\mathbf{y}(k)), i=2, \cdots, n\end{array}\right.$

However, (P2) does not totally equivalent to the origin problem, because

$\mathbf{x}(N) \neq \mathbf{y}(N)$ will cause the two systems apart from each other eventually due to the sensitivity to initial state of chaotic systems, even though $\|\mathbf{x}(N)-\mathbf{y}(N)\|$ is arbitrarily small. So we should deal with (P2) on-line at some step $k^{\prime}$ with $\mathbf{x}_{0}=\mathbf{x}\left(k^{\prime}\right), \mathbf{y}_{0}=\mathbf{y}\left(k^{\prime}\right)$, when $\left\|\mathbf{x}\left(k^{\prime}\right)-\mathbf{y}\left(k^{\prime}\right)\right\|$ is larger than a threshold $\delta$. For the above problems, it needs to determine suitable $u(k)$ or $K(k)$ to minimize objective function value. Thus, from the viewpoint of optimization, (P1) and (P2) are both multi-dimensional constrained numerical optimization problems.

# 3. EDAMA 

### 3.1. Estimation of distribution algorithm (EDA)

In EDA, the $i$-th individual in the $d$-dimensional search space at generation $t$ can be represented as $X_{i}(t)=\left\{x_{i, 1}^{t}, x_{i, 2}^{t}, \ldots, x_{i, d}^{t}\right\},(i=1,2, \ldots, N P$, where $N P$ denotes the size of the population). The procedure of EDA is summarized as follows.

Step 1: Randomly initialize the population of individual for EDA, where each individual contains $d$ variables (i.e., $d=N$ ). Repair individuals if required.

Step 2: Evaluate the objective values of all individuals, and recode the best individual $X_{\text {best }}$ together with its objective value.

Step 3: Select $M$ individuals from population based on the selection strategy.
Remark: In this case, truncation selection strategy is employed by which individuals are sorted according to their objective values and the best $M(M=N P / 2)$ individuals are selected.

Step 4: Build a probabilistic model based on the statistical information of the selected individuals in Step 3 using a learning method.

Remark: Gaussian model with diagonal covariance matrix (GM/DCM) [9] is used, in which the $d$-dimensional joint probability distribution is factorized as a product of $d$ univariate and independent normal distributions:

$$
p_{i}(x)=\prod_{j=1}^{d} N\left(x_{j} ; \mu_{j}^{t}, \sigma_{j}^{t}\right), \quad N\left(x_{j} ; \mu_{j}^{t}, \sigma_{j}^{t}\right)=\frac{1}{\sqrt{2 \pi \sigma_{j}^{t}}} e^{\frac{\left(\frac{1}{2} x_{j}-\mu_{j}^{t}\right)^{2}}{\sigma_{j}^{t}}}
$$

In Eq. (6), the mean $\mu_{j}^{t}$ and standard deviation $\sigma_{j}^{t}$ of the $j$-dimension variable for the $t$-th generation can be estimated respectively as follows:

$$
\tilde{\mu}_{j}^{t}=\frac{1}{M} \sum_{i=1}^{M} x_{i, j}^{t}, \quad \tilde{\sigma}_{j}^{t}=\sqrt{\frac{1}{M} \sum_{i=1}^{M}\left(x_{i, j}^{t}-\tilde{\mu}_{j}^{t}\right)^{2}}
$$

Step 5: Sample $N P$ new offspring individuals from the model built in Step 4. Repair individuals if required.

Step 6: Evaluate the objective values of the offspring individuals.
Step 7: Update population using replacement strategy.
Remark: As for the replacement strategy, steady-state replace is used, by which the pool of the parents and offspring are ranked based on their objective values, and top individuals are selected for next generation.

Step 8: Determine the best individual of the current new population with the best objective value. If the objective value is better than the objective value of $X_{\text {best }}$, then update $X_{\text {best }}$ and its objective value with the value and objective value of the current

best individual.
Step 9: If a stopping criterion is met, then output $X_{\text {best }}$ and its objective value; otherwise go back to Step (3).

As for the problems to direct chaotic orbit and to synchronize chaotic systems, the searching solutions are $(u(0), u(1), \cdots, u(N-1))^{T}$ and $(K(0), K(1), \cdots, K(N-1))^{T}$ respectively. Obviously, multiple variables need to be determined if $N$ is large. Besides, in Steps 1 and 5, if newly generated $u$ or $K$ is exceeded its bound (i.e. $\pm \mu$ or $\pm \kappa$ ), it will be set as its nearest bound value based on the repairing strategy.

# 3.2. EDAMA 

Starting from an initial state, simulated annealing (SA) randomly generates a new state in the neighborhood of the original one, which causes a change of $\Delta E$ in the objective function value. For minimization problems, the new state is accepted with probability $\min \{1, \exp (-\Delta E / T)\}$, where $T$ is a control parameter. SA provides a mechanism to probabilistically escape from local optima and the search process can be controlled by the cooling schedule [12].

In EDAMA, SA-based local search is inserted after Step 7 in EDA to enrich the local searching behaviors and to avoid premature convergence. Based on its performances, each solution is assigned a probability to be selected by the rank-based fitness assignment technique [10]. Then, the roulette wheel mechanism [10] is used to decide which solutions will be selected. Subsequently, the selected solutions will perform the SA-based local search with a predefined probability $p_{t s}$. Due to the mechanism of roulette wheel rule, good solution will gain more chance for exploitation. Besides, it is easy to control such an exploitation process by adjusting the value of $p_{t s}$. Moreover, for the parameter settings of SA, proper initial temperature should be high enough so that all states of the system have an equal probability of being visited and at the same time it should not be rather high so that a lot of unnecessary searches in high temperature will be avoided. In EDAMA, an initial temperature is set as $t_{0}=-\left(c_{t s}-c_{b}\right) / \ln p_{t}$, where $c_{t s}$ and $c_{b}$ denote the worst and best objective values in the initial population, respectively; $p_{t}$ denotes the acceptance probability of the worst solution compared with the best one. Exponential cooling schedule, $t_{k}=\lambda t_{k-1}, 0<\lambda<1$, is applied, which is believed to be an excellent cooling recipe, since it provides a rather good compromise between a computationally fast schedule and the ability to reach low-energy state.

## 4. SIMULATION

### 4.1. Simulation on directing chaotic orbits

As a typical discrete chaotic system, Hénon Map is described as follows.

$$
\left\{\begin{array}{l}
x_{1}(k+1)=-p x_{1}^{2}(k)+x_{2}(k)+1 \\
x_{2}(k+1)=q x_{1}(k)
\end{array}\right.
$$

where $p=1.4$, and $q=0.3$.
Consider (P1) first, the target $\mathbf{x}_{1}$ is set to be a fixed point $(0.63135,0.18941)^{T}$.

Let $\mathbf{x}_{0}=(0,0)^{T}$, and $u(k)$ is only added to $x_{1}$ with the bound $\mu=0.01$. To test the performance of EDAMA, EDAMA is compared with standard EDA and SA. In EDAMA, the population size is 100 , the maximum generation is $200, p_{0}=0.1$, $p_{e}=0.05$, and cooling rate $\lambda=0.9$. In EDA, the population size is 100 , and the maximum generation is 200 . In SA, $p_{e}=0.05, \lambda=0.9$, the step of Metropolis sampling process under each temperature is set to 1000 , and the maximum generation is set to 20 . Under different values of $N$, Table 1 lists the mean objective value and the best objective value of 100 independent runs for each of the above three algorithms. From Table 1, it can be seen that EDAMA is superior to EDA and SA in term of searching quality and derivation of the results. It could be concluded that EDAMA is more effective and more robust on initial conditions.

Table 1 Statistics performance of EDAMA, EDA and SA under different $N$
# 4.2. Simulation on synchronization of chaotic systems 

Next, we consider chaos synchronization problem based on EDAMA. The driven system is Eq. (8) with $\mathbf{x}(0)=(0.2,0.3)^{T}$, and the response system is as follows.

$$
\left\{\begin{array}{l}
y_{1}(k+1)=-p y_{1}^{2}(k)+y_{2}+1+K(k) \cdot\left(y_{1}(k)-x_{1}(k)\right) \\
y_{2}(k+1)=q y_{1}(k)
\end{array}\right.
$$

where $\mathbf{y}(0)=(0.8,0.5)^{T}$.
Chaos synchronization can be formulated as (P2). We set $N=5, \kappa=1$ and $\delta=0.03$. One of the typical results is showed in Fig. 1. Fig. 1 (a) is the error of the first component between two systems by dealing with (P2) online; (b) is the corresponding value of $K$; (c) illustrates the bias of $x_{1}-y_{1}$ without dealing with (P2) online. It can be seen from Fig. 1 (a) that the response system synchronizes the driven system very well, but without dealing with (P2) online the two systems get apart from each other only

after a few steps as shown in Fig. 1 (c). In a word, it is concluded that EDAMA can effectively and efficiently solve the problem synchronizing chaotic dynamical systems.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Chaos synchronization

## 5. CONCLUSION

To our knowledge, this is the first report of hybridizing estimation of distribution algorithm and simulated annealing for chaos control and chaos synchronization. The proposed approach not only performs exploration by using the population-based evolutionary searching ability of EDA, but also performs exploitation by using the SA-based local searching behavior. Simulation results based on Hénon Map demonstrated the effectiveness and efficiency of EDAMA.
