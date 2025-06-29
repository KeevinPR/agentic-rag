# Blocked Stochastic Sampling versus Estimation of Distribution Algorithms 

Roberto Santana ${ }^{\ddagger}$ and Heinz Mühlenbein ${ }^{\dagger}$<br>$\dagger$ ICIMAF, Calle 15, e/ C y D, Vedado, CP-10400, La Habana, Cuba<br>${ }^{\ddagger}$ AiS.FHG -- Schloss Birlinghoven, D-53757 Sankt Augustin, Germany


#### Abstract

The Boltzmann distribution is a good candidate for a search distribution for optimization problems. In this paper we compare two methods to approximate the Boltzmann distribution - Estimation of Distribution Algorithm's (EDA) and Markov Chain Monte Carlo methods (MCMC). It turns out that in the space of binary functions even blocked MCMC methods outperform EDA on a small class of problems only. In these cases a temperature of $T=0$ performed best.


## I. Introduction

Let $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)$ denote a vector, $x_{i} \in\{0,1\}$. We use the following conventions. Capital letters $X_{i}$ denote variables, small letters $x_{i}$ assignments. For simplicity we only consider binary variables here. Let a function $f$ : $\{0,1\}^{n} \rightarrow \mathbb{R}_{>0}$ be given. We consider the optimization problem $\mathbf{x}_{\text {opt }}=\operatorname{argmax} f(\mathbf{x})$.

The Boltzmann distribution has been proposed as a search distribution for optimization problems a number of times. It is defined as follows:

$$
\pi_{B}(x)=\frac{1}{Z_{T}} e^{\frac{f(x)}{T}}
$$

where $Z_{T}$ is the usual partition function. In this paper we will mainly use the inverse temperature $\beta=\frac{1}{T}$ as a parameter of the search algorithms. If search points can be generated according to the Boltzmann distribution, then points of high fitness are generated more often than points of low fitness. The central problem is how to efficiently compute this distribution.

There has been a new proposal to use the Boltzmann distribution in population based search methods [9]. The Boltzmann Estimation Distribution Algorithm is defined in algorithm 1.

The convergence of this algorithm to the set of global optima can easily be shown. The problem is to compute efficiently the Boltzmann distribution [7], [9]. The most simple approximation UMDA uses only univariate marginal frequencies [6]. From this algorithm FDA, the

E-mail: $\dagger$ rsantana@cidet.icmf.inf.cu, $\ddagger$ muehlenbein@gmd.de

## Algorithm 1: BEDA

$t \quad t \Leftarrow 0$. Generate $N$ points according to the uniform distribution $p(\mathbf{x}, 0)=2^{-n}$.
2 With a given $\Delta \beta(t)>0$, let

$$
p^{s}(\mathbf{x}, t)=\frac{p(\mathbf{x}, t) e^{\Delta \beta(t) f(\mathbf{x})}}{\sum_{g} p(\mathbf{y}, t) e^{\Delta \beta(t) f(\mathbf{y})}} .
$$

3 Generate $N$ new points according to the distribution $p(\mathbf{x}, t+1)=p^{s}(\mathbf{x}, t)$.
$t \Leftarrow t+1$.
5 If stopping criterion not met go to STEP 2
factorized distribution algorithm and $L F D A$ are derived. $L F D A$ computes the factorization out of the sampled data. The interested reader is referred to [8]

In this paper we will investigate another techniques to approximate the Boltzmann distribution. These techniques are based on stochastic sampling.

## II. Stochastic sampling techniques

Stochastic sampling algorithms (also called stochastic simulation or Monte Carlo algorithms) are a family of algorithms used to approximate a distribution $\pi$ and to estimate expectations derived from $\pi$. These methods comprise different algorithms able to devise an ergodic Markov chain such that the steady-state distribution of the chain is $\pi$. To approximate the probability, the chain can be started at any point $x$, and after a sufficiently long time (say for $k$ steps) take each state of the chain as a sample of the desired probability $\pi$. Therefore these algorithms are called Markov chain Monte Carlo methods MCMC.

Most algorithms use a sufficient large $k$ in order to be sure that the chain has reached the equilibrium. We started our investigation with newly developed exact MCMC methods. A typical example is the coupling from the past algorithm from Propp and Wilson [11]. This algorithm uses a test to decide if the chain has reached equilibrium. To our great disappointment it turned out

that for optimization the approximate MCMC methods performed better. Thus we do not include these results here.

The performance of any MCMC method further depends on the temperature. If a small $T$ is used, it takes a very long time to reach equilibrium. If a large $T$ is used, the optima will be generated very seldomly. Simulated annealing [4] circumvents this problem, but at the expense of finding a suitable annealing schedule. Again, using some of the popular annealing schedules gave for our benchmark problems in almost all cases worse results than using a fixed temperature. This paper gives some explanation for this result.

The well known Gibbs sampler is described in [3]. It is also known as the heat bath algorithm for discrete problems. To draw samples from $\pi(x)$, start with an initial state $x^{0}=\left(x_{1}^{0}, \ldots, x_{n}^{0}\right)$. At each time $t$ of the Gibbs sampler, a location $i$ to be updated is randomly chosen from $x^{t}$ and the new value of the variable at this position is selected using the conditional probabilities of the chosen variables given the values assigned to the rest of variables. In this way the new vector $x^{t+1}$ is constructed.

The performance of updating a single variable at a time MCMC samplers deteriorate for problems with highly correlated components [5]. A remedy for this problem has been to "block" the variables into groups that are then updated simultaneously using a Gibbs or Metropolis Hasting step [2]. This technique is called "blocking" and when it is used with Gibbs Sampling the algorithm is usually called blocked Gibbs Sampling.

In this paper we present results in the use of the blocked Gibbs Sampling for the optimization of $f(x)$. In our implementation the block size is fixed along the simulation.

## Algorithm 2: Blocked Gibbs Sampler

1 Set $t \Leftarrow 0$. Generate randomly an initial point $x^{0}$ from the state space.
2 Select a set $N g$ of $s$ different uniformly selected variables of $X$.
3 While $t<k$ generate $x^{t+1}=\phi\left(x^{t}, U, W, N g\right)$.
4 While $t<N_{s}$ generate $x^{t+1}=\phi\left(x^{t}, U, W, N g\right)$ and add it to the sample set $A$.
5 Estimate $\pi$ using the sample set $A$.

In algorithm 2 we present our blocked Gibbs Sampler. The algorithm receives as a parameter the block size $s$, i.e. the maximum number of variables that can change their values together, $s$ also determines a neighborhood of the solution $x$ comprised by those vectors that have a Hamiltonian distance to $x$ equal or less than $s$. The
input of the algorithm is the time $(k)$ the Markov chain is run before sample points are taken and the maximum number of steps $N_{s} . \phi\left(x^{t}, U, W, N g\right)$ is the transition rule for the state $x^{t}$, where $N g$ is the set of variables to be updated and $U$ and $W$ are random variables, that are used to determine the new configuration of $N g$, and if the new point is accepted or not. The transition rule is shown in equation (2) where $T$ is the fixed temperature. The determination of the proposal comprises two steps. First, one determines the set of variables to be updated, and second, one selects the new values for this set of variables.

$$
x^{t+1}= \begin{cases}x_{j}^{t+1}=x_{j}^{t} & : \quad \text { for } j \notin N g \\ x_{N g}^{t+1}=x_{N g}^{t} & \text { if } W \leq \frac{\left.U_{g}\right)}{\epsilon^{\frac{U_{g}}{U_{g}}}+\epsilon^{\frac{U_{g}}{U_{g}}}} \\ x_{N g}^{t+1}=x_{N g}^{t} & \text { otherwise }\end{cases}
$$

Available information about the structure of the problem can be used at both steps. In the first step we can select with higher probability $s$ variables known to be related.

In our experiments we considered two versions of the blocked Gibbs Sampling. In the first, the set of variables $N_{g}$ is selected from the vector with uniform distribution. In another version the $s$ variables to be chosen will be related (they appear together in the definition set of an additive function) with a probability $p_{u}$. This implies to change only the second step of the algorithm shown in algorithm 2. The way in which transitions are done has been implemented as in [10], the probability of taking a new value $x_{N g}^{\prime}$ depends on the Hamiltonian weight of the final solution.

## III. Easy functions for population search

The following functions were used in our first group of experiments $\left(u=\sum x_{i}\right)$ :

$$
\begin{gathered}
f_{d e c}^{3}= \begin{cases}2 & \text { for } \quad u=0 \\
1 & \text { for } \quad u=1 \\
0 & \text { for } \quad u=2 \\
3 & \text { for } \quad u=3\end{cases} \\
f_{\text {3deceptive }}(X)=\sum_{i=1}^{i=\frac{n}{2}} f_{d e c}^{3}\left(X_{3 i-2}, X_{3 i-1}, X_{3 i}\right) \\
\operatorname{Jump}(n, g, x)= \begin{cases}u & u<n-g \\
2 *(n-g)-u & n-g \leq u \\
n & u=n\end{cases}
\end{gathered}
$$

The $f_{3 \text { deceptive }}$ function (4) is defined as a sum of more elementary deceptive functions $f_{d e c}^{3}$ of 3 variables. The Jump function (5) was used in [10], its parameter $g$ defines the number of steps one has to go downhill in order to reach the unique maximum. For $g=0$ we have the very simple Onemax function. As the parameter $g$ increases so does the difficulty of the function.

The Gibbs Sampling algorithms with local updates and random blocks are implemented as it has been previously described. For the sampling algorithm that uses problem information we determine the probability of a variable to be included in the block in the following way. First, a variable $x_{i}$ is randomly selected with uniform distribution. The neighborhood of $x_{i}$ is a set $s_{i}$ defined for an additively decomposed function as all the variables which appear together in a sub-function.

For $f_{3 \text { deceptive }}$ it is clear that using this method the probability of having $s$ related variables in a block is higher than when blocks are selected at random. This method can be applied uniquely when the related variables are sequentially ordered. The important point however, is that when some information about the dependencies between variables is available it can be used to form the blocks, even if it is not exact. Note that in our method to form the blocks there is always the possibility to include in the blocks variables that are not related.

## A. Blocked MCMC algorithms for optimization

Now we present results in the optimization of the $f_{3 \text { deceptive }}$ function using the blocked Gibbs Sampling with random and neighborhood based selected blocks. The chain simulation is stopped when the optimum is found. Experiments are done for different values of $n$ and $\beta$. In table I a comparison among the three algorithms is presented: Local (ordinary Gibbs Sampling), Random and Neighborhood blocked Gibbs Sampling. For the blocked Gibbs Sampling algorithms values of $s$ between 2 and 6 were evaluated. For each value of $n$ and $\beta$ the best result in terms of the average passage time is presented with the size of the neighborhood it was achieved with.

As expected best results are obtained with the neighborhood based algorithm, and in almost all the cases they were achieved when $s=3$, i.e. when the size of the block was equal to the size of the set of related variables. For the random blocked algorithm results change. First, it seems to be that when $\beta$ is increased better results are achieved by increasing the neighborhood size. Second, the best value of $\beta$ for the random blocked Gibbs Sampling algorithm is different to the best inverse temperature for the Neighborhood algorithm. Third, results are better than when local update is used, however, the

TABLE I
Different versions of the Gibbs Sampling algorithm For the $f_{\text {deceptive }}$ Function.

difference for some values of $n$ is small.
Table II shows the results of population based heuristics. By far the best results are obtained by FDA. The results of $U M D A$ and $L F D A$ are very similar. This indicates that the network computed by $L F D A$ is too small and does not capture the real interactions [9].

TABLE II
Results for the $f_{\text {deceptive }}$ function.


The results for the function Jump are still more in favor of population search. Whereas $U M D A$ solves these kind of problem in $O\left(n^{1.5}\right)$ [6], scales even blocked Gibbs sampling like $O\left(n^{g a p+1}\right)[10]$.

Thus for these kind of problems, we find that blocked Gibbs Sampling is better than the local Gibbs Sampling. Nevertheless, the results are worse than those achieved with population based search methods. Therefore we tried to find functions where stochastic local search performs substantially better. It turned out that this was more complicated than expected.

## IV. Easy functions for blocked Gibbs sampling

We start with the function $F_{\text {Block }}$. It is maximal when $x$ contains only one block of $B$ contiguous variables set to 1 . The block can start at the end of the vector and continue at the beginning.

$$
F_{\text {Block }}(x, B)=2 n-|B-G(x, B)|-|u(x)-G(x, B)|
$$

Where $u(x)=\sum_{i=1}^{n} x_{i}$ and $G(x, B)$ is the size of the block with size closest to $B$ in $x$.

The maximum of this function is $2 n$, it is reached when the second and third terms in the expression are 0 , i.e. there is only one block with size $B$. The first term is 0 when there is at least one block of size $B$. The second is 0 when there is only one block of ones in the vector. If $B \in[1, n-1]$ then $F_{\text {Block }}(x, B)$ is a multi-modal function with exactly $n$ optima. Each optima corresponds to a block beginning at position $i \in[1, n]$.

TABLE III
Example function $F_{\text {Block }}(x, B)$

Table III shows an example of the evaluation of this function for two vectors of size $n=11$ and different values of the block size $B$.

We conducted a number of experiments to compare the behavior of the GS, the UMDA and the LFDA in the optimization of this function. In these experiments we have used GS with $\beta \mapsto \infty$, this algorithm is better known as local hill climber or $(1+1)$ - algorithm [1]. At every step a new move is proposed. It is accepted only if it is better or equal to the current one. Tables IV and V present the results of the experiments. In each case we have run 100 experiments, and in every case the optimum was found. The population size for the LFDA and the UMDA were of 100 and 50 points. In the tables, Ave. gen. is the average number of generation for the population based search methods, eval. is the average number of evaluation calculated for every set of 100 experiments.

TABLE IV
Results for the function $F_{\text {Block }}$.


In table IV it can be seen that $F_{\text {Block }}(X, B)$ is a very easy function for a single point searcher. Results for the

EDAs are worse. One possible explanation of the behavior of the GS in this case is that for function $F_{\text {Block }}(X, B)$ a monotonic path can be constructed from every point of the search space to one of the optima by changing only one variable in every step. Let us explain this point.

Let us suppose that we start from a random solution $x$ with one or none block. If $x$ is not the optimum then at every step there exists at least one move that increments the value of the function. It is to set or reset (depending if the size of the block is smaller or higher than $B$ ) one of the variables at the extreme of the block. The probability of this move is $\frac{2}{5}$. On the other hand, if the initial point $x$ has more than one block then every move that reduces the size of the blocks other than the one closest to $B$ will increase the fitness of the function until the other blocks will eventually disappear and we will then be in the previously considered case.

Now we analyze why this function is difficult for the UMDA. In the first selected population of the UMDA there is the same probability of having solutions close to any of the optima. The expected univariate probabilities of all the variables is the same and the next population will have then solutions with more than one block or very large blocks. As $B$ approaches $n$ the probability of generating vectors with higher unitation is increased. This function is also deceptive for the LFDA.

The failure of the EDAs in this particular case is that they are unable to learn the constraint related to the maximum number of variables in the block, and they will focus on one of the optima only after a high number of evaluations have been done. Nevertheless, as a mutation effect is present due to the use of priors, the algorithm will find the optimum by means of the diversity injected by the local moves. In this case a very small selected set helps the algorithm to concentrate the search around only one of the optima. However, still the number of evaluations will be higher that in the case of the local hill climber.

TABLE V
Results for the function $F_{\text {Block }}, B=n-5$.


In table V Gibbs sampling is compared with UMDA for different values of $n$. It turns out that both Gibbs sampling and $U M D A$ scale as $o\left(n^{2}\right)$, but Gibbs sampling needs only $1 / 4$ of the function evaluations. It has to be noted that $U M D A$ with a population size of 50 and a truncation value of $\tau=0.02$ selects just one individual. Thus it cannot estimate the univariate marginal distributions, but it heavily depends on mutation (Bayesian prior). This algorithm can be seen as a $(1,50)$ - algorithm adapted to discrete variables [1].

## A. Hierarchical function $F_{\text {Block }}^{h}(x, B)$

Next we consider an extension of the function $F_{\text {Block }}$ by means of a hierarchical function of only two levels. In this hierarchical function the initial vector $x$ is divided in groups of $k$ variables. The current assignment for each group variables determines the values for another single variable in the next level. In the first level are the input variables $\left(x_{1}, \ldots, x_{n}\right)$. The binary value of variable $y_{i}$ in the second level is determined from the set of variables $\left(x_{(i-1) k}, \ldots, x_{(i) k}\right)$ of the first level. The mapping between $\left(x_{(i-1) k}, \ldots, x_{(i) k}\right)$ and $y_{i}$ is done by means of a contribution function $g$. We will call $k$ as the order of the hierarchical function and we assume that $n$ is a multiple of $k$. The $F_{\text {Block }}$ function is evaluated on $\left(y_{1}, \ldots, y_{\frac{n}{k}}\right)$. The following function $g$ is used to interpret a subset of variables $\left(x_{i}, \ldots, x_{i+k}\right)$ of the input vector $x$.

$$
g\left(x_{1}, \ldots, x_{k}\right)= \begin{cases}1 & \text { for } \quad u\left(x_{1}, \ldots, x_{k}\right)=k \\ 0 & \text { otherwise }\end{cases}
$$

We denote the hierarchical version of function $F_{\text {Block }}$ as $F_{\text {Block }}^{h}$, and it is defined as follows.

$$
F_{\text {Block }}^{h}(x, B)=k \cdot F_{\text {Block }}\left(\left(y_{1}, \ldots, y_{\frac{n}{k}}\right), B\right)
$$

The maximum value of $F_{\text {Block }}\left(\left(y_{1}, \ldots, y_{\frac{n}{k}}\right), B\right)$ is $\frac{2 n}{k}$, we multiply by $k$ to guarantee that $F_{\text {Block }}^{h}$ reaches the same maximum ( $2 n$ ) for any $k$. The range of feasible values for $B$ is: $0<B \leq \frac{n}{k}$.

Table VI presents the results achieved in the optimization of this function. In this case no all the runs were successful and the table includes the success rate (succ.) achieved in the 100 runs. The population size used for the UMDA and LFDA were the same as before. The truncation parameter for the UMDA was $T=0.02$, and for the LFDA $T=0.1$. As it can be seen, the performance of the GS for this function is as good as in the case of the $F_{\text {Block }}$ function. The existence of a hierarchy does not make any change in its behavior. For this function the LFDA reaches the optimum more times and with less function evaluations than the UMDA. The LFDA is able

TABLE VI
Results for the function $F_{\text {Block }}^{h}$

to detect the hierarchical structure and to exploit it. As expected both EDAs are sensitive to an increment in the order of the function.

## B. Deceptive hierarchical function $D F_{\text {Block }}^{h}$

Finally we will introduce the function $D F_{\text {Block }}^{h}$ that is the combination of $F_{\text {Block }}^{h}$ and the following bimodal function:

$$
\operatorname{Sim}(x, p)=n-\min (x, n-u(x))^{p}
$$

The optimum of $\operatorname{Sim}(x, p)$ is reached for a vector with all the variables set to one, or all the variables set to zero. The parameter $p$ determines the penalty given to points that are far from the optima. As $p$ is increased higher is the gap from one optimum to the other.

$$
D F_{\text {Block }}^{h}=F_{\text {Block }}^{h}+n-\sum_{i=1}^{i=\frac{n}{k}-1} \operatorname{Sim}\left(\left(x_{(i-1) k}, \ldots, x_{i k}\right), p\right)
$$

The maximum of $D F_{\text {Block }}^{h}$ is $3 n$ and it is reached at the same points that are optima of $F_{\text {Block }}^{h}$. We have chosen function $D F_{\text {Block }}^{h}$ because it combines two different sources of difficulty for optimization algorithms. The existence of a barrier that has to be crossed to reach the optima, and the presence of multiple optima. Notice that the second term of the function can be maximized for any combinations of null-blocks and one-blocks of order $k$. The first term is only maximized for certain combinations of null and one-blocks. One conflict arises when the second term has reached its maximum at a configuration that is not yet the optimum of the first term. In this case the optimization algorithm has to be able to decrease the value of the second term in order to reach the global optimum, and this is very difficult as is shown in table VII.

TABLE VII
Results for the function $D F_{B l o c k}^{h}, n=40, k=4, B=9$

In the table are presented the results of the comparison between the GS, blocked GS and the LFDA for the function $D F_{B l o c k}^{h}, n=40, k=4$ and $B=9$. A maximum of 500000 evaluations are allowed to each run of the algorithms. For GS we have tried different values of the temperature. When $p=1$ we have selected the temperature where less function evaluations are required to reach the optimum. For $p=5$ the algorithm does not improve the results when the temperature is changed. Ave. is the average number of evaluations for the successful runs.

The difference in the behavior of the algorithms is very clear. EDAs cannot solve this problem, as already explained for $F_{B l o c k}^{h}$. GS with infinite $\beta$ can not solve it either because it can not escape from the local optimum. GS with a low $\beta$ is the most interesting. When $p=1$, a low $\beta$ will allow the algorithm to reach the global optimum with much less functions evaluations than those needed for blocked GS. Nevertheless as $p$ is increased changes in the inverse temperature will be useless.

The changes in the behavior of the algorithms due to changes in $p$ can be explained as follows. When $p$ is low, a number of consecutive moves away from the local optima can be accepted, increasing the probability of falling in a basin of attraction of the global optima. When $p$ is increased, moves away from the local optimum are very rare, and the probability of falling in a basin of attraction of the global optimal is much smaller than that of returning to the previous point.

Blocked GS can solve this problem by jumping from the local optimum to the global optimum in only one transition. In this case the probability of hitting the optimum does not depend on $p$ but on the size of the neighborhood. Nevertheless, even for the blocked GS the number of steps to reach the optimum increase exponentially with the distance between the optima.

## V. Conclusions

We have shown that it is difficult to find in the space of binary functions optimization problems where stochastic
sampling techniques outperform population search using a suitable search distribution substantially. We have defined such a class of problems. In these optimization problems there exist many paths leading to the optima, requiring either single bit or blocked bit flips.

In all cases considered, using a suitable neighborhood and accepting more or less only points of better or equal probability, performed better than using an annealing schedule for the temperature. This results confirms the theoretical analysis described in [10].

The class of problems where stochastic local search outperforms population search based on the Boltzmann distribution seems to be small, compared to the class where population search outperforms stochastic local search. This result confirms what has been already found in practice - to use stochastic local search not as an alternative to population search, but to use it as a hill-climber within population search.
