# Feature Subset Selection by Bayesian network-based optimization 

I. Inza *, P. Larrañaga, R. Etxeberria, B. Sierra<br>Department of Computer Science and Artificial Intelligence, University of the Basque Country, P.O. Box 649, E-20080 Donostia - San Sebastián, Basque Country, Spain

Received 12 December 1999


#### Abstract

A new method for Feature Subset Selection in machine learning, FSS-EBNA (Feature Subset Selection by Estimation of Bayesian Network Algorithm), is presented. FSS-EBNA is an evolutionary, population-based, randomized search algorithm, and it can be executed when domain knowledge is not available. A wrapper approach, over Naive-Bayes and ID3 learning algorithms, is used to evaluate the goodness of each visited solution. FSS-EBNA, based on the EDA (Estimation of Distribution Algorithm) paradigm, avoids the use of crossover and mutation operators to evolve the populations, in contrast to Genetic Algorithms. In absence of these operators, the evolution is guaranteed by the factorization of the probability distribution of the best solutions found in a generation of the search. This factorization is carried out by means of Bayesian networks. Promising results are achieved in a variety of tasks where domain knowledge is not available. The paper explains the main ideas of Feature Subset Selection, Estimation of Distribution Algorithm and Bayesian networks, presenting related work about each concept. A study about the 'overfitting' problem in the Feature Subset Selection process is carried out, obtaining a basis to define the stopping criteria of the new algorithm. (c) 2000 Elsevier Science B.V. All rights reserved.


Keywords: Machine learning; Supervised learning; Feature Subset Selection; Wrapper; Predictive accuracy; Estimation of Distribution Algorithm; Estimation of Bayesian Network Algorithm; Bayesian network; Overfitting

## 1. Introduction

In supervised machine learning, the goal of a supervised learning algorithm is to induce a classifier that allows us to classify new examples $E *=\left\{e_{n+1}, \ldots, e_{n+m}\right\}$ that are only

[^0]
[^0]:    * Corresponding author.

    E-mail address: ccbincai@si.ehu.es (I. Inza).

characterized by their $d$ descriptive features. To generate this classifier we have a set of $n$ samples $E=\left\{e_{1}, \ldots, e_{n}\right\}$, characterized by $d$ descriptive features $X=\left\{X_{1}, \ldots, X_{d}\right\}$ and the class label $C=\left\{w_{1}, \ldots, w_{n}\right\}$ to which they belong. Machine learning can be seen as a 'data-driven' process where, putting less emphasis on prior hypotheses than is the case with classical statistics, a 'general rule' is induced for classifying new examples using a learning algorithm. Many representations with different biases have been used to develop this 'classification rule'. Here, the machine learning community has formulated the following question: "Are all of these d descriptive features useful for learning the 'classification rule'?" Trying to respond to this question the Feature Subset Selection (FSS) approach appears, which can be reformulated as follows: given a set of candidate features, select the best subset under some learning algorithm.

This dimensionality reduction made by an FSS process can carry out several advantages for a classification system in a specific task:

- a reduction in the cost of acquisition of the data,
- improvement of the comprensibility of the final classification model,
- a faster induction of the final classification model,
- an improvement in classification accuracy.

The attainment of higher classification accuracies is the usual objective of machine learning processes. It has been long proved that the classification accuracy of machine learning algorithms is not monotonic with respect to the addition of features. Irrelevant or redundant features, depending on the specific characteristics of the learning algorithm, may degrade the predictive accuracy of the classification model. In our work, the FSS objective will be the maximization of the performance of the classification algorithm. In addition, with the reduction in the number of features, it is more likely that the final classifier is less complex and more understandable by humans.

Once the objective is fixed, FSS can be viewed as a search problem, with each state in the search space specifying a subset of the possible features of the task. Exhaustive evaluation of possible feature subsets is usually unfeasible in practice because of the large amount of computational effort required. Many search techniques have been proposed to solve the FSS problem when there is no knowledge about the nature of the task, carrying out an intelligent search in the space of possible solutions. As randomized, evolutionary and population-based search algorithm, Genetic Algorithms (GAs) have long been used as the search engine in the FSS process. GAs need crossover and mutation operators to make the evolution possible. However, the optimal selection of crossover and mutation rates is an open problem in the field of GAs [33] and they are normally fixed by means of experimentation.

In this work, a new search engine, Estimation of Bayesian Network Algorithm (EBNA) [29], inspired in the Estimation of Distribution Algorithm paradigm (EDA), will be used for FSS, resulting in the new FSS-EBNA algorithm. FSS-EBNA shares the basic characteristics with GAs, with the attractive property of avoiding crossover and mutation operators. In the new FSS algorithm the evolution is based on the probabilistic modeling by Bayesian networks of promising solutions of each generation to guide further exploration of the space of features.

The work is organized as follows: the next section introduces the FSS concept and its components. Section 3 introduces the EDA paradigm, Bayesian networks and the EBNA

search algorithm. Section 4 presents the details of the new algorithm for Feature Subset Selection, FSS-EBNA. Section 5 presents the datafiles and learning algorithms used to test the new approach and the corresponding results appear in the sixth section. We conclude with a summary and future work.

# 2. Feature Subset Selection as a search problem 

Even if our work is located in machine learning, the FSS literature includes plenty of works in other fields such as pattern recognition (Jain and Chandrasekaran [39], Stearns [83], Kittler [43], Ferri et al. [31]), statistics (Narendra and Fukunaga [69], Boyce et al. [13], Miller [62]), data mining (Chen et al. [20], Provost and Kolluri [75]) or text learning (Mladenić [63], Yang and Pedersen [89]). In this way, different communities have exchanged and shared ideas among them to deal with the FSS problem.

As reported by Aha and Bankert [2], the objective of Feature Subset Selection in machine learning is to reduce the number of features used to characterize a dataset so as to improve a learning algorithm's performance on a given task. Our objective will be the maximization of the classification accuracy in a specific task for a certain learning algorithm; as a co-lateral effect we will have the reduction in the number of features to induce the final classification model. The feature selection task can be exposed as a search problem, each state in the search space identifying a subset of possible features. A partial ordering on this space, with each child having exactly one more feature than its parents, can be stated.

Fig. 1 expresses the search algorithm nature of the FSS process. Blum and Langley [10] argue that the structure of this space suggest that any feature selection method must take a stance on the next four basic issues that determine the nature of the search process: a starting point in the search space, an organization of the search, an evaluation strategy of the feature subsets and a criterion for halting the search.
![img-0.jpeg](img-0.jpeg)

Fig. 1. In this 3-feature (F1, F2, F3) problem, each individual in the space is related with a feature subset, possible solution for the FSS problem. In each individual, when a feature's rectangle is filled, it indicates that it is included in the feature subset.

# 2.1. Starting point in the space 

The starting point in the space determines the direction of the search. One might start with no features and successively add them, or one might start with all the features and successively remove them. One might also select an initial state somewhere in the middle of the search space.

### 2.2. Organization of the search

The organization of the search determines the strategy of the search in a space of size $2^{d}$, where $d$ is the number of features in the problem. Roughly speaking, the search strategies can be optimal or heuristic. Two classic optimal search algorithms which exhaustively evaluate all possible subsets are depth-first and breadth-first (Liu and Motoda [58]). Otherwise, Branch \& Bound search (Narendra and Fukunaga [69]) guarantees the detection of the optimal subset for monotonic evaluation functions without the systematic examination of all subsets.

When monotonicity cannot be satisfied, in a search space with a $2^{d}$ cardinality, depending in the evaluation function used, an exhaustive search can be impractical. Can we make some smart choices based on the information available about the search space, but without looking it on the whole? Here appears the heuristic search concept. They find near optimal solution, if not optimal. Among heuristic algorithms, there are deterministic heuristic and non-deterministic heuristic algorithms. Classic deterministic heuristic FSS algorithms are sequential forward and backward selections (SFS and SBS, Kittler [43]), floating selection methods (SFFS and SFBS, Pudil et al. [76]) or best-first search (Kohavi and John [47]). They are deterministic in the sense that all the runs always obtain the same solution. Vafaie and De Jong [86] results suggest that classic greedy hill-climbing approaches, tend to get trapped on local peaks caused by interdependencies among features. In this sense the work of Pudil et al. [76] is an interesting idea in an attempt to avoid this phenomenon. Non-deterministic heuristic search appears in a motivation to avoid getting stuck in local maximum. Randomness is used to escape from local maximum and this implies that one should not expect the same solution from different runs. Up until now, the next non-deterministic search engines have been used in FSS: Genetic Algorithms [30,51,81,86,88], Simulated Annealing [27], Las Vegas Algorithm [57,82] (see Liu and Motoda [58] or Jain and Zongker [40] for other kinds of classifications of FSS search algorithms).

### 2.3. Evaluation function

The evaluation function measures the effectiveness of a particular subset of features after the search algorithm has chosen it for examination. Being the objective of the search its maximization, the search algorithm utilizes the value returned by the evaluation function to help guide the search. Many measures carry out this objective regarding only the characteristics of the data, capturing the relevance of each feature or set of features to define the target concept. As reported by John et al. [41], when the goal of FSS is the maximization of the accuracy, the features selected should depend not only on

the features and the target concept to be learned, but also on the learning algorithm. Kohavi and John [47] report domains in which a feature, although being in the target concept to be learned, does not appear in the optimal feature subset that maximizes the predictive accuracy for the specific learning algorithm used. This occurs due to the intrinsic characteristics and limitations of the classifier used: feature relevance and accuracy optimality are not always coupled in FSS. The idea of using the error reported by a classifier as the feature subset evaluation criterion appears in many previous works done, for example, by Stearns [83] in 1976 or Siedelecky and Skalansky [81] in 1988. Doak [27] in 1992 used the classification error rate to guide non-large searches. In John et al.'s [41] the wrapper concept definitively appears. This implies that the FSS algorithm conducts a search for a good subset of features using the induction algorithm itself as a part of the evaluation function, the same algorithm that will be used to induce the final classification model. Once the classification algorithm is fixed, the idea is to train it with the feature subset encountered by the search algorithm, estimating the error percentage, and assigning it as the value of the evaluation function of the feature subset. In this way, representational biases of the induction algorithm used to construct the final classifier are included in the FSS process. Wrapper strategy needs a high computational cost, but technical computer advances in the last decade have made the use of this wrapper approach possible, calculating an amount of accuracy estimations (training and testing on significant amount of data) not envisioned in the 1980s.

Before applying the wrapper approach, an enumeration of the available computer resources is critical. Two different factors become an FSS problem 'large' (Liu and Setiono [59]): the number of features and the number of instances. One must bear in mind the time needed for the learning algorithm used in the wrapper scheme as a training phase is required for every possible solution visited by the FSS search engine. Many approaches have been proposed in literature to alleviate the loading of the training phase, such as Caruana and Freitag [17] (avoiding the evaluation of many subsets taking advantage of the intrinsic properties of the used learning algorithm) or Moore and Lee [64] (reducing the burden of the cross-validation technique for model selection).

When the learning algorithm is not used in the evaluation function, the goodness of a feature subset can be assessed regarding only the intrinsic properties of the data. The learning algorithm only appears in the final part of the FSS process to construct the final classifier using the set of selected features. The statistics literature proposes many measures for evaluating the goodness of a candidate feature subset (see Ben-Bassat [9] for a review of these classic measures). These statistical measures try to detect the feature subsets with higher discriminatory information with respect to the class (Kittler [43]) regarding the probability distribution of data. These measures are usually monotonic and increase with the addition of features that afterwards can hurt the accuracy classification of the final classifier. In pattern recognition FSS works, in order to recognize the forms of the task, it is so common to fix a positive integer number $d$ and select the best feature subset of $d$ cardinality found during the search. When this $d$ parameter is not fixed a examination of the slope of the curve-value of the proposed statistical measure versus cardinality of the selected feature subset-of the best feature subsets is required to select the cardinality of the final feature subset. In text-learning, its predictive accuracy will be assessed running the classifier only with the selected features (Doak [27]). This type of FSS

![img-1.jpeg](img-1.jpeg)

Fig. 2. Summarization of the whole FSS process for filter and wrapper approaches.
approach, which ignores the induction algorithm to assess the merits of a feature subset, is known as filter approach. Mainly inspired on these statistical measures, in the 1990s, more complex filter measures which do not use the final induction algorithm in the evaluation function generate new FSS algorithms, such as FOCUS (Almuallin and Dietterich [4]), RELIEF (Kira and Rendell [42]), Cardie's algorithm [16], Koller and Sahami's work with probabilistic concepts [50] or the named 'Incremental Feature Selection' (Liu and Setiono [59]). Nowadays, the filter approach is receiving considerable attention from the 'data mining' community to deal with huge databases when the wrapper approach is unfeasible (Liu and Motoda [58]). Fig. 2 locates the role of filter and wrapper approaches within the overall FSS process.

When the size of the problem allows the application of the wrapper approach, works in the 1990s have noted its superiority, in terms of predictive accuracy over the filter approach. Doak [27] in the early 1990s, also empirically showed this superiority of the wrapper model, but due to computational availability limitations, he could only apply Sequential Feature Selection with the wrapper model, discarding the use of computationally more expensive global search engines (Best-First, Genetic Algorithms, etc.) in his comparative work between FSS algorithms.

Blum and Langley [10] also present another type of FSS, known as embedded. This concept covers the feature selection process made by the induction algorithm itself. For

example, both partitioning and separate-and-conquer methods implicitly select features for inclusion in a branch or rule in preference to other features that appear less relevant, and in the final model some of the initial features might not appear. On the other hand, some induction algorithms (i.e., Naive-Bayes [19] or IB1 [1]) include all the presented features in the model when no FSS is executed. This FSS approach is done within the learning algorithm preferring some features instead of others and possibly not including all the available features in the final classification model induced by the learning algorithm. However, filter and wrapper approaches are located one abstraction level above the embedded approach, performing a feature selection process for the final classifier apart from the embedded selection done by the learning algorithm itself.

# 2.4. Criterion for halting the search 

An intuitive approach for stopping the search will be the non-improvement of the evaluation function value of alternative subsets. Another classic criterion will be to fix an amount of possible solutions to be visited along the search.

## 3. EDA paradigm, Bayesian networks and EBNA approach

In this section, EDA paradigm and Bayesian networks will be explained. Bearing in mind these two concepts, EBNA, the search engine used in our FSS algorithm will be presented. EDA paradigm is the general formula of the EBNA algorithm and Bayesian networks can be seen as the most important basis of EBNA.

### 3.1. EDA paradigm

Genetic Algorithms (GAs, see Holland [37]) are one of the best known techniques for solving optimization problems. Their use has reported promising results in many areas but there are still some problems where GAs fail. These problems, known as deceptive problems, have attracted the attention of many researchers and as a consequence there has been growing interest in adapting the GAs in order to overcome their weaknesses.

The GA is a population-based search method. First, a set of individuals (or candidate solutions to our optimization problem) is generated (a population), then promising individuals are selected, and finally new individuals which will form the new population are generated using crossover and mutation operators.

An interesting adaptation of this is the Estimation of Distribution Algorithm (EDA) [65] (see Fig. 3). In EDA, there are neither crossover nor mutation operators, the new population is sampled from a probability distribution which is estimated from the selected individuals.

In this way, a randomized, evolutionary, population-based search can be performed using probabilistic information to guide the search. It is shown that although EDA approach process solutions in a different way to GAs, it has been empirically proven that the results of both approaches can be very similar (Pelikan et al. [74]). In this way, both approaches do the same except that EDA replaces genetic crossover and mutation operators by means of the following two steps:

EDA
$D_{0} \leftarrow$ Generate $N$ individuals (the initial population) randomly.
Repeat for $l=1,2, \ldots$ until a stop criterion is met.
$D_{l-1}^{s} \leftarrow$ Select $S \leqslant N$ individuals from $D_{l-1}$ according to a selection method.
$p_{l}(\boldsymbol{x})=p\left(\boldsymbol{x} \mid D_{l-1}^{s}\right) \leftarrow$ Estimate the joint probability distribution of an individual being among the selected individuals.
$D_{l} \leftarrow$ Sample $N$ individuals (the new population) from $p_{l}(\boldsymbol{x})$.
Fig. 3. Main scheme of the EDA approach.
(1) a probabilistic model of selected promising solutions is induced,
(2) new solutions are generated according to the induced model.

The main problem of EDA resides on how the probability distribution $p_{l}(\boldsymbol{x})$ is estimated. Obviously, the computation of $2^{n}$ probabilities (for a domain with $n$ binary variables) is impractical. This has led to several approximations where the probability distribution is assumed to factorize according to a probability model (see Larrañaga et al. [55] or Pelikan et al. [74] for a review).

The simplest way to estimate the distribution of good solutions assumes the independence between the features ${ }^{1}$ of the domain. New candidate solutions are sampled by only regarding the proportions of the values ${ }^{2}$ of all features independently to the remaining solutions. Population-Based Incremental Learning (PBIL, Baluja [7]), Compact Genetic Algorithm (cGA, Harik et al. [34]), Univariate Marginal Distribution Algorithm (UMDA, Mühlenbein [66]) and Bit-Based Simulated Crossover (BSC, Syswerda [84]) are four algorithms of this type. They have worked well under artificial tasks with no significant interactions among features and so, the need for covering higher order interactions among the variables is seen for more complex or real tasks.

Efforts covering pairwise interactions among the features of the problem have generated algorithms such as population-based MIMIC algorithm using simple chain distributions (De Bonet et al. [25]), the so-called dependency trees (Baluja and Davies [8]) and Bivariate Marginal Distribution Algorithm (BMDA, Pelikan and Mühlenbein [72]). Pelikan and Mühlenbein [72] have demonstrated that only covering pairwise dependencies is not enough with problems which have higher order interactions.

In this way, the Factorized Distribution Algorithm (FDA, Mühlenbein et al. [67]) covers higher order interactions. This is done using a previously fixed factorization of the joint probability distribution. However, FDA needs prior information about the decomposition and factorization of the problem which is often not available.

Without the need of this extra information about the decomposition and factorization of the problem, Bayesian networks are graphical representations which cover higher order interactions. EBNA (Etxeberria and Larrañaga [29]) and BOA (Pelikan et al. [73]) are algorithms which use Bayesian networks for estimating the joint distribution of promising solutions. In this way multivariate interactions among problem variables can be covered.

[^0]
[^0]:    ${ }^{1}$ In the Evolutionary Computation community, the term 'variable' is normally used instead of 'feature'. We use both terms indistinctly.
    ${ }^{2}$ In the FSS problem there are two values for each candidate solution: ' 0 ' denoting the absence of the feature and ' 1 ' denoting its presence.

Based on the EBNA work of Etxeberria and Larrañaga [29], we propose the use of Bayesian networks as the models for representing the probability distribution of a set of candidate solutions in our FSS problem, using the application of automatic learning methods to induce the right distribution model in each generation in an efficient way.

# 3.2. Bayesian networks 

### 3.2.1. Definition

A Bayesian network (Castillo [18], Lauritzen [56], Pearl [71]) encodes the relationships contained in the modelled data. It can be used to describe the data as well as to generate new instances of the variables with similar properties as those of given data. A Bayesian network encodes the probability distribution $p(\boldsymbol{x})$, where $\boldsymbol{x}=\left(X_{1}, \ldots, X_{d}\right)$ is a vector of variables, and it can be seen as a pair $(M, \theta) . M$ is a directed acyclic graph (DAG) where the nodes correspond to the variables and the arcs represent the conditional (in)dependencies among the variables. By $X_{i}$, both the variable and the node corresponding to this variable is denoted. $M$ will give the factorization of $p(\boldsymbol{x})$ :

$$
p(\boldsymbol{x})=\prod_{i=1}^{d} p\left(x_{i} \mid \pi_{i}\right)
$$

where $\Pi_{i}$ is the set of parent variables (nodes) that $X_{i}$ has in $M$ and $\pi_{i}$ its possible instantiations. The number of states of $\Pi_{i}$ will be denoted as $\left|\Pi_{i}\right|=q_{i}$ and the number of different values of $X_{i}$ as $\left|X_{i}\right|=r_{i} . \theta=\left\{\theta_{i j k}\right\}$ are the required conditional probability values to completely define the joint probability distribution of $X . \theta_{i j k}$ will represent the probability of $X_{i}$ being in its $k$ th state while $\Pi_{i}$ is in its $j$ th instantiation. This factorization of the joint distribution can be used to generate new instances using the conditional probabilities in a modelled dataset.

Informally, an arc between two nodes relates the two nodes so that the value of the variable corresponding to the ending node of the arc depends on the value of the variable corresponding to the starting node. Every probability distribution can be defined by a Bayesian network. As a result, Bayesian networks are widely used in problems where uncertainty is handled using probabilities.

Two following sections relate the learning process of Bayesian networks from data and the generation of new instances from the Bayesian networks.

### 3.2.2. Learning Bayesian networks from data

The key step of any EDA is the estimation of the probability distribution $p\left(\boldsymbol{x} \mid D_{i-1}^{s}\right)$. Depending on how it is estimated, the results of the algorithm will vary. In this section, we will show how this can be done automatically using Bayesian networks. Selected individuals will be treated as data cases which form a data set $D_{i-1}^{s}$. Our goal will be to set a method which, in each generation, obtains $p\left(\boldsymbol{x} \mid D_{i-1}^{s}\right)$ as fast as possible in a multiple connected form.

Let $D$ be a data set of $S$ selected cases and $p(\boldsymbol{x} \mid D)$ the probability distribution we want to find. If we represent as $\mathcal{M}$ the possible DAGs, then from probability theory we obtain:

$$
p(\boldsymbol{x} \mid D)=\sum_{M \in \mathcal{M}} p(\boldsymbol{x} \mid M, D) p(M \mid D)
$$

This equation is known as Bayesian model averaging (Madigan et al. [60]). As it requires the summing of all possible structures, its use is unfeasible and usually two approximations are used instead of the afore mentioned approach.

The first is known as selective model averaging, where only a reduced number of promising structures is taken into account. In this case, denoting the set of this promising structures by $\mathcal{M}^{\mathcal{S}}$, we have:

$$
p(\boldsymbol{x} \mid D) \approx \sum_{M \in \mathcal{M}^{\mathcal{S}}} p(\boldsymbol{x} \mid M, D) p(M \mid D)
$$

where

$$
\sum_{M \in \mathcal{M}^{\mathcal{S}}} p(M \mid D) \approx 1
$$

The second approximation is known as model selection where $p(\boldsymbol{x} \mid D)$ is approximated in the following manner:

$$
p(\boldsymbol{x} \mid D) \approx p(\boldsymbol{x} \mid \tilde{M}, D)
$$

where

$$
\tilde{M}=\arg \max _{M \in \mathcal{M}^{\mathcal{S}}} p(M \mid D)
$$

This means that only the structure with the maximum posterior likelihood is used, knowing that for large enough $D$, we have $p(\tilde{M} \mid D) \approx 1$.

Obviously, better results must be obtained using model averaging, but due to its easier application and lower cost model selection, it is preferred most of the times. In our case, we will also use the second approximation, remembering that the estimation of $p(\boldsymbol{x} \mid D)$ must be done quickly. In Heckerman et al. [35] it is shown that under some assumptions, for any structure $M$ :

$$
p(\boldsymbol{x} \mid M, D)=\prod_{i=1}^{d} E\left[\theta_{i j k} \mid M, D\right]
$$

where $E\left[\theta_{i j k} \mid M, D\right]$ is the expected probability of the variable $X_{i}$ being in its $k$ th state when its parent nodes in $M, \Pi_{i}$, are in their $j$ th configuration.

Furthermore, in Cooper and Herskovits [23] it is shown that:

$$
E\left[\theta_{i j k} \mid M, D\right]=\frac{N_{i j k}+1}{N_{i j}+r_{i}}
$$

$N_{i j k}$ is the number of times that $X_{i}$ is in its $k$ th state and $\Pi_{i}$ in its $j$ th configuration in $D$. $N_{i j}=\sum_{k} N_{i j k}$.

Combining (1), (2) and (3), we obtain:

$$
p(\boldsymbol{x} \mid D) \approx p(\boldsymbol{x} \mid \tilde{M}, D)=\prod_{i=1}^{d} \frac{N_{i j k}+1}{N_{i j}+r_{i}}=\prod_{i=1}^{d} p\left(x_{i} \mid \pi_{i}\right)
$$

which allows us to represent the probability distribution $p(\boldsymbol{x} \mid D)$ using a Bayesian network whose structure has the maximum posterior likelihood, and whose parameters can be computed directly from the data set.

But to get things working, we must be able to find $\widehat{M}$, we must be able to learn it from the data. $\widehat{M}$ is the structure with the maximum posterior likelihood. From Bayes theorem:

$$
p(M \mid D) \propto p(D \mid M) p(M)
$$

$p(M)$ is the prior probability of the structures. In our case, we know nothing about these structures, so we will set in a uniform way. Thus,

$$
p(M \mid D) \propto p(D \mid M)
$$

Therefore, finding the structure with the maximum posterior likelihood becomes equivalent to finding the structure which maximizes the probability of the data. Under some assumptions, it has been proved that $p(D \mid M)$ can be calculated in closed form (Cooper and Herskovits [23], Heckerman et al. [35]); however, in our case we will use the BIC approximation (Schwarz [80]) because being asymptotically equivalent, it has the appealing property of selecting simple structures (Bouckaert [12]), which reduces the computation cost:

$$
\log p(D \mid M) \approx B I C(M, D)=\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k} \log \frac{N_{i j k}}{N_{i j}}-\frac{\log N}{2} \sum_{i}\left(r_{i}-1\right) q_{i}
$$

where $N_{i j k}$ and $N_{i j}$ and $q_{i}$ are defined as before.
Unfortunately, finding $\widehat{M}$ requires searching through all possible structures, which has been proven to be NP-hard (Chickering et al. [21]). Although promising results have been obtained using global search techniques (Larrañaga et al. [53,54], Etxeberria et al. [28], Chickering et al. [22], Wong et al. [87]) their computation cost makes them unfeasible for our problem. We need to find $\widehat{M}$ as fast as possible, so a simple algorithm which returns a good structure, even if it is not optimal, will be preferred.

In our implementation, Algorithm B (Buntine [14]) is used for learning Bayesian networks from data. Algorithm B is a greedy search heuristic. The algorithm starts with an arc-less structure and at each step, it adds the arc with the maximum increase in the BIC approximation (or whatever measure is used). The algorithm stops when adding an arc does not increase the utilized measure.

# 3.2.3. Sampling from Bayesian networks 

Once we have represented the desired probability distribution using a Bayesian network, new individuals must be generated using the joint probability distribution encoded by the network. These individuals can be generated by sampling them directly from the Bayesian network, for instance, using the Probabilistic Logic Sampling algorithm (PLS, Henrion [36]).

PLS (see Fig. 4) takes advantage of how a Bayesian network defines a probability distribution. It generates the values for the variables following their ancestral ordering which guarantees that $\Pi_{\mu(i)}$ will be instantiated every time. This makes generating values from $p\left(X_{\mu(i)} \mid \pi_{\mu(i)}\right)$ trivial.

### 3.2.4. Estimation of Bayesian Network Algorithm: EBNA

The general procedure of EBNA appears in Fig. 5. To understand the steps of the algorithm, the following concepts must be clarified:

PLS
Find an ancestral ordering of the nodes in the Bayesian network $(\mu)$
For $i=1,2, \ldots, n$
$x_{\mu(i)} \leftarrow$ generate a value from $p\left(x_{\mu(i)} \mid \pi_{\mu(i)}\right)$
Fig. 4. Probabilistic Logic Sampling scheme.

```
EBNA
    \(B N_{0} \leftarrow\left(\widehat{M}_{0}, \theta_{0}\right)\).
    \(D_{0} \leftarrow\) Sample \(N\) individuals from \(B N_{0}\).
    For \(l=1,2, \ldots\) until a stop criterion is met
        \(D_{l-1}^{s} \leftarrow\) Select \(S\) individuals from \(D_{l-1}\).
        \(\widehat{M}_{l} \leftarrow\) Find the structure which maximizes \(\operatorname{BIC}\left(M_{l}, D_{l-1}^{s}\right)\).
        \(\theta_{l} \leftarrow\) Calculate \(\left\{\theta_{i j k}=\frac{N_{i j k}+1}{N_{i j}+r_{i}}\right\}\) using \(D_{l-1}^{s}\) as the data set.
        \(B N_{l} \leftarrow\left(\widehat{M}_{l}, \theta_{l}\right)\).
        \(D_{l} \leftarrow\) Sample \(N\) individuals from \(B N_{l}\) using PLS.
```

Fig. 5. EBNA basic scheme.
$\widehat{M}_{0}$ is the DAG with no arcs at all and $\theta_{0}=\left\{\forall i: p\left(X_{i}=x_{i}\right)=1 / r_{i}\right\}$, which means that the initial Bayesian network $B N_{0}$ assigns the same probability to all individuals. $N$ is the number of individuals in the population. $S$ is the number of individuals selected from the population. Although $S$ can be any value, we take the suggestion that appears in Etxeberria and Larrañaga [29] into consideration, being $S=N / 2$. If $S$ is close to $N$ then the populations will not evolve very much from generation to generation. On the other hand, a low $S$ value will lead to low diversity resulting in early convergence.

In the previous section we have shown how individuals are created from Bayesian networks and how Bayesian networks can estimate the probability distribution of the selected individuals but so far nothing has been said about how individuals are selected or when the algorithm is stopped.

For individual selection range based selection is proposed, i.e., selecting the best $N / 2$ individuals from the $N$ individuals of the population. However, any selection method could be used.

For stopping the algorithm different criteria can be used:

- fixing a number of generations,
- when all the individuals of the population are the same,
- when the average evaluation function value of the individuals in the population does not improve in a fixed number of generations,
- when any sampled individual from the Bayesian network does not have a better evaluation function value than the best individual of the previous generation.
A variation of the last criterion will be used, depending on the dimensionality (number of features) of the problem. This concept will be explained in the next section.

Finally, the way in which the new population is created must be pointed out. In the given procedure, all individuals from the previous population are discarded and the new population is composed of all newly created individuals. This has the problem of losing the

best individuals that have been previously generated, therefore, the following minor change has been made: instead of discarding all the individuals, we maintain the best individual of the previous generation and create $N-1$ new individuals.

An elitist approach has been used to form iterative populations. Instead of directly discarding the $N-1$ individuals from the previous generation replacing them with $N-1$ newly generated ones, the $2 N-2$ individuals are put together and the best $N-1$ taken among them. These best $N-1$ individuals will form the new population together with the best individual of the previous generation. In this way, the populations converge faster to the best individuals found; however, this also implies a risk of losing diversity within the population.

# 4. Feature Subset Selection by Estimation of Bayesian Network Algorithm: FSS-EBNA 

We will explain the proposed FSS-EBNA method, presenting its different pieces. First, the connection between the EBNA search algorithm and the FSS problem will be clarified. In the second subsection, the evaluation function of the FSS process will be explained. In a third subsection, several considerations about the final evaluation process and the stopping criterion of FSS-EBNA will be presented, coupled with a reflection on the 'overfitting' risk in FSS-EBNA.

### 4.1. FSS and EBNA connection and the search space

Once the FSS problem and EBNA algorithm are presented, we will use the search engine provided by EBNA to solve the FSS problem. FSS-EBNA, as a search algorithm, will seek in the feature subset space for the 'best' feature subset. Being an individual in the search space a possible feature subset, a common notation will be used to represent each individual: for a full $d$ feature problem, there are $d$ bits in each state, each bit indicating whether a feature is present (1) or absent (0). In each generation of the search, the induced Bayesian network will factorize the probability distribution of selected individuals. The Bayesian network will be formed by $d$ nodes, each one representing a feature of the domain. Each node has two possible values or states ( 0 : absence of the feature; 1 : presence of the feature).

Bearing the general EBNA procedure in mind, Fig. 6 summarizes the FSS-EBNA method.

FSS-EBNA is an evolutionary, population-based, randomized search algorithm, and it can be executed when domain knowledge is not available. Although GAs share these characteristics, they need crossover and mutation operators to evolve the population of solutions. Otherwise, FSS-EBNA does not need these operators and must only fix a population size $(N)$ and a size for the selection set $(S)$. We have selected the following numbers:

- as explained in the former section, $S=N / 2$ is used,
- $S$ is fixed to 1000 .

![img-2.jpeg](img-2.jpeg)

Fig. 6. FSS-EBNA method.

The election of the population size is related to the dimensionality of the domain and the used evaluation function. The justification of the population size will be explained after the presentation of the used datasets.

At this point of the explanation we would like to point out the similarities of the new algorithm with the work of Koller and Sahami [50]. They also use concepts from probabilistic reasoning to build a near optimal feature subset by a filter approach. They use concepts like conditional independence and Markov blanket, concepts which are used in the construction of Bayesian networks.

# 4.2. Characteristics of the evaluation function 

A wrapper approach will be used to calculate the evaluation function value for each individual. The value of the evaluation function of a feature subset found by the EBNA search technique, once the classification algorithm is fixed, will be calculated by an error estimation in the training data.

The accuracy estimation, seen as a random variable, has an intrinsic uncertainty [44]. Based on Kohavi's [45] work on accuracy estimation techniques, a 10-fold cross-validation multiple times, combined with a heuristic proposed by Kohavi and John [47], will be used to control the intrinsic uncertainty of the evaluation function. This heuristic works as follows:

- If the standard deviation of the accuracy estimate is above $1 \%$, another 10 -fold crossvalidation is executed.
- This is repeated until the standard deviation drops below $1 \%$, a maximum of five times.
- In this way, small datasets will be cross-validated many times. However, larger ones possibly once.


# 4.3. Internal loop and external loop in FSS-EBNA 

We consider that FSS-EBNA, as any machine learning algorithm to assess its accuracy, must be tested on unseen instances which do not participate in the selection of the best feature subset. Two accuracy estimation loops can be seen in the FSS process (see in Fig. 2):

- The internal-loop 10-fold cross-validation accuracy estimation that guides the search process is explained in the previous point. The internal loop represents the evaluation function of the proposed solution.
- The external-loop accuracy estimation, reported as the final 'goodness' of FSSEBNA, is testing the feature subset selected by the internal loop on unseen instances not used in the search for this subset. Due to the non-deterministic nature of FSSEBNA (two executions could not give the same result), five iterations of a two-fold cross-validation ( $5 \times 2 \mathrm{cv}$ ) have been applied as external-loop accuracy estimator.


### 4.4. The 'overfitting' problem and the stopping criterion

In the initial stages of the definition of FSS-EBNA, we hypothesized to report the accuracy of the internal loop as the final performance. However, Aha [3] and Kohavi [49], in personal communications, alerted us of the overtly optimistic nature of the crossvalidation estimates which guide the search. Due to the search nature of FSS-EBNA, it is possible that one feature subset (from the big amount of subsets visited) could be very well adapted to the training set, but when presented to new instances not presented in the training process, the accuracy could dramatically decay: an 'overfitting' [78] can occur internally in the FSS process. Although it was not done by some authors, we recommend not to report the accuracy used to guide the search as the final accuracy of an FSS process.

Jain and Zongker [40] reported for a non-deceptive function in a pattern recognition problem that the quality of selected feature subsets for small training sets was poor; however, improved as the training set increased. Kohavi [46] also noted in a wrapper machine learning approach that the principal reason of 'overfitting' was the low amount of training instances.

To study this issue for FSS-EBNA, we have carried out a set of experiments with different training sizes of the Waveform-40 dataset [15] with the Naive-Bayes classification

![img-3.jpeg](img-3.jpeg)

Fig. 7. Internal- and external-loop accuracy values in FSS-EBNA for different training sizes with the Waveform-40 dataset and the Naive-Bayes learning algorithm. The internal-loop accuracy 10 -fold cross-validation is multiple times repeated until the standard deviation of the accuracy estimation drops below $1 \%$. Dotted lines show the internal-loop accuracy estimation and solid lines the external-loop one. Both loop accuracies for the best solution of each search generation are represented. ' 0 ' generation represents the initial generation of the search.
algorithm [19]: training sizes of 100, 200, 400, 800 and 1600 samples and tested over a fixed test set with 3200 instances. Fig. 7 summarizes the set of experiments.

For 100, 200 and 400 training sizes, although the internal-loop cross-validation was repeated multiple times, differences between internal- and external-loop accuracies were

greater than twice the standard deviation of the internal loop. However, when the training size increases, the fidelity between internal- and external-loop accuracies increases, and the accuracy estimation of the external loop appears in the range formed by the standard deviation of the internal-loop accuracy.

Apart from these accuracy estimation differences between both loops, a serious 'overfitting' risk arises for small datasets: as the search process advances, the internal loop's improvement deceives us, as posterior performance on unseen instances does not improve. The difference between internal and external estimations would not be so important if both estimations had the same behaviour: that is, an improvement in the internal estimation coupled with an external improvement and a decrease in internal estimation coupled with an internal improvement. However, it clearly seems that this can not be guaranteed for small size training sets, where two curves show an erratic relation. Thus, FSS results generalization must be done with high care for small datasets.

It seems obvious that for small datasets it is not possible to see FSS-EBNA as an 'anytime algorithm' (Boddy and Dean [11]), where the quality of the result is a nondecreasing function in time. Looking at Fig. 7, we discard this 'monotonic-anytime idea' (more time $\leftrightarrow$ better solution) for small training set sizes. Our findings follow the work of Ng [70], who in an interesting work on the 'overfitting' problem, demonstrates that when cross-validation is used to select from a large pool of different classification models in a noisy task with too small training set, it may not be advisable to pick the model with minimum cross-validation error, and a model with higher cross-validation error will have better generalization error over novel test instances.

Regarding this behaviour, so related with the number of instances in the training set, the next heuristic as stopping criterion is adopted for FSS-EBNA:

- For datasets with more than 2000 instances (more than 1000 instances in each training subset for the $5 \times 2 \mathrm{cv}$ external-loop accuracy estimation), the search is stopped when in a sampled new generation no feature subset appears with an evaluation function value improving the best subset found in the previous generation. Thus, the best subset of the search, found in the previous generation, is returned as FSS-EBNA's solution.
- For smaller datasets (less than 1000 instances in each training subset for the $5 \times 2 \mathrm{cv}$ external-loop accuracy estimation), the search is stopped when in a sampled new generation no feature subset appears with an evaluation function value improving, at least with a p-value smaller than $0.1,{ }^{3}$ the value of the evaluation function of the feature subset of the previous generation. Thus, the best subset of the previous generation is returned as FSS-EBNA's solution.
An improvement in the internal-loop estimation is not the only measure to take into account to allow the continuation of the search in FSS-EBNA. The number of instances of the dataset is also critical for this permission. For larger datasets the 'overfitting' phenomenon has a lesser impact and we hypothesize that an improvement in the internalloop estimation will be coupled with an improvement in generalization accuracy on unseen instances. Otherwise, for smaller datasets the 'overfitting' phenomenon has a

[^0]
[^0]:    ${ }^{3}$ Using a 10 -fold cross-validated paired $t$ test between the folds of both estimations, taking only the first run into account when 10 -fold cross-validation is repeated multiple times.

greater risk in occurring and the continuation of the search is only allowed when a significant improvement in the internal-loop accuracy estimation of best individuals of consecutive generations appears. We hypothesize that when this significant improvement appears, the 'overfitting' risk decays and there is a basis for further generalization accuracy improvement over unseen instances.

# 5. Datasets and learning algorithms 

### 5.1. Used datasets

Table 1 summarizes some characteristics of the selected datasets. Five real datasets come from the UCI repository [68]. The image dataset comes from the Statlog project [85].

LED24 (Breiman et al. [15]) is a well known artificial dataset with 7 equally relevant and 17 irrelevant binary features. We designed another artificial domain, called Redundant21, which involves 21 continuous features in the range [3,6]. The target concept is to define whether the instance is nearer (using the Euclidean distance) to $(0,0, \ldots, 0)$ or $(9,9, \ldots, 9)$. The first nine features appear in the target concept and the rest of the features are repetitions of relevant ones, where the 1st, 5th and 9th features are respectively repeated four times.

As the wrapper approach is used we must take into account the number of instances in order to select the datasets. Although the used learning algorithms (they we will be explained in the next point) are not computationally very expensive, the running times could be extremely high for datasets with more than 10,000 instances.

In order to select the datasets, another basic criterion is the number of features of the dataset. Once Bayesian networks are used to factorize the probability distribution of the best solutions of a population, a sufficient number of solutions must fixed to reliably estimate the parameters of the network. If we choose datasets of a larger dimensionality (more than 50 features), we would need an extremely large number of solutions (much more than the actual population size, 1000), associated with the cost of the calculation of

Table 1
Details of experimental domains. $\mathrm{C}=$ continuous. $\mathrm{N}=$ nominal

![img-4.jpeg](img-4.jpeg)

Fig. 8. Relations between relevant concepts to estimate a reliable Bayesian network.
their evaluation functions by wrapper approach, to reliably estimate the parameters of the network.

FSS-EBNA is independent to the evaluation function used and a filter approach could also be used. In this way, before the execution of FSS-EBNA, we must take into account the quantity of available computational resources in order to fix the following parameters for the estimation of a reliable Bayesian network: characteristics of the evaluation function, number of instances and features of the dataset and number of solutions in the population. Fig. 8 shows the relations between these concepts.

# 5.2. Learning algorithms 

Two learning algorithms from different families are used in our experiments. ${ }^{4}$

- ID3 (Quinlan [77]) classification tree algorithm uses the gain-ratio measure to carry out the splits in the nodes of the tree. It does not incorporate a post-pruning strategy in the construction of the tree. It only incorporates a pre-pruning strategy, using the chi-squared statistic to guarantee a minimum dependency between the proposed split and the class.
- Naive-Bayes (NB) (Cestnik [19]) algorithm uses a variation of the Bayes rule to predict the class for each instance, assuming that features are independent to each other for predicting the class. The probability for nominal features is estimated from data using maximum likelihood estimation. A normal distribution is assumed to estimate the class conditional probabilities for continuous attributes. In spite of its simplicity Kohavi and John [47] noted NB's accuracy superiority over C4.5 (Quinlan [79]) in a set of real tasks.
ID3 has an embedded low capacity for discarding irrelevant features. It may not use all the available features in the tree structure, but it tends to make single class 'pure' folds in the decision tree, even if they only have a single training sample. Its tendency to 'overfit'

[^0]
[^0]:    ${ }^{4}$ It must be noted that in the 'wrapper' schema any classifier can be inserted.

the training data and damage the generalization accuracy on unseen instances has been noticed by many authors (Caruana and Freitag [17], Kohavi and John [47], Bala et al. [6]). Because one must not trust ID3's embedded capacity to discard irrelevant features, FSS can play a 'normalization' role to avoid these irrelevant splits, hiding the attributes from the learning algorithm which may 'overfit' the data in deep stages of the tree and do not have generalization power.

Despite its good scaling with irrelevant features, NB can improve its accuracy level discarding correlated and redundant features. NB, based on the independence assumption of predictive features to predict the class, is hurt by correlated features which violate this independence assumption. Thus, FSS can also play a 'normalization' role to discard these groups of correlated features, ideally selecting one of them in the final model. Although Langley and Sage [52] proposed a forward feature selection direction for detecting these correlations, Kohavi and John [47] proposed the backward direction.

# 6. Experimental results 

As 5 iterations of a 2-fold cross-validation were applied, the reported accuracies are the mean of ten accuracies. The standard deviation of the mean is also reported. Tables 2 and 3 respectively show the accuracy of ID3 and NB, both with and without FSS-EBNA feature subset selection. Tables 4 and 5 respectively show the average cardinality of features used by ID3 and NB. Once 5 iterations of a 2 -fold cross-validation were executed, a $5 \times 2 \mathrm{cv}$ $F$ (Alpaydin [5]) test was applied to determine whether accuracy differences between FSS-EBNA approach and no feature selection are significant or not. $5 \times 2 \mathrm{cv} F$ test is a variation of the well known $5 \times 2 \mathrm{cv}$ paired $t$ test (Dietterich [26]). The p-value of the test is reported, which is the probability of observing a value of the test statistic that is at least as contradictory to the null hypothesis (compared algorithms have the same accuracy) as the one computed from sample data (Mendenhall and Sincich [61]).

Table 2
A comparison of accuracy percentages of ID3 with and without FSS-EBNA
Table 3
A comparison of accuracy percentages of NB with and without FSS-EBNA
Table 4
Cardinalities of selected feature subsets for ID3 with and without FSS-EBNA. It must be taken into account that ID3 carries out an embedded FSS and it can discard some of the available features in the construction of the decision tree. The third column shows the full set cardinality

Table 6 shows in which generation stopped each of the ten runs of the 5 x 2 cv procedure. Table 7 shows the average running times (in seconds) for these ten single folds. Experiments were run in a SUN-SPARC machine. The MLC++ software (Kohavi et al. [48]) was used to execute Naive-Bayes and ID3 algorithms.

- FSS-EBNA has helped ID3 to induce decision trees with significantly fewer attributes coupled with a maintenance of the predictive accuracy in the majority of databases. We place this result near the assertion made by Kohavi and John [47] on the preprocessing step already made to many real datasets which only include relevant features. ID3's accuracy is specially damaged by irrelevant features, and when the dataset is already preprocessed a FSS process is only able to detect a smaller feature subset that equalizes the accuracy of features used in the tree when no FSS process

Table 5
Cardinalities of selected feature subsets for NB with and without FSS-EBNA. It must be taken into account that when no FSS is applied to NB, it uses the full feature set to induce the classification model

Table 6
Generation in which stopped each of the ten runs of the $5 \times 2 \mathrm{cv}$ procedure. It must be noted that the subset returned by the algorithm was the best subset of the previous generation respect the stop. The initial generation is considered as ' 0 '

is made. The average accuracy improvement over the set of databases is due to only three domains. In Ionosphere domain, a slight accuracy improvement is achieved and in Horse-colic, the improvement is significant. In LED24 artificial domain, specially selected to test the robustness of FSS-EBNA wrapped by ID3, the 17 irrelevant features are always filtered by FSS-EBNA and only the 7 relevant features are finally returned by FSS-EBNA. Otherwise, when no FSS is made, all the irrelevant features also appear in the tree.

- FSS-EBNA has also helped NB to significantly reduce the number of features needed to induce the final models. This dimensionality reduction is coupled with considerable accuracy improvements for all except one domain. In LED24 NB tolerates the influence of the 17 irrelevant features and further FSS is only able to reduce the dimensionality maintaining the predictive accuracy. The average accuracy

Table 7
CPU times, in seconds, for FSS-EBNA. Reported numbers reflect the average times and standard deviation for the ten folds of $5 \times 2 \mathrm{cv}$

with respect to all domains increases from $83.48 \%$ to $89.57 \%$, which implies a $36.86 \%$ relative reduction in the error rate. In Redundant21 artificial domain, specially selected to test the robustness of FSS-EBNA wrapped by NB, FSS-EBNA is able to detect all the redundancies that hurt NB's accuracy and violate its independence assumption among features, selecting only once, the repeated features which appear in the target concept.

- Owing to the fact that the wrapper approach FSS-EBNA needs large CPU times for ID3. Our approach, based on the evolution of populations, needs a minimum amount of individuals to be evaluated in order to reliably induce the Bayesian networks that guarantee the evolution of the process. The times needed to induce the Bayesian networks in each generation are insignificant in comparison to the time needed to calculate the evaluation functions: more than $99 \%$ of the whole CPU time is employed 'wrapping' over both learning algorithms in all the domains. The induction of the Bayesian networks by the presented local search mechanism has demonstrated a low cost. In order to induce a Bayesian network over the best individuals 3 CPU seconds are needed by average in Image domain (the domain with fewer features) and 14 CPU seconds in Anneal (the domain with more features). Due to the simplicity of the NB learning algorithm to be trained and tested (storage of conditional probabilities for each attribute given the class), the overall times for FSS-EBNA are considerably smaller.
- To understand the CPU times of Table 7, the generations where the searches stop must be also taken into account (Table 6). Each generation supposes the evaluation of 1000 individuals and differences in the stop generation generate the presented standard deviations of CPU time.


# 7. Summary and future work 

GAs, due to its attractive, randomized and population-based nature, have long been applied for the FSS problem by statistics, pattern recognition and machine learning

communities. This work presents FSS-EBNA, a new search engine which shares these interesting characteristics of GAs. In FSS-EBNA, the FSS problem, stated as a search problem, uses the EBNA (Estimation of Bayesian Network Algorithm) search engine, a variant of the EDA (Estimation of Distribution Algorithm) approach. EDA, also based as GAs on the evolution of populations of solutions, is an attractive approach because it avoids the necessity of fixing crossover and mutation operators (and respective rates) so needed in GAs. The selection of crossover and mutation operators and rates is still an open problem in GA tasks. However, EDA guarantees the evolution of solutions by the factorization of the probability distribution of best individuals in each generation of the search. In EBNA, this factorization is carried out by a Bayesian network induced by a cheap local search mechanism.

The work exposes the different roots of the FSS-EBNA method and related work for each concept: the FSS process as a search problem, the EDA approach and the Bayesian networks. Joining the pieces provided by these three concepts the FSS-EBNA process can be understood.

Once the basic pieces are exposed, the different parameters of the FSS-EBNA process itself are presented and justified. A reflexion on the 'overfitting' problem in FSS is carried out and inspired on this reflexion the stop criterion of FSS-EBNA is determined, so related with the number of instances of the domain.

Our work has included two different, well known learning algorithms: ID3 and NB. The wrapper approach is used to asses the evaluation function of each proposed feature subset and it has needed a large amount of CPU time with the ID3 learning algorithm. However, the induction of the Bayesian networks that guarantees the evolution has demonstrated to be very cheap in CPU time. FSS-EBNA has been able to filter in artificial tasks, the special kind of features that hurt the performance of the specific learning a As future work, we consider lengthening the work already done (Inza [38]) using EBNA for the Feature Weighting problem in Nearest Neighbor Algorithm. Continuing the work within the EDA approach for FSS, an interesting way to be explored when the presented CPU times are prohibitive, is the use of filter approaches to calculate the evaluation function. In order to deal with domains with much larger numbers of features ( $>100$ ), future work should address the use of simpler probability models to factorize the probability distribution of best individuals, models which assume fewer or no dependencies between the variables of the problem. Another way of research will be the employment of a metric which fixes for each domain, the number of individuals needed to reliably learn (Friedman and Yakhini [32]) the parameters of the Bayesian network.

# Acknowledgements 

This work was supported by grants PI 96/12 from the Basque Country Government, Departamento de Educación, Universidades e Investigación and by CICYT under TIC97-1135-C04-03 grant.
