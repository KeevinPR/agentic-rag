# A Hybrid Estimation of Distribution Algorithm with Differential Evolution for Global Optimization 

Bing Dong, Aimin Zhou and Guixu Zhang<br>Shanghai Key Laboratory of Multidimensional Information Processing<br>Department of Computer Science and Technology<br>East China Normal University, 3663 North Zhongshan Road, Shanghai 200062, China<br>Email: bing@stu.ecnu.edu.cn, \{amzhou,gxzhang\}@cs.ecnu.edu.cn


#### Abstract

In evolutionary algorithms, it is difficult to balance the exploration and exploitation. Usually, global search is utilized to find promising solutions, and local search is beneficial to the convergence of the solutions in the population. Combing different search strategies is a promising way to take advantages of different methods. Following the idea of DE/EDA, this paper proposes another way to combine estimation of distribution algorithm and differential evolution for global optimization. The basic idea is to choose either differential evolution or estimation of distribution algorithm for generating new trial solutions. To improve the algorithm performance, a local search strategy is used as well. The new approach, named as EDA/DE-EIG, is systematically compared with two state-of-art algorithms, and the experimental results show the advantages of our method.


Index Terms-DE, EDA, global optimization, eigenvector

## I. INTRODUCTION

Estimation of distribution algorithms (EDAs) are stochastic optimization algorithms exploring the space of potential solutions [1]-[3]. Unlike traditional evolutionary algorithms (EAs), there is no mutation or crossover in EDAs. They build explicit probabilistic models and sample from the built probabilistic models to obtain promising solutions. The explicit use of the probabilistic model has significant advantages over other methods, as it can utilize the global information of the population for producing more promising solutions.

Differential evolution (DE) has attracted a number of researchers from various background since proposed by Storn and Price [4], [5]. It uses the distance and direction information from the solutions in the current population to guide the process of search. DE is easy to be implemented and it has been widely applied to a variety of fields, i.e., control systems [6], robot control [7], remote sensing [8], electrical engineering [9], economic dispatch [10]. The main reasons of the popularity of DE are as follows [11]: (a) DE is much more simple to implement compared to other EAs with complex operations, (b) the parameters are fewer in comparison with other EAs ( $C R, F, N P$ in classical DE), and (c) recent researches have shown its superior performance on a wide variety of problems [12]-[14].

To improve the efficiency of DE for dealing with hard optimization problems, DE has also been hybridized with other search strategies, and the examples include DE/EDA [15], DE/BBO [16], DEPSO [17], DEFO [18], and etc.. Among them, DE/EDA utilizes the global information extracted by

EDA and the differential information exploited by DE to obtain promising solutions [15]. The differential information (i.e., direction and distance) from the solutions of the population is beneficial to accelerate the convergence speed, whereas the global information produced by EDA can guide the search to a more promising direction. By combing DE and EDA, ED/EDA is able to utilize both of the information and thus to balance the exploration and exploitation.

Following the idea of DE/EDA, this paper proposes another way to combine DE and EDA. The basic idea is to use either a DE operator or an EDA operator to generate a new trail solution. The new approach, named as EDA/DE-EIG, combines EDA with an enhanced DE [19], which utilizes an eigenvectorbased crossover operator. Meanwhile, in order to improve the performance and avoid the solutions converged without obtaining optimal solutions, a local search is incorporated into this algorithm.

The remainder of the paper is organized as follows. In Section II, the definition of the problem is presented, and the basic algorithm frameworks of DE and EDA are introduced as well. Section III gives the details of the proposed algorithm EDA/DE-EIG. In Section IV, a systematic experiment is conducted to show the performance of EDA/DE-EIG. Finally, the paper is concluded in Section V.

## II. Related Work

This section firstly defines the global optimization problem. Then the basic algorithm frameworks of DE and EDA algorithms are introduced.

## A. Definition

The box-constrained continuous global optimization can be stated in the following:

$$
\begin{array}{ll}
\min & f(x) \\
\text { s.t } & x \in\left[a_{i}, b_{i}\right]^{n}
\end{array}
$$

where $x=\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{T} \in R^{n}$ is a decision vector, $\left[a_{i}, b_{i}\right]^{n}$ is the search space and $f: R^{n} \rightarrow R$ is the objective function.

## B. Differential Evolution

DE is a population-based global optimization algorithm. There are mainly three operations in classical DE, i.e., mutation, crossover and selection. The main algorithm framework of classic DE is given in Algorithm 1.

```
Algorithm 1: DE
1 Initial the population \(P_{0}\) randomly :
    \(P_{0}=\left\{x_{1, D}, x_{2, D}, x_{3, D}, \cdots, x_{N, D}\right\}\)
2 while not terminate do
    // mutation
    \(v_{i, G}=x_{r 1, G}+F \cdot\left(x_{r 2, G}-x_{r 3, G}\right)\)
    // crossover
    if \(\operatorname{rand}_{j}(0,1) \leq C R\) or \(j=j_{\text {rand }}\) then
        \(u_{i, j, G}=v_{i, j, G}\)
    else
        \(u_{i, j, G}=x_{i, j, G}\)
    end
    // selection
    if \(f\left(u_{i, G}\right) \leq f\left(x_{i, G}\right)\) then
        \(x_{i, G+1}=u_{i, G}\)
    else
        \(x_{i, G+1}=x_{i, G}\)
    end
14 end
```

Some details of DE is given as follows.

- Initial population: The points in the population are the target vectors. $N$ is the size of the population, and $D$ is the dimension of the target vector.
- Mutation: The rand-1-bin mutation schema is used here, and there are other schemas that can be utilized in DE. At each generation $G$, a mutant vector $v_{i, G}$ is obtained by the mutation operator. $F$ is the scaling factor, $r 1, r 2, r 3$ are mutually different integers randomly selected from $[1, N]$ and also different from $i$.
- Crossover: The trial vector $u_{i, j, G}$ is generated by combing the mutant vector $v_{i, G}$ and the target vector $x_{i, j, G}$ according to the crossover operator. Hereby, $\operatorname{rand}_{j}(0,1)$ is a uniformly distributed random number between 0 and 1 , and $j_{\text {rand }}$ is a random integer between $j$ and $D$, avoiding the trial vector is totally same as the target vector. $C R$ is the controlling parameter.
- Selection: The trial vector $u_{i, G}$ and the target vector $x_{i, G}$ compete to enter the next generation in accordance with the objective function value.


## C. Estimation of Distribution Algorithm

EDA is an emerging algorithm for the optimization, and it is distinct from traditional EAs. EDA consists of three main steps, including modeling, sampling and selection generally. The basic framework of EDA is shown in Algorithm 2.

## III. Our Method

DE/EDA is a hybrid algorithm for global optimization based on the combination of DE and EDA. However, as the DE

## Algorithm 2: EDA

1 Initialization: Initial the $\operatorname{Pop}(t)$ randomly, and $t$ is the generation.
2 while not terminate do
3 Modeling: Build a probabilistic model $p(x)$ according to the statistical information of the $\operatorname{Pop}(t)$.
4 Sampling: Generate a new solution set $Q$ by sampling from the built probabilistic model $p(x)$.
5 Selection: Select from $Q \cup \operatorname{Pop}(t)$ to construct the next population $\operatorname{Pop}(t+1)$. The selection criterion is the objective function value.
$6 \quad t=t+1$
7 end
utilized in DE is quite simple. A more promising DE algorithm DE-EIG is imported to improve the performance. DE/EDA generates the offspring generation by utilizing the DE and EDA by the CRP. Meanwhile, for the further improvement, expensive LS [20] is applied. This section will introduce the framework of DE/EDA, DE-EIG and expensive LS respectively. And the algorithm framework of EDA/DE-EIG is presented finally.

## A. DE-EIG

As traditional DE operates the crossover in the original coordinate, it is inevitable to lose some statistical information. To utilize the statistical information of the population, the eigenvectors of the solutions have been applied to the crossover in DE [19], [21]. DE-EIG makes the crossover rotationally invariant by transform the coordinate system of the solutions in the population [19]. It has shown impressive advantages over BBOB 2012 [22] and CEC 2013 [23] benchmark functions and two real-world optimization problems in CEC 2011 [24] compared other six algorithms.

In DE-EIG, an alternate coordinate system is employed by the individuals during the crossover. The eigenvector of the population is utilized to transform the coordinate system. Meanwhile, to exploit the diversity of the population and prevent the premature of the solutions in the population, the candidate solutions are generated with the original coordinate system or the rotated coordinated system randomly by a parameter.

The Algorithm 3 is the main framework of DE-EIG.

## B. $D E / E D A$

The EDA/DE-EIG is proposed on the basis of the frame work of DE/EDA [15]. EDA is incorporated with DE to generate more promising solutions. Hence, the efficiency of the search is improved meanwhile. The main algorithm framework of DE/EDA is presented in Algorithm 4.

## C. Expensive local search

It is noteworthy that EAs are not very good at refining promising solutions especially in the later stage. Hence, it is significant to apply other search methods to accelerate

## Algorithm 3: DE-EIG

1 Initial the population $\operatorname{Pop}(t)=\left\{x_{1}, x_{2}, x_{3}, \cdots, x_{N}\right\}(N$ is the size of the population)
2 while not terminate do
$v_{i, G}=x_{r 1, G}+F \cdot\left(x_{r 2, G}-x_{r 3, G}\right)$
if $\operatorname{rand}()<p$ then
if $\operatorname{rand}() \leq C R$ then
$u_{i, G}=v_{i, G}$
else
$u_{i, G}=x_{i, G}$
end
else
Compute the the eigenvector matrix $E$ of $x_{i, G}$, let $E^{\prime}$ be the inverse matrix.
$x_{i, G}^{\prime}=E^{\prime} \cdot x_{i, G}$
$v_{i, G}^{\prime}=E^{\prime} \cdot v_{i, G}$
if $\operatorname{rand}() \leq C R$ then
$u_{i, G}^{\prime}=v_{i, G}^{\prime}$
else
$u_{i, G}^{\prime}=x_{i, G}^{\prime}$
end
$u_{i, G}=E \cdot u_{i, G}^{\prime}$
end
if $f\left(u_{i, G}\right) \leq f\left(x_{i, G}\right)$ then
$x_{i, G+1}=u_{i, G}$
else
$x_{i, G+1}=x_{i, G}$
end
$t=t+1$
end
the convergence speed. For this purpose, the expensive local search (LS) is introduced to improve this condition [20]. For simplicity, the details of the algorithm will not be presented here.

## D. EDA/DE-EIG

In order to combine an enhanced DE with EDA and balance the global search and local search, the EDA/DE-EIG is proposed. EDA is utilized to extract the statistical information of the population, and the DE-EIG is beneficial to obtain the most important information of the population. The $C R P$ to allocate the resource of EDA and DE-EIG is crucial to the performance of the algorithm. It is relatively problem-dependent. Hence it is a significant topic to study the $C R P$ setting of the algorithm.

In Algorithm 5, the $C R P$ is utilized to generate solutions by DE-EIG and EDA. Both the two algorithms play an important role to generate promising solutions. For Converage $\left(\theta, G, G_{e}\right)$ at line 18 , it is essential to judge whether to operate expensive local search. Full description can be obtained from [20].

## IV. EXPERIMENTAL STUDY

In this section, EDA/DE-EIG will be compared with JADE [25] and DE/EDA [15]. The source codes of JADE are

## Algorithm 4: DE/EDA

1 Generate population $\operatorname{Pop}(t)$ randomly consists of N solutions $x_{1}, x_{2}, \cdots, x_{N}$ from the feasible search space. while not terminate do
Construct the probabilistic model:
$p_{k}(x)=\prod_{i=1}^{n} \mathcal{N}\left(x_{i} ; \mu_{i}, \sigma_{i}\right)$
For all $j=1,2, \cdots, n$, produce a trial solution $u=\left(u_{1}, u_{2}, \cdots, u_{n}\right)$
if $\operatorname{rand}()<C R P$ then
$u_{j}=\frac{\left(x_{i}\right)_{j}+\left(x_{d}\right)_{j}}{2}+F \cdot\left[\left(x_{d}\right)_{j}-\left(x_{i}\right)_{j}+\left(x_{b}\right)_{j}-\left(x_{c}\right)_{j}\right]$
else
$u_{j}$ is sampled according to $\mathcal{N}\left(x_{i} ; \mu_{i}, \sigma_{i}\right)$ end
where $C R P$ is the controlling parameter.
if $f(u)<f\left(x_{i}\right)$ then
$x_{i}^{t+1}=u$
else
$x_{i}^{t+1}=x_{i}^{t}$
end
$t=t+1$
end

## Algorithm 5: EDA/DE-EIG

1 Initial the population $\operatorname{Pop}(t)=\left\{x_{1}, x_{2}, x_{3}, \cdots, x_{N}\right\}(N$ is the size of the population)
2 while not terminate do
Construct the probabilistic model:
$p(x)=\prod_{i=1}^{n} \mathcal{N}\left(x_{i} ; \mu_{i}, \sigma_{i}\right)$
Generate a trial solution $u_{i, G}$ as follows:
if $\operatorname{rand}()<C R P$ then
$u_{i, G}$ is produced by DE-EIG.
else
$u_{i, G}$ is sampled from the probabilistic model $p(x)$.
end
if $f\left(u_{i, G}\right)<f\left(x_{i, G}\right)$ then
$x_{i, G+1}=u_{i, G}$
else
$x_{i, G+1}=x_{i, G}$
end
if Converage $\left(\theta, G, G_{e}\right)$ then
Operate the expensive local search.
end
$t=t+1$
end
from the authors. DE/EDA is implemented by ourself. The test instances and parameter settings are introduced in this section. A comprehensive study of the experimental results will be presented to illustrate the impressive advantages of EDA/DE-EIG.

TABLE I
statistical results (mean $\pm$ std) for the three algorithms on instances $f 1-f 13$.


${ }^{1}$ The bold ones mean the best.

## A. Algorithms for Comparison

JADE [25] is an adaptive DE with a novel mutation strategy "DE/current-to-pbest" with optional external archive and updating control parameters. JADE has been compared with several state-of-art algorithm and performs impressively. DE/EDA [15] is a hybrid algorithm incorporating EDA with DE, and it is the main framework of EDA/DE-EIG meanwhile. The three algorithms will be compared to EDA/DE-EIG on the same test instances.

## B. Test Instances

All the algorithms will be compared on the first 13 test instances from YYL test instances [26]. The global minimum objective value is 0 for all test instances. And the test instances can be categorized into four kinds: $f 1-f 5$ are unimodal functions. $f 6$ is a step function. And $f 7$ is a function with white noise. $f 8-f 13$ are multimodal functions with many local optimal solutions. Hence, the test instances can be able to assess the performance of the algorithms from various aspects.

## C. Parameter Settings

To compare the performance of the algorithms fairly, the parameter setting will be set according to the setting in the corresponding papers. All the algorithms are implemented by Matlab and executed in the same computer. The parameter settings are as follow:

1) The dimension of the population will be set to be 30 for all test instances. All algorithms are run independently 50 times and stopped after 450,000 function evaluations.
2) JADE: The parameters $N=150, p=0.05, c=$ $0.1, F=0.5$ and $C R=0.9$ are recommended in [25].
3) DE/EDA: The parameters are set as: $N=150, F=0.5$ and $C R P=0.9$, which are considered according to the experimental results in [15].
4) EDA/DE-EIG: The $C R P$ is $0.5 ; F$ is set to be 0.5 ; $C R$ is set to be 0.6 ; the parameter $p$ to control the probability to operate crossover two coordinate systems is 0.5 ; the convergence threshold $\theta=0.1$; the size of the population $N$ is 150 . For the parameter setting of expensive local search, it is same as that in [20].

## D. Experimental Results and Analysis

Table I illustrates the mean and the standard deviation of the results obtained by the four algorithms after 450,000 FEs over 50 independent runs. The Wilcoxon rank sum test at 0.05 significance is performed to compare the function value obtained by EDA/DE-EIG to another algorithm. And " + ", "-", and " $\sim$ " respectively denotes the function objective value of another algorithm is larger than, less than, and similar to that of EDA/DE-EIG at 0.05 significance level by a Wilcoxon rank sum test.

From Table I, the impressive performance of EDA/DE-EIG is distinct with comparison to the other two algorithms for the mean value of the final results. EDA/DE-EIG obtain the best results on 9 test instances except $f 5, f 7, f 8$ and $f 9$. For further comparison, EDA/DE-EIG will be compared with the other two algorithms respectively. For DE/EDA, EDA/DE-EIG has a substantial improvement of the performance. EDA/DE-EIG

![img-0.jpeg](img-0.jpeg)

Fig. 1. The mean function value versus evaluation counts on the test instances.

performs better than DE/EDA on 7 test instances. EDA/DEEIG has made a relatively significant improvement for the first five test instances and $f 11$. The difference between the two algorithms over these test instances are distinct.

Compare EDA/DE-EIG with JADE, EDA/DE-EIG has advantages over JADE on 5 test instances. And both the two algorithms obtain the best results on $f 6, f 10, f 12$ and $f 13$. In conclusion, the significant performance of EDA/DE-EIG is competitive. For $f 6, f 10, f 12, f 13$, the three algorithms have the same results. For $f 11$, only EDA/DE-EIG obtains the best result. JADE does not perform well enough because of worse performance of several runs. It should be noteworthy that EDA/DE-EIG has a distinct performance for $f 1-f 4$ and $f 11$. As for $f 7 f 8$ and $f 9$, EDA/DE-EIG may be impacted by the local optimum of DE. It is worthwhile to improve the performance of EDA/DE-EIG on these test instances.

Meanwhile, from a more objective prospect, the Wilcoxon rank sum test is implemented to compare the performance of EDA/DE-EIG with that of others. For JADE, EDA/DEEIG outperforms on 3 test instances. And the two algorithms obtain the similar performance on 6 test instances. EDA/DEEIG does not perform as well as JADE on 4 test instances. In general, EDA/DE-EIG has made an substantial improvement in comparison with DE/EDA. It does indicate the effect brought by DE-EIG. As for JADE, EDA/DE-EIG nearly has similar performance on 13 test instances statistically. Hence, the performance of EDA/DE-EIG is relatively promising and need further exploration.

Moreover, for a more detailed illustration of the performance of EDA/DE-EIG, the Figure 1 is the mean function value of the three algorithms, intuitively illustrates the comparison of the performance of the three algorithms on 12 test instances except $f 6$. As the results of JADE and EDA/DEEIG except DE/EDA converges very fast on $f 6$. For a better presentation, the result of $f 6$ will not be presented here. Statistically, EDA/DE-EIG obtain the best results on 8 out of 12 test instances. EDA/DE-EIG is superior to the other two algorithms on convergence speed or the final solution. Especially for some instances, including $f 1, f 2, f 3 f 4$ and $f 11$, the improvement is extremely distinct. For DE/EDA, it performs worse than EDA/DE-EIG on 11 test instances except $f 7$ and $f 8$. In comparison with JADE, EDA/DE-EIG outperforms on $f 1-f 4$ both on convergence speed and the final solution. As for $f 5$, though JADE obtains a better solution. EDA/DE-EIG has a more promising convergence trend and converge faster. For $f 7, f 8$ and $f 9$, EDA/DE-EIG does not have a desired performance. Hence, the performance of ED-EIG to improve the solution need more exploration. For $f 10, f 12$ and $f 13$, EDA/DE-EIG has advantages on the convergence speed. In conclusion, EDA/DE-EIG has made a impressive improvement of DE/EDA. Meanwhile, with comparison to JADE, EDA/DEEIG has the advantages on convergence speed or the final solution. In conclusion, the performance of EDA/DE-EIG is relatively competitive.

## V. CONCLUSIONS AND FUTURE WORK

DE/EDA [15] is a promising method that utilizes both the the global and local information for global optimization. However, the potential improvement of the performance of this algorithm has not been exploited furthermore. In this paper, an improved DE, DE-EIG, is imported to combine with EDA, bringing an impressive improvement on the performance. DEEIG is beneficial to utilize the statistics information of the population to accelerate the convergence. And expensive local search is applied to improve the performance further. The experimental results have shown the distinct advantages of the proposed method, named as EDA/DE-EIG, in comparison with two state-of-art algorithms JADE [25] and DE/EDA [15].

The results reported in this paper is preliminary and there are several ways to improve the algorithm performance. Firstly, the algorithm framework of EDA/DE-EIG can be simplified. Secondly, it is worth to investigate how to allocate the computational resources to both DE-EIG and EDA.

## ACKNOWLEDGEMENT

This work is supported by the National Natural Science Foundation of China under Grant No.61273313 and 61673180, and the Science and Technology Commission of Shanghai Municipality under Grant No.14DZ2260800.
