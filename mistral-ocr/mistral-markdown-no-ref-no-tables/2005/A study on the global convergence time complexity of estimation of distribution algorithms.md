# A Study on the Global Convergence Time Complexity of Estimation of Distribution Algorithms 

R. Rastegar and M.R. Meybodi<br>Computer Engineering Department, Amirkabir University, Tehran, Iran<br>\{rrastegar, meybodi\}@ce.aut.ac.ir


#### Abstract

The Estimation of Distribution Algorithm is a new class of population based search methods in that a probabilistic model of individuals are estimated based on the high quality individuals and used to generate the new individuals. In this paper we compute 1) some upper bounds on the number of iterations required for global convergence of EDA 2) the exact number of iterations needed for EDA to converge to global optima.


## 1 Introduction

Genetic Algorithms (GAs) are a class of optimization algorithm motivated from the theory of natural selection and genetic recombination. It tries to find better solution by selection and recombination of promising solution. It works well in wide verities of problem domains. The poor behaviors of genetic algorithms in some problems, in which the designed operators of crossover and mutation do not guarantee that the building block hypothesis is preserved, have led to the development of other type of algorithms. The search for techniques to preserve building blocks has led to the emergence of new class of algorithm called Probabilistic Model Building Genetic Algorithm (PMBGA) also known as Estimation of Distribution Algorithm (EDA). The principle concept in this new technique is to prevent disruption of partial solutions contained in an individual by giving them high probability of being presented in the child individual. It can be achieved by building a probabilistic model to represent correlation between variables in individual and build model to generate next population.

The EDAs are classified into three classes based on the interdependencies between variables in individuals [9]. Instances of EDAs algorithm include Population-based Incremental Learning (PBIL) [1], Univariate Marginal Distribution Algorithm (UMDA) [10], Learning Automata-based Estimation of Distribution Algorithm (LAEDA) [14], Compact Genetic Algorithm (cGA) [7] for no dependencies model, Mutual Information Maximization for Input Clustering (MIMIC) [3], Combining Optimizer with Mutual Information Trees (COMIT) [2] for bivariate dependencies model, and Factorized Distribution Algorithm (FDA) [11], Bayesian Evolutionary Algorithm (BOA) [13] for multiple dependencies model, to name a few.

Some researchers have studied the working mechanism of EDAs. Mühlenbein [10], González et al [4][5], Höhfeld and Rudolph [6] have studied the behavior of UMDA and PBIL. Mühlenbein and Mahnig [12] discussed the convergence of FDA for

separable additively decomposable functions. In [15], Zhang and Mühlenbein proved that EDAs with infinite population size globally converge. Despite the fact that working mechanisms of EDAs has been studied, the time complexity and the speed of convergence of EDAs algorithm are not known. In this paper we propose some results on the number of iterations needed for EDAs to converge globally when population size is infinite. Our approach is proposed in two sections. At first some upper bounds on the number of iterations required for global convergence of EDA are calculated and then in the second section the exact number of iterations needed for EDA to converge to global optima is calculated.

The rest of paper is organized as follows. Section 2 briefly presents the EDA algorithm and its modeling when EDA uses an infinite population size. Section 3 and 4 demonstrate some theorems about time complexity of EDAs. Conclusion is given in final section.

# 2 Estimation of Distribution Algorithm with Infinite Population Size 

Given a search space $D$ and a positive and continuous function $f(\mathbf{x}): D \rightarrow \mathcal{R}^{20}$, find $\max \{f(\mathbf{x}) ; \mathbf{x} \in D\}$.

Let $D^{*}$ be a set of all points at which function $f$ reaches its maximum value $f_{\max }$. The steps of the EDA algorithm for solving such an optimization problem are described below.

1-Initialization: generate an initial population, $\xi(0)$, of $N$ individuals.
2-Selection: choose $S e(S e<N)$ individuals from population $\xi(\mathrm{n})$ (i.e. population in iteration $n$ ) to form the parent population $\xi^{5}(n)$ using a selection schema such as truncation, tournament or proportional selection schema.
3-Updating: perform updating operations on individuals of parent population at iteration $n, \xi^{5}(n)$, and generate new individuals to form the new population at time $n$, $\xi(n+I)$, e.g. $\xi(n+I)=\xi^{5}(n)$.
4- If $E\{f(\mathbf{X}) \mid \xi(n+I)\}=f_{\max }$ then stop else go to step 2 .
Condition of step 4 of the above algorithm is met when every individual in the population is an optimal solution, that is, the EDA has globally converged.

Let the underlying probability distribution functions for the individuals of $\xi(n)$ and $\xi^{5}(n)$ be $P(\mathbf{X} \mid \xi(n))$ and $P\left(\mathbf{X} \mid \xi^{5}(n)\right)$, respectively. By the famous Glivenko-Canteli theorem [17], the empirical probability density functions induced by individuals in $\xi(n)$ and $\xi^{5}(n)$ will converge to $P(\mathbf{X} \mid \xi(\mathrm{n}))$ and $P\left(\mathbf{X} \mid \xi^{5}(\mathrm{n})\right)$ respectively, as the sizes of $\xi(n)$ and $\xi^{5}(n)$ tend to infinity. Therefore $P(\mathbf{X} \mid \xi(\mathrm{n}))$ and $P\left(\mathbf{X} \mid \xi^{5}(\mathrm{n})\right)$ can be thought of as the population and the parent population at iteration $n$ in EDA with infinite population [15]. Below we describe the selection schemes used in this paper.
The Truncation Selection Schema: Truncation selection ranks all the individuals in population $\xi(n)$ according to their fitness and selects the best ones as the set of parents $\xi^{5}(n)$. In truncation selection with threshold $0<\mu<1$ only the $100 \mu \%$ of best individuals

are selected to become the parents for the next generation. When the population size is infinite, it can be modeled as [15]:

$$
P\left(\mathbf{X}=\mathbf{x} \mid \xi^{S}(n)\right)=\left\{\begin{array}{cc}
\frac{P(\mathbf{X}=\mathbf{x} \mid \xi(n))}{\mu} & f(\mathbf{x}) \geq \beta(n) \\
0 & \text { otherwise }
\end{array} .\right.
$$

Where:

$$
\mu=\int_{f(\mathbf{x}) \geq \beta(n)} P(\mathbf{X}=\mathbf{x} \mid \xi(n))
$$

The Two-Tournament Selection Schema: In the two-tournament selection model, 2 individuals are chosen from the current population $\xi(n)$ and the best individual is selected to be a parent. This selection must be repeated $S e$ times to generate the set of parents $\xi^{S}(n)$. When the population size is infinite then this schema can be modeled as [15][16],

$$
P\left(\mathbf{X}=\mathbf{x} \mid \xi^{S}(n)\right)=2 P(\mathbf{X}=\mathbf{x} \mid \xi(n)) \int_{f(\mathbf{y}) \leq f(\mathbf{x})} P(\mathbf{X}=\mathbf{y} \mid \xi(n))
$$

Remark 1. In [15] Zhang and Mühlenbein have proved that EDA with truncation, or two-tournament selection schema, when using infinite population size, will globally converge.

Let $d(\xi)$ be the ratio of the number of individuals in population $\xi$, that do not belong to $D^{*}$, to the size of $\xi$. The sequence $\{d(\xi(n)) ; \mathrm{n}=0,1,2, \ldots\}$ generated by EDA is a random sequence in general. If $d(\xi)$ is 0 , then all individuals of population $\xi$, are members of $D^{*}$. If the population size tends to infinity, then according to GlivenkoCanteli theorem [17] $d(\xi(n))$ can be computed as follows,

$$
d(\xi(n))=\sum_{s \in D-D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n))=1-\sum_{s \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n))
$$

Define the global convergence stopping time of EDA as $\tau=\min \{n \mid E\{f(X) \mid \xi(n)\}=f_{\max }\}$ where for every $\tau \leq t E\{f(X) \mid \xi(t)\}=f_{\max }$. According to the definition of it, $\tau$ is the first time that EDA globally converges. $\tau$ can be infinite or finite. In the same manner, we define $\tau^{\prime}$ as $\min \{n \mid d(\xi(n))=0\}$. In the following we state two lemmas to show the relationship between $\tau^{\prime}$ and $\tau$
Lemma 1. The global convergence stopping time of $\mathrm{EDA}, \tau$, is equal to $\tau^{\prime}=$ $\min \{n \mid d(\xi(n))=0\}$.
Proof. We prove this lemma by contradiction. First assume that $\tau \leq \tau^{\prime}$, by the definition of $\tau^{\prime}$ we have $d(\xi(\tau)>0$ i.e. there exists at least one $\mathbf{y} \in \xi(\tau)$ that doesn't belong to $D^{*}$ (i.e. $f(\mathbf{y})<f_{\max }$ ) and $\mathrm{P}(\mathbf{X}=\mathbf{y} \mid \xi(\tau)=\mathrm{b}>0$. Thus we have

$$
E\{f(\mathbf{X}) \mid \xi(\tau)\}=\sum_{s \in D} f(\mathbf{x}) P(\mathbf{X}=\mathbf{x} \mid \xi(\tau)) \leq b f(\mathbf{y})+f_{\max }(1-b)
$$

Using (5) and the fact that $E\{f(\mathbf{X}) \mid \xi(\tau)\}=f_{\max }$ we can conclude that $f_{\max } \leq f(\mathbf{y})$ and hence a contradiction. Second, assume that $\tau>\tau^{\prime}$. Using definitions of $\tau$ and $\tau^{\prime}$, and (4) we have

$$
d\left(\xi\left(\tau^{\prime}\right)\right)=\sum_{\mathbf{x} \in D-D^{n}} P\left(\mathbf{X}=\mathbf{x} \mid \xi\left(\tau^{\prime}\right)\right)=0
$$

Using (6) and $0 \leq \mathrm{P}\left(\mathbf{X}=\mathbf{x} \mid \xi\left(\tau^{\prime}\right)\right) \leq 1$, we have,

$$
P\left(\mathbf{X}=\mathbf{x} \mid \xi\left(\tau^{\prime}\right)\right)=0 \quad \text { if } \quad \mathbf{x} \in D-D^{*}
$$

By definition of $E\left\{f(\mathbf{X}) \mid \xi\left(\tau^{\prime}\right)\right\}$ we can write

$$
\begin{aligned}
& E\left\{f(\mathbf{X}) \mid \xi\left(\tau^{\prime}\right)\right\}=\sum_{\mathbf{x} \in D} f(\mathbf{x}) P\left(\mathbf{X}=\mathbf{x} \mid \xi\left(\tau^{\prime}\right)\right)= \\
& \sum_{\mathbf{x} \in D^{n}} \underbrace{f(\mathbf{x}) P\left(\mathbf{X}=\mathbf{x} \mid \xi\left(\tau^{\prime}\right)\right)}_{f_{\max }}+\sum_{\mathbf{x} \in D-D^{n}} f(\mathbf{x}) P\left(\mathbf{X}=\mathbf{x} \mid \xi\left(\tau^{\prime}\right)\right)
\end{aligned}
$$

Using (7) and (8) we have

$$
E\left\{f(\mathbf{X}) \mid \xi\left(\tau^{\prime}\right)\right\}=f_{\max }(1)+\sum_{\mathbf{x} \in D-D^{n}} 0 \times f(\mathbf{x})=f_{\max }
$$

Which contradicts the assumption that $\tau>\tau^{\prime}$ and hence the proof. Q.E.D.
Lemma 2. If $\tau^{\prime}=\min \{n \mid d(\xi(n))=0\}$, then for every $\tau^{\prime} \leq t, d(\xi(t))=0$.
Proof. Proof is done by contradiction. Assume that $d(\xi(t)) \neq 0$, then there exists at least one $\mathbf{y} \in \xi(t)$ that doesn't belong to $D^{*}$ (i.e. $f(\mathbf{y})<f_{\max }$ ) and $\mathrm{P}(\mathbf{X}=\mathbf{y} \mid \xi(t))=\mathrm{b}>0$. So we have,

$$
E\{f(\mathbf{X}) \mid \xi(t)\}=\sum_{s \in D} f(\mathbf{x}) P\left(\mathbf{X}=\mathbf{x} \mid \xi(t)\right) \leq b f(\mathbf{y})+f_{\max }(1-b)
$$

Using (9) and $E\{f(\mathbf{X}) \mid \xi(t)\}=f_{\max }$ (By lemma 1), we have $f_{\max } \leq f(\mathbf{y})$ and hence a contradiction. Q.E.D.

Lemma 1 indicates that $\tau=\tau^{\prime}$ and Lemma 2 and Remark 1 state that $\tau^{\prime}$ is the stopping time of $\{d(\xi(n)) ; n=0,1,2, \ldots\}$. That is the stopping time of $\{E\{f(\mathbf{X}) \mid$ $\xi(n)\} ; \mathrm{n}=0,1,2, \ldots\}$ is the same as the stopping time of $\{d(\xi(n)) ; n=0,1,2, \ldots\}$ and for this reason in the rest of the paper we study the time complexity of $d(\xi(n))$ rather than the time complexity of $\{E\{f(\mathbf{X}) \mid \xi(n)\} ; n=0,1,2, \ldots\}$.

Using above notations and lemmas the EDA algorithm can be described as follows.
1- Initialization: $P(\mathbf{X}=\mathbf{x} \mid \xi(0))>0$ for all $\mathbf{x}$ (That is $P(\mathbf{X}=\mathbf{x} \mid \xi(0))=p$ for all $\mathbf{x}$ where $0<p<1)$.
2- Selection: generate $P\left(\mathbf{X} \mid \xi^{S}(n)\right)$ from $P(\mathbf{X} \mid \xi(n))$ according to a selection schema.
3- Updating: $P(\mathbf{X} \mid \xi(n+I))$ is set to $P\left(\mathbf{X} \mid \xi^{S}(n)\right)$.
4 - if $d(\xi(n+I))=0$ then stop; otherwise go to step 2 .

# 3 Upper Bounds on Time Complexity of Global Convergence 

The Results for upper bounds on time complexity of global convergence of EDA reported in this paper can be summarized by the following two theorems.
Theorem 1. If an EDA with infinite population size and truncation selection schema is used for optimizing function $f$, then the termination condition is met at most after $(\mu d(\xi(0)) /((1-\mu)(1-d(\xi(0)))))+I$ iterations.

It is obvious that $0<\mu<1$ is an important parameter for the stopping time of EDA when EDA use truncation selection schema. Lower values for $\mu$ will impose a lower upper bound on the stopping time and higher values for $\mu$ will exert a higher upper bound on the stopping time of EDA.
Theorem 2. If an EDA using infinite population size and 2-tournament selection schema is considered for optimizing $f$, at most after $(d(\xi(0)) /(1-d(\xi(0))))+1$ iterations the termination condition is met.

Before we give the proofs of the above two theorems we state one useful lemma.
Lemma 3. If $d(\xi) \leq h_{0}, h_{0}>0$, for any given population $\xi$ and $\{E\{d(\xi(n))-d(\xi(n+1))\}$ $d(\xi(n))>0\} \geq\left(1 / h_{l}\right)\}$ then starting from any initial population $\xi(0)$ with $d(\xi(0))>0$,

$$
E\{\tau \mid d(\xi(0))>0\} \leq h_{0} h_{1}
$$

Proof ${ }^{1}$. Since $\{E\{d(\xi(n))-d(\xi(n+1)) \mid d(\xi(n))>0\} \geq\left(1 / h_{l}\right)\}$ we have $\{d(\xi(n))$; $n=0,1,2, \ldots\}$ as a super-martingale. Since $h_{0} \geq d(\xi(n)) \geq 0$, it ultimately converges, that is

$$
\lim _{n \rightarrow \infty} E\{d(\xi(n)) \mid d(\xi(0))>0\}=0
$$

From the definition of stopping time $\tau$, we have $d(\xi(\tau)=0$. Therefore,

$$
E\{d(\xi(\tau)) \mid d(\xi(0))>0\}=0
$$

For $n \geq 1$, we have

$$
\begin{aligned}
& E\{d(\xi(n)) \mid d(\xi(0))>0\}= \\
& \quad E\{E\{d(\xi(n-1))+d(\xi(n))-d(\xi(n-1)) \mid \xi(n-1)\} \mid d(\xi(0))>0\}
\end{aligned}
$$

Since $E\{d(\xi(n))-d(\xi(n+1)) \mid d(\xi(n))>0\} \geq\left(1 / h_{l}\right)\}$, for $n-1<\tau$, we have

$$
E\{d(\xi(n-1))+d(\xi(n))-d(\xi(n-1)) \mid \xi(n-1)\} \leq d(\xi(n-1))-\frac{1}{h_{1}}
$$

From (11) we can write

$$
E\{d(\xi(n)) \mid d(\xi(0)>0\} \leq E\{d(\xi(n-1))-\frac{1}{h_{1}} \mid d(\xi(0))>0\}
$$

Using (12) and by induction on $n$, we can get

$$
\begin{aligned}
& E\{d(\xi(n)) \mid d(\xi(0))>0\} \leq E\{d(\xi(0))-\frac{n}{h_{1}} \mid d(\xi(0))>0\} \text { and } \\
& 0=E\{d(\xi(\tau)) \mid d(\xi(0))>0\} \leq E\{d(\xi(0))\}-\frac{1}{h_{1}} E\{\tau \mid d(\xi(0))>0\}
\end{aligned}
$$

From (13) and $d(\xi) \leq h_{0}$, we have

$$
E\{\tau \mid d(\xi(0))>0\} \leq E\{d(\xi(0))\} h_{1} \leq h_{0} h_{1}
$$

and hence the proof. Q.E.D.

[^0]
[^0]:    ${ }^{1}$ The idea of the proof is borrowed from [8].

Now we are ready to prove theorems 1 and 2 . To do this we first prove that conditions of lemma 3 stand and then using lemma 3 we conclude the theorems.
Proof of theorem 1: We first show that conditions of lemma 3 hold and then use lemma 3 to conclude the theorem.
Using the definition of $d(\xi(n))$ and steps 2 and 3 of EDA algorithm we can write

$$
\begin{aligned}
& E\{d(\xi(n))-d(\xi(n+1)) \mid d(\xi(n))>0\}=E\left\{\sum_{\mathbf{x} \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n+1))-\right. \\
& \left.\sum_{\mathbf{x} \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n)) \mid d(\xi(n))>0\right\}= \\
& E\left\{\sum_{\mathbf{x} \in D^{*}} P\left(\mathbf{X}=\mathbf{x} \mid \xi^{S}(n)\right)-\sum_{\mathbf{x} \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n)) \mid d(\xi(n))>0\right\}
\end{aligned}
$$

Using (2) and the fact that for all $\mathbf{x} \in \mathrm{D}^{*}$ we have $f(\mathbf{x})=f_{\max } \geq \beta(n)$, (14) can be rewritten as

$$
\begin{aligned}
& E\left\{\sum_{\mathbf{x} \in D^{*}} \frac{P(\mathbf{X}=\mathbf{x} \mid \xi(n))}{\mu}-\sum_{\mathbf{x} \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n)) \mid d(\xi(n))>0\right\}= \\
& E\left\{\left(\frac{1}{\mu}-1\right) \sum_{\mathbf{x} \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n)) \mid d(\xi(n))>0\right\}=\left(\frac{1}{\mu}-1\right)(1-d(\xi(n)))
\end{aligned}
$$

Using (15) and induction on $n$ we have

$$
d(\xi(n)) \leq d(\xi(0))=h_{0}
$$

From (16) we have,

$$
\begin{aligned}
& E\{d(\xi(n))-d(\xi(n+1)) \mid d(\xi(n))>0\} \geq\left(\frac{1}{\mu}-1\right)(1-d(\xi(0)))= \\
& \frac{1}{\frac{\mu}{(1-\mu)(1-d(\xi(0)))}}=\frac{1}{h_{1}}
\end{aligned}
$$

From (16) and (17) we conclude that conditions of Lemma 3 are satisfied and therefore we can write,

$$
E\{\tau \mid d(\xi(0))>0\} \leq h_{0} h_{1}=\frac{\mu d(\xi(0))}{(1-\mu)(1-d(\xi(0)))}
$$

Hence the proof. Q.E.D.
Proof theorem 2: Using the definition of $d(\xi(n))$ and steps 2 and 3 of EDA algorithm, we can write,

$$
\begin{aligned}
& E\{d(\xi(n))-d(\xi(n+1)) \mid \xi(n)\}=E\left\{\sum_{\mathbf{x} \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n+1))-\right. \\
& \left.\sum_{\mathbf{x} \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n)) \mid \xi(n)\right\}=E\left\{\sum_{\mathbf{x} \in D^{*}} P\left(\mathbf{X}=\mathbf{x} \mid \xi^{S}(n)\right)-\sum_{\mathbf{x} \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n)) \mid \xi(n)\right\}
\end{aligned}
$$

Using (3) and the fact that for all $\mathbf{y} \in \mathrm{D}$ we have $f_{\max } \geq f(\mathbf{y})$, we can rewrite (18) as

$$
\begin{aligned}
& E\left\{\sum_{\mathbf{x} \in D^{*}}\{2 P(\mathbf{X}=\mathbf{x} \mid \xi(n)) \underbrace{\int_{f_{\max }=f(\mathbf{x}) \geq f(\mathbf{y})} P(\mathbf{X}=\mathbf{y} \mid \xi(n))}_{1}-\sum_{\mathbf{x} \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n)) \mid \xi(n)\right\} \\
& E\left\{\sum_{\mathbf{x} \in D^{*}} P(\mathbf{X}=\mathbf{x} \mid \xi(n)) \mid \xi(n)\right\}=(1-d(\xi(n)))
\end{aligned}
$$

Using (19) and induction on $n$ we can write

$$
d(\xi(n)) \leq d(\xi(0))=h_{0}
$$

Using the (18), (19) and (20) we have

$$
E\{d(\xi(n))-d(\xi(n+1)) \mid \xi(n)\} \geq(1-d(\xi(0)))=\frac{1}{h_{1}}
$$

Since conditions of Lemma 3 are satisfied and we have,

$$
E\{\tau \mid d(\xi(0))>0\} \leq h_{0} h_{1}=\frac{d(\xi(0))}{1-d(\xi(0))}
$$

Hence the theorem. Q.E.D.

# 4 Computation of Global Convergence Stopping Time 

In this section, some strong results about the convergence of EDA are derived. As stated before $\{d(\xi(n)) ; n=0,1,2, \ldots\}$ is a random sequence in general and when population size tends to infinity this sequence becomes a deterministic sequence. In other words by knowing $d(\xi(n-I))$ we can compute the exact value of $d(\xi(n))$. We can use these properties to derive some strong results about the convergence of EDA.
Definition 1. (Convergence Rate). Let $\left\{a_{n} ; n=0,1,2, \ldots\right\}$ be a sequence that converges to $a^{*}$. If we have

$$
\lim _{n \rightarrow \infty} \frac{\left|a_{n+1}-a^{*}\right|}{\left|a_{n}-a^{*}\right|}=\beta
$$

then $\left\{a_{n} ; n=0,1,2, \ldots\right\}$ converges to $a^{*}$ with convergence rate $\beta$.
The results for the exact number of iterations needed for EDA to converge to global optima reported in this paper can be summarized by the following two theorems
Theorem 3. If we use an EDA with infinite population size and truncation selection method having threshold $\mu$ then a) After $1+(\log (1-d(\xi(0))) / \log \mu)$ iterations the condition of termination is met. b) $\{d(\xi(n)) ; n=0,1,2, \ldots\}$ converges to 0 with convergence rate $1 / \mu$.
Theorem 4. If we use an EDA with infinite population size and 2 -tornumant selection method, then a) After $1+(\log (1-d(\xi(0))) / \log 0.5)$ iterations the condition of termination is met. b) $\{d(\xi(n)) ; n=0,1,2, \ldots\}$ converges to 0 with convergence rate 2 .

Before we give the proofs of theorems 3 and 4 , we state two lemmas for the computation of $d(\xi(n))$.

Lemma 4. For EDA algorithm with infinite population size and truncation selection method $d(\xi(n))$ can be computed as follows,

$$
d(\xi(n))=1-(1-d(\xi(0))) \frac{1}{\mu}^{n}
$$

where $0<\mu<l$ is the selection threshold.
Proof. We the definition $d(\xi(n))$ and (2) we have,

$$
\begin{aligned}
d(\xi(n+1)) & =1-\sum_{\mathbf{x} \in D^{n}} P(\mathbf{X}=\mathbf{x} \mid \xi(n+1))=1-\sum_{\mathbf{x} \in D^{n}} P\left(\mathbf{X}=\mathbf{x} \mid \xi^{S}(n)\right) \\
& =1-\frac{1}{\mu} \sum_{\mathbf{x} \in D^{n}} P\left(\mathbf{X}=\mathbf{x} \mid \xi(n)\right)=1-\frac{1}{\mu}(1-d(\xi(n)))
\end{aligned}
$$

From (21) we have

$$
d(\xi(n+1))-\frac{1}{\mu} d(\xi(n))=\left(1-\frac{1}{\mu}\right)
$$

Characteristic equation of (22) is,

$$
r^{2}-\left(\frac{1}{\mu}+1\right) r+\frac{1}{\mu}=0
$$

By solving (23) we have

$$
d(\xi(n))=1-(1-d(\xi(0))) \frac{1}{\mu}^{n}
$$

# Q.E.D. 

Lemma 5. For EDA algorithm with infinite population size and tournament selection method we have

$$
d(\xi(n))=1-(1-d(\xi(0))) 2^{n}
$$

Proof. By the definition of $d(\xi(n))$.and (3) we have,

$$
d(\xi(n+1))-2 d(\xi(n))+1=0
$$

The characteristic equation of (24) is,

$$
r^{2}-3 r+2=0
$$

By solving (24) we have

$$
d(\xi(n))=1-(1-d(\xi(0))) 2^{n}
$$

## Q.E.D.

Now we use Lemmas 4 and 5 and prove theorems 3 and 4.
Proof of theorem 3. (a) By definition of stopping time and Lemma 4 we have

$$
d(\xi(\tau))=1-(1-d(\xi(0))) \frac{1}{\mu}^{\tau}=0
$$

Using (26) we conclude,

$$
\tau=\log (1-d(\xi(0))) / \log \mu
$$

By (27) after $1+(\log (1-d(\xi(0))) / \log \mu)$ iterations the condition of termination is met. (b) By lemma 4, we have

$$
\lim _{n \rightarrow \infty} \frac{1 d(\xi(n+1))-0 \mid}{1 d(\xi(n))-0 \mid}=\frac{1}{\mu}
$$

From definition $1,\{d(\xi(n)) ; n=0,1,2, \ldots\}$ converges to 0 with convergence rate $1 / \mu$. Q.E.D.

Proof of theorem 4: (a) By definition of stopping time and lemma 5 we have

$$
d(\xi(\tau))=1-(1-d(\xi(0))) 2^{\tau}=0
$$

Using (28) we have,

$$
\tau=\log (1-d(\xi(0))) / \log (0.5)
$$

By (29) after $1+(\log (1-d(\xi(0))) / \log 0.5)$ iterations the condition of termination is met. (b) By lemma 5, we conclude that

$$
\lim _{n \rightarrow \infty} \frac{1 d(\xi(n+1))-0 \mid}{1 d(\xi(n))-0 \mid}=2
$$

According to definition $1,\{d(\xi(n)) ; n=0,1,2, \ldots\}$ converges to 0 with convergence rate 2. Q.E.D.

# 5 Conclusion 

This paper presented some new results for global convergence computation time for EDA algorithms. The following quantities were computed: 1) some upper bounds on the number of iterations required for global convergence of EDA 2) the exact number of iterations needed for EDA to converge to global optima.
