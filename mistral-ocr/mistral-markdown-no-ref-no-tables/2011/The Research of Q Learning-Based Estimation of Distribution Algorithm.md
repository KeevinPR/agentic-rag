# The Research of Q Learning-Based Estimation of Distribution Algorithm 

Hu yugang<br>Information Department<br>Changzhou Textile Garment Institute<br>Changzhou china<br>Huyugang80@163.com


#### Abstract

This paper focuses on the theory of estimation of distribution algorithms. First, elaborated the idea of estimation of distribution algorithms, And then for the limitations of solving complex optimization problems,proposed Q Learning-Based Estimation of Distribution Algorithm. The Q learning algorithm is introduced into evolutionary computation, through the Agent and group interaction, to achieve a probability model of adaptive updates. Test functions using six classical comparative experiment, the results show that the algorithm performance is stable, running time is short, with a strong global search ability, is an efficient solving algorithm for function optimization problems.


Keywords- Estimation of Distribution Algorithm, Q Learning, Evolutionary Search

## I THE PROPOSED ESTIMATION OF DISTRIBUTION ALGORITHM

In order to overcome the genetic algorithm because of chromosomal rearrangements lead to the chain problem, people ask if you can not use the crossover and mutation operations, but by the optimal solution set from the extracted information, and then use this information to generate new solutions of the probability distribution, which Chain Linkage Leaning. The probability model using constructive thinking into the evolution of computing the theoretical basis for estimation of distribution algorithms.

The concept of estimation of distribution algorithm first proposed in 1996, and after the year 2000 has been developing rapidly. It will build into the probability model and the sampling process of evolution to replace the traditional crossover and mutation. As is the use of probabilistic models to guide the search process, to avoid the blindness caused by chromosomal recombination and random, Thus effectively improving the efficiency of search, Fast, reliable solution to many of the traditional genetic algorithm optimization problem difficult to solve.

## II Q LEARNING-BASED ESTIMATION OF DISTRIBUTION ALGORITHM

## A Questions

Not difficult to find by analyzing the existing distribution of variables unrelated to the reason why estimation algorithm will often display a poor performance is due to update its probability vector normal to a single fixed strategy, not only can not guarantee that the whole evolution process of the strategy is always effective, Does not take into account the evolution of the gene locus that
appears when the difference. If the probability of each gene locus corresponding values can be adaptive in the evolutionary process of updating, it will help to improve the performance of evolutionary search

In order to achieve the adaptive update the probability vector can be associated with a different gene locus Agent, and the selection probability update rules as its action. Thus, the probability value of each update to convert into Agent performs an action. If the group as a further evolution of the environment, each Agent can use reinforcement learning method and the environment interact to find the optimal movement strategy.

Q learning as a typical reinforcement learning algorithm does not need to estimate the environmental model, but an iterative calculation by optimizing the Q function to obtain the optimal movement strategy, which can be selected as the Agent of learning. It is based on this idea, the following proposed Q Learning-Based Estimation of Distribution Algorithm(QEDA). B Algorithm design

Q Learning-Based Estimation of Distribution Algorithm with the binary coding, population size is N , code length $m$, the first generation of the probability vector $t$ is denoted by $p(t)=(p 1(t), p 2(t), \ldots p m(t))$, Where pi (t) for the first i loci the probability of taking one. The basic flow algorithm consistent with Figure 1, each iteration including selection, construction (updated) probability models and sampling and other operations.

Sampling operation and PBIL, UMDA, etc. the same algorithm, using Monte Carlo method, in accordance with the probability vector N individuals randomly generated. Options selected in addition to the fitness of each generation according to the optimal sub-groups, but also select the worst sub-groups, based selectivity are $\mathrm{r}(0<\mathrm{r}$ $<1$ ), the size of the sub-groups are $\mathrm{M}=\lfloor\mathrm{rr}\rfloor$. Updated statistical probability model, respectively, the optimal operation of first and worst in you to take a sub-group the frequency of, denoted by gi (t) and bi (t), then accordingly update the probability pi $(\mathrm{t})$.

Q learning method using the update pi $(\mathrm{t})$, required for each gene locus associated with an Agent, and the evolution of the corresponding groups of bits of each generation as the environment. The definition of state of the environment, should be able to distinguish the gene locus in the evolutionary process in which the different stages. Therefore, according to the gi (t) and bi (t) to define the relationship between the state.

Greater frequency threshold set $\theta_{\text {high }}, \theta_{\text {low }}$ smaller frequency threshold, $\theta_{\text {diff }}$ for the frequency difference

threshold, Agent; the first t generations of the state are divided as follows.
(1) $\mathrm{gi}(\mathrm{t})>\theta_{\text {high }}$. and $\mathrm{bi}(\mathrm{t})>\theta_{\text {high }}$, or $\mathrm{gi}(\mathrm{t})<\theta_{\text {low }}$ and $\mathrm{bi}(\mathrm{t})<$ $\theta_{\text {low }}$;
(2) $\mid g i(t)-b i(t)\left|>\theta_{\text {diff }}\right|$;
(3) Otherwise does not meet the above criteria.

Agent, the first generation of action $t$ set includes the following probability update rules.
(1) Action 1, the probability decreases
$\operatorname{Pi}(\mathrm{t}+1)=\beta \mathrm{pi}(\mathrm{t})$
(2) Action 2, the probability increases
$\operatorname{Pi}(\mathrm{t}+1)=1-\beta[1-\mathrm{pi}(\mathrm{t})]$
(3) Action 3, probability values remain unchanged
$\operatorname{Pi}(\mathrm{t}+1)=\mathrm{pi}(\mathrm{t})$
equation $(0)-(2), \mathrm{i}=1,2, \ldots, \mathrm{~m}, \beta(\mathrm{o}<\beta<1)$ to adjust the rate. Agenti interact with the environment, you can choose to perform the appropriate action to obtain the next generation of probability pi $(\mathrm{t}+1)$. To store Agenti corresponding to a set of Q , the definition of matrix Qi: $\mathrm{Q}_{i}=\left[\mathrm{Q}_{i}\left(\mathrm{~s}_{\mathrm{i}}, \mathrm{a}_{\mathrm{k}}\right)\right]_{i>3}$

Algorithm for each iteration, each Agenti $\square$-greedy strategy selection in accordance with action, according to the rewards and status of their conversions update the corresponding Q values. If the first $\mathrm{t}-1$ on behalf of the state when the environment Agenti s, choose action $\alpha$ executed, the first generation of environmental state transition t to $\mathrm{s}^{\prime}$, then press the style update $\mathrm{Qi}(\mathrm{s}, \mathrm{a})$ :
Qi (s , a) $\leftarrow$ Qi (s , a) $+\alpha\left[r_{i}(t-1)+\gamma \max \mathrm{Qi}\left(\mathrm{s}^{\prime}, \mathrm{a}^{\prime}\right)-\mathrm{Qi}\right.$ (s , a) $]$
$\mathrm{r}_{\mathrm{i}}(\mathrm{t}-1)=\left\{\begin{array}{l}1 \downarrow \mathrm{pi}(\mathrm{t})-\mathrm{gi}(\mathrm{t})|<| \mathrm{pi}(\mathrm{t}-1)-\mathrm{gi}(\mathrm{t}-1)| \\ -1, \quad \text { others }\end{array}\right\}$
Where, ri (t-1) for the Agenti in t-1 obtained on behalf of an immediate return.

Q Learning-Based Estimation of Distribution Algorithm is given below the steps. Algorithm to replace the elitist strategy group to ensure the optimal solution search is not degraded.
Algorithm1: Q Learning-Based Estimation of Distribution AlgorithmInitialization Qi, $\mathrm{i}=1,2, \ldots, \mathrm{~m}$ zero matrix, p (1) $==\left(0.5,0.5, \ldots, 0.5\right), \quad \mathrm{t}=1$; While (termination condition is not satisfied algorithm) do

According to p (t) sampled individuals generate $\mathrm{N}-1$, and $\mathrm{t}-1$ together constitute the best individual on behalf of the current groups. New individual determination of i-bit value is: generate a random number $\xi \in[0,1]$, if $\xi \leq$ pi (t) is taken 1 , or take 0 ;
Calculation of N individuals of fitness function and sorting;
M -choose the best and the worst individuals, the frequency of statistics you get a value of gi (t) and bi (t), i $=1,2, \ldots, \mathrm{~m}$;
For (i-loci associated Agenti, $1 \leq \mathrm{i} \leq \mathrm{m}$ )
Recorded before found their $\mathrm{t}-1$ action on behalf of the state s and a , by gi (t) and bi (t) determine the current state s';

By equation (5) calculated an immediate return, according to equation (3.14) update Qi (s, a);
Generate random numbers $\xi \mathrm{i} \in[0,1]$, if $\xi \mathrm{i} \leq \square$, Randomly selected with equal probability of action a ', otherwise select
$\mathrm{a}^{\prime}=\operatorname{argmax} \mathrm{Qi}\left(\mathrm{s}^{\prime}, \mathrm{a}^{\prime}\right)$;
According to equation (0) - (2) and the action a 'corresponds to the formula. Calculate the new probability value pi $(\mathrm{t}+1)$;
End
$\mathrm{t} \leftarrow \mathrm{t}+1$;
End
C Improvement Strategies
The algorithm each update probability pi (t) time, Agenti $\square$-greedy strategy to choose an action, that is, the greater the probability of $1-\square$ select the maximum Q value of the current state of the corresponding action, but with a smaller probability of randomly selected action $\square$. As $\square$-greedy strategy is not always accept the best action, but increased the probability of random selection, thus contributing to Agent explore new knowledge, than the greedy strategy with better results.

However, the value of using a fixed $\square$ has some limitations. Especially in the Ageni some time after learning, the current strategy is near optimal, if the probability of $1-\square$ still randomly choose an action, it will have an impact on the convergence of the algorithm. If you can gradually reduce the evolution $\square$ values, will further enhance the Q study the performance of estimation of distribution algorithms. The use of simulated annealing (SA) algorithm MetroPolis criteria to be able to do this, it is the way by reducing the temperature to gradually reduce the probability of receiving inferior solution.

Here are guidelines for improved use of MetroPolis Q Learning-Based Estimation of Distribution Algorithm Algorithm2: Improved Q Learning-Based Estimation of Distribution Algorithm
Initialization $\mathrm{Qi}_{\mathrm{s}}, \mathrm{i}=1,2, \ldots, \mathrm{~m}$ zero matrix, the temperaturer $=\tau 0, \mathrm{p}(1)=(0.5,0.5, \ldots 0.5), \mathrm{t}=1$;
While (termination condition is not satisfied algorithm) do
According to p (t) sampled individuals generate $\mathrm{N}-1$, and $\mathrm{t}-1$ together constitute the best individual on behalf of the current population;
Calculation of N individuals of fitness function and sorting;
M -choose the best and the worst individuals, the frequency of statistics you get a value of gi (t) and bi (t), i $=1,2, \ldots, \mathrm{~m}$;
For (i-loci associated Agenti, $1 \leq \mathrm{i} \leq \mathrm{m}$ )
Recorded before found their $\mathrm{t}-1$ action on behalf of the state s and a , by gi (t) and bi (t) determine the current state $\mathrm{s}^{\prime}$;
By (5) calculation of an immediate return, according to equation (4) Update Qi (s, a);
Come to a ' $=\operatorname{argmax} \mathrm{Qi}\left(\mathrm{s}^{\prime}, \mathrm{a}^{\prime \prime}\right)$, randomly select an action ar, according to the following probability to determine a ':

$$
\begin{aligned}
& \mathrm{P}\left\{\mathrm{a}^{\prime}=\mathrm{a}^{*}\right\}=\varnothing \quad \tau \\
& \mathrm{P}\left\{\mathrm{a}^{\prime}=\mathrm{a}^{*}\right\}=1-\mathrm{P}\left\{\mathrm{a}^{\prime}=\mathrm{a}^{\prime}\right\}
\end{aligned}
$$

According to equation (0) - (2) and the action a 'new formula to calculate the corresponding probability value pi $(t+1)$;
End
Cool: $\tau \leftarrow \lambda \tau$;
$t \leftarrow t+1$
End
Algorithm to geometric cooling strategy $\tau \leftarrow \lambda \tau$, Where $\lambda \in(0,1)$ is the temperature coefficient ${ }_{*}$ As the temperature decreases , Agenti randomly selected probability of action will become increasingly smaller, When the temperature tends to 0 , the strategy is equivalent to the greedy strategy.

## III COMPARATIVE EXPERIMENT

## A Test Functions

To evaluate the performance of Q Learning-Based Estimation of Distribution Algorithm, The following algorithm using the UMDA, PBIL algorithm, MIMIC algorithm And genetic algorithm function optimization comparative experiments. Select 6 Benchmark test functions for testing. Are the Sphere function, Quadric function, Schaffer function, Griewank function, Rosenbrock function and Rastrigin function. Benchmark functions of these different patterns, with good test performance. Which, Schaffer function, Griewank function and Rastrigin functions are multimodal function, there are a lot of local minima, generally more difficult to find the global optimum algorithm, the algorithm used to test the ability to jump out of local optimum; Rosenbrock function as a single Peak, non-convex pathological function of the flat trend in the value range, the convergence to the global optimal point is remote, can be used to evaluate the efficiency of the algorithm; Sphere function and the Quadric function is a single peak function, can test the accuracy of optimization algorithm, Examine the implementation of the algorithm performance.
B Experimental Analysis
After several tests, Q Learning-Based Estimation of Distribution Algorithm parameters are as follows: frequency threshold were $\theta_{\text {high }}=0.75, \theta_{\text {low }}=0.25, \theta_{\text {diff }}=$ 0.35 , select the rate of $\gamma=0.2$, probability adjusted rate $\beta$ $=0.9$, learning factor $\mathrm{a}=0.2$, discount factor $=0.9$. For comparison UMDA PBIL algorithm selection algorithm and the rate is taken 0.2 , PBIL learning rate algorithm to take 0.1 ; MIMIC algorithm selection ratio is 0.4 ; genetic algorithm uses single point crossover, crossover rate 0.7 , mutation rate 0.1 ; their Elitist strategy are used. All of the above algorithm population size are set to 50 , the termination condition for the search to the global optimum or the maximum evolution generation T, take T $=200$.

Taking into account all the above algorithm has a certain randomness, use them to function $\Omega-\beta 6$ are independently tested 50 times, the experimental results shown in the table. Among them, Table 1 for each algorithm the number of global optimal value obtained, Table 2 shows the results of 50 runs on average, standard deviation and worst values, Table 3 shows the average running time of each method (unit: Seconds). Table $\square$ QEDA and M-QEDA represent the use of strategies and MetroPolis $\square$-greedy Q Learning-Based Estimation of Distribution Algorithm, the former taking $\square=0.1$, initial temperature of the latter: $\tau 0=50$, temperature coefficient of $\lambda=0.9$. Table 1 Algorithm for number of times the global optimal value obtained


Table 2 The results of the algorithm is run 50 times the mean, standard deviation and worst values
Table 3 The average running time of each algorithm

It can be seen, both the traditional genetic algorithm, or UMDA, PBIL and MIMIC other existing distribution algorithm, function optimization in solving these complex problems are not easy to search the global optimum value. Which, PBIL search success rate of slightly higher average of $68 \%$, other 3 , the algorithm less than $50 \%$. Q LearningBased Estimation of Distribution Algorithm are demonstrated excellent performance, especially after using Metropolis criterion and, for the 6 functions are $100 \%$ Benchmark global optimal value obtained. In the algorithm execution time, the dual variable associated MIMIC worst performance of the algorithm, generally longer than the other algorithms 5-10 times; and M-QEDA algorithm in addition to solving the Rosenbrock function as PBIL algorithm, but in other cases have shown The best time performance.
