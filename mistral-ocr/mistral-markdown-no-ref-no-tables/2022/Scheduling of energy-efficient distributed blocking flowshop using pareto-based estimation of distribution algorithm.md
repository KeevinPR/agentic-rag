# Scheduling of energy-efficient distributed blocking flowshop using pareto-based estimation of distribution algorithm 

Xiaohui Zhang ${ }^{\mathrm{a}}$, Xinhua Liu ${ }^{\mathrm{b}, \mathrm{c}}$, Andrzej Cichon ${ }^{\mathrm{d}}$, Grzegorz Królczyk ${ }^{\mathrm{e}}$, Zhixiong Li ${ }^{\mathrm{e}, f, \mathrm{c}}$<br>${ }^{a}$ School of Electrical and Control Engineering, Xuzhou University of Technology, Xuzhou 221018, China<br>${ }^{\text {b }}$ School of Mechanical and Electrical Engineering, China University of Mining \& Technology, Xuzhou 211006, China<br>${ }^{c}$ Technology and Innovation Research Center of JiangYan EDZ, Taizhou 225500, China<br>${ }^{d}$ Department of Electrical, Control and Computer Engineering, Opole University of Technology, Opole 45758, Poland<br>${ }^{e}$ Department of Manufacturing Engineering and Automation Products, Opole University of Technology, Opole 45758, Poland<br>${ }^{f}$ Yonsei Frontier Lab, Yonsei University, Seoul 03722, Republic of Korea

## A R T I C L E I N F O

Keywords:
Estimation of distribution algorithm
Blocking constraint
Multi-objective optimization
Energy efficiency

## A B S T R A C T

This study investigates the impact of production scheduling decisions aims at improving productive and energyefficient performances simultaneously in distributed blocking flowshops (EDBFSP). To reach a compromise between the conflicting objectives, a Pareto multi-objective optimization model based on the estimation of distribution algorithm (MOEDA) is proposed. Firstly, an initialization method based on the problem-specific characteristics is designed to create a promising population with quality and diversity; secondly, a probabilistic model based on a Bayesian network is constructed to predict position relationships between jobs. Two neighborhood operators with modified insertion technique are proposed to realize the adjustments of both job sequence and processing speed; thirdly, two operators are developed to execute multi-objective local searches on the elite solutions. Aiming at efficient utilization of the resulted blocking and idle time, an energy-saving method is designed for EDBFSP. In the experimental parts, to gain the best performance, the key parameters of MOEDA have been calibrated. The validation is conducted to assess the performances of the designed initialization method, neighborhood search, local search, and energy-saving strategies. The proposed MOEDA is also compared with mainstream metaheuristics for solving green scheduling problems. The experiment results show that the optimization and search ability of MOEDA have gained prominent advantages over other metaheuristics in both precision and distributivity.

## 1. Introduction

With the development of 'Kanban' and 'just-in-time' (JIT) concepts, manufacturing with zero or finite intermediate buffer has gained sustained attention. Such patterns are often mapped as the blocking flowshop manufacturing in academic researches, which has been extensively investigated over the past years. In a classical blocking flowshop, it is generally held that no buffers exist between two adjacent machines. The job that already finished one certain operation should be immediately transferred to the next operation/process unit for machining. If the next machine is tied up, this job has to be blocked on the previous machine and can be released until the next machine is available. The optimization of the scheduling problems in a blocking flowshop (BFSP) with makespan criterion is to eliminate or at least minimize the existed blocking
intervals between operations. Heretofore, BFSP has been arisen in many industrial fields (Shao et al., 2018), such as the iron and steel industry, chemicals and pharmaceuticals, aeronautics parts fabrication, etc.

On the other hand, with the promotion of economic globalization and increased mergers between enterprises, the emergence of large-scale or concurrent production brings the pattern of distributed manufacturing essential. Distributed manufacturing decentralizes tasks into factories or workshops from different geographical locations. This pattern can help the manufacturers raise productivity, reduce cost, control risks, and adjust marketing policies more flexibly. Herein, we extend the aforementioned BFSP in a distributed environment as a distributed BFSP (DBFSP), which is demonstrated in Fig. 1. DBFSP considers $f$ blocking factories, of which the machine configurations are the same. The jobs can be assigned to any factories and the processing of

[^0]
[^0]:    ${ }^{a}$ Corresponding author.
    E-mail address: zhixiong.li@yonsie.ac.kr (Z. Li).

each job follows the manufacturing procedure of a single blocking flowshop. To solve DBFSP, two decisions need to be made: the allocation of jobs to different factories, and the sequencing of jobs in the respective factory. Apparently, both decisions are highly associated with each other and could not be addressed without considering their serial characteristics.

Practical DBFSP often reveals that a single optimization goal is insufficient to figure a realistic scenario since the manufacturing system usually contains multiple conflicting objectives (Feng et al., 2020). The conflicting objectives concerned usually include the maximum completion time (makespan), total tardiness (TT), total flow time (TFT), energy consumption, carbon footprint, and so on. When optimizing multiple conflicting objectives, the improvement of one single objective may lead to the performance degradation of another or several other objectives. For instance, minimizing the makespan may require raising the processing speeds of jobs, but higher processing speed could form a stark contrast to the equilibrium of energy consumption or carbon emission, which may cause the over-run of energy or pollution costs. Hence, effective metaheuristics are needed to find desirable results in solution space and provide promising trade-offs for decision-makers.

Bearing the above observations, we have summarized the following motivations for this study:

Though different types of distributed flowshop scheduling problems have been studied, more practical objectives are still advised to consider. Recently, increasing environmental protection consciousness has resulted in the necessity of energy conservation measures in industrial fields. Making desirable decisions on schedules will be a green and effective way to improve energy efficiency. Therefore, the research on energy-conscious multi-objective DBFSP is of great
significance to promote energy conservation for distributed manufacturing.
Due to the problem-specific characteristics of distributed flowshop with multiple optimization objectives, it is hard to work out schemes that can obtain global optimal values for each objective simultaneously. An effective and efficient algorithm is required to optimize the solutions deeply, as well as obtain the diversity to cover the partially quite distinctive features of other objectives.

Estimation of distribution algorithm (EDA) (Mühlenbein \& Paass, 1996), as a kind of evolutionary optimization algorithm, is intended to avoid the damage of building blocks caused by crossover and mutation operation of genetic algorithm (GA). EDA describes the distribution of candidate solutions in their objective space through a probability model, which is constructed by the statistical method from a macro point of view. Then, EDA predicts better search space and generates new individuals by sampling the probabilistic model established from incumbent individuals. Compared to traditional GA, the main advantages of EDA are concluded as follows: (1) EDA uses joint probability distribution to express the linkage relationship between genes, which avoids the damage of building blocks caused by the crossover and mutation operation of GA; (2) EDA reduces the blindness and randomness of operator selection and parameter settings of GA, and also reduces the requirement of prior knowledge for the problem; (3) EDA employs the probability model to express the joint probability distribution among gene variables, and uses statistics to learn the parameters of the probability model, which has a higher theoretical basis and evolution orientation.

In this study, we propose a Pareto multi-objective estimation of distribution algorithm (MOEDA) to solve the energy-aware distributed blocking flowshop scheduling problem (EDBFSP). EDBFSP widely exists
![img-0.jpeg](img-0.jpeg)

Fig. 1. An example of DBFSP with a Gantt chart.

in many industrial fields, especially the group such as pharmaceuticals and semiconductor enterprise, which usually have multiple factories all over the world. Limited to the process technology (i.e. cleanliness and temperature), the buffer zone is not provided between adjacent equipment. On the other hand, these groups should shoulder the social responsibility of energy conservation and emission reduction. Hence, EDBFSP has attracted more and more attention. The objectives of EDBFSP to be optimized are makespan and energy consumption. For each operation of all jobs, a speed scale vector was applied to adjust the processing speed, which is considered as the energy-related decision variable. The contributions to the MOEDA are introduced as follows: (1) A Bayesian network-based probabilistic model was constructed to predict the new individuals; (2) Two neighborhood operators were designed according to problem-specific characteristics of EDBFSP. A modified job insertion technique was proposed to realize the adaptive adjustment of speed level during the insertion procedure. (3) A Pareto multi-objective local search framework was designed to perturb the obtained elite solutions. At last, an energy-saving method based on noncritical operations was developed. We validated the effectiveness of MOEDA by conducting experimental simulations on benchmark instances along with a comparative study using the mainstream algorithms for energy-aware scheduling problems in distributed manufacturing systems.

The rest components of this paper are outlined as follows. Section 2 systematically reviews the relevant literature. Section 3 states the EDBFSP and gives the corresponding mathematical model. The detailed procedure of MOEDA is presented in Section 4. Section 5 demonstrates the numerical experiments and statistical analysis. Conclusions and future works are summarized in Section 6.

## 2. Related work

Recent publications related to this study are divided into three parts: distributed flowshop scheduling problem (DFSP), energy-aware flowshop scheduling problem, and the estimation of distribution algorithm. The relevant literature is summarized in the subsections.

### 2.1. Distributed flowshop scheduling problem (DFSP)

As aforementioned, DFSP is more sophisticated than a single flowshop scheduling problem since the assignment of jobs to factories should be considered in advance. This problem-specific characteristic also requires a reversal-change of optimization techniques such as neighborhood strategies and local search schemes. In 2010, DFSP with makespan criterion was studied by Naderi and Ruiz (2010) for the first time. The authors have analyzed different mathematical models of DFSP and proposed 12 heuristics combining with 2 job-to-factory assignment rules. Following this vein, various approaches were proposed to address DFSP. Recent optimization models are such as iterated greedy (IG) algorithm (Ruiz et al., 2019), benders decomposition algorithm (Hannasdayi, 2020), artificial bee colony (ABC) algorithm (Meng \& Pan, 2021), and iterated local-search (ILS) algorithm (Jing et al., 2021).

As the research further developed, some variants have been studied by extending the permutation constraints of DFSP. For instance, DBFSP was raised by changing the permutation mode to "no buffer between adjacent operations" mode. To optimize the makespan criterion, Zhang et al. (2019) proposed a discrete fruit fly optimization algorithm (DFOA). Later on, Shao et al. (2020a) proposed a hybrid enhanced discrete fruit fly optimization algorithm (HEDFOA). Zhao et al. (2020) developed an ensemble discrete differential evolution (EDE) algorithm. Chen et al. (2020) designed an iterated greedy algorithm. Chen et al. (2021) also proposed an enhanced IG algorithm based on their previous work. Besides, Zhang et al. (2019) investigated DFSP with limited buffer constraint (DFSPLB) and proposed a dedicated DDE algorithm. Shao et al. (2020b) studied the distributed assembly blocking flowshop scheduling problem (DABFSP) and have proposed an ILS algorithm with
a multi-type perturbation procedure containing four kinds of perturbed operators based on problem-specific knowledge.

The aforementioned literature, however, focused only on a single objective. Regarding the multi-objective DFSP, the literature is limited due to the complexity of the optimization models. Deng and Wang (2017) developed a competitive memetic algorithm (CMA) for a multiobjective DFSP with the same criteria. Wang and Wang (2018) proposed a knowledge-based cooperative algorithm (KCA) to address energy-efficient scheduling of DFSP with makespan and energy consumption as optimization objectives. Shao et al. (2019) proposed a hybrid EDA to optimize the DNWFSP considering total weighted tardiness (TWT) and makespan as performance criteria.

### 2.2. Energy-Conscious flowshop scheduling problem

Recently, the energy-conscious flowshop scheduling problem has gained extensive attention. A variety of machine-based policies and strategies have been investigated to improve energy efficiency. Mouzon et al. (2007) observed that the non-bottleneck machines would waste a huge amount of energy in idle time. They constructed a manufacturing framework with turn-on and turn-off strategies for non-bottleneck machines to minimize the energy cost and other objectives. Limited by the actual situation on-site, the turn-on and turn-off strategy may not applicable since machine status cannot be frequently switched during the manufacturing process. Wang et al. (2018) found that converting blocking time to idle time could save energy while keeping makespan unvaried. They integrated this strategy into a parallel variable neighborhood search algorithm (PNVS) to optimize the energy consumption and makespan for a BFSP. Similar to Wang et al. (2018), Jiang and Zhang (Jiang \& Zhang, 2019) have investigated the property of nonprocessing energy in a hybrid flow-shop with buffer constraint and developed a multi-objective evolutionary algorithm based on decomposition (MOEA/D). Besides, Fazli and Wang (Fazli Khalaf \& Wang, 2018) proposed a framework that decreased the energy demand through on-site renewables and energy storage strategy, which was proven to be effective to optimize the electricity cost for a two-stage stochastic flowshop. Recently, some researchers considered that machines can consume different energy due to different operation patterns. Thereby, a speed control mechanism for machine operation was proposed (Fang et al., 2011, 2013). When the mechanism requires a machine to processes at a higher speed, the energy consumption grows whereas the processing time reduces. Obviously, the setting of speed level will cause a conflict between the processing time and energy consumption. Based on this framework, some scheduling models have been further proposed and investigated (Lei et al., 2018). For an energy-aware flowshop scheduling problem, Ding et al. (2016) developed an extended NEHInsertion procedure, which was able to realize the synchronous adjustment of processing speed when executing the job insertion procedure for finding a better position in solution space. Jiang and Wang (Jiang \& Wang, 2019) proposed an improved multi-objective evolutionary algorithm (IMOEA) to optimize the flowshop with makespan and energy consumption criteria. Öztop et al. (2020) proposed a multi-objective variable block insertion heuristic to study the trade-off between TFT and energy consumption of a permutation flowshop. Yüksel et al. (2020) proposed a multi-objective discrete artificial bee colony algorithm to minimize total tardiness and energy consumption for a no-wait flowshop scheduling problem (NWPFSP). Besides, Schulz et al. (2019) proposed three energy-saving strategies, which not only consider the varied process speed of the machine but also the varied energy unit price and the peak-valley load as energy-related decision variables. The proposed strategies were integrated to optimize the multi-objective for a hybrid flowshop.

Concerning the energy-aware scheduling problems in a distributed manufacturing environment, the literature is rather limited. Deng and Wang et al. (2016) investigated the DFSP with multi-objective developed a competitive memetic algorithm (CMA) to minimize the

makespan and carbon emission, which is directly derived from energy consumption. Jiang, Wang, and Lu (2017) employed MOEA/D with a critical-path-based energy-saving method. For DFSP with no-wait constraint, Wang et al. (2017) designed a cooperative algorithm (CA) to improve energy consumption and makespan. Fu et al. (2019) have studied DFSP with the stochastic processing time constraint and designed a brainstorm optimization algorithm (MOBO) to evaluate three objectives: total tardiness, makespan, and energy consumption. Zheng et al. (2020) combined EDA with IG to address the multi-objective fuzzy distributed hybrid flow shop scheduling problem, which considers the fuzzy total tardiness and robustness as the objectives.

### 2.3. Engineering application of EDA

EDA (Mühlenbein \& Paass, 1996) is a new kind of intelligent algorithm based on statistical theory. Unlike other typical evolutionary algorithms that evolve through movement-based operation (e.g., crossover and mutation), EDA evolves through the probabilistic model. Since the probability distribution of good solutions can guide the search direction, the randomness of evolution could be effectively avoided. It implies that EDA can learn good information from the incumbent elite individuals. The flow diagram of basic EDA is presented in Fig. 2. Generally, the flow path of basic EDA is described as follows:

Set the parameter, initialize the population, and select elite individuals;
Build a probabilistic model through learning the statistical information of the elite individuals;
Sample the updated probabilistic model, and predict the new individuals.

EDA has been verified with good global search and optimization ability and applied to solve engineering problems such as traveling salesman problem (Song et al., 2017), communication detection problem (Zhou et al., 2018), contract distribution (Hu et al., 2018), etc. For scheduling problems, Tian et al. (Tian et al., 2019) designed a hybrid EDA in dealing with a scheduling problem with resource constraints and time uncertainty. Pérez-Rodríguez and Hernández-Aguirre (2018)
![img-1.jpeg](img-1.jpeg)

Fig. 2. Flow diagram of basic EDA.
embedded mallows distribution into EDA to construct better sequences for the flexible jobshop scheduling problem (FJSP). Zhou et al. (2018) proposed a reentrant hybrid flowshop model where inspection and repair operations are considered. A hybrid differential evolution algorithm with EDA using an ensemble model was proposed to solve the problem. For multi-objective scheduling problems, Wu and Wang (2018) adopted multi-model EDA to determine the task process permutation and voltage supply levels under a cloud computing system. Amiri and Behnamian (2020) applied EDA to solve the flowshop scheduling problem with makespan and energy consumption under uncertainty.

### 2.4. Discussion

From the literature review, it can be concluded that some methodologies were proposed to address the distributed scheduling problems. Nevertheless, the vast majority of them still focused on single-objective optimization. Practical productions, in fact, often need to consider complex environments with multiple conflicting objectives. On the other side, with growing concerns over cost-down and environmental requirements, the energy-saving concept is receiving extensive attention. Therefore, it is strongly necessary to study energy-aware DBFSP from both theoretical and applicable perspectives.

## 3. Problem statement

For a better understanding, the general concept of multi-objective optimization is firstly introduced in this section; then, the mathematical model and properties of EDBFSP are described in the subsections.

### 3.1. Multi-objective optimization problem (MOP)

MOP depicts a procedure that can improve the performance of more than one objective, which aims at offering a set of criteria that enable decision-makers to improve a given activity compared to previous levels continuously. For solving MOP, the decomposition-based approach and the Pareto-dominance-based approach are considered as two popular approaches for approximating optimal solution sets (Wang et al., 2018). The former approach decomposes MOP into a set of sub-problems through linear or non-linear aggregation functions and assesses all sub-problems synchronously while the latter one addresses MOP with more than two objectives according to dominance relation between solutions. Since the Pareto-based approach is with the property of easy implementation and mostly solves problems with no more than three objectives, we adopt it to solve EDBFSP. In general, a MOP for minimization issue can be expressed in the following form (Shao et al., 2019):
$\min f(\mathrm{X})=\left(f_{1}(\mathrm{X}), f_{2}(\mathrm{X}), \ldots, f_{r}(\mathrm{X})\right)$
$\mathrm{X}=\left(x_{1}, x_{2}, \ldots, x_{n}\right) \in R^{n}$
$\mathrm{s} \boldsymbol{\perp}\left\{\begin{array}{l}g_{i}(\mathrm{X}) \geqslant 0 \\ h_{i}(\mathrm{X}) \geqslant 0\end{array} \quad \begin{aligned} & i=1, \ldots, p \\ & j=1, \ldots, s\end{aligned}\right.$
where $f_{r}(\mathrm{X})$ represents the. $r$-th. sub-objective, X indicates the solution set in the decision variable space $R^{n} . p$ and $s$ denote the number of equality and inequality constraints, respectively. To apply the Paretobased approach, the following concepts need to be clarified:

Pareto Dominance: There exist two feasible solutions $\times$ and $\mathbf{y}, \mathbf{x}$ dominates $\mathbf{y}$ (denote as $\mathbf{x}<\mathbf{y}$ ) if and only if the following conditions are satisfied:
$\left\{\begin{array}{l}\forall a \in\{1,2, \ldots, r\}, f_{, x}(\mathbf{x}) \in f_{, x}(\mathbf{y}) \\ \exists b \in\{1,2, \ldots, r\}, f_{, x}(\mathbf{x}) \in f_{, x}(\mathbf{y})\end{array}\right.$

Pareto optimal/non-dominated solution: If the solution $\times$ is not dominated by all other solutions of a certain algorithm, it is defined as a non-dominated solution.
Pareto optimal solution set: The set constructed by all Pareto optimal/non-dominated solutions obtained from a certain algorithm. Pareto front (PF): The PF is formed by the non-dominated solutions in Pareto optimal solution set. When solving practical problems, decision-makers can consider the equilibrium of multiple objectives that need to be optimized and select the final decision solution on the Pareto frontier. Thus, it can be concluded that the essence of Pareto multi-objective optimization is to obtain an optimal solution set whose distribution and convergence are as close as possible to the real PF.

### 3.2. Problem statement of EDBFSP

EDBFSP can be expressed in the following form. Assume a set of jobs $J=\left\{J_{1}, J_{2}, \ldots, J_{n}\right\}$ and a set of identical factories $F=\left\{F_{1}, F_{2}, \ldots, F_{f}\right\}$, each of which furnishes with a set of machines. $M=\left\{M_{1}, M_{2}, \ldots, M_{m}\right\}$. The jobs can be assigned to any of the $f$ factories for processing. Each machine can process at a set of speed scale $V=\left\{V_{1}, V_{2}, \ldots, V_{n m}\right\}$. In general, EDBFSP consists of three sub-problems: the assignment of jobs to factories, the sequencing of jobs in each factory, and the selection of speed scale for each operation. Assume $n_{k}\left(n_{k}<n\right)$ jobs are assigned to the factory $F_{k}$, and the job sequence is denoted $\operatorname{ass} x_{k}$, where $x_{k}(l)$ represents the $l$-th job in $x_{k}$. Then, $O_{x_{k}(l), i}$ denotes the operation of job $x_{k}(l)$ on machine $i$. The processing speed of a certain operation $O_{x_{k}(l), i}$ is represented as $v_{x_{k}(l), i} \in V$. Also, the operation $O_{x_{k}(l), i}$ has a standard processing time $P_{x_{k}(l), i}$. If $O_{x_{k}(l), i}$ is processed at speed $v_{x_{k}(l), i}$, its actual processing time $p_{x_{k}(l), i}$ can be calculated as $p_{x_{k}(l), i}=P_{x_{k}(l), i} / v_{x_{k}(l), i}$. Assume $S_{x_{k}(l), 0}$ denotes the start time of job $x_{k}(l)$ on the first machine in factory $F_{k}$, and $d_{x_{k}(l), i}$ is defined as the departure time of operation $O_{x_{k}(l), i}$. Regarding the energyrelated concept, a machine has 2 operation modes: standby and process. Under standby mode, the energy consumption per unit time is defined asSE, which is defined as a constant; while under process mode, the energy consumption per unit time is $\mathrm{PE}_{x_{k}(l), i, \pi}$. If a job is blocked on a machine, this machine is switched to standby mode. Let $E C$ be the total energy consumption, the mathematical model of EDBFSP can be expressed as follows.

Objectives: $\min \left\{C_{\max }, E C\right\}$
s.t.
$X_{x_{k}(l), i} \in\{0,1\}, l=1,2, \ldots n_{k}, i=1,2, \ldots, m, k=1,2, \ldots, f$
$Y_{x_{k}(l), i, \pi} \in\{0,1\}, l=1,2, \ldots n_{k}, i=1,2, \ldots, m, k=1,2, \ldots, f$
$p_{x_{k}(l), i}=P_{x_{k}(l), i} / \sum_{i=1}^{n_{k}} \sum_{x_{k_{i}(l), i}} V_{x_{k}(l), i} / l=1,2, \ldots n_{k}, i=1,2, \ldots, m, k=1,2, \ldots, f, v=1,2 \ldots, s m$
$D_{x_{k}(0), i} \geqslant 0, i=1,2, \ldots m, k=1,2, \ldots f$
$D_{x_{k}(l), i} \geqslant D_{x_{k}(l-1), i+1}, l=2, \ldots n_{k}, i=1,2,3, \ldots, m-1, k=1,2, \ldots, f$
$D_{x_{k}(l), i} \geqslant D_{x_{k}(l), i-1}+\sum_{j=1}^{n} X_{x_{k}(l), i} \times p_{x_{k}(l), i}, l=2, \ldots n_{k}, i=1,2,3, \ldots, m-1, k=1,2, \ldots, f$
$D_{x_{k}(l), 0} \geqslant D_{x_{k}(l-1), 1}, l=1,2, \ldots n_{k}, k=1,2, \ldots f$
$C_{\max } \geqslant D_{x_{k}(l), m}, l=2, \ldots n_{k}, k=1,2, \ldots, f$
$\sum_{k=1}^{f} \sum_{l=1}^{n} X_{x_{k}(l), j}=1, j=1,2, \ldots, n$
$\sum_{j=1}^{n} X_{x_{k}(l), j} \leqslant 1, j=1,2, \ldots, n, k=1,2, \ldots f$
$Z_{k, i}(t) \in\{0,1\}, i=1,2, \ldots, m, k=1,2, \ldots, f$
In the above equations, Eq. (5) sets up a binary decision variable $X_{x_{k}(l), i}$. When a job appears on the $l$-th position of $x_{k}, X_{x_{k}(l), i}=1$; otherwise, $X_{x_{k}(l), i}=0$. Eq. (6) denotes a binary decision variable. When a job is processed with a speed $v_{x_{k}(l), i} \in V, Y_{x_{k}(l), i, \pi}=1$; otherwise, $Y_{x_{k}(l), i, \pi}=$ 0 . Eq. (7) calculates the actual processing time of a job. Eq. 8 defines the start time constraint of processing. Eq. (9) represents the time relationship of leaving machines between two adjacent jobs in $x_{k}$ in factory $F_{k}$. Eq. (10) defines the departure time relationship between two adjacent processes of jobs $x_{k}(l)$. Eq. (11) gives the relationship between the departure time of each job on the first machine and its precedence job on next machine. Eq. (12) denotes the process finish time of the factory. Eq. (13) ensures that one job can only appear in one position of $x_{k}$. Eq. (14) guarantees that each position in $x_{k}$ can only be assigned with one job. Eq. (15) denotes a binary decision variable $Z_{k, i}(t)$. When a machine in factory $F_{k}$ is processed at time $t, Z_{k, i}(t)=1$; otherwise, $Z_{k, i}(t)=0$.

The calculation of makespan for DBFSP refers to (Shao et al., 2020a; Zhang et al., 2019). As a result, the global makespan for EDBFSP is determined through the comparison between the makespans of all factories:
$C_{\max }(\Pi)=\operatorname{max}_{k=1}^{f}\left(C\left(x_{k}\right)\right)$
The total energy consumption of a schedule can be derived as follows:
$E C=\sum_{k=1}^{f} \int_{0}^{\left(C x_{k}\right)}\left(\sum_{i=1}^{n_{k}} \sum_{i=1}^{n} P E_{x_{k}(l), i, \pi} \cdot Z_{k, i}(t)+\sum_{i=1}^{n_{k}} S E \cdot\left(1-Z_{k, i}(t)\right)\right) d t$
For an EDBFSP with 6 jobs, 2 factories, and 3 machines, a diagrammatical real-time energy consumption curve is sketched in Fig. 3 as an example. In Fig. 3, $C_{1}$ and $C_{2}$ represent the makespan of each factory, respectively. The area occupied by the energy consumption curve signifies the energy consumption of each factory.

### 3.3. Property of EDBFSP

In this section, some problem-specific properties are explored and introduced, which help to obtain more non-dominated solutions during the search procedure.
Property. ((Shao et al., 2019)) Assumes that two schedules $\Pi_{1}$ and $\Pi_{2}$ have the same makespan, i.e., $C_{\max }\left(\Pi_{1}\right)=C_{\max }\left(\Pi_{2}\right)$. The relationship fulfills: $(1) v( \in\{1,2, \ldots m\}, j \in\{1,2, \ldots, n\}, v_{j, 1}\left(\Pi_{1}\right) \leqslant v_{j, 1}\left(\Pi_{2}\right) ;(2) / 3 \in\{1,2$, $\ldots, m\}, j \in\{1,2, \ldots, n\}, v_{j, 1}\left(\Pi_{1}\right)<v_{j, 1}\left(\Pi_{2}\right)$. Then, the dominance relationship of energy consumption can be described as $E\left(\Pi_{1}\right)<E\left(\Pi_{2}\right)$.

## 4. MOEDA for EDBFSP

Although EDA has presented strong global search ability and shown excellent performances in various industrial applications, difficulties yet expose when employing it to address the complex and multidimensional scheduling problems. The reasons could be summarized as follows. Firstly, the random initialization strategy of basic EDA reduces the quality of solutions, which raises difficulties in seeking nondominated solutions. Secondly, a simple probabilistic model could not promote the convergence of the population, especially when dealing with multi-objective problems. Thirdly, it lacks an effective local intensification strategy to implement sophisticated searches nearby the solutions with good quality.

To break through the above shortcomings, we designed MOEDA that

![img-2.jpeg](img-2.jpeg)

Fig. 3. Demonstration of real-time energy consumption in a distributed blocking flowshop.
inherits and extends the searching idea of basic EDA to optimize EDBFSP. The flowchart of the proposed MOEDA is illustrated in Fig. 4. MOEDA contains 4 key components: initialization, neighborhood search, local search, and energy saving. In the neighborhood search phase, a Bayesian network-based probabilistic model was developed to inherit information from the incumbent non-dominant solutions, with the view of exploring better solution spaces. An effective insertion method was proposed to adjust the speed level of each operation during the job sequencing procedure. To enhance the exploitation ability, a Pareto multi-objective local search framework was designed. Finally, a non-critical operation-based energy-saving method was presented. Since MOEDA equilibrates the exploration and exploitation, satisfactory performances were expected to reach when adopting it in addressing EDBFSP.

### 4.1. Encoding and decoding scheme

A complete solution of EDBFSP contains two parts: the job sequence and the speed level matrix for each operation of the jobs. The solution $\Pi$ is encoded as a sequence-speed list: $\Pi=\left\{\boldsymbol{x}, \boldsymbol{V}\right\}$. In $\Pi, \boldsymbol{x}=\left\{x_{1}, x_{2}, \ldots, x_{f}\right\}$ denotes the job sequence which is composed of all partial sequences $x_{k}$ for each factory. This presentation can be easily decoded since $x_{k}$ decides not only the jobs assigned to factory $F_{k}$, but also the operation sequence of the jobs in this factory. On the other side, $\boldsymbol{V}$ is a $n \times m$ matrix that gives the speed levels for each operation of all jobs. For a better understanding, an example of the encoding and decoding scheme is given in Example 1.

Example 1. A feasible solution $\Pi$ of EDBFSP with job number $n=6$, machine numberm $=3$, and factory number $f=2$ is assumed. The job sequence part $\left(\mathrm{s} \boldsymbol{x}=\left\{x_{1}, x_{2}\right\}\right.$, in which $x_{1}=\left\{J_{1}, J_{2}, J_{5}\right\}$ and $x_{2}=\left\{J_{4}, J_{1}\right.$, $\left.J_{6}\right\}$. When decoding $\Pi$, job $J_{1}, J_{2}$, and $J_{5}$ are allocated to factory $F_{1}$ and are processed in the order $\alpha U_{1} \rightarrow J_{2} \rightarrow J_{5}$. Similarly, the decoding result of $x_{2}$ for another factory $F_{2}$ is $J_{4} \rightarrow J_{3} \rightarrow J_{6}$. The speed matrix for each operation is shown as Eq. (18), where the row number and column number represent the machine number of each factory and the total number of jobs, respectively.
$\boldsymbol{V}=\left[\begin{array}{llllll}1 & 2 & 1 & 1 & 3 & 3 \\ 2 & 1 & 3 & 1 & 1 & 1 \\ 2 & 3 & 2 & 3 & 2 & 3\end{array}\right]^{\mathrm{T}}$

### 4.2. Initialization of population

Good seeds can lead to a rapid convergence of the algorithm when a candidate makes one of the objectives minimal in an initial population for solving MOP (Gong et al., 2018). In this study, MOEDA aims to start from solutions with good makespan, and then stepwise guide the search to the energy-related objective. The graphical evolution procedure of the initial solution is demonstrated in Fig. 5.

Since $\boldsymbol{x}$ and $\boldsymbol{V}$ in a feasible solution $\Pi=\{\boldsymbol{x}, \boldsymbol{V}\}$ have different dimensions, they can only be initialized separately. In this study, $\boldsymbol{V}$ is randomly initialized, with the view of keeping the diversity and distributivity. To obtain $\boldsymbol{x}$ with good makespan, we have modified the ECF (earliest completion factory) initialization rule (Naderi \& Ruiz, 2010). ECF firstly extended the insertion idea of the NEH heuristic (Nawaz et al., 1983) into the distributed flowshop scheduling. The ECF heuristic can be presented in following three steps:

Step 1: Calculating the total processing time $T_{j}=\sum_{i=1}^{m} P_{j i}$ of each job, arrange all jobs in descending order according to $T_{j}$.
Step 2: Orderly assign each job to the factory which can finish processing of this job at the earliest time, namely, the minimum $C_{\max }$ that considers this job as the last one.
Step 3: Repeat Step 1 and Step 2, until all jobs are assigned.
ECF was originally developed for traditional DFSP with permutation constraints. It considers that a job with a greater $T_{j}$ ought to be allocated preferentially than those with smaller $T_{j}$. Nevertheless, for blocking constraint, allocating a job with higher $T_{j}$ in the forepart of a schedule could result in a greater block for the subsequent jobs. Consequently, the greater block generates a larger makespan. Thus, the original ECF is not suitable for DBFSP. Pan et al. (2011) investigated such characteristics and proposed NEH-P concept that arranges jobs with shorter $T_{j}$ preferentially. NEH-P concept has been verified to be more efficient and suitable than the NEH method for blocking mode through extensive experiments (Miyata \& Nagano, 2019). In this study, we employ the concept of NEH-P and modify the first step of ECF to arrange all jobs in ascending order according to $T_{j}$. The rest steps of ECF remain. We define the initialization heuristic is defined as ECFPV (earliest completion factory NEH-P with velocity variable), which is sketched in Pseudocode

![img-3.jpeg](img-3.jpeg)

Fig. 4. Flowchart of the proposed MOEDA.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Evolutionary stages of initial solutions of MOEDA.

1. 

## Pseudocode 1 ECFPV Initialization

Input: population size $P n$, factory number $f$, job number $n$, temporary archive TA Output: population POP, TA
01: For $i=1$ to $P i$
02: Randomly generate the speed level matrix $V_{i}$
03: Calculate the total processing time $T_{j}$ according to $V_{i}$ and standard processing time
04: Sort the jobs in ascending order according to the value of $T_{j}$
05: Generate $\boldsymbol{x}_{i}$ using Step 2 of ECF heuristic
06: let $\Pi_{i}=\left(\boldsymbol{x}_{i}, V_{i}\right)$
07: End For
08: Evaluate the population POP, obtain the non-dominated solutions
09: Store the found non-dominated solutions in TA

After initialization, the Pareto dominance relationship introduced in Section 3.1 is applied to select the non-dominated individuals. It is worth mentioning that a temporary archive TA is set to store the obtained non-dominated solutions in each generation. A Pareto archive PA

is established to record the non-dominated solutions found along with the whole evolution. The solutions in TA need to be compared to those in PA from each generation, and PA is stepwise updated to approximate the Pareto front (PF).

### 4.3. Neighborhood search

After initialization, a neighborhood search framework is designed to help MOEDA search in a promising solution space. On one hand, a probabilistic model based on the Bayesian network is employed to predict the job sequence $\boldsymbol{\alpha}$. On the other hand, the speed matrix $V$ is updated based on specifically designed speed adjustment operators.

### 4.3.1. Bayesian network-based probabilistic model

Since EDBFSP is a discrete multi-variable problem, it is necessary to figure out the dependence between different variables. Bayesian network (Qian et al., 2017) is a typical probabilistic model that represents the relationship between multiple random variables, it is a more ideal choice to employ the Bayesian network to construct the probabilistic model for MOEDA. The prototype diagram of the Bayesian network is shown in Fig. 6. In a Bayesian network, each node represents a probabilistic variable, and the directed arc between two nodes represents their dependent relationship. In Fig. 6, if the parent nodes of the child node $X_{3}$ are $X_{1}$ and $X_{2}$, the conditional occurrence probability of variable $X_{3}$ can be expressed as:
$P\left(X_{3}=x_{3} \mid X_{1}=x_{1} ; X_{2}=x_{2} ; \ldots ; X_{7}=x_{7}\right)=P\left(X_{3}=x_{3} \mid X_{1}=x_{1}, X_{2}=x_{2}\right)$
In general, there are two methods to count the nodes in Bayesian networks (Yanai \& Ihn, 2013). One is to average the occurrence number of the same node, and the other is to calculate the weight value for the product of the occurrence number and its fitness value. In this study, we employed the first method: assume the sampling size is $N s$, the probability variable is defined as $P\left(X_{i}\right)$. The set of nodes on which $X_{i}$ is associated is denoted as $C_{i}$. The probability of the corresponding variable in $C_{i}$ of solution $s$ can be obtained as follows:
$P\left(X_{i}=x \mid C_{i}=c\right)=\frac{\sum_{i=1}^{N_{s}} \delta\left(x, X_{i}=x \mid C_{i}=c\right)}{N s}$
where $\delta$ is a binary decision variable:
$\delta\left(x, X_{i}=x \mid C_{i}=c\right)=\left\{\begin{array}{cc}1 & \text { if there exists } X_{i}=x \text { and } C_{i}=c \\ 0 & \text { else }\end{array}\right.$
Bayesian network only selects high-quality solutions from the current population to build a probabilistic model. The purpose is to
![img-5.jpeg](img-5.jpeg)

Fig. 6. Example of Bayesian network.
complete the inheritance and learning of high-quality information. The probability model needs to be updated and sampled to produce new individuals. The update mechanisms used in this study is the well-known machine learning concept-Heb rule (Shao et al., 2019):
$I^{j}=\left(1-\alpha_{n}\right) P\left(X_{i}=x \mid C_{i}=c\right)+\alpha_{n} P_{\text {default }}\left(X_{i}=x \mid C_{i}=c\right)$
In Eq. (22), $\alpha_{n} \in(0,1)$ represents the update rate or learning rate of the probabilistic model. The update mechanism based on Heb rule can overlook the quantitative changes in the probability distribution and keep the probabilities of nodes positive, to avoid the appearance of illegal solutions. In Eq. (22), the occurrence probability of nodes $P_{\text {default }}$ can be initialized normally:
$P_{\text {default }}=\frac{1}{\text { number of nodes }}$
In job sequence $\alpha$ for EDBFSP, $P_{\text {default }}\left(X_{i}=\boldsymbol{x} \mid C_{i}=\boldsymbol{c}\right)$ denotes the probability that a job has appeared at one node (position). From Eq. (20) to (23), it can be concluded that the update procedure of the probabilistic model is essentially a process of reinforcement learning. After iterative updating, Bayesian network will fully learn the information of high-quality solutions. The distribution status of solutions will be described more accurately, which is helpful for the convergence of the algorithm.

For a better understanding, Fig. 7 presents a Bayesian network with 3 jobs and 10 non-dominant solutions. Each node $N_{i j}$ represents that job $j$ appears at the $i$-th position of the sequence $\alpha$. The nodes in each row of the network represent the jobs that appear in one position of $\alpha$, while the nodes in each column represent all positions of $\alpha$ that one certain job appears. The occurrence numbers of job combinations in all nondominant solutions are expressed by the number of probabilities between two nodes connected by directed arcs. Therefore, the sum of all probability degrees is the number of non-dominant solutions. The nodes surrounded by dashed lines represent nonexistent nodes. In Fig. 7, $N_{2,3}$ denotes the situation that job 3 never appears at the second position in $\alpha$ of the 10 selected non-dominant solutions.

In the view of EDBFSP, we use a two-dimensional matrix $M_{,} j s(g)$ to represent the probabilistic model between genes and the evolutionary direction of the population:
$M_{,} j s(g)=\left(\begin{array}{ccc}l_{1,1}(g) & \ldots & l_{n, 1}(g) \\ \vdots & \ddots & \vdots \\ l_{1, n}(g) & \ldots & l_{n, n}(g)\end{array}\right)$
In Eq. (24), $l_{i j}(g)$ denotes the probability that job $j(j=1,2,3 \ldots, n)$ appears at the $l$-th position of $\alpha$, which can be calculated with Eq. (20). When initializing $M_{,} j s(g)$, to ensure the uniform sampling space in the initial stage of the algorithm, MOEDA sets the initial distribution of the probabilistic model to uniform distribution according to Eq. (23), i. e, $l_{i j}(g)=1 / n$, where $n$ is the total number of jobs.

After initializing the probabilistic model, MOEDA employs the Heb's rule with the learning rate $\alpha_{n}$ to select high-quality individuals and then updates the probabilistic model. Then, the tournament selection strategy (Miller \& Goldberg, 1995) is adopted to sample the new model, and further generate new individuals. The deatiled procedure is as follows. Firstly, Bayesian network updates all normalized probability values for the $l-th$ position in the probabilistic model (normally start from the first position). Then, adopt the tournament selection strategy to select the job with good probability values for the $l$-th position. Later on, the same sampling procedure is executed to selected the job at the $l+1$-th position based on the job at $l$-th position. The above steps repeat until the job at the last position of $\alpha$ is selected. Then, Bayesian network completes the generation of one new individual.

Since $\alpha$ and $V$ are separately encoded due to different dimensions, it is impossible to build a Bayesian network-based probabilistic model to predict $\alpha$ and $V$ at the same time. In this study, we construct a Bayesian network to update $\alpha$. After the new sequence $\alpha$ is generated, the corre-

![img-6.jpeg](img-6.jpeg)

Fig. 7. An exemplary diagram of the Bayesian network for EDBFSP.
sponding speed level matrix $\boldsymbol{V}$ still initialized randomly. Moreover, to ensure the diversity and distribution of the population, $70 \%$ of the offspring are created by sampling the probabilistic model, and the remaining are generated using the proposed initialization strategy proposed in Section 4.2.

### 4.3.2. Update mechanism for process speed

After predicting the new job sequence $x$, the corresponding speed level matrix $\boldsymbol{V}$ is to be adjusted. Based on the properties analyzed in Section 3.3, two speed adjustment operators are designed for MOEDA, to further improve the individual quality of the population.

ED operator: According to Property, randomly select one operation, and reduce its speed level to the allowable minimum. The purpose of designing this operator is to obtain the longest processing time so that the energy consumption of this operation can be reduced without affecting the original makespan.

EC operator: Randomly select one job from the factory with maximum energy consumption, insert it into the factory with minimum energy consumption. The aim of designing EC operator is to adjust both operation speed level and job sequence. Since the EDBFSP model takes discrete speed levels, it is of great significance to determine the minimum speed level that an operation could allow when executing the insertion procedure. Ding et al. (2016) have proposed a job insertion technique (denote as ES), which realized the synchronous optimization of speed and job sequence for permutation flowshop scheduling problems. In this study, we extended ES for EDBFSP. Assume job $q$ will be
inserted in position $h$ of the job sequence, its speed vector (speed levels for all operations) after inserting is defined as $V_{q}^{h}$. The overall insertion procedure is described in Pseudocode 2 and sketched in Fig. 8. In Pseudocode 2, Line 01 calculates the corresponding variables after insertion, where $D_{h, i}$ defines the earliest departure time of job $q$ on machine $i, Q_{h, i}$ is the tail that is the duration between the end of all operations and the latest starting time of job $q$, and $F_{h, i}$ denotes the earliest completion time on machine $i$ after insertion. The detailed deduction procedure refers to speed-up method used for DBFSP (Ying \& Lin, 2017; Zhang et al., 2019). Line 02 calculates the makespan with maximum allowable speed level $V_{q}^{m} . \Delta_{m}$ in Line 03 denotes the maximum processing time increment of job $q$ on the last machine. Line 04 determines the minimum speed level $u$ in relation to $\Delta_{m}$. Since EDBFSP takes discrete speed levels, the real processing time increment on machine $m$ might not be as exact as $\Delta_{m}$. Hence, the start time of job $q$ on machine $m$ can be postponed with maximal $G a p_{m}$ time units as derived in Line 07 through setting $i=m-1$. Then, $\Delta_{m-1}$ for job $q$ on machine $m-1$ is determined. In EDBFSP, $\Delta_{m-1}$ is restricted by two constraints. The first one is that the processing time increment should not result in any postponement (blocking) of job $q$ on its succeeding machine $m$, which is presented in Line 08. The second one is that the processing time increment ought not to affect the start time of its sequential operations on the same machinem -1 , as stated in Line 09. Then, the insertion procedure for job $q$ on the current machine finishes. The insertion procedure continues until the speed levels of job $q$ on all
![img-7.jpeg](img-7.jpeg)

Fig. 8. Illustration of job insertion procedure with speed adjustment.

machines have been identified. After insertion, all the operations are unable to degrade the processing speed levels unless changing the job sequence (makespan) or the processing speeds of other jobs. Hence, it can be concluded that ES is a greedy-based search procedure essentially.

## Pseudocode 2 ES insertion procedure

Input: job $q$ to be inserted, maximum speed vector $V_{q}^{\text {max }}$, makespan $C_{\text {max }}\left(\boldsymbol{x}_{q}^{\mathrm{L}}, V_{q}^{\text {max }}\right)$
Output: speed vector $V_{q}^{\mathrm{L}}$ after adjustment
01: calculates $D_{0, i}, Q_{0, i}$ and $F_{0, i}$
02: determine the $C_{\text {max }}\left(\boldsymbol{x}_{q}^{\mathrm{L}}, V_{q}^{\text {max }}\right) \#$ insert $q$ with $V_{q}^{\text {max }}$
$03: \Delta_{m}=C_{\text {max }}\left(\Pi_{q}^{\mathrm{L}}, V_{q}^{\text {max }}\right)-F_{0, m}-Q_{0, m}$
04: $\Delta_{m}$ determines minimum speed level $v_{\text {min }} \in V$ of job $q$ on the last
machine, $p_{m, q, v_{\min }} \sim p_{m, q, v^{m}, v_{m, q}} \in \Delta_{m}$
05: set $v^{h}(q, m)=v_{\text {min }} \#$ determine the speed level for job $q$ on the last machine
06: For $i=m-1$ to 1
07: $\operatorname{Gap}_{i+1}=\Delta_{i+1} \sim\left(p_{i+1, q, v^{h}(i+1, q)} \sim p_{i+1, q, v^{m}(i+1, q)}\right)$
08: $d i s_{1}=\max \left\{D_{0, i, i+1}-F_{0, i} 0\right\}+G a p_{i+1} \#$ blocking constraint
09: $d i s_{2}=C_{\text {max }}\left(\Pi^{L}, V_{a n}\right)-F_{0, i}-Q_{0, i}$
10: $\Delta_{i}=m \ln \left\{d i s_{1}, d i s_{2}\right\}$
11: $\Delta_{i}$ determines minimum speed level $v_{\text {min }} \in V$ on the other
machines, $p_{m, q, v^{h}(q, i)} \sim p_{m, q, v^{h}(q, i)} \in \Delta_{m}$
12: set $V^{h}(q, i)=v_{\text {min }}$
13: End For

In brief, to ensure the diversity and distribution of solutions, the proposed speed adjustment operators are randomly applied to each individual of the population. The new individual is compared with the incumbent individual, and the non-dominated one will be kept. After neighborhood search, the non-dominated solutions found are recorded in TA. The overall neighborhood search procedure is sketched as Pseudocode 3.

## Pseudocode 3 Neighborhood search

Input: population size $P n$, temporary archive TA, job number $n$, factory number $f$, machine number $m$
Output: TA
01: While termination criterion not satisfies do
02: For $i=1$ to $P n$
03: $\#$ adjust the sequence $\pi$
04: select the non-dominated solutions from TA to construct a probabilistic model
05: update the probabilistic model $M \_j \varepsilon(g)$ by employing the Heb rule
06: generate new sequence $\pi_{i}(i=1 \ldots, 0.7^{*} \mathrm{~Ps})$ through sampling $M \_j \varepsilon(g+1)$
07: generate new sequence $\pi_{i}(i=0.7^{*} P s+1, \ldots, P s)$ through ECFPV heuristic
08: $\#$ adjust the speed level matrix $V$
09: implement the speed adjustment operators (ED or EC) randomly on each individual
10: update $V_{i}$
11: create a new schedule solution $\Pi_{i}=\left(\boldsymbol{x}_{i}, V_{i}\right)$
12: End For
13: Evaluate the offspring based on the Pareto concept, store the non-dominated solutions in TA
14: End While

### 4.4. Pareto multi-objective local search

For an intelligent algorithm, the exploitation and exploration capacity should be well balanced. Although the neighborhood search can explore better solution space, it cannot fully contribute to the convergence of the whole population. In other words, MOEDA still needs a
technique that helps avoid search stagnation and escape from the local optimum. In this study, two local search operators are designed and implemented on a randomly selected non-dominated solution from TA. The local search operators are expected to optimize the job sequence and speed synchronously.

Pareto local search operator 1 (Insertion): This operator refers to the factory with maximum makespan (denote as critical factory $f c$ ). Remove a job in $f c$ and insert it in all possible positions of all other factories. When the makespan can not be improved anymore, the insertion step restarts by choosing another job in $f c$.

Pareto local search operator 2 (Swap): Each job in $f c$ is removed sequentially and swapped with all jobs of all the other factories. The swap procedure terminates until all jobs in $f c$ have been visited.

To implement the above-designed operators, a local search framework is presented. A solution is labeled if it is fully explored by both two local search operators. All solutions generated in the local search phase are stored and evaluated. The non-dominated solutions are added in TA. The Pareto multi-objective local search procedure is presented as Pseudocode 4.

Pseudocode 4 Pareto multi-objective local search framework
Input: temporary archive TA, Nset1, Nset2
Output: TA
01: While $\Pi$ in TA is not selected
02: Nset1 $=$ Pareto local search insert (П)
03: Nset2 $=$ Pareto local search swap (П)
04: mark $\Pi$ as visited
05: For $\Pi_{\text {new }} \in\left(\right.$ Nset $\left._{1}, \operatorname{Nset}_{2}, \Pi\right)$ do
06: if $\Pi_{\text {new }}$ is not dominated by any solutions of TA
07: put $\Pi_{\text {new }}$ in TA, delete the dominated solutions
08: End For
09: End While

### 4.5. Energy-saving method

When investigating the inherent characteristics of blocking flowshop, we found that the blocking time of a job could be converted to processing time by reducing its operation speed without affecting the makespan (Property). Inspired by this property, a non-critical-pathbased energy-saving method is presented to optimize the energy consumption of all non-dominated solutions stored in TA. The critical path in flowshop refers to a sequential job sequence from the starting time to the completion time without intervals between any two adjacent jobs (Jiang \& Wang, 2019). The operations apart from the critical path are defined as non-critical operations. The proposed energy-saving method is implemented on the non-critical operations of the solutions from TA. The energy-saving method is demonstrated in Fig. 9.

In Fig. 9(b), the red dotted line with an arrow depicts the critical path for a factory with 4 jobs processing on 4 machines. Firstly, the energysaving method identifies the non-critical operations; then, the idle time $I_{n_{i}(j), i}$ and blocking time $B_{n_{b}(j), i}$ are calculated using the following equations:
$I_{n_{i}(j), i}=\max \left\{\left(D_{n_{i}(j+1), i}-p_{n_{i}(j+1), i}\right)-D_{n_{i}(j), i}, 0\right\}, \quad j=1, \ldots, n, i=1, \ldots, m, k=1, \ldots, f$
$B_{n_{i}(j), i}=\max \left\{D_{n_{i}(j-1), i+1}-\left(D_{n_{i}(j), i-1}+p_{n_{i}(j), i}\right), 0\right\}, \quad j=1, \ldots, n, i=1, \ldots, m, k=1, \ldots, f$

![img-8.jpeg](img-8.jpeg)

Fig. 9. Demonstration of critical path-based energy saving procedure.

The maximum allowable extension of processing time $\max \left(\Delta T_{i}(u)\right)$ and $\max \left(\Delta T_{B}(v)\right)$ should comply with the following principle:
$\max \left(\Delta T_{i}(u)\right) \leqslant I_{u_{i}(j), i}$
$\max \left(\Delta T_{B}(v)\right) \leqslant B_{u_{i}(j), i}$
By slowing down the operation speed to an appropriate levelv $\in \boldsymbol{V}$, the processing time is increased, and the energy consumption is therefore reduced. If there is no appropriate speed for the current operation, the original speed level is kept. Finally, the solutions after adjustment are evaluated and the non-dominated solutions are stored in PA. The energy-saving method is sketched in Pseudocode 5.

Pseudocode 5 Energy-saving method
Input: solutions in TA, PA
Output: PA
01: For each solution in TA do
02: identify the non-critical operations
03: calculate the idle time $I_{u_{i}(i), i}$ and blocking time $B_{u_{i}(j), i}$
04: calculate the maximum allowable extension time $\max \left(\Delta T_{i}(u)\right)$ and $\max \left(\Delta T_{B}(v)\right)$
05: identify the maximum allowable speed $v$
06: update the speed level matrix and corresponding processing time
07: End For
08: Evaluate the new solutions and store the non-dominated solutions in PA

### 4.6. Overview of MOEDA framework

Based on the previous descriptions, this study proposed a Paretobased MOEDA to optimize EDBFSP. MOEDA mainly includes the following 4 parts: population initialization, neighborhood search, Pareto multi-objective local search, and energy conservation. First of all, the ECFPV heuristic aimed to generate initial solutions with good makespans. Secondly, the Bayesian network-based probabilistic model was constructed to learn the information from the non-dominated solutions. To reduce energy consumption, two speed adjustment operators were designed, and an improved insertion technique was embedded to realize the adaptive adjustment of the speed level during the job insertion procedure. Subsequently, a Pareto multi-objective local search framework that contains two search operators was proposed. Besides, an energy-saving method was performed to further decrease energy consumptions. The overall framework of MOEDA is depicted in Pseudocode 6. MOEDA is expected to balance the exploration and exploitation during the search procedure.

## Pseudocode 6 Procedure of MOEDA

Input: population size $P s$, learning rates $_{k}$, temporary archive TA, Pareto archive PA Output: Pareto archive PA
01: set TA and PA to be empty
02: generate the population with ECFPV and random heuristics, evaluate each individual
03: store the non-dominated solutions in TA
04: initialize the probabilistic model $M \_j(\boldsymbol{g})$
05: While termination criterion not meet do
(continued on next column)
(continued)

Pseudocode 6 Procedure of MOEDA
06: extract the non-dominated solutions in TA to construct the probabilistic model $M \_j(\boldsymbol{g})$
07: sample $M \_j(\boldsymbol{g})$ and generate a new sequence $x$, random initialize speed level matrix $\boldsymbol{V}$
08: implement the search operators on each individual, update the speed level matrix $\boldsymbol{V}$
09: generate new individual by integrating $\boldsymbol{x}$ and $\boldsymbol{V}$
10: evaluate the offspring and update TA
11: perform Pareto multi-objective local search on the non-dominated solutions from TA
12: store the non-dominated solutions in TA
13: implement the energy-saving method on the non-dominated solutions in TA
14: evaluate the non-dominated solutions, set $\mathrm{PA}=\mathrm{PA} \cup \mathrm{TA}$
15: End While
16: construct PF

## 5. Experimental validation

In this paragraph, the system performance of MOEDA is assessed in different dimensions. Firstly, the experimental environment and the performance indicators are introduced. Secondly, the key parameters of MOEDA are calibrated. Afterward, the effectiveness of the proposed algorithmic components and optimization strategies are validated. Finally, MOEDA is compared with other well-known metaheuristics developed for energy-aware DFSP.

### 5.1. Experiment setting

The algorithm is coded in Python and loaded on a PC with an Intel(R) Core(TM) i7-8700 CPU @ 3.2 GHz/16G RAM under Windows 10. Since there was no published benchmark for EDBFSP, we generate test instances based on (Deng \& Wang, 2017; Deng \& Wang et al., 2016; Ding et al., 2016; Wang et al., 2018). The parameter scale is defined as:n $=$ $\{20.30 .50 .80 .100 .200\}, m=\{5.10,20\}$ and $f=\{2.3 .4 .5\}$. There are in total 48 combinations, each of which contains 10 different instances. As a result, the test benchmark comprises 480 instances. The processing time for each operation is randomly generated and fixed, which is set uniformly distributed between 1 and 99 . Five operation processing speed levels are pre-defined as $V=\{1,1.3,1.55,1.75,2.1\}$. According to literature (Deng \& Wang et al., 2016), the energy consumption indicators are defined as $P E_{u_{i}(f), i, v}=4+v^{2}$ and $S E=1.5$, respectively. As a matter of experience, the experiment results can approximate the real objective values when the replication number of the simulation is set infinitely. However, the simulation is limited by the computational capacity. Thus, in the experiment, the replication number is set as 10 .

### 5.2. Evaluation indicators

Strictly speaking, to evaluate the performance of a multi-objective solver comprehensively and scrupulously, the evaluation index should cover at least two aspects: unary indicator and binary indicator, which describe the convergence and distribution (diversity) of the obtained

solutions (Wang et al., 2018). It also implies that "good" non-dominated solutions found by one particular algorithm should access the Pareto front as closely as possible while covering the Pareto front as widely as possible. In this study, we adopt three metrics for the experiment:

Unary Hypervolume metric $\left(I_{H}\right): I_{H}$ scales the normalized amount of space that is formed by the non-dominated/Pareto-optimal solutions. Meanwhile, the covered normalized space considers reference points (optimum and anti-optimum) as its boundary for each objective.

The $I_{H}$ of a bi-objective is formulated as follows:
$I_{H}(S)=\operatorname{VOL}\left(\frac{1}{|\cdot|}\left|f_{1}^{\prime}(\gamma), z_{1}\right| \times\left|f_{2}^{\prime}(\gamma), z_{2}\right|\right)$
where $\operatorname{VOL}(\cdot)$ represents the Lebesgue measurement, $f_{1}^{\prime}$ and $f_{2}^{\prime}$ denote the normalized objective values, $\boldsymbol{S}$ is the non-dominated solution set used for constructing the solution space. $\boldsymbol{z}^{\prime}=\left(\boldsymbol{z}_{1}, \boldsymbol{z}_{2}\right)$ denotes the referent points set for demarcating the optimum and anti-optimum boundaries. The accuracy of calculating the $I_{H}$ relies highly on the selection of reference points. To create a fair comparison, the reference points are normally set as $\boldsymbol{z}_{1}>1$ and $\boldsymbol{z}_{2}>1$ (Ciavotta et al., 2013; Shao et al., 2019). Like (Shao et al., 2019), we set $\left(\boldsymbol{z}_{1}, \boldsymbol{z}_{2}\right)=(1.2,1.2)$ to guarantees a relative larger $I_{H}$, which further ensures better coverage and convergence of the Pareto front.

Binary coverage metric $\left(I_{C}\right)$ (Deng \& Wang et al., 2016): $I_{C}$ evaluates the quality of solutions by measuring the dominance relationship between the solution sets $\boldsymbol{P}_{1}$ and $\boldsymbol{P}_{2}$ that obtained via two comparing algorithms. The index $C\left(\boldsymbol{P}_{1}, \boldsymbol{P}_{2}\right)$ denotes the ratio of the solutions in $\boldsymbol{P}_{2}$ that are dominated by the solutions in $\boldsymbol{P}_{1}$ :
$C\left(\boldsymbol{P}_{1}, \boldsymbol{P}_{2}\right)=\left|\left(\boldsymbol{b} \in \boldsymbol{P}_{2}\right) \exists \boldsymbol{a} \in \boldsymbol{P}_{1}, \boldsymbol{a}>\boldsymbol{b} \boldsymbol{o r a}>\boldsymbol{b}\right| /\left|\boldsymbol{P}_{2}\right|$
where $\left|\boldsymbol{P}_{2}\right|$ represents the solution number in $\boldsymbol{P}_{2}, \boldsymbol{a}$ and $\boldsymbol{b}$ represent two comparing solutions. Apparently, The larger $C\left(\boldsymbol{P}_{1}, \boldsymbol{P}_{2}\right)$ is, the better solutions in $P_{1}$ than solutions in $P_{2}$.

The non-dominance ratio $\left(I_{R}\right)$ (Ishibuchi et al., 2017): $I_{R}$ estimates the rate of the non-dominated solutions obtained by a certain algorithm to the non-dominated solutions provided by all solution sets:
$R S=|S| \boldsymbol{x} \in S|\exists \boldsymbol{y} \in F S, \boldsymbol{x}=\boldsymbol{y}\}|/| F S|$
where $S$ is the solution set considered, $F S$ denotes the total solution sets obtained by integrating all single solution sets. $\boldsymbol{x}$ and $\boldsymbol{y}$ represent two compared solutions. It can be found that the greater the value of $R S$ is, the better the performance of the specified solution set (algorithm) has. With the above-mentioned indicators, the experiments are implemented from the following perspectives:

1) Calibration of the key parameters;
2) Effectiveness validation of algorithmic components and optimization strategies;
3) Comparison with other metaheuristics designed for multi-objective scheduling problems.

### 5.3. Parameter calibration

MOEDA contains two key parameters: population size $P s$ and
Table 1
ANOVA Analysis results of parameter combinations of MOEDA.
learning rates $_{\alpha}$. We employed the well-known Design of Experiment (DOE) to calibrate the key parameters. The candidate values for the parameters are set as follows: $P s=\{20.40 .60 .80 .100\}$, and $\alpha_{n}=\{0.1$. 0.2.0.3.0.4\}. 60 instances are randomly generated for calibration, with $90^{*} n^{*} m^{*} f$ milliseconds as the standard termination criterion. The two key parameters are denoted as the control factors and $I_{H}$ is defined as the response variable. The Analysis of Variance (ANOVA) is applied to analyze the calibration results. Table 1 shows the statistical results of ANOVA. In Table 1, $F$-ratio represents the influence of control factors, $p$ value represents whether the control factors have significant influences on the response value. The confidence interval is set at $95 \%$.

As can be seen from Table 1, the $p$-values of $P s$ and $\alpha_{n}$ are 0.0071 and 0.0008 , which are smaller than 0.05 . It means that both $P s$ and $\alpha_{n}$ have a great influence on the performance of MOEDA. The $F$-ratio of $\alpha_{n}$ is greater than that of $P s$, which indicates that $\alpha_{n}$ has a greater impact on algorithm performance. The main effect plot is shown in Fig. 10. As can be seen, with the increment of $P s$, the performance becomes better. This is because the increment of $P s$ can enrich the diversity of the population, which improves the probability of obtaining optimal solutions. However, an overlarge $P$ may waste computing resources, which leads to the compression of local search time, thereby, the search efficiency of the algorithm is affected. It can be observed that, when $\alpha_{n}=0.2$, the algorithm performs its best. Based on the above analysis, the key parameters of MOEDA are set as $P s=60$ and $\alpha_{n}=0.2$.

### 5.4. Effectiveness of the proposed optimization strategies

In this section, the effectiveness of the proposed algorithmic components (initialization strategy, neighborhood structure, and local search scheme) of MOEDA are validated. We generated 4 variant algorithms, i.e., MOEDA_NI, MOEDA_NN, MOEDA_NL and MOEDA_NES from the original MOEDA. Each variant only varied one component comparing to the proposed MOEDA. The acronym MOEDA_NI denotes MOEDA without initialization strategy, while MOEDA_NN, MOEDA_NL, and MOEDA_NES represent MOEDA without neighborhood structure, local search scheme, and energy conversation strategy, respectively. In the experiment, 60 instances for factory number $f=3$ were chosen as the test instances, $I_{H}$ and $I_{R}$ were chosen as the performance indicators. All variants adopted the same elapsed CPU time as the termination criterion. Table 1 demonstrates the statistical results of the two performance indicators. Table 2 presents the average values of results across 60 test instances with 10 replicative runnings per instance, and the best results of each combination are emphasized in bold.

As seen from Table 2, MOEDA has obtained larger $I_{H}$ than MOEDA_NI, MOEDA_NN, MOEDA_NL, and MOEDA_NES, which implies the proposed optimization strategies have made significant contributions to MOEDA. To be specific, MOEDA_NN obtained the worst computational results, which indicates that the neighborhood search strategy influences the performance of MOEDA more. The neighborhood search plays the role in generating new populations and record non-dominated solutions. The speed-up mechanism has reduced the evaluation time of the generated neighboring solutions, and thereby strengthens the search efficiency effectively. The exploration of the entire algorithm would enormously reduce when the neighborhood search is excluded. MOEDA_NL obtained the second-worst results, which reveal that the local search scheme has also made a large contribution in boosting the performance of MOEDA. The local search scheme aims to help MOEDA escape from the local optimum. When the neighbor structures of the non-dominated solutions have not been renewed for a long time, meanwhile local search operators are not implemented, the evolution procedure of the population could stepwise stagnate and the algorithm would trap into local optimum. Thus, the exploitation of MOEDA can be enhanced with the proposed local search scheme. MOEDA_NI with a random initialization approach is also inferior to MOEDA, which indicates that the initialization scheme affects MOEDA partially. The ECFPV heuristic aims to start from the best region for makespan, and

![img-9.jpeg](img-9.jpeg)

Fig. 10. Main effects plot of parameters for MOEDA.

Table 2
Comparisons between MOEDA and its variant algorithms.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Mean plots with $95 \%$ confidence intervals of $I_{H}$ and $I_{R}$ for all compared variants of MOEDA.

Table 3
Statistical results for binary indicator $I_{G}$ of all compared algorithms.
stepwise guide the search to the energy-related objective. Thus, ECPPV can provide good start points for MOEDA. The MOEDA_NES performs worse than MOEDA, but better than other variant algorithms. Essentially, the energy-saving strategy is the perturbation of non-dominant solutions. The result has shown that it can influence the performance of MOEDA partially and increase the diversity of the solutions. Besides, the non-dominance ratio $I_{B}$ of all the variants is inferior to MOEDA, which further reveals that the proposed optimization components are crucial for MOEDA in obtaining Pareto optimal solutions.

To further confirm the aforementioned conclusions, the mean and $95 \%$ confidence interval plot of the results from Table 2 are presented in Fig. 11. Note that the overlapping intervals imply no significant differences from statistical views. As shown in Fig. 11, the $95 \%$ confidence interval of MOEDA places over all variants of MOEDA without any overlapping, which reveals that there are significant differences between MOEDA and all variant algorithms. The effectiveness of MOEDA also confirms the necessity of each proposed improvement strategies. A lack of any components will degrade the overall performance of the algorithm.

Furthermore, the statistical results over indicator $I_{G}$ between the original MOEDA and the variant algorithms are shown in Table 3. Due to space limitations, the MOEDA, MOEDA_NI, MOEDA_NN, MOEDA_NL and MOEDA_NES are represented by M, M_NI, M_NN, M_NL and M_NES, respectively. As can be seen in Table 3, all groups of comparisons share one feature that MOEDA is superior to its variant algorithms over $I_{G}$. Since $I_{G}$ measures the quality of solutions, the results either imply that the solution set obtained by MOEDA approximates more closely to the Pareto optimal set. As a rule, to obtain good search results, the cooperation of all algorithmic components is indispensable.

### 5.5. Comparison with well-known approaches

Since there are no dedicated algorithms designed for solving EDBFSP, we compared MOEDA with the following metaheuristics: CMA (Deng \& Wang, 2017), CA (Wang et al., 2017), KCA (Wang \& Wang, 2018), and EDE (Zhao et al., 2020). CMA was proposed for optimizing the carbon footprint of DPFSP, CA was developed for energy-aware DFSP with no wait constraint (EDNWFSP), and KCA was designed for energy-conscious DPFSP. The abovementioned metaheuristics have demonstrated superiorities over the classical algorithm such as NSGA-II and SPEA-II. EDE was originally designed for DBFSP with makespan as single performance criterion. It was modified to optimize EDBFSP, that is, the Pareto concept was embedded in EDE. The speed-related variables were adopted with random strategy in different search stages, i.e. initialization, neighborhood search, and local search. Since all other
compare metaheuristics have energy-saving steps, EDE was also equipped with this strategy. In the experiment, all metaheuristics were coded under the same compiling environment, involving the same programming language. We hew to obey the presentations of literature to implement the compared algorithms. Even if they were not originally proposed for EDBFSP, the core search ideas including algorithmic structure, solution presentation method, global and local search methods were preserved. Besides, the same data structure, fitness function, and library functions (e.g. insertion mechanism) were shared for all metaheuristics, to avoid the influences of different implementations on the performance of each metaheuristic. The parameters of the compared algorithms were fine-tuned for solving EDBFSP. The parameter settings of compared algorithms are listed in Table 4.

The experiments were conducted based on the 480 instances generated in Section 5.1. To avoid the effect of randomness, each algorithm has run 10 replications for each instance independently. The termination criterion is set as $90 \times n \times m \times f$ milliseconds CPU elapsed time. The statistical results in terms of three indicators for each combination are presented in Tables 5 to 8 , which are grouped by different numbers of factories.

From Tables 5 to 8, it can be seen that in terms of all performance indicators, MOEDA outperforms its competitors on the instances. Whether on Hypervolume $I_{H}$, non-dominance ratio $I_{R}$, or coverage metric $I_{C}$, the results obtained by MOEDA are close to optimum values ( 1.44 for $I_{H}, 1.0$ for $I_{R}$, and 1.0 for $I_{C}$ ), which also implies that MOEDA achieved nearest to the reference Pareto front.

Although Tables 5-8 have validated the effectiveness of MOEDA, the results are still not convincing enough since the compared algorithms always have stochastic behaviors during their runtime. There is a need to take additional tests to identify whether the results between different approaches are statistically significant. For this purpose, two statistical tests including a parametric test and a non-parametric test were conducted, which are described as follows.

For the parametric test, two ANOVA tests were implemented, in which the performance indicators $I_{H}$ and $I_{R}$ were considered as the response variables. The results grouped by different factories are presented in the ANOVA plots with $95 \%$ confidence intervals in Fig. 12. As can be seen from Fig. 12, there are no overlapping intervals between MOEDA and other compared metaheuristics on each single test problem, which implies clearly that MOEDA has statistical differences with compared algorithms. In other words, MOEDA is statistically significantly better than other metaheuristics. Moreover, it can be observed that all the compared metaheuristics performed well on small-scale instances (e.g. $n=20$ ), but degrade more or less when the problem scales become more complicated. To investigate such influence, the interaction plots between algorithms and the combination of $n \times m$ are demonstrated in Fig. 13. As revealed in Fig. 13(a), the compared metaheuristics have shown strong competitiveness over small-scale instances, the obtained results of Hypervolume are very close to those of MOEDA. With the increment of the instance scales, the performances of all metaheuristics have declined. Especially for compared metaheuristics, the obtained results have shown that their performances sharply reduced over larger instances. Different from them, the performance of MOEDA is slightly affected. From Fig. 13(b), it can be seen that the nondominance ratio obtained by MOEDA along each combination maintains an upward trend, whereas the values from the other metaheuristics

![img-11.jpeg](img-11.jpeg)

![img-12.jpeg](img-12.jpeg)

![img-13.jpeg](img-13.jpeg)

Fig. 12. Mean plots with $95 \%$ confidence intervals of $I_{H}$ and $I_{R}$ for all compared metaheuristics.
![img-14.jpeg](img-14.jpeg)

Fig. 13. Mean plots with $95 \%$ confidence intervals of all compared algorithms and combinations for indicators: (a) Hypervolume $I_{H}$; (b) Non-dominance ratio $I_{R}$.

Table 9
Result of Holm's test.
Note: R/A denotes reject/accept the hypotheses.
degrade severely. It implies that MOEDA is more efficient in finding high-quality solutions that are proximal to the Pareto front. In the concrete, MOEDA has shown stability in different scales of test instances, which also reveals that its robustness is better than the compared algorithms.
2) For the non-parametric test, Holm's method is employed. Holm's test is a closed testing procedure designed for multiple hypotheses. In the test, a set $H=\left\{H_{1}, \ldots, H_{r}\right\}$ contains $r$ hypotheses, the set $P=\left\{P_{1}, \ldots\right.$ $\left.P_{r}\right\}$ contains the $p$-values that represent the probabilities of monitoring the statistical results by accident. The $p$-values are sorted in ascending order $\operatorname{asp}_{(1)} \leqslant p_{(2)} \leqslant \ldots \leqslant p_{(r)}$. Let $\delta$ be a significance threshold that
determines to reject the null hypothesis, and $k$ represents a minimum indicatrix that satisfies the inequality relations of $\mathrm{p}_{k} \geqslant \delta /(r+1-k)$. As a result, null hypotheses from $H_{1}$ to $H_{k-1}$ are rejected. In contrast, the hypotheses from $H_{k}$ to $H_{r}$ are accepted. In this study, the performance indicators $I_{H}$ and $I_{R}$ are defined as the response variables. MOEDA is considered as the reference algorithm, and the other two algorithms are assumed respectively equal to MOEDA. Hence, in total two hypotheses are yielded. To demonstrate the differences clearly, a $95 \%$ confidence level is also considered, which means $\delta=0.05$. As shown in Table 9, all revenant $p$-values of hypotheses $H_{r}$ on the performance indicators are close to zero, which are much smaller than the value of $\delta$. Hence, all hypotheses in this test are rejected. The test result reveals that MOEDA significantly outperforms the compared metaheuristics from the statistical view.

To visualize the algorithmic performances, the Pareto fronts obtained by the compared algorithms for certain instances (factory number $f=3$ ) are sketched in Fig. 14. It is worth noting that the Pareto fronts discussed in this study are formed by those Pareto optimal solutions, which were selected in advance using the well-known fast nondominated sorting method proposed by Deb et al. (Deb et al., 2002). As presented in Fig. 14, all Pareto fronts are relatively close and superposed on small instances (e.g., Instance 20_5_3_1, Instance 30_5_3_1, and Instance $30,10 \_3 \_1$ ). With the increment of instance scales, the Pareto fronts of MOEDA are closer to the origin of coordinates, which indicates that MOEDA can find Pareto fronts that dominate those of other algorithms observably. It also reveals the strong exploration and

![img-15.jpeg](img-15.jpeg)

Fig. 14. The Pareto fronts obtained from selected test instances.
exploitation ability of MOEDA in both small and large instances.
To analyze the non-dominant solutions of PF, the test instance $50,5,3,1$ is taken as an example. From the PF of MOEDA, it can be observed that the minimum mean makespan obtained by MOEDA is 1294.5, and the corresponding processing energy consumption of this solution is 87898.2. In the contrast, the minimum average energy consumption obtained by MOEDA is 85208.7 , and the average mean makespan corresponding to this solution is 1436.5 . When comparing the two solutions, the former one shortens the manufacturing time by about $9.87 \%$ but increases the total energy consumption by $3.16 \%$ correspondingly. This phenomenon also reflects the conflicted relationship between the two objectives. The decision-makers can make quantitative indicators according to the actual needs of manufacturing, to select the appropriate solution on the PF, and guide the scheduling task.

## 6. Conclusions and future works

This study investigated the EDBFSP that considers both productivity and energy consumption as optimization indicators. The adjustment of energy consumption is correlated to different operation speed levels of jobs under a pre-defined speed scaling framework. To solve EDBFSP, a multi-objective estimation of distribution algorithm (MOEDA) was proposed. First, a hybridized improved initialization strategy was designed to generate the population. Second, a Bayesian inference-based probabilistic model and specific speed adjustment operators were proposed to find better search spaces for both objectives. Afterward, a local search framework was proposed to perturb high-quality individuals, which aims at equilibrating the exploration and exploitation of the proposed algorithm. Lastly, an energy-saving method was implemented
based on problem-specific characteristics. To validate its performance, the key parameter of MOEDA was calibrated. In the meantime, the performances of the proposed algorithmic components and optimization policies were verified in a simulative test. The proposed MOEDA was compared with two well-known metaheuristics on different benchmark instances. The analysis results demonstrated that MOEDA is significantly better than its competitors. The study also presents that energy consumption can be significantly reduced by employing energy-efficient machine behavior policies.

Other than conclusions, there are some observations reported for future work:

The presented MOEDA could be methodologically improved in future work. The neighborhood search framework might be implemented in an integrated way. Also, the search for Pareto nondominated solutions could be enhanced in regions with higher makespans, despite the practical application scenario. Moreover, the parameter calibration would be optimized by employing it for different problem scales.
The assumption for estimating the energy consumption applied in this research is insufficiently precise. Relying on the research characteristics at the present stage, some other aspects corresponding to manufacturing planning and scheduling might be surveyed. For instance, it is meaningful to embed the energy effects of switching machines on and off explicitly.

## CRediT authorship contribution statement

Xiaohui Zhang: Formal analysis, Writing - original draft. Xinhua

Liu: Methodology, Software, Investigation, Funding acquisition. Andrzej Cichon: Resources, Software, Writing - review \& editing. Grzegorz Króczyk: Supervision, Data curation, Writing - review \& editing, Funding acquisition. Zhixiong Li: Conceptualization, Resources, Supervision, Writing - review \& editing, Funding acquisition.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

The support of the Natural Science Foundation of Xuzhou, China (KC21070), National Natural Science Foundation of China (51975568\& 61803192), National Natural Science Foundation of Jiangsu Province (BK20191341), Narodowego Centrum Nauki (No. 2020/37/K/STB/ 02748), Industry-University-Research Collaboration Project of Jiangsu Province (BY2021559) and Priority Academic Program Development of Jiangsu Higher Education Institutions (PAPD) in carrying out this research is gratefully acknowledged.
