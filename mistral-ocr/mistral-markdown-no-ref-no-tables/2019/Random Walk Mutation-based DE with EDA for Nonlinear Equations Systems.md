# Random Walk Mutation-based DE with EDA for Nonlinear Equations Systems 

Zuowen Liao<br>School of Computer Science,<br>China University of Geosciences,<br>Wuhan 430074, China<br>Wenyin Gong<br>School of Computer Science, China University of Geosciences, Wuhan 430074, China<br>wygong@cug.edu.cn<br>Zhihua Cai<br>School of Computer Science, China University of Geosciences, Wuhan 430074, China<br>Ling Wang<br>Department of Automation,<br>Tsinghua University,<br>Beijing 100084, China<br>Yong Wang<br>School of Information Science and Engineering, Central South University, Changsha 410083, China


#### Abstract

Finding multiple roots of nonlinear equations systems (NESs) in a single run is an important yet difficult task. It requires to keep a balance between explorative and exploitative traits. In this paper, we present a random walk mutation-based differential evolution (DE) with estimation of distribution algorithm (EDA) to address this problem. The major characteristics are: i) the random walk mutation is capable of preserving the population diversity, which guides individuals to move toward different promising regions; ii) probability selection is employed to provide suitable parent individuals for evolution; iii) EDA is used to accelerate the convergence and obtains the roots. To evaluate the performance of our approach, 30 NESs with diverse features are selected as test suite. Experimental results indicate that the proposed approach is able to yield better performance compared with other state-of-the-art methods.


Index Terms-Nonlinear equations systems, random walk mutation, differential evolution, estimation of distribution algorithm.

## I. INTRODUCTION

Nonlinear equations systems (NESs) contain multiple roots and arise in many real-world applications, such as economics [1], physics systems [2], engineering [3]. In practical applications, multiple roots are equally important because they represent a great deal of information and a decision maker can make a final decision by using them [4]. Locating multiple roots of NESs remains a challenging work in numerical computation, especially to find them in a single run.

Niching methods, also named as "multi-solution" methods, have been designed to locate multiple solutions of multimodal optimization (MMO) problems [5]. Classic niching methods include crowding [6], speciation [7] , fitness sharing [8], clearing [9], and clustering [10]. They have been integrated into evolutionary algorithms (EAs) to modify the behavior of EAs such that preserve the population diversity and detect multiple optima.

This work was partly supported by the National Natural Science Foundation of China under Grant Nos. 61573324, and 61673554, , in part by the National Natural Science Fund for Distinguished Young Scholars of China under Grant 61525304. (Corresponding author: Wenyin Gong.)

A random walk mutation strategy was proposed to deal with multi-modal optimization problems in [11] and achieved appealing performance. This strategy simulates the random walk process to select the parent vectors, which utilized to generate offspring for preserving the population diversity during the run. However, random walk mutation suffers from the issue of low-quality root if directly using it to solve NESs.

Estimation of distribution algorithms (EDAs) are a branch of EAs. In EDA, the technique of probability distribution estimated is applied to generate offspring from the excellent individuals of previous generations. Although EDAs have been used to deal with many optimization problems [12], most of them are designed only for locating one root.

Based on the above considerations, a random walk mutation-based differential evolution (DE) with EDA, referred to as RWDE-EDA, was proposed to locate multiple roots of NESs in one run. Especially, the main characteristics of RWDE-EDA are listed as follows:

- Random walk mutation strategy is able to maintain the diversity of the population. This strategy imitates the random walk process to select the individual $\left(\mathbf{x}_{<1}, \mathbf{x}_{<2}\right.$ and $\left.\mathbf{x}_{<3}\right)$ to generate offspring. The random walk mutation enables the individual to evolve toward its nearby optima. Thus, the promising regions in the search space can be detected.
- Probability selection is adopted to select parent individuals during the run. In this way, more suitable parent individuals will have a higher probability of being selected for next evolution.
- In our approach, EDA is regraded as a local search methods to find the exact roots in the promising regions. EDA can improve the quality of the solution by generating offspring near the optimal solution according to the Gaussian distribution and continuously evolving towards the direction of the solution.
The rest of the paper is organized as follows. Section II

briefly introduces the general approaches for solving NESs. Section III gives a detailed description of our approach. Experiment and statistical results are presented in Section IV. Finally, the conclusion is given in Section V.

## II. Related Work

This section briefly introduces the NES problem and the related work for solving the NESs with evolutionary algorithms.

## A. Problem Statement

Without loss of generality, a NES is described as:

$$
\mathbf{F}(\mathbf{x})= \begin{cases}e_{1}\left(x_{1}, \ldots, x_{D}\right)=0 \\ \vdots \\ e_{n}\left(x_{1}, \ldots, x_{D}\right)=0\end{cases}
$$

where $n$ is number of equations, $\mathbf{x}=\left(x_{1}, \ldots, x_{D}\right)$ represents a $D$-dimensional decision vector, $\mathbf{x} \in \mathbb{S}$, and $\mathbb{S} \subseteq \mathbb{R}^{D}$ is the search space. Generally,

$$
\mathbb{S}=\left[\underline{x}_{j}, \bar{x}_{j}\right]^{m}
$$

where $j=1, \cdots, D, \underline{x}_{j}$ and $\bar{x}_{j}$ are the lower bound and upper bound of $x_{j}$, respectively.

Generally, a NES is transformed into a minimization problem before to solve :

$$
\text { minimize } \quad \mathbf{F}(\mathbf{x})=\sum_{i=1}^{n} e_{i}^{q}(\mathbf{x})
$$

Subsequently, the goal of solving a NES is equivalent to find the global minimizers of Equation (2).

## B. Related Work for NESs

Recently, a great deal of algorithms have been presented to locate multiple roots of NESs in a single run, which can be categorized into three cases:

- Multiobjective optimization-based approaches: Locating a set of Pareto optimal solutions is the major work of multiobjective optimization problem [13], which is similar to find numerous roots of NESs. Before solving NESs, they are usually transformed into multiobjective optimization problems and handled by multiobjective algorithms. In [14], a NES was transformed into n-objective optimization problem. Wang et al. [15] proposed a biobjective transformation technique (MONES) for NESs. Gong et al. [16] extended the work of MONES and presented the weighted bi-objective transformation tehnique (A-WeB) for locating multiple roots of NESs.
- Repulsion-based approaches: The repulsion techniques have the ability to guide individuals toward different promising regions and achieve numerous different roots. Recently, some approaches based on repulsion techniques were developed to solve NESs, such as C-GRASP [17], harmony search algorithm [18], and Nelder-Mead [19]. Moreover, Gong et al. [20] proposed a RADE, which employs the repulsive technique, niching mutation and the
![img-0.jpeg](img-0.jpeg)

Fig. 1. The process of random walk mutation
adaptive parameter setting to solve NESs so that it obtains competitive performance. Very recently, Liao et al. [21] extended this work and designed dynamic repulsive radius technique for NESs.

- Clustering-based approaches: The clustering techniques are mainly utilized to split the whole population into different clusters in which the similar individuals are gathered together. In [22], the clustering technique was adopted to locate the exact root. Additionally, The clusteringbased Minfider was proposed to deal with NESs in [22]. Sacco et al. [23] designed the fuzzy clustering means to find multiple roots of NESs.


## III. Our APPROACH

In this section, our proposed method will be descried in detail.

## A. Random Walk Mutation

In the standard DE, trial vector is generated by parent individuals based on randomly selecting from the same population. If the parent individuals are far from one another, the difference vector will become very large. It avoids trapped in local optima and improves the probability of finding global optima. Although such a mechanism is beneficial to find a global optima, it is difficult in finding multiple roots. To overcome the shortcoming, paper [11] proposed a random walk mutation to locate global and local optima of multimodal problems. The process of selecting parent individuals is considered as a random walk.

Fig 1 demonstrates the process of random walk mutation. Next, we briefly introduce how to choose parent individuals in the evolution process. At the beginning stages, $\mathbf{x}_{i}$ is the initial vector, the vector $\mathbf{x}_{k 1}$ is chosen from $\mathbf{x}_{i}$ 's $n 1$ nearest neighbors, where $n 1$ is a random integer between $5 \% N P$ and $25 \% N P$. Each neighbor $\mathbf{y}_{i, j}(j \in[1, n 1])$ of $\mathbf{x}_{i}$ is given a selection probability, which is calculated as:

$$
p_{i, j}=\frac{o f i t\left(\mathbf{y}_{i, j}\right)}{\sum_{m=1}^{k 1} o f i t\left(\mathbf{y}_{i, m}\right)}
$$

where $\operatorname{ofit}\left(\mathbf{y}_{i, j}\right)$ is the modified fitness. Different from the formula proposed in [11], in this paper, the formula of $\operatorname{ofit}\left(\mathbf{y}_{i, j}\right)$ is slightly modified for NESs problems. It is computed as:

$$
\operatorname{ofit}\left(\mathbf{y}_{i, j}\right)=1-\frac{f\left(\mathbf{y}_{i, j}\right)}{\sum_{m=1}^{k} f\left(\mathbf{y}_{i, m}\right)}
$$

In (4), $f\left(\mathbf{y}_{i, j}\right)$ is the fitness value of $\mathbf{y}_{i, j}$, which is computed by the Equation (2). $\mathbf{x}_{k 1}$ is chosen utilizing a roulette wheel according to the probabilities. By analogy, $\mathbf{x}_{k 2}$ is chosen from $\mathbf{x}_{k 1}$ 's $n 2$ nearest neighbors and $\mathbf{x}_{k 3}$ is chosen from from $\mathbf{x}_{k 2}$ 's $n 3$ nearest neighbors. $n 2$ and $n 3$ are two random integers within $[5 \% N P, 25 \% N P]$.

Parent individuals selected according to the process of random walk have fully used the information including fitness value and neighborhood. At the initial stages, all individuals are randomly distributed in decision space, the offspring generated by the random walk mutation is able to explore different areas, and hence population diversity can be preserved. Subsequently, the offsprings will move toward promising areas with the increase of iterations and individuals with similar characteristics gradually gather in the same region. In the later search process, individuals will converge to different promising regions, which is beneficial to exploit the candidate regions.

## B. Estimation of Distribution Algorithms

EDAs are a branch of EAs, which have proven serviceable in multimodal optimization and demonstrated favorable results [24]. In [25], the author proposed a local search strategy according to Gaussian distribution to improve the quality of the found root. This scheme can refine the individuals that meet certain conditions, such as fitness value is less than a fixed threshold. It is similar to the local search method that accelerates convergence speed. Generally, a new individual generation is computed as:

$$
\mathbf{x}_{i}=\operatorname{Gaussian}\left(\mathbf{u}_{i}, \delta\right)
$$

where $\mathbf{x}_{i}, \mathbf{u}_{i}$, and $\delta$ represent a new individual, parent individual, and standard deviation, respectively. $\delta$ is a critical parameter to determine whether EDA is prone to explore or exploit. When $\delta$ is small, Gaussian distribution owns a narrow sample space, which is beneficial for the exploitation of EDA. In this paper, $\delta$ is set to 0.01 .

In Algorithm 1, EDA is mainly used to refine the individual and improve the quality of root. $N F E$ is current number of function evaluation; $N F E_{\text {smax }}$ is the maximum fitness evaluation number. The experiment in section IV-F will illustrate the influence of solving NESs by employing different $\delta$.

## C. Motivation

The target of solving NESs is to find multiple roots simultaneously in one run. Thus, the requirement of maintaining diversity population is essential. In [11], a random walk mutation has been proposed to deal with multimodal optimization problems and locate multiple global and local optima.

Algorithm 1: The framework of modified EDA
Input: Control parameters: $N P, N F E, N F E s_{\max }$
Output: the whole individual
1 while $N F E<N F E s_{\max }$ do
2 Select a individual $\mathbf{u}_{i}$ satisfied condition from the population;
3 Generate new individuals $\mathbf{x}_{i}$ via (5);
4 if $f\left(\mathbf{x}_{i}\right)<f\left(\mathbf{u}_{i}\right)$ then
$\mathbf{u}_{i}=\mathbf{x}_{i}$
5
6
7 if $f\left(\mathbf{u}_{i}\right)<\epsilon$ then
8 End of the loop;
$N F E=N F E+1 ;$
Algorithm 2: The framework of RWDE-EDA
Input: Control parameters: $N P, N F E, N F E s_{\max }$
Output: The whole population
1 Set $N F E=0$;
2 Randomly initial the population $\left\{\mathbf{u}_{1}, \cdots, \mathbf{u}_{N P}\right\}$;
3 Calculate the fitness value of $u$ via Equation (2);
4 $N F E=N F E+N P$;
5 while $N F E<N F E s_{\max }$ do
6 for $i=1$ to $N P$ do
7 Generate the offspring $\mathbf{v}_{i}$ using random walk mutation;
8 Evaluate the fitness value of the trial vector $\mathbf{v}_{i}$;
9
10
11 if $f\left(\mathbf{v}_{i}\right)<f\left(\mathbf{u}_{i}\right)$ then
$\mathbf{u}_{i}=\mathbf{v}_{i}$
if $f\left(\mathbf{u}_{i}\right)<\eta$ then
12 Generate the offspring via Algorithm 1;
$N F E=N F E+1 ;$

However, it may suffer from the problem of obtaining low quality roots due to the preservation of population diversity.

In recent year, most EDAs have been modified to locate global and local optima of the multimodal optimization problem. However, few papers focus on locating the roots of NESs with EDA.

Based on the above considerations, in this paper, we propose a random walk mutation-based DE with EDA (RWDE-EDA) to solve NESs. On one hand, random walk mutation is able to maintain population diversity and improve the probability of finding multiple roots. On the other hand, EDA based on Gaussian distribution generates the individual around the optima and improve the exploitation ability to find the exact roots.

## D. Proposed Approach

In order to find numerous roots in one run simultaneously, in this work, we propose the combination between random walk mutation-based on DE and EDA to solve NESs. The reasons could be two-fold: i) random walk mutation guides the individuals toward different promising regions, which can preserve the population diversity; ii) EDA increases the exploitation ability and improve the quality of root.

The detailed steps of our proposed RWDE-EDA is demonstrated in Algorithm 2, it works as follows:

- In line 7, random walk mutation can maintain the population diversity; Based on this mutation, the algorithm can detect different promising regions and improve the probability to find multiple roots.
- Once the fitness value of $\mathbf{u}_{i}$ is less than $\eta$, the program of EDA is triggered to generate the offspring $\mathbf{x}_{i}$. If the fitness value is less than $\epsilon, \mathbf{x}_{i}$ is referred to as a candidate solution.


## IV. EXPERIMENTAL RESULTS AND ANALYSIS

In this section, we carry out experiments to verify the performance of RWDE-EDA in this paper. Additionally, our approach is compared with some state-of-the-art approaches for solving NESs to illustrate its performance. Moreover, the impact of different parameter setting is also discuss herein.

## A. Test Problems

To investigate the effectiveness of different methods, 30 NES instances with different characteristics are chosen from [20]. Table I mainly illustrates the features of distinct NES instances. It is worth highlighting that different test instances may have different $N F E s_{\max }$ due to their own different features.

TABLE I
BRIEF INTRODUCTION OF THE TEST INSTANCES UTILIZED IN THIS PAPER, WHERE " $D$ " IS THE NUMBER OF DECTION VARIABLES; " $L E$ " AND " $N E$ " ARE RESPECTIVELY THE NUMBER OF LINEAR AND NONLINEAR EQUATIONS; " $N o R$ " IS THE NUMBER OF ROOTS; AND " $N F E s_{\max }$ " IS THE MAXIMAL NUMBER OF FUNCTION EVALUATIONS.


## B. Performance Measure

In order to evaluate the performance of different approaches for NESs, in this paper, two prevailing performance criteria in [20] are utilized, i.e., root ratio $(R R)$ and success rate $(S R)$. $R R$ is the percentage of detected the roots that satisfy certain condition, for example, its fitness value is less than $\epsilon$. And $S R$ is the ratio of successful run ${ }^{1}$ within multiple runs. To make sure whether the root identified or not, an accuracy level $\epsilon$ is needed to be specified. In this paper, $\epsilon=1 e-05, \delta=0.01$ and $\eta=0.05$. Moreover, each approach is conducted over 30 independent runs for fair comparison.

To obtain the statistical results among distinct methods, KEEL [26] is selected to conduct the multiple problem Wilcoxon' test and the Friedman's test, $p<0.05$ demonstrates that there is a significant difference between the two compared methods.

## C. Comparison Different Random Walk based DE Variants

In this subsection, three random walk mutation based DE (RWDE) variants, such as RWDE with random selection (RWDE-RS), RWDE with probability selection (RWDE-PS) and RWDE with estimation of distribution algorithm (RWDEEDA) are selected to verify the performance for solving NESs. The main difference of three approaches is detailed as follow:

- RWDE-RS denotes that the parent individuals are selected randomly from a set of individuals which close to the current individual. From Fig 1, n1 individuals based on minimal distance to $x_{i}$ are chose. Subsequently, $x_{k 1}$ is determined by randomly selecting from n 1 individuals. $x_{k 2}$ and $x_{k 3}$ are selected in the same way.
- Different from RWDE-RS, RWDE-PS determines the parent individuals by probability selection which is introduce in Section III.
- RWDE-EDA is a hybrid approach that combines random walk mutation, probability selection and estimation of distribution algorithm together to find multiple roots of NESs.

To depict the evolution of three RWDE variants mentioned above, the third test problem F03 is selected as an instance. All parameter settings obtain from Table I, such as $N F E s_{\max }=$ 50,000 . F03 includes two decision variables and contains 15 different roots. The same initial population is used for fair comparison.

Fig 2-Fig 4 show the evolution of three RWDE variants over a typical run on F03. From Fig 2-Fig 4, we can observe that:

- Random walk mutation has capability of preserving population diversity. From Fig 2-Fig 4, the same initial population is randomly distributed before evolution. Subsequently, individuals gradually search toward different promising regions according to random walk mutation. At the end of evolution, the individuals respectively converge to different promising regions. Such phenomenon demonstrates that random walk mutation is an effective method for maintaining diversity population.
${ }^{1}$ A successful run is that all known roots of a NES are found.

![img-3.jpeg](img-3.jpeg)

Fig. 2. Evolution of RWDE-RS over a typical run on F03. Circle denote the individuals in the population, and diamonds denote the known roots, and pentagrams denote the obtained roots (the same below).
![img-3.jpeg](img-3.jpeg)

Fig. 3. Evolution of RWDE-PS over a typical run on F03. Circle denote the individuals in the population, and diamonds denote the known roots, and pentagrams denote the obtained roots (the same below).
![img-3.jpeg](img-3.jpeg)

Fig. 4. Evolution of RWDE-EDA over a typical run on F03. Circle denote the individuals in the population, and diamonds denote the problem roots (the same below).

- RWDE-RS adopts random selection to choose parent individuals while the probability selection is used in RWDE-PS. RWDE-PS can improve the search ability of algorithm by using neighborhood and fitness information. From Fig 2, It can be seen clearly that RWDE-RS at iter $=500$ obtains 13 roots in the end of evolution but RWDE-PS yields 14 roots from Fig 3. Thus, probability selection is superior to a random selection in RWDE for solving NESs.
- From Fig 4, RWDE-EDA succeeds in obtaining all the roots of NESs at $i t e r=500$. The success is mainly attributed to the fact that: 1) the diversity population can be maintained due to random walk mutation; 2) probability selection is able to provide suitable parent individuals to generate the offsprings; 3) EDA is integrated into RWDE for enhancing the quality of roots.
The multiple-problem Wilcoxon's test result reports in Table II. From Table II, it shows that RWDE-EDA obtains better result than RWDE-RS and RWDE-PS since RWDE-EDA
yields the higher $R^{+}$than $R^{-}$value in all cases. Additionally, the Friedman's test result demonstrates in Table III, which shows that RWDE-EDA achieves the best ranking. One should take care to note that RWDE-PS achieves the better result than RWDE-RS due to probability selection.

From Algorithm 2, random walk mutation is used in the earlier phases to explore different promising regions. $x_{k 1}, x_{k 2}$, and $x_{k 3}$ are selected according to the probability selection. The difference vector may be large and the algorithm is able to increase the probability of searching various regions. In what follows, the similar individuals gradually collect in the same region due to the fact that difference vectors become small with the increase of iteration. Once the fitness value of individual is less than $\eta$, EDA is conducted to further refine the individual. The statistical results have demonstrated that utilizing RWDE-EDA can be advantageous for locating multiple roots.

TABLE II
REAULTS ORAINED BY THE WILCUSION TEST IN TERMS OF $R R$ AND $S R$ BETWEEN THE DIFFERENT RANDOM WALK BASED DE VARIANTS.

TABLE III
AVERAGE RANKINGS OF RWDE-EDA, RWDE-RS, AND RWDE-PS OPTAINED BY THE FRIEDMAN TEST FOR BOTH $R R$ AND $S R$.

## D. Comparison with Other Methods for NESs

In this subsection, four state-of-the-art methods, MONES [15], NCDE [27], DR-JADE [21], and RADE [20] are chose to compare with RWDE-EDA for evaluating the performance of solving NESs.

MONES is a multiobjective optimization based methods for solving NESs. NCDE is proposed to deal with multimodal problems. DR-JADE handles repulsion radius setting problem and adopts a dynamic repulsion radius to detect multiple roots. RADE locates different roots of NESs by the combination of the repulsive technique, adaptive parameter control and the neighborhood mutation, which also achieved appealing results in the experiment. The parameter settings of compared methods are shown in Table V. All the parameter settings were kept the same in our experiments unless a change was mentioned.

The average $S R$ and $R R$ values of the compared methods are showed in Table IV. From Table IV, RWDE-EDA obtain the highest average $S R$ value, i.e., 0.86 and the highest average $R R$ value, i.e., 0.97 . The statistical results of the Wilcoxon test and the Friedman test are reported in Table VI and VII, respectively. From Table VI, it is shown that RWDEEDA obtains significantly better results than MONES, NCDE since all $p-$ values are less than 0.05 . And it also provides slight better results than RADE and DR-JADE. In addition, RWDE-EDA yields the best ranking among the five methods in Table VII. As a consequence, RWDE-EDA is an effective alternative to solve NESs.

TABLE V
PARAMETER SETTINGS FOR DIFFERENT METHODS. NOTE THAT ALL OTHER PARAMETERS UNED IN DIFFERENT METHODS ARE KEPT THE SAME AS USED IN THEIR ORIGINAL LITERATURE.

TABLE VI
REAULTS ORAINED BY THE WILCUSION TEST IN TERMS OF $R R$ AND $S R$ FOR DIFFERENT METHODS .

TABLE VII
AVERAGE RANKINGS OF DIFFERENT METHODS OPTAINED BY THE FRIEDMAN TEST FOR BOTH $R R$ AND $S R$.

## E. Influence of $\eta$

In RWDE-EDA, the value of parameter $\eta$ determines whether EDA is used to generate a new individual. If $\eta$ is small, the individual is close to optima, and vice versa. In this subsection, different $\eta$ are set to discuss the effect of our approach, such as $\eta=$ $\{0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09\}$. The statistical result of the Friedman test is showed in Table VIII.

From Table VIII, $\eta=0.05$ obtains the best average ranking in terms of $R R$ and $S R$. It means that our approach obtains the significant results by using EDA for exploitation in $\eta=0.05$. Moreover, $\eta \in[0.05,0.06]$ is a suggestion value in RWDEEDA for solving NESs. If $\eta$ too small, the convergence speed is not guaranteed due to the absence of EDA. Conversely, large $\eta$ leads to generate individual which is far from the optima via EDA.

TABLE VIII
AVERAGE RANKINGS OF DIFFERENT $\eta$ BY THE FRIEDMAN TEST FOR BOTH $R R$ AND $S R$.

## F. Effect of $\delta$

Parameter $\delta$ determines the sample space of Gaussian distribution. Different $\delta$ values represent different search ability of EDA. For example, large $\delta$ is conducive to keeping a wide sample space and enhancing the exploration ability. In contrast, EDA focuses on exploitation. In this paper, the main role of EDA is to accelerate the convergence speed and yield the high-quality roots. Thus, we need to discuss

TABLE IV
COMPARISON BETWEEN RWDE-EDA AND OTHER STATE-OF-THE-ART METHODS WITH RESPECT TO $S R$ AND $R R$.


the impact of different $\delta$ values on our approach, such as $\eta=\{0.1,0.01,0.001,0.0001\}$.

The result of average ranking by Friedman test is outlined in Table IX. If $\delta=0.1$, generated individual may be far from the potential root, which decreases the exploitation ability. On the contrary, EDA is prone to trap into local optima due to the small $\delta$ value, such as $\delta=0.0001$. From Table IX, $\delta=0.001$ is a reasonable value since it obtains the best average ranking.

TABLE IX
AVERAGE RANKINGS OF DIFFERENT $\eta$ BY THE FRIEDMAN TEST FOR BOTH $R R$ AND $S R$.


## V. CONCLUSIONS

In this paper, random walk mutation based-DE with EDA is proposed to handle NESs. Random walk mutation is able to preserve population diversity while EDA can obtain satisfactory solution in different promising regions. The proposed approach has capability of the balance of exploration and exploitation. In order to evaluate the performance of our approach, we select

30 different NESs as the test suite. Experiments illustrate that RWDE-EDA obtains the significant performance in solving NESs. Additionally, compared with state-of-the-art methods for solving NESs, RWDE-EDA also yields competitive performance. Therefore, the proposed algorithm is an effective alternative for NESs.
