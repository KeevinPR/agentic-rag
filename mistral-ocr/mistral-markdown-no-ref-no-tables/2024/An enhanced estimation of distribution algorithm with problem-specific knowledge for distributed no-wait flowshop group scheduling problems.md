# An enhanced estimation of distribution algorithm with problem-specific knowledge for distributed no-wait flowshop group scheduling problems 

Zi-Qi Zhang ${ }^{\mathrm{a}, \mathrm{b}}$, Yan-Xuan Xu ${ }^{\mathrm{a}}$, Bin Qian ${ }^{\mathrm{a}, \mathrm{b},{ }^{\mathrm{a}}}$, Rong Hu ${ }^{\mathrm{a}, \mathrm{b}}$, Fang-Chun Wu ${ }^{\mathrm{a}}$, Ling Wang ${ }^{\mathrm{c}}$<br>${ }^{a}$ School of Information Engineering and Automation, Kunming University of Science and Technology, Kunming 650500, PR China<br>${ }^{\mathrm{b}}$ Yunnan Key Laboratory of Artificial Intelligence, Kunming University of Science and Technology, Kunming 650500, PR China<br>${ }^{\mathrm{c}}$ Department of Automation, Tsinghua University, Beijing 100084, PR China

## A R T I C L E I N F O

Keywords:
Flowshop group scheduling
Distributed no-wait flowshop group scheduling Estimation of distribution algorithm Problem-specific knowledge

## A B S T R A C T

With the trend of economic globalization, distributed manufacturing widely exists in modern manufacturing systems. As an extension of the distributed flowshop scheduling problem, the distributed no-wait flowshop group scheduling problem with sequence-dependent setup times (DNFGSP_SDSTs) is investigated in this article. To address DNFGSP_SDSTs with the criterion of minimizing makespan, this study proposes an enhanced estimation of distribution algorithm-(EEDA) with problem-specific knowledge. First, a mixed integer linear programming (MILP) model of DNFGSP_SDSTs is established. Second, based on the characteristics of DNFGSP_SDSTs, five problem-specific properties about local search operators are derived as prior knowledge to reduce computational cost. Third, two NEH-based two-stage heuristics are presented to construct a high-quality population with diversity. Fourth, a probability model with problem-specific knowledge and a family-based updating mechanism are developed to accumulate valuable pattern information from high-quality solutions, while a sampling strategy is designed to generate new populations with the accumulated information. Fifth, several local search operators are devised to refine the obtained solutions. Furthermore, perturbation and reinitalization methods are developed to avoid premature convergence. Finally, the validity of the MILP model is verified by using the Gurobi solver. The parameters of EEDA are tuned through a design of experiments. The effectiveness of key components in EEDA is confirmed through extensive experiments, and the computational comparisons with the state-of-theart algorithms indicate the effectiveness of the proposed EEDA for solving DNFGSP_SDSTs.

## 1. Introduction

Amidst the backdrop of economic globalization and the advent of industrial intelligence, the role of distributed manufacturing has gained increasing importance in efficiently coordinating resources across regions, flexibly adapting to demands, reducing costs, and enhancing efficiency, which has proactively promoted the upgrading of modern supply chains and cell manufacturing systems (CMS) [1,2]. As a crucial challenge within distributed manufacturing, the distributed flowshop group scheduling problem (DFGSP) has attracted considerable attention and dedicated research efforts [3]. Unlike traditional flowshop production, distributed flowshop group production has the advantages of flexible resource allocation and rapid adaptation to requirements, prioritizing cost-efficient group lots and facilitating mass-customized production [4]. Given these significant strengths, it is vital to study distributed scheduling problems (DSPs), specifically those involving
collaborative production across multiple factories. Hence, employing emerging techniques to develop effective and efficient approaches for addressing DSPs holds both academic interest and practical significance [5].

Over the past decade, substantial scholarly studies have surfaced, mainly focusing on DSPs and their extensions, with distributed flowshop scheduling problems (DFSPs) emerging as a prominent focus [6]. Pioneering work by Naderi and Ruiz [7] in modeling and optimizing DFSPs have laid the foundation for research on various variants in distributed environments. The concept of CMS has garnered attention for its potential to enhance efficiency and flexibility in production processes by grouping similar jobs into families and processing them in specific cells, thus reducing setup time and inventory cost. This concept, pioneered by Radharamanan [8], has found successful studies and applications across industries, including automotive, smart furniture, semiconductor, and electronics [9]. However, practical production practices necessitate

[^0]
[^0]:    a Corresponding author.

    E-mail address: bin.qian@vlp.163.com (B. Qian).

scheduling considerations that account for setup times, which play pivotal roles in resource readiness and just-in-time delivery [10]. In general, the durations of operations, such as machine cleaning, tool changeover, and job transfer between machines, often referred to as sequence-dependent setup times (SDSTs), depend on both the current and subsequent families in lines [11]. For FGSP, jobs are grouped based on common characteristics of the production process and processing priorities within cells [12]. Therefore, it becomes essential to consider only setup times between families, enabling to exclude setup time considerations among jobs within the families, enhancing efficiency and reducing waiting times [13]. Given current interests in SDSTs, further in-depth research on FGSPs with SDSTs is of practical significance. In addition, considering real-world applications in industries such as steelmaking, food processing, and chemical and pharmaceutical industries, it is imperative to take into account both SDSTs and no-wait constraints [14]. The no-wait constraints require that job processing cannot be interrupted on consecutive machines [15]. To meet no-wait condition in practical production processes, substantial scholarly studies have emerged in recent years [16], [17], [18], [19], [20]. Despite the significance of solving no-wait FGSP_SDSTs (NFGSP_SDSTs) has been stressed, it has not been sufficiently studied in distributed manufacturing. Given the increasing interest of DSPs in CMS, it has become increasingly important to handle the complex constraints of distributed NFGSP_SDSTs (DNFGSP_SDSTs). As a response to this need, this study undertakes the challenge of addressing DNFGSP_SDSTs.

DNFGSP_SDSTs commonly comprises coupled subproblems, including the family assignment subproblem and the job processing order subproblem. The crucial challenge lies in determining the allocation of families to cellulars, the arrangement of families within each cellular, and the order of jobs within each family to minimize the makespan. Both of subproblems inherently involve SDSTs and no-wait constraints, rendering them highly complex and challenging. Notably, the FGSP with SDSTs is NP-hard in a strong sense [21], whereas the FGSP_SDSTs is a generalization of the DNFGSP_SDSTs, which is also NP-hard. To facilitate clear representation, Graham et al. [22] introduced the three-field notation $o i j \beta j \gamma$, where $\alpha$ is the production environment, and $\beta$ and $\gamma$ denote the process constraints and criteria, respectively. For DNFGSP_SDSTs aiming to minimize the makespan, it can be denoted as $F_{m} \ldots . F_{m} \mid f m l s . n w t . S D S T s / C_{\max }$ [23]. Here, $F_{m}$ represents a flowshop with $m$ machines, $F_{m} \ldots . F_{m}$ represents distributed flowshops with $m$ machines, fmls, nwt, SDSTs represent group processing, no-wait constraint, and SDSTs, respectively, and $C_{\text {max }}$ refers to the makespan. DFGSP_SDSTs can be represented as $F_{m} \ldots . F_{m} \mid f m l s . S D S T s / C_{\max }$ and NFGSP_SDSTs as $F_{m} \ldots . F_{m} \mid f m l s, n w t . S D S T s / C_{\max }$. Since $F_{m} \ldots . F_{m} \mid f m l s$, $S D S T s / C_{\max }$ and $F_{m} \mid f m l s, n w t . S D S T s / C_{\max }$ have been proven to be NP-hard [18,24], it follows that the strongly constrained variant $F_{m} \ldots . F_{m} \mid f m l s$, nwt. SDSTs/Cmax of both is also NP-hard. To address the NP-hardness challenges effectively, there are both exact and approximate approaches available. Exact approaches, such as mixed integer linear programming (MILP), constraint programming (CP), column generation (CG) and benders decomposition (BD), are available but may cause considerable computational costs, especially when dealing with large-sized FGSPs, limiting their practical utility. Conversely, approximate approaches, including constructive heuristics and metaheuristics, provide practical insights for solving FGSPs and their extensions in distributed environments. Constructive heuristics can quickly generate feasible solutions based on problem characteristics and constraints, although the quality of these solutions may not always be desirable. However, extracting features or formulating effective heuristic rules for addressing complex FGSPs may be challenging. As typical approaches in metaheuristics, hybrid intelligent optimization algorithms (HIOAs) have garnered attention for their exceptional efficacy in solving scheduling problems. HIOAs commonly combine problem-specific global search frameworks and local search strategies based on feasible encodings. Specifically, the potential of HIOAs in solving strongly coupled scheduling problems is stimulated by well-integrated use of constructive
heuristics and local search operators, along with mechanisms like diversity maintenance to effectively balance global and local search, thus yielding high-quality solutions within a limited timeframe [23]. Various studies have employed HIOAs, such as GA [13,16,25-27], TS [28,29], PSO [17,30], SA [19,31,32], and ACO [33], to tackle FGSPs, DFGSPs, and their variants. A review of recent related research on FGSPs is summarized in Table 1.

Among HIOAs, the estimation of distribution algorithm (EDA) stands out as holding significant research value and promising prospects, as probability modeling and implicit parallelism provide novel insights and methodologies for addressing various types of complex and large-scale problems [20,34]. By utilizing probability models to estimate the structural and distributional characteristics of high-quality solutions, EDA has been demonstrated to explore complex search spaces effectively, efficiently guiding the search scope towards promising regions for seeking superior solutions. When addressing DNFGSP_SDSTs, family constraints constrain the allocation of jobs, no-wait constraints tighten the connections between jobs, and SDSTs stresses the significance of family sequencing for the quality of solutions, all of which cause challenges. Although existing EDAs excelled at learning relationships between jobs, they struggled to effectively capture correlations of families, resulting in the oversight of specific features crucial to superior solutions. Inspired by multiple probability model-based EDAs [14,35] and multidimensional probability model-based EDAs (MEDAs) [20,36-39], this study presents a knowledge-enhanced EDA tailored for DNFGSP_SDSTs. This EEDA focuses on extracting and estimating information between adjacent jobs and patterns across families. To capture the connections between families and between jobs, the probability model is divided into multiple partition matrices based on the relationships of intra- and inter-family jobs, respectively. A family-based updating mechanism is used to extract potential patterns from high-quality solutions, and promising patterns are converted into probabilities to be accumulated in these partition matrices. Next, a specific sampling strategy is used to yield new solutions with certain quality by extracting valuable information from this probability model. Compared to previous EDAs, an enhanced EDA with problem-specific knowledge has been developed for DNFGSP_SDSTs, aiming to retain EDA's strengths while adapting to problem's characteristics for seeking superior solutions. The prospect of this knowledge-enhanced learning paradigm in tackling the challenges posed by DNFGSP_SDSTs seems promising.

As mentioned above, the main contributions of this article are highlighted below.

- The MILP model for DNFGSP_SDSTs is developed, which considers family assignment and job arrangement subproblems with no-wait constraints and sequence-dependent setup times.
- Five problem properties are derived as problem-specific knowledge, and several knowledge-based speedup strategies are designed to save computational efforts in evaluating solutions.
- To efficiently solve DNFGSP_SDSTs, EEDA with problem-specific knowledge is presented. In EEDA, the probability model is designed by partitioning matrices used to record relations of intraand inter-family jobs, which captures the connections between families and between jobs to effectively guide the global search towards promising regions.
- To yield high-quality initial solutions with certain diversity, an effective hybrid initialization method based on two problem-specific heuristics is proposed, which can reasonably refine population quality and reduce the processing times for both job and family sequences.
- A family-based updating mechanism and a novel sampling strategy are embedded in EEDA to estimate the distribution of crucial characteristics and execute effective exploration in the solution space, so as to efficiently direct search scopes toward promising regions for seeking superior solutions, while both perturbation and

Table 1
Summarization of papers on FGSPs.
Note: $S T s$ : SDSTs, $m w t$ : no-wait, block: a blockage of the machine due to limited buffer space of the next machine, $t s t$ : transportation time, $r d$ : release date, $D M$ : distributed manufacturing, $F_{m}$ : flowshop with $m$ machines, $F F_{s}$ : Flexible flowshop with $s$ stages, $f m l s$ : part families: $M$ families with $n_{b}$ jobs are assigned to a flowshop cell to be processed; LBD: Lower-bound development; GA: Genetic algorithm, TS: Tabu search, PSO: Particle swarm optimization, SA: Simulated annealing, VNS: Variable neighborhood search, IG: Iterated greedy, RMSA: Revised multi-start simulated annealing, DDE: Discrete differential evolution, B\&P: Branch-and-price, HHS: Hybrid harmony search, BBO: Biogeography-based optimization, CCEA: Cooperative co-evolutionary algorithm, MA: Memetic algorithm, MM: Mathematical model, MOGA: Multi objective genetic algorithm, NSGA-II: Non-dominated sorting genetic algorithm; $C_{\text {max }}$ : Makespan, TCT: Total completion time, TWT: Total weighted tardiness, TWET: Total weighted earliness and tardiness, TT: Total tardiness, TWCT: Total weighted completion time.
reinitialization methods are also designed to sidestep search stagnation and stimulate search vitality.

- To enhance the local exploitation of EEDA and refine the obtained solutions, three problem-specific local search strategies are presented, where the family-based and job-based swap or insertion operators are properly utilized to further reduce the makespan.
- To verify the effectiveness of the MILP model, the Gurobi solver is employed and validated on small and medium sized instances. Furthermore, the proposed knowledge-enhanced EDA is compared with several state-of-the-art algorithms on instances of different sizes and the statistical results demonstrate the superiority of EEDA for DNFGSP_SDSTs.

The subsequent sections are organized as follows. In Section 3, we provide a detailed description of the MILP formulation for DNFGSP_SDSTs and explain speed-up evaluation methods. Moreover, we provide an in-depth analysis of problem properties. Section 4 describes the knowledge-enhanced EDA, including coding schemes, partitioned probability model, family-based updating mechanism, sampling strategy, and perturbation and reinitialization. Furthermore, problemspecific local search strategies for DNFGSP_SDSTs are introduced. Section 5 is dedicated to extensive experiments and comprehensive comparisons. In Section 6, we discuss some findings, research limitations, and make suggestions for future research.

## 2. Literature review

In this study, we propose an effective enhanced EDA with problemspecific knowledge to tackle the DNFGSP_SDSTs. It is worth noting that, to the best of our knowledge, research on this problem has rarely been reported in the literature. Thus, we conduct a comprehensive review of the related works on FGSPs, DFSPs, and the applications of EDAs
to scheduling problems.

### 2.1. Flowshop group scheduling problems

FGSPs are widely recognized as considerable challenges in flexible manufacturing systems, and in recent years, studies on FGSPs have garnered increasing attention due to their potential to shorten manufacturing cycles, reduce inventory levels, and decrease production costs [9]. The core concept behind group scheduling aims to enhance efficiency by grouping similar jobs into families, thereby reducing adaptation and preparation times. Radharamanan [8] first introduced this concept, providing a heuristic method for determining both the optimal group and job order in a batch-type production process with a functional layout. It is further confirmed that enterprises implementing CMS receive multiple benefits, including reduced setup and process times, work-in-process inventories, simplified flow of jobs, and improved production efficiency [26]. To ensure that machines are running on time, machine downtime is reduced, and delivery dates are met, it is inevitable that setup times need to be emphasized [10,11]. Thus, the study scope has been extended by further considering the SDSTs as a key factor in optimizing the makespan of FGSPs [50]. For minimizing the makespan of FGSP_SDSTs, Ying et al. [31] proposed an effective SA approach that showed effectiveness in yielding high-quality results. They recommended the utilization of non-permutation schedules to enhance efficiency within reasonable computational costs. Expanding the scope to consider other criteria for FGSP_SDSTs and its variants, numerous endeavors have emerged. Karimi et al. [25] dealt with flexible FGSP_SDSTs which considers minimizing the criteria of both makespan and TWT by implementing a multi-phase bi-objective GA. Yuan et al. [21] investigated FGSP_SDSTs further taking into account the round-trip transportation time between machines and proposed a co-evolutionary DDE algorithm (CDDEA) for minimizing the makespan.

Subsequently, Naderi et al. [40] proposed a metaheuristic hybridizing genetic and simulated annealing (GSA) algorithm for minimizing the total completion time, while Hajinejad et al. [30] introduced a hybrid PSO (HPSO) algorithm for optimizing FGSP_SDSTs with the goal of minimizing TCT. Both GSA and HPSO outperformed the hybrid ACO (HACO) algorithm proposed by Salmasi et al. [33]. Li et al. [45] presented a hybrid harmony search (HHS) for solving the flowline manufacturing cell scheduling problem (FMCSP) with SDSTs to minimize both total tardiness and mean total flowtime. Further contributions by Costa et al. [26,27] introduced a hybrid GA (HGA) and a parallel self-adaptive genetic algorithm (PSAGA), both of which outperformed GSA [40] and HPSO [30], among them, PSAGA achieved the best results, delivering the best results in terms of optimizing the makespan of FGSP_SDSTs. In addition, the practical industrial applications of CMS, spanning diverse sectors like hot rolling, chemical or pharmaceutical processes, and food industries, add additional constraints such as no-wait constraints, escalating the complexity of group scheduling challenges. Considering FGSP_SDSTs with no-wait constraints, Ying et al. [16] proposed three heuristics, i.e., GA-based, SA-based, and IG-based heuristics, for minimizing the makespan of NFGSP_SDSTs. Experimental results revealed that although the SA-based heuristic performed the best among the three, there was no significant difference between them. To find more efficient algorithms for optimizing the TWET of NFGSP_SDSTs, Arabameri and Salmasi [51] developed several HIOAs based on TS and PSO. The results indicated a slight superiority of PSO-based algorithms, especially when handling medium- and large-sized problems. For minimizing the TCT of NFGSP_SDSTs, Behjat and Salmasi [17] proposed several versions of PSO- and VNS-based algorithms, incorporating multiple neighborhood search structures for enhanced problem-solving capabilities. Recently, Cheng et al. [19] also proposed two types of HIOAs, i.e., a revised multi-start SA (RMSA) and a local search-based variant (RMSA $\mathrm{LS}_{2}$ ), both of which yielded better solutions than PSO- and VNS-based algorithms [17]. Remarkably, the efficacy of RMSA $_{\text {LS }}$ was better than that of RMSA, particularly in real-life applications demanding high-quality solutions for industrial scenarios. According to above review, critical observation shows that the study of NFGSP_SDSTs is still scarce. This gap is motivated by the need to improve productivity, reduce costs and optimize production cycles, emphasizing the significance of investigating FGSPs to tackle the multifaceted challenges posed by complex constraints and setup time dependencies inherent in CMS.

### 2.2. Distributed flowshop scheduling problems

DFGSPs share similar characteristics with DFSPs, with the latter being more extensively explored, and therefore providing valuable insights into the study of the former, which are of great interest. As for the minimization of the makespan for DFSP, Naderi and Ruiz [7] presented a comprehensive characterization of the problem through the formulation of six MILP models. They provided two factory allocation rules, i.e., $\mathrm{NR}_{1}$ and $\mathrm{NR}_{2}$, and then devised 14 heuristics incorporating several VND-based local search methods, resulting in excellent effectiveness. After this pioneering effort, Wang et al. [52] also introduced an earliest completion factory (ECF) allocation rule and proposed an effective EDA to address this challenge. Considering no-wait constraints, Shao et al. [53] attempted to address the DNFSP with the goal of minimizing makespan by developing an IG-based heuristic. Comparing the efficacy of EDA [52] and IG [53] with several heuristics [7], both EDA and IG proved to be more effective, especially for large-scale problems. Notably, the effectiveness of the IG based on VND surpassed that of the EDA and other IG-based versions proposed by Shao et al. [53]. For solving DFGSP_SDSTs with the aim of minimizing makespan, Pan et al. [3] proposed a CCEA and Wang et al. [24] presented a two-stage IG (TIG $\mathrm{v}_{1}$ ). Both CCEA and TIG ${ }_{v 1}$ outperformed IG, and TIG ${ }_{v 1}$ achieved the best results among them. In addition, Wang et al. [54] proposed a TIG ${ }_{v 2}$ to minimize the TT in DFGSP_SDST. Unlike the reconstruction
mechanism of $\mathrm{TIG}_{\mathrm{v} 1}$, which examined all extracted families at all possible positions, that of $\mathrm{TIG}_{\mathrm{v} 2}$ selectively tested potential positions. Li et al. [55] further introduced the destruction-construction mechanism inherent in IGs into the framework of ABC algorithm to address DFSP with peak power consumption, which provided a new perspective on the design of improved ABC (IABC). More recently, He et al. [56] provided a novel insight by developing a greedy CCEA with problem-specific knowledge to solve energy-efficient FGSP with the criteria of minimizing the makespan, total flow time (TFT), and total energy consumption (TEC), simultaneously. Furthermore, Niu et al. [57] designed a two-stage CCEA (TS-CCEA) to minimize both makespan and TEC to address the energy-efficient distributed group blocking flowshop problem with setup carryover in precast systems. Compared with existing multi-objective evolutionary algorithms, TS-CCEA demonstrated superior search performance and stability. Consequently, these research efforts collectively contribute to the development of innovative methodologies and efficient scheduling strategies to address the complex challenges posed by DFGSP. Considering their potential applications in distributed manufacturing systems, the study of DFGSPs is of both academic and engineering significance.

### 2.3. Estimation of distribution algorithms

As effective and efficient learning-based paradigms within swarm intelligence and evolutionary computation, the recent emergence of EDAs has made crucial contributions to mitigating the building block breakage caused by classical crossover and mutation operators in GAs [58]. The crux of what makes EDAs work is that they can estimate and exploit promising patterns extracted from superior solutions. By formulating probability models and capturing crucial characteristics, EDAs accurately describe and reveal the distribution of building blocks, thus facilitating the detailed analysis and utilization of implicit relations in block structures. The excellent learning ability and good generalization capability of EDAs have triggered substantial studies, suggesting their promising prospects for solving various optimization problems [59]. Notably, recent years have witnessed their successful applications in addressing a variety of different scheduling problems. Jarbouri et al. [60] made the first attempt to address the PFSP by using a two-dimensional (2D) probability model-based EDA that aims to minimize the total flowtime. This 2D probability model focuses on the priority of job order and the presence of similar job blocks in selected superior solutions. Chen et al. [61] further investigated the convergence behavior of EDAs and provided guidelines for designing EDAs that take into account the effects of both intensification and diversification. Their adaptive EA/G demonstrated efficacy in minimizing earliness and tardiness for solving single machine scheduling problems. They claimed that EDAs can retain good structural features and converge faster than that of using genetic operators. Wang et al. [62] put forward an EDA-based memetic algorithm (EDAMA) to solve the distributed assembly permutation flow-shop scheduling problem (DAPFSP). In EDAMA, a problem-specific 2D probability model was built to describe the distribution of superior solutions in the search space, and EDA-based global exploration and critical-path-based local exploitation were integrated into the framework of EDAMA. Qian et al. [63] introduced a copula-based hybrid EDA (CHEDA) to solve the reentrant PFSP. In this approach, the copula theory was utilized to build a 2D probability model based on the joint distribution function to extract features from elite solutions. Shao et al. [14] proposed a pareto-based EDA (PEDA) for multi-objective DNFSP with SDSTs aimed at minimizing the criteria of makespan and total weight tardiness. In PEDA, three 2D probability models were developed to capture the characteristics of jobs in different scenarios. Recently, Zhao et al. [64] developed an EDA-based hyperheuristic (EDA-HH) for minimizing the makespan of distributed assembly mixed no-idle PFSP (DAMNIPFSP). The EDA-HH utilized EDA as a high-level strategy, adjusting low-level heuristics (LLHs) with a 2D probability model. This 2D probability model was used to record

inherent information in the sequences of LLHs, indicating the potential of EDAs in the field of hyper heuristics. Clearly, for EDAs, probability models are ideal carriers for capturing ordinal relations and learning block structures, providing the potential for significant breakthroughs in addressing the bottlenecks faced by traditional HIOAs. Most of the existing studies mainly focus on adopting 2D probability models to learn pattern information. Due to the inherent limitations in the model structure, they only accumulate the frequency of blocks, rather than accurately capturing the distribution of blocks implicit in sequential relationships. Recent efforts have been devoted to the development of more efficient learning-based paradigms and the design of effective probability models to enhance the efficacy of EDAs and extend their application scope in addressing the challenges of complex scheduling problems. Zhang et al. [37] pioneered the adoption of the matrix cube to learn information about blocks and their positions. Building on this innovation, they designed a multidimensional probability model with a specific sampling strategy to exactly estimate the distribution trend of promising patterns and guide the global search for seeking superior solutions. Experimental results showed that matrix-cube-based EDA (MCEDA) can yield favorable results with significant advantages. Following this pioneering work, MCEDA has been successfully applied to solve some shop scheduling problems, such as the EE_DAPFSP [38], the BFSP_SDSTs [39], and the NFSSP_SDSTs_RDs [20], with remarkable results. Motivated by these advancements, the above insights inspire this study to develop a knowledge-based enhanced estimation of distribution algorithm (EEDA) to address the DNFGSP_SDSTs, which has not been investigated to the best of the authors' knowledge.

## 3. Problem statement

### 3.1. Distributed no-wait flowshop sequence-dependent group scheduling problems

The DNFGSP_SDSTs can be briefly described as follows. There is a set of $F$ identical cellulars, each with a flowshop layout consisting of $m$ machines. A set of $S$ families is considered, where the family set is defined as $\Gamma=\left\{\Gamma_{1}, \Gamma_{2}, \ldots, \Gamma_{S}\right\}$ and each one includes $n_{k}$ jobs. Each family can be processed at any cellular and can be assigned to only one cellular. All jobs from the same family must be processed continuously without interruption and preemption. There is no wait time between successive operations of the same job. The sequence-dependent family setup time $s_{h, h, j}$ are considered when the changeover from family $\Gamma_{h}$ to the family $\Gamma_{h}$ takes place on the machine $M_{j}$. If $\Gamma_{h}$ is the first family on $M_{j}$, the initial setup time $s_{0, h, j}$ is required. Suppose that all machines are available at time 0 . Each machine can process at most one operation for each job at a time, and each job can be processed at most on one machine. (Tables 2 and 3)

### 3.1.1. MILP model of DNFGSP_SDSTs

$\min \left(C_{\max }(\pi)\right)$,
$C_{\max }(\pi)=\max \left\{C_{i, m}\right\}, \forall i$,
$\sum_{i=0, i \neq i}^{n} x_{i, j}=1, \forall i$,
$\sum_{i=0, i \neq i}^{n} x_{i, j}=1, \forall i$,
$\sum_{i=1}^{s} x_{i, 0}=\left\{\begin{array}{l}F, F \leq S \\ S, F>S\end{array}\right.$.

Table 2
Notations used in the model of DNFGSP_SDSTs.
Table 3
Notations used in the calculation of DNFGSP_SDSTs.

$\sum_{i=1}^{n} x_{0, i}=\left\{\begin{array}{l}F, F \leq S \\ S, F>S\end{array}\right.$,
$\sum_{j=0}^{n} \sum_{i=0}^{m} x_{i, j} \leq|\Psi|-1, \forall \Psi \subseteq J, i \neq i$,
$\sum_{i=0}^{m} \sum_{j=0}^{n} \sum_{i=n_{i}, j=1}^{m} x_{i, j}+\sum_{i=n_{i}+1}^{m} \sum_{j=n_{i}, j=1}^{n} x_{i, j}=1, \forall h$,
$y_{h, h}=\left\{\begin{array}{l}\sum_{i=n_{i}, j=1}^{n} \sum_{i=n_{i}, j=1}^{m} x_{i, j}, \forall h, h \wedge h \neq h \\ \sum_{i=n_{i}, j=1}^{n} x_{0, i}, h=0, \forall h \\ \sum_{i=n_{i}, j=1}^{n} x_{i, h}, \forall h, h=0\end{array}\right.$,

$C_{i j} \geq C_{i j-1}+p_{i j}, \forall i, j$,
$C_{i j} \geq C_{i j}+p_{i j}+\left(x_{i, i}-1\right) \cdot X, \forall j$,
$\forall i, i \in\left\{z_{h-1}+1, \ldots, z_{h}\right\} \wedge i \neq i, \forall h^{\prime}$
$C_{i j} \geq C_{i j}+p_{i j}+s_{k, h j}+\left(y_{i, i}-1\right) \cdot X, \forall j$
$i \in\left\{z_{h-1}+1, \ldots, z_{h}\right\} i \in\left\{z_{h-1}+1, \ldots, z_{h}\right\}, \forall h, h \wedge h \neq h^{\prime}$
$C_{i j} \geq C_{0, i}+s_{0, h, j}+p_{i j}+\left(y_{0, h}-1\right) \cdot X, \forall j$
$j=z_{h-1}+1, \ldots, z_{h}, \forall h$
$C_{i j}=C_{i j-1}+\sum_{k=1}^{n_{h}} I_{k, i} \cdot p_{i j}, \forall i, j$.
The objective function is shown in Eq. (1) and can be calculated by Eq. (2), Eq. (3) and Eq. (4) enforce that each position has only one immediate predecessor and successor, respectively. Eq. (5) and Eq. (6) ensure that the dummy job $J_{0}$ is an immediate successor and an immediate predecessor of the jobs in set $J$ with $\min (F, S)$ times. Subtours are eliminated by Eq. (7). Eq. (8) ensures the jobs from one family are never split up and combined with jobs from other families. The sequence relationship of two families is determined by the relationship of their jobs, which is considered by Eq. (9). The completion time of $O_{i j}$ must be larger than or equal to the completion time of its upstream $O_{i j-1}$ plus the processing time $p_{i j}$ for two successive operations of $J_{i}$, as shown in Eq. (10). Note that $C_{i, 0}=0$ and $C_{0, i}=0$. The completion time of $O_{i j}$ for $J_{i}$ and its immediate predecessor $J_{i}$ on $M_{j}$ must not be less than the sum of $p_{i j}$ and the completion time of $O_{i, j}$, shown in Eq. (11); otherwise, if the two are distinct from one another and come from $\Gamma_{h}$ and $\Gamma_{S}, s_{k, h, j}$ must be added to the computation of the completion time of $O_{i j}$, as enforced by Eq. (12). Eq. (13) determines the initial setup time $s_{0, h, j}$ is taken into consideration for the first family of jobs processed on $M_{j}$. Eq. (14) ensures that the different processes of the same job must be continuous, which satisfies the no-wait constraint.

### 3.1.2. Encoding and decoding schemes

The effective encoding and decoding schemes can reasonably reflect the crucial characteristics and critical constraints for complex and coupled problems [65]. The considered DNFGSP_SDSTs is composed of two subproblems: the cellular assignment for each family and the processing sequence for all jobs. Thus, a two-segment encoding scheme is designed to describe feasible solutions, which is denoted as $\boldsymbol{\pi}=\left[\boldsymbol{\pi}^{C}, \boldsymbol{\pi}^{F}\right]$. The first segment $\boldsymbol{\pi}^{C}$ represents the family sequence in cellular, i.e., $\boldsymbol{\pi}^{C}=$ $\left[\left(\Gamma_{1}^{1}, \ldots, \Gamma_{d_{1}}^{1}\right), \ldots,\left(\Gamma_{1}^{d}, \ldots, \Gamma_{d_{h}}^{F}\right)\right]$, and the second segment $\boldsymbol{\pi}^{F}$ represents the job sequence in family, i.e., $\boldsymbol{\pi}^{F}=\left[\left(\Gamma_{1}(1), \ldots, \Gamma_{1}\left(n_{1}\right)\right), \ldots,\left(\Gamma_{2}(1), \ldots, \Gamma_{2}\left(n_{2}\right)\right)\right]$. The representation of a feasible solution $\boldsymbol{\pi}$ is shown in Fig. 1. It is clear that $\Gamma_{1}$ and $\Gamma_{2}$ are assigned to $U_{1}$ and $\Gamma_{2}$ is allocated to $U_{2}$. The job sequence of families $\Gamma_{1}, \Gamma_{2}$, and $\Gamma_{3}$ is $\left(J_{1}, J_{2}, J_{3}\right),\left(J_{4}\right)$, and $\left(J_{5}, J_{6}\right)$, respectively.

For the decoding scheme of DNFGSP_SDSTs, $M L_{h, h, j}$ can be calculated by Eq. (15). $D_{h, i, i+1}$ is the difference of the completion time between
![img-0.jpeg](img-0.jpeg)

Fig. 1. The representation of a feasible solution $\boldsymbol{\pi}$.
adjacent jobs, which can be calculated by Eq. (16). $C_{\max }(\boldsymbol{\pi})$ can be calculated by Eq. (17). The Gantt chart of an example with $S=2, n=4$, and $m=3$ is provided in Fig. 2.
$M L_{h, h, j}=\left\{\begin{array}{l}\max \left\{s_{k, h, 1}+p_{i, 1}-p_{i-1,2}, s_{k, h, 2}\right\}+p_{i, 2}, j=2 \\ \max \left\{M L_{h, h, j-1}-p_{i, j}, s_{k, j, i}\right\}+p_{i, j}, j=3, \ldots, m\end{array}, \forall i, \forall h, h^{\prime}\right.$,
$D_{h, i, i+1}=\max _{h=1,2, \ldots, n}\left\{\sum_{k=2}^{n_{h}}\left(p_{i+1,1}-p_{i, 1}\right)+p_{i, h}\right\}, i=1,2, \ldots, n_{h}-1, h$
$=1,2, \ldots, S$,
$C_{\max }(\boldsymbol{\pi})=\sum_{h=1}^{S} M L_{h-1, h, m}+\sum_{h=1}^{S} \sum_{i=1}^{n_{h}-1} D_{h, i, i+1}$.

### 3.1.3. Example instance

Considering 4 families, 8 jobs, 3 machines, and 2 cellulars, an example is given in this subsection. Four families are denoted as $\Gamma_{1}=$ $\left(J_{1}, J_{2}, J_{3}\right), \Gamma_{2}=\left(J_{4}\right), \Gamma_{3}=\left(J_{5}, J_{6}\right)$, and $\Gamma_{4}=\left(J_{7}, J_{8}\right)$. Two cellulars are represented as $U_{1}=\left[\left(J_{1}, J_{2}, J_{3}\right),\left(J_{4}\right)\right]$ and $U_{2}=\left[\left(J_{5}, J_{6}\right),\left(J_{7}, J_{8}\right)\right]$, respectively. Thus, the feasible solution can be represented as $\boldsymbol{\pi}_{0}=\left[\left(\left(J_{1}\right.\right.\right.$, $\left.J_{2}, J_{3}\right),\left(J_{4}\right)\right],\left[\left(J_{5}, J_{6}\right),\left(J_{7}, J_{8}\right)\right]$ ]. The job processing time and family sequence-dependence setup time are given in Tables 4 and 5 , respectively. The corresponding Gantt chart of a feasible scheduling solution $\boldsymbol{\pi}_{0}$ is shown in Fig. 3.

### 3.2. Analysis of problem properties

To reduce the computational complexity (CC) and enhance efficiency, it is of great importance to analyze the problem properties and design effective speed-up evaluation methods to accelerate the calculation while executing some search operators [20]. To the best of our knowledge, the speed-up evaluation methods devised for DNFGSPs are still scarce. Therefore, in this section, we derive five problem-specific properties as knowledge to aid in the design of five speed-up evaluation methods.

Property 1. For a feasible solution $\boldsymbol{\pi}$, randomly select family $\Gamma_{a}$ in cellular $f$ and family $\Gamma_{b}$ in cellular $f \mid f \neq f$ and each cellular has $m$ machines) from $\boldsymbol{\pi}^{C}$. Next, swap the positions of two families $\Gamma_{a}$ and $\Gamma_{b}$ in $\boldsymbol{\pi}^{C}$. After performing this swap operator, a new solution $\boldsymbol{\pi}$ is obtained. The CC of calculating $C_{\max }(\boldsymbol{\pi})$ can be reduced from $O(n \times m)$ to $O(m)$.

Proof. Assuming that there are $S_{f}$ and $S_{f}$ families assigned to cellulars $f$ and $f$, respectively. According to Eqs. (15)-(17), $C_{\max }^{\prime}(\boldsymbol{\pi})$ and $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be calculated by Eq. (18). When families $\Gamma_{a}$ and $\Gamma_{b}(a=1, \ldots$, $\left.S_{f}, b=1, \ldots, S_{f}\right)$ are chosen from cellulars $f$ and $f$, respectively, $C_{\max }^{\prime}(\boldsymbol{\pi})$ and $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be further represented as shown in Eq. (19). After swapping two families $\Gamma_{a}$ and $\Gamma_{b}, C_{\max }^{\prime}(\boldsymbol{\pi})$ and $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be calculated by Eq. (20). Then, the completion time differences $\Delta t_{f}$ and $\Delta t_{f}$ in cellulars $f$ and $f$ can be calculated by using Eq. (21). As shown in Eqs. (19) (20), $\sum_{h=1}^{m} M L_{h-1, h, m}, \sum_{h=1}^{m} \sum_{i=1}^{n_{h}-1} D_{h, i, i+1}$ in front of $\Gamma_{a}$ and $\sum_{h=a+2}^{d_{h}} M L_{h-1, h, m}, \sum_{h=a+1}^{d_{h}} \sum_{i=1}^{n_{h}-1} D_{h, i, i+1}$ behind $\Gamma_{a}$ in cellular $f$ are not changed after swapping families $\Gamma_{a}$ and $\Gamma_{b}$. Thus, $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be calculated as Eq. (21), and the same derivations can be applied to $C_{\max }^{\prime}(\boldsymbol{\pi})$. Based on Eqs. (19)-(22), the CC of calculating $C_{\max }(\boldsymbol{\pi})$ can be reduced from $O(n \times m)$ to $O(m)$.
$\left\{\begin{array}{l}C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{h=1}^{S_{f}} M L_{h-1, h, m}+\sum_{h=1}^{S_{f}} \sum_{i=1}^{n_{h}-1} D_{h, i, i+1} \\ C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{h=1}^{S_{f}} M L_{h-1, h, m}+\sum_{h=1}^{S_{f}} \sum_{i=1}^{n_{h}-1} D_{h, i, i+1}\end{array}\right.$

![img-3.jpeg](img-3.jpeg)

Fig. 2. Gantt chart of an example.

Table 4
Processing time of jobs on machines.

Table 5
Sequence-dependence setup time of families on machines.
![img-3.jpeg](img-3.jpeg)

$$
C_{\max }^{\prime}(\boldsymbol{x})=\sum_{b=1}^{n_{1}} M L_{b-1, b, m}+\sum_{b=a+1}^{b_{2}} M L_{b-1, b, m}+M L_{a-1, a, m}+M L_{a, a+1, m}+
$$

$$
\sum_{b=1}^{a} \sum_{i=1}^{n_{b}-1} D_{b, i, i+1}+\sum_{b=a+1}^{b_{2}} \sum_{i=1}^{n_{b}-1} D_{b, i, i+1}+\sum_{i=1}^{n_{b}-1} D_{b, i, i+1}
$$

$C_{\max }^{\prime}(\boldsymbol{x})=\sum_{b=1}^{n_{1}} M L_{b-1, b, m}+\sum_{b=b+2}^{b_{2}} M L_{b-1, b, m}+M L_{b-1, b, m}+M L_{a, b+1, m}+$

$$
\sum_{b=1}^{b} \sum_{i=1}^{n_{b}-1} D_{b, i, i+1}+\sum_{b=a+1}^{b_{2}} \sum_{i=1}^{n_{b}-1} D_{b, i, i+1}+\sum_{i=1}^{n_{b}-1} D_{b, i, i+1}
$$

For ease of understanding, an intuitive example is provided in Fig. 4. As illustrated in Fig. 4(a), families $\Gamma_{3}$ and $\Gamma_{2}$ are assigned to cellular $f_{2}$ and $f_{1}$, respectively. From Fig. 4(b), after swapping the positions of $\Gamma_{3}$ and $\Gamma_{2}$, it can be concluded that the processing time of $\Gamma_{1}$ before $\Gamma_{3}$ in cellular 1 is not affected, while only $M L_{2,4,3}$ is changed to $M L_{2,4,3}$ in the calculation of processing time after $\Gamma_{2}$ in cellular 2 .

Property 2. For a feasible solution $\boldsymbol{x}$, randomly select family $\Gamma_{n}$ in
![img-3.jpeg](img-3.jpeg)

Fig. 3. Gantt chart of a feasible scheduling solution $\boldsymbol{x}_{0}$.

![img-4.jpeg](img-4.jpeg)
(a) Gantt chart of $\boldsymbol{\pi}$.
![img-5.jpeg](img-5.jpeg)
(b) Gantt chart after swapping $\Gamma_{2}$ and $\Gamma_{3}$.
![img-6.jpeg](img-6.jpeg)

Fig. 4. Illustration of Property 1 and Property 2.

![img-7.jpeg](img-7.jpeg)
(c) Gantt chart after inserting $\Gamma_{3}$ in front of $\Gamma_{1}$.

Fig. 5. Illustration of Property 3 and Property 4.
cellular $f$ and family $\Gamma_{b}$ in cellular $f(f \neq f$ and each cellular has $M$ machines) from $\boldsymbol{x}^{C}$. Next, insert $\Gamma_{b}$ in front of $\Gamma_{a}$ in $\boldsymbol{x}^{C}$. After performing this insert operator, a new solution $\boldsymbol{x}$ is obtained. The CC of calculating $C_{\max }(\boldsymbol{x})$ can be reduced from $O(n \times m)$ to $O(m)$.

Proof. Assuming that $S_{f}$ and $S_{f}$ families are assigned to cellulars $f$ and $f$, respectively. According to Eqs. (15)-(17), $C_{\max }^{\prime}(\boldsymbol{x})$ and $C_{\max }^{\prime}(\boldsymbol{x})$ can
reduced from $O(n \times m)$ to $O(m)$ based on Eqs. (24)-(27).

$$
\left\{\begin{array}{l}
C_{\max }^{\prime}(\boldsymbol{x})=\sum_{b-1}^{s_{f}} M L_{b-1, b, m}+\sum_{b-1}^{s_{f}} \sum_{a-1}^{m-1} D_{b, i, i+1} \\
C_{\max }^{\prime}(\boldsymbol{x})=\sum_{b-1}^{s_{f}} M L_{b-1, b, m}+\sum_{b-1}^{s_{f}} \sum_{a-1}^{m-1} D_{b, i, i+1}
\end{array}\right.
$$

be calculated by Eq. (23). When families $\Gamma_{a}$ and $\Gamma_{b}(a=1, \ldots, S_{f}, b=1, \ldots$, $S_{f}$ ) are chosen from cellulars $f$ and $f$, respectively, $C_{\max }^{\prime}(\boldsymbol{x})$ and $C_{\max }^{\prime}(\boldsymbol{x})$ can be further represented as Eq. (24). After inserting family $\Gamma_{b}$ in front of $\Gamma_{a}$ in $\boldsymbol{x}^{C}, C_{\max }^{\prime}(\boldsymbol{x})$ and $C_{\max }^{\prime}(\boldsymbol{x})$ can be calculated by Eq. (25). The completion time differences $\alpha t_{f}$ and $\alpha t_{f}$ in cellulars $f$ and $f$ are obtained by Eq. (26). As shown in Eqs. (24)-(25), $\sum_{b-1}^{a} M L_{b-1, b, m}$ in front of $\Gamma_{a}$, $\sum_{b-a+1}^{b} M L_{b-1, b, m}$ behind $\Gamma_{a}$, and $\sum_{b-1}^{s_{f}} \sum_{a-1}^{m-1} D_{b, i, i+1}$ in cellular $f$ are not changed after inserting $\Gamma_{b}$. While $\sum_{b-1}^{a} M L_{b-1, b, m}, \sum_{b-1}^{b} \sum_{a-1}^{m-1} D_{b, i, i+1}$ in front of $\Gamma_{b}$ and $\sum_{b-b+2}^{s_{f}} M L_{b-1, b, m}, \sum_{b-b+1}^{s_{f}} \sum_{a-1}^{m-1} D_{b, i, i+1}$ behind $\Gamma_{b}$ in cellular are also not changed after extracting $\Gamma_{b}, C_{\max }^{\prime}(\boldsymbol{x})$ and $C_{\max }^{\prime}(\boldsymbol{x})$ can be calculated as Eq. (26). Thus, the CC of calculating $C_{\max }(\boldsymbol{x})$ can be
![img-8.jpeg](img-8.jpeg)

$$
\begin{aligned}
& \Delta t_{f}=C_{\max }^{\prime}(\boldsymbol{\pi})-C_{\max }^{\prime}(\boldsymbol{\pi})=M L_{n-1, b, m}+M L_{0, a, m}+\sum_{i=1}^{n_{0}-1} D_{h, i, i+1}-M L_{n-1, a, m} \\
& \Delta t_{f}=C_{\max }^{\prime}(\boldsymbol{\pi})-C_{\max }^{\prime}(\boldsymbol{\pi})=M L_{h-1, b+1, m}-M L_{h-1, b, m}-M L_{0, b+1, m}-\sum_{i=1}^{n_{0}-1} D_{h, i, i+1}
\end{aligned}
$$

$C_{\max }(\boldsymbol{\pi})=\max \left(C_{\max }^{\prime}(\boldsymbol{\pi})+\Delta t_{f}, C_{\max }^{\prime}(\boldsymbol{\pi})+\Delta t_{f}\right)$.
As shown in Fig. 4(c), after extracting $\Gamma_{3}$ and inserting it into the

$$
C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{h=1}^{N_{3}} M L_{h-1, b, m}+\sum_{h=1}^{N_{3}} \sum_{i=1}^{n_{0}-1} D_{h, i, i+1}
$$

$$
\left\{\begin{array}{l}
C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{h=1}^{N_{3}} M L_{h-1, b, m}+\sum_{h=1}^{N_{3}} \sum_{i=1}^{n_{0}-1} D_{h, i, i+1} \\
\left\{\begin{array}{l}
C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{h=1}^{N_{3}} M L_{h-1, b, m}+\sum_{h=1}^{N_{3}} \sum_{i=1}^{n_{0}-1} D_{h, i, i+1} \\
M L_{n-1, a, m}+M L_{a, a+1, m}+M L_{h-1, b, m}+M L_{a, b+1, m}+\sum_{h=1}^{N_{0}} \sum_{i=1}^{n_{0}-1} D_{h, i, i+1}, \Gamma_{a} \neq \Gamma_{b-1} \\
C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{h=1}^{N_{3}} M L_{h-1, b, m}+\sum_{h=1}^{N_{3}} M L_{h-1, b, m}+M L_{a, b, m}+ \\
M L_{n-1, a, m}+M L_{a, b+1, m}+\sum_{h=1}^{N_{0}} \sum_{i=1}^{n_{0}-1} D_{h, i, i+1}, \Gamma_{a}=\Gamma_{b-1}
\end{array}\right.
$$

$$
\begin{aligned}
& C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{h=1}^{N_{3}} M L_{h-1, b, m}+\sum_{h=1}^{N_{3}} \sum_{i=1}^{N_{0}-1} M L_{h-1, b, m}+\sum_{h=1}^{N_{0}} M L_{h-1, b, m}+ \\
& M L_{n-1, b, m}+M L_{a, a+1, m}+M L_{h-1, a, m}+M L_{a, b+1, m}+\sum_{h=1}^{N_{0}} \sum_{i=1}^{n_{0}-1} D_{h, i, i+1}, \Gamma_{a} \neq \Gamma_{b-1} \\
& C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{h=1}^{N_{3}} M L_{h-1, b, m}+\sum_{h=1}^{N_{0}} M L_{h-1, b, m}+M L_{n-1, b, m}+ \\
& M L_{0, a, m}+M L_{a, b+1, m}+\sum_{h=1}^{N_{0}} \sum_{i=1}^{n_{0}-1} D_{h, i, i+1}, \Gamma_{a}=\Gamma_{b-1}
\end{aligned}
$$

position in front of $\Gamma_{2}$, the processing time before $\Gamma_{3}$ is not affected, and only $M L_{1,2,3}$ changes to $M L_{3,2,3}$ in the calculation of processing time after $\Gamma_{3}$ in cellular 1. Meanwhile, for cellular 2, only $M L_{3,4,5}$ changes to $M L_{0,4,3}$ in the calculation of the processing time after the extracting position of $\Gamma_{3}$.

Property 3. For a feasible solution $\boldsymbol{\pi}$, randomly select two families $\Gamma_{a}$ and $\Gamma_{b}(b>a)$ in cellular $f$ with $m$ machines from $\boldsymbol{\pi}^{C}$. Next, swap the positions of $\Gamma_{a}$ and $\Gamma_{b}$ in $\boldsymbol{\pi}^{C}$. After performing this swap operator, a new solution $\boldsymbol{\pi}$ is obtained. The CC of calculating $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be reduced from $O\left(n^{f} \times m\right)$ to $O(m)$.

Proof. Assuming that $S_{f}$ families are assigned to cellular $f$. According to Eqs. (15)-(17), $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be calculated by Eq. (28). When families $\Gamma_{a}$ and $\Gamma_{b}\left(a=1, \ldots, S_{f}, b=2, \ldots, S_{f}, b>a\right)$ are chosen from cellular $f$, $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be further represented as Eq. (29), where the case of $\Gamma_{a}=$ $\Gamma_{b-1}$ is also considered. After swapping two families $\Gamma_{a}$ and $\Gamma_{b}, C_{\max }^{\prime}(\boldsymbol{\pi})$ can be calculated by Eq. (30). Then, the completion time differences $\Delta t_{f}$ in cellular $f$ can be calculated by Eq. (31). As shown in Eqs. (29)-(30), if $\Gamma_{a} \neq \Gamma_{b-1}, \sum_{h=1}^{N_{3}} M L_{h-1, b, m}$ in front of $\Gamma_{a}, \sum_{h=b+2}^{N_{0}} M L_{h-1, b, m}$ behind $\Gamma_{b}$, and $\sum_{h=a+2}^{b-1} M L_{h-1, b, m}$ between two families in cellular $f$ are not changed after swapping families $\Gamma_{a}$ and $\Gamma_{b}, C_{\max }^{\prime}(\boldsymbol{\pi})$ can be calculated as Eq. (31) and similar derivations can be applied to $\Gamma_{a}=\Gamma_{b-1}$. Thus, the CC of calculating $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be reduced from $O\left(n^{f} \times m\right)$ to $O(m)$ by using Eqs. (29)-(32).

$$
\begin{aligned}
\Delta t_{f} & =C_{\max }^{\prime}(\boldsymbol{\pi})-C_{\max }^{\prime}(\boldsymbol{\pi}) \\
& =\left\{\begin{array}{l}
M L_{n-1, b, m}+M L_{0, a+1, m}+M L_{h-1, a, m}+M L_{a, b+1, m}- \\
M L_{n-1, a, m}-M L_{a, a+1, m}-M L_{h-1, b, m}-M L_{a, b+1, m}, \Gamma_{a} \neq \Gamma_{b-1} \\
C_{\max }^{\prime}(\boldsymbol{\pi})=M L_{n-1, b, m}+M L_{0, a, m}+M L_{a, b+1, m}- \\
M L_{a, b, m}-M L_{n-1, a, m}-M L_{0, b+1, m}, \Gamma_{a}=\Gamma_{b-1}
\end{array}\right.
$$

$C_{\max }^{\prime}(\boldsymbol{\pi})=C_{\max }^{\prime}(\boldsymbol{\pi})+\Delta t_{f}$.
Property 4. For a feasible solution $\boldsymbol{\pi}$, randomly select two families $\Gamma_{a}$ and $\Gamma_{b}$ in cellular $f$ with $m$ machines. Next, insert $\Gamma_{b}$ in front of $\Gamma_{a}$ in $\boldsymbol{\pi}^{C}$. After performing this insertion, a new solution $\boldsymbol{\pi}$ is obtained. The CC of calculating $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be reduced from $O\left(n^{f} \times m\right)$ to $O(m)$.

Proof. Assuming that $S_{f}$ families are assigned to cellular $f$. According to Eqs. (15)-(17), $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be calculated by Eq. (33). When families $\Gamma_{a}$ and $\Gamma_{b}\left(a=1, \ldots, S_{f}, b=2, \ldots, S_{f}, b>a\right)$ are chosen from cellular $f$, $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be further represented as Eq. (34). After inserting $\Gamma_{b}$ in front of $\Gamma_{a}, C_{\max }^{\prime}(\boldsymbol{\pi})$ can be calculated by Eq. (35). Then, the completion time differences $\Delta t_{f}$ in cellular $f$ can be calculated by using Eq. (36). As shown in Eqs. (34)-(35), $\sum_{h=1}^{N_{3}} M L_{h-1, b, m}$ in front of $\Gamma_{a}, \sum_{h=b+2}^{N_{0}} M L_{h-1, b, m}$ behind $\Gamma_{b}$, and $\sum_{h=a+1}^{b-1} M L_{h-1, b, m}$ between two families in cellular $f$ are not changed after inserting $\Gamma_{b}$. Next, $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be calculated as Eq. (36).

According to Eqs. (34)-(37), the CC of calculating $C_{\max }^{\prime}(\boldsymbol{\pi})$ can be reduced from $O(\boldsymbol{n} \mid \times \boldsymbol{m})$ to $O(\boldsymbol{n})$.
$C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{n=1}^{N_{1}} M L_{n-1, b, m}+\sum_{n=1}^{N_{2}} \sum_{i=1}^{n_{k}-1} D_{h, i, i+1}$,
$C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{n=1}^{i-1} M L_{n-1, b, m}+\sum_{n=i+1}^{k-1} M L_{n-1, b, m}+\sum_{n=k+2}^{N_{k}} M L_{n-1, b, m}+$
$M L_{n-1, b, m}+M L_{n-1, b, m}+M L_{n, k+1, m}+\sum_{n=1}^{N_{k}} \sum_{i=1}^{n_{k}-1} D_{h, i, i+1}$
shown in Eqs. (39)-(40), after inserting $J_{i}$ in front of $J_{n}$, if $i=1 \wedge i=2$, $\ldots, n_{k}-1, \sum_{i=1}^{i-2} D_{h, t, t+1}$ are not changed; if $i=2, \ldots, n_{k}-1 \wedge i=n_{k}$, $\sum_{t=i}^{i-2} D_{h, t, t+1}, \sum_{t=1}^{i-2} D_{h, t, t+1}$ are not changed; if $i=1 \wedge i=n_{k}, \sum_{t=i}^{i-2} D_{h, t, t+1}$ are not changed; else, $\sum_{t=1}^{i-2} D_{h, t, t+1}, \sum_{t=i}^{i-1} D_{h, t, t+1}, \sum_{t=i+1}^{n_{k}-1} D_{h, t, t+1}$ are not changed. Next, $T_{h}$ can be calculated as Eq. (42). According to Eqs. (39)-(42), the CC of calculating $T_{h}$ can be reduced from $O\left(n_{h} \times m\right)$ to $O(m)$.
$T_{h}=M L_{h-1, b, m}+\sum_{t=1}^{n_{h}-1} D_{h, t, t+1}$,
$T_{h}=\left\{\begin{array}{l}\sum_{t=1}^{i-2} D_{h, t, t+1}+M L_{h-1, b, m}+D_{h, i-1, i}+D_{h, i, i+1}, i=1 \wedge i=2, \ldots, n_{h}-1 \\ \sum_{t=1}^{i-2} D_{h, t, t+1}+\sum_{t=1}^{i-2} D_{h, t, t+1}+D_{h, i-1, i}+D_{h, i-1, i}+M L_{h, k+1, m}, i=2, \ldots, n_{h}-1 \wedge i=n_{k} \\ \sum_{t=1}^{i-2} D_{h, t, t+1}+M L_{h-1, b, m}+D_{h, i-1, i}+M L_{h, k+1, m}, i=1 \wedge i=n_{k} \\ \sum_{t=1}^{i-2} D_{h, t, t+1}+\sum_{t=1}^{i-2} D_{h, t, t+1}+\sum_{t=i+1}^{n_{k}-1} D_{h, t, t+1}+D_{h, i-1, i}+D_{h, i, i}+D_{h, i-1, i+1}, \text { otherwise }\end{array}\right.$,
$T_{h}=\left\{\begin{array}{l}M L_{h-1, b, m}+D_{h, i, i}+D_{h, i-1, i+1}+\sum_{t=i}^{i-2} D_{h, t, t+1}, i=1 \wedge i=2, \ldots, n_{h}-1 \\ \sum_{t=1}^{i-2} D_{h, t, t+1}+\sum_{t=1}^{i-2} D_{h, t, t+1} D_{h, i-1, i}+D_{h, i, i}+M L_{h, k+1, m}, i=1, \ldots, n_{h}-1 \wedge i=n_{k} \\ \sum_{t=1}^{i-2} D_{h, t, t+1}+M L_{h-1, b, m}+D_{h, i, i}+M L_{h, k+1, m}, i=1 \wedge i=n_{k} \\ \sum_{t=1}^{i-2} D_{h, t, t+1}+\sum_{t=1}^{i-2} D_{h, t, t+1}+\sum_{t=i+1}^{n_{k}-1} D_{h, t, t+1}+D_{h, i-1, i}+D_{h, i, i}+D_{h, i-1, i+1}, \text { otherwise }\end{array}\right.$,
$C_{\max }^{\prime}(\boldsymbol{\pi})=\sum_{n=1}^{n-1} M L_{n-1, b, m}+\sum_{n=i+1}^{k-1} M L_{n-1, b, m}+\sum_{n=k+2}^{N_{k}} M L_{n-1, b, m}+$
$M L_{n-1, b, m}+M L_{h, a, m}+M L_{h-1, k+1, m}+\sum_{n=1}^{N_{k}} \sum_{i=1}^{n_{k}-1} D_{h, t, t+1}$
$\Delta I_{f}=C_{\text {min }}^{\prime}(\boldsymbol{\pi})-C_{\text {min }}^{\prime}(\boldsymbol{\pi})=M L_{n-1, b, m}+M L_{h, a, m}+M L_{h-1, k+1, m}-$
$M L_{n-1, a, m}-M L_{h-1, b, m}-M L_{h, k+1, m}$
$C_{\text {min }}^{\prime}(\boldsymbol{\pi})=C_{\text {min }}^{\prime}(\boldsymbol{\pi})+\Delta I_{f}$
As shown in Fig. 5, a feasible solution $\boldsymbol{\pi}_{1}=\left[\left(J_{1}, J_{2}, J_{3}\right),\left(J_{4}\right),\left(J_{5}, J_{6}\right)\right.$, $\left.\left(J_{7}, J_{8}\right)\right]$ is used as an example to explain Property 3 and Property 4. In Fig. 5(b), after swapping the positions of $\Gamma_{1}$ and $\Gamma_{3}$, only $M L_{1,2,3}$ changes to $M L_{0,2,3}$ between $\Gamma_{1}$ and $\Gamma_{3}$, and the calculation of processing time after $\Gamma_{1}$ only has changed $M L_{0,4,3}$ to $M L_{1,4,3}$. In Fig. 5(c), after inserting family $\Gamma_{3}$, only $M L_{0,1,3}$ changes to $M L_{0,1,3}$ in the calculation of processing time after the family $\Gamma_{3}$, and the calculation of the processing time after the extracting position of $\Gamma_{3}$ only changes $M L_{0,4,3}$ to $M L_{0,4,3}$.

Property 5. For a feasible solution $\boldsymbol{\pi}$, randomly select two jobs $J_{i}$ and $J_{i}$ from family $\Gamma_{h}$. Next, insert $J_{i}$ to the position in front of $J_{i}$ in $\boldsymbol{\pi}^{E}$. After performing such an insert operator, a new $\boldsymbol{\pi}$ is obtained. The calculation of $T_{h}$ can be reduced from $O\left(n_{h} \times m\right)$ to $O(m)$.

Proof. Assuming that $n_{h}\left(n_{h}>2\right)$ jobs in $\Gamma_{h}(h=1, \ldots, S)$. According to Eqs. (15)-(17), $T_{h}$ can be calculated by Eq. (38). When jobs $J_{i}$ and $J_{i}(i$ $=1, \ldots, n_{h}-1, i=2, \ldots, n_{h}, i>i)$ are chosen from cellular $f, T_{h}$ can be further represented as Eq. (39), where four cases are also considered. As

$$
\Delta T_{h}=T_{h}-T_{h}=\left\{\begin{array}{l}
M L_{h-1, b, m}+D_{h, i, i}+D_{h, i-1, i+1}-M L_{h-1, b, m}-D_{h, i-1, i}- \\
D_{h, i, i+1}, i=1 \wedge i=2, \ldots, n_{h}-1 \\
D_{h, i-1, i}+D_{h, i, i}+M L_{h, k+1, m}-D_{h, i-1, i}-D_{h, i-1, i}- \\
M L_{h, k+1, m}, i=1, \ldots, n_{h}-1 \wedge i=n_{k} \\
M L_{h-1, b, m}+D_{h, i, i}+M L_{h, k+1, m}-M L_{h-1, b, m}-D_{h, i-1, i}- \\
M L_{h, k+1, m}, i=1 \wedge i=n_{k} \\
D_{h, i-1, i}+D_{h, i, i}+D_{h, i-1, i+1}-D_{h, i-1, i}-D_{h, i-1, i}- \\
D_{h, i, i+1}, \text { otherwise }
\end{array}\right.
$$

$T_{h}=T_{h}+\Delta T_{h}$
As shown in Fig. 6, a feasible solution $\boldsymbol{\pi}_{2}=\left[\left(J_{1}, J_{2}, J_{3}, J_{4}, J_{5}, J_{6}\right), \ldots\right.$, $\left.\left(J_{n-n_{k}}, \ldots, J_{n}\right)\right]$ is used as an example to explain Property 5. After performing the insertion, $M L_{0,1,3}, D_{1,2,3}, D_{1,3,4}$ and the calculation of processing time after $\Gamma_{1}$ are not affected, while $D_{1,1,2}, D_{1,4,5}, D_{1,5,6}$ has changed to $D_{1,1,5}, D_{1,4,6}, D_{1,4,6}$.

According to these properties, the CC for evaluating the solution can be significantly reduced. In addition, for the subsequent SubSections 4.3.1-4.3.3, the makespan of the newly generated solution can be quickly calculated by using these speed-up evaluation methods based on problem-specific properties after performing the local search operations.

![img-9.jpeg](img-9.jpeg)
(b) Gantt chart after inserting $J_{5}$ in front of $J_{2}$.

Fig. 6. Illustration of Property 5.

# 4. EEDA for DNFGSP_SDSTs 

In this section, the knowledge-enhanced EDA for solving DNFGSP_SDSTs is described in detail. First, the hybrid initialization method, the EEDA-based global search, and three local search operators are proposed. Then, the perturbation and reinitialization methods are presented. Next, the computational complexity of the critical components of EEDA is analyzed. Finally, the framework of EEDA is given. The illustration of EEDA for DNFGSP_SDSTs is described in Fig. 7. Some necessary notations used in EEDA are listed in Table 6.

### 4.1. Initialization method

Insight into previous work, high-quality initialization solutions are crucial for the speed, diversity, stability, and efficiency of HIOAs. To generate an excellent initial population with a certain diversity, two

Table 6
Notations used in EEDA.

![img-10.jpeg](img-10.jpeg)

Fig. 7. Illustration of EEDA for DNFGSP_SDSTs.

```
Randomly generate \(\boldsymbol{\pi}^{C}=\left[\left(\Gamma_{1}(1), \ldots, \Gamma_{l}\left(n_{1}\right)\right), \ldots,\left(\Gamma_{S}(1), \ldots, \Gamma_{S}\left(n_{S}\right)\right)\right]\). //Firststage
for \(t=1\) to \(S\) do
    Sort jobs within family according to descending \(s p_{t} \rightarrow \Gamma_{t}=\left(\Gamma_{t}(1), \ldots, \Gamma_{t}\left(n_{t}\right)\right)\).
    Extract all jobs within \(\Gamma_{t}\).
    for \(t=1\) to \(n_{t}\) do
    1. Test \(\Gamma_{t}(l)\) in all the possible positions within \(\Gamma_{t}$.
    Insert \(\Gamma_{t}(l)\) in the position within \(\Gamma_{t}\) resulting in the minimum \(p_{\Gamma_{t}}\).
    end for
    end for
    Get the improved job sequence \(\boldsymbol{\pi}^{C}=\left[\left(\Gamma_{1}^{\prime}(1), \ldots, \Gamma_{l}^{\prime}\left(n_{1}\right)\right), \ldots,\left(\Gamma_{S}^{\prime}(1), \ldots, \Gamma_{S}^{\prime}\left(n_{S}\right)\right)\right]\).
    Sort families according to descending \(p_{\Gamma_{t}} \rightarrow \Gamma=\left[\Gamma_{0}^{\prime}, \Gamma_{1}^{\prime}, \ldots, \Gamma_{0}^{\prime}\right]\). //Secondstage
for \(t=1\) to \(S\) do
    for \(v=1\) to \(F\) do
    Test family \(\Gamma_{t}\) in all the possible positions in \(\boldsymbol{\pi}^{C}\).
    \(\operatorname{Pos} \leftarrow\) The position in \(\boldsymbol{\pi}^{C}\) resulting in the minimum \(C_{\max }\).
    end for
    Insert \(\Gamma_{t}\) in position Pos in \(\boldsymbol{\pi}^{C}\).
    end for
Output: A complete solution \(\boldsymbol{\pi}=\left[\boldsymbol{\pi}^{C}, \boldsymbol{\pi}^{Z}\right]$.
```

Algorithm 2
B-NEH.
![img-11.jpeg](img-11.jpeg)

Fig. 8. Illustration of the probability model $P M^{G}$.

![img-12.jpeg](img-12.jpeg)

Fig. 9. Illustration of the updating mechanism for $R M^{G}$.
problem-specific heuristics are introduced in this section. When addressing DNFGSP_SDSTs, determining both the family sequence $\boldsymbol{\pi}^{C}$ and the job sequence $\boldsymbol{\pi}^{E}$ for each solution $\boldsymbol{\pi}$ in the population $\operatorname{Pop}(G)$ is essential. Inspired by the constructive heuristics proposed in Ref. [66], we develop a two-stage heuristic based on NEH (TS-NEH) and a random heuristic based on NEH (R-NEH). TS-NEH primarily aims at refining the job orders of the families and reducing the completion time of the cellulars, while R-NEH is devised to ensure population diversity. In TS-NEH, the LPT rule [66] is adopted in the first stage to obtain initial job sequences for families. Then, the NEH rule is applied to further fine-tune these partial job sequences with the aim of minimizing the completion time of each family. Based on these partial job sequences, the total job sequence $\boldsymbol{\pi}^{E}$ is generated. In the second stage, the total processing time of each family is calculated separately and the initial family sequence $\Gamma$ is generated using the LPT rule. Then, the NEH rule is applied on initial family sequence $\Gamma$ to obtain to obtain the final family sequence $\boldsymbol{\pi}^{C}$. This process results in generating a high-quality initial solution $\boldsymbol{\pi}=\left[\boldsymbol{\pi}^{C} \cdot \boldsymbol{\pi}^{E}\right]$. The pseudo-code of TS-NEH is presented in Algorithm 1. In R-NEH, the job sequence for each family is generated randomly, and the total job sequence $\boldsymbol{\pi}^{E}$ is formed from these partial job sequences. Then, both the LPT and NEH rules are applied similarly to the second stage of R-NEH. Both of these proposed heuristics are utilized to generate the initial population $\operatorname{Pop}(0)$, with one solution generated via TS-NEH and the remaining solutions generated by R-NEH. The pseudo-code of R-NEH is shown in Algorithm 2.

### 4.2. EEDA-based global search

This section introduces an EEDA-based global search, which consists of three key components, i.e., a probability model with problem-specific knowledge, a family-based updating mechanism, and a specific sampling strategy. This knowledge-dependent global search can effectively
drive the search behavior towards promising regions. Each of the components of EEDA is detailed in the following subsections.

### 4.2.1. Probability model

As a crucial component of EDA, probability models are commonly utilized to capture potential patterns implicit in high-quality solutions [20]. In EEDA, the proposed probability model not only preserves information regarding relationships between jobs but also accumulates information about characteristic connections across families. The matrix representation of the proposed probabilistic model $P M^{G}$ of the Gth generation is shown in Eq. (43). Note that partition matrices within $P M^{G}$ are categorized based on the feature information of families and jobs. To visually demonstrate the proposed probability model $P M^{G}$, a graphical representation of it is shown in Fig. 8. Within $P M^{G}, P M_{G}^{G}$ denotes the estimation of the first job in cellulars, $P M_{G}^{G}$ records the inherent connections of jobs within $\Gamma_{\mathrm{a}}$, and $P M_{G}^{G}{ }_{b}$ represents connections among jobs across the families $\Gamma_{\mathrm{a}}$ and $\Gamma_{\mathrm{b}}$. Note that $p_{a b}^{G}(x, y)$ indicates the probability value that the job following $J_{x}$ is $J_{y}$ in $\Gamma_{\mathrm{a}}$, while $p_{a b}^{G}(x, y)$ denotes the probability value that the last job $J_{x}$ of $\Gamma_{\mathrm{a}}$ is followed by the first job $J_{y}$ of $\Gamma_{\mathrm{b}}$. Through these partitioned matrices, $P M^{G}$ establishes a close connection between the family and the job, ensuring that the structural features and valuable information of superior solutions are fully captured without omission.

$$
P M^{G}=\left[\begin{array}{cccc}
p_{01}^{G}(0,1) & \cdots & p_{01}^{G}(0, n) \\
p_{11}^{G}(1,1) & \cdots & p_{11}^{G}(1, n) \\
\vdots & \ddots & \vdots \\
p_{21}^{G}(n, 1) & \cdots & p_{21}^{G}(n, n)
\end{array}\right]_{(n+1)=n}
$$

### 4.2.2. Family-based updating mechanism

To precisely guide the global search trend and track promising regions in the solution space, the probability model must be appropriately adapted to critical characteristics. Hence, a family-based updating mechanism is introduced to adjust the probability model, preserving promising patterns while preventing the disruption of connections between jobs and families. The counting matrix $R M^{G}$ is designed to capture valuable information implicit in high-quality solutions so as to update the $P M^{G}$. Each element $r_{a b}^{G}(x, y)$ in $R M^{G}$ corresponds to the probability value $p_{a b}^{G}(x, y)$ in $P M^{G}$, as depicted in Eq. (44).
$R M^{G}=\left[\begin{array}{cccc} 
& & & \\
& & & \\
r_{01}^{G}(0,1) & \cdots & r_{01}^{G}(0, n) \\
r_{11}^{G}(1,1) & \cdots & r_{11}^{G}(1, n) \\
\vdots & \ddots & \vdots \\
r_{21}^{G}(n, 1) & \cdots & r_{21}^{G}(n, n)
\end{array}\right]_{(n+1)=n}$
To calculate each element $r_{a b}^{G}(x, y)$ of $R M^{G}$, two indicator functions are employed to record information about the relationship between jobs and families extracted from high-quality solutions. $I r_{a b}^{G}(x, y)$ serves as an indicator function to record job correlations in $\Gamma_{\mathrm{a}}$, which indicates job $J_{x}$ is followed by job $J_{y}$ in $\Gamma_{\mathrm{a}} . I r_{a b}^{G}(x, y)$ indicates the relationship between $J_{x}$ of $\Gamma_{\mathrm{a}}$ and $J_{y}$ of $\Gamma_{\mathrm{b}}$. If the first job of cellular is $J_{y}$ and its family is $\Gamma_{\mathrm{b}}$, it can be indicated by $I r_{0 b}^{G}(0, y)$. To capture the information between families efficiently, when $\Gamma_{\mathrm{a}}$ is followed by $\Gamma_{\mathrm{b}}$ in the feasible solution, $I r_{a b}^{G}(x, y)$ is set to 1 . In addition, if $J_{x}$ is followed by $J_{y}, I r_{a b}^{G}(x, y)$ is set to 2. The calculations of $I r_{a b}^{G}(x, y), I r_{0 b}^{G}(x, y), I r_{0 b}^{G}(0, y)$, and $r_{a b}^{G}(x, y)$ are illustrated by Eqs. (45)-(48), respectively. The family-based updating mechanism enables the recording of the relationship information between jobs while recording the information between families within high-quality solutions, further exploring the relationship information

```
Input: \(P M^{G}\) ；
    for \(y=1\) to \(n\) do
    \(R_{P M}^{G}(y)=\sum_{j=1}^{y} P M^{G}(0, z) . / / C a l c u l a t e\) the cumulative probability
    end for
    Produce a random value \(p_{r}\), where \(p_{r} \in\left[0, \sum_{j=1}^{n} R_{P M}^{G}(y)\right)\).
    if \(p_{r} \in\left[0, R_{P M}^{G}(1)\right)\) then
        \(\pi_{k}^{P}(i) \leftarrow 1\).
        else
        for \(t=1\) to \(n-1\) do //Roulette wheel selection
        if \(p_{r} \in\left[\sum_{j=1}^{t} R_{P M}^{G}(y), \sum_{j=1}^{t+1} R_{P M}^{G}(y)\right)\) then
            \(\pi_{k}^{P}(i) \leftarrow t+1\), break.
        end if
        end for
    end if
    for $t=0$ to \(n\) do //Avoid repeated selection of jobs
        \(P M^{G}\left(t, \pi_{k}^{P}(i)\right)=0\).
    end for
Output: \(\pi_{k}^{P}(i)\).
```

```
Input: \(P M^{G}, \pi_{k}^{P}(i-1)\).
    for \(y=\Gamma_{k}(1)\) to \(\Gamma_{k}\left(n_{k}\right)\) do
        \(R_{P M}^{G}(y)=\sum_{j=1}^{y} P M^{G}\left(\pi_{k}^{P}(i)\right), z) . / / C a l c u l a t e\) the cumulative probability
    end for
    Produce a random value \(p_{r}\), where \(p_{r} \in\left[0, \sum_{j=1}^{n} R_{P M}^{G}(y)\right)\).
    if \(p_{r} \in\left[0, R_{P M}^{G}(1)\right)\) then
        \(\pi_{k}^{P}(i) \leftarrow \Gamma_{k}(1)\).
        else
        for \(t=1\) to \(n-1\) do //Roulette wheel selection
        if \(p_{r} \in\left[\sum_{j=1}^{t} R_{P M}^{G}(y), \sum_{j=1}^{t+1} R_{P M}^{G}(y)\right)\) then
            \(\pi_{k}^{P}(i) \leftarrow \Gamma_{k}(t)+1\), break.
        end if
        end for
    end if
    for $t=0$ to \(n\) do //Avoid repeated selection of jobs
        \(P M^{G}\left(t, \pi_{k}^{P}(i)\right)=0\).
    end for
Output: \(\pi_{k}^{P}(i)\).
```

between jobs and families. Fig. 9 shows the illustration of the updating mechanism for the counting matrix $R M^{G}$. The initialization method of the initial probability values of different partition matrices in the probability model $P M^{G}$ is given in Eq. (49). The updating mechanism of $P M^{G}$ is described by Eq. (50), where $l r$ is the learning rate.

$$
\begin{aligned}
& I . r_{m}^{G}(x, y)= \begin{cases}1, & \text { if } x=\Gamma_{n}(i) \text { and } y=\Gamma_{n}(i+1) \\
0, & \text { otherwise }\end{cases} \\
& I . r_{m}^{G}(x, y)= \begin{cases}1, & \text { if } x=\Gamma_{n}\left(n_{n}\right), y=\Gamma_{n}(1) \text { and } a+1=b \\
0, & \text { otherwise }\end{cases} \\
& a=1, \ldots, S-1
\end{aligned}
$$

$$
\left\{\begin{array}{l}
p_{i j k}^{0}(0, y)=1 /\left(S \times n_{b}\right) \\
p_{a n}^{0}(x, y)=1 / n_{a}^{0} \\
p_{a b}^{0}(x, y)=1 /\left(n_{a} \times n_{b} \times(S-1)\right) \\
a, b=1,2, \ldots, S, a \neq b, J_{s} \in \Gamma_{a}, J_{z} \in \Gamma_{b}
\end{array}\right.
$$

$\left\{\begin{array}{l}p_{i j k}^{1}(0, y)=(1-I r) \times p_{i j k}^{0}(0, y)+I r \times r_{i j k}^{1}(0, y) /\left(\sum_{s=1}^{n} \sum_{k=1}^{n_{s}} r_{i k}^{1}(0, k)\right) \\ p_{a n}^{1}(x, y)=(1-I r) \times p_{a n}^{0}(x, y)+I r \times r_{a n}^{1}(x, y) /\left(\sum_{k=1}^{n_{s}} \sum_{k>1}^{n_{s}} r_{a n}^{1}(k, k)\right) \\ p_{a b}^{1}(x, y)=(1-I r) \times p_{a b}^{0}(x, y)+I r \times r_{a b}^{1}(x, y) /\left(\sum_{k=1}^{n_{s}} \sum_{k>1}^{n_{s}} r_{a b}^{1}(k, k)\right)\end{array}\right.$.
$a, b=1,2, \ldots, S, a \neq b, J_{s} \in \Gamma_{a}, J_{z} \in \Gamma_{b}$
According to the above, the steps of the family-based updating mechanism are as follows.

Step 1: Initialize the problem-specific probability model $P M^{G}$ via Eq. (49), and set $G=1$.

Step 2: Select $h p \times$ popsize solutions from $\operatorname{Pop}(G)$ and calculate $R M^{G}$ by Eqs. (45)-(48), where $h p$ represents the percentage of high-quality sub-populations.

Step 3: Update the probability model $P M^{G}$ according to Eq. (50).
Step 4: Set $G=G+1$. If termination conditions are not met, go to Step 2.

### 4.2.3. Sampling strategy

Suitable sampling strategies can improve the accuracy and stability of distribution estimation and increase computational efficiency. Probabilistic models can implicitly capture crucial characteristics inherent in the distribution of superior solutions in the solution space by mapping promising patterns to corresponding probability values. To effectively extract the correlation between families and jobs recorded in $P M^{G}$, this section provided a problem-specific sampling strategy to generate new solutions with quality and diversity. To generate the first family and its job sequence, we define PickFirstJob (shown in Algorithm 3) as the first job selection function, and PickNextJob (shown in Algorithm 4) as the next job selection function in the same family. The first job is picked by PickFirstJob, and the subsequent ones are chosen by using PickNextJob until all the jobs in this family have been selected. Then, the next job and
its family are selected by PickFamily (shown in Algorithm 5), after which PickNextJob is used to obtain all jobs in $\Gamma_{k}$, and so on until all families and jobs are chosen. Thus, the new population generation process is denoted by NewPopGeneration, as detailed in Algorithm 6, and Fig. 10 illustrates the generation process of the feasible solution in a cellular. To be specific, first, $P M_{1}^{G}$ is sampled by PickFirstJob to generate the first job $J_{2}$ of $\Gamma_{1}$, then $P M_{1}^{G}$ is sampled by PickNextJob to obtain the two jobs $J_{1}$ and $J_{2}$. Next, PickFamily is used to sample $P M_{1 / 6}^{G}$ to select the next family $\Gamma_{3}$ and its first job $J_{6}$. Finally, the process repeats with PickJob and PickFamily until all families and jobs are selected.

### 4.3. Local intensification

It is common that embedding local searches in EDAs for intensification can effectively enhance the local exploitation capability, focusing on fine-grained seeking for promising regions found by global searches. In order to strike the balance between global exploration and local exploitation of EEDA, three problem-specific local search operators are proposed to refine the obtained solutions. These local search operators are described in detail in the following subsections.

### 4.3.1. Local search for family swap

As shown in Algorithm 7, a family $\Gamma_{a}$ is randomly selected from the critical cellular $c$ in $\boldsymbol{\pi}^{C}$, and then $\Gamma_{a}$ is swapped with all other families in each cellular to find the swapped family resulting in the minimum $C_{\max }(\boldsymbol{\pi})$. Next, the positions of two families in $\boldsymbol{\pi}^{C}$ are exchanged to generate a new feasible solution $\boldsymbol{\pi}$. When evaluating the solution $\boldsymbol{\pi}$, the CC of calculating $C_{\max }(\boldsymbol{\pi})$ can be reduced based on Property 2 and Property 4.

### 4.3.2. Local search for family insertion

First, a family $\Gamma_{a}$ is randomly taken from the critical cellular $c$ (the one with the maximum completion time) in $\boldsymbol{\pi}^{C}$. Then, $\Gamma_{a}$ is reinserted into all possible positions of each cellular to determine the inserted position with the minimum makespan. Next, insert $\Gamma_{a}$ into the identified position of $\boldsymbol{\pi}^{C}$ to generate a new feasible solution $\boldsymbol{\pi}$. The pseudo-code is shown in Algorithm 8, which provides a detailed representation of this process. To reduce the CC in the calculation of $C_{\max }(\boldsymbol{\pi})$, Property 3 and Property 5 can be adopted here.

## Algorithm 5

PickFamily.

```
Input: \(P M^{G}, \pi_{k}^{T}(i-1)\).
for \(y=1\) to \(\pi\) do
    \(R_{P M}^{G}(y)=\sum_{s=1}^{n} P M^{G}\left(\pi_{k}^{T}(i-1), \tau\right) \cdot\)//Calculate the cumulative probability
    end for
    Produce a random value \(p_{i}\), where \(p_{i} \in\left(0, \sum_{s=1}^{n} R_{P M}^{G}(y)\right)\).
if \(p_{i} \in\left(0, R_{P M}^{G}(1)\right)\) then
    \(\pi_{k}^{T}(i) \leftarrow \Gamma_{k}(1)\).
else
    for \(t=1\) to \(n-1\) do //Roulette wheel selection
    if \(p_{i} \in\left[\sum_{s=1}^{t} R_{P M}^{G}(y), \sum_{s=1}^{t+1} R_{P M}^{G}(y)\right)\) then
        \(\pi_{k}^{T}(i) \leftarrow \Gamma_{k}(t+1)\), break.
    end if
    end for
    end if
for \(t=0\) to \(\pi\) do //Avoid repeated selection of jobs.
    \(\operatorname{PM}^{G}\left(t, \pi_{k}^{T}(i)\right)=0\).
    end for
Output: \(\pi_{k}^{T}(i)\).
```

Input: $P M^{G}$, popsize, $F$.
Set $\operatorname{Pop}(G)=\left[\pi_{1}, \pi_{2}, \ldots, \pi_{\text {popsize }}\right]$.
for $k=1$ to popsize do
for $v=1$ to $F$ do
$\pi_{h}^{F}(1) \leftarrow$ PickFirstJob . //Algorithm 2
for $r=2$ to $n_{h}-1$ do
$\pi_{h}^{F}(r) \leftarrow$ PickNextJob . //Algorithm 3 end for
Assign $\Gamma_{h}$ to cellular $v$ in $\pi^{C}$.
end for
for $l=1$ to $(S-F)$ do
Determine the cellular $s$ with the smallest current processing time.
$\pi_{h}^{F}(1) \leftarrow$ PickFamily //Algorithm 4
Assign $\Gamma_{h}$ to cellular $s$ in $\pi^{C}$.
for $r=2$ to $n_{h}-1$ do
$\pi_{h}^{F}(r) \leftarrow$ PickNextJob . //Algorithm 3 end for
end for
end for
18: $\pi_{k} \leftarrow\left[\pi^{C}, \pi^{F}\right]$.
19: end for
Output: $\operatorname{Pop}(G)$.

### 4.3.3. Local search for job insertion

Randomly select a family $\Gamma_{n}$ from critical cellular $c$ in $\pi^{C}$, then a job $J_{x}$ is randomly taken out from $\Gamma_{n}$ in $\pi^{C}$. Reinsert $J_{x}$ into all possible positions in $\Gamma_{n}$ to find the position with the smallest $C_{\max }(\pi)$. Next, insert the job into the found position to generate a new solution $\pi$. The pseudocode of the procedure is provided as Algorithm 9. According to Property 6 , the CC of calculating $C_{\max }(\pi)$ can be reduced.

### 4.4. Perturbation and reinitialization

It is useful to add specific perturbation and reinitialization methods to the global search of EDAs to enhance the diversity of search behaviors and skip search stagnation, thus effectively combating the challenge of falling into local optima by introducing small variations to the feasible solutions [3,20]. In EEDA, if there is no improvement after $\alpha$ iterations, families are randomly selected from each cellular of $\pi_{\text {best }}^{C}$ to form a temporary set Y. Then, the families of the set are sequentially inserted into all possible positions in $\pi_{\text {best }}^{C}$ to identify the positions that minimize $C_{\max }\left(\pi_{\text {best }}\right)$, until all the families in the set have been inserted. Next, $\pi_{\text {best }}$ is updated. Finally, due to the lack of updates to $\pi_{\text {best }}$ for several generations, this may result in overly similar information within the probability model. However, resetting the entire probability model would lead to the loss of previously retained high-quality information. Hence, all values of the probability model $P M^{G}$ are partially reset by Eq. (51) to prevent premature convergence. The detailed description of the perturbation and reinitialization methods is shown in Algorithm 10.
$p_{i o}^{G}(a, b)=p_{i o}^{G}(a, b) \times(1-b^{r})+p_{i o}^{b}(a, b) \times b^{r}$.
$a=0,1, \ldots, S, b=1,2, \ldots, S, x=0,1, \ldots, n_{a}, y=1,2, \ldots, n_{b}$.

### 4.5. Computational complexity of EEDA

In EEDA, the analysis of CC for critical components involves the analysis of initialization, sorting operation, updating mechanism, sampling and local search strategies. Firstly, initializing the initial population $\operatorname{Pop}(0)$ by Algorithm 1 with the CC of $O\left(n \times S^{2}\right)$ and by Algorithm 2
with the CC of $O\|\left(p o p s i z e-1\right) \times S^{2} \|$; Secondly, sorting $h p \times$ popsize highquality solutions from $\operatorname{Pop}(G)$ with the CC of $O($ popsize $\times n \times m)$; Thirdly, updating the probability model $P M^{G}$ by using $h p \times$ popsize high-quality solutions with the CC of $O(h p \times p o p s i z e \times n \times(n+1))$; Fourthly, sampling the probability model $P M^{G}$ to generate popsize solutions with the CC of $O($ popsize $\times n)$; Finally, sorting new $h p \times$ popsize high-quality solutions from $\operatorname{Pop}(G+1)$ with the CC of $O($ popsizelogpopsize $)$ and performing three problem-specific local searches with the CC of $O(S \times m+$ $n \times m)$. It is noteworthy that the five problem properties provided in Section 3.2 are employed to reduce the CC of these local searches from $O(S \times n \times m+n^{2} \times m)$ to $O(S \times m+n \times m)$. The CC of the critical components of EEDA can be detailed in Table 7. Thus, the total CC (TCC) of EEDA can be represented by Eq. (52). If critical components are not all active in the iteration, the CC of EEDA is about $O($ popsizelogpopsize $+S \times$ $m+n \times m)$; if these components are active, the CC can be represented as $O(h p \times$ popsize $\times n \times(n+1))$, which is still acceptable for EEDA to address DNFGSP_SDSTs.
$\operatorname{TCC}_{(\text {EEDA })}=O\left(\right.$ popsize $\left.\times S^{2}\right)+O\left(n \times S^{2}\right)$
$+O(S \times m)+O(n \times m)+O($ popsize $\times n \times m)$
$+O($ popsizelogpopsize $)+O\left(h p \times\right.$ popsize $\left.\times n^{2}\right)^{-}$
$+O($ popsize $\times n)$

### 4.6. Framework of EEDA with problem-specific knowledge

This subsection gives the framework of EEDA. In EEDA, the probability model with problem-specific knowledge is devised to accumulate valuable pattern information of high-quality solutions, and the familybased updating mechanism is designed to update this probability model. To generate new solutions with certain quality, the sampling strategy is proposed for sampling probability model to enhance the search capability of EEDA. Then, three local search operators are developed to refine the solutions found by the global search. Moreover, perturbation and reinitialization methods are presented to avoid premature convergence. The flowchart of EEDA is shown in Fig. 11. The detailed description are as follows.

![img-13.jpeg](img-13.jpeg)

Fig. 10. Illustration of sampling from $P M^{G}$ to generate a cellular of $\pi$.

# Algorithm 7 

LeFam_Swap.

Input: $\pi$.
for $v=1$ to $F$ do
Find the critical cellular $c$.
if there are two or more critical cellulars:
Randomly select a critical cellular $c$.
end if
end for
Randomly extract a family $\Gamma_{n}$ from cellular $c$.
for $v=1$ to $F$ do
$\mathrm{Swap} \Gamma_{n}$ with all other families in $\pi^{C}$.
Record the family in cellular $v$ of $\pi^{C}$ with the minimum $C_{\max }(\pi)$ as Fam.
11: end for
12: $\operatorname{Inser} \Gamma_{n}$ at position Pos in $\pi^{C}$ to generate a new solution $\pi^{\prime}$.
Output: $\pi^{\prime}$

# Input: $\pi$. 

1: Randomly select a family $\Gamma_{\alpha}$ from critical cellular $c$.
2: Randomly extract $J_{x}$ from $\Gamma_{\alpha}$.
3: for $t=1$ to $n_{\alpha}$ do
4: Reinsert $J_{x}$ into all possible positions in $\Gamma_{\alpha}$.
5: Record the position in $\Gamma_{\alpha}$ with the minimum $C_{\text {max }}^{c}(\pi)$ as Pos.
6: end for
7: Insert $\Gamma_{\alpha}$ into position Pos in $\Gamma_{\alpha}$ to generate a new solution $\pi^{\prime}$.
Output: $\pi^{\prime}$.

Step 1: Initialize key parameters of EEDA, including popsize, $h p, l r$, and $\alpha$, all of which are calibrated in Section 5.1. Initialize probability model $P M^{G}$ and generate initial population $\operatorname{Pop}(0)$ by using the hybrid initialization method in Section 4.1 and SubSection 4.2.2.

Step 2: Evaluate each feasible solution and sort to obtain popsize $=\boldsymbol{h p}$ high-quality solutions.

Step 3: Calculate the counting matrix $R M^{G}$ and update the probability model $P M^{G}$ by $R M^{G}$ via Eqs. (45)-(48) and Eq. (50) in SubSection 4.2.2.

Step 4: Generate $\operatorname{Pop}(G+1)$ by sampling $P M^{G}$ and update $\pi_{\text {best }}$ in SubSection 4.3.3.

Step 5: Perform three types of local search operators on $\pi_{\text {best }}$ in Section 4.3.

Step 6: Determine if the search is stagnant. If $\pi_{\text {best }}$ is not updated in successive $\alpha$ generations, perform perturbation and reinitialization methods given in Section 4.4.

Step 7: Examine the termination condition. If it is not met, go to Step 2, otherwise output $\pi_{\text {best }}$.

According to the above steps, it can be observed that the performance of EEDA is well emphasized and balanced by combining the advantages of global exploration and local exploitation. These strategies strengthen the ability of EEDA to solve DNFGSP_SDSTs.

## 5. Experimental comparisons and statistical analysis

In this section, a series of statistical experiments and computational comparisons are conducted to evaluate the efficiency and effectiveness of the proposed EEDA in solving the DNFGSP_SDSTs. Section 5.1 provides details of the experimental setups, including the introduction of the benchmark instances, the experimental environment, and the evaluat
and analyzed to refine the performance of EEDA, ensuring the best behavior in handing various problem instances. Section 5.3 verifies the proposed MILP model on small- and medium-scale instances by using the Gurobi solver, confirming the validity of the MILP model in terms of both scale and computational complexity. In Section 5.4, the efficacy of each element of EEDA is examined, revealing the impact and implications of improvement strategies. Finally, comprehensive comparisons of EEDA versus several state-of-the-art approaches are performed, and the experimental results are analyzed in detail in Section 5.5. Some

Table 7
Computational complexity of critical components of EEDA.
## Algorithm 10

Perturbation and reinitialization.

```
Input: \(\pi_{\text {best }}, P M^{G}, P M^{G}\)
    for \(v=1\) to \(F\) do \(\mathcal{O}\) Perturbation
    Randomly generate a number rm from 1 and 2 .
    Randomly extract rm family from cellular \(v\) of \(\boldsymbol{\pi}_{\text {best }}^{\mathrm{C}}\) and put them into set \(\Gamma\).
    end for
    for \(t=1\) to length( \(\Gamma\) ) do
    for \(v=1\) to \(F\) do
    Test family \(\Gamma_{t}\) in all the possible positions in cellular \(v\) of \(\boldsymbol{\pi}_{\text {best }}^{\mathrm{C}}\).
    Pos \(\leftarrow\) The position in cellular \(v\) of \(\boldsymbol{\pi}_{\text {best }}^{\mathrm{C}}\) with the minimum \(C_{\text {max }}\left(\pi_{\text {best }}\right)\).
    end for
    Insert \(\Gamma_{t}\) at position Pos in \(\boldsymbol{\pi}_{\text {best }}^{\mathrm{C}}\) to update \(\pi_{\text {best }}\).
    end for
    for \(t=1\) to \(n+1\) do \(\mathcal{O}\) Reinitialization
    for \(v=1\) to \(n\) do
    \(P M^{G}(t, v)=P M^{G}(t, v) \times(1-l r)+P M^{G}(t, v) \times l r . \mathcal{O}\) Eq. (51)
    end for
    end for
Output: \(\pi_{\text {best }}\) and new \(P M^{G}\).
```

conclusions are drawn, and the superiority of EEDA is discussed in Section 5.6.

### 5.1. Experimental setup

To evaluate the efficacy of EEDA for solving DNFGSP_SDSTs across various scenarios, a set of 810 instances was adapted from a benchmark dataset provided by Pan et al. [3], which is widely used in DFGSPs. This dataset was grouped into a total of 162 combinations, each of which contains five instances. Each instance is characterized by parameters including three different scales of setup times, six different cellular scales $F \in\{2,3,4,5,6,7\}$, three machine scales $m \in\{2,4,6\}$, and three family scales $S \in\{20,40,60\}$. For the instances of each combination, $n_{0}$ and $p_{i, j}$ are uniformly distributed integers ranging from 1 to 10 , and the setup times $s_{0,0, j}$ for small, medium, and large types are randomly generated integers from uniform distribution ranges [1,20], [1,40], and $[1,60]$, respectively. All algorithms, including the MILP solver, were implemented by Python programming language, compiled by Python 3.11 in PyCharm Studio 2021. The MILP solver typically employs the branch-and-cut technique that incorporates cutting planes and branch-and-bound methods, which works by branching and bounding, while utilizing cutting planes to tighten the LP relaxation. The numerical experiments were executed independently on a PC equipped with an Intel(R) Core i7-8700 M CPU @ 3.20 GHz processor and 16 GB RAM with a 64-bit Windows 7 OS. To ensure fairness and accuracy, the same library functions and backend running environments were adopted, and no other programs were executed in parallel during algorithm implementation. Under the same experimental conditions, each algorithm was independently executed for 10 runs on 810 instances, with the same maximum elapsed CPU time of $\rho \times m \times S$ milliseconds, where $\rho$ has been tested at three values $\rho \in\{100,200,300\}$. To compare the performance of the proposed EEDA with other efficient algorithms, the relative percentage increase (RPI) was used as a comparison standard, which is calculated by Eq. (53) to measure the performance of algorithms in the experiments.
$R P I_{i}=\frac{c_{i}-c_{\text {best }}}{c_{\text {best }}} \times 100$,
where $c_{\text {best }}$ is the best fitness value found by all comparison algorithms for each instance, and $c_{i}$ is the best fitness value determined by the given algorithm, i.e., EEDA, TIG $_{+1}$ [24], TIG $_{+2}$ [49], CIG [67], CCEA [3], DIWO [68], CCABC [69], DABC [70] and IABC [55]. Clearly, smaller $R P I_{e}$
means better performance of the algorithm. In addition, if there are $R$ runs of each algorithm for each instance, the average RPI (ARPI) is employed as the response variable (RV) to evaluate the effectiveness of the algorithm, which is calculated as $A R P I=\sum_{i=1}^{R} R P I_{i} / R$, where $R$ represents the total number of runs.

### 5.2. Sensitivity analysis of parameters

Since parameter calibration significantly impacts the performance of algorithms, superior search behaviors greatly depend upon their parameter configurations. To determine the proper parameter combination for EEDA, the design of experiment (DOE) method [71] is implemented to investigate the influence of parameters on EEDA. EEDA incorporates four key parameters: (1) population size popsize (2) percentage of high-quality sub-populations $h p$; (3) learning rate $l r$; (4) perturbation factor $\alpha$. Suitable values (levels) for these parameters were determined both through experience and preliminary experiments, so the levels of parameters are listed below: popsize $=\{30,50,70,90\}, l r=$ $\{0.05,0.1,0.3,0.5\}, h p=\{0.1,0.3,0.5,0.7\}$, and $\alpha=\{5,10,15,20\}$. Each of these parameters has four levels, resulting in a total of $4 \times 4 \times 4 \times 4=$ 256 different configurations, as shown in Table 6. To evaluate the effect of parameter settings and eliminate the risk of overfitting, we used the ARPI, an evaluation metric in the averaged sense, and inspired by Ref. [3], we regenerated 81 instances at three setup time scales with $F \in$ $\{2,4,6\}, m \in\{2,4,6\}$, and $S \in\{20,40,60\}$. To adequately reveal the effects between parameters, each configuration was independently tested 20 times on a set of 81 instances, and the maximum elapsed CPU time was set to $300 \times m \times S$ milliseconds for parameter calibration. As a result, it required at least 268.8 CPU days to finish all calibration experiments. However, due to the parallel computing capability of PC with multiple cores, it took almost 13.4 days to acquire all numerical results. To analyze these results and assess the significance of parameter interactions, this section employed the multifactor analysis of variance (ANOVA). The ANOVA results for parameters are provided in Table 8, with $p$-values marked in bold when they are smaller than 0.05 .

As observed from Table 9, the $p$-values of popsize, $l r$, and $\alpha$ are all less than 0.05 , indicating the significance of these three parameters in influencing the performance of the proposed EEDA. It is worth noting that since popsize has the largest $F$-ratio, this implies that population size has a much greater effect on the efficiency of EEDA. Fig. 12 provides the main effect plots of the parameters, indicating that the impact of popsize is more significant than the other parameters. From Fig. 12, the most
![img-14.jpeg](img-14.jpeg)

Fig. 11. The flowchart of EEDA for DNFGSP_SDSTs.

favorable performance is achieved with popsize $=50$, while the least favorable outcome is associated with popsize $=90$. This observation suggests that insufficient diversity of solutions may result from smaller popsize, and larger values of popsize may increase computational complexity and decrease search efficiency. In contrast, there is also a significant effect of $l r$ in EEDA, with the $F$-ratio slightly lower than that of popsize. It can be seen in Fig. 12 that $l r=0.1$ can yield the best results, potentially because smaller values of the learning rate $l r$ may fail to retain sufficient valuable information in the probability model $P M^{G}$, whereas larger values may lead to homogenous information. The trend curves of $h p$ in Fig. 12 further support the superior performance achieved by $h p=0.3$. This phenomenon arises due to the suboptimal solutions occupy excessive search resources when $h p$ exceeds a certain value. Conversely, when $h p$ falls below a certain value, it risks constraining the informational diversity essential for the generation of highquality solutions. Furthermore, for the parameter $\alpha$, if it is too small, there is a risk of prematurely introducing perturbations before convergence, resulting in wastage of computational resources. Conversely, if $\alpha$ exceeds a certain value, it may lead to excessive iterations of futile searches, also resulting in a waste of computational resources. As indicated in Fig. 12, the best results are obtained when the perturbation factor $\alpha$ is set to 15 , indicating that when 15 iterations are not improved then the perturbation is performed to re-activate the search. In addition, it is further observed from Fig. 12 that small changes in parameters lead to slight swings in ARPI and these variations remain small. Nonetheless, EEDA shows stability and strong robustness at different parameter settings, as evidenced by the consistent performance under varied conditions.

While main effects provide valuable insights into the choice of parameters, analyzing potential interactions between parameters is equally essential. Table 9 provides a detailed examination of the bifactor interactions, with corresponding interaction effect plots presented in Fig. 13. Notably, the $p$-values of popsize $* l r$, popsize $* \alpha, l r * \alpha$ are less than 0.05 , indicating statistical significance in these interactions. However, it is noteworthy that the $F$-ratios of single parameters surpass those of the interactions, suggesting that the interaction effects between parameters may be remarkably weak. It can be concluded in Table 9 that the interactions of popsize $* h p, l r * h p, h p * \alpha$ are weak, and this finding is further confirmed by the interaction effects of parameter pairs in Fig. 13. Therefore, the best parameter configurations, derived from the above analysis, are suggested as popsize $=50, l r=0.1, h p=0.3$, and $\alpha=15$.

### 5.3. Evaluation of MILP model

This section provides a comprehensive comparison and evaluation of the MILP model (refer to SubSection 3.1.1 for details). As observed in previous studies, MILP models are typically tested and analyzed based on scale complexity (SC), computational complexity (CC), or both. Regarding SC, the effectiveness of MILP models can be evaluated using multiple indicators, including the number of binary decision variables (NBVs), the number of continuous decision variables (NCVs), and the number of constraints (NCs). In general, NBVs, NCVs, and NCs are proportional to instance sizes. In terms of CC, several aspects of MILP models can be compared, such as the number of optimal or best solutions found in a given time limit, CPU time, and optimality gap, among others [57]. Note that the gap denotes the difference in optimality between the

Table 8
The levels of parameters.
Table 9
Results of ANOVA for parameters calibration.

Note: All $F$-ratios are based on the residual mean square error.
obtained solutions and the optimal solutions within the time limit, which can be calculated as the value of the RPI. Obviously, smaller gap values suggest higher solution quality. The correctness of the MILP model is validated by using the Gurobi solver (version 9.5.0) to tackle 36 different small-scale and medium-scale instances within a time limit of 3600 s . If no optimal solution is found within this timeframe, the best solution found is returned. The computational results of the MILP model for these instances, including NBVs, NCs, and CPU time, are reported in Table 10. It is observed from Table 10 that the Gurobi solver can achieve the best makespan for relatively small-scale instances, ranging from sFG_2_4_2_1_1 to sFG_2_15_2_3_1, and several medium-scale instances are also tested as a comparison. Detailed results for large-scale instances are available upon request. However, for relatively large-scale instances, the MILP model may fail to find any feasible solution within an acceptable CPU time. This is because the Gurobi solver tackles MILP models by default using the branch-and-cut method, which integrates cut-plane and branch-and-bound (B\&B) methods, depending mainly on the size of the solved problem. As instance scale increases, the branch-and-cut strategy becomes significantly challenging in dealing with MILP models due to the increased constraints (i.e., NCs), decision variables (i.e., NBVs and NCVs), and enlarged solution spaces, leading to difficulties in branching, seeking new bounds, and cutting subspace. Obviously, it is undeniable that the Gurobi solver can effectively solve small-scale instances to optimality, but it is not efficient in solving relatively large-scale instances. As a basis in comparison to calculate RPI values, EEDA is run independently 10 times for each instance, with the maximum CPU time set to $300 \times m \times S$ milliseconds. With the increased number of families $S$, setup times for more families and processing times for more jobs have to be considered, so the problem's complexity significantly increases. As demonstrated in Table 10, NBVs, NCs, and CPU times of the MILP model notably increase as problem complexity escalates, while solution quality does not significantly improve. Nevertheless, when compared with results from EEDA and other metaheuristics (i.e., $\mathrm{TIG}_{\mathrm{v} 1}$ [24], TIG $_{\mathrm{v} 2}$ [49], CCEA [3], and DIWO [68]), as shown in Table 13, although the MILP model requires more CPU time to solve the problem at hand, the RPI values of the solutions obtained by the MILP model are much larger. With the scale increases, EEDA achieves more satisfactory results than the MILP solver, and the runtime of the metaheuristic is quite lower than that of the MILP solver. This implies that the proposed EEDA outperform Gurobi solver, making it easier to obtain high-quality solutions compared to several state-of-the-art MILP solvers, thereby rendering EEDA more suitable for solving DNFGSP_SDSTs.

### 5.4. Effectiveness of key components in EEDA

As detailed in the previous sections, EEDA comprises three pivotal components: (1) speed-up evaluation methods developed in Section 3.2; (2) family-based updating mechanism designed in SubSection 4.2.2; (3)

![img-15.jpeg](img-15.jpeg)

Fig. 12. Main effect plots of parameters.
![img-16.jpeg](img-16.jpeg)

Fig. 13. Interaction effect plots of parameter pairs.
perturbation and reinitialization methods detailed in Section 4.4; (4) initialization method in Section 4.1. To investigate the efficacy of these components within EEDA, four variants, namely $\mathrm{EEDA}_{\mathrm{v} 1}, \mathrm{EEDA}_{\mathrm{v} 2}$, $\mathrm{EEDA}_{\mathrm{v} 3}$, and $\mathrm{EEDA}_{\mathrm{v} 4}$ are created by separately eliminating the effect of each component and then compared with EEDA. To be specific, EEDA $_{\mathrm{v} 1}$ is derived by excluding speed-up evaluation methods from EEDA. $\mathrm{EEDA}_{\mathrm{v} 2}$ is generated by substituting the probability model updating mechanism of EEDA with an alternative updating mechanism that only records the connected jobs between two different families in $R M^{G}$. $\mathrm{EEDA}_{\mathrm{v} 3}$ is created by removing both the perturbation and reinitialization methods from EEDA. EEDA $_{\mathrm{v} 4}$ is generated from EEDA by using a randomly generated population to substitute the population generated by the initialization method. Each variant is altered in only one component that differs from the EEDA, and their key parameters are fine-tuned to achieve the best behavior. For EEDA and its three variants,
their performance is evaluated by the solving of all 810 instances, each of which is executed independently 10 times, with the maximum elapsed CPU time of $\rho \times m \times S$ milliseconds, where $\rho=\{100,200,300\}$. The statistical results are reported in Table 11, grouped by $F, S$, and $m$, respectively. The best values of each group are highlighted in bold, the second-best values are marked in bold italics, and the third-best values are underlined. To visually evaluate the performance of the key components in EEDA, Fig. 14 shows the means plots of EEDA and its variants with $95 \%$ Tukey's HSD confidence intervals.

According to the findings from Table 11 and Fig. 14, the following conclusions can be drawn: (i) EEDA exhibits significantly superior performance compared to its three variants across all factors, i.e. $F, S$, and $m$. This indicates the effectiveness of the proposed improvement strategies in enhancing the effectiveness of EEDA. (ii) From Fig. 14, it is evident that the gap between EEDA and $\mathrm{EEDA}_{\mathrm{v} 3}$ is the most pronounced,

Table 10
NBVs, NCs, CPU times, and RPI values for MILP model.

indicating that the perturbation and reinitialization methods can exert the most substantial influence on the diversity and vitality of the search behavior within EEDA. (iii) As shown in Table 11, in certain cases of $\rho=$ 300, the results of $\mathrm{EEDA}_{\mathrm{v} 3}$ surpass those of $\mathrm{EEDA}_{\mathrm{v} 1}$ and $\mathrm{EEDA}_{\mathrm{v} 2}$, which reflects the efficiency and effectiveness of the speed-up evaluation method and the family-based updating mechanism, respectively. This implies that when $\rho$ is large enough, the possibility of being trapped into the local optimum is thus reduced. (iiii) It can be observed from Table 11 that $\mathrm{EEDA}_{\mathrm{v} 4}$ obtains its best results under $\rho=300$, but still slightly behind EEDA. In Fig. 14, the length of the confidence interval for $\mathrm{EEDA}_{\mathrm{v} 4}$ is similar to that for EEDA. The performance of $\mathrm{EEDA}_{\mathrm{v} 4}$ indicates that the proposed initialization method can provide a high-quality and diverse initial population for EEDA, thus effectively avoiding invalid searches during the initial phase. Based on these results and analyses, it can be concluded that speed-up evaluation methods, family-based updating mechanism, perturbation and reinitialization method, and initialization method are all effective components of EEDA.

### 5.5. Comparison between different state-of-the-art algorithms

To the best of our knowledge, the DFGSP with both no-wait and SDSTs constraints has not yet been studied so far, and there are no existing comparative algorithms. To validate the efficacy of EEDA, in this section, we conduct a comparative analysis with existing state-of-the-art algorithms, including i.e., $\mathrm{TIG}_{\mathrm{v} 1}$ [24], $\mathrm{TIG}_{\mathrm{v} 2}$ [49], CIG [67], CCEA [3], $\mathrm{DIWO}_{\mathrm{v} 1}, \mathrm{DIWO}_{\mathrm{v} 2}, \mathrm{DIWO}_{\mathrm{v} 3}$ [68], CCABC [69], DABC [70], and IABC [55]. These algorithms are employed to solve other scheduling problems, which consist of minimizing the makespan of DFGSP, DFSP with no-wait constraint, and DFSP with SDSTs. To be specific, both $\mathrm{TIG}_{\mathrm{v} 1}$ and $\mathrm{TIG}_{\mathrm{v} 2}$ achieved remarkable results in tackling DFGSPs using the two-stage strategy, while CIG, CCEA, and CCABC adopted cooperative co-evolutionary strategies to yield satisfactory solutions in decomposing and solving subproblems of DFGSPs. DIWO and ABC, well known for their effectiveness in addressing DNFSPs, are also chosen as comparison algorithms. It's worth noting that IABC is an improved ABC algorithm with a destruction-construction mechanism proposed for solving DFSP, demonstrating considerable reference value. Moreover, typical algorithms for DFSPs may be effective for dealing with their extensions. Since DNFGSP_SDSTs is a generalization of DFSP, selecting several sophisticated algorithms to tackle the extension of DFSP holds important interest. The differences between $\mathrm{DIWO}_{\mathrm{v} 1}, \mathrm{DIWO}_{\mathrm{v} 2}$, and $\mathrm{DIWO}_{\mathrm{v} 3}$ lie in their search strategies. $\mathrm{DIWO}_{\mathrm{v} 1}$ employs a two-phase strategy, where the first stage focuses on searching for suitable family sequences, and the second stage aims at adjusting job sequences; $\mathrm{DIWO}_{\mathrm{v} 2}$ directly searches for both family sequences and job sequences; and $\mathrm{DIWO}_{\mathrm{v} 3}$ randomly determines the search sequences during each iteration. For a fair
comparison, all algorithms are adapted to problem-specific characteristics, and the same decoding and population initialization methods are applied. Additionally, speed-up methods proposed in Section 3.2 are incorporated into all algorithms to enhance efficiency. Main parameters were set based on original suggestions, adapted to the problem, as shown in Table 12. Under the same experimental environments, all algorithm were conducted independently 10 times as previously mentioned on all instances, with the maximum elapsed CPU time of $\rho \times$ $m \times S$ milliseconds as the termination criterion, where $\rho=(100,200$. 300). These statistical results under three termination criteria, grouped by $F, S$, and $m$, are reported in Table 13-15, with the best, second-best, and third-best values marked accordingly. The best value in each group is marked in bold, the second one in italicized bold, and the third one is underlined. To verify whether the results obtained in the above tables are statistically significant, Fig. 15 and Fig. 16 show the means plots with $95 \%$ Tukey's HSD confidence intervals and boxplots of EEDA and the compared algorithms, respectively.

As reported in Tables 13-15, EEDA achieves the best results in terms of ARPI values in almost all test instances except for several scenarios, remarkably outperforming other algorithms, whereas DABC, IABC, and $\mathrm{DIWO}_{\mathrm{v} 1}$ achieve seemingly decent results in these scenarios. Nevertheless, there is still a considerable gap between the average results of both DABC, IABC, and $\mathrm{DIWO}_{\mathrm{v} 1}$ against EEDA. Further analysis of these statistical results in Tables 13-15 reveals interesting insights and findings. As for $\rho=100$ in Table 13, EEDA provides the best results in all scenarios, while $\mathrm{TIG}_{\mathrm{v} 1}, \mathrm{TIG}_{\mathrm{v} 2}, \mathrm{DABC}$, and IABC also achieve promising results. This indicates that the convergence performance of these five algorithms is excellent. As shown in Table 14, all the algorithms under $\rho=200$ obtained better results than those under $\rho=100$. Although CCEA is still slightly inferior to EEDA, the performance of CCEA has improved significantly. This may be due to the fact that CCEA effectively utilizes the correlations between families and jobs. With the increase of the termination factor $\rho$, each algorithm achieves the best results when $\rho=300$, and the average ARPI values for all algorithms in all instances are as follows: EEDA (1.95), TIG $_{\mathrm{v} 1}$ (4.37), TIG $_{\mathrm{v} 2}$ (4.19), CIG (4.56), CCEA (5.06), $\mathrm{DIWO}_{\mathrm{v} 1}$ (5.16), $\mathrm{DIWO}_{\mathrm{v} 2}$ (7.27), $\mathrm{DIWO}_{\mathrm{v} 3}$ (6.57), CCABC (9.30), DABC (2.96), and IABC (3.84). It is clear that these ARPI averages are enough to emphasize the excellent performance of EEDA, while CCABC yields the worst results. As can be observed from Tables 13-15, the performance of $\mathrm{TIG}_{\mathrm{v} 1}, \mathrm{TIG}_{\mathrm{v} 2}, \mathrm{CIG}$, and IABC in solving small-scale instances is remarkably better than that in solving large-scale instances, which may be because the large-scale instances are subjected to their larger solution spaces, and the destruction-construction on the only single solution may limit the search scope in the solution space. Unlike IG variants, IABC also gets outstanding performance under large-scale instances, which can be attributed to the search mechanism of ABC.

Table 11
The ARPI values of EEDA, $\mathrm{EEDA}_{\mathrm{v} 1}, \mathrm{EEDA}_{\mathrm{v} 2}, \mathrm{EEDA}_{\mathrm{v} 3}$, $\mathrm{EEDA}_{\mathrm{v} 4}$.

![img-17.jpeg](img-17.jpeg)

Fig. 14. Means plots with $95 \%$ Tukey's HSD confidence intervals of EEDA and its variants.

For the variants of ABC, DABC achieves better results overall than other variants due to the improved search mechanism in the employed bee and scout bee phases, and IABC achieves better results in small-scale instances by adding the destruction-construction mechanism, while CCABC performs worse due to its failure to be properly based on the problem characteristics. As illustrated in Figs. 15 and 16, $\mathrm{TIG}_{\mathrm{v} 1}, \mathrm{TIG}_{\mathrm{v} 2}$, and IABC perform reasonably well, and CIG excels within certain contexts, but its performance slightly lags behind that of the other IGs. The IG's search behavior suggests that $\mathrm{TIG}_{\mathrm{v} 1}, \mathrm{TIG}_{\mathrm{v} 2}$, IABC, and CIG can perform deeper exploration of the solution space. Moreover, the results yielded by $\mathrm{DIWO}_{\mathrm{v} 1}$ are all the best among the variants of DIWO, which demonstrates that the two-stage search strategy of $\mathrm{DIWO}_{\mathrm{v} 1}$ is effective in solving DNFGSP_SDSTs.

Although the superiority of EEDA was analyzed above, the interaction effect was still worth further investigation. Interaction effect analysis, as a commonly used statistical analysis method, is useful in revealing the interaction between factors and their impact on results. In this study, the test instances are mainly composed of three factors, including the number of cellulars $(F)$, families $(S)$, and machines $(m)$, each tested on three termination factors $(\rho)$. To elucidate how these factors interact with the performance of EEDA, a multifactor ANOVA was used to clarify some interesting findings. Figs. 17 and 18 depict interaction plots and box plots of all the algorithms with different

Table 12
The parameters of the compared algorithms.

factors, respectively. From these figures, it is evident that changes in any of the factors have slight effects on the efficacy of EEDA compared to other competitors, suggesting that EEDA is stable under different scenarios. Furthermore, the ARPI values yielded by EEDA are significantly lower than those of others, which also indicates the superior performance of EEDA. It is clear from Fig. 17(a) that each algorithm's performance improves as the termination time increases, while EEDA significantly outperforms all algorithms across all termination factors. In Fig. 17(a), the ranking of algorithms at $\rho=300$, from bottom to top, is

Table 13
The ARPI values of EEDA and compared algorithms with $\rho=100$.

as follows: EEDA, DABC, $\mathrm{TIG}_{\mathrm{v} 2}$, $\mathrm{TIG}_{\mathrm{v} 1}$, CIG, CCEA, DIWO ${ }_{v 1}$, DIWO $_{v 3}$, DIWO $_{v 2}$, and CCABC. From Fig. 17(b), the curve of EEDA has the smallest impact with the increase of $F$, whereas $\mathrm{TIG}_{\mathrm{v} 1}$ and $\mathrm{TIG}_{\mathrm{v} 2}$ are relatively more influenced. The overlapping intervals of $\mathrm{TIG}_{\mathrm{v} 1}$ and $\mathrm{TIG}_{\mathrm{v} 2}$ indicate that their performance is comparable in the statistical sense. With smaller $F$, the curves of TIGs are close to those of both DABC and IABC but higher than EEDA. As cellular $F$ increases, CIG and CCEA gradually catch up, while DIWO $_{v 1}$ improves significantly. Notably, DIWO $_{v 1}$ and CCEA exhibit overlapping in their intervals, while CCEA also shows better performance when $F$ becomes larger. As shown in Fig. 17(c), DABC and the three variants of DIWO are less affected by $S$,
improving solution quality with increasing termination time. Fig. 17(d) demonstrates that all algorithms perform better with increasing $m$, likely due to the fact that the CC is not greatly affected by $m$. As can be observed in Figs. 17 and 18, EEDA consistently outperforms other algorithms across all the factors. For most of the cases in Fig. 18, although the box plots of $\mathrm{TIG}_{\mathrm{v} 1}$ and $\mathrm{TIG}_{\mathrm{v} 2}$ have lower bounds, their box lengths are significantly longer than those of the others, and the box length of CIG is also longer. This suggests that although the desired results can be yielded via single soluation iterations under the effect of certain factors, overall the quality of the solutions is not stable. In contrast, despite the higher lower bound of CCEA, its box length remains short in most cases,

![img-18.jpeg](img-18.jpeg)

Fig. 15. Means plots with $95 \%$ Tukey's HSD confidence intervals of all algorithms.
![img-19.jpeg](img-19.jpeg)

Fig. 16. Box plots for all the algorithms.
showing significant stability of the cooperative coevolutionary strategy. Notably, the box lengths of the EEDA are the shortest, indicating its superior stability. Finally, Fig. 19 depicts the Gantt chart of the best solution found by EEDA for FG_2_20_6_1_1, with the makespan of 582.

### 5.6. Discussion

Through the conducted experiments, the effectiveness of crucial components in EEDA and the efficacy of EEDA have been systematically examined and evaluated. In comparison to state-of-the-art algorithms employed in the experiments, the proposed EEDA consistently demonstrates stable and efficient performance across instances of different scales. The superiority of EEDA can be concluded as follows. (1) Unlike the destruction-construction mechanism of IG, EEDA strategically learns valuable information hidden in high-quality solutions through a problem-specific probability model. This approach circumvents the
inadvertent destruction of promising patterns extracted from highquality solutions, contributing to the algorithm's efficacy. (2) The experimental results of CCABC are the least favorable among all compared algorithms, while DABC and IABC exhibit remarkable effectiveness. Notably, the distinction between CCABC, IABC, and DABC lies in the employed bee phase and scout bee phase. In the employed bee phase, DABC intelligently switches between searching the current neighborhood and moving on to the next if a superior solution is not found. The scout bee phase employs a VND-based method, effectively executing neighborhood searches. These well-developed search strategies in DABC can reduce blind exploration, enhancing its overall effectiveness. Compared to DABC, IABC gains better results in small-scale instances by introducing the destruction-construction mechanism and weakening the employed bee phase. As for solving large-scale instances, DABC outperforms IABC due to the limited times of destruction and construction of both family and job sequences. For CCABC, both

Table 14
The ARPI values of EEDA and compared algorithms with $\rho=200$.

employed and scout bee phases fail to efficiently search for neighborhoods based on problem characteristics. Similarly, for EEDA, the demonstrated effectiveness of speed-up evaluation methods indicates that these search strategies are efficient for exploring these neighborhoods. (3) Despite incorporating a reinitialization method, CCEA tends to be trapped in local optima. The reason may be that the valuable information retained in the reference of CCEA becomes homogenous after several generations, making it difficult to ensure the quality of newly generated solutions. CCABC may also face similar issues. In contrast, by utilizing family-based updating mechanism and specific sampling strategy, EEDA can capture diverse information from high-quality
solutions, generating superior solutions with certain quality and enriching population diversity. Therefore, EEDA can yield better results than both CCEA and CCABC, which commonly employ effective cooperative co-evolutionary frameworks. (4) Among the variations of DIWO, DIWO $_{ v 1}$ has a better performance than DIWO $_{ v 2}$ and DIWO $_{ v 3}$. DIWO $_{ v 1}$ employs a two-stage strategy, operating on family sequences and job sequences sequentially. While effective to some extent, there is still a lack of cooperation between the two stages in DIWO $_{ v 1}$. The excellent efficacy of EEDA can be attributed to its emphasis on the relationships between families and jobs, which allows global search to be guided by problem-specific knowledge. Consequently, it can be concluded that the

Table 15
The ARPI values of EEDA and compared algorithms with $\rho=300$.

effectiveness of EEDA on DNFGSP_SDSTs is highly successful since the devised search strategies are based on problem-specific knowledge.

## 6. Findings, research limitations, and recommendations for future search

### 6.1. Findings

The research on DFGSPs has emerged as a focal point in smart manufacturing research, while the study of knowledge-enhanced EDAs (EDAs) is a frontier in the evolutionary computation domain. Due to the
fact that DFGSPs with no-wait constraints and setup times have considerable challenges such as strongly coupled complexities, how to design efficient EDAs to solve DNFGSP_SDSTs based on problem characteristics and solution structures is a crucial concern urgently needs to be solved, yet relevant research and reports are still scarce. This article presents in-depth research from aspects of problem property analysis, algorithm framework development, and search strategy design, aiming at the effective development of probabilistic models by using problemspecific knowledge, focusing on achieving significant breakthroughs in terms of the overall performance of EDAs and learning-based paradigms. By analyzing the characteristics of FGSPs, we design problem-specific

![img-20.jpeg](img-20.jpeg)

Fig. 17. Interactions for all the algorithms. (a) Interactions of algorithms and $\rho$. (b) Interactions of algorithms and $F$. (c) Interactions of algorithms and $S$. (d) Interactions of algorithms and $m$.
speed-up evaluation methods, fast search strategies for specific neighborhood structures, and enhanced EDA (EEDA) by considering domain knowledge. In EEDA, an effective probability model and a family-based updating mechanism are established to extract the implicit information within and between families through partitioned matrices, adequately revealing the crucial characteristics inherent in superior solutions and the concealed connections among them, learning the potential promising patterns and enriching the searching behaviors, which further offer new ideas and ways for designing high-performance EDAs. Some of the findings are as follows. 1) a MILP model was developed for this strongly NP-hard problem and its validity was verified by the advanced Gurobi solver; 2) a problem-dependent probability model was established that can not only accumulate the frequencies of building blocks but also accurately capture the distribution of these blocks implicit in the sequences of superior solutions; 3) the efficacy of speed-up evaluation methods, family-based updating mechanism, perturbation and reinitialization methods were verified as critical components of EEDA; 4) the effectiveness and efficiency of the proposed EEDA with problem-specific knowledge was comprehensively compared and confirmed.

Several conclusions can be drawn from these findings, which provide insights and inspiration for future researchers. Firstly, as an effective knowledge-enhanced learning paradigm, EEDA relies on rational representation of crucial characteristics and exact extraction of potential patterns, provides the possibility of significant breakthroughs in guiding
global search towards promising regions, and thus can moderately reduce search blindness as compared to most of the existing HIOAs that are based on trial-and-error evolutionary mechanisms. Secondly, through probabilistic modeling based on problem-specific knowledge, EEDA can capture crucial connections between families and jobs so as to avoid omitting valuable information, adapting well to changes in the evolutionary process versus the most commonly used breadth-first and depth-first search strategies. Consequently, EEDA emerges as the topperforming algorithm and has achieved the best performance among state-of-the-art algorithms in addressing DNFGSP_SDST with the criterion of minimizing the makespan.

### 6.2. Research limitations

The limitations and impediments of this research are twofold: the interactivity between the global and local searches of EEDA, and the applicability of EEDA in addressing other types of problems. Firstly, the lack of substantial and sufficient interaction between global and local search may cause failure to effectively enable the sharing and transfer of information between the two. It is suggested that the valuable information extracted and estimated by the probability model during the global search should be used to regulate and guide the local search. In addition, the search scope should be further restricted by problem properties to avoid ineffective search, so that the limited search

![img-21.jpeg](img-21.jpeg)
(a) $\rho=100$
![img-22.jpeg](img-22.jpeg)
(e) $F=4,5$
![img-23.jpeg](img-23.jpeg)
(i) $S=60$
![img-24.jpeg](img-24.jpeg)
(b) $\rho=200$
![img-25.jpeg](img-25.jpeg)
(f) $F=6,7$
![img-26.jpeg](img-26.jpeg)
(j) $m=2$
![img-27.jpeg](img-27.jpeg)
(c) $\rho=300$
![img-28.jpeg](img-28.jpeg)
(g) $S=20$
![img-29.jpeg](img-29.jpeg)
(k) $m=4$
![img-30.jpeg](img-30.jpeg)
(d) $F=2,3$
![img-31.jpeg](img-31.jpeg)
(h) $S=40$
![img-32.jpeg](img-32.jpeg)
(l) $m=6$

Fig. 18. Box plots of all the algorithms with different factors.
![img-33.jpeg](img-33.jpeg)

Fig. 19. Gantt chart of the best solution found by EEDA for FG_2_20_6_1_1.
resources are targeted to promising regions within the solution space to enhance search efficiency. Secondly, EEDA was designed based on problem-specific knowledge analyzed and extracted from the
characteristics of DNFGSPs, which may not be sufficiently applicable to address other types of shop scheduling problems. Hence, additional attempts are required to explore the potential of knowledge-enhanced

EDAs and to widen their application scope.

### 6.3. Recommendations for future research

Future research efforts can be outlined in two aspects, focusing on the extension of DFGSPs and the design of efficient EDAs. First, knowledge-based search strategies and search mechanisms, as well as knowledge-enhanced learning-based paradigms, need to be investigated in depth to develop effective co-evolutionary search mechanisms, and complementary collaborative search strategies, and then present robust and effective approaches to tackle the energy-efficient DNFGSP_SDST. Second, attempts will be made to enhance the global search capability of EEDA while exploring its potential applicability to FGSPs and their extended problems. In addition, it is of interest to extend EEDA to solve distributed production, transportation, and assembly integration scheduling problems, which can effectively improve the generality of EDAs and broaden their practical engineering applications.

## CRediT authorship contribution statement

Zi-Qi Zhang: Writing - original draft, Methodology, Investigation, Funding acquisition, Conceptualization. Yan-Xuan Xu: Writing - original draft, Software, Methodology, Investigation. Bin Qian: Writing review \& editing, Supervision, Methodology, Funding acquisition. Rong Hu: Writing - review \& editing, Funding acquisition, Supervision. FangChun Wu: Software, Investigation. Ling Wang: Supervision, Project administration.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

The authors are sincerely grateful to the anonymous reviewers for their insightful comments and suggestions, which greatly improve this paper. This work was financially supported by the National Natural Science Foundation of China (Grant Nos. 72201115, 62173169, and 61963022), the Yunnan Fundamental Research Projects (Grant No. 202201BE070001-050 and 202301AU070069), and the Basic Research Key Project of Yunnan Province (Grant No. 202201AS070030).
