# Effect of Model Complexity for Estimation of Distribution Algorithm in NK Landscapes 

Rung-Tzuo Liaw and Chuan-Kang Ting<br>Department of Computer Science and Information Engineering and Advanced Institute of Manufacturing with High-tech Innovations<br>National Chung Cheng University<br>Chia-Yi 621, Taiwan<br>Email: \{lrt101p, ckting\}@cs.ccu.edu.tw


#### Abstract

Evolutionary algorithms (EAs) have been widely proved to be effective in solving complex problems. Estimation of distribution algorithm (EDA) is an emerging EA, which manipulates probability models instead of genes for evolution. EDA creates probability models based on the promising solutions in the population and generates offspring by sampling from these models. The model complexity is a key factor in the performance of EDA. Complex models can express the relations among variables more accurately than simple models. However, for some problems with strong interaction among variables, building a complex model for all the relations becomes unrealistic and impractical due to its high computational cost and requirement for a large population size. This study aims to understand the behaviors of EDAs with different model complexities in NK landscapes. Specifically, this study compares the solution quality and convergence speed of univariate marginal distribution algorithm (UMDA), bivariate marginal distribution algorithm (BMDA), and estimation of Bayesian network (EBNA) in the NK landscapes with different parameter settings. The comparative results reveal that high complexity does not imply high performance: Simple model such as UMDA and BMDA can outperform complex model like EBNA on the tested NK landscape problems. The results also show that BMDA achieves a stable high probability of generating the best solution and satisfactory solution quality; by contrast, the probability for EBNA drastically declines after some generations.

Index Terms-Estimation of distribution algorithm, model complexity, NK landscapes, probability model.


## I. InTRODUCTION

Evolutionary algorithms (EAs) have widely proved to be an effective way to resolve complex and large-scale problems. One of the most famous EAs is the genetic algorithm (GA) proposed by Holland in 1970's [1], which introduces the concept of nature selection from Darwin to evolve candidate solutions through selection and variation operators. GA has achieved a lot of successes on search and optimization problems [2]. Nevertheless, some problems are hard for GA since the fitness is involved with the interaction of several genes. These genes are viewed to be linked or form a building block. To deal with this issue, some approaches based on the concept of exploiting the information in the population are proposed. Estimation of distribution algorithm (EDA) is a famous family of these EAs. Algorithm 1 presents the general framework of EDA. Like most EAs, EDA is a stochastic, population based optimization method [3], [4], [5]; however, it differs from other EAs in several places. The major difference lies in the
variation operators: For example, GA performs crossover and mutation to generate new individuals, whereas EDA selects a set of promising solutions to build probability models and then generate new solutions from these models through sampling.

A variety of EDAs have been proposed. According to [4], EDAs can be classified by the graphical model. A graphical model consists of graph structure and local parameters. The graph structure indicates the inference relations among random variables, where each variable has a local parameter for its distribution. Depending on the graph structure, EDAs are classified into univariate model, bivariate model (also known as tree-based model), and multivariate model (see Fig. 1).

The univariate model is the simplest probability model utilized in EDAs. This model assumes that all random variables are mutually independent. The EDA of this class includes population based incremental learning (PBIL) [6], compact genetic algorithm (cGA) [7], and univariate marginal distribution algorithm (UMDA) [8]. For the univariate model, the joint probability density function of a solution in the search space can be represented by the following factorization of random variables.

$$
\mathcal{P}(\boldsymbol{x})=\prod_{i=1}^{n} \mathcal{P}\left(x_{i}\right)
$$

Beyond the assumption of mutual independence, the bivariate model considers conditional independence between random variables. The graph structure is then subject to the learning algorithm and may form a chain [9], a tree [10], or a forest [11]. Let $x_{p a(i)}$ denote the parent variable of random variable $x_{i}$. Equation (2) shows the factorization of conditional joint density function for solutions with bivariate model.

$$
\mathcal{P}(\boldsymbol{x})=\prod_{i=1}^{n} \mathcal{P}\left(x_{i} \mid x_{p a(i)}\right)
$$

The multivariate model is a more complex model in which the graph structure is often represented as directed acyclic graph (DAG). Some multivariate EDAs based on different learning methods for the graph structure or local parameters have been proposed, e.g., Bayesian optimization algorithm (BOA) [12], hierarchical Bayesian optimization algorithm (hBOA) [13], estimation of Bayesian network (EBNA) [14],

and estimation of Gaussian network (EGNA) [15]. Equation (3) gives the factorization of probability distribution for solutions with multivariate model, where $p a_{i}$ denotes the instantiation of $x_{i}$ 's parent set.

$$
\mathcal{P}(\boldsymbol{x})=\prod_{i=1}^{n} \mathcal{P}\left(x_{i} \mid p a_{i}\right)
$$

Complex graph structures are commonly believed to have a high ability of correctly describing the inference relations among variables and therefore to achieve good solution quality. However, Ceberio et al. [3] indicated that EDAs with complex model fail to outperform those with simple model on some permutation-based problems such as TSP, QAP, and LOP.

In this paper, we analyze the behavior of EDAs with different model complexities in NK landscapes. This study compares the solution quality and convergence speed of three EDAs. Furthermore, we investigate the probability of generating the known best solution. The remainder of this paper is organized as follows. Section II describes the NK landscape problem. Section III recapitulates the studies on model analysis of EDA and introduces the three adopted EDAs. Section IV presents the experimental results and discussion. Finally, in Section V we draw the conclusions and recommend some directions for future work.

## II. NK LANDSCAPES

In 1989, Kauffman and Weinberger [16] proposed the NK model and NK landscape problem. The NK model can be regarded as a system composed of $n$ parts, each of which corresponds to an element with several states and each part has interaction with other $k$ parts. This model provides a family of benchmarks that can be easily tuned by adjusting parameters $n$ and $k$, standing for the size and connectivity of the model respectively. In addition, the landscape of NK model with the same size $n$ is changed whenever the connectivity $k$ is changed. Restated, the connectivity $k$ determines the ruggedness of the landscape. For instance, the landscape becomes linear for $k=0$ and is most rugged for $k=n-1$.

The NK landscape problem is a real-valued optimization problem whose objective is to maximize the sum of evaluation results from each part in the NK model. The main objective function of the problem consists of $n$ sub-functions. The evaluation value of each sub-function is subject to the $k+1$ corresponding elements. Let $X$ and $x \in\{0, \ldots, p-1\}$ be a discrete random variable with $p$ possible values and its instantiation, respectively. Similarly, let $\boldsymbol{X}=\left(X_{1}, \ldots, X_{n}\right)$ denote a random vector and $\boldsymbol{x}$ stand for its instantiation. Given an NK model $\mathrm{NK}(n, k)$, where $n$ denotes the dimension and $0 \leq k \leq n-1$ represents the degree of connectivity, the problem can be formulated as an optimization problem

$$
\underset{\boldsymbol{x} \in \boldsymbol{X}}{\operatorname{argmax}} f(\boldsymbol{x})=\frac{1}{n} \sum_{i=1}^{n} f_{i}\left(x_{i}, \ldots, x_{i+k}\right)
$$

The value of each sub-function $f_{i}(\cdot)$ is predefined and generated according to an arbitrary distribution $L$; therefore, we

Algorithm 1 General framework of EDA
1 Population initialization
2 Evaluation
3 while (Termination criterion is not met) do
4 Selection from population
5 Update model using selected individuals
6 Sampling new individuals from model
7 Evaluation new individuals
8 Replacement
9 end while
![img-0.jpeg](img-0.jpeg)

Figure 1: Graphical structures of probability models used in EDAs.
need to sample $p^{k+1}$ values from $L$ to determine the evaluation of a sub-function for each state, where totally $n p^{k+1}$ values will be sampled. For simplicity of analysis, $\boldsymbol{X}$ is usually considered as a binary random vector and the distribution $L$ is a uniform distribution between 0 and 1 . In the experiments, we will use $p=2$ and $L=U[0,1)$, where the value corresponding to each state in each sub-function $f_{i}(\cdot)$ will be randomly sampled from $L$.

## III. Methodology

The probability model plays an important role in EDAs since all the new individuals are sampled from it. Several studies are focused on the analysis of probability model for EDAs. Echegoyen et al. [17] analyzed the limitation on estimation of Bayesian network (EBNA) through the additively decomposable functions ( ADFs ) and found that the required population size will increase exponentially with the degree of interactions among sub-functions. They also pointed out that the number of edges in the learned structure through EBNA will be bounded in a small range when the number of subfunction increases. Furthermore, Echegoyen et al. [18], [19] conducted a quantitative analysis to understand the internal behavior of EBNA by comparing the probabilities of sampling the optimum solution and the most probable solution (MPS) between success and failure trials. They utilized three different structures of Bayesian network, a learned structure, a given structure corresponding to the problem, and a tree-based structure, to observe the influence on the solution quality. The results show that reducing the information accuracy in the probability model leads to the decrease in the probability of

Algorithm 2 UMDA
$1 \quad D_{0} \leftarrow$ Random sampling
$2 \quad D_{0} \leftarrow$ Evaluation
$3 \quad t \leftarrow 0$
4 while (Termination criterion is not met) do
$5 \quad D_{t}^{s} \leftarrow \operatorname{Selection}\left(D_{t}\right)$
$6 \quad \mathcal{P}_{t}^{c}(\boldsymbol{X}) \leftarrow \operatorname{Update} \operatorname{model}\left(D_{t}^{s}\right)$
$7 \quad D_{t+1} \leftarrow \operatorname{Sampling}\left(\mathcal{P}_{t}^{c}(\boldsymbol{X})\right)$
$8 \quad D_{t+1} \leftarrow$ Evaluation
$9 \quad D_{t+1} \leftarrow \operatorname{Survival}\left(D_{t} \cup D_{t+1}\right)$
$10 \quad t \leftarrow t+1$
11 end while
generating the optimum solution. Lima et al. [20] investigated the model accuracy using the model structural accuracy (MSA) determined by the ratio between the number of correct edges to the total edges in the Bayesian network.

In this paper, we adopt the NK landscape problem to analyze the behavior of EDAs in terms of model complexity. Three EDAs with different graph structures are considered: univariate marginal distribution algorithm (UMDA) [8], bivariate marginal distribution algorithm (BMDA) [11], and estimation of Bayesian network algorithm (EBNA) [14], corresponding to the univariate model, bivariate model and multivariate model, respectively. More details about the three algorithms are given below.

## A. UMDA

The univariate marginal distribution algorithm (UMDA) is proposed by Mühlenbein and Paaß [8]. As aforementioned, UMDA assumes that random variables are mutually independent. Recapturing the factorization of joint probability density function in (1), the probability $\mathcal{P}_{t}\left(X_{i}=x_{i}\right)$ of each random variable at time $t$ is calculated by the frequency of $x_{i}$ in the position $i$ among the selected individuals, i.e.,

$$
\mathcal{P}_{t}\left(X_{i}=x_{i}\right)=\frac{N\left(X_{i}=x_{i}\right)}{\left|D_{t}^{s}\right|}
$$

where $D_{t}^{s}$ represents the set of selected individuals at time $t$ and function $N\left(X_{i}=x_{i}\right)$ gives the number of $x_{i}$ existing in $D_{t}^{s}$. Note that the situation $N\left(X_{i}=x_{i}\right)=0$, i.e., $x_{i}$ not existing in $D_{t}^{s}$, causes the probability $\mathcal{P}_{t}\left(X_{i}=x_{i}\right)=0$. Since new individuals are sampled from the probability model, such a zero probability in position $i$ will cause the loss of diversity and consequently the premature convergence. The Laplace correction [5] resolves this problem by adding one to the number of occurrences for each possible $x_{i}$ value. Hence,

$$
\mathcal{P}_{t}\left(X_{i}=x_{i}\right)=\frac{N\left(X_{i}=x_{i}\right)+1}{\left|D_{t}^{s}\right|+p}
$$

where $p$ is the number of possible values of $x_{i}$, e.g., $p=2$ for binary strings.

To balance the information accumulated from the past population to the current, a learning rate $\alpha$ is introduced to

Algorithm 3 Structure learning of BMDA
$1 \quad A \leftarrow V \leftarrow\{1, \ldots, n\}, E \leftarrow \phi$
$2 \quad R \leftarrow$ arbitrary node $i$ from $A$
$3 \quad A \leftarrow A \backslash i$
4 if $A=\phi$ then goto 9
5 if $\mathcal{X}_{i, j}^{2}<3.84 \forall i \in A$ and $\forall j \in V \backslash A$ then goto 2
$6 \quad i \leftarrow \underset{\text { argmax }}{\operatorname{argmax}} \mathcal{X}_{i, j}^{2} \forall i \in A$ and $\forall j \in V \backslash A$
$7 \quad E \leftarrow E \cup e(i, j)$
8 goto 3
9 End

## Algorithm 4 BMDA

$1 \quad D_{0} \leftarrow$ Random sampling
$2 \quad D_{0} \leftarrow$ Evaluation
$3 \quad t \leftarrow 0$
4 while (Termination criterion is not met) do
$5 \quad D_{t}^{s} \leftarrow \operatorname{Selection}\left(D_{t}\right)$
$6 \quad M \leftarrow$ Structure learning $\left(D_{t}^{s}\right)$
$7 \quad \mathcal{P}_{t}(\boldsymbol{X}) \leftarrow\left(M, D_{t}^{s}\right)$
$8 \quad O \leftarrow$ Ancestral order $(M)$
$9 \quad D_{t+1} \leftarrow \operatorname{Sampling}\left(O, \mathcal{P}_{t}(\boldsymbol{X})\right)$
$10 \quad D_{t+1} \leftarrow$ Evaluation
$11 \quad D_{t+1} \leftarrow \operatorname{Survival}\left(D_{t} \cup D_{t+1}\right)$
$12 \quad t \leftarrow t+1$
13 end while
the calculation of probability:

$$
\mathcal{P}_{t}^{c}\left(X_{i}=x_{i}\right)=\alpha \mathcal{P}_{t}\left(X_{i}=x_{i}\right)+(1-\alpha) \mathcal{P}_{t-1}^{c}\left(X_{i}=x_{i}\right)
$$

and $\mathcal{P}_{0}^{c}\left(X_{i}=x_{i}\right)=\mathcal{P}_{0}\left(X_{i}=x_{i}\right)$. In UMDA, the sampling order does not matter due to its assumption of mutual independence. Algorithm 2 presents the procedure of UMDA.

## B. BMDA

Bivariate marginal distribution algorithm (BMDA) is an EDA with bivariate model proposed by Pelikan and Mühlenbein [11]. Unlike UMDA, there are two stages in constructing the probability model in BMDA, including the graph structure learning and the conditional probability calculation. As mentioned in Section I, an arc $e(i, j)$ from node $i$ to node $j$ represents an inference relation between them. To establish the graph structure, BMDA checks the Pearson's chi-square statistics between different random variables, which express the independence of the two variables. Let $\mathcal{X}_{i, j}^{2}$ indicate the chi-square value of variables $i$ and $j$. Two variables are viewed as independent if $\mathcal{X}_{i, j}^{2}<3.84$ at $95 \%$ confidence level. Equation (4) shows the formula for calculating the Pearson's chi-square, where $\mathcal{P}\left(x_{i}\right)$ denotes the frequency of $X_{i}=x_{i}$ and $\mathcal{P}\left(x_{i}, x_{j}\right)$ stands for the frequency of $\left(X_{i}=x_{i}\right) \cap\left(X_{j}=x_{j}\right)$, both with Laplace correction as aforementioned.

$$
\mathcal{X}_{i, j}^{2}=\sum_{x_{i}, x_{j}} \frac{\left(\left|D_{t}^{s}\right| \mathcal{P}\left(x_{i}, x_{j}\right)-\left|D_{t}^{s}\right| \mathcal{P}\left(x_{i}\right) \mathcal{P}\left(x_{j}\right)\right)^{2}}{\left|D_{t}^{s}\right| \mathcal{P}\left(x_{i}\right) \mathcal{P}\left(x_{j}\right)}
$$


Algorithm 3 describes a greedy method for the dependency graph with maximal sum of chi-square. This method outputs a structure $E$ containing multiple trees and a node set $R$ containing the root nodes of each tree. After construction of graph structure, we need to calculate the frequency for sampling. For the root nodes, the calculation is the same as UMDA; as for other nodes, it needs to calculate the conditional probability. Further, BMDA uses the probabilistic logic sampling algorithm (PLS) [21] to find the ancestral order and sample new individuals depending on this order. For example, arc $e(i, j)$ represents that node $i$ precedes node $j$; therefore, the variable $X_{i}$ must be sampled before variable $X_{j}$. Algorithm 4 displays the procedure of BMDA.

## C. EBNA

Etxeberria and Larrañaga [14] proposed an EDA based on Bayesian network called estimation of Bayesian network algorithm (EBNA), which consists of a graph structure $M$ and local parameters $\theta_{i}$ for each random variable $X_{i}$. Like BMDA, EBNA needs to learn a graph structure and then calculate the local parameters $\theta_{i}$ for sampling. To learn the graph structure of Bayesian network, EBNA uses a metric called Bayesian information criterion (BIC):

$$
\begin{aligned}
\operatorname{BIC}\left(M, D_{t}^{\mathrm{s}}\right)= & \sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k} \log \frac{N_{i j k}+1}{N_{i j}+r_{i}} \\
& -\frac{\log N}{2} \sum_{i=1}^{n}\left(r_{i}-1\right) q_{i}
\end{aligned}
$$

where $q_{i}$ denotes the number of instantiations for the set of parents of random variable $X_{i}$ and $r_{i}$ denotes the number of instantiations of random variable $X_{i}$. Let $X(k)$ be the $k$-th instantiation of random variable $X$ and $p a_{i}(j)$ be the $j$-th instantiation of the set of parents of random variable $X_{i}$. The equations $X_{i}=X_{i}(k)$ and $P a_{i}=p a_{i}(j)$ mean that the random variable $X_{i}$ is in its $k$-th instantiation and the set of parents of random variable $X_{i}$ is in its $j$-th instantiation, respectively.

The first term in (5) represents the likelihood of the given structure $M$ according to the set of individuals $D_{t}^{\mathrm{s}}$ with

Table I: Parameter setting

Laplace correction, where $N_{i j k}$ indicates the number of individuals satisfying $X_{i}=X_{i}(k)$ and $P a_{i}=p a_{i}(j)$. The second term in (5) gives a penalty for complex models. The objective of structure learning is to maximize the BIC; thus, it needs to maximize the likelihood as well as minimize the penalty. In other words, the aim is to find a structure with maximum likelihood as simple as possible. However, to find a Bayesian network with maximum likelihood is an NP-complete problem. As a suggested in [14], we use the randomized hill climbing (HC) to build the graph structure $M$ from an arcless topology with one edge addition or deletion neighborhood function.

For sampling a new individual, we need to calculate the local parameters $\theta_{i j k}$ for all $j \in S_{P a_{i}}$ and $k \in S_{X_{i}}$ by

$$
\theta_{i j k}=\mathcal{P}\left(X_{i}=X_{i}(k) \mid P a_{i}=p a_{i}(j)\right)=\frac{N_{i j k}+1}{N_{i j}+r_{i}}
$$

where $S_{P a_{i}}$ is the collection of parent instantiations of random variable $X_{i}$ and $S_{X_{i}}$ is the set of all possible values of $X_{i}$. An individual can thus be sampled through the PLS determined by the graph structure $M$ and the local parameters $\theta_{i}$. Algorithm 5 shows the process of EBNA.

## IV. RESULTS

This study investigates the performance of EDAs on the NK landscape problems of $n \in\{10,30\}$ and $k \in\{2,6\}$. Table I lists the parameter setting for UMDA, BMDA and EBNA. To observe the influence of model complexity on the solution quality, we check three EBNA versions, to wit, $\mathrm{EBNA}_{2}, \mathrm{EBNA}_{4}, \mathrm{EBNA}_{6}$, which restrict the degrees of in and out order in the Bayesian network to 2,4 , and 6 , respectively. The maximal degree of order for the test EBNAs is set to 6 since Echegoyen et al. [17] indicated, as the number of sub-function increases, the maximum degree of order is within the range from 3 to 6 . To examine the behavior of each algorithm, we record the best known solution over all trials and trace the variation in the probability of generating the best solution [19]. All experiments are conducted on Intel core i7-920 machines with 30 trials.

Figure 2 shows the anytime behavior and the logarithm of probability of test EDAs on the NK landscape problems with fixed problem size $n=10$ and different $k$ values. The results indicate that, as $k$ increases, the convergence speed decreases for all the test EDAs; that is, EDAs generally require more generations if the interaction between variables is intensified. Additionally, UMDA and BMDA converge faster than EBNA

![img-1.jpeg](img-1.jpeg)

Figure 2: Anytime behavior (left column) and log probability of generating the best known solution (right column) of UMDA, BMDA, and EBNAs on the NK landscape problems with $n=10$.
does. The experimental results demonstrate that UMDA outperforms others in both solution quality and convergence speed for $k=2$, while BMDA does for $k=6$. According to the logarithm of probability, EBNAs with different degrees of order behave similarly. Furthermore, UMDA converges to the best known solution very fast for $k=2$, but suffers from premature convergence for $k=6$. BMDA achieves the best solution quality and the highest probability of sampling the best known solution for $k=6$.

This study further looks into the anytime behavior of the test EDAs on the NK landscape problems with a larger problem size $n=30$. Since the problem size is associated with the number of sub-functions, a larger problem size brings about a harder problem. According to Fig. 3, UMDA performs well for $k=2$ but fails to find the best known solution for $k=6$ due to premature convergence. By contrast, BMDA converges slowly for $k=2$ and yet outperforms others for $k=6$. For the EBNAs with different orders, there is no significant difference in solution quality and convergence speed. As $k$
increases, EBNAs converge very slowly in comparison with the UMDA and BMDA. In view of the logarithmic probability of sampling the best known solution, the low probability of UMDA corresponds to its poor solution quality, which implies the vulnerability of UMDA to local optima. On the other hand, BMDA achieves a stable high probability and satisfactory solution quality. Compared to the stable probabilities of UMDA and BMDA, the probability for EBNAs varies with the number of generations; in particular, the probability drastically declines after some generations.

Next, we examine the statistical significance using the Kruskal-Wallis test, a non-parametric analysis of variance suggested by García et al. [22]. All statistical analyses are under significance level $\alpha=0.05$. Tables II and III summarize the statistical results, where the label Chi-square denotes the Chi-square statistics in the Kruskal-Wallis test and the term $\operatorname{Pr}>$ Chi-square indicates a significance difference among all test methods if the value is smaller than $\alpha$. The results exhibit that there is no significant difference among the test

![img-2.jpeg](img-2.jpeg)

Figure 3: Anytime behavior (left column) and log probability of generating the best known solution (right column) of UMDA, BMDA, and EBNAs on the NK landscape problems with $n=30$.

EDAs for small $n$ and $k$. However, as $n$ or $k$ increases, the significance emerges: BMDA outperforms other methods on the problems with large size or high connectivity (e.g. $\mathrm{NK}(10,6)$ and $\mathrm{NK}(30,6)$ ). Similar to the results of anytime behavior, the three EBNAs have insignificant difference in the solution quality. This outcome reveals that EBNA is insensitive to the order of degrees for the graphical structure in terms of solution quality.

According to the above results on the NK landscape problems, EDAs with low model complexity like UMDA render good optimizers for simple small problem, namely, smaller problem size and low interaction between variables. Nonetheless, for more complex problems, such EDAs may suffer from premature convergence. BMDA, on the other hand, can nicely resolve the complex problems (large size and strong interaction) in terms of solution quality and convergence speed. Surprisingly, EDAs with even higher model complexity like EBNA may not perform satisfactorily on the complex problems, as shown in our experiments. Additionally, EBNAs
converge slower than UMDA and BMDA. In general, it shows that a simple model is not necessarily worse than a complex one for EDAs: The bivariate model outperforms the univariate and multivariate models in both solution quality and convergence speed on the NK landscape problem.

## V. CONCLUSIONS

The model complexity is a key factor in the performance of EDA. Complex models can express the relations among variables more accurately than simple models. However, for some problems with strong interaction among variables, building a complex model for all the relations becomes unrealistic and impractical due to its high computational cost and requirement for large population size. In this study, we take the EDAs based on three different models, namely, univariate, bivariate and multivariate models, to observe their behaviors in terms of solution quality and convergence speed in NK landscapes. This study further tracks the variation in the logarithmic probability of generating the best known solution to examine

Table II: Kruskal-Wallis non-parametric analysis of variance with multiple comparison post-hoc analysis for the NK landscape problems with $n=10$ and $k \in\{2,6\}$. All methods are tested under 30 trials and the significance level $\alpha=0.05$.
(a) $k=2$


(a) $k=2$


(b) $k=6$

Table III: Kruskal-Wallis non-parametric analysis of variance with multiple comparison post-hoc analysis for NK landscapes problems with $n=30$ and $k \in\{2,6\}$. All methods are tested under 30 trials and the significance level $\alpha=0.05$.
(a) $k=2$

(b) $k=6$

the convergence of the probability model. For comparing the solution quality among EDAs, we adopt the Kruskal-Wallis non-parametric analysis of variance to evaluate the statistical significance.

On the NK landscapes problem with low interaction and small problem size, we found that UMDA can perform well in solution quality and convergence speed. As the problem complexity increases, UMDA suffers from premature convergence and gets stuck on local optima. Meanwhile, BMDA and EBNA can solve more complex problems; in particular, the former can converge much faster than the latter. Additionally, BMDA outperforms other methods on the problems with large size or high connectivity. In general, the study reveals that a simple model is not necessarily worse than a complex one for EDAs on the NK landscape problem. Furthermore, we adopted different degrees of order in the Bayesian network to observe the influence of model complexity. The results show that the three EBNAs have insignificant difference in the solution quality. That is, EBNAs are insensitive to the order of graphical model. This outcome infers that a simple graphical model is good enough for EBNA to tackle the NK landscape problem.

Some directions remain for future work. First, other problems or larger instance size should be further considered in performance comparison. Second, our study compares three EDAs: UMDA, BMDA and EBNA. More EDAs and other models can be applied in the comparison. In addition, our work suggests that a simple model is not necessarily worse than a complex one. Given that efficiency is an important issue in the design of algorithms, combination of simple models is a promise alternative to a single complex model used in EDA.

## ACKNOWLEDGMENT

This study was supported by the Ministry of Education, Taiwan.
