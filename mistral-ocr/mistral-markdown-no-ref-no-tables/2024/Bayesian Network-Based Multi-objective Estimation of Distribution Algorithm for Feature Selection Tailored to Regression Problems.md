# Bayesian Network-Based Multi-objective Estimation of Distribution Algorithm for Feature Selection Tailored to Regression Problems 

José A. López ${ }^{1}$ (D), Felipe Morales-Osorio ${ }^{2}$ (D), Maximiliano Lara ${ }^{3}$ (D), Jonás Velasco ${ }^{1,4}$ (D), and Claudia N. Sánchez ${ }^{3(\boxtimes)}$ (D)<br>${ }^{1}$ Centro de Investigación en Matemáticas (CIMAT), A.C., 20200 Aguascalientes, Mexico<br>\{jose.portillo,jvelasco\}@cimat.mx<br>${ }^{2}$ Massachusetts Institute of Technology, Cambridge, MA 02139, USA<br>fmorales@mit.edu<br>${ }^{3}$ Facultad de Ingeniería, Universidad Panamericana, 20296 Aguascalientes, Mexico<br>\{0218259, cnsanchez\}@up.edu.mx<br>${ }^{4}$ Consejo Nacional de Humanidades Ciencias y Tecnologías (CONAHCYT), 03940 Ciudad de México, Mexico


#### Abstract

Feature selection is an essential pre-processing step in Machine Learning for improving the performance of models, reducing the time of predictions, and, more importantly, identifying the most significant features. Sometimes, this identification can reduce the time and cost of obtaining feature values because it could imply buying fewer sensors or spending less human time. This paper proposes an Estimation of Distribution Algorithm (EDA) for feature selection tailored to regression problems with a multi-objective approach. The objective is to maximize the performance of learning models and minimize the number of selected features. We use a Bayesian Network (BN) as the EDA distribution probability model. The main contribution of this work is the process used to create this BN structure. It aims to capture the redundancy and relevance among features. Also, the BN is used to create the initial EDA population. We test and compare the performance of our proposal with other multi-objective algorithms: an EDA with a Bernoulli distribution probability model, NSGA II, and AGEMOEA, using different datasets. The experimental results show that the proposed algorithm found solutions with a considerably fewer number of features. Additionally, the proposed algorithm achieves comparable results on models' performance compared with the other algorithms. Our proposal generally expended less time and had fewer objective function evaluations.


Keywords: Feature selection $\cdot$ estimation distribution algorithms $\cdot$ bayesian network $\cdot$ multi-objective optimization $\cdot$ regression problems

# 1 Introduction 

In Machine Learning, most real-world problems involve a large amount of data. Usually, this data has a high number of features, which makes the learning process difficult. However, not all features are essential since many of them are redundant or even irrelevant, which may reduce the performance of a learning algorithm. Feature Selection (FS) problems involve reducing the size of the original datasets by selecting a small subset of relevant features from the original dataset while maintaining model performance $[1,23]$. According to the mathematical definition presented on [1], an FS problem can be formulated as follows. Assume a dataset consists of a set of features $\mathcal{F}$ with exactly $d$ number of features, $\mathcal{F}=\left\{\mathcal{F}_{1}, \mathcal{F}_{2}, \mathcal{F}_{3}, \ldots, \mathcal{F}_{d}\right\}$, the objective is to select the best subsets of features of size $k$ from $\mathcal{F}$, where $k<d$. Feature selection becomes a difficult task as the number of features increases. For $d$ features, there are $2^{d}$ subsets that can be selected to train a learning algorithm $[6,9,23]$.

According to [8], there are three different approaches for solving the FS task: filter, wrapper, and embedded methods. Filter methods consist of finding the best subset of features according to the intrinsic characteristics of the data (e.g., correlation coefficient) that measure the relevance and redundancy of features. They are independent of the learning algorithms. Because of this, they are computationally faster than the other methods. Wrapper methods train a learning algorithm on a selected subset of features and use the algorithm's performance to evaluate the quality of the subset. They aim to find a subset of features that minimizes the learning algorithm's error. However, because they need to train on each subset of features, they are computationally more expensive than filter methods but generally offer better performance. Embedded methods incorporate feature selection into model training. For example, decision trees can be used in these models. After generating the prediction model, decision trees return a feature's importance, which can be used to create new solutions. As pointed out in [12], hybrid methods have been developed to exploit the benefits of different approaches (e.g., using a filter method to reduce computation time and a wrapper method to increase model performance).

Most of the documents tailored to feature selection have recently used a multi-objective approach [12]. Commonly, the first objective function is related to the performance of a learning model, and the second objective aims to reduce the number of features. These techniques return a set of feature subsets, and the end user can use the one better adapted to its application. Since FS is an optimization problem whose search space grows exponentially according to the number of features $d$, Evolutionary Algorithms (EAs) are techniques that can be used to solve this problem. Some of the EAs that have been applied for solving FS with a multi-objective approach are Genetic Algorithms [21], Particle Swarm Optimization (PSO) [22], and Differential Evolution (DE) [24]. The choice of the solution representation is highly related to the applied EA [23], but using continuous representations, such as the one used in PSO or DE, increases the search space. Genetic Algorithms and Estimation of Distribution Algorithms are techniques that can use binary representation. Specifically, NSGA

II (Nondominated Sorting Genetic Algorithm) [7] is a fast and powerful technique for solving multi-objective problems. It has been widely used for FS [10,19,21].

In this work, we explore the Estimation of Distribution Algorithms (EDAs) because they can combine filter metrics for measuring the redundancy and the relevance of features with the wrapper techniques evaluating the performance of learning models. Soliman and Rassem [20] proposed a filter technique that consisted of a quantum bio-inspired EDA for correlation-based feature selection to obtain optimal feature subsets. Maza and Touahria [16] proposed an EDA, a hybrid methodology, for FS in classification problems. Instead of randomly creating the initial population, they use the relevance between features and the class. In addition, they propose four probabilistic models for estimating the probability of each feature being selected. Those models use metrics of relevance and redundancy among features. However, they calculate the probability of features being selected separately. We propose using a Bayesian Network as the probabilistic model for sampling the selection values of features according to the selection values previously assigned to other features.

Some documents previously used Bayesian Networks for FS in EDAs. Their creation of the net is described as follows. Larrañaga et al. [11] used Estimation of Bayesian Networks Algorithm (EBNA) [14], which is a greedy search which starts with an arc-less structure and, at each step, adds the arc with the maximum improvement in the measure used. The algorithm stops when adding an arc would not increase the scoring measure. Castro and Von Zuben [3] begins with an initial network generated at random. Next, the probability distribution of each variable is estimated using the dataset, and the network score is computed. The search process generally proposes small changes to the structure to obtain a network with a higher score than the previous one. These small changes can be accomplished by adding or deleting an edge or reversing the edge direction. Every time a change is made, it is necessary to compute the probability distribution of the variables for the modified network. In contrast, our proposal creates the network structure as a tree, where each node represents an input feature and the arcs represent the redundancy among them. We use this graph structure because we are interested in establishing a unique dependence among the variables in order to create the simplest algorithm while keeping complexity as low as possible. The objective is to maximize a redundance metric among the connected features.

This paper proposes a Bayesian network-based multi-objective estimation of distribution algorithm for feature selection tailored to regression problems. The regression problems have numeric vectors from $\mathbb{R}^{d}$ as inputs, where $d$ is the number of features, and numeric scalars from $\mathbb{R}$ as outputs. We focus on two criteria: maximizing the performance of the learning models and minimizing the number of selected features. The main contribution of our proposal is that the probabilistic model of the EDA is a Bayesian Network defined to capture the relevance and redundancy in the features. Mainly, the difference between our proposal and others using EDAs with Bayesian Networks is how the BN is created. In our case, it is a tree where the arcs represent the redundancy among

features. In addition, the first generation is a filter method that creates solutions based on the BN structure, maximizing relevance and minimizing redundancy among features.

The rest of the paper is organized as follows. Section 2 presents the background concepts. Our proposal is described in the Methodology Sect.3. The experiments and results are presented in Sect.4. Finally, Sect. 5 concludes this document and describe the future work.

# 2 Background 

In this section, we briefly review the fundamental concepts of this research. We started with Multi-objective Evolutionary Optimization, followed by Estimation of Distribution Algorithms (EDAs), and finalized with Bayesian Networks (BN).

### 2.1 Multi-objective Evolutionary Optimization

In multi-objective optimization [4], a variety of optimization problems are tackled, each involving one of the $n$ distinct objective functions $f_{1}(s), \ldots, f_{n}(s)$. These functions operate on $s$, a vector of parameters from a specific domain. Consider $\mathcal{S}$ to be the potential solution space for such a multi-objective optimization problem. A solution set is classified as non-dominated (alternatively referred to as Pareto optimal) when there is no $t \in \mathcal{S}$ that, for any $s \in \mathcal{S}$, can satisfy the following:

- $\exists i$, where $i \in\{1, \ldots, n\}, f_{i}(t)$ enhances $f_{i}(s)$,
$-\forall j$, where $j \in\{1, \ldots, n\}$ and $j \neq i, f_{j}(s)$ cannot improve $f_{j}(t)$.
The main point is that one solution $s$ is considered to dominate another $t$ if $s$ surpasses $t$ on at least one objective and is not inferior on the remaining ones. We term $s$ as non-dominated when no other solution outperforms it. The set of these non-dominated solutions within $\mathcal{S}$ is known as the Pareto front. The goals of multiobjective optimization is to find set of solutions as close as possible to Pareto-optimal front and to find a set of solutions as diverse as possible. When it comes to multi-objective optimization, multi-objective evolutionary algorithms are particularly beneficial as they concurrently pursue multiple best solutions. These algorithms can locate a collection of top solutions in the end population with just a single run, and once this set is ready, the most pleasing solution can be picked based on a preference criterion.

Feature selection consists of two main objectives: minimizing the cardinality of the subset of selected features and maximizing the model's performance. These objectives often conflict, giving space for multiobjective optimization techniques such as evolutionary multi-objective optimization. In these algorithms, more than one solution is returned, and each solution corresponds to a specific trade-off between the objectives. This way, of the reported solutions, some will represent a larger subset with better performance. In comparison, others will give a smaller subset but diminish the model's performance.

In this work, we use two algorithms: the Non-dominated Sorting Genetic Algorithm II (NSGA-II) [7] and Adaptive Geometry Estimation based MultiObjective Evolutionary Algorithms (AGEMOEA) [18]. The NSGA-II and AGEMOEA are examples of Evolutionary Algorithms designed for solving multiobjective optimization problems. The former finds a diverse set of solutions and covers near the true Pareto optimal set. The latter, AGEMOEA, modifies NSGAII by replacing the fitness assigned to the solutions in each non-dominated front. In AGEMOEA, the crowding distance of NSGA-II is replaced by a survival score that combines both diversity and proximity of the solutions within the same non-dominated front.

# 2.2 Estimation of Distribution Algorithms (EDAs) 

Introduced in [17], Estimation of Distribution Algorithms (EDAs) are based on Evolutionary Algorithms where a population of $N$ individuals becomes better to their fitness value each iteration [14]. This algorithm replaces crossover and mutation operators of EAs by estimation of parameters of the $M$ best individuals of the population. The probability distribution function is used to sample new $N$ individuals who will become part of the next generation of the algorithm. This process is repeated until a stopping criterion is met. It could be the maximum number of iterations, convergence criterion based on stagnation, etc. The algorithm learns from the population and modifies the probability distribution in each generation. The overall fitness value of the population will be better in each iteration. It is important to see that exploitation and exploration in the search space are controlled by random sampling of new individuals.

```
Algorithm 1: The basic steps of an EDA.
    Input : population size \(N\), selection size \(M\), where \(M<N\)
    Output: the best solution(s) found \(S_{\text {Best }}\)
    \(P_{0} \leftarrow\) Generate initial population with \(N\) random individuals
    2 Evaluate each individual \(s\) in \(P_{0}\) using the objective function
    \(S_{\text {Best }} \leftarrow\) Get the best solution(s) from \(P_{0}\)
    \(t \leftarrow 0\)
    while termination criteria are not met do
        \(S_{t} \leftarrow\) Select \(M\) individuals from \(P_{t}\) according to a selection method
        \(\bar{p}_{t} \leftarrow\) Estimate the probability density of solutions in \(S_{t}\)
        \(P_{t+1} \leftarrow\) Sample \(N\) individuals from \(\bar{p}_{t}\)
        Evaluate \(P_{t+1}\) using the objective function
        Update \(S_{\text {Best }}\) according to the solutions in \(P_{t+1}\)
        \(t \leftarrow t+1\)
    end
    return \(S_{\text {Best }}\)
```

Algorithm 1 shows the basic pseudo-code of a typical EDA. EDAs utilize several parameters, including the population size $N$, the number of generations

(or iterations) $G$, and the number of individuals selected, $M$ for estimate the probability density of solutions, $\bar{p}_{t}$. The set of selected solutions $S_{t}$ serves as a training dataset to estimate the probabilistic model and leads the search towards regions with better fitness. The set of new solutions $P_{t+1}$ is generated using the probabilities encoded in the probabilistic model in accordance with the statistics collected from the solutions in $S_{t}$.

Early EDAs were developed for discrete domains, as it is common in evolutionary algorithms to represent solutions with binary representations. Variations of EDAs are widely used for combinatorial optimization problems where more sophisticated distributions are used for sampling new individuals. For solving optimization problems in continuous domains, variations of the original EDAs approach also exist.

EDA algorithms are commonly grouped according to the degree of interaction among variables into univariate, bivariate, and multivariate EDAs. Univariate EDAs, such as Univariate Marginal Distribution Algorithm (UMDA), assume that all variables are independent and factorize the joint probability of the selected solutions as a product of univariate marginal probabilities. Multivariate EDAs do not necessarily limit the degree of interactions among variables and can be modelled with unrestricted Bayesian Networks. The choice of probabilistic model can have a major influence on the performance and efficiency of EDAs.

# 2.3 Bayesian Networks 

A Bayesian Network (BN) [13] is a probabilistic graphical model which provides a robust general approach especially suited to modeling complex non-deterministic systems. A BN models the causal relationships between the features of a model. It consists of a Directed Acyclic Graph (DAG) $\mathcal{G}$ [13], and a set of parameters $\Theta$, defining the strength and the shape of the relationships between features. To use a BN, one must define the graph $\mathcal{G}$ and then calculate its parameters $\Theta$. Defining the graph $\mathcal{G}$ is a task that can be done by learning through data or by consulting human experts in a specific field [13].
$\mathcal{G}$ consists of a set of vertices $\mathcal{V}$ and a set of directed edges $\mathcal{E}$. The vertices in $\mathcal{V}$ represent the features whose relationship is modeled by the BN, and the edges in $\mathcal{E}$ represent the relationships between the features. A directed edge from $V_{i}$ to $V_{j}$ where $V_{i}, V_{j} \in \mathcal{V}$ is symbolically represented by the tuple $\left(V_{i}, V_{j}\right) \in \mathcal{E}$ or graphically represented as $V_{i} \rightarrow V_{j}$. The directed edge $\left(V_{i}, V_{j}\right) \in \mathcal{E}$ indicates that $V_{i}$ is the parent of $V_{j}$ and that $V_{j}$ is the child of $V_{i}$. A BN models a parentchild relationship as the parent variable causing the child variable. Therefore, the directed edge $\left(V_{i}, V_{j}\right)$ in a BN means that the parent variable $V_{i}$ causes the child variable $V_{j}$. Additionally, every directed edge $\left(V_{i}, V_{j}\right) \in \mathcal{E}$ has a parameter $\theta_{i, j} \in \Theta$. The parameter $\theta_{i, j}$ associated with this edge is a matrix modeling $\operatorname{Pr}\left(V_{j} \mid V_{i}\right)$ (the conditional probability of $V_{j}$ given $V_{i}$ ). If $V_{i}, V_{j}$ can take on $\left|V_{i}\right|,\left|V_{j}\right|$ different values respectively, then this matrix $\theta_{i, j}$ will have $\left|V_{i}\right| \times\left|V_{j}\right|$ different entries.

Finally, a BN assumes that the joint probability distribution of the variables $P\left(V_{1}=v_{1}, V_{2}=v_{2}, \ldots, V_{n}=v_{n}\right)$, defined in Eq. (1), can be decomposed as the product of the conditional distribution of the variables given the value of their parents $P\left(V_{i}=v_{i} \mid \mathbf{P a}\left(V_{i}\right)\right)$.

$$
P\left(V_{1}=v_{1}, V_{2}=v_{2}, \ldots, V_{n}=v_{n}\right)=\prod_{i=1}^{n} P\left(V_{i}=v_{i} \mid \mathbf{P a}\left(V_{i}\right)\right)
$$

# 3 Methodology 

Our proposal is an Estimation of Distribution Algorithm for feature selection tailored to regression problems with a multi-objective approach. Our regression problems have numeric vectors from $\mathbb{R}^{d}$ as inputs, where $d$ is the number of features, and numeric scalars from $\mathbb{R}$ as outputs. We focus on two criteria: maximizing the performance of the learning models and minimizing the number of selected features. Our main contribution is using a Bayesian Network (BN) as the sample distribution model. The BN aims to capture the redundancy among features. Additionally, the first generation can be seen as a filter method that creates solutions that maximize relevance and minimize redundancy among features.

We follow the Algorithm 1, explained in the previous section. In this section, we describe the details of the implementation. First, in Subsect.3.1, we explain the individuals' representation and evaluation. The selection of the individuals used for calculating the distribution model, in this case, the BN, is described in Subsect. 3.2. The creation of the structure of the BN is described in Subsect. 3.3. Subsection 3.4 describes the initialization of the population. In this case, instead of being totally random, it is initialized using the BN. The BN's probabilities calculation is explained in Subsect. 3.5. Finally, Subsect. 3.6 describes how the individuals of the new population are sampled using the BN.

### 3.1 Representing and Evaluating Individuals

Our proposal aim to solve the feature selection in regression problems. Regression can be mathematically expressed as follows. We are given a set $\mathcal{D}=$ $\left\{\left(\overrightarrow{x_{1}}, y_{1}\right), \ldots,\left(\overrightarrow{x_{n}}, y_{n}\right)\right\}$ of $n$ input-output data pairs with $d$ features in the inputs where $\overrightarrow{x_{i}} \in \mathbb{R}^{d}$ and $y_{i} \in \mathbb{R}$ for all $i \in\{1 \ldots n\}$. The regression model $\mathcal{M}$ aims to minimize $\sum_{(\vec{x}, y) \in \mathcal{D}} E(\mathcal{M}(\vec{x}), y)$, where $E$ is a function that measures the difference or error between $\mathcal{M}(\vec{x})$ and $y$. The ideal scenario would be $\mathcal{M}(\vec{x})=y \forall(\vec{x}, y) \in \mathcal{D}$. The model predictions $\mathcal{M}(\vec{x})$ also are defined as $\widehat{y}$. Feature selection consists of selecting the best subsets of features of size $k$, where $k<d$. An individual representing a solution for the feature selection problem is a binary vector of size $d$, where the $i$-th element corresponds to the $i$-th feature in the dataset. A value of 1 means that the $i$-th feature is selected for fitting the model, while 0 indicates that the $i$-th feature is left out.

We define two criteria as objective functions. The first is related to the regression models' performance, and the other to the number of selected features. Regression involves finding a mathematical model that relates input features to an output feature to reduce an error. The determination of coefficient $R^{2}$ (Eq. 2) can be used for measuring the performance of a regression model. If its value is close to 1 indicates a good performance of the model, or in other words, that the regression model explains a large portion of the variability in the response. A number near 0 indicates that the regression does not explain much of the variability in the response, and it is almost equal to random guesses according to the output feature distribution. Finally, negative values indicate that the regression model gives worse results than random guesses. In our proposal, for having minimization objective functions, we define $\overline{R^{2}} \equiv 1-R^{2}$. By doing this, we focus on minimizing the performance of the regression model trained with a subset of features.

$$
R^{2}(y, \widehat{y})=1-\frac{\sum_{i}\left(y_{i}-\widehat{y}_{i}\right)^{2}}{\sum_{i}\left(y_{i}-\bar{y}_{i}\right)^{2}}
$$

The second objective function is designed to minimize the number of selected features. It is defined as $|\mathcal{F}|$ and corresponds to the number of selected features in the subset divided by the total number of features in the data set. A number near to 0 indicates that the subset has a few features selected. On the other hand, a number close to 1 indicates that most of the features have been selected.

# 3.2 Selection of Individuals for Estimating the Parameters of the Bayesian Network 

Step 6 of Algorithm 1 consists of selecting the best $M$ individuals from the population to calculate the parameters of the distribution model, in this case, the probabilities of the Bayesian Network. For sorting the individuals, we use the fast non-dominated sorting algorithm presented in [7] and the non-domination rank that corresponds to the non-dominated front an individual belongs to.

### 3.3 Creating Bayesian Network Graph

A BN must be a DAG by definition. However, our BN is more restrictive because it is a tree. Our Bayesian Network $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ is a tree whose vertices $V_{i} \in \mathcal{V}$ represent the feature at index $i$ and whose edges $\left(V_{i}, V_{j}\right) \in \mathcal{E}$ represent the causal relationship between feature $i$ and feature $j$. The strength of the causal relationship between $V_{i}, V_{j}$ is approximated by $\left|C_{i, j}\right|$, corresponding to the absolute value of the Pearson correlation coefficient between the two features $i, j$ in a dataset. Our objective is to construct a tree capturing the redundancy between variables. In other words, we want to construct a tree with an edge set $\mathcal{E}$ that maximizes $R(\mathcal{E})$ as defined in Eq. (3).

$$
R(\mathcal{E})=\sum_{\left(V_{i}, V_{j}\right) \in \mathcal{E}}\left|C_{i, j}\right|
$$

Maximizing $R(\mathcal{E})$ is equivalent to finding the maximum spanning tree of $\mathcal{H}$ where $\mathcal{H}$ is a fully connected graph containing the vertices in our problem and the weighted edges $\left(V_{i}, V_{j}\right)$ are the values of $\left|C_{i, j}\right|$ between features. We use a modified version of Prim's Minimum Spanning Tree [5] algorithm to find the maximum spanning tree. In particular, we set the root vertex to the feature that has maximum relevance with the output feature in a dataset. We approximate relevance with $\left|C_{i}\right|$, the absolute value of the Pearson correlation coefficient between the feature $i$ and the output feature in the dataset.

Figure 1 illustrates the Bayesian Network produced by our algorithm using the Concrete Compressive Strength dataset (See Table 5). The root vertex corresponds to the feature Fly Ash because this is the one with the highest relevance to the output feature. In other words, Fly Ash had the highest absolute value of the Pearson correlation coefficient with the output variable. Next, an edge from the root to the vertex Blast Furnace Slag is drawn because it has the greatest redundancy with the root. This means it has the highest absolute value of the Pearson correlation coefficient with the root. Then, each successive edge added to the tree must not produce a cycle while also being the edge with the highest possible redundancy.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Bayesian Network produced from concrete data.

# 3.4 Creating Initial Population 

To create the initial population of individuals for the EDA, we use the parentchild structure of the BN and using the redundance and the relevance of features calculated with the Pearson correlation coefficient. Our proposal generates half of the individuals of the initial population via relevance and half via redundancy.

To generate individuals via redundancy, we want to avoid selecting two features that have a high redundancy with each other. To achieve this, we want every child variable to be more likely be the binary opposite of its parent variable if the parent-child redundancy metric is high. For example, if a parent $V_{i}=1$, then the child $V_{j}=0$ should have a high probability of occurring if the redundancy $\left|C_{i, j}\right|$ is high. Similarly, if a parent $V_{i}=0$, then the child $V_{j}=1$ should occur with high probability when $\left|C_{i, j}\right|$ is high. We model this expected probability distribution using a Bernoulli trial. $\operatorname{BERNOULLI}(p)$ runs a Bernoulli trial

to generate a binary value. The single parameter $p$ specifies the probability of a success. A success generates a 1 while a failure generates a 0 . The desired outcome $v_{j}$ for a child $V_{j}$ given value $v_{i}$ of its parent $V_{i}$ is the result of the Bernoulli trial with the parameter $p=\left|v_{i}-\left|C_{i, j}\right|\right|$ as $v_{j}=$ BERNOULLI $\left(\left|v_{i}-\left|C_{i, j}\right|\right|\right)$.

To generate individuals via relevance, we want the probability of feature $i$ being selected to be proportional to its relevance $\left|C_{i}\right|$ with the output. If a feature has high relevance, then it should have a high probability of being selected. Again, we model this probability distribution using a Bernoulli trial. The binary value $v_{i}$ of the variable $V_{i}$ should be determined as $v_{i}=$ BERNOULLI $\left(\left|C_{i}\right|\right)$.

# 3.5 Calculating Bayesian Network Parameters 

The Bayesian Network parameters are related to probability distributions; each vertex has its values. The probabilities are calculated based on the best individuals selected for making the distribution model in each algorithm iteration. First, we estimate $P\left(V_{r}\right)$, which corresponds to the probability distribution of $V_{r}$, the root variable of the tree. Table 1 shows the equations for calculating the $P\left(V_{r}\right)$ values, where $F$ represents the occurrence frequency of the feature values in the selected individuals. The rest of the vertices on the BN corresponds to conditional probabilities $P\left(V_{j} \mid V_{i}\right)$, where vertex $V_{i}$ can be seen as the parent of vertex $V_{j}$. Table 2 shows the equations for calculating the $P\left(V_{j} \mid V_{i}\right)$ values.

Table 1. Probability distribution of the root vertex $P\left(V_{r}\right)$

Table 2. Probability distribution $P\left(V_{j} \mid V_{i}\right)$

### 3.6 Sampling from Bayesian Network

Once the structure of the Bayesian Network and its parameters are calculated, it can be used to generate a new population of individuals. To start, we generate the binary value $v_{r}$ associated with the root $V_{r}$ using the BERNOULLI function based on $P\left(V_{r}\right)$. Once we have generated the root's binary value, we generate the

binary values associated with the remaining vertices from top to bottom. This is done so that the values of parent vertices are decided before the values of child vertices. To generate the binary value $v_{j}$ associated with vertex $V_{j}$ we must have a value $v_{i}$ associated with the parent vertex $V_{i}$. We generate the binary value associated with $V_{j}$ using the BERNOULLI function based on $P\left(V_{j} \mid V_{i}=v_{i}\right)$.

# 4 Experiments and Results 

In this section, we present our proposal's experiments and results. We used Linear Regression as the regression model because it is simple and fast. To analyze the performance of our proposal, we compare it with Non-dominated Sorting Genetic Algorithm II (NSGA-II) and Adaptive Geometry Estimation based Multi-Objective Evolutionary Algorithms (AGEMOEA) previously mentioned in Sect. 2. We used the implementation of those algorithms provided by the library Pymoo [2]. The hyper-parameters of those algorithms, defined by default in Pymoo, are presented in Table 3.

In addition, we compare our results with an Estimation of Distribution Algorithm that uses a Bernoulli model as the probability distribution, defined as EDA Bernoulli. This implementation initializes the population $P$ of individuals using Bernoulli trials. As mentioned in the previous section, an individual is a binary vector whose entry $v_{i}$ associated with feature $i$ is decided via a Bernoulli trial. In the initial population, the entry $v_{i}$ is given by the Bernoulli trial $v_{i}=\operatorname{BERNOULLI}(0.5)$. In the following generations of the algorithm, the population is sampled using the Bernoulli trial $v_{i}=\operatorname{BERNOULLI}\left(\operatorname{PROPORTION}\left(v_{i}\right)\right)$ where $\operatorname{PROPORTION}\left(v_{i}\right)$ is the proportion of times $v_{i}=1$ in the selected population. The hyper-parameters of the EDA implementations are presented in Table 4.

Table 3. Hyper-parameters of NSGA II and AGEMOEA

Our implementation was developed in the Python programming language, and we use the libraries Scikit-learn and numpy. Our computational experiments were run with an Intel Core i7-5500U Dual-Core Processor @ 2.40 GHz running the Windows 1064 -bit operating system based on an $\times 64$ processor with 8.00 GB of RAM.

Table 4. Hyper-parameters of EDA Bernoulli and EDA Bayesian Network

# 4.1 Datasets 

Five datasets are adopted from the UCI repository [15] (See Table 5). The datasets are of different dimensions, varying from 8 to 100 , and the number of instances is 395 to 515345 . Since we are solving a regression problem, we need the input features, and the output feature, to be of numerical type. For each dataset, the last column corresponds to the target feature. We had to preprocess this data because some of the features were categorical, or it contained missing values. The preprocess methodology is described as follows. First, columns with a high ratio of missing values were deleted. For example, the Communities and Crime dataset had many columns with around $84 \%$ missing values. Rows containing null values were removed from the datasets. Categorical variables with only two possible values were transformed into numerical variables by changing the value of one class to 0 and the other to 1 . Those variables with three or more possible values were transformed into numerical variables by applying one-hot encoding. In the case the categorical variables had more than 30 categories, they were removed from the dataset. In the Forest Fires dataset, the values of the feature month were transformed from 'jan', 'feb', 'mar', ..., 'dec' to $1,2,3, \ldots, 12$. And for the feature day, values were transformed from 'mon', 'tue', 'wed', ..., 'sun' to $1,2,3, \ldots, 7$. We randomly divided the datasets into training $(70 \%)$ and testing $(30 \%)$ sets to validate the results.

Table 5. Datasets

### 4.2 Comparison of Our Proposal Against Other Techniques

To the best of our knowledge, no study has been conducted on feature selection for the datasets described in Table 5. Most of the documents related to

feature selection are related to classification. However, we compare the results of our proposal, EDA Bayesian Network, with other multi-objective evolutionary algorithms: EDA Bernoulli, NSGA-II, and AGEMOEA. Each experiment was executed 100 times, except the experiment of the YearPredictionMSD dataset, which was executed only ten times for the expensive time required.

Figure 2, 3, 4, 5 and 6 show the non-dominated solutions found by the different algorithms. They contain the best solutions for different executions. In Fig. 2 and Fig. 3 can be observed that all the algorithms obtain similar results in the two smallest datasets, Concrete Compressive Strength and Forest Fires. On the medium dataset, Student Performance Math, EDA Bayesian Network found solutions with a less number of features (see Fig. 4). And in the two biggest datasets, YearPredictionMSD and Communities and crime, AGMOEA got better results in the regression model performance, but our proposal got considerably better results in the number of selected features (see Fig. 5 and Fig. 6).
![img-1.jpeg](img-1.jpeg)

Fig. 2. Non-dominated solutions for the Concrete Compressive Strength dataset.

We also compare the algorithms based on the time (in seconds) and the number of evaluations of the regression model. For optimizing the execution time, we store the model's evaluation of different solutions aiming to evaluate only once time each different subset of features. Table 6 shows this comparison. It can be observed that in most cases, our implementation, EDA Bayesian Network, presented the best performance having less number of evaluations and the shortest time. In the case of the Communities Crime dataset, NSGA II was better in the

![img-2.jpeg](img-2.jpeg)

Fig. 3. Non-dominated solutions for the Forest Fires dataset.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Non-dominated solutions for the Student Performance Math dataset.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Non-dominated solutions for the Communities and crime dataset.
number of evaluations, and EDA Bernoulli was better in time. In the case of the Student Performance dataset, EDA Bernoulli was better in time. The number of evaluations can be seen as how much the search space is explored because it is related to the different solutions found. In some cases, when the objective function is expensive, we wanted good results with a few evaluations. In this experiment, our proposal proportionate good results with the smallest number of evaluations. It indicates that we can improve the exploration in future work and maybe get better results.

Table 6. Comparison of time and number of evaluations between algorithms for all datasets. Bold numbers correspond to the smallest values in time or number of evaluations.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Non-dominated solutions for the Year Predictions MSD dataset.

# 5 Conclusion 

This paper proposes an Estimation of Distribution Algorithm for feature selection tailored to regression problems with a multi-objective approach. The main objective was maximizing the learning models' performance, calculated as the determination coefficient $R^{2}$, and minimizing the number of selected features. Our proposal used a Bayesian Network (BN) as the distribution model. The BN aims to capture the redundancy among features. The generation of the initial population can be seen as a filter method that randomly creates solutions maximizing the relevance and minimizing the redundancy among features. The relevance and the redundancy were measured using the Pearson correlation coefficient.

We compared our proposal with other multi-objective algorithms such as EDA Bernoulli, NSGA II, and AGEMOEA, and we used five different datasets. According to the performance of the regression and the number of features of the non-dominated solutions found, all the algorithms obtain similar results in the two smallest datasets. On the medium dataset, our proposal found solutions with a less number of features. Finally, in the two biggest datasets, AGMOEA got better results in the regression model performance, but our proposal got considerably better results in the number of selected features. However, our proposal generally expended less time and evaluated fewer times the objective function. The experimental results indicate that it could be improved for exploring more the search space.

In future work, we expect to improve the exploration of our proposed algorithm. It obtains good results in the number of features but can improve the model's performance. We plan to extend the experiments by trying different regression models, and we can optimize the hyper-parameters values of the evolutionary algorithms.
