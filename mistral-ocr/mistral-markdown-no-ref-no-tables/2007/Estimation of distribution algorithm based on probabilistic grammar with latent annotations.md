# Estimation of Distribution Algorithm based on Probabilistic Grammar with Latent Annotations 

Yoshihiko Hasegawa $\dagger$ and Hitoshi Iba $\dagger$


#### Abstract

Genetic Programming (GP) which mimics the natural evolution to optimize functions and programs, has been applied to many problems. In recent years, evolutionary algorithms are seen from the viewpoint of the estimation of distribution. Many algorithms called EDAs (Estimation of Distribution Algorithms) based on probabilistic techniques have been proposed. Although probabilistic context free grammar (PCFG) is often used for the function and program evolution, it assumes the independence among the production rules. With this simple PCFG, it is not able to induce the building-blocks from promising solutions. We have proposed a new function evolution algorithm based on PCFG using latent annotations which weaken the independence assumption. Computational experiments on two subjects (the royal tree problem and the DMAX problem) demonstrate that our new approach is highly effective compared to prior approaches.


## I. INTRODUCTION

In this paper, we propose a function optimization algorithm based on probabilistic context free grammar (PCFG) with latent annotations (PCFG-LA) [12]. Our approach named PAGE (Programming with Annotated Grammar Estimation) uses latent annotations which enable an induction of promising sub-functions (sub-routines).

GP (Genetic Programming) [7], [8] is an extended algorithm of GA (Genetic Algorithm) and is capable of handling programs and functions. Because GP has structural chromosomes which are very flexible, GP has been applied to many problems (robot engineering, financial engineering, bio informatics, etc) and is considered to be a very powerful way for solving these problems.

GA and GP evolve solution candidates with crossover and mutation operators. These methods are considered to be highly effective because they take advantage of the mechanism of natural evolution. Recently, Evolutionary Algorithms are seen from the viewpoint of the distribution estimation. A new way for evolving solutions based on the estimation of distribution has been proposed. More and more attention has been paid to this method, which is called EDA (Estimation of Distribution Algorithm) [10], [14]. In EDAs, there are two types of algorithms : those based on GA style linear chromosome (GA-EDA) and those based on GP style tree chromosome (GP-EDA).

In GP-EDA, algorithms can be broadly classified into two groups: proto-type tree based method and PCFG based method. The former method translates variable length treestructures into fixed length structures (mostly linear arrays).

[^0]The later method uses context free grammar (CFG) for expressing programs and functions. Algorithms based on PCFG are considered to be well suited for expressing functions in GP. Thus many algorithms based on the later approach have been proposed (Section II).

The basic PCFG adopts the context freedom assumption that the probabilities of production rules do not depend on the ascendant nodes or sibling nodes. The basic GP-EDA based on PCFG just estimates parameters (production rule probability) and generate the programs using the parameters. Although the independence assumption makes the statistical estimation easier, this PCFG basically can not take into account the interactions among nodes. Thus it is not suitable for grasping the sub-functions or sub-routines in GP programs, because GP functions often have strong interactions among nodes. In order to weaken the independence assumption in PCFG, annotations have been proposed in the natural language. For example, vertical markovization annotates the symbols with their ancestor symbols. Prior GP-EDAs such as PEEL or Grammar Transformation in EDA (GT-EDA) used annotated PCFG for base line grammars. In these algorithms, the depth of the production rules is taken into account. Although these annotations may work in specific problems, this assumption may be too strong or wrong in other problems.

Matsuzaki et. al. proposed the PCFG with latent annotations (PCFG-LA) [12] which assumes that the annotations are hidden and the production rules with annotations can be estimated with EM algorithm. We expect that PCFG-LA is suitable for more precisely grasping the interactions in GP compared to previous methods and it is more flexible compared to the method based on heuristics based annotations as depth.

This paper is structured as follows. In the next section, we briefly introduce the program evolution methods based on probabilistic techniques. In Section III we explain the PCFGLA which is used in our proposal describing parameters update formula. In section V, we compare the performance of our method to other methods, selecting two benchmark tests for experiments. We discuss the results obtained in the experiment in section VI. Finally, we conclude this paper in section VII.

## II. RELATED WORKS

Probabilistic evolutionary algorithms based on probabilistic models have been first carried in GA style linear chromosome. Because GP uses tree structures which are more complex than linear arrays used in GA, GP-EDA is a newer


[^0]:    $\dagger$ Department of Frontier Informatics, Graduate School of Frontier Sciences, The University of Tokyo (email: yoshihiko.hasegawa@gmail.com, iha@iba.k.u-tokyo.ac.jp)

![img-0.jpeg](img-0.jpeg)

Fig. 1. A complete tree with annotations (a) and its observed tree (b).
field than GA-EDA. Many GP-EDAs have been proposed up to now and can be broadly classified into two groups: (i) prototype tree based method and (ii) grammar model based methods.

The method (i) takes advantage of the techniques devised in GA-EDA. This type of algorithms translates tree structures into fixed length chromosomes used in GA and applies the probabilistic model. PIPE (Probabilistic Incremental Program Evolution) [19] adopted the univariate model which can be considered as the combination of PBIL (Population Based Incremental Learning) [1] and GP. EDP (Estimation of Distribution Programming) [25], [26] considered the parentchildren relationship in the tree structure. EDP considers conditional probability distribution of children given parent nodes. ECGP (Extended Compact GP) [20] combines the ECGA (Extended Compact GA) [4] with GP to take into account the relationship among nodes. This algorithm estimates the group of joint distribution with MDL principle. BOAP extends BOA (Bayesian Optimization Algorithm) [15] to be able to handle programs and functions. BOAP (BOA Programming) [11] uses zig-zag tree which is based on lambda function. POLE (Program Optimization with Linkage Estimation) [5], [6] estimated the interactions among nodes with estimating the Bayesian network. In this algorithm, special chromosome called expanded parse tree is used to convert the GP programs into linear arrays.

The method (ii) which is based on PCFG has a lot to do with GGGP (Grammar Guided Genetic Programming) [24]. GGGP applies the CFG to GP. SG-GP (Stochastic Grammar based GP) [17] uses simple PCFG. SG-GP integrates PBIL with GGGP. In this algorithm, the parameters are updated using an incremental learning strategy. PEEL (Program Evolution with Explicit Learning) [21] is an extended algorithm of SG-GP which takes into account the depth of symbols. GMPE (Grammar Model based Program Evolution) [22] merge the production rules to find the general production rules. GMPE starts from specialized production rules and merge non-terminals to be more general production rules with MDL principle. Grammar Transformation in EDA (GTEDA) [2] takes advantage of MDL principle to estimate expanded production rules (tree structure) to extract good subroutines. BAP (Bayesian Automatic Programming) [18] uses Bayesian network to consider the relation among pro-
duction rules.
Unlike PEEL and GT-EDA which use fixed annotations, our proposal uses annotations which are induced from promising solutions using EM algorithm. Our method is more flexible than the fixed annotation model and we expect that our method is more effective than the methods based on fixed annotations. In GA-EDA, an algorithm taking advantage of latent variables have been proposed [23]. In this work, EM algorithm is also used to estimated the parameters.

## III. PCFG WITH LATENT ANNOTATIONS

In CFG, many approaches have been proposed to weaken the context freedom assumption by annotating non-terminal symbols with many features. Many of the works use fixed annotations as labels of ancestor symbols, and sibling nodes. Matsuzaki et. al. [12] proposed the probabilistic context free grammar with latent annotations (PCFG-LA) which automatically induces the production rules with latent annotations. They also derived the parameter update formula with EM algorithm.

In PCFG-LA, every non-terminal is labeled with annotations. In the complete form, non-terminals are represented $A[x]$, where $A$ is the non-terminal symbol and $x$ is an annotation which is not observed ( $x \in H$, where $H$ is a set of annotations). Figure 1 is an example of trees with annotations (a) and observed tree (b). The probability of the annotated tree can be represented with Equation 1.

$$
P(T, \mathbf{X} ; \Theta)=\pi\left(\mathcal{S}\left[x_{1}\right]\right) \prod_{r \in D_{\mathcal{T}[\mathbf{X}]}} \beta(r)
$$

In this equation, $T$ is a derivation tree, $x_{i}$ is an annotation of $i$ th non-terminal (all the non-terminals are numbered from the root), $\mathbf{X}$ is $\mathbf{X}=\left\{x_{1}, x_{2}, \ldots\right\}, \pi(\mathcal{S}[x])$ is a probability of $\mathcal{S}[x]$ at the root position, $\beta(r)$ is a probability of annotated production rule $r, D_{\mathcal{T}[X]}$ is a multi-set of used annotated rules in tree $T$ and $\Theta$ denotes a set of parameters $\Theta=\{\pi, \beta\}$.

The probability of a observed tree can be calculated with summing over annotations given by

$$
P(T ; \Theta)=\sum_{\mathbf{X}} P(T, \mathbf{X} ; \Theta)
$$

Because annotations are not observed, the parameters ( $\pi$ and $\beta$ ) have to be estimated by EM algorithm. The difference of log-likelihood between parameters $\Theta^{\prime}$ and $\Theta$ can be calculated by Equation 3.

$$
\begin{aligned}
& \log P\left(T ; \Theta^{\prime}\right)-\log P(T ; \Theta) \\
& =\log \frac{P\left(T ; \Theta^{\prime}\right)}{P(T ; \Theta)} \\
& =\sum_{\mathbf{X}} P(\mathbf{X} \mid T ; \Theta) \log \frac{P(T, \mathbf{X} ; \Theta^{\prime})}{P(T, \mathbf{X} ; \Theta)} \frac{P\left(\mathbf{X} \mid T ; \Theta\right)}{P(\mathbf{X} \mid T ; \Theta^{\prime})} \\
& \geq \sum_{\mathbf{X}} P(\mathbf{X} \mid T ; \Theta) \log \frac{P\left(T, \mathbf{X} ; \Theta^{\prime}\right)}{P(T, \mathbf{X} ; \Theta)}
\end{aligned}
$$

Using Equation 3, the update formula can be obtained by optimizing $Q\left(\Theta^{\prime} \mid \Theta\right)$ (Equation 4).

$$
Q\left(\Theta^{\prime} \mid \Theta\right)=\sum_{T_{i} \in \mathbf{T}} \sum_{\mathbf{X}_{i}} P\left(\mathbf{X}_{i} \mid T_{i} ; \Theta\right) \log P\left(T_{i}, \mathbf{X}_{i} ; \Theta^{\prime}\right)
$$

In this paper, production rules are not CNF (Chomsky Normal Form) which is assumed in the original PCFG-LA paper, because of understandability of GP programs. Any functions which can be handled with traditional GP can be represented by

$$
\mathcal{S} \rightarrow g \mathcal{S} . . \mathcal{S}
$$

which is a subset of GNF (Greibach Normal Form). Here $\mathcal{S} \in \mathcal{N}$ and $g \in \mathcal{T}(\mathcal{N}$ and $\mathcal{T}$ are sets of non-terminal and terminal symbols in CFG, respectively). $g$, terminal symbol in CFG, is a function node $(+,-, \sin , \cos )$ or a terminal $(x, y)$ in GP. In the program evolution, only $\mathcal{S}$ is used for non-terminal. In the right-side of Equation 5, the number of $\mathcal{S}$ is identical to the arity of $g$. If $g=+$, then $\mathcal{S} \rightarrow+\mathcal{S} \mathcal{S}$ and if $g=x$, then $\mathcal{S} \rightarrow x$. Annotated production rules can be expressed by Equation 6,

$$
\mathcal{S}[x] \rightarrow g \mathcal{S}\left[z_{1}\right] \ldots \mathcal{S}\left[z_{a}\right]
$$

where $x, z_{m} \in H, a$ is the arity of $g$ in GP. However, we made an assumption in our algorithm because of the following reason. Let us $h$ be the size of annotation $H$. If $g$ has $a$ arity, the number of parameters for the production rule $\mathcal{S} \rightarrow g \mathcal{S} . . \mathcal{S}$ with annotations becomes $h^{a+1}$. Estimating the large number of parameters may cause an over fitting problem and requires much more computational power. In order to reduce the number of parameters, we assume that all right-side non-terminal symbols have the same annotation.

$$
\mathcal{S}[x] \rightarrow g \mathcal{S}[y] \mathcal{S}[y] . . \mathcal{S}[y]
$$

With this assumption, the size of parameters can be reduced to $h^{2}$, which is tractable. Because there are many functions which are commutative (e.g. $+, \times$, etc) in GP, we think that this assumption may not be so strong. From now on, we assume Equation 7 in the following explanation. In the following sections, let $\mathcal{R}[H]$ be the set of annotated rules expressed by Equation 7.

$$
\mathcal{R}[H]=\{\mathcal{S}[x] \rightarrow g \mathcal{S}[y] \mathcal{S}[y] . . \mathcal{S}[y]|x, y, \in H, g \in \mathcal{T}\}
$$

## A. Forward-backward probability

For calculating the Equation 4, forward-backward probability is used. Backward probability $b_{T}^{\prime}(x)$ stands for the probability that the tree beneath $i$ th non-terminal $\mathcal{S}[x]$ is generated. Forward probability $f_{T}^{i}(y)$ stands for the probability that the tree above $i$ th non-terminal $\mathcal{S}[y]$ is generated. These probabilities can be recursively calculated (Equation 8, 9 and 10).

$$
b_{T}^{\prime}(x)=\sum_{y \in H} \beta\left(\mathcal{S}[x] \rightarrow g_{i} \mathcal{S}[y] . . \mathcal{S}[y]\right) \prod_{j \in c h(i, T)} b_{T}^{\prime}(y)
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. An example of the derivation tree and values of the specific functions. Superscriptions denote the indices of non-terminals.

$$
\begin{gathered}
f_{T}^{\prime}(y)=\sum_{x \in H} f_{T}^{p a(i, T)}(x) \beta\left(\mathcal{S}[x] \rightarrow g_{T}^{p a(i, T)} \mathcal{S}[y] . . \mathcal{S}[y]\right) \\
\times \prod_{j \in c h(p a(i, T), T), j \neq i} b_{T}^{\prime}(y) \\
f_{T}^{i}(y)=\pi(\mathcal{S}[y]) \quad(i=1)
\end{gathered}
$$

In these equations, $c h(i, T)$ is a function which returns the set of non-terminal children indices of $i$ th non-terminal in $T . p a(i, T)$ returns a parent index of $i$ th non-terminal in $T$. $g_{T}^{\prime}$ is a terminal symbol in CFG and is connected to $i$ th non-terminal symbol in $T$. For example, $c h(3, T)=\{5,6\}$, $p a(5, T)=3$ and $g_{T}^{3}=\sin$ in Figure 2.

Using the forward-backward probability, $P(T ; \Theta)$ can be represented by following Equations.

$$
\begin{gathered}
P(T ; \Theta)=\sum_{x \in H} \pi(\mathcal{S}[x]) b_{T}^{1}(x) \\
P(T ; \Theta)=\sum_{x, y \in H} \beta\left(\mathcal{S}[x] \rightarrow g \mathcal{S}[y] . . \mathcal{S}[y]\right) f_{T}^{i}(x) \\
\times \prod_{j \in c h(i, T)} b_{T}^{\prime}(y) \quad(i \in \operatorname{cover}(g, T))
\end{gathered}
$$

In this equation, $\operatorname{cover}\left(g, T_{i}\right)$ represents a function which returns a set of non-terminal indices at which the production rule generating $g$ without annotations is rooted in $T_{i}$. For example, if $g=+$ and $T$ is a tree represented in Figure 2, then $\operatorname{cover}(+, T)=\{1,3\}$.

## B. Parameter update formula

Using the forward-backward probability and optimizing $Q\left(\Theta^{\prime} \mid \Theta\right)$, the update formula can be derived. Because our approach is not based on CNF and we limit the rightside annotations in production rules, the update formula is different from that in the original paper (see Appendix).

$$
\begin{gathered}
\pi^{\prime}(\mathcal{S}[x]) \propto \pi(\mathcal{S}[x]) \sum_{T_{i} \in \mathbf{T}} \frac{b_{T_{i}}^{\prime}(x)}{P\left(T_{i}\right)} \\
\beta^{\prime}\left(\mathcal{S}[x] \rightarrow g \mathcal{S}[y] . . \mathcal{S}[y]\right) \propto \beta\left(\mathcal{S}[x] \rightarrow g \mathcal{S}[y] . . \mathcal{S}[y]\right) \\
\times \sum_{T_{i} \in \mathbf{T}} \frac{1}{P\left(T_{i}\right)} \sum_{j \in \operatorname{cover}\left(g, T_{i}\right)} f_{T_{i}}^{j}(x) \prod_{k \in c h\left(j, T_{i}\right)} b_{T_{i}}^{k}(y)
\end{gathered}
$$

EM algorithm maximizes the log-likelihood $(L(\Theta ; \mathbf{T})=$ $\log P(\mathbf{T} ; \Theta)=\sum_{T_{i} \in \mathbf{T}} \log P\left(T_{i} \mid \Theta\right)$ ) monotonically from the initial parameters. For initial parameters, we used the values represented with Equation 15 and 16.

$$
\begin{gathered}
\beta(\mathcal{S}[x] \rightarrow g \mathcal{S}[y] \ldots \mathcal{S}[y]) \propto \frac{e^{-\kappa}}{h-1} \gamma(\mathcal{S} \rightarrow g \mathcal{S} \ldots \mathcal{S}) \\
\beta(\mathcal{S}[x] \rightarrow g) \propto e^{-\kappa} \gamma(\mathcal{S}[x] \rightarrow g)
\end{gathered}
$$

In Equation 15, $\kappa$ is a random value which is uniformly distributed over $[-\log 3, \log 3]$ and $\gamma(\mathcal{S} \rightarrow g \mathcal{S} \ldots \mathcal{S})$ is a probability of observed production rule (without annotations). We also set $\beta(\mathcal{S}[x] \rightarrow g \mathcal{S}[x] \ldots \mathcal{S}[x])=0$.

Because the obtained parameters are greatly affected by initial values, we carried EM algorithm several times (in this paper, 3 times at each generation) with different initial parameters and then adopted the parameters which gave the best likelihood.

## IV. FLOWCHART

Combining the PCFG-LA with GP, we propose a new algorithm PAGE (Programming with Annotated Grammar Estimation). In this section, a flowchart of PAGE is shown.

1) Initialization of individuals

Individuals are generated randomly according to the initial parameters. The number of initialized individuals is represented with $M$.
2) Evaluation of individuals

All individuals are assigned fitness values according to the evaluation function.
3) Selection of individuals

Promising individuals are selected which are used for the parameter estimation. In our implementation, a truncate selection is used. The number of individuals to select is represented by $M \times P_{s}$.
4) Estimation of parameters

Parameters are estimated with EM algorithm explained in the proceeding section. Parameters are estimated at every generation. We stop updating the parameters if the log-likelihood improvement is smaller than $0.5 \%$.
5) Generation of new individuals

New individuals are generated with estimated parameters. If we want to use an elitist strategy, the best $M \times P_{s}$ individuals are copied from the previous generation.
Steps from (2) to (5) are repeated until termination criteria are met.

## V. COMPARATIVE EXPERIMENTS

We carried comparative experiments to show the effectiveness of our approach (PAGE). We compared the search performance among the algorithms listed below.

## - PAGE

This is our proposed method. This method extends PCFG-GP by introducing the latent annotations. The

TABLE I
MAIN PARAMETERS FOR PAGE.

number of latent annotations $h(h>1)$ is given beforehand. The annotations in PAGE are represented by integer $(H=\{0,1, \ldots, h-1\})$.

## - PCFG-GP

We denote PCFG-GP for expressing a GP based on a simple PCFG. This algorithm does not take annotations into account. This is $h=1$ case of PAGE, and it is basically identical to the GP-EDA which uses simple PCFG for probabilistic model (SG-GP [17]).

## - Simple GP (SGP)

This is a simple implementation of GP. In the experiments, $P_{c}=0.01$ (elite rate), $P_{c}=0.9$ (crossover rate), $P_{c o}=0$ (mutation rate) and $P_{c}=0.09$ (reproduction rate) are used. Crossover points are selected in the following way: When applying crossover to two individuals, we select the first crossover point from function nodes at the probability of 0.9 and from terminals at 0.1 . The second crossover point is selected under the condition that the depth of both individuals does not exceed the depth limitation.

## A. Royal Tree Problem

We applied PAGE to the royal tree problem to compare the performance between PAGE and PCFG-GP. This experiment shows the effectiveness of latent annotations.

1) Problem Description: In order to show the effectiveness of latent annotations, we compared the search performance in the royal tree problem [16]. The royal tree problem is an extension of the royal road function[13] which has been the famous benchmark test in GA. The royal tree problem uses a set of functions which are defined with alphabetical symbols $\mathfrak{F}=\{a, b, c, d, \ldots\}$ which have increasing arity ( $a$ has 1 arity, $b$ has 2 arity and so on) and terminal nodes $\mathfrak{T}=\{x\}(\mathfrak{F}$ and $\mathfrak{T}$ represents sets of GP functions and GP terminals, respectively). The royal tree problem defines the state perfect tree in each level. Perfect tree of some level is composed of the perfect tree whose level is smaller by 1 level than the level. Perfect tree of level $c$ is composed of the perfect tree of level $b$. In perfect trees, alphabets of functions descend by one from a root to leaves in a tree. A function $a$ has a terminal $x$. For more details, see [16].

In our setups, we used level $d$ royal tree problem. The production rules for the royal tree problem are shown in the list below, where symbols with small case denote terminal symbols in CFG. $a \sim d$ are function nodes and $x$ is a terminal node in GP.

![img-2.jpeg](img-2.jpeg)

Fig. 3. The probability of success in the royal tree problem. The number attached to PAGE in the parentheses represents the annotation size $h$.

$$
\begin{aligned}
\mathcal{S} & \rightarrow a \mathcal{S} \\
\mathcal{S} & \rightarrow b \mathcal{S} \mathcal{S} \\
\mathcal{S} & \rightarrow c \mathcal{S} \mathcal{S} \mathcal{S} \\
\mathcal{S} & \rightarrow d \mathcal{S} \mathcal{S} \mathcal{S} \mathcal{S} \\
\mathcal{S} & \rightarrow x
\end{aligned}
$$

In this experiment, $M=1000$ is used in both PAGE and PCFG-GP. We observe the behavior of our algorithm in terms of the number of latent annotations $(h)$ with $h=2,4,8,16$ in PAGE.
2) Results: Figure 3 represents the probability of success at each generation. As can been seen in Figure 3, PCFGGP did not obtain the optimum at all. This reason can be easily estimated. Table II (lower table) describes the obtained production rule probabilities of PCFG-GP. As can been seen with this table, probability of production rule $\mathcal{S} \rightarrow x$ is the highest. Thus using simple PCFG, the size of generated individuals tends to be small, because probabilities of large trees tends to be very small. On the other hand, our approach uses the production rules with latent annotations. In Table II (upper table), the production rules with annotations are described $(h=8)$. In this table, because of space limitation, we omitted the production rules which have very small probabilities (smaller than 0.01 ). In the probabilities with annotations, the annotations are used for generating different symbols. For example, $\mathcal{S}[0]$ and $\mathcal{S}[3]$ generate $x$ and $\mathcal{S}[1]$ generates $d$ exclusively. Using these production rules, we can grasp the sub-structures with higher probability.

In PAGE, the number of annotations $h$ strongly affect the search performance. In Figure 3, we can see that the larger $h$ gives the better performance. In the case of smaller annotation size, there are many overlapping symbols. For example in Table III, we can see $\mathcal{S}[2]$ mainly generates $a \mathcal{S}[0]$ and $a \mathcal{S}[3]$. However, $\mathcal{S}[2]$ also generates $b \mathcal{S}[3] \mathcal{S}[3]$ and $c \mathcal{S}[3] \mathcal{S}[3] \mathcal{S}[3]$. This overlap makes the probability $P(T ; \Theta)$ of the optimum smaller and it is more difficult to find the optimum. On the other hand, in the case of large $h$, there are
![img-3.jpeg](img-3.jpeg)

Fig. 4. Transition of log-likelihood in the royal tree problem using PAGE. We show the transition at generation $=0$ and 11 .

TABLE II
Obtained PRObABILITIES OF PAGE $(h=8)$ AND PCFG-GP. We SELECTED THE RULE WITH THE HIGHEST PROBABILITIES FROM A START SYMBOL (GRAY RULES).

many redundant symbols. Thus overlappingly used symbol as $\mathcal{S}[2]$ is less in this case.

PAGE estimates the parameters with EM algorithm which monotonically increases the likelihood. Figure 4 describes the increase of log-likelihood $\left(\sum_{T_{i} \in \mathbf{T}} \log P\left(T_{i} ; \Theta\right)\right)$ in the royal tree problem using PAGE. We show the transition of generation 0 and generation 11 . As can been seen with this figure, parameters are converged around by 10 iterations. The log-likelihood improvement at generation 11 is larger than that at generation 0 , because the tree structures are converged at the end of the search.

## B. DMAX problem

1) Problem Description: We applied our approach to DMAX problem [5] to show the superiority of our proposal over Simple GP. DMAX problem is an extended problem of the MAX problem. Because the original MAX problem does not have deceptiveness, it is very easy to solve by GP-EDAs without considering the interactions. We extended the MAX problem by adding the deceptiveness and we call this extended problem deceptive MAX problem (DMAX problem). We employed the function $\mathfrak{F}$ and terminal $\mathfrak{T}$ given by

$$
\begin{aligned}
\mathfrak{F} & =\left\{+_{m}, \times_{m}\right\} \\
\mathfrak{T} & =\{\lambda, 0.95\}
\end{aligned}
$$

with

$$
\lambda^{r}=1, \lambda \in \mathbb{C}, r \in \mathbb{N}
$$

where $+_{m}$ and $\times_{m}$ are $m$ arity version of + and $\times$, respectively, and $\lambda$ is generally a complex value.

The main objective of the DMAX problem is identical to the original one: to find the functions which return the largest real value under the limitation on maximum tree depth $D$. However, the symbols used in the DMAX problem are different from those used in the MAX problem. The DMAX problem uses the symbols represented with Equation 17. A fitness value of individual is the real part of its function. If the value of a function is $a+b i$ (where $a, b \in \mathbb{R}, i=\sqrt{-1}$ ), then its fitness value is $a$. The DMAX problem can be represented with 3 parameters, $m$ (arity), $r$ (power) and $D$ (maximum tree depth).

In this problem, the optimum value is more complicated than that of the MAX problem [3], [9] which does not have the deceptiveness. We explain the optimum with an intuitive example. We use $m=5, r=3$, for example, because DMAX problem has very strong deceptiveness with this setup. In the comparative experiment, we used $D=4$, but for simplification, we explain the case with $D=3$ (Figure 5). In this parameter setup, $\lambda=\cos \frac{2 \pi}{a}+i \sin \frac{2 \pi}{a}$. First, we add $\lambda$ with $+_{5}$ to make $5 \lambda$. Then we multiply this value with $\times_{5}$ which leads to $(5 \lambda)^{5}=5^{5} \lambda^{5}=5^{5} \lambda^{2}$. However, $R e\left(5^{5} \lambda^{2}\right)$ is negative value and is not a good solution. So 2 values out of 5 values multiplied have to be real values. $5 \times 0.95$ is used as a substitution for $5 \lambda$ and the maximum value is $(5 \lambda)^{3}(0.95 \times 5)^{2}=2820.3125$. In $D=4$, the maximum value is $(5 \lambda)^{24}(0.95 \times 5)=2.83 \times 10^{17}$. Figure 6 shows a visualization of the values in the complex plane whose horizontal (real) axis expresses a fitness value. As can been seen, the replacement of one $0.95 \times 5$ with $5 \lambda$ increases the argument by 120 degrees in the complex plane. After three times of replacement, the value returns to the same phase but has a larger absolute value.

The production rules employed in PAGE and PCFG-GP are represented by following equations.
![img-4.jpeg](img-4.jpeg)

Fig. 5. The optimum of the DMAX problem in the complex plane (see text).
![img-5.jpeg](img-5.jpeg)

Fig. 6. Probability of success in the DMAX problem with $M=3000$ PAGE and Simple GP . The result of PCFG-GP is not presented because it could not obtain optimum even at once.

$$
\begin{aligned}
\mathcal{S} & \rightarrow+_{5} \mathcal{S} \mathcal{S} \mathcal{S} \mathcal{S} \\
\mathcal{S} & \rightarrow \times_{5} \mathcal{S} \mathcal{S} \mathcal{S} \mathcal{S} \\
\mathcal{S} & \rightarrow 0.95 \\
\mathcal{S} & \rightarrow \lambda
\end{aligned}
$$

For the DMAX problem of $D=4, m=5$ and $r=3$, we used $M=3000$ in PAGE, PCFG-GP and SGP. The number of latent annotations $h$ is set to 8 . The tournament size of SGP is $t_{s}=2, t_{s}=4$. We run each algorithm 20 times and observed the probability of success at each generation. We stop every algorithm when they obtain the optimum. Furthermore, we stop PAGE and PCFG-GP when the best fitness is not improved for 10 consecutive generations and stop SGP when the best fitness is not improved for generation $g$ to $2 g(g>10)$.
2) Result: We show the probability of success in DMAX problem in Figure 6. Because PCFG-GP could not find the optimum even at once, we omit the result of PCFG-GP. In DMAX problem, two building-blocks have to be used to obtain the optimum: the one composed of five 0.95 and

TABLE III
Estimated PRObABILITIES IN PAGE $(h=8)$. BECAUSE OF SPACE LIMITATION, RULES WITH PROBABILITIES SMALLER THAN 0.01 ARE OMITTEO.


one composed of five $\lambda$. Production rules which generate 0.95 and $\lambda$ have the same left-side symbol $(\mathcal{S} \rightarrow 0.95$ and $\mathcal{S} \rightarrow \lambda$ ). Because PCFG-GP does not distinguish two symbols, structures composed of mixture of 0.95 and $\lambda$ are generated (e.g. $\lambda+\lambda+0.95+\lambda+0.95$ ). Thus the algorithm without annotations failed to obtain the optimum. On the other hand, in PAGE, 0.95 and $\lambda$ are generated from different production rules. Table III shows the estimated production rules by PAGE $(h=8)$. As can been seen with Table III, $\lambda$ and 0.95 are generated from different symbols. $\mathcal{S}[0]$, $\mathcal{S}[3], \mathcal{S}[4], \mathcal{S}[5]$ generate $\lambda$ and $\mathcal{S}[7]$ generates 0.95 . Thus the substructures which are mixtures of $\lambda$ and 0.95 are not generated.

As can been seen with Figure 6, PAGE shows the much better performance compared to those of GPs ( $t_{a}=2$ and $t_{a}=4$ ). As shown in the paper [5], DMAX problem has very strong deceptiveness when using the crossover in GP especially when using higher selection pressure. DMAX problem takes advantage of the defect of a crossover operator. Our approach effectively estimates the parameters with latent annotations, the deceptiveness of DMAX problem can be overcome.

## VI. DISCUSSION

We have employed the PCFG with latent annotations which weakens the independence assumption. Because the statistical estimation in PAGE uses EM algorithm and is a much more complex way compared to simple PCFG, our approach is more computationally expensive. However, the performance of PAGE is much more superior to the algorithm not including the annotations. We can say that PAGE is a stronger algorithm than simple PCFG-GP as a whole.

PAGE has extra parameters and the number of annotations has to be given in advance. The experiment of the royal tree problem showed that the larger $h$ gave the better performance. However, an estimation of larger $h$ requires more computational time. We have to optimize these two contradicting factors which will be examined in the future work. Because EM algorithm is basically hill-climbing strategy,
the optimized parameters are greatly affected by the initial parameters. In this paper, we tried EM algorithm 3 times at each generation and adopted the set of parameters which offered the best log-likelihood. More sophisticated way to optimize parameters may be used.

## VII. CONCLUSION

We proposed the probabilistic program evolution algorithm named PAGE. Our proposal takes advantage of latent annotations which weaken the context freedom assumption in CFG. With two computational experiments, we confirmed that the latent annotations are highly effective for grasping the building-blocks. In the royal tree problem, we showed that the number of annotations greatly affects the search performance and larger annotation size offered better performance. The result of DMAX problem showed that PAGE is highly effective for the problem with strong deceptiveness. We hope that POLE is applied to a wide class of real world problems, which is our future subject.

## APPENDIX

In Appendix, we show the derivation of Equation 13 and 14. Using Equation 1, $Q\left(\Theta^{\prime} \mid \Theta\right)$ can be rewritten into Equation 19.

$$
Q\left(\Theta^{\prime} \mid \Theta\right)=\sum_{T_{i} \in \mathbf{T}} \frac{1}{P\left(T_{i} ; \Theta\right)} \sum_{\mathbf{X}_{i}} P\left(T_{i}, \mathbf{X}_{i} ; \Theta\right)
$$

$$
\times\left\{\log \pi^{\prime}\left(\mathcal{S}\left[x_{j}^{i}\right]\right)+\log \prod_{r \in D_{T_{i} ;} x_{j} ;} \beta^{\prime}(r)\right\}
$$

In this equation, $x_{j}^{i}$ is an annotation of a $j$ th node in an $i$ th tree. Equation 19 consists of two terms $\left(\pi^{\prime}\left(\mathcal{S}[x]\right)\right.$ and $\beta^{\prime}(r)$ ) and both parts can be minimized independently. Let the left and right part be $Q_{\pi}$ and $Q_{\beta}$, respectively.

We only show the derivation of $\beta^{\prime}$, because $\pi^{\prime}$ can be derived in the similar and easier way. By using Equation 12, $Q_{\beta}$ can be represented by Equation 20.

$$
Q_{\beta}=\sum_{T_{i} \in \mathbf{T}} \frac{1}{P\left(T_{i} ; \Theta\right)} \sum_{\mathbf{X}_{i}} P\left(\mathbf{X}_{i}, T_{i} ; \Theta\right) \sum_{r \in D_{T_{i} ;} \mathbf{x}_{i} ;} \log \beta^{\prime}(r)
$$

Let us focus on the production rule which generates $g$ $\left(\mathcal{S}[x] \rightarrow g \mathcal{S}[y] \ldots \mathcal{S}[y]\right)$. Equation 20 can be decomposed into Equation 21.

$$
Q_{\beta}=\sum_{g \in T} Q_{\beta}(g)
$$

Let $x_{j}^{i}$ be the annotation of $j$ th non-terminal at $T_{i}$ and $y_{j}^{i}$ be the annotation of right-side symbol of $j$ th non-terminal at $T_{i}$.

$$
\begin{aligned}
Q_{\beta}(g)= & \sum_{T_{i} \in \mathbf{T}} \frac{1}{P\left(T_{i} ; \Theta\right)} \sum_{j \in \operatorname{cover}\left(g, T_{i}\right)} \sum_{\mathbf{X}_{i}} P\left(\mathbf{X}_{i}, T_{i} ; \Theta\right) \\
& \times \log \beta^{\prime}\left(\mathcal{S}\left[x_{j}^{i}\right] \rightarrow g \mathcal{S}\left[y_{j}^{i}\right] \ldots \mathcal{S}\left[y_{j}^{i}\right]\right) \\
= & \sum_{T_{i} \in \mathbf{T}} \frac{1}{P\left(T_{i} ; \Theta\right)} \\
& \times \sum_{j \in \operatorname{cover}\left(g, T_{i}\right) x_{j}^{i}, g_{j}^{i} \in H} \log \beta^{\prime}\left(\mathcal{S}\left[x_{j}^{i}\right] \rightarrow g \mathcal{S}\left[y_{j}^{i}\right] \ldots \mathcal{S}\left[y_{j}^{i}\right]\right) \\
& \times \sum_{\mathbf{X}_{i} ; x_{j}^{i}, g_{j}^{i}} P\left(\mathbf{X}_{i}, T_{i} ; \Theta\right) \\
= & \sum_{T_{i} \in \mathbf{T}} \frac{1}{P\left(T_{i} ; \Theta\right)} \\
& \times \sum_{j \in \operatorname{cover}\left(g, T_{i}\right) x_{j}^{i}, g \in H} \log \beta^{\prime}\left(\mathcal{S}[x] \rightarrow g \mathcal{S}[y] \ldots \mathcal{S}[y]\right) \\
& \times \beta\left(\mathcal{S}[x] \rightarrow g \mathcal{S}[y] \ldots \mathcal{S}[y]\right) f_{T_{i}}^{j}(x) \prod_{k \in \operatorname{ch}(j, T_{i})} b_{T_{i}}^{k}(y)
\end{aligned}
$$

To optimize $Q\left(\Theta^{\prime} \mid \Theta\right)$ with constraint $\sum_{\zeta} \beta^{\prime}\left(\mathcal{S}[x] \rightarrow \zeta\right)=$ $1(\zeta \in\{\eta \mid \mathcal{S}[x] \rightarrow \eta \in \mathcal{R}[H]\})$, Lagrange multiplier $\mu$ is used.

$$
\begin{aligned}
\mathcal{L}= & Q_{\beta}+\mu\left(1-\sum_{\zeta: \mathcal{S}[x] \rightarrow \zeta \in R[H]} \beta^{\prime}(\mathcal{S}[x] \rightarrow \zeta)\right) \\
& \frac{\partial}{\partial \beta^{\prime}\left(\mathcal{S}[x] \rightarrow g \mathcal{S}[y] \ldots \mathcal{S}[y]\right)} \mathcal{L}=0
\end{aligned}
$$

Parameter update formula can be obtained by solving Equation 22. Update formula of $\pi^{\prime}(\mathcal{S}[x])$ in $Q_{\pi}$ can be derived in the same ways.