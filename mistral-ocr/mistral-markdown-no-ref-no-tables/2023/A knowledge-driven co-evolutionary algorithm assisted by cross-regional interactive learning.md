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

Table 3
The results of KCACIL and 12 comparison algorithms (30D) for the CEC 2017 test suite.

Table 4
The results of KCACIL and 12 comparison algorithms (50D) for the CEC 2017 test suite.
Table 5
The results of KCACIL and 12 comparison algorithms (100D) for the CEC 2017 test suite.

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

quartile, and maximum (Moeini et al., 2021). The 51 experimental results of the selected functions in four dimensions for each algorithm are employed as drawing data, and the discrete degree and deviation of the data are reflected by the length of the box, the shape of the upper and lower spacing, and the length of the line at both ends (Corner, 2013). The box plots of Figs. 7-10 display the stability of the algorithms. The experimental results of $f_{3}, f_{7}, f_{17}$, and $f_{29}$ in four dimensions illustrate that

Table 7
Friedman test results of KCACIL and the comparison algorithms for CEC 2017 test suite.

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

Table 12
The results of KCACIL and the comparison algorithms (30D) for the CEC 2014 test suite.

Table 13
The results of KCACIL and the comparison algorithms (50D) for the CEC 2014 test suite.

Table 14
The results of KCACIL and the comparison algorithms (100D) for the CEC 2014 test suite.

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
algorithms on $f_{5}, f_{8}, f_{14}, f_{15}$, and $f_{16}$ at 10D, 30D and 50D, and also on $f_{5}$, $f_{7}, f_{9}, f_{14}$, and $f_{15}$ at 100D. It indicates that KCACIL has strong exploration to escape from the local minimum. KCACIL achieves the best results on $f_{20}$ at 10D, on $f_{19}$ and $f_{22}$ at 30D, and is also superior to the comparison algorithms on $f_{17}, f_{19}, f_{20}$, and $f_{21}$ at both 50D and 100D. For the composition functions $f_{23}-f_{30}$, the solutions obtained by KCACIL are
preferable. KCACIL shows outstanding superiority on $f_{24}, f_{25}$, and $f_{26}$ at four dimensions.

The stability and convergence are analyzed on $f_{2}, f_{15}, f_{19}$, and $f_{26}$ at the four dimensions. In Fig. 24, the stability of the algorithms is shown through the box plots. The experimental results show that KCACIL is robust. The convergence curves of the algorithms are listed in Fig. 25 where the horizontal axis represents the evaluated number, and the vertical axis represents the logarithm of the error value. KCACIL has a remarkable advantage in terms of high precision and fast convergence at four dimensions.

All the results indicate that the KCACIL shows a significant superiority over the CEC 2014 test suite.

### 4.2.3. Results of the non-parameter tests

Friedman test, post-hoc test, and Kolmogorov-Smirnov prediction accuracy test (KSPA) are adopted in this subsection. Friedman test compares the significant differences between multiple samples by rank at four dimensions in Table 15. The results at 50D are shown in Fig. 27 where the horizontal axis represents the selected algorithms, and the vertical axis represents the average ranking. KCACIL ranks optimally for the critical difference of the confidence intervals of $90 \%$ and $95 \%$.

Post-hoc test is implemented to determine the location of the differences between the algorithms. KCACIL is selected as the control algorithm. The $p$-value is from the Friedman test, and the computation methods of adjusted $p$-value are introduced, including the methods of Bonferroni-Dunn, Holm, Hochberg, Hommel, Holland, and Rom. The

Table 16
Results of post-hoc test using KCACIL as control algorithm ( $\mathrm{D}=50$ ).
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
![img-43.jpeg](img-43.jpeg)

Fig. 28. Stability of KCACIL and the comparison algorithms in DED.
sharing and transfer. Furthermore, search efficiency and convergence accuracy are facilitated.

The inferior solutions with small $Q$ feedback of reinforcement learning and dense aggregation are improved by the revised strategy of the inferior solutions to ameliorate premature convergence. The collaboration of the strategies promotes the rapid population evolution toward the optimal direction and improves the accuracy of the solutions. The individual regeneration mechanism activates the population and effectively avoids evolutionary stagnation. The adaptive strategies of multiple parameters dynamically adjust KCACIL to the appropriate state in different stages. The robustness is improved.

## 5. KCACIL for engineering applications problems

### 5.1. KCACIL for the dynamic economic dispatch problem

The dynamic economic dispatch (DED) problem (Das and Suganthan, 2011) belongs to the hourly scheduling problem. Power demand changes with hours, and a clear 24-h power generation plan is to be
developed. The objective and constraints of DED are shown in Eqs. (56)(63).

First, the definition of the symbol used in this engineering application problem is given.


# Minimize 

Table 18
Results of problems RC01-RC08.

Table 19
Results of problems RC09-RC16.

Table 20
Results of problems RC17-RC25.

Table 21
Results of problems RC26-RC33.

Table 22
Results of problems RC34-RC41.

Table 23
Results of problems RC42-RC49.

Table 24
Results of problems RC50-RC57.

Table 25
Performance measure of all algorithms.
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
