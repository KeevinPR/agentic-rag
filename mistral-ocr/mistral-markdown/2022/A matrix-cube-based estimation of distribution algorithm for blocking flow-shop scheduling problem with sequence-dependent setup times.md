# A matrix-cube-based estimation of distribution algorithm for blocking flow-shop scheduling problem with sequence-dependent setup times 

Zi-Qi Zhang ${ }^{\mathrm{a}, \mathrm{b}, \mathrm{c}}$, Bin Qian ${ }^{\mathrm{a}, \mathrm{b}, \mathrm{c},{ }^{*}}$, Rong $\mathrm{Hu}^{\mathrm{a}, \mathrm{c}}$, Huai-Ping Jin ${ }^{\mathrm{a}}$, Ling Wang ${ }^{\mathrm{d}}$, Jian-Bo Yang ${ }^{\mathrm{e}}$<br>${ }^{a}$ School of Information Engineering and Automation, Kunming University of Science and Technology, Kunming 650500, PR China<br>${ }^{\mathrm{b}}$ School of Mechanical and Electrical Engineering, Kunming University of Science and Technology, Kunming 650500, PR China<br>${ }^{\mathrm{c}}$ Yunnan Key Laboratory of Artificial Intelligence, Kunming University of Science and Technology, Kunming 650500, PR China<br>${ }^{d}$ Department of Automation, Tsinghua University, Beijing 100084, PR China<br>${ }^{e}$ Alliance Manchester Business School, The University of Manchester, Manchester M15 6P8, United Kingdom

## A R TICLE INFO

Keywords:
Blocking flow-shop scheduling
Estimation of distribution algorithm
Setup times
Multi-dimensional probabilistic model
Iterated local search

## A B STR A C T

The blocking flow-shop scheduling problem with sequence-dependent setup times (BFSP_SDST) is a strong NPhard problem that exists widely in practice. However, research on this issue is still quite limited. Hence, this paper presents a novel matrix-cube-based estimation of distribution algorithm (MCEDA) to minimize the makespan criterion of the BFSP_SDST. In MCEDA's global search, a matrix cube is devised to reasonably learn the promising patterns in excellent solutions or individuals, and then a matrix-cube-based probabilistic model is developed to quickly guide global search toward the potential promising regions in solution space. A diversity controlling mechanism is also added to avoid the stagnation of global search. In MCEDA's local search, an iterated multi-neighborhood local search controlled by the probabilistic model in global search is designed to execute deeper exploitation from those promising regions. Additionally, two constructive heuristics for generating high-quality initial individuals and one fast Insert-based neighbor evaluation method for accelerating the efficiency of local search are presented based on an analysis of the problem's features. MCEDA's efficacy and superiority in solving the BFSP SDST are demonstrated through comprehensive comparisons with 22 state-of-theart algorithms.

## 1. Introduction

Production scheduling has been recognized as a realistic and reliable decision-making approach for allocating restricted resources within a certain time period in order to achieve one or more decision-makerdefined objectives (Pinedo, 2015). As a hot research topic in the field of production scheduling, the flow-shop scheduling problem (FSP) has a wide range of applications in numerous manufacturing systems, production and assembly lines, and information service facilities. For the typical FSP, it is commonly assumed that there are infinitely storage facilities or buffer units between any two adjacent machines, where finished jobs can be stored in these buffer units for an unlimited amount of time. However, in many real-world manufacturing situations, due to production characteristics and technical constraints, there are usually no intermediate storage units between machines (Grabowski \& Pempera, 2007). In this sense, the traditional FSP is converted into the blocking

FSP (BFSP), which is a typical NP-hard problem in the strong sense (Hall and Sriskandarajah, 1996; Ronconi \& Henriques, 2009; Wang, et al., 2010). As a significant subfield of FSP, BFSP has attracted the considerable attention and interest from both researchers and practitioners in recent decades. A wide variety of real-world industrial processes and manufacturing systems can be modeled as the BFSP, such as chemical and pharmaceutical manufacturing (Ronconi, 2004), iron and steel manufacturing (Gong, et al., 2010), robotic cells (Elmi \& Topaloglu, 2013), serial manufacturing processes (Koren, et al., 2017), and waste treatment (Riahi, et al., 2017). Nowadays, the BFSP has garnered the tremendous attention and interest of both researchers and practitioners (see Section 2).

Setup time is prevalent in a variety of real-life manufacturing systems. In many factories, setup time is frequently derived from nonproductive activities such as cleaning devices, adjusting equipment, switching machines, repairing or releasing jobs, especially in chemical

[^0]
[^0]:    a Corresponding author.
    E-mail addresses: zhangziqi@kust.edu.cn (Z.-Q. Zhang), bin.qian@vip.163.com (B. Qian), wangling@tsinghua.edu.cn (L. Wang), jian-bo.yang@umist.ac.uk (J.-B. Yang).

or pharmaceutical plants. Although in almost all the existing research works related to BFSPs, it is usually assumed that the setup time is negligible or included in processing time, however, substantial setup times should be separable (Shao, et al., 2018b). Nevertheless, the improper handling of setup operations may result in the consumption of more than $20 \%$ of the available machine capacity (Pinedo, 2015). To the best of our knowledge, there are still very few works on BFSP that involve setup time, especially for sequence-dependent setup times (SDST) (Shao, et al., 2018b). Therefore, this paper investigates an extension of the BFSP, namely the BFSP with SDST (BFSP_SDST), whose criterion is to minimize makespan (i.e., $C_{\max }$ ). The SDST indicates that the setup time of each job on each machine depends not only on the job itself but also on its immediately preceding job. According to the widely used three-field notation $a \mid j \mid i j r$ proposed by Graham, et al. (1979), the BFSP under the makespan criterion and the studied problem herein can be denoted as $F m\left(\right.$ blocking $\left|C_{\max }\right.$ and $F m\left(\right.$ blocking. $\left.S T_{\mathrm{ul}}\right) C_{\max }$, respectively. Since $F m\left(\right.$ blocking $\left|C_{\max }\right|$ is already recognized as strongly NP-hard, and it is obviously reduced to $F m\left(\right.$ blocking. $\left.S T_{\mathrm{ul}}\right) C_{\max }$, it can be concluded that $F m\left(\right.$ blocking. $\left.S T_{\mathrm{ul}}\right) C_{\max }$ is also NP-hard in the strong sense.

For the NP-hard scheduling problems, existing mathematical algorithms are often of limited use due to their excessive computation time or poor performance under reasonable runtime. Hence, numerous hybrid intelligent optimization algorithms (HIOAs) have been developed to tackle this issue, aiming to achieve satisfactory solutions for a wide variety of traditional scheduling problems within several seconds or tens of seconds. Among these algorithms, the hybrid estimation of distribution algorithm (HEDA) is a unique one. Unlike the crossover and mutation operators in most existing HIOAs (e.g., hybrid genetic algorithm, hybrid particle swarm optimization algorithm, hybrid differential evolution algorithm), HEDA generates the offspring population by sampling an EDA-based probability model, which can learn and accumulate valuable information about excellent individuals from a macro perspective, as well as establish explicit probability models to effectively estimate the distribution of superior solutions and to predict promising regions in the feasible solution space. To a certain extent, such novel population generation mechanism can avoid the destruction of the blocks (i.e., the partial ordered patterns) in excellent individuals or solutions to a certain extent (Larranga \& Lozano, 2001). Due to its stronger global exploration, simpler framework, and faster convergence speed, HEDA has been widely utilized to solve various scheduling problems (Faraji Amiri \& Behnamian, 2020; Jarboui, et al., 2009; Pan \& Ruiz, 2012; Qian, et al., 2017; Wang, et al., 2014; Wang, et al., 2013; Wu, et al., 2021). These successful applications have indicated that HEDA has considerable competitive advantage against other algorithms. Therefore, HEDA is selected as the main framework of our proposed algorithm for $F m\left(\right.$ blocking. $\left.S T_{\mathrm{ul}}\right) C_{\max }$.

Unfortunately, the majority of currently available HEDAs have two drawbacks. The first drawback is that most existing HEDAs commonly use one or more two-dimensional probabilistic models or matrices to learn the characteristic information of excellent individuals. The structure of two-dimensional matrix directly determines that only the matrix's elements and the subscripts of these elements can be utilized to store information. For the two-dimensional matrix $\boldsymbol{M}_{\boldsymbol{n} \times \boldsymbol{n}}$, its element $M_{n \times n}(\boldsymbol{x}, \boldsymbol{y})$ is used to record the occurrence frequency of the block $\{\boldsymbol{x}, \boldsymbol{y}\}$ in excellent individuals, while the subscript $(x, y)$ is only enough to save the information of one block's structure or pattern. There is no extra space to record the position of this block $\{x, y\}$ in each corresponding excellent individual. This makes it difficult for two-dimensional probabilistic models to correctly guide the search direction, so that the practical performance of the existing HEDAs is relatively limited (see Subsection 4.2.1). The second drawback is that almost all existing HEDAs and other HIOAs lack substantive interaction between their global and local searches. In each of these algorithms, the local search can only execute the neighborhood exploitation by using a very limited number of pre-defined common neighborhood operators (e.g., Insert, Swap, and Interchange). The lack of global exploration information to
assist the local search undoubtedly limits the depth of the local search, resulting in the algorithm's overall practical performance being constrained. To overcome the aforementioned defects, a novel matrix-cubebased HEDA, namely MCEDA, is proposed to address the considered problem.

The main characteristics of our MCEDA are summarized as follows.

- A three-dimensional matrix (i.e., matrix cube) is devised to reasonably record and reserve the valuable patterns in excellent individuals or solutions. For a three-dimensional matrix, the $z$ in its subscript $(x$. $\left.y, z\right)$ is used to record the position of job block $\{x, y\}$ in the corresponding excellent solutions. Meanwhile, a matrix-cube-based probabilistic model with a sampling strategy is developed to estimate the distribution of excellent solutions in solution space and correctly guide global search to promising regions. Moreover, a simple diversity controlling mechanism is designed to avoid the stagnation of global search.
- Different from most existing HIOA's local searches that execute local search independently, a new iterated multi-neighborhood local search controlled by the matrix-cube-based probabilistic model in global search is presented to undertake deeper exploitation from those promising regions. This novel local search utilizes the block patterns saved in the probability model to approximately evaluate neighbors and dynamically create promising neighborhoods for performing fast and rich search.
- Based on the problem's characteristics, two effective constructive heuristics are designed to ensure the quality and diversity of the initial population. Meanwhile, a fast Insert-based neighbor evaluation method is presented to improve search efficiency.
- The proposed MCEDA is compared against twenty-two state-of-theart algorithms on different instances. The statistical results demonstrate the efficacy and superiority of MCEDA.

The remainder of this paper is organized as follows. Section 2 briefly reviews the related literature. Section 3 describes the model of the problem. Section 4 presents MCEDA after explaining two effective heuristics for initialization, the matrix cube based global search, and the probabilistic model controlled local search. The comparison results and statistical analysis are provided in Section 5. Finally, Section 6 gives some concluding remarks and suggestions for future research.

## 2. Literature review of BFSP and BFSP_SDST

The comprehensive review of the BFSP can be found in (Miyata \& Nagano, 2019). Since 2010, there have been mainly three types of algorithms for the BFSP.

The first is the HIOA. The existing studies have mainly concentrated on minimizing the makespan criterion. Wang, et al. (2010) presented a hybrid discrete differential evolution (HDDE), in which a speedup method was utilized to evaluate the Insert-based neighbor solutions. The test results showed that HDDE outperformed the famous tabu search (TS) algorithm (Grabowski \& Pempera, 2007). Wang, et al. (2011) developed a hybrid modified global-best harmony search (hmgHS), which performed better than HGA (Wang, et al., 2011) and TS (Grabowski \& Pempera, 2007). Wang, et al. (2012) devised a three-phase algorithm (TPA), in which a priority rule, a NER's variant, and a modified simulated annealing are utilized in three phases, respectively. The comparative results demonstrated that TPA was relatively more efficient than HDDE (Wang, et al., 2010). Lin and Ying (2013) proposed a revised artificial immune system (RAIS) algorithm, where a simple iterated greedy algorithm (IGA) was embedded to intensively exploit around the better solutions. The test results indicated that the RAIS was superior to both HDDE (Wang, et al., 2010) and IGA (Ribas, et al., 2011). Han, et al. (2015) designed a discrete artificial bee colony algorithm incorporating differential evolution (DE_ABC). The test results demonstrated that DE_ABC was superior to the compared algorithms.

Tasgetiren, et al. (2015) presented a populated local search with differential evolution (DE_PLS). The test results showed that DE_PLS performed better than some of the best performing algorithms from the literature. Han, et al. (2016) introduced a modified fruit fly optimization (MFFO) algorithm, in which a problem-specific heuristic, a neighborhood strategy, and a speedup insert-neighborhood based local search are employed. Shao, et al. (2018a) developed an EDA with a path relinking technique (P-EDA). The path relinking technique here is utilized to avoid performing the blind search. The results compared with various other high-performing algorithms verified the effectiveness of P-EDA. Shao, et al. (2019) proposed a discrete invasive weed optimization (DIWO), in which a random-insertion-based spatial dispersal, a shufflebased referenced local search, and an improved competitive exclusion are devised. The results demonstrated that DIWO outperformed the compared algorithms. Besides the makespan minimization, Ribas, et al. (2015) devised an effective discrete artificial bee colony algorithm (DABC_RCT) for minimizing the total flowtime criterion. Shao, et al. (2017) presented a self-adaptive discrete invasive weed optimization (SaDIWO), and Nagano, et al. (2017) designed an evolutionary clustering search (ECS) algorithm to minimize the total tardiness criterion.

The second is the constructive heuristic. As for the makespan minimization, Pan and Wang (2012) introduced six effective heuristics, namely PF-NEH $(x)$, wPF-NEH $(x)$, PW-NEH $(x)$, PF-NEH $\left._{L S}(x), \mathrm{wPF}-\right.$ $\mathrm{NEH}_{L S}(x)$, and PW-NEH $\left._{L S}(x), \mathrm{in}\right.$ which the variable $x$ is employed to control the number of sequences generated. The test results demonstrated that PW-NEH $\left._{L S}(S)\right.$ beat NEH (Nawaz, et al., 1983), MME (Ronconi, 2004), and PFE (Ronconi, 2004). As for the total flowtime minimization, Tasgetiren, et al. (2016) developed a variable block insertion heuristic (VBIH), and Fernandez-Viagas, et al. (2016) proposed an effective beam-search- based heuristic (BSH).

The third is the iterated greedy algorithm (IGA). As for the makespan minimization, Tasgetiren, et al. (2017) devised two enhanced IGAs, i.e., iterated greedy with jumping probability (IG_U) and iterated greedy with RIS local search (IG_RIS), which combined an effective constructive heuristic and employed two speedup methods for the insert-based and swap-based neighborhood searches, respectively. Extensive experimental results demonstrated that the devised algorithms achieved better results than most state-of-the-art algorithms. Ribas, et al. (2013) proposed two competitive variable neighborhood search methods (namely SVNS_S and SVNS_D). The experimental results revealed that SVNS outperformed both HDDE (Wang, et al., 2010) and IGA (Ribas, et al., 2011). Moslehi and Khorasanian (2014) developed a hybrid variable neighborhood search (HVNS), whose performance surpassed several state-of-the-art algorithms. As for the total flowtime minimization, Khorasanian and Moslehi (2012) presented an IGA, in which a modified NEH was employed to generate the initial solution. Ding, et al. (2016) investigated several properties of the BFSP and presented an IGA based on these problem-specific properties.

Recently, several researchers studied the BFSP_SDST and the other BFSP's variants, and they all adopted HIOA to address the corresponding problems. Shao, et al. (2018b) devised a novel discrete water wave optimization (DWWO) to minimize the makespan of the BFSP_SDST. In DWWO, a path relinking technique and a variable neighborhood search (VNS) are employed to further improve the algorithm's performance. The test results indicated that DWWO defeated several highly effective algorithms. Nouri and Ladhari (2018) introduced a multi-objective genetic algorithm (MBGA) for the BFSP that considers minimizing both the makespan and the total completion time. Gong, et al. (2018) developed a hybrid artificial bee colony (HABC) to minimize the makespan and the earliness of the lot-streaming BFSP. Han, et al. (2019) designed a robust multi-objective evolutionary algorithm to minimize the makespan, the tardiness and the robustness of the lot-streaming BFSP with machine breakdowns. Han, et al. (2020) presented an effective multi-objective discrete evolutionary optimization (MDEO) to minimize the makespan and the energy consumption of the energy-efficient BFSP_SDST. Ribas, et al. (2021) proposed an enhanced IGA to minimize the makespan of the

Table 1
Notations applied in the model of BFSP_SDST.

| Parameters |  |
| :--: | :--: |
| $n$ | The total number of jobs. |
| $m$ | The total number of machines. |
| $J$ | The set of jobs, i.e., $J=\left\{J_{1}, J_{2}, \ldots, J_{n}\right\}$. |
| $M$ | The set of machines, i.e., $M=\left\{M_{1}, M_{2}, \ldots, M_{m}\right\}$. |
| Indices |  |
| $i$ | The index of jobs $(i=1,2, \ldots, n)$. |
| $j$ | The index of machines $(j=1,2, \ldots, m)$. |
| Variables |  |
| $\boldsymbol{\pi}$ | The processing order of jobs, i.e., $\boldsymbol{\pi}=\{e(1), e(2), \ldots, e(n)\}$. $x(i)$ is a dummy job. |
| $\Pi$ | The set of all feasible schedules. |
| $O_{i, j}$ | The operation corresponding to processing of job $J_{i}$ on machine $M_{j}$. |
| $p_{e(i), j}$ | The processing time of operation $O_{e(i), j}$. |
| $S_{e(i-1), e(i), j}$ | The setup time between two consecutive jobs $x(i-1)$ and $x(i)$ on machine $M_{j} . S_{e(i), e(i), j}$ is the initial setup time of job $x(i)$. |
| $d_{e(i), j}$ | The departure time of job $x(i)$ on machine $M_{j}$. $d_{e(i), 0}$ is the start time of job $x(i)$ on machine $M_{j}$. |
| $f_{e(i), j}$ | The duration time between the starting time of $x(i)$ on $M_{j}$ and the starting time of the last job on the same machine. |
| $C_{\text {max }}(\boldsymbol{\pi})$ | The makespan of a sequence or schedule $\boldsymbol{\pi}$. |

parallel BFSP_SDST. Shao, et al. (2021) devised an effective constructive heuristic and an IGA to minimize the makespan of the distributed mixed BFSP. Zhao, et al. (2022) developed an effective water wave optimization to minimize the total tardiness of the distributed assembly BFSP.

From the above literature, it can be seen that although researchers have undertaken much research on the BFSP and its variants, only Shao, et al. (2018b) considers the SDST in the BFSP. Thus, it is necessary and meaningful to consider such a significant problem.

## 3. Problem statement

### 3.1. permutation-based model

The BFSP_SDST can be briefly described as follows. There are $n$ jobs and $m$ machines in a flow shop without intermediate buffers. Each job $J_{i} \in J$ has a sequence of operations $\left\{O_{i, 1}, O_{i, 2}, \ldots, O_{i, m}\right\}$ to be processed sequentially on machine $M_{1}, M_{2}$, and so on until machine $M_{m}$. The operation $O_{i, j}$ of job $J_{i}$ should be executed on machine $M_{j}$ with a period of processing time $p_{i, j}$. Since there are no buffers between consecutive machines and each machine has to take some time to prepare before processing, jobs that have completed all operations must remain on the current machine if the downstream machine is not free or not prepared for processing. Setup times are considered sequence-dependent and separable from processing times. In addition, the following assumptions must be met:

- The processing time of each job on each machine is a positive integer and predetermined.
- The release time and transportation time of all jobs are negligible. All jobs are independent and available from zero onwards.
- At any time, each job can be processed on at most one machine, and each machine can only process at most one job.
- Preemption is not permitted. Each job is processed without interruption on each machine.

The related notations are provided in Table 1. According to the above description, the permutation-based model of BFSP_SDST can be established as follows.
$d_{e(0), j}=0, j=1,2, \ldots, m$,
$d_{e(i), 0}=d_{e(i-1), 1}+S_{e(i-1), e(i), 1}, i=1,2, \ldots, n$,

Table 2
Processing and setup times of an example of BFSP_SDST.

| Process time |  |  |  |  |  | Sequence-dependent setup time |  |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  |  | Machine 1 |  | Machine 2 |  |  | Machine 3 |  |  |  |
|  | $M_{1}$ | $M_{2}$ | $M_{3}$ | $x(1)$ | $x(2)$ | $x(3)$ | $x(1)$ | $x(2)$ | $x(3)$ | $x(1)$ | $x(2)$ | $x(3)$ |
| $x(0)$ | 0 | 0 | 0 | 2 | 1 | 4 | 1 | 2 | 3 | 2 | 3 | 3 |
| $x(1)$ | 1 | 3 | 2 | 0 | 1 | 2 | 0 | 3 | 1 | 0 | 1 | 4 |
| $x(2)$ | 1 | 2 | 1 | 3 | 0 | 4 | 4 | 0 | 2 | 1 | 0 | 1 |
| $x(3)$ | 3 | 2 | 1 | 2 | 2 | 0 | 3 | 4 | 0 | 2 | 3 | 0 |

$d_{x(i), j}=\max \left\{d_{x(i), j-1}+p_{x(i), j}, d_{x(i-1), j+1}+S_{x(i-1), x(i), j+1}\right\}$
$i=1,2, \ldots, n ; j=1,2, \ldots, m-1$
$d_{x(i), m}=d_{x(i), m-1}+p_{x(i), m}, i=1,2, \ldots, n$
$C_{\max }(\boldsymbol{x})=d_{x(x), m}$
Eq. (1) determines the departure time of the dummy job $x(0)$ on all machines. Eq. (2) calculates the starting time of each job on the first machine. Eq. (3) calculates the departure time of each job on all machines except the last machine. Eq. (4) calculates the departure time or completion time of each job on the last machine. Eq. (5) is the maximum completion time (i.e., makespan) of $\boldsymbol{x}$. The aim of $F m \mid$ blocking. $S T_{s t} \mid C_{\max }$ is to find an optimal solution $x^{*}$ in the schedule set II such that.
$x^{*}=\arg \min _{x \in \mathrm{II}}\left\{C_{\max }(\boldsymbol{x})\right\}$
In contrast to mathematical models of FSPs, the permutation-based models have no explicitly expressed constraints. For the permutationbased model of BFSP_SDST, the constraints are implicit in Eqs. (1)-(4), which stipulate that each job $x(i)$ on the current machine $M_{j}$ can only depart to the next machine $M_{j+1}$ under three conditions: (1) the operation $O_{x(i), j}$ has been completed, (2) the job $x(i+1)$ has already departed machine $M_{j+1}$, and (3) the setup operation between $x(i)$ and $x(i+1)$ on machine $M_{j+1}$ has been completed. When a solution $\boldsymbol{x}$ contains different jobs, the departure times of these jobs on each machine are determined by using Eqs. (1)-(4) and no constraints are violated. Thus, a solution $\boldsymbol{x}$ is feasible if and only if all jobs in that solution are different from each other.

In the following proposed MCEDA, both the new population sampling strategy in global search (see Section 4.2) and the new neighbor generation methods in local search (see Section 4.3) can ensure that the jobs in each solution $\boldsymbol{x}$ (i.e., individual or neighbor) are different from each other. That is to say, any solution $\boldsymbol{x}$ obtained in MCEDA is always feasible. Indeed, the most of existing HIOAs optimize the variables of the permutation-based models since researchers using such models can concentrate on the design of the algorithm without considering complex constraint handling.

### 3.2. permutation-based model using backward calculation

According to the computational reversibility of the permutationbased model of FSPs (Tasgetiren, et al., 2017; Wang, et al., 2010), the makespan (i.e. $C_{\max }(\boldsymbol{x})$ ) of the solution $\boldsymbol{x}$ can be computed by traversing the solution $\boldsymbol{x}$ in reverse order. The backward calculation is described as follows:
$f_{x(x), m+1}=0$
$f_{x(x), j}=f_{x(x), j+1}+p_{x(x), j}, j=m, m-1, \ldots, 2$,
$f_{x(i), n+1}=f_{x(i+1), m}+S_{x(i), x(i+1), m}$,
$i=n-1, \ldots, 1,0$,
$f_{x(i), j}=\max \left\{f_{x(i), j+1}+p_{x(i), j}, f_{x(i+1), j-1}+S_{x(i), x(i+1), j}\right\}$
$i=n-1, \ldots, 2,0 ; j=m, m-1, \ldots, 2$
$f_{x(i), i}=f_{x(i), 2}+p_{x(i), 1}, i=n, n-1, \ldots, 0$,
$C_{\max }(\boldsymbol{x})=f_{x(0), 1}$
So, $C_{\max }(\boldsymbol{x})$ can be calculated not only forward via Eqs. (1)-(5) but also backward via Eqs. (7)-(12) with complexity of $O(n m)$. With Eqs. (7) (12) and Eq. (6), another form of the permutation model of $F m \mid$ blocking. $S T_{\mathrm{st}} \mid C_{\max }$ can be established.

Furthermore, for $1 \leqslant i \leqslant n-1$, it has.
$C_{\max }(\boldsymbol{x})=\max _{j=1,2, \ldots, m}\left\{d_{x(i), j}+S_{x(i), x(i+1), j}+f_{x(i+1), j}\right\}$
With Eq. (13), a fast neighbor evaluation method (see Subsection 4.3.1) can be devised to calculate the objective functions of the solutions in the insertion neighborhood for $F m \mid$ blocking. $S T_{\mathrm{st}} \mid C_{\max }$. This fast neighbor evaluation method is adopted to speed up the efficiency in MCEDA's local search.

### 3.3. Small numerical example of the forward and backward calculations

To illustrate the forward and backward calculations, a small example with three jobs and three machines is provided. Table 2 shows the processing and setup times of jobs. Let the processing order of jobs be $x=|x(2), x(1), x(3)|$. The departure time of each job is determined by using Eqs. (1)-(4) as follows:
$d_{x(2), 0}=d_{x(0), 1}+S_{x(0), x(2), 1}=3 ; d_{x(2), 1}=\max \left\{d_{x(0), 2}+S_{x(0), x(2), 2}\right.$, $\left.d_{x(2), 0}+p_{x(2), 1}\right\}=6 ; d_{x(2), 2}=\max \left\{d_{x(0), 3}+S_{x(0), x(2), 3}, d_{x(2), 1}+p_{x(2), 2}\right\}=$ $10 ; d_{x(2), 3}=d_{x(2), 2}+p_{x(2), 3}=14 ; d_{x(1), 0}=d_{x(2), 1}+S_{x(2), x(1), 1}=$ $9 ; d_{x(1), 1}=\max \left\{d_{x(2), 2}+S_{x(2), x(1), 2}, d_{x(1), 0}+p_{x(1), 1}\right\}=13 ; d_{x(1), 2}=$ $\max \left\{d_{x(2), 3}+S_{x(2), x(1), 3}, d_{x(1), 1}+p_{x(1), 2}\right\}=18 ; d_{x(1), 3}=d_{x(1), 2}+p_{x(1), 3}=$ $20 ; d_{x(3), 0}=d_{x(1), 1}+S_{x(1), x(3), 1}=15 ; d_{x(3), 1}=\max \left\{d_{x(1), 2}+S_{x(1), x(3), 2}\right.$, $\left.d_{x(3), 0}+p_{x(3), 1}\right\}=20 ; d_{x(3), 2}=\max \left\{d_{x(1), 3}+S_{x(1), x(3), 3}, d_{x(3), 1}+p_{x(3), 2}\right\}=$ $24 ; d_{x(3), 3}=d_{x(3), 2}+p_{x(3), 3}=27$.

Then, based on the forward calculation (see Eqs. (1)-(5)), it has $C_{\max }(\boldsymbol{x})=d_{x(3), 3}=27$.

According to Eqs. (7)-(11), the duration time of each job in $x$ can be computed as follows:
$f_{x(3), 3}=f_{x(3), 4}+p_{x(3), 3}=3 f_{x(3), 2}=f_{x(3), 3}+p_{x(3), 2}=5 ; f_{x(3), 1}=$ $f_{x(3), 2}+p_{x(3), 1}=7 ; f_{x(1), 4}=f_{x(3), 3}+S_{x(1), x(3), 3}=7 ; f_{x(1), 3}=\max \left\{f_{x(3), 2}+\right.$ $\left.S_{x(1), x(3), 2}, f_{x(1), 4}+p_{x(1), 3}\right\}=9 ; f_{x(1), 2}=\max \left\{f_{x(3), 1}+S_{x(1), x(3), 1}, f_{x(1), 3}+\right.$ $\left.p_{x(1), 2}\right\}=12 ; f_{x(1), 1}=f_{x(1), 2}+p_{x(1), 1}=14 ; f_{x(2), 4}=f_{x(1), 3}+S_{x(2), x(1), 3}=$ $13 ; f_{x(2), 3}=\max \left\{f_{x(1), 2}+S_{x(2), x(1), 2}, f_{x(2), 4}+p_{x(2), 3}\right\}=17 ; f_{x(2), 2}=$ $\max \left\{f_{x(1), 1}+S_{x(2), x(1), 1}, f_{x(2), 3}+p_{x(2), 2}\right\}=21 ; f_{x(2), 1}=f_{x(2), 2}+p_{x(2), 1}=$ $24 ; f_{x(0), 4}=f_{x(2), 3}+S_{x(0), x(2), 3}=20 ; f_{x(0), 3}=\max \left\{f_{x(2), 2}+S_{x(0), x(2), 2}\right.$, $\left.f_{x(0), 4}+p_{x(0), 3}\right\}=25 ; f_{x(0), 2}=\max \left\{f_{x(2), 1}+S_{x(0), x(2), 1}, f_{x(0), 3}+p_{x(0), 2}\right\}=$ $27 ; f_{x(0), 1}=f_{x(0), 2}+p_{x(0), 1}=27$.

Then, based on the backward calculation (see Eqs. (7)-(12)), it has $C_{\max }(\boldsymbol{x})=f_{x(0), 1}=27$.

To be more intuitive, we draw Gantt charts illustrating the forward and backward calculations in Fig. 1. As shown in Fig. 1, the front delay is determined by the first job in $x$, and the non-processing time of the machine includes both the blocking time and idle time.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The Gantt chart of BFSP_SDST with two calculations.

## 4. MCEDA for BFSP_SDST

In this section, the matrix-cube-based estimation of distribution algorithm (MCEDA) is proposed to address the BFSP_SDST with makespan criterion. In the following subsections, the heuristic and initialization, the multi-dimensional probabilistic model, the diversity controlling mechanism, the multi-neighborhood based local search are firstly described in detail, and then the MCEDA's framework is outlined. Meanwhile, the analysis of MCEDA's computational complexity is provided.

### 4.1. Heuristic and initialization

The solution representation has a significant effect on the performance of HIOAs. As is reported in the literature, the permutation-based representation has been widely used for various FSPs (Shao, et al., 2017, 2018a, 2018b). Therefore, we utilize the permutation-based encoding scheme to describe feasible solutions to the BFSP_SDST. Each solution corresponds to a specific scheduling scheme for the problem under consideration. Note that the quality of the initial population has an important impact on the search efficiency of HIOAs. If all initial solutions are generated randomly, their quality cannot be guaranteed. Conversely, the initial population formed only by constructive heuristics may be deficient in diversity and dynamism, resulting in premature convergence (Wang, et al., 2010). Some better initial solutions can narrow the search scope suitably, especially for the large-scale instances. Therefore, the initial population should be constructed with a certain quality, i.e., only a few high-quality individuals should be formed via heuristics, while the others are generated randomly. To balance quality and diversity, the population is initialized by using a hybrid strategy. In this section, combining the problem characteristics of BFSP_SDST, the $\operatorname{PFT}_{-} \mathrm{NEH}(x)$ heuristic based on the PFT and NEH heuristics (Tasgetiren, et al., 2017) and the PFZ_RZ(x) heuristic based on the PFZ and RZ heuristics (Rajendran \& Ziegler, 1997) are proposed to generate some initial individuals.

### 4.1.1. PFT_NEH(x) heuristic

The NEH heuristic (Nawaz, et al., 1983) is a straightforward but pretty powerful constructive heuristic for PFSP and BFSP with makespan criterion in the literature (Pan \& Wang, 2012, Tasgetiren, et al., 2017; Wang, et al., 2010). The basic idea behind the NEH heuristic is that jobs with a longer total processing time should be given higher priority.

However, when blocking constraints are taken into account, providing higher priority to jobs with a longer total processing time may result in blocking of jobs between machines, yielding in a larger front delay (Wang, et al., 2010). With a longer front delay, the total idle and blocking times may be increased, resulting in decreased machine utilization and increased maximum completion time. Therefore, a suitable strategy for the BFSP is to prioritize jobs with both smaller total processing time and shorter front delay. As illustrated in Fig. 1, when determining the priority of jobs, the total idle and blocking times of machines, as well as the front delay of jobs, must be considered. Numerous studies in the existing literature have shown that after producing the initial sequence, applying the NEH heuristic (Nawaz, et al., 1983) may considerably improve the solution quality. Thus, the PF heuristic (McCormick, et al., 1989) coupled with the NEH heuristic, i.e., $\operatorname{PF}_{-} \mathrm{NEH}(x)$, is proposed to solve the BFSP with makespan criterion (Pan \& Wang, 2012). The outline of the PF heuristic is given in Algorithm 1. For the PF heuristic, the initial job at the first position in the partial sequence is determined by the shortest total processing time. Then, it prioritizes the other jobs by using the total idle and blocking times as a cost function. However, it is obvious that the front delay of the first job cannot be ignored and should be taken into account (Ribas, et al., 2015). Tasgetiren, et al. (2017) tackled such issue by extending the PF heuristic and developing the PFT heuristic, which is an effective heuristic for solving $F m /$ blocking $/ C_{\max }$. In this subsection, the PFT heuristic is also adapted to address the $F m /$ blocking_SDSTs $/ C_{\max }$. In the PFT heuristic, it prioritizes the jobs by an indicator $I(i)$ that contains the front delay and total processing time. After ascending each job according to $I(i)$, an initial sequence of jobs is obtained. The indicator $I(i)$ can be calculated by the formula in Eq. (14).
$I(i)=\left(\sum_{j=1}^{m}(m-j) p_{i, j}\right) \frac{2}{m-1}+\sum_{j=1}^{m} p_{i, j}$,
$i=1,2, \ldots, n$.
According to Eq. (14), the job with the lowest priority indicator is obtained, and such job is chosen as the first job in the initial sequence. Then, the rest of the jobs are added to the initial sequence via the cost index $n_{i}$ to produce a complete candidate solution. To be specific, let $U$ be the set of unscheduled jobs and $\tilde{\boldsymbol{s}}=\left|\tilde{s}(1), \tilde{s}(2), \ldots, \tilde{s}(i-1)\right|$ be a partial sequence containing $i-1$ jobs. In order to determine the job $\tilde{s}(i)$ at the $i$ th position in $\tilde{s}$, each of the $n-i+1$ unscheduled jobs is attempted to be placed at such position, and the job with the lower cost index value is

placed at the $i$ th position of $\bar{x}$. The cost index $e_{i}$ is given in Eq. (15).
$e_{i}=(n-i-2) \sum_{j=1}^{m}\left(d_{i, j}-d_{i-1, j}-p_{i, j}\right)+d_{i, m}$
Obviously, if job $\bar{x}(i)$ is added to the partial sequence $\overline{\boldsymbol{x}}$ with a minimum cost index $e_{0}$, it means that the total idle and blocking time, as well as the departure time of job $\bar{x}(i)$ on the last machine, are all minimized. Therefore, the PFT heuristic is used to determine an initial feasible solution $\pi=[x(1), x(2), \ldots, x(n)]$, and the NEH heuristic is used to further
improve the quality of such solution. Let $\overline{\boldsymbol{x}}^{1}=[x(1), x(2), \ldots, x(n-\lambda)]$ and $\overline{\boldsymbol{x}}^{2}=[x(n-\lambda+1), x(n-\lambda+2), \ldots, x(n)]$ be two subsequences of $\pi$. Each job in $\overline{\boldsymbol{x}}^{2}$ is extracted and reinserted into all possible positions in $\overline{\boldsymbol{x}}^{1}$, and the best position for each job extracted in $\overline{\boldsymbol{x}}^{2}$ is determined and then inserted it into $\overline{\boldsymbol{x}}^{1}$ till a new solution $\pi$ is formed. According to the PF$\operatorname{NEH}(x)$ proposed by Pan and Wang (2012), the PFT heuristic that incorporates the NEH heuristic is denoted as $\operatorname{PFT} \operatorname{NEH}(x)$, as detailed in Algorithm 2.

# Algorithm 1: Profile fitting (PF) 

Input: The processing time of jobs $p_{\pi(i), j}, i=1, \ldots, n ; j=1, \ldots, m$.
Output: An initial solution $\pi$.
for $i=1$ to $n$ do
Calculate the total processing time of each job, i.e.,

$$
T P(i)=\sum_{j=1}^{m} p_{i, j} ; / / o b t a i n \text { total processing time. }
$$

## 3: end for

4: Select a job with the smallest $T P$ as the initial job. Set $\boldsymbol{\pi}=[\pi(1)]$.
5: $U \leftarrow J-\{\pi(1)\}$. Let job in $U$ be $\pi_{u}(t), t=1,2, \ldots,|U|$.
for $i=1$ to $n-2$ do
Compute the departure time $d_{\pi(i), j}$ for $\pi=[\pi(1), \pi(2), \ldots, \pi(i)]$.
for $t=1$ to $|U|$ do
Compute the departure time $d_{\pi_{u}(t), j}=d_{\pi(i+1), j}$. If job $\pi_{u}(t)$ is appended and became the $(i+1)$ th job in partial sequence $\pi$.
Compute the sum of idle and blocking time.

$$
\delta_{\pi_{u}(t), i}=\sum_{j=1}^{m}\left(d_{\pi(i+1), j}-d_{\pi(i), j}-p_{\pi_{u}(t), j}\right)
$$

11: Select a job resulting in smallest $\delta_{\pi_{u}(t), i}$ as the $(i+1)$ th job in $\pi$. Remove the selected job $\pi_{u}(t)$ from the unscheduled job set $U$. end for
13: end for
14: The last job in $U$ is directly appended to $\pi$ as the $n$th job of $\pi$.
15: return $\pi$.

# Algorithm 2:PFT_NEH $(x)$ 

Input: $\pi, \tilde{\boldsymbol{\Pi}}, x, \lambda$.
Output: The best solution $\pi$ in $\tilde{\boldsymbol{\Pi}}$.
1: Initial solution set $\tilde{\boldsymbol{\Pi}}$. Set $\tilde{\boldsymbol{\Pi}} \leftarrow \varnothing$.
2: Initial sequence $\hat{\pi}=[\hat{\pi}(1), \hat{\pi}(2), \ldots, \hat{\pi}(n)]$ is obtained by ascending jobs in unscheduled job set $U$ according to the priority indicator $I(i)$.
for $i=1$ to $x$ do
Select job $\hat{\pi}(i)$ from $\hat{\pi}=[\hat{\pi}(1), \hat{\pi}(2), \ldots, \hat{\pi}(n)]$ as the initial job in $\pi$.
5: Perform the PFT heuristic to produce a solution $\pi$. Set $\tilde{\boldsymbol{\Pi}} \leftarrow \tilde{\boldsymbol{\Pi}} \cup \pi$.
6: Divide $\pi=[\pi(1), \pi(2), \ldots, \pi(n)]$ into two partial sequences by $\lambda$,
$\hat{\pi}^{\mathbf{1}}=[\pi(1), \pi(2), \ldots, \pi(n-\lambda)], \hat{\pi}^{\mathbf{2}}=[\pi(n-\lambda+1), \pi(n-\lambda+2), \ldots, \pi(n)]$.
for $k=n-\lambda+1$ to $n$ do //NEH heuristic.
Select job $\pi(k)$ from $\pi$ and reinsert it into $n-\lambda+1$ possible positions of $\hat{\pi}^{\mathbf{1}}$ to obtain $n-\lambda+1$ partial sequences.
Select a partial sequence resulting in the lowest makespan.
end for
11: Obtain a new feasible solution $\pi^{\prime}$. Set $\tilde{\boldsymbol{\Pi}} \leftarrow \tilde{\boldsymbol{\Pi}} \cup \pi^{\prime}$.
12: end for
13: return $\tilde{\boldsymbol{\Pi}}$.

In Algorithm 2, the value of $x$ in the first layer loop directly determines the number of solutions obtained in $\Pi$, and the value of $\lambda$ in the second loop controls the number of jobs to be inserted by the NEH heuristic. Note that the tie-breaking strategy is utilized in both the ordering and constructing phases if two jobs with the same $I(i)$ or two positions result in the same $n_{i}$. It is clear that there are $(2 n-\lambda+1) \lambda / 2$ partial sequences that need to be calculated in the NEH heuristic of the PFT_NEH $(x)$. It should be noted that the fast Insert-based neighbor evaluation method explained in Subsection 4.3.1 is employed in the NEH heuristic, and its complexity can be reduced from $O\left(\mathrm{~mm}^{3}\right)$ to $O\left(\mathrm{~mm}^{2}\right)$. Thus, Algorithm 2 has a total complexity of about $O\left(\mathrm{xmm}^{2}\right)$.

### 4.1.2. PFZ_RZ(x) heuristic

The RZ heuristic is an effective heuristic proposed by Rajendran and Ziegler (1997). As with the PFT heuristic, the RZ heuristic can construct a complete solution sequence from a partial sequence by using basic insertion neighborhood. However, when the RZ heuristic is used to construct a solution, the jobs to be inserted are chosen according to a specified reference sequence. Consider two solution sequences $[3,5,4,1,2]$ and $[1,2,3,4,5]$, each consisting of five jobs, and assume that the former is a reference sequence and the latter is an incumbent sequence. The RZ heuristic first removes job 3 from the incumbent sequence $[1,2,3,4,5]$ and reinserts it into all possible positions of the incumbent sequence. Then, it removes job 2 from the incumbent sequence to execute the insertion operation. This procedure is repeated until all jobs in the reference sequence are already picked and the best feasible solution is produced. It is crucial to create the reference sequence of the RZ heuristic as the baseline. As shown in Eq. (14), two sorts of indicators, namely the front delay of the first job (i.e., $\sum_{d=1}^{m}\left(m-j / p_{i, j}\right)$ and the total processing time of each job (i.e., $\sum_{d=1}^{m}\left(p_{i, j}\right)$, have an impact on the performance of heuristics for solving BFSP. However, besides these two indicators, the average processing time, the standard deviation of processing time, and the skewness should be considered depending on the problem's characteristics. Since the strong
correlation between skewness and front delay, if skewness is small, front delay may likewise decrease. The formulas for these indicators are given in Eqs. (16) to (18):
$T_{\text {avg }}(i)=\frac{1}{m}\left(\sum_{j=1}^{m} p_{i, j}\right)$
$T_{\text {sal }}(i)=\sqrt{\frac{1}{m-1} \sum_{j=1}^{m}\left(p_{i, j}-T_{\text {avg }}(i)\right)^{2}}$,
$T_{\text {dx }}(i)=\frac{\frac{1}{m}\left(\sum_{d=1}^{m}\left(p_{i, j}-T_{\text {avg }}(i)\right)^{3}\right)}{\left(\sqrt{\frac{1}{m}\left(\sum_{j=1}^{m}\left(p_{i, j}-T_{\text {avg }}(i)\right)^{3}\right.}\right)^{3}}$.
Based on Eqs. (17)-(18), the newly proposed job priority indicator $I_{Z}(i)$ is shown in Eq. (19).
$I_{Z}(i)=\left(\sum_{j=1}^{m}(m-j) p_{i, j}\right) \frac{2}{m-1}+\left(T_{\text {sal }}(i)+T_{\text {dx }}(i)\right), i=1,2, \ldots, n$.
Each job $J_{i}$ in the job set $J$ is arranged in ascending order according to the $I_{Z}(i)$ in Eq. (19) to produce a job sequence that serves as a reference sequence for the RZ heuristic. As with PFT_NEH $(x)$ in Subsection 4.1.1, the initial solution for the RZ heuristic is produced by using a newly presented heuristic, namely the PFZ heuristic, and then the Insert-based neighborhood search is performed on the initial solution in accordance with the order of jobs in the reference sequence. If an improvement is achieved, the worse solution is replaced by a new one and then the cycle continues. According to the above considerations, the PFZ_RZ $(x)$ heuristic is proposed in this subsection by incorporating the PFZ heuristic and the RZ heuristic (see Algorithm 3). In PFZ_RZ $(x)$, a total of $x$ feasible solutions are generated. Each solution produced by PFZ_RZ $(x)$ needs to

calculate $(n-1)^{2}$ neighbor solutions. In order to reduce the computational cost and speed up the neighborhood search, the fast Insert-based neighbor evaluation method can be used in the implementation of Algorithm 3 to effectively decrease the total time complexity. It is clear that the complexity of Algorithm 3 is $O\left(x \mathrm{~mm}^{2}\right)$, which is the same as that of Algorithm 2. According to the relevant conclusions in the literature (Pan, et al., 2013), the parameter of two heuristics, $\operatorname{PFT} \_\operatorname{NEH}(x)$ and $\operatorname{PFZ} \_\operatorname{RZ}(x)$, is set to $\lambda=20$ and $x=5$.

To be specific, $10 \%$ of the solutions in the initial population are created by $\operatorname{PFT} \_\operatorname{NEH}(x)$, whereas $10 \%$ are produced by $\operatorname{PFZ} \_\operatorname{RZ}(x)$. The remaining $80 \%$ of solutions are randomly generated. Due to the fact that the two proposed heuristics are designed according to the problem's characteristics, the initial population with high-quality individuals or solutions may contain rich and valuable structural features and promising patterns. Hence, it may be desirable to expend a certain amount of computational effort to generate high-quality initial population.
4.2.1.1. Matrix cube. In order to effectively extract excellent structural features or promising patterns from quality individuals in a population, a matrix cube structure is designed to capture these valuable structural features and to reasonably retain promising patterns. Let $\boldsymbol{P o p}(\boldsymbol{g e n})$ be the population at generation gen, and $\boldsymbol{S P o p}(\boldsymbol{g e n})$ be the high-quality subpopulation or superior solutions derived from $\boldsymbol{P o p}(\boldsymbol{g e n})$, i.e., $\boldsymbol{S P o p}(\boldsymbol{g e n})=$ $\left\{\boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, k}, \boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, 2}, \ldots, \boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }} \text {, }_{2}\right\}$, where popsize and spsize respectively represent the size of $\operatorname{Pop}(\boldsymbol{g e n})$ and $\boldsymbol{S P o p}(\boldsymbol{g e n})$, gen $=1.2 \ldots$ maxgen. maxgen is the maximum number of runs of the algorithm. Let $\boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, k}$ be the $k$ th individual in $\boldsymbol{S P o p}(\boldsymbol{g e n})$, i.e., $\boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, k}=\left[\boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, k}(1), \boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, k}(2), \ldots, \boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, k}(n)\right], k=1$, ..., spsize. Without loss of generality, $\boldsymbol{M C}_{\boldsymbol{n} \times \boldsymbol{n} \times \boldsymbol{n}}^{\text {gen }}$ is defined as the matrix cube at generation gen. $M C_{\boldsymbol{n} \times \boldsymbol{n} \times \boldsymbol{n}}^{\text {gen }}(x, y, z), x, y, z \in\{1,2, \ldots, n\}$ is the element in $\boldsymbol{M C}_{\boldsymbol{n} \times \boldsymbol{n} \times \boldsymbol{n}}^{\text {gen }}$ with the ternary subscript $(x, y, z)$, where $x$ corresponds to the $x$ th position of the solution sequence, and $(y, z)$ is used to represent the job block $[y, z]$ at that position. Firstly, for the $k$ th individual $\boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, k}$ in $\boldsymbol{S P o p}(\boldsymbol{g e n})$, the sequential relationship of the job

# Algorithm 3:PFZ_RZ $(x)$ 

Input: $\pi, \overline{\mathbf{n}}, x, \lambda$.
Output: The best solution $\boldsymbol{\pi}$ in $\overline{\mathbf{n}}$.
1: Initial solution set $\overline{\mathbf{n}}$. Set $\overline{\mathbf{n}} \leftarrow \varnothing$.
2: Initial sequence $\hat{\boldsymbol{\pi}}=[\hat{\pi}(1), \hat{\pi}(2), \ldots, \hat{\pi}(n)]$ is obtained by ascending jobs in the unscheduled job set $U$ according to the priority indicator $I(i)$.
3: Obtain reference sequence $\boldsymbol{\pi}^{k}=\left[\pi^{x}(1), \pi^{x}(2), \ldots, \pi^{x}(n)\right]$ by ascending jobs in $U$ according to the priority indicator $I_{Z}(i)$ in Eq. (19).
4: for $i=1$ to $x$ do
5: Select job $\hat{\pi}(i)$ from $\hat{\boldsymbol{\pi}}=[\hat{\pi}(1), \hat{\pi}(2), \ldots, \hat{\pi}(n)]$ as the initial job in $\boldsymbol{\pi}$.
6: Perform the PFZ heuristic to produce a solution $\boldsymbol{\pi}$. Set $\boldsymbol{\pi}^{\mathbf{t}}=\boldsymbol{\pi}$.
7: for $k=n-\lambda+1$ to $n$ do //NEH heuristic.
8: $\quad$ Remove the job $\pi^{x}(k) \in \boldsymbol{\pi}^{k}$ in $\pi^{t}$ and reinsert the job $\pi^{x}(k)$ into $n$ possible positions in $\pi^{t}$ to obtain $n$ partial sequences.
9: Select solution $\pi^{\prime}$ with the lowest makespan after removing repetition.

Update $\pi^{t}$. Set $\pi^{\mathbf{t}}=\pi^{\prime}$.
10: if $C_{\max }\left(\pi^{t}\right)<C_{\max }(\pi)$ then
11: $\pi=\pi^{\mathrm{t}}$.
12: end if
13: end for
14: $\quad$ Obtain a feasible solution $\pi^{\prime}$. Let $\overline{\mathbf{n}} \leftarrow \overline{\mathbf{n}} \cup \pi^{\prime}$.
15: end for
16: return $\overline{\mathbf{n}}$.

### 4.2. Global search guided by multi-dimensional probabilistic model

### 4.2.1. Multi-dimensional probabilistic model

In general, permutation-based solutions have a number of distinguishing features, including the priority order of jobs and the distribution characteristics of job blocks. In this subsection, a multidimensional probabilistic model is proposed to capture promising patterns and adequately accumulate valuable structural information, which can effectively drive the search toward high-quality regions.
$\pi_{\text {Shoor }}^{\text {gen }, k}(x+1)$ that appears immediately after the job $\pi_{\text {Shoor }}^{\text {gen }, k}(x)$ located at the $x$ th position in $\boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, k}$ can be recorded separately by using the indicator function $I F_{n \times n \times n}^{\text {gen }, k}(x, y, z)$, as given in Eq. (20).

$$
\begin{gathered}
I F_{n \times n \times n \times n}^{\text {gen }, k}(x, y, z)=\left\{\begin{array}{c}
1, \text { if } y=\boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, k}(x) \text { and } z=\boldsymbol{\pi}_{\text {Shoor }}^{\text {gen }, k}(x+1) \\
0, \text { else } \\
x=1, \ldots, n-1 ; y, z=1, \ldots, n ; k=1, \ldots, \text { spsize }
\end{array}\right. \text {, }
\end{gathered}
$$

Then, the characteristic information about the order of jobs and the

distribution of blocks for each of the selected superior solutions is obtained based on Eq. (21).

$$
\begin{aligned}
& M C_{n \times n \times n}^{\text {gen }}(x, y, z)=\sum_{k=1}^{n p n \times p} I F_{n \times n \times n}^{\text {gen }}(x, y, z) \\
& \quad x=1, \ldots, n-1 ; y, z=1, \ldots, n
\end{aligned}
$$

Finally, the detailed definition of the proposed matrix cube is described below.

$$
\begin{aligned}
& M C_{n \times n \times n}^{\text {gen }}(x, y)=\left[M C_{n \times n \times n}^{\text {gen }}(x, y, 1), M C_{n \times n \times n}^{\text {gen }}(x, y, 2), \ldots, M C_{n \times n \times n}^{\text {gen }}(x, y, n)\right]_{1 \times n} \\
& x=1,2, \ldots, n-1 ; y=1,2, \ldots, n \\
& M C_{n \times n \times n}^{\text {gen }}(x)=\left[\begin{array}{c}
M C_{n \times n \times n}^{\text {gen }}(x, 1) \\
\vdots \\
M C_{n \times n \times n}^{\text {gen }}(x, n)
\end{array}\right]_{n=1}^{x} \\
& =\left[\begin{array}{ccc}
M C_{n \times n \times n}^{\text {gen }}(x, 1,1) & \cdots & M C_{n \times n \times n}^{\text {gen }}(x, 1, n) \\
\vdots & \ddots & \vdots \\
M C_{n \times n \times n}^{\text {gen }}(x, n, 1) & \cdots & M C_{n \times n \times n}^{\text {gen }}(x, n, n)
\end{array}\right]
\end{aligned}
$$

According to Eq. (23), the two-dimensional submatrix $\boldsymbol{M C}_{n \times n \times n}^{\text {gen }}(\boldsymbol{x})$ can record the characteristic information about job order and job block distribution at the $x$ th position in all superior solutions. In other words, the matrix cube structure can exactly determine the priority of each job and the distribution of the job block $[\boldsymbol{y}, \boldsymbol{z}]$ located in the $x$ th position of the $k$ th individual in $\boldsymbol{S P o p}(\boldsymbol{g e n})$, i.e., $\left[\pi_{\text {Shor }}^{\text {gen }}(x), \pi_{\text {Shor }}^{\text {gen }}(x+1)\right]$, it can retain total order relationships via a series of position-based submatrices, i.e., $\boldsymbol{M C}_{n \times n \times n}^{\text {gen }}(\mathbf{1}), \boldsymbol{M C}_{n \times n \times n}^{\text {gen }}(\mathbf{2}), \ldots \boldsymbol{M C}_{n \times n \times n}^{\text {gen }}(\boldsymbol{n})$. Thus, these advantageous characteristics or promising patterns derived from superior solutions can be effectively and intuitively recognized and retained. By adopting the matrix cube $\boldsymbol{M C}_{n \times n \times n}^{\text {gen }}$ described above, the multi-dimensional probabilistic model can be established. To illustrate the proposed $\boldsymbol{M C}_{n \times n \times n}^{\text {gen }}$, an example of five superior solutions (quize $=5$ ) containing four jobs $(n=4)$ is used to instantiate it. In this case, the size of $\boldsymbol{S P o p}(\boldsymbol{g e n})$ is quize $=5$ and gen $=1$. The selected superior solutions are $\pi_{\text {Shor }}^{1,1}=$ $\left[\pi_{\text {Shor }}^{1,1}(1), \pi_{\text {Shor }}^{1,1}(2), \quad \pi_{\text {Shor }}^{1,1}(3), \pi_{\text {Shor }}^{1,1}(4)\right]=\left[\begin{array}{llll}1, & 2, & 3, & 4\end{array}\right], \quad \pi_{\text {Shor }}^{1,1}=$ $\left[\pi_{\text {Shor }}^{1,2}(1), \pi_{\text {Shor }}^{1,2}(2), \quad \pi_{\text {Shor }}^{1,2}(3), \pi_{\text {Shor }}^{1,2}(4)\right]=\left[\begin{array}{llll}2, & 3, & 1, & 4\end{array}\right], \quad \pi_{\text {Shor }}^{1,2}=$ $\left[\pi_{\text {Shor }}^{1,2}(1), \pi_{\text {Shor }}^{1,2}(2), \quad \pi_{\text {Shor }}^{1,2}(3), \pi_{\text {Shor }}^{1,2}(4)\right]=\left[\begin{array}{llll}3, & 2, & 1, & 4\end{array}\right], \quad \pi_{\text {Shor }}^{1,4}=$ $\left[\pi_{\text {Shor }}^{1,4}(1), \pi_{\text {Shor }}^{1,4}(2), \quad \pi_{\text {Shor }}^{1,4}(3), \pi_{\text {Shor }}^{1,4}(4)\right]=\left[\begin{array}{llll}4, & 3, & 2, & 1\end{array}\right], \quad \pi_{\text {Shor }}^{1,5}=$ $\left[\pi_{\text {Shor }}^{1,5}(1), \pi_{\text {Shor }}^{1,5}(2), \pi_{\text {Shor }}^{1,5}(3), \pi_{\text {Shor }}^{1,5}(4)\right]=\left[\begin{array}{llll}4, & 3, & 1,2\end{array}\right]$, respectively. For the first position $(x=1)$ of all individuals, it is clear that job blocks [1,2] (i. e., $\boldsymbol{y}=1, \boldsymbol{z}=2),[2,3]$ (i.e., $\boldsymbol{y}=2, \boldsymbol{z}=3),[3,2]$ (i.e., $\boldsymbol{y}=3, \boldsymbol{z}=2$ ), and $[4,3]$ (i.e., $\boldsymbol{y}=4, \boldsymbol{z}=3$ ) appeared in these individuals from $\pi_{\text {Shor }}^{\text {gen }, 1}$ to $\pi_{\text {Shor }}^{\text {gen }}$, is recorded in accordance with Eqs. (20)-(23) as follows:

$$
\begin{aligned}
& M C_{4 \times 4 \times 4}^{1}(1,1,2)=\sum_{k=1}^{5} I F_{4 \times 4 \times 4}^{1,1}(1,1,2)=I F_{4 \times 4 \times 4}^{1,1}(1,1,2) \\
& +I F_{4 \times 4 \times 4}^{1,2}(1,1,2)+I F_{4 \times 4 \times 4}^{1,3}(1,1,2)+I F_{4 \times 4 \times 4}^{1,4}(1,1,2) \\
& +I F_{4 \times 4 \times 4}^{1,5}(1,1,2)=1+0+0+0+0=1 \\
& M C_{4 \times 4 \times 4}^{1}(1,2,3)=\sum_{k=1}^{5} I F_{4 \times 4 \times 4}^{1,4}(1,2,3)=I F_{4 \times 4 \times 4}^{1,1}(1,2,3) \\
& +I F_{4 \times 4 \times 4}^{1,2}(1,2,3)+I F_{4 \times 4 \times 4}^{1,3}(1,2,3)+I F_{4 \times 4 \times 4}^{1,4}(1,2,3) \\
& +I F_{4 \times 4 \times 4}^{1,5}(1,2,3)=0+1+0+0+0=1 \\
& M C_{4 \times 4 \times 4}^{1}(1,3,2)=\sum_{k=1}^{5} I F_{4 \times 4 \times 4}^{1,4}(1,3,2)=I F_{4 \times 4 \times 4}^{1,1}(1,3,2) \\
& +I F_{4 \times 4 \times 4}^{1,2}(1,3,2)+I F_{4 \times 4 \times 4}^{1,3}(1,3,2)+I F_{4 \times 4 \times 4}^{1,4}(1,3,2) \\
& +I F_{4 \times 4 \times 4}^{1,4}(1,3,2)=0+0+1+0+0=1
\end{aligned}
$$

$$
\begin{aligned}
& M C_{4 \times 4 \times 4}^{1}(1,4,3)=\sum_{k=1}^{5} I F_{4 \times 4 \times 4}^{1,4}(1,4,3)=I F_{4 \times 4 \times 4}^{1,1}(1,4,3) \\
& +I F_{4 \times 4 \times 4}^{1,2}(1,4,3)+I F_{4 \times 4 \times 4}^{1,3}(1,4,3)+I F_{4 \times 4 \times 4}^{1,4}(1,4,3) \\
& +I F_{4 \times 4 \times 4}^{1,5}(1,4,3)=0+0+0+1+1=2
\end{aligned}
$$

The remaining elements in $\boldsymbol{M} \boldsymbol{C}_{4 \times 4 \times 4}^{\text {gen }}(\mathbf{1})$ are set to zero. Likewise, for the second position $(x=2)$ of all individuals, job blocks $[2,1]$ (i.e., $y=$ $2, z=1),[2,3]$ (i.e., $y=2, z=3),[3,1]$ (i.e., $y=3, z=1)$, and $[3,2]$ (i. e., $\boldsymbol{y}=3, \boldsymbol{z}=2$ ) can also be recorded, respectively. Then we have.

$$
\begin{aligned}
& M C_{4 \times 4 \times 4}^{1}(2,2,1)=\sum_{k=1}^{5} I F_{4 \times 4 \times 4}^{1,1}(2,2,1) \\
& =0+0+1+0+0=1 \\
& M C_{4 \times 4 \times 4}^{1}(2,2,3)=\sum_{k=1}^{5} I F_{4 \times 4 \times 4}^{1,1}(2,2,3) \\
& =1+0+0+0+0=1 \\
& M C_{4 \times 4 \times 4}^{1}(2,3,1)=\sum_{k=1}^{4} I F_{4 \times 4 \times 4}^{1,1}(2,3,1) \\
& =0+1+0+0+1=2 \\
& M C_{4 \times 4 \times 4}^{1}(2,3,2)=\sum_{k=1}^{5} I F_{4 \times 4 \times 4}^{1,1}(2,3,2) \\
& =0+0+0+1+0=1
\end{aligned}
$$

The other cells of $\boldsymbol{M} \boldsymbol{C}_{4 \times 4 \times 4}^{1, n}(\mathbf{2})$ are set to zero. Since four job blocks $[1$, $2],[1,4],[2,1]$, and $[3,4]$ are located in the third position $(x=3)$, the characteristic information can also be saved, and we have $\boldsymbol{M C}_{4 \times 4 \times 4}^{1}(3,1$, $2)=1, \boldsymbol{M C}_{4 \times 4 \times 4}^{1}(3,1,4)=2, \boldsymbol{M C}_{4 \times 4 \times 4}^{1}(3,2,1)=1$, and $\boldsymbol{M C}_{4 \times 4 \times 4}^{1}(3,3,4)=$ 1 , respectively. It is worth noting that the information about job blocks in the last position of the job sequence is already included in the penultimate position. Therefore, the values of all the cells in $\boldsymbol{M} \boldsymbol{C}_{4 \times 4 \times 4}^{1, n}(\mathbf{4})$ are set to zero. It is indicated that the job blocks at different positions in superior solutions may be precisely learnt and entirely preserved in accordance with the position-based submatrices in $\boldsymbol{M} \boldsymbol{C}_{4 \times 4 \times 4}^{n m}$, However, in the aforementioned case, the critical characteristic information about the similar blocks from $\pi_{\text {Shor }}^{\text {gen }}$, i.e., $[1,2],[2,3]$, and $[3,2]$, is kept exclusively in the subscripts (1,2), (2,3), and (3,2) via utilizing the twodimensional probabilistic model (Pan \& Ruiz, 2012). Indeed, for each selected elite solution, the important patterns of the positions in which similar blocks or job blocks are located have been completely lost and fused. Then, the two-dimensional probabilistic model's sampling strategy cannot precisely predict the most proper position to place these valued similar blocks. To compensate the limitations of two-dimensional EDAs, we design the matrix cube to learn the structural information relating to the order relationships of jobs and the position of similar blocks through the use of different layers of $\boldsymbol{M} \boldsymbol{C}_{4 \times n \times n}^{\text {gen }}$. To be specific, the block $[2,3]$ in $\pi_{\text {Shor }}^{\text {gen } 1}=[1,2,3,4]$ can be reserved in $\boldsymbol{M} \boldsymbol{C}_{4 \times 4 \times 4}^{1}(\mathbf{2})$ (i.e., the second layer of $\boldsymbol{M} \boldsymbol{C}_{4 \times 4 \times 4}^{1}$ ), but the identical block [2,3]), but the identical block $[2,3]$ in $\pi_{\text {Shor }}^{\text {gen } 2}=[2,3,1,4]$ can be recorded in $\boldsymbol{M} \boldsymbol{C}_{4 \times 4 \times 4}^{1}(\mathbf{1})$ (i.e., the first layer of $\boldsymbol{M} \boldsymbol{C}_{4 \times 4 \times 4}^{1}$ ), but the identical block [2,3]), respectively. It is clear that $\boldsymbol{M} \boldsymbol{C}_{4 \times n \times n}^{\text {gen }}$ facilitates the accurate identification and differentiation of various interesting similar blocks located at different positions in job sequences. That is, the distribution characteristics of these similar blocks in the feasible solution space can be precisely described by a multi-dimensional probabilistic model, which may be capable of effectively directing the search toward more promising regions and preventing promising patterns from being destroyed or improperly fused.
4.2.1.2. Probabilistic model. Probabilistic models are essential for the successful application of EDA since they enable for the accurate estimation of the distribution of promising patterns of superior solutions to

the problem under consideration. In other words, it is highly advantageous to enhance the algorithm's performance if the proposed probabilistic model correctly learns the structural features from the selected superior solutions. It should be noted that the proposed matrix cube $\boldsymbol{M C}_{\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}$ can completely capture the structural features of some superior solutions, i.e., the ordinal of jobs and the dependency of jobs, during the iterative process. In contrast to existing two-dimensional probabilistic models (Jarboui, et al., 2009; Pan \& Ruiz, 2012; Wang \& Wang, 2016; Wang, et al., 2013), a matrix-cube-based multi-dimensional probabilistic model is devised by taking advantage of promising patterns derived from superior solutions. The critical characteristic information implicit in different solution sequences can be effectively extracted and appropriately accumulated, while valuable information can be interacted with and integrated via an incremental learning mechanism. Offspring individuals can be generated directly by sampling from the proposed probabilistic model. Let $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}$ be the multi-dimensional probabilistic model. Detailed definitions are described in Eqs. (24)-(25).

$$
\begin{aligned}
& \boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}(\boldsymbol{x}, \boldsymbol{y})= \\
& {\left[\begin{array}{l}
P M_{n=n+n}^{\text {ave }}(\boldsymbol{x}, \boldsymbol{y}, 1), P M_{n=n+n}^{\text {ave }}(\boldsymbol{x}, \boldsymbol{y}, 2), \ldots, P M_{n=n+n}^{\text {ave }}(\boldsymbol{x}, \boldsymbol{y}, n)
\end{array}\right]_{1=n}, } \\
& x=1,2, \ldots, n-1 ; y=1,2, \ldots, n \text {. } \\
& \boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }} \boldsymbol{x}=\left[\begin{array}{c}
\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}(\boldsymbol{x}, \mathbf{1}) \\
\vdots \\
\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}(\boldsymbol{x}, \boldsymbol{n})
\end{array}\right]_{n=1}
\end{aligned}
$$

Each element $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}(\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z})$ in $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}$ corresponds to a probability value for the occurrence of the job block $[y, x]$ at the $x$ th position in the genth iteration, referring to the job block's relevance. To clearly describe the multi-dimensional probabilistic model, let $\boldsymbol{S}_{\boldsymbol{P M}}^{\text {ave }}(\boldsymbol{x})$ and $\boldsymbol{S}_{\boldsymbol{P M}}^{\text {ave }}(\boldsymbol{x})$ represent the summation function of the $x$ th layer of $\boldsymbol{M C}_{\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}$ and $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}$, respectively, where $\boldsymbol{S}_{\boldsymbol{M C}}^{\text {ave }}(\boldsymbol{x})=\sum_{y=1}^{n} \sum_{n=1}^{n} \boldsymbol{M C}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}(\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z})$ and $\boldsymbol{S}_{\boldsymbol{P M}}^{\text {ave }}(\boldsymbol{x})=\sum_{y=1}^{n} \sum_{n=1}^{n} P M_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}(\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z})$. Thus, by utilizing both a matrix cube and a multi-dimensional probabilistic model, the incremental learning update mechanism can be stated in Eq. (26).

$$
\begin{aligned}
& \boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}(\boldsymbol{x})= \\
& (1-r) \times \boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}(\boldsymbol{x})+r \times\left(\boldsymbol{M C}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}(\boldsymbol{x}) / \boldsymbol{S}_{\boldsymbol{M C}}^{\text {ave }}(\boldsymbol{x})\right) \text {. } \\
& x=1,2, \ldots, n-1 .
\end{aligned}
$$

Note that the parameter $r \in[0,1]$ in Eq. (26), represents the learning rate. If $r=1$, the multi-dimensional probabilistic model is updated only by using the matrix cube; otherwise, it is updated by using historical evolutionary information. The proposed updating strategy can adequately accumulate characteristic information about promising patterns of superior solutions. That is, the incremental learning mechanism can take into account not only the current distribution characteristics of similar blocks, but also make use of the previously obtained useful historical information, resulting in a suitable trade-off in terms of learning rate $r$. Notice that the normalization for each layer of $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}$ in Step 3 should be performed before to sampling, i.e., $\boldsymbol{S}_{\boldsymbol{M C}}^{\text {ave }}(\boldsymbol{x})=1$, gen $>$ $1, x=1, \ldots, n-1$. Moreover, the features of the first job block in the selected superior subpopulation have a considerable effect on the performance of the developed algorithm for dealing with the considered problem. If this feature is not well handled, the algorithm's superiority will be diminished. Therefore, the steps for developing and updating a probability model with the aforementioned characteristics are detailed as follows.

Step 1: Initialize $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\boldsymbol{a}}$. Set $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {0 }}(\boldsymbol{x}, \boldsymbol{y}, \boldsymbol{z})=$ $\left\{\begin{array}{c}0, x=1 ; y, z=1, \ldots, n \\ 1 / n^{2}, x=2,3, \ldots, n-1 ; y, z=1, \ldots, n .^{\prime}\end{array}\right.$
Step 2: Obtain $\boldsymbol{M C}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}$ by the initial population $\boldsymbol{P o g}(\boldsymbol{0})$, then compute

$$
P M_{n=n+n}^{\mathrm{I}}(x, y, z)=\left\{\begin{array}{c}
\frac{M C_{n=n+n}^{\mathrm{I}}(x, y, z)}{S_{\mathrm{HC}}^{\mathrm{I}}(x)} \\
x=1 ; y, z=1, \ldots, n \\
\frac{P M_{n=n+n}^{\mathrm{O}}(x, y, z)+M C_{n=n+n}^{\mathrm{O}}(x, y, z)}{S_{\mathrm{PM}}^{\mathrm{O}}(x)+S_{\mathrm{HC}}^{\mathrm{O}}(x)} \\
x=2,3, \ldots, n-1 ; y, z=1, \ldots, n
\end{array}\right.
$$

Step 3: Set gen $=2$. Compute $\boldsymbol{M C}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}$ and $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}(\boldsymbol{x})$ using Eq. (26).

$$
\begin{aligned}
& P M_{n=n+n}^{\text {ave }}(x, y, z)= \\
& (1-r) \times P M_{n=n+n}^{\text {ave }}(x, y, z)+r \times\left(\frac{M C_{n=n+n}^{\text {ave }}(x, y, z)}{S_{\text {HC }}^{\mathrm{I}}(x)}\right) \\
& x=1,2, \ldots, n-1 ; y, z=1,2, \ldots, n
\end{aligned}
$$

Step 4: Set gen $=$ gen +1 . If gen $<$ maxgen, then go to Step 3.
Notably, for $x=2,3, \ldots, n-1$, all values in $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{a}}$ is initialized to $1 / n^{2}$, ensuring that the entire solution space is uniformly sampled. In addition, when $x=1$, the cell values in the first layer of $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{a}}$ are set to 0 , instead of $1 / n^{2}$, which can highlight potential patterns of job blocks at the first position of all individuals in the superior subpopulation and effectively increase guidance to promising regions during the initial phase. To illustrate, an example of establishing a matrix-cube-based multi-dimensional probabilistic model is provided below, with the learning rate set to $r=0.3$.
(1) Firstly, $\boldsymbol{M C}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}$ is computed by counting the initial subpopulation via Eqs. (20)-(21). For the first layer of $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}, \mathrm{i} . e ., \boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(1)$, the probability values can be calculated as follows: $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(1,1,2)=$ $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(1,2,3)=\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(1,3,1)=(0+1) / 5=0.2, \boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(1,3,1)$ $=(0+2) / 5=0.4$. The values of the other cells are set to zero.
(2) Secondly, the probability values of the second layer of $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}$ can be computed as follows: $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(2,2,1)=\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(2,2,3)=$ $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(2,3,2)=(1 / 16+1) /(1+5)=0.177, \boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(2,3,1)=$ $(1 / 16+2) /(1+5)=0.344$. Then, all other cell values are set to $(1 / 16+0) /(1+5)=0.010$.
(3) Thirdly, the probability values of the third layer of $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}$ can be computed as follows: $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(3,1,2)=\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(3,2,1)=$ $=\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(3,3,4)=(1 / 16+1) /(1+5)=0.177$ and $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\mathbf{1}}(3,1,4)=$ $(1 / 16+2) /(1+5)=0.344$. Similarly, the values of the other cells are equal to 0.01 .
(4) Finally, $\boldsymbol{P M}_{\boldsymbol{n}=\boldsymbol{n}=\boldsymbol{n}}^{\text {ave }}$ (gen $>1$ ) is updated by using the incremental learning mechanism proposed in Step 3. Considering five superior solutions, each of which contains four jobs, Fig. 2 illustrates the updating process of a multi-dimensional probabilistic model.

### 4.2.2. New population generation

According to the above subsection, it is clear that proper probabilistic models may be employed to effectively extract excellent features from the superior solutions. The sampling strategy also has an effect on the search behavior of EDA-based algorithms, since such sampling strategy determines how to guide the population's evolutionary direction in the search space. Therefore, it is important to set up suitable sampling strategies for sampling from the multi-dimensional

probabilistic model to generate a new population.
Let $\pi^{g e n, k}=\left[\pi^{g e n, k}(1), \pi^{g e n, k}(2), \ldots, \pi^{g e n, k}(n)\right]$ denote the $k$ th individual in $\operatorname{Pop}(g e n), k=1,2, \ldots$, popsize. Due to the fact that the multidimensional probabilistic model records the probability information of both the order of jobs and the distribution of blocks, the probability value of each block or similar block $\left[\pi^{g e n, k}(i-1), \pi^{g e n, k}(i)\right],(i=2, \ldots, n)$ in the job sequence $\pi^{g e n, k}$ is stored in the $(i-1)$ th layer of $\boldsymbol{P M}_{\mathrm{n} \times \pi \times \pi}^{g e n}, k$. $\pi_{c} P M_{\mathrm{n} \times \pi \times \pi}^{g e n}(i-1)$. The selection of job $\pi^{g e n, k}(i)$ at the $i$ th position is dependent upon the appearance of job $\pi^{g e n, k}(i-1)$ at the $(i-1)$ th position in $\pi^{g e n, k}$. Let SelectJob $\left(P M_{\pi \times \pi \times \pi}^{g e n}, \pi^{g e n, k}, i\right)$ be a selection function that is utilized to determine the candidate job $x_{c}$ at the $i$ th position of $\pi^{g e n, k}$ $(i>1)$. That is, the selection of the candidate job $x_{c}$ at the $i$ th position in the $\pi^{g e n, k}$ should sample from the $\left(\pi^{g e n, k}(i-1)\right)$ th row of the $(i-1)$ th layer in $\boldsymbol{P M}_{\mathrm{n} \times \pi \times \pi}^{g e n}$, i.e., $\boldsymbol{P M}_{\mathrm{n} \times \pi \times \pi}^{g e n}(i-1, \pi^{g e n, k}(i-1))$. To eliminate duplication to guarantee the generation of feasible solutions, the probability values of the $x_{c}$ th column from the $i$ th layer to the $(n-1)$ th layer in $\boldsymbol{P M}_{\mathrm{n} \times \pi \times \pi}^{g e n}$ should be set as 0 and all elements in $\boldsymbol{P M}_{\pi \times \pi \times \pi}^{g e n}$ need to be renormalized if the job $x_{c}$ is already scheduled in the $i$ th position of $\pi^{g e n, k}$. The procedure of SelectJob $\left(\boldsymbol{P M}_{\pi \times \pi \times \pi}^{g e n}, \pi^{g e n, k}, i\right)$ is described in Algorithm 4.In order to precisely learn the promising patterns of jobs located at the first position of high-quality individuals in the population, and to compress the front delay as much as possible, a first positionbased selection strategy (FPBSS) is presented in Algorithm 5 for determining the first job in the $\pi^{g e n, k}$. According to Algorithms 4 and 5, the new population generation method is provided in Algorithm 6. As seen from Algorithm 6, if $i=1$, the job $x_{c}$ is selected by $\operatorname{FPBSS}\left(\boldsymbol{P M}_{\pi \times \pi \times \pi}^{g e n}\right.$, $\pi^{g e n, k}$ ), otherwise, the job block $\left[\pi^{g e n+1, k}(i), \pi^{g e n+1, k}(i+1)\right]$ at the $i$ th position of $\pi^{g e n, k}$ is selected by SelectJob $\left(\boldsymbol{P M}_{\pi \times \pi \times \pi}^{g e n}, \pi^{g e n, k}, i\right)$. Thereafter, job blocks at different positions in the solution sequence are determined, and these job blocks are connected according to the sequential relationship among jobs to produce new feasible solutions.

Algorithm 4:SelectJob $\left(P M_{\mathrm{n} \times \mathrm{n} \times \mathrm{n}}^{g e n}, \pi^{g e n, k}, i\right)$

Input: $\mathbf{P M}_{\mathrm{n} \times \mathrm{n} \times \mathrm{n}}^{\text {gen }}, \pi^{\text {gen }, \mathrm{k}}$ and $i$.
Output: the candidate job $\pi_{c}$.
1: Produce a random number $r$, i.e., $r \in\left[0, \sum_{h=1}^{n} P M_{\pi \times \pi \times n}^{g e n}(i-1, \pi^{g e n, k}(i-1), h)\right)$.
2: if $r \in\left[0, P M_{\pi \times \pi \times n}^{g e n}(i-1, \pi^{g e n, k}(i-1), 1)\right)$ then
3: $\quad \pi_{c} \leftarrow 1$.
4: else
5: for $t=1$ to $n-1$ do
6: if $r \in\left[\sum_{h=1}^{t} P M_{\pi \times \pi \times n}^{g e n}(i-1, \pi^{g e n, k}(i-1), h), \sum_{h=1}^{t+1} P M_{\pi \times \pi \times n}^{g e n}(i-1, \pi^{g e n, k}(i-1), h)\right)$ then
7: $\pi_{c} \leftarrow t+1$, break.
8: end if
9: end for
10: end if
11: for $t=i$ to $n-1$ do //avoid repeated selection of jobs.
12: for $j=1$ to $n-1$ do
$13: \quad P M_{\pi \times \pi \times n}^{g e n}\left(t, j, \pi_{c}\right)=0$.
14: end for
15: end for
16: return $\pi_{c}$.

# Algorithm 5: $F P B S S\left(M C_{n \times n \times n}^{\text {gen }} ; \pi^{g e n, k}\right)$ 

Input: $\mathbf{P M}_{\mathrm{n}=\mathrm{n}=\mathrm{n}}^{\text {gen }, \mathrm{k}} \cdot \pi^{\text {gen, }}$
Output: The first job $\pi^{\text {gen }, k}(1)$
1: Produce a random number $r$, i.e., $r \in[0,1)$.
2: for $t=1$ to $n-1$ do
3: $\quad$ if $r \in\left[\sum_{h=1}^{t} \sum_{z=1}^{n}\left(M C_{n \times n \times n}^{\text {gen }}(1, h, z) / S_{M C}^{\text {gen }}(1)\right), \sum_{h=1}^{t+1} \sum_{z=1}^{n}\left(M C_{n \times n \times n}^{\text {gen }}(1, h, z) / S_{M C}^{\text {gen }}(1)\right)\right)$ then
$4: \quad \pi^{\text {gen }, k}(1)=t+1$, break;
5: end if
6: end for
7: for $t=1$ to $n-1$ do //avoid repeated selection of jobs
8: $\quad$ for $j=1$ to $n-1$ do
9: $\quad M C_{n \times n \times n}^{\text {gen }}(t, j, \pi^{\text {gen }, k}(1))=0$.
10: end for
11: end for

## Algorithm 6: New Population Generation

Input: $\mathbf{P M}_{\mathrm{n}=\mathrm{n}=\mathrm{n}}^{\text {gen }}, \mathbf{M C}_{\mathrm{n}=\mathrm{n}=\mathrm{n}}^{\text {gen }}, \pi^{\text {gen, } \mathrm{k}} \cdot$
Output: Pop(gen +1 )
for $k=1$ to popsize do
for $i=1$ to $n$ do
if $i=1$ then
$\pi_{c} \leftarrow F P B S S\left(\mathbf{M C}_{\mathrm{n}=\mathrm{n}=\mathrm{n}}^{\text {gen }}, \pi^{\text {gen, } \mathrm{k}}\right)$.
else
$\pi_{c} \leftarrow$ SelectJob $\left(\mathbf{P M}_{\mathrm{n}=\mathrm{n}=\mathrm{n}}^{\text {gen }}, \pi^{\text {gen, } \mathrm{k}}, i\right)$.
end if
$\pi^{\text {gen }, k}(i)=\pi_{c}$
end for
10: $\quad \operatorname{Pop}(\text { gen }+1)=\operatorname{Pop}(\text { gen }+1) \cup \pi^{\text {gen, } \mathrm{k}}, \pi^{\text {gen, } \mathrm{k}} \leftarrow \varnothing$.
11: end for
12: return $\operatorname{Pop}(\operatorname{gen}+1)$.

### 4.2.3. Diversity controlling mechanism

As stated in Section 4.1, although the initial population is of high quality and well distribution, the diversity of the population may decline as the evolutionary process progresses. In order to maintain a reasonable balance between global exploration and local exploitation, a diversity control mechanism is provided to effectively prevent the proposed algorithm from prematurely converging to local optima. Let $P_{d i v}$ be defined as the diversity index and $\delta$ as the diversity threshold. $P_{d i v}$ can be used to measure the similarity between individuals in a population. If the value of $P_{d i v}$ is less than $\delta$, the top $20 \%$ of high-quality individuals in the population are retained and the remaining $80 \%$ are reinitialized. Specifically, $20 \%$ of the remaining $80 \%$ of individuals are formed by employing two constructive heuristics, i.e., PFT_NEH(x) and PFZ_RZ(x), described in Subsections 4.1.1 and 4.1.2, while the others are randomly
generated. The corresponding calculation steps are given below.
Step 1: According to Eqs. (20)-(23), $M C_{n \times n \times n}^{\text {gen }}$ in the genth generation is determined.

Step 2: Count the number of elements greater than 0 in the $i$ th layer of $M C_{n \times n \times n}^{\text {gen }}$, denoted as $a_{i}$.

Step 3: The value of diversity index $P_{d i v}$ is calculated by using Eq. (27).
$P_{d i v}=\frac{1}{n-1} \sum_{i=1}^{n-1} \frac{a_{i}-1}{\min \left(n^{2}-n-1\right.}$, spsize $-1\rangle$
Notice that the population size or subpopulation size often exceeds one. According to Eq. (27), the range of $P_{d i v}$ is $|0.1|$. If the $P_{d i v}$ value is closer to one, the better the diversity of the population. Conversely, the closer the value of $P_{d i v}$ is to zero, the more similar the individuals in the

![img-2.jpeg](img-2.jpeg)

Fig. 2. Illustration of updating process of multi-dimensional probabilistic model.
population are. That is, the population has poor diversity if the individuals in the population have similar structural features or patterns. In order to reduce computational effort, the value of diversity index $P_{d w}$ is calculated every ten generations, and the diversity threshold $\delta$ is tuned in detail in the next section (see Subsection 5.2). To facilitate intuitive comprehension, the example of $\boldsymbol{M}_{\boldsymbol{\lambda}=\pi / \pi}^{1}$ depicted in Fig. 2 is utilized to illustrate the diversity mechanism, while still considering those five high-quality individuals. It is evident from the preceding stages that $\alpha_{1}=4, \quad \alpha_{2}=4, \quad \alpha_{3}=4$, and the diversity index
$P_{d w}=(3 / 4+3 / 4+3 / 4) / 3=3 / 4=0.75$ can be computed by using Eq. (27).

# 4.3. Local search controlled by multi-dimensional probabilistic model 

### 4.3.1. Fast Insert-based neighbor evaluation method

It is well known that the insertion neighborhood structure is one of the most effective neighborhood structures for the permutation-based models of BFSPs (Pan \& Wang, 2012; Schiavinotto \& Stutzle, 2007;
![img-2.jpeg](img-2.jpeg)

Fig. 3. An example of using the probability model to determine whether to evaluate $\pi_{t}$ in $N S_{P_{M} \text { boost }}$.

Tasgetiren, et al., 2017; Wang, et al., 2010). Therefore, it makes sense to select the insertion neighborhood to design neighborhood searches in the next Subsections 4.3.2 and 4.3.3. Since the number of neighbor solutions in the insertion neighborhood is $\langle n-1\rangle^{2}$, the time complexity of such neighborhood search is $O\left(m n^{3}\right)$ by using forward and backward calculations given in Section 3. Following the reversibility of the permutation-based model for the BFSP_SDST stated in Section 3, a fast Insert-based neighbor evaluation method is devised by using a bidirectional calculation method. The devised fast evaluation method is beneficial for enhancing the efficiency of evaluating Insert-based neighbors. Its procedure is provided in Algorithm 7.

The pivotal point of the proposed fast Insert-based neighbor evaluation method is to remarkably reduce the complexity by appropriately
adding the space storage. Specifically, $d_{\pi / i ; j}$ and $f_{\pi(i ; j}$ can be calculated and conserved at the beginning in Algorithm 7 (see Lines 1-2), and their numerical values can be treated as constants while evaluating Insertbased neighbors (see Lines 5-17). Although Algorithm 7 applies to the basic insertion neighborhood (see Lines 4 and 15), it can be easily extended to block-based insertion neighborhoods, i.e., picking multiple jobs to form job blocks and performing neighborhood search based on those blocks. Therefore, both the job-based insertion neighborhood in Subsection 4.3.2 (see Lines 2-27 in Algorithm 8) and the block-based insertion neighborhood in Subsection 4.3.3 (see Lines 4-7 in Algorithm 10) can utilize the above-mentioned fast evaluation method to quickly calculate neighbors.

# Algorithm 7: The fast Insert-based neighbor evaluation method 

Input: $p, q$, and $\pi$.
Output: $\pi^{*}$ and $C_{\max }\left(\pi^{*}\right)$.

1: Calculate departure time $d_{\pi(i), j}$ of job $\pi(i)$ by Eqs. (1)-(5), $i=1,2, \ldots, n ; j=1,2, \ldots, m$.
2: Calculate duration time $f_{\pi(i), j}$ of job $\pi(i)$ by Eqs. (7)-(11), $i=n, n-1, \ldots, 1 ; j=m, m-1, \ldots, 1$.
3: for $p=1$ to $n$ do
$4: \quad \pi^{\prime} \leftarrow$ Remove job $\pi(p)$ at the $p$ th position from $\pi$.
5: if $i<p$ then //calculate departure time.
6: $\quad d_{\pi^{\prime}(i), j}^{\prime}=d_{\pi(i), j}, i=1,2, \ldots, n-1 ; j=1,2, \ldots, m$.
else
7: $\quad$ Compute departure time $d_{\pi^{\prime}(i), j}^{\prime}$ by Eqs. (1)-(4).
end if
10: if $i>p$ then //calculate duration time.
$11:$
12: else
13: Compute duration time $f_{\pi(i), j}^{\prime}$ by Eqs. (6)-(10).
end if
14: $\pi^{*} \leftarrow$ Reinsert job $\pi(p)$ into the $q$ th position of $\pi^{\prime}$, $q \in\{1,2, \ldots, n\} \wedge q \notin\{p-1, p\}$.
16: Compute departure time $d_{\pi^{*}(q), j}^{*}$ by the obtained $d_{\pi^{\prime}(q-1), j}^{\prime}$, $j=1,2, \ldots, m$.
17: Compute $C_{\max }\left(\pi^{*}\right)$ of new solution $\pi^{*}$ as follows:

$$
C_{\max }\left(\pi^{*}\right)=\max _{j=1,2, \ldots, m}\left\{d_{\pi^{*}(q), j}^{*}+S_{\pi^{*}(q), \pi^{\prime}(q), j}+f_{\pi^{\prime}(q), j}^{\prime}\right\}
$$

18: end for

### 4.3.2. Neighborhood search boosted by probabilistic model ( $\mathrm{NS}_{\mathrm{PM} \text {,boost }}$ )

Since the multi-dimensional probabilistic model contains complete information of both the order relations and the block distributions of excellent individuals (see Subsection 4.2.1), it can be utilized to boost the neighborhood search. Thus, the Insert-based neighborhood search boosted by the probabilistic model, denoted as $N S_{\mathrm{PM} \text {,boost }}$, is proposed to perform fast exploitation.

The procedure of the $N S_{\mathrm{PM} \text {,boost }}$ is provided in Algorithm 8, where $\pi_{\text {best }}$ is the best solution obtained so far. In Algorithm 8, when performing the $N S_{\mathrm{PM} \text {,boost }}$, the corresponding conditional probability is calculated via the probabilistic model (see Lines 7 and 14). If the conditional probability value acquired satisfies the predefined condition,
the insertion operation is executed, and then the corresponding new neighbor is evaluated. Otherwise, a certain probability value is randomly generated to determine whether to perform the insertion operation (see Lines 9 and 16). It should be noted that the $N S_{\mathrm{PM} \text {,boost }}$ can reasonably utilize the structural patterns of excellent individuals to adjust the search scope in the Insert-based neighborhood, thereby avoiding the evaluations of potentially poor neighbors and improving the search efficiency. In order to facilitate a better understanding, Fig. 3 gives an example of using the probability model to determine whether to perform the insertion operation on the current neighbor $\pi_{i}=[1,2,3,4]$ in the $N S_{\mathrm{PM} \text {,boost }}$.

```
\(\operatorname{Algorithm} 8: P M_{-} \operatorname{NeighborSearch}\left(\boldsymbol{\pi}_{b e s t}, P M_{n \times n \times n}^{g e n}\right)\)
```

Input: $\pi_{\text {best }}, \mathrm{PM}_{\mathrm{n} \times \mathrm{n} \times \mathrm{n}}^{\mathrm{gen}}$.
Output: The updated $\pi_{\text {best }}$ and $C_{\max }\left(\pi_{\text {best }}\right)$.

$$
\pi_{\mathrm{t}}=\pi_{\text {best }}, \text { flag }=\text { true }
$$

for $k=1$ to $n$ do
$\pi^{\prime} \leftarrow$ Remove job $\pi_{i}(k)$ at the $k$ th position from $\pi_{t}$.
for $i=1$ to $n$ do
$\pi^{\prime \prime} \leftarrow$ Reinsert the job $\pi_{i}(k)$ into the $i$ th slot of $\pi^{\prime}$.
if $i<k$ then //forward insertion
if $\sum_{l=i}^{k} P M_{n \times n \times n}^{\text {gen }}\left(l, \pi^{\prime \prime}(l), \pi^{\prime \prime}(l+1)\right)>\sum_{l=i}^{k} P M_{n \times n \times n}^{\text {gen }}\left(l, \pi_{l}(l), \pi_{l}(l+1)\right)$ then
$\pi_{t} \leftarrow \pi^{\prime \prime}$.
else if $\operatorname{rand}()<1 /(k-i+1) \sum_{l=i}^{k} P M_{n \times n \times n}^{\text {gen }}\left(l, \pi^{\prime \prime}(l), \pi^{\prime \prime}(l+1)\right)$ then
$\pi_{t} \leftarrow \pi^{\prime \prime} . / /$ accept the solution by probability
else flag = false .
end if
else //backward insertion
if $\sum_{l=k}^{i} P M_{n \times n \times n}^{\text {gen }}\left(l, \pi^{\prime \prime}(l), \pi^{\prime \prime}(l+1)\right)>\sum_{l=k}^{i} P M_{n \times n \times n}^{\text {gen }}\left(l, \pi_{l}(l), \pi_{l}(l+1)\right)$ then
$\pi_{t} \leftarrow \pi^{\prime \prime}$.
else if $\operatorname{rand}()<1 /(i-k+1) \sum_{l=k}^{i} P M_{n \times n \times n}^{\text {gen }}\left(l, \pi^{\prime \prime}(l), \pi^{\prime \prime}(l+1)\right)$ then
$\pi_{t} \leftarrow \pi^{\prime \prime} . / /$ accept the solution by probability
else flag = false .
end if
end if
if flag = true then
if $C_{\max }\left(\pi_{t}\right)<C_{\max }\left(\pi_{\text {best }}\right)$ then
$\pi_{\text {best }}=\pi_{t}, C_{\max }\left(\pi_{\text {best }}\right)=C_{\max }\left(\pi_{t}\right)$.
end if
end if
end for
end for
return $\pi_{\text {best }}, C_{\max }\left(\pi_{\text {best }}\right)$.

![img-3.jpeg](img-3.jpeg)

Fig. 4. The flow chart of the proposed MCEDA.
4.3.3. Neighborhood search guided by probabilistic model and reference sequence $\left(N S_{\text {PM_RS_guide }}\right)$

According to Subsection 4.2.1, the probability information related to the block distribution is saved in a series of position-based probability matrices, i.e., $\boldsymbol{P M}_{n \rightarrow n}^{\text {pos }}(\mathbf{1}), \boldsymbol{P M}_{n \rightarrow n}^{\text {pos }}(\mathbf{2}), \ldots, \boldsymbol{P M}_{n \rightarrow n}^{\text {pos }}(\boldsymbol{n})$. Therefore, the Insert-based neighborhood search guided by the probabilistic model and the reference sequence, denoted as $N S_{\text {PM_RS_guide }}$, is designed to execute deep exploitation.

Let $p_{r}$ be the correlation coefficient of jobs. $p_{r}$ is calculated according to the following Eq. (28):
$p_{r}=\frac{\sum_{i=1}^{n} P M_{i \rightarrow n \rightarrow n}^{\text {pos }}\left(x, \pi^{y z n}(l), \pi^{y z n}(\bar{l})\right)}{\sum_{i=1}^{n} \sum_{i=1}^{n} P M_{n \rightarrow n \rightarrow n}^{\text {pos }}\left(x, \pi^{y z n}(l), z\right)}$
where $l \neq l$ and $l, l=1,2, \ldots, n$. When $p_{r} \geqslant 0.2$, it indicates that two jobs $\pi^{g m k}(l)$ and $\pi^{g m k}(l)$ in $\pi^{g m k}$ are strongly correlated. Obviously, $p_{r}$ represents the tightness of the connection between the job $\pi^{g m}(l)$ and the job $\pi^{g m}(l)$ in $\pi^{g m}$. Firstly, a block construction strategy is presented in Algorithm 9, where the block $\pi_{\text {block }}$ is extracted from the current
individual or solution sequence $\pi^{g m}$ via utilizing the reference sequence $\pi_{b s s}$ (i.e., the best solution obtained so far) and the probability model $\boldsymbol{P M}_{n \rightarrow n}^{\text {pos }}$. Then, the procedure of the $N S_{\text {PM_RS_guide }}$ is outlined in Algorithm 10, where $\pi_{b g b}$ is a partial sequence after removing $\pi_{b t s k}$ from $\pi_{b s s}^{\text {pos }}$, and Insert $\left(\pi_{b g b}, i, \pi_{b t s k}\right)$ means that $\pi_{b t s k}$ is inserted in the $i$ th position in $\pi_{b g b}$.

From Algorithm 10, it can be seen that the core idea of the $N S_{\text {PM_RS_guide }}$ is to dynamically construct blocks with strong correlation and promising pattern in the process of neighborhood search (see Line 7), and then search the Insert-based neighborhood determined by each block (see Lines 11-17). Since the constructed blocks are different in most cases, the $N S_{\text {PM_RS_guide }}$ can perform rich searches in a variety of Insert-based neighborhoods, which is conducive to increasing the search depth. Moreover, the $N S_{\text {PM_RS_guide }}$ can ensure that the overall quality of neighbors in the constructed neighborhood is high, which helps to improve the search quality.

Algorithm 9:Variable_Block $\left(k\right.$, pos, len, $\left.\boldsymbol{\pi}^{\text {gen }}, \boldsymbol{\pi}_{\text {best }}, P M_{n \times n \times n}^{\text {gen }}\right)$
Input: $k$, pos, len, $\boldsymbol{\pi}^{\text {gen }}, \boldsymbol{\pi}_{\text {best }}$, and $\mathbf{P M}_{\mathbf{n}=\mathbf{n}=\mathbf{n}}^{\text {gen }}$.
Output: len and $\boldsymbol{\pi}_{\text {block }}$.

1: while $\pi^{\text {gen }}(k+\operatorname{len})=\pi_{\text {best }}(\operatorname{pos}+l$ len $)$ do
2: Calculate $p_{r}$ for $\pi^{\text {gen }}(k+l e n-1)$ and $\pi^{\text {gen }}(k+l e n)$.
3: $\quad$ if $\left(p_{r} \geq 0.2\right)$ or $\left(\left(p_{r}<0.2\right)\right.$ and $\left(\operatorname{rand}()<0.35\right)$ ) then
4: $\quad \pi_{\text {block }}(\operatorname{len}) \leftarrow \pi^{\text {gen }}(k+l e n)$.
5: else
6: $\quad$ break.
7: end if
8: $\quad$ len $=$ len +1 .
9: end while
10: return len and $\boldsymbol{\pi}_{\text {block }}$.

Algorithm 10:Reference_NeighborSearch $\left(\boldsymbol{\pi}^{\text {gen }}, \boldsymbol{\pi}_{\text {best }}, P M_{n \times n \times n}^{\text {gen }}\right)$
Input: $\boldsymbol{\pi}_{\text {best }}, \boldsymbol{\pi}^{\text {gen }}$ and $\mathbf{P M}_{\mathbf{n}=\mathbf{n}=\mathbf{n}}^{\text {gen }}$.
Output: The updated $\boldsymbol{\pi}^{\text {gen }}$ and $C_{\max }\left(\boldsymbol{\pi}^{\text {gen }}\right)$.
$1: \quad N_{c}=1$.
2: while $N_{c} \leq n$ do
$3: \quad k=1, \operatorname{len}=1, \operatorname{pos}=N_{c}, \boldsymbol{\pi}_{\text {block }} \leftarrow \varnothing$.
while $\pi^{\text {gen }}(k) \neq \pi_{\text {best }}(\operatorname{pos})$ do
$4: \quad k=k+1$.
end while
7: $\boldsymbol{\pi}_{\text {block }} \leftarrow$ Variable_Block $\left(k\right.$, pos,len, $\left.\boldsymbol{\pi}^{\text {gen }}, \boldsymbol{\pi}_{\text {best }}, \mathbf{P M}_{\mathbf{n}=\mathbf{n}=\mathbf{n}}^{\text {gen }}\right)$. //Algorithm 9
8: if len $=1$ then
$9: \quad \pi_{\text {block }}(1)=\pi_{\text {best }}(\operatorname{pos})$.
10: end if
11: $\boldsymbol{\pi}_{\text {left }} \leftarrow$ Remove job block $\boldsymbol{\pi}_{\text {block }}$ from $\boldsymbol{\pi}^{\text {gen }}$.
12: for $i=1$ to $(n-l e n+1)$ do
$13: \quad \pi_{\text {new }} \leftarrow \operatorname{Insert}\left(\boldsymbol{\pi}_{\text {left }}, i, \boldsymbol{\pi}_{\text {block }}\right)$.
14: if $C_{\max }\left(\boldsymbol{\pi}_{\text {new }}\right)<C_{\max }\left(\boldsymbol{\pi}^{\text {gen }}\right)$ then
$15: \quad \pi^{\text {gen }}=\boldsymbol{\pi}_{\text {new }}, C_{\max }\left(\boldsymbol{\pi}^{\text {gen }}\right)=C_{\max }\left(\boldsymbol{\pi}_{\text {new }}\right), N_{c}=1$.
end if
17: end for
$18: \quad N_{c}=N_{c}+1$.
19: end while
20: return $\boldsymbol{\pi}^{\text {gen }}, C_{\max }\left(\boldsymbol{\pi}^{\text {gen }}\right)$.

### 4.3.4. Multi-neighborhood iterated local search

In the last decade, various local search methods based on the VNS framework have been proposed, among which iterated local search (ILS) proposed by Lourenco et al. (Lourenço, et al., 2010) is one of the most effective local search methods. The main idea of ILS is to first perturb the current best solution for preventing cycle search and jumping out of local optima, and then to undertake an iterative variable neighborhood search to find more satisfied solutions. Nowadays, ILS has been widely applied to solve a variety of scheduling problems. Therefore, a new multi-neighborhood ILS (MNILS) combing the $N S_{\text {PM_boost }}$ (Algorithm 8) and the $N S_{\text {PM_RS_guide }}$ (Algorithm 10) is devised to perform deeper exploitation from promising regions obtained by the global search in Section 4.2.

The procedure of the MNILS is given in Algorithm 11, where Interchange $\left(\pi_{\mathrm{cl}}^{\mathrm{gen}}, u, v\right)$ means interchange the uth job and the $v$ th job in $\pi_{\mathrm{cl}}^{\mathrm{gen}}, \pi_{\text {best }}^{\mathrm{gen}}$ is the current best individual or sequence at generation gen, and $T$ is the temperature control parameter set to $T=\sum_{i=1}^{n} \sum_{j=1}^{n} p_{i, j} / 5 \mathrm{nm}$ in the proposed MCEDA. From Algorithm 11, it can be known that the MNILS starts the exploitation from the promising regions (i.e., $\pi_{\text {best }}$ and $\pi_{\text {best }}^{\text {gen }}$ ), and iteratively executes the $N S_{\text {PM_boost }}$ (see Lines 1 and 6) and the $N S_{\text {PM_RS_guide }}$ (see Lines 2 and 7) to guide the exploitation down to the optimal or near optimal solution. Moreover, the hybrid perturbation strategy combining Interchange-based moves (see Lines 4 and 5) and simulated annealing mechanism (see Line 13) is used to drive the local search to jump out of local optima.

### 4.4. The framework of MCEDA

In general, EDA reproduces offspring by sampling from a welldesigned probabilistic model, which mainly consists of the following five steps (Pan \& Ruiz, 2012): (a) generating initial population, (b) selecting elite individuals, (c) updating probability model with superior solutions, (d) sampling from the probability model to create a new population, and ( $e$ ) repeating steps $(b)-(d)$ until the termination condition is satisfied. After covering each component in detail in the preceding sections, Fig. 4 illustrates the MCEDA framework.

From Fig. 4, it can be seen that the proposed MCEDA consists of two main aspects, i.e., a breadth global search and a depth local search. First, two effective constructive heuristics are applied to generate some highquality initial individuals. Second, an effective EDA-based global search is adopted to estimate the distribution of excellent individuals or solutions, which is beneficial to quickly guide the exploration to discover the promising regions in solution space. Third, a multi-neighborhood iterated local search with a fast Insert-based neighbor evaluation method is devised to conduct in-depth exploitation in the promising regions found by global search. Since both global exploration and local exploitation are well stressed, it is expected that the proposed MCEDA can achieve good performance in solving BFSP_SDST.

### 4.5. Computational complexity analysis

According to Fig. 4, the computational complexity (CC) of the pri-

# Algorithm 11: Multi-neighborhood iterated local search (MNILS) 

Input: $\pi_{\text {best }}, \pi^{\text {gen }}$ and $\mathbf{P M}_{\mathrm{n}=\mathrm{n}=\mathrm{n}}^{\text {gen }}$.
Output: $\pi_{\text {best }}$ and $C_{\max }\left(\pi_{\text {best }}\right)$.

1: $\pi_{\text {best }} \leftarrow P M \_$NeighborSearch $\left(\pi^{\text {gen }}, \pi_{\text {best }}, \mathbf{P M}_{\mathrm{n}=\mathrm{n}=\mathrm{n}}^{\text {gen }}\right) . / /$ Algorithm 8
2: $\pi_{\mathrm{cl}}^{\mathrm{gen}} \leftarrow$ Reference_ NeighborSearch $\left(\pi^{\mathrm{gen}}, \pi_{\text {best }}, \mathbf{P M}_{\mathrm{n}=\mathrm{n}=\mathrm{n}}^{\text {gen }}\right) . / /$ Algorithm 10
3: while the termination condition not met do
4: $\quad$ Randomly generate $u$ and $v$ and meet $|u-v|>|n / 3|$, Perform $\lceil n / 10\rceil$ times interchange operation on $\pi_{\mathrm{cl}}^{\mathrm{gen}}$.
5: $\quad \pi_{\mathrm{cl}}^{\mathrm{gen}} \leftarrow$ Interchange $\left(\pi_{\mathrm{cl}}^{\mathrm{gen}}, u, v\right) . / /$ perturbation phase
6: $\pi_{\text {best }} \leftarrow P M \_$NeighborSearch $\left(\pi_{\mathrm{cl}}^{\mathrm{gen}}, \pi_{\text {best }}, \mathbf{P M}_{\mathrm{n}=\mathrm{n}=\mathrm{n}}^{\mathrm{gen}}\right) . / /$ Algorithm 8
7: $\pi_{\mathrm{cl}}^{\mathrm{gen}} \leftarrow$ Reference_ NeighborSearch $\left(\pi_{\mathrm{cl}}^{\mathrm{gen}}, \pi_{\text {best }}, \mathbf{P M}_{\mathrm{n}=\mathrm{n}=\mathrm{n}}^{\mathrm{gen}}\right) . / /$ Algorithm 10
8: if $C_{\max }\left(\pi_{\mathrm{cl}}^{\mathrm{gen}}\right)<C_{\max }\left(\pi_{\mathrm{cl}}^{\mathrm{gen}}\right)$ then
9: $\pi_{\mathrm{cl}}^{\mathrm{gen}}=\pi_{\mathrm{cl}}^{\mathrm{gen}}$.
if $C_{\max }\left(\pi_{\mathrm{cl}}^{\mathrm{gen}}\right)<C_{\max }\left(\pi_{\text {best }}\right)$ then
11: $\pi_{\text {best }}=\pi_{\mathrm{cl}}^{\mathrm{gen}}$.
end if
13: else if $\operatorname{rand}() \leq \exp \left\{-\left(C_{\max }\left(\pi_{\mathrm{cl}}^{\mathrm{gen}}\right)-C_{\max }\left(\pi_{\mathrm{cl}}^{\mathrm{gen}}\right)\right) / T\right\}$ then
14: $\pi_{\mathrm{cl}}^{\mathrm{gen}}=\pi_{\mathrm{cl}}^{\mathrm{gen}} . / /$ accept the solution by probability
15: end if
16: end while
17: return $\pi_{\text {best }}$ and $C_{\max }\left(\pi_{\text {best }}\right)$.

mary parts of the proposed MCEDA is analyzed as follows. At the initialization phase, since the CC of determining makespan by the forward calculation in Eqs. (1)-(5) or by the backward calculation in Eqs. (7)-(12) is $O(m n)$, the CC of evaluating the population is $O$ (popsize $\times$ $m n$ ). In Algorithm 2, the CCs of calculating $I(i)$ and $e_{i}$ are $O(m n)$, and the CCs of Line 2, Line 5, Lines 7-10, and Lines 3-12 are $O(n \log n), O\left(m n^{2}\right)$, $O\left(m n^{3}\right)$, and $O\left(\operatorname{zmn}^{3}\right)$, respectively. Hence, the CC of Algorithm 2 is $O\left(\operatorname{zmn}^{3}\right)$. In Algorithm 3, the CC of computing $L_{2}(i)$ is $O(m n)$, and the CCs of Lines 2-3, Line 6, Lines 7-13, and Lines 4-15 are $O(n \log n), O\left(m n^{2}\right)$, $O\left(m n^{3}\right)$, and $O\left(\operatorname{zmn}^{3}\right)$, respectively. Hence, the CC of Algorithm 3 is $O\left(\operatorname{zmn}^{3}\right)$. Since the fast Insert-based neighbor evaluation method given in Subsection 4.3.1 is used to reduce the CC of evaluating solution from $O(m n)$ to $O(m)$, the CCs of Algorithms 2 and 3 are also reduced from $O\left(\operatorname{zmn}^{3}\right)$ to $O\left(\operatorname{zmn}^{2}\right)$. In Subsection 4.2.1, the CC of calculating $M C_{n \times n \times n}^{\text {gen }}$ is $O(n^{3})$ when using Eqs. (20)-(23) and the CC of initializing $P M_{n \times n \times n}^{\text {gen }}$ is $O\left(n^{3}\right)$ when using Eqs. (24)-(26).

At the iterative process, since spsize superior solutions are selected from $\boldsymbol{P o p}(\boldsymbol{g e n})$ to calculate $\boldsymbol{M} C_{n \times n \times n}^{\text {gen }}$, the CC of sorting the population via quick sort method is $O$ (popsize $\times$ logpopsize). In Algorithm 4, the CC of Line 1 is $O(n)$ and that of Lines 2-10 is also $O(n)$. So, the CC of Algorithm 4 is $O(n)$. In Algorithm 5, the CC of Lines 2-6 is $O(n)$. Thus, the CC of Algorithm 5 is $O(n)$. In Algorithm 6, the CCs of Lines 2-9 and Lines 1-11 are $O\left(n^{2}\right)$ and $O$ (popsize $\times n^{2}$ ), respectively. So, the CC of generating a new population by sampling $P M_{n \times n \times n}^{\text {gen }}$ in Subsection 4.2.2 is $O$ (popsize $\times$ $n^{2}$ ). Note that the CC of updating $P M_{n \times n \times n}^{\text {gen }}$ is also $O\left(n^{3}\right)$ according to Eq. (26). Moreover, in Subsection 4.2.3, the CCs of calculating diversity index value $P_{\text {div }}$ and that of reinitializing part of the individuals in the population are nearly $O(n)$ and $O$ (popsize $\times n^{2}$ ), respectively. In Algorithm 8, the CCs of Lines 7-12, Lines 14-19, Lines 4-26, and Lines 2-27 are nearly $O(n), O(n), O\left(m n^{2}\right)$, and $O\left(m n^{3}\right)$, respectively. In Algorithm 10, the CCs of Line 7, Lines 12-17, and Lines 2-19 are nearly $O(\operatorname{len}),$ $O\left(m n^{2}\right)$, and $O\left(m n^{3}\right)$. In Algorithm 11, the CCs of Line 1, Line 2, and Lines 3-16 are all approximately equal to $O\left(m n^{3}\right)$. Since the fast Insertbased neighbor evaluation method is used to calculate neighbor solutions and the probabilistic model is employed to guide neighborhood searches, the CC of conducting MNILS in Algorithm 11 is estimated to be $O(m n \log n)$, where $O(\log n)$ is less than linear time $O(n)$.

Let $T_{\mathrm{CC}}$ be the total CC of MCEDA, and $K_{2}^{\text {gen }}\left(K_{2}^{\text {gen }}\right)$ the repeat times of Algorithms 8 (Algorithms 10) at generation gen for a given instance. Then, denote $K_{1}=\sum_{g m=1}^{m n \text { nggen }} K_{1}^{\text {gen }}$ and $K_{2}=\sum_{g m=1}^{m n \text { nggen }} K_{2}^{\text {gen }}$. Since $K_{2}^{\text {gen }}$ and $K_{2}^{\text {gen }}$ are no less than one, we have $K_{1}, K_{2} \geq$ maxgen. In general, $n$ is larger than $m$ and len. According to the above analysis, $T_{\mathrm{CC}}$ can be expressed as.

$$
\begin{aligned}
& T_{C C}=O\left(\text { maxgen } \times\left(\operatorname{zmn}^{2}+m n^{2}+n^{3}+\text { popsize } \times n^{2}\right)\right. \\
& \quad+K_{1} \times m n \log n+K_{2} \times m n \log n) \\
& =O\left(\text { maxgen } \times\left(n^{3}+\text { popsize } \times n^{2}\right)+\bar{K} \times m n \log n\right),
\end{aligned}
$$

where $\bar{K}$ is the average repeat times of executing Algorithms 8 and 10. From Eq. (29), it can be observed that the CC of MCEDA is acceptable because the highest degree in $\left(\right.$ maxgen $\times\left(n^{2}+\right.$ popsize $\times n^{2}$ ) $+\bar{K} \times m n \log n$ ) is three.

## 5. Experimental results and statistical analysis

This section implements the extensive experiments to demonstrate the effectiveness and efficiency of the proposed MCEDA. Firstly, the experimental setup is briefly described in Section 5.1, including the testing instances, performance metrics, and experimental environment. Then, the effects of MCEDA's parameters are discussed in Section 5.2. Afterwards, the superiority of multi-dimensional probabilistic model and the advantages of improvement strategies are investigated in Section 5.3 and Section 5.4, respectively. Finally, computational comparisons and statistical analysis of MCEDA against several state-of-the-art algorithms are conducted and discussed.

### 5.1. Experimental setup

In order to investigate the performance of the proposed MCEDA, a set of well-known benchmark datasets provided by Ruiz, et al. (2005) for PFSP_SDST are employed as test sets, which are available at https://soa. ifl.es/. These test sets contain a total of 480 instances with different sizes, which can be divided into four subsets according to different setup times, namely SSD-10, SSD-50, SSD-100, and SSD-125. Each subset consists of 120 different instances, ranging from 20 jobs and 5 machines to 500 jobs and 20 machines. The processing time of each job is randomly generated in the uniformly distributed interval [1, 99]. The setup times in each test subset SSD-K ( $K=10,50,100$ and 125) are randomly generated in the uniformly distributed interval $[1, K-1]$. The comparison algorithms are all conducted in the same programming environment and computer configuration. All algorithms are coded in Pascal language, compiled by Embarcadero Rad Studio (XE8), and executed independently on a PC equipped with Inter(R) Core(TM) i7-8700 M @ 3.2 GHz processor and 32 GB of RAM memory under Windows 7 OS. It should be noted that all algorithms have the same termination condition, i.e., the maximum elapsed CPU time of 60 nm milliseconds. Moreover, to fairly derive reliable computation results in the same time, each algorithm for each specific instance is performed 30 times independently. Therefore, a total number of 14,400 results are available for each algorithm, and the computational comparisons are completely fair and comparable. In order to evaluate the performance of the algorithms, the average relative percent deviation (ARPD) is used to measure the average relative quality of the experimental results, as stated by Eq. (30):
$A R P D=\frac{1}{R} \sum_{i=1}^{R} \frac{\left(C_{i}-C_{s p t}\right)}{C_{s p t}} \times 100 \%$
where $R$ is the number of runs. $C_{i}$ is the makespan obtained by a specific algorithm in the $i$ th experiment for a given instance. $C_{s p t}$ is the optimal makespan for that instance. Since few algorithms are devised to solve the problem under consideration, the minimum makespan found by all algorithms is selected as $C_{s p t}$. For the calibration of the algorithm parameters, $C_{s p t}$ is the best makespan found by all configurations for the calibration instance. It is obvious that the smaller the value of ARPD, the better the performance of the algorithm. In the statistical table of the experimental results, the best values obtained are highlighted in bold font, the second-best values are indicated in bold and underlined font, and the third-best values are marked in italic and underlined font.

### 5.2. Parameter calibration

Parameter calibration has an important impact on the efficacy and efficiency of HIOAs. As stated in Section 4, the proposed MCEDA contains four controllable parameters, i.e., population size (popsize), proportion of superior solutions $(\psi)$, learning rate $(\nu)$, and diversity threshold $(\delta)$. In order to calibrate these parameters, the Design of Experiments (DOE) approach (Montgomery, 2008) is employed to provide proper parameters of MCEDA. To further investigate the sensitivity and interaction of parameters, all of the obtained experiment results are analyzed by the multi-factor Analysis of Variance (ANOVA) technique, which has been widely used in the scheduling literature (Shao, et al., 2018a, 2018b). According to the research in recent years (Shao, et al., 2018b), if the algorithm's parameters are calibrated by using the same instances (see Section 5.1) that will later be used for comparison, the calibrated parameters may over fit (Shao, et al., 2018b). Thus, the additional subsets (i.e., ASSD-10, ASSD-50, ASSD-100 and ASSD-125) are generated for parameter calibration. The instances in each ASSD-K $(K=10,50,100$ and 125) are generated in the same way as those in the corresponding SSD- $K$ in Section 5.1, and each ASSD-K is half the size of the SSD- $K$. That is, there are a total of 240 instances. Moreover, since the range of parameter values is more flexible, it is required to restrict the

Table 3
The level of each parameter for MCEDA.

| Parameter | Factor level |  |  |  |
| :-- | :-- | :-- | :-- | :-- |
|  | 1 | 2 | 3 | 4 |
| popsize | 50 | 100 | 150 | 200 |
| $\varphi$ | 0.1 | 0.2 | 0.3 | 0.4 |
| $r$ | 0.1 | 0.2 | 0.3 | 0.4 |
| $\delta$ | 0.2 | 0.3 | 0.4 | 0.5 |

Table 4
Results of ANOVA for MCEDA`s parameters.

| Source | Sum of squares | Degrees of freedom | Mean <br> square | F-ratio | $p$ -value |
| :--: | :--: | :--: | :--: | :--: | :--: |
| Main effects |  |  |  |  |  |
| popsize | 0.016 | 3 | 0.005 | 537.00 | 0.000 |
| $\varphi$ | 0.010 | 3 | 0.003 | 346.13 | 0.000 |
| $r$ | 0.016 | 3 | 0.005 | 538.97 | 0.000 |
| $\delta$ | 0.008 | 3 | 0.003 | 272.97 | 0.000 |
| Interactions |  |  |  |  |  |
| popsize* $\varphi$ | 0.033 | 15 | 0.002 | 215.487 | 0.000 |
| popsize* $r$ | 0.008 | 12 | 0.001 | 68.555 | 0.000 |
| popsize* $\delta$ | 0.010 | 12 | 0.001 | 86.743 | 0.000 |
| $\varphi^{*} r$ | 0.000 | 9 | 0.000 | 0.039 | 1.000 |
| $\varphi^{*} \delta$ | 0.000 | 9 | 0.000 | 0.590 | 0.804 |
| $r^{*} \delta$ | 0.000 | 9 | 0.000 | 0.108 | 0.999 |
| Residual | 0.002 | 189 | 0.000 |  |  |
| Total | 0.053 | 255 |  |  |  |

selection range of parameters. The reasonable range for each parameter is determined according to the previous literature (Pan \& Ruiz, 2012; Zhang, et al., 2021; Zhang, et al., 2022) and our preliminary experiments. Following that, the multiple potential levels (values) for each factor (parameter) are determined by trial and error.

The levels of each parameter are listed in Table 3. The full factorial experimental design is conducted for the proposed MCEDA with $4 \times 4 \times$ $4 \times 4=256$ distinct configurations. MCEDA is repeated 30 times with a running time of 60 mm milliseconds on each instance. As a result, a total of $256 \times 30 \times 240=1843200$ results are obtained. In consequence, if the test program runs as a whole single process program. it needs at least 280 CPU days to obtain the entire experimental results. Fortunately, due to the multi-core architecture in our personal computers, the test program was divided into different sub-programs, which were arranged to run on different cores. So, it actually took about 12.5 days to complete the calibration.

The parameter is regarded as the controller factor, and the average ARPD value is regarded as the response variable (RV). Obviously, the lower the RV value is, the better the performance is. Moreover, three
major hypotheses (i.e., normality, homogeneity of variance, and independence of residuals) are checked before ANOVA is conducted. The checked results reveal that no significant deviations are found, so these hypotheses can be accepted. Note that the $F$-ratio is a strong signal of significance when the $p$-value is less than the confidence level. The larger the $F$-ratio is, the greater the effect of the factor on the RV is. The ANOVA results are reported in Table 4. The main effects plot for all parameters is shown in Fig. 5.

It is clearly observed from Table 4 that four parameters popsize, $\varphi, r$ and $\delta$ are statistically significant since their $p$-values are smaller than $\alpha=$ 0.05 ( $\alpha$ denotes the confidence level). The parameter popsize achieves the largest $F$-ratio, indicating that the population size has the most significant effect on the performance of the proposed MCEDA. As can be seen in Fig. 5, the choice of popsize $=100$ yields the best result, while popsize $=200$ obtains the worst result. It suggests that a medium-scale population is advantageous to maintain a proper search scope in solution space and ensure a certain search efficiency. The second largest $F$ ratio value corresponds to the factor $\varphi$. As also can be seen in Fig. 5, the value $\varphi=0.2$ can achieve the best performance, while $\varphi=0.1$ and $\varphi=$ 0.4 yield worse results. It is obvious that the proportion of superior solutions has a significant effect on the probabilistic model's ability of accumulating the valuable information of promising patterns in highquality subpopulation. The third significant factor is parameter $r$. It is clear from Fig. 5 that too small or too large learning rate $r$ may degrade algorithm performance, and $r=0.3$ is a suitable choice. If the value of $r$ is set too high, the algorithm may converge prematurely, otherwise it may lead to slow convergence. Although the diversity threshold $\delta$ has the least impact on the algorithm's effectiveness, a lack of population diversity directly results in search stagnation. So, an appropriate diversity threshold still favors MCEDA in suitably switching between exploration and exploitation. Fig. 5 reveals that the proper value of $\delta$ is 0.3 .

Although the main effects in Fig. 5 show the best choice of each single parameter, the analysis on single parameter is incomplete if there are significant interactions between parameters (Tasgetiren, et al., 2017). Thus, the two-level interactions between the involved parameters are also investigated, and the relevant results are reported in Table 4. It is observed from Table 4 that the interactions of three parameter pairs (i.e., popsize* $\varphi$, popsize* $r$, and popsize* $\delta$ ) are statistically significant since their $p$-values are less than 0.05 . The interaction effect plots of these parameter pairs are depicted in Fig. 6. From Fig. 6, it can be seen that all the interactions of popsize* $\varphi$, popsize* $r$, and popsize* $\delta$ are weak and coincide with the conclusions drawn from Fig. 5. Based on the above analyses, the parameters of MCEDA are set as: popsize $=100, \varphi=$ $0.2, r=0.3, \delta=0.3$.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Main effect plots of parameters.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Interaction effect plots of parameter pairs.

### 5.3. Performance analysis of improvement strategies

As stated in Section 4, there are four important improvement strategies contributing to improving the performance of our presented MCEDA: (1) the problem's characteristics based two constructive heuristics developed in Subsections 4.1.1 and 4.1.2; (2) the diversity controlling mechanism described in Subsection 4.2.3; (3) the fast Insertbased neighbor evaluation method provided in Subsection 4.3.1; and (4) the multi-neighborhood local search controlled by multi-dimensional probabilistic model referred in Subsections 4.3.2-4.3.4. In order to analyze the performance of these strategies, in this section, six variants of MCEDA are implemented to investigate and validate their contributions. Firstly, to evaluate the effectiveness of the initialization method, we utilize the random initialization method to replace the original one, yielding a variant named MCEDA $_{v 1}$. In MCEDA $_{v 1}$, the initial population is randomly generated without using constructive heuristics or scheduling rules. Secondly, to validate the proposed diversity controlling mechanism, the diversity controlling mechanism is removed from MCEDA and a variant algorithm named MCEDA $_{v 2}$ is developed, in which the population is never reinitialized throughout the execution of MCEDA $_{v 2}$. Thirdly, to determine if the proposed fast evaluation method promotes the efficiency of local search, we adjust the neighbor calculation method in local search to produce a variant that does not employ the fast Insert-based neighbor evaluation method, designated as MCEDA $_{v 3}$. Finally, to examine the effectiveness of local search controlled by the multi-dimensional probabilistic model, we implement three variants of MCEDA, including MCEDA without $N S_{\text {PM_boost }}$ (denoted as MCEDA $_{v 4}$ ), MCEDA without $N S_{\text {PM_85_guide }}$ (denoted as MCEDA $_{v 5}$ ), and MCEDA without MNILS (denoted as MCEDA $_{v 6}$ ). Note that for the first two variants, i.e., MCEDA $_{v 4}$ and MCEDA $_{v 5}$, MNILS is implemented based only on a single neighborhood search strategy, i.e., $N S_{\text {PM_boost }}$ or $N S_{\text {PM_85_guide }}$. These two variants are adopted to certify that the proposed two neighborhood search strategies are essential for local search. The last one is
used to verify the vital role of the devised MNILS for the proposed MCEDA.

To sum up, a total of six MCEDA's variants are created to demonstrate the effectiveness of these improvement strategies. The controlled experiments are conducted in such a way that each variant modifies a single component of the complete MCEDA. To guarantee a fair comparison, the probabilistic model update mechanism and sampling strategy remain the same in MCEDA and its variants, and the parameters of the above algorithms are also the same. The MCEDA and all variants adopt the same 60 nm millisecond elapsed CPU time, and they are tested by running 30 times independently on each instance. The benchmark instances introduced in Section 5.1 are employed as the testbed. The statistical results obtained by computational comparisons are reported in Table 5, grouped by each scenario and per number of jobs.

As shown in Table 5, the proposed MCEDA outperforms the other variants over a variety of scale instances. The results obtained by MCEDA are remarkably better in terms of both the average relative percent deviation (ARPD) and the standard deviation (SD), indicating that these improvement strategies contribute considerably to improving the performance of MCEDA. Specifically, MCEDA yields much better ARPD values than MCEDA $_{v 1}$ for different scales and scenarios, implying that both constructive heuristics affect algorithm's performance, especially for the large-scale instances. The two constructive heuristics (i.e., PFT_NEH(x) and PFZ_BZ(x)) utilize problem properties to produce partially promising solutions, which can provide better starting points for subsequent searches and notably narrow the search scope. That is, MCEDA is afforded more opportunities to find promising search regions within the reduced search space. Moreover, the results of MCEDA $_{v 2}$ is slightly weaker than MCEDA, indicating that the proposed diversity mechanism not only ensures the vitality of the search to avoid stagnation, but also preserves the population diversity and evolutionary information. As can be observed from Table 5, MCEDA $_{v 3}$ is somewhat inferior to MCEDA in all scenarios, which demonstrates the effectiveness

Table 5
Comparison results of MCEDA with its six variants.

| Scenario | n | $\mathrm{MCEDA}_{v 3}$ |  | $\mathrm{MCEDA}_{v 2}$ |  | $\mathrm{MCEDA}_{v 5}$ |  | $\mathrm{MCEDA}_{v 4}$ |  | $\mathrm{MCEDA}_{v 5}$ |  | $\mathrm{MCEDA}_{v 6}$ |  | $\mathrm{MCEDA}$ |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | ARPD | SD | ARPD | SD | ARPD | SD | ARPD | SD | ARPD | SD | ARPD | SD | ARPD | SD |
| SSD-0 | 20 | 0.027 | 0.296 | 0.017 | 0.286 | 0.023 | 0.293 | 0.193 | 0.332 | 0.182 | 0.361 | 0.334 | 0.557 | 0.013 | 0.284 |
|  | 50 | 1.154 | 0.288 | 0.843 | 0.263 | 1.224 | 0.282 | 1.773 | 0.341 | 1.569 | 0.355 | 2.532 | 0.584 | 0.357 | 0.257 |
|  | 100 | 1.108 | 0.282 | 0.885 | 0.257 | 1.182 | 0.271 | 1.554 | 0.336 | 1.375 | 0.343 | 2.375 | 0.611 | 0.383 | 0.248 |
|  | 200 | 0.579 | 0.264 | 0.712 | 0.253 | 0.761 | 0.264 | 1.141 | 0.363 | 0.973 | 0.376 | 1.794 | 0.573 | 0.362 | 0.245 |
|  | 500 | 0.475 | 0.323 | 0.555 | 0.295 | 0.637 | 0.295 | 1.773 | 0.425 | 0.825 | 0.443 | 1.483 | 0.607 | 0.188 | 0.283 |
| Average |  | 0.669 | 0.291 | 0.602 | 0.271 | 0.765 | 0.281 | 1.287 | 0.359 | 0.985 | 0.376 | 1.704 | 0.586 | 0.261 | 0.263 |
| SSD-10 | 20 | 0.021 | 0.291 | 0.015 | 0.281 | 0.021 | 0.286 | 0.186 | 0.343 | 0.176 | 0.363 | 0.323 | 0.561 | 0.011 | 0.279 |
|  | 50 | 1.027 | 0.298 | 0.736 | 0.268 | 1.207 | 0.291 | 1.652 | 0.347 | 1.464 | 0.367 | 2.434 | 0.578 | 0.243 | 0.265 |
|  | 100 | 1.054 | 0.282 | 0.827 | 0.262 | 1.118 | 0.268 | 1.478 | 0.344 | 1.262 | 0.355 | 2.324 | 0.597 | 0.335 | 0.257 |
|  | 200 | 0.533 | 0.279 | 0.652 | 0.253 | 0.667 | 0.272 | 1.034 | 0.371 | 0.918 | 0.368 | 1.732 | 0.566 | 0.328 | 0.246 |
|  | 500 | 0.436 | 0.323 | 0.517 | 0.284 | 0.541 | 0.314 | 1.766 | 0.432 | 0.775 | 0.437 | 1.426 | 0.612 | 0.173 | 0.258 |
| Average |  | 0.614 | 0.295 | 0.549 | 0.270 | 0.711 | 0.286 | 1.223 | 0.367 | 0.919 | 0.378 | 1.648 | 0.583 | 0.218 | 0.261 |
| SSD-50 | 20 | 0.026 | 0.288 | 0.018 | 0.283 | 0.024 | 0.282 | 0.193 | 0.345 | 0.188 | 0.364 | 0.338 | 0.553 | 0.014 | 0.271 |
|  | 50 | 1.112 | 0.296 | 0.823 | 0.264 | 1.218 | 0.286 | 1.742 | 0.332 | 1.543 | 0.373 | 2.524 | 0.581 | 0.345 | 0.254 |
|  | 100 | 1.027 | 0.278 | 0.746 | 0.258 | 1.043 | 0.272 | 1.424 | 0.347 | 1.215 | 0.356 | 2.257 | 0.594 | 0.287 | 0.243 |
|  | 200 | 0.436 | 0.267 | 0.612 | 0.255 | 0.634 | 0.261 | 1.007 | 0.355 | 0.826 | 0.372 | 1.671 | 0.568 | 0.243 | 0.246 |
|  | 500 | 0.413 | 0.324 | 0.523 | 0.276 | 0.535 | 0.295 | 1.731 | 0.428 | 0.796 | 0.445 | 1.433 | 0.611 | 0.186 | 0.257 |
| Average |  | 0.601 | 0.291 | 0.544 | 0.267 | 0.691 | 0.279 | 1.219 | 0.361 | 0.914 | 0.382 | 1.645 | 0.581 | 0.215 | 0.254 |
| SSD-100 | 20 | 0.022 | 0.295 | 0.015 | 0.287 | 0.021 | 0.289 | 0.186 | 0.361 | 0.174 | 0.355 | 0.331 | 0.546 | 0.013 | 0.271 |
|  | 50 | 1.024 | 0.277 | 0.752 | 0.262 | 1.163 | 0.268 | 1.632 | 0.345 | 1.438 | 0.364 | 2.423 | 0.576 | 0.287 | 0.258 |
|  | 100 | 1.085 | 0.273 | 0.836 | 0.263 | 0.985 | 0.273 | 1.439 | 0.353 | 1.312 | 0.343 | 2.354 | 0.591 | 0.322 | 0.255 |
|  | 200 | 0.417 | 0.267 | 0.554 | 0.252 | 0.572 | 0.262 | 0.976 | 0.365 | 0.753 | 0.368 | 1.548 | 0.563 | 0.167 | 0.227 |
|  | 500 | 0.337 | 0.326 | 0.473 | 0.281 | 0.506 | 0.295 | 1.711 | 0.416 | 0.762 | 0.437 | 1.412 | 0.603 | 0.143 | 0.263 |
| Average |  | 0.577 | 0.288 | 0.526 | 0.269 | 0.649 | 0.277 | 1.189 | 0.368 | 0.888 | 0.373 | 1.614 | 0.576 | 0.186 | 0.255 |
| SSD-125 | 20 | 0.024 | 0.292 | 0.017 | 0.281 | 0.019 | 0.285 | 0.182 | 0.356 | 0.167 | 0.352 | 0.328 | 0.552 | 0.011 | 0.268 |
|  | 50 | 1.017 | 0.288 | 0.782 | 0.257 | 1.183 | 0.267 | 1.651 | 0.348 | 1.426 | 0.356 | 2.513 | 0.571 | 0.283 | 0.252 |
|  | 100 | 1.021 | 0.279 | 0.743 | 0.251 | 0.894 | 0.272 | 1.374 | 0.344 | 1.221 | 0.338 | 2.221 | 0.587 | 0.245 | 0.246 |
|  | 200 | 0.483 | 0.265 | 0.615 | 0.245 | 0.632 | 0.257 | 0.979 | 0.357 | 0.864 | 0.362 | 1.624 | 0.553 | 0.223 | 0.241 |
|  | 500 | 0.412 | 0.323 | 0.531 | 0.273 | 0.546 | 0.303 | 1.761 | 0.422 | 0.812 | 0.426 | 1.457 | 0.592 | 0.182 | 0.254 |
| Average |  | 0.591 | 0.289 | 0.538 | 0.261 | 0.655 | 0.277 | 1.189 | 0.365 | 0.898 | 0.367 | 1.629 | 0.571 | 0.189 | 0.252 |
| Tot. average |  | 0.611 | 0.291 | 0.552 | 0.268 | 0.694 | 0.280 | 1.222 | 0.364 | 0.921 | 0.375 | 1.648 | 0.579 | 0.214 | 0.257 |

of the fast Insert-based neighbor evaluation method. Indeed, the proposed fast evaluation method facilitates the efficiency of evaluating Insert-based neighbor solutions and reduces the computational cost, thereby allowing more iterations and raising the chances of discovering more promising solutions with less computational effort.

From Table 5, it can be seen that the total average values of MCEDA ${ }_{v 4}$ (1.222), MCEDA ${ }_{v 5}(0.921)$ and MCEDA ${ }_{v 6}(1.648)$ are inferior to MCEDA (0.214). As regards MCEDA $_{v 6}$, it achieves the worst results, remarkably lags behind other competitors, clearly revealing that the integration of both $N S_{\text {PM_boost }}$ and $N S_{\text {PM_RS_guide }}$ in the multi-neighborhood iterated local search effectively enhances the searchability. Since both neighborhood search strategies, i.e., $N S_{\text {PM_boost }}$ and $N S_{\text {PM_RS_guide }}$, can utilize valuable probability information of promising patterns from superior solutions to drive neighborhood search, MNILS can fully exploit local areas in depth by cyclically switching between neighborhood search strategies through the framework of ILS. If it is eliminated, the capacity for local exploitation would be greatly diminished. Furthermore, the $S D$ values of MCEDA are smaller than those of its variants, i.e., MCEDA produces more stable results across various scale instances, indicating that MCEDA has good robustness and stability. As a consequence of such comparison, MCEDA has a stronger and superior search power, demonstrating the advantages of all well-designed improvement strategies.

Although the statistical results in Table 5 illustrate the superiority of incorporating improvement strategies, ANOVA is still used to further confirm the significance of the observed differences. The results of the ANOVA are reported in Fig. 7, which depicts the interaction between algorithms and scenarios with $95 \%$ Tukey's Honest Significant
![img-6.jpeg](img-6.jpeg)

Fig. 7. Interaction plot with 95\% Tukey's HSD confidence interval between algorithm and scenario.

Difference (HSD) confidence intervals. Note that the overlapping intervals among algorithms imply that there are statistically insignificant differences in their performances. As shown in Fig. 7, MCEDA is significantly superior to the other six variants due to the absence of overlapping intervals, confirming the above conclusion that these improvement strategies have a great potential to boost the performance of MCEDA.

![img-7.jpeg](img-7.jpeg)

Fig. 8. Comparisons of EDA's global performance.

# 5.4. Comparisons of MCEDA and other two-dimensional EDAs 

Since most well-performing EDA-based algorithms use twodimensional probabilistic models to guide the global search direction, it is critical to conduct a comprehensive investigation of the global search performance of EDA-based algorithms. To verify the proposed MCEDA's superiority over existing two-dimensional probabilistic model-based EDAs for BFSP_SDST, we compared it with three recently proposed two-dimensional probabilistic model-based EDAs, including the state-of-the-art EDA (JEDA) (Jarboui, et al., 2009), the effective EDA (EEDA) (Wang, et al., 2013), and the modified JEDA (P-EDA) (Pan \& Ruiz, 2012). To eliminate the effect of local search on the global performance of these EDAs, only the framework of global search for all EDA-based algorithms is used to perform global exploration without local search. These variants are abbreviated as MCEDA ${ }_{\text {nib }}$, JEDA ${ }_{\text {nib }}$, EEDA $_{\text {nib }}$, and P-EDA ${ }_{\text {nib }}$. The parameters of these EDA-based algorithms are set to the same values as in the original literature. The experimental results under five different scenarios are summarized in Table 6 .

As can be observed from Table 6, MCEDA ${ }_{\text {nib }}$ achieves the best results in almost all instances compared to the existing effective twodimensional probabilistic model-based EDAs. Specifically, the global performance of $\mathrm{P}-\mathrm{EDA}_{\text {nib }}$ is significantly better than that of $\mathrm{JEDA}_{\text {nib }}$ and $\mathrm{EEDA}_{\text {nib }}$, which indicates that $\mathrm{P}-\mathrm{EDA}_{\text {nib }}$ can attain better search performance by using two two-dimensional matrices to preserve information of both the order of jobs and the number of similar blocks. However, the proposed MCEDA ${ }_{\text {nib }}$ notably outperforms all the existing EDA-based algorithms in terms of ARPD values for five scenarios, SSD-0, SSD-10, SSD-50, SSD-100, and SSD-125. For different setup time scenarios, the histogram including means with $95 \%$ Tukey's HSD confidence interval is illustrated in Fig. 8. It is clear that, as compared to other EDA-based algorithms, MCEDA ${ }_{\text {nib }}$ can yield significantly lower ARPD and relatively smaller $S D$ with considerable advantages. These findings demonstrate the benefits of the matrix-cube-based probabilistic model in improving the performance of MCEDA. The main reason is explained by the fact that the three-dimensional probabilistic model employed in MCEDA ${ }_{\text {nib }}$ is capable of not only learning valuable information about the order of jobs that existed in superior solutions, but also accurately and reasonably recording the relative position of each similar block, which is difficult to do with two-dimensional probabilistic models. So, for the two-dimensional probabilistic model-based EDAs, similar blocks cannot be placed in the correct positions to produce new individuals during the sampling process, resulting in relatively poor search capability of these comparison algorithms. According to the above experiments and analysis, it can be concluded that the proposed matrix-cube-based probabilistic model plays an important role in MCEDA. Also, it may be

worthwhile to consider embedding the developed multi-dimensional probabilistic model into other HIOAs for solving BFSPs in future research.

### 5.5. Comparisons of MCEDA and the state-of-the-art methods

To evaluate the effectiveness and efficiency of the proposed MCEDA, this section aims to compare the performance of MCEDA against several state-of-the-art algorithms available in the literature. As described in Section 2, it should be noted that few algorithms are directly designed to address the BFSP_SDST; accordingly, any algorithms that attempt addressing the BFSP_SDST and its relevant problems are considered for computational comparison. For various types of FSPs and BFSPs with makespan criterion, the efficacy of MCEDA with various highperformance algorithms is comprehensively compared according to the same benchmark test sets as SSD-10, SSD-50, SSD-100, and SSD-125 introduced in Section 5.1. These algorithms may be classified into three categories. The first group has a single algorithm, i.e., DWWO (Shao, et al., 2018b), which is developed to solve the BFSP_SDST; The second group contains fourteen algorithms, including HDDE (Wang, et al., 2010), hmgHS (Wang, et al., 2011), TPA (Wang, et al., 2012), MA (Pan, et al., 2013), RAIS (Lin \& Ying, 2013), SVNS_S and SVNS_D (Ribas, et al., 2013), HVNS (Moslehi \& Khorasanian, 2014), DE_ABC (Han, et al., 2015), DE_PLS (Tasgetiren, et al., 2015), MFFO (Han, et al., 2016), IG_U
and IG_RLS (Tasgetiren, et al., 2017), and P-EDA (Shao, et al., 2018a), where these algorithms are designed to address the BFSP; The third group contains six algorithms, including HGA (Ruiz, et al., 2005), PACA (Gajpal, et al., 2006), IG_RS (Ruiz \& Stutzle, 2008), $\mathrm{AHA}_{1}$ and $\mathrm{AHA}_{2}$ (Li \& Zhang, 2012), EMBO (Sioad \& Gagne, 2018), all of which are developed to deal with the PFSP. Additionally, since the proposed MCEDA is designed based on the multi-dimensional probabilistic model, it is necessary to further conduct a comparison between MCEDA and an effective two-dimensional probabilistic-model-based EDA, i.e., EEDA (Wang, et al., 2013). The total of twenty two typical algorithms mentioned above are the most effective algorithms available for dealing with BFSP, PFSP and their extensions. Among these algorithms, DWWO, HDDE, HMGHS, MA, RAIS, DE_ABC, DE_PLS, MFFO, P-EDA, HGA, PACA, AHA1, AHA3, EMBO, and EEDA all fall within the category of population-based HIOAs. All algorithms are re-implemented strictly in accordance with the original literature, with appropriate adjustments to adapt the BFSP SDST with makespan criterion. Meanwhile, the fast Insert-based neighbor evaluation method described in Subsection 4.3.1 is incorporated into these re-implemented algorithms to expedite search efficiency. The parameters of each algorithm are derived from the suggested settings in the original literature, and the same calibration method as stated in Section 5.2 is employed to recalibrate the relevant parameters. The parameter values for all algorithms are reported in Table 7.

Table 7
Parameters of the compared algorithms for BFSP_SDST.

| Algorithm | Author(s) | Parameter setting |
| :--: | :--: | :--: |
| DWWO | Shao, et al. (2018b) | popsize $=5, i_{\max }=1, i_{\max }=2, b_{\max }=10, \omega=40$. |
| HDDE | Wang, et al. (2010) | popsize $=20, F=0.2, C R=0.2, P_{t}=0.2$. |
| hmgHS | Wang, et al. (2011) | $M S=5, P_{C R}=0.95, P_{A R}=0.95$. |
| TPA | Wang, et al. (2012) | $\begin{aligned} & T_{\text {frad }}=\sum_{s=1}^{n} \sum_{j=1}^{n} p_{s j} / 5 \mathrm{~mm}, T_{\text {frad }}=1, N_{\text {opt }}=100000, \\ & \alpha=0.8, \beta=\left(T_{\text {frad }}-T_{\text {frad }}\right) /\left(\left(N_{\text {opt }}-1\right) \times T_{\text {frad }}+T_{\text {frad }}\right), \end{aligned}$ |
| MA | Pan, et al. (2013) | popsize $=10, P_{t 0}=0.8, P_{c}=0.2, \lambda=20, \gamma=20$. |
| RAIS | Lin and Ying (2013) | $\begin{aligned} & T_{0}=0.6 \times \sum_{s=1}^{n} \sum_{j=1}^{n} p_{s j} / 10 \mathrm{~m}, D_{\text {threshold }}=5, G_{T}=4000, \\ & n_{c}=6, \alpha=0.97, \text { Max } T=60 \mathrm{~mm} . \\ & \alpha=0.75, \beta=0.5, d=8 . \end{aligned}$ |
| SVNS_D | Ribas, et al. (2013) | $\begin{aligned} & T_{\text {frad }}=\sum_{s=1}^{n} \sum_{j=1}^{n} p_{s j} / 5 \mathrm{~mm}, T_{\text {frad }}=0.1 \times T_{\text {frad }}, k_{\max }=100000, \\ & \beta=\left(T_{\text {frad }}-T_{\text {frad }}\right) /\left(\left(N_{\text {opt }}-1\right) \times T_{\text {frad }}+T_{\text {frad }}\right), \end{aligned}$ |
| HVNS | Roslehi and Khorasanian (2014) | popsize $=20, P_{t 00}=0.9, P_{c}=0.1, P_{b}=0.2$. |
| DE_ABC | Han, et al. (2015) | popsize $=10, F=20, P_{c}=0.1, \beta=0.0005, F=0.1$, $T_{\max }=60 \mathrm{~mm}$. |
| DE_PLS | Tasgetiren, et al. (2015) | popsize $=20, \varphi=0.75, p l s=0.6, T=5, T i m e_{\max }=60 \mathrm{~mm}$. |
| MFFO | Han, et al. (2016) | $\mathrm{d} s=8, \tau \mathrm{P}=0.5, j \mathrm{P}=0.001, T_{\max }=60 \mathrm{~mm}$. |
| IG_RLS | Tasgetiren, et al. (2017) | $\begin{aligned} & \text { popsize }=50, \lambda=0.3, t=60 \mathrm{~mm} . \\ & \text { popsize }=50, P_{c}=0.1, P_{t 0}=0.005, G_{t}=25 . \end{aligned}$ |
| P-EDA | Shao, et al. (2018a) | $\begin{aligned} & \tau_{\mathrm{p}}=1 / M_{\max } \rho=0.75 . \\ & \text { Temperature }=T \times \sum_{s=1}^{n} \sum_{j=1}^{n} p_{s j} / 10 \mathrm{~mm}, T=0.5, d=4 . \end{aligned}$ |
| HGA | Ruiz, et al. (2005) |  |
| PACA | Gajpal, et al. (2006) | $\begin{aligned} & \text { Temperature }=T \times \sum_{s=1}^{n} \sum_{j=1}^{n} p_{s j} / 10 \mathrm{~mm}, T=0.5, d=4 . \end{aligned}$ |
| IG_RS | Ruiz and Stutzle (2008) | popsize $=50, \alpha=20, \beta=20, \rho=1, \eta_{i}=0.7, P_{c}=0.6$, $P_{t 0}=0.02, P_{t}=0.1$. |
| AHA3 | Li and Zhang (2012) | popsize $=9, m=100, k=5, x=1$, age $=100, q_{0}=0.7, l=10$. |
| EMBO | Sioad and Gagne (2018) | popsize $=150, \eta=10, \alpha=0.1$. |
| EEDA | Wang, et al. (2013) |  |

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

The comprehensive comparison results of MCEDA against 22 different algorithms under different scenarios are summarized in Tables 8-12. Notably, the setup time for all instances in SSD-0 is zero, implying that the BFSP SDST is reduced to the BFSP in this scenario. As seen in Table 8, all ARPD values obtained by MCEDA are the smallest when compared to the other algorithms. These numerical results reflect that the proposed MCEDA is capable of successfully solving BFSP. Moreover, it can be observed from Tables 9-12 that MCEDA yields the lowest ARPD values on the other four test sets, SSD-10, SSD-50, SSD100, and SSD-125, indicating that the proposed MCEDA has a stronger search engine in terms of tackling the problem under consideration. Furthermore, MCEDA achieves the lowest overall average values of ARPD on 12 instances spanning a range of scales and scenarios, demonstrating that MCEDA outperforms the other algorithms in an average sense.

To further investigate the performance differences amongst algorithms, all results are also analyzed by means of multifactor ANOVA. The ANOVA is applied to determine whether or not there are indeed statistically significant differences in the ARPD values acquired by all of the compared algorithms. It is worth mentioning that in statistical trials with $95 \%$ confidence level $(\alpha=0.05)$, three main hypotheses are checked, including normality, homoscedasticity, and independence of residuals. From the analysis of the residuals resulting from the experimental results, all hypotheses are readily satisfied. Figs. 9-13 display the mean plots with $95 \%$ Tukey's HSD confidence intervals and the corresponding box plots for all test results obtained by MCEDA and 22 algorithms at different scales and scenarios, respectively. It is remarkable that the presence of overlapping confidence intervals between any two algorithms signifies that the observed differences are not statistically significant, signaling that there is no significant difference in the performance of algorithms. As can be seen in Figs. 9-13, there is no overlap between MCEDA and the other compared algorithms in different scenarios, indicating that the results achieved by MCEDA are statistically significant different from those acquired by other algorithms. In other words, from a statistical point of view, MCEDA has significant advantages in solving both BFSP and BFSP_SDST.

Moreover, when compared to several two-dimensional probabilistic model-based EDAs, MCEDA statistically significantly outperforms EEDA and P-EDA across all test sets, which highlights the fact that the developed multi-dimensional probabilistic model has obvious advantages in learning and utilizing promising patterns of superior solutions. It exhibits its prowess in terms of exploration and exploitation. Furthermore, the recently proposed DWWO and a series of enhanced or hybrid IG versions, including IG_RS, IG_RLS, and IG_U, are also competitive in all scenarios. It is obvious that the confidence intervals of DWWO and several extended IG are almost completely overlapped on SSD-0 and partially overlapped on SSD-10, SSD-50, SSD-100, and SSD-150, revealing that these algorithms perform similarly in these scenarios. In this sense, the results obtained by DWWO are slightly better than IG_RLS, except on the SSD-0, due to the SSD-performing local search mechanism, while the proposed MCEDA beats all its competitors by a considerable margin on small to large-scale instances. Also, as illustrated in the box plots in Figs. 9-13, MCEDA remarkably outperforms other state-of-the-art algorithms. In view of the abovementioned observations, not only the scheduling solutions provided by MCEDA are of higher quality, but the numerical results also have a narrower fluctuation range, implying that the proposed MCEDA is competitive and stable.

Additionally, according to the above analysis, it can be seen that there are significant differences in the performance of the compared algorithms for different scale instances and scenarios. To further investigate these behaviors, the interaction plots with $95 \%$ Tukey's HSD confidence interval between algorithm and $n$, between algorithm and $m$, and between algorithm and scenario, are provided in Figs. 14-16. As revealed in these figures, all algorithms are sensitive to the number of jobs, machines, and scenarios. However, as for the proposed MCEDA, it is depicted in Fig. 16 that the scales and scenarios have slight effect on it.

![img-11.jpeg](img-11.jpeg)

Fig. 9. Means plots with 95\% Tukey's HSD confidence interval and box plots for MCEDA compared with 22 different algorithms (SSD-0).
![img-12.jpeg](img-12.jpeg)

Fig. 10. Means plots with 95\% Tukey's HSD confidence interval and box plots for MCEDA compared with 22 different algorithms (SSD-10).
![img-13.jpeg](img-13.jpeg)

Fig. 11. Means plots with 95\% Tukey's HSD confidence interval and box plots for MCEDA compared with 22 different algorithms (SSD-50).

![img-14.jpeg](img-14.jpeg)

Fig. 12. Means plots with 95\% Tukey's HSD confidence interval and box plots for MCEDA compared with 22 different algorithms (SSD-100).
![img-15.jpeg](img-15.jpeg)

Fig. 13. Means plots with 95\% Tukey's HSD confidence interval and box plots for MCEDA compared with 22 different algorithms (SSD-125).
![img-16.jpeg](img-16.jpeg)

Fig. 14. Interaction plot with 95\% Tukey's HSD confidence interval between algorithm and $n$.
![img-17.jpeg](img-17.jpeg)

Fig. 15. Interaction plot with 95\% Tukey's HSD confidence interval between algorithm and $m$.

![img-18.jpeg](img-18.jpeg)

Fig. 16. Interaction plot with $95 \%$ Tukey's HSD confidence interval between algorithm and scenario.

Meanwhile, it is obvious that the proposed MCEDA performs superiorly and stably under different scale instances and scenarios, particularly when addressing the large-scale instances with $\pi \geq 100$, which suggests that MCEDA has superiority and stability.

Furthermore, to further verify the statistical validity of the numerical results obtained by these algorithms, the parametric Duncan's multiple range test (DMRT) is employed, which is a post hoc test for detecting the specific differences between pairs of means. Here, DMRT is used to categorize all comparing algorithms into distinct levels. Table 13 summarizes the results of DMRT under different scenarios with a confidence level of $\alpha=0.05$. As shown in Table 13, all algorithms are graded into twelve levels. MCEDA ranks the first level (i.e., A) for all scenarios, i.e., SSD-0, SSD-10, SSD-50, SSD-100, and SSD-125. There are no other algorithms except MCEDA in the level A, demonstrating that the differences between MCEDA with other compared algorithms are statistically significant and underlining the fact that MCEDA delivers the best performance among all compared algorithms. Meanwhile, DWWO, MA, IG_RLS, IG_U, IG_RS, and HVNS are grouped together at the second level, indicating that they have similar performance, and the remaining comparison algorithms perform worse. The DMRT further confirms the competitiveness of MCEDA.

To sum up, according to the above comparative results and statistical analysis, it can be credibly concluded that MCEDA is an extremely effective and efficient algorithm for BFSP_SDST aiming at minimizing makespan. The superiority of MCEDA is mainly attributed to the following aspects: (1) the designed fast Insert-based neighbor evaluation method reduces the computational cost and speeds up the search

Table 13
Results of Duncan's multiple range test $(\alpha=0.05)$.

| Rank | SSD-0 | SSD-10 | SSD-50 | SSD-100 | SSD-125 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| A | (MCEDA) | (MCEDA) | (MCEDA) | (MCEDA) | (MCEDA) |
| B | (IG,RLS, IG_U, DWWO, HVNS, IG_RS, MA, TPA, P-EDA, EEDA) | (DWWO, MA, IG,RLS, IG_U, IG_RS, HVNS, TPA) | (DWWO, MA, IG,RLS, IG_U, IG_RS, HVNS) | (DWWO, MA, IG,RLS, IG_U, IG_RS, HVNS) | (DWWO, IG,RLS, MA, IG_U, IG_RS, HVNS) |
| C | (SVNS_S, SVNS_D) | (SVNS_S, hmgHS, P-EDA, DE, PLS, SVNS_D) | (TPA, hmgHS, <br> EEDA, DE, PLS) | (SVNS_S, SVNS_D, <br> TPA, hmgHS) | (TPA, SVNS_S, <br> SVNS_D, hmgHS) |
| D | (hmgHS) | (EEDA) | (P-EDA) | (DE, PLS) | (DE, PLS) |
| E | (DE,PLS) | (MFFO, DE_ABC) | (SFNS_S) | (HODE, P-EDA) | (DE_ABC) |
| F | (EMBO) | (EMBO, HDDE) | (MFFO, SVNS_D, <br> DE_ABC, EMBO, HDDE) | (EEDA, DE_ABC) | (P-EDA, HDDE, EEDA, |
| G | (MFFO) | $\left(\mathrm{AHA}_{3}, \mathrm{HGA}, \mathrm{AHA}_{1}\right)$ | (AHA3) | (MFFO) | (EMBO, AHA ${ }_{3}, \mathrm{AHA}_{1}$ ) |
| H | (HDDE, DE_ABC, AHA ${ }_{3}$, HGA) | (RAIS, PACA) | (AHA3) | (AHA $_{3}$, EMBO) | (HGA) |
| I | (AHA) |  | (HGA) | (AHA) | (PACA) |
| J | (RAIS) |  | (RAIS) | (HGA) | (RAIS) |
| K | (PACA) |  | (PACA) | (PACA) |  |
| L |  |  |  | (PACA) |  |
| F-ratio | 6.752 | 7.294 | 6.921 | 6.322 | 6.000 |
| $p$-value | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Table 14
Best solutions for BFSP with makespan criterion.

| Instance | Best | MCEDA | Instance | Best | MCEDA | Instance | Best | MCEDA |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Ta1 | 1374 | 1374 | Ta41 | 3611 | 3617 | Ta81 | 7712 | 7712 |
| Ta2 | 1408 | 1408 | Ta42 | 3470 | 3470 | Ta82 | 7744 | 7744 |
| Ta3 | 1280 | 1280 | Ta43 | 3466 | 3466 | Ta83 | 7723 | 7723 |
| Ta4 | 1448 | 1448 | Ta44 | 3650 | 3650 | Ta84 | 7743 | 7743 |
| Ta5 | 1341 | 1341 | Ta45 | 3582 | 3596 | Ta85 | 7730 | 7734 |
| Ta6 | 1363 | 1363 | Ta46 | 3571 | 3571 | Ta86 | 7779 | 7779 |
| Ta7 | 1381 | 1381 | Ta47 | 3667 | 3667 | Ta87 | 7870 | 7870 |
| Ta8 | 1379 | 1379 | Ta48 | 3554 | 3554 | Ta88 | 7898 | 7921 |
| Ta9 | 1373 | 1373 | Ta49 | 3508 | 3515 | Ta89 | 7818 | 7818 |
| Ta10 | 1283 | 1283 | Ta50 | 3608 | 3608 | Ta90 | 7856 | 7856 |
| Ta11 | 1698 | 1698 | Ta51 | 4479 | 4479 | Ta91 | 13,149 | 13,149 |
| Ta12 | 1833 | 1833 | Ta52 | 4262 | 4262 | Ta92 | 13,100 | 13,100 |
| Ta13 | 1659 | 1659 | Ta53 | 4261 | 4261 | Ta93 | 13,204 | 13,204 |
| Ta14 | 1535 | 1535 | Ta54 | 4338 | 4345 | Ta94 | 13,125 | 13,125 |
| Ta15 | 1617 | 1617 | Ta55 | 4249 | 4252 | Ta95 | 13,150 | 13,150 |
| Ta16 | 1590 | 1590 | Ta56 | 4271 | 4274 | Ta96 | 12,922 | 12,922 |
| Ta17 | 1622 | 1622 | Ta57 | 4291 | 4291 | Ta97 | 13,431 | 13,445 |
| Ta18 | 1731 | 1731 | Ta58 | 4298 | 4298 | Ta98 | 13,299 | 13,299 |
| Ta19 | 1747 | 1747 | Ta59 | 4304 | 4304 | Ta99 | 13,105 | 13,105 |
| Ta20 | 1782 | 1782 | Ta60 | 4399 | 4399 | Ta100 | 13,201 | 13,201 |
| Ta21 | 2436 | 2436 | Ta61 | 6070 | 6070 | Ta101 | 14,192 | 14,237 |
| Ta22 | 2234 | 2234 | Ta62 | 5943 | 5943 | Ta102 | 14,749 | 14,749 |
| Ta23 | 2479 | 2479 | Ta63 | 5851 | 5851 | Ta103 | 14,874 | 14,874 |
| Ta24 | 2348 | 2348 | Ta64 | 5656 | 5667 | Ta104 | 14,808 | 14,808 |
| Ta25 | 2435 | 2435 | Ta65 | 5901 | 5908 | Ta105 | 14,628 | 14,628 |
| Ta26 | 2383 | 2383 | Ta66 | 5759 | 5764 | Ta106 | 14,765 | 14,793 |
| Ta27 | 2390 | 2390 | Ta67 | 5920 | 5922 | Ta107 | 14,787 | 14,787 |
| Ta28 | 2328 | 2328 | Ta68 | 5809 | 5809 | Ta108 | 14,836 | 14,845 |
| Ta29 | 2363 | 2363 | Ta69 | 6035 | 6035 | Ta109 | 14,711 | 14,711 |
| Ta30 | 2323 | 2323 | Ta70 | 6059 | 6059 | Ta110 | 14,750 | 14,758 |
| Ta31 | 2980 | 2980 | Ta71 | 6916 | 6916 | Ta111 | 35,513 | 35,524 |
| Ta32 | 3182 | 3182 | Ta72 | 6669 | 6671 | Ta112 | 35,805 | 35,805 |
| Ta33 | 2995 | 2995 | Ta73 | 6797 | 6797 | Ta113 | 35,479 | 35,479 |
| Ta34 | 3116 | 3116 | Ta74 | 7039 | 7039 | Ta114 | 35,030 | 35,124 |
| Ta35 | 3139 | 3139 | Ta75 | 6733 | 6736 | Ta115 | 35,487 | 35,487 |
| Ta36 | 3158 | 3162 | Ta76 | 6537 | 6537 | Ta116 | 35,803 | 35,803 |
| Ta37 | 3005 | 3008 | Ta77 | 6707 | 6707 | Ta117 | 35,451 | 35,451 |
| Ta38 | 3042 | 3044 | Ta78 | 6746 | 6746 | Ta118 | 35,644 | 35,644 |
| Ta39 | 2889 | 2889 | Ta79 | 6928 | 6935 | Ta119 | 35,421 | 35,421 |
| Ta40 | 3097 | 3097 | Ta80 | 6844 | 6851 | Ta120 | 35,761 | 35,773 |

would be meaningful to design a probability model combined with reinforcement learning mechanism to further enhance the guidance ability of global search and the in-depth exploitation ability of local search. Secondly, the proposed MCEDA can be extended to address other important scheduling problems, such as the low-carbon production and transportation integrated scheduling problems.

## CRediT authorship contribution statement

Zi-Qi Zhang: Investigation, Methodology, Software, Writing - original draft. Bin Qian: Methodology, Funding acquisition, Supervision, Writing - review \& editing. Rong Hu: Methodology, Funding acquisition, Investigation, Writing - review \& editing. Huai-Ping Jin: . Ling Wang: Supervision, Project administration. Jian-Bo Yang: Supervision.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This research is partially supported by the Basic Research Key Project of Yunnan Province (202201AS070030), and the National Natural Science Foundation of China (62173169, 61963022, 61873328).

## References

Ding, J. Y., Song, S. J., Gupta, J. N. D., Wang, C., Zhang, R., \& Wu, C. (2016). New block properties for flowshop scheduling with blocking and their application in an iterated greedy algorithm. International Journal of Production Research, 54, 4759-4772.
Elmi, A., \& Topaloglu, S. (2013). A scheduling problem in blocking hybrid flow shop robotic cells with multiple robots. Computers \& Operations Research, 40, 2543-2555.
Faraji Amiri, M., \& Behnamian, J. (2020). Multi-objective green flowshop scheduling problem under uncertainty: Estimation of distribution algorithm. Journal of Cleaner Production, 251, Article 119734.
Fernandez-Viagas, V., Leisten, R., \& Framinan, J. M. (2016). A computational evaluation of constructive and improvement heuristics for the blocking flow shop to minimise total flowtime. Expert Systems with Applications, 61, 290-301.
Gajpal, Y., Rajendran, C., \& Ziegler, H. (2006). An ant colony algorithm for scheduling in flowshops with sequence-dependent setup times of jobs. International Journal of Advanced Manufacturing Technology, 30, 416-424.
Gong, D. W., Han, Y. Y., \& Sun, J. Y. (2018). A novel hybrid multi-objective artificial bee colony algorithm for blocking lot-streaming flow shop scheduling problems. Knowledge-Based Systems, 148, 115-130.
Gong, H., Tang, L. X., \& Duan, C. W. (2010). A two-stage flow shop scheduling problem on a batching machine and a discrete machine with blocking and shared setup times. Computers \& Operations Research, 37, 960-969.
Grabowski, J., \& Pompeza, J. (2007). The permutation flow shop problem with blocking. A tabo search approach. Omega-International Journal of Management Science, 35, $302-311$.
Graham, R. L., Lawler, E. L., Lenzra, J. K., \& Kan, A. H. G. R. (1979). Optimization and Approximation in Deterministic Sequencing and Scheduling: A Survey. Annals of Discrete Mathematics, 5, 287-326.
Hall, N. G., \& Srishandarajah, C. (1996). A Survey of Machine Scheduling Problems with Blocking and No-Wait in Process. Operations Research, 44, 510-525.
Han, Y., Gong, D., Jin, Y., \& Pan, Q. (2019). Evolutionary Multiobjective Blocking LotStreaming Flow Shop Scheduling With Machine Breakdowns. IEEE Trans Cybern, 49, 184-197.
Han, Y. Y., Gong, D. W., Li, J. Q., \& Zhang, Y. (2016). Solving the blocking flow shop scheduling problem with makespan using a modified fruit fly optimisation algorithm. International Journal of Production Research, 54, 6782-6797.

Han, Y. Y., Gong, D. W., \& Sun, X. Y. (2015). A discrete artificial bee colony algorithm incorporating differential evolution for the flow-shop scheduling problem with blocking. Engineering Optimization, 47, 927-946.
Han, Y. Y., Li, J. Q., Sang, H. Y., Liu, Y. P., Gao, K. Z., \& Pan, Q. K. (2020). Discrete evolutionary multi-objective optimization for energy-efficient blocking flow shop scheduling with setup time. Applied Soft Computing, 93, Article 106343.
Jarboui, B., Eddaly, M., \& Siarry, P. (2009). An estimation of distribution algorithm for minimizing the total flowtime in permutation flowshop scheduling problems. Computers \& Operations Research, 36, 2638-2646.
Khorasanian, D., \& Moslehi, G. (2012). An Iterated Greedy Algorithm for Solving the Blocking Flow Shop Scheduling Problem with Total Flow Time Criteria. International Journal of Industrial Engineering, 23, 301-308.
Koren, Y., Wang, W. C., \& Gu, X. (2017). Value creation through design for scalability of reconfigurable manufacturing systems. International Journal of Production Research, 55, 1227-1242
Larrange, P., \& Lozano, J. A. (2001). Estimation of Distribution Algorithms: A New Tool for Evolutionary Computation. US: Springer.
Li, X. P., \& Zhang, Y. (2012). Adaptive Hybrid Algorithms for the Sequence-Dependent Setup Time Permutation Flow Shop Scheduling Problem. Ieee Transactions on Automation Science and Engineering, 9, 578-595.
Lin, S. W., \& Ying, K. C. (2013). Minimizing makespan in a blocking flowshop using a revised artificial immune system algorithm. Omega-International Journal of Management Science, 41, 383-389.
Lourenço, H. R., Martin, O. C., \& Stützte, T. (2010). Iterated Local Search: Framework and Applications. Handbook of Mendeurs, 146, 363-397.
McCormick, S. T., Pinedo, M. L., Shenker, S., \& Wolf, B. (1989). Sequencing in an Assembly Line with Blocking to Minimize Cycle Time. Operations Research, 37, 925-935.
Miyata, H. H., \& Nagano, M. S. (2019). The blocking flow shop scheduling problem: A comprehensive and conceptual review. Expert Systems with Applications, 137, 130-156.
Montgomery, D. C. (2008). Design and Analysis of Experiments. John Wiley \& Sons.
Moslehi, G., \& Khorasanian, D. (2014). A hybrid variable neighborhood search algorithm for solving the limited-buffer permutation flow shop scheduling problem with the makespan criterion. Computers \& Operations Research, 52, 260-268.
Nagano, M. S., Komesu, A. S., \& Miyata, H. H. (2017). An evolutionary clustering search for the total tardiness blocking flow shop problem. Journal of Intelligent Manufacturing, 30, 1843-1857.
Nawaz, M., Estocov, E. E., \& Ham, I. (1983). A heuristic algorithm for the m-machine, n-job flow-shop sequencing problem. Omega, 11, 91-95.
Noori, N., \& Ladhari, T. (2018). Evolutionary multidisciplinary optimization for the multimachine flow shop scheduling problem under blocking. Annals of Operations Research, 267, 413-430.
Pan, Q.-K., \& Wang, L. (2012). Effective heuristics for the blocking flowshop scheduling problem with makespan minimization. Omega, 40, 218-229.
Pan, Q. K., Ling, W., Hong-yan, S., Jun-qing, L., \& Min, L. (2013). A High Performing Memeitic Algorithm for the Flowshop Scheduling Problem With Blocking. Ieee Transactions on Automation Science and Engineering, 10, 741-756.
Pan, Q. K., \& Ruiz, R. (2012). An estimation of distribution algorithm for lot-streaming flow shop problems with setup times. Omega-International Journal of Management Science, 40, 166-180.
Pinedo, M. (2015). Scheduling: Theory, Algorithms, and Systems (fourth ed.). Springer Verlag.
Qian, B., Li, Z. C., \& Hu, R. (2017). A copula-based hybrid estimation of distribution algorithm for m-machine reentrant permutation flow-shop scheduling problem. Applied Soft Computing, 61, 921-934.
Rajendran, C., \& Ziegler, H. (1997). An efficient heuristic for scheduling in a flowshop to minimize total weighted flowtime of jobs. European Journal of Operational Research, 103, 129-138.
Riahi, V., Khorramizadeh, M., Newton, M. A. H., \& Sattar, A. (2017). Scatter search for mixed blocking flowshop scheduling. Expert Systems with Applications, 79, 20-32.
Ribas, I., Companys, R., \& Martorell, X. T. (2013). A competitive variable neighbourhood search algorithm for the blocking flow shop problem. European J. of Industrial Engineering, 7, 729-754.
Ribas, I., Companys, R., \& Tort-Martorell, X. (2011). An iterated greedy algorithm for the flowshop scheduling problem with blocking. Omega-International Journal of Management Science, 39, 293-301.
Ribas, I., Companys, R., \& Tort-Martorell, X. (2015). An efficient Discrete Artificial Bee Colony algorithm for the blocking flow shop problem with total flowtime minimization. Expert Systems with Applications, 42, 6155-6167.
Ribas, I., Companys, R., \& Tort-Martorell, X. (2021). An iterated greedy algorithm for the parallel blocking flow shop scheduling problem and sequence-dependent setup times. Expert Systems with Applications, 184, Article 115535.

Ronconi, D. P. (2004). A note on constructive heuristics for the flowshop problem with blocking. International Journal of Production Economics, 87, 39-48.
Ronconi, D. P., \& Henriques, L. R. S. (2009). Some heuristic algorithms for total tardiness minimization in a flowshop with blocking. Omega-International Journal of Management Science, 37, 272-281.
Ruiz, R., Maroto, C., \& Alcaraz, J. (2005). Solving the flowshop scheduling problem with sequence dependent setup times using advanced metaheuristics - Discrete optimization. European Journal of Operational Research, 165, 34-54.
Ruiz, R., \& Stutzle, T. (2008). An Iterated Greedy heuristic for the sequence dependent setup times flowshop problem with makespan and weighted tardiness objectives. European Journal of Operational Research, 187, 1143-1159.
Schievinotto, T., \& Stutzle, T. (2007). A review of metrics on permutations for search landscape analysis. Computers \& Operations Research, 34, 3143-3153.
Shao, Z., Pi, D., Shao, W., \& Yuan, P. (2019). An efficient discrete invasive weed optimization for blocking flow-shop scheduling problem. Engineering Applications of Artificial Intelligence, 78, 124-141.
Shao, Z., Shao, W., \& Pi, D. (2021). Effective constructive heuristic and iterated greedy algorithm for distributed mixed blocking permutation flow-shop scheduling problem. Knowledge-Based Systems, 221, Article 106959.
Shao, Z. S., Pi, D. C., \& Shao, W. S. (2017). Self-adaptive discrete invasive weed optimization for the blocking flow-shop scheduling problem to minimize total tardiness. Computers \& Industrial Engineering, 111, 331-351.
Shao, Z. S., Pi, D. C., \& Shao, W. S. (2018a). Estimation of distribution algorithm with path relinking for the blocking flow-shop scheduling problem. Engineering Optimization, 30, 894-916.
Shao, Z. S., Pi, D. C., \& Shao, W. S. (2018b). A novel discrete water wave optimization algorithm for blocking flow-shop scheduling problem with sequence-dependent setup times. Swarm and Evolutionary Computation, 40, 53-75.
Siosul, A., \& Gagne, C. (2018). Enhanced migrating birds optimization algorithm for the permutation flow shop problem with sequence dependent setup times. European Journal of Operational Research, 264, 66-73.
Tangetiren, M., Pan, Q. K., Kizilay, D., \& Gao, K. Z. (2016). A Variable Block Insertion Heuristic for the Blocking Flowshop Scheduling Problem with Total Flowtime Criterion. Algorithms, 9, 71-95.
Tangetiren, M. F., Kizilay, D., Pan, Q. K., \& Suganthan, P. N. (2017). Iterated greedy algorithms for the blocking flowshop scheduling problem with makespan criterion. Computers \& Operations Research, 77, 111-126.
Tangetiren, M. F., Pan, Q., Kizilay, D., \& Suer, G. (2015). A populated local search with differential evolution for blocking flowshop scheduling problem. In In 2015 IEEE Congress on Evolutionary Computation (CEC) (pp. 2789-2796).
Wang, C., Song, S. J., Gupta, J. N. D., \& Wu, C. (2012). A three-phase algorithm for flowshop scheduling with blocking to minimize makespan. Computers \& Operations Research, 39, 2880-2887.
Wang, L., Fang, C., Suganthan, P. N., \& Liu, M. (2014). Solving system-level synthesis problem by a multi-objective estimation of distribution algorithm. Expert Systems with Applications, 41, 2496-2513.
Wang, L., Pan, Q. K., Suganthan, P. N., Wang, W. H., \& Wang, Y. M. (2010). A novel hybrid discrete differential evolution algorithm for blocking flow shop scheduling problems. Computers \& Operations Research, 37, 509-520.
Wang, L., Pan, Q. K., \& Tangentien, M. F. (2011). A hybrid harmony search algorithm for the blocking permutation flow shop scheduling problem. Computers \& Industrial Engineering, 61, 76-83.
Wang, S. Y., \& Wang, L. (2016). An Estimation of Distribution Algorithm-Based Memetic Algorithm for the Distributed Assembly Permutation Flow-Shop Scheduling Problem. Ieee Transactions on Systems Man Cybernetics-Systems, 46, 139-149.
Wang, S. Y., Wang, L., Liu, M., \& Xu, Y. (2013). An effective estimation of distribution algorithm for solving the distributed permutation flow-shop scheduling problem. International Journal of Production Economics, 145, 387-396.
Wu, C.-G., Wang, L., \& Wang, J.-J. (2021). A path relinking enhanced estimation of distribution algorithm for direct acyclic graph task scheduling problem. KnowledgeBased Systems, 228, Article 105235.
Zhang, Z.-Q., Qian, B., Hu, R., Jin, H.-P., \& Wang, L. (2021). A matrix-cubebased estimation of distribution algorithm for the distributed assembly permutation flowshop scheduling problem. Swarm and Evolutionary Computation, 60, Article 100785.
Zhang, Z. Q., Hu, R., Qian, B., Jin, H. P., Wang, L., \& Yang, J. B. (2022). A matrix cubebased estimation of distribution algorithm for the energy-efficient distributed assembly permutation flow-shop scheduling problem. Expert Systems with Applications, 194, Article 116484.
Zhao, F., Shao, D., Wang, L., Xu, T., Zhu, N., \& Amrisialdi, (2022). An effective water wave optimization algorithm with problem-specific knowledge for the distributed assembly blocking flow-shop scheduling problem. Knowledge-Based Systems, 243, Article 108471.