# On the model updating operators in univariate estimation of distribution algorithms 

Andrey G. Bronevich ${ }^{1}$ ・ José Valente de Oliveira ${ }^{2}$ (D)

Published online: 9 May 2015
(c) Springer Science+Business Media Dordrecht 2015


#### Abstract

The role of the selection operation-that stochastically discriminate between individuals based on their merit-on the updating of the probability model in univariate estimation of distribution algorithms is investigated. Necessary conditions for an operator to model selection in such a way that it can be used directly for updating the probability model are postulated. A family of such operators that generalize current model updating mechanisms is proposed. A thorough theoretical analysis of these operators is presented, including a study on operator equivalence. A comprehensive set of examples is provided aiming at illustrating key concepts, main results, and their relevance.


Keywords Compact genetic algorithm $\cdot$ Estimation of distribution algorithms $\cdot$ Selection operator $\cdot$ Theoretical analysis

## 1 Introduction

Estimation of distribution algorithms (EDAs) are playing a significant role as optimization tools (Larrañaga and Lozano 2001; Hauschild and Pelikan 2011; Ceberio et al. 2012). EDAs combine machine learning and evolutionary

[^0]computation techniques as they are stochastic population based optimizers whose central idea is to estimate a (probabilistic) model of the population from which new individuals are sampled, evaluated, and used to update the model; the whole process being repeated until convergence. Individuals encode a candidate solution of the optimization problem. In a sense, EDAs evolve probability distributions aiming at converging them to one in which an optimal solution can be sampled from with high probability.

In recent years a considerable amount of research has been devoted to the development and applications of EDAs, see e.g., Larrañaga and Lozano (2001), Hauschild and Pelikan (2011) and Ceberio et al. (2012). Depending on the probabilistic model used, EDAs can be classified as univariate, bivariate or multivariate. In the former case it is assumed that variables of a solution are independent from each other. In this category the following algorithms are worth noting. The population based incremental learning (PBIL) algorithm (Baluja 1994); the univariate marginal distribution algorithm (UMDA) (Mühlenbein 1997) where the entire population is used for estimating probabilities, and a more parsimonious algorithm known as the compact genetic algorithm (cGA) (Harik et al. 1999), where in each step only two candidate solutions are sampled from the model and undergo a tournament-like procedure whose result is used to update the probability distribution.

Bivariate EDAs are characterized by a 2-variable modeling of interaction between variables. Bivariate models include the chain model (MMIC (De Bonet et al. 1997)), the tree (COMIT (Baluja and Davies 1997)) and forest model (BMDA (Pelikan and Mühlenbein 1999)).

In multivariate EDAs various models can be used for estimating the probability distribution of individuals. The factorized distribution algorithm (Mühlenbein et al. 1999;


[^0]:    1 National Research University Higher School of Economics, Myasnitskaya 20, 101000 Moscow, Russia
    2 CEOT and FCT, Universidade do Algarve, Campus de Gambelas, 8005-139 Faro, Portugal

Mühlenbein and Mahnig 1998) was the first of such EDAs. An extension of the cGA, named extended compact GA (ECGA), was proposed in Harik (1999). ECGA handles multivariate interactions by searching over all possible disjoint partitions. ECGA generates all possible disjoint partitions and selects the best one in each iteration. The selection is based on information and complexity theory principles, such as the minimum description length principle. Another classical instances of multivariate EDA are the Bayesian optimization algorithm (BOA) (Pelikan et al. 2000; Pelikan and Goldberg 2001) and the estimation of Bayesian network algorithm (EBNA) (Bengoetxea et al. 2002) where the probability distribution is approximated by a Bayesian network. Another interesting approach to multivariate interactions resorts to clustering (Pelikan and Goldberg 2000; Peña et al. 2005; Emmendorfer and Pozo 2009). In this case, the population is represented by a set of clusters with a reduced complexity probability distribution being estimate for each cluster. After clustering it is possible to use probability models of lower order, such as univariate ones.

Relatively less efforts have been paid to the theoretical analysis of EDAs, cf. Hauschild (2011). Some theoretical results for univariate EDAs are available though. The work of Johnson and Shapiro (2002) was the first to stress the importance of model updating operators in EDAs showing that, for some selected problems, these operators have an higher impact on EDA's performance than model complexity. More specifically, it was shown that a univariate EDA equipped with a suitable operator outperforms a more complex bivariate EDA for such problems. In González et al. (2001) the PBIL algorithm is analyzed in the framework of discrete dynamical systems. The analysis reveals that (local) optima are stable fixed points of the correspondent discrete dynamic system; all other search space points being unstable. Convergence follows as a consequence. In Mühlenbein and Mahnig (2002) it is proposed two extensions of UMDA resorting to the Boltzmann distribution. A stochastic analysis of the proposed algorithms (BEDA and FDA) is also provided. Zhang (2004a, b) and Zhang and Mühlenbein (2004) thoroughly studied the global convergence of univariate EDAs, specially in the scope of UMDA and its variants. In Droste (2006) an as-sumption-free runtime analysis of cGA for linear pseudoBoolean functions is presented. More recently (LozadaChang and Santana 2011) investigate the variations in the UMDA dynamics within a certain class of fitness functions. In a related subject (Echegoyen et al. 2013) established a first taxonomy of equivalent problems in which univariate EDAs have the same behavior.

In this study we are interested in further pursuing this analytical line of work for binary problems and univariate EDAs. In particular, the role of the selection operation on
the updating of the probability distribution is thoroughly investigated for the univariate case. Necessary conditions for an operator to model selection in such a way that it can be used directly for updating the probability model are postulated. A family of such operators generalizing current selection effects is proposed. A comprehensive theoretical analysis of these operators is presented, including a study on operator equivalence. Examples are provided all through the text aiming at illustrating key concepts, main results, and their relevance. These include a generalization of the well-known cGA as an illustration of how the proposed theoretical results can be applied to algorithm design. While the necessary conditions must be taken into account while searching for an operator for a given optimization problem, the merit of an operator depends on that problem. To further illustrate this, an operator is derived that outperforms cGA in a parametric fitness function.

The remaining of this paper is organized as follows. In Sect. 2 a general optimization problem is formulated. The necessary notation and terminology is briefly presented resorting to the general computational scheme of an EDA. Section 3 postulates the necessary conditions a model updating operator should have and several examples of such operators are provided and their properties evaluated. In Sect. 4 several fundamental theoretical results are derived for the univariate case. A section on conclusions ends the paper.

## 2 Background

### 2.1 Problem formulation

Let $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ be a basic finite set and let $\mu$ : $2^{X} \rightarrow \mathbb{R}$ be an arbitrary set function, where $2^{X}$ stands for the power set of $X$, the set of all subsets of $X$. In this paper, the following optimization problem is considered:
$B=\arg \max _{A \in 2^{X}} \mu(A)$.
In plain word, the problem consist in finding a subset of $X$ that maximizes the function $\mu$. This problem has an unique solution under the condition $\mu(A) \neq \mu(B)$ if $A \neq B$ for any $A, B \in 2^{X}$. Of course, any subset of $X$ can be described by a binary string, i.e., if $A \subseteq X$ then $A$ can be described by the binary string $b(A)=\left(b_{A}\left(x_{1}\right), \ldots, b_{A}\left(x_{n}\right)\right)$, where $b_{A}\left(x_{i}\right)=$ 1 if $x_{i} \in A$ and $b\left(x_{i}\right)=0$ otherwise. For example, let $X=$ $\left\{x_{1}, x_{2}, x_{3}\right\}$ and $A=\left\{x_{2}, x_{3}\right\}$, then $b(\emptyset)=(0,0,0)$, $b(A)=(0,1,1)$, and $b(X)=(1,1,1)$.
Example 1 Let $X=\left\{x_{1}, x_{2}\right\}$ be the set of all possible individuals as given in Table 1. The table also includes an arbitrary set function $\mu$ viewed as a fitness function. The maximum of $\mu(A)$ is achieved for $A=\left\{x_{2}\right\}$.

Table 1 The set of possible individuals for $X=\left\{x_{1}, x_{2}\right\}$ together with an arbitrary set function $\mu$ viewed as a fitness function

| Id | $b\left(x_{1}\right)$ | $b\left(x_{2}\right.$ | $\mu$ |
| :-- | :-- | :-- | :-- |
| $A_{0}$ | 0 | 0 | 0.2 |
| $A_{1}$ | 0 | 1 | 0.6 |
| $A_{2}$ | 1 | 0 | 0.0 |
| $A_{3}$ | 1 | 1 | 0.4 |

A remark is in order here. At first, the problem statement may seem trivial. However, for a sufficiently large cardinality of $X$, as found in many real-world applications, the problem of calculating all the values of the set function $\mu$ can be computationally intractable, thus it is reasonable to use the type of algorithms that we are interested in this study, among others metaheuristics.

A binary sequence $\left\{b\left(x_{1}\right), \ldots, b\left(x_{n}\right)\right\}$ is called individual and consists of variables $b\left(x_{i}\right)$. At position $x_{i}$ two values are possible, $b\left(x_{i}\right)=0$ and $b\left(x_{i}\right)=1$. Therefore, the above
of variables in the population. For instance, under the assumption of variable independence, the probability distribution $p$ is uniquely defined by the probabilities $p\left(x_{i}\right)=$ $\operatorname{Pr}\left(b_{A}\left(x_{i}\right)=1\right) ; i=1, \ldots, n$, where $n$ is the length of the individual, and obviously $p(A)=\prod_{x_{i} \in A} p\left(x_{i}\right) \prod_{x_{i} \notin A}\left(1-p\left(x_{i}\right)\right)$.

We can describe an EDA by a sequence of probability distributions $\left\{p_{1}, p_{2}, \ldots, p_{i}, \ldots\right\}$ where the index $i$ refers to the iteration (or generation) number, and $p_{i}$ is defined over $2^{X}$. We can think about a general computation scheme for an EDA such as that presented in Algorithm 1. In the step identified by (1) in this algorithm we view the ranking procedure as a recovering from the sample $D$ of the cumulative distribution function (cdf) $F: 2^{X} \rightarrow[0,1]$ defined by

$$
F(B)=\sum_{\mu(A) \leqslant \mu(B)} p(A) ; \quad B \in 2^{X}
$$

```
Algorithm 1: A general computational scheme for EDAs (Larrañaga and Lozano, 2001; Ceberio
et al., 2012)
    Define the fitness function \(\mu\) or a linear order among individuals (whatever is available);
    Set the size of generated samples (progenitors) \(N\);
    Initialize the iteration counter \(i(i:=0)\);
    Initialize the probability distribution over individuals \(p_{i=0}\);
    \(D_{i=0}:=\) Sample \(N\) individuals from \(p_{i=0}\);
    output: The solution \(A\) for which \(p_{i}(A) \approx 1\)
    repeat
    \(1 \quad D_{i}:=\) Rank individuals in \(D_{i}\) by their fitness or using linear order information (whatever is available);
    \(D_{i}^{*}:=\) Select \(M \leq N\) individuals from \(D_{i}\) according to a selection method;
    \(p_{i}(x):=p\left(x \mid D_{i}^{*}\right)\) Update the probability distribution based on the selected individuals \(D_{i}^{*}\);
    \(D_{i+1}:=\) Sample \(M\) individuals (the new population) from \(p_{i}\);
    \(i:=i+1\)
until \(A\) convergence condition is met;
```

formulation is a sufficient framework for modeling a population of individuals.

### 2.2 The general computational scheme for EDA

EDAs rely on population modeling. This can be accomplished by resorting to probability theory. For this purpose, we can assign to a given population a probability distribution $p$ over the power set of $X, 2^{X}$ such that $\sum_{A \in 2^{X}} p(A)=1$. Of course, the value $p(A)$ can be interpreted as the frequency of individual $A$ in the population and is related to the frequency

Table 2 shows an example of the both a probability distribution $p$ and the corresponding cdf $F$ under the conditions of Example 1.

## 3 On model updating operators

Roughly speaking, for maximization problems the selection operation prefers high fitness individuals to low fitness ones. It turns out that the selection operation plays a crucial role in EDAs, cf. Johnson and Shapiro (2002). To illustrate this, consider one of the simplest EDA, the cGA. cGA uses

Table 2 An hypothetical probability distribution $p$, and the corresponding $\operatorname{cdf} F$, under the conditions of Example 1

| Id | $b\left(x_{1}\right)$ | $b\left(x_{2}\right)$ | $\mu$ | $p$ | $F$ |
| :-- | :-- | :-- | :-- | :-- | :-- |
| $A_{0}$ | 0 | 0 | 0.2 | $1 / 2$ | $2 / 3$ |
| $A_{1}$ | 0 | 1 | 0.6 | 0 | 1 |
| $A_{2}$ | 1 | 0 | 0.0 | $1 / 6$ | $1 / 6$ |
| $A_{3}$ | 1 | 1 | 0.4 | $1 / 3$ | 1 |

the results of a selection operation for estimating its probability distribution model of the population. cGA adopts the so-called Block selection which is a steady-state binary tournament equivalent selection. Block selection takes two individuals and duplicates the winner while discards the looser. Based on this, cGA uses a simple updating rule for probability distribution, i.e., $p\left(x_{i}\right)=$ $\operatorname{Pr}\left(b_{A}\left(x_{i}\right)=1\right) ; i=1, \ldots, n$, where $n$ is the length of the individual, is updated by the amount $\pm 1 / S, S$ being the user-defined size of the modeled population.

Notice that by applying this rule, the proportion of variables in the population equal to 1 in a given position will increase by $1 / S$ if the winning individual has a 1 in that position; it will decrease by the same amount if the winning individual has a 0 in the same position; for the general case where winner is different from the looser. Curiously enough, it was experimentally shown that when equipped with this updating rule cGA runs with the same convergence rate and reliability as the simple genetic algorithm under uniform crossover (Harik et al. 1999; Harik 1999).

In this section, we generalize the updating of the probability distribution model by defining a pair of model updating operators. Assume that population is ordered by the function $\mu$. Let $\mu(A)>\mu(B)$ then
$p_{k+1}\left(x_{i}\right)= \begin{cases}p_{k}\left(x_{i}\right) & b_{A}\left(x_{i}\right)=b_{B}\left(x_{i}\right) \\ \varphi\left(p_{k}\left(x_{i}\right)\right) & b_{A}\left(x_{i}\right)<b_{B}\left(x_{i}\right) \\ \psi\left(p_{k}\left(x_{i}\right)\right) & b_{A}\left(x_{i}\right)>b_{B}\left(x_{i}\right)\end{cases}$
if $\mu(A)<\mu(B)$ we act symmetrically. That is, we model the effects of selection in the individual probability distribution using a pair of operators $(\varphi, \psi)$ where $\varphi$ is called the selection operator, and $\psi$ is its dual, and are defined as follows. The operator $\varphi, \varphi:[0,1] \rightarrow[0,1]$, maps the $\operatorname{cdf} F$ of a individual into new $\operatorname{cdf} F^{\prime}$, i.e., $F^{\prime}=\varphi \circ F$. For reasons discussed next, this mapping should satisfy the following necessary properties:

1. Boundary conditions: $\varphi(0)=0$ and $\varphi(1)=1$;
2. Monotonically increasing: $\varphi(x) \leqslant \varphi(y)$ if $x \leqslant y$ for $x, y \in[0,1]$
3. Convexity: $\varphi(x+\Delta x)-\varphi(x) \leqslant \varphi(x+2 \Delta x)-\varphi(x+$ $\Delta x)$ for $\Delta x>0$, and $x, x+2 \Delta x \in[0,1]$.
The operator $\psi$ is the dual of $\varphi$, i.e., $\psi:[0,1] \rightarrow[0,1]$ and $\psi(x)=1-\varphi(1-x)$.

Clearly, Properties 1 and 2 are necessary and sufficient to preserve the properties of the cdf. Property 3 (convexity) allows us to specify the desirable selection effect. Again assume that population is ordered by the function $\mu$, i.e., the population can be represented as a chain

$$
\left(A_{1}, \ldots, A_{m-2}, A_{m-1}, A_{m}, A_{m+1}, \ldots, A_{2^{n}}\right)
$$

where $\mu\left(A_{i}\right)<\mu\left(A_{j}\right)$ if $i<j$, and $A_{m-1}, A_{m}$ are two nearest individuals in fitness terms such that $p\left(A_{m-1}\right)-$ $p\left(A_{m}\right)=\Delta z$. Then $p\left(A_{m-1}\right)=F\left(A_{m-1}\right)-F\left(A_{m-2}\right), p\left(A_{m}\right)$ $=F\left(A_{m}\right)-F\left(A_{m-1}\right)$, and after selection there will be new probabilities $p^{\prime}\left(A_{m-1}\right)=\varphi\left(F\left(A_{m-1}\right)\right)-\varphi\left(F\left(A_{m-2}\right)\right)$ and $p^{\prime}\left(A_{m}\right)=\varphi\left(F\left(A_{m}\right)\right)-\varphi\left(F\left(A_{m-1}\right)\right)$. According to selection we should have at least $p^{\prime}\left(A_{m-1}\right) \leqslant p^{\prime}\left(A_{m}\right)$. Denoting $z=F\left(A_{m-1}\right)$, we get the inequality: $\varphi(z+\Delta z)-\varphi(z) \leqslant$ $\varphi(z+2 \Delta z)-\varphi(z+\Delta z)$. If the function $\varphi$ is two times differentiable on $[0,1]$, then Properties 2 and 3 are clearly equivalent to $\varphi^{\prime}(x) \geqslant 0$ and $\varphi^{\prime \prime}(x) \geqslant 0$ for any $x \in[0,1]$.
Lemma 1 Let $\varphi:[0,1] \rightarrow[0,1]$ be a continuous function on $[0,1)$ such that $\varphi(0)=0, \varphi(1)=1$, and $\varphi(x)<x$ for all $x \in(0,1)$. Then any sequence $\left\{x_{k}\right\}_{k=1}^{\infty}$, defined by $x_{1} \in[0,1), x_{2}=\varphi\left(x_{1}\right), \ldots, x_{k}=\varphi\left(x_{k-1}\right), \ldots$, converges to 0 , i.e. $\lim _{k \rightarrow \infty} x_{k}=0$.

Proof The analyzed sequence is decreasing and bounded, therefore its limit exists, i.e., we can write $\lim _{k \rightarrow \infty} x_{k}=a$. Clearly, $\lim _{k \rightarrow \infty} \varphi\left(x_{k}\right)=\lim _{k \rightarrow \infty} x_{k}=a$. Because $\lim _{k \rightarrow \infty} \varphi\left(x_{k}\right)=\varphi\left(\lim _{k \rightarrow \infty} x_{k}\right)$ $=\varphi(a)$, we get $\varphi(a)=a$ and there is only the possibility $a=0$, because $\varphi(x)<x$ for all $x \in(0,1)$.
Remark 1 Notice that any convex function $\varphi:[0,1] \rightarrow$ $[0,1]$ such that $\varphi(0)=0, \varphi(1)=1$, is continuous in $[0,1)$ and $\varphi(x) \leqslant x$ for all $x \in[0,1]$, and if $\varphi(x) \neq x$ at least in one point $x \in(0,1)$, then obviously $\varphi(x)<x$ for all $x \in(0,1)$.
Remark 2 Lemma 1 gives us also sufficient and necessary conditions for convergence. Assume that ranking is known, the initial cdf being $F_{0}: 2^{X} \rightarrow[0,1]$. Further assume that $A$ is the best individual and its probability is not equal to zero. Then $F_{0}(A)=1$ and $F_{0}(B) \in[0,1)$ for any $B \neq A$. Consider the sequence of cdfs $F_{1}=\varphi \circ F_{0}, \ldots$, $F_{n}=\varphi \circ F_{n-1}$, where the function $\varphi$ satisfies the conditions of Lemma 1. Then obviously, there is a limit $F=\lim _{k \rightarrow \infty} F_{k}$ and $F(B)=1$ if $B=A$ and $F(B)=0$ otherwise. If $\varphi$ does not satisfies the conditions of Lemma 1, for example, $\varphi(x)=x$ for some $x \in(0,1)$, then it is possible that $F(B) \neq 0$ for some $B \neq A$, or if the probability of the individual $A$ is equal to zero, then for the next best individual $B$, we also have $F(B)=1$.

To illustrate the application of the pair $(\varphi, \psi)$ we generalize one of the simplest EDA algorithm, the cGA. This algorithm constitutes a parsimonious concretization of the general computational scheme for an EDA (Algorithm 1).
$0.5 p\left(A_{i}\right)$ to model the situation where a pair consists of two identical individuals. Let us compute the cdf for the selected population. We start by simplifying first the following expression:

```
Algorithm 2: A generalized compact GA (cGA) algorithm
    input : the length of the individuals \(n\); a pair \((\varphi, \psi)\); fitness function \(\mu\) or a linear order among individuals; a
        termination tolerance parameter \(\varepsilon>0\)
    output: The individual for which \(p \approx 1\)
    \(p:=\left[\begin{array}{lll:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:l:\end{array}\right.\) // Probability distribution
    repeat
        individual1 \(:=\) generate \((p)\);
        individual2 \(:=\) generate \((p)\);
        \(\{\) winner, loser \} \(:=\) compete (individual1, individual2 \);
        for \(j:=1\) to \(n\) do
            if winner[j] != loser[j] then
                if winner \([j]==1\) then \(p[j]:=\psi(p[j])\);
                else \(p[j]:=\varphi(p[j])\);
            end
        end
    until \(p_{i} \notin(0+\epsilon, 1-\epsilon) ; i=1, \ldots, n\);
    with \(\psi(x):=1-\varphi(1-x)\);
```

A full theoretical justification for using the proposed pair $(\varphi, \psi)$ in this algorithm is provided in Sect. 4.

It is clear that Algorithm 2 includes cGA as a special case for $\left(\varphi_{1}, \psi_{1}\right)$ with

$$
\varphi_{1}(x)=\left\{\begin{array}{cc}
0, & x \in[0,1 / S] \\
x-1 / S, & x \in(1 / S, 1) \\
1, & x=1
\end{array}\right.
$$

where $S$ is the user-defined parameter representing the population size, and $\psi_{1}(x)=1-\varphi_{1}(1-x)$.

In the same vein, the proposed updating operator can also be viewed as a generalization of the incremental selection operator of PBIL for $\left(\varphi^{\prime}, \psi^{\prime}\right)$ with $\varphi^{\prime}(x)=$ $(1-\alpha) x+\alpha \varphi(x)$, and $\psi^{\prime}(x)=1-\varphi^{\prime}(1-x)=(1-\alpha) x+$ $\alpha(1-\varphi(1-x))=(1-\alpha) x+\alpha \psi(x), \alpha$ being the so-called learning rate.

Consider now the specification of the mapping $\varphi$. Suppose we have a sample of individuals from the probability distribution defined by a cdf, $F$. Suppose that we divide this sample randomly in pairs and perform tournament among pair individuals. For the sake of simplicity let us enumerate individuals $A_{i}, i=1, \ldots, 2^{n}$, such that $\mu\left(A_{i}\right)<\mu\left(A_{j}\right)$, if $i<j$. The win probability of individual $A_{i}$ is $F\left(A_{i}\right)-0.5 p\left(A_{i}\right)$. Here we subtract

$$
\begin{aligned}
& \sum_{i=1}^{j} p\left(A_{i}\right)\left(F\left(A_{i}\right)-0.5 p\left(A_{i}\right)\right) \\
& \quad=0.5 \sum_{i=1}^{j} p^{2}\left(A_{i}\right)+\sum_{i=2}^{j} \sum_{k=1}^{i} p\left(A_{i}\right) p\left(A_{k}\right)=0.5 F^{2}\left(A_{j}\right)
\end{aligned}
$$

Therefore, progenitors have the cdf $F^{2}$ and $\varphi(x)=x^{2}$. We can model also other forms of selection. For example, if we consider that a given individual has a probability $a$ of taking part in the tournament, then the operator becomes:

$$
\varphi(x)=a x^{2}+(1-a) x
$$

Example 2 In this example we apply the generalized cGA, Algorithm 2, equipped with operator (2) to the wellknown and widely used onemax (or bit counting) problem. The fitness function for this problem can be given by Harik et al. (1999 and Pelikan et al. (2000): $\mu(A)=\sum_{i=1}^{n} b_{A}\left(x_{i}\right)$.

Figure 1 shows the obtained results for a sequence of $a$ values. As the probability $a$ of an arbitrary individual to take part in the competition increases the number of generations required to achieve convergence decreases significantly attaining his minimum at $a=1$. Concomitantly, the reliability of the whole algorithm to attain the optimum of $\mu$ also decreases; an issue that will be further studied in the next sections.

![img-0.jpeg](img-0.jpeg)

Fig. 1 Mean and standard deviation of the number of generations computed over 50 runs of the generalized cGA (Algorithm 2) versus $a$ of the operator (2) when applied to the 100-bit onemax problem

### 3.1 On the comparison of operators

The merit of model updating operator $\varphi$ depends on the class of fitness function (optimization problem) considered and, all other things being equal, it can be characterized by the associated (1) convergence rate, (2) convergence reliability, i.e., the ability to guide the algorithm to an extreme of the fitness function, and (3) scalability. Convergence rate is related to how $\varphi$ updates probability distributions. Consider an ideal situation where the fitness function $\mu$ is linear, i.e.,

$$
\mu(A)=\sum_{i=1}^{n} \alpha_{i} b_{A}\left(x_{i}\right)
$$

with $\alpha_{i}<0, i=1, \ldots, n$, i.e., $\emptyset$ is the best individual while $X$ is the worst. Under these conditions, probabilities $p^{(k)}\left(x_{i}\right)$ at generation $k$, are such that:

$$
\begin{aligned}
p^{(0)}\left(x_{i}\right) & =0.5 \\
p^{(1)}\left(x_{i}\right) & =\varphi(0.5) \\
p^{(2)}\left(x_{i}\right) & =\varphi\left(p^{(1)}\left(x_{i}\right)\right)=\varphi(\varphi(0.5))=\varphi^{(2)}(0.5) \\
\cdots & \cdots \\
p^{(k)}\left(x_{i}\right) & =\varphi\left(p^{(k-1)}\left(x_{i}\right)\right)=\varphi\left(\varphi^{(k-1)}(0.5)\right)=\varphi^{(k)}(0.5)
\end{aligned}
$$

Here we are adopting the usual assumption, i.e., the initial population distribution $p^{(0)}$, is such that 0 and 1 are equiprobable values in any position $x_{i}$. We say that two selection operators $\varphi_{1}$ and $\varphi_{2}$ are $(\varepsilon, N)$-equivalent if $\varphi_{1}^{(N)}(0.5)=\varphi_{2}^{(N)}(0.5)=\varepsilon$. Therefore, we will observe the same convergence rate for two $(\varepsilon, N)$-equivalent selection operators after $N$ iterations in ideal conditions. However, $(\varepsilon, N)$-equivalent selection operators can show different convergence rates and different reliability when applied to real optimization problems. The later can be simply evaluated by evaluating $\mu$ at the found solution.

Example 3 In the following we derive five $(\varepsilon, N)$-equivalent selection functions.

1. $\varphi_{1}(x)=\left\{\begin{array}{cc}0, & x \in[0, h] \\ x-h, & x \in(h, 1) \\ 1, & x=1\end{array}\right.$
where $h$ is a user-defined parameter. Again this operator is the equivalent to the original operator used for modeling selection in cGA with $h=1 / S$. Consequently,

$$
\varphi_{1}^{(N)}(x)=\left\{\begin{array}{cc}
0, & x \in[0, h N] \\
x-N h, & x \in(h N, 1) \\
1, & x=1
\end{array}\right.
$$

and $\varphi_{1}$ is in the class of $(\varepsilon, N)$-equivalent selection operators if $\varphi_{1}^{(N)}(0.5)=\varepsilon$, i.e., $0.5-N h=\varepsilon$ and $h=(0.5-\varepsilon) / N$. See Fig. 2a for the characteristic of $\varphi_{1}$ for a range of population size parameter $S$.
2. $\varphi_{2}(x)=x^{a}$, where $a>1$. Then $\varphi_{2}^{(N)}(x)=x^{a^{b}}$ and $\varphi_{2}$ is in the class of $(\varepsilon, N)$-equivalent selection operators if $\varphi_{2}^{(N)}(0.5)=\varepsilon$, i.e., $0.5^{a^{b}}=\varepsilon$ and $a=\sqrt[a]{-\operatorname{lg}_{2}(\varepsilon)}$. See Fig. 2b for the characteristic of $\varphi_{2}$ for the admissible range of $a$ values.
3. $\varphi_{3}(x)=1-(1-x)^{a}$, where $0<a<1$. Then $\varphi_{3}^{(N)}(x)=$ $1-(1-x)^{a^{b}}$ and $\varphi_{3}$ is in the class of $(\varepsilon, N)$-equivalent selection operators if $\varphi_{3}^{(N)}(0.5)=\varepsilon$, i.e., $1-0.5^{a^{b}}=\varepsilon$ and $a=\sqrt[a]{-\operatorname{lg}_{2}(1-\varepsilon)}$. See Fig. 2c for the characteristic of $\varphi_{3}$ for the admissible range of $a$ values.
4. $\varphi_{4}(x)=a x^{2}+(1-a) x$, where $0<a \leqslant 1$. In this case it is not possible to find the analytical solution of the equation $\varphi_{4}^{(N)}(0.5)=\varepsilon$ but it can be solved numerically. See Fig. 2d for the characteristic of $\varphi_{4}$ for the admissible range of $a$ values.
5. $\varphi_{5}(x)=\Phi\left(a+\Phi^{-1}(x)\right)$, where $\Phi$ is the cdf of the standard normal distribution, i.e.,

$$
\Phi(x)=\frac{1}{\sqrt{(2 \pi)}} \int_{-\infty}^{x} \mathrm{e}^{-t / 2} d t
$$

$\Phi^{-1}$ is the normal inverse cdf (quantile) function, and $a<0$. In this case $\varphi_{5}^{(N)}(x)=\Phi\left(a N+\Phi^{-1}(x)\right)$ and $\varphi_{5}$ is in the class of $(\varepsilon, N)$-equivalent selection operators if $\varphi_{5}^{(N)}(0.5)=\varepsilon, \quad$ i.e., $\quad \Phi\left(a N+\Phi^{-1}(0.5)\right)=\varepsilon \quad$ and $a=\Phi^{-1}(\varepsilon) / N$. See Fig. 2e for the characteristic of $\varphi_{5}$ for the admissible range of $a$ values.

![img-1.jpeg](img-1.jpeg)

Fig. 2 Characteristics of the proposed operators as function of their parameters a operator $\varphi_{1}(x)$, i.e., cGA, $\mathbf{b}$ operator $\varphi_{2}(x)=x^{a}$, $\mathbf{c}$ operator $\varphi_{3}(x)=1-(1-x)^{a}$, $\mathbf{d}$ operator $\varphi_{4}(x)=a x^{2}+(1-a) x$, e operator $\varphi_{5}(x)=\Phi\left(a+\Phi^{-1}(x)\right)$. (Color figure online)

See Sect. 4 for a theoretical justification of the above proposed operators. See Fig. 2 for the different characteristics of these operators as function of their parameters.

An alternative way of assessing the merits of a model updating operator $\varphi$ on a given fitness function (optimization problem) is to establish a criterium for its
convergence reliability and computes the required effort for convergence. A possibility is to compare the number of generations required by a given operator for which the maximum likelihood estimation (MLE) of the probability of success (reaching a global maximum) is greater or equal than a given confidence level. This approach is also used in

Sastry and Goldberg (2001) and followed in the example below.

### 3.2 An optimal updating operator based on a prior information

It should be clear that while conditions 1,2 , and 3 in the beginning of Sect. 3 are necessary conditions to be taken into account while searching for an operator for a given optimization problem, the merit of an operator depends on that problem. To further stress this point, assume that the fitness function $\mu$ has the following structure:
$\mu(B)=\sum_{i=1}^{n} \xi_{i} b_{B}\left(x_{i}\right)$
where $\xi_{i}=\left\{\begin{array}{ll}1, & i \in A \\ -1 & i \notin A\end{array}\right.$ and $A \subseteq\{1,2, \ldots, n\}$. Clearly this problem has a maximum for $B$ equals to $A$. Let us assume that our prior information about the optimal individual denoted as $\left(b_{A}^{*}\left(x_{1}\right), \ldots, b_{A}^{*}\left(x_{n}\right)\right)$ is described by probabilities $p\left(x_{i}\right)=\operatorname{Pr}\left(\xi_{i}\right), i=1, \ldots, n$, and we observe two individuals $B$ and $C$ such that $\mu(B)>\mu(C)$. Let us update probabilities $p\left(x_{i}\right)$ using the Bayes rule, i.e., compute probabilities $p^{*}\left(x_{i}\right)=\operatorname{Pr}\left(\xi_{k}=1 \mid \mu(B)>\mu(C)\right), i=1, \ldots, n . \quad$ Let us compute the probability $\operatorname{Pr}(\mu(B)>\mu(C))$. For this we can assume that random variables $\xi_{1}, \ldots, \xi_{n}$ are independent and analyze the random variable
$\xi=\mu(B)-\mu(C)=\sum_{x_{i} \in B \backslash C} \xi_{i}-\sum_{x_{i} \in C \backslash B} \xi_{i}$
then
$\xi=\left\{\begin{array}{cl}\eta+\xi_{k}, & x_{k} \in B \backslash C, \\ \eta-\xi_{k}, & x_{k} \in C \backslash B, \\ \eta & \text { otherwise }\end{array}\right.$
with
$\eta=\sum_{x_{i} \in B \backslash\left(C \cup\left\{x_{k}\right\}\right)} \xi_{i}-\sum_{x_{i} \in C \backslash\left(B \cup\left\{x_{k}\right\}\right)} \xi_{i}$
Thus, following Bayes, the optimal updating expression for $p\left(x_{k}\right), p^{*}\left(x_{k}\right) ; k=1, \ldots, n$ is:
$p^{*}\left(x_{k}\right)=\frac{p\left(x_{k}\right) \operatorname{Pr}(\eta+a>0)}{p\left(x_{k}\right) \operatorname{Pr}(\eta+a>0)+\left(1-p\left(x_{k}\right)\right) \operatorname{Pr}(a>0)}$
where
$a=\left\{\begin{array}{ll}1 & x_{k} \in B \backslash C, \\ -1 & x_{k} \in C \backslash B, \\ 0 & \text { otherwise }\end{array}\right.$
Notice that $p^{*}\left(x_{k}\right)=p\left(x_{k}\right)$ if $x_{k} \in(B \backslash C) \cup(C \backslash B)$. Because $\eta$ is the sum of independent random variables, it can be approximated by a normal distribution of mean

$$
\begin{aligned}
\mathbb{E}[\eta] & =\mathbb{E}\left[\sum_{x_{i} \in B \backslash\left(C \cup\left\{x_{k}\right\}\right)} \xi_{i}-\sum_{x_{i} \in C \backslash\left(B \cup\left\{x_{k}\right\}\right)} \xi_{i}\right] \\
& =\sum_{x_{i} \in B \backslash\left(C \cup\left\{x_{k}\right\}\right)}\left(2 p\left(x_{i}\right)-1\right)-\sum_{x_{i} \in C \backslash\left(B \cup\left\{x_{k}\right\}\right)}\left(2 p\left(x_{i}\right)-1\right)
\end{aligned}
$$

and variance

$$
\begin{aligned}
\sigma^{2}[\eta] & =\sigma^{2}\left[\sum_{x_{i} \in B \backslash\left(C \cup\left\{x_{k}\right\}\right)} \xi_{i}-\sum_{x_{i} \in C \backslash\left(B \cup\left\{x_{k}\right\}\right)} \xi_{i}\right] \\
& =4\left[\sum_{x_{i} \in B \backslash\left(C \cup\left\{x_{k}\right\}\right)} p\left(x_{i}\right)\left(1-p\left(x_{i}\right)\right)+\sum_{x_{i} \in C \backslash\left(B \cup\left\{x_{k}\right\}\right)} p\left(x_{i}\right)\left(1-p\left(x_{i}\right)\right)\right]
\end{aligned}
$$

Thus it is legitime to approximate probabilities as follows

$$
\begin{aligned}
\operatorname{Pr}(\eta+a>0) & =1-\operatorname{Pr}(\eta \leq-a) \approx 1-\Phi\left(\frac{-a-\mathbb{E}[\eta]}{\sigma[\eta]}\right) \\
\operatorname{Pr}(\eta>0) & =1-\operatorname{Pr}(\eta \leq 0) \approx 1-\Phi\left(\frac{-\mathbb{E}[\eta]}{\sigma[\eta]}\right)
\end{aligned}
$$

where again $\Phi$ stands for the cdf of the standard normal distribution. ${ }^{1}$ For the sake of computation efficiency, we can assume a priori $p\left(x_{i}\right)=0.5$ in expressions (5) and (6) yielding $\mathbb{E}[\eta]=0$ and $\sigma[n]=\sqrt{|C \backslash B|+|B \backslash C|-1}$, respectively. Under these assumptions, the new updating operator is hereafter referred to as the Bayesian operator.
Example 4 In this example we assess the performance of the above updating operator by contrasting its performance with the performance of cGA. In particular we compare the number of iterations required to achieve the same MLE of the probability of success $\hat{p}_{s}$, i.e., reaching the global maximum of fitness function (4) with $n=20$ and $A=\{1,3,10,20\}$.

To begin with we examine the performance of the Algorithm 2 equipped with $\varphi_{1}$ above, i.e., acting as the classic cGA. From Fig. 3a we observe that at least $S=30$ is required for achieving $\hat{p}_{s}=1$ over 1000 independent runs for a stop criterium with $\epsilon=0.01$.

Figure 3b shows the number of generations averaged over 1000 runs for the cGA versus the population size $S$ the same conditions above. The proposed updating operator has always converged to the global maximum (i.e., it ran always with $\hat{p}_{s}=1$ ). As can be seen in Fig. 5a the number of generations required by the proposed Bayesian operator is significantly lower than that required by cGA.

Example 5 In this example a first attempt is made to assess the scalability of the proposed operator. The

[^0]
[^0]:    ${ }^{1}$ Several software packages include efficient ways of computing the normal cdf.

![img-4.jpeg](img-4.jpeg)

Fig. 3 a MLE of prob. of success $\hat{p}_{x}$ and $\mathbf{b}$ average number of generations over 1000 independent runs for cGA versus the population size $S$ when applied to a 20-bit problem characterized by the
![img-5.jpeg](img-5.jpeg)

Fig. 4 a MLE of prob. of success $\hat{p}_{x}$ and $\mathbf{b}$ number of generations averaged over 50 independent runs for cGA versus the population size $S$ when applied to a 100-bit problem characterized by the fitness
example is essentially the same as the previous one except for the size of individuals that changed from $n=20$ to $n=100$ and
$A=$
$\{1,3,10,20,21,22,25,30,35,38,40,50,60,70,80,90,100\}$
in function (4).
Following a process similar to the previous example we observe in Fig. 4a that at least $S=57$ is required for achieving $\hat{p}_{x}=1$ over 50 independent runs. The proposed updating operator has always converged to the global maximum. As can be seen in Fig. 5b the number of generations required by the proposed Bayesian operator is again significantly lower than that required by cGA.

Comparing Figure. 5a, b we see that while cGA has suffered an increment of 675 in the average number of generations, the proposed Bayesian operator required only more 521 generations in average when $n$ changed from 20 to 100 .
![img-4.jpeg](img-4.jpeg)
fitness function (4). The green vertical line shows $S=30$ as the minimum value required for achieving $\hat{p}_{x}=1$. (Color figure online)
![img-5.jpeg](img-5.jpeg)
function (4).The green vertical line shows $S=57$ as the minimum value required for achieving $\hat{p}_{x}=1$. (Color figure online)

Example 6 Following the same methodology of the previous examples, here we compare the performance of the proposed operators with the performance of cGA in yet another fitness function, i.e.,
$\mu(A)=\sum_{i=1}^{n} 2^{n-i} b_{A}\left(x_{i}\right)$
for $n=20,30,40$, and 50 . Again we require a reliability characterized by $\hat{p}_{x}=1$ over 50 independent runs for a stop criterium with $\epsilon=0.01$.

Figures 6, 7, 8 and 9 show both (a) the MLE of prob. of success $\hat{p}_{x}$ and (b) the average number of generations for Algorithm 2 when equipped with each one of the proposed operators versus their respective parameters, when applied to the fitness function (7) with $n=40$. The figures also show those parameter values that allow us to achieve the minimum average generations for the above defined reliability. Operator $\varphi_{2}$ performs very poorly in this problem; it requires more than 3000 generations in average

![img-6.jpeg](img-6.jpeg)

Fig. 5 Box plots exhibiting the dispersion, skewness, as well as outliers of the number of generations achieved over 100 independent runs for the proposed Bayesian operator and for cGA under the
![img-7.jpeg](img-7.jpeg)

Fig. 6 Performance of operator $\varphi_{1}(x)$, i.e., cGA, showing (green vertical line) $S=145$ as the value required for achieving $\hat{p}_{x}=1$ over 50 independent runs with fitness function (7) with $n=40$ a $\hat{p}_{x}$ versus $S$, b mean generations versus $S$. (Color figure online)
![img-8.jpeg](img-8.jpeg)

Fig. 7 Performance of operator $\varphi_{3}(x)=1-(1-x)^{n}$ showing (green vertical line) $a=0.61$ as the value required for achieving $\hat{p}_{x}=1$ over 50 independent runs with fitness function (7) with $n=40$ a $\hat{p}_{x}$ versus $a$, b mean generations versus $a$. (Color figure online)
for $n=20$ and hence it is immediately excluded from further comparisons.

Figure 10 clearly show that, for this optimization problem, the proposed Bayesian operator has a convergence rate significantly higher than all the others, requiring an average
of about 450 generations. Ranking second in this comparison is operator $\varphi_{3}$ with an average of 894 generations. The cGA is the last of the group with an average of about 3327 generations.

Figure 11 allows us to infer the scalability of the different operators in this problem. A first observation is

![img-9.jpeg](img-9.jpeg)

Fig. 8 Performance of operator $\varphi_{4}(x)=a x^{2}+(1-a) x$ showing (green vertical line) $a=0.13$ as the value required for achieving $\hat{p}_{x}=1$ over 50 independent runs with fitness function (7) with $n=40$, a $\hat{p}_{x}$ versus $a$, b mean generations versus $a$. (Color figure online)
![img-10.jpeg](img-10.jpeg)

Fig. 9 Performance of operator $\varphi_{5}(x)=\Phi\left(a+\Phi^{-1}(x)\right)$ showing (green vertical line) $a=-0.11$ as the value required for achieving $\hat{p}_{x}=1$ over 50 independent runs with fitness function (7) with $n=40$ a $\hat{p}_{x}$ versus $a$, b mean generations versus $a$. (Color figure online)
![img-11.jpeg](img-11.jpeg)

Fig. 10 Box plots exhibiting the dispersion, skewness, as well as outliers of the number of generations achieved over 100 independent runs for a cGA, $\mathbf{b} \varphi_{3}, \mathbf{c} \varphi_{4}, \mathbf{d} \varphi_{5}$, and $\mathbf{e}$ Bayesian under the conditions required for achieving $\hat{p}_{x}=1$ when applied to the fitness function (7) with $n=40$

![img-12.jpeg](img-12.jpeg)

Fig. 11 Average number of generations and the corresponding confidence interval for a confidence level of $95 \%$ versus the size of the problem (7) relatively to 100 independent runs for cGA and the proposed operators. (Color figure online)
that there is a statistically significant difference between the convergence rate of the operators. The figure also shows that cGA scales worst, i.e., exhibits the higher growing rate in the average number of generations when the number of bits in (7) increases. On the hand, Algorithm 2 equipped with the proposed Bayesian operator is the fastest and has a growing rate that appear to be linear in the size of the problem. The absolute difference of the average number of generations between these two extreme cases is almost one order of magnitude for $n=50$. The other operators are within these two cases.

In the light of reproducible research, the source code in R programming language used for generating the presented results is publicly available at w3.ualg.pt/ jvo/pubs/NACO-S-14-00107

## 4 Main results

Assume that the population is described by a probability distribution $p: 2^{X} \rightarrow[0,1]$, where again $X=\left\{x_{1}, \ldots, x_{n}\right\}$. Then we can say that each $p$ defines a random set $\mathcal{A}$ together with the random variables $b_{\mathcal{A}}\left(x_{1}\right), \ldots, b_{\mathcal{A}}\left(x_{n}\right)$. One of the simplest assumptions one can make is to admit independent random variables $b_{\mathcal{A}}\left(x_{1}\right), \ldots, b_{\mathcal{A}}\left(x_{n}\right)$. This is the assumption found in univariate EDAs (Baluja 1994; Mühlenbein 1997; Harik et al. 1999). In this case the probability distribution $p$ is uniquely defined by the probabilities $p\left(x_{i}\right)=\operatorname{Pr}\left(b_{\mathcal{A}}\left(x_{i}\right)=1\right)$, and obviously $p(\mathcal{A})=$ $\prod_{x_{i} \in \mathcal{A}} p\left(x_{i}\right) \prod_{x_{i} \notin \mathcal{A}}\left(1-p\left(x_{i}\right)\right)$.

Now suppose we know that the fitness function $\mu$ can be approximated by a linear function $f$ :

$$
f(A)=\sum_{i=1}^{n} \alpha_{i} b_{A}\left(x_{i}\right)
$$

where $\alpha_{i}$ is a real number. For example, if we know the value of fitness function for two individuals $B$ and $C$, and that $\mu(B)>\mu(C)$, then we can define $\alpha_{i}=b_{B}\left(x_{i}\right)-b_{C}\left(x_{i}\right)$ stressing which variables in $B$ are better than in $C$.

We will analyze next the effect of applying the selection operator $\varphi$ to the $\operatorname{cdf} \hat{F}(B)=\sum_{f(A) \leqslant f(B)} p(A)$ that can be considered as an approximation of the cdf $F(B)=\sum_{p(A) \leqslant \mu(B)} p(A)$. We will show that under some assumptions on the selection operator $\varphi$, we can approximate the new probability distribution described by the $\operatorname{cdf} \varphi \circ \hat{F}$ using probabilities $p^{\prime}\left(x_{i}\right)$ of variables calculated by

$$
p^{\prime}\left(x_{i}\right)= \begin{cases}\varphi\left(p\left(x_{i}\right)\right), & \alpha_{i}<0 \\ p\left(x_{i}\right), & \alpha_{i}=0 \\ \psi\left(p\left(x_{i}\right)\right), & \alpha_{i}>0\end{cases}
$$

Now, let us evaluate the value $\hat{F}(B)$ for an arbitrary individual $B$. Without restricting generality, we can assume that $\alpha_{i} \leqslant 0$, i.e., $\emptyset$ is the best individual while $X$ is the worst. In this case $\mu(A) \leqslant \mu(B)$ for all $B \subseteq A$, therefore:

$$
\hat{F}(B)=\sum_{f(A) \leqslant f(B)} p(A) \geqslant \sum_{B \subseteq A} p(A)=\prod_{x_{i} \in B} p\left(x_{i}\right)
$$

Analogously, $f(A)>f(B)$ for all $A \subset B$, therefore, 1$\hat{F}(B)=\sum_{f(A)>f(B)} p(A) \geqslant \sum_{A \subset B} p(A)=\sum_{A \subseteq B} p(A)-$ $p(B)=\prod_{x_{i} \in X \backslash B}\left(1-p\left(x_{i}\right)\right)-p(B)$. Thus we have the following inequalities:

$$
\begin{aligned}
\prod_{x_{i} \in B} p\left(x_{i}\right) \leqslant \hat{F}(B) \leqslant & 1-\left(\prod_{x_{i} \in X \backslash B}\left(1-p\left(x_{i}\right)\right)\right) \\
& \times\left(1-\prod_{x_{i} \in B} p\left(x_{i}\right)\right)
\end{aligned}
$$

Observe that the upper bound is equal to the lower bound if $\prod_{x_{i} \in X \backslash B}\left(1-p\left(x_{i}\right)\right)=1$. Clearly, the above estimates are very rough and in the most cases $P(B)$ is considerably smaller than $\prod_{x_{i} \in X \backslash B}\left(1-p\left(x_{i}\right)\right)$. Therefore, for simplicity, we assume that $\hat{F}(B) \leqslant 1-\prod_{x_{i} \in X \backslash B}\left(1-p\left(x_{i}\right)\right)$. Now, consider the following problem. Let the mapping $\varphi:[0,1] \rightarrow$ $[0,1]$ be a selection operator, i.e., the cdf is defined as $\varphi \circ \hat{F}$ on the next generation. The question is how to approximate this probability distribution by a random set $\mathcal{A}^{\prime}$ assuming that random variables $b_{\mathcal{A}^{\prime}}\left(x_{1}\right), \ldots, b_{\mathcal{A}^{\prime}}\left(x_{n}\right)$ are independent? Let us denote $p^{\prime}\left(x_{i}\right)=\operatorname{Pr}\left(b_{\mathcal{A}^{\prime}}\left(x_{i}\right)=1\right)$. Clearly, if we use some approximation the algorithm has approximately, at least, the same convergence as the algorithm producing pure selection if

$$
\begin{aligned}
\varphi\left(\prod_{x_{i} \in B} p\left(x_{i}\right)\right) & \geqslant \prod_{x_{i} \in B} p^{\prime}\left(x_{i}\right), \quad \varphi\left(1-\prod_{x_{i} \in X \backslash B}\left(1-p\left(x_{i}\right)\right)\right) \\
& \leqslant 1-\prod_{x_{i} \in X \backslash B}\left(1-p^{\prime}\left(x_{i}\right)\right)
\end{aligned}
$$

Observe that if $\varphi(t)=t^{\mathrm{a}}$ then $\varphi\left(\prod_{x_{i} \in B} p\left(x_{i}\right)\right)=$ $\left(\prod_{x_{i} \in B} p\left(x_{i}\right)\right)^{\mathrm{a}}=\prod_{x_{i} \in B} p^{\mathrm{a}}\left(x_{i}\right)$, i.e., in this case at least for the lower bound the choice $p^{\prime}\left(x_{i}\right)=\varphi\left(p\left(x_{i}\right)\right)=p^{\mathrm{a}}\left(x_{i}\right)$ is justifiable. This allows us to conclude that we have a good approximation at least for the lower bound if a function $\varphi$ is close in some sense to the power function. Observe that the power function $\varphi(t)=t^{\mathrm{a}}$ obeys the following characteristic equation:
$\varphi^{q_{1}}\left(t_{1}\right) \cdot \varphi^{q_{2}}\left(t_{2}\right)=\varphi\left(t_{1}^{q_{1}} \cdot t_{2}^{q_{2}}\right)$.
If $q_{1} \in[0,1]$ and $q_{2}=1-q_{1}$ the expression
$\varphi\left(t_{1}^{q_{1}} \cdot t_{2}^{q_{2}}\right) \approx \varphi^{q_{1}}\left(t_{1}\right) \cdot \varphi^{q_{2}}\left(t_{2}\right)$
can be conceived as the interpolation of $\varphi$ in the point $t_{1}^{q_{1}} \cdot t_{2}^{q_{2}}$ by its values in points $t_{1}$ and $t_{2}$. Therefore, we can say that the function $\varphi:[0,1] \rightarrow[0,1]$ gives us the lower interpolation of the power function if

$$
\begin{aligned}
\varphi\left(t_{1}^{q} \cdot t_{2}^{1-q}\right) \leqslant & \varphi^{q}\left(t_{1}\right) \cdot \varphi^{1-q}\left(t_{2}\right) \text { for any } t_{1}, t_{2}, t_{1} \\
& +t_{2}, q \in[0,1]
\end{aligned}
$$

We can also analyze the required conditions for the selection operator considering the upper bound. In this case the inequality can be rewritten as
$\varphi\left(1-\prod_{x_{i} \in X \backslash B}\left(1-p\left(x_{i}\right)\right)\right) \geqslant 1-\prod_{x_{i} \in X \backslash B}\left(1-\varphi\left(p\left(x_{i}\right)\right)\right)$.
Using the auxiliary function $\psi(x)=1-\varphi(1-x)$ it is straightforward to rewrite the above inequality as
$\prod_{x_{i} \in X \backslash B} \psi\left(1-p\left(x_{i}\right)\right) \geqslant \psi\left(\prod_{x_{i} \in X \backslash B}\left(1-p\left(x_{i}\right)\right)\right)$
i.e., in this case it is desirable that the function $\psi$ should be the upper interpolation of power function:

$$
\begin{aligned}
\psi\left(t_{1}^{q} \cdot t_{2}^{1-q}\right) \geqslant & \psi^{q}\left(t_{1}\right) \cdot \psi^{1-q}\left(t_{2}\right) \text { for any } t_{1}, t_{2}, t_{1} \\
& +t_{2}, q \in[0,1]
\end{aligned}
$$

This choice is analyzed in the following lemma.
Lemma 2 Let $\varphi:[0,1] \rightarrow[0,1]$ be a selection operator. Then it satisfies Properties 2 and 3 of selection operators for $\psi(x)=1-\varphi(1-x)$ iff

1. the function $\gamma_{1}(y)=\ln \left(\varphi\left(e^{y}\right)\right)$ is convex on $(-\infty, 0]$;
2. the function $\gamma_{2}(y)=\ln \left(1-\varphi\left(1-e^{y}\right)\right)$ is concave on $(-\infty, 0]$.

Proof Let us show that (9) is equivalent to 1 . The inequality (9) can be rewritten as $\ln \left(\varphi\left(t_{1}^{q} \cdot t_{2}^{1-q}\right)\right) \leqslant$ $q \ln \left(\varphi\left(t_{1}\right)\right)+(1-q) \ln \left(\varphi\left(t_{2}\right)\right)$. Then after changing variables $t_{1}=e^{y_{1}}$ and $t_{2}=e^{y_{2}}$, we get the inequality
$\gamma_{1}\left(q y_{1}+(1-q) y_{2}\right) \leqslant q \gamma_{1}\left(y_{1}\right)+(1-q) \gamma_{2}\left(y_{2}\right)$
for all $y_{1}, y_{2}, y_{1}+y_{2} \leqslant 0$ and $q \in[0,1]$. This means the convexity of $\gamma_{1}$ in $(-\infty, 0]$. In the same way, one can show that (10) is equivalent to 2 .

Remark 3 The conditions formulated in statements 1 and 2 of Lemma 2 are different from those that define the convexity of $\varphi$ and the concavity of $f(x)=1-\varphi(1-x)$. To illustrate it, suppose that the function $\gamma_{1}(y)=\ln \left(\varphi\left(e^{y}\right)\right)$ is convex. Then it is equivalent to
$\gamma_{1}(x)+\gamma_{1}(y) \geqslant 2 \gamma_{1}\left(\frac{x+y}{2}\right)$,
or
$\varphi\left(e^{x}\right) \varphi\left(e^{y}\right) \geqslant \varphi^{2}\left(e^{\frac{2 y z}{2}}\right)$.
Denoting $a=e^{x}$ and $b=e^{y}$, we get $\varphi(a) \varphi(b) \geqslant \varphi^{2}(\sqrt{a b})$ for all $a, b \in[0,1]$. While the convexity of $\varphi$ on $[0,1]$ means that for all $a, b \in[0,1]$,

$$
\varphi(a)+\varphi(b) \geqslant 2 \varphi\left(\frac{a+b}{2}\right)
$$

Example 7 Let $\varphi(t)=a t^{2}+(1-a) t$, where $a \in[0,1]$. Then $\gamma_{1}(y)=\ln \left(a e^{2 y}+(1-a) e^{y}\right)$ and $\gamma_{2}(y)=\ln ((1+a)$ $\left.e^{y}-a e^{2 y}\right)$. In this case, $\frac{d^{2}}{d y^{2}} \gamma_{1}(y)=\frac{(1-a) a e^{y}}{\left(a e^{y}+(1-a)\right)^{2}} \geqslant 0$ for all $y \in(-\infty, 0]$ and $\frac{d^{2}}{d y^{2}} \gamma_{2}(y)=-\frac{(1+a) a e^{y}}{\left((1+a)-a e^{y}\right)^{2}} \leqslant 0$ for all $y \in(-\infty, 0]$, i.e., $\gamma_{1}$ is convex on $(-\infty, 0]$ and $\gamma_{2}$ is concave on $(-\infty, 0]$.

Example 8 Let $\varphi(t)=t^{\alpha}$, where $\alpha>1$. Then $\gamma_{1}(y)=\alpha y$, $\gamma_{2}(y)=\ln \left(1-e^{\alpha(1-y)}\right)$,
$\frac{d^{2}}{d y^{2}} \gamma_{2}(y)=-\frac{\alpha e^{\alpha}\left(1-e^{y}\right)^{\alpha}\left(\left(1-e^{y}\right)^{\alpha}+\alpha e^{\alpha}-1\right)}{\left(1-e^{y}\right)^{\alpha}\left(1-\left(1-e^{y}\right)^{\alpha}\right)^{2}} \leqslant 0$,
because all the involved factors are non-negative. For example, to prove that for all $y \in(-\infty, 0],\left(1-e^{y}\right)^{\alpha}+\alpha e^{\alpha}-$ $1 \geqslant 0$, start by denoting $x=1-e^{y}$ then the corresponding inequality is rewritten as $f(x)=x^{a}+\alpha(1-x)-1 \geqslant 0$, where $x \in[0,1]$. The minimum of this function on $[0,1]$ is $f(1)=0$. Therefore, $\gamma_{1}$ is convex on $(-\infty, 0]$ and $\gamma_{2}$ is concave on $(-\infty, 0]$.

Example 9 Let

$$
\varphi(t)= \begin{cases}\frac{b x}{a}, & x \in[0, a] \\ \frac{(1-b)(x-1)}{1-a}+1, & x \in(a, 1]\end{cases}
$$

where $0<b \leqslant a<1$. As $\varphi$ is a convex function,
$\frac{d^{2}}{d y^{2}} \gamma_{1}(y)=\frac{\left(1-\frac{1-b}{1-a}\right)\left(\frac{1-b}{1-a}\right) e^{y}}{\left(\left(\frac{1-b}{1-a}\right)\left(e^{y}-1\right)+1\right)^{2}}$
for $y \in(\ln a, 0]$ and $\frac{d^{2}}{d y^{2}} \gamma_{1}(y) \geqslant 0$ for $y \in(\ln a, 0]$ iff $a \leqslant b$, i.e., the condition 1 of Lemma 2 is fulfilled iff $a=b$ or equivalently $\varphi(t)=t, t \in[0,1]$. Analogously, one can show that condition 2) of Lemma 2 is fulfilled iff $a=b$ or equivalently $\varphi(t)=t, t \in[0,1]$.

The following theorems give the full description of functions that satisfy conditions of Lemma 2 under certain differentiable conditions.

Theorem 1 Let $\varphi:[0,1] \rightarrow[0,1]$ be an increasing and convex function such that
(a) $\varphi(0)=0, \varphi(1)=1$
(b) $\varphi$ is increasing, convex and differentiable on $[0,1]$;
(c) the function $\gamma_{1}(y)=\ln \left(\varphi\left(e^{y}\right)\right)$ is convex on $(-\infty, 0] ;$
(d) the function $\gamma_{2}(y)=\ln \left(1-\varphi\left(1-e^{y}\right)\right)$ is concave on $(-\infty, 0] ;$
(e) $F(x)=\frac{\varphi^{\prime}(x) x}{\varphi(x)}$ is defined and differentiable on $[0,1]$. Here we assume that $F(0)=\lim _{x \rightarrow 0} F(x)=a$. Then for $a \geqslant 1, F$ is an increasing function on $[0,1]$ and $\varphi$ can be represented as
$\varphi(x)=x^{a}\left(\frac{e^{\int \frac{x_{0} d d y}{y}} d y}{\int \frac{x_{0} d x_{0}}{y} d y}\right)$
where $F_{0}(y)=F(y)-a$.
Conversely, let $F_{0}:[0,1] \rightarrow[0,+\infty)$ be an increasing and differentiable function in $[0,1]$ with $F_{0}(0)=0$. Then any function $\varphi$ defined by (11) satisfies the conditions (a)-(e) for $a \geqslant 1$.

Proof See "Appendix".
We will use also the following counterpart of Theorem 1.

Theorem 1* Let $\psi:[0,1] \rightarrow[0,1]$ be an increasing and concave function such that
(a) $\psi(0)=0, \psi(1)=1$
(b) $\psi$ is increasing, concave and differentiable on $[0,1]$;
(c) the function $\gamma_{1}(y)=\ln \left(\psi\left(e^{y}\right)\right)$ is concave on $(-\infty, 0]$
(d) the function $\gamma_{2}(y)=\ln \left(1-\psi\left(1-e^{y}\right)\right)$ is convex on $(-\infty, 0]$
(e) $F(x)=\frac{\varphi^{\prime}(x) x}{\varphi(x)}$ is defined and differentiable on $[0,1]$. Again, assume that $F(0)=\lim _{x \rightarrow+0} F(x)=a$.
Then for $0<a \leqslant 1, F$ is an increasing function on $[0,1]$ and $\varphi$ can be represented as
$\varphi(x)=x^{a}\left(\frac{e^{\int \frac{x_{0} d x_{0}}{y}} d y}{\int \frac{x_{0} d x_{0}}{y} d y}\right)$
where $F_{0}(y)=F(y)-a$.
Conversely, let $F_{0}:[0,1] \rightarrow(-\infty, 0]$ be an decreasing and differentiable function on $[0,1]$ with $F_{0}(0)=0$ and $F(1) \geqslant-a$. Then any function $\varphi$ defined by (12) satisfies the conditions (a)-(e) for $0<a \leqslant 1$.

Proof Follows the same path as the proof of Theorem 1 and is omitted for brevity.

Proposition 1 The inequality

$\varphi\left(\prod_{x_{i} \in B} p\left(x_{i}\right)\right) \geqslant \prod_{x_{i} \in B} \varphi\left(p\left(x_{i}\right)\right)$
is satisfied for a selection operator $\varphi$ if the function $g(y)=$ $\gamma_{1}(y) / y$ is increasing in $(-\infty, 0]$, where $\gamma_{1}(y)=\ln \left(\varphi\left(e^{y}\right)\right)$.
Proof Take the logarithm from both sides of inequality (13) and let $e^{y_{i}}=p\left(x_{i}\right)$. Then the inequality (13) can be rewritten as
$f\left(\sum_{x_{i} \in B} y_{i}\right) \geqslant \sum_{x_{i} \in B} f\left(y_{i}\right)$
or
$\left(\sum_{x_{i} \in B} y_{i}\right) g\left(\sum_{x_{i} \in B} y_{i}\right)=\sum_{x_{i} \in B} y_{i} g\left(\sum_{x_{i} \in B} y_{i}\right) \geqslant \sum_{x_{i} \in B} y_{i} g\left(y_{i}\right)$
Notice that the function $g$ is non-negative in $(-\infty, 0]$ and $g\left(\sum_{x_{i} \in B} y_{i}\right) \leqslant g\left(y_{i}\right)$ by our assumption, i.e., $y_{i} g\left(\sum_{x_{i} \in B} y_{i}\right) \geqslant y_{i} g\left(y_{i}\right)$. This implies that the inequality (14) is valid.

Proposition 2 The inequality

$$
\prod_{x_{i} \in X \backslash B} \psi\left(1-p\left(x_{i}\right)\right) \leqslant \psi\left(\prod_{x_{i} \in X \backslash B}\left(1-p\left(x_{i}\right)\right)\right)
$$

is satisfied for a function $\psi$ if the function $g(y)=\gamma_{1}(y) / y$ is increasing in $(-\infty, 0]$, where $\gamma_{1}(y)=\ln \left(\psi\left(e^{y}\right)\right)$.
Proof This follows the same reasoning of the proof of Proposition 1 and is omitted for brevity.
Corollary 1 (1) A selection operator $\varphi$ obeys the inequality (13) if the function $g_{1}(x)=\frac{\ln \varphi(x)}{\ln x}$ is increasing, and (2) it obeys the inequality (15) for $\psi(x)=1-\varphi(1-$ $x)$ if the function $g_{2}(x)=\frac{\ln (1-\varphi(x))}{\ln (1-x)}$ is increasing.

Proof The first statement follows directly from Proposition 1 after putting $y=\ln x$ in function $g$. Analogously, Proposition 2 implies that the inequality (15) is valid if the function $g_{2}(1-x)=\frac{\ln (1-\psi(1-x))}{\ln x}$ is decreasing, i.e., $g_{2}$ is an increasing function.

Corollary 2 Let the operators $\varphi$ and $\psi$ obey the conditions of Theorem 1 and Theorem 1*, respectively. Then the inequalities (13) and (15) are also respectively satisfied.

Proof Let a selection operator $\varphi$ obey the conditions of Proposition 1. Then it can be represented as $\varphi(x)=x e^{g_{1}(x)}$, where $g_{1}$ is an increasing function. We can derive the
analogous representation if the selection operator $\varphi$ obey the conditions of Theorem 1. Actually, in this case $\varphi(x)=x e^{(a-1) \ln x+\int_{0}^{L_{0}(x)} d y-A}$, where $a \geqslant 1, F_{0}$ is an increasing function with $F_{0}(0)=0$, and $A=\int_{0}^{1} \frac{F_{0}(y)}{y} d y$. We see that in this case $g_{1}(x)=(a-1) \ln x+\int_{0}^{x} \frac{F_{0}(y)}{y} d y-A$ is an increasing function, i.e., the inequality (13) is fulfilled by Proposition 1.

Let a selection operator $\varphi$ obey the conditions of Proposition 2. Then the function $\psi(x)=1-\varphi(1-x)$ can be represented as $\psi(x)=x e^{g_{2}(x)}$, where $g_{2}$ is a decreasing function. We can derive the analogous representation if the selection operator $\varphi$ obeys the conditions of Theorem 1*. Actually, in this case $\psi(x)=x e^{(a-1) \ln x+\int_{0}^{L_{0}(x)} d y-A}$, where $0<a \leqslant 1, F_{0}$ is a decreasing function with $F_{0}(0)=0$ and $F_{0}(1) \leqslant a$, and $A=\int_{0}^{1} \frac{F_{0}(y)}{y} d y$. We see that in this case $g_{2}(x)=(a-1) \ln x+\int_{0}^{x} \frac{F_{0}(y)}{y} d y-A$ is a decreasing function, i.e., the inequality (15) is fulfilled by Proposition 2.

Remark 4 It is possible to weaken the second part of Theorem 1. Namely, if $F_{0}:[0,1] \rightarrow[0,+\infty)$ is an increasing function on $[0,1]$ with $F_{0}(0)=0$. Then any function $\varphi$ defined by (10) satisfies the conditions a)-d) for $a \geqslant 1$. For example, if we take
$F_{0}(x)=\left\{\begin{array}{ll}0, & x \in[0, b], \\ c, & x \in(b, 1],\end{array}\right.$
where $b \in[0,1]$ and $c>0$. Then
$\varphi(x)=\left\{\begin{array}{ll}b^{c} x^{a}, & x \in[0, b], \\ x^{a+c}, & x \in(b, 1] .\end{array}\right.$
Remark 5 Theorem 1 gives us also a simple way to check conditions (b)-(d). To do this, it is sufficient to check whether function $F$ is increasing and $F(0) \geqslant 1$.

Consider the case where (8) verifies $\alpha_{1}<\alpha_{2}<\cdots<\alpha_{n}<0$ and $\sum_{k=i+1}^{n} \alpha_{k}>\alpha_{i}$ for any $i=1, \ldots, n-1$. Then $f(A)<f(B)$ iff $b_{A}\left(x_{i}\right)=b_{B}\left(x_{i}\right)$ for $i=1, \ldots, k-1$, but $b_{A}\left(x_{i}\right)=1$ and $b_{B}\left(x_{i}\right)=0$ for $i=k$. Consider an increasing sequence of sets $\left\{C_{k}\right\}_{k=1}^{n}$, such that $C_{k}=\left\{x_{1}, \ldots, x_{k}\right\}$. Then the above condition can be rewritten as $f(A)<f(B)$ iff there is a $k \in\{1, \ldots, n\}$ such that $A \cap C_{k-1}=B \cap C_{k-1}$ and $A \cap C_{k} \supset B \cap C_{k}$. Therefore,
$\{B \mid f(A)<f(B)\}=\bigcup_{k \mid x_{k} \in A}\left\{B \mid B \cap C_{k-1}=A \cap C_{k-1}, x_{k} \notin B\right\}$.

We see that

$$
\begin{aligned}
& P\left(\left\{B \mid B \cap C_{k-1}=A \cap C_{k-1}, x_{k} \notin B\right\}\right) \\
& \quad=\left(1-p\left(x_{k}\right)\right) \prod_{x_{i} \in A \cap C_{k-1}} p\left(x_{i}\right) \prod_{x_{i} \in C_{k-1} \backslash A}\left(1-p\left(x_{i}\right)\right)
\end{aligned}
$$

Since sets $\left\{B \mid B \cap C_{k-1}=A \cap C_{k-1}, x_{k} \notin B\right\}$ are disjoint for different $x_{k} \in A$, we get

$$
\begin{aligned}
& P(\{B \mid f(A)<f(B)\}) \\
& \quad=\sum_{k \mid x_{k} \in A}\left(1-p\left(x_{k}\right)\right) \prod_{x_{i} \in A \cap C_{k-1}} p\left(x_{i}\right) \prod_{x_{i} \notin C_{k-1} \backslash A}\left(1-p\left(x_{i}\right)\right)
\end{aligned}
$$

or

$$
\begin{aligned}
\hat{F}(B)= & \sum_{f(A) \in f(B)} p(A)=1-\sum_{k \mid x_{k} \in B}\left(1-p\left(x_{k}\right)\right) \\
& \prod_{x_{i} \in B \cap C_{k-1}} p\left(x_{i}\right) \prod_{x_{i} \in C_{k-1} \backslash B}\left(1-p\left(x_{i}\right)\right)
\end{aligned}
$$

In particular,
$\hat{F}\left(\left\{x_{k}\right\}\right)=\sum_{f(A) \in f(B)} p(A)=1-\prod_{i=1}^{k}\left(1-p\left(x_{i}\right)\right)$,
and if $B=\left\{x_{k+1}, \ldots, x_{n}\right\}$, then
$\hat{F}(B)=1-\left(\prod_{x_{i} \in X \backslash B}\left(1-p\left(x_{i}\right)\right)\right)\left(1-\prod_{x_{i} \in B} p\left(x_{i}\right)\right)$
In this case the upper bound of $\hat{F}(B)$ calculated above is achieved.

For this ordering, it is also possible to get another formula for $F$. This is derived from:

$$
\{A \mid f(A)<f(B)\}=\bigcup_{k \mid x_{k} \notin B}\left\{A \mid B \cap C_{k-1}=A \cap C_{k-1}, x_{k} \in A\right\}
$$

Clearly,

$$
\begin{aligned}
& P\left(\left\{A \mid B \cap C_{k-1}=A \cap C_{k-1}, x_{k} \in A\right\}\right) \\
& \quad=p\left(x_{k}\right) \prod_{x_{i} \in B \cap C_{k-1}} p\left(x_{i}\right) \prod_{x_{i} \in C_{k-1} \backslash B}\left(1-p\left(x_{i}\right)\right)
\end{aligned}
$$

and $\left\{A \mid B \cap C_{k-1}=A \cap C_{k-1}, x_{k} \in A\right\}$ are disjoint for different $x_{k} \notin B$. Therefore,

$$
\begin{aligned}
& P(\{A \mid f(A)<f(B)\}) \\
& \quad=\sum_{k \mid x_{k} \notin B} p\left(x_{k}\right) \prod_{x_{i} \in B \cap C_{k-1}} p\left(x_{i}\right) \prod_{x_{i} \in C_{k-1} \backslash B}\left(1-p\left(x_{i}\right)\right)
\end{aligned}
$$

and

$$
\begin{aligned}
\hat{F}(B)= & \sum_{f(A) \in f(B)} p(A)=\sum_{k \mid x_{k} \notin B} p\left(x_{k}\right) \prod_{x_{i} \in B \cap C_{k-1}} p\left(x_{i}\right) \\
& \prod_{x_{i} \in C_{k-1} \backslash B}\left(1-p\left(x_{i}\right)\right)+P(B)
\end{aligned}
$$

In particular,
$\hat{F}\left(X \backslash\left\{x_{k}\right\}\right)=\prod_{i=1}^{k} p\left(x_{k}\right)+P\left(X \backslash\left\{x_{k}\right\}\right)$
and
$\hat{F}\left(\left\{x_{1}, \ldots, x_{k}\right\}\right)=\prod_{i=1}^{k} p\left(x_{k}\right)$,
i.e., in this case the lower bound of $\hat{F}(B)$ calculated above is achieved.

Assume that $\alpha_{1}=\alpha_{2}=\cdots=\alpha_{n}=-1$. Then $f(A) \leqslant$ $f(B)$ if $|A| \geqslant|B|$. Therefore,
$\hat{F}(B)=\sum_{f(A) \in f(B)} p(A)=\sum_{|A| \geqslant|B|} \prod_{x_{i} \in A} p\left(x_{i}\right) \prod_{x_{i} \notin A}\left(1-p\left(x_{i}\right)\right)$.
In particular, a random value $f$ has a binomial distribution if $p\left(x_{i}\right)=a$ for all $i \in\{1, \ldots, n\}$. Observe that in this case the function $\hat{F}$ may be approximated by a cdf of a normal distribution. For this case, we have
$\hat{F}(B)=\sum_{f(A) \in f(B)} p(A) \approx \Phi\left(\frac{x+n a}{\sqrt{n a(1-a)}}\right)$
where again $\Phi$ is the cdf of the standard normal distribution. Expression (16) can be interpreted in another way. Instead of approximating $\hat{F}$, we can approximate first independent random variables $b_{A}\left(x_{1}\right), \ldots, b_{A}\left(x_{n}\right)$ by continuous independent random variables $\xi_{1}, \ldots, \xi_{n}$, distributed normally with means equal to $a$ and variances equal to $\sigma^{2}=a(1-a)$. Then we approximate
$f(\mathcal{A})=\sum_{i=1}^{n} \alpha_{i} b_{A}\left(x_{i}\right) \approx \sum_{i=1}^{n} \alpha_{i} \xi_{i}$.
Observe that a random variable $\xi=\sum_{i=1}^{n} \alpha_{i} \xi_{i}$ has normal distribution with a mean $\sum_{i=1}^{n} \alpha_{i} a=-n a$ and a variance $\sum_{i=1}^{n} \alpha_{i}^{2} \sigma^{2}=n \sigma^{2}$, i.e., in this case we get (16) again. Using the same approximation, but for the general case, when $\alpha_{i}$ and $p\left(x_{i}\right)$ are arbitrary, we obtain
$\hat{F}(B) \approx \Phi\left(\frac{x-\sum_{i=1}^{n} \alpha_{i} p\left(x_{i}\right)}{\sqrt{\sum_{i=1}^{n} \alpha_{i}^{2} p\left(x_{i}\right)\left(1-p\left(x_{i}\right)\right)}}\right)$
The conditions under which this expression is justifiable can be found in the various generalizations of the central limit theorem.

In the same vein, it is of interest the problem of describing all justifiable selection operators that map any normal distribution to another normal distribution. Let us remind that any cdf of normally distributed random value $\xi$ can be represented as $F(x)=\Phi((x-a) / \sigma)$, where $a$ is the mean value of $\xi$, and $\sigma^{2}$ is its variance. The selection operator $\varphi:[0,1] \rightarrow[0,1]$ with $\varphi(0)=0$ and $\varphi(1)=1$ that

maps $\operatorname{cdf} \Phi\left(\left(x-a_{1}\right) / \sigma_{1}\right)$ to $\operatorname{cdf} \Phi\left(\left(x-a_{2}\right) / \sigma_{2}\right)$ can be found as a solution of the following equation:
$\varphi\left(\Phi\left(\left(x-a_{1}\right) / \sigma_{1}\right)\right)=\Phi\left(\left(x-a_{2}\right) / \sigma_{2}\right)$.
Let us denote $z=\Phi\left(\left(x-a_{1}\right) / \sigma_{1}\right)$. Then $x=\sigma_{1} \Phi^{-1}(z)+$ $a_{1}$ and
$\varphi(z)=\Phi\left(\alpha+\beta \Phi^{-1}(z)\right)$
where $\alpha=\left(a_{1}-a_{2}\right) / \sigma_{2}$ and $\beta=\sigma_{1} / \sigma_{2}$. Notice that by using a selection operator we are searching for a maximum of the function $\mu$ while simultaneously attempt to reduce of search region, this implies that $a_{2}>a_{1}$ and $\sigma_{1} \geqslant \sigma_{2}$, i.e., $\alpha<0$ and $\beta \geqslant 1$. The next proposition establishes when such a $\varphi$ has desirable properties.

Proposition 3 Let $\varphi:[0,1] \rightarrow[0,1]$ be defined by (17). Then $\varphi$ is a selection operator and it satisfies the conditions of Theorem 1 iff $\alpha<0$ and $\beta=1$.

Proof See "Appendix".
Let us analyze the consequences of Proposition 3. Let $f(\mathcal{A})=\sum_{i=1}^{n} \alpha_{i} b_{\mathcal{A}}\left(x_{i}\right)$, with $\alpha_{i}<0, i=1, \ldots, n$. Assume the cdfs
$F_{i}(t)=\operatorname{Pr}\left\{\alpha_{i} b_{\mathcal{A}}\left(x_{i}\right) \leqslant t\right\}= \begin{cases}0, & t<\alpha_{i} \\ p\left(x_{i}\right), & \alpha_{i} \leqslant t<0 \\ 1, & t \geqslant 0\end{cases}$
and apply the selection operator $\varphi$ to $F_{i}$ to produce the cdf
$\varphi \circ F_{i}(t)=\operatorname{Pr}\left\{\alpha_{i} b_{\mathcal{A}}\left(x_{i}\right) \leqslant t\right\}= \begin{cases}0, & t<\alpha_{i} \\ \varphi\left(p\left(x_{i}\right)\right), & \alpha_{i} \leqslant t<0 \\ 1, & t \geqslant 0\end{cases}$
Notice that in Algorithm 2 we approximate the probability distribution after selection by probabilities $\left(\varphi\left(p\left(x_{i}\right)\right)\right.$, $\left.1-\varphi\left(p\left(1-x_{i}\right)\right)\right)$, i.e., we show that our approximation of applying the selection operator is produced by applying the same selection operator to random variables $\alpha_{i} b_{\mathcal{A}}\left(x_{i}\right)$. Let us assume that we approximate random variables $\alpha_{1} b_{\mathcal{A}}\left(x_{1}\right)$, $\ldots, \alpha_{n} b_{\mathcal{A}}\left(x_{n}\right)$ by independent normally distributed random variables $\xi_{1}, \ldots, \xi_{n}$ and $\xi=\sum_{i=1}^{n} \xi_{i}$. Let $a_{i}$ be a mean value of $\xi_{i}$ and $\sigma_{i}^{2}$ be its variance. Then the application of the selection operator $\varphi$ to the cdf of $\xi_{i}$ means that we obtain a new normally distributed random variable $\xi_{i}^{\prime}$ with mean value $a_{i}^{\prime}=a_{i}-\alpha \sigma_{i}$ and with variance $\sigma_{i}^{2}$. Analogously, the normally distributed random variable $\xi$ has the mean value $a=\sum_{i=1}^{n} a_{i}$ and the variance $\sigma^{2}=\sum_{i=1}^{n} \sigma_{i}^{2}$ and after applying the selection operator to its cdf, we get the normally distributed random variable $\xi^{\prime}$ with the mean value $a^{\prime}=$ $a-\alpha \sigma$ and variance $\sigma^{2}$. Let us consider the sum $\xi^{\prime \prime}=\sum_{i=1}^{n} \xi_{i}^{\prime}$. This normally distributed random variable has a mean value $a^{\prime \prime}=a-\alpha \sum_{i=1}^{n} \sigma_{i}$ and variance $\sigma^{2}$.

Notice that $a^{\prime \prime}>a^{\prime}$ since $\sigma^{2}=\sum_{i=1}^{n} \sigma_{i}^{2} \leqslant\left(\sum_{i=1}^{n} \sigma_{i}\right)^{2}$ and $\alpha<0$.

## 5 Conclusions

Estimation of distribution algorithms (EDAs) are stochastic population-based optimizers that combine techniques of machine learning and evolutionary computation. Currently there is a wealth of EDAs and many applications have been reported. However relatively less theoretical results are available.

In this paper, the role of the selection operation on the updating of the probability distribution was thoroughly investigated. Necessary conditions for an operator to model selection in such a way that it can be directly used for updating the probability model were postulated. A family of such operators was proposed. The properties of these operators were thoroughly analyzed, including a study on the equivalence of operators. The proposed operators were shown to generalize existing operators, namely they generalize both the operator used in the cGA and the updating operator used in the PBIL algorithm. As an application example in algorithm design, a generalization of cGA was presented. As our main theoretical results a comprehensive theoretical rationale for the proposed operators and for their application to univariate EDA design was provided.

Examples aiming at illustrating key concepts, main results, and their relevance were presented. These include simulation studies revealing some empirical evidence on the convergence rate, convergence reliability, and scalability of the proposed operators. While it should be clear that the merit of an operator depends on the optimization problem, our studies reveal that, when equipped with a selection of the proposed operators, the presented generalized cGA was able to outperform cGA in two different optimization problems under different parametrization and problem sizes.

Although the presented results are mainly for the univariate case, these can also be used for extending some multivariate EDAs, specially those relying in clustering for obtaining groups of variables where intra group independence is reasonable to assume.

Acknowledgments Andrey Bronevich is grateful to the Erasmus Mundus Triple I Consortium that supported a 10-months academic visit to the University of Algarve in 2010. This work is an outcome of a research cooperation between the authors that began with this visit. Andrey Bronevich also thanks the National Research University Higher School of Economics, Moscow, Russia for providing him with 1 month research grant for visiting University of Algarve in July 2014 facilitating the conclusion of the work. José Valente de Oliveira also thanks the National Research University Higher School of Economics, for inviting him for one week visit in November 2014.

## Appendix

Proof of Theorem 1 Under conditions (a)-(e) function $\gamma_{1}$ is differentiable in $(-\infty, 0]$ and its convexity implies that $\frac{d}{d y} \gamma_{1}(y)=\frac{\varphi^{\prime}\left(e^{x}\right) e^{y}}{\varphi\left(e^{x}\right)}$
is increasing in $(-\infty, 0]$. This is obviously equivalent to have $F(x)=\frac{\varphi^{\prime}(x)}{\varphi(x)}$ as an increasing function in $(0,1]$. Solving this differential equation w.r.t. $\varphi$ we see that the function $\varphi$ can be expressed as $\varphi(x)=C x^{a} e^{\int \frac{F_{0}(x)}{x} d y}$, where an arbitrary constant $C$ should be chosen such that $\varphi(1)=1$, i.e., $C=e^{-\int \frac{F_{0}(x)}{x} d y}$.

Let us show that the value $a \geqslant 1$ (clearly $a>0$ in order to have $\varphi(0)=0$ ). Denote $\varphi_{0}(x)=C e^{\int \frac{F_{0}(x)}{x} d y}$. Then

$$
\begin{aligned}
\varphi(x) & =x^{a} \varphi_{0}(x) \\
\varphi^{\prime}(x) & =x^{a} \varphi_{0}^{\prime}(x)+a x^{a-1} \varphi_{0}(x) \\
& =x^{a-1} \varphi_{0}(x) F_{0}(x)+a x^{a-1} \varphi_{0}(x) \\
& =x^{a-1} \varphi_{0}(x)\left(F_{0}(x)+a\right) \\
\varphi^{\prime \prime}(x) & =\varphi^{\prime}(x)\left(\frac{a-1}{x}+\frac{\varphi_{0}^{\prime}(x)}{\varphi_{0}(x)}+\frac{F_{0}^{\prime}(x)}{F_{0}(x)+a}\right) \\
& =\varphi^{\prime}(x)\left(\frac{a-1}{x}+\frac{F_{0}(x)}{x}+\frac{F_{0}^{\prime}(x)}{F_{0}(x)+a}\right)
\end{aligned}
$$

Therefore, if $a-1<0$ then $\varphi^{\prime \prime}(x)<0$ for some values that are close to 0 , since $\lim _{x \rightarrow+0}\left(\frac{F_{0}(x)}{x}\right)^{\frac{a-1}{x}} \int=0$. This means that $a \geqslant 1$.

For the second part of the theorem, if we choose the function $F_{0}$ as stated by the theorem, then conditions (a)(c), and (e) are obviously satisfied. It remains to show that (d) is also satisfied. Function $\gamma_{2}(y)=\ln \left(1-\varphi\left(1-e^{y}\right)\right)$ is differentiable and the function
$\frac{d}{d y} \gamma_{2}(y)=-\frac{\varphi^{\prime}\left(1-e^{y}\right) e^{y}}{1-\varphi\left(1-e^{y}\right)}$
should be decreasing. This is equivalent to
$g(x)=\frac{\varphi^{\prime}(x)(1-x)}{1-\varphi(x)}$
be an increasing function. Substituting $\varphi(x)=x^{a} \varphi_{0}(x)$, $\varphi^{\prime}(x)=x^{a-1} \varphi_{0}(x)\left(F_{0}(x)+a\right)$, we get
$g(x)=\frac{x^{a-1} \varphi_{0}(x)\left(F_{0}(x)+a\right)(1-x)}{1-x^{a} \varphi_{0}(x)}$.
Then

$$
\begin{aligned}
g^{\prime}(x)= & g(x)\left(\frac{a-1}{x}+\frac{\varphi_{0}(x)}{\varphi_{0}^{\prime}(x)}+\frac{F_{0}^{\prime}(x)}{F_{0}(x)+a}\right. \\
& \left.+\frac{x^{a-1} \varphi_{0}(x)\left(F_{0}(x)+a\right)}{1-x^{a} \varphi_{0}(x)}-\frac{1}{1-x}\right)
\end{aligned}
$$

Notice that
$\frac{\varphi_{0}(x)}{\varphi_{0}^{\prime}(x)}=\frac{F_{0}(x)}{x}$
$\frac{x^{a-1} \varphi_{0}(x)\left(F_{0}(x)+a\right)}{1-x^{a} \varphi_{0}(x)}=\frac{F_{0}(x)+a}{x\left(1-x^{a} \varphi_{0}(x)\right)}-\frac{F_{0}(x)+a}{x}$.
Therefore,
$g^{\prime}(x)=g(x)\left(\frac{F_{0}^{\prime}(x)}{F_{0}(x)+a}+\frac{F_{0}(x)+a}{x\left(1-x^{a} \varphi_{0}(x)\right)}-\frac{1}{x(1-x)}\right)$.
Because $\varphi_{0}(x) \leqslant 1$ and $F_{0}(x) \geqslant 0, F_{0}^{\prime}(x) /\left(F_{0}(x)+a\right) \geqslant 0$, we get
$g^{\prime}(x) \geqslant g(x)\left(\frac{a}{x\left(1-x^{a}\right)}-\frac{1}{x(1-x)}\right)$.
We see that
$\frac{a}{x\left(1-x^{a}\right)}-\frac{1}{x(1-x)}=\frac{x^{a}+a(1-x)-1}{x\left(1-x^{a}\right)(1-x)} \geqslant 0$,
where the inequality $x^{a}+a(1-x)-1 \geqslant 0$ for $a \geqslant 1$ and $x \in[0,1]$ is proved as in Example 3, i.e., $g^{\prime}(x) \geqslant 0$ and the condition d) is also fulfilled.

Proof of Proposition 3 We will use the notation from Theorem 1. Computing the function $g$ for this case, we get
$g(x)=\frac{\beta \Phi^{\prime}\left(\alpha+\beta \Phi^{-1}(x)\right) x}{\Phi^{\prime}\left(\Phi^{-1}(x)\right) \Phi\left(\alpha+\beta \Phi^{-1}(x)\right)}$
Let us compute the limit $b=\lim _{x \rightarrow+0} g(x)$, involving a new variable $y=\Phi^{-1}(x)$ :
$b=\lim _{y \rightarrow-\infty} \frac{\beta \Phi^{\prime}(\alpha+\beta y) \Phi(y)}{\Phi^{\prime}(y) \Phi(\alpha+\beta y)}=\beta \lim _{y \rightarrow-\infty} \frac{e^{-\frac{(y+\beta y)^{2}-y^{2}}{2}} \Phi(y)}{\Phi(\alpha+\beta y)}$
Obviously, $b=1$ for $\beta=1$. Applying the L'Hospital rule for the general case, one can obtain that $b=\beta^{2}$, i.e., we conclude that $\beta \geqslant 1$.

Let us check now when $g$ is an increasing function. This condition is equivalent to the non-negativity of the derivative
$f(y)=\frac{d}{d y} \ln \left(\frac{\beta \Phi^{\prime}(\alpha+\beta y) \Phi(y)}{\Phi^{\prime}(y) \Phi(\alpha+\beta y)}\right)$
for any $y \in(-\infty,+\infty)$. Making simple calculations, we get

$$
\begin{aligned}
f(y) & =\beta \frac{\Phi^{\prime \prime}(\alpha+\beta y)}{\Phi^{\prime}(\alpha+\beta y)}+\frac{\Phi^{\prime}(y)}{\Phi(y)}-\frac{\Phi^{\prime}(y)}{\Phi^{\prime \prime}(y)}-\beta \frac{\Phi^{\prime}(\alpha+\beta y)}{\Phi(\alpha+\beta y)} \\
& =-\alpha \beta-\left(\beta^{2}-1\right) y+\frac{\Phi^{\prime}(y)}{\Phi(y)}-\beta \frac{\Phi^{\prime}(\alpha+\beta y)}{\Phi(\alpha+\beta y)}
\end{aligned}
$$

Notice that $\lim _{y \rightarrow+\infty} f(y)=-\infty$ for $\beta>1$ and $\lim _{y \rightarrow+\infty} f(y)=$ $-\alpha$ for $\beta=1$, therefore, the function $\varphi$ can satisfy the conditions of Theorem 1 if $\alpha<0$ and $\beta=1$. For this case we can represent the function $f$ in the form $f(y)=$ $w(y)-w(y+\alpha)$, where $w(y)=y+\frac{\Phi^{\prime}(y)}{\Phi(y)}$ and $f(y) \geqslant 0$ for all $y \in \mathbb{R}$ and $\alpha<0$, if $\frac{d w}{d y} \geqslant 0$. Let us denote $u(y)=\frac{\Phi^{\prime}(y)}{\Phi(y)}$. The function $u$ can be conceived as a partial solution of the Bernoulli differential equation $\frac{d u}{d y}=-u y-u^{2}$. This equation and the condition $\frac{d w}{d y}=\frac{d u}{d y}+1 \geqslant 0$ imply that the function $f$ is increasing iff $\frac{d u}{d y}=-u y-u^{2} \geqslant-1$ or, taking in account that the function $u$ is non-negative, that

$$
u \leqslant \frac{-y+\sqrt{y^{2}+4}}{2}
$$

By expressing the last inequality in terms of $\operatorname{cdf}$ for the standard normal distribution one gets:

$$
\Phi(y) \geqslant \frac{2}{\left(-y+\sqrt{y^{2}+4}\right) \sqrt{2 \pi}} e^{-\frac{y^{2}}{2}}=\frac{\left(y+\sqrt{y^{2}+4}\right)}{2 \sqrt{2 \pi}} e^{-\frac{y^{2}}{2}}
$$

which implies
$\frac{d}{d y} \Phi(y) \geqslant \frac{d}{d y} \frac{\left(y+\sqrt{y^{2}+4}\right)}{2 \sqrt{2 \pi}} e^{-\frac{y^{2}}{2}}$ for all $y \in \mathbb{R}$,
or
$\frac{1}{\sqrt{2 \pi}} e^{-\frac{y^{2}}{2}} \geqslant \frac{1}{2 \sqrt{2 \pi}} e^{-\frac{y^{2}}{2}}\left(1+\frac{y}{\sqrt{y^{2}+4}}-y^{2}-y \sqrt{y^{2}+4}\right)$
or
$1 \geqslant \frac{1}{2}\left(1+\frac{y}{\sqrt{y^{2}+4}}-y^{2}-\frac{y\left(y^{2}+4\right)}{\sqrt{y^{2}+4}}\right)$
Now denote $v=y / \sqrt{y^{2}+4}$. Then $y^{2}=4 v^{2} /\left(1-v^{2}\right)$ and we get:

$$
\begin{aligned}
& 1 \geqslant \frac{1}{2}\left(1+v-\frac{4 v^{2}}{1-v^{2}}-v\left(4+\frac{4 v^{2}}{1-v^{2}}\right)\right) \\
& =\frac{1}{2}\left(1-3 v-\frac{4 v^{2}}{1-v^{2}}(1+v)\right)
\end{aligned}
$$

We proceed taking in to account that $|v|<1$ :

$$
1 \geqslant-3 v-\frac{4 v^{2}}{1-v}
$$

or

$$
v^{2}+2 v+1 \geqslant 0
$$

As this inequality is satisfied for all real $v$ we conclude that $g$ is an increasing function and that the function $\varphi$ satisfies the conditions of Theorem 1 for $\alpha<0$ and $\beta=1$.

## References

Baluja S (1994) Population-based incremental learning: a method for integrating genetic search based function optimization and competitive learning. Technical report CMU-CS-94-13. Carnegie Mellon University, Pittsburgh, Pennsylvania, USA
Baluja S, Davies S (1997) Using optimal dependency-trees for combinatorial optimization: learning the structure of the search space. In: Proceedings of the 14-th International Conference on Machine Learning. San Francisco, California, USA, pp 30-38
Bengoetxea E, Larrañaga P, Bloch I, Perchant A, Boeres C (2002) Inexact graph matching by means of estimation of distribution algorithms. Pattern Recognit 35(12):2867-2880
Ceberio J, Irurozki E, Mendiburu A, Lozano JA (2012) A review on estimation of distribution algorithms in permutation-based combinatorial optimization problems. Prog AI 1(1):103-117
De Bonet JS, Isbell CL, Viola P (1997) MIMIC: finding optima by estimating probability densities. In: Petsche T, Mozer MC, Jordan MI (eds) Advances in neural information processing systems. MIT Press, Cambridge, pp 424-430
Droste S (2006) A rigorous analysis of the compact genetic algorithm for linear functions. Nat Comput 5:257-283
Echegoyen C, Mendiburu A, Santana R, Lozano JA (2013) On the taxonomy of optimization problems under estimation of distribution algorithms. Evolut Comput 21(3):471-495
Emmendorfer LR, Pozo AT (2009) Effective linkage learning using low-order statistics and clustering. IEEE Trans Evolut Comput 13(6):1233-1246
González C, Lozano JA, Larrañaga P (2001) Analyzing the PBIL algorithm by means of discrete dynamical systems. Complex Syst 12(4):465-479
Harik GR (1999) Linkage learning via probabilistic modeling in the ECGA. Technical report 99010. Illinois Genetic Algorithms Laboratory, University of Illinois, Urbana, Illinois, USA
Harik GR, Lobo FG, Goldberg DE (1999) The compact genetic algorithm. IEEE Trans Evolut Comput 3(4):287-297
Hauschild M, Pelikan M (2011) An introduction and survey of estimation of distribution algorithms. Swarm Evolut Comput 1:111-128
Johnson A, Shapiro JL (2002) The importance of selection mechanisms in distribution estimation algorithms. In: Collet P, Fonlupt C, Hao JK, Lutton E, Schoenauer M (ed) Evolution artificial, vol 2310. Lecture Notes in Computer Science, Springer, pp 91-103
Larrañaga P, Lozano JA (2001) Estimation of distribution algorithms: a new tool for evolutionary computation. Kluwer Academic Publishers, Norwell
Lozada-Chang L, Santana R (2011) Univariate marginal distribution algorithm dynamics for a class of parametric functions with unitation constraints. Inf Sci 181(11):2340-2355

Mühlenbein H (1997) The equation for response to selection and its use for prediction. Evolut Comput 5:303-346
Mühlenbein H, Mahnig T (1998) Convergence theory and applications of the factorized distribution algorithm. J Comput Inf Technol 7:19-32
Mühlenbein H, Mahnig T (2002) Evolutionary algorithms and the Boltzmann distribution. In: DeJong KA, Poli R, Rowe J (eds) Foundation of genetic algorithms 7. Morgan Kaufmann, Burlington, pp 133-150
Mühlenbein H, Mahnig T, Rodriguez AO (1999) Schemata, distributions and graphical models in evolutionary optimization. J Heuristics 5:215-247
Pelikan M, Goldberg DE (2000) Genetic algorithms, clustering, and the breaking of symmetry. Lecture Notes in Computer Science 1917, pp 385-394
Pelikan M, Goldberg DE (2001) Escaping hierarchical traps with competent genetic algorithms. In: Genetic and Evolutionary Computation Conference, pp 511-518
Pelikan M, Goldberg DE, Cantu-Paz E (2000) Linkage problem, distribution estimation, and Bayesian networks. Evolut Comput 8:311-340

Pelikan M, Mühlenbein H (1999) The bivariate marginal distribution algorithm. In: Chawdhry PK, Roy R, Furuhashi T (eds) Advances in soft computing-engineering design and manufacturing. Springer, Berlin, pp 521-535
Peña J, Lozano J, Larrañaga P (2005) Globally multimodal problem optimization via an estimation of distribution algorithm based on unsupervised learning of Bayesian networks. Evolut Comput 13(1):43-66
Sastry K, Goldberg DE (2001) Modeling tournament selection with replacement using apparent added noise. In: Proceedings of the Genetic and Evolutionary Computation Conference (GECCO2001). San Francisco, California, USA, p 781

Zhang Q (2004a) On stability of fixed points of limit models of univariate marginal distribution algorithm and factorized distribution algorithm. IEEE Trans Evolut Comput 8(1):80-93
Zhang Q (2004b) On the convergence of a factorized distribution algorithm with truncation selection. Complexity 9(4):17-23
Zhang Q, Mühlenbein H (2004) On the convergence of a class of estimation of distribution algorithms. IEEE Trans Evolut Comput 8(2):127-136