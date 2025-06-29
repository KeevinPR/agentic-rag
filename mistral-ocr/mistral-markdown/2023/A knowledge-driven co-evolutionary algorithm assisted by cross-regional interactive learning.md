# A knowledge-driven co-evolutionary algorithm assisted by cross-regional interactive learning 

Ningning Zhu ${ }^{\mathrm{a}}$, Fuqing Zhao ${ }^{\mathrm{a}, *}$, Jie Cao ${ }^{\mathrm{a}}$, Jonrinaldi ${ }^{\mathrm{b}}$<br>${ }^{a}$ School of Computer and Communication, Lanzhou University of Technology, Lanzhou, 730050, China<br>${ }^{\mathrm{b}}$ Department of Industrial Engineering, Universitas Andalas, Padang, 25163, Indonesia

## A R T I C L E I N F O

Keywords:
Comprehensive co-evolution
Cross-regional interactive learning
Reinforcement learning
Knowledge guided
Parameter adaptive strategy

## A B STR A C T

Differential evolution (DE) and Estimation of distribution algorithm (EDA) exhibit complementary superiority in solving complex continuous optimization and engineering problems. The design of appropriate strategies coordinated with the two algorithms to balance exploration and exploitation is conducive to obtaining high-precision solutions. A knowledge-driven co-evolutionary algorithm assisted by a cross-regional interactive learning mechanism (KCACIL) is proposed to achieve a comprehensive collaboration between the algorithms, diverse strategies, and cross-regional individuals. Various elite-guided mutation strategies and a self-feedback strategy based on successful experience in light of implicit knowledge are devoted to fulfilling self-learning and crossregional interactive learning to accomplish individual collaboration and knowledge transfer in the three regions. Reinforcement learning based on $c$ - greedy and simulated annealing is employed as feedback on the crossregional individual information to promote the collaboration between opposition-based learning, interaction learning mechanism, and the revised strategy of inferior solutions with small $Q$ values and high distance density. The dynamic self-adaptive adjustment strategies of multiple parameters are adopted to balance diversity and convergence. KCACIL is verified on the CEC 2014, 2017, 2020 benchmark test suites, and engineering applications. Experimental results indicate KCACIL is superior to the state-of-the-art comparison algorithms.

## 1. Introduction

With the rapid development of society, an increasing number of researchers are paying close attention to optimization problems in various domains (Gurses et al., 2021; Yildiz et al., 2021) (Mehta et al., 2022), such as engineering, transportation, and biology. Multifarious improved optimization algorithms in intelligent computing are proposed based on the original algorithm framework with the incremental complexity of optimization problems (Zhou et al., 2023; Yildiz et al., 2023). The primary target of optimization is to find the optimal solution from a series of candidate solutions to a minimizing or a maximizing problem (Tian et al., 2022). Complex continuous optimization problems reveal the characteristics of the graded level of linkages, rotational invariance, non-separability, asymmetry, and diverse properties around different local optima (Awad et al., 2016), which contain abundant implicit knowledge.

The methods to solve complex optimization problems are divided into gradient-based and intelligent optimization methods. The gradientbased methods exhibit plenty of limitations and are employed to settle
simple functions mostly (Mehta et al., 2022). Numerous practical problems are complex and multimodal, and the gradient-based methods are no more suitable for such problems. On account of the characteristics of wide applicability, strong robustness, splendid self-adaptation, and self-learning, multiple intelligent optimization algorithms have shown advantages for solving complex continuous and engineering problems (Yildiz et al., 2022a, 2022b). Moreover, these algorithms are not restricted by the nature of the idiographic problems.

Various metaheuristics algorithms have been applied to efficiently solve the real-world optimization problems (Yildiz et al., 2021a, 2021b). Metaheuristic algorithms (Benítez-Hidalgo et al., 2019) include swarm intelligence optimization algorithms, evolution-based algorithms, and physical rule-based and human behavior-based methods. Swarm intelligence optimization algorithms utilize the information exchange and cooperation between individuals to find the optimal or approximate optimal solution (Yildiz, 2020a, 2020b). The classical differential evolution (DE) (Houssein et al., 2022), estimation of distribution algorithm (EDA) (Shirazi et al., 2023), genetic algorithm (GA) (Xie et al., 2022), and particle swarm optimization algorithm (PSO) (Chih, 2022) belong to

[^0]
[^0]:    a Corresponding author.

    E-mail addresses: 307516638@qq.com (N. Zhu), zhaofq@lut.edu.cn (F. Zhao), caoj2976016@qq.com (J. Cao), jonrinaldi@eng.unand.ac.id (Jonrinaldi).

this category.
The DE, first proposed by Storn and Price in 1995 (Storn, 1997), includes mutation, crossover, and selection. The evolutionary behavior is guided through the mutation operators and differential terms. The optimal solution is approached iteratively. DE is widely applied to different complex optimization problems because of outstanding performance, few parameters, simple structure, and powerful global search (Jiang et al., 2022). Meanwhile, the DE exerts some limitations due to the lack of knowledge about the characteristics of the problem structures (Yue et al., 2021). It is affected by the population quality of the early stage, and convergence accuracy and speed are not desirable. The DE is adept at exploration but has insufficient exploitation (Son et al., 2020). Diverse DE variants or collaborative algorithms are proposed to conquer these limitations. (Zhou et al., 2023) explores a novel multimodal multiobjective DE (MMO_CDE) based on a neighborhood-based dual mutation strategy and a clustering-based environmental selection mechanism, however, the framework of the algorithm is complex. (Li et al., 2023) designs a novel cooperative evolutionary framework with an improved DE and EDA (IDE-EDA) to balance exploitation and exploration. (Zhou and Tan, 2020) studies a self-adaptive EDA with DE (DE/AEDA) to solve a discrete supermarket location problem that considers the utilization rate and the capacity constraint. However, the aforementioned work does not take advantage of the reinforcement learning mechanism.

The EDA originates from GA and has a different evolutionary mode from DE. Based on probability theory and statistics (Shirazi et al., 2022), it involves mathematical statistics and intelligent computing (Cao et al., 2022). Different from the crossover, mutation, and selection of the GA, the EDA preserves the selection process and replaces the crossover and mutation with the statistical sampling theory. The probabilistic models are established according to the selected dominant individuals, and guide the evolution of the population. High-quality solutions are generated, while inferior solutions are superseded in the original population. Ultimately, the global optimal solution is found with a high probability. Population-based incremental learning (PBIL) (Zeng and Ge, 2020), Covariance matrix adaptive evolution strategy (CMA-ES) (Tong et al., 2019), and the Bayesian optimization algorithm (BOA) (Lan et al., 2022) are the typical representatives. Although the solution quality of previous generations is improved, exploration is scarce. The diversity decreases with the iterative process and it is liable to fall into the local optima (B. C. Wang et al., 2022). From this aspect, EDA and DE have complementary characteristics.

Reinforcement learning is applied to various optimization problems to learn the sequence decision tasks (Chen et al., 2021). An agent optimizes the behavior through continuous experience and learns successively by interacting with the dynamic environment. The current environment is evaluated through feedback on rewards. A single-use of reinforcement learning is not efficient. The combination of reinforcement learning and swarm intelligent optimization algorithms is a popular research topic. (Tan et al., 2022) presents a reinforcement learning-based DE with hybrid parameters and mutation strategies, and the agent adaptively selects an optimal combination of mutation strategies and parameters to generate offspring. Most of the previous work has applied reinforcement learning to the parameter and strategy tuning of meta-heuristic algorithms. Knowledge from specific problems is not considered. The proposed KCACIL provides a new idea by incorporating reinforcement learning with specific problem knowledge, diversified adjustment strategies, and collaboration mechanisms.

Coevolution is the mainstream of current research. Various literature has proposed diverse collaboration framework which incorporates multiple algorithm characteristics or reinforcement learning mechanisms. The coevolutionary algorithms fully exploit the advantages of each algorithm and eliminate the limitations to some extent. The complementary advantage is achieved by designing an appropriate collaboration strategy (Zhao et al., 2021). The coevolutionary framework renders the optimization schemes suitable for the potential search areas,
which improves the adaptability, convergence speed, or search accuracy under different circumstances (Zhao et al., 2022b). However, only local coordination between algorithms or strategies is achieved in the current research, and the specific problems are not considered.

Can the collaboration of algorithms, strategies, and individuals in the population be implemented comprehensively? Can the specific characteristics of the problems be utilized to effectively guide the coevolution process? Inspired by this motivation, this paper makes full use of the respective advantages of DE and EDA in exploration and exploitation to accomplish collaboration between the algorithms. Furthermore, the population is divided into three regions based on distance, and crossregional individual coevolution is achieved in light of individual knowledge. The cross-regional elite information efficiently guides evolutionary behavior. In addition, the learning mechanisms and adjustment strategies are designed to interact with each other based on the specific needs during the evolutionary process. In summary, comprehensive interactive learning is achieved through the collaboration and interaction of algorithms, strategies, and cross-regional individuals. A knowledge-driven co-evolutionary algorithm assisted by a cross-regional interactive learning mechanism (KCACIL) is presented to achieve comprehensive coevolution based on knowledge from the fitness landscape, characteristics of three regions, parameters, and implicit information. The contributions are summarized as follows.

The population is divided into three regions based on distance. Based on the implicit knowledge characteristics of the three regions, diverse mutation strategies and a self-feedback strategy that utilizes the successful mutation are designed and resource allocation is adjusted dynamically. Efficient knowledge transfer is fulfilled by introducing elite strategies with various characteristics to guide intra-regional self-learning for self-evolution, and cross-regional interactive learning for co-evolution.

- Reinforcement learning based on $c$-greedy and simulated annealing is designed. The optimal state value function of reinforcement learning is employed to provide feedback on the individual information to guide opposition-based learning and the selection of elite and inferior solutions for different purposes. Opposition-based learning, mutation strategies, and the revised strategy of inferior solutions based on reinforcement learning feedback play crucial roles in three regions. Population diversity and convergence rate are balanced.
- The revised strategy of the inferior solutions and individual regeneration mechanism is designed for the specific phenomenon during evolution. The revised strategy of the inferior solutions strengthens individuals with small Q values and high density and avoids ignoring forgotten solutions and premature convergence. Individual regeneration mechanism based on the Cholesky decomposition is an effective method to generate new individuals when fitness is not updated for successive generations.
- The dynamic adaptive adjustment strategy for multiple parameters is introduced based on specific individual knowledge and problem characteristics to form a flexible "local conditions" scheme, which improves the search efficiency and the reliability of the proposed algorithm.

The remainder of this paper is organized as follows. Section 2 summarizes the literature review. Section 3 introduces a knowledge-driven co-evolutionary algorithm assisted by a cross-regional interactive learning mechanism. The experimental settings and analysis are demonstrated in Section 4. The conclusion is drawn in Section 5.

## 2. Literature review

Swarm intelligence optimization algorithms exhibit outstanding performance in solving complex continuous and engineering optimization problems (Gupta et al., 2021; Aye et al., 2019; Yildiz et al., 2022c).

The classical DE with various mutation strategies has been studied by researchers, and a variety of variants are derived to achieve excellent effects. (Zhang and Sanderson, 2009) proposes an adaptive DE with an optional external archive (JADE), and the DE/current-to-pbest/1 strategy is employed to adaptively update the control parameters and invoke historical data in an external archive, improving the population diversity and convergence rate. (Tanabe and Fukunaga, 2013) proposes a new parameter adaptation technique for DE, named SHADE, which employs a historical memory to select future control parameters. An extension of SHADE proposed by (Tanabe and Fukunaga, 2014), known as LSHADE, decreases the population size according to a linear function. All the aforementioned variations of DE show splendid performance and are compared in various literature.

Novel EDA variants proposed in recent years achieve excellent effects. (Wu et al., 2016) introduces a new DE variant named multi-population ensemble DE (MPEDE), which consists of three mutation strategies, i.e., "current-to-pbest/1", "current-to-rand/1" and "rand/1" for three equally sized indicator subpopulations. (Li et al., 2023) presents a mutation operator selector and a parameter selector through the fitness landscape (FL), and the relationship between the FL and operators is analyzed by two different methods. (Yu et al., 2022) implements a constrained multi-objective DE by considering the selection pressure, and ranking the population based on the non-dominated crowd sort and constrained dominated principle. (W. Wang et al., 2022) studies a two-phase DE based on an archive-based comparison strategy and the dynamical resource allocation. (Zeng et al., 2022) designs a best-discarded vector selection strategy with an external archive for an individual. Based on the classical DE, several variants with excellent performance have emerged by combining multiple variants or parameter adaptive strategies. However, the characteristics of the specific problem and the strategic interaction are not fully explored.

The generation solution of EDA includes four steps (Martínez-López
et al., 2021): initialization, selection, modeling, and individual generation. A population is generated randomly in the initialization stage. Three selection techniques are commonly utilized in the selection process: proportional selection, competitive selection, and truncated selection. In this paper, the truncated selection is employed to construct the probabilistic model by selecting $\varepsilon=\tau \times N P$ individuals with the top fitness. This is followed by the modeling. Probabilistic models integrate excellent information, and are updated constantly with each generation. Ultimately, new individuals are generated. The process is repeated until the convergence condition is met. The improvement of the probability model and the perfection of population diversity combined with other strategies are the common methods to improve EDA (Du et al., 2022; Ren et al., 2018) introduces a novel anisotropic adaptive variance scaling (AAVS) technique, which anisotropically scales the variances along different eigendirections to tune the main search direction, and adopts an auxiliary global monitor to ensure convergence. (Dang et al., 2022) presents an efficient mixture sampling model (EMSM) by exploring more promising regions, which achieves a good trade-off between diversity and convergence. Although the above research is preeminent, the performance of a single algorithm is always limited in some aspects.

Another popular and promising means of improving performance is incorporating various intelligent optimization algorithms with the superiority of each algorithm (Shi et al., 2022). The collaboration between the EDA and DE is representative. (Liao et al., 2019) presents a hybrid DE with EDA by the random walk mutation to preserve the population diversity, and the EDA is employed to accelerate the convergence. (Fang et al., 2018) develops a novel algorithm, named the DE/GM, which utilizes both crossover/mutation operators from the DE and a Gaussian probabilistic model-based operator from the EDA for offspring generation. (Zhou and Tan, 2020) studies a discrete supermarket location problem that considers the utilization rate and capacity constraint of the
![img-0.jpeg](img-0.jpeg)

Fig. 1. The main idea of KCACIL.

![img-1.jpeg](img-1.jpeg)

Fig. 2. The flow chart of KCACIL.
supermarkets by a self-adaptive EDA with a differential DE. In (Zhou and Tan, 2020), a hybrid DE with EDA using an ensemble model is studied to minimize the total weighted completion time for a reentrant hybrid flow shop scheduling problem.

The performance of the algorithms is related to exploration and exploitation in the search space (Zhao et al., 2022a). Exploration finds the potential area where the optimal solution is located and involves searching over a large range. Exploitation focuses on the precise location and a refined search over a small area (Khishe, 2020). If the exploration is emphasized excessively, it improves the potential to find the optimal solution but ignores the accuracy of the generated solutions. In contrast, the candidate solutions are refined when only the exploitation is focused. However, the opportunity to seek high-quality solutions from the global area is abandoned, and the search falls into the local optimum. Exploration is vital during the early stage of the algorithms, and refined exploitation is paid more attention during the later evolution (Givi and Hubalovska, 2023). Hence, the trade-off between exploration and exploitation is essential to achieve promising effects. The design of a reasonable algorithm framework and efficient rules are indispensable and challenging (Karaduman et al., 2019).

Dynamic adaptive adjustment of key parameters is beneficial for exploration and exploitation. (Liao et al., 2023a) presents a knowledge transfer-based adaptive DE that carries out parameter adaptation with niching level and knowledge transfer between two niching techniques to balance diversity and convergence. Reasonable individuals are selected for the transfer to overcome the deficiencies of crowding and speciation. (Huynh et al., 2021) implements the Q-learning DE, which integrates the Q-learning model into the DE to adaptively adjust the control parameters of the algorithm at each iteration for different search domains. (Wei et al., 2020) presents a PSO variant based on multiple adaptive strategies (MAPSO) with an adaptive strategy for the population size. (Liao et al., 2023b) develops a neighborhood information-based adaptive DE with a dynamic neighborhood size mechanism and a novel mutation strategy. (Xiong et al., 2023) develops an enhanced neighborhood-based
speciating DE with adaptive control parameters, an external archive, and a crowding relieving mechanism to solve multimodal optimization problems. The aforementioned research shows that parameter adaptation is helpful for exploration and exploitation and saves computational resources. However, multiple-parameter adaptive strategies combined with diverse mechanisms to fully achieve automatic configuration based on various stages is rare.

Various literature introduces the learning mechanisms, adjustment methods, or parameter adaptive strategies, perhaps solely or partly. Moreover, the specific problem knowledge is not sufficiently extracted. Knowledge is power. The proposed KCACIL excavates knowledge and designs the corresponding learning mechanisms and improved solution strategies. The implicit knowledge of the fitness landscape, three regional features, parameters, and individual distance is embedded into the problem from the perspective of the evolutionary search. An interactive learning mechanism across three regions based on a self-feedback strategy is introduced in this paper. A comprehensive collaboration framework with diverse algorithms, strategies, and individuals is designed. Reinforcement learning combined with diversified knowledge, the elite strategy with multiple characteristics, and inferior information are applied to the evolution process, which provides a promising novel method to improve the performance of the proposed algorithm.

## 3. A knowledge-driven co-evolutionary algorithm assisted by a cross-regional interactive learning mechanism (KCACIL)

### 3.1. The framework of KCACIL

The performance of the algorithms is limited when the methods of generating solutions are only based on certain fixed rules. Various problems arise such as the imbalance between exploration and exploitation, rapid loss of population diversity, premature convergence, and low accuracy of solutions. The proposed KCACIL extracts the

complementary superiority and remedies the respective weaknesses of DE and EDA macroscopically. It is not merely a simple collaboration of two algorithms but is based on specific problem characteristics. The interactive learning with the elite strategy of three regions combines the implicit knowledge, which reflects the additional information of the optimization problems. The design of a knowledge-driven collaborative algorithm enables the KCACIL to fully explore the knowledge of the evaluation function, implicit parameter, cross-regional individual information, and characteristics of different evolutionary stages. Furthermore, opposition learning and the revised strategy of inferior solutions are integrated with reinforcement learning to achieve comprehensive collaboration. Fig. 1 shows the main idea of the proposed KCACIL.

Algorithm 1. KCACIL

The population is partitioned based on the distance. Various mutation strategies with Gaussian or Cauchy distribution and interaction mechanisms with diverse elite individuals are designed to accomplish self-learning, self-interaction, and cross-regional interaction in the three regions based on the problem characteristics. Effective knowledge transfer is achieved. When the mutation is successful with a small fitness value, a self-feedback strategy is implemented to enhance the impact of these parameters. Simulated annealing and $\epsilon-$ greedy are introduced into reinforcement learning to select various types of $Q$ values to avoid premature convergence caused by greedy selection. The feedback knowledge of the optimal state value function in reinforcement learning is refined in the interaction mechanism, opposition-based learning, and the revised strategy of the inferior solutions collaboratively as an operation conducive to improving the holistic performance of KCACIL.

Opposition learning is designed for individuals with non-ideal values in reinforcement learning. The revised strategy of the inferior solutions

```
Input: \(\quad \tau, N P_{\text {total }}, G_{\max }, D, \zeta, U_{d}, L_{d}\)
Output: The best individual and fitness.
Initialize the population according to Eq. (3).
For \(i=1,2, \cdots, N P_{\text {total }}\)
    Calculate the distance according to Eq. (1), and sort them;
    Divide three regions evenly with \(N P=N P_{\text {total }} / 3 ;\)
End for
While the stop condition is not satisfied do
    For \(i=1,2, \cdots, N P / /\) when the enhancement region
        Select \(p\) individuals with the smallest fitness values;
        Perform the operations of the enhancement region as shown in Algorithm 4;
        Perform reinforcement learning as Algorithm 2;
        Perform opposition-based learning as Algorithm 3;
        Perform the revised strategy of the inferior solutions as Algorithm 5;
    End for
    For \(i=N P+1, N P+2, \cdots, 2 N P / /\) when the stabilization region
        Select \(p\) individuals with the smallest fitness in this region and ones with the smallest distances from the best in the
        enhancement region;
        Perform the operations for the stabilization region as shown in Algorithm 4;
        Perform the operations for the stabilization region as shown in steps 10-12;
    End for
    For \(i=2 N P+1,2 N P+2, \cdots, N P_{\text {total }} / /\) when the attenuation region
        Select \(p\) individuals with the biggest \(Q_{g}\) in these regions;
        Perform the operations for the attenuation region as shown in Algorithm 4;
        Perform the operations for the attenuation region an shown in steps 10-12;
    End for
    If fitness is not updated continuously
        Generate \(M\) according to Eq. (47);
        Generate \(R\) based on \(N(0,1)\);
        Update \(\eta(g)\) according to Eqs. (49)-(52);
        Generate new individuals according to Eq. (48);
    End if
    Merge all individuals in these regions.
    Calculate the fitness values.
    Calculate \(\sigma^{2}\) according to Eq. (53). // The exploitation stage
If \(\sigma^{2}<\vartheta\)
    Sort all the fitness values;
    Select \(\tau * N P\) dominant individuals for EDA modeling; // The local search
    Calculate the mean \(\mu_{i} ;\)
    Calculate \(\delta_{i}\) according to Eq. (54);
    Generate new individuals according to Eq. (55);
End if
\(g=g+1\).
End while
```

is presented for the individuals with the minimum $Q$ value easy to be forgotten, as well as ones with a large density degree based on distance. The individual regeneration mechanism based on the Cholesky decomposition is introduced to address the specific phenomenon that population stagnation occurs during evolution. The dynamic adaptive adjustment strategies of the multi-parameters are adopted in the whole process, and the flexible "local conditions" scheme is achieved to balance diversity and convergence. When the condition of the exploitation stage is satisfied, EDA local search is performed for the refined search. The pseudocode of KCACIL and its flowchart are shown in Algorithm 1 and Fig. 2, respectively.

### 3.2. Strategy composition of KCACIL

### 3.2.1. Partition of three regions

Population diversity determines exploration and considerably influences the accuracy and convergence rate of the algorithms. Crossregional coevolution is introduced to achieve interaction and share specific knowledge in various regions. Population diversity is maintained.

Three regions are divided according to the distance between the individuals and the elite, where the distance is calculated as Eq. (1). The regions where the nearest and farthest $1 / 3$ individuals are located are defined as the enhancement and attenuation regions, respectively. The remaining region is named the stabilization region.
$d\left(X_{i}, X_{\text {best }}\right)=\left\|X_{i}-X_{\text {best }}\right\|, i \in\{1,2, \cdots, N P\}$
$N P=N P_{\text {total }} / 3$
where $X_{\text {best }}$ is the elite solution with the lowest fitness value, $X_{i}$ is the $i$ th individual, $N P$ is the number of individuals in each region, and $N P_{\text {total }}$ is the total population size.

### 3.2.2. Improved DE

The individuals iterate to produce favorable solutions. The DE mainly involves four stages: initialization, mutation, crossover, and selection (Su et al., 2022).
(1) Initialization stage

The initial population is generated randomly according to Eq. (3). $X_{i, k}=X_{k}^{\min }+\operatorname{rand}(0,1)\left(X_{k}^{\max }-X_{k}^{\min }\right), i=\{1,2, \cdots, N P\}, k=\{1,2,3\}$
where $\operatorname{rand}(0,1)$ is any random number between $(0,1)$, and $X_{k}^{\max } \operatorname{and} X_{k}^{\min }$ represent the individuals with the maximum and minimum fitness in the $k$ th region, respectively.
(2) Mutation operation

The DE/current-to-pbest/1 mutation strategy is adopted and improved further.
$V_{i, k}^{g}=X_{i, k}^{g}+F_{i, k}^{g}\left(X_{\text {best }, k}^{g, g}-X_{i, k}^{g}\right)+F_{i, k}^{g}\left(X_{i, k}^{g, g}-X_{i, k}^{g}\right)$
where $g=\{1,2, \cdots, G_{\max }\}$ represents the number of iterations, $G_{\max }$ represents the maximum number of iterations, $X_{\text {best }, k}^{g, g}$ represents the first $100 p \%$ of the best individuals in the $k$ th region at the $g$ th generation, $X_{i, k}^{g, g}$ and $X_{i, k}^{g}$ are the randomly selected individuals varying from $X_{i, k}^{g}$ in the $k$ th region at the $g$ th generation, and $F_{i, k}^{g}$ is a mutation operator in the scope $(0,1)$.

The setting of $F_{i, k}^{g}$ is a key to the mutation. The traditional DE has low accuracy because its search consumes plentiful computing resources and it is difficult to find the potential region where the optimal solution is distributed. Various mutation strategies with diverse characteristics are
designed according to the specific characteristics of the three regions in this paper.
(3) Crossover method

The target individual $X_{i}^{g}$ and the mutant one $V_{i}^{g+1}$ are crossed to obtain $U_{i}^{g+1}$.
$U_{i}^{g+1}=\left\{\begin{array}{c}V_{i}^{g+1}, \text { rand, } \leq C_{r}, \text { or } j=\text { jrand } \\ X_{i}^{g}, \text { otherwise }\end{array}\right.$
where $U_{i}^{g+1}$ is the trail vector, $C_{r}$ is the crossover rate, $C_{r} \in[0,1]$, and jrand represents a random number between $(0,1)$. This operation causes the trail individual to randomly pass information from t $X_{i}^{g}$ and $V_{i}^{g+1}$ to the next generation with at least one dimension of $U_{i}^{g+1}$ containing information from $V_{i}^{g+1}$.
(4) Selection process
$X_{i}^{g+1}=\left\{\begin{array}{c} U_{i}^{g}, f\left(U_{i}^{g}\right) \leq f\left(X_{i}^{g}\right) \\ X_{i}^{g}, \text { otherwise }\end{array}\right.$
Individuals with the lowest fitness values are selected for subsequent iterations through the selection process.
3.2.2.1. Update of mutation and crossover operators. Fixed parameter settings can not be adapted dynamically for various problems or evolution stages. Encoding the best combinations of operators at different generations into an individual is beneficial. $F_{i}$ and $C_{r}$ have a considerable influence on the algorithm. $F_{i}$ controls the vector deviation. When $F_{i}$ is large, exploration is emphasized, otherwise, exploitation is promoted. Different distributions also affect exploration and exploitation. The Gaussian and Cauchy distributions possess disparate characteristics (Li et al., 2019). Compared with the Gaussian distribution, the Cauchy distribution owns a longer tailing, which augments the search scope, and contributes to exploration. The premature convergence caused by the greedy strategy is retarded. The Gaussian distribution is used for exploitation. In addition, the Lehmer mean is larger than the conventional mathematical mean in favor of propagation to future generations.

The stabilization and attenuation regions require high exploration. Diverse distribution characteristics of parameter settings and mean calculation methods are designed based on specific regional knowledge.
3.2.2.2. Setting of $p$. According to the specific knowledge of the three regions, the dynamic adaptive adjustment of $p$-value elevates the search efficiency. The first $100 p \%$ excellent individuals are selected to enter the next iteration based on the current-to- $p$ best/1 mutation strategy. The value of $p$ is improved according to Eq. (7).
$p_{k}=\left(1-\frac{\sum_{i=1}^{n p} f\left(x_{i, k}\right)}{\sum_{k}^{n p} \sum_{i=1}^{n p} f\left(x_{i, k}\right)}\right)^{2}, k \in\{1,2,3\}$
The $p$-value of the enhancement region is large in the early stage of evolution, and more excellent individuals are extracted from this region. With the progress of iteration, more and more excellent individuals are extracted from the stabilization and attenuation regions. Consequently, the individuals in the regions evolve rapidly.

### 3.2.3. Reinforcement learning

The $Q$ value in reinforcement learning is the basis of interactive learning for different types of individuals. The evaluation of $Q$ value enables the opposition-based learning (in Section 3.2.4), the elite-guided mutation strategy (in Section 3.2.5), and the improvement strategy of

Table 1
ANOVA results for the parameter settings of KCACIL.

| Source | Sum Sq. | d.f. | Mean Sq. | F-ratio | p -value |
| :--: | :--: | :--: | :--: | :--: | :--: |
| $N P_{\text {total }}$ | $3.42 \mathrm{E}+03$ | 3 | $1.14 \mathrm{E}+03$ | 5.73 | 0.0013 |
| $\tau$ | $7.61 \mathrm{E}+02$ | 3 | $2.54 \mathrm{E}+02$ | 1.28 | 0.2885 |
| $\theta$ | $2.60 \mathrm{E}+02$ | 3 | $8.67 \mathrm{E}+01$ | 0.44 | 0.7280 |
| $\zeta$ | $9.52 \mathrm{E}+02$ | 3 | $3.17 \mathrm{E}+02$ | 1.59 | 0.1973 |
| $N P_{\text {total }}+\tau$ | $2.42 \mathrm{E}+03$ | 9 | $2.69 \mathrm{E}+02$ | 1.35 | 0.2244 |
| $N P_{\text {total }}+\theta$ | $2.27 \mathrm{E}+03$ | 9 | $2.52 \mathrm{E}+02$ | 1.26 | 0.2688 |
| $N P_{\text {total }}+\zeta$ | $9.86 \mathrm{E}+02$ | 9 | $1.10 \mathrm{E}+02$ | 0.55 | 0.8331 |
| $\tau+\theta$ | $2.21 \mathrm{E}+03$ | 9 | $2.46 \mathrm{E}+02$ | 1.24 | 0.2853 |
| $\tau+\zeta$ | $2.94 \mathrm{E}+03$ | 9 | $3.27 \mathrm{E}+02$ | 1.64 | 0.0473 |
| $\theta+\zeta$ | $2.08 \mathrm{E}+03$ | 9 | $2.31 \mathrm{E}+02$ | 1.16 | 0.3319 |
| $N P_{\text {total }}+\tau+\theta$ | $6.69 \mathrm{E}+03$ | 27 | $2.48 \mathrm{E}+02$ | 1.24 | 0.2241 |
| $N P_{\text {total }}+\tau+\zeta$ | $6.54 \mathrm{E}+03$ | 27 | $2.42 \mathrm{E}+02$ | 1.22 | 0.2475 |
| $N P_{\text {total }}+\theta+\zeta$ | $6.26 \mathrm{E}+03$ | 27 | $2.32 \mathrm{E}+02$ | 1.16 | 0.3319 |
| $\tau+\theta+\zeta$ | $6.40 \mathrm{E}+03$ | 27 | $2.37 \mathrm{E}+02$ | 1.19 | 0.2702 |
| Error | $1.61 \mathrm{E}+04$ | 81 | $1.99 \mathrm{E}+02$ |  |  |
| Total | $6.11 \mathrm{E}+04$ | 255 |  |  |  |

inferior solutions (in Section 3.2.6) to play a role in the collaboration and interaction between various mechanisms.

The purpose of reinforcement learning is to maximize the total reward (Chen et al., 2021). As evolution is a continuous learning process, the discount factor $\gamma$ emphasizes the contribution of different iterations to the total reward. Therefore, $\gamma$ does not take a fixed value, but an adaptive update, as shown in Eq. (8). Reinforcement learning considers $Q$ as the learning objective. $Q$ is defined as Eq. (9).
$\gamma=0.5 \times\left(0.9-0.6 \times \frac{g}{G_{\max }}\right)$
where $T_{0}$ is the initial temperature with the maximum value, $T_{\min }$ is the minimum, and $\theta \in[0,1]$ represents the annealing factor.

The $\varepsilon$ is defined by the dynamic temperature and the difference between $Q$ values. The decreasing temperature causes $\varepsilon$ to reduce gradually with the iteration. This strategy avoids falling into the local optimum due to the excessive selection of individuals with large $Q$ values. The evolutionary process is continuously affected by the total reward feedback to the population, and interactive learning with environmental perception is formed. The pseudocode of reinforcement learning is shown in Algorithm 2.

Algorithm 2. Reinforcement learning

```
Obtain \(\gamma\) according to Eq. (8).
Calculate the distances according to Eq. (10), and obtain \(R_{g}\).
Calculate \(Q_{g}\) according to Eq. (9).
Sort the solutions based on \(Q_{g}\).
Employ \(\varepsilon\) - greedy and Simulated Annealing to update \(\varepsilon\) according to Eqs. (11)-(13).
If \(\operatorname{rand}(0,1)<\varepsilon\)
Select the individuals randomly.
    else
    Select the individuals with big \(Q_{g}\).
End if
```

$Q_{g} \leftarrow Q_{g}+\alpha\left[R_{g+1}+\gamma \times \Delta Q_{g+1}\right]$
where $\alpha$ is the learning rate, and $R_{g}$ is the reward at the $g$ generation.
$R_{g}$ is set according to the distance based on the following principle.
First, the distance between the individuals and the best individual in each region is defined as Eq. (10).
$L\left(X_{i, k}, X_{b \in o t, k}\right)=\left\|X_{i, k}-X_{b \in o t, k}\right\|, k=\{1,2,3\}$
$R_{g}$ is obtained by the reward or punishment based on the comparison of the distance. The smaller $R_{g}$ is, the further the individuals are from the best one. The selection of individuals with large $R_{g}$ leads to fall into the local optima. The $\varepsilon$-greedy strategy and simulated annealing are introduced to adjust dynamically $\varepsilon$ according to Eqs. (11)-(13).
$T_{0}=T_{\max }$
$T_{g+1}=T_{\min }+\theta \times\left(T_{g}-T_{\min }\right)$
$\varepsilon=\exp \left(\frac{-\left(\Delta Q_{g}\right)}{T_{g}}\right)$
The first step obtains $\gamma$ according to Eq. (8). In Step 2, distance is calculated in Eq. (10), and $R_{g}$ is acquired. In Step 3, $Q_{g}$ is acquired according to Eq. (9). In Step 4, the solutions are sorted based on $Q_{g}$. Step 5 is that $\varepsilon$-greedy and simulated annealing are employed to update $\varepsilon$. In Steps 6-10, if any random number between $(0,1)$ is less than $\varepsilon$, an individual is selected randomly, otherwise, the individual with a large $Q_{g}$ is appropriate.

### 3.2.4. Opposition-based learning

The mutation strategy guided by the elite improves the convergence rate. Opposition-based learning generates the reverse individuals to increase the population diversity (Mandavi et al., 2018). Both strategies stimulate population evolution along the potential direction. The quadratic reverse reflection has significant advantages in exploration compared with other opposition-based learning methods.
$X$ is a point in $n$ dimensional space, $X=\left\{x_{1}, x_{2}, \cdots, x_{n}\right\}$, where $x_{i}$ belongs to $\left(x_{\min }, x_{\max }\right)$. The reverse point of $X$ is $\bar{X}=\left\{\bar{x}_{1}, \bar{x}_{2}, \cdots, \bar{x}_{n}\right\}$ as shown in Eq. (15). The secondary reverse point for $X$ is $\bar{X}=\left\{\bar{x}_{1}^{\prime}, \bar{x}_{2}^{\prime}, \cdots\right.$, $\left.\bar{x}_{n}^{\prime}\right\}$ in Eq. (16). The secondary reverse reflection point of $X$ is $\bar{X}^{\prime}=\left\{\bar{x}_{1}^{\prime}\right.$, $\left.\bar{x}_{2}^{\prime}, \cdots, \bar{x}_{n}^{\prime}\right\}$ in Eq. (17).

$\dot{x}_{i}^{\prime}=x_{\text {max }}+x_{\text {min }}-x_{i}$
$x_{i}^{\mathrm{d}}=\left(x_{\text {max }}+x_{\text {min }}\right) / 2$
$\dot{x}_{i}^{\prime}=\operatorname{rand}\left(x_{i}^{\mathrm{d}}, \dot{x}_{i}^{\prime}\right)$
$\dot{x}_{i}^{\prime}=\operatorname{rand}\left(\dot{x}_{i}^{\prime}, \dot{x}_{i}^{\prime}\right)$
where $\operatorname{rand}\left(x_{i}^{\mathrm{d}}, x_{i}^{\prime}\right)$ is a random number between $x_{i}^{\mathrm{d}}$ and $x_{i}^{\prime}$, and $\operatorname{rand}\left(\dot{x}_{i}^{\prime}, \dot{x}_{i}^{\mathrm{d}}\right)$ is that between $\dot{x}_{i}^{\prime}$ and $\dot{x}_{i}^{\mathrm{d}}$.

The reverse population generates better solutions for the stabilization and attenuation regions and expands the search scope for the enhancement region, which increases the population diversity. The pseudocode of opposition-based learning is shown in Algorithm 3. First, the individuals with small Q values are selected. Subsequently, the secondary reversal reflection points are generated according to Eqs. (14), (16) and (17). Specifically, the new solution is substituted into the fitness function. If the fitness value is less than that of the original solution, the new solution replaces the original one. Otherwise, the original solution is retained.

Algorithm 3. The opposition-based learning
sharing diverse types of dominant knowledge because exploring the regions where the dominant solutions exist creates more chances to find the optimal solution.

The individuals in the enhancement region are guided by the selflearning and elite strategy and utilize the optimal knowledge to implement self-learning, self-evolution, and self-interaction. The collaborative guidance of the elite from the enhancement region is integrated into the stabilization region through the interaction of mutual learning and self-learning. The cross-regional interactive guidance in the attenuation region is adopted to achieve comprehensive collaboration.
3.2.5.2. Update of parameters in the three regions. The enhancement region emphasizes exploitation. The stabilization region calls for the appropriate degree of exploration and exploitation, and the attenuation region is relatively more focused on exploration. In light of this consideration, the parameters of the three regions are updated according to different modes.

An individual with a lower fitness value after mutation is deemed to be successful. The corresponding parameter setting and strategy are taken as excellent configurations. The dominant individuals are generated through self-feedback, which should be maintained and propagated in subsequent iterations to reinforce the impact of dominant knowledge.

```
1 Select \(\tau \star N P\) individuals with small \(Q\) values by reinforcement learning.
2 Generate the reversal point \(X_{I}^{\prime}\) according to Eq. (14).
3 Generate the secondary reversal point \(X_{I}^{\prime \prime}\) according to Eq. (16).
4 Generate the secondary reversal reflection point \(X_{I}^{\prime \prime \prime}\) according to Eq. (17).
5 If \(f\left(X_{I}^{\prime \prime \prime}\right)<f\left(X_{I}\right)\)
6 \(\quad X_{I}=X_{I}^{\prime \prime \prime}\)
7 else
8 \(\quad X_{I}=X_{I}\)
9 End if
```


### 3.2.5. Cross-regional collaborative mutation strategy

3.2.5.1. Dynamical resources configuration across regions. The implicit knowledge of the three regions is different. Individuals with diverse characteristics guide co-evolution and information sharing within and across the regions to achieve effective interaction and knowledge transfer. Different mutation strategies possess various search characteristics and evolutionary directions. In light of the specific characteristics of the individuals in three regions, the appropriate mutation strategies are customized efficiently balance exploration and exploitation, which is key for KCACIL.

The DE guides the evolution direction based on three parameters: $F_{I}$, $C_{T}$, and $N P$. The mutation strategies of the enhancement, stabilization, and attenuation regions are shown in Eqs. (18)-(20), respectively.
$V_{i, 1}^{\mathrm{d}}=X_{i, 1}^{\mathrm{d}}+F_{i, 1}\left(X_{\text {min }, 1}^{\mathrm{d}, \mathrm{d}}-X_{i, 1}^{\mathrm{d}}\right)+F_{i, 1}\left(X_{i, 1}^{\mathrm{d}}-X_{i, 2,1}^{\mathrm{d}}\right)$
$V_{i, 2}^{\mathrm{d}}=X_{i, 2}^{\mathrm{d}}+F_{i, 2}\left(X_{\text {min }}^{\mathrm{d}, \mathrm{d}}\left(\lambda\left(x_{i, 1}-X_{\text {min }, 1}\right)\right)-X_{\text {min }, 2}-X_{i, 2}^{\mathrm{d}}\right)+F_{i, 2}\left(X_{i, 2}^{\mathrm{d}}-X_{i, 2}^{\mathrm{d}}\right)$
$V_{i, 3}^{\mathrm{d}}=X_{i, 3}^{\mathrm{d}}+F_{i, 3}\left(X_{\text {min } 2}^{\mathrm{d}, \mathrm{d}}-X_{i, 3}^{\mathrm{d}}\right)+F_{i, 3}\left(X_{i, 2,3}^{\mathrm{d}}-X_{i, 3,3}^{\mathrm{d}}\right)$
where $X_{\text {min }, 1, \left(X_{i, 1}-X_{\text {min }, 1}\right) \backslash, X_{\text {min }, 2}}$ represents the individuals nearest to the best one in the enhancement region and the elite from the stabilization region, and $X_{\text {min } 2}^{\mathrm{d}, \mathrm{d}}$ represents the first $100 \mathrm{p} \%$ individuals with large Q values.

The mutation strategies guided by the elite combine knowledge within and across three regions to achieve comprehensive cross-regional interaction and information sharing. The solution quality is improved by

The elitist-guided strategies and diverse mutation mechanisms based on regional characteristics achieve a trade-off between diversity and greed.
(1) Parameter update in the enhancement region
$\left\{\begin{array}{c}F_{i, 1} \in \operatorname{randn}_{1}\left(\mu_{F_{i}}, 0.1\right) \\ C r_{i, 1} \in \operatorname{randn}_{1}\left(\mu_{C r_{i}}, 0.1\right)\end{array}\right.$
$\left\{\begin{array}{c}F_{i+1,1}=c \times F_{i+1,1}+(1-c) F_{i, 1} \\ C r_{i+1,1}^{\prime}=c \times C r_{i+1,1}+(1-c) C r_{i, 1}\end{array}\right.$
$c=0.9-0.9 \times 10^{-5} \times \frac{g}{G_{\max }}$
$\mu_{F_{i}}=(1-c) \mu_{F_{i}}+c \times \operatorname{mean}_{A}\left(\omega, F_{i, 1}\right)$
$\mu_{C r_{1}}=(1-c) \mu_{C r_{1}}+c \times \operatorname{mean}_{A}\left(\omega, C r_{i, 1}\right)$
$\omega_{1}=\frac{\Delta f i c}{\sum_{F_{i, 1} \in \mathrm{P}} \Delta f i c}$
where $\operatorname{mean}_{A}(\bullet)$ represents the arithmetic mean.
The smaller values of $F_{i}$ and $C r_{i}$ contribute to exploitation. $F_{i, 1}$ and $C r_{i, 1}$ follow the Gaussian distribution in this region. The contribution of various parameters is especially strengthened. The difference in the fitness values is considered the weight coefficient. The mean is calculated based on the arithmetic average.
(2) Parameter update in the stabilization region

![img-2.jpeg](img-2.jpeg)

Fig. 3. Main effects plot and interaction plot of parameters by ANOVA and Tukey HSD.
$\left\{\begin{array}{l}F_{1,2} \in \operatorname{randc}_{1}\left(\mu_{F_{2}}, 0.1\right) \\ C_{1,2} \in \operatorname{randn}_{1}\left(\mu_{C_{2}}, 0.1\right)\end{array}\right.$
$\left\{\begin{array}{c}F_{i+1,2}=c \times F_{i+1,2}+(1-c) F_{i, 2} \\ C_{i+1,2}=c \times C_{i+1,2}+(1-c) C_{i, 2}\end{array}\right.$
$\mu_{F_{2}}=(1-c) \mu_{F_{2}}+c \times \operatorname{mean}_{L}\left(\omega_{1} F_{1,2}\right)$
$\mu_{C_{2}}=(1-c) \mu_{C_{2}}+c \times \operatorname{mean}_{A}\left(\omega_{1} C_{1,2}\right)$
$\operatorname{mean}_{L}\left(\omega_{1} F_{1,2}\right)=\frac{\sum \omega_{1} F_{1,2}^{2}}{\sum \omega_{1} F_{1,2}}$
Considering the characteristics of the stabilization region, $F_{1}$ obeys the Cauchy distribution. The Lemmer mean $\operatorname{mean}_{L}\left(\omega_{1} * F_{1,2}\right)$ is introduced to stimulate a certain degree of exploration, and $C_{1}$ follows the Gaussian distribution. The arithmetic mean is employed to achieve a reasonable level of exploitation.
(3) Parameter updating in the attenuation region
$\left\{\begin{array}{l}F_{1,3} \in \operatorname{randc}_{1}\left(\mu_{F_{3}}, 0.1\right) \\ C_{1,3} \in \operatorname{randc}_{1}\left(\mu_{C_{3}}, 0.1\right)\end{array}\right.$
$\left\{\begin{array}{c}F_{i+1,3}=c \times F_{i+1,3}+(1-c) F_{i, 3} \\ C_{i+1,3}=c \times C_{i+1,3}+(1-c) C_{i, 3}\end{array}\right.$
$\mu_{F_{3}}=(1-c) \mu_{F_{3}}+c \times \operatorname{mean}_{L}\left(\omega_{1} F_{1,3}\right)$
$\mu_{C_{3}}=(1-c) \mu_{C_{3}}+c \times \operatorname{mean}_{L}\left(\omega_{1} C_{1,3}\right)$
$\operatorname{mean}_{L}\left(\omega_{1} F_{1,3}\right)=\frac{\sum \omega_{1} F_{1,3}^{2}}{\sum \omega_{1} F_{1,3}}$
$\operatorname{mean}_{L}\left(\omega_{1} C_{1,3}\right)=\frac{\sum \omega_{1} C_{1,3}^{2}}{\sum \omega_{1} C_{F_{1,3}}}$
$F_{i}$ and $C_{i}$ are subject to Cauchy distribution. The Lemmer mean is utilized to explore the knowledge, and the difference in the fitness values is considered as the weight coefficient.

In each region, $\varphi$ and $\varphi$ represent the average fitness values before and after crossover at each generation, and are calculated according to Eqs. (38) and (39), respectively. If Eq. (40) is satisfied, the mutation is successful, and the self-feedback for $F_{1}$ and $C_{1}$ is executed. The selffeedback of the three areas is implemented according to Eqs. (22), (28) and (33), respectively. Otherwise, it is executed based on Eqs. (21), (27) and (32).
$\varphi=\frac{\sum_{i=1}^{20} F\left(X_{i}^{a}\right)}{N P}$
$\varphi=\frac{\sum_{i=1}^{60} F\left(U_{i}^{a}\right)}{N P}$
$\varphi<\varphi$

Algorithm 4. The improved DE for the enhancement/stabilization/ attenuation region

| 1 | Initial the population. |
| :--: | :--: |
| 2 | While the stop condition is not satisfied do |
| 3 | For $i=1,2, \cdots, N P / /$ when the enhancement region |
| 4 | For $i=N P+1, N P+2, \cdots, 2 N P / /$ when the stabilization region |
| 5 | For $i=2 N P+1,2 N P+2, \cdots, N P_{\text {total }} / /$ when the attenuation region |
| 6 | Sort the individuals; |
| 7 | Select $p$ dominant individuals according to Eq. (7); |
| 8 | Calculate $c$ according to Eq. (23); |
| 9 | Calculate $\omega_{1}$ according to Eq. (26); |
| 10 | Update $\mu_{F}, \mu_{\mathrm{Cr}}$ according to Eqs. (24)-(25); // just for the enhancement region |
| 11 | Update $\mu_{F}, \mu_{\mathrm{Cr}}$ according to Eqs. (29)-(31); // just for the stabilization region |
| 12 | Update $\mu_{F}, \mu_{\mathrm{Cr}}$ according to Eqs. (34)-(37); // just for the attenuation region |
| 13 | Perform the mutation according to Eq. (18); |
| 14 | Perform the cross-over according to Eq. (5); |
| 15 | Calculate and compare the fitness values; |
| 16 | Calculate $\varphi$ and $\varphi^{\prime}$ according to Eqs. (38)-(39); |
| 17 | If Eq. (40) is satisfied |
| 18 | Generate $F_{1}, C r_{1}$ according to Eq. (22); // just for the enhancement region |
| 19 | Generate $F_{1}, C r_{1}$ according to Eq. (28); // just for the stabilization region |
| 20 | Generate $F_{1}, C r_{1}$ according to Eq. (33); // just for the attenuation region |
| 21 | else |
| 22 | Generate $F_{1}, C r_{1}$ according to Eq. (21); // just for the enhancement region |
| 23 | Generate $F_{1}, C r_{1}$ according to Eq. (27); // just for the stabilization region |
| 24 | Generate $F_{1}, C r_{1}$ according to Eq. (32); // just for the attenuation region |
| 25 | End if |
| 26 | End for |
| 27 | $g=g+1$. |
| 28 | End while |
| 29 | Return the new individuals. |

The variance in both statistical distributions equals 0.1 . The flexible adaptive strategies are designed based on the specific problem characteristics to elevate the search efficiency and the reliability of KCACIL. The pseudocode of the improved DE for three regions is shown in Algorithm 4. Although different strategies are applied in each region, the ideas are similar, therefore, they are detailed in the same table. For the enhancement region, Steps 1-3, 6-10, 13-18, 21, 22, 25-29 are performed. Steps 1, 2, 4, 6-10, 13-17, 19, 21, 23, 25-29 are implemented for the stabilization region. Steps 1, 2, 5-9, 12-17, 20, 21, 24-29 are used for the attenuation region.

### 3.2.6. Revised strategy of the inferior solution

The inferior solutions with available knowledge are introduced into the evolutionary process. The possibility of ignoring the forgotten solutions is avoided. A large population density increases the risk of premature convergence. The individuals with small $Q$ values and excessive density are ameliorated. The individuals from the enhancement and stabilization regions are susceptible to falling into the local optimal by the greedy principle.

The average distance between the individuals and the regional centroid, as well as the average fitness value, are employed to compute the density of the individuals.
$m_{c}=\frac{\sum_{i=1}^{N P} X_{i}}{N P}$
$\bar{d}=\frac{\sum_{i=1}^{N P}\left\|X_{i}-m_{c}\right\|}{N P}$
$\Delta f=\frac{\sum_{i=1}^{N P}\left(f\left(X_{i}\right)-f\left(m_{c}\right)\right)}{N P}$
$D D=\Delta f\left(1+\frac{\lambda}{\bar{d}}\right)$
where $m_{c}$ is regional centroid, $\bar{d}$ is average distance, $\Delta f$ is average fitness difference, and $D D$ is distance density.

The individuals disperse at a partial bottom of the fitness landscape with small $\Delta f$ and big $\bar{d}$. If fitness differs greatly, the individuals are sparse. The density is higher when $\bar{d}$ is smaller. If $\lambda=0, D D=\Delta f . \Delta f$ has a minor effect with a large $\lambda, \lambda$ is vital to $D D$ for the balance of $\Delta f$ and $\bar{d}$. It is computed as Eq. (45).
$\lambda=\sqrt{\sum_{d=1}^{D}\left(\frac{U_{d}-L_{d}}{N P}\right)^{2}}$
where $D$ is the dimension, $L_{d}$ and $U_{d}$ are the lower and upper bounds. $\lambda$ is adjusted adaptively with the search space. Ameliorating individuals with small $Q$ values and high density can improve the quality. The solution with either characteristic is defined as inferior, denoted as $I_{i}$ in Eq. (46).
$I_{i}=I_{i}+\zeta\left(m_{c}-I_{i}\right), i \in\{1,2, \cdots, N P\}$
where $I_{i}$ is the $i$ th improvement solution, and $\zeta \in[0,1]$ controls the degree to which the inferior solution approaches the regional centroid.
Algorithm 5. The revised strategy of the inferior solutions

1 Calculate the centroid according to Eq. (41).
2 Calculate the average distances according to Eq. (42).
3 Calculate the average fitness increments according to Eq. (43).
4 Set $\lambda$ according to Eq. (45).
5 Calculate the density of individuals according to Eq. (44).
6 If $D D<10^{-5}$ or the individual with the smallest $Q$
7
8
The pseudocode for the revised strategy of the inferior solutions is shown in Algorithm 5. In Step 1, the centroid is calculated according to Eq. (41). Step 2 is that the average distance is obtained according to Eq. (42). The average fitness increment is calculated in Step 3. In Step 4, $\lambda$ is set according to Eq. (45). Steps 6-9 implement the revised strategy of the inferior solutions when the relevant conditions are met.

### 3.2.7. Individual regeneration mechanism

Given that the fitness values are not updated for several successive generations during the evolution process, the individual regeneration method is carried out in the following steps.
(1) The covariance matrix $C$ is generated by Cholesky decomposition into a lower-triangular one as Eq. (47).
$C=M \times M^{T}$
(2) An $1 \times D$ matrix $R$ is obtained by sampling the standard normal distribution $N(0,1)$.
(3) The new individuals are generated according to Eqs. (48)-(52).
$X^{\text {new }}=\mu+\eta(g) \times M \times R$
$\eta(g)=\eta_{\min }+\left(\frac{G_{\max }-g}{G_{\max }}\right)^{\beta}\left(\eta_{\max }-\eta_{\min }\right)$
$\eta_{\max }=\left(U_{d}-L_{d}\right) \times 0.01$
$\eta_{\min }=\eta_{\max } / 10$
$\beta=1-e^{-\left(\frac{1}{\sqrt{3}+\frac{1}{\max \alpha}}\right)}$
where $\eta(g)>1$ is the scaling factor, $\eta_{\max }$ and $\eta_{\min }$ represent the maximum and minimum values determined by the scale of the search space, $L_{d}$ and $U_{d}$ represent the lower and upper bounds, $G_{\max }$ is the maximum number of iterations, and $\beta$ is the non-linear correction parameter for $\eta$.

### 3.3. Exploitation stage of KCACIL

(1) Symbol of the exploitation stage

The population converges gradually with the iteration, and the differences between the fitness values are reduced. In this paper, the fitness variation of all individuals is employed to assess the population state, and considered as the symbol of the exploitation stage as shown in Eq. (53). A large $\sigma^{2}$ means that the population is searching randomly. When $\sigma^{2}<\vartheta(\vartheta=0.001)$, the exploitation stage takes precedence.
$\sigma^{2}=\sum_{i=1}^{N \pi}\left(\frac{f\left(x_{i}\right)-\bar{f}}{\max \left\{\max \left\{\left[f\left(x_{i}\right)-\bar{f}\right)\right\}, 1\right\}}\right)^{2}$
where $\bar{f}$ represents the average fitness of all individuals.
(2) EDA-based local search

The EDA is updated based on the probabilistic model such that the search space where the optimal solution is located is reached with a high selection probability (Liang et al., 2020). Specific knowledge is utilized to adjust the search strategy. The EDA is equipped with strong exploitation and speeds up convergence as a local search method (Bosman and Gallagher, 2018). The fitness values are small in the exploitation stage. The dominant solutions are highly concentrated. Subsequently, the local search is carried out based on the generated dominant solutions, which promotes convergence accuracy.

The local search is performed according to Eqs. (54) and (55). If the individuals are far away from the elite during the local search, $\delta_{i}$ is large. The search is carried out in an extended search range. If the distance is close, $\delta_{i}$ is small. The search in a contractible range ensures effective exploitation near the selected dominant solutions.
$X_{i}(g+1)=G a u s s i a n\left(\mu_{i}, \delta_{i}\right)$
$\delta_{i}=\mathrm{r}\left\|X_{\text {rec } i}-X_{i}(g)\right\|$

## 4. Experimental results and analysis

### 4.1. Experiments on the CEC 2017 Test Suite

The proposed KCACIL and the comparison algorithms are tested on the CEC 2017 test suite with 2 unimodal functions ( $f_{1}$ and $f_{5}$ ), 7 simple multimodal functions ( $f_{4}-f_{10}$ ), 10 hybrid functions ( $f_{11}-f_{20}$ ), and 10 composition functions $\left(f_{21}-f_{20}\right)$ (Awad et al., 2016). These functions own diverse characteristics and offer in-depth observations on the whole performance of KCACIL and the comparison algorithms. All experimental data are obtained by Matlab2016b on a PC with a 3.4 GHz Intel (R), Core (TM) i7-6700 CPU, 8 GB of RAM, and a 64-bit Operating System. According to the standard test suites, all experiments are run independently a total of 51 times to reduce statistical errors. The average values are evaluated at $10,30,50$, and 100 dimensions, denoted as 10 D , 30D, 50D, and 100D, respectively. The termination condition is $G_{\max }=$ $10000 \times D$. The values less than $10^{-8}$ are set to 0 . The material data can be downloaded at https://github.com/Znnalgorithms/KCACIL.git.

The classical competitive LSHADE (Tanabe and Fukunaga, 2014) and CMA-ES (Tong et al., 2019) are adopted to illustrate the effectiveness and superiority of KCACIL. In addition, considering that the current-to-pbest/1 mutation strategy is improved in KCACIL, JADE proposed by (Zhang and Sanderson, 2009) is also employed for comparison. The state-of-the-art collaborative algorithms DE/GM (Fang et al., 2018), IDE_EDA (Li et al., 2023), EA4eig (Bujok and Kolenovsky, 2022), JSO_CMA-ES_LBFGS (Zhao et al., 2022c), multi-population-based MPEDE (Wu et al., 2016), and an advanced variant AAVS_EDA (Ren et al., 2018), as well as the novel algorithms with learning mechanisms RLBSO (Zhao et al., 2022d), OLBSO (Ma et al., 2021), LDE (Sun et al., 2021), are selected for a comprehensive comparison. The experimental environment of all the algorithms is identical to guarantee fairness, and the parameters are set as the original literature. The performance is evaluated by the error between the obtained best solution and the optimum for each function.

Table 2
The results of KCACIL and 12 comparison algorithms (10D) for the CEC 2017 test suite.

| Fun |  | JADE | LSHADE | CMA-ES | AAVS_EDA | DE/GM | MPEDE | IDE_EDA | EAAvg | jSO_CMA-ES_LBFGS | RLBSO | OLBSO | LDE | KCACIL |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| F1 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 4.63E+03 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.36E+03 | 0.00E+00 | 0.00E+00 |  |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 3.31E+04 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.88E+03 | 0.00E+00 | 0.00E+00 |  |
| F3 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.83E-01 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.73E+03 | 0.00E+00 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.31E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.59E+03 | 0.00E+00 | 0.00E+00 |
| F4 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 3.14E+00 | 0.00E+00 | 2.28E-07 | 2.92E+00 | 0.00E+00 | 0.00E+00 | 1.02E+00 | 1.25E+01 | 2.03E-02 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.18E+00 | 0.00E+00 | 1.04E-06 | 9.91E-01 | 0.00E+00 | 0.00E+00 | 1.48E+00 | 1.79E+01 | 4.37E-02 | 0.00E+00 |
| F5 | Mean | 5.91E+00 | 2.38E+00 | 6.09E+01 | 1.85E+00 | 1.40E+00 | 6.12E+00 | 4.70E+00 | 9.17E-01 | 1.79E+00 | 1.06E+01 | 3.60E+01 | 5.71E+00 | 5.18E-01 |
|  | Std | 1.27E+00 | 8.22E-01 | 4.72E+01 | 1.03E+00 | 9.78E-01 | 1.56E+00 | 2.19E+00 | 9.72E-01 | 8.67E-01 | 4.29E+00 | 1.45E+01 | 1.40E+00 | 7.83E-02 |
| F6 | Mean | 1.96E-05 | 0.00E+00 | 5.51E+01 | 0.00E+00 | 0.00E+00 | 2.05E-05 | 2.75E-06 | 0.00E+00 | 0.00E+00 | 5.40E-03 | 7.57E+00 | 0.00E+00 | 0.00E+00 |
|  | Std | 6.38E-06 | 0.00E+00 | 8.74E+00 | 0.00E+00 | 0.00E+00 | 7.36E-06 | 9.83E-06 | 0.00E+00 | 0.00E+00 | 1.25E-02 | 5.33E+00 | 0.00E+00 | 0.00E+00 |
| F7 | Mean | 1.74E+01 | 1.21E+01 | 8.98E+01 | 1.08E+01 | 1.17E+01 | 1.78E+01 | 1.65E+01 | 1.19E+01 | 1.20E+01 | 2.01E+01 | 5.71E+01 | 1.72E+01 | 1.10E+01 |
|  | Std | 1.40E+00 | 9.54E-01 | 3.36E+01 | 4.07E-01 | 6.16E-01 | 1.91E+00 | 3.46E+00 | 8.75E-01 | 4.18E-01 | 5.85E+00 | 1.96E+01 | 1.68E+00 | 3.56E-01 |
| F8 | Mean | 6.76E+00 | 2.45E+00 | 3.17E+01 | 8.00E-01 | 1.29E+00 | 6.53E+00 | 5.14E+00 | 1.50E+00 | 2.09E+00 | 9.68E+00 | 3.14E+01 | 7.01E+00 | 6.02E-01 |
|  | Std | 1.36E+00 | 1.09E+00 | 2.58E+00 | 9.34E-01 | 1.04E+00 | 1.50E+00 | 2.31E+00 | 1.10E+00 | 1.21E+00 | 3.64E+00 | 1.21E+01 | 1.63E+00 | 3.31E-01 |
| F9 | Mean | 0.00E+00 | 0.00E+00 | 7.72E+02 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.07E-02 | 0.00E+00 | 0.00E+00 | 1.25E-01 | 1.99E+02 | 0.00E+00 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 1.42E+02 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 6.46E-02 | 0.00E+00 | 0.00E+00 | 5.74E-01 | 1.55E+02 | 0.00E+00 | 0.00E+00 |
| F10 | Mean | 2.96E+02 | 2.38E+01 | 1.36E+03 | 4.43E+01 | 6.64E+01 | 2.68E+02 | 7.57E+02 | 3.40E+01 | 6.21E+01 | 6.13E+02 | 9.92E+02 | 3.58E+02 | 3.05E+00 |
|  | Std | 9.11E+01 | 3.71E+01 | 3.83E+02 | 5.55E+01 | 9.63E+00 | 1.07E+02 | 4.06E+02 | 5.91E+01 | 3.70E+01 | 2.22E+02 | 3.44E+02 | 1.11E+02 | 3.79E+00 |
| F11 | Mean | 3.08E+00 | 4.44E-01 | 3.32E-01 | 2.58E+00 | 3.12E-01 | 2.40E+00 | 1.03E+00 | 0.00E+00 | 0.00E+00 | 4.03E+00 | 5.50E+01 | 1.37E+00 | 3.90E-03 |
|  | Std | 8.14E-01 | 6.89E-01 | 5.86E-01 | 1.20E+00 | 6.45E-02 | 6.12E-01 | 1.19E+00 | 0.00E+00 | 0.00E+00 | 3.16E+00 | 4.83E+01 | 7.90E-01 | 1.95E-03 |
| F12 | Mean | 9.41E+01 | 3.46E+01 | 1.74E+02 | 1.00E+02 | 1.24E+02 | 1.11E+01 | 4.27E+03 | 9.70E+00 | 6.12E-01 | 5.93E+02 | 1.30E+06 | 7.69E+01 | 4.20E+01 |
|  | Std | 7.13E+01 | 5.53E+01 | 1.11E+02 | 5.23E+01 | 7.08E+01 | 1.09E+01 | 6.17E+03 | 4.13E+01 | 1.68E-01 | 2.24E+03 | 1.19E+06 | 6.34E+01 | 9.13E+00 |
| F13 | Mean | 8.13E+00 | 3.58E+00 | 4.26E+00 | 6.30E+00 | 4.52E+00 | 5.00E+00 | 7.74E+01 | 1.35E+00 | 3.51E+00 | 6.23E+00 | 9.29E+03 | 5.94E+00 | 4.57E+00 |
|  | Std | 2.76E+00 | 2.23E+00 | 6.53E-01 | 5.42E+00 | 2.98E+00 | 1.58E+00 | 3.54E+02 | 1.76E+00 | 2.36E+00 | 2.47E+00 | 7.57E+03 | 2.70E+00 | 2.44E+00 |
| F14 | Mean | 3.44E+00 | 2.84E-01 | 1.48E+01 | 2.78E+00 | 4.06E+00 | 5.07E+00 | 1.84E+01 | 2.32E-02 | 9.95E-02 | 2.26E+01 | 2.23E+03 | 3.42E-01 | 3.51E-01 |
|  | Std | 1.45E+00 | 4.68E-01 | 9.50E+00 | 5.79E+00 | 3.70E+00 | 1.56E+00 | 6.40E+00 | 1.39E-01 | 2.98E-01 | 3.55E+00 | 3.07E+03 | 1.89E-01 | 1.24E-01 |
| F15 | Mean | 1.48E+00 | 1.76E-01 | 7.05E-01 | 1.88E+00 | 1.25E+00 | 6.99E-01 | 3.48E+00 | 4.27E-01 | 3.01E-01 | 1.60E+01 | 3.34E+03 | 2.81E-01 | 3.23E-03 |
|  | Std | 3.93E-01 | 2.08E-01 | 6.20E-01 | 2.23E+00 | 1.08E+00 | 2.10E-01 | 3.29E+00 | 4.31E-01 | 2.37E-01 | 9.92E+01 | 4.44E+03 | 1.39E-01 | 2.97E-03 |
| F16 | Mean | 3.45E+00 | 3.36E-01 | 3.75E+02 | 1.44E+00 | 1.03E+00 | 2.76E+00 | 6.98E+00 | 4.72E-01 | 5.48E-01 | 9.32E+01 | 2.52E+02 | 4.76E+03 | 1.54E-01 |
|  | Std | 1.57E+00 | 1.73E-01 | 8.90E+01 | 7.02E-01 | 3.54E-01 | 8.39E-01 | 2.35E+01 | 8.99E-02 | 2.54E-01 | 9.03E+01 | 1.37E+02 | 3.89E+01 | 1.12E-01 |
| F17 | Mean | 4.57E+00 | 1.45E-01 | 1.32E+02 | 1.81E+01 | 1.67E+01 | 8.58E+00 | 3.89E+01 | 1.97E-02 | 4.74E-01 | 1.79E+01 | 6.76E+01 | 1.40E+00 | 1.26E-01 |
|  | Std | 1.79E+00 | 1.80E-01 | 1.06E+02 | 9.94E+00 | 9.82E+00 | 2.62E+00 | 7.05E+00 | 1.72E-01 | 2.06E-01 | 1.83E+01 | 4.48E+01 | 4.95E-01 | 4.72E-01 |
| F18 | Mean | 7.75E+00 | 1.94E-01 | 1.37E+01 | 5.91E+00 | 6.08E+00 | 3.29E+00 | 1.95E+01 | 1.35E-02 | 3.02E-01 | 1.92E+01 | 1.84E+04 | 3.14E-01 | 4.13E-02 |
|  | Std | 6.24E+00 | 2.07E-01 | 9.74E+00 | 8.67E+00 | 8.71E-01 | 1.29E+00 | 4.82E+00 | 6.67E-02 | 2.07E-01 | 5.28E+00 | 1.73E+04 | 1.74E-01 | 2.02E-02 |
| F19 | Mean | 6.55E-01 | 1.04E-02 | 1.77E+00 | 2.44E-01 | 6.16E-01 | 6.44E-01 | 2.28E+00 | 0.00E+00 | 9.30E-03 | 1.04E+00 | 4.81E+03 | 1.09E-01 | 2.14E-02 |
|  | Std | 2.01E-01 | 1.07E-02 | 1.30E+00 | 3.16E-01 | 4.75E-01 | 2.01E-01 | 5.43E-01 | 9.39E-03 | 1.75E-02 | 8.39E-01 | 6.53E+03 | 5.73E-02 | 1.60E-02 |
| F20 | Mean | 5.52E-02 | 0.00E+00 | 4.40E+02 | 1.22E+01 | 1.22E+01 | 1.20E+00 | 1.22E+01 | 7.91E-01 | 8.43E-01 | 2.18E+01 | 7.57E+01 | 1.47E-02 | 3.81E-05 |
|  | Std | 3.98E-02 | 0.00E+00 | 2.00E+01 | 1.12E+01 | 1.00E+01 | 7.43E-01 | 9.46E+00 | 0.00E+00 | 9.37E-02 | 1.71E+01 | 4.85E+01 | 2.46E-02 | 2.06E-05 |
| F21 | Mean | 1.60E+02 | 1.51E+02 | 2.02E+02 | 1.89E+02 | 1.68E+02 | 1.13E+02 | 2.02E+02 | 1.75E+02 | 1.41E+02 | 1.14E+02 | 1.50E+02 | 1.11E+02 | 1.02E+02 |
|  | Std | 4.46E+01 | 5.20E+01 | 4.82E+00 | 2.87E+01 | 1.64E+01 | 3.51E+01 | 2.10E+01 | 5.29E+01 | 5.06E+01 | 3.64E+01 | 5.90E+01 | 3.48E+01 | 6.27E+00 |
| F22 | Mean | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 8.02E+01 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.81E+02 | 1.06E+02 | 9.35E+01 | 1.00E+02 |
|  | Std | 1.33E-01 | 5.58E-02 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.00E+01 | 3.51E-01 | 0.00E+00 | 0.00E+00 | 2.61E+02 | 4.25E+00 | 2.08E+01 | 4.69E-02 |
| F23 | Mean | 3.07E+02 | 3.03E+02 | 3.52E+02 | 3.04E+02 | 3.02E+02 | 3.06E+02 | 3.08E+02 | 3.03E+02 | 3.01E+02 | 3.15E+02 | 3.48E+02 | 3.09E+02 | 2.96E+02 |
|  | Std | 1.84E+00 | 1.54E+00 | 1.62E+02 | 3.93E+00 | 2.02E+00 | 1.95E+00 | 2.57E+00 | 1.46E+00 | 1.49E+00 | 5.23E+00 | 1.82E+01 | 2.46E+00 | 2.23E+00 |
| F24 | Mean | 2.97E+02 | 3.02E+02 | 1.00E+02 | 3.24E+02 | 3.28E+02 | 2.42E+02 | 3.31E+02 | 3.30E+02 | 2.89E+02 | 3.46E+02 | 3.19E+02 | 1.21E+02 | 2.04E+02 |
|  | Std | 7.15E+01 | 8.09E+01 | 0.00E+00 | 9.22E+00 | 4.25E+00 | 5.15E+02 | 3.32E+01 | 7.21E+01 | 9.15E+01 | 5.72E+00 | 1.15E+02 | 6.52E+01 | 1.02E+01 |
| F25 | Mean | 4.12E+02 | 4.16E+02 | 4.42E+02 | 4.09E+02 | 4.09E+02 | 4.02E+02 | 4.44E+02 | 4.01E+02 | 4.17E+02 | 4.20E+02 | 4.31E+02 | 4.08E+02 | 4.01E+02 |
|  | Std | 2.15E+01 | 2.26E+01 | 8.94E+00 | 1.77E+01 | 1.37E+01 | 1.23E+01 | 1.33E+01 | 1.82E+01 | 2.36E+01 | 2.06E+01 | 1.89E+01 | 1.21E+01 |  |
| F26 | Mean | 3.00E+02 | 3.00E+02 | 2.75E+02 | 3.07E+02 | 2.69E+02 | 3.00E+02 | 3.37E+02 | 3.00E+02 | 3.00E+02 | 4.04E+02 | 4.89E+02 | 3.20E+02 | 3.00E+02 |
|  | Std | 7.52E-11 | 0.00E+00 | 4.40E+01 | 1.01E+01 | 6.59E+00 | 0.00E+00 | 6.45E+01 | 0.00E+00 | 0.00E+00 | 1.32E+02 | 3.07E+02 | 4.16E+01 | 0.00E+00 |
| F27 | Mean | 3.89E+02 | 3.89E+02 | 4.70E+02 | 3.94E+02 | 3.74E+02 | 3.89E+02 | 3.73E+02 | 3.84E+02 | 3.89E+02 | 3.82E+02 | 4.17E+02 | 3.89E+02 | 3.76E+02 |
|  | Std | 1.94E-01 | 1.22E-01 | 2.22E+01 | 2.00E+00 | 6.80E-01 | 4.12E-01 | 1.53E+00 | 8.34E+00 | 1.74E-02 | 3.00E+01 | 6.84E+01 | 1.98E+00 | 2.02E+00 |
| F28 | Mean | 4.19E+02 | 3.46E+02 | 4.86E+02 | 3.07E+02 | 3.71E+02 | 3.00E+02 | 4.16E+02 | 3.85E+02 | 3.16E+02 | 4.76E+02 | 4.96E+02 | 1.82E+05 | 3.00E+02 |
|  | Std | 1.48E+02 | 1.08E+02 | 1.29E+01 | 1.44E+01 | 3.92E+01 | 1.19E-01 | 4.46E+01 | 3.45E+01 | 9.00E+01 | 2.22E+01 | 1.16E+02 | 1.16E+02 | 5.27E-01 |
| F29 | Mean | 2.55E+02 | 2.34E+02 | 2.32E+02 | 2.35E+02 | 2.42E+02 | 2.52E+02 | 2.50E+02 | 2.33E+02 | 2.34E+02 | 2.58E+02 | 3.55E+02 | 2.63E+02 | 2.30E+02 |
|  | Std | 6.88E+00 | 2.94E+00 | 2.00E+01 | 5.25E+00 | 9.50E+00 | 5.16E+00 | 8.99E+00 | 2.32E+00 | 2.80E+00 | 2.74E+01 | 5.67E+01 | 7.26E+00 | 2.11E+00 |
| F30 | Mean | 1.89E+03 | 3.25E+04 | 2.01E+02 | 1.12E+03 | 2.01E+03 | 3.96E+02 | 2.02E+02 | 3.02E+04 | 3.96E+02 | 2.15E+02 | 6.10E+05 | 4.41E+02 | 2.85E+02 |
|  | Std | 4.00E+03 | 1.60E+05 | 3.81E-01 | 1.63E+03 | 9.55E+02 | 7.68E-01 | 6.85E-01 | 1.54E+00 | 9.74E-01 | 2.80E+01 | 4.81E+05 | 5.94E+01 | 1.94E+02 |

Table 3
The results of KCACIL and 12 comparison algorithms (30D) for the CEC 2017 test suite.

| Fun |  | JADE | LSHADE | CMA-ES | AAVS_EDA | DE/GM | MPEDE | IDE_EDA | EA4wig | JSO_CMA-ES_LBFGS | RLBSO | OLBSO | LDE | KCACIL |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| F1 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 3.86E+09 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 2.78E-01 | 4.70E+04 | 0.00E+00 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.29E+09 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.37E+00 | 3.22E+04 | 0.00E+00 | 0.00E+00 |
| F3 | Mean | 1.78E+04 | 0.00E+00 | 0.00E+00 | 2.04E+04 | 0.00E+00 | 0.00E+00 | 8.76E+00 | 0.00E+00 | 0.00E+00 | 1.29E+03 | 4.82E+03 | 0.00E+00 | 0.00E+00 |
|  | Std | 2.71E+04 | 0.00E+00 | 0.00E+00 | 5.38E+03 | 0.00E+00 | 0.00E+00 | 1.68E+01 | 0.00E+00 | 0.00E+00 | 1.84E+03 | 8.85E+03 | 0.00E+00 | 0.00E+00 |
| F4 | Mean | 4.56E+01 | 5.86E+01 | 0.00E+00 | 7.12E+02 | 8.77E+01 | 5.38E+01 | 3.47E+01 | 2.10E+01 | 1.43E+01 | 3.76E+01 | 7.22E+01 | 7.87E+00 | 7.80E-03 |
|  | Std | 2.54E+01 | 0.00E+00 | 0.00E+00 | 2.96E+02 | 1.15E+01 | 1.78E+01 | 2.30E+01 | 1.72E+01 | 2.56E+00 | 2.70E+01 | 2.09E+01 | 1.79E+01 | 1.67E-03 |
| F5 | Mean | 4.04E+01 | 6.71E+00 | 5.68E+00 | 6.20E+01 | 6.58E+00 | 2.58E+01 | 3.31E+01 | 2.76E+01 | 8.76E+00 | 6.96E+01 | 1.85E+02 | 4.11E+01 | 2.78E+00 |
|  | Std | 5.68E+00 | 1.32E+00 | 2.23E+00 | 1.26E+01 | 2.30E+00 | 6.63E+00 | 9.52E+00 | 6.96E+00 | 2.74E+00 | 2.46E+01 | 4.73E+01 | 7.47E+00 | 1.20E+00 |
| F6 | Mean | 2.98E-05 | 0.00E+00 | 2.14E+01 | 1.29E+01 | 0.00E+00 | 0.00E+00 | 6.42E-04 | 0.00E+00 | 1.95E-05 | 8.78E-01 | 1.31E+01 | 1.30E-07 | 0.00E+00 |
|  | Std | 2.05E-05 | 0.00E+00 | 2.68E+01 | 2.80E+00 | 0.00E+00 | 1.49E-07 | 1.95E-03 | 1.66E-07 | 3.04E-05 | 9.94E-01 | 6.37E+00 | 3.40E-07 | 0.00E+00 |
| F7 | Mean | 6.95E+01 | 3.76E+01 | 3.56E+01 | 7.97E+01 | 3.58E+01 | 5.55E+01 | 6.17E+01 | 5.81E+01 | 3.71E+01 | 9.37E+01 | 2.28E+02 | 8.88E+01 | 1.66E+01 |
|  | Std | 5.36E+00 | 1.35E+00 | 1.34E+00 | 1.34E+01 | 1.12E+00 | 6.24E+00 | 7.76E+00 | 5.32E+00 | 1.68E+00 | 1.85E+01 | 3.80E+01 | 1.74E+01 | 8.44E-01 |
| F8 | Mean | 3.85E+01 | 6.84E+00 | 5.93E+00 | 4.90E+01 | 6.50E+00 | 2.79E+01 | 3.52E+01 | 2.79E+01 | 8.36E+00 | 7.06E+01 | 1.73E+02 | 3.61E+01 | 1.53E+00 |
|  | Std | 5.70E+00 | 1.79E+00 | 2.18E+00 | 1.04E+01 | 2.21E+00 | 5.77E+00 | 9.51E+00 | 6.98E+00 | 1.49E+00 | 2.03E+01 | 4.39E+01 | 8.93E+00 | 1.12E+00 |
| F9 | Mean | 0.00E+00 | 0.00E+00 | 4.48E+03 | 2.60E+02 | 0.00E+00 | 1.42E-02 | 1.75E+00 | 1.78E-02 | 0.00E+00 | 1.53E+02 | 5.16E+03 | 5.44E-02 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 4.54E+01 | 1.30E+02 | 0.00E+00 | 6.64E-02 | 4.04E+00 | 8.91E-02 | 0.00E+00 | 2.03E+02 | 2.21E+03 | 1.43E-01 | 0.00E+00 |
| F10 | Mean | 2.74E+03 | 1.75E+03 | 3.23E+03 | 2.32E+03 | 7.17E+02 | 2.66E+03 | 3.26E+03 | 1.77E+03 | 1.54E+03 | 3.28E+03 | 4.73E+03 | 3.84E+03 | 7.21E+02 |
|  | Std | 2.40E+02 | 1.92E+02 | 5.35E+02 | 4.22E+02 | 3.19E+02 | 4.03E+02 | 6.98E+02 | 3.47E+02 | 2.42E+02 | 4.90E+02 | 7.02E+02 | 1.86E+02 | 2.43E+02 |
| F11 | Mean | 4.49E+01 | 2.17E+01 | 3.52E+01 | 1.16E+02 | 5.87E+01 | 2.19E+01 | 2.44E+01 | 1.66E+01 | 4.08E+00 | 2.59E+01 | 1.77E+02 | 1.52E+01 | 1.29E+01 |
|  | Std | 3.55E+01 | 2.69E+01 | 2.90E+01 | 5.03E+01 | 1.20E+01 | 9.70E+00 | 9.21E+00 | 4.41E+00 | 2.05E+00 | 1.20E+01 | 6.21E+01 | 4.69E+00 | 2.45E+00 |
| F12 | Mean | 1.68E+03 | 9.50E+02 | 1.32E+03 | 1.61E+08 | 9.42E+02 | 9.31E+02 | 7.77E+04 | 4.75E+02 | 1.67E+02 | 1.02E+05 | 3.59E+06 | 6.06E+03 | 2.57E+02 |
|  | Std | 1.34E+03 | 3.63E+02 | 3.88E+02 | 1.20E+08 | 2.62E+02 | 3.99E+02 | 5.57E+04 | 2.40E+02 | 1.23E+02 | 1.04E+05 | 2.85E+06 | 4.16E+03 | 2.79E+01 |
| F13 | Mean | 5.18E+02 | 1.64E+01 | 1.44E+01 | 9.00E+03 | 8.61E+01 | 2.10E+01 | 1.16E+04 | 2.05E+01 | 1.70E+01 | 1.99E+03 | 2.40E+04 | 8.01E+01 | 9.36E+00 |
|  | Std | 3.38E+03 | 5.82E+00 | 5.22E+00 | 4.02E+03 | 4.90E+01 | 7.96E+00 | 1.03E+04 | 1.30E+01 | 9.70E+00 | 7.66E+03 | 1.68E+04 | 3.87E+01 | 6.64E+00 |
| F14 | Mean | 7.98E+03 | 2.15E+01 | 1.33E+02 | 5.36E+01 | 5.81E+00 | 1.64E+01 | 3.71E+02 | 1.93E+01 | 2.15E+01 | 1.54E+02 | 2.51E+04 | 5.52E+01 | 1.69E+01 |
|  | Std | 1.26E+04 | 4.85E+00 | 3.06E+01 | 1.17E+01 | 5.81E+00 | 1.06E+01 | 3.80E+02 | 9.83E+00 | 1.03E+01 | 4.58E+02 | 3.67E+04 | 1.80E+01 | 4.36E+00 |
| F15 | Mean | 6.95E+03 | 3.62E+00 | 7.47E+01 | 1.40E+03 | 9.60E+00 | 8.51E+00 | 2.89E+03 | 5.05E+00 | 3.58E+00 | 8.73E+02 | 8.89E+03 | 1.83E+01 | 3.66E+00 |
|  | Std | 1.42E+04 | 2.18E+00 | 8.00E+01 | 1.28E+03 | 6.54E+00 | 3.52E+00 | 2.96E+03 | 2.44E+00 | 2.35E+00 | 2.38E+03 | 7.39E+03 | 2.07E+01 | 2.05E+00 |
| F16 | Mean | 5.70E+02 | 5.53E+01 | 8.05E+01 | 2.97E+02 | 5.36E+01 | 3.65E+02 | 3.53E+02 | 2.36E+02 | 4.28E+01 | 9.06E+02 | 1.48E+03 | 3.47E+02 | 7.96E+00 |
|  | Std | 1.54E+02 | 5.14E+01 | 9.56E+01 | 1.41E+02 | 3.34E+01 | 2.05E+02 | 1.94E+02 | 1.24E+02 | 1.06E+01 | 3.00E+02 | 3.08E+02 | 1.46E+02 | 1.41E-01 |
| F17 | Mean | 1.23E+02 | 3.33E+01 | 5.90E+01 | 6.60E+01 | 3.19E+01 | 5.42E+01 | 1.06E+02 | 2.64E+01 | 2.98E+01 | 5.01E+01 | 7.29E+02 | 4.91E+01 | 2.06E+01 |
|  | Std | 3.25E+01 | 5.93E+00 | 4.03E+01 | 5.64E+00 | 5.02E+00 | 1.94E+01 | 5.25E+01 | 9.96E+00 | 9.25E+00 | 1.80E+02 | 2.51E+02 | 7.00E+00 | 3.10E+00 |
| F18 | Mean | 3.11E+04 | 2.09E+01 | 8.78E+01 | 7.22E+03 | 2.33E+01 | 2.28E+01 | 1.06E+04 | 2.32E+01 | 2.10E+01 | 1.83E+04 | 2.70E+05 | 8.40E+01 | 2.21E+01 |
|  | Std | 6.76E+04 | 1.62E+00 | 4.50E+01 | 5.36E+03 | 2.84E+00 | 6.61E+00 | 1.70E+04 | 5.71E+00 | 7.05E-01 | 2.08E+04 | 2.07E+05 | 5.22E+01 | 7.15E-01 |
| F19 | Mean | 6.80E+03 | 5.42E+00 | 8.82E+01 | 5.72E+02 | 8.69E+00 | 7.50E+00 | 4.94E+03 | 5.61E+00 | 4.30E+00 | 1.95E+01 | 2.98E+04 | 1.75E+01 | 3.46E+00 |
|  | Std | 1.32E+04 | 1.33E+00 | 3.07E+01 | 1.01E+03 | 2.55E+00 | 2.23E+00 | 5.20E+03 | 1.57E+00 | 1.88E+00 | 9.79E+00 | 5.22E+04 | 4.47E+00 | 1.99E+00 |
| F20 | Mean | 1.68E+02 | 3.18E+01 | 5.33E+02 | 1.51E+02 | 5.43E+01 | 6.37E+01 | 1.39E+02 | 3.00E+01 | 3.19E+01 | 4.84E+02 | 5.73E+02 | 4.84E+01 | 3.27E+01 |
|  | Std | 5.92E+01 | 4.94E+00 | 2.51E+02 | 5.03E+01 | 2.55E+01 | 4.46E+01 | 8.24E+01 | 3.01E+01 | 8.10E+00 | 1.49E+02 | 2.21E+02 | 5.30E+01 | 4.63E+00 |
| F21 | Mean | 2.38E+02 | 2.11E+02 | 2.07E+02 | 2.61E+02 | 2.06E+02 | 2.28E+02 | 2.32E+02 | 2.27E+02 | 2.09E+02 | 2.69E+02 | 4.06E+02 | 2.32E+02 | 1.97E+02 |
|  | Std | 5.04E+00 | 1.65E+00 | 2.42E+00 | 1.29E+01 | 2.01E+00 | 7.75E+00 | 8.24E+00 | 6.98E+00 | 2.23E+00 | 1.87E+01 | 6.11E+01 | 9.24E+00 | 9.35E-01 |
| F22 | Mean | 1.00E+02 | 1.00E+02 | 2.34E+02 | 5.45E+02 | 1.00E+02 | 1.00E+02 | 1.27E+03 | 1.00E+02 | 1.00E+02 | 3.37E+03 | 3.03E+03 | 1.00E+02 | 1.00E+02 |
|  | Std | 0.00E+00 | 0.00E+00 | 2.60E+02 | 1.57E+02 | 0.00E+00 | 0.00E+00 | 1.58E+03 | 1.05E-05 | 0.00E+00 | 6.43E+02 | 2.56E+03 | 0.00E+00 | 0.00E+00 |
| F23 | Mean | 3.86E+02 | 3.60E+02 | 3.62E+02 | 5.31E+02 | 4.60E+02 | 3.79E+02 | 3.90E+02 | 3.75E+02 | 3.50E+02 | 4.27E+02 | 6.10E+02 | 3.74E+02 | 3.42E+02 |
|  | Std | 7.27E+00 | 2.71E+00 | 5.62E+00 | 3.26E+01 | 5.58E+00 | 1.03E+01 | 6.59E+00 | 3.15E+00 | 1.94E+01 | 6.73E+01 | 1.41E+01 | 2.81E+00 |  |
| F24 | Mean | 4.51E+02 | 4.26E+02 | 4.27E+02 | 6.46E+02 | 4.22E+02 | 4.42E+02 | 4.63E+02 | 4.46E+02 | 4.28E+02 | 4.93E+02 | 6.78E+02 | 4.48E+02 | 4.24E+02 |
|  | Std | 5.52E+00 | 1.56E+00 | 2.40E+00 | 6.54E+01 | 3.65E+00 | 7.49E+00 | 9.21E+00 | 8.39E+00 | 2.56E+00 | 2.21E+01 | 6.89E+01 | 1.06E+01 | 1.48E+00 |
| F25 | Mean | 3.87E+02 | 3.97E+02 | 3.78E+02 | 4.94E+02 | 4.25E+02 | 3.87E+02 | 3.75E+02 | 3.79E+02 | 3.80E+01 | 3.79E+02 | 4.07E+02 | 3.88E+02 | 4.04E+02 |
|  | Std | 1.59E-01 | 2.66E-02 | 1.86E-02 | 2.30E+01 | 6.03E-01 | 6.64E-02 | 1.44E+00 | 4.20E-01 | 1.14E+02 | 7.56E-01 | 2.26E+01 | 3.46E+00 | 2.30E-02 |
| F26 | Mean | 1.29E+03 | 9.34E+02 | 8.97E+02 | 1.70E+03 | 9.25E+02 | 1.17E+03 | 1.48E+03 | 1.18E+03 | 9.17E+02 | 1.54E+03 | 3.38E+03 | 1.20E+03 | 5.91E+02 |
|  | Std | 6.74E+01 | 3.80E+01 | 2.28E+02 | 4.15E+02 | 7.78E+01 | 9.44E+01 | 1.47E+02 | 2.60E+02 | 5.45E+01 | 3.05E+02 | 1.27E+03 | 3.66E+02 | 3.56E+01 |
| F27 | Mean | 5.03E+02 | 5.13E+02 | 5.00E+02 | 5.36E+02 | 4.99E+02 | 5.00E+02 | 5.00E+02 | 4.94E+02 | 4.95E+02 | 5.00E+02 | 4.96E+02 | 5.03E+02 | 5.00E+02 |
|  | Std | 5.84E+00 | 5.91E+00 | 3.43E-04 | 2.16E+01 | 2.97E+00 | 6.09E+00 | 1.76E-04 | 1.89E+01 | 6.46E-05 | 2.43E-04 | 7.63E+00 | 4.42E+00 | 7.03E-05 |
| F28 | Mean | 3.36E+02 | 3.52E+02 | 5.00E+02 | 6.71E+02 | 4.37E+02 | 3.28E+02 | 4.70E+02 | 3.29E+02 | 3.12E+02 | 5.00E+02 | 4.33E+02 | 3.00E+02 | 3.15E+02 |
|  | Std | 5.51E+01 | 5.52E+01 | 4.44E-04 | 7.92E+01 | 4.87E+01 | 4.88E+01 | 4.14E+01 | 5.32E+01 | 4.16E-03 | 2.16E+00 | 2.44E+01 | 5.36E-14 | 3.45E-03 |
| F29 | Mean | 5.18E+02 | 4.44E+02 | 3.56E+02 | 4.38E+02 | 4.21E+02 | 4.53E+02 | 4.70E+02 | 4.06E+02 | 4.34E+02 | 6.00E+02 | 1.45E+03 | 5.24E+02 | 3.65E+02 |
|  | Std | 3.93E+01 | 5.37E+00 | 4.82E+01 | 3.39E+01 | 5.20E+01 | 1.49E+02 | 1.07E+02 | 5.50E+01 | 1.77E+02 | 1.86E+02 | 2.71E+02 | 5.95E+01 | 5.73E+00 |
| F30 | Mean | 2.37E+03 | 1.98E+03 | 8.50E+02 | 2.79E+04 | 2.18E+03 | 1.99E+03 | 1.57E+03 | 4.78E+02 | 1.98E+03 | 3.24E+02 | 7.18E+05 | 2.15E+03 | 9.42E+02 |
|  | Std | 1.51E+03 | 4.36E+01 | 1.67E+03 | 1.24E+04 | 4.83E+02 | 4.70E+01 | 2.05E+03 | 1.53E+01 | 9.03E+02 | 4.26E+02 | 4.50E+05 | 1.13E+02 | 2.13E+02 |

Table 4
The results of KCACIL and 12 comparison algorithms (50D) for the CEC 2017 test suite.

| Fun |  | JADE | LSHADE | CMA-ES | AAVS_EDA | DE/GM | MPEDE | IDE_EDA | EA4eig | jSO_CMA-ES_LBPGS | RLBSO | OLBSO | LDE | KCACIL |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| F1 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 2.84E+10 | 0.00E+00 | 0.00E+00 | 3.31E+03 | 0.00E+00 | 0.00E+00 | 5.09E+03 | 2.82E+05 | 1.88E+03 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 4.75E+09 | 0.00E+00 | 0.00E+00 | 3.89E+03 | 0.00E+00 | 0.00E+00 | 9.62E+03 | 1.72E+05 | 3.07E+03 | 0.00E+00 |
| F3 | Mean | 2.79E+04 | 0.00E+00 | 0.00E+00 | 1.11E+04 | 1.87E-03 | 4.81E-04 | 4.65E+03 | 0.00E+00 | 0.00E+00 | 4.28E+04 | 2.32E+01 | 5.48E+02 | 0.00E+00 |
|  | Std | 5.78E+04 | 0.00E+00 | 0.00E+00 | 1.23E+04 | 1.43E-03 | 1.93E-03 | 2.69E+03 | 0.00E+00 | 0.00E+00 | 1.91E+04 | 8.06E+00 | 7.49E+02 | 0.00E+00 |
| F4 | Mean | 5.01E+01 | 9.73E+01 | 0.00E+00 | 5.05E+03 | 2.00E+02 | 4.87E+01 | 5.04E+01 | 5.48E+01 | 2.83E+00 | 6.54E+01 | 1.51E+02 | 8.93E+01 | 1.16E+00 |
|  | Std | 4.38E+01 | 4.46E+01 | 0.00E+00 | 1.03E+03 | 2.14E+00 | 4.49E+01 | 1.88E+01 | 4.06E+01 | 6.21E+00 | 3.29E+01 | 4.72E+01 | 2.92E+01 | 1.06E+00 |
| F5 | Mean | 7.47E+01 | 1.21E+01 | 1.26E+01 | 2.27E+02 | 9.72E+00 | 5.11E+01 | 7.22E+01 | 7.25E+01 | 1.92E+01 | 1.52E+02 | 3.95E+02 | 1.64E+02 | 6.97E+00 |
|  | Std | 9.98E+00 | 2.49E+00 | 2.65E+00 | 2.35E+01 | 3.82E+00 | 1.22E+01 | 2.04E+01 | 1.65E+01 | 2.52E+00 | 2.84E+01 | 1.03E+02 | 1.63E+01 | 2.23E+00 |
| F6 | Mean | 1.60E-05 | 4.12E-05 | 6.96E+00 | 3.09E+01 | 0.00E+00 | 8.50E-04 | 1.68E-02 | 1.18E-06 | 1.03E-04 | 7.12E+00 | 1.24E+01 | 3.52E-03 | 0.00E+00 |
|  | Std | 1.82E-05 | 2.12E-04 | 1.93E+01 | 3.72E+00 | 0.00E+00 | 2.54E-03 | 3.60E-02 | 1.89E-06 | 1.35E-05 | 3.50E+00 | 4.57E+00 | 5.22E-03 | 0.00E+00 |
| F7 | Mean | 1.27E+02 | 6.35E+01 | 6.20E+01 | 3.28E+02 | 5.70E+01 | 1.04E+02 | 1.17E+02 | 1.22E+02 | 8.50E+01 | 2.35E+02 | 4.36E+02 | 2.41E+02 | 2.70E+01 |
|  | Std | 8.21E+00 | 1.63E+00 | 2.51E+00 | 4.28E+01 | 1.10E+00 | 1.20E+01 | 1.46E+01 | 1.19E+01 | 2.90E+00 | 4.61E+01 | 9.00E+01 | 2.86E+01 | 1.00E+00 |
| F8 | Mean | 7.52E+01 | 1.22E+01 | 1.28E+01 | 2.34E+02 | 1.00E+01 | 5.45E+01 | 6.88E+01 | 6.79E+01 | 2.01E+01 | 1.54E+02 | 3.36E+02 | 1.75E+02 | 5.36E+00 |
|  | Std | 1.00E+01 | 2.31E+00 | 3.09E+00 | 2.00E+01 | 3.96E+00 | 1.26E+01 | 1.50E+01 | 1.53E+01 | 2.30E+00 | 3.02E+01 | 9.26E+01 | 1.53E+01 | 2.17E+00 |
| F9 | Mean | 7.69E-01 | 0.00E+00 | 1.22E+04 | 4.34E+03 | 0.00E+00 | 9.38E-01 | 1.45E+01 | 4.43E-01 | 0.00E+00 | 2.39E+03 | 1.28E+04 | 1.13E+01 | 0.00E+00 |
|  | Std | 9.19E-01 | 0.00E+00 | 6.58E+01 | 8.57E+02 | 0.00E+00 | 8.84E-01 | 1.44E+01 | 6.42E-01 | 0.00E+00 | 2.74E+03 | 4.78E+03 | 1.67E+01 | 0.00E+00 |
| F10 | Mean | 5.13E+03 | 3.16E+03 | 3.93E+03 | 6.54E+03 | 2.04E+03 | 4.78E+03 | 6.17E+03 | 3.80E+03 | 3.64E+03 | 5.64E+03 | 7.76E+03 | 6.76E+03 | 2.20E+03 |
|  | Std | 3.46E+02 | 2.70E+02 | 1.02E+03 | 7.89E+02 | 4.28E+02 | 7.67E+02 | 8.19E+02 | 4.66E+02 | 2.32E+02 | 8.06E+02 | 8.50E+02 | 2.51E+02 | 2.55E+02 |
| F11 | Mean | 7.74E+02 | 4.78E+01 | 1.14E+02 | 2.24E+03 | 2.09E+02 | 1.02E+02 | 7.35E+01 | 5.79E+01 | 2.05E+01 | 7.61E+01 | 3.10E+02 | 1.26E+02 | 3.36E+01 |
|  | Std | 9.59E+01 | 8.56E+00 | 2.80E+01 | 8.26E+02 | 4.17E+01 | 2.62E+01 | 2.13E+01 | 1.62E+01 | 1.28E+01 | 2.70E+01 | 8.46E+01 | 4.15E+01 | 4.39E+00 |
| F12 | Mean | 1.17E+04 | 2.35E+03 | 2.59E+03 | 7.50E+09 | 1.29E+03 | 6.78E+03 | 8.95E+05 | 3.38E+04 | 1.78E+03 | 6.04E+05 | 1.24E+07 | 7.18E+04 | 1.32E+03 |
|  | Std | 9.40E+03 | 4.87E+02 | 4.51E+02 | 2.79E+09 | 2.88E+02 | 5.69E+03 | 6.37E+05 | 9.41E+04 | 3.98E+02 | 3.24E+05 | 5.88E+06 | 3.26E+04 | 2.13E+02 |
| F13 | Mean | 2.28E+02 | 5.88E+01 | 6.54E+01 | 8.16E+08 | 3.47E+02 | 9.11E+01 | 4.33E+03 | 8.92E+01 | 2.73E+01 | 8.49E+03 | 3.99E+04 | 1.79E+03 | 4.66E+01 |
|  | Std | 1.66E+02 | 3.57E+01 | 2.53E+01 | 8.00E+08 | 1.84E+02 | 4.02E+01 | 4.95E+03 | 3.78E+01 | 1.82E+01 | 1.13E+04 | 2.49E+04 | 1.83E+03 | 2.63E+01 |
| F14 | Mean | 1.87E+04 | 2.96E+01 | 3.14E+02 | 1.21E+04 | 2.83E+01 | 5.81E+01 | 3.23E+03 | 5.74E+01 | 2.85E+01 | 2.54E+04 | 8.54E+04 | 2.79E+03 | 2.87E+01 |
|  | Std | 5.15E+04 | 3.07E+00 | 1.28E+02 | 5.95E+04 | 4.90E+00 | 1.52E+01 | 2.78E+03 | 1.59E+01 | 7.65E+00 | 2.36E+04 | 7.16E+04 | 5.65E+03 | 3.04E+00 |
| F15 | Mean | 6.69E+02 | 4.04E+01 | 3.61E+02 | 5.53E+03 | 8.60E+01 | 6.62E+01 | 7.00E+03 | 5.96E+01 | 2.61E+01 | 6.08E+03 | 1.24E+04 | 1.78E+03 | 3.91E+01 |
|  | Std | 2.04E+03 | 9.29E+00 | 1.28E+02 | 2.80E+03 | 2.34E+01 | 2.93E+01 | 7.47E+03 | 2.55E+01 | 1.22E+01 | 8.43E+03 | 1.04E+04 | 2.40E+03 | 2.06E+00 |
| F16 | Mean | 1.09E+03 | 3.87E+02 | 1.56E+02 | 8.64E+02 | 2.91E+02 | 9.09E+02 | 1.00E+03 | 7.00E+02 | 4.27E+02 | 2.00E+03 | 2.42E+03 | 9.45E+02 | 1.34E+02 |
|  | Std | 1.84E+02 | 1.51E+02 | 1.28E+02 | 2.20E+02 | 4.56E+01 | 3.34E+02 | 3.41E+02 | 2.23E+02 | 1.87E+02 | 4.56E+02 | 5.35E+02 | 1.81E+02 | 1.69E+01 |
| F17 | Mean | 8.10E+02 | 2.53E+02 | 3.60E+02 | 4.90E+02 | 1.53E+02 | 5.75E+02 | 8.54E+02 | 4.50E+02 | 2.95E+02 | 1.37E+03 | 1.94E+03 | 7.39E+02 | 1.57E+02 |
|  | Std | 1.46E+02 | 7.73E+01 | 1.30E+02 | 1.42E+02 | 5.64E+01 | 1.58E+02 | 2.53E+02 | 1.34E+02 | 8.90E+01 | 3.47E+02 | 3.78E+02 | 1.21E+02 | 6.06E+00 |
| F18 | Mean | 7.42E+04 | 4.14E+01 | 2.54E+02 | 1.97E+05 | 2.94E+01 | 1.06E+02 | 1.23E+05 | 4.84E+01 | 2.96E+01 | 1.52E+05 | 8.30E+05 | 2.18E+04 | 2.30E+01 |
|  | Std | 4.23E+05 | 1.39E+01 | 8.89E+01 | 2.79E+05 | 5.00E+00 | 7.82E+01 | 9.41E+04 | 1.58E+01 | 1.59E+00 | 1.48E+05 | 6.53E+05 | 2.11E+04 | 5.12E+00 |
| F19 | Mean | 1.40E+02 | 2.59E+01 | 1.38E+02 | 3.67E+04 | 2.55E+01 | 4.01E+01 | 1.45E+04 | 2.28E+01 | 1.40E+01 | 1.19E+03 | 2.09E+04 | 6.45E+03 | 1.43E+01 |
|  | Std | 4.57E+01 | 6.53E+00 | 5.31E+01 | 3.12E+04 | 3.48E+00 | 1.48E+01 | 9.23E+03 | 5.79E+00 | 1.59E+00 | 3.02E+03 | 2.14E+04 | 5.76E+03 | 2.82E+00 |
| F20 | Mean | 6.62E+02 | 1.54E+02 | 1.54E+03 | 2.36E+02 | 1.94E+02 | 3.86E+02 | 6.26E+02 | 2.24E+02 | 1.49E+02 | 9.37E+02 | 1.41E+03 | 5.03E+02 | 1.14E+02 |
|  | Std | 1.59E+02 | 5.31E+01 | 1.88E+02 | 6.02E+01 | 1.14E+01 | 1.61E+02 | 2.23E+02 | 1.17E+02 | 7.90E+01 | 2.75E+02 | 3.85E+02 | 1.37E+02 | 8.82E+00 |
| F21 | Mean | 2.75E+02 | 2.14E+02 | 4.63E+02 | 2.14E+02 | 2.54E+02 | 2.74E+02 | 2.71E+02 | 2.37E+02 | 3.65E+02 | 5.35E+02 | 3.36E+02 | 2.05E+02 |  |
|  | Std | 9.55E+00 | 2.41E+00 | 3.29E+00 | 2.96E+01 | 3.42E+00 | 1.52E+01 | 1.65E+01 | 1.41E+01 | 1.95E+00 | 3.66E+01 | 1.03E+02 | 2.33E+01 | 3.04E+00 |
| F22 | Mean | 4.20E+03 | 2.13E+03 | 7.78E+02 | 6.94E+03 | 1.59E+02 | 3.40E+03 | 6.15E+03 | 3.76E+03 | 1.54E+03 | 6.62E+03 | 8.43E+03 | 4.72E+03 | 1.71E+02 |
|  | Std | 2.32E+03 | 1.80E+03 | 4.39E+02 | 1.16E+03 | 1.36E+02 | 2.74E+03 | 1.15E+03 | 1.89E+03 | 1.45E+03 | 9.24E+02 | 1.47E+03 | 4.00E+03 | 1.24E+02 |
| F23 | Mean | 4.99E+02 | 4.31E+02 | 4.40E+02 | 1.08E+03 | 5.41E+02 | 4.73E+02 | 5.07E+02 | 5.01E+02 | 4.39E+02 | 5.77E+02 | 9.42E+02 | 5.90E+02 | 4.33E+02 |
|  | Std | 1.18E+01 | 4.26E+00 | 1.32E+01 | 6.78E+01 | 1.34E+01 | 1.29E+01 | 2.39E+01 | 1.74E+01 | 5.42E+00 | 5.98E+01 | 1.13E+02 | 2.58E+01 | 3.04E+00 |
| F24 | Mean | 5.53E+02 | 5.08E+02 | 5.10E+02 | 1.55E+03 | 4.99E+02 | 5.38E+02 | 5.83E+02 | 5.67E+02 | 5.16E+02 | 6.59E+02 | 9.77E+02 | 6.32E+02 | 5.01E+02 |
|  | Std | 1.00E+01 | 2.75E+00 | 3.30E+00 | 1.11E+02 | 6.58E+00 | 1.04E+01 | 1.78E+01 | 1.71E+01 | 3.82E+00 | 3.83E+01 | 1.06E+02 | 2.42E+01 | 2.87E+00 |
| F25 | Mean | 5.22E+02 | 4.82E+02 | 4.31E+02 | 2.83E+03 | 5.51E+02 | 5.19E+02 | 4.43E+02 | 4.72E+02 | 4.78E+02 | 4.57E+02 | 4.93E+02 | 5.67E+02 | 4.33E+02 |
|  | Std | 3.31E+01 | 6.12E+00 | 7.64E-03 | 5.77E+02 | 2.34E+01 | 3.06E+01 | 2.26E+01 | 2.01E+01 | 1.44E+02 | 2.75E+01 | 4.08E+01 | 2.84E+01 | 5.18E-02 |
| F26 | Mean | 1.78E+03 | 1.16E+03 | 1.59E+03 | 6.41E+03 | 9.96E+02 | 1.58E+03 | 2.10E+03 | 1.86E+03 | 1.12E+03 | 2.89E+03 | 5.27E+03 | 3.24E+03 | 6.06E+02 |
|  | Std | 1.27E+02 | 5.05E+01 | 2.05E+02 | 7.46E+02 | 1.10E+02 | 1.40E+02 | 2.01E+02 | 2.05E+02 | 5.06E+01 | 5.99E+02 | 2.22E+03 | 1.81E+02 | 4.35E+01 |
| F27 | Mean | 5.47E+02 | 5.35E+02 | 5.00E+02 | 9.32E+02 | 5.22E+02 | 5.42E+02 | 5.01E+02 | 4.98E+02 | 5.10E+02 | 5.00E+02 | 5.05E+02 | 6.68E+02 | 5.00E+02 |
|  | Std | 2.18E+01 | 2.06E+01 | 5.21E-04 | 7.20E+01 | 8.52E+00 | 2.36E+01 | 2.14E-04 | 1.42E+01 | 1.51E+02 | 2.67E-04 | 2.03E+01 | 7.47E+01 | 1.36E-04 |
| F28 | Mean | 4.93E+02 | 4.84E+02 | 5.00E+02 | 2.68E+03 | 5.27E+02 | 4.84E+02 | 4.94E+02 | 4.55E+02 | 4.40E+02 | 5.00E+02 | 4.90E+02 | 5.02E+02 | 4.72E+02 |
|  | Std | 2.11E+01 | 2.47E+01 | 5.09E-04 | 3.78E+02 | 4.63E+01 | 2.47E+01 | 1.69E+01 | 1.70E+01 | 1.73E+01 | 2.09E-04 | 1.05E+01 | 9.27E+00 | 3.20E+00 |
| F29 | Mean | 5.42E+02 | 3.51E+02 | 4.75E+02 | 1.35E+03 | 4.65E+02 | 4.32E+02 | 7.01E+02 | 3.99E+02 | 3.57E+02 | 1.31E+03 | 2.52E+03 | 7.29E+02 | 3.30E+02 |
|  | Std | 7.74E+01 | 1.15E+01 | 1.30E+02 | 2.50E+02 | 3.97E+01 | 1.16E+02 | 2.39E+02 | 8.72E+01 | 1.68E+02 | 3.35E+02 | 4.75E+02 | 1.22E+02 | 1.17E+01 |
| F30 | Mean | 6.52E+05 | 6.68E+05 | 8.60E+02 | 7.80E+06 | 5.46E+05 | 6.74E+05 | 3.21E+03 | 1.35E+03 | 1.74E+05 | 1.01E+03 | 1.00E+07 | 6.05E+05 | 1.06E+03 |
|  | Std | 7.68E+04 | 9.53E+04 | 7.25E+02 | 3.80E+06 | 2.23E+05 | 8.29E+04 | 3.69E+03 | 5.39E+02 | 4.65E+05 | 1.87E+03 | 2.42E+06 | 2.81E+04 | 8.26E+02 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Table 5
The results of KCACIL and 12 comparison algorithms (100D) for the CEC 2017 test suite.

| Fun |  | JADE | LSHADE | CMA-ES | AAVS_KDA | DE/GM | MPEDE | IDE_KDA | EA4vig | jSO_CMA-ES_LBFGS | RLBSO | OLBSO | LDE | KCACIL |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| F1 | Mean | 1.56E-06 | 0.00E+00 | 0.00E+00 | 1.32E+11 | 0.00E+00 | 0.00E+00 | 7.70E+03 | 7.01E-02 | 0.00E+00 | 5.70E+03 | 1.26E+06 | 5.95E+00 | 0.00E+00 |
|  | Std | 6.85E-06 | 0.00E+00 | 0.00E+00 | 9.53E+09 | 0.00E+00 | 0.00E+00 | 8.15E+03 | 1.73E-01 | 0.00E+00 | 9.42E+03 | 4.77E+05 | 5.80E+00 | 0.00E+00 |
| F3 | Mean | 1.08E+05 | 8.49E-07 | 0.00E+00 | 2.46E+05 | 2.48E+03 | 4.02E+01 | 6.74E+04 | 7.58E-07 | 0.00E+00 | 7.84E+05 | 3.60E+02 | 1.61E+04 | 0.00E+00 |
|  | Std | 1.78E+05 | 1.20E-06 | 0.00E+00 | 2.53E+04 | 5.81E+03 | 7.67E+01 | 1.65E+04 | 9.72E-07 | 0.00E+00 | 4.52E+05 | 6.87E+01 | 6.06E+03 | 0.00E+00 |
| F4 | Mean | 9.92E+01 | 1.96E+02 | 1.73E+01 | 2.71E+04 | 2.09E+02 | 8.54E+01 | 1.55E+02 | 1.49E+02 | 2.83E+01 | 1.88E+02 | 2.40E+02 | 2.44E+02 | 2.37E+01 |
|  | Std | 5.87E+01 | 9.65E+00 | 5.20E-01 | 3.41E+03 | 4.16E+01 | 6.76E+01 | 4.70E+01 | 9.35E+01 | 0.00E+00 | 6.78E+01 | 5.16E+01 | 9.20E+01 | 4.14E+01 |
| F5 | Mean | 1.82E+02 | 3.92E+01 | 3.47E+01 | 8.75E+02 | 2.27E+01 | 1.50E+02 | 2.02E+02 | 2.15E+02 | 4.34E+01 | 4.90E+02 | 9.57E+02 | 3.59E+02 | 1.08E+01 |
|  | Std | 1.79E+01 | 5.59E+00 | 6.33E+00 | 3.25E+01 | 7.94E+00 | 2.40E+01 | 2.68E+01 | 4.58E+01 | 4.38E+00 | 8.78E+01 | 2.37E+02 | 1.35E+02 | 3.67E+00 |
| F6 | Mean | 9.23E-04 | 7.57E-03 | 2.01E+01 | 5.59E+01 | 8.31E-05 | 1.32E-01 | 5.36E-01 | 3.16E-04 | 3.89E-04 | 2.84E+01 | 1.57E+01 | 2.07E-05 | 0.00E+00 |
|  | Std | 2.36E-03 | 4.50E-03 | 2.75E+01 | 3.24E+00 | 1.94E-05 | 1.45E-01 | 2.23E-01 | 1.94E-04 | 2.09E-05 | 5.91E+00 | 6.02E+00 | 1.96E-05 | 0.00E+00 |
| F7 | Mean | 3.08E+02 | 1.41E+02 | 1.33E+02 | 1.56E+03 | 1.36E+02 | 2.97E+02 | 3.31E+02 | 3.41E+02 | 1.45E+02 | 9.74E+02 | 9.42E+02 | 4.88E+02 | 1.12E+02 |
|  | Std | 2.46E+01 | 3.84E+00 | 4.26E+00 | 9.36E+01 | 2.04E+00 | 3.29E+01 | 4.28E+01 | 4.46E+01 | 7.17E+00 | 2.00E+02 | 1.90E+02 | 1.87E+02 | 1.38E+00 |
| F8 | Mean | 1.80E+02 | 3.68E+01 | 3.42E+01 | 9.42E+02 | 3.62E+01 | 1.45E+02 | 1.87E+02 | 2.23E+02 | 4.11E+01 | 5.03E+02 | 9.20E+02 | 3.34E+02 | 2.06E+01 |
|  | Std | 2.16E+01 | 4.37E+00 | 4.93E+00 | 4.05E+01 | 7.38E+00 | 2.19E+01 | 3.29E+01 | 4.04E+01 | 4.04E+00 | 1.03E+02 | 2.67E+02 | 1.25E+02 | 4.31E+00 |
| F9 | Mean | 5.01E+01 | 4.29E-01 | 2.21E+04 | 2.43E+04 | 0.00E+00 | 2.92E+01 | 7.00E+02 | 2.91E+01 | 0.00E+00 | 1.51E+04 | 2.81E+04 | 7.90E+03 | 0.00E+00 |
|  | Std | 2.71E+01 | 4.20E-01 | 9.75E+01 | 2.82E+03 | 0.00E+00 | 3.02E+01 | 4.16E+02 | 5.84E+01 | 0.00E+00 | 7.24E+03 | 9.66E+03 | 2.99E+03 | 0.00E+00 |
| F10 | Mean | 1.28E+04 | 1.04E+04 | 8.97E+03 | 2.07E+04 | 2.68E+03 | 1.09E+04 | 1.38E+04 | 1.14E+04 | 9.19E+03 | 1.46E+04 | 1.61E+04 | 8.35E+03 | 2.84E+03 |
|  | Std | 4.89E+02 | 5.44E+02 | 1.69E+03 | 1.10E+03 | 7.44E+02 | 1.03E+03 | 1.31E+03 | 8.84E+02 | 8.85E+02 | 1.49E+03 | 1.43E+03 | 3.21E+03 | 4.23E+02 |
| F11 | Mean | 1.01E+04 | 4.35E+02 | 1.13E+03 | 6.40E+04 | 6.49E+02 | 8.15E+02 | 6.94E+02 | 3.32E+02 | 6.22E+01 | 7.40E+02 | 1.45E+03 | 3.68E+02 | 6.98E+01 |
|  | Std | 9.84E+03 | 1.12E+02 | 2.91E+02 | 1.23E+04 | 1.79E+02 | 2.55E+02 | 2.52E+02 | 9.81E+01 | 4.66E+01 | 2.95E+02 | 1.94E+02 | 1.51E+02 | 2.08E+01 |
| F12 | Mean | 3.85E+04 | 2.18E+04 | 5.31E+03 | 6.00E+10 | 3.32E+04 | 2.87E+04 | 3.40E+06 | 1.08E+05 | 6.25E+03 | 2.93E+06 | 2.70E+07 | 2.53E+05 | 5.78E+03 |
|  | Std | 2.15E+04 | 7.39E+03 | 9.13E+02 | 8.64E+09 | 1.25E+04 | 1.10E+04 | 1.79E+06 | 4.88E+04 | 1.72E+03 | 1.72E+06 | 8.18E+06 | 1.12E+05 | 2.88E+03 |
| F13 | Mean | 3.12E+03 | 5.18E+02 | 3.88E+03 | 7.16E+09 | 6.87E+02 | 4.82E+02 | 5.00E+03 | 1.70E+03 | 3.13E+02 | 6.98E+03 | 3.07E+04 | 2.07E+03 | 3.20E+02 |
|  | Std | 2.85E+03 | 2.46E+02 | 8.78E+02 | 1.84E+09 | 4.99E+02 | 6.38E+02 | 5.07E+03 | 1.73E+03 | 8.46E+01 | 7.34E+03 | 1.07E+04 | 8.25E+02 | 8.15E+01 |
| F14 | Mean | 6.54E+02 | 2.58E+02 | 3.39E+02 | 9.16E+05 | 4.73E+01 | 4.47E+02 | 1.85E+05 | 2.70E+02 | 4.86E+01 | 1.09E+05 | 4.49E+05 | 3.07E+04 | 5.06E+01 |
|  | Std | 2.95E+02 | 3.16E+01 | 6.71E+01 | 6.65E+05 | 7.38E+00 | 1.09E+02 | 1.38E+05 | 9.22E+01 | 2.84E+01 | 7.64E+04 | 2.18E+05 | 2.70E+04 | 4.93E+00 |
| F15 | Mean | 5.73E+02 | 2.48E+02 | 4.95E+02 | 1.05E+09 | 2.83E+02 | 3.16E+02 | 2.97E+03 | 6.28E+02 | 4.04E+02 | 5.57E+03 | 1.12E+04 | 1.29E+03 | 1.73E+02 |
|  | Std | 3.75E+02 | 4.62E+01 | 1.45E+02 | 6.69E+08 | 6.30E+01 | 1.41E+02 | 2.76E+03 | 4.52E+02 | 6.87E+01 | 6.56E+03 | 4.27E+03 | 8.95E+02 | 3.15E+01 |
| F16 | Mean | 3.14E+03 | 1.68E+03 | 3.68E+02 | 4.98E+03 | 3.89E+02 | 2.88E+03 | 3.17E+03 | 2.54E+03 | 6.93E+02 | 4.32E+03 | 4.98E+03 | 2.51E+03 | 4.26E+02 |
|  | Std | 2.73E+02 | 2.61E+02 | 2.02E+02 | 5.45E+02 | 1.46E+02 | 5.29E+02 | 5.77E+02 | 3.29E+02 | 7.98E+02 | 5.97E+02 | 7.67E+02 | 9.47E+02 | 8.79E+01 |
| F17 | Mean | 2.31E+03 | 1.10E+03 | 1.33E+03 | 1.34E+03 | 9.82E+02 | 1.92E+03 | 2.79E+03 | 1.66E+03 | 1.38E+03 | 3.35E+03 | 4.02E+03 | 1.92E+03 | 5.99E+02 |
|  | Std | 2.54E+02 | 2.22E+02 | 3.09E+02 | 3.52E+02 | 6.09E+01 | 4.10E+02 | 4.41E+02 | 2.64E+02 | 1.87E+02 | 5.81E+02 | 6.34E+02 | 7.20E+02 | 2.99E+01 |
| F18 | Mean | 6.33E+03 | 2.32E+02 | 2.37E+02 | 4.42E+05 | 3.94E+02 | 8.57E+02 | 4.91E+05 | 3.46E+03 | 2.29E+02 | 5.64E+05 | 7.19E+05 | 8.41E+04 | 2.41E+02 |
|  | Std | 4.99E+03 | 4.79E+01 | 4.98E+01 | 3.96E+05 | 1.51E+01 | 9.07E+02 | 2.14E+05 | 1.85E+03 | 6.13E+01 | 3.39E+05 | 2.81E+05 | 4.17E+04 | 2.74E+01 |
| F19 | Mean | 1.04E+03 | 1.69E+02 | 3.62E+02 | 8.89E+08 | 9.23E+01 | 2.43E+02 | 2.41E+03 | 1.90E+02 | 1.42E+02 | 6.48E+03 | 1.18E+05 | 2.43E+03 | 7.75E+01 |
|  | Std | 1.84E+03 | 2.29E+01 | 1.06E+02 | 4.64E+08 | 1.13E+01 | 6.25E+01 | 3.15E+03 | 1.17E+02 | 1.17E+01 | 8.01E+03 | 1.21E+05 | 2.48E+03 | 1.01E+01 |
| F20 | Mean | 2.38E+03 | 1.54E+03 | 3.79E+03 | 9.57E+02 | 3.71E+02 | 1.90E+03 | 2.45E+03 | 1.43E+03 | 7.49E+02 | 2.92E+03 | 4.03E+03 | 1.65E+03 | 2.59E+02 |
|  | Std | 2.25E+02 | 1.93E+02 | 4.32E+02 | 2.76E+02 | 4.44E+01 | 4.32E+02 | 4.59E+02 | 2.49E+02 | 8.00E+01 | 5.72E+02 | 6.09E+02 | 6.19E+02 | 3.10E+01 |
| F21 | Mean | 4.02E+02 | 2.57E+02 | 2.58E+02 | 4.03E+02 | 2.72E+02 | 3.57E+02 | 4.37E+02 | 8.56E+02 | 2.67E+02 | 8.38E+02 | 1.21E+03 | 4.88E+02 | 2.32E+02 |
|  | Std | 2.13E+01 | 7.21E+00 | 6.20E+00 | 3.53E+01 | 1.17E+01 | 2.33E+01 | 3.59E+01 | 8.06E+01 | 2.00E+00 | 1.02E+02 | 1.78E+02 | 1.86E+02 | 5.42E+00 |
| F22 | Mean | 1.38E+04 | 1.13E+04 | 2.01E+03 | 4.41E+02 | 1.35E+04 | 1.00E+04 | 1.47E+04 | 9.74E+03 | 8.54E+03 | 1.61E+04 | 1.77E+04 | 1.10E+04 | 4.54E+03 |
|  | Std | 6.77E+02 | 5.92E+02 | 8.43E+02 | 1.71E+03 | 1.83E+03 | 1.13E+03 | 1.30E+03 | 1.04E+03 | 1.48E+03 | 1.74E+03 | 1.34E+03 | 4.22E+03 | 1.36E+02 |
| F23 | Mean | 6.90E+02 | 5.69E+02 | 5.68E+02 | 6.96E+02 | 6.04E+02 | 6.91E+02 | 7.76E+02 | 7.56E+03 | 7.79E+02 | 1.18E+03 | 1.53E+03 | 6.41E+02 | 4.69E+02 |
|  | Std | 1.49E+01 | 9.89E+00 | 1.17E+01 | 5.09E+01 | 8.25E+01 | 2.83E+01 | 3.98E+01 | 6.12E+01 | 5.45E+00 | 1.03E+02 | 2.18E+02 | 2.47E+02 | 7.87E+00 |
| F24 | Mean | 1.05E+03 | 9.09E+02 | 8.97E+02 | 9.94E+02 | 9.33E+02 | 1.02E+03 | 8.81E+02 | 1.32E+03 | 9.56E+02 | 1.75E+03 | 1.98E+03 | 1.12E+03 | 8.91E+02 |
|  | Std | 2.77E+01 | 7.56E+00 | 6.59E+00 | 1.06E+02 | 7.37E+01 | 3.12E+01 | 4.30E+01 | 1.11E+02 | 3.88E+00 | 2.04E+02 | 2.25E+02 | 4.29E+02 | 7.43E+00 |
| F25 | Mean | 7.55E+02 | 7.46E+02 | 7.23E+02 | 9.38E+02 | 7.57E+02 | 7.66E+02 | 7.75E+02 | 5.64E+02 | 7.78E+02 | 7.73E+02 | 7.20E+02 | 7.54E+02 | 7.22E+02 |
|  | Std | 6.08E+01 | 3.27E+01 | 2.94E+01 | 7.55E+01 | 8.89E+01 | 4.05E+01 | 5.08E+01 | 4.67E+01 | 1.48E+02 | 6.49E+01 | 5.61E+01 | 2.97E+02 | 2.71E+01 |
| F26 | Mean | 4.73E+03 | 3.30E+03 | 3.32E+03 | 5.46E+02 | 3.96E+03 | 4.43E+03 | 6.06E+03 | 9.65E+03 | 3.92E+03 | 1.10E+04 | 1.38E+04 | 7.86E+03 | 1.89E+03 |
|  | Std | 2.75E+02 | 9.88E+01 | 1.51E+02 | 1.06E+03 | 1.12E+02 | 2.94E+02 | 4.32E+02 | 1.81E+03 | 5.16E+01 | 1.59E+03 | 4.25E+03 | 2.94E+03 | 8.57E+01 |
| F27 | Mean | 7.23E+02 | 6.30E+02 | 5.00E+02 | 2.61E+03 | 6.90E+02 | 6.95E+02 | 5.00E+02 | 8.11E+02 | 6.10E+02 | 5.00E+02 | 5.00E+02 | 6.76E+02 | 5.01E+02 |
|  | Std | 3.58E+01 | 2.07E+01 | 4.69E-04 | 2.88E+02 | 5.45E+01 | 3.41E+01 | 2.45E-04 | 1.51E+01 | 1.53E+02 | 3.33E-04 | 2.19E-04 | 2.59E+02 | 6.84E-04 |
| F28 | Mean | 5.41E+02 | 5.23E+02 | 5.00E+02 | 1.46E+04 | 5.38E+02 | 5.32E+02 | 5.03E+02 | 6.79E+02 | 5.23E+02 | 5.00E+02 | 5.00E+02 | 5.02E+02 | 5.02E+02 |
|  | Std | 4.01E+02 | 2.50E+01 | 4.97E-04 | 1.29E+03 | 8.64E+01 | 3.46E+01 | 1.24E+01 | 2.97E+01 | 1.29E+01 | 2.74E-04 | 8.74E+00 | 1.96E+02 | 5.19E-01 |
| F29 | Mean | 2.39E+03 | 1.24E+03 | 1.65E+03 | 2.52E+03 | 8.08E+02 | 2.44E+03 | 2.89E+03 | 1.58E+03 | 3.06E+03 | 3.41E+03 | 5.45E+03 | 2.18E+03 | 9.79E+02 |
|  | Std | 2.70E+02 | 1.89E+02 | 3.67E+02 | 3.43E+02 | 1.68E+02 | 3.44E+02 | 5.72E+02 | 7.90E+02 | 1.69E+02 | 5.67E+02 | 6.05E+02 | 8.27E+02 | 8.78E+01 |
| F30 | Mean | 4.03E+03 | 2.39E+03 | 1.32E+03 | 3.06 + 04 | 1.59E+04 | 2.56E+03 | 5.99E+03 | 3.12E+03 | 1.94E+05 | 2.41E+03 | 1.46E+06 | 6.13E+03 | 2.17E+03 |
|  | Std | 2.11E+03 | 1.35E+02 | 2.64E+02 | 2.64E+03 | 6.24E+03 | 1.93E+02 | 6.04E+03 | 2.81E+02 | 4.61E+05 | 4.30E+03 | 4.94E+05 | 2.56E+03 | 9.35E+02 |

![img-3.jpeg](img-3.jpeg)

Fig. 4. Diversity curves of the four types of functions.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Trajectory curves of the four types of functions.

### 4.1.1. Parameters sensitivity analysis

Tuning the parameters to achieve the optimal configuration is crucial to improve the performance of the algorithms. There are coordinated methods, such as CRS-Tuning (Crepinšek and Ve, 2016), F-Race (Paquete al., 2002), REVAC (Nannen, 2007), and AVOVA (Zamani et al., 2021; Nadimi-Shahraki and Zamani, 2022). The first three methods are based on the evolutionary process, and ANOVA looks up the F table through the inter-group and intra-group variances to show the difference between various configurations of each group. There are three basic assumptions in ANOVA (Dhiman, 2021), that is normality, variance homogeneity, and sample independence. The hypotheses are satisfied through the experiments. The number of samples selected in the experiments is large, and the normality is guaranteed according to the central limit theorem. The individuals are randomly generated and the null hypothesis is rejected based on the Leneve test of SPSS. Moreover, the validity of variance homogeneity is confirmed.

In addition to the aforementioned adaptive adjustment parameters, there are remaining 4 parameters involved in KCACIL, including the population size ( $\mathrm{NP}_{\text {total }}$ ), selection rate ( $\tau$ ), annealing factor ( $\theta$ ), and revised coefficient of the inferior solutions $(\zeta)$. The optimal combination is obtained through a parameter calibration test. Based on the experience of relevant references, $N P_{\text {total }}=\{40.50 .60 .70\}, \tau=$ $\{0.2,0.3,0.4,0.5\}, \zeta=\{0.5,0.6,0.7,0.8\}$, and $\theta=\{0.1,0.2,0.3,0.4\} . \mathrm{A}$ total of $4 * 4 * 4 * 4=256$ parameter combinations are acquired. The results obtained by Design of the Experiments (DOE) and Multifactor Analysis of Variance (ANOVA) (Shao et al., 2019) are shown in Table 1 and Fig. 3, respectively. The p-value of $N P_{\text {total }}$ is less than the confidence level, and the F-value is the largest. $N P_{\text {total }}$ has a significant impact on
performance. A large population enriches diversity, nonetheless, it results in excessive computational costs and poor convergence speed. A small population leads to an insufficient search and is unable to cover more space. The $\tau$ determines the number of dominant individuals. From Table 1, $\tau * \zeta \leq 0.05$ indicates that there is an interaction between $\tau$ and $\zeta$. In the interaction plots, $\tau=0.3$. and $\zeta=0.7$. Combined with the main effects plot and interaction plots employing ANOVA and Tukey HSD in Fig. 3, $\tau=0.3, N P_{\text {total }}=60 . \zeta=0.7$ and $\theta=0.2$ is the best parameter combination. The corresponding results are top.

### 4.1.2. Comparison with the state-of-the-art algorithms

The performance of the proposed KCACIL and the comparison algorithms is verified by comparing the mean and variance in this section. The mean reflects the holistic optimization performance of the algorithms, while the variance demonstrates stability. The KCACIL and the comparison algorithms are evaluated at 10D, 30D, 50D, and 100D, respectively, as shown in Tables 2-5. The average value of the experimental data is taken as the evaluation standard to avoid a random error. The best mean is indicated in bold.

For the unimodal functions $f_{1}$ and $f_{3}$, CMA-ES, jSO_CMA-ES_LBFGS, and KCACIL find the optimum solutions on $f_{1}$ and $f_{3}$ at 10D, 30D, 50D, and 100D. The LSHADE and EA4eig also obtain the optimal solution on $f_{1}$ and $f_{3}$ at 10D, 30D and 50D. Besides, DE/GM and MPEDE reveal strong exploitation and gain the best stable solution. For the simple multimodal functions $f_{4}-f_{10}$ with multiple local minima, KCACIL shows obvious superiority at 10D, 30D, 50D, and 100D. Solving this kind of problem with traditional methods is difficult. The experimental results on these functions verify the exploration of the algorithms. From
![img-5.jpeg](img-5.jpeg)

Fig. 6. Performance index (PI) at 10D, 30D, 50D, and 100D.

![img-18.jpeg](img-18.jpeg)
(a). $f_{3}$
![img-19.jpeg](img-19.jpeg)
(b). $f_{7}$
![img-20.jpeg](img-20.jpeg)
(c). $f_{17}$
![img-21.jpeg](img-21.jpeg)
(d). $f_{29}$

Fig. 7. Box plots of four typical functions (10D) for the CEC 2017 test suite.
![img-16.jpeg](img-16.jpeg)
(a). $f_{3}$
![img-17.jpeg](img-17.jpeg)
(b). $f_{7}$
![img-18.jpeg](img-18.jpeg)
(c). $f_{17}$
![img-19.jpeg](img-19.jpeg)
(d). $f_{29}$

Fig. 8. Box plots of four typical functions (30D) for the CEC 2017 test suite.
![img-20.jpeg](img-20.jpeg)
(a). $f_{3}$
![img-21.jpeg](img-21.jpeg)
(b). $f_{7}$
![img-16.jpeg](img-16.jpeg)
(c). $f_{17}$
![img-17.jpeg](img-17.jpeg)
(d). $f_{29}$

Fig. 10. Box plots of four typical functions (100D) for the CEC 2017 test suite.
![img-18.jpeg](img-18.jpeg)
(a). $f_{3}$
![img-19.jpeg](img-19.jpeg)
(b). $f_{7}$
![img-20.jpeg](img-20.jpeg)
(c). $f_{17}$
![img-21.jpeg](img-21.jpeg)
(d). $f_{29}$

Fig. 11. Convergence curves of four typical functions (10D) for the CEC 2017 test suite.

![img-22.jpeg](img-22.jpeg)

Fig. 12. Convergence curves of four typical functions (30D) for the CEC 2017 test suite.
![img-23.jpeg](img-23.jpeg)

Fig. 13. Convergence curves of four typical functions (50D) for the CEC 2017 test suite.

Tables 2-5, JADE, LSHADE, CMA-ES, DE/GM, EA4eig, jSO_CMA-ES_LBFGS, and KCACIL all find the optimal solution on $f_{4}$ at 10D. The LSHADE, DE/GM, EA4eig, and KCACIL find the optimal solution of $f_{6}$ at 10D and 30D. The proposed KCACIL acquires the best values on $f_{5}-f_{9}$ at 30D, and gets a minimum of five functions compared to other algorithms at 50D and 100D. It indicates that the cross-regional coevolution based on the elite strategy and the parameter adaptive strategy enriches the population diversity and helps KCACIL escape from the local minimum.

The hybrid functions $f_{11}-f_{20}$ are difficult to optimize, as there is a large number of local optima. The number of local optimums rises exponentially as the dimension of the functions increases. The proposed KCACIL shows excellent performance at 10D, 30D, 50D, and 100D, and obtains the best solution for multiple functions, such as $f_{11}, f_{13}, f_{15}, f_{16}, f_{17}$, and $f_{19}$. It illustrates that the multiple strategies collaboration and crossregional coevolution adopted by KCACIL have outstanding advantages to settle such problems. For the composition functions $f_{21}-f_{30}$, although KCACIL has similar results as other comparison algorithms, its solution quality is overall preferable. KCACIL acquires better results than other algorithms on $f_{21}, f_{23}, f_{26}$, and $f_{29}$, and also reveals outstanding performance on $f_{22}, f_{25}$, and $f_{28}$.

The aforementioned conclusions show that the proposed KCACIL simultaneously incorporates the advantages of DE and EDA, and is provided with strong competitiveness. In addition, based on the various specific knowledge characteristics implicit in the three regions, effective knowledge transfer is implemented through cross-regional self-learning and interactive learning coordinated with multiple strategies guided by reinforcement learning. The implementation promotes population
![img-24.jpeg](img-24.jpeg)
(a), $f_{3}$
![img-25.jpeg](img-25.jpeg)
(b), $f_{7}$
evolution to the potential region and finds the best solution.
The average distance between individuals is calculated as the method mentioned by (Gupta et al., 2020) to illustrate the advantages of the proposed KCACIL in maintaining population diversity. $f_{3}, f_{7}, f_{17}$, and $f_{29}$ are selected representatives of the four types of functions respectively to plot the diversity curves as shown in Fig. 4. The experimental results show that the population diversity of the proposed KCACIL is better than that of most comparison algorithms in various dimensions. The reason for the rich population diversity of KCACIL is the application of the revised strategy of inferior solutions and individual regeneration mechanism, which dramatically reduces the probability of falling into local optimal. The trajectory of the individuals at the first dimension is plotted in Fig. 5 to visualize the search behavior of the algorithms. The trajectory curves indicate the improved strategies of KCACIL are conducive to the movement of individuals and approaching the optimal solution.

Performance index (PI) is introduced to compare the performance of the proposed KCACIL and other comparison algorithms in terms of less error and calculation time, which are attached to different weights (w) respectively according to (Gupta et al., 2020). The PI curves of the algorithms at 10D, 30D, 50D, and 100D are shown in Fig. 6. It can be seen that the proposed KCACIL finds high-quality solutions with small error requirements and limited calculation time.

One function is selected as a representative of each of the four types of functions. Next, $f_{3}, f_{7}, f_{17}$, and $f_{29}$ are considered at 10D, 30D, 50D and 100D, respectively to analyze the stability and convergence. The box plots are composed of 5 points: minimum, lower quartile, median, upper
![img-26.jpeg](img-26.jpeg)

Fig. 14. Convergence curves of four typical functions (100D) for the CEC 2017 test suite.

Table 6
The results of computing complexity.

| Algorithm | Dim | T0 | T1 | $\overline{T 2}$ | $\overline{T 2}-T 1 / T 0$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| JADE | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $1.27 \mathrm{E}+00$ | $1.57 \mathrm{E}+01$ |
|  | 30D |  | 4.22E-01 | $1.53 \mathrm{E}+00$ | $1.62 \mathrm{E}+01$ |
|  | 50D |  | 9.25E-01 | $2.16 \mathrm{E}+00$ | $1.80 \mathrm{E}+01$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $4.74 \mathrm{E}+00$ | $2.13 \mathrm{E}+01$ |
| LEHADE | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $3.67 \mathrm{E}+01$ | $5.32 \mathrm{E}+02$ |
|  | 30D |  | 4.22E-01 | $2.06 \mathrm{E}+01$ | $2.94 \mathrm{E}+02$ |
|  | 50D |  | 9.25E-01 | $1.97 \mathrm{E}+01$ | $2.74 \mathrm{E}+02$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $3.75 \mathrm{E}+01$ | $4.99 \mathrm{E}+02$ |
| CMA-ES | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $2.49 \mathrm{E}+00$ | $3.35 \mathrm{E}+01$ |
|  | 30D |  | 4.22E-01 | $2.55 \mathrm{E}+00$ | $3.10 \mathrm{E}+01$ |
|  | 50D |  | 9.25E-01 | $3.72 \mathrm{E}+00$ | $4.07 \mathrm{E}+01$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $1.11 \mathrm{E}+01$ | $1.14 \mathrm{E}+02$ |
| AAVS_EDA | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $5.30 \mathrm{E}-01$ | $4.96 \mathrm{E}+00$ |
|  | 30D |  | 4.22E-01 | $1.15 \mathrm{E}+00$ | $1.06 \mathrm{E}+01$ |
|  | 50D |  | 9.25E-01 | $1.95 \mathrm{E}+00$ | $1.49 \mathrm{E}+01$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $5.94 \mathrm{E}+00$ | $3.88 \mathrm{E}+01$ |
| DE/GM | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $1.45 \mathrm{E}+00$ | $1.84 \mathrm{E}+01$ |
|  | 30D |  | 4.22E-01 | $3.36 \mathrm{E}+00$ | $4.28 \mathrm{E}+01$ |
|  | 50D |  | 9.25E-01 | $7.35 \mathrm{E}+00$ | $9.37 \mathrm{E}+01$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $2.58 \mathrm{E}+01$ | $3.28 \mathrm{E}+02$ |
| MPEDE | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $2.06 \mathrm{E}+00$ | $2.73 \mathrm{E}+01$ |
|  | 30D |  | 4.22E-01 | $2.65 \mathrm{E}+00$ | $3.25 \mathrm{E}+01$ |
|  | 50D |  | 9.25E-01 | $2.96 \mathrm{E}+00$ | $2.97 \mathrm{E}+01$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $5.75 \mathrm{E}+00$ | $3.60 \mathrm{E}+01$ |
| IDE_EDA | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $1.99 \mathrm{E}+00$ | $2.62 \mathrm{E}+01$ |
|  | 30D |  | 4.22E-01 | $2.65 \mathrm{E}+00$ | $3.25 \mathrm{E}+01$ |
|  | 50D |  | 9.25E-01 | $3.68 \mathrm{E}+00$ | $4.02 \mathrm{E}+01$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $7.30 \mathrm{E}+00$ | $5.86 \mathrm{E}+01$ |
| EA4eig | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $3.44 \mathrm{E}+02$ | $5.01 \mathrm{E}+03$ |
|  | 30D |  | 4.22E-01 | $1.68 \mathrm{E}+02$ | $2.44 \mathrm{E}+03$ |
|  | 50D |  | 9.25E-01 | $2.39 \mathrm{E}+02$ | $3.47 \mathrm{E}+03$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $3.44 \mathrm{E}+02$ | $4.97 \mathrm{E}+03$ |
| jSO_CMA- <br> ES_LBFGS | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $3.53 \mathrm{E}+02$ | $5.14 \mathrm{E}+03$ |
|  | 30D |  | 4.22E-01 | $3.96 \mathrm{E}+02$ | $5.77 \mathrm{E}+03$ |
|  | 50D |  | 9.25E-01 | $4.61 \mathrm{E}+02$ | $6.71 \mathrm{E}+03$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $9.71 \mathrm{E}+02$ | $1.141 \mathrm{E}+04$ |
| RLBSO | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $5.67 \mathrm{E}+01$ | $8.24 \mathrm{E}+02$ |
|  | 30D |  | 4.22E-01 | $6.06 \mathrm{E}+01$ | $8.77 \mathrm{E}+02$ |
|  | 50D |  | 9.25E-01 | $6.97 \mathrm{E}+01$ | $1.00 \mathrm{E}+03$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $7.75 \mathrm{E}+01$ | $1.08 \mathrm{E}+03$ |
| OLBSO | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $1.85 \mathrm{E}+00$ | $2.42 \mathrm{E}+01$ |
|  | 30D |  | 4.22E-01 | $3.76 \mathrm{E}+00$ | $4.87 \mathrm{E}+01$ |
|  | 50D |  | 9.25E-01 | $7.85 \mathrm{E}+00$ | $1.01 \mathrm{E}+02$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $3.28 \mathrm{E}+01$ | $4.30 \mathrm{E}+02$ |
| LDE | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $9.17 \mathrm{E}+00$ | $1.31 \mathrm{E}+02$ |
|  | 30D |  | 4.22E-01 | $1.32 \mathrm{E}+01$ | $1.86 \mathrm{E}+02$ |
|  | 50D |  | 9.25E-01 | $1.75 \mathrm{E}+01$ | $2.42 \mathrm{E}+02$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $3.96 \mathrm{E}+01$ | $5.29 \mathrm{E}+02$ |
| KCACIL | 10D | $\begin{aligned} & 6.86 \mathrm{E}- \\ & 02 \end{aligned}$ | 1.90E-01 | $2.93 \mathrm{E}+00$ | $3.99 \mathrm{E}+01$ |
|  | 30D |  | 4.22E-01 | $2.35 \mathrm{E}+00$ | $2.81 \mathrm{E}+01$ |
|  | 50D |  | 9.25E-01 | $2.44 \mathrm{E}+00$ | $2.21 \mathrm{E}+01$ |
|  | 100D |  | $3.28 \mathrm{E}+00$ | $4.45 \mathrm{E}+00$ | $1.71 \mathrm{E}+01$ |

quartile, and maximum (Moeini et al., 2021). The 51 experimental results of the selected functions in four dimensions for each algorithm are employed as drawing data, and the discrete degree and deviation of the data are reflected by the length of the box, the shape of the upper and lower spacing, and the length of the line at both ends (Corner, 2013). The box plots of Figs. 7-10 display the stability of the algorithms. The experimental results of $f_{3}, f_{7}, f_{17}$, and $f_{29}$ in four dimensions illustrate that

Table 7
Friedman test results of KCACIL and the comparison algorithms for CEC 2017 test suite.

| Algorithms | Mean rank |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
|  | 10D | 30D | 50D | 100D |
| JADE | 7.71 | 9.10 | 8.22 | 8.10 |
| LEHADE | 4.95 | 4.88 | 4.26 | 4.52 |
| CMAES | 9.09 | 6.05 | 5.31 | 4.38 |
| AAVS_EDA | 7.43 | 10.69 | 11.72 | 10.60 |
| DE/GM | 5.91 | 5.36 | 4.67 | 4.71 |
| MPEDE | 6.43 | 5.98 | 6.41 | 6.62 |
| IDE_EDA | 9.05 | 8.72 | 8.55 | 8.81 |
| EA4eig | 4.31 | 4.64 | 5.33 | 7.24 |
| jSO_CMA-ES_LBFGS | 4.48 | 3.47 | 3.52 | 4.90 |
| RLBSO | 9.83 | 10.00 | 9.60 | 10.12 |
| OLBSO | 12.00 | 12.14 | 11.76 | 11.03 |
| LDE | 6.72 | 7.22 | 9.66 | 7.86 |
| KCACIL | 3.09 | 2.74 | 1.98 | 2.10 |
| Crit. Diff $\alpha=0.05$ | 2.70 | 2.70 | 2.70 | 2.70 |
| Crit. Diff $\alpha=0.10$ | 2.45 | 2.45 | 2.45 | 2.45 |

the KCACIL is more stable than other algorithms in most cases. The reason is that the stability of KCACIL is improved by the revised strategy of the inferior solutions as well as other multiple strategies.

Figs. 11-14 show the convergence of various algorithms. The convergence plots are drawn by 14 points according to the CEC 2017 test suite. The horizontal axis represents the evaluated number, and the vertical axis represents the logarithm of the error value in Figs. 11-14. The proposed KCACIL exhibits remarkable superiority over other algorithms in terms of high precision and fast convergence in four dimensions. Although the accuracy is slightly worse on $f_{29}$ at 30D and 100D, the convergence rate is faster. It benefits from the cross-regional collaboration of KCACIL with the elite strategy and the reward feedback of reinforcement learning. Moreover, the self-feedback strategy based on superior parameters also promotes better convergence.

The computing time is compared to illustrate the performance in computing complexity. According to the CEC 2017 test suit, T0, T1, and T2 represent the appointed time, the computing time on $f_{18}$ for 200,000 evaluations of a certain dimension, and the average computing time for 5 times on the same dimension. The experimental results of Table 6 illustrate that the computing complexity of KCACIL is lower than that of most comparison algorithms.

In summary, KCACIL shows evident superiority over other comparison algorithms.

### 4.1.3. Results of the non-parameter tests

Friedman test, Wilcoxon symbolic rank test, Tukey HSD test, and Kolmogorov-Smirnov prediction accuracy test (KSPA) are all adopted in this section to indicate the performance of KCACIL.

Friedman test and Wilcoxon symbolic rank test are routine statistical analysis tests employed in most existing literature. The two nonparametric statistical test methods illustrate whether there are significant differences between the algorithms. The Friedman test in Table 7 compares the significant differences between multiple samples by rank. The statistical results of the KCACIL and 12 comparison algorithms at 10D, 30D, 50D, and 100D are shown in Fig. 15 where the horizontal axis represents all the selected algorithms, and the vertical axis represents the average ranking. The proposed KCACIL ranks optimally for the critical difference of the confidence intervals of $90 \%$ and $95 \%$.

The experimental results with the Wilcoxon symbolic rank test are listed in Table 8, where $R^{+}$and $R^{-}$represent the rank sum of KCACIL superior and inferior to the comparison algorithms, respectively. "yes" means that there is a significant difference between two samples, and "no" means there is no significant difference. The proposed KCACIL exhibits significant differences with respect to others at 10D, 30D, 50D, and 100D within the confidence interval of $90 \%-95 \%$.

The results of the Tukey HSD test shown in Fig. 16 demonstrate the

![img-27.jpeg](img-27.jpeg)

Fig. 15. Rankings obtained through Friedman test for the CEC 2017 test suite.

Table 8
Rankings obtained through the Wilcoxon test.

| D | Algorithm | vs | R+ | R- | Z | p-value | 0.05 | 0.1 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 10 | KCACIL | JADE | $2.76 \mathrm{E}+02$ | $1.20 \mathrm{E}+01$ | $-4.20 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | LSHADE | $2.22 \mathrm{E}+02$ | $1.31 \mathrm{E}+01$ | $-3.10 \mathrm{E}+00$ | $2.00 \mathrm{E}-03$ | yes | yes |
|  |  | CMA-ES | $2.83 \mathrm{E}+02$ | $1.35 \mathrm{E}+01$ | $-3.24 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | AAVS_EDA | $3.48 \mathrm{E}+02$ | $1.39 \mathrm{E}+01$ | $-4.38 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | DE/GM | $2.49 \mathrm{E}+02$ | $1.25 \mathrm{E}+01$ | $-3.38 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | MPEDE | $2.60 \mathrm{E}+02$ | $1.18 \mathrm{E}+01$ | $-3.14 \mathrm{E}+00$ | $2.00 \mathrm{E}-03$ | yes | yes |
|  |  | IDE_EDA | $3.24 \mathrm{E}+02$ | $1.35 \mathrm{E}+01$ | $-3.77 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | EA4eig | $1.85 \mathrm{E}+02$ | $1.32 \mathrm{E}+01$ | $-2.42 \mathrm{E}+00$ | $1.60 \mathrm{E}-02$ | yes | yes |
|  |  | JSO_CMA-ES_LBFGS | $2.18 \mathrm{E}+02$ | $1.28 \mathrm{E}+01$ | $-2.97 \mathrm{E}+00$ | $3.00 \mathrm{E}-03$ | yes | yes |
|  |  | RLBSO | $3.58 \mathrm{E}+02$ | $1.38 \mathrm{E}+01$ | $-4.06 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | OLBSO | $4.35 \mathrm{E}+02$ | $1.50 \mathrm{E}+01$ | $-4.70 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | LDE | $2.90 \mathrm{E}+02$ | $1.32 \mathrm{E}+01$ | $-3.43 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
| 30 | KCACIL | JADE | $2.76 \mathrm{E}+02$ | $1.20 \mathrm{E}+01$ | $-4.20 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | LSHADE | $2.22 \mathrm{E}+02$ | $1.31 \mathrm{E}+01$ | $-3.10 \mathrm{E}+00$ | $2.00 \mathrm{E}-03$ | yes | yes |
|  |  | CMA-ES | $2.83 \mathrm{E}+02$ | $1.35 \mathrm{E}+01$ | $-3.24 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | AAVS_EDA | $3.48 \mathrm{E}+02$ | $1.39 \mathrm{E}+01$ | $-4.38 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | DE/GM | $2.49 \mathrm{E}+02$ | $1.25 \mathrm{E}+01$ | $-3.38 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | MPEDE | $2.60 \mathrm{E}+02$ | $1.18 \mathrm{E}+01$ | $-3.14 \mathrm{E}+00$ | $2.00 \mathrm{E}-03$ | yes | yes |
|  |  | IDE_EDA | $3.24 \mathrm{E}+02$ | $1.35 \mathrm{E}+01$ | $-3.77 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | EA4eig | $1.85 \mathrm{E}+02$ | $1.32 \mathrm{E}+01$ | $-2.42 \mathrm{E}+00$ | $1.60 \mathrm{E}-02$ | yes | yes |
|  |  | JSO_CMA-ES_LBFGS | $2.18 \mathrm{E}+02$ | $1.28 \mathrm{E}+01$ | $-2.97 \mathrm{E}+00$ | $3.00 \mathrm{E}-03$ | yes | yes |
|  |  | RLBSO | $3.58 \mathrm{E}+02$ | $1.38 \mathrm{E}+01$ | $-4.06 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | OLBSO | $4.35 \mathrm{E}+02$ | $1.50 \mathrm{E}+01$ | $-4.70 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | LDE | $2.90 \mathrm{E}+02$ | $1.32 \mathrm{E}+01$ | $-3.43 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
| 50 | KCACIL | JADE | $4.06 \mathrm{E}+02$ | $1.45 \mathrm{E}+01$ | $-4.62 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | LSHADE | $3.47 \mathrm{E}+02$ | $1.39 \mathrm{E}+01$ | $-4.36 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | CMA-ES | $3.32 \mathrm{E}+02$ | $1.44 \mathrm{E}+01$ | $-3.98 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | AAVS_EDA | $4.35 \mathrm{E}+02$ | $1.50 \mathrm{E}+01$ | $-4.70 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | DE/GM | $2.98 \mathrm{E}+02$ | $1.49 \mathrm{E}+01$ | $-3.10 \mathrm{E}+00$ | $2.00 \mathrm{E}-03$ | yes | yes |
|  |  | MPEDE | $4.06 \mathrm{E}+02$ | $1.45 \mathrm{E}+01$ | $-4.62 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | IDE_EDA | $4.35 \mathrm{E}+02$ | $1.50 \mathrm{E}+01$ | $-4.70 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | EA4eig | $3.70 \mathrm{E}+02$ | $1.48 \mathrm{E}+01$ | $-4.35 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | JSO_CMA-ES_LBFGS | $2.94 \mathrm{E}+02$ | $1.55 \mathrm{E}+01$ | $-3.00 \mathrm{E}+00$ | $3.00 \mathrm{E}-03$ | yes | yes |
|  |  | RLBSO | $4.01 \mathrm{E}+02$ | $1.49 \mathrm{E}+01$ | $-4.51 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | OLBSO | $4.35 \mathrm{E}+02$ | $1.50 \mathrm{E}+01$ | $-4.70 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | LDE | $4.35 \mathrm{E}+02$ | $1.50 \mathrm{E}+01$ | $-4.70 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
| 100 | KCACIL | JADE | $4.35 \mathrm{E}+02$ | $1.50 \mathrm{E}+01$ | $-4.70 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | LSHADE | $4.02 \mathrm{E}+02$ | $1.49 \mathrm{E}+01$ | $-4.53 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | CMA-ES | $2.92 \mathrm{E}+02$ | $1.53 \mathrm{E}+01$ | $-2.46 \mathrm{E}+00$ | $1.40 \mathrm{E}-02$ | yes | yes |
|  |  | AAVS_EDA | $4.11 \mathrm{E}+02$ | $1.52 \mathrm{E}+01$ | $-4.18 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | DE/GM | $3.34 \mathrm{E}+02$ | $1.45 \mathrm{E}+01$ | $-3.48 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | MPEDE | $4.06 \mathrm{E}+02$ | $1.45 \mathrm{E}+01$ | $-4.62 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | IDE_EDA | $4.29 \mathrm{E}+02$ | $1.59 \mathrm{E}+01$ | $-4.56 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | EA4eig | $4.28 \mathrm{E}+02$ | $1.53 \mathrm{E}+01$ | $-4.55 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | JSO_CMA-ES_LBFGS | $3.34 \mathrm{E}+02$ | $1.52 \mathrm{E}+01$ | $-4.03 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | RLBSO | $4.32 \mathrm{E}+02$ | $1.60 \mathrm{E}+01$ | $-4.64 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | OLBSO | $4.29 \mathrm{E}+02$ | $1.65 \mathrm{E}+01$ | $-4.57 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |
|  |  | LDE | $4.06 \mathrm{E}+02$ | $1.45 \mathrm{E}+01$ | $-4.62 \mathrm{E}+00$ | $1.00 \mathrm{E}-03$ | yes | yes |

mean difference of the algorithms in four dimensions. The higher the dimension, the greater the difference.

Kolmogorov-Smirnov prediction accuracy test (KSPA), as a nonparametric test, is employed to evaluate whether there are significant differences between the two prediction models (Hassani and Silva, 2015; Fan et al., 2022). In this paper, KSPA is introduced to verify whether
there is a statistically significant difference between the error distribution of the proposed KCACIL and other comparison algorithms through the two-sample two-tailed test. Moreover, the random advantage principle of KSPA is used to determine whether the KCACIL has a smaller random error than the comparison algorithms. All 13 algorithms are performed by this test on different types of functions on the CEC 2014

![img-28.jpeg](img-28.jpeg)
(a), $f_{3}$
![img-29.jpeg](img-29.jpeg)
(b), $f_{2 x}$
Fig. 16. Tukey HSD analysis of $f_{3}, f_{7}, f_{17}, f_{29}$ at $10 \mathrm{D}, 30 \mathrm{D}, 50 \mathrm{D}$, and 100 D .

Table 9
The results of the two-sample Kolmogorov-Smirnov test.

| Algorithm | vs | p-value | vs | p-value |
| :-- | :-- | :-- | :-- | :-- |
| KCACIL | JADE | $2.20 \mathrm{E}-16$ | IDE_KDA | $2.20 \mathrm{E}-16$ |
|  | LSHADE | $4.22 \mathrm{E}-07$ | KA4eig | $6.26 \mathrm{E}-05$ |
|  | CMA-ES | $2.20 \mathrm{E}-16$ | JSO_CMAES_LBFGS | $2.20 \mathrm{E}-16$ |
|  | AAVS_KDA | $3.50 \mathrm{E}-06$ | RLBSO | $2.20 \mathrm{E}-16$ |
|  | DE/GM | $2.403-04$ | OLBSO | $2.20 \mathrm{E}-16$ |
|  | MPEDE | $2.20 \mathrm{E}-16$ | LDE | $2.20 \mathrm{E}-16$ |

and CEC 2017 test suits at four dimensions. The results of 51 independent runs of each function are tested as observations. The null hypothesis means that there is no significant difference between the errors of the algorithms, and it is rejected when the test statistic obtained by the two-tailed KSPA test is less than the significance level.

The results of the two-sample two-tailed KSPA tests are shown in Table 9. Taking $f_{19}$ at 10D on CEC 2017 as an example, all the p-values of the 12 groups are less than 0.01 . Therefore, it is inferred that there are statistically significant differences between the two algorithms. Figs. 17-19 shows the error distribution and empirical cumulative
distribution function (c.d.f.) for 13 algorithms. Based on the c.d.f., the proposed KCACIL has a smaller random error than the other 12 comparison algorithms. In conclusion, the performance of the proposed KCACIL is better than that of the comparison algorithms.

All of the aforementioned results show that these improvement strategies play an important role in KCACIL. The contribution of major strategies is explained by analyzing the effectiveness of strategy composition further in the next sub-section.

### 4.1.4. Effectiveness analysis of strategy composition

The effectiveness analysis of strategy composition is implemented to further evaluate the contribution of the three core improvement strategies to KCACIL. Any one strategy in the proposed algorithm is removed, including KCACIL without cross-regional collaboration, KCACIL without reinforcement learning, and KCACIL without the revised strategy of inferior solutions, while other strategies are maintained. Three corresponding variants are denoted as KCACIL1, KCACIL2, and KCACIL3. KCACIL1 means that cross-regional co-evolution is deleted from KCACIL, while all other strategies are retained. Accordingly, KCACIL2 omits the reinforcement learning mechanism in KCACIL, while KCACIL3 expurgates the revised strategy of the inferior solutions.
![img-30.jpeg](img-30.jpeg)

Fig. 17. The error distribution and empirical c.d.f. of errors on $f_{19}$ of CEC 2017 at 10D.
![img-31.jpeg](img-31.jpeg)

Fig. 18. The error distribution and empirical c.d.f. of errors on $f_{18}$ of CEC 2017 at 50D.

![img-32.jpeg](img-32.jpeg)

Fig. 19. The error distribution and empirical c.d.f. of errors on $f_{21}$ of CEC 2017 at 1000.
![img-33.jpeg](img-33.jpeg)

Fig. 20. The comparison between KCACIL and the three variants.

Table 10
The comparison results of 30 functions.

| Fun | KCACIL1 |  | KCACIL2 |  | KCACIL3 |  | KCACIL |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Mean | Std | Mean | Std | Mean | Std | Mean | Std |
| 1 | 3.08E-06 | 6.60E-06 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 |
| 2 | 3.88E-10 | 7.22E-10 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 |
| 3 | 1.44E-09 | 1.46E-09 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 |
| 4 | 1.30E+00 | 5.53E-01 | 1.29E-01 | 8.60E-02 | 7.67E-03 | 3.32E-02 | 0.00E+00 | 0.00E+00 |
| 5 | 2.67E+01 | 2.37E+00 | 1.09E+01 | 8.04E-01 | 2.48E+00 | 7.55E-01 | 5.18E-01 | 7.83E-02 |
| 6 | 1.57E-06 | 1.52E-06 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 |
| 7 | 3.63E+01 | 7.35E+00 | 2.61E+01 | 2.34E+00 | 1.54E+01 | 8.82E-01 | 1.10E+01 | 3.56E-01 |
| 8 | 2.02E+01 | 7.96E+00 | 3.88E+00 | 1.69E+00 | 9.78E-01 | 5.84E-01 | 6.02E-01 | 3.31E-01 |
| 9 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 |
| 10 | 1.32E+03 | 2.52E+02 | 6.43E+01 | 2.46E+02 | 5.68E+00 | 4.81E+01 | 3.05E+00 | 3.70E+00 |
| 11 | 4.92E+00 | 1.28E+00 | 5.67E+00 | 1.15E+00 | 9.95E-02 | 3.06E-01 | 3.90E-03 | 1.95E-03 |
| 12 | 1.83E+02 | 3.24E+01 | 9.63E+01 | 2.96E+01 | 7.82E+01 | 2.50E+01 | 4.20E+01 | 9.13E+00 |
| 13 | 9.74E+00 | 3.17E+00 | 8.60E+00 | 3.09E+00 | 6.34E+00 | 3.02E+00 | 4.57E+00 | 2.44E+00 |
| 14 | 2.03E+01 | 3.77E+00 | 7.59E+00 | 1.08E+00 | 8.49E-01 | 4.87E-01 | 3.51E-01 | 1.24E-01 |
| 15 | 1.09E+00 | 5.07E-01 | 7.71E-02 | 1.41E-02 | 9.87E-03 | 5.17E-03 | 3.23E-03 | 2.97E-03 |
| 16 | 2.78E+01 | 1.50E+01 | 1.07E+00 | 4.49E+00 | 7.76E-01 | 4.46E-01 | 1.54E-01 | 1.12E-01 |
| 17 | 2.36E+01 | 9.89E+00 | 5.82E+00 | 7.72E+00 | 9.61E-01 | 2.76E+00 | 1.26E-01 | 4.72E-01 |
| 18 | 1.12E+01 | 1.32E+00 | 3.28E-01 | 7.22E-02 | 9.17E-02 | 2.50E-02 | 4.13E-02 | 2.02E-02 |
| 19 | 1.05E+00 | 4.81E-01 | 7.85E-01 | 3.69E-01 | 8.90E-02 | 8.70E-02 | 2.14E-02 | 1.60E-02 |
| 20 | 6.88E+00 | 1.05E+00 | 4.37E-01 | 1.08E-01 | 9.38E-03 | 1.02E-03 | 3.81E-05 | 2.06E-05 |
| 21 | 1.85E+02 | 5.38E+01 | 1.45E+02 | 2.34E+01 | 1.22E+02 | 2.29E+01 | 1.02E+02 | 6.27E+00 |
| 22 | 9.19E+01 | 7.66E+01 | 1.05E+02 | 3.70E+00 | 1.00E+02 | 6.02E-02 | 1.00E+02 | 4.69E-02 |
| 23 | 3.29E+02 | 7.27E+00 | 3.16E+02 | 3.73E+00 | 3.08E+02 | 3.35E+00 | 2.96E+02 | 2.23E+00 |
| 24 | 3.52E+02 | 5.51E+01 | 3.06E+02 | 5.08E+01 | 2.33E+02 | 4.79E+01 | 2.04E+02 | 1.02E+01 |
| 25 | 4.19E+02 | 2.39E+01 | 4.10E+02 | 1.43E+01 | 4.05E+02 | 1.37E+01 | 4.01E+02 | 1.21E+01 |
| 26 | 3.09E+02 | 3.63E-07 | 3.00E+02 | 0.00E+00 | 3.00E+02 | 0.00E+00 | 3.00E+02 | 0.00E+00 |
| 27 | 3.97E+02 | 2.55E+00 | 3.89E+02 | 2.28E+00 | 3.81E+02 | 2.04E+00 | 3.76E+02 | 2.02E+00 |
| 28 | 4.64E+02 | 1.16E+01 | 3.68E+02 | 8.39E+00 | 3.32E+02 | 1.40E+00 | 3.00E+02 | 5.27E-01 |
| 29 | 2.47E+02 | 6.87E+00 | 2.39E+02 | 5.04E+00 | 2.36E+02 | 4.35E+00 | 2.30E+02 | 2.11E+00 |
| 30 | 5.95E+03 | 3.80E+03 | 1.28E+03 | 1.03E+03 | 6.88E+02 | 2.00E+02 | 2.85E+02 | 1.94E+02 |

![img-34.jpeg](img-34.jpeg)

Fig. 21. The fitness landscape of LSHADE, MPEDE, and KCACIL on unimodal functions.

The variants KCACIL1, KCACIL2, KCACIL3, and KCACIL are tested on the CEC 2017 test suite. Each algorithm is run 51 times independently. When the mean and variance are less than $10^{-8}$, they are set to 0 . The experimental results are shown in Fig. 20 and Table 10. The horizontal axis represents the functions, and the vertical axis represents the error values in Fig. 20.

The results in Table 10 show that the performance of KCACIL is optimal. It obtains better optimization results than the three variants, indicating that the three pivotal strategies are effective improvements for KCACIL. The adaptive cross-regional co-evolution based on the elite guidance significantly affects the global performance of KCACIL and improves search efficiency as well as population diversity. The collaboration with other strategies guided by reinforcement learning also promotes the search speed and precision of the proposed algorithm. The revised strategy of the inferior solutions further improves the quality of the solutions. Three strategies are indispensable for KCACIL.

### 4.1.5. Analysis of the fitness landscape

The fitness landscape (Yan et al., 2022) reproduces the behavior of the evolutionary algorithms intuitively and contributes to the quality of solutions by providing rich knowledge information, such as local fitness, distance correlation, landscape features, and topology structure of the solutions. By virtue of the fitness landscape, the relationship between the search space and individuals is constantly and effectively adjusted based on landscape features (Zeng et al., 2022). The abundant knowledge hidden in the fitness landscape is excavated in depth on account of the specific characteristics of the search space. The design and improvement of the algorithms are deemed as the process of investigating the fitness landscape such as canyons or basins, and the best solution is located successfully.

Based on the experimental conclusions presented in the previous sections, the classical LSHADE, multi-population-based MPEDE, and KCACIL are selected in this section to draw their three-dimensional topographic map and two-dimensional plane figure. Different types of functions $f_{2}, f_{4}, f_{6}, f_{23}, f_{24}$, and $f_{26}$ are taken as representatives. The final result of evolution is the three-dimensional topographic map, as shown in Figs. 21-23, where the red dots represent the individuals under different evaluation times, and the green dots represent the optimal
solution. As the evolution continues, the green dots are covered gradually. The proposed KCACIL visibly exhibits superiority through visualization, which demonstrates the proposed KCACIL achieves splendid exploration and exploitation.

### 4.2. Experiments on the CEC 2014 test suite

### 4.2.1. CEC 2014 test suite

The performance of the proposed KCACIL and the selected comparison algorithms are further verified on 30 functions of the CEC 2014 test suite in this sub-section. These benchmark functions with minimization problems (Liang et al., 2014) are widely adopted by the researchers to test the performance of the algorithms. Among 30 functions, $f_{1}-f_{3}$ are 3 unimodal functions, $f_{4}-f_{16}$ is 13 simple multimodal functions, $f_{17}-f_{22}$ are 6 hybrid functions, and $f_{23}-f_{30}$ are 8 composition functions. As specified in the test suite, the termination criterion is max_nfes $=10000 \times D$, where $\mathrm{D}=10,30,50,100$. All the algorithms are carried out in the same experimental environment to ensure the fairness of the experiment and executed independently 51 times to reduce random errors. All experimental data are obtained by Matlab2016b on a PC with a 3.4 GHz Intel (R), Core (TM) i7-6700 CPU, 8 GB of RAM, and a 64-bit Operating System.

### 4.2.2. Comparison with the state-of-the-art algorithms

The comparison algorithms selected in the CEC 2014 test suite are from those tested in the CEC 2017 test suite to fully illustrate their performance. The experimental environment of all the algorithms is identical to guarantee fairness, and the parameters are set as the original literature. The performance is evaluated by the error between the obtained best solution and the optimum for each function. The mean and standard deviation are shown in Tables 11-14. The best mean of each function is indicated in bold.

For the unimodal functions $f_{1}-f_{3}$, LSHADE, CMA-ES, DE/GM, MPEDE, EAAeig, and KCACIL find the optimum solutions on $f_{1}-f_{3}$ at 10D and 30D. The CMA-ES and KCACIL also obtain the optimal solutions on $f_{2}$ and $f_{3}$ at 50D and 100D. For the simple multimodal functions $f_{4}-$ $f_{16}$ with multiple local minima, KCACIL achieves promising results at four dimensions. The proposed KCACIL outperforms the comparison

![img-35.jpeg](img-35.jpeg)

Fig. 22. The fitness landscape of LSHADE, MPEDE, and KCACIL on multimodal functions.

![img-36.jpeg](img-36.jpeg)

Fig. 23. The fitness landscape of LSHADE, MPEDE, and KCACIL on composition functions.

Table 11
The results of KCACIL and the comparison algorithms (10D) for the CEC 2014 test suite.

| Fun |  | JADE | LSHADE | CMA-ES | AAVS_EDA | DE/GM | MPKDE | IDE_EDA | EA4eig | RLBSO | OLBSO | LDE | KCACIL |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| F1 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 4.96E+03 | 0.00E+00 | 0.00E+00 | 7.02E+02 | 0.00E+00 | 3.16E+03 | 1.65E-04 | 4.36E+08 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.73E+04 | 0.00E+00 | 0.00E+00 | 2.10E+03 | 0.00E+00 | 9.77E+03 | 1.02E-04 | 1.62E+08 | 0.00E+00 |
| F2 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.93E+00 | 0.00E+00 | 0.00E+00 | 6.28E+02 | 0.00E+00 | 3.16E+03 | 0.00E+00 | 1.01E+10 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 5.14E-01 | 0.00E+00 | 0.00E+00 | 9.40E+02 | 0.00E+00 | 9.77E+03 | 0.00E+00 | 7.42E+08 | 0.00E+00 |
| F3 | Mean | 1.34E-03 | 0.00E+00 | 0.00E+00 | 4.11E-05 | 0.00E+00 | 0.00E+00 | 6.38E-02 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 4.92E+06 | 0.00E+00 |
|  | Std | 4.24E-03 | 0.00E+00 | 0.00E+00 | 2.03E-05 | 0.00E+00 | 0.00E+00 | 9.43E-02 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 8.56E+06 | 0.00E+00 |
| F4 | Mean | 2.78E+01 | 3.33E+01 | 0.00E+00 | 2.41E+01 | 7.71E+00 | 2.48E+01 | 3.09E+00 | 7.52E+00 | 7.54E-01 | 3.91E+00 | 3.19E+03 | 3.48E+01 |
|  | Std | 1.47E+01 | 1.10E+01 | 0.00E+00 | 1.68E+01 | 8.57E-01 | 1.61E+01 | 1.15E+00 | 0.00E+00 | 1.21E+00 | 1.09E+01 | 2.00E+03 | 0.00E+00 |
| F5 | Mean | 1.77E+01 | 1.57E+01 | 2.00E+01 | 2.04E+01 | 1.62E+01 | 1.74E+01 | 2.04E+01 | 1.79E+01 | 2.00E+01 | 1.99E+01 | 2.11E+01 | 8.69E+00 |
|  | Std | 3.86E+00 | 9.46E+00 | 3.48E-06 | 5.83E-02 | 8.56E+00 | 4.63E+00 | 4.99E-02 | 6.12E+00 | 3.55E-04 | 9.40E-01 | 8.80E-02 | 9.77E+00 |
| F6 | Mean | 5.06E-01 | 0.00E+00 | 3.00E-01 | 8.41E-03 | 0.00E+00 | 2.53E-02 | 1.03E-01 | 0.00E+00 | 7.40E-01 | 2.79E-02 | 1.35E+01 | 0.00E+00 |
|  | Std | 3.45E-01 | 0.00E+00 | 6.32E-01 | 3.78E-03 | 0.00E+00 | 5.97E-02 | 3.25E-01 | 0.00E+00 | 7.41E-01 | 7.86E-02 | 1.41E+00 | 0.00E+00 |
| F7 | Mean | 4.10E-02 | 8.19E-03 | 0.00E+00 | 8.73E-04 | 0.00E+00 | 1.25E-02 | 3.08E-02 | 7.82E-03 | 8.81E-02 | 5.42E-02 | 2.09E+02 | 1.97E-03 |
|  | Std | 1.99E-02 | 8.05E-03 | 0.00E+00 | 8.29E-04 | 0.00E+00 | 1.03E-02 | 2.31E-02 | 5.82E-03 | 5.74E-02 | 6.72E-02 | 7.63E+01 | 4.16E-03 |
| F8 | Mean | 0.00E+00 | 0.00E+00 | 5.80E+01 | 8.76E-01 | 1.59E+00 | 2.37E-08 | 3.78E+00 | 0.00E+00 | 1.19E+00 | 3.79E-01 | 1.33E+02 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 4.81E-01 | 8.28E-01 | 6.96E-01 | 2.28E-08 | 1.86E+00 | 0.00E+00 | 9.14E-01 | 8.00E-01 | 1.60E+01 | 0.00E+00 |
| F9 | Mean | 5.96E+00 | 3.99E+00 | 5.06E+01 | 7.56E-01 | 1.39E+00 | 6.01E+00 | 4.38E+00 | 1.83E+00 | 9.25E+00 | 1.22E+01 | 1.34E+02 | 1.30E+00 |
|  | Std | 1.12E+00 | 1.15E+00 | 3.15E-01 | 7.75E-01 | 1.34E+00 | 1.27E+00 | 1.34E+00 | 1.40E+00 | 4.35E+00 | 9.03E+00 | 1.33E+01 | 4.83E-01 |
| F10 | Mean | 2.42E-02 | 0.00E+00 | 1.25E+03 | 1.09E+02 | 3.96E+01 | 9.18E-01 | 4.01E+02 | 1.20E-02 | 9.54E+01 | 1.84E+02 | 2.54E+03 | 1.25E-02 |
|  | Std | 1.64E-02 | 0.00E+00 | 0.00E+00 | 9.91E+01 | 7.88E+01 | 3.02E-01 | 2.82E+02 | 1.25E-02 | 6.04E+01 | 5.92E+01 | 2.28E+02 | 2.63E-02 |
| F11 | Mean | 3.49E+02 | 7.02E+01 | 1.14E+03 | 2.45E+01 | 5.85E+01 | 3.12E+02 | 8.22E+02 | 4.39E+01 | 3.32E+02 | 4.46E+02 | 2.58E+03 | 1.67E+01 |
|  | Std | 1.14E+02 | 3.68E+01 | 1.85E+02 | 4.07E+01 | 1.27E+02 | 1.48E+02 | 2.57E+02 | 7.10E+01 | 2.06E+02 | 3.25E+02 | 3.07E+02 | 1.82E+01 |
| F12 | Mean | 4.53E-01 | 6.87E-02 | 0.00E+00 | 4.75E-01 | 6.15E-01 | 4.16E-01 | 1.34E+00 | 1.26E-01 | 1.91E-01 | 2.20E-01 | 4.59E+00 | 6.84E-02 |
|  | Std | 7.59E-02 | 1.47E-02 | 0.00E+00 | 4.28E-01 | 3.13E-01 | 8.31E-02 | 3.01E-01 | 6.52E-02 | 1.53E-01 | 1.02E-01 | 1.49E+00 | 2.06E-02 |
| F13 | Mean | 1.07E-01 | 9.96E-02 | 7.98E-03 | 2.84E-02 | 9.87E-03 | 1.24E-01 | 1.06E-01 | 5.49E-02 | 1.06E-01 | 1.86E-01 | 5.96E+00 | 3.20E-02 |
|  | Std | 1.83E-02 | 1.14E-02 | 2.98E-03 | 7.89E-03 | 2.45E-03 | 2.11E-02 | 2.73E-02 | 1.06E-02 | 5.16E-02 | 2.38E-02 | 1.28E+00 | 1.73E-02 |
| F14 | Mean | 1.32E-01 | 9.87E-02 | 4.31E-01 | 3.14E-01 | 3.68E-01 | 1.52E-01 | 2.69E-01 | 9.84E-02 | 1.59E-01 | 9.37E-02 | 7.06E+01 | 9.80E-02 |
|  | Std | 3.47E-02 | 2.62E-02 | 4.87E-02 | 5.23E-02 | 1.01E-01 | 2.38E-02 | 6.75E-02 | 5.25E-02 | 7.43E-02 | 3.36E-02 | 1.65E+01 | 5.95E-02 |
| F15 | Mean | 8.87E-01 | 5.97E-01 | 8.73E-01 | 1.13E+00 | 9.21E-01 | 9.35E-01 | 1.12E+00 | 5.19E-01 | 7.56E-01 | 1.07E+00 | 2.48E+05 | 3.52E-01 |
|  | Std | 1.29E-01 | 5.10E-02 | 2.17E-01 | 2.10E-01 | 2.57E-01 | 1.74E-01 | 4.02E-01 | 5.25E-02 | 1.79E-01 | 6.99E-01 | 2.10E+05 | 5.38E-02 |
| F16 | Mean | 2.11E+00 | 1.34E+00 | 4.32E+00 | 2.95E+00 | 1.88E+00 | 2.10E+00 | 2.57E+00 | 6.78E-01 | 1.99E+00 | 2.56E+00 | 4.49E+00 | 5.46E-01 |
|  | Std | 2.12E-01 | 2.83E-01 | 1.96E-01 | 2.16E-01 | 3.78E-01 | 2.49E-01 | 2.80E-01 | 2.53E-01 | 7.74E-01 | 4.21E-01 | 1.46E-01 | 4.56E-01 |
| F17 | Mean | 2.92E+01 | 2.66E+01 | 1.57E+02 | 2.17E+01 | 6.92E+01 | 2.21E+01 | 1.99E+02 | 4.71E+01 | 6.04E+01 | 2.99E+01 | 1.70E+07 | 4.90E+01 |
|  | Std | 1.44E+01 | 8.85E+00 | 1.33E+02 | 3.03E+01 | 7.45E+01 | 1.44E+01 | 1.11E+02 | 1.72E+01 | 6.14E+01 | 1.85E+01 | 1.76E+07 | 4.94E+01 |
| F18 | Mean | 3.27E+00 | 9.18E-01 | 3.18E+00 | 7.79E-01 | 2.24E+00 | 1.64E+00 | 9.09E+01 | 1.19E+00 | 3.58E+00 | 1.07E+00 | 2.73E+08 | 9.84E-01 |
|  | Std | 1.99E+00 | 1.61E-01 | 5.24E+00 | 5.94E-01 | 2.13E+00 | 7.97E-01 | 2.41E+02 | 1.10E-01 | 2.08E+00 | 1.29E+00 | 2.72E+08 | 1.88E+00 |
| F19 | Mean | 5.49E-01 | 8.50E-02 | 9.03E-01 | 1.15E+00 | 8.04E-01 | 4.85E-01 | 1.76E+00 | 9.39E-01 | 1.32E+00 | 7.81E-01 | 1.21E+02 | 3.92E-01 |
|  | Std | 1.46E-01 | 4.12E-02 | 6.19E-01 | 3.81E-01 | 5.65E-01 | 1.24E-01 | 4.65E-01 | 1.55E-01 | 2.66E-01 | 1.79E-01 | 7.77E+01 | 4.75E-01 |
| F20 | Mean | 1.28E+00 | 3.77E-01 | 1.49E+00 | 8.71E-01 | 8.00E-01 | 8.31E-01 | 2.32E+00 | 2.80E-01 | 1.51E+00 | 4.31E-01 | 3.08E+07 | 3.76E-01 |
|  | Std | 4.01E-01 | 1.72E-01 | 1.92E+00 | 4.02E-01 | 5.11E-01 | 2.28E-01 | 7.62E-01 | 1.09E-01 | 7.23E-01 | 1.94E-01 | 3.61E+07 | 1.14E-01 |
| F21 | Mean | 3.14E+00 | 8.04E-01 | 3.32E+01 | 2.13E+00 | 2.38E+00 | 3.60E+00 | 1.46E+01 | 8.41E-01 | 5.02E+01 | 4.79E-01 | 7.91E+06 | 3.85E+00 |
|  | Std | 2.05E+00 | 2.70E-01 | 5.27E+01 | 4.57E+00 | 5.08E+00 | 1.17E+00 | 1.29E+01 | 8.45E-02 | 6.17E+01 | 2.46E-01 | 8.68E+06 | 7.03E+00 |
| F22 | Mean | 2.57E+00 | 9.22E-01 | 1.37E+02 | 1.90E+01 | 1.43E+01 | 5.50E+00 | 2.74E+01 | 2.22E+00 | 2.52E+01 | 4.73E+00 | 7.25E+02 | 4.15E+00 |
|  | Std | 5.06E-01 | 1.77E-01 | 1.03E+01 | 1.54E+01 | 8.98E+00 | 8.61E-01 | 1.28E+00 | 2.29E-01 | 1.43E+01 | 8.25E+00 | 1.79E+02 | 8.57E+00 |
| F23 | Mean | 3.29E+02 | 3.29E+02 | 2.00E+02 | 3.29E+02 | 3.29E+02 | 3.29E+02 | 2.00E+02 | 3.29E+02 | 3.29E+02 | 3.29E+02 | 7.06E+02 | 2.00E+02 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 6.28E-08 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.92E+02 | 6.25E+01 |
| F24 | Mean | 1.12E+02 | 1.18E+02 | 2.00E+02 | 1.01E+02 | 1.06E+02 | 1.10E+02 | 1.13E+02 | 1.13E+02 | 1.20E+02 | 1.16E+02 | 2.54E+02 | 1.05E+02 |
|  | Std | 1.76E+00 | 2.30E+00 | 0.00E+00 | 2.55E+00 | 3.51E+00 | 3.40E+00 | 6.48E+00 | 8.67E-01 | 7.22E+00 | 9.79E+00 | 2.01E+01 | 1.89E+00 |
| F25 | Mean | 1.45E+02 | 1.36E+02 | 2.00E+02 | 1.92E+02 | 1.95E+02 | 1.20E+02 | 1.56E+02 | 1.19E+02 | 2.00E+02 | 1.23E+02 | 2.28E+02 | 1.21E+02 |
|  | Std | 3.76E+01 | 4.03E+01 | 0.00E+00 | 5.89E+00 | 7.55E+00 | 6.33E+00 | 3.84E+01 | 3.05E+01 | 3.39E-02 | 1.68E+01 | 9.21E+00 | 5.64E+00 |
| F26 | Mean | 1.00E+02 | 1.00E+02 | 2.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.08E+02 | 1.00E+02 |
|  | Std | 2.13E-02 | 1.51E-02 | 0.00E+00 | 4.61E-03 | 3.81E-03 | 1.97E-02 | 1.96E-02 | 1.79E-02 | 5.19E-02 | 5.06E-02 | 3.93E+00 | 1.87E-02 |
| F27 | Mean | 1.04E+02 | 1.01E+02 | 2.00E+02 | 2.24E+02 | 3.00E+02 | 4.24E+01 | 2.23E+02 | 1.32E+00 | 3.81E+02 | 4.24E+01 | 6.98E+02 | 1.31E+00 |
|  | Std | 1.65E+02 | 1.63E+02 | 0.00E+00 | 7.01E+01 | 0.00E+00 | 1.26E+02 | 1.06E+02 | 2.58E-02 | 4.07E+01 | 1.26E+02 | 8.26E+01 | 5.96E-01 |
| F28 | Mean | 3.88E+02 | 3.70E+02 | 2.00E+02 | 1.34E+02 | 3.18E+02 | 3.66E+02 | 2.68E+02 | 3.63E+02 | 3.16E+02 | 3.73E+02 | 1.90E+03 | 3.66E+02 |
|  | Std | 4.32E+01 | 1.37E+00 | 0.00E+00 | 5.40E+01 | 2.99E+01 | 9.49E+00 | 5.07E+01 | 6.62E+01 | 2.97E+01 | 8.71E+00 | 3.44E+02 | 6.78E+01 |
| F29 | Mean | 2.56E+02 | 2.22E+02 | 2.00E+02 | 1.44E+03 | 2.20E+02 | 2.22E+02 | 2.03E+02 | 2.22E+02 | 2.04E+02 | 2.22E+02 | 6.21E+07 | 2.24E+02 |
|  | Std | 6.52E+01 | 3.00E-01 | 0.00E+00 | 6.06E+03 | 1.47E+01 | 4.25E-02 | 1.87E+00 | 2.49E-01 | 2.24E+00 | 8.41E-01 | 3.22E+07 | 1.52E+00 |
| F30 | Mean | 5.13E+02 | 4.89E+02 | 2.00E+02 | 4.94E+02 | 5.25E+02 | 4.84E+02 | 2.66E+02 | 4.85E+02 | 2.50E+02 | 4.63E+02 | 3.63E+05 | 4.88E+02 |
|  | Std | 5.35E+01 | 1.64E+01 | 0.00E+00 | 1.33E+01 | 7.14E+01 | 2.09E+01 | 5.33E+01 | 1.82E+01 | 2.34E+01 | 2.17E-01 | 2.45E+05 | 3.02E+01 |

Table 12
The results of KCACIL and the comparison algorithms (30D) for the CEC 2014 test suite.

| Fun |  | JADE | LSHADE | CMA-ES | AAVS_EDA | DE/GM | MPKDE | IDE_EDA | EA-Seq | RLBSO | OLBSO | LDE | KCACIL |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| F1 | Mean | 6.35E+03 | 0.00E+00 | 0.00E+00 | 2.00E+07 | 2.97E+04 | 0.00E+00 | 1.46E+06 | 1.62E+00 | 1.08E+06 | 2.59E+05 | 4.36E+09 | 0.00E+00 |
|  | Std | 4.60E+03 | 0.00E+00 | 0.00E+00 | 1.63E+07 | 8.77E+04 | 0.00E+00 | 1.31E+06 | 2.57E+00 | 3.96E+05 | 1.53E+05 | 1.07E+09 | 0.00E+00 |
| F2 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 3.97E+07 | 0.00E+00 | 0.00E+00 | 2.27E+03 | 0.00E+00 | 9.27E+03 | 9.27E+02 | 1.26E+11 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 3.05E+08 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 3.51E+03 | 0.00E+00 | 7.51E+03 | 7.51E+02 | 3.05E+08 | 0.00E+00 |
| F3 | Mean | 2.57E+01 | 0.00E+00 | 0.00E+00 | 2.71E+00 | 0.00E+00 | 0.00E+00 | 2.43E+02 | 0.00E+00 | 2.99E-07 | 0.00E+00 | 5.42E+06 | 0.00E+00 |
|  | Std | 1.87E+01 | 0.00E+00 | 0.00E+00 | 2.22E+01 | 0.00E+00 | 0.00E+00 | 2.31E+02 | 0.00E+00 | 4.99E-07 | 0.00E+00 | 9.82E+06 | 0.00E+00 |
| F4 | Mean | 1.03E-01 | 0.00E+00 | 0.00E+00 | 5.60E+00 | 7.95E+01 | 0.00E+00 | 2.86E+01 | 4.59E+00 | 4.87E+01 | 2.08E+01 | 3.68E+04 | 0.00E+00 |
|  | Std | 3.26E-01 | 0.00E+00 | 0.00E+00 | 1.90E+01 | 4.28E+01 | 0.00E+00 | 1.78E+01 | 1.03E+01 | 2.77E+01 | 3.16E+01 | 1.41E+04 | 0.00E+00 |
| F5 | Mean | 2.04E+01 | 2.02E+01 | 2.00E+01 | 2.09E+01 | 2.09E+01 | 2.04E+01 | 2.10E+01 | 2.04E+01 | 2.00E+01 | 2.06E+01 | 2.14E+01 | 2.00E+01 |
|  | Std | 4.31E-02 | 2.21E-02 | 1.59E-04 | 5.56E-02 | 5.63E-02 | 3.53E-02 | 5.72E-02 | 1.45E-01 | 1.61E-02 | 8.17E-02 | 5.00E-02 | 2.40E-02 |
| F6 | Mean | 1.22E+01 | 0.00E+00 | 0.00E+00 | 3.67E-03 | 0.00E+00 | 1.18E+00 | 2.55E+00 | 1.60E-02 | 1.63E+01 | 4.27E+00 | 4.95E+01 | 0.00E+00 |
|  | Std | 1.21E+00 | 0.00E+00 | 0.00E+00 | 2.37E-04 | 0.00E+00 | 1.24E+00 | 3.13E+00 | 2.49E-02 | 3.96E+00 | 3.51E+00 | 1.65E+00 | 0.00E+00 |
| F7 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 2.95E+00 | 0.00E+00 | 0.00E+00 | 2.46E-03 | 0.00E+00 | 7.39E-03 | 1.73E-03 | 1.28E+03 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 6.08E+00 | 0.00E+00 | 0.00E+00 | 4.03E-03 | 0.00E+00 | 7.96E-03 | 3.68E-03 | 2.28E+02 | 0.00E+00 |
| F8 | Mean | 0.00E+00 | 0.00E+00 | 2.10E+01 | 1.43E+01 | 5.27E+00 | 5.68E-14 | 3.19E+01 | 0.00E+00 | 2.65E+01 | 6.85E+01 | 5.20E+02 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 5.03E+01 | 4.58E+00 | 2.53E+00 | 5.99E-14 | 1.07E+01 | 0.00E+00 | 7.72E+00 | 1.29E+01 | 3.51E+01 | 0.00E+00 |
| F9 | Mean | 4.08E+01 | 6.90E+00 | 5.17E+00 | 1.54E+01 | 5.08E+00 | 2.74E+01 | 3.12E+01 | 2.51E+01 | 7.00E+01 | 5.36E+01 | 6.34E+02 | 5.00E+00 |
|  | Std | 4.83E+00 | 1.57E+00 | 1.98E+00 | 5.32E+00 | 1.74E+00 | 9.34E+00 | 3.90E+00 | 7.46E+00 | 1.68E+01 | 4.45E+01 | 3.89E+01 | 2.26E+00 |
| F10 | Mean | 8.80E-01 | 1.08E-02 | 1.71E+03 | 8.38E+02 | 3.59E+02 | 1.76E+00 | 2.67E+03 | 5.84E-02 | 7.28E+02 | 3.95E+03 | 9.29E+03 | 1.25E-02 |
|  | Std | 2.38E-01 | 6.58E-03 | 5.98E+02 | 4.02E+02 | 2.61E+02 | 1.39E+00 | 4.52E+02 | 2.28E-02 | 2.19E+02 | 9.61E+02 | 5.61E+02 | 1.76E-02 |
| F11 | Mean | 2.44E+03 | 1.28E+03 | 1.76E+03 | 8.96E+02 | 5.27E+02 | 2.42E+03 | 3.25E+03 | 1.90E+03 | 2.87E+03 | 4.07E+03 | 9.82E+03 | 1.25E+03 |
|  | Std | 2.20E+02 | 1.26E+02 | 7.32E+02 | 3.78E+02 | 2.41E+02 | 3.93E+02 | 6.20E+02 | 2.61E+02 | 6.06E+02 | 1.08E+03 | 2.79E+02 | 1.57E+02 |
| F12 | Mean | 5.18E-01 | 1.73E-01 | 2.75E-03 | 1.76E-04 | 1.95E+00 | 4.83E-01 | 1.41E+00 | 2.04E-01 | 3.65E-01 | 9.39E-01 | 6.95E+00 | 1.54E-01 |
|  | Std | 4.25E-02 | 1.43E-02 | 3.73E-03 | 2.43E-04 | 2.07E-01 | 5.80E-02 | 1.03E+00 | 1.18E-01 | 1.04E-01 | 5.50E-01 | 1.23E+00 | 2.83E-02 |
| F13 | Mean | 2.53E-01 | 1.28E-01 | 2.00E-02 | 1.76E-01 | 3.26E-02 | 2.13E-01 | 1.98E-01 | 3.20E-01 | 2.27E-01 | 3.56E-01 | 1.18E+01 | 9.74E-02 |
|  | Std | 5.16E-02 | 1.75E-02 | 4.95E-03 | 4.03E-02 | 1.23E-02 | 3.01E-02 | 3.72E-02 | 3.19E-02 | 5.71E-02 | 6.48E-02 | 7.63E-01 | 1.60E-02 |
| F14 | Mean | 2.56E-01 | 2.48E-01 | 4.31E-01 | 2.09E-01 | 3.60E-01 | 2.48E-01 | 3.03E-01 | 2.04E-01 | 3.64E-01 | 2.80E-01 | 4.66E+02 | 2.04E-01 |
|  | Std | 2.27E-02 | 3.81E-02 | 5.32E-02 | 2.63E-02 | 3.29E-02 | 2.75E-02 | 6.71E-02 | 2.42E-02 | 2.01E-01 | 3.95E-02 | 2.61E+01 | 2.26E-02 |
| F15 | Mean | 4.61E+00 | 2.12E+00 | 2.90E+00 | 5.53E+00 | 2.63E+00 | 4.23E+00 | 3.83E+00 | 2.13E+00 | 5.61E+00 | 8.58E+00 | 3.30E+05 | 2.06E+00 |
|  | Std | 5.04E-01 | 1.70E-01 | 4.53E-01 | 1.28E+00 | 3.75E-01 | 6.46E-01 | 1.27E+00 | 3.85E-01 | 1.49E+00 | 3.79E+00 | 1.68E+05 | 1.32E-01 |
| F16 | Mean | 1.01E+01 | 8.54E+00 | 1.37E+01 | 1.17E+01 | 1.09E+01 | 9.98E+00 | 1.16E+01 | 8.57E+00 | 1.06E+01 | 1.16E+01 | 1.44E+01 | 7.79E+00 |
|  | Std | 4.33E-01 | 3.83E-01 | 9.57E-02 | 3.89E-01 | 3.02E-01 | 6.41E-01 | 4.45E-01 | 2.30E-01 | 8.49E-01 | 1.17E+00 | 1.91E-01 | 7.23E-01 |
| F17 | Mean | 1.02E+03 | 1.34E+02 | 1.36E+03 | 3.57E+02 | 2.50E+02 | 2.33E+02 | 1.82E+04 | 1.50E+02 | 1.04E+05 | 1.66E+03 | 6.02E+08 | 2.85E+02 |
|  | Std | 3.67E+02 | 8.64E+01 | 4.52E+02 | 2.09E+02 | 1.17E+02 | 1.91E+02 | 1.88E+04 | 1.12E+02 | 8.05E+04 | 1.57E+02 | 2.68E+08 | 1.19E+02 |
| F18 | Mean | 6.94E+01 | 7.86E+00 | 8.04E+01 | 1.44E+01 | 1.39E+01 | 1.01E+01 | 6.75E+02 | 9.64E+00 | 1.51E+03 | 1.46E+01 | 1.16E+10 | 1.27E+01 |
|  | Std | 3.92E+01 | 3.18E+00 | 3.20E+01 | 6.20E+00 | 6.77E+00 | 4.23E+00 | 8.48E+02 | 4.01E+00 | 2.50E+03 | 1.15E+01 | 4.83E+09 | 4.60E+00 |
| F19 | Mean | 5.56E+00 | 3.73E+00 | 3.74E+00 | 4.01E+00 | 4.02E+00 | 3.68E+00 | 1.09E+01 | 2.98E+00 | 8.50E+00 | 3.93E+00 | 1.53E+03 | 1.96E+00 |
|  | Std | 9.78E-01 | 6.05E-01 | 1.41E+00 | 4.10E-01 | 7.16E-01 | 5.19E-01 | 9.39E-01 | 4.51E-01 | 1.83E+00 | 8.86E-01 | 7.97E+02 | 7.45E-01 |
| F20 | Mean | 3.54E+03 | 3.10E+00 | 1.06E+01 | 1.28E+01 | 3.58E+00 | 8.60E+00 | 4.11E+02 | 5.91E+00 | 6.62E+01 | 4.08E+01 | 1.44E+07 | 4.63E+00 |
|  | Std | 2.74E+03 | 8.39E-01 | 1.54E+01 | 5.27E+00 | 2.06E+00 | 3.47E+00 | 1.43E+02 | 1.73E+00 | 6.99E+01 | 6.33E+00 | 1.35E+07 | 1.63E+00 |
| F21 | Mean | 1.14E+04 | 7.85E+01 | 5.19E+02 | 1.65E+02 | 1.25E+02 | 7.43E+01 | 1.21E+04 | 6.71E+01 | 4.61E+04 | 8.77E+02 | 2.07E+08 | 1.37E+02 |
|  | Std | 3.55E+04 | 6.41E+01 | 1.75E+02 | 9.66E+01 | 5.51E+01 | 8.65E+01 | 1.17E+04 | 7.74E+01 | 7.14E+04 | 1.63E+02 | 1.54E+08 | 1.02E+02 |
| F22 | Mean | 2.35E+02 | 3.96E+01 | 9.04E+01 | 1.48E+02 | 1.19E+02 | 8.56E+01 | 1.04E+02 | 4.57E+01 | 5.65E+02 | 4.70E+02 | 7.64E+04 | 3.80E+01 |
|  | Std | 3.72E+01 | 5.76E+00 | 9.57E+01 | 3.00E+00 | 5.12E+01 | 6.33E+01 | 6.87E+01 | 4.88E+01 | 1.98E+02 | 2.78E+02 | 1.04E+05 | 5.65E+01 |
| F23 | Mean | 3.15E+02 | 3.15E+02 | 2.00E+02 | 3.15E+02 | 3.14E+02 | 3.15E+02 | 2.00E+02 | 3.14E+02 | 3.14E+02 | 3.15E+02 | 2.37E+02 | 3.04E+02 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 2.82E-01 | 6.97E-02 | 0.00E+00 | 0.00E+00 | 9.29E-06 | 3.86E-13 | 0.00E+00 | 4.84E+02 | 3.64E+01 |
| F24 | Mean | 2.24E+02 | 2.24E+02 | 2.00E+02 | 2.23E+02 | 2.23E+02 | 2.25E+02 | 2.00E+02 | 2.24E+02 | 2.35E+02 | 2.17E+02 | 5.74E+02 | 2.00E+02 |
|  | Std | 9.33E-01 | 1.47E+00 | 0.00E+00 | 8.92E-01 | 8.82E-01 | 1.65E+00 | 0.00E+00 | 5.85E-01 | 9.28E+00 | 9.11E+00 | 5.13E+01 | 6.97E+00 |
| F25 | Mean | 2.05E+02 | 2.03E+02 | 2.00E+02 | 2.03E+02 | 2.03E+02 | 2.03E+02 | 2.00E+02 | 2.00E+02 | 2.00E+02 | 2.02E+02 | 4.53E+02 | 2.00E+02 |
|  | Std | 2.04E+00 | 4.85E-02 | 0.00E+00 | 5.23E-02 | 7.68E-01 | 2.77E-01 | 0.00E+00 | 2.64E-02 | 1.08E-01 | 8.50E-01 | 6.10E+01 | 5.20E-02 |
| F26 | Mean | 1.00E+02 | 1.00E+02 | 2.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 3.72E+02 | 1.00E+02 |
|  | Std | 2.80E-02 | 1.23E-02 | 0.00E+00 | 3.55E-01 | 3.69E-02 | 2.78E-02 | 5.08E-02 | 3.55E-02 | 8.13E-02 | 3.57E-02 | 1.13E+02 | 8.85E-03 |
| F27 | Mean | 3.13E+02 | 3.00E+02 | 2.00E+02 | 3.00E+02 | 3.00E+02 | 3.41E+02 | 2.20E+02 | 3.60E+02 | 8.06E+02 | 4.07E+02 | 1.94E+03 | 3.00E+02 |
|  | Std | 2.22E+01 | 0.00E+00 | 0.00E+00 | 6.40E-03 | 1.44E-13 | 5.13E+01 | 6.38E+01 | 5.50E+01 | 8.76E+01 | 3.92E+01 | 1.76E+02 | 0.00E+00 |
| F28 | Mean | 8.08E+02 | 8.39E+02 | 2.00E+02 | 3.65E+02 | 5.07E+02 | 8.45E+02 | 2.44E+02 | 3.86E+02 | 4.03E+02 | 8.49E+02 | 9.00E+03 | 8.48E+02 |
|  | Std | 4.13E+01 | 1.63E+01 | 0.00E+00 | 1.81E+02 | 1.07E+01 | 2.72E+01 | 9.36E+01 | 1.58E+01 | 2.78E+00 | 6.16E+01 | 7.11E+02 | 2.03E+01 |
| F29 | Mean | 7.20E+02 | 7.17E+02 | 2.00E+02 | 6.72E+02 | 7.44E+02 | 7.16E+02 | 2.07E+02 | 2.10E+02 | 2.10E+02 | 7.39E+02 | 8.71E+08 | 7.25E+02 |
|  | Std | 5.10E+00 | 6.12E+00 | 1.54E-13 | 1.27E+02 | 4.92E+02 | 1.67E+00 | 3.50E+00 | 2.05E+00 | 1.79E+00 | 4.59E+01 | 2.91E+08 | 9.97E+00 |
| F30 | Mean | 1.38E+03 | 1.11E+03 | 2.00E+02 | 4.15E+02 | 6.20E+02 | 7.54E+02 | 4.42E+02 | 6.36E+02 | 7.50E+02 | 1.34E+03 | 1.72E+07 | 9.15E+02 |
|  | Std | 5.53E+02 | 3.61E+02 | 2.16E-10 | 5.52E+01 | 2.10E+02 | 4.18E+02 | 1.48E+02 | 7.34E+01 | 1.31E+02 | 5.87E+02 | 8.62E+06 | 2.87E+02 |

Table 13
The results of KCACIL and the comparison algorithms (50D) for the CEC 2014 test suite.

| Fun |  | JADE | LSHADE | CMA-ES | AAVS_EDA | DE/GM | MPKDE | IDE_EDA | EA-Seq | RLBSO | OLBSO | LDE | KCACIL |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| F1 | Mean | 8.47E+04 | 3.72E+02 | 0.00E+00 | 8.99E+07 | 2.00E+04 | 5.03E+04 | 2.99E+06 | 8.23E+04 | 3.18E+06 | 4.44E+06 | 1.01E+10 | 4.61E+00 |
|  | Std | 5.23E+04 | 6.69E+02 | 0.00E+00 | 5.32E+07 | 6.26E+04 | 3.44E+04 | 1.17E+06 | 9.71E+04 | 1.31E+06 | 9.31E+05 | 2.59E+09 | 7.60E+00 |
| F2 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 1.65E+09 | 0.00E+00 | 0.00E+00 | 5.30E+03 | 0.00E+00 | 5.30E+05 | 3.04E+06 | 3.00E+11 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 2.01E+09 | 0.00E+00 | 0.00E+00 | 6.71E+03 | 0.00E+00 | 6.70E+05 | 8.31E+05 | 5.59E+08 | 0.00E+00 |
| F3 | Mean | 5.21E+03 | 0.00E+00 | 0.00E+00 | 1.95E+02 | 0.00E+00 | 8.45E-05 | 3.27E+03 | 0.00E+00 | 1.88E+00 | 1.23E+01 | 1.29E+07 | 0.00E+00 |
|  | Std | 2.20E+03 | 0.00E+00 | 0.00E+00 | 7.58E+02 | 0.00E+00 | 1.04E-04 | 2.57E+03 | 0.00E+00 | 3.71E+00 | 1.97E+01 | 2.41E+07 | 0.00E+00 |
| F4 | Mean | 2.79E+01 | 5.12E+01 | 0.00E+00 | 9.10E+01 | 1.10E+02 | 2.82E+01 | 5.83E+01 | 3.72E+01 | 5.45E+01 | 9.53E+01 | 1.23E+05 | 1.96E+01 |
|  | Std | 3.64E+01 | 4.94E+01 | 0.00E+00 | 4.18E+01 | 8.43E+00 | 4.26E+01 | 2.34E+01 | 2.63E+01 | 2.40E+01 | 2.81E+00 | 3.41E+04 | 4.14E+01 |
| F5 | Mean | 2.05E+01 | 2.02E+01 | 2.00E+01 | 2.11E+01 | 2.11E+01 | 2.05E+01 | 2.09E+01 | 2.02E+01 | 2.01E+01 | 2.09E+01 | 2.14E+01 | 2.00E+01 |
|  | Std | 4.83E-02 | 2.55E-02 | 1.27E-05 | 3.50E-02 | 4.32E-02 | 6.17E-02 | 4.82E-01 | 1.83E-01 | 5.94E-02 | 1.78E-01 | 8.06E-02 | 4.52E-02 |
| F6 | Mean | 2.55E+01 | 5.40E-01 | 0.00E+00 | 4.59E+00 | 8.95E-02 | 5.41E+00 | 6.29E+00 | 2.00E+00 | 2.79E+01 | 1.10E+01 | 8.63E+01 | 5.19E-02 |
|  | Std | 3.33E+00 | 7.70E-01 | 0.00E+00 | 2.16E+00 | 2.83E-01 | 2.38E+00 | 2.63E+00 | 1.54E+00 | 5.07E+00 | 5.29E+00 | 2.23E+00 | 1.64E-01 |
| F7 | Mean | 1.73E-03 | 0.00E+00 | 0.00E+00 | 1.63E+01 | 0.00E+00 | 7.40E-04 | 6.90E-03 | 1.97E-03 | 7.63E-03 | 1.97E-03 | 2.89E+03 | 0.00E+00 |
|  | Std | 3.69E-03 | 0.00E+00 | 0.00E+00 | 1.35E+01 | 0.00E+00 | 2.34E-03 | 8.52E-03 | 4.41E-03 | 7.90E-03 | 4.16E-03 | 3.01E+02 | 0.00E+00 |
| F8 | Mean | 0.00E+00 | 0.00E+00 | 1.07E+01 | 4.23E+01 | 9.95E+00 | 0.00E+00 | 6.29E+01 | 0.00E+00 | 7.55E+01 | 1.13E+02 | 9.70E+02 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 3.92E+00 | 1.24E+01 | 5.18E+00 | 0.00E+00 | 1.74E+01 | 0.00E+00 | 1.52E+01 | 6.42E+01 | 4.39E+01 | 0.00E+00 |
| F9 | Mean | 7.46E+01 | 1.12E+01 | 1.17E+01 | 4.25E+01 | 8.06E+00 | 5.14E+01 | 7.89E+01 | 6.59E+01 | 1.48E+02 | 1.01E+02 | 1.23E+03 | 6.67E+00 |
|  | Std | 9.36E+00 | 1.15E+00 | 3.97E+00 | 9.99E+00 | 3.68E+00 | 1.33E+01 | 1.08E+01 | 1.39E+01 | 3.41E+01 | 8.30E+01 | 9.49E+01 | 2.30E+00 |
| F10 | Mean | 3.28E+00 | 3.75E-02 | 3.92E+03 | 2.81E+03 | 1.13E+03 | 6.81E-01 | 5.50E+03 | 2.46E-01 | 2.26E+03 | 8.08E+03 | 1.65E+04 | 1.75E-01 |
|  | Std | 6.50E-01 | 1.56E-02 | 9.36E+02 | 6.41E+02 | 3.76E+02 | 2.19E-01 | 1.26E+03 | 5.79E-02 | 3.63E+02 | 1.05E+03 | 8.29E+02 | 2.78E-02 |
| F11 | Mean | 5.15E+03 | 3.15E+03 | 3.55E+03 | 2.52E+03 | 1.14E+03 | 5.31E+03 | 6.35E+03 | 3.86E+03 | 6.12E+03 | 7.58E+03 | 1.70E+04 | 3.03E+03 |
|  | Std | 3.58E+02 | 3.70E+02 | 1.80E+03 | 5.33E+02 | 5.37E+02 | 7.21E+02 | 6.67E+02 | 5.60E+02 | 7.86E+02 | 2.42E+03 | 4.22E+02 | 4.49E+02 |
| F12 | Mean | 4.97E-01 | 2.18E+01 | 3.82E-04 | 1.20E-03 | 2.79E+00 | 5.50E-01 | 1.04E+00 | 1.91E-01 | 5.77E-01 | 1.48E+00 | 7.33E+00 | 2.12E-01 |
|  | Std | 7.94E-02 | 2.44E-02 | 5.12E-04 | 8.75E-04 | 1.73E-01 | 1.14E-01 | 1.04E+00 | 1.24E-01 | 1.77E-01 | 5.18E-01 | 5.89E-01 | 1.96E-02 |
| F13 | Mean | 3.16E-01 | 1.65E-01 | 4.31E-02 | 3.89E-01 | 5.30E-02 | 2.61E-01 | 2.58E-01 | 2.86E-01 | 4.04E-01 | 4.26E-01 | 1.30E+01 | 1.87E-01 |
|  | Std | 4.83E-02 | 1.44E-02 | 9.22E-03 | 7.33E-02 | 1.99E-02 | 3.21E-02 | 4.68E-02 | 1.98E-02 | 7.16E-02 | 6.21E-02 | 6.60E-01 | 2.03E-02 |
| F14 | Mean | 3.27E-01 | 3.10E-01 | 4.51E-01 | 2.88E-01 | 4.57E-01 | 3.09E-01 | 4.20E-01 | 2.54E-01 | 3.53E-01 | 3.36E-01 | 7.70E+02 | 2.53E-01 |
|  | Std | 1.12E-01 | 2.06E-02 | 4.24E-02 | 2.31E-02 | 3.67E-02 | 1.49E-02 | 1.80E-01 | 4.91E-02 | 1.65E-01 | 3.16E-02 | 7.14E+01 | 1.99E-02 |
| F15 | Mean | 1.03E+01 | 5.11E+00 | 5.49E+00 | 1.57E+01 | 5.55E+00 | 6.34E+00 | 7.45E+00 | 6.22E+00 | 1.60E+01 | 1.65E+01 | 2.06E+08 | 4.81E+00 |
|  | Std | 1.11E+00 | 4.23E-01 | 7.18E-01 | 1.74E+00 | 7.39E-01 | 1.19E+00 | 1.60E+00 | 5.98E-01 | 6.00E+00 | 1.03E+01 | 7.41E+07 | 5.04E-01 |
| F16 | Mean | 1.86E+01 | 1.68E+01 | 2.25E+01 | 2.13E+01 | 2.01E+01 | 1.82E+01 | 1.99E+01 | 1.73E+01 | 2.02E+01 | 2.15E+01 | 2.42E+01 | 1.61E+01 |
|  | Std | 3.10E-01 | 4.39E-01 | 3.04E-02 | 5.82E-01 | 5.56E-01 | 8.34E-01 | 8.15E-01 | 5.17E-01 | 8.78E-01 | 5.02E-01 | 2.33E-01 | 6.76E-01 |
| F17 | Mean | 4.04E+03 | 1.58E+03 | 2.42E+03 | 1.27E+07 | 5.71E+02 | 1.61E+03 | 2.77E+05 | 1.24E+03 | 5.90E+05 | 1.61E+04 | 1.50E+09 | 5.63E+02 |
|  | Std | 2.45E+03 | 5.07E+02 | 5.33E+02 | 1.05E+07 | 3.50E+02 | 4.39E+02 | 1.81E+05 | 6.45E+02 | 2.44E+05 | 9.90E+03 | 4.91E+08 | 2.64E+02 |
| F18 | Mean | 1.66E+02 | 1.02E+02 | 2.84E+02 | 1.86E+02 | 4.43E+01 | 1.06E+02 | 2.37E+03 | 7.77E+01 | 8.20E+03 | 7.60E+01 | 3.42E+10 | 4.18E+01 |
|  | Std | 5.34E+01 | 1.33E+01 | 7.29E+01 | 2.11E+01 | 1.65E+01 | 1.75E+01 | 1.77E+03 | 1.44E+01 | 9.62E+03 | 6.16E+01 | 8.92E+09 | 1.62E+01 |
| F19 | Mean | 2.49E+01 | 7.72E+00 | 1.11E+01 | 8.22E+00 | 3.60E+01 | 6.92E+00 | 2.05E+01 | 1.63E+01 | 1.82E+01 | 1.08E+01 | 6.55E+02 | 5.75E+00 |
|  | Std | 1.14E+01 | 1.78E+00 | 2.78E+00 | 1.34E+00 | 2.71E+00 | 1.53E+00 | 1.67E+00 | 6.73E+00 | 4.18E+00 | 1.95E+00 | 1.79E+02 | 1.04E+00 |
| F20 | Mean | 1.31E+04 | 1.33E+01 | 2.44E+02 | 5.23E+01 | 9.85E+00 | 7.32E+01 | 8.95E+02 | 2.95E+01 | 8.11E+02 | 1.07E+02 | 3.56E+07 | 9.69E+00 |
|  | Std | 8.53E+03 | 3.84E+00 | 8.69E+01 | 1.88E+01 | 3.45E+00 | 2.27E+01 | 3.28E+02 | 1.27E+01 | 1.81E+03 | 1.25E+01 | 6.20E+07 | 2.62E+00 |
| F21 | Mean | 1.15E+03 | 5.14E+02 | 1.38E+03 | 1.08E+03 | 4.76E+02 | 7.20E+02 | 1.06E+05 | 5.70E+02 | 1.80E+05 | 3.74E+03 | 6.05E+08 | 4.65E+02 |
|  | Std | 3.21E+02 | 1.02E+02 | 4.34E+02 | 3.06E+02 | 1.39E+02 | 2.77E+02 | 9.67E+04 | 1.91E+02 | 1.08E+05 | 3.69E+03 | 3.23E+08 | 1.76E+02 |
| F22 | Mean | 7.38E+02 | 1.37E+02 | 2.95E+02 | 1.92E+02 | 9.90E+01 | 6.40E+02 | 4.90E+02 | 3.97E+02 | 9.87E+02 | 9.53E+02 | 1.66E+06 | 1.04E+02 |
|  | Std | 1.30E+02 | 6.96E+01 | 1.60E+02 | 7.06E+01 | 6.27E+01 | 1.67E+02 | 1.89E+02 | 2.26E+02 | 2.61E+02 | 3.18E+02 | 1.91E+06 | 5.94E+01 |
| F23 | Mean | 3.44E+02 | 3.44E+02 | 2.00E+02 | 3.44E+02 | 3.40E+02 | 3.44E+02 | 2.00E+02 | 3.37E+02 | 3.37E+02 | 3.44E+02 | 4.53E+03 | 3.44E+02 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 2.77E-02 | 5.61E-01 | 0.00E+00 | 0.00E+00 | 3.37E-02 | 3.46E-12 | 0.00E+00 | 8.87E+02 | 0.00E+00 |
| F24 | Mean | 2.75E+02 | 2.75E+02 | 2.00E+02 | 2.60E+02 | 2.70E+02 | 2.76E+02 | 2.00E+02 | 2.67E+02 | 2.69E+02 | 2.70E+02 | 9.21E+02 | 2.00E+02 |
|  | Std | 1.08E+00 | 4.48E-01 | 2.33E-13 | 5.23E+00 | 3.02E+00 | 1.50E+00 | 0.00E+00 | 7.91E+00 | 4.40E+00 | 2.23E+00 | 6.71E+01 | 1.57E+00 |
| F25 | Mean | 2.23E+02 | 2.05E+02 | 2.00E+02 | 2.03E+02 | 2.06E+02 | 2.02E+02 | 2.00E+02 | 2.01E+02 | 2.01E+02 | 2.06E+02 | 8.03E+02 | 2.00E+02 |
|  | Std | 1.94E+00 | 3.52E-01 | 0.00E+00 | 2.78E+00 | 3.48E+00 | 5.50E+00 | 0.00E+00 | 2.53E-01 | 2.12E-01 | 3.67E-01 | 1.13E+02 | 3.07E-01 |
| F26 | Mean | 1.00E+02 | 1.00E+02 | 2.00E+02 | 1.11E+02 | 1.05E+02 | 1.20E+02 | 1.60E+02 | 1.00E+02 | 1.00E+02 | 1.00E+02 | 7.75E+02 | 1.00E+02 |
|  | Std | 4.53E-02 | 1.46E-02 | 0.00E+00 | 2.02E+01 | 2.29E+00 | 4.21E+01 | 5.15E+01 | 6.17E-02 | 1.39E-01 | 6.21E-02 | 1.17E+02 | 2.48E-02 |
| F27 | Mean | 3.79E+02 | 3.31E+02 | 2.00E+02 | 3.85E+02 | 3.45E+02 | 4.44E+02 | 2.00E+02 | 4.09E+02 | 1.41E+03 | 4.44E+02 | 3.69E+03 | 3.04E+02 |
|  | Std | 3.66E+01 | 3.55E+01 | 8.70E-14 | 4.68E+01 | 1.80E+00 | 6.89E+01 | 0.00E+00 | 5.37E+01 | 1.15E+02 | 6.22E+01 | 6.63E+02 | 1.22E+01 |
| F28 | Mean | 1.13E+03 | 1.11E+03 | 2.00E+02 | 6.67E+02 | 7.49E+02 | 1.19E+03 | 2.39E+02 | 3.87E+02 | 4.04E+02 | 1.08E+03 | 1.94E+04 | 1.13E+03 |
|  | Std | 4.60E+01 | 3.88E+01 | 0.00E+00 | 4.33E+02 | 5.37E+01 | 5.29E+01 | 8.20E+01 | 1.14E+01 | 1.66E+01 | 4.67E+01 | 2.75E+03 | 5.83E+01 |
| F29 | Mean | 9.40E+02 | 8.11E+02 | 2.00E+02 | 8.94E+02 | 5.80E+03 | 7.26E+02 | 2.23E+02 | 3.12E+02 | 2.19E+02 | 2.34E+07 | 3.07E+09 | 8.12E+02 |
|  | Std | 5.48E+01 | 4.17E+01 | 0.00E+00 | 3.59E+01 | 2.92E+03 | 1.45E+02 | 3.27E+01 | 1.58E+02 | 3.88E+00 | 2.03E+07 | 5.86E+08 | 4.39E+01 |
| F30 | Mean | 1.00E+04 | 8.98E+03 | 2.00E+02 | 1.01E+04 | 2.55E+03 | 9.54E+03 | 9.80E+02 | 1.26E+03 | 1.27E+03 | 8.29E+03 | 7.43E+07 | 8.76E+03 |
|  | Std | 7.04E+02 | 7.55E+02 | 0.00E+00 | 7.99E+02 | 3.75E+02 | 4.10E+02 | 2.72E+02 | 1.17E+02 | 3.53E+02 | 3.10E+02 | 2.37E+07 | 5.39E+02 |

Table 14
The results of KCACIL and the comparison algorithms (100D) for the CEC 2014 test suite.

| Fun |  | JADE | LSHADE | CMA-ES | AAVS_EDA | DE/GM | MPEDE | IDE_EDA | EA4eig | RLBSO | OLBSO | LDE | KCACIL |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| F1 | Mean | 3.81E+05 | 1.41E+05 | 0.00E+00 | 4.07E+06 | 1.82E+06 | 2.48E+05 | 8.40E+06 | 2.47E+05 | 9.35E+06 | 5.92E+06 | 2.51E+10 | 9.21E+04 |
|  | Std | 1.32E+05 | 3.58E+04 | 0.00E+00 | 1.57E+06 | 1.38E+06 | 8.25E+04 | 2.69E+06 | 1.09E+05 | 2.52E+06 | 2.02E+06 | 5.34E+09 | 2.14E+04 |
| F2 | Mean | 0.00E+00 | 0.00E+00 | 0.00E+00 | 5.36E+09 | 8.30E+04 | 0.00E+00 | 2.18E+04 | 3.72E-05 | 9.45E+01 | 2.12E+03 | 6.20E+11 | 0.00E+00 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 5.36E+09 | 2.64E+04 | 0.00E+00 | 1.95E+04 | 3.06E-05 | 1.31E+02 | 1.17E+03 | 4.67E+08 | 0.00E+00 |
| F3 | Mean | 6.62E+03 | 3.98E-13 | 0.00E+00 | 1.77E+04 | 8.35E+00 | 4.61E+02 | 7.13E+03 | 2.08E-07 | 1.81E+02 | 2.02E+02 | 2.96E+05 | 0.00E+00 |
|  | Std | 6.10E+03 | 1.56E-13 | 0.00E+00 | 6.38E+03 | 2.64E+01 | 5.52E+02 | 3.79E+03 | 1.13E-07 | 7.78E+01 | 5.06E+01 | 5.43E+04 | 0.00E+00 |
| F4 | Mean | 1.28E+02 | 1.68E+02 | 2.77E+01 | 4.03E+02 | 3.01E+02 | 9.54E+01 | 1.35E+02 | 9.04E+01 | 2.02E+01 | 2.11E+02 | 2.16E+01 | 1.54E+02 |
|  | Std | 5.33E+01 | 2.88E+01 | 1.07E+00 | 4.60E+01 | 4.07E+01 | 7.11E+01 | 3.47E+01 | 6.76E+01 | 7.67E-02 | 1.14E-01 | 2.82E-02 | 2.46E+01 |
| F5 | Mean | 2.07E+01 | 2.05E+01 | 2.06E+01 | 2.13E+01 | 2.13E+01 | 2.07E+01 | 2.09E+01 | 2.02E+01 | 9.96E+01 | 3.10E+01 | 1.79E+02 | 2.02E+01 |
|  | Std | 2.73E-02 | 4.75E-02 | 5.59E-01 | 1.33E-02 | 2.49E-02 | 4.12E-02 | 6.33E-01 | 2.29E-01 | 1.13E+01 | 6.37E+00 | 2.98E+00 | 2.57E-02 |
| F6 | Mean | 5.03E+01 | 9.71E+00 | 6.58E-01 | 3.90E+01 | 2.09E+00 | 4.32E+01 | 4.27E+01 | 2.32E+01 | 1.25E-02 | 3.70E-03 | 6.21E+03 | 1.97E-01 |
|  | Std | 1.68E+01 | 2.33E+00 | 4.98E-01 | 3.67E+00 | 2.61E+00 | 7.73E+00 | 5.44E+00 | 4.62E+00 | 3.96E-02 | 6.06E-03 | 4.34E+02 | 4.15E-01 |
| F7 | Mean | 7.40E-04 | 0.00E+00 | 0.00E+00 | 2.87E+02 | 0.00E+00 | 2.22E-03 | 2.91E-02 | 1.48E-03 | 2.45E+02 | 1.31E+02 | 2.12E+03 | 0.00E+00 |
|  | Std | 2.34E-03 | 0.00E+00 | 0.00E+00 | 4.96E+01 | 0.00E+00 | 3.57E-03 | 4.94E-02 | 3.31E-03 | 4.79E+01 | 6.44E+01 | 9.76E+01 | 0.00E+00 |
| F8 | Mean | 0.00E+00 | 1.17E-03 | 3.95E+01 | 1.68E+02 | 2.38E+01 | 1.99E-01 | 1.71E+02 | 0.00E+00 | 7.55E+01 | 1.84E+02 | 2.54E+03 | 2.36E+01 |
|  | Std | 0.00E+00 | 3.84E-04 | 2.30E+00 | 3.05E+01 | 6.72E+00 | 4.20E-01 | 3.59E+01 | 0.00E+00 | 1.52E+01 | 3.78E+01 | 6.77E+01 | 3.08E+00 |
| F9 | Mean | 1.83E+02 | 3.80E+01 | 3.78E+01 | 3.41E+01 | 2.15E+01 | 1.56E+02 | 1.95E+02 | 2.58E+02 | 1.48E+02 | 1.77E+04 | 3.55E+04 | 2.05E+01 |
|  | Std | 2.25E+01 | 3.35E+00 | 5.20E+00 | 3.41E+01 | 9.23E+00 | 3.29E+01 | 2.76E+01 | 3.37E+01 | 3.41E+01 | 2.32E+03 | 1.02E+03 | 2.66E+00 |
| F10 | Mean | 1.57E+01 | 2.00E+01 | 1.09E+04 | 1.10E+04 | 2.88E+03 | 5.13E-01 | 1.32E+04 | 2.12E+00 | 2.26E+03 | 1.78E+04 | 3.56E+04 | 2.82E+01 |
|  | Std | 1.98E+00 | 5.18E+00 | 1.74E+03 | 1.18E+03 | 1.05E+03 | 3.00E-01 | 1.38E+03 | 1.43E+00 | 3.63E+02 | 8.16E+03 | 7.42E+02 | 8.58E+00 |
| F11 | Mean | 1.30E+04 | 1.04E+04 | 8.16E+03 | 9.29E+03 | 3.56E+03 | 1.09E+04 | 1.31E+04 | 1.15E+04 | 6.12E+03 | 1.33E+00 | 7.07E+00 | 8.32E+03 |
|  | Std | 5.81E+02 | 5.04E+02 | 1.75E+03 | 1.43E+03 | 8.03E+02 | 7.59E+02 | 1.56E+03 | 5.02E+02 | 7.86E+02 | 8.03E-01 | 6.42E-01 | 1.04E+03 |
| F12 | Mean | 6.15E-01 | 4.15E-01 | 7.08E-03 | 7.93E-03 | 3.51E+00 | 8.19E-01 | 1.09E+00 | 2.92E-01 | 5.77E-01 | 5.82E-01 | 1.48E+01 | 3.87E-01 |
|  | Std | 1.53E-01 | 3.35E-02 | 5.60E-05 | 2.28E-03 | 2.20E-01 | 1.17E-01 | 3.94E-01 | 1.09E-01 | 1.77E-01 | 8.33E-02 | 6.77E-01 | 4.28E-02 |
| F13 | Mean | 4.15E-01 | 2.37E-01 | 9.85E-02 | 2.06E+00 | 1.13E-01 | 3.77E-01 | 4.37E-01 | 4.33E-01 | 4.04E-01 | 3.43E-01 | 1.75E+03 | 2.95E-01 |
|  | Std | 3.82E-02 | 2.20E-02 | 3.46E-02 | 1.07E+00 | 2.09E-02 | 3.09E-02 | 4.87E-02 | 6.06E-02 | 7.16E-02 | 2.62E-02 | 1.27E+02 | 2.19E-02 |
| F14 | Mean | 3.24E-01 | 3.30E-01 | 4.83E-01 | 5.93E+01 | 4.11E-01 | 3.12E-01 | 4.96E-01 | 2.90E-01 | 3.53E-01 | 5.50E+01 | 8.36E+08 | 2.67E-01 |
|  | Std | 3.10E-02 | 1.16E-02 | 5.93E-02 | 2.17E+01 | 2.98E-02 | 1.76E-02 | 1.93E-01 | 2.57E-02 | 1.65E-01 | 2.28E+01 | 3.05E+08 | 1.86E-02 |
| F15 | Mean | 3.61E+01 | 1.58E+01 | 1.43E+01 | 2.80E+02 | 1.45E+01 | 1.65E+01 | 4.24E+01 | 1.68E+01 | 1.60E+01 | 4.55E+01 | 4.80E+08 | 1.40E+01 |
|  | Std | 3.49E+00 | 8.83E-01 | 1.11E+00 | 1.37E+02 | 8.56E-01 | 2.42E+00 | 1.44E+01 | 2.02E+00 | 6.00E+00 | 1.26E+00 | 2.00E+05 | 2.00E+00 |
| F16 | Mean | 4.08E+01 | 3.95E+01 | 5.58E+01 | 4.35E+01 | 4.45E+01 | 4.04E+01 | 4.39E+01 | 4.13E+01 | 2.02E+01 | 9.30E+05 | 4.55E+09 | 3.85E+01 |
|  | Std | 6.50E-01 | 4.17E-01 | 2.29E-02 | 6.11E-01 | 2.88E-01 | 6.91E-01 | 8.93E-01 | 3.17E-01 | 8.78E-01 | 3.29E+05 | 1.70E+09 | 8.52E-01 |
| F17 | Mean | 2.38E+04 | 4.63E+03 | 5.77E+03 | 6.58E+05 | 3.09E+03 | 2.13E+04 | 1.03E+06 | 6.34E+03 | 5.90E+05 | 3.18E+03 | 8.94E+10 | 3.06E+03 |
|  | Std | 1.15E+04 | 8.13E+02 | 6.11E+02 | 2.06E+06 | 3.95E+02 | 7.23E+03 | 4.72E+05 | 7.25E+02 | 2.44E+05 | 1.19E+03 | 1.10E+10 | 9.61E+02 |
| F18 | Mean | 7.80E+02 | 2.19E+02 | 5.35E+02 | 7.55E+02 | 1.81E+02 | 2.94E+02 | 3.59E+03 | 4.57E+01 | 8.20E+03 | 9.68E+01 | 2.70E+04 | 1.74E+02 |
|  | Std | 4.37E+02 | 1.30E+01 | 1.17E+02 | 2.95E+02 | 2.84E+01 | 4.49E+01 | 4.15E+03 | 3.64E+01 | 9.62E+03 | 5.87E+00 | 6.81E+03 | 1.45E+01 |
| F19 | Mean | 9.59E+01 | 9.73E+01 | 7.35E+01 | 8.29E+01 | 1.27E+02 | 1.03E+02 | 7.03E+01 | 7.83E+01 | 7.82E+01 | 1.66E+03 | 3.47E+04 | 7.03E+01 |
|  | Std | 1.40E+01 | 2.77E+00 | 1.21E+01 | 2.27E+01 | 1.01E+01 | 6.82E+00 | 2.43E+01 | 5.73E+00 | 4.18E+00 | 1.05E+03 | 4.30E+03 | 9.90E-01 |
| F20 | Mean | 7.62E+03 | 1.23E+02 | 4.83E+02 | 4.64E+02 | 3.49E+01 | 5.06E+02 | 3.71E+03 | 8.65E+01 | 8.11E+02 | 2.39E+05 | 2.13E+09 | 4.44E+01 |
|  | Std | 1.54E+04 | 2.66E+01 | 1.00E+02 | 4.29E+01 | 8.88E+00 | 1.61E+02 | 1.42E+03 | 3.77E+01 | 1.81E+03 | 1.29E+05 | 6.90E+08 | 1.06E+01 |
| F21 | Mean | 7.47E+03 | 2.16E+03 | 3.69E+03 | 5.44E+03 | 8.84E+02 | 5.30E+03 | 4.46E+05 | 2.16E+03 | 1.80E+05 | 2.14E+03 | 3.27E+06 | 8.77E+02 |
|  | Std | 3.55E+03 | 4.49E+02 | 6.08E+02 | 1.29E+03 | 1.66E+02 | 2.76E+03 | 1.68E+05 | 1.03E+03 | 1.08E+05 | 7.87E+02 | 2.25E+06 | 3.27E+02 |
| F22 | Mean | 1.98E+03 | 9.86E+02 | 5.85E+02 | 8.02E+02 | 8.77E+01 | 1.64E+03 | 1.89E+03 | 8.77E+02 | 9.87E+02 | 3.48E+02 | 8.84E+03 | 8.39E+02 |
|  | Std | 2.41E+02 | 9.25E+01 | 1.51E+02 | 3.09E+02 | 8.34E+01 | 4.30E+02 | 5.79E+02 | 3.16E+02 | 2.61E+02 | 1.06E-08 | 1.24E+03 | 2.15E+02 |
| F23 | Mean | 3.48E+02 | 3.48E+02 | 3.00E+02 | 3.56E+02 | 3.50E+02 | 3.48E+03 | 2.00E+02 | 3.42E+02 | 3.37E+02 | 3.86E+02 | 2.04E+03 | 3.48E+02 |
|  | Std | 0.00E+00 | 0.00E+00 | 0.00E+00 | 3.86E+00 | 6.85E-01 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 3.83E+00 | 1.34E+02 | 0.00E+00 |
| F24 | Mean | 3.98E+02 | 3.94E+02 | 2.05E+02 | 3.72E+02 | 3.72E+02 | 3.96E+02 | 2.00E+02 | 3.57E+02 | 2.69E+02 | 2.15E+02 | 1.79E+03 | 2.00E+02 |
|  | Std | 4.75E+00 | 2.96E+00 | 0.00E+00 | 7.70E+00 | 2.28E+00 | 4.86E+00 | 0.00E+00 | 0.00E+00 | 4.40E+00 | 2.50E+01 | 2.35E+02 | 3.13E+00 |
| F25 | Mean | 2.60E+02 | 2.00E+02 | 2.00E+02 | 2.01E+02 | 2.00E+02 | 2.00E+02 | 2.00E+02 | 2.01E+02 | 2.01E+02 | 2.01E+02 | 1.74E+03 | 2.00E+02 |
|  | Std | 4.66E+00 | 0.00E+00 | 0.00E+00 | 1.81E+00 | 0.00E+00 | 0.00E+00 | 0.00E+00 | 2.53E+00 | 2.12E-01 | 3.15E+01 | 3.01E+02 | 1.24E+00 |
| F26 | Mean | 2.00E+02 | 2.00E+02 | 2.00E+02 | 2.00E+02 | 1.75E+02 | 2.00E+02 | 1.90E+02 | 2.01E+02 | 1.00E+02 | 8.88E+02 | 9.19E+02 | 2.00E+02 |
|  | Std | 6.57E-03 | 0.00E+00 | 0.00E+00 | 9.88E-03 | 4.10E+01 | 2.64E-02 | 3.15E+01 | 5.27E-02 | 1.39E-01 | 8.28E+01 | 8.29E+02 | 0.00E+00 |
| F27 | Mean | 9.80E+02 | 3.82E+02 | 2.00E+02 | 1.13E+03 | 3.08E+02 | 1.06E+03 | 2.00E+02 | 6.09E+02 | 1.41E+03 | 9.54E+02 | 3.69E+03 | 3.00E+02 |
|  | Std | 7.79E+01 | 3.12E+01 | 0.00E+00 | 1.14E+02 | 8.57E+00 | 7.86E+01 | 0.00E+00 | 7.17E+01 | 1.15E+02 | 5.02E+02 | 6.63E+02 | 1.50E-02 |
| F28 | Mean | 2.25E+03 | 2.23E+03 | 4.00E+02 | 1.07E+03 | 2.87E+03 | 2.23E+03 | 2.00E+02 | 1.01E+03 | 4.04E+02 | 4.68E+03 | 1.94E+04 | 2.18E+03 |
|  | Std | 7.42E+01 | 4.87E+01 | 0.00E+00 | 1.13E+03 | 6.73E+02 | 2.19E+02 | 0.00E+00 | 2.34E+01 | 1.66E+01 | 7.97E+01 | 2.75E+03 | 6.28E+01 |
| F29 | Mean | 1.39E+03 | 7.72E+02 | 2.08E+02 | 1.05E+04 | 1.75E+04 | 1.04E+03 | 2.71E+02 | 1.03E+02 | 2.19E+02 | 8.94E+07 | 3.07E+09 | 7.46E+02 |
|  | Std | 8.85E+01 | 5.87E+01 | 0.00E+00 | 5.57E+03 | 2.61E+04 | 2.53E+02 | 3.35E+01 | 3.47E+02 | 3.88E+00 | 3.43E+07 | 5.86E+08 | 3.33E+01 |
| F30 | Mean | 9.11E+03 | 8.31E+03 | 4.10E+02 | 9.77E+03 | 3.71E+03 | 6.49E+03 | 2.23E+03 | 8.24E+03 | 1.27E+03 | 9.79E+03 | 7.43E+07 | 5.30E+03 |
|  | Std | 1.20E+03 | 9.70E+02 | 4.56E-02 | 1.32E+03 | 1.47E+03 | 1.37E+03 | 1.19E+03 | 1.17E+02 | 3.53E+02 | 8.70E+02 | 2.37E+07 | 6.32E+02 |

![img-37.jpeg](img-37.jpeg)
(a), $f_{3}$
![img-38.jpeg](img-38.jpeg)
(b), $f_{15}$
![img-39.jpeg](img-39.jpeg)
(c), $f_{19}$
![img-40.jpeg](img-40.jpeg)
(d), $f_{26}$

Fig. 24. Box plots of four typical functions for the CEC 2014 test suite.
Fig. 25. Convergence curves of four typical functions for the CEC 2014 test suite.

Table 15
Friedman test results of KCACIL and the comparison algorithms for the CEC 2014 test suite.

| Algorithms | Mean rank |  |  |  |
| :-- | :-- | :-- | :-- | :-- |
|  | 10D | 360 | 560 | 1060 |
| JADE | 6.75 | 7.47 | 7.38 | 7.53 |
| LSHADE | 4.43 | 4.10 | 4.38 | 5.17 |
| CMAES | 6.90 | 4.60 | 4.27 | 3.92 |
| AAVS_EDA | 6.92 | 6.57 | 7.30 | 8.30 |
| DE/GM | 5.82 | 5.67 | 5.43 | 5.63 |
| MPEDE | 5.67 | 5.55 | 6.22 | 6.48 |
| IDE_EDA | 8.03 | 7.38 | 7.08 | 7.30 |
| EA\&sig | 4.15 | 4.40 | 4.55 | 5.20 |
| RLBSO | 7.63 | 8.30 | 7.85 | 6.12 |
| OLBSO | 6.22 | 8.53 | 8.65 | 7.65 |
| LDE | 11.73 | 11.98 | 12.00 | 11.30 |
| KCACIL | 3.75 | 3.45 | 2.88 | 3.40 |
| Crit. Diff $\alpha=0.05$ | 2.43 | 2.43 | 2.43 | 2.43 |
| Crit. Diff $\alpha=0.10$ | 2.20 | 2.20 | 2.20 | 2.20 |

algorithms on $f_{5}, f_{8}, f_{14}, f_{15}$, and $f_{16}$ at 10D, 30D and 50D, and also on $f_{5}$, $f_{7}, f_{9}, f_{14}$, and $f_{15}$ at 100D. It indicates that KCACIL has strong exploration to escape from the local minimum. KCACIL achieves the best results on $f_{20}$ at 10D, on $f_{19}$ and $f_{22}$ at 30D, and is also superior to the comparison algorithms on $f_{17}, f_{19}, f_{20}$, and $f_{21}$ at both 50D and 100D. For the composition functions $f_{23}-f_{30}$, the solutions obtained by KCACIL are
preferable. KCACIL shows outstanding superiority on $f_{24}, f_{25}$, and $f_{26}$ at four dimensions.

The stability and convergence are analyzed on $f_{2}, f_{15}, f_{19}$, and $f_{26}$ at the four dimensions. In Fig. 24, the stability of the algorithms is shown through the box plots. The experimental results show that KCACIL is robust. The convergence curves of the algorithms are listed in Fig. 25 where the horizontal axis represents the evaluated number, and the vertical axis represents the logarithm of the error value. KCACIL has a remarkable advantage in terms of high precision and fast convergence at four dimensions.

All the results indicate that the KCACIL shows a significant superiority over the CEC 2014 test suite.

### 4.2.3. Results of the non-parameter tests

Friedman test, post-hoc test, and Kolmogorov-Smirnov prediction accuracy test (KSPA) are adopted in this subsection. Friedman test compares the significant differences between multiple samples by rank at four dimensions in Table 15. The results at 50D are shown in Fig. 27 where the horizontal axis represents the selected algorithms, and the vertical axis represents the average ranking. KCACIL ranks optimally for the critical difference of the confidence intervals of $90 \%$ and $95 \%$.

Post-hoc test is implemented to determine the location of the differences between the algorithms. KCACIL is selected as the control algorithm. The $p$-value is from the Friedman test, and the computation methods of adjusted $p$-value are introduced, including the methods of Bonferroni-Dunn, Holm, Hochberg, Hommel, Holland, and Rom. The

Table 16
Results of post-hoc test using KCACIL as control algorithm ( $\mathrm{D}=50$ ).

| Algorithms | z-value | p-value | Bonferroni | Holm | Hochberg | Hommel | Holland | Rom |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LDE | $9.79 \mathrm{E}+00$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{4 . 6 5 E - 0 3}$ | $\mathbf{4 . 7 8 E - 0 3}$ |
| OLBSO | $6.19 \mathrm{E}+00$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{5 . 1 2 E - 0 3}$ | $\mathbf{5 . 2 6 E - 0 3}$ |
| RLBSO | $5.34 \mathrm{E}+00$ | $\mathbf{0 . 0 0 E + 0 0}$ | $\mathbf{1 . 0 0 E - 0 6}$ | $\mathbf{1 . 0 0 E - 0 6}$ | $\mathbf{1 . 0 0 E - 0 6}$ | $\mathbf{1 . 0 0 E - 0 6}$ | $\mathbf{5 . 6 8 E - 0 3}$ | $\mathbf{5 . 8 4 E - 0 3}$ |
| JADE | $4.83 \mathrm{E}+00$ | $\mathbf{1 . 0 0 E - 0 6}$ | $\mathbf{1 . 5 0 E - 0 5}$ | $\mathbf{1 . 1 0 E - 0 5}$ | $\mathbf{1 . 1 0 E - 0 5}$ | $\mathbf{9 . 0 0 E - 0 6}$ | $\mathbf{6 . 3 9 E - 0 3}$ | $\mathbf{6 . 5 7 E - 0 3}$ |
| AAVS_EDA | $4.74 \mathrm{E}+00$ | $\mathbf{2 . 0 0 E - 0 6}$ | $\mathbf{2 . 3 0 E - 0 5}$ | $\mathbf{1 . 3 0 E - 0 5}$ | $\mathbf{1 . 5 0 E - 0 5}$ | $\mathbf{1 . 5 0 E - 0 5}$ | $\mathbf{7 . 3 0 E - 0 3}$ | $\mathbf{7 . 5 1 E - 0 3}$ |
| IDE_EDA | $4.51 \mathrm{E}+00$ | $\mathbf{6 . 0 0 E - 0 6}$ | $\mathbf{7 . 1 0 E - 0 5}$ | $\mathbf{3 . 9 0 E - 0 5}$ | $\mathbf{3 . 9 0 E - 0 5}$ | $\mathbf{3 . 9 0 E - 0 5}$ | $\mathbf{8 . 5 1 E - 0 3}$ | $\mathbf{8 . 7 6 E - 0 3}$ |
| MPEDE | $3.58 \mathrm{E}+00$ | $\mathbf{3 . 4 3 E - 0 4}$ | $\mathbf{3 . 7 7 E - 0 3}$ | $\mathbf{1 . 7 1 E - 0 3}$ | $\mathbf{1 . 7 1 E - 0 3}$ | $\mathbf{1 . 7 1 E - 0 3}$ | $\mathbf{1 . 0 2 E - 0 2}$ | $\mathbf{1 . 0 5 E - 0 2}$ |
| DE/GM | $2.74 \mathrm{E}+00$ | $\mathbf{6 . 1 6 E - 0 3}$ | $6.78 \mathrm{E}-02$ | $\mathbf{2 . 4 6 E - 0 2}$ | $\mathbf{2 . 4 6 E - 0 2}$ | $\mathbf{2 . 4 6 E - 0 2}$ | $\mathbf{1 . 2 7 E - 0 2}$ | $\mathbf{1 . 3 1 E - 0 2}$ |
| EA\&sig | $1.79 \mathrm{E}+00$ | $7.34 \mathrm{E}-02$ | $8.07 \mathrm{E}-01$ | $2.20 \mathrm{E}-01$ | $1.37 \mathrm{E}-01$ | $1.37 \mathrm{E}-01$ | $\mathbf{1 . 7 0 E - 0 2}$ | $\mathbf{1 . 6 7 E - 0 2}$ |
| LSHADE | $1.61 \mathrm{E}+00$ | $1.07 \mathrm{E}-01$ | $1.18 \mathrm{E}+00$ | $2.20 \mathrm{E}-01$ | $1.37 \mathrm{E}-01$ | $1.37 \mathrm{E}-01$ | $\mathbf{2 . 5 3 E - 0 2}$ | $\mathbf{2 . 5 0 E - 0 2}$ |
| CMA-ES | $1.49 \mathrm{E}+00$ | $1.37 \mathrm{E}-01$ | $1.51 \mathrm{E}+00$ | $2.20 \mathrm{E}-01$ | $1.37 \mathrm{E}-01$ | $1.37 \mathrm{E}-01$ | $\mathbf{5 . 0 0 E - 0 2}$ | $\mathbf{5 . 0 0 E - 0 2}$ |

![img-41.jpeg](img-41.jpeg)

Fig. 26. The error distribution and empirical c.d.f. of errors on $f_{17}$ of CEC 2014 at 50D.
![img-42.jpeg](img-42.jpeg)

Fig. 27. Friedman test for the CEC 2014 test suite ( $\mathrm{D}=50$ ).
results at 50D are listed in Table 16 where the $p$-values and the adjusted $p$-values exhibit differences in these algorithms. Statistical differences exist between the KCACIL and comparison algorithms in most cases.

KSPA verifies whether there is a statistically significant difference between the error distribution of KCACIL and the comparison algorithms. All 13 algorithms are tested on $f_{17}$ at 50D on the CEC 2014 test suite. The results of 51 independent runs of each function are tested as observations. The error distribution and empirical cumulative distribution function (c.d.f.) are shown in Fig. 26. Based on the c.d.f., the proposed KCACIL has a smaller random error than other algorithms. The performance of KCACIL outperforms that of the comparison algorithms.

### 4.3. Result analysis and conclusion

The experimental results and statistic analysis in the CEC 2014 and

CEC 2017 test suites illustrate that a knowledge-driven co-evolutionary algorithm assisted by cross-regional interactive learning achieves a trade-off between exploration and exploitation by utilizing the complementary superiority of DE and EDA. KCACIL is superior to most state-of-the-art algorithms and variants with reinforcement learning in terms of solution accuracy, convergence speed, and stability in most cases.

The DE provides powerful exploration, while the EDA promotes local exploitation. The comprehensive collaboration is implemented from the three aspects of diverse algorithms, improvement strategies, and individual interaction. Based on the specific knowledge implicit in three regions, the cross-regional co-evolution guided by reinforcement learning with opposition-based learning, elite strategy, and the revised strategy of the inferior solutions balances the convergence rate and population diversity. The mechanisms of cross-regional self-learning, interactive learning, and self-feedback promote effective knowledge

Table 17
Results on DED problem.

| max. $n f e x$ |  | AAVS_EDA | MPEDE | EA4eig | LDE | KCACIL |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 5.00E+04 | Mean | 1.91E+08 | 1.86E+08 | 9.78E+07 | 1.32E+08 | 2.32E+07 |
|  | Max | 2.32E+08 | 2.28E+08 | 1.28E+08 | 1.69E+08 | 7.76E+07 |
|  | Min | 1.18E+08 | 1.06E+08 | 8.31E+07 | 9.72E+07 | 6.95E+06 |
| 1.00E+05 | Mean | 1.81E+07 | 1.63E+07 | 9.85E+06 | 1.16E+07 | 6.18E+06 |
|  | Max | 2.19E+07 | 2.06E+07 | 1.42E+07 | 2.11E+07 | 8.53E+06 |
|  | Min | 1.09E+07 | 9.78E+06 | 8.13E+06 | 8.96E+06 | 4.27E+06 |
| 1.50E+05 | Mean | 9.35E+06 | 9.10E+06 | 7.12E+06 | 8.73E+06 | 4.02E+06 |
|  | Max | 1.06E+07 | 1.00E+07 | 8.96E+06 | 9.16E+06 | 4.89E+06 |
|  | Min | 8.14E+06 | 8.03E+06 | 4.72E+06 | 5.75E+06 | 3.04E+06 |

![img-43.jpeg](img-43.jpeg)

Fig. 28. Stability of KCACIL and the comparison algorithms in DED.
sharing and transfer. Furthermore, search efficiency and convergence accuracy are facilitated.

The inferior solutions with small $Q$ feedback of reinforcement learning and dense aggregation are improved by the revised strategy of the inferior solutions to ameliorate premature convergence. The collaboration of the strategies promotes the rapid population evolution toward the optimal direction and improves the accuracy of the solutions. The individual regeneration mechanism activates the population and effectively avoids evolutionary stagnation. The adaptive strategies of multiple parameters dynamically adjust KCACIL to the appropriate state in different stages. The robustness is improved.

## 5. KCACIL for engineering applications problems

### 5.1. KCACIL for the dynamic economic dispatch problem

The dynamic economic dispatch (DED) problem (Das and Suganthan, 2011) belongs to the hourly scheduling problem. Power demand changes with hours, and a clear 24-h power generation plan is to be
developed. The objective and constraints of DED are shown in Eqs. (56)(63).

First, the definition of the symbol used in this engineering application problem is given.

| $i$ | The generating unit. $i=\left(1.2 \ldots . N_{G}\right)$. |
| :-- | :-- |
| $P_{0}$ | The real power delivery (in MW) of generator $i$ during time $t$. |
| $N_{G}$ | The number of the scheduled online generating units. |
| $T$ | The total time of scheduling. |
| $P D$ | The total loads. |
| $P L$ | The total losses. |
| $P_{i}^{\text {min }}$ | The minimum value allowed for power delivery of the generating unit $i$. |
| $P_{i}^{\text {max }}$ | The maximum value allowed for power delivery of the generating unit $i$. |
| $P_{i}^{-\mathrm{t}}$ | The power generation of unit $i$ at time $t-1$. |
| $U R_{i}$ | The upper ramp rate limits. |
| $D R_{i}$ | The lower ramp rate limits. |
| $n$ | The number of hours spent. |
| $N$ | The total number of units. |

# Minimize 

Table 18
Results of problems RC01-RC08.

| Criteria |  | RC01 | RC02 | RC03 | RC04 | RC05 | RC06 | RC07 | RC08 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Best | $f$ | 1.8940E+02 | 7.0490E+03 | $-4.1165 \mathrm{E}+03$ | $-3.8801 \mathrm{E}-01$ | $-\mathbf{3 . 5 6 8 1 E}+\mathbf{0 2}$ | 1.9528E+00 | 1.9641E+00 | 2.0000E+00 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 1.3144E-02 | 0.0000E+00 |  |
| Median | $f$ | 1.8942E+02 | 7.0490E+03 | $-4.1165 \mathrm{E}+03$ | $-3.6734 \mathrm{E}-01$ | $-1.5951 \mathrm{E}+02$ | 2.5373E+00 | 1.7746E+00 | 2.0000E+00 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 4.7919E-02 | 0.0000E+00 |
| Mean | $f$ | 1.8948E+02 | 7.0490E+03 | $-4.0813 \mathrm{E}+03$ | $-3.8725 \mathrm{E}-01$ | $-1.7772 \mathrm{E}+02$ | 2.3044E+00 | 1.9707E+00 | 2.0000E+00 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 9.3080E-04 | 1.2647E-01 | 0.0000E+00 |
| Worst | $f$ | 1.9010E+02 | 7.0490E+03 | $-3.8987 \mathrm{E}+03$ | $-3.8569 \mathrm{E}-01$ | $-7.7457 \mathrm{E}+01$ | 2.0880E+00 | 1.9969E+00 | 2.0000E+00 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 2.1338E-02 | 6.5846E-01 | 0.0000E+00 |
| Std | $f$ | 1.9382E-01 | 7.2483E-08 | 3.2872E+02 | 5.0017E-04 | 6.3142E+01 | 2.4946E-01 | 2.5322E-01 | 0.0000E+00 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 4.2623E-03 | 1.8675E-01 | 0.0000E+00 |
| FR(\%) |  | 100 | 100 | 100 | 100 | 100 | 63 | 0 | 100 |
| C |  | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,7,12)$ | $(0,0,0)$ |  |

Table 19
Results of problems RC09-RC16.

| Criteria |  | RC09 | RC10 | RC11 | RC12 | RC13 | RC14 | RC15 | RC16 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Best | $f$ | 2.5577E+00 | 1.0765E+00 | 1.0283E+02 | 2.9248E+00 | 2.6887E+04 | 5.8505E+04 | 2.9944E+03 | 3.2213E-02 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| Median | $f$ | 2.5577E+00 | 1.0765E+00 | 1.0885E+02 | 2.9248E+00 | 2.6887E+04 | 5.8505E+04 | 2.9944E+03 | 3.7246E-02 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| Mean | $f$ | 2.5577E+00 | 1.0770E+00 | 1.1050E+02 | 2.9248E+00 | 2.6887E+04 | 5.8505E+04 | 2.9944E+03 | 4.3878E-02 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| Worst | $f$ | 2.5577E+00 | 1.0846E+00 | 9.9956E+01 | 2.9248E+00 | 2.6887E+04 | 5.8505E+04 | 2.9944E+03 | 1.1508E-01 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| Std | $f$ | 0.0000E+00 | 3.4758E-04 | 5.4881E+00 | 0.0000E+00 | 1.0258E-10 | 8.2577E-06 | 4.6414E-13 | 1.9268E-02 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| FR(\%) |  | 100 | 100 | 23 | 100 | 100 | 100 | 56 | 100 |
|  |  | $(0,0,0)$ | $(0,0,0)$ | $(0,0,2)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,1,3)$ | $(0,0,0)$ |  |

Table 20
Results of problems RC17-RC25.

| Criteria |  | RC17 | RC18 | RC19 | RC20 | RC21 | R22 | RC23 | RC24 | RC25 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Best | $f$ | 1.2665E-02 | 6.0597E+03 | 1.6702E+00 | 2.6390E+02 | 2.3524E-01 | 5.2623E-01 | 1.6070E+01 | 2.5438E+00 | 1.6161E+03 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |  |
| Median | $f$ | 1.2665E-02 | 6.0597E+03 | 1.6702E+00 | 2.6390E+02 | 2.3524E-01 | 5.2810E-01 | 1.6070E+01 | 2.5432E+00 | 1.6223E+03 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |  |
| Mean | $f$ | 1.2665E-02 | 6.0672E+03 | 1.6702E+00 | 2.6390E+02 | 2.3524E-01 | 5.2879E-01 | 1.6070E+01 | 2.5496E+00 | 1.6497E+03 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |  |
| Worst | $f$ | 1.2665E-02 | 6.0910E+03 | 1.6702E+00 | 2.6390E+02 | 2.3524E-01 | 5.3282E-01 | 1.6070E+01 | 2.5760E+00 | 1.7671E+03 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |  |
| Std | $f$ | 2.3046E-10 | 2.1354E+00 | 4.4573E-18 | 0.0000E+00 | 1.1331E-16 | 1.8182E-03 | 1.7045E-14 | 7.5038E-03 | 4.7388E+01 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| FR(\%) |  | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 100 | 68 |
|  |  | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,2,3)$ |  |

Table 21
Results of problems RC26-RC33.

| Criteria |  | RC26 | RC27 | RC28 | RC29 | RC30 | RC31 | RC32 | RC33 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Best | $f$ | 3.9147E+01 | 5.2445E+02 | 1.4621E+04 | 2.9649E+06 | 2.6147E+02 | 0.0000E+00 | $-3.0666 E+04$ | 2.6394E+00 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| Median | $f$ | 4.6368E+01 | 5.2445E+02 | 1.4621E+04 | 2.9649E+06 | 2.6147E+00 | 0.0000E+00 | $-3.0666 E+04$ | 2.6448E+00 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| Mean | $f$ | 4.7941E+01 | 5.2472E+02 | 1.4622E+04 | 2.9649E+06 | 2.6147E+00 | 0.0000E+00 | $-3.0666 E+04$ | 2.6456E+00 |
|  | $\nu$ | 8.3184E-05 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| Worst | $f$ | 5.0774E+01 | 5.2976E+02 | 1.4640E+04 | 2.9649E+06 | 2.6147E+00 | 0.0000E+00 | $-3.0666 E+04$ | 2.6551E+00 |
|  | $\nu$ | 2.0793E-03 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| Std | $f$ | 5.2660E+00 | 1.0336E+00 | 3.7942E+00 | 1.4258E-09 | 1.1272E-12 | 0.0000E+00 | 3.7130E-12 | 4.5002E-03 |
|  | $\nu$ | 4.1590E-04 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 |
| FR(\%) |  | 90 | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
|  |  | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ |

Table 22
Results of problems RC34-RC41.

| Criteria |  | RC34 | RC35 | RC36 | RC37 | RC38 | RC39 | RC40 | RC41 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Best | $f$ | 1.9262E-01 | 8.3269E-02 | 6.5148E-02 | 3.1884E-02 | 3.3547E+00 | 3.6909E+00 | 8.7655E+00 | 3.3901E-02 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 1.0216E+00 | 1.7277E-01 |
| Median | $f$ | 4.7800E-01 | 9.3438E-02 | 1.0594E-01 | 4.1809E-01 | 5.2693E+00 | 6.4644E+00 | 2.3978E+00 | 2.9759E+00 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 1.1997E+00 | 4.7302E-01 |
| Mean | $f$ | 5.0618E-01 | 9.7237E-02 | 1.0744E-01 | 4.7531E-01 | 5.7537E+00 | 6.9620E+00 | 2.5585E+01 | 1.4267E+03 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 1.2458E+00 | 2.7826E+00 |
| Worst | $f$ | 8.7110E-01 | 1.3912E-01 | 1.7257E-01 | 1.5519E+00 | 9.0943E+00 | 1.0612E+01 | 5.1299E+01 | 2.9300E+04 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 1.3759E+00 | 9.3329E+00 |
| Std | $f$ | 1.9464E-01 | 1.3126E-02 | 2.3779E-02 | 4.1430E-01 | 1.4381E+00 | 1.7705E+00 | 1.0870E+01 | 5.8469E+03 |
|  | $\nu$ | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 0.0000E+00 | 3.1679E-01 | 3.4531E+00 |
| FR(\%) |  | 100 | 71 | 100 | 100 | 0 | 0 | 0 | 100 |
|  |  | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,1,0)$ | $(0,3,1)$ | $(0,1,5)$ | $(0,0,0)$ |

Table 23
Results of problems RC42-RC49.

| Criteria |  | RC42 | RC43 | RC44 | RC45 | RC46 | RC47 | RC48 | RC49 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Best | $f$ | 1.7715E-01 | 1.2409E-01 | $-6.1280 \mathrm{E}+03$ | 3.6059E-02 | 2.3586E-02 | 1.1412E-02 | 1.6792E-02 | 1.0524E-02 |
|  | $\nu$ | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 |
| Median | $f$ | 5.9234E+01 | 3.8799E+01 | $-5.9683 \mathrm{E}+03$ | 3.9920E-02 | 2.2126E-02 | 2.1226E-02 | 3.5298E-02 | 2.7963E-02 |
|  | $\nu$ | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 |
| Mean | $f$ | 4.4060E+01 | 4.3094E+01 | $-5.9663 \mathrm{E}+03$ | 4.6039E-02 | 2.1250E-02 | 2.1250E-02 | 3.4492E-02 | 2.6119E-02 |
|  | $\nu$ | 2.7002E-02 | 5.1352E-04 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 |
| Worst | $f$ | $-2.0393 \mathrm{E}+00$ | 2.2629E+01 | $-5.8203 \mathrm{E}+03$ | 1.0108E-01 | 3.4603E-02 | 3.4603E-02 | 8.3843E-02 | 3.7352E-02 |
|  | $\nu$ | 2.8308E-01 | 1.2835E-02 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 |
| Std | $f$ | 3.1812E+01 | 2.3629E+01 | 8.9272E+01 | 1.7440E-02 | 5.1366E-03 | 5.1366E-03 | 1.5091E-02 | 7.6242E-03 |
|  | $\nu$ | 6.9326E-02 | 2.5673E-03 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 | 0.0000E +00 |
| FR(\%) |  | 71 | 0 | 100 | 100 | 100 | 100 | 100 | 100 |
| C |  | $(0,0,0)$ | $(0,6,3)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ | $(0,0,0)$ |

Table 24
Results of problems RC50-RC57.

| Criteria | RC50 | RC51 | RC52 | RC53 | RC54 | RC55 | RC56 | RC57 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Best | $f$ | 1.4975E-02 | 4.4228E+03 | 3.7629E+03 | 5.6587E+03 | 3.6383E+03 | 7.8307E+03 | 1.4361E+04 | 1.0153E+04 |
|  | $\nu$ | 0.0000E+00 | 3.0270E-03 | 0.0000E+00 | 2.4653E-04 | 2.1213E-03 | 2.4045E-03 | 4.2300E-03 | 8.3179E-04 |
| Median | $f$ | 1.5802E-02 | 4.3546E+03 | 4.7335E+03 | 5.1436E+03 | 4.4348E+03 | 5.1056E+03 | 1.5557E+04 | 5.3832E+03 |
|  | $\nu$ | 0.0000E+00 | 7.3367E-03 | 0.0000E+00 | 7.6985E-03 | 1.5955E-02 | 5.2874E-03 | 1.2629E-02 | 2.1664E-03 |
| Mean | $f$ | 1.8031E-02 | 4.2337E+03 | 4.8238E+03 | 5.3350E+03 | 4.3166E+03 | 6.3408E+03 | 1.3040E+04 | 6.6262E+03 |
|  | $\nu$ | 0.0000E+00 | 1.5856E-02 | 2.9667E-03 | 1.6337E-02 | 4.4042E-02 | 5.5193E-03 | 1.1901E-02 | 2.4241E-04 |
| Worst | $f$ | 6.8341E-02 | 4.1366E+03 | 6.0505E+03 | 5.3845E+03 | 4.4645E+03 | 9.4123E+03 | 1.2812E+04 | 5.9073E+03 |
|  | $\nu$ | 0.0000E+00 | 1.1506E-01 | 2.4191E-02 | 7.6658E-02 | 2.2336E-01 | 9.3757E-03 | 1.9674E-02 | 4.3799E-03 |
| Std | $f$ | 1.0548E-02 | 1.5689E+02 | 6.7624E+02 | 2.7704E+02 | 1.0548E+03 | 1.2369E+03 | 1.6778E+03 | 1.7470E+03 |
|  | $\nu$ | 0.0000E+00 | 2.3606E-02 | 6.0406E-03 | 1.8647E-02 | 5.7876E-02 | 1.6397E-03 | 4.0561E-03 | 8.2652E-04 |
| FR(\%) |  | 100 | 0 | 69 | 0 | 0 | 0 | 0 | 0 |
| C |  | $(0,0,0)$ | $(0,1,0)$ | $(0,0,0)$ | $(0,3,1)$ | $(0,2,1)$ | $(0,1,3)$ | $(0,3,1)$ | $(0,1,1)$ |

Table 25
Performance measure of all algorithms.

| Algorithms | Performance Measure |
| :-- | :--: |
| IDE,EDA | 0.4365 |
| LSHADE | 0.3076 |
| KCACIL | 0.2813 |

$F_{c}=\sum_{k=1}^{n} \sum_{i=1}^{N_{t i}} P_{i k}\left(P_{i k}\right)$
$F_{i k}\left(P_{i k}\right)=a_{i} P_{i k}^{2}+b_{i} P_{i i}+c_{i}+\left|c_{i} \sin \left(f_{i k}\left(P_{i k}^{\max }-P_{i k}\right)\right)\right|$
Subject to
$\sum_{i=1}^{N_{t i}} P_{i i}=P_{i k}+P_{i, i}$
$P_{i, i}=\sum_{i=1}^{N_{t i}} \sum_{j=1}^{N_{t i}} P_{i j} B_{i j} P_{j i}$
$P_{i}^{\min } \leq P_{i i} \leq P_{i}^{\max }$
$\max \left(P_{i}^{\min }, U R_{i}-P_{i}\right) \leq P_{i} \leq \min \left(P_{i}^{\max }, P_{i}^{(-1}-D R_{i}\right)$
$f_{k}=\sum_{i=1}^{n} \sum_{i=1}^{N} F_{i}\left(P_{i k}\right)+\lambda_{1}\left(\sum_{i=1}^{n} \sum_{i=1}^{N} P_{i i}-P_{i k}\right)+\lambda_{2}\left(\sum_{i=1}^{n} \sum_{i=1}^{N} P_{i i}-P_{i \text { lim }}\right)$
$P_{i \text { lim }}=\left\{\begin{array}{c}P_{(i+1)}-D R_{i}, P_{i i}<P_{(i+1)}-D R_{i} \\ P_{(i+1)}+U R_{i}, P_{i i}>P_{(i+1)}+U R_{i} \\ P_{i i}, \text { otherwise }\end{array}\right.$
Eq. (56) is the objective function of production cost. $F_{i k}\left(P_{i k}\right)$ represents the cost function of the unit with valve point loading effect, and is
listed in Eq. (57), where $a_{i}, b_{i}$ and $c_{i}$ represent the cost functions of the cost coefficients in the $i$ th unit, and $e_{i}$ and $f_{i}$ represent the cost coefficients of the valve point loading effect. The solution is liable to be trapped in the local optimum due to the valve point loading, which adds nonlinearity to the system. The limited DEDP is under a variety of constraints that rest on practical assumptions. Eq. (58) represents the constraint of power balance. $P_{i, i}$ is acquired with B-coefficients in Eq. (59). This constraint is corresponding to the balance principle between PD, PL, and the total power generation.

Eq. (60) is the generator constraint. The lower and upper bounds exist in the output power of each generating unit, and it can not exceed these two boundaries. The climbing rate limits the operating range of the in-line units, and the operation of the generator between two cycles is adjusted in practical industrial production. Power generation increases or decreases the up and down ramp rate limits. If it increases, $P_{i k}-$ $P_{i}^{(-1} \leq U R_{i}$. When it decreases, $P_{i}^{(-1}-P_{i k} \leq D R_{i}$. The accession of ramp rate limits modifies the constraints of generator operation as shown in Eq. (61). The fitness function model is adopted in this paper, as shown in Eq. (62) where $\lambda_{1}$ and $\lambda_{2}$ are penalty parameters. It is employed for simulation to evaluate the fitness values of the individuals. Under the unit and system constraints, the fuel cost is minimized. The penalty factor causes the algorithm to be given a higher cost, instead of estimating that the solution is not feasible. The penalty term embodies the violation of the equality constraint, which produces a high cost on the penalty function. $P_{i \text { lim }}$ is shown in Eq. (63).

The performance of KCACIL and the comparison algorithms are verified by the engineering practical problem. All the algorithms run 25 times independently. The mean, maximum, and minimum of the objective functions are obtained when the max_nfes is 50000, 100000, and 150000, respectively. The results are listed in Table 17, and the values of KCACIL are less than other comparison algorithms.

The scatter graphs of all the algorithms under the three evaluation conditions are shown in Fig. 28. The horizontal axis represents all the algorithms, and the vertical axis represents the minimum values of the corresponding algorithms. Each algorithm consists of 25 points, and

each dot represents a one-run result. The more concentrated the distribution of points is, the better the stability of the corresponding algorithm is. The lower the point is, the better the performance is. Fig. 28 illustrates that the stability of KCACIL is better than that of other comparison algorithms.

### 5.2. KCACIL for the CEC 2020 test suite with the real-world optimization problems

All the algorithms are verified on the CEC 2020 test suite to further illustrate the performance of the proposed KCACIL in solving engineering practical problems. The CEC 2020 test suite contains 57 constrained functions representing different real-world optimization problems (Kumar et al., 2020). These functions are roughly divided into 6 types of problems, including 7 industrial chemical processes (RC01-RC07), 7 process synthesis and design problems (RC08-RC14), 19 mechanical engineering problems (RC15-RC33), 11 power system problems (RC34-RC44), 6 power electronic problems (RC45-RC50), and 7 livestock feed ration optimization problems (RC51- RC57). The relevant experimental rule is carried out in accordance with the CEC 2020 test suite. Each algorithm independently runs 25 times. Ultimately, detailed results are obtained on the 57 practical problems. The performance statistics include the objective function values $f$ and the constraint violation $v$ of the best, median, and worst solutions through 25 independent runs on each single constrained real-world problem. The mean objective function value and the mean constraint violation together with the standard deviations, as well as the feasibility rate $F R$ and the tuple $c$ are all listed in Tables 18-24. FR and $c$ are calculated according to the methods in (Kumar et al., 2020).

The experimental results reveal that the proposed KCACIL finds 38 feasible solutions for 57 constrained real-world optimization problems with $100 \%$ efficiency, as shown in Tables 18-24. The performance of KCACIL is better than that of the comparison algorithms in solving these problems, as shown in Table 25.

## 6. Conclusion and future work

A knowledge-driven co-evolutionary algorithm assisted by crossregional interactive learning (KCACIL) is proposed to achieve mutual promotion by a comprehensive collaboration between diverse algorithms, strategies, and cross-regional individuals. The results of KCACIL and other comparison algorithms on the CEC 2014, CEC 2017, and CEC 2020 test suites, as well as the real-world engineering application problems show that the holistic performance of KCACIL is preferable to that of the comparison algorithms.

The Friedman, Wilcoxon, post-hoc, and KSPA tests are employed to statistically analyze the experimental results, which verify that the KCACIL outperforms most state-of-the-art algorithms and advanced variants with reinforcement learning. The computing complexity is analyzed to reveal the superiority in computing time. The convergence curves and boxplots indicate that the convergence speed and stability of KCACIL are superior to that of the comparison algorithms. The effectiveness of strategy composition is also verified. The fitness landscape reproduces the relationship between the search space and individuals, which is conducive to the design of the algorithm. The diverse eliteguided mutation strategies and a self-feedback strategy based on successful experience achieve self-learning and cross-regional interactive learning, and individual collaboration is implemented. The feedback of reinforcement learning on the individual information guides the collaboration of opposition-based learning, the interaction mechanism, and the revised strategy of the inferior solutions. The dynamic adjustment strategies of multiple parameters ameliorate search efficiency. The diversity and convergence are balanced. Furthermore, the KCACIL is applied to the engineering practical problems including the DED and 57 constrained real-world optimization problems on CEC 2020 test suite. The results illustrate the practicability of KCACIL in solving these
application problems.
The collaborative framework designed in this paper improves the performance of the single usage of DE or EDA. It can be extended to other meta-heuristic algorithms and corresponding applications to achieve more powerful optimization effects to solve complex practical problems, such as large-scale black-box optimization problems, and multi-objective distributed flow shop scheduling problems with energy consumption constraints.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

This work was financially supported by the Excellent Postgraduate Innovation Star Project of Gansu Provincial Education Department (2023CXZX-476). It was also supported by the National Natural Science Foundation of China under grant 62063021, the Key Program of National Natural Science Foundation of Gansu Province under Grant 23JRRA784, the High-level Foreign Experts Project of Gansu Province under Grant 22JR10KA007, the Key Research Programs of Science and Technology Commission Foundation of Gansu Province (21YP5WA086), and Lanzhou Science Bureau Project (2018-rc-98), respectively.

## References

Awad, N.H., Ali, M.Z., Suganthan, P.N., Liang, J.J., Qu, R.Y., 2016. Problem Definitions and Evaluation Criteria for the CEC2017 Special Session and Competition on Single Objective Real-Parameter Numerical Optimization.
Aye, C.M., Pholdee, N., Yildiz, A.B., Burzerat, S., Sait, S.M., 2019. Multi-surrogateassisted metabeuristics for crashworthiness optimization. Int. J. Veh. Des. 80, 223-240. https://doi.org/10.1504/LIVD.2019.109866.
Benitez-Hidalgo, A., Nebeu, A.J., García-Nieto, J., Oregi, I., Del Ser, J., 2019. iMetaDY: a Python framework for multi-objective optimization with metabeuristics. Swarm Evol. Comput. 31, 100598 https://doi.org/10.1016/j.swarm.2019.100598.
Bosman, P.A.N., Gallagher, M., 2018. The importance of implementation details and parameter settings in black-box optimization: a case study on Gaussian estimation-of-distribution algorithms and circles-in-a-square packing problems. Soft Comput. 22, 1209-1223. https://doi.org/10.1007/s00500-016-2408-5.
Bujok, P., Kolenovsky, P., 2022. Eigen crossover in cooperative model of evolutionary algorithms applied to CEC 2022 single objective numerical optimization. 2022 IEEE Congr. Evol. Comput. CEC 2022-Conf. Proc. https://doi.org/10.1109/ CEC55065.2022.9870433.
Cao, H., He, Q., Wang, H., Xiang, Z., Zhang, N., Yang, Y., 2022. An estimation of distribution algorithm based on variational Bayesian for point-set registration. IEEE Trans. Evol. Comput. 26, 926-940. https://doi.org/10.1109/TEVC.2021.3139304.
Chen, S.P., Wu, J., Liu, X.Y., 2021. EMORL: effective multi-objective reinforcement learning method for hyperparameter optimization. Eng. Appl. Artif. Intell. 104, 10431S https://doi.org/10.1016/j.engapput.2021.104315.
Chih, M., 2022. Stochastic stability analysis of particle swarm optimization with pseudo random number assignment strategy. Eur. J. Oper. Res. 305, 562-593. https://doi. org/10.1016/j.ejor.2022.06.009.
Corner, S., 2013. The box plot: an alternative way to present a distribution of observations. Statistics Corner 22, 114-116.
Crepinnck, M., Ve, N., 2016. Parameter tuning with chess rating system (CRS-Tuning) for meta-heuristic algorithms. Inf. Sci. 372, 446-469. https://doi.org/10.1016/j. ins.2016.08.066.
Dang, Q.L., Gao, W.F., Gong, M.G., 2022. An efficient mixture sampling model for Gaussian estimation of distribution algorithm. Inf. Sci. 608, 1157-1182. https://doi. org/10.1016/j.ins.2022.07.016.
Dai, S., Suganthan, P.N., 2011. Problem definitions and evaluation criteria for CEC 2011 competition on testing evolutionary algorithms on real world optimization problems. Electronics 1-42.
Dhiman, G., 2021. ESA: a hybrid bio-inspired metabeuristic optimization approach for engineering problems. Eng. Comput. 37, 327-353. https://doi.org/10.1007/s00366-019-00826-xi.
Du, Y., Li, J.Q., Chen, X.L., Duan, P.Y., Pan, Q.K., 2022. Knowledge-based reinforcement learning and estimation of distribution algorithm for flexible job shop scheduling

problem. IEEE Trans. Emerg. Top. Comput. Intell 1-15. https://doi.org/10.1109/ TETC1.2022.3145706.

Fan, G.P., Zhang, L.Z., Yu, M., Hong, W.C., Dong, S.Q., 2022. Applications of random forest in multivariable response surface for short-term load forecasting. Int. J. Electr. Power Energy Syst. 139, 108073 https://doi.org/10.1016/j.ipspes.2022.108073.
Fang, H., Zhou, A., Zhang, H., 2018. Information fusion in offspring generation: a case study in DE and EDA. Swarm Evol. Comput. 42, 99-108. https://doi.org/10.1016/j .swwo.2018.02.014.
Givi, H., Hubalovska, M., 2023. Skill optimization algorithm: a new human-based metahearistic technique. Comput. Mater. Continua (CMC) 74, 179-202. https://doi .org/10.32604/cmc.2023.030379.
Gupta, S., Abderazek, H., Yildiz, B.S., Yildiz, A.R., Mirjalili, S., Sait, S.M., 2021. Comparison of metahearistic optimization algorithms for solving constrained mechanical design optimization problems. Expert Syst. Appl. 183 https://doi.org/ 10.1016/j.eswa.2021.115351.

Gupta, S., Deep, K., Mirjalili, S., 2020. An efficient equilibrium optimizer with mutation strategy for numerical optimization. Appl. Soft Comput. 96 https://doi.org/ 10.1016/j.asoc.2020.106542.

Gurses, D., Bureerat, S., Said, S.M., Yildiz, A.R., 2021. Comparison of the arithmetic optimization algorithm, the slime mold optimization algorithm, the marine predators algorithm, the salp swarm algorithm for real-world engineering applications. Mater. Test. 63, 448-452. https://doi.org/10.1515/mt-2020-0076.
Hassani, H., Silva, E.S., 2015. A Kolmogorov-Smirnov based test for comparing the predictive accuracy of two sets of forecasts. Econometrics 3, 590-609. https://doi .org/10.3390/econometris.0030596.
Houssein, E.H., Rezk, H., Fathy, A., Mahdy, M.A., Nassef, A.M., 2022. A modified adaptive guided differential evolution algorithm applied to engineering applications. Eng. Appl. Artif. Intell. 113, 104920 https://doi.org/10.1016/j .engappai.2022.104920.
Huyob, Y.N., Do, D.T.T., Lee, J., 2021. Q-Learning-based parameter control in differential evolution for structural optimization. Appl. Soft Comput. 107, 107464 https://doi.org/10.1016/j.asoc.2021.107464.
Jiang, Y., Chen, C.H., Zhan, Z.H., Li, Y., Zhang, J., 2022. Adversarial differential evolution for multimodal optimization problems. 2022 IEEE Congr. Evol. Comput. CEC 2022-Conf. Proc. 52, 6059-6070. https://doi.org/10.1109/ CEC50685.2022.9870298.
Karaduman, A., Yildiz, B.S., Yildiz, A.R., 2019. Experimental and numerical fatiguebased design optimization of clutchdiaphragm spring in the automotive industry. Int. J. Veh. Des. 80, 330-345. https://doi.org/10.1504/UVD.2019.109875.
Khiche, M., 2020. Greedy opposition-based learning for chimp optimization algorithm. Artif. Intell. Rev. https://doi.org/10.1007/s10462-022-10343-x.
Kumar, A., Wu, G., Ali, M.Z., Mallipeddi, R., Suganthan, P.N., Das, S., 2020. A test-suite of non-convex constrained optimization problems from the real-world and some baseline results. Swarm Evol. Comput. 56 https://doi.org/10.1016/j . swwo.2020.100693.
Lan, G., Tomczak, J.M., Roijers, D.M., Eiben, A.E., 2022. Time efficiency in optimization with a Bayesian evolutionary algorithm. Swarm Evol. Comput. 69, 100970 https:// doi.org/10.1016/j.swwo.2021.100970.
Li, S., Li, W., Tang, J., Wang, F., 2023. A new evolving operator selector by using fitness landscape in differential evolution algorithm. Inf. Sci. 624, 709-731. https://doi . org/10.1016/j.inv. 2022.11.071.
Li, W., Li, S., Chen, Z., Zhong, L., Ouyang, C., 2019. Self-feedback differential evolution adapting to fitness landscape characteristics. Soft Comput. 23, 1151-1163. https:// doi.org/10.1007/s00500-017-2833-y.
Li, Y., Han, T., Tang, S., Huang, C., Zhou, H., Wang, Y., 2023. An improved differential evolution by hybridizing with estimation-of-distribution algorithm. Inf. Sci. 619, 439-456. https://doi.org/10.1016/j.inv. 2022.11.028.
Liang, J.J., Qu, B.Y., Suganthan, P.N., 2014. Problem definitions and evaluation criteria for the CEC 2014 special session and competition on single objective real-paramete numerical optimization. Electronics 1-32.
Liang, Y.S., Ren, Z.G., Yao, X.H., Feng, Z.R., Chen, A., Guo, W.H., 2020. Enhancing Gaussian estimation of distribution algorithm by exploiting evolution direction with archive. IEEE Trans. Cybern. 50, 140-152. https://doi.org/10.1109/ TCTB.2018.2860067.
Liao, Z., Gong, W., Gui, Z., Wang, L., Wang, Y., 2019. Random walk mutation-based DE with EDA for nonlinear equations systems. 2019 IEEE Congr. Evol. Comput. CEC 2019-Proc 3118-3125. https://doi.org/10.1109/CEC.2019.8790111.
Liao, Z., Gu, Q., Li, S., Sun, Y., 2023a. A knowledge transfer-based adaptive differential evolution for solving nonlinear equation systems. Knowl. Base Syst. 261, 110214 https://doi.org/10.1016/j.knows.2022.110214.
Liao, Z., Zhu, F., Mi, X., Sun, Y., 2023b. A neighborhood information-based adaptive differential evolution for solving complex nonlinear equation system model. Expert Syst. Appl. 216, 119455 https://doi.org/10.1016/j.eswa.2022.119455.
Ma, L., Cheng, S., Shi, Y., 2021. Enhancing learning efficiency of brain storm optimization via orthogonal learning design. IEEE Trans. Syst. Man, and Cybern. Syst. 51, 6723-6742. https://doi.org/10.1109/TSMC.2020.2963943.
Mandavi, A., Rahnamayan, S., Deb, K., 2018. Opposition based learning: a literature review. Swarm Evol. Comput. 39, 1-23. https://doi.org/10.1016/ . swwo.2017.09.016.
Martínez-López, Y., Rodríguez-González, A.Y., Madera, J., Bethencourt Mayedo, M., Lozama, F., 2021. Cellular estimation of distribution algorithm designed to solve the energy resource management problem under uncertainty. Eng. Appl. Artif. Intell. 101, 104231 https://doi.org/10.1016/j.engappai.2021.104231.
Mehta, P., Yildiz, B.S., Sait, S.M., Yildiz, A.R., 2022a. Hunger games search algorithm for global optimization of engineering design problems. Mater. Test. 64, 524-532. https://doi.org/10.1515/mt-2022-0013.

Mehta, P., Yildiz, B.S., Sait, S.M., Yildiz, A.R., 2022b. Gradient-based optimizer for economic optimization of engineering problems. Mater. Test. 64, 690-696. https:// doi.org/10.1515/mt-2022-0055.
Moeini, B., Haack, H., Fairley, N., Fernandez, V., Gengenbach, T.R., Easton, C.D., Linford, M.R., 2021. Box plate: a simple graphical tool for visualizing overfitting in peak fitting as demonstrated with X-ray photoelectron spectroscopy data. J. Electron. Spectrosc. Relat. Phenom. 250, 147094 https://doi.org/10.1016/j .ehpex.2021.147094.
Nadimi-Shahraki, M.H., Zamani, H., 2022. DMDE: diversity-maintained multi-trial vector differential evolution algorithm for non-decomposition large-scale global optimization. Expert Syst. Appl. 198, 116895 https://doi.org/10.1016/ . eswa.2022.116895.
Nannen, V., 2007. Efficient relevance estimation and value calibration of evolutionary algorithmParameters. 2007 IEEE Congr. Evol. Comput. CEC 2007-Proc, 9889423. https://doi.org/10.1109/CEC.2007.4424460.
Ren, Z., Liang, Y., Wang, L., Zhang, A., Pang, R., Li, R., 2018. Anisotropic adaptive variance scaling for Gaussian estimation of distribution algorithm. Knowl. Base Syst. 146, 142-151. https://doi.org/10.1016/j.knows.2018.02.001.
Shao, Z., Pi, D., Shao, W., Yuan, F., 2019. An efficient discrete invasive weed optimization for blocking flow-shop scheduling problem. Eng. Appl. Artif. Intell. 78, 124-141. https://doi.org/10.1016/j.engappai.2018.11.005.
Shi, W., Chen, W.N., Kwong, C., Zhang, Jie, Wang, H., Gu, T., Yuan, H., Zhang, J., 2022. A coevolutionary estimation of distribution algorithm for group insurance portfolio. IEEE Trans. Syst. Man, Cybern. Syst. 52, 6714-6728. https://doi.org/10.1109/ TSMC.2021.3096015.
Shirazi, A., Ceberio, J., Lozano, J.A., 2023. TnJet-v: estimation of distribution algorithms with feasibility conserving mechanisms for constrained continuous optimization. IEEE Trans. Evol. Comput. 26, 1144-1156. https://doi.org/10.1109/ TEXC.2022.3153933.
Son, N.N., Van Kien, C., Anh, H.P.H., 2020. Parameters identification of Bouc-Wen hysteresis model for piezoelectric actuators using hybrid adaptive differential evolution and Jaya algorithm. Eng. Appl. Artif. Intell. 87, 103317 https://doi.org/ 10.1016/j.engappai.2019.103317.
Storm, R., 1997. Differential evolution: a simple and efficient heuristic for global optimization over continuous space. J. Global Optics. 11.
Su, Q., Cai, G., Hu, Z., Yang, X., 2022. Test case generation using improved differential evolution algorithms with novel hypercube-based learning strategies. Eng. Appl. Artif. Intell. https://doi.org/10.1016/j.engappai.2022.104840.
Sun, J., Liu, X., Back, T., Xu, Z., 2021. Learning adaptive differential evolution algorithm from optimization experiences by policy gradient. IEEE Trans. Evol. Comput. 25, 666-680. https://doi.org/10.1109/TEVC.2021.3060811.
Tan, Z., Tang, Y., Li, K., Huang, H., Luo, S., 2022. Differential evolution with hybrid parameters and mutation strategies based on reinforcement learning. Swarm Evol. Comput. 75, 101194 https://doi.org/10.1016/j.swwo.2022.101194.
Tanabe, R., Fukunaga, A., 2013. Success-history based parameter adaptation for differential evolution. In: 2013 IEEE Congr. Evol. Comput. CEC 2013 71-78. https:// doi.org/10.1109/CEC.2013.6807559.
Tanabe, R., Fukunaga, A.S., 2014. Improving the search performance of SHADE using linear population size reduction. https://doi.org/10.1109/CEC.2014.6900380.
Tian, Y., Feng, Y., Wang, C., Cao, B., Zhang, X., Pei, X., Tan, K.C., Jin, Y., 2022. A largescale combinatorial many-objective evolutionary algorithm for intensity-modulated radiotherapy planning. IEEE Trans. Evol. Comput. 26, 1511-1525. https://doi.org/ 10.1109/TEVC.2022.3144675.

Tong, X., Yuan, R., Li, B., 2019. Model complex control CMA-ES. Swarm Evol. Comput. 50, 100558 https://doi.org/10.1016/j.swwo.2019.100558.
Wang, B.C., Feng, Y., Meng, X.B., Wang, S., 2022. A two-phase differential evolution for minimax optimization. Appl. Soft Comput. 131, 109797 https://doi.org/10.1016/ j . user.2022.109797.
Wang, W., Li, K., Jalil, H., Wang, H., 2022. An improved estimation of distribution algorithm for multi-objective optimization problems with mixed-variable. Neural Comput. Appl. 34, 19703-19721. https://doi.org/10.1007/s00521-022-07695-3.
Wei, R., Xia, X., Yu, F., Zhang, Y., Xu, X., Wu, H., Gui, L., He, G., 2020. Multiple adaptive strategies based particle swarm optimization algorithm. Swarm Evol. Comput. 57, 100731 https://doi.org/10.1016/j.swwo.2020.100731.
Wu, G., Mallipeddi, R., Suganthan, P.N., Wang, R., Chen, H., 2016. Differential evolution with multi-population based ensemble of mutation strategies. Inf. Sci. 329, 329-345. https://doi.org/10.1016/j.inv.2015.09.009.
Xie, Y., Sheng, Y., Qiu, M., Gui, F., 2022. An adaptive devading biased random key genetic algorithm for cloud workflow scheduling. Eng. Appl. Artif. Intell. 112, 104879 https://doi.org/10.1016/j.engappai.2022.104879.
Xiong, S., Gong, W., Wang, K., 2023. An adaptive neighborhood-based herniation differential evolution for multimodal optimization. Expert Syst. Appl. 211, 118571 https://doi.org/10.1016/j.eswa.2022.118571.
Yan, B., Zhao, Q., Li, M., Zhang, J., Zhang, J.A., Yao, X., 2022. Fitness landscape analysis and niching genetic approach for hybrid beamforming in RIS-sided communications. Appl. Soft Comput. 131, 109725 https://doi.org/10.1016/j.asec.2022.109725.
Yildiz, B.S., 2020a. Slime mould algorithm and kriging surrogate model-based approach for enhanced crashworthiness of electric vehicles. Int. J. Veh. Des. 83, 54-68. https://doi.org/10.1504/UVD.2020.114786.
Yildiz, B.S., 2020b. Robust design of electric vehicle components using a new hybrid salp swarm algorithm and radial basis function-based approach. Int. J. Veh. Des. 83, 38-53. https://doi.org/10.1504/UVD.2020.114779.

Yildiz, B.S., Kumar, S., Panagant, N., Mehta, P., Sait, S.M., Yildiz, A.R., Pholdee, N., Bureerat, S., Mirjalili, S., 2023. A novel hybrid arithmetic optimization algorithm for solving constrained optimization problems. Knowledge-based Syst 271. https://doi. org/10.1016/j.knosys.2023.110554.
Yildiz, B.S., Kumar, S., Pholdee, N., Bureerat, S., Sait, S.M., Yildiz, A.R., 2022a. A new chaotic Levy flight distribution optimization algorithm for solving constrained engineering problems. Expert Syst. https://doi.org/10.1111/exsy. 12992.
Yildiz, B.S., Patel, V., Pholdee, N., Sait, S.M., Bureerat, S., Yildiz, A.R., 2021a. Conceptual comparison of the ecoprography-based algorithm, equilibrium algorithm, marine predators algorithm and slime mold algorithm for optimal product design. Mater. Test. 63, 336-340. https://doi.org/10.1515/mt-2020-0049.
Yildiz, B.S., Pholdee, N., Bureerat, S., Erdas, M.U., Yildiz, A.R., Sait, S.M., 2021b. Comparison of the political optimization algorithm, the Archimedes optimization algorithm and the Levy flight algorithm for design optimization in industry. Mater. Test. 63, 356-359. https://doi.org/10.1515/mt-2020-0053.
Yildiz, B.S., Pholdee, N., Bureerat, S., Yildiz, A.R., Sait, S.M., 2022b. Enhanced grasshopper optimization algorithm using elite opposition-based learning for solving real-world engineering problems. Eng. Comput. 38, 4207-4219. https://doi.org/ 10.1007/s00366-021-01368-w.

Yildiz, B.S., Pholdee, N., Bureerat, S., Yildiz, A.R., Sait, S.M., 2021. Robust design of a robot gripper mechanism using new hybrid grasshopper optimization algorithm. Expert Syst. 38, e12666.
Yildiz, B.S., Pholdee, N., Panagant, N., Bureerat, S., Yildiz, A.R., Sait, S.M., 2022c. A novel chaotic Henry gas solubility optimization algorithm for solving real-world engineering problems. Eng. Comput. 38, 871-883. https://doi.org/10.1007/s00366-020-01268-5.
Yu, X., Luo, W., Xu, W.Y., Li, C.L., 2022. Constrained multi-objective differential evolution algorithm with ranking mutation operator. Expert Syst. Appl. 208, 118055 https://doi.org/10.1016/j.eswa.2022.118055.
Yue, C., Suganthan, P.N., Liang, J., Qu, R., Yu, K., Zhu, Y., Yan, L., 2021. Differential evolution using improved crowding distance for multimodal multiobjective optimization. Swarm Evol. Comput. 62, 100849 https://doi.org/10.1016/j. ewrew. 2021.100849.
Zamani, H., Nadimi-Shahraki, M.H., Gandonni, A.H., 2021. QANA: quantum-based avian navigation optimizer algorithm. Eng. Appl. Artif. Intell. 104, 104314 https://doi. org/10.1016/j.engappai.2021.104314.

Zeng, L., Ge, Z., 2020. Improved population-based incremental learning of Bayesian networks with partly known structure and parallel computing. Eng. Appl. Artif. Intell. 95, 103920 https://doi.org/10.1016/j.engappai.2020.103920.
Zeng, Z., Hong, Z., Zhang, H., Zhang, M., Chen, C., 2022. Improving differential evolution using a best discarded vector selection strategy. Inf. Sci. 609, 353-375. https://doi.org/10.1016/j.isx.2022.07.075.
Zhang, J., Sanderson, A.C., 2009. JADE: adaptive differential evolution with optional external archive. IEEE Trans. Evol. Comput. 13, 945-958. https://doi.org/10.1109/ TEVC.2009.2014613.
Zhao, F., Zhang, H., Wang, L., Ma, R., Xu, T., Zhu, N., Jonrinaldi, 2022a. A surrogateassisted Jaya algorithm based on optimal directional guidance and historical learning mechanism. Eng. Appl. Artif. Intell. 111, 104775. https://doi-arg-s.hst.yitl ink.com/443/10.1016/j.engappai.2022.104775.
Zhao, F., Zhu, R., Wang, L., Xu, T., Zhu, N., Jonrinaldi, J., 2022b. An offline learning coevolutionary algorithm with problem-specific knowledge. Swarm Evol. Comput. 75, 101148 https://doi.org/10.1016/j.swevo.2022.101148.
Zhao, F.Q., He, X., Wang, L., 2021. A two-stage cooperative evolutionary algorithm with problem-specific knowledge for energy-efficient scheduling of no-wait flow-shop problem. IEEE Trans. Cybern. 51, 5291-5303. https://doi.org/10.1109/ TCYR-2020-3025662.
Zhao, F.Q., Bao, H., Wang, L., He, X., Jonrinaldi, 2022c. A hybrid cooperative differential evolution assisted by CMA-ES with local search mechanism. Neural Comput. Appl. 34, 7173-7197. https://doi.org/10.1007/s00521-021-06849-z.
Zhao, F.Q., Hu, X., Wang, L., Zhao, J., Tang, J., Jonrinaldi, 2022d. A reinforcement learning brain storm optimization algorithm (BSO) with learning mechanism. Knowl. Base Syst. 235, 107645 https://doi.org/10.1016/j.knosys.2021.107645.
Zhou, B.H., Tan, F., 2020. A self-adaptive estimation of distribution algorithm with differential evolution strategy for supermarket location problem. Neural Comput. Appl. 32, 5791-5804. https://doi.org/10.1007/s00521-019-04052-9.
Zhou, T., Hu, Z., Su, Q., Xiong, W., 2023. A clustering differential evolution algorithm with neighborhood-based dual mutation operator for multimodal multiobjective optimization. Expert Syst. Appl. 216, 119438 https://doi.org/10.1016/j. eswa.2022.119438.