# Multisource Selective Transfer Framework in Multiobjective Optimization Problems 

Jun Zhang ${ }^{\oplus}$, Weien Zhou, Xianqi Chen, Wen Yao, and Lu Cao


#### Abstract

For complex system design [e.g., satellite layout optimization design (SLOD)] in practical engineering, when launching a new optimization instance with another parameter configuration from the intuition of designers, it is always executed from scratch which wastes much time to repeat the similar search process. Inspired by transfer learning which can reuse past experiences to solve relevant tasks, many researchers pay more attention to explore how to learn from past optimization instances to accelerate the target one. In real-world applications, there have been numerous similar source instances stored in the database. The primary question is how to measure the transferability from numerous sources to avoid the notorious negative transferring. To obtain the relatedness between source and target instance, we develop an optimization instance representation method named centroid distribution, which is by the aid of the probabilistic model learned by elite candidate solutions in estimation of distribution algorithm (EDA) during the evolutionary process. Wasserstein distance is employed to evaluate the similarity between the centroid distributions of different optimization instances, based on which, we present a novel framework called multisource selective transfer optimization with three strategies to select sources reasonably. To choose the suitable strategy, four selection suggestions are summarized according to the similarity between the source and target centroid distribution. The framework is beneficial to choose the most suitable sources, which could improve the search efficiency in solving multiobjective optimization problems. To evaluate the effectiveness of the proposed framework and selection suggestions, we conduct two experiments: 1) comprehensive empirical studies on complex multiobjective optimization problem benchmarks and 2) a real-world SLOD problem. Suggestions for strategy selection coincide with the experiment results, based on which, we propose a mixed strategy to deal with the negative transfer in the experiments successfully. The results demonstrate that our proposed framework achieves competitive performance on most of the benchmark problems in convergence speed and hypervolume values and performs best on the real-world applications among all the comparison algorithms.


Manuscript received October 22, 2018; revised February 2, 2019, April 16, 2019, and June 24, 2019; accepted June 27, 2019. Date of publication July 1, 2019; date of current version May 29, 2020. This work was supported by the National Natural Science Foundation of China under Grant 11725211 and Grant 51675525. (Corresponding author: Wen Yao.)
J. Zhang is with the National Innovation Institute of Defense Technology, Chinese Academy of Military Science, Beijing 100071, China, and also with the Department of Computer Science and Technology, Tsinghua University, Beijing 100084, China (e-mail: mcgrady150318@163.com).
W. Zhou, W. Yao, and L. Cao are with the National Innovation Institute of Defense Technology, Chinese Academy of Military Science, Beijing 100071, China (e-mail: wendy0782@126.com).
X. Chen is with the National University of Defense Technology, Changsha 410072, China.

Color versions of one or more of the figures in this paper are available online at http://eeeexplore.ieee.org.
Digital Object Identifier 10.1109/TEVC.2019.2926107

Index Terms—Estimation of distribution algorithm (EDA), multiobjective optimization, multisource transfer, transfer optimization, Wasserstein distance (WD).

## I. INTRODUCTION

$\mathbf{E}$OR COMPLEX system design problems in practical engineering, taking satellite system design for example, there are plenty of past experiences such as the different design of satellite layout solutions have been stored in the database before launching a new design. Exploiting past experiences are not only enhance optimization effectiveness but also improve the convergence rate. It is very important for complex system design as generally involving computationally expensive multidisciplinary analysis [1]. However, how to exploit the knowledge to accelerate the new design confuses the satellite designers. Transfer learning is concerned with the shift in data distribution from one domain to another. Various research has been applied to classical machine learning tasks successfully, e.g., classification task [2]-[4], like sentiment analysis [5], and digits recognition [6]. In recent years, researchers in the evolutionary algorithm community attempt to employ transfer learning to the optimization task [7]-[10].

When applying transfer learning methods to solve the optimization problems, three issues should be considered as follows.

Q1 (Transferability): In real-world case studies, a large number of similar problems have been solved and saved in the database. The critical question is how to identify the transferability of all the sources. Negative transfer occurs if the selected sources are not suitable.

Q2 (Transfer Component): In the following step, the transfer component of the problem should be determined, such as solutions, structures, features, parameters or something else.

Q3 (Transfer Algorithm): How to reuse the information extracted from the source problems is the final step. Most research focuses on one-to-one domain adaptation algorithms, such as transfer component analysis (TCA) [11], TrAdaBoost [12] in benchmarks like MNIST dataset [13] and WIFI dataset [14]. However, very few research concentrates on multisource transfer learning problems.

In transfer learning research field, most of the works are focused on Q2 and Q3, especially on Q3. But, Q1 is also very important as transferring from inappropriate sources will lead to negative transfer. In this paper, we pay special attention to the transferability of multisource problems and investigate how to measure the similarity of different optimization problems.

Liu et al. [15] showed that relatedness of tasks is crucial to the effectiveness of multitask learning in his work. Feng et al. [16] developed an evolutionary multitasking method based on autoencoder, and tasks in the experiments are chosen relied on two factors: 1) degree of the intersection of the Pareto optimal solutions and 2) similarity in the fitness landscape between tasks. The factors guarantee the relatedness. However, in actual scenes, we cannot obtain the information as mentioned above of the target problem at the beginning.

To evaluate the relatedness of different optimization problems, representation of different optimization instances should be determined first. Santana et al. [17] figured the optimization problem as a graph via the estimation of Bayesian networks algorithm (EBNA), which is one type of the estimation of distribution algorithms (EDAs). In his work, a task is represented by a graph. The relevance of tasks could be obtained by the network analysis method, but the representation method depends on human-made graph features very much, which may miss relevant information on tasks. Yu et al. [18] invented a new representation method of the reinforcement learning tasks with different parameters sampled by the uniform distributions. He uses reward vectors obtained by prototype policies via few iterations named shallow trials to represent the task, to make the past reinforcement learning tasks reusing. However, shallow trials in the evolution would make too many noises to represent the optimization instance accurately. Utilizing the population distribution produced by EDA in each generation, we can represent the instance by the compositive distribution, which is called centroid distribution here. Centroid means the centralization of all the population in each generation of evolution. Similar instances have similar centroid distribution, based on which, the similarity between different instances could be obtained easily via the Wasserstein distance (WD). By the similarities, we can make use of the three source selection strategies to produce transferred knowledge to the GA-style algorithm like NSGAII, to accelerate the searching process during the evolution. To use the strategy effectively, four selection suggestions are summarized.

As a summary, this paper makes the following contributions.

1) Invent a novel representation method named centroid distribution to measure the similarity of different optimization instances.
2) Propose a novel multisource selective transfer optimization framework with three strategies based on EDA and NSGA-II [19] to solve multiobjective optimization problems.
3) Summarize four suggestions of source selection strategy, based on which, we propose a mixed strategy to deal with the negative transfer issue.
The rest of this paper is organized as follows. A related work is surveyed in transfer optimization, EDAs, and evolutionary dynamic optimization (EDO) are presented in Section II. The general framework and workflow of multisource selective transfer optimization (MSSTO) based on EDA and NSGA-II is introduced in details in Section III. Section IV provides the comprehensive empirical studies on the commonly used multiobjective evolutionary benchmarks and summarizes four
![img-0.jpeg](img-0.jpeg)

Fig. 1. Illustration of an MSSTO workflow.
using suggestions of source selection strategy. A real-world design optimization problem of satellite layout is used to evaluate our proposed framework and validate the selection suggestions in Section V. Finally, the concluding remarks of this paper are discussed in Section VI.

## II. Related Work

## A. Transfer Optimization

In practical applications, engineers always restart a new optimization instance when the constraints and objective function parameters meet with a slice modification. Indeed there are many common features among these instances, searching from scratch will result in repeated computation. Recently, many works focusing on improving the efficacy of existing evolutionary algorithms through machine learning techniques are developed, especially reusing past search experiences from related problems. Feng et al. [7] proposed a new transfer method based on the autoencoder model to solve the multiobjective optimization problems, which accelerates the search process in the evolutionary algorithm. Santana et al. [10] puts forward four types of transfer learning methods when solving the multimarker tagging singlenucleotide polymorphism (SNP) selection problems, namely, the transfer of solutions, structure transfer, behavioral or algorithmic transfer, and combined transfer, and any combination of the previous three alternatives.

Transfer optimization's mathematical definition is given in Gupta's survey [20], which is defined as follows: given a knowledge base consists of numerous past experiences $M=\cup_{i \in k} m_{k}$, and target optimization instance $(T)$, transfer optimization improves performance speedup measured as $Q_{t}(T \mid M)-Q_{t}(T) \geq 0$, where $Q_{t}(T \mid M)$ is the algorithmic efficiency based on the knowledge embedded in $M$.

Research in transfer optimization can be divided into two categories according to the source quantity, namely, single source and multisource. Plenty of research works concentrate on one-to-one transfer algorithms in popular benchmarks, but multisource problems are more common in practical applications. Multisource transfer optimization task is concentrated on in this paper. As illustrated in Fig. 1, a general multisource transfer optimization workflow usually contains source selection and transfer algorithm. Source selection problem represents the transferability, including the representation of instance and source selection strategy. Here, we focus on

```
Algorithm 1 EDAs General Procedure
    \(t=0\).
    Initialize model \(M O(0)\) to represent uniform distribution
        over admissible solutions
    while termination criteria not reaches do
        \(P=\) generate \(N>0\) candidate solutions by sampling
        \(M O(t)\)
        \(F=\) evaluate all candidate solutions in \(P\)
        \(M O(t+1)=\operatorname{adjust} \_ \operatorname{model}(P, F, M O(t))\)
        \(t=t+1\)
    end while
```

studying the transferability especially instance representation method and multisource selection strategy. Feng's work [7] is taken as our transfer method.

## B. Estimation of Distribution Algorithms

EDAs are stochastic optimization methods that guide the search for the optimum point by learning and sampling an explicit probabilistic model of elite candidate solutions. The main difference between EDAs and conventional evolutionary algorithms (GA-style algorithms) is that the latter one generates new candidate solutions via the mutation and crossover operation, which can be viewed as an implicit distribution. However, EDAs use an explicit distribution represented by a probabilistic model, such as multivariate normal distribution, Bayesian network, etc.

The general procedure of EDAs is outlined as Algorithm 1. Based on the decision variable interdependence, EDAs are classified into three categories [21].

1) Univariate factorizations, which assumes each variable is mutually independent. The representative algorithms consist of population-based incremental learning (PBIL) [22], univariate marginal distribution algorithm (UMDA) [23], compact genetic algorithm (cGA) [24], etc.
2) Bivariate factorizations, in this class of models, dependencies between variables form a tree or forest graph. The representative algorithms contain mutual information maximizing input clustering (MIMIC) [25], EDA based on dependency trees and bivariate marginal distribution algorithm (BMDA) [26], etc.
3) Multivariate factorizations which represent dependencies using either directed acyclic graphs or undirected graphs. Two representative models are Bayesian networks [27] and Markov networks [28].
EDAs have been employed to numerous challenging optimization problems in recent years, especially in multiobjective optimization problems [29]-[33] and multimodal optimization problems [34], [35]. By the aid of the probabilistic model learned from elite candidate solutions, many types of research [36] focus on how to reuse the model from past experiences to accelerate the target instance searching. Inspired by the transfer learning research in EDA, we propose a novel method to represent instance called centroid distribution. Based on the representation, we propose three
source selection strategies to produce proper knowledge to transfer.

## C. Evolutionary Dynamic Optimization

EDO is one of the most active research areas in the field of evolutionary computation. In certain cases of EDO, some common patterns could be found with the changes of environments. Inspired by this, a lot of research focus on reusing the past search experiences from the similar environments to accelerate the evolution process [37], [38].

One common approach is learning to predict the movement of optimum based on some special points. Li et al. [39] proposed a predictive strategy based on the special points (SPPS), such as feed-forward center point, boundary point, and knee point, which can do well in EDO. Ruan et al. [40] proposed a hybrid diversity maintenance method to improve prediction accuracy based on the center points. Zou et al. [41] proposed a method to predict the nondominated set based on the knee points to make population quickly converge to PF.

Another approach is to predict the locations which individuals or population should be reinitialized when a change occurs. Zhou's work [42] utilizes history search experiences to guide similar target search to solve the dynamic optimization problems efficiently. Two reinitialization strategies are proposed, one is predicting the new location of individual according to the history; the other one is perturbing the current population by some noise whose variance estimated by the previous changes.

The third kind of approach named memory-based method is often used for solving the EDO problems via reusing the relevant Pareto-optimal set (POS) information stored in the memory when the environment changes periodically [43]-[46]. Jiang and Yang [37] proposed a new method called steadystate and generational evolutionary algorithm (SGEA), which reuses some past solutions with good distribution and relocates some solutions related to the new Pareto front based on the information of the previous and current environments when a change is detected. Besides, the multipopulation schemes are useful methods to solve the problems [47], [48].

Some recent works integrated the transfer learning algorithms such as TCA with the dynamic optimization algorithms directly. Jiang presents two algorithm frameworks in this way. One is called Tr-DMOEA which integrates transfer learning and population-based evolutionary algorithms [8], and the other one is the combination of domain adaptation and nonparametric estimation-based EDA, called DANE-EDA [9]. Different from his works, we mainly focus on how to select the suitable source from multiple source tasks to speed up the evolutionary process.

For EDO methods, the information of past generations during the optimization process is reused to facilitate the optimum search in the upcoming generations. In EDO process, the optimization problem formulation is unchanged except for some environmental parameters. But for transfer optimization, it aims to reuse the information from past optimization instances, which are totally independent of current target optimization task. How to properly judge the

![img-2.jpeg](img-2.jpeg)

Fig. 2. Comprehensive illustration of an MSSTO workflow.
relevance between the sources and the target, based on which the appropriate sources can be selected to accelerate the target task, is an important and challenging issue. To solve this problem, this paper is focused on the similarity measurement methods and source select strategies, which will be discussed in Section III.

## III. Multisource Selective Transfer OPTIMIZATION FRAMEWORK

In most practical applications [such as satellite layout optimization design (SLOD) problems], massive design instances have been launched, executed, and stored in the database for reuse. However, most researchers are more interested in one-to-one transfer optimization and neglect the multisource property in the real-world scenes. In this paper, we present a multisource selective transfer optimization framework to solve the many-reusable-instance problems.

EDAs are one type of black box optimization algorithms which have been introduced in Section II-B. Generic algorithms (GA-style) are heuristic-based searching algorithms, which are always inspired by human beings action or the other animals' action, free to the model during the searching process and depend on the crossover and mutation operation to find the better solution in the space. EDA performs better in describing the population distribution than GA-style via the explicit probabilistic model and GA-style retains an implicit one.

To solve the multisource transfer optimization problems in real-world applications, we combine the two types of optimization algorithms. As shown in Fig. 2, instance representation is introduced first. Next, the source-target similarity measurement method would be presented. Three source selection strategies are explored in the Section III-C. Then the
![img-2.jpeg](img-2.jpeg)

Fig. 3. Every optimization instance is represented by multivariate normal distribution.
transfer method is shown in Section III-D. Last, our MSSTO is presented.

## A. Optimization Instance Representation

To represent optimization instance during the searching process, we propose a novel method called centroid distribution (see Fig. 3). With GA-style algorithm running, we can obtain the elite population through selection operation, the distribution of selected solutions can be learned as an explicit probabilistic model of EDA. We call the learned model centroid distribution, to represent the current population dispersal trending in the space.

Denote the centroid distribution as $C \sim N\left(\boldsymbol{\mu}, \boldsymbol{\sigma}^{2}\right)$, which is independent multivariate normal distribution, $\boldsymbol{\mu}=$ $\left(\mu_{1}, \mu_{2}, \ldots, \mu_{n}\right), \boldsymbol{\sigma}^{2}=\left(\sigma_{1}^{2}, \sigma_{2}^{2}, \ldots, \sigma_{n}^{2}\right)$, where $n$ represents the variable dimension, $\mu_{i}$ denotes the mean of $i$ th dimension, and $\sigma_{i}^{2}$ represents the variance of $i$ th dimension. Each variable

is independent of each other

$$
\begin{aligned}
\mu_{i} & =\frac{1}{N} \sum_{j=1}^{N}\left(\text { elite }_{i j}\right) \\
\sigma_{i}^{2} & =\frac{1}{N-1} \sum_{j=1}^{N}\left(\text { elite }_{i j}-\mu_{i}\right)^{2}
\end{aligned}
$$

where elite denotes the selected population via the selection operation in GA-style algorithm. $i$ represents the $i$ th dimension and $j$ means the $j$ th individual. $N$ denotes the population size.

To avoid the notorious negative transfer, suitable sources should be determined before the transfer algorithm is launched. Our proposed representation method could reflect some similarity information between the source and target during the evolution, which can assist target instance to choose suitable sources to transfer.

## B. Source Target Similarity Measurement

WD is a distance function defined between probability distributions on a given metric space [50]. In this paper, we use WD to calculate the distance between the source and target centroid distribution.

Since centroid distribution $C$ obeys the independent multivariate normal distribution law, WD between the source and target centroid distribution can be computed by

$$
\mathrm{WD}\left(C_{s}, C_{t}\right)=\sqrt{\left\|\boldsymbol{\mu}_{s}-\boldsymbol{\mu}_{t}\right\|_{2}^{2}+\left\|\boldsymbol{\sigma}_{s}-\boldsymbol{\sigma}_{t}\right\|_{2}^{2}}
$$

where $C_{s}$ represents the source centroid distribution and $C_{t}$ represents the target centroid distribution. $\mu_{s}$ denotes the mean vector of source distribution and $\mu_{t}$ denotes the mean vector of the target distribution. $\sigma_{s}$ means the standard deviation of the source distribution and $\sigma_{t}$ means the standard deviation of the target distribution.

The nearer distance of centroid distributions is, the more related instance is. We define the similarity between source and target instance as follows:

$$
\operatorname{sim}(s, t)=\frac{1}{\mathrm{WD}\left(C_{s}, C_{t}\right)}
$$

where $\operatorname{sim}(s, t)$ denotes the similarity.
Kullback-Leibler divergence [51] can also be used for measuring the distance between two distributions, which will be investigated in the future.

## C. Source Selection Strategy

Due to the different optimization methods are used or different stopping conditions are used, different results may be obtained even for the similar optimization tasks. Besides, for the complex highly nonlinear and multimodal problems with disconnected local optimal regions, the optimization results may be quite different even with the same optimization algorithms. Thus, given the sources which are quite different, they may be actually from the similar tasks. Actually, given the vast source data and without a priori knowledge about the detailed optimization formulation and the optimization solver used for each source, it is really difficult to correctly judge whether the
![img-3.jpeg](img-3.jpeg)

Fig. 4. Three strategies for recommending suitable sources to transfer method are proposed, including NSS, WSS, and Top-K.
dissimilarity between the source and the target results from the dissimilarity between the tasks or not. Therefore, in this paper, we propose the selection strategies that "the nearer distance of centroid distributions is, the more related instance is," which actually is a sufficient but not necessary condition. If the distance is near, we judge that the instances are related and can be selected. But in the opposite, if the instances are related, we cannot judge that the distribution will be close.

Based on the analysis above, three source selection strategies are proposed to generate the transferred population to the target instance based on the similarities, see Fig. 4. Four suggestions of strategy selection are summarized in part 4.

1) Nearest Selection Strategy: During the evolution, the similarity between each source and target population can be calculated by 2 -norm WD in (4). When all the similarities between sources and target centroid distributions are obtained, the strategy selects the nearest source as the transferred knowledge to target. We name it nearest selection strategy (NSS).

Denote the population in source instances as $P_{i(D \times N)}$, where $i=1,2, \ldots, \mathrm{num}_{s}, \mathrm{num}_{s}$ represents the number of source problems, $N$ denotes the population size, and $D$ denotes the variable dimension. When the transfer operation is called by the framework over the evolutionary process, NSS will take the largest score source as transferred one in the current generation, as follows:

$$
P_{\text {transfer }}=P_{\text {arg max },(\operatorname{sim}(s_{i}, t))}
$$

where $s_{i}$ means the $i$ th source instance and $t$ means the target instance. $P_{\text {transfer }}$ denotes the transfered population produced

by NSS and $\arg \max _{i}\left(\operatorname{sim}\left(s_{i}, t\right)\right)$ represents the largest similarity score source index.

In NSS, we note that the most similar source contains the most useful knowledge to the target instance.
2) Weighted Selection Strategy: In certain circumstances, some sources may be located in the same similarity level almost. If we use one source to transfer, some useful information about other sources would be missed. Under the situation, a new strategy is proposed to exploit the knowledge of all the sources. Because of different sources making different level contributions to the transfer effectiveness, final source population is a weighted sum of all sources in the current generation. This strategy is called weighted selection strategy (WSS). Denote the source weight as $w_{i}$, the transferred population is given by

$$
P_{\text {transfer }}=\sum_{i=1}^{\text {num. }_{i}} w_{i} P_{i}
$$

where

$$
w_{i}=\frac{\operatorname{sim}\left(s_{i}, t\right)}{\sum_{i=1}^{\text {num. }}\left(\operatorname{sim}\left(s_{i}, t\right)\right)}
$$

Here, $w_{i}$ is a scalar and $P_{i}$ is a matrix.
In WSS, we note that every source is helpful to the target instance, but different sources have the different level of importance, reflected by source weights here.
3) Top-K Selection Strategy: Top-K selection strategy (Top-K) can be regarded as the particular form of WSS. In this situation, some dissimilar sources are eliminated, and the K most similar ones are chosen to transfer. All the calculation methods are the same as WSS.

In this strategy, the transferred source set is obtained as follows:

$$
P_{\text {transfer }}=\sum_{i \in S} w_{i} P_{i}
$$

where $S$ denotes the index set of the K most similar sources.
4) Suggestions for Strategy Selection: In this part, four suggestions are summarized to guide to choose the suitable selection strategy under certain conditions.

First, a metric called max similarity rate is defined as follows:

$$
\mathrm{msr}=\frac{\max \left(\operatorname{sim}\left(s_{i}, t\right)\right)}{\sum_{i=1}^{\text {num. }}\left(\operatorname{sim}\left(s_{i}, t\right)\right)}
$$

where msr denotes the max score ratio which represents the ratio between the highest similarity score and the sum of all the similarity scores. When the selected source has a higher msr, it is more similar to the target than any other sources obviously. Under this situation, NSS could lead to better performance improvements.

Then, the variances of similarities between different sources are used for determining whether to choose WSS or Top-K. The variance determines the volatility of distribution. Smaller variances mean the equalization of all the sources, based on which, taking all the sources to combine into a learned population via WSS would lead to better performance. Larger
variances imply that part of sources is suitable to transfer via Top-K.

Based on the above analysis, suggestions of choosing source selection strategy can be summarized as follows.

1) When the msr is relatively high, we should make use of NSS to select one suitable source.
2) When the msr is relatively low, and the variances of similarities are small, we could take WSS as our selection strategy.
3) When the msr is relatively low, and the variances of similarities are large, the Top-K strategy is our best choice.
4) When the msr is relatively low, and the variances locate at the critical range between the WSS and Top-K strategy, the transfer operation is not recommended to call.
Based on the above suggestions, we propose a mixed version of the three strategies called mix selection strategy (MSS). To explore whether to transfer in each generation during the evolution, the source selection strategy part would be triggered every time. Whether to transfer or not would be determined by the suggestions above according to the similarity information between all the sources and target. More similarity calculation brings more computational cost, but it also exploits more information indeed. A separate experiment will also be conducted to evaluate MSS.

## D. Transfer Method

In the whole framework pipeline, transfer method is used to receive final source population from three strategies in some generation. Then it produces the learned population via the mapping method proposed by Feng et al. [7], finally sends them to the selection operation of the GA-style as the candidate population. By using Feng's transfer method, for one thing, it can be injected into GA-style algorithm easily. For another, the mapping method can obtain a closed-form solution and is easy to solve during the evolution.

The source population and target population could be connected by one single layer denoising autoencoder [7] with solid theoretical derivations. As shown in Fig. 5, the key of autoencoder-based transfer method is learning a mapping from source to target population. We can obtain the closed-form mapping $M$ by solving

$$
L_{s q}(M)=\frac{1}{2 N} \operatorname{tr}\left[\left(P_{t}-M P_{\text {transfer }}\right)^{T}\left(P_{t}-M P_{\text {transfer }}\right)\right]
$$

where $\operatorname{tr}(\cdot)$ denotes the trace operation of a matrix, $L_{s q}(M)$ represents the squared reconstruction loss from the source population space to target, $P_{\text {transfer }}$ represents the transferred population from selection strategies, and $P_{t}$ denotes the target population during the evolution. So mapping $M$ between transferred population $P_{\text {transfer }}$ obtained by selection strategies in Section III-C and target population $P_{t}$ is given by

$$
M=\left(P_{t} P_{\text {transfer }}^{T}\right)\left(P_{\text {transfer }} P_{\text {transfer }}^{T}\right)^{-1}
$$

However, the learned mapping is changed with the evolution. The optimized solutions from past problems contain vast knowledge to improve the target optimization searching

![img-4.jpeg](img-4.jpeg)

Fig. 5. Transfer method proposed by Feng which is based on autoencoder.
speed so that we can transfer the best solutions in the previous experiences into the target by the learned mapping.

Thought here is very similar to works in deep learning area which is popular in natural language processing [52], [53], computer vision tasks [54], [55], etc. The learned population can be obtained by

$$
P_{\text {learned }}=M P_{s, \text { optimized }}
$$

where $P_{s, \text { optimized }}$ denotes the best population in source instance for strategy NSS and $P_{\text {learned }}$ represents the learned population via the transfer method. Especially for WSS and Top-K, best population and $P_{\text {transfer }}$ are the weighted sums of all suitable sources.

## E. Proposed Framework

Based on the four parts above, our MSSTO is proposed. As shown in Fig. 6, MSSTO inherits from the conventional evolutionary algorithm. The most important difference is that selected candidates consist of three parts: 1) parent population from the last generation; 2) offspring population from mutation and crossover operation; and 3) learned population from past experiences by the transfer method. The learned population is injected into the selection operation of GA-style.

The general procedure of MSSTO is outlined as Algorithm 2. $G$ in step 5 denotes the transfer cycle and Feng sets it as 10 in his work [7].

After the initialization, the framework starts a loop with the population reproduction, transfer and selection operation. Transfer occurs when the generation can divide exactly $G$. During the transfer operation, the source and target instance are represented by centroid distribution defined by (1) and (2) first. Then the similarity score between the source and target could be calculated by (3) and (4). Next, suitable source would be selected according to (5)-(9). Last, the learned population
![img-5.jpeg](img-5.jpeg)

Fig. 6. Illustration of an MSSTO framework procedure.

```
Algorithm 2 MSSTO Framework General Procedure
    Set \(\operatorname{Gen}=0\).
    Initialization.
    while condition is not satisfied do
        Reproduction, including crossover and mutation opera-
        tion.
        If \(\operatorname{Gen} \bmod G==0\), go to step 6, else go to step 11 .
        Transfer, execute Step 7-10.
        Represent source and target instances with centroid dis-
        tribution defined by the formulas (1)(2) in Section III-A.
        Calculate the similarity score by the formulas (3)(4) in
        Section III-B.
        Select suitable source according to the formulas (5)-(9)
        in Section III-C.
        Produce the learned population by the formulas (10)(11)
        in Section III-D.
        Population Selection.
        \(\operatorname{Gen}=\operatorname{Gen}+1\)
    end while
```

to transfer is produced by (10) and (11). The loop stops when the final fitness evaluation is done.

Three selection strategies defined in (5)-(9) could produce the final source population for the later process with transfer method. The strategies may not only improve optimization effect but also increase the convergence speed, so as to decrease the fitness evaluation quantity. Fewer evaluations in real-world applications mean fewer simulations or experiments which can save a lot of computational or experimental cost.

## IV. Empirical Study

In this section, the experiments are setup up to validate the proposed framework.

Before a new optimization instance is launched in experiments, a large number of similar synthetic instances should be run by the same algorithm. Here the "similar" means that instances objectives and constraints have the same form, but the parameters in objectives and constraints are different. To simplify the research, parameters are sampled from uniform distribution here. We empirically evaluate MSSTO, particularly, addressing the following points.

1) Can MSSTO with three source selection strategies accelerate new similar instance searching process via the past experiences?
2) Are the suggestions of strategy selection effective?
3) Can the mixed strategy based on the suggestions solve the negative transfer issues?

## A. Experiment Settings

Twelve commonly used multiobjective problem (MOP) benchmarks, consisting of five MOPs in ZDT family problems with two objectives [56] and seven MOPs in DTLZ family problems with three objectives [57] are considered here. For comparison, a popular multiobjective evolutionary algorithm (MOEA) named NSGA-II [19] and Fengs transferred method based on autoencoder (NSGAII+AE) [7] are employed as our baseline MOP solvers. NSGA-II is also used as GA-style in MSSTO.

In Feng's method, the past experiences come from different problems. When the ZDT problem is regarded as the target, other problems in the ZDT family or problems in the DTLZ family will be regarded as the source problems without selection. In this paper, to validate the relatedness measurement method via the distance of source population distributions and the effectiveness of MSSTO, we synthesize new similar problems based on the given target problem through some transformation tricks. Transformation means that the optimization problem template keeps constant, but the parameters in objectives and constraints change randomly. Every target instance can accumulate knowledge learned from ten similar sources which are transformed by the target via a random disturbance to the parameters in objectives and constraints.

In the experimental results, we denote the comparison algorithms as follows.

1) NSGAII denotes the NSGAII algorithm.
2) NSGAII+AE denotes the algorithm proposed by Feng.
3) NSGAII+ST1 denotes the proposed algorithm with the NSS.
4) NSGAII+ST2 denotes the proposed algorithm with the WSS.
5) NSGAII+ST3 denotes the proposed algorithm with the Top-K.
6) NSGAII+MIX denotes the proposed algorithm with the MSS.
Furthermore, our experiments are developed based on the evolutionary multiobjective optimization platform (PlatEMO) [58], which is an open source and free MATLABbased platform for evolutionary multiobjective optimization, that includes more than 60 existing MOEAs and 100 popular
benchmark MOPs, and the specific experimental settings are outlined as follows.
7) Population size $N$ is configured as 50 in all the algorithms.
8) Evolutionary operators in NSGAII [19]: SBX crossover: $p_{c}=0.9, \eta_{c}=20$, polynomial mutation: $p_{m}=$ $(1 / n), \eta_{m}=20$.
9) Maximum function evaluation is MaxFES $=75000$, and the stopping criterion is reaching the maximum function evaluation.
10) Independent number of runs is runs $=20$.
11) Interval of injecting solution obtained by source problem learning is $G=10$.
12) Source instance parameters distribution. For the given target instance, similar sources would be synthesized via sampling the parameters in objectives and constraints. Suppose the value of the objective parameter is $r$, the parameters are sampled concerning the uniform distribution of $[r-5, r+5]$.
13) Source instance number num $_{s}=10$, each target instance has ten similar sources synthesized by the random processing method.
14) Top $30 \%$ source instances are selected in the Top-K strategy.
Other parameters are kept as the default values in PlatEMO [58].
In the evaluation step, all the algorithms are evaluated by the metric hypervolume (HV), which is the only single set quality measure that is known to be strictly monotonic with regards to Pareto dominance [59], [60]. The motivation of this paper is trying to improve Feng's work (NSGAII+AE). For comparing easily, we take the same indicator as Feng's work, namely HV.
The numerical experiments include three steps. First, the benchmark test problems are solved by the proposed MSSTO framework with three different source selection strategies, respectively and compared against the standard NSGAII result. Second, the source selection suggestions are evaluated by the intermediate process of some typical benchmark test problems. Third, the MSS based on the suggestions would be evaluated by one problem which occurs negative transfer.

## B. Experimental Results

1) Evaluation of MSSTO With Three Strategies on Benchmark: Five algorithms are compared in the experimental study, consisting of one classical multiobjective algorithm NSGA-II and four variants of NSGA-II. In ZDT/DTLZ MOPs, all algorithms execute 20 independent runs with 75000 function evaluations. The results are tabulated in Table I. The best HV values are bold in Table I.
As illustrated in Table I, MSSTO, including NSGAII-ST1, NSGAII-ST2, and NSGAII-ST3 achieve nine champions in all of the 12 MOPs, NSGA-II wins three remained problems. Here, the champion is defined as achieving the most considerable HV value. Since the standard deviation magnitude is much smaller than HV value, it could be neglected in the comparison. Our framework has achieved similar performance as

TABLE I
HV MEDIAN AND STANDARD DEVIATION Values Obtained by NSGAII, NSGAII+AE, NSGAII+ST1, NSGAII+ST2, and NSGAII+ST3 ON ZDT/DTLZ MOPS ACROSS 20 INDEPENDENT RUNS WITH 75000 FUNCTION EVALUATIONS


NSGA-II on some problems, e.g., DTLZ1, DTLZ2, DTLZ5, DTLZ6, DTLZ7, ZDT2, ZDT3, and ZDT6, but MSSTO shows superior performance over NSGA-II and NSGAII+AE on ZDT1, ZDT4, DTLZ3, and DTLZ4, which demonstrates our framework can learn the best population among all the comparison algorithms.

In all problems we evaluate, MSSTO consistently outperforms NSGAII-AE, which means selective and combination strategies in our framework can learn more useful knowledge to guide the search of target instance evolution than transferring from all the sources without source selection operation in NSGAII-AE.

Compared with our three proposed strategies, ST1 wins in six problems, ST2 wins three problems, while ST3 wins twice. The selective strategy performs better than combining with all the sources strategy in most of the situations, ST2 is on par with ST3 which means combining all the sources has a similar effect as mixing the Top-K in all the MOPs here. Though the results show that ST1 is the best, we think three strategies adapt to different situations. We will make a further study on the issue later.

To access the efficiency of our proposed framework, we plot the convergence graphs of the NSGA-II, NSGAII-AE and three NSGAII variants on the representative MOPs. In particular, Fig. 7 shows the convergence graphs of NSGAII, NSGAII+AE, NSGAII+ST1, NSGAII-ST2, and NSGAII-ST3. In the figures, the $x$-axis denotes the fitness evaluations which represents the algorithm efficiency, and fewer function evaluations imply a better computation performance. $Y$-axis denotes the mean HV values obtained across 20 independent runs.

Compared with NSGAII and NSGAII-AE, MSSTO with three different selection strategies achieves the competitive performance in most of the MOPs. NSGAII-ST1 outperforms the other two strategies in most MOPs of ZDT family, but in DTLZ MOPs, NSGAII-ST3 is best-performing.

Furthermore, we track the transfer process of compared algorithms during the evolution. As illustrated in Fig. 8, we define a metric called average contribution rate to evaluate the transfer effectiveness of NSGAII+AE and our MSSTO. The $x$-axis denotes the evolutionary generation, and the $y$-axis denotes the average contribution rate obtained across 20 independent runs, which is given as follows:

$$
\operatorname{acr}_{i}=\frac{N_{i, \text { selected }}}{N_{i, \text { total }}}
$$

where $\mathrm{acr}_{i}$ means the average contribution rate of the $i$ th generation during evolution, $N_{\text {selected }}$ represents the size of selected population in $i$ th generation, and $N_{\text {total }}$ denotes the total size of population sent by the transfer method in $i$ th generation. Here, we choose ZDT1 as our tracking problem to validate the algorithm transfer effect. As seen in Fig. 8, NSGAII+AE performs worst among all of the transferred algorithms, NSGAII+ST1 achieves the best performance, and NSGAII+ST2 performs on par with NSGAII+ST3. This explains the observations shown in Fig. 7(a) and Table I that NSGAII+ST1 achieves the best convergence speed, and NSGAII+AE performs worst in HV value. NSGAII+ST2 has achieved similar performance as NSGAII+ST3 in both HV value and convergence speed.
2) Evaluation of Source Selection Suggestions: To validate the suggestions of choosing the different source selection strategies, we make a further study on the similarities among all the sources and target.

First, we consider when to use NSGAII+ST1 during the evolution. Observed from Fig. 7(d)-(f) and (h) that on ZDT4 and ZDT6, NSGAII+ST1 performs better than the other two algorithms, but on DTLZ1 and DTLZ3, NSGAII+ST1 achieves the worse performance than the other two. So we choose ZDT4, ZDT6, DTLZ1, and DTLZ3 as our experimental problems. As shown in Fig. 9, the $x$-axis denotes the evolutionary generation, and the $y$-axis denotes the max similarity rate obtained across 20 independent runs.

On ZDT4 and ZDT6, the msr values are significantly higher than the performance on DTLZ1 and DTLZ3, which brings into correspondence with the previous results. It is suggested when the msr is relatively high, using the WSS and Top-K would lead to a slower convergence speed.

Then, when to use NSGAII+ST2 is considered in our discussion. Observed from Fig. 7, we find that NSGAII+ST2 performs better than NSGAII+ST3 on DTLZ1, but NSGAII+ST3 performs better on ZDT4 and ZDT6. In Fig. 10, the $x$-axis denotes the evolutionary generation, and the $y$-axis denotes the variances of sources obtained across 20 independent runs. For convenient comparison, we plot the logarithm of variances in the figure. As shown in Fig. 10, the variance values on ZDT4 and ZDT6 are several orders of magnitudes greater than DTLZ1. It concludes when the msr is relatively low and the variances of similarities are large, WSS should be chosen. Contrarily, the Top-K would be the most suitable choice. If NSS is selected under this condition, it will miss more useful knowledge.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Mean HV values obtained by NSGAII, NSGAII+AE, NSGAII+ST1, NSGAII+ST2, and NSGAII+ST3 with respect to FES on representative ZDT/DTLZ MOPs across 20 independent runs. (a) ZDT1. (b) ZDT2. (c) ZDT3. (d) ZDT4. (e) ZDT6. (f) DTLZ1. (g) DTLZ2. (h) DTLZ3. (i) DTLZ4. (j) DTLZ5. (k) DTLZ6. (1) DTLZ7.
3) Evaluation of Mix Selection Strategy: To evaluate NSGAII+MIX, a separate experiment is conducted on DTLZ3. Consider that on DTLZ3, the negative transfer occurs in all of the transferred algorithms. In Fig. 11, $x$-axis and $y$-axis have the same meaning as Fig. 7. In this experiment, we set three hyperparameters to denote the msr threshold, the upper and lower bound of the variance according to the strategy selection suggestions. Different from the previous
experiments, the transfer strategy part is called in each generation. In each generation, the strategy aims to decide whether to transfer [here principle (4) means no transfer occurs] and which strategy should be taken if the transfer is needed. NSGAII+MIX is a dynamic decision process during the evolution. It is designed for taking the best decisions in each generation according to the current information. As illustrated in Fig. 11, NSGAII+MIX achieves better convergence speed

![img-7.jpeg](img-7.jpeg)

Fig. 8. Average contribution rate varies along with the evolutionary process on ZDT1.
![img-8.jpeg](img-8.jpeg)

Fig. 9. Max similarity score ratio between the selected source and target via NSGAII+ST1 on ZDT4, ZDT6, DTLZ1, and DTLZ3.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Variance of similarity score between the selected source and target via NSGAII+ST1 on ZDT4, ZDT6, and DTLZ1.
and HV values than all the algorithms (including NSGAII). It concludes that our summarized suggestions can be used in the source selection problems well.
4) Discussion: After the empirically evaluations, we can answer the three questions at the beginning of this section.
![img-10.jpeg](img-10.jpeg)

Fig. 11. HV value on DTLZ3 with NSGAII+MIX compared to the above algorithms across independent 20 runs.

1) Observed from Fig. 7 and Table I, it is convinced that MSSTO can accelerate the new similar instance by our proposed three source selection strategies in most situations.
2) Observed from Figs. 8-10, we validated the effectiveness of our strategy suggestions. Based on the suggestions, we propose a mixed strategy NSGAII+MIX, to solve the negative transfer issue occurs in the DTLZ3 problem successfully (see in Fig. 11).
This paper is a preliminary research on multisource transfer optimization. In this paper, we explore the simplest homogeneous situation. Here, the homogeneity means the same variable number and type in both source and target instance. In the real-world engineering scenes, our proposed method can be used well. Take SLOD task in Section V for example, the design is processed iteratively. In different design phases, the objectives and constraints would change slightly, but the design variables (the locations of the components) are kept unchanged. We can accumulate large amounts of historical optimization experiences to reuse in the new design phase. In the future research, we will expand our method to the heterogeneous situation which is more complex.

## V. APPLICATION ON SATELLITE LAYOUT Optimization Design Problem

In this section, we consider the application of the proposed framework on SLOD problems. In particular, this application aims to carry out the computationally demanding simulationbased optimization of two different satellite layout design tasks. It would be another critical improvement in shortening the satellite design cycle and enhancing the quality of satellite layout design, thereby playing a pivotal role in realizing the intelligent system design for aerospace vehicles.

The purpose of satellite layout design is to place the satellite components in the proper position and orientation so that various engineering requirements or constraints can be satisfied to ensure the satellite in a normal and smooth in-orbit operation state [61]. In most engineering cases, such layout schemes can be determined through repeated adjustment and modification,

![img-11.jpeg](img-11.jpeg)

Fig. 12. Illustration of the SLOD model.
which dramatically extends the design cycle and thus hampers the rapid deployment of micro- and nano-satellites. Under this circumstance, the SLOD problem is proposed as an automatic optimization approach to generate some better layout candidate schemes for engineers to choose from [62].

The SLOD problem is a 3-D layout optimization problem with complex performance constraints (see Fig. 12). It has a nonlinear and nonconvex layout design space with numerous local optima, which is known as a class of NP-hard problems [63]. The SLOD model concerning the satellite mass characteristics, attitude dynamics issues, and thermal performance are considered in this real-world application. This model has two objectives: one is to minimize the moments of inertia of the whole satellite so that the satellite attitude controllability can be enhanced as much as possible, and the second is to minimize the nonuniformity of satellite heat flux so that a uniform thermal distribution within the satellite can be reached. The second objective function is represented using the intersection area of the active areas determined by the component dissipation powers, which is first proposed by Hengeveld et al. [64] and later combined in the SLOD research [62]. The corresponding layout constraints can be summarized as the performance constraints (system centroid constraint and inertia angle constraint) and the primary geometric constraint (nonoverlap constraint).

Assume that there are total $N$ cylindrical layout components to be placed in the simplified cylindrical satellite module as shown in Fig. 12. All these components are installed on two surfaces of the bearing plate which is fixed to the shell of the satellite. The SLOD model in this section mainly focuses on optimizing the component centroid coordinates within the 2-D layout domain. Therefore, the bi-objective constrained SLOD model can be formulated as follows:

$$
\begin{aligned}
& \text { Find } X=\left\{X_{1}, X_{2}, \ldots, X_{N}\right\}=\left\{X_{i}=\left(x_{i}, y_{i}\right) \mid i=1 \ldots N\right\} \\
& \operatorname{Min}\left\{\begin{array}{l}
f_{1}(X)=J_{x}(X)+J_{y}(X)+J_{z}(X) \\
f_{2}(X)=\sum_{k=1}^{n}\left(\sum_{i=1}^{N_{k}-1} \sum_{j=i+1}^{N_{k}} \operatorname{int}\left(A_{i j}\right)\right) \\
g_{1}(X)=\sum_{i=0}^{N-1} \sum_{j=i+1}^{N} \Delta V_{i j} \leq 0 \\
g_{2}(X)=\left|x_{c}-x_{e}\right|-\delta x_{e} \leq 0 \\
g_{3}(X)=\left|y_{c}-y_{e}\right|-\delta y_{e} \leq 0 \\
g_{4}(X)=\left|\theta_{x}(X)\right|-\delta \theta_{x} \leq 0 \\
g_{5}(X)=\left|\theta_{y}(X)\right|-\delta \theta_{y} \leq 0 \\
g_{6}(X)=\left|\theta_{z}(X)\right|-\delta \theta_{z} \leq 0
\end{array}\right.
\end{aligned}
$$

![img-12.jpeg](img-12.jpeg)

Fig. 13. Mean HV values obtained by NSGAII. NSGAII+AE, NSGAII+ST1, NSGAII+ST2, NSGAII+ST3, and NSGAII+MIX with respect to FES on SLOD across 20 independent runs.
where $X$ represents the design variables and refers to the layout scheme to be optimized. $f_{1}$ means the summation of the moments of inertia of the whole satellite. $n$ denotes the number of layout surfaces and here $n=2 . N_{k}$ is the number of layout components that are placed on the $k$ th $(k=1 n)$ layout surface. According to [64], $f_{2}$ can represent the heat flux nonuniformity approximately. Regarding the nonoverlap constraint $g_{1}, \Delta V_{i j}(i, j>0, i \neq 0)$ refers to the amount of overlap between components. When $i=0$, the component $i$ denotes the satellite module shell, and it means the container protrusion is also not allowed. $g_{23}$ mean the system centroid error constraints, where $\delta x_{e}$ and $\delta y_{e}$ are the maximum permissible centroid errors and set as 3 mm here. And $g_{4,5,6}$ describe the inertia angle constraints, where $\delta \theta_{x}, \delta \theta_{y}$, and $\delta \theta_{z}$ are the maximum permissible inertia angles and set as 0.03 rad . Their relevant calculation can be found in [62].

Hence, a multiobjective multiconstraint numerical optimization problem is formed to represent the SLOD case in this paper.

Noted that when calculating the HV values, the reference set representing the approximation of the ideal and nadir points is set as (28.0, 3.6). Observed from Fig. 13 and Table II (best result is bold), NSGAII+MIX based on the selection suggestions is top-performing, and our proposed framework with three strategies achieves better performance than NSGAII+AE and NSGAII, respectively. It is also verified the effectiveness of our summarized selection suggestions. However, the standard deviation of NSGAII+MIX is larger than other methods a lot, which means the mixed method is not stable. We need to take much time to tune the hyperparameters. We will make a further study on the stableness of NSGAII+MIX in the future work.

Based on the selection from multisource instances in realworld applications, the target instance can achieve an impressive boosting in HV values and convergence speed. The effect of reusing more knowledge from similar instances is powerful for practical applications in the actual scenes, e.g., SLOD problem. Better searching the performance implies the saving more time and costs.

TABLE II
HV Median and Standard Deviation Values Obtained by NSGAII, NSGAII+AE, NSGAII+ST1, NSGAII+ST2, NSGAII+ST3, AND NSGAII+MIX ON SLOD ACROSS 20 INDEPENDENT RUNS WITH 75000 FUNCTION EVALUATIONS

## VI. CONCLUSION

In this paper, to reuse knowledge from past searching experiences for accelerating the target optimization instance in a new parameter configuration, we proposed a novel multisource selective transfer optimization framework combining GA-style and EDA. Employing EDA probabilistic model learned by elite candidate solutions from the selection operation of GAstyle EA, we present an optimization instance representation method named centroid distribution to measure the relatedness of different optimization instances during the evolution. The relatedness can assist the target instance to select the most suitable sources to learn and transfer. In the source selection step, we propose three strategies: 1) NSS; 2) WSS; and 3) Top-K. The first one aims at selecting the nearest source, but the latter two produce a combined source from multiple sources with different weights. To guide the use of the suitable selection strategy during the evolution, four using suggestions are summarized. To evaluate the effectiveness of the proposed framework, comprehensive studies on the multiobjective optimization problem benchmarks and a realworld application from the SLOD problem are conducted. The obtained results confirm the efficacy of our proposed framework for accelerating the searching process via the multisource selective transfer step when compared with the classical EA (NSGA-II) without selection among the sources. Our further study validates the effectiveness of strategy selection suggestions and the ability to solve negative transfer issues by our proposed MSS.

In the future, our research will focus as follows.

1) Improve the stableness of mixed and dynamic selection strategy.
2) Verify the effectiveness of MSSTO on multiple heterogeneous sources problems.
3) Evaluate the applicability of MSSTO in other types of optimization problems, e.g., multimodel optimization.
