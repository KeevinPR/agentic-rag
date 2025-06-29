# Competition-Driven Dandelion Algorithms With Historical Information Feedback 

Shoufei Han ${ }^{\odot}$, Kun Zhu ${ }^{\odot}$, Member, IEEE, and MengChu Zhou ${ }^{\odot}$, Fellow, IEEE


#### Abstract

A Dandelion algorithm (DA) inspired by the seed dispersal process of dandelions has been proposed as a newly intelligent optimization algorithm. For improving its exploration ability as well as reducing the probability of its falling into a local optimum, this work proposes to add a novel competition mechanism with historical information feedback to current DA. Specifically, the fitness value of each dandelion in the next generation, which is calculated by linear prediction, is compared with the current best dandelion, and the loser is replaced by a new offspring. Current DA generates new offsprings without considering historical information. This work improves its offspring generation process by exploiting historical information with an estimation-of-distribution algorithm. Three historical information models are designed. They are best, worst, and hybrid historical information feedback models. The experimental results show that the proposed algorithms outperform DA and its variants, and the proposed algorithms are superior or competitive to nine participating algorithms benchmarked on 28 functions from CEC2013. Finally, the proposed algorithms demonstrate the effectiveness on four real-world problems, and the results indicate that the proposed algorithms have better performance than its peers.


Index Terms—Applications, competition mechanism, dandelion algorithm (DA), estimation-of-distribution algorithm (EDA), historical information, intelligent optimization, linear prediction, machine learning.

## I. INTRODUCTION

NOWADAYS, optimization problems are becoming more complex and difficult. Their aims are to find a set of parameter values that satisfy the constraints while optimizing their single or multiple performance indicators. Their solution

Manuscript received January 5, 2020; revised April 8, 2020; accepted July 13, 2020. Date of publication August 5, 2020; date of current version January 17, 2022. This work was supported in part by the National Natural Science Foundation of China under Grant 61701230; in part by the Natural Science Foundation of Jiangsu Province under Grant BK20170805; and in part by the Fundamental Research Funds for the Central Universities under Grant NE2018107. This article was recommended by Associate Editor M. K. Tiwari. (Corresponding authors: Kun Zhu; MengChu Zhou.)

Shoufei Han and Kun Zhu are with the College of Computer Science and Technology, Nanjing University of Aeronautics and Astronautics, Nanjing 210016, China, and also with the Collaborative Innovation Center of Novel Software Technology and Industrialization, Nanjing 211106, China (e-mail: hanshoufei@ gmail.com; zhukun@nuaa.edu.cn).

MengChu Zhou is with the Department of Electrical and Computer Engineering, New Jersey Institute of Technology, Newark, NJ 07102 USA, and also with the Institute of Systems Engineering and Collaborative Laboratory for Intelligent Science and Systems, Macau University of Science and Technology, Macau 999078, China (e-mail: zhou@njit.edu).

This article has supplementary material provided by the authors and color versions of one or more figures available at https://doi.org/10.1109/TSMC.2020.3010052.

Digital Object Identifier 10.1109/TSMC.2020.3010052
methods can be roughly divided into two categories: 1) exact methods and 2) intelligent optimization algorithms [1]. The former can get the optimal solution and always generates the same results for different runs under the same conditions. The latter often provides a near-optimal solution and tends to generate different solutions under the same conditions. For large-scale problems, the former is time-consuming and often impossible, while the latter can provide a satisfactory solution in a reasonable time. Therefore, many intelligent optimization algorithms have been proposed including genetic algorithm [2], differential evolution [3], cultural algorithm [4], particle swarm optimization (PSO) [5], ant colony optimization [6], artificial bee colony (ABC) [7], bat algorithm [8], grey wolf algorithm [9], harmony search [10], brain storm optimization [11], fireworks algorithm [12], and teaching-learning-based optimization (TLBO) [13]. These algorithms have been applied in many fields [14]-[17].

A dandelion algorithm (DA) [18] is recently proposed, which has been applied to optimize an extreme learning machine for biomedical classification problems. In DA, there are two types of dandelions, they are the best dandelion (BD) and assistant ones (ADs). The dandelions in different types have different seed dispersal ways. Due to the advantages, such as simplicity and efficiency, DA has attracted attentions of researchers, and some variants have been proposed [19], [20]. In [19], an improved DA is proposed (abbreviated as MDA), in which the convergence and parameters of DA are studied, and the mean position of all seeds is used to replace the Levy mutation. In [20], a variant of DA, i.e., a DA with probability-based mutation (DAPM), aiming to improve its mutation ability is proposed, in which three probability models are presented to switch among different mutations, and DAPM with three probability models is abbreviated as DAPML (linear), DAPMB (binomial), and DAPME (exponential), respectively.

Note that exploitation and exploration significantly impact the performance of intelligent optimization algorithms [21]. Excessive exploitation can easily lead them to local optima, while excessive exploration causes their difficulty to find the optimal solution. Cooperation could enhance their exploitation ability, and competition can improve their exploration ability. Thus, the phenomenon of cooperation ([5], [12], [22]), competition ([2], [9]) and their combination ([3], [23], [24]) often appear when designing such algorithms [25].

In this article, we design a novel competition mechanism for DA to enhance its exploration ability and reduce the probability of falling into local optima. This mechanism is based

on the linear prediction of fitness values. The predicted fitness value of a dandelion is compared with the best one, and a losing dandelion (loser) should be abandoned and replaced with a new offspring to avoid wasting resources on searching unpromising areas. Thus, how to generate its new offspring is an another important issue.
The generation of new offspring in a current DA ignores the historical information including historically best and worst dandelions, which contain rich information. In this article, we reuse such information to generate new offspring and propose three historical information feedback model-based DAs, which are best-historical-information-feedback-modelbased DA (BDA), worst-historical-information-feedback-model-based DA (WDA), and hybrid-historical-informationfeedback-model-based DA (HDA). In the proposed algorithms, we use the estimation-of-distribution algorithm (EDA) [26], instead of using traditional historical feedback methods, which tend to consume large memory, to estimate the distribution information of historical information and generate new offsprings.
The main contributions of this article are as follows.

1) A competition mechanism is proposed to improve the exploration ability of DA and to reduce the probability of DA to fall into its local optima.
2) Three historical information feedback models based on EDA are proposed to generate new offsprings, which are used to replace losers in the competition.
3) Our proposed algorithms are compared with DA's variants and other intelligent optimization algorithms on CEC2013 standard functions to show their superiority.
4) The proposed algorithms are applied to four real-world problems and the results show their superiority over other state-of-the-art methods.
The remainder of this article is organized as follows. Related studies about competition and information feedback in intelligent optimization algorithms are introduced in Section II. Section III introduces a framework and the operators of DA. Our proposed algorithms are presented and discussed in Section IV. Section V provides the mathematical analyses. Experimental and comparison results are given in Section VI. Section VII concludes this article.

## II. Related Work

## A. Competition Mechanisms in Intelligent Optimization

Competition mechanisms have been widely applied to design intelligent optimization algorithms. Genetic algorithm is one of the most popular ones [2]. Its selected individuals are directly inherited to the next generation via a competitive mechanism. The greedy selection is adopted in differential evolution [3]. The individual with the better fitness is retained, and the loser is abandoned. The selection strategy of fireworks algorithm always keeps the best fireworks into the next generation [12]. The competition mechanisms in these algorithms are due to a selection mechanism. Some other algorithms without a selection process adopt a competition mechanism. In PSO [5], choosing the $g$ Best and $p$ Best from particles may be viewed as a competition mechanism. In the grey wolf algorithm [9], the selection of $\alpha, \beta$, and $\delta$ wolves also involves
a competition mechanism. Different competition mechanisms are applied to different heuristic algorithms, but they have one thing in common: the best or better individual is selected.

In DA, a competition mechanism is triggered due to selection, i.e., BD in the population is always kept into the next generation. In this article, a novel competition mechanism is designed for DA to improve its exploration ability, which is different from the existing one of DA.

## B. Information Feedback in Intelligent Optimization

In recent years, team of scholars have exploited feedback information from various sources to improve the performance of intelligent optimization algorithms. Reusing valuable information to guide current and future search shows promising effects for them. In this section, related studies are briefly reviewed.

In the original ABC [7], the previous bee colony history information is not reused. Therefore, a bare bones ABC is proposed [27], which generates candidates by combining the Gaussian distribution and the best bee at the onlooker phase, and a neighborhood mechanism is introduced to enhance the search ability at the employed bee phase.

In order to make full use of the historical information of all particles in PSO, Li et al. [28] proposed a new composite PSO. Therein, EDA is first used to estimate and preserve the historical promising distribution information of particles to construct a historical information pool, which can generate new individuals to guide the evolution of PSO. A comprehensive learning PSO is proposed by using all other particles' historical best information [5], [29], which is the most popular algorithm among PSO variants.

TLBO is a promising intelligent optimization algorithm. In order to improve the convergence speed and accuracy, a novel TLBO is proposed by using empirical information to help learners judge learning behavior [30]. In addition, in order to improve the global performance of TLBO, Zou et al. [31] proposed an improved TLBO algorithm by using other learners' learning experience.

In order to make full use of the spark information generated by the fireworks algorithm at an explosion process, a novel guiding strategy is designed [32]. Therein, the sparks are sorted according to the fitness value, and then a guide vector is constructed by calculating the difference between the top ones and remaining sparks.

Wang et al. [33] proposed a variable neighborhood bat algorithm. Therein, a bat can be guide to search by its neighbors. In addition, Wang and Tan [1] presented a novel method to reuse the valuable information provided by previous individuals to guide future search.

Surrogate-assisted evolutionary algorithms (SAEAs) have been developed mainly for solving the optimization problems that have high cost in computing fitness values [34]. Their main idea is to replace expensive fitness evaluations with computationally cheap surrogate that can be constructed based on historical information [35]-[37].

Different from the previous studies, instead of simply reusing historical information, a competition mechanism is designed to judge whether historical information needs to be

reused, and only the losers in the competition need be guided by historical information. Meanwhile, in this article, three historical information feedback models are constructed and used to improve the performance of DA.

## III. OVERVIEW OF DA

For convenience to illustrate DA, we only consider the following minimization problem in this article:

$$
y=\min f(\mathbf{x})
$$

where $\mathbf{x}$ is a $D$-dimensional solution, and the objective is to find a suitable $\mathbf{x}$ such that $f(\mathbf{x})$ reaches its minimum.

Before introducing the rationale of DA, we need to explain some proper nouns, in order to help the reader better understand the technical details. The number of seeds represents the number of solutions; dispersal radius represents step size, i.e., search range; search space is the solution domain; and position stands for a solution.

Like other algorithms, DA can be divided into two phases: 1) initialization and 2) iterative optimization. In initialization, we generate dandelions in search space randomly as the initial population. Iterative optimization consists of normal seed dispersal, mutation seed dispersal, and selection, as introduced next.

## A. Normal Seed Dispersal

In normal seed dispersal, dandelions generate a certain number of seeds within dispersal radius. Thus, the number of seeds generated by each dandelion is calculated, and then the dispersal radius is computed. Finally, the process of generating normal seeds is given.

Consider $N$ dandelions in a $D$-dimensional search space. The $i$ th dandelion at generation $t$ has a current position $\mathbf{x}_{i}(t)=\left(x_{i}^{1}(t), \ldots, x_{i}^{d}(t), \ldots, x_{i}^{D}(t)\right)$. In DA, there are two types of dandelions: BD (the one with the minimum fitness) and ADs (other than the best one).

The number of the $i$ th dandelion seeds at the $t$-th generation is

$$
C_{i}(t)=\Phi\left(\hat{C} \times \frac{\hat{y}(t)-f\left(\mathbf{x}_{i}(t)\right)+\varepsilon}{\hat{y}(t)-\hat{y}(t)+\varepsilon}\right)
$$

where $C$ is the number of seeds, and $\hat{C}$ is the maximum number of seeds. The purpose of the function $\Phi()$ is to round a variable to its nearest integer, and $\hat{y}(t)$ and $\hat{y}(t)$ are the maximum and minimum fitness values at the $t$-th generation, respectively. $f\left(\mathbf{x}_{i}(t)\right)$ is the fitness value of the $i$ th dandelion at the $t$-th generation, and $\varepsilon$ is given to avoid a denominator of zero. Note that $C_{i}$ is set to $\hat{C}$ when $C_{i}<\hat{C}$, where $\hat{C}$ is the minimum number of seeds.

The dispersal radius of BD at the $t$-th generation is

$$
R_{B}(t)=\left\{\begin{array}{lr}
U-L, & t=1 \\
R_{B}(t-1) \times \gamma, & a=1 \\
R_{B}(t-1) \times v, & a \neq 1
\end{array}\right.
$$

where $U$ and $L$ are, respectively, the upper and lower bounds of the search space, while $\gamma$ and $v$ are two factors to control the enlargement and reduction of the radius. When $t=1$, the

```
Algorithm 1 Generating Normal Seeds for \(\mathbf{x}_{i}\)
Input: \(\mathbf{x}_{i}, C_{i}, R_{B}, R_{i}\)
Output: all \(\mathbf{s}_{i k}\)
    for \(k=1\) to \(C_{i}\) do
        for \(d=1\) to \(D\) do
            Randomly take a value for \(\theta\) in \((0,1)\)
            if \(\theta<0.5\) then
                Randomly take a value for \(\varphi\) in \((-1,1)\)
                if \(\mathbf{x}_{i}==\mathbf{x}_{B}\) then
                    \(\mathbf{s}_{i k}^{d}=\mathbf{x}_{i}^{d}+\varphi \cdot R_{B}\)
                else
                    \(\mathbf{s}_{i k}^{d}=\mathbf{x}_{i}^{d}+\varphi \cdot R_{i}\)
                    end if
                    if \(\mathbf{s}_{i k}^{d}\) out of bounds then
                        Randomly take a value for \(\mathbf{s}_{i k}^{d}\) in \([L, U]\)
                    end if
            else
                \(\mathbf{s}_{i k}^{d}=\mathbf{x}_{i}^{d}\)
            end if
        end for
end for
```

dispersal radius is initialized to the diameter of the search space. Parameter $a$ is defined as

$$
a=\frac{\hat{y}(t)+\varepsilon}{\hat{y}(t-1)+\varepsilon}
$$

where $\hat{y}(t)$ and $\hat{y}(t-1)$ are the minimum fitness value in generation $t$ and $t-1$, respectively. When $a=1$, i.e., $\hat{y}(t)=\hat{y}(t-1)$, which means a better solution is not found in generation $t$. In contrast, $a \neq 1$ means that $\hat{y}(t) \neq \hat{y}(t-1)$, i.e., a better solution is found in generation $t$.

The dispersal radius of the $i$ th dandelion belonging to ADs at the $t$-th generation is

$$
R_{i}(t)=\left\{\begin{array}{lr}
U-L, & t=1 \\
\omega \times R_{i}(t-1)+\left(\left\|\mathbf{x}_{B}\right\|_{\infty}-\left\|\mathbf{x}_{i}\right\|_{\infty}\right), & \text { otherwise }
\end{array}\right.
$$

where $\mathbf{x}_{B}$ is the position of BD , and $\omega$ is the weight factor, which is designed to control the effect of the dispersal radii between the previous and current generations dynamically. It is calculated as

$$
\omega=1-\frac{F_{E}(t)}{F_{M}}
$$

where $F_{E}(t)$ is the number of function evaluations at generation $t$, and $F_{M}$ is the maximum number of function evaluations.

Algorithm 1 shows how the seeds are generated for each dandelion. Therein, some dimensions are chosen to update their positions based on dispersal radius (lines 5-10); while others remain unchanged (line 15). Meanwhile, note that position updates of BD and ADs are different (lines 7 and 9) due to different dispersal radii.

## B. Mutation Seed Dispersal

To help jump out of local optima, Levy mutation is selected to update the position of BD , and this process is called

```
Algorithm 2 Generating Mutation Seeds for \(B D\)
Input: \(z, \mathbf{x}_{B}\)
Output: all \(\mathbf{m}_{j}\)
    for \(j=1\) to \(z\) do
        for \(d=1\) to \(D\) do
            Randomly take a value for \(\theta\) in \((0,1)\)
            if \(\theta<0.5\) then
                \(\mathbf{m}_{j}^{d}=\mathbf{x}_{B}^{d} \cdot(1+\operatorname{Levy}())\)
                if \(\mathbf{m}_{j}^{d}\) out of bounds then
                    Randomly take a value for \(\mathbf{m}_{j}^{d}\) in \([L, U]\)
                    end if
            else
                \(\mathbf{m}_{j}^{d}=\mathbf{x}_{B}^{d}\)
            end if
        end for
    end for
```

mutation seed dispersal, i.e.,

$$
\mathbf{m}=\mathbf{x}_{B} \cdot(1+\operatorname{Levy}())
$$

where $\mathbf{m}$ is the position of a mutation seed, and $\operatorname{Levy}()$ is a random number following Levy distribution.

Algorithm 2 shows the process to generate the mutation seeds for BD, where $z$ is the number of mutation seeds. Therein, same as Algorithm 1, some dimensions are chosen to update their positions based on Levy mutation (line 5); while others remain unchanged (line 10). Note that mutation seed dispersal is only for BD but not for ADs.

## C. Selection

In this article, in order to implement a fair competition, we design a new selection strategy based on a greedy strategy. Its core idea is that a dandelion and its own seeds are considered as a single population and greedily select the best individual in the population into the next generation

$$
\mathbf{x}_{i}(t+1)=\left\{\begin{array}{ll}
\arg \min \left\{f\left(\mathbf{x}_{i}(t)\right), f\left(\mathbf{s}_{i k}\right), f\left(\mathbf{m}_{j}\right)\right\}, & \mathbf{x}_{i}=\mathbf{x}_{B} \\
\arg \min \left\{f\left(\mathbf{x}_{i}(t)\right), f\left(\mathbf{s}_{i k}\right)\right\}, & \text { otherwise }
\end{array}\right.
$$

where $f\left(\mathbf{s}_{i k}\right)$ is the fitness values of normal seeds generated by the $i$ th dandelion, and $f\left(\mathbf{m}_{j}\right)$ is the fitness values of mutation seeds generated by BD.

Algorithm 3 summarizes the framework of DA. Therein, $N$ dandelions are generated randomly in search space as initial population (line 1), and then each dandelion generates its normal seeds by Algorithm 1 (line 4), while BD is selected to generate the mutation seeds by Algorithm 2 (line 5). Finally, selecting $N$ dandelions into the next generation from all dandelions (dandelions, normal seeds and mutation seeds) via a selection strategy. BD is returned when the termination condition is satisfied.

## IV. PROPOSED AlGORITHMS

In this section, we introduce the proposed algorithms in detail. First, a novel competition mechanism is designed, and then three historical information feedback models are proposed

## Algorithm 3 Framework of DA

## Input: $N$

Output: Best dandelion
: Randomly generating $N$ dandelions as initial population
Assess $N$ dandelions' fitness
while a termination condition is not satisfied do
Generating normal seeds according to Algorithm 1
Generating mutation seeds according to Algorithm 2
Assess the fitness of all seeds
Select $N$ dandelions into the next generation via a selection strategy
end while
based on EDA. Finally, we give a complete framework of the proposed algorithms.

## A. Competition Mechanism

In this article, our competition mechanism is designed based on fitness values, and if the fitness value of a dandelion in the next generation, which can be predicted by evolutionary speed $e$, is not better than that of the current BD , it is considered as a loser and then is replaced. Define $e$ in generation $t$ as

$$
\begin{aligned}
\tilde{f}(t-1) & =\frac{1}{N} \sum_{i=1}^{N} f\left(\mathbf{x}_{i}(t-1)\right) \\
e(t) & =\tilde{f}(t-1)-\hat{y}(t)
\end{aligned}
$$

where $\tilde{f}(t-1)$ is the average fitness value of dandelions in generation $t-1$ and $\hat{y}(t)$ is the minimum fitness value of dandelions in generation $t . e$ is the difference between $\tilde{f}(t-1)$ and $\hat{y}(t)$ reflecting how fast dandelions evolve.

From (10), if $e$ is large, which means that DA evolve quickly, few dandelions are the losers. It becomes smaller when the algorithm falls into a local or global optimum.

However, how to estimate the fitness value of dandelions in generation $t+1$ is a challenge. To address this, we introduce a simple linear model to predict the fitness value based on the fitness values in generation $t$ and $e$. It is designed as follows:

$$
\tilde{f}\left(\mathbf{x}_{i}(t+1)\right)=f\left({ }_{i}(t)\right)-e \times \delta
$$

where $\delta$ is the learning rate, and its detailed empirical analysis is given in Section VI-B.

For each dandelion $\mathbf{x}_{i}$, the approximate fitness value in the next generation could be calculated according to (11). The framework to realize the above competition mechanism is shown in Algorithm 4.

In Algorithm 4, line 2 is a trigger condition to use the proposed competition mechanism, which means that the mechanism is triggered if a better solution is found. On the contrary, if a better solution is not found, the mechanism should not be triggered because all dandelions are losers. Furthermore, in DA evolution, the above situation often occurs when a better solution cannot be found, thus indicating that the losers are often replaced if a trigger condition is deleted, and DA loses its current potential area. Thus, a trigger condition is necessary for starting a competition mechanism.

## Algorithm 4 Competition Mechanism

Input: $N$ ( $N$ is the number of dandelion)
Output: the position and the fitness of losers
for $i=1$ to $N$ do
if $\frac{\hat{y}(t)}{\hat{y}(t-1)} \neq 1$ then
$\tilde{f}(t-1)=\frac{1}{N} \sum_{i=1}^{N} f\left(\mathbf{x}_{i}(t-1)\right)$
$e=\tilde{f}(t-1)-\hat{y}(t)$
if $f\left(\mathbf{x}_{i}(t)\right)-e \times \delta>\hat{y}(t)$ then
$\mathbf{x}_{i}(t)$ is the loser
end if
end if
end for

Lines 3 and 4 calculate the evolutionary speed $e$. Instead of using average fitness value, if the maximum fitness value is used, $e$ would be larger, and $f\left(\mathbf{x}_{i}(t)\right)-e \times \delta$ would be small, which means that there are few losers to be replaced and it is more difficult to jump out of a local optimum. Similarly, if using the minimum fitness value, $e$ is small, and $f\left(\mathbf{x}_{i}(t)\right)-e \times \delta$ would be large, which means that there are many losers to be replaced and DA may lose its current promising area.

Line 5 is to determine whether a dandelion is a loser. Given $e$ and $\delta$, if the condition of line 5 is satisfied, it is considered a loser. In the following, the effectiveness of the proposed competition mechanism is illustrated by comparing the resulting DA with a single-population DA.

For example, there is a function to be optimized, and assume it has $p$ local optima and one global optimum. For singlepopulation DA, the probability of finding the global optimum with $q$ trials is calculated as follows:

$$
\begin{aligned}
P_{s p} & =\frac{p-1}{p} \cdot \frac{p-1}{p} \cdots \cdot \frac{p-1}{p} \cdot \frac{1}{p} \\
& =\left(\frac{p-1}{p}\right)^{q-1} \cdot \frac{1}{p}
\end{aligned}
$$

With the proposed competition mechanism in multipopulation DA, the probability of falling into the same local optima is reduced, and the probability of finding the global optimum with $q$ trials increases, i.e.,

$$
\begin{aligned}
P_{c s} & =\frac{p-1}{p} \cdot \frac{p-2}{p-1} \cdots \cdot \frac{p-q+1}{p-q+2} \cdot \frac{1}{p-q+1} \\
& =\frac{1}{p}
\end{aligned}
$$

From (12) and (13), we conclude that the probability of finding the global optimum $P_{c s}>P_{s p}$ when the number of trials $q>1$. It indicates that the proposed mechanism is effective for jumping out of a local optimum.

Line 6 is to replace the loser with a new offspring generated by a historical information feedback model. Here, we must consider the following case: if a loser is not replaced, it may be BD in the next generation, and if it is replaced, it is harmful to the search process.

But we find that the following conditional probability is low:

$$
P\left(\mathbf{x}_{i}(t+1) \text { is } \mathrm{BD} \mid \mathbf{x}_{i}(t) \text { is a loser }\right)
$$

![img-0.jpeg](img-0.jpeg)
(a)
![img-1.jpeg](img-1.jpeg)
(b)

Fig. 1. Trend of dispersal radius $R$ of BD on test functions (a) $f 1$ and (b) $f 23$ from CEC2013 in Table I.
where $\mathbf{x}_{i}(t)$ is the loser in generation $t$. The reasons are as follows: 1) DA does not have an improvement in every generation, so that the condition in line 2 is not always triggered and 2) in DA, the dispersal radius of BD is dynamically changing, whose trend is shown in Fig. 1, where the differences between Fig. 1(a) and (b) are that the trends of dispersal radius are different on different functions, numbers on the horizontal and vertical axes represent iteration count, and logarithm of dispersal radius, respectively. From Fig. 1(a), it can be seen that the overall trend of the radius is decreasing, and the speed of decline is faster in the later stage than that in the early stage. From Fig. 1(b), it can be observed that the radius drops slowly in the early stage, but the speed of decline has accelerated when iteration count is between 1500 and 2000. Overall, the radius has a clear downward trend in a whole process, and the number of drops is significantly more than the number of rises, which means that the current BD is also a BD in the next generation in most cases. Thus, the probability of $\mathbf{x}_{i}(t+1)$ being BD is low, and thus the above conditional probability is also low.

Unavoidably, losers may also be wrongly replaced, and this case is considered to be acceptable because BD is always retained in every generation. On the other hand, the proposed competition mechanism is effective because the losers are directly replaced without wasting resources, i.e., fitness evaluations. Meanwhile, the replacements can search in (disperse into) an unknown area, which enhances the exploration of DA.

## B. Historical Information Feedback Models

In an evolutionary process of DA, historical information may be reused to guide its search process. If all historical information of a particular individual, i.e., BDs, is kept, it needs large memory space. In order to solve this problem, EDA is used to model the distribution of historical information. Here, we only consider the historical information of the best and worst dandelions. In the following, EDA is first introduced to construct a distribution model and generate new offsprings, and then three historical information feedback models are proposed.

1) Construct Distribution Model and Generate New Offsprings: We assume that there are $H$ historical records of the best or worst dandelions. We use EDA to estimate the distribution of $H$ records. For each dandelion $\mathbf{x}_{i}$, a distribution of $x_{i}^{d}$ follows a Gaussian distribution is assumed, the reasons are as follows: 1) Gaussian distribution is used in this article

```
Algorithm 5 Constructing a Distribution Model and
Generating a New Offspring
Input: \(H_{M}\), BD
Output: \(\widetilde{\mathbf{x}}_{B}=\left(x^{1}, x^{2}, \ldots, x^{D}\right)\)
    Calculate the number of current historical records: \(L\)
    if \(L<H_{M}\) then
        Add BD into historical records
    else
        Replace the worst individual with BD
    end if
    for \(d=1\) to \(D\) do
        Calculate the mean: \(\mu_{d}\)
        Calculate the standard deviation: \(\sigma_{d}\)
        Generate new dimension \(x^{d}\) by following \(\mathcal{N}\left(\mu_{d}, \sigma_{d}\right)\)
    end for
```

following the suggestions in [28] and [38], in which it is used in EDA to generate new individuals and 2) the new individuals generated by the Gaussian distribution is closer to the mean of samples with a large probability, and thus the new individuals can well simulate the characteristics of the samples. In the Gaussian distribution, the mean and standard deviation need be determined as

$$
\begin{aligned}
& \mu_{d}=\frac{1}{H} \sum_{i=1}^{H} x_{i}^{d} \\
& \sigma_{d}=\sqrt{\frac{1}{H} \sum_{i=1}^{H}\left(x_{i}^{d}-\mu_{d}\right)^{2}}
\end{aligned}
$$

where $\mu_{d}$ and $\sigma_{d}$ are the mean and standard deviation of the $d$ th attribute of historical information of the best or worst dandelions. Once $\mu_{d}$ and $\sigma_{d}$ are determined, the $d$ th attribute of a new offspring is generated which follows the Gaussian distribution $\mathcal{N}\left(\mu_{d}, \sigma_{d}\right)$. Taking the historical information of the BD as an example, the process of constructing a distribution model and generating new offsprings is shown in Algorithm 5, where $H_{M}$ is the maximum number of historical records. In Algorithm 5, a distribution model is first constructed, and then a new offspring is generated. Note that for the historical information of the worst dandelion, the process of constructing its distribution model and generating a new offspring is same as the construction process for BD. The only changes are that the input is replaced by the worst dandelion in the current generation.
2) Three Historical Information Feedback Models: Based on the new offspring generated by EDA, historical information feedback models can be built. In this section, we present best historical information feedback model (BM), worst one (WM), and hybrid one (HM).
a) Best historical information feedback model: The one stores the probability model that characterizes the historically BDs, and then the new offspring $\widetilde{\mathbf{x}}_{B}$ is generated. Based on $\widetilde{\mathbf{x}}_{B}$, the replacement of a loser can be defined as follows:

$$
\widetilde{\mathbf{x}}_{B}=L+U-\widetilde{\mathbf{x}}_{B}
$$

In (16), we use the opposite solution of $\widetilde{\mathbf{x}}_{B}$ to replace the loser instead of using $\widetilde{\mathbf{x}}_{B}$. There are two reasons: the first is
that $\widetilde{\mathbf{x}}_{B}$ has the same distribution as the selected BD , and if $\widetilde{\mathbf{x}}_{B}$ is used to replace a loser, it may repeat BDs' previous search process. Using its opposite solution can avoid this situation. Second, an opposite solution has $50 \%$ chance of finding a better solution, which can help DA find a better search area.
b) Worst historical information feedback model: The one stores the probability model that characterizes the historically worst dandelions, and then the new offspring $\widetilde{\mathbf{x}}_{W}$ is generated. Based on $\widetilde{\mathbf{x}}_{W}$, the replacement of a loser can be defined as follows:

$$
\widetilde{\mathbf{x}}_{W}=L+U-\widetilde{\mathbf{x}}_{W}
$$

Similar to the above, this model uses the opposite solution to replace a loser.
c) Hybrid historical information feedback model: This one is the combination of the prior two models, we have

$$
\widetilde{\mathbf{x}}_{H}=\alpha_{B} \cdot \widetilde{\mathbf{x}}_{B}+\alpha_{W} \cdot\left(L+U-\widetilde{\mathbf{x}}_{W}\right)
$$

where $\alpha_{B}$ and $\alpha_{W}$ are the weighting factors, defined as follows:

$$
\begin{aligned}
\alpha_{B} & =\frac{\left|f\left(\widetilde{\mathbf{x}}_{B}\right)\right|}{\left|f\left(\widetilde{\mathbf{x}}_{B}\right)\right|+\left|f\left(\widetilde{\mathbf{x}}_{W}\right)\right|} \\
\alpha_{W} & =\frac{\left|f\left(\widetilde{\mathbf{x}}_{W}\right)\right|}{\left|f\left(\widetilde{\mathbf{x}}_{B}\right)\right|+\left|f\left(\widetilde{\mathbf{x}}_{W}\right)\right|}
\end{aligned}
$$

where $\left|f\left(\widetilde{\mathbf{x}}_{B}\right)\right|$ and $\left|f\left(\widetilde{\mathbf{x}}_{W}\right)\right|$ are the absolute value of fitness of $\widetilde{\mathbf{x}}_{B}$ and $\widetilde{\mathbf{x}}_{W}$, respectively. The following outlines a theoretical analysis to show the effectiveness of replacing a loser with $\widetilde{\mathbf{x}}_{H}$.

Consider function $f=x^{2}$. Assume that $x^{d}$ is the value of an attribute of $f$, and $R$ is the dispersal radius. Then $x^{d}$ takes a value in $[-R, R]$ randomly. The following theorem presents the error bound of irrelevant directions.

Theorem 1: If $x^{d}$ follows a uniform distribution $\mathcal{U}(-R, R)$, and $\widetilde{x}_{H}$ is generated by (18). For any $D \neq 1$, with probability at least $1-p$, the error bound of irrelevant directions can be obtained as

$$
\left|\widetilde{x}_{H}^{d}\right| \leq \sqrt{\frac{R^{2}}{3 p}}
$$

Proof: Since $x^{d} \sim \mathcal{U}(-R, R)$, so $\widetilde{x}_{H}^{d} \sim \mathcal{U}(-R, R)$. Then, the expectation of $\widetilde{x}_{H}^{d}$ is

$$
E\left(\widetilde{x}_{H}^{d}\right)=0
$$

The variance is

$$
D\left(\widetilde{x}_{H}^{d}\right)=E\left(\left(\widetilde{x}_{H}^{d}\right)^{2}\right)+E\left(\widetilde{x}_{H}^{d}\right)^{2}
$$

Since $E\left(\widetilde{x}_{H}^{d}\right)^{2}=0$, we have

$$
\begin{aligned}
D\left(\widetilde{x}_{H}^{d}\right) & =E\left(\left(\widetilde{x}_{H}^{d}\right)^{2}\right) \\
& =\int_{-R}^{R}\left(\widetilde{x}_{H}^{d}\right)^{2} \frac{1}{2 R} d \widetilde{x}_{H}^{d} \\
& =\frac{1}{2 R} \int_{-R}^{R}\left(\widetilde{x}_{H}^{d}\right)^{2} d \widetilde{x}_{H}^{d} \\
& =\frac{1}{2 R} \frac{\left(\widetilde{x}_{H}^{d}\right)^{3}}{3} \int_{-R}^{R} \\
& =\frac{1}{2 R} \frac{R^{3}+R^{3}}{3}=\frac{R^{2}}{3}
\end{aligned}
$$

where $(1 / 2 R)$ is the probability density function for $\widetilde{x}_{H}^{d}$.

## Algorithm 6 Framework of the Proposed Algorithms

Input: $N$
Output: Best dandelion
Randomly generating $N$ dandelions
Assess the fitness of dandelions
while a termination condition is not satisfied do
Generating normal seeds by Alg. 1
Generating mutation seeds by Alg. 2
Assess the fitness of all seeds
Select $N$ dandelions via selection strategy
Dandelions compete with each other by Alg. 4
Construct a distribution model and generate a new offspring by Alg. 5
Built BM, WM or HM by the new offspring
Replace the loser with BM, WM or HM
end while

By the Chebyshev's theorem, for any $\varepsilon>0$, we have

$$
P\left\{\left|\frac{\gamma_{i d}^{d}}{2_{H}^{d}}-0\right| \geq \varepsilon\right\} \leq \frac{R^{2}}{3 \varepsilon^{2}}
$$

Thus, we take the probability getting error bound of irrelevant directions $p=\left(R^{2} / 3 \varepsilon^{2}\right)$. Then (21) holds.

In DA, dispersal radius $R$ is dynamically changing. However, we find that $R$ is becoming smaller in its process of evolution. Thus, the error bound of irrelevant directions and $p$ are becoming smaller. It can be concluded that the proposed HM can get smaller error bound of irrelevant directions with higher probability $(1-p)$.
3) Framework of Proposed Algorithms: The complete framework is shown in Algorithm 6. At initialization, $N$ dandelions are generated randomly in search space. During optimization, normal seeds and mutation ones are generated by Algorithms 1 and 2. $N$ dandelions are then selected from the whole population via our selection strategy. Finally, if there are losers among $N$ dandelions, they are replaced with the new offspring generated by one of three models.

In the framework of the proposed algorithms, lines 1 and 2 are the initialization phase and require $N$ function evaluations. The number of normal and mutation seeds are assumed to be $C$ and $z$, respectively. Thus, lines 4 and 5 require $C+M$ function evaluations. In Algorithm 4, the replacements of the best, worst, and hybrid historical information feedback models need to be evaluated once, once, and three times, respectively. In summary, if the maximum number of generations is set to $T$, the computational complexity of BDA, WDA, and HDA are $O(N+T(C+z+1)), O(N+T(C+z+1))$, and $O(N+T(C+z+3))$, respectively.

## V. MATHEMATICAL ANALYSES

The following outlines a mathematical analysis for the convergence of the proposed algorithms. We first recall a result for convergence of basic DA from [19], and then prove the convergence of the proposed algorithms.

Theorem 2: DA can converge to a local or global optimal solution with enough function evaluations.

Theorem 2 has been proved in [19], which indicates that as long as DA search within a given range, i.e., $[L, U]$, it can obtain a local or global optimal solution with enough function evaluations. Thus, we only need to prove that the replacements generated by BDA, WDA, and HDA are in $[L, U]$.

Theorem 3: The new offsprings generated by BDA, WDA, or HDA are in $[L, U]$.

Proof:

1) $B D A$ : Here, $\widetilde{\mathbf{x}}_{\bar{B}}$ is a new offspring generated by BDA. So $L \leq \widetilde{\mathbf{x}}_{B} \leq U$. If $\widetilde{\mathbf{x}}_{B}$ takes $U$

$$
\begin{aligned}
\widetilde{\mathbf{x}}_{\bar{B}} & =L+U-\widetilde{\mathbf{x}}_{B} \\
& \geq L+U-U=L
\end{aligned}
$$

Meanwhile, if $\widetilde{\mathbf{x}}_{B}$ takes $L$

$$
\begin{aligned}
\widetilde{\mathbf{x}}_{\bar{B}} & =L+U-\widetilde{\mathbf{x}}_{B} \\
& \leq L+U-L=U
\end{aligned}
$$

From (26) and (27), we have

$$
L \leq \widetilde{\mathbf{x}}_{\bar{B}}=L+U-\widetilde{\mathbf{x}}_{B} \leq U
$$

Thus, $\widetilde{\mathbf{x}}_{\bar{B}}$ falls in $[L, U]$.
2) $W D A$ : The proof is similar to BDA. We have

$$
L \leq \widetilde{\mathbf{x}}_{\bar{B}^{\prime}}=L+U-\widetilde{\mathbf{x}}_{W} \leq U
$$

3) $H D A$ : Since $L \leq \widetilde{\mathbf{x}}_{B} \leq U$ and $L \leq L+U-\widetilde{\mathbf{x}}_{W} \leq U$, then we have $\alpha_{B} \cdot L \leq \alpha_{B} \cdot \widetilde{\mathbf{x}}_{B} \leq \alpha_{B} \cdot U$ and $\alpha_{W} \cdot L \leq \alpha_{W} \cdot(L+U-$ $\left.\widetilde{\mathbf{x}}_{W}\right) \leq \alpha_{W} \cdot U$. Thus, we can get

$$
\begin{aligned}
\left(\alpha_{B}+\alpha_{W}\right) \cdot L & \leq \widetilde{\mathbf{x}}_{H}=\alpha_{B} \cdot \widetilde{\mathbf{x}}_{B}+\alpha_{W} \cdot\left(L+U-\widetilde{\mathbf{x}}_{W}\right) \\
& \leq\left(\alpha_{B}+\alpha_{W}\right) \cdot U
\end{aligned}
$$

Since $\alpha_{B}+\alpha_{W}=1$, we have

$$
L \leq \widetilde{\mathbf{x}}_{H}=\alpha_{B} \cdot \widetilde{\mathbf{x}}_{B}+\alpha_{W} \cdot\left(L+U-\widetilde{\mathbf{x}}_{W}\right) \leq U
$$

Thus, $\widetilde{\mathbf{x}}_{H}$ falls in $[L, U]$.
In sum, the new offsprings of the proposed algorithms fall in $[L, U]$.

Theorem 4: The proposed algorithms can converge to a local or global optimal solution with enough function evaluations

Proof: In the proposed algorithms, the normal and mutation seeds must be in the range $[L, U]$ due to cross-border handling, and the new offsprings are also in the range based on Theorem 3.

From the above analysis, we can conclude that the proposed algorithms can obtain a local or global optimal solution with enough function evaluations at all times based on Theorem 2.

## VI. EXPERIMENTS AND RESULT ANALYSES

## A. Benchmark Functions and Parameters Settings

Twenty eight benchmark functions are selected from CEC2013 [39], as shown in Table I, where $f 1-f 5$ are unimodal, $f 6-f 20$ are multimodal, and $f 21-f 28$ are composed functions, to verify the performance of the proposed algorithms. "Accept" represents an acceptable solution, which is found by an algorithm and its mean error falls in the range. For a fair comparison, the number of fitness evaluations of

TABLE I
28 BENCHMARK FUNCTIONS FROM CEC2013

each compared algorithm is set to $3 \times 10^{5}$, and each comparison is repeated 51 times to reduce statistical errors. The dimension of each test function is set to 30 . The parameters of all compared algorithms are set to be same as their corresponding references, and parameters of the improved DAs follow the suggestion in [18] with $H_{M}=40$.

## B. Sensitivity to Learning Rate

In this section, we study the impact of learning rate $\delta$ of Algorithm 4 on the proposed algorithms' performance. Set $\delta$ to $0.1,0.3,0.5,1,2,10,20,50,70,100$, and 150 for each proposed algorithm. In order to compare the performance of $\delta$ taking different values, a set of pairwise Wilcoxon rank-sum tests is used to show if $\delta$ taking a value significantly better than taking other values. Meanwhile, we define that if a method performs significantly better than another one on a certain test function, it receives one point. Thus, the maximum total score (the total number of received points) for an algorithm with $\delta$ taking a specific value is $28 \times(11-1)=280$. The results with different $\delta$ values are shown in Fig. 2. We conclude that when $\delta=50$, BDA has better performance, $\delta=70$ is suitable for WDA, and HDA reaches its best with $\delta=100$. Thus, $\delta$ is set to 50,70 , and 100 for them in the following experiments, respectively.

## C. Efficiency of Our Competition Mechanism

In this section, we need to answer the following question: Why is the average fitness chosen instead of the minimum or maximum fitness in Algorithm 4?
![img-2.jpeg](img-2.jpeg)

Fig. 2. Total scores of (a) BDA, (b) WDA, and (c) HDA taking different learning rates.

In the following, we take BDA as an example to answer the above question, with the minimum fitness we denote it as BDAm, and with the maximum fitness as BDAM. The detail results of WDA and HDA are given in Table S1 and S2 of the supplementary file.

The mean errors are presented in Table II, and the smallest mean error is marked bold. The Wilcoxon rank-sum tests

TABLE II
CompAriSON Among BDAM, BDAM, and BDA


between BDA and BDAm/BDAM are conducted. In Table II, " 1 " indicates that BDA performs significantly better than a compared algorithm, " -1 " indicates otherwise, and " 0 " means no significant difference between them.

From Table II, BDAm only has the best performance on function $f 1$ and $f 2$, BDAM performs the best on function $f 5, f 7, f 13$, and $f 20$, and BDA performs best on all the other functions. Judging from the average rankings, BDA has the best average ranking, which means that BDA has better performance than BDAm and BDAM on most test functions.

In the pairwise comparisons, the results achieved by BDA are significantly better than those by BDAm and BDAM, which proves that choosing the average in line 3 of Algorithm 4 is the best.

## D. Efficiency of Information Feedback Models

The proposed algorithms use a solution from three information feedback models to replace a loser in the competition. In order to verify the effectiveness of using these models, we need to answer the following two questions.

1) Do the proposed algorithms perform better than DA with our proposed selection in Section III-C, denoted as DAS?
2) Do the proposed algorithms perform better than DA with a random replacement mechanism, denoted as DAR?
In DAR, if a dandelion is a loser, it is replaced with an individual randomly generated in the feasible domain. For a fair comparison, the learning rate is set to 50,70 , and 100
for DAR (abbreviated as $\mathrm{DAR}_{50}, \mathrm{DAR}_{70}$, and $\mathrm{DAR}_{100}$ ). The mean errors and standard deviations are shown in Table III. The smallest mean error of each function and the best average ranking are marked bold. The results achieved by pairwise Wilcoxon rank-sum tests between the proposed algorithms and DAS/DAR are shown in the bottom of Table III, in which " + " indicates that the proposed algorithms perform significantly better than the compared algorithm, and " - " indicates otherwise.

From Table III, DAS, DAR $_{50}$, DAR $_{70}$, and DAR $_{100}$ perform well on $f 1, f 20, f 5$, and $f 7$, respectively, and they perform poorly on other functions. The results of the proposed ones are comparable. It can be seen that their average rankings are better than DAS and DARs. Judging from the average rankings, HDA is the best and $\mathrm{DAR}_{70}$ is the worst, and BDA and WDA are the second and third places, respectively. The results of pairwise Wilcoxon rank-sum tests indicate that the proposed algorithms are significantly better than DAS and DARs. We can conclude that the proposed information feedback models are more effective than a random replacement mechanism.

## E. Comparison With DA and Its Variants

In this section, the proposed algorithms are compared with DA and its variants [19], [20]. Note that the super parameter $p$ of DAPML, DAPMB, and DAPME is, respectively, set to $0.5,0.5$, and 0.1 according to [20]. The mean errors and the ranking on each function are shown in Table IV. The average rankings are presented at its bottom.

From Table IV, it is easy to find that DA performs poorly, and its average ranking is also the worst. Its variants have better results on $f 1-f 5$ except $f 3$, but perform poorly on other functions. BDA, WDA, and HDA have the best results on 8, 5 , and 10 functions, respectively. It means that the proposed algorithms have better performance than DA and its variants on $f 6-f 28$ except $f 20$. Judging from the average rankings, HDA ranks the first on the 28 test functions with the average ranking of 2.57 . BDA and WDA take the second and third place. The results of the proposed algorithms are comparable.

The results achieved by pairwise Wilcoxon rank-sum tests between the proposed algorithms and their peers are shown in the bottom of Table IV, in which " + " indicates that the proposed algorithms statistically outperform its peers, " - " indicates otherwise, and " $=$ " indicates no significant difference between them. It can be seen that the proposed algorithms outperform DA and its variants significantly. Moreover, their convergence curves are shown in Fig. S1 of the supplementary file.

The convergence time of these eight algorithms is compared. We define an algorithm that has converged when an acceptable solution (defined in Table I) is found. All compared algorithms are run in MATLAB (R2018a) on a PC with Windows 7 operating system ( 64 bit) and 4-GB RAM. The results of convergence time are shown in Table V, where the best total and average convergence time are marked in bold. From Table V, it can be seen that the convergence time of DAPML, DAPMB, and DAPME is comparable. MDA is the worst among them. BDA, WDA, and HDA are better than

TABLE III
Comparison of DAS, DAR $_{50}$, DAR $_{70}$, DAR $_{100}$, BDA, WDA, and HDA


TABLE IV
COMPARISON OF THE PROPOSED ALGORITHMS WITH DA AND ITS VARIANTS


others, and HDA is the best. Finally, our proposed algorithms have the least convergence time on these functions among all algorithms.

## F. Comparison With Competitors

To further study their performance, the proposed algorithms are compared with eight optimizers participating
in the CEC2013 competitions. The results of optimizers used in the comparison are taken from the original articles. The competitors are ABC [7], Standard PSO 2011 (SPSO) [40], A hybrid PSO and ABC (PSOABC) [41], genetic algorithm with three-parent crossover (GATC) [42], population's variance-based adaptive differential evolution (PVADE) [43], differential evolution with automatic parameter configuration (DEAPC) [44], continuous differential

TABLE V
Comparison of Convergence Time, Where "Sum" and "Avg" Indicate That Total and Average Convergence Time for All Functions


TABLE VI
Mean Values of 12 Algorithms on Test Functions

ant-stigmergy algorithm (CDAA) [45], restart covariancematrix-adaptation evolution strategy with increasing population size (RCES) [46], and parameter-less evolutionary search (PLES) [47]. The mean values of these 12 algorithms with $D=30$ are shown in Table VI. The best mean value on each function is highlighted. "AR1" and "AR2" indicate the average rankings on $f 1-f 20$ and $f 21-f 28$ (composed functions), respectively.

From Table VI, it can be seen that BDA and HDA achieves the better performance on $f 21-f 28$ (AR2 is the top rank), the
best results on $f 1-f 20$ are obtained by RCES (AR1 is the top rank). ABC performs the best on nine functions, but it has bad performance on other functions. WDA ranks the second on $f 21-f 28$ with AR2 of 4.50 . Moreover, according to the pairwise Wilcoxon rank-sum tests, BDA, WDA, and HDA are significantly better than ABC, SPSO, PSOABC, GATC, PVADE, DEAPC, CDAA, and PLES. In comparison with RCES, they provide better results in eight cases, comparable results in three cases. In the rest of the test functions, they have worse results than it. It indicates that the proposed algorithms

TABLE VII
Comparison of Nine Algorithms on Real-World Problems

are superior or competitive to nine participating algorithms benchmarked on 30-D CEC2013 benchmark functions.

## G. Comparison on Real-World Problems

Four real-world problems are selected from CEC2011 [48] to validate the performance of our proposed algorithms in applications. They are parameter estimation for frequencymodulated sound waves (FMSW), Lennard-Jones potential (LJP), optimal control of a nonlinear stirred tank reactor (NLSTR), and spread spectrum radar polyphase code design (SSRPCD) problems. RCES (its performance is the best in the above comparison), DA and its variants are selected for comparison. Their parameters are the same as the above, and $F_{M}=$ $1.5 \times 10^{5}$. The results of maximum fitness (Max), minimum fitness (Min), mean fitness (Mean), and standard deviation (Std) after 25 independent runs are shown in Table VII, and the best mean fitness and average ranking values are in a boldface.

RCES has the best performance on SSRPCD due to a restart mechanism, but performs poorly on other three problems. HDA achieves the better performance on FMSW. BDA is the best on LJP and NLSTR. The results of our proposed algorithms are comparable. BDA ranks the first on these problems, HDA takes the second place, and followed by WDA. The outstanding results on these problems prove the superiority of the proposed algorithms over its compared algorithms and indicate that our proposed competition mechanism is a more promising methodology than a restart one.

## VII. CONCLUSION

In this article, a competition-driven DA has been proposed, in which dandelions compete with each other, and losers are abandoned and replaced by new offsprings. Three historical information feedback models were innovatively proposed to generate the offsprings based on the EDA for losers. The experimental results showed that the proposed algorithms have better performance than its compared algorithms. Finally, the proposed algorithms are validated on four real-world problems, and the results indicate their superiority over their peers in solving these problems.

In the future, developing other competition mechanisms is important for DA. Furthermore, a cooperative mechanism
in DA is also worth studying. Extending these principles [49]-[56] to DA for further improving its performance is another interesting direction.
