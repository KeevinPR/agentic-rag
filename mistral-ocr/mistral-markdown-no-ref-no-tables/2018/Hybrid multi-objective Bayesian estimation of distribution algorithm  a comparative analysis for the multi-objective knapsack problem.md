# Hybrid multi-objective Bayesian estimation of distribution algorithm: a comparative analysis for the multi-objective knapsack problem 

Marcella S. R. Martins ${ }^{1}$ (D) $\cdot$ Myriam R. B. S. Delgado ${ }^{1}$ ・ Ricardo Lüders ${ }^{1}$ ・ Roberto Santana ${ }^{2} \cdot$ Richard A. Gonçalves ${ }^{3} \cdot$ Carolina P. de Almeida ${ }^{3}$<br>Received: 23 December 2016 / Revised: 28 May 2017 / Accepted: 28 August 2017 (C) Springer Science+Business Media, LLC 2017


#### Abstract

Nowadays, a number of metaheuristics have been developed for efficiently solving multi-objective optimization problems. Estimation of distribution algorithms are a special class of metaheuristic that intensively apply probabilistic modeling and, as well as local search methods, are widely used to make the search more efficient. In this paper, we apply a Hybrid Multi-objective Bayesian Estimation of Distribution Algorithm (HMOBEDA) in multi and many objective scenarios by modeling the joint probability of decision variables, objectives, and the configuration parameters of an embedded local search (LS). We analyze the benefits of the online configuration of LS parameters by comparing the proposed approach with LS off-line versions using instances of the multi-objective knapsack problem with two to five and eight objectives.


[^0]
[^0]:    Marcella S. R. Martins marcella@utfpr.edu.br

    Myriam R. B. Delgado myriamdelg@utfpr.edu.br

    Ricardo Lüders
    luders@utfpr.edu.br
    Roberto Santana roberto.santana@ehu.es

    Richard A. Gonçalves
    richard@unicentro.br
    Carolina P. de Almeida
    carol@unicentro.br
    1 Federal University of Technology - Paraná (UTFPR), Av. Sete de Setembro, 3165, Curitiba, PR, Brazil

    2 University of the Basque Country (UPV/EHU), 20018 Donostia, San Sebastián, Spain
    3 Midwest State University of Parana (UNICENTRO), Guarapuava, PR, Brazil

HMOBEDA is also compared with five advanced evolutionary methods using the same instances. Results show that HMOBEDA outperforms the other approaches including those with off-line configuration. HMOBEDA not only provides the best value for hypervolume indicator and IGD metric in most of the cases, but it also computes a very diverse solutions set close to the estimated Pareto front.

Keywords Multi-objective estimation of distribution algorithms $\cdot$ Probabilistic modeling $\cdot$ Local search $\cdot$ Hybridization $\cdot$ Automatic algorithm configuration

# 1 Introduction 

In many optimization problems, maximizing/minimizing several objective functions represents a challenge to a large number of optimizers (specially for single-objective approaches which are usually no longer applicable in these cases) (Luque 2015). This class of problems is known as Multi-objective Optimization Problems (MOPs), and multi-objective optimization has thus been established as an important field of research (Deb 2001). Recently, problems with more than three objectives are becoming usual and the area has been referred to as many objective optimization (Ishibuchi et al. 2008).

Evolutionary algorithms (EAs) and other metaheuristics have been widely used for solving multi and many objective optimization, mainly due to their ability to discover multiple solutions in parallel and to handle the complex features of such problems (Coello 1999). In most of cases, local optimizers and probabilistic modeling can also be aggregated to capture and exploit the potential regularities that arise in the promising solutions.

As a special case of these hybrid approaches, Multi-objective Evolutionary Algorithms (MOEAs) incorporating local search (LS) have been investigated, and can often achieve good performance for many problems (Lara et al. 2010; Zhou et al. 2011, 2015. However, as discussed in Martins et al. (2016), they still present challenges, like the choice of suitable LS parameters (e.g., the type, frequency and intensity of LS applied on a specific candidate solution).

Some previous works have proposed techniques for configuring and tuning the parameters, like in Freitas et al. (2014), where the authors present a method based on evolutionary strategies with local search and self-adaptation of the parameters for single-objective optimization. Another example is Corriveau et al. (2016), where an adaptive parameter setting approach solves multimodal problems using genetic algorithms and Bayesian networks. These techniques can also be extended to multi-objective optimization. In López-Ibáñez et al. (2011), the I/F-race tool integrates the hypervolume indicator into the iterated process to automatically configure multi-objective algorithms with many parameters for an optimization problem. This technique can be used with other unary quality indicators, such as epsilon or Rindicator.

Another strategy widely used in evolutionary optimization is probabilistic modelling, which is the base of Estimation of Distribution Algorithms (EDAs) (Mühlenbein and Paab 1996). The main idea of EDAs (Larrañaga and Lozano 2002) is to extract and represent, using a probabilistic graphical model (PGM), the regularities shared by

a subset of high-valued problem solutions. New solutions are then sampled from the PGM biasing the search to areas where optimal solutions are more likely to be found. Normally, EDAs integrate both, the model building and sampling techniques, into evolutionary optimizers using special selection schemes (Laumanns and Ocenasek 2002).

This paper addresses a combinatorial MOP-the multi-objective version of the well known knapsack problem named Multi-objective Knapsack Problem (MOKP) which has been recently explored in other works in the literature (Ishibuchi et al. 2015; Ke et al. 2014; Tan and Jiao 2013; Tanigaki et al. 2014; Vianna and de Fátima Dianin Vianna 2013). In particular, Multi-objective Estimation of Distribution Algorithms (MOEDAs) that use different types of probabilistic models have already been applied to MOKP (Li et al. 2004; Wang et al. 2012), specially those EDAs based on Bayesian networks as reported in Laumanns and Ocenasek (2002), Martins et al. (2016) and Schwarz and Ocenasek (2001).

The approach considered in this paper is named HMOBEDA and is based on a joint probabilistic modeling of decision variables, objectives, and parameters of the local optimizer. As discussed in Martins et al. (2016), the rationale of HMOBEDA is that the embedded PGM can be structured to sample appropriate LS parameters for different configurations of decision variables and objective values during the search (which is named online configuration). However, differently from Martins et al. (2016), this work includes an additional investigation of off-line versions of LS parameter tuning: HMOBEDA ${ }_{f}$, HMOBEDA $_{f_{\text {init }}}$ and HMOBEDA $_{\text {irace }}$.

In HMOBEDA $_{\text {irace }}$ for example, an automatic configuration tool (irace) that is considered a state-of-the-art method for parameter tuning is adopted to define the LS parameters. Therefore in our framework it is possible to compare both techniques: online and off-line LS configuration approaches. Aiming to evaluate an indicator-based approach, this work presents another HMOBEDA version based on the hypervolume indicator (Bader 2009) as part of the selection procedure.

This work also compares HMOBEDA with traditional approaches for multi and many objective optimization based on the Inverted Generational Distance (IGD) quality indicator in addition to the hypervolume (HV) metric. Our work has intersections with other previous published works (Bader 2009; Karshenas et al. 2014; Li et al. 2004). It is linked to the work presented in Karshenas et al. (2014) in which a joint probabilistic model of objectives and variables is proposed, and related to Li et al. (2004) by considering a weighted sum method in the fitness computation of each neighbor produced by the LS procedure. In contrast with the research presented in Li et al. (2004), our work considers an objective alternate mode to fitness computation and a bayesian network as the PGM.

Therefore, besides providing a natural extension of previous works to investigate probabilistic modeling of variables, objectives and LS parameters all together, the main contributions on the present work are: (i) it extends the original HMOBEDA proposal providing other variants where the LS parameters are determined in different ways and fixed along the search (off-line configuration); (ii) it also presents a different HMOBEDA version that computes and uses the hypervolume indicator (Bader 2009) as part of the selection procedure; (iii) the comparison with state-of-the-art-algorithms includes the IGD metric to provide a more complete picture of HMOBEDA behavior.

This paper is organized as follows. Section 2 provides a brief introduction to EDAs and Bayesian network as PGM (Larrañaga et al. 2012). Section 3 details the proposed approach. Results from numerical experiments are shown and discussed in Sect. 4, with the conclusions and future directions presented in Sect. 5.

# 2 Preliminaries 

EDAs are population based optimization algorithms that have been claimed as a paradigm shift in the field of EA, which employ explicit probability distributions in optimization (Larrañaga and Lozano 2002).

EDAs have achieved good performance when applied in several problems (Pham 2011) including environmental monitoring network design (Kollat et al. 2008), protein side chain placement problem (Santana et al. 2008), table ordering (Bengoetxea et al. 2011), multi-objective knapsack (Shah and Reed 2011) and MOPs in a noisy environment (Shim et al. 2013).

Based on the problem solution representation, EDAs can be classified in discrete and real-valued, considering the variables that can either be discrete ones or receive a real value that covers an infinite domain. According to the interactions between variables, EDA models can be categorized into three classes (Hauschild and Pelikan 2011): Univariate, Bivariate and Multivariate based on the level of interactions among variables.

Univariate EDAs assume no interaction among variables, and Univariate Marginal Distribution Algorithm (UMDA) (Mühlenbein and Paab 1996) is an example. For bivariate EDAs, pairwise interactions among variables in the solutions are considered, like in Bivariate Marginal Distribution Algorithm (BMDA) (Pelikan and Muehlenbein 1999). Multivariate EDAs use probabilistic models capable of capturing multivariate interactions between variables (Bengoetxea et al. 2011). Algorithms using multivariate models of probability distribution include: Extended Compact Genetic Algorithm (ECGA) (Harik 1999), Bayesian Network Algorithm (EBNA) (Etxeberria and Larrañaga 1999), Factorised Distribution Algorithm (FDA) (Mühlenbein and Mahnig 1999), Bayesian Optimisation Algorithm (BOA) (Pelikan et al. 1999), Hierarchical Bayesian Optimisation Algorithm (hBOA) (Pelikan et al. 2003), Markovianity-based Optimisation Algorithm (MOA) (Shakya and Santana 2008) and Affinity Propagation EDA (AffEDA) (Santana et al. 2010).

Another relevant classification is according to the probability model learning: algorithms that only make a parametric learning of the probabilities, like UMDA; and algorithms where structural learning of the model is also done, like the ones using Bayesian networks (Santana et al. 2008).

### 2.1 Bayesian network as PGM

Bayesian networks (BN) are directed acyclic graphs (DAG) whose nodes represent variables, and whose missing edges encode conditional independencies between triplets of variables. Random variables represented by nodes may be observable quantities, latent variables, unknown parameters or hypotheses. Each node is associated with a probability function that takes as input a particular set of values for the node's

parent variables and gives the probability of the variable represented by the node (Cooper and Herskovits 1992; Korb and Nicholson 2010).

Let $\mathbf{Y}=\left(Y_{1}, \ldots, Y_{M}\right)$ be a set of random variables, and let $y_{m}$ be a value of $Y_{m}$, the $m$-th component of $\mathbf{Y}$. The representation of a bayesian model is given by two components (Larrañaga et al. 2012): a structure and a set of local parameters. The set of local parameters $\theta_{B} \in \boldsymbol{\Theta}_{B}$ containing, for each variable, the conditional probability distribution of its values given different value settings for its parents, according to structure $B$.

The structure $B$ for $\mathbf{Y}$ is a DAG that describes a set of conditional independencies about triplets of variables in $\mathbf{Y} . \mathbf{P a}_{m}^{B}$ represents the set of parents (variables from which an arrow is coming out in $B$ ) of the variable $Y_{m}$ in the PGM which structure is given by $B$ (Bengoetxea 2002). The structure $B$ for $\mathbf{Y}$ assumes that $Y_{m}$ and its non descendants are conditionally independent given $\mathbf{P a}_{m}^{B}, m=2, \ldots, M$, where $Y_{1}$ is the root note.

Therefore, a Bayesian network encodes a factorization for the joint probability distribution of the variables as follows:

$$
\rho(\mathbf{y})=\rho\left(y_{1}, y_{2}, \ldots, y_{M}\right)=\prod_{m=1}^{M} \rho\left(y_{m} \mid \mathbf{p a}_{m}^{B}\right)
$$

Equation 1 states that the joint probability distribution of the variables can be computed as the product of each variables conditional probability distributions given the values of its parents. These conditional probabilities are stored as local parameters $\theta_{B}$, where $\theta_{B}=\left(\theta_{1}, \ldots, \theta_{M}\right)$.

In discrete domains, $Y_{m}$ has $s_{m}$ possible values, $y_{m}^{1}, \ldots, y_{m}^{s_{m}}$, therefore the local distribution, $p\left(y_{m} \mid \mathbf{p a}_{m}^{j, B}, \theta_{m}\right)$ is a discrete distribution:

$$
p\left(y_{m}^{k} \mid \mathbf{p a}_{m}^{j, B}, \theta_{m}\right)=\theta_{y_{m}^{k} \mid \mathbf{p a}_{m}^{j, B}}=\theta_{m j k}
$$

where $\mathbf{p a}_{m}^{1, B}, \ldots, \mathbf{p a}_{m}^{t_{m}, B}$ denotes the combination of values of $\mathbf{P a}_{m}^{B}$, that is the set of parents of the variable $Y_{m}$ in the structure $B ; t_{m}$ is the number of different possible instantiations of the parent variables of $Y_{m}$. The possible number of $t_{m}$ combination of values that $\mathbf{P a}_{m}$ can assumes is $t_{m}=\prod_{Y_{v} \in \mathbf{P a}_{m}^{B}} s_{v}$. The parameter $\theta_{m j k}$ represents the conditional probability that variable $Y_{m}$ takes its $k$-th value $\left(y_{m}^{k}\right)$, knowing that its parent variables have taken their $j$-th combination of values $\left(\mathbf{p a}_{m}^{j, B}\right)$.

The BN learning process can be divided into (i) structural learning, i.e., identification of the topology $B$ of the BN and (ii) parametric learning, estimation of the numerical parameters (conditional probabilities $\boldsymbol{\Theta}$ ) for a given network $B$.

Most of the developed structure learning algorithms fall into the score-based approaches. Score-based learning methods evaluate the quality of BN structures using a scoring function, like Bayesian Dirichlet (BD)-metric (Heckerman et al. 1995), and search for the best one. The BD metric, defined by Eq. 3, combines the prior knowledge about the problem and the statistical data from a given data set.

$$
p(B \mid P o p)=p(B) \prod_{m=1}^{M} \prod_{j=1}^{t_{m}} \frac{\Gamma\left(\alpha_{m j}\right)}{\Gamma\left(\alpha_{m j}+N_{m j}\right)} \prod_{k=1}^{s_{m}} \frac{\Gamma\left(\alpha_{m j k}+N_{m j k}\right)}{\Gamma\left(\alpha_{m j k}\right)}
$$

where $p(B)$ is the prior factor of quality information of the network $B$. If there is no prior information for $B, p(B)$ is considered a uniform probability distribution (Luna 2004) and generally its value is set to 1 (Crocomo and Delbem 2011). The product on $j \in\left\{1, \ldots, t_{m}\right\}$ runs over all combinations of the parents of $Y_{m}$ and the product on $k \in\left\{1, \ldots, s_{m}\right\}$ runs over all possible values of $Y_{m} . N_{m j}$ is the number of instances in Pop with the parents of $Y_{m}$ instantiated to its $j$-th combination. By $N_{m j k}$, we denote the number of instances in Pop that have both $Y_{m}$ set to its $k$-th value as well as the parents of $Y_{m}$ set to its $j$-the combination of values. $\Gamma(x)=(x-1)$ ! for $x \in N$ is the Gamma function used in Dirichlet prior (DeGroot 2005) that satisfies $\Gamma(x+1)=x \Gamma(x)$ and $\Gamma(1)=1$.

Through $\alpha_{m j k}$ and $p(B)$, prior information about the problem is incorporated into the metric. The parameters $\alpha_{m j k}$ stands for prior information about the number of instances that have $Y_{m}$ set to its $k$-th value and the set of parents of $Y_{m}$ is instantiated to its $j$-th combination. The prior network can be set to an empty network, when there is no such information.

In the so-called K2 metric (Cooper and Herskovits 1992) for instance, the parameters $\alpha_{m j k}$ can be set to 1 as there is no prior information about the problem, and Eq. 3 becomes Eq. 4:

$$
p(B \mid \text { Pop })=p(B) \prod_{m=1}^{M} \prod_{j=1}^{t_{m}} \frac{\left(s_{m}-1\right)!\left(N_{m j}+s_{m}-1\right)!} \prod_{k=1}^{s_{m}}\left(N_{m j k}\right)!
$$

Since the factorials in Eq. 4 can grow to huge numbers, a computer overflow might occur. Thus the logarithm of the scoring metric $\log (p(B \mid$ Pop $)$ ) is usually used, as shown in Eq. 5.

$$
\log (p(B \mid P o p))=\log (p(B))+\sum_{m=1}^{M} \sum_{j=1}^{t_{m}}\left(\log \left(\frac{\left(s_{m}-1\right)!}{\left(N_{m j}+s_{m}-1\right)!}\right)+\sum_{k=1}^{s_{m}} \log \left(\left(N_{m j k}\right)!\right)\right)
$$

Various algorithms can be used for searching the networks structures to maximize the value of a scoring metric, like a simple greedy algorithm, local hill-climbing, simulated annealing, tabu search and evolutionary computation (Larrañaga et al. 2012).

The K2 algorithm is a greedy local search technique that applies K2 metric in its logarithmic form (Eq. 5). It starts by assuming that a node does not have parents, then in each step it gradually adds the edges which increase the scoring metric the most until no edge increases the metric anymore. The variables ordering are the incoming input to the algorithm, which might heavily alter the results (Larrañaga et al. 2013), as it pre-establishes a possible relation between a node and its parents (ascendent nodes).

Other greedy local search techniques also apply K2 metric, like in Pelikan (1999), where the authors implemented a modified K2 algorithm considering no variables ordering, resulting in a high DAG search space.

In this work we adopted K2 metric as score-based technique, although any other method could be used as well. We use the K2 algorithm considering the objectives as parents in the network.

Regarding to the parameter estimation and considering that BN's are often used for modeling multinomial data with discrete variables (Pearl 1988), we applied the Bayesian estimate, which considers the expected value $E\left(\theta_{m j k} \mid \mathbf{N}_{m j}, B\right)$ of $\theta_{m j k}$ as an estimate of $\theta_{m j k}$, as shown in Eq. 6.

$$
E\left(\theta_{m j k} \mid \mathbf{N}_{m j}, B\right)=\left(1+N_{m j k}\right) /\left(s_{m}+N_{m j}\right)
$$

where $N_{m j k}$ fits a multinomial distribution, and $N_{m j}=\sum_{k=1}^{s_{m}} N_{m j k}$.

# 3 The algorithm: HMOBEDA 

In this section, we detail the HMOBEDA framework emphasizing its main characteristics, i.e., the probabilistic model encompassing three types of nodes: decision variables, objectives and configuration parameters of its embedded LS.

### 3.1 Encoding scheme

Every individual is represented by a joint vector with $Q+R+L$ elements, $\mathbf{y}=$ $(\mathbf{x}, \mathbf{z}, \mathbf{p})=\left(X_{1}, \ldots, X_{Q}, Z_{1}, \ldots, Z_{R}, P_{1}, \ldots, P_{L}\right)$, denoting the decision variables $\left(X_{1}, \ldots, X_{Q}\right)$, objectives $\left(Z_{1}, \ldots, Z_{R}\right)$ and LS parameters $\left(P_{1}, \ldots, P_{L}\right)$. Subvectors $\mathbf{x}, \mathbf{z}$ and $\mathbf{p}$ can be specified as:

- $\mathbf{x}$ is a binary subvector of items, with element $X_{q} \in\{0,1\}, q=1 \ldots Q$, indicating the presence or absence of the associated item;
- $\mathbf{z}$ is a subvector of objectives, with element $Z_{r}, r=1 \ldots R$, representing the discrete value of the $r t h$ objective.
- $\mathbf{p}$ is a subvector of elements, where each element $P_{l}, l=1 \ldots L$, indicates the value associated with an LS parameter. Different parameters can be considered. For example, the maximum number of iterations performed by LS, the neighborhood type and the type of procedure used to compute the neighbor fitness.


### 3.2 The HMOBEDA framework

A general schema of the adopted version of HMOBEDA is presented in Fig. 1.
The Initialization process randomly generates $N$ subvectors $\mathbf{x}$ and $\mathbf{p}$ to compose the initial population $P o p^{1}$. For each subvector $\mathbf{x}$, the values of the corresponding objectives are calculated based on the objective functions of the addressed problem and further made discrete to form the subvector $\mathbf{z}$.

The Survival block sorts individuals using the non-dominated sorting procedure (Srinivas and Deb 1994). It calculates the Dominance Rank (DR) (Zitzler et al. 2000), and also a diversity criterion named Crowding Distance (CD) (Deb et al. 2002). Individuals are sorted taking at first DR and secondly (in case of ties) the CD criterion. Finally, truncation selection takes place selecting the best $N$ solutions (at the first generation the entire population is selected). Besides the original HMOBEDA(Martins et al. 2016), in this work we have also implemented another online configuration of

![img-0.jpeg](img-0.jpeg)

Fig. 1 HMOBEDA framework

HMOBEDA based on the hypervolume indicator, named $\mathrm{HMOBEDA}_{h y p e}$, which substitutes the CD tie-breaker criterion by the hypervolume fitness value in the Survival block of Fig. 1.

In the sequence, the Local Search block adopts a very simple LS procedure based on Hill Climbing (HC) (Russel and Norvig 2003). For every solution in Pop ${ }^{g}$, HCLS generates a neighbor ( $n h b$ ), calculates its fitness and $n h b$ substitutes the original solution in case it has a better fitness. As previously discussed, the subvector $\mathbf{p}$ defines the parameters associated with HCLS. In this paper it defines how many iterations $\left(N_{\text {iter }}\right)$ will be used, how each neighbor will be generated $\left(T_{n b h}\right)$, and finally how to compute the neighbor fitness $\left(T_{F n b h}\right)$ in a single-objective way. If a neighbor is infeasible, the algorithm applies the same greedy repair method as in Zitzler and Thiele (1999). It repairs the solution by removing items in an ascending order of the relation profit/weight until all the constraints conditions are satisfied.

The EDA Selection block starts with the PGM construction phase. A binary tournament selects $N_{P G M}$ individuals from $P o p^{g}$. The procedure randomly selects two solutions and the one positioned in the best front is chosen. If they lie in the same front, it chooses that solution with the greatest CD. Then, $P o p_{P G M}^{g}$ is obtained encompassing $N_{P G M}$ good individuals.

BN structure and BN parameters are estimated based on the joint probabilistic model of $Q$ decision variables, $R$ objectives and $L$ local search parameters, (i.e. $\mathbf{Y}=$ $\left.\left(Y_{1}, \ldots Y_{M}\right)=\left(Z_{1}, \ldots Z_{R}, X_{1}, \ldots X_{Q}, P_{1}, \ldots P_{L}\right)\right)$. It encodes a factorization of the joint probability distributions $\rho(\mathbf{y})=\rho\left(z_{1}, \ldots, z_{R} ; x_{1}, \ldots, x_{Q} ; p_{1}, \ldots, p_{L} ;\right)$ given by:

$$
\rho(\mathbf{y})=\prod_{r=1}^{R} \rho\left(z_{r} \mid \mathbf{p a}_{r}^{B}\right) \cdot \prod_{q=1}^{Q} \rho\left(x_{q} \mid \mathbf{p a}_{q}^{B}\right) \cdot \prod_{l=1}^{L} \rho\left(p_{l} \mid \mathbf{p a}_{l}^{B}\right)
$$

where $\mathbf{P a}_{r}^{B}=\emptyset, \mathbf{P a}_{q}^{B} \subseteq\left\{Z_{1}, \ldots Z_{R}\right\}$ and $\mathbf{P a}_{l}^{B} \subseteq\left\{Z_{1}, \ldots Z_{R}\right\}$ are the parents of each objective, variable and LS parameter node respectively, and $\mathbf{p a}_{r}^{B}, \mathbf{p a}_{q}^{B}$ and $\mathbf{p a}_{l}^{B}$ represent one of their combination of values.

Fig. 2 An example of a PGM used by HMOBEDA
![img-1.jpeg](img-1.jpeg)

Therefore, aiming to learn the probabilistic model, the EDA Model block divides the objective values collected from vector $\mathbf{z}$ in $P o p_{P G M}^{g}$ into $s d_{r}$ discrete states. ${ }^{1}$ Considering that the BN model is estimated using the K2-metric (Eq. 5) and the Bayesian estimate (Eq. 6) with objectives as BN nodes, $\mathbf{z}$ also fits a multinomial distribution. Thus, to minimize the computational efforts to model $B$ using all the $s_{r}$ states, we have applied the discretization process with a limited number of possible values for each $z_{r} \in \mathbf{z}$ fixed as $s d_{r}$. In this case we assume the same $s d_{r}$ value for each $z_{r}$ node. The K2 algorithm is used here by setting parent nodes as objectives in the network. The same parents relationship was considered in Karshenas et al. (2014).

As discussed in Martins et al. (2016), the advantage of HMOBEDA over traditional EDA-based approaches is that besides providing good decision variables (based on the model captured from good solutions present in $P o p_{P G M}^{g}$ ) it can also provide LS parameters more related to good objective values which are fixed as evidence.

In the Sampling block, the obtained PGM is used to sample the set of new individuals (Pop $p_{s m p}$ ). In this case, not only decision variables $\mathbf{x}$, but also, local search parameters p can be sampled. Although the proposed methodology accepts any Bayesian Network structure, in the experiments, all learned structures are as the one represented in Fig. 2, considering no relation between variables, between parameters and between both (variables and parameters). This naive Bayesian model, is adopted to facilitate the sampling process: fixing objective values with high values (for maximization problems) enables the estimation of their associated decision variables and LS parameters.

The union of the sampled population $\left(P o p_{s m p}\right)$ and the current population $\left(P o p^{g}\right)$ in the EDA Merge block is used to create the new population for the next generation $g+1$. Individuals (the old and the new ones) are selected to the next generation in the Survival block, and the main loop continues until the stop condition is achieved.

# 4 Experiments and results 

The multi-objective knapsack problem addressed in this paper can be formulated as follows:

$$
\max _{\mathbf{x}} \mathbf{z}(\mathbf{x})=\left(z_{1}(\mathbf{x}), \ldots, z_{R}(\mathbf{x})\right)
$$

[^0]
[^0]:    ${ }^{1}$ The discretization process converts each objective value into $s d_{r}$ discrete states considering the maximum possible value for each objective $\left(M a x_{r}\right)$. For each objective $r$, its discrete value is calculated as $z d_{r}=$ $\left\lceil z_{r} s d_{r} / M a x_{r}\right\rceil$.

Table 1 Parameters of the algorithms
$$
\begin{aligned}
& \text { subject to } \sum_{q=1}^{Q} b_{r q} x_{q} \leq c_{r}, r=1, \ldots, R \\
& \text { with } z_{r}(\mathbf{x})=\sum_{q=1}^{Q} a_{r q} x_{q}, \mathbf{x} \in\{0,1\}^{Q}
\end{aligned}
$$

where $\mathbf{x}$ is a $Q$-dimension binary vector, such that $x_{q}=1$ means that item $q$ is selected to be in $r$-th knapsack and $a_{r q}, b_{r q}$ and $c_{r}$ are nonnegative coefficients. Given a total of $R$ objective functions (knapsacks) and $Q$ items, $a_{r q}$ is the profit of item $q=1, \ldots, Q$, according to knapsack $r=1, \ldots, R, b_{r q}$ denotes the weight of item $q$ according to knapsack $r$, and $c_{r}$ is the constraint capacity of knapsack $r$.

Experiments conducted in this paper adopt the union of each set of instances considered in Ishibuchi et al. (2015), Tanigaki et al. (2014) and Zitzler and Thiele (1999). We use thus instances for 100 and 250 items, with 2 to 5 and 8 objectives. We characterize each instance as $R-Q$, where $R$ is the number of objectives and $Q$ is the number of items. The values of $a_{q}^{r}$ and $b_{q}^{r}$ are specified as integers in the interval $[10,100]$. According to Zitzler and Thiele (1999), the capacity $c_{r}$ is specified as $50 \%$ of the sum of all weights related to each knapsack $r$.

In this section, we compare the original HMOBEDA(Martins et al. 2016) with four modified versions: HMOBEDA ${ }_{f}$, HMOBEDA $f_{\text {f-inst }}$, HMOBEDA $_{\text {trace }}$ and HMOBEDA $_{\text {hype }}$; and, further, with MBN-EDA (Karshenas et al. 2014), NSGA-II (Deb et al. 2002), S-MOGLS (NSGA-II with local search) (Ishibuchi et al. 2008), MOEA/D (Zhang and Li 2007), and NSGA-III (Deb and Jain 2014).

All algorithms used for comparison are the original ones found in the literature. The exception is NSGA-III that has been adapted for combinatorial optimization. MOEA/D and NSGA-III are implemented in C++, and the remaining algorithms in MatLab.

# 4.1 Algorithm settings 

The parameters for each algorithm are shown in Table 1.
As in Ishibuchi et al. (2008), for S-MOGLS we set the probabilities $P_{l s}$ and bit-flip operation in LS as 0.1 and $4 / 500$, respectively; the number of neighbors $\left(N_{l s}\right)$ to be examined as 20. Therefore, for NSGA-III, we adopt the same configuration used in

Deb and Jain (2014), i.e., the number of reference points $(H)$ defines the population size $N$. For $R$-objective functions, if $p$ divisions are considered along each objective, the authors in Deb and Jain (2014) define $H=C_{R+p-1}^{p}$. In MOEA/D, the number of subproblems equals the population size $N$ and the weight vectors $\lambda^{1}, \ldots, \lambda^{N}$ are controlled by the configuration parameter $W$, calculated as proposed in Zhang and Li (2007) (this is the same procedure used to generate the reference points in NSGA-III). As in Deb and Jain (2014), the size of the neighborhood for each weight vector is $T=10$. MOEA/D considers the weighted sum approach. ${ }^{2}$

The fitness calculation of $\mathrm{HMOBEDA}_{\text {hype }}$ is based on a hypervolume approximation using Monte Carlo simulation, as presented in HypE algorithm proposed by Bader and Zitzler ${ }^{3}$ (Bader and Zitzler 2011) due to the very expensive and time consuming computation of the exact hypervolume fitness (Bader and Zitzler 2011). This method generates random samples in the objective space and it counts the number of samples which are dominated by $P o p^{g}$. The hypervolume is approximated by the ratio between the dominated and total samples. The number of samples used for MonteCarlo approximation is 10,000 .

# 4.2 Testing the influence of LS online configuration 

The LS online configuration adopted by HMOBEDA during the evolution considers the following elements in the vector $\mathbf{p}$ : the number of LS iterations $N_{\text {iter }} \in\{5,6 \ldots, 20\}$; the type of neighbor fitness calculation $T_{F n b h} \in\{1,2\}$ : with (1) representing Linear Combination and (2) Alternation of included objectives (i.e. one objective after the other in each LS iteration); the neighborhood type $T_{n b h} \in\{1,2\}$ : with (1) defining drop-add and (2) insertion.

This paper aims to answer the question "What is the influence (on the HMOBEDA performance) of including LS parameters as BN nodes? As previously discussed, this is a relevant question since the automatic and informed determination of the LS parameters can notably improve the efficiency of the search.

As an attempt to answer this question, we modified the original version of HMOBEDA providing three other versions: $\mathrm{HMOBEDA}_{f}, \mathrm{HMOBEDA}_{f-\text { inst }}$ and $\mathrm{HMOBEDA}_{\text {trace }}$. None of these versions has LS parameter encoded as nodes in the PGM structure and all of them consider the same HMOBEDAparameters of Table 1.

In the LS off-line configuration adopted by the modified algorithms, the first version, $\mathrm{HMOBEDA}_{f}$, considers $N_{\text {iter }}=19, T_{F n b h}=0$ and $T_{n b h}=1$. These values represent the most frequent value of each LS-parameter provided by the original HMOBEDA in the set of non-dominated solutions, considering all the instances and executions. $\mathrm{HMOBEDA}_{f-\text { inst }}$ considers the same rule (i.e. the most frequent value found in all HMOBEDA executions) but now separated for each instance. In this case

[^0]
[^0]:    ${ }^{2}$ This approach is used in an usual application for MOKP (Zhang and Li 2007), which can be downloaded from http://http://dces.essex.ac.uk/staff/zhang/webofmoead.htm and is also suggested in Ishibuchi et al. (2015).
    ${ }^{3}$ This implementation is used in Bader and Zitzler (2011) for more than three objectives and can be downloaded from http://www.tik.ee.ethz.ch/sop/download/supplementary/hype/.

we have $T_{F n b h}=0$ and $T_{n b h}=1$ for all instances; $N_{\text {iter }}=18$ for 3-100, 2-250 and 4-250 instances; $N_{\text {iter }}=10$ for 3-250; $N_{\text {iter }}=19$ for 4-100; $N_{\text {iter }}=16$ for 2-100 and 5-100; and $N_{\text {iter }}=20$ for 8-100, 5-250 and 8-250 instances. $\mathrm{HMOBEDA}_{\text {irace }}$ considers $N_{\text {iter }}=14, T_{F n b h}=0$ and $T_{n b h}=1$. The LS off-line configuration method used for $\mathrm{HMOBEDA}_{\text {irace }}$ is I/F-Race (Birattari et al. 2010), which is a state-of-the-art automatic configuration method. We use the implementation of I/F-Race provided by the irace package (López-Ibáñez et al. 2011). As in López-Ibáñez and Stützle (2012), it performs the configuration process using the hypervolume $\left(\mathrm{HV}^{-}\right)$as the evaluation criterion.

The same instances are used for training and testing off-line versions. The results obtained by $\mathrm{HMOBEDA}_{f} \mathrm{HMOBEDA}_{f-\text { inst }}$ and $\mathrm{HMOBEDA}_{\text {irace }}$ are, thus, quite better than would be expected if the test instances were different.

Aiming to be as fair as possible, we define a stop condition based on the maximum number of fitness evaluations ( $M a x_{\text {eval }}$ ), which includes repair procedures and LSiterations. Then, all algorithms stop when the total number of fitness computations achieve the value 100,000 . A total of 20 independent executions are conducted for each algorithm and from these results the performance metrics are computed.

# 4.3 Performance metrics 

The optimal Pareto front for each instance of the addressed problem is not known. So, we use a reference set, denoted by Ref, which is constructed by gathering all non-dominated solutions obtained by all algorithms over all executions. Two main convergence-diversity (Jiang et al. 2014) metrics, usually adopted for measuring the quality of the optimal solution set for multi and many objective optimization, are then considered: Hypervolume (HV) (Zitzler and Thiele 1999; Bader 2009) and Inverted Generational Distance (IGD) (van Veldhuizen and Lamont 1999).

The hypervolume metric considers the difference $\left(\mathrm{HV}^{-}\right)$between the hypervolume of the solution set of an algorithm and that of the reference set. The IGD metric is the average distance from each solution in the reference set to the nearest solution in the solution set. So, smaller values of $\mathrm{HV}^{-}$and IGD correspond to higher quality solutions in non-dominated sets indicating both better convergence and good coverage of the reference set.

### 4.4 Numerical results

In this section we aim to compare the results of HMOBEDA, HMOBEDA $_{f}$, $\mathrm{HMOBEDA}_{f-\text { inst }}, \mathrm{HMOBEDA}_{\text {irace }}, \mathrm{HMOBEDA}_{\text {hype }}, \mathrm{MOEA} / \mathrm{D}, \mathrm{MBN}-\mathrm{EDA}, \mathrm{NS}-$ GA-II, NSGA-III and S-MOGLS.

Table 2 shows the hypervolume difference $\left(\mathrm{HV}^{-}\right)$and IGD metric, both averaged over 20 executions of each algorithm. The lowest values are highlighted (in bold). We use PISA framework (Bleuler et al. 2003) to compute $\mathrm{HV}^{-}$and Matlab to compute IGD.

We note, in Table 2, that HMOBEDA always produces the lowest average values for $\mathrm{HV}^{-}$(except in 2-500 instance, where MOEA/D has competitive values for

Table 2 Average $\mathrm{HV}^{-}$and IGD
Average hypervolume differences $\left(\mathrm{HV}^{-}\right)$


Average IGD metric

both $\mathrm{HV}^{-}$and IGD). Regarding IGD metric, NSGA-III achieves lower average values for instances that have 2, 3 and 4 objectives with 100 items, and $\mathrm{HMOBEDA}_{h y p e}$ has the lowest average value for $5-250$. However the remaining instances stand HMOBEDA as a competitive approach.

The analysis is now expanded to include statistical tests. First we aim to analyze the use of CD versus hypervolume as tie-breaker criterion comparing HMOBEDAwith $\mathrm{HMOBEDA}_{\text {hype }}$. Then we proceed with the analysis by evaluating the influence of LS online configuration based on BN nodes, comparing the original HMOBEDA with its off-line configured versions. Then, we define the standard version that will be further compared with other approaches reported in the literature.

Based on the Shapiro-Wilk normality test (Conover 1999) we have concluded that $\mathrm{HV}^{-}$and IGD results are not normally distributed. Then, the Kruskal-Wallis test has been applied for statistical analysis (Casella and Berger 2001) of the results for the LS off-line versions, and the Mann-Whitney-Wilcoxon test for HMOBEDA $_{h y p e}$. All tests have been executed with a significance level of $\alpha=0.05$.

Table 3 Results for pairwise comparisons between HMOBEDAand $\mathrm{HMOBEDA}_{\text {hype }}$ using Mann-Whitney-Wilcoxon test with $\alpha=0.05$ for each problem instance

First we compare HMOBEDA with HMOBEDA $_{\text {hype }}$, and then, with its off-line modified versions. The results of the test reveal that the null hypothesis that all the algorithms have $\mathrm{HV}^{-}$values with no statistically significant difference can be rejected for all instances. The same hypothesis can be rejected in the case of IGD. In case of the comparison with the off-line modified versions, a post-hoc analysis is performed to evaluate which algorithms present statistically significant difference.

Table 3 shows the statistical analysis of pairwise comparisons between HMOBEDA and HMOBEDA $_{\text {hype }}$ for each instance with respect to $\mathrm{HV}^{-}$and IGD values. In Table 4 the numbers in parentheses show the results of pairwise comparisons between HMOBEDA and off-line algorithms using Dunn-Sidak's post-hoc test with a significance level of $\alpha=0.05$. For both tables, the first number shows how many algorithms are better than the algorithm listed in the corresponding line, and the second number shows how many algorithms are worse. The entry related to the algorithm with the lowest (best) average metric is emphasized (bold).

HMOBEDA presents statistically significant differences in comparison with $\mathrm{HMOBEDA}_{\text {hype }}$ for $2-250,5-100,8-100$ and $8-250$, and regarding only IGD metric, for $2-100,3-100,3-250,4-100,4-250$ and $5-250$ instances.

There is no statistically significant differences between HMOBEDA and $\mathrm{HMOBEDA}_{\text {hype }}$ for instances $2-100,3-100,3-250,4-100$ and $4-250$ for $\left(\mathrm{HV}^{-}\right)$ metric. Regarding IGD metric, HMOBEDA's results present statistically significant differences for almost all instances, except in 5-250, where $\mathrm{HMOBEDA}_{\text {hype }}$ presents the lowest metric value.

We can now analyze the influence of including LS-parameters in the PGM structure. HMOBEDA shows statistically significant differences in comparison with its off-line modified versions for almost all instances, particularly those with high number of objectives and variables ( $5-100,4-250,8-100$ and $8-250$ ), where HMOBEDA is better than the other three algorithms. There is no statistically significant differences between HMOBEDA and $\mathrm{HMOBEDA}_{\text {trace }}$ for instance $4-100$ for both $\mathrm{HV}^{-}$and IGD values. For all instances with 4,5 and 8 objectives, HMOBEDA is better than $\mathrm{HMOBEDA}_{f-i n s t}$ and $\mathrm{HMOBEDA}_{f}$.

These results justify, in our opinion, the relevance of adding LS parameters into the probability model, and we assume that HMOBEDA is better or at least equal to its modified versions with LS off-line configuration. We also conclude that despite using

Table 4 Results for pairwise comparisons among HMOBEDA versions using Kruskal-Wallis and DunnSidak's post-hoc tests with $\alpha=0.05$ for each problem instance

Table 5 Results for pairwise comparisons among HMOBEDA and advanced evolutionary methods using Kruskal-Wallis and Dunn-Sidak's post-hoc tests with $\alpha=0.05$ for each problem instance

less computational resources, HMOBEDA is competitive with HMOBEDA $_{\text {hype }}$. So, we define HMOBEDA as our standard version and it will be compared with other traditional approaches.

Table 5 shows the statistical analysis of the results considering the other approaches. The same methodology adopted in the comparison HMOBEDA versus its off-line modified versions is considered here.

The analysis of Table 5 reveals that the proposed approach shows statistically significant differences with almost all other algorithms (except for instances with 2 objectives with respect to the IGD metric, where there is no statistically significant differences

Table 6 Average run time (min) for each algorithm and instance

between all the algorithms). It also shows that both $\mathrm{HV}^{-}$and IGD present consistent results.

For instances 3-100 in both HV ${ }^{-}$and IGD metrics, the performances of MBN-EDA, NSGA-II, S-MOGLS and MOEA/D do not present statistically significant differences and all of them are worse than HMOBEDA (which has similar performance to NSGAIII), indicating that HMOBEDA is better than four other approaches- (0, 4). Also, for instances $4-100$, there is no statistically significant differences between the $\mathrm{HV}^{-}$ performance of HMOBEDA and NSGA-III (both are better than other four algorithms$(\mathbf{0 , 4}))$. Considering the IGD performance, HMOBEDA, NSGA-III and MOEA/D are better than MBN-EDA, NSGA-II and S-MOGLS. MOEA/D is better than two (MNBEDA and NSGA-II) and worse than one (NSGA-III)- (1, 2).

Another example can be seen for instances 3-250, both HV ${ }^{-}$and IGD performances do not present statistically significant differences between HMOBEDA, NSGA-III and MOEA/D. Regarding IGD, MOEA/D are not better nor worse than any other approach- $(\mathbf{0 , 0})$. For the remaining instances we can conclude that, based on $\mathrm{HV}^{-}$ and IGD, HMOBEDA has the best performance among the compared approaches.

Therefore, we can affirm that HMOBEDA is a competitive approach for the instances considered in this work. We have observed that it is better than the compared approaches, except for instances of small size where there is no statistically significant difference between HMOBEDA, NSGA-III and MOEA/D. Also, HMOBEDA is better than its off-line modified versions, which evidences that the flexibility imposed by modeling LS parameters as nodes of the PGM model results in benefits to the hybrid model encompassing variables and objectives. Finally, results show that the use of hypervolume instead of crowding distance is not beneficial, as it does not improve the performance and still increases the computational cost of the approach.

The average run time for each algorithm is presented in Table 6.
We can observe in Table 6 that the computational efforts for each algorithm are in the same time scale, keeping the runtime at practical levels. However, increasing the number of objectives and variables severely impacts the average computational time of all approaches. We also include statistical tests in order to compare the run time for

Table 7 Results for pairwise run time comparisons among HMOBEDA and all other algorithms using Kruskal-Wallis and Dunn-Sidak's post-hoc tests with $\alpha=0.05$ for each problem instance
all instances considering the total number of executions. Table 7 shows the results for pairwise comparisons among HMOBEDA and all other algorithms. The entry with the lowest average run time is emphasized in bold.

We can observe that HMOBEDA and off-line variations, NSGA-III and MOEA/D do not present statistically significant differences between its execution times for almost all instances. HMOBEDA $_{\text {hype }}$ has the highest computational time for all instances due to the intensive calculations necessary to compute hypervolumes. Note that we are mainly interested in the quality of the solution. Thus, the run time is given only for guidance.

# 4.5 PGM structure analysis 

In order to discuss the learned PGM structures we provide an interpretation of the probabilistic model resulted at the end of evolution for $2-100$ and $8-100$ instances. These instances correspond to examples of easy bi-objective and difficult many objective optimization instances, respectively.

Figure 3 shows the interactions (blue circles) between each decision variable $X_{q}$, $q \in\{1, \ldots, 100\}$, and the objectives $Z_{1}$ and $Z_{2}$, learned by the BN for the $2-100$ instance. Each circle has coordinates indicating the number of times an arc $\left(Z_{1}, X_{q}\right)$ has been captured along the evolutionary process for all executions versus a similar measure for $\operatorname{arc}\left(Z_{2}, X_{q}\right)$. Note that the interaction is quite similar for the two objectives, since most of points are located nearby the +1 slope line. In other words, based on Fig. 3, we can conclude that variables (specially if the number of interactions for a given variable is either very low or very high) are equally affected by both objectives.

Figure 4 focuses on the analysis of BN structure concerning the relations between objectives and LS parameters for the $8-100$ instance. The relations between each objective and the three LS parameters considered in this paper are illustrated by star

![img-2.jpeg](img-2.jpeg)

Fig. 3 For 2-100 instance, number of times $\operatorname{arc}\left(Z_{1}, X_{q}\right)$ has been captured in the BN versus a similar measure for $\operatorname{arc}\left(Z_{2}, X_{q}\right)$. Each circle corresponds to one decision variable $X_{q}, q \in\{1, \ldots, 100\}$

Fig. 4 Glyph representation of the three LS parameters (spokes) for each objective $Z_{1}$ to $Z_{8}$ of $8-100$ instance
![img-3.jpeg](img-3.jpeg)
glyphs. In such representation, each spoke represents one parameter $P_{l}$ and it is proportional to the number of times the $\operatorname{arc}\left(Z_{r}, P_{l}\right), l \in\{1,2,3\}, r \in\{1, \ldots, 8\}$, has been captured along the evolutionary process for all executions. The glyphs allow us to visualize which is the relative strength of the relations. For example, it can be seen in Fig. 4 that objectives $Z_{1}$ and $Z_{6}$ have small influence on the way the parameters are instantiated. On the other hand, $Z_{3}$ and $Z_{7}$ have great influence, although $Z_{3}$ is better balanced among the parameters than $Z_{7}$.

In this section we have aimed to illustrate one of the main advantages of using EDAs: the possibility of scrutinizing its probabilistic model which usually encompasses useful information about the relationship among variables. We have shown with two examples that HMOBEDA model allows a step forward. First, it is possible to estimate the relevance that the variables have on the objectives, from the analysis of how frequent objective-variable interactions are. Second, it is possible to determine how sensitive are the different objectives to the setting of the distinct local search parameters from the analysis of the frequency of the objective-parameters interactions. Notice that while,

for sampling purposes, objectives are set as parents of variables and of local search parameters, the quality of the solutions, i.e., the objective values are the ones sensitive to the variables and parameters assignments.

# 5 Conclusions and future work 

In this paper we have analyzed a new MOEDA based on Bayesian Network in the context of multi and many objective optimization. The approach named HMOBEDA has a hill climbing procedure embedded in the probabilistic model as a local optimizer. We have thus incorporated a local search (LS) procedure to exploit the search space and a joint probabilistic model of objectives, variables and LS parameters to generate new individuals through the sample process. The Bayesian network is learned using the K2 method and since the LS parameters are part of the network, they are adapted as the algorithm evolves.

The main issue investigated in this paper concerns whether the auto-adaptation of LS parameters improves the search by allowing the Bayesian network to represent and set these parameters. We have thus modified the original HMOBEDA to build three other off-line versions with no LS parameter encoded as a node in the probabilistic model. The first version $\left(\mathrm{HMOBEDA}_{f}\right)$ is based on the best LS parameters found by HMOBEDA. The second version $\left(\mathrm{HMOBEDA}_{f-\text { ins }}\right)$ is specialized for each instance by setting the LS parameters to the best ones found by HMOBEDA for that instance. The third version $\left(\mathrm{HMOBEDA}_{\text {trace }}\right)$ defines the LS parameters through the irace package. We have also implemented an online configuration of HMOBEDA based on the hypervolume indicator (HMOBEDA $_{\text {hype }}$ ) as part of the selection procedure. We have analyzed the performance of the proposed approaches for ten instances of the multiobjective knapsack problem, considering two traditional metrics: Hypervolume ( $\mathrm{HV}^{-}$) and Inverted Generational Distance (IGD).

Based on the experiments with the MOKP instances addressed in this work, we can conclude that the inclusion of online configuration of the LS parameters is beneficial for HMOBEDA. In other words, the online parameter setting based on the PGM is more effective than fixing good parameters along optimization. We have shown that the better performance of the proposed approach is more related with the probabilistic model than with LS: as modified versions of HMOBEDA using different tuned LS parameters did not provide the same trade-off. Another conclusion is that using hypervolume instead of crowding distance as a tie-breaker neither improves the solution found nor presents good computational cost.

We have also concluded that the proposed hybrid EDA is competitive when compared with the other evolutionary algorithms investigated. One possible explanation points to the fact that since the LS parameters are in the same probabilistic model, HMOBEDA provides an automatic and informed decision at the time of setting these parameters. Thus a variety of non-dominated solutions can be found during different stages of the evolutionary process. This finding is relevant for the development of other adaptive hybrid MOEAs. Probabilistic modeling arises as a sensible and feasible way not only to learn and explore dependencies between variables and objectives but also to automatically control the application of local search operators.

An analysis of the resulting BN structures has also been carried to evaluate how the interactions among variables, objectives and local search parameters are captured by the BNs. As a way to illustrate the types of information that can be extracted from the models, we have shown how the frequency of arcs in the BNs indicate that the variables of the $2-100$ instance have a similar influence on both objectives. For 8-100 instance, a similar analysis shows that LS parameters are more related to objectives $Z_{3}$ and $Z_{7}$ than to the others. This illustrative analysis can be further extended.

In the future, MOEA techniques other than Pareto-based approaches should be examined, such as scalarizing functions, for example. These new approaches should be investigated with more than eight objectives. Beyond that, we intend to relax some of the current restrictions of our model to represent reacher types of interactions (e.g., dependencies between variables). Consequently, other classes of methods to learn the BN structures, such as constraint based (Aliferis et al. 2010; Tsamardinos et al. 2003) and hybrid (Tsamardinos et al. 2006) methods could be investigated.

Finally, we intend to compare HMOBEDA with a larger set of traditional approaches, including a baseline method commonly used in hyperheuristics contexts which randomly generates LS parameters.

Acknowledgements M. Delgado acknowledges CNPq Grant 309197/2014-7. M. Martins acknowledges CAPES/Brazil. R. Santana acknowledges support by: IT-609-13 Program (Basque Government), TIN201341272P (Spanish Ministry of Science and Innovation) and CNPq Program Science Without Borders No. 400125/2014-5 (Brazil Government).
