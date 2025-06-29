# History Information Based Optimization of Additively Decomposed Function with Constraints 

Qingsheng Ren ${ }^{1}$, Jin Zeng ${ }^{2}$, and Feihu Qi ${ }^{1}$<br>${ }^{1}$ Department of Computer Science and Engineering, Shanghai Jiaotong University, Shanghai 200030, P.R. China<br>\{ren-qs, fhqi\}@cs.sjtu.edu.cn<br>${ }^{2}$ Department of Mathematics, Shanghai Jiaotong University, Shanghai 200030, P.R. China<br>zengjin@sjtu.edu.cn


#### Abstract

In this paper, we propose a modified estimation of distribution algorithm HCFA (History information based Constraint Factorization Algorithm) to solve the optimization problem of additively decomposed function with constraints. It is based on factorized distribution instead of penalty function and any transformation to a linear model or others. The history information is used and good results can be achieved with small population size. The feasibility of the new algorithm is also given.


## 1 Introduction

The constraint problem we discuss here is defined as the following:

$$
\begin{aligned}
& \max f(X)=\sum_{i} f_{i}\left(S_{i}\right) \\
& \text { s.t. } C_{i}\left(S_{i}\right)
\end{aligned}
$$

where $X=\left\{x_{1}, \cdots, x_{n}\right\}$ and the value of the $i$ th variable belongs to the set $\left\{x_{i, 1}, \cdots, x_{i, n_{i}}\right\} . C_{i}\left(S_{i}\right)$ stands for the $i$ th constraint function (it may be equality or inequality) and the variable set $S_{i} \subseteq X(i=1, \cdots, l)$. The function $f(x)$ is called additively decomposed function (ADF). This class of functions is of great theoretical and practical importance. Optimization of an arbitrary function in this space is NP complete.

Evolutionary computation (EC) is widely used for constraint optimization [1]. This method is loosely based on the mechanics of artificial selection and genetic recombination. Two crucial factors of the EC success, a proper growth and mixing of good building blocks, are often not achieved [2]. The problem of building block disruption is often referred to as the linkage problem [3]. Various attempts to prevent the disruption of important partial solutions have been done. One way to generate new individuals is to use the information extracted from the entire set of promising solutions. A general scheme of the algorithms based

on this principle is called the estimation of distribution algorithm (EDA) 4 . The main problems of EDA are how to estimate the distribution and how to get new individuals by this distribution. EDA is used successfully not only for unconstrained optimization but also for constrained optimization [5].

Although EDA is used successfully in real application, it also has the shortcoming of large population size. One of the reasons is that EDA only uses the information of the selected population and does not use any information of the population before selection. In this paper a history information based algorithm is proposed to solve additively decomposed function with constraints. We called this new algorithm as HCFA (History information based Constraint Factorization Algorithm). The main advantage of HCFA is that it can get good results with small population size. It can always produce feasible solutions if the individuals of the initial population are all feasible by using a factorization of the distribution of selected points. It can handle not only linear constraints but also nonlinear constraints. The paper is organized as follows. Section 2 gives the frame of the algorithm. In section 3, some important topics, including initialization and feasibility are discussed. Some numerical results are given in section 4 to show the efficiency of the algorithm.

# 2 The Frame of the Algorithm 

### 2.1 Factorization

To solve the problem, we must get a factorization of the probability of distribution at first. For convenience, just suppose $X=\bigcup_{i=1}^{l} S_{i}$. Define

$$
d_{i}=\bigcup_{j=1}^{i} S_{j}, b_{i}=S_{i} \backslash d_{i-1}, c_{i}=S_{i} \cap d_{i-1}
$$

Set $d_{0}=\phi$ and then we get the factorization as

$$
P(X)=\prod_{i=1}^{l} P\left(x_{b_{i}} \mid x_{c_{i}}\right)
$$

Let's see an example. Suppose $X=\left\{x_{1}, x_{2}, x_{3}\right\}, x_{i} \in\{0,1\}$ and the constraint functions are:

$$
\begin{aligned}
& x_{1}+x_{2} \leq 1 \\
& x_{2}+x_{3} \leq 1
\end{aligned}
$$

Then we have

$$
S_{1}=\left\{x_{1}, x_{2}\right\}, S_{2}=\left\{x_{2}, x_{3}\right\}
$$

So the factorization is

$$
P(X)=P\left(x_{1}, x_{2}\right) P\left(x_{3} \mid x_{2}\right)
$$

If

$$
\begin{gathered}
b_{i} \neq \phi, \forall i=1, \cdots l ; d_{l}=X \\
\forall i \geq 2, \exists j<i \text { such that } c_{i} \subseteq S_{j}
\end{gathered}
$$

we say the factorization satisfy the running intersection property. At this condition, $P\left(x_{1}, \cdots, x_{n}\right)=\prod_{i=1}^{l} P\left(x_{b_{i}} \mid x_{c_{i}}\right)$ really holds [6].

If the running intersection property is violated the factorization might not be exact. But we will show the running intersection property is not necessary by the numerical examples.

# 2.2 Algorithm 

We assume the factorization of the probability distribution is given. The following is the frame of the algorithm HCFA to solve the constraint problem:

1. Get initial feasible population;
2. Selection;
3. Compute the probabilities $P^{s}\left(x_{b_{i}} \mid x_{c_{i}}, t-1\right)$ using the selected individuals;
4. Generate a new population according to

$$
P(x, t)=\prod_{i=1}^{t}\left[\lambda P^{s}\left(x_{b_{i}} \mid x_{c_{i}}, t-1\right)+(1-\lambda) P^{s}\left(x_{b_{i}} \mid x_{c_{i}}, t-2\right)\right]
$$

where $0<\lambda \leq 1$
5. If the termination criterion is met, finish;
6. Add the best point of the previous generation to the generated points;
7. $t=t+1$, go to 2 ).

This algorithm can be run with any popular selection methods.

## 3 Further Discussion

### 3.1 Feasibility

Before the further discussion, we should know if the algorithm HCFA is feasible. This means the final solution should be feasible. The following theorem gives us the guarantee.

Theorem 1. If the former generation is feasible, the new generation will be feasible too.

Proof: If $\exists x \in$ Population $(t)$ and $x$ doesn't satisfy the $k$ th constraint $C_{k}\left(S_{k}\right)$. Then

$$
\begin{aligned}
0 \neq P(x, t) & =\prod_{i=1}^{l}\left[\lambda P^{s}\left(x_{b_{i}} \mid x_{c_{i}}, t-1\right)+(1-\lambda) P^{s}\left(x_{b_{i}} \mid x_{c_{i}}, t-2\right)\right] \\
\rightarrow & P^{s}\left(x_{b_{k}} \mid x_{c_{k}}, t-1\right) \neq 0 \text { or } P^{s}\left(x_{b_{k}} \mid x_{c_{k}}, t-2\right) \neq 0 \\
& \rightarrow P^{s}\left(x_{S_{k}}, t-1\right) \neq 0 \text { or } P^{s}\left(x_{S_{k}}, t-2\right) \neq 0
\end{aligned}
$$

Then $\exists \tilde{x} \in$ Population $(t-1), \tilde{x}_{S_{k}}=x_{S_{k}}$ or $\tilde{\exists} x \in$ Population $(t-2)$, $\tilde{x}_{S_{k}}=x_{S_{k}}$. Therefore $\tilde{x}$ or $\hat{x}$ does not satisfy $C_{k}\left(S_{k}\right)$

And it is impossible because we suppose the former generation is feasible.

# 3.2 How to Get Feasible Initial Population 

Although Theorem 1 guarantees that we can get a feasible population from a feasible former, we need a feasible initial population. The easiest way is to create a solution randomly and then check the feasibility. When $t=1$, we will generate new population according to $P(x, 1)=\prod_{i=1}^{l} P^{s}\left(x_{b_{i}} \mid x_{c_{i}}, 0\right)$.

## 4 Numerical Results

In the following examples, the experiment results are expressed by how many runs it gets the global optimum among 100 independent runs. The max generation is 100 and the population size is denoted as N.

Example 1.

$$
\begin{aligned}
& \max \sum_{i=1}^{n} x_{i} \\
& \text { s.t. } 2 \leq x_{2 j-1}^{2}+x_{2 j}^{2}+x_{2 j+1}^{2} \leq 8
\end{aligned}
$$

where $n=2 m+1, x_{i} \in\{0, \pm 1, \pm 2\}, i=1, \cdots n, j=1, \cdots, m$.
This example is a nonlinear programming problem with concave domain. The table 1 shows the results. When $\lambda=1$, it is the algorithm used in [5]. From this table we can see that the new algorithm can get better results with smaller population size.

Example 2.

$$
\begin{aligned}
& \max \sum_{i=1}^{n} x_{i} \\
& \text { s.t. } x_{2 j-1}+x_{2 j}+x_{2 j+1} \leq 2 \\
& x_{1}+x_{n-1}+x_{n} \leq 2
\end{aligned}
$$

where $n=2 m, x_{i} \in\{0,1\}, i=1, \cdots n, j=1, \cdots, m-1$

Table 1. Results of Example 1
Table 2. Results of Example 2. Not satisfy the running intersection property

The table 2 shows the results. When $\lambda=1$, it is the algorithm used in [5].
This example is a linear programming problem. In order to achieve the same convergence ratio, the population size needed by the new algorithm is much smaller than that of [5]. At the same time the factorization we used is

$$
P\left(x_{1}, \cdots, x_{n}\right)=P\left(x_{1} x_{2} x_{3}\right) P\left(x_{4} x_{5} \mid x_{3}\right) \cdots P\left(x_{n-2} x_{n-1} \mid x_{n-3}\right) P\left(x_{n} \mid x_{1} x_{n-1}\right)
$$

Obviously it does not satisfy the running intersection property. But we can still get the global optimum. We can also use the following factorization which satisfies the running intersection property.

$$
\begin{aligned}
& P\left(x_{1}, \cdots, x_{n}\right) \\
& =P\left(x_{1} x_{2} x_{3}\right) P\left(x_{4} x_{5} \mid x_{1} x_{3}\right) \cdots P\left(x_{n-2} x_{n-1} \mid x_{1} x_{n-3}\right) P\left(x_{n} \mid x_{1} x_{n-1}\right)
\end{aligned}
$$

Table 3 shows the result with the above factorization. We get much better results just because we change the factorization. This example shows the running

Table 3. Results of Example 2. Satisfy the running intersection property

intersection property is not necessary. In our research we do find that some examples can not converge to the global optimum just because the factorization does not satisfy the running intersection property. We still need further study.

# 5 Conclusion 

In this paper we proposed a new algorithm based on factorized distribution to solve constraint optimization problems of additively decomposed function. Future research work will focus on the running intersection property, converge theory, population size, etc.

## Acknowledgement

This project was supported by the National Natural Science Foundation of China.
