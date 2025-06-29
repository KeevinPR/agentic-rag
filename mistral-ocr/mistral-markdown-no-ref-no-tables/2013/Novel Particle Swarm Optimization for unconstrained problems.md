# Novel Particle Swarm Optimization for Unconstrained Problems 

Peifeng $\mathrm{Wu}^{1}$, Jianhua Zhang ${ }^{1}$<br>1. School of Electrical and Electronic Engineering, North China Electric Power University, Beijing 102206<br>E-mail: wuzheng820807@yahoo.cn


#### Abstract

Estimation of Distribution Algorithm (EDA) is a class of evolutionary algorithms which construct the probabilistic model of the search space and generate new solutions according to the probabilistic model. Particle Swarm Optimization (PSO) is an algorithm that simulates the behavior of birds flocks and has good local search ability. This paper proposes a combination (EDAPSO) of EDA with PSO for the global optimization problems. The EDAPSO proposed in this paper combines the exploration of EDA with the exploitation of PSO. EDAPSO can perform a global search over the entire search space with faster convergence speed. EDAPSO has two main steps. First, the algorithm generates new solutions according to the probabilistic model. Then, EDAPSO updates the whole population according to improved velocity updating equation. EDAPSO has been evaluated on a series of benchmark functions. The results of experiments show that EDAPSO can produce a significant improvement in terms of convergence speed, solution accuracy and reliability.


Key Words: Exploration, Exploitation, Convergence speed

## 1 INTRODUCTION

Particle swarm optimization (PSO) has been proposed by Kennedy and Eberhart in [1]. PSO simulates the population behavior of birds and is easy to implement. The algorithm has better robustness than many algorithms such as GA, is less sensitive to the nature of the problems and can be used for function optimization [2], control system [3], parameters optimization [4] and neural network[5]. However, similar to other population-based evolutionary algorithms, basic PSO may get trapped in local optima when solving complex multimodal problems Therefore, avoiding local optima and accelerating convergence speed of algorithm have become the two most important goals in the research of PSO. Many versions of improved PSO have been proposed to achieve the above two goals. In [6], an intelligent move mechanism was introduced to solve high-dimensional problems. Shi and Eberhart introduced a linearly decreasing weight to balance global and local search abilities[7]. Liuetal. proposed the center particle swarm optimization (Center PSO) to improve the performance of LDWPSO [8].Higashi and Iba introduced Gaussian mutation operator to increase the diversity of the population[9].
In this paper, we propose a novel version of PSO (EDAPSO). To avoid premature convergence of PSO and to accelerate the convergence speed, we combine the exploration of EDA with the exploitation of PSO. In EDAPSO, new solutions are sampled from a probability model and then the whole population updates according to the improved PSO with a novel velocity updating equation. This paper provides a comprehensive set of experimental verifications of our proposed algorithm.

## 2 PARTICLE SWARM OPTIMIZATION ALGORITHM

PSO is a population based optimization algorithm. The algorithm is initialized with a population of random particles in search space and searches for optima by updating direction vectors and velocity vectors. In n-dimensional search space, the direction vector of the i-th particle can be represented by vector $X_{i}=\left(x_{i 1}, x_{i 2}, \cdots x_{i n}\right)$ and the velocity vector of the i-th particle can be represented by another vector $V_{i}=\left(v_{i 1}, v_{i 2}, \cdots v_{i n}\right)$. At each generation, the particles update their velocities and directions according to the following two equations:

$$
\begin{gathered}
v_{i d}^{(t+1)}=\omega v_{i d}^{(t)}+c_{1} r_{1}\left(p_{i d}^{(t)}-s_{i d}^{(t)}\right)+c_{2} r_{2}\left(p_{g d}^{(t)}-s_{i d}^{(t)}\right) \\
x_{i d}^{(t+1)}=x_{i d}^{(t)}+v_{i d}^{(t+1)}
\end{gathered}
$$

where $\omega$ is called inertia weight. This factor has the function of balancing exploration and exploitation. If the factor is increased, the exploration of the algorithm will be enhanced. The exploitation will be enhanced with the decreasing of the factor. $r_{1}$ and $r_{2}$ are independently uniformly distributed random number with range $(0,1)$. $c_{1}$ and $c_{2}$ are positive constant parameters called learning factors. $p_{i d}^{(t)}$ is the best solution obtained by the i-th particle and $p_{g d}^{(t)}$ is the best solution obtained by the whole population.

## 3 EDAPSO

There are two main steps in most population-based optimization algorithms. They are generating population and updating population. Basic PSO generates uniformly

distributed random population and updates population according to velocity updating equation and direction updating equation.
However, PSO doesn't have mechanism to obtain the global information about the whole search space. This case may make the algorithm get trapped in local optima. After researching EDA[10], [11], we incorporate the idea of EDA into PSO to generate solutions which are more promising than those solutions generated by the PSO, and consequently, to explore the search space more effectively. EDAPSO updates the population with an improved velocity updating equation which can accelerate convergence speed. The procedure of EDAPSO is given as follows:
Step1:Generate M uniformly distributed random solutions to form initial population pop(0)
Step2:Select e promising solutions from the current population to form elite set $\mathrm{E}(\mathrm{k})$ and build probabilistic model P(k) according to Eqs. (3)-(4)

$$
\begin{gathered}
p(x)=\prod_{i=1}^{e} N\left(x_{i} ; \mu_{i}^{k}, \sigma_{i}^{k}\right) \\
N\left(x_{i} ; \mu_{i}^{k}, \sigma_{i}^{k}\right)=\frac{1}{\sqrt{2 \pi} \sigma_{i}} e^{\frac{1}{2}\left(\frac{x_{i}-\mu_{i}}{\sigma_{i}}\right)^{2}}
\end{gathered}
$$

In Eq.(3), we use n univariate and independent normal distributions as the joint probability distribution. The mean $\hat{\mu}_{i}^{k}$ and the standard deviation $\hat{\sigma}_{i}^{k}$ of the i-th variable at k -th generation are the two parameters need to be estimated.
The two parameters can be estimated as follows:

$$
\begin{gathered}
\hat{\mu}_{i}^{k}=\frac{1}{e} \sum_{k=1}^{e} x_{i k} \\
\hat{\sigma}_{i}^{k}=\frac{1}{e} \sum_{k=1}^{e}\left(x_{i k}-\hat{\mu}_{i}\right)^{2}
\end{gathered}
$$

Where e is the size of $\mathrm{E}(\mathrm{k})$.
Step3:Save the better half of the solutions in pop(k) and the other half of the solutions are sampled according to the constructed probabilistic model $\mathrm{P}(\mathrm{k})$.
Step4:Use PSO with improved updating equation to update $\operatorname{pop}(\mathrm{k})$. The velocity updating equation is as follow:

$$
v_{i d}^{(t+1)}=\omega v_{i d}^{(t)}+2 \omega_{1} \times\left(p_{g d}-x_{i d}^{(t)}\right)
$$

Step5:If the given stopping criterion is not met, $\mathrm{k}=\mathrm{k}+1$, goto step 2 .

## 4 EXPERIMENTAL RESULTS AND ANALYSIS

### 4.1 Benchmark Functions for Comparison

In order to verify the performance of EDAPSO, we compare the performance of EDAPSO with basic PSO, LDWPSO and CFPSO. The four algorithms are applied to settle a comprehensive set of benchmark functions which has 11 different optimization problems[2]. The functions are presented as follows:

The first is Rosenbrock function, defined as:

$$
f_{1}=\sum_{i=1}^{N-1}\left(100\left(x_{i+1}-x_{i}^{2}\right)^{2}+\left(x_{i}-1\right)^{2}\right)
$$

With $-100 \leq x_{i} \leq 100$, the best solution of $f_{1}$ is $x^{*}=(1,1, \ldots, 1)$ and $f\left(x^{*}\right)=0$.

$$
f_{2}=\frac{1}{4000} \sum_{i=1}^{N} x_{i}^{2}-\prod_{i=1}^{N} \cos \left(\frac{x_{i}}{\sqrt{i}}\right)+1
$$

With $-100 \leq x_{i} \leq 100$, the best solution of $-0.5 \leq x_{i} \leq 0.5$ is $x^{*}=(0,0, \ldots, 0)$ and $f\left(x^{*}\right)=0$

$$
f_{3}=\sum_{i=1}^{N}\left(\sum_{j=1}^{N} x_{j}\right)^{2}
$$

With $-100 \leq x_{i} \leq 100$, the best solution of $f_{3}$ is $x^{*}=(0,0, \ldots, 0)$ and $f\left(x^{*}\right)=0$

$$
f_{4}=\sum_{i=1}^{N} x_{i}^{2}+\left(\sum_{i=1}^{N} 0.5 i x_{i}\right)^{2}+\left(\sum_{i=1}^{N} 0.5 i x_{i}\right)^{4}
$$

With $-100 \leq x_{i} \leq 100$, the best solution of $f_{4}$ is $x^{*}=(0,0, \ldots, 0)$ and $f\left(x^{*}\right)=0$

$$
f_{5}=\sum_{i=1}^{N}\left|x_{i}\right|+\prod_{i=1}^{N}\left|x_{i}\right|
$$

With $-100 \leq x_{i} \leq 100$, the best solution of $f_{5}$ is $x^{*}=(0,0, \ldots, 0)$ and $f\left(x^{*}\right)=0$

$$
f_{6}=\sum_{i=1}^{N}\left(|x_{i}+0.5|\right)^{2}
$$

With $-100 \leq x_{i} \leq 100$, the best solution is $-0.5 \leq x_{i} \leq 0.5$ and best function value is 0 .

$$
f_{7}=\sum_{i=1}^{N}\left|x_{i} \sin \left(x_{i}\right)+0.1 x_{i}\right|
$$

With $-100 \leq x_{i} \leq 100$, the best solution of $f_{7}$ is $x^{*}=(0,0, \ldots, 0)$ and $f\left(x^{*}\right)=0$

$$
f_{8}=\sum_{i=1}^{N} x_{i}^{2}
$$

With $-5.12 \leq x_{i} \leq 5.12$, the best solution of $f_{8}$ is $x^{*}=(0,0, \ldots, 0)$ and $f\left(x^{*}\right)=0$

$$
f_{9}=\sum_{i=1}^{N} i x_{i}^{2}
$$

With $-5.12 \leq x_{i} \leq 5.12$, the best solution of $f_{9}$ is $x^{*}=(0,0, \ldots, 0)$

$$
f_{10}=\sum_{i=1}^{N}\left(x_{i}^{2}-10 \cos \left(2 \pi x_{i}\right)+10\right)
$$

With $-100 \leq x_{i} \leq 100$, the best solution of $f_{10}$ is $x^{*}=(0,0, \ldots, 0)$ and $f\left(x^{*}\right)=0$

$$
f_{11}=\sum_{k=1}^{N}\left[\sum_{i=1}^{N}\left(t^{k}+0.5\right)\left(\frac{x_{i}}{i}\right)^{k}-1\right]^{2}
$$

With $-N \leq x_{i} \leq N$, the best solution of $f_{11}$ is $x^{*}=(1,2, \ldots, N)$ and $f\left(x^{*}\right)=0$

### 4.2 Comparison Strategies and Metrics:

We measure the number of function calls (NFCs) which is commonly used metric in literature [12-13] to compare the convergence speed. If the NFCs of an algorithms is smaller than other algorithms, this algorithm has higher convergence speed. The termination criterion is to find a value smaller than VTR(value to reach)before reaching the maximum number of function calls $\left(M A X_{N F C}\right)$.In order to compare the convergence speed with NFC more directly, we introduce the parameter acceleration rate(AR). AR is defined as follows:

$$
A R_{\substack{\text { algorithm A } \\ \text { algorithm B }}}=\frac{N F C_{\text {algorithm A }}}{N F C_{\text {algorithm B }}}
$$

Where $\mathrm{AR}>1$ means the convergence speed of algorithm b is faster than the speed of algorithm a.
In the experiments, we also use success rate(SR) to compare the performance of the algorithms. SR for each test function is defined as follows:

$$
S R=\frac{\text { number of times reached VTR }}{\text { total number of trials }}
$$

To present the convergence speed of different problems and the robustness of the algorithms, we introduce the average acceleration rate $A R_{\text {ave }}$ and the average success rate $S R_{\text {ave }}$ over n test functions. The two parameters are calculated as follows

$$
\begin{aligned}
& A R_{\text {ave }}=\frac{1}{n} \sum_{i=1}^{n} A R_{i} \\
& S R_{\text {ave }}=\frac{1}{n} \sum_{i=1}^{n} S R_{i}
\end{aligned}
$$

The parameter settings in the experiments are showed as follows:
population size: $\mathrm{M}=100$
Basic PSO: $c_{1}=c_{2}=2[1]$
LDWPSO: $\omega_{\min }=0.4, \omega_{\max }=0.9[7]$
$A R_{-} \frac{P S O}{L D W P S O}$ is 0.97 , which means the convergence speed of PSO is 106

Maximum NFCs $\left(M A X_{N F C}\right)=10^{6}$
Value to reach (VTR) $=10^{-6}$
To make the comparisons reliable and fair, for all the experiments: (1)the presented values are the average of for 30 independent runs.(2) in EDAPSO, the extra number of function calls which is required for the promising particles sampled according to the constructed probabilistic model are counted.

### 4.3 Comparison EDAPSO with basic PSO, LDWPSO and CFPSO

We compare EDAPSO with three classical PSO (basic PSO, LDWPSO and CFPSO). Table 1 shows the results of solving 11 functions. The results of the experiments show NFCs, SR for each function. The last row of the table shows the average success rates and the average acceleration rate over 11 functions. The functions in this section are low dimensional functions. The parameter e is set to be $0.3 \mathrm{M} / \mathrm{M}$ is the size of particles in population). Table. 1 is too long. Thus, we divide it into two parts. The average success rates of PSO, LDWPSO, CFPSO and EDAPSO are $0.6483,0.7,0.7363$ and 0.8696 , respectively. The four algorithms fail to solve $f_{10}$ (Rastrigin's function). Basic PSO,LDWPSO and CFPSO all fail to solve $f_{2}$. The comparison of average success rates reveals that EDAPSO has the best robustness among the four algorithms.
$A R_{-} \frac{P S O}{L D W P S O}$ is 0.97 , which means the convergence speed of PSO is $3 \%$ faster than the convergence speed of LDWPSO. $A R_{-} \frac{P S O}{C F P S O}$ is 1.04 , which means the convergence speed of CFPSO is $4 \%$ faster than the convergence speed of PSO. $A R \frac{P S O}{E D A P S O}$ is 9.25 , which means the convergence speed of EDAPSO is $825 \%$ faster than the convergence speed of PSO.
$A R_{\text {ave }} \frac{L D W P S O}{E D A P S O}=\frac{A R_{\text {ave }} \frac{P S O}{E D A P S O}}{A R_{\text {ave }} \frac{P S O}{L D W P S O}}=9.53$, which means the convergence speed of EDAPSO is $853 \%$ faster than the convergence speed of EDWPSO.
$A R_{\text {ave }} \frac{L D W P S O}{E D A P S O}=\frac{A R_{\text {ave }} \frac{P S O}{E D A P S O}}{A R_{\text {ave }} \frac{E D A P S O}{E D W P S O}}=8.89$, which means convergence speed of EDAPSO is $789 \%$ faster than the convergence speed of CFPSO. The comparisons of average acceleration rate indicate that EDAPSO has the fastest

Table1. Comparison of Four Algorithms for Low-dimensional Problems



convergence speed among the four algorithms. The comparison shows that EDAPSO has the best robustness and the fastest convergence among the four algorithms. The optimization ability is the best among the four algorithms on the whole.

## 5 CONCLUSION

In this paper, the search idea of EDA has been employed to collect global information. An improved velocity updating equation was used to accelerate the speed of the algorithm. Embedding these two improvements, we proposed EDAPSO.
PSO, LDWPSO, CFPSO and EDAPSO were compared in terms of robustness and convergence speed. The comparisons for SR (success rates) and AR (accelerate rates) show that EDAPSO has the fastest convergence speed and best robustness among the four algorithms.
Utilizing the idea of EDA to obtain more global information and improving the solution accuracy of the problems is a new method. Further studies are still required to investigate its advantages, disadvantages and
limitations. This paper can be viewed as a first step in this direction. Possible directions for future work include adaptive setting of e (size of elite set) or applying the idea of EDA to other popular algorithms.
