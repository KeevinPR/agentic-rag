# Estimation of Distribution Algorithm Based on Archimedean Copulas 

Li-Fang Wang ${ }^{1,2}$ wlf1001@163.com

1. College of Electrical and Information Engineering, Lanzhou University of Technology, Lanzhou, 730050, China

Jian-Chao Zeng ${ }^{2}$ zengjianchao@263.net

Yi Hong ${ }^{1}$ yudongmei@cnn.cn

## 2. Complex System and Computational Intelligence Laboratory, Taiyuan University of Science and Technology, Taiyuan, 030024, China


#### Abstract

Both Estimation of Distribution Algorithms (EDAs) and Copula Theory are hot topics in different research domains. The key of EDAs is modeling and sampling the probability distribution function which need much time in the available algorithms. Moreover, the modeled probability distribution function can not reflect the correct relationship between variables of the optimization target. Copula Theory provides a correlation between univariable marginal distribution functions and the joint probability distribution function. Therefore, Copula Theory could be used in EDAs. Because Archimedean copulas possess many nice properties, an EDA based on Archimedean copulas is presented in this paper. The experimental results show the effectiveness of the proposed algorithm.


## Categories and Subject Descriptors

G.1.6 [Numerical Analysis]: Optimization—global optimization;
G. 3 [Probability and statistics]: Random number generation ; I.2.8 [Artificial Intelligence]: Problem Solving, Control Methods, and Search

## General Terms

Algorithms, Theory.

## Keywords

Estimation of distribution algorithms (EDAs), Copula Theory, Archimedean copulas, Sklar's theorem

## 1. INTRODUCTION

Estimation of Distribution Algorithms (EDAs) catches many researchers' eyes since it was proposed [1] because of its new search strategy and its power to solve hard optimization problems. EDAs deriving from Genetic Algorithm are different from it. There are not cross operator and mutation operator in EDAs, which are replaced by modeling and sampling the probability distribution of the selected population. Thus, modeling and sampling the probability distribution is the kernel of EDAs. The classical algorithms are PBIL [2,3], UMDA [4,5], MIMIC [6,7], BOA [8], ENGA [9], etc. EDAs has been applied in many research areas such as multiobjective optimization [10,11,12], Flow Shop [13] and so on $[14,15]$.

[^0]There are two problems in the available EDAs. One is that the probability function of the promising population could not be estimated correctly, especially for the multivariate-dependant optimization problem; the other is that the process of modeling the probability distribution function is an optimization problem and need much time to optimize.

Copula Theory is popular in statistical area [16,17] and financial area $[18,19]$ because it provides a way of studying scale-free measures of dependence. But the research of copula in computation intelligence is not available until now. Copulas join multivariate distribution functions to their one-dimensional marginal distribution functions. Alternatively, copulas are multivariate distribution functions whose one-dimensional margins are uniform on the interval $(0,1)[16]$. An EDA modeling and sampling the probability distribution in the light of Copula Theory will save the operation time and reflect exactly the dependence of variables.

In section 2, a brief description of copula theory is provided. In section 3, the EDAs based on Archimedean copulas (Archimedean Copula EDAs) is discussed. The results of experiments are presented in section 4 and the conclusions are provided in section 5 .

## 2. COPULA THEORY

The definition of copula and an essential theorem in copula theory are provided in the following.
Definition 1: Let $\mathbf{I}=[0,1]$. A two-dimensional copula (or 2-copula, or briefly, a copula) is a function $C$ from $\mathbf{I}^{2}$ to $\mathbf{I}$ with the following properties:

1) For every $u, v$ in I ,

$$
C(u, 0)=0=C(0, v)
$$

and

$$
C(u, 1)=u \text { and } C(1, v)=v
$$

2) For every $u_{1}, u_{2}, v_{1}, v_{2}$ in $\mathbf{I}$ such that $u_{1} \leqq u_{2}$ and $v_{1} \leqq v_{2}$,

$$
C(u 2, v 2)-C(u 2, v 1)-C(u 1, v 2)+C(u 1, v 1) \geqq 0
$$

Sklar's theorem: Let $H$ be a joint distribution function with margins $F$ and $G$. Then there exists a copula $C$ such that for all $x, y$ in $\mathbf{R}$,

$$
H(x, y)=C(F(x), G(y))
$$

If $F$ and $G$ are continuous, then $C$ is unique; otherwise, $C$ is uniquely determined on $\operatorname{Ran} F \times \operatorname{Ran} G$. Conversely, if $C$ is a copula and $F$ and $G$ are distribution functions, then the function $H$ defined by (4) is a joint distribution function with margins $F$ and $G$.


[^0]:    Copyright is held by the author/owner(s). GEC'09, June 12-14, 2009, Shanghai, China. ACM 978-1-60558-326-6/09/06.

Sklar's theorem plays an important role in Copula Theory, and the argument could be found in [16]. Copulas are divided into two classes, elliptical copulas and Archimedean copulas. Archimedean copulas find a wide range of applications because of the ease with which they can be constructed and the many nice properties possessed by the members of this class. [16] lists a great variety of Archimedean copulas.

## 3. ARCHIMEDEAN COPULA EDAs

According to Sklar's theorem, two steps are performed in order to construct the joint probability distribution function of a random vector. The first step is constructing the margins of each random variable separately. The second step is selecting a proper copula to construct the joint distribution. Therefore, the distribution character of each random variable and their relationship can be studied by themselves. This way can be used in EDAs to model the joint probability distribution function. And then samples are generated from the specified joint distribution by use of the copula.

The optimization problem is

$$
\min f(X)=f\left(x_{1}, x_{2}\right), x_{i} \in\left[a_{i}, b_{i}\right] \quad(i=1,2)
$$

Denote the selected population with size $s$ as

$$
\mathbf{x} @\left\{x^{i}=\left(x_{1}^{i}, x_{2}^{i}\right), i=1,2, \ldots, s\right)\}
$$

In other words, $\mathbf{x}$ are the $s$ observations of the random vector $\left(X_{1}\right.$, $X_{2}$ ). The marginal distribution function of each random variable $X_{i}$ can be estimated by normal distribution, t-distribution or empirical distribution, etc. Denote the marginal distribution function of $X_{i}$ as $u=F\left(x_{1}\right)$ and $v=G\left(x_{2}\right)$. The joint probability distribution function is constructed with a selected copula $C$ and the estimated margins in the light of Sklar's theorem.

The next step is generating samples from the joint distribution using the copula as a tool. By virtue of Sklar's theorem, it is need only to generate a pair $(u, v)$ of observations of uniform $(0,1)$ random variables $(U, V)$ whose joint distribution function is $C$, and then transform those uniform variates via the quasi-inverse of the marginal distribution functions. One procedure for generating such of a pair $(u, v)$ of uniform $(0,1)$ variates is the conditional distribution method. For this method, the conditional distribution function for $V$ given $U=u$ is need, which is denoted as $C_{u}(v)$ :
$C_{u}(v)=P(V \notin v \mid U=u)=\lim _{u \rightarrow v} \frac{C(u+\mathrm{D} u, v)-C(u, v)}{\mathrm{D} u}=\frac{C(u, v)}{Q_{u}}$
$C_{u}(v)$ exists and is non-decreasing almost everywhere in $\mathbf{I}$.
Conclusively, the generation of sample is performed as the following steps:
s1. Generate two independent uniform $(0,1)$ variates $u$ and $t$;
s2. Set $v=C_{u}^{(-1)}(t)$, where $C_{u}^{(-1)}(t)$ denotes a quasi-inverse of $C_{u}(v)$.
s3. The desired pair is $(u, v)$.
s4. Set $x_{1}=F^{(-1)}(u), x_{2}=G^{(-1)}(v)$, then $\left(x_{1}, x_{2}\right)$ is a sample of the specified joint distribution.

To sum up, the process for implementing 2-D Copula-EDA is as follows:
s1: Initialize (pop, $N$ ). Randomly generate initial population pop with size $N$. set generation count $g \leftarrow 0$.
s2: Selection (pop, spop, select-rate). Select the best select-rate* $N$ agents form pop to spop according to the agents' fitness.
s3: Copula-generator (pop, spop, mutate-rate).
s3.1: Construct the distribution model of spop;
s3.2: Generate a new population based on the specified joint distribution, and randomly generate some agents by the rate mutate-rate.
s4: Stop if the termination criterion is met.
s5: Set $g \leftarrow g+1$, and then go to s2.

## 4. EXPERIMENTS

The following functions are used to test the effectiveness of the proposed algorithm. $f_{1}-f_{3}$ and $f_{4}-f_{8}$ are adopted from [3].

- $\min f_{1}=-\frac{100}{10^{-5}+\hat{\mathbf{a}}_{1}\left|y_{i}\right|}, \quad y_{1}=x_{1}, y_{i}=x_{i}+y_{i-1}\left(i^{3} 2\right)$
$x_{1} \hat{1}[-3,3]$, the optimal is $f_{1} *(0,0, \ldots 0)=-10^{7}$.
- $\min f_{3}=-\frac{100}{10^{-5}+\hat{\mathbf{a}}_{1}\left|y_{i}\right|}, \quad y_{3}=x_{1}, y_{i}=x_{i}+\sin y_{i-1}\left(i^{3} 2\right)$
$x_{i} \hat{1}[-3,3]$, the optimal is $f_{2} *(0,0, \ldots 0)=-10^{7}$.
- $\min f_{3}=-\frac{100}{10^{-5}+\hat{\mathbf{a}}_{1}\left|y_{i}\right|}, \quad y_{3}=0.024^{\circ}(i+1)-x_{i} \cdot x_{i} \hat{1}[-3,3]$, the optimal is $f_{3} *(0.024^{\circ} 2,0.024^{\circ} 3, \ldots 0.024^{\circ}(n+1))=-10^{7}$.
- $\min f_{4}=\hat{\mathbf{a}}_{1} x_{i}^{2} \quad, \quad x_{i} \hat{1}[-500,500]$, the optimal is $f_{4} *(0,0, \ldots 0)=0$.
- $\min f_{5}=1+\hat{\mathbf{a}}_{1}\left(\sin x_{i}\right)^{2}-0.1 \exp \left(-\hat{\mathbf{a}}_{1} x_{i}^{2}\right) \cdot x_{i} \hat{1}[-10,10]$, the optimal is $f_{5} *(0,0, \ldots 0)=0.9$.
- $\min f_{6}=\hat{\mathbf{a}}_{1}\left(x_{i}^{2}-A \cos \left(2 p x_{i}\right)\right)+A\right) \cdot x_{i} \hat{1}[-5,5]$, the optimal is $f_{6} *(0,0, \ldots 0)=0$.
- $\min f_{7}=\hat{\mathbf{a}}_{1}\left(418.9829+x_{i} \sin \sqrt{\left|x_{i}\right|}\right), x_{i} \hat{1}[-500,500]$, the optimal is $f_{7} *(-420.9687,-420.9687, \ldots-420.9687)=0$.
- $\min f_{8}=\hat{\mathbf{a}}_{1} x_{i}^{2}-\bigodot_{i} \cos \left(\frac{x_{i}}{\sqrt{i+1}}\right) \cdot x_{i} \hat{1}[-100,100]$, the optimal is $f_{8} *(0,0, \ldots 0)=-1$.
- $\min f_{8}=\left[1+\left(x_{1}+x_{2}+1\right)^{2}\left(19-14 x_{1}+3 x_{1}^{2}-14 x_{2}+6 x_{1} x_{2}+3 x_{2}^{2}\right)\right]$
$\left[30+\left(2 x_{1}-3 x_{2}\right)^{2}\left(18-32 x_{1}+12 x_{1}^{2}+48 x_{2}-36 x_{1} x_{2}+27 x_{2}^{2}\right)\right]$,
$x_{1}, x_{2} \hat{1}[-2,2]$, the optimal is $f_{8} *(0,-1)=3^{\circ}$
The following two Archimedean copulas are chosen.
- $C_{1}(u, v)=\left(u^{-\theta}+v^{-\theta}-1\right)^{-1 / \theta}, \theta \geq-1, \theta \neq 0$
- $C_{2}(u, v)=\frac{u v}{1-\theta(1-u)(1-v)},-1 \leq \theta<1$

All the one-dimensional marginal distributions are normal distributions. Table 1 displays the experimental results.

Table 1. Experimental results of Archimedean Copula EDAs

All test functions are optimized in 2-dimensional spaces, the maximal generation $g$ is set to 1000 . The search terminates if the distance between the best solution found so far and the optimum is less than the predefined precision $\left(10^{-5}\right.$ for other test functions in spite of $10^{-5}$ for $f_{7}$ ). Parameters are set to (select-rate $=0.2$, mutate-rate $=0.05$, population size $N=100$ ) for all experiments. The convergence rate and the convergence generations are the average results of 50 runs. The experimental results show that Copula-EDA converges to the global optimum quickly in the test functions. There is not much difference in performance between two copulas for other test functions despite $f_{3}$ and $f_{6}$. Both the algorithms proposed in this paper perform better than the copula-EDA based on Gaussian copula and PBILc [20].

## 5. CONCLUSION

Compared with GAs, EDAs utilizes well the information provided from the promising population, and becomes the hot topic of Intelligence Computation. Whereas, it is a complex process to model and sample the probability distribution of the promising population. Copula theory in statistics provides an easier way for it. The process of modeling the probability distribution can be divided into modeling univariate margins and selecting a copula. Sampling from the constructed model can also be done by use of copula. From the experimental results it is obvious that the

Archimedean Copula EDAs proposed in this paper is effective. But two-dimensional Archimedean copula EDAs is only an attempt to join EDAs with copulas. The multi-dimensional algorithm is the next target of our study.

## 6. ACKNOWLEDGMENTS

This work was supported in part by the Youth Research Fund of Taiyuan University of Science and Technology (No.2007116), the Chinese Nature Science Fund (No. 60674104) and the Youth Research Fund of ShanXi province (No. 2006021019).
