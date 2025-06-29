# A matrix-cube-based estimation of distribution algorithm for the distributed assembly permutation flow-shop scheduling problem 

Zi-Qi Zhang ${ }^{\mathrm{a}, \mathrm{b}}$, Bin Qian ${ }^{\mathrm{a}, \mathrm{b}, \mathrm{c}, \mathrm{c}}$, Rong $\mathrm{Hu}^{\mathrm{a}, \mathrm{c}}$, Huai-Ping Jin ${ }^{\mathrm{a}}$, Ling Wang ${ }^{\mathrm{d}}$<br>*School of Information Engineering and Automation, Kunming University of Science and Technology, Kunming 650500, China<br>${ }^{\mathrm{b}}$ School of Mechanical and Electrical Engineering, Kunming University of Science and Technology, Kunming 650500, China<br>${ }^{\mathrm{c}}$ Yunnan Key Laboratory of Artificial Intelligence, Kunming University of Science and Technology, Kunming 650500, China<br>${ }^{\mathrm{d}}$ Department of Automation, Tsinghua University, Beijing 100084, China

## A R T I C L E I N F O

Keywords:
Scheduling
Matrix cube
Estimation of distribution algorithm
Distributed assembly permutation flow shop
Variable neighborhood descent

## A B STR A C T

The distributed assembly permutation flow-shop scheduling problem (DAPFSP) is a typical NP-hard combinatorial optimization problem that has wide applications in advanced manufacturing systems and modern supply chains. In this work, an innovative three-dimensional matrix-cube-based estimation of distribution algorithm (MCEDA) is first proposed for the DAPFSP to minimize the maximum completion time. Firstly, a matrix cube is designed to learn the valuable information from elites. Secondly, a matrix-cube-based probabilistic model with an effective sampling mechanism is developed to estimate the probability distribution of superior solutions and to perform the global exploration for finding promising regions. Thirdly, a problem-dependent variable neighborhood descent method is proposed to perform the local exploitation around these promising regions, and several speedup strategies for evaluating neighboring solutions are utilized to enhance the computational efficiency. Furthermore, the influence of the parameters setting is analyzed by using design-of-experiment technique, and the suitable parameters are suggested for different scale problems. Finally, a comprehensive computational campaign against the state-of-the-art algorithms in the literature, together with statistical analyses, demonstrates that the proposed MCEDA produces better results than the existing algorithms by a significant margin. Moreover, the new best-known solutions for 214 instances are improved.

## 1. Introduction

The permutation flow-shop scheduling problem (PFSP) is one of the most extensively investigated combination optimization problems and widely exists in machinery factories, assembly lines, information service facilities, and petrochemical systems [1-4]. According to the research work of Garey et al. [5] and Gonzalez and Sahni [6], the PFSP is NP-hard in the strong sense. Due to its significance in both theory and practice, the PFSP has been studied by many researchers. The traditional PFSP assumes that all jobs have to be scheduled in a single factory. However, with the deepening of the global economy, many factories are now more actively involved in international and regional cooperation. As a consequence, the production scheduling in multi-factory mode, referred to as the distributed scheduling problem. Among all types of distributed scheduling problems, the distributed PFSP (DPFSP) is a generalization of the traditional PFSP. The DPFSP addressing both the allocation of jobs among factories and the scheduling of jobs in each factory has gained an increasing attention in the literature. Naderi and Ruiz [7] first introduced the DPFSP and presented six mixed integer linear program-
ming (MILP) models for it. They also proposed 14 constructive heuristics and fast local search methods based on variable neighborhood descent (VND) to minimize the makespan of the problem. Afterward, some researchers proposed different algorithms for the DPFSP. These algorithms include one tabu search [8], three estimation of distribution algorithm [9-11], and three iterated greedy (IG) algorithms [12-14]. As for the multi-objective DPFSP, an adaptive large neighborhood search algorithm [15] and a competitive memetic algorithm [16] were developed.

In the past few decades, assembly systems have been widely applied in the flow-oriented manufacturing industry. The distributed assembly permutation flow-shop scheduling problem (DAPFSP) is a classical model where the components of a product are produced independently on flow-shop-type processing lines in the first stage and then all these components are assembled on one assembly machine in the second stage. In real world, many scheduling problems in multi-factory manufacturing companies can be modeled as DAPFSP. Typical examples can be found in automotive engine companies, personal computer manufacturing companies, and smartphone manufacturing companies. Since

[^0]
[^0]:    ${ }^{\text {a }}$ Corresponding authors.
    E-mail address: bin.qian@vip.163.com (B. Qian).

the PFSP is already strongly NP-hard and it reduces to the DAPFSP, the latter problem is also NP-hard.

Nowadays, the DAPFSP has received increasing attention from researchers due to its practical application and theoretical complexity. Since 2013, three types of the DAPFSP have been proposed in the literature. The first is the DAPFSP with makespan criterion. The existing research mainly focused on this problem. Hatami et al. [17] first considered this problem and generated 900 small-scaled instances and 810 large-scaled instances to evaluate the compared algorithms. They proposed three constructive algorithms and a fast variable neighborhood descent (VND) algorithm for solving it. Computational results indicated that the VND algorithm is quite effective and can offer good performance. Li et al. [18] developed a genetic algorithm (GA) by adopting an enhanced crossover operator and three local search strategies. Test results showed that the proposed GA can obtain good performance. Wang and Wang [19] presented an estimation of distribution algorithm-based memetic algorithm (EDAMA), which used a two-dimensional probabilistic model to guide exploration and designed a critical-path-based local search to perform exploitation. Experimental results demonstrated that EDAMA can update the best-known solutions of 181 instances. Lin and Zhang [20] designed a hybrid biogeography-based optimization (HBBO) algorithm that integrated the path-relinking based heuristic, the insertion-based heuristic, and the problem-based local search. Computational results showed that HBBO can find the best-known solutions of 181 instances. Lin et al. [21] presented a backtracking search hyperheuristic (BS-HH) algorithm where the backtracking search algorithm was employed as the high-level heuristic strategy to manipulate a set of low-level heuristics (LLHs) to search solution space. Computational results indicated that the presented BS-HH can achieve better performance than the state-of-the-art algorithms. In addition, Hatami et al. [22] further generalized the first type of problem by adding sequencedependent setup times and presented two constructive heuristics and two meta-heuristics (i.e., VND and IG) for solving it. Test results showed that $\mathrm{IG}_{2}$ (one variant of IG) has better performance. Most recently, Pan et al. [23] considered an extended DAPFSP, in which each factory has its own assembly machine. They proposed three constructive heuristics, two variable neighborhood search methods, and an iterated greedy algorithm (IGA). Computational comparisons demonstrated that their proposed IGA outperforms the existing algorithms by a significant margin. The second is the DAPFSP with the total flowtime criterion. Sang et al. [24] presented a two-level discrete invasive weed optimization (TDIWO), a discrete invasive weed optimization with hybrid search operators (HDIWO), and a HDIWO with selection probability (HDIWOp) for this problem. Test results verified that the presented algorithms perform better than the other algorithms in the literature and HDIWO is the best one. The third is the DAPFSP with the total tardiness criterion. Yang et al. [25] proposed a scatter-search-based memetic algorithm (SS-MA), in which a subset generation mechanism and a solution combination method were designed to execute global search, and an enhanced scatter search was devised to perform local search. Experimental results showed that the proposed SS-MA outperforms several NEH-based heuristics. In the tests of the above algorithms, GA, EDAMA, HBBO, BS-HH and SSMA used both the small-scaled and the large-scaled instances generated by Hatami et al. [17], IGA, TDIWO, HDIWO and HDIWOp only used these large-scaled instances, and the other algorithms used their own randomly generated instances. From the above literature review, it is clear that the DAPFSP with makespan criterion has been becoming a research hotspot in recent years. Thus, it is meaningful to design a new algorithm that can solve this problem more effectively.

Traditional mathematical algorithms use linear algebra and geometric analysis as basic tools. They try to utilize the structural information of the objective function and constraints of mixed integer programming model to narrow the search area, and execute the search that traverses or partially traverses solution space [26]. When the problem is NP-hard, the relationship between its inner geometric structure and the optimal solution is still an open problem [27,28]. As a consequence,
for large-scaled or complex scheduling problems, mathematical algorithms are often of limited use due to their excessive computation time or poor results under reasonable computation time. To settle this issue, meta-heuristic algorithms based on permutation-based model have been presented. They do not depend on the structure of the model, but perform the search by using certain evolutionary mechanisms. This kind of algorithms can often obtain satisfactory solutions of various complex scheduling problems within seconds or tens of seconds. This is why almost all existing algorithms for solving the DAPFSP are meta-heuristic algorithms (see the pervious paragraph). So, it is necessary to design a meta-heuristic algorithm to deal with the DAPFSP.

As a novel meta-heuristic algorithm based on statistical learning technique, the estimation of distribution algorithm (EDA) establishes a probabilistic model to estimate the distribution of the promising or excellent solutions and generates new individuals through sampling from this model. Unlike the traditional evolutionary algorithms, the evolutionary mechanism of EDA can avoid the destruction of the blocks (i.e., the partial ordered patterns) in promising solutions [29]. Due to its outstanding global exploration, inherent parallelism and fast convergence, EDA has led to increasing studies and extensive applications during recent years [30]. In the field of intelligent production scheduling, EDA-based algorithms have been designed to address a variety of shop scheduling problems, such as the hybrid FSP [31], the PFSP [32], the lot-streaming FSP [33], the flexible job-shop scheduling problem (FJSP) [34], the DPFSP [9], the multi-objective PFSP [35], and the DAPFSP [19]. Hence, in this study, we select EDA as the basic framework to construct an effective algorithm for the DAPFSP.

The above currently existing EDA-based algorithms always tried to use a two-dimensional model to save the information of the blocks and the order of jobs from each promising solution or individual. Here one block consists of any two consecutive jobs in a solution. Nevertheless, owing to the limit of its own structure, a two-dimensional model cannot accurately record the position information of each block and the whole order information of jobs, which causes that the sampling procedure may misplace the blocks in new individuals. As a result, the search direction cannot be reasonably guided. To overcome the drawback of the existing two-dimensional models and solve the DAPFSP with makespan criterion more effectively, we develop a matrix-cube-based EDA (MCEDA) in this paper. The main features of MCEDA lie in two aspects: the global search based on the three-dimensional probabilistic model and the local search boosted by the speed-up strategies. As for the global search, a three-dimensional probabilistic model is built to save the valuable information of excellent individuals, and the new individuals are generated by sampling this model via a special sampling method. As for the local search, a VND framework coupled with rich neighborhood operators is constructed to execute exploitation, and two speed-up strategies based on the problem's property are utilized to boost search efficiency.

The remainder of this paper is organized as follows. The DAPFSP is described in the next section. The proposed MCEDA is elaborated in Section 3. Numerical results and comparisons are analyzed in Section 4. Finally, some concluding remarks and future research directions are provided in Section 5.

## 2. Problem description

As illustrated in Fig. 1, the considered DAPFSP contains two stages, i.e., a production stage and an assembly stage. The production stage consists of a series of production factories, and each of them can be regarded as a flowshop configuration. All operations of jobs are performed by the same route in any of the assigned factories. The assembly stage can be executed after all parts of each product have been finished and the single assembly machine is free.

The DAPFSP can be described as follows. There is a set of $S$ products $\left(P_{1}, P_{2}, \ldots, P_{S}\right)$ and each product is produced by assembling a set of its parts in terms of bill of material. The production stage consists of

![img-0.jpeg](img-0.jpeg)

Fig. 1. Illustration of the distributed assembly flowshop.

Table 1
Notations applied in the model of DAPFSP.

a set $F$ of $f$ distributed factories that are responsible for processing the set of $n$ jobs on the set of $m$ machines and each factory has the same capacity for production. Each of these factories is regarded as the flowshop with a series of machines $M=\left\{M_{1}, M_{2}, \ldots, M_{m}\right\}\left(\left|M_{k}\right| \geq 2\right.$ for all factories and $|\cdot|$ is the cardinality of a set). All jobs must be assigned to any of the factories and processed in the same route, i.e., first on machine $M_{1}$, then on machine $M_{2}$, and so on until machine $M_{m}$. A series of operations $\left\{O_{i, 1}, O_{i, 2}, \ldots, O_{i, m}\right\}$ of job $i$ are executed one after another and $O_{i, j}$ is performed on machine $M_{j}$ during a period of processing time $p_{m}(i, j)$ without interruption. All operations of each job must be completed in the assigned factory which cannot be transferred to another factory. Each product $P_{h}$ consists of $\omega_{h}$ jobs and each job only belongs to one product, i.e., $\sum_{i=1}^{k} \omega_{h}=n$. Once all parts of product $P_{h}$ are finished, they are immediately delivered to an assembly machine $M_{n}$. At the assembly stage, all jobs are assembled to obtain a set of final products by a defined program. The assembly time that a product $P_{h}$ requires to be assembled in $M_{A}$ is referred to as $p_{n}(h)$ and the assembly operation of $P_{h}$ cannot be started until its all parts have arrived and the assembly machine has released. For the convenience and readability, the detailed notation description including indices, parameters and variables are shown in Table 1. Additionally, a number of additional assumptions of PFSP are also met. Machines are always available and no breakdowns are considered and all the jobs are independent and available at time 0 .

The processing times are deterministic and the setup times and transportation times are considered to be included in processing times. At any time, each machine is capable of processing no more than one job and each job can only be processed on at most one machine and preemption is forbidden, i.e., each job should be processed sequentially on all machines as no intermingling is allowed. The goal of the DAPFSP is to determine the assignment of jobs to factories, the sequence of jobs in factories and the order of products in the assembly stage so that the maximum completion time (i.e., makespan) of the entire manufacturing process is minimized.

At the production stage, all $n$ jobs assigned to $F$ different factories can be represented as a set of subsequences $\left\{\boldsymbol{x}_{1}, \boldsymbol{x}_{2}, \ldots, \boldsymbol{x}_{\boldsymbol{F}}\right\}$ where $\boldsymbol{x}_{i}=\left\{\pi_{f}(1), \pi_{f}(2), \ldots, \pi_{f}\left(n_{f}\right)\right\}$ is the sequence of jobs in factory $f$ and $\sum_{f=1}^{F} n_{f}=n$. For a schedule $\boldsymbol{x}$ of the DAPFSP, the makespan $C_{\max }(\boldsymbol{x})$ can be calculated as follows:

$$
\begin{aligned}
C\left(\pi_{f}(1), 1\right) & =p_{m}\left(\pi_{f}(1), 1\right), f=1,2, \ldots, F \\
C\left(\pi_{f}(i), 1\right) & =C\left(\pi_{f}(i-1), 1\right)+p_{m}\left(\pi_{f}(i), 1\right) \\
i & =2,3, \ldots, n_{f}, f=1,2, \ldots, F \\
C\left(\pi_{f}(1), j\right) & =C\left(\pi_{f}(1), j-1\right)+p_{m}\left(\pi_{f}(1), j\right) \\
j & =2,3, \ldots, m, f=1,2, \ldots, F
\end{aligned}
$$

Table 2
Processing times, assembly times and job-ownership constraints of the given instance.

$$
\begin{aligned}
C\left\{\pi_{f}(i), j\right\} & =\max \left\{C\left\{\pi_{f}(i-1), j\right\}, C\left\{\pi_{f}(i), j-1\right\}\right\}+p_{m}\left\{\pi_{f}(i), j\right\} \\
i & =2,3, \ldots, n_{f}, j=2,3, \ldots, m, f=1,2, \ldots, F
\end{aligned}
$$

At the assembly stage, all jobs are assembled to produce a set of $S$ final products. The product sequence $\lambda=[\lambda(1), \lambda(2), \ldots, \lambda(S)]$ on the assembly machine can be determined according to the completion times of all jobs in the first stage, and then
$C_{P}(h)=\max _{\pi_{f}(i) \in \lambda(h)} C\left\{\pi_{f}(i), m\right\}, i=1,2, \ldots, n_{f}, f=1,2, \ldots, F$
$C_{A}(1)=C_{P}(1)+p_{n}(1)$
$C_{A}(h)=\max \left\{C_{A}(h-1), C_{P}(h)\right\}+p_{n}(h), h=2,3, \ldots, S$.
Hence, the makespan of $\boldsymbol{x}$ is determined as
$C_{\max }(\boldsymbol{x})=C_{A}(S)$
The aim of solving the DAPFSP with makespan criterion is to find a schedule $\boldsymbol{x}^{*}$ in the set of all permutations $\Pi$, such that
$C_{\max }\left(\boldsymbol{x}^{*}\right)=\min _{\boldsymbol{x} \in \Pi} C_{\max }(\boldsymbol{x})$.
Obviously, the model adopted in this section is a permutation-based model, which consists of several equations to calculate the complete time of each job or product on each machine. The optimization variables of this model are represented as a job sequence $\boldsymbol{x}$. Some existing studies on the meta-heuristics for the assembly flow-shop scheduling problems always establish the mixed-integer mathematical models. However, each individual or solution in these meta-heuristics actually corresponds to the decision variables of the unprovided permutationbased model. Many beginning researchers are easily confused by this phenomenon. Thus, this section only adopts a permutation-based model. If researchers are interested in the mathematical models of the DAPFSP, they can find them in [7].

The permutation-based models of production scheduling problems have no explicitly expressed constraints, which is different from the mathematical models of these problems. The operational constraints of DAPFSP's permutation-based model are implicitly included in its equations and a job-ownership table. There are two types of these constraints. The first type includes the general constraints for both the PFSP and the DPFSP. These general constraints are included in Eqs. (2)-(4), which require that each operation $O_{\pi_{f}(i), j}$ can only be performed after the operations $O_{\pi_{f}(i-1), j}$ and $O_{\pi_{f}(i), j-1}$ are completed. The second type includes the special job-ownership constraints for the DAPFSP. These special constraints are usually given in a job-ownership table (see Table 2), which determines the relations among jobs and products.

The constraints of the permutation-based model are easier to handle than those of the mathematical model. By using a job assignment rule, a solution or sequence $\boldsymbol{x}$ that contains different jobs can be decoded
to a series of subsequences, each of which belongs to a corresponding factory. Then, the processing start times of the jobs on each machine of a factory are calculated through Eqs. (1)-(5), and no general constraints are violated. Moreover, since Eq. (5) utilizes the job-ownership constraints (see $\pi_{f}(i) \in \lambda(h)$ ) to calculate $C_{P}(h)$, no special constraints are violated. Hence, a solution $\boldsymbol{x}$ is feasible if and only if all the jobs in this solution are different from each other. In MCEDA, both the sampling method for generating new individuals (see Section 3.2.3) and the neighborhood searches for reaching new neighbors (see Section 3.3) can ensure that the jobs in each solution $\boldsymbol{x}$ (i.e., individual or neighbor) are different from each other. This means that any solution $\boldsymbol{x}$ obtained in MCEDA is feasible. From these analyses, it can be seen that by using the permutation-based model, researchers can focus more on algorithm design without spending too much time dealing with complex constraints. Therefore, most of the existing meta-heuristics choose to optimize the variables of the permutation-based model.

## 3. MCEDA for DAPFSP

### 3.1. Solution representation

The permutation-based representation has been widely used in the literature [7,19,33,23,36,37]. Therefore, regarding the DAPFSP with $n$ jobs and $F$ factories, a feasible solution is represented by a total job permutation or sequence $\boldsymbol{x}=[\pi(1), \pi(2), \ldots, \pi(n)]$ where the element $\pi(i)$ $(i=1, \ldots, n)$ implies one job with the $i$ th processing priority. The job assignment rule proposed by Hatami et al. [17] is adopted to convert $\boldsymbol{x}$ into a feasible scheduling scheme. This rule continually selects each job $\pi(i)$ in $\boldsymbol{x}$ according to its priority from high to low and assigns it to a factory which has the lowest makespan after including this job. Then, a set of subsequences $\left\{\boldsymbol{x}_{1}, \boldsymbol{x}_{2}, \ldots, \boldsymbol{x}_{\boldsymbol{F}}\right\}$ in $F$ factories are obtained and the makespan $C_{\max }(\boldsymbol{x})$ can be calculated by using Eqs. (1)-(9) and a preset $\lambda$ in Section 2.

To facilitate understanding, Fig. 2 illustrates the Gantt chart of a high-quality schedule for the instance 1,24,5,3,2,2 generated by Hatami et al. [17], where 24,5,3,2 represents the instance scale ( $n=24, m=5, F=3, S=2$ ) and the last number 2 means that this instance is the second one of this scale. The relations among jobs and products, the processing times of jobs and the assembly times of products are provided in Table 2. As shown in Fig. 2, it is obvious that the product sequence is $\lambda=[1,2]$ and the subsequences of jobs assigned into three factories are $\boldsymbol{x}_{1}=[3,18,17,16,23,12,9], \boldsymbol{x}_{2}=[4,11,2,15,20,5,21,6]$, and $\boldsymbol{x}_{3}=[1,14,22,10,24,19,8,7,13]$, respectively. Moreover, it is clear from Fig. 2 that all jobs belonging to the same product are tied closely at the production stage and the assembly operation of the first product should be performed as early as possible if a smaller $C_{\max }(\boldsymbol{x})$ is expected. Thus, when decoding a solution of the proposed MCEDA, the products in $\lambda$ are sorted in ascending order of their respective $C_{P}\left(P_{h}\right)$.

![img-1.jpeg](img-1.jpeg)

Fig. 2. A scheduling Gantt chart of instance 1,24,5,3,2,2. (Makespan:1479).

# 3.2. Matrix-cube-based global search 

A matrix-cube-based global search is proposed to find promising regions in solution space. In this section, a matrix-cube-based probabilistic model is developed to explicitly extract the distributing characteristic of the similar blocks and accurately accumulate the valuable information of superior solutions or individuals. It is expected to potentially guide the evolutionary direction toward promising regions in solution space. Then, the matrix-cube-based probabilistic model and the new population generation method are devised.

### 3.2.1. Matrix cube

In this subsection, we first introduce an effective data structure which is referred to as matrix cube. Then, the three-dimensional matrix cube is devised to reasonably reserve the valuable information of the order of jobs and the position of similar blocks of excellent individuals, which is essential for developing a probabilistic model. Let Pop(gen) be the population of MCEDA at genth $(g e n=0, \ldots, \max g e n)$ generation, popsize the size of $\operatorname{Pop}(\mathbf{g e n})$, $\operatorname{SbestPop}(\mathbf{g e n})=\left\{\pi_{\text {Sbest }}^{\text {gen }, k}, \pi_{\text {Sbest }}^{\text {gen }, 2}, \pi_{\text {Sbest }}^{\text {gen-spsize }}\right\}$ the superior sub-population or excellent solutions selected from Pop(gen), spsize the size of SbestPop(gen), and $\pi_{\text {Sbest }}^{\text {gen }, k}=\left\{\pi_{S h e n k}^{\text {gen }, k},(1, \pi_{S h e n k}^{\text {gen }, k}(2), \ldots, \pi_{S h e n k}^{\text {gen }, k}(n)\right\}(k=1, \ldots$, spsize $)$ the $k$ th individual in the $\operatorname{SbestPop}(\mathbf{g e n})$. Then, the details of the presented three-dimensional matrix or matrix cube $\mathbf{M C}_{\text {ncdecm }}^{\text {gen }}$ are given as follows:

$$
\begin{aligned}
N_{c, c} M C_{\text {ncdecm }}^{\text {gen }, k}(x, y, z) & =\left\{\begin{array}{l}
1, \text { if } y=\pi_{\text {Sbest }}^{\text {gen }, k}(x) \text { and } z=\pi_{\text {Sbest }}^{\text {gen }, k}(x+1) \\
0, \text { else }
\end{array}\right. \\
x & =1, \ldots, n-1 ; y, z=1, \ldots, n ; k=1, \ldots, \text { spsize } \\
M C_{\text {ncdecm }}^{\text {gen }}(x, y, z) & =\sum_{k=1}^{\text {spsize }} N_{c, c} M C_{\text {ncdecm }}^{\text {gen }, k}(x, y, z), \\
x & =1, \ldots, n-1 ; y, z=1, \ldots, n
\end{aligned}
$$

$\mathbf{M C}_{\text {ncdecm }}^{\text {gen }}(\mathbf{x})=\left[\begin{array}{c}\mathbf{M C}_{\text {ncdecm }}^{\text {gen }}(\mathbf{x}, \mathbf{1}) \\ \left.\mathbf{M C}_{\text {ncdecm }}^{\text {gen }}(\mathbf{x}, \mathbf{n})\right]_{\text {tot } 1}=\left[\begin{array}{c:c:c:c:l:l}M C_{\text {ncdecm }}^{\text {gen }}(x, 1,1) & \cdots & M C_{\text {ncdecm }}^{\text {gen }}(x, 1, n) \\ M C_{\text {ncdecm }}^{\text {gen }}(x, n, 1) & \cdots & M C_{\text {ncdecm }}^{\text {gen }}(x, n, n)\end{array}\right]_{\text {total }}$

$$
\begin{aligned}
& \mathbf{M C}_{\text {ncdecm }}^{\text {gen }}(\mathbf{y}, \mathbf{z})=\left[\begin{array}{l}
M C_{\text {ncdecm }}^{\text {gen }}(1, y, z), M C_{\text {ncdecm }}^{\text {gen }}(2, y, z), \ldots, M C_{\text {ncdecm }}^{\text {gen }}(n, y, z)
\end{array}\right]_{1 \times n} \\
& y, z=1,2, \ldots, n
\end{aligned}
$$

In Eq. (10), $N_{c, c} M C_{\text {ncdecm }}^{\text {gen }, k}(x, y, z)$ is an indicator function that records the information of the order of jobs and the position of similar blocks
for the $k$ th individual in SbestPop(gen). In Eq. (11), the element $M C_{\text {ncdecm }}^{\text {gen }}(x, y, z)$ of $\mathbf{M C}_{\text {ncdecm }}^{\text {gen }}$ can save the statistical information for all individuals in $\operatorname{SbestPop}(\mathbf{g e n})$ according to the $N_{c, c} M C_{\text {ncdecm }}^{\text {gen }, k}(x, y, z)$ $(k=1, \ldots$, spsize $)$. That is, the subscripts $x$ and $(y, x)$ of $M C_{\text {ncdecm }}^{\text {gen }}(x, y, z)$ record both the ordinal number of job (i.e., the position of $\pi_{\text {Sbest }}^{\text {gen }, k}(x)$ in $\pi_{\text {Sbest }}^{\text {gen }, k}$ ) and the occurrence frequency of the corresponding similar block (i.e., $\left.\left[\pi_{\text {Sbest }}^{\text {gen }, k}(x), \pi_{\text {Sbest }}^{\text {gen }, k}(x+1)\right]\right)$, respectively. In Eq. (12), it is clear that each two-dimensional submatrix $\mathbf{M C}_{\text {ncdecm }}^{\text {gen }}(\mathbf{x})$ can learn the ordinal numbers of jobs and the distributing information of similar blocks at $x$ th position of solutions in $\operatorname{SbestPop}(\mathbf{g e n})$. Moreover, in Eq. (13), the hierarchical structure of the proposed three-dimensional matrix cube $\mathbf{M C}_{\text {ncdecm }}^{\text {gen }}$ can reasonably reserve the total information of the order of jobs and the position of similar blocks by means of a series of the position-based two-dimensional submatrices, i.e., $\mathbf{M C}_{\text {ncdecm }}^{\text {gen }}(\mathbf{1}), \mathbf{M C}_{\text {ncdecm }}^{\text {gen }}(\mathbf{2}), \ldots, \mathbf{M C}_{\text {ncdecm }}^{\text {gen }}(\mathbf{n})$. Thus, the valuable information of the distinctive features of superior solutions at each generation can be learned and conserved in an appropriate and intuitive way. The matrix cube $\mathbf{M C}_{\text {ncdecm }}^{\text {gen }}$ is an important ingredient to construct an effective probabilistic model of the proposed MCEDA. In order to facilitate the understanding, a simple example with $n=4$ and spsize $=5$ is given as follows. In this example, five superior solutions are considered, i.e., $\pi_{\text {Sbest }}^{\text {gen }, 1}=\left[\pi_{\text {Sbest }}^{\text {gen }, 1}(1), \pi_{\text {Sbest }}^{\text {gen }, 1}(2), \pi_{\text {Sbest }}^{\text {gen }, 1}(3), \pi_{\text {Sbest }}^{\text {gen }, 1}(4)\right]=[1,2,3,4],$

$$
\begin{aligned}
& \pi_{\text {Sbest }}^{\text {gen }, 2}=\left[\pi_{\text {Sbest }}^{\text {gen }, 2}(1), \pi_{\text {Sbest }}^{\text {gen }, 2}(2), \pi_{\text {Sbest }}^{\text {gen }, 2}(3), \pi_{\text {Sbest }}^{\text {gen }, 2}(4)\right]=[2,3,1,4], \\
& \pi_{\text {Sbest }}^{\text {gen }, 3}=\left[\pi_{\text {Sbest }}^{\text {gen }, 3}(1), \pi_{\text {Sbest }}^{\text {gen }, 3}(2), \pi_{\text {Sbest }}^{\text {gen }, 3}(3), \pi_{\text {Sbest }}^{\text {gen }, 3}(4)\right]=[3,2,1,4], \quad \pi_{\text {Sbest }}^{\text {gen }, 4}= \\
& {\left[\pi_{\text {Sbest }}^{\text {gen }, 4}(1), \pi_{\text {Sbest }}^{\text {gen }, 4}(2), \pi_{\text {Sbest }}^{\text {gen }, 4}(3), \pi_{\text {Sbest }}^{\text {gen }, 4}(4)\right]=[4,3,2,1], \text { and } \pi_{\text {Sbest }}^{\text {gen }, 5}=\left[\pi_{\text {Sbest }}^{\text {gen }, 5}(1)\right. \\
& \left.\pi_{\text {Sbest }}^{\text {gen }, 5}(2), \pi_{\text {Sbest }}^{\text {gen }, 5}(3), \pi_{\text {Sbest }}^{\text {gen }, 5}(4)\right]=[4,3,1,2] \text {. When } x=1 \text {, according to } \\
& \text { Eqs. (10) and (11), the similar blocks [1,2] (i.e., } y=1 \text { and } z=2 \text { ), } \\
& {[2,3] \text { (i.e., } y=2 \text { and } z=3), [3,2] \text { (i.e., } y=3 \text { and } z=2), \text { and } [4,3] \text { (i.e., } } \\
& y=4 \text { and } z=3 \text { ) at the first position of the five superior solutions can be } \\
& \text { recorded respectively. That is, we can get }
\end{aligned}
$$

$$
\begin{aligned}
& M C_{4 \times 4 \times 4}^{\text {gen }}(1,1,2)=\sum_{k=1}^{5} N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, k}(1,1,2) \\
& =N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, 1}(1,1,2)+N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, 2}(1,1,2) \\
& \quad+N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, 3}(1,1,2)+N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, 4}(1,1,2) \\
& \quad+N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, 5}(1,1,2)=1+0+0+0+0=1 \\
& M C_{4 \times 4 \times 4}^{\text {gen }}(1,2,3)=\sum_{k=1}^{5} N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, k}(1,2,3) \\
& =N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, 1}(1,2,3)+N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, 2}(1,2,3) \\
& \quad+N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, 3}(1,2,3)+N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, 4}(1,2,3) \\
& \quad+N_{c, c} M C_{4 \times 4 \times 4}^{\text {gen }, 5}(1,2,3)=0+1+0+0+0=0=1
\end{aligned}
$$

$$
\begin{aligned}
& M C_{4 \times 4 \times 4}^{g m}(1,3,2)=\sum_{k=1}^{8} N_{c-} M C_{4 \times 4 \times 4}^{g m, k}(1,3,2) \\
& =N_{c-} M C_{4 \times 4 \times 4}^{g m, 3}(1,3,2)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 2}(1,3,2) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 3}(1,3,2)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 4}(1,3,2) \\
& +N_{c-} M C_{4 \times 4 \times 4}^{g m, 5}(1,3,2)=0+0+1+0+0=1 \\
& M C_{4 \times 4 \times 4}^{g m}(1,4,3)=\sum_{k=1}^{8} N_{c-} M C_{4 \times 4 \times 4}^{g m, k}(1,4,3) \\
& =N_{c-} M C_{4 \times 4 \times 4}^{g m, 1}(1,4,3)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 2}(1,4,3) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 3}(1,4,3)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 4}(1,4,3) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 5}(1,4,3)=0+0+0+1+1=2
\end{aligned}
$$

The values of other cells in $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4}}^{(2)}$ (1) are set to 0 . Similarly, when $x=2$, the four similar blocks of jobs [2,1] (i.e., $y=2$ and $z=1$ ), [2,3] (i.e., $y=2$ and $z=3$ ), [3,1] (i.e., $y=3$ and $z=1$ ) and [3,2] (i.e., $y=3$ and $z=2$ ) at the second position of these superior solutions can also be recorded respectively. Then, we have

$$
\begin{aligned}
& M C_{4 \times 4 \times 4}^{g m}(2,2,1)=\sum_{k=1}^{8} N_{c-} M C_{4 \times 4 \times 4}^{g m, k}(2,2,1) \\
& =N_{c-} M C_{4 \times 4 \times 4}^{g m, 1}(2,2,1)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 2}(2,2,1) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 3}(2,2,1)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 4}(2,2,1) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 5}(2,2,1)=0+0+1+0+0=1 \\
& M C_{4 \times 4 \times 4}^{g m}(2,2,3)=\sum_{k=1}^{8} N_{c-} M C_{4 \times 4 \times 4}^{g m, k}(2,2,3) \\
& =N_{c-} M C_{4 \times 4 \times 4}^{g m, 1}(2,2,3)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 2}(2,2,3) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 3}(2,2,3)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 4}(2,2,3) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 5}(2,2,3)=1+0+0+0+0=1 \\
& M C_{4 \times 4 \times 4}^{g m}(2,3,1)=\sum_{k=1}^{8} N_{c-} M C_{4 \times 4 \times 4}^{g m, k}(2,3,1) \\
& =N_{c-} M C_{4 \times 4 \times 4}^{g m, 1}(2,3,1)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 2}(2,3,1) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 3}(2,3,1)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 4}(2,3,1) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 5}(2,3,1)=0+1+0+0+1=2 \\
& M C_{4 \times 4 \times 4}^{g m}(2,3,2)=\sum_{k=1}^{8} N_{c-} M C_{4 \times 4 \times 4}^{g m, k}(2,3,2) \\
& =N_{c-} M C_{4 \times 4 \times 4}^{g m, 1}(2,3,2)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 2}(2,3,2) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 3}(2,3,2)+N_{c-} M C_{4 \times 4 \times 4}^{g m, 4}(2,3,2) \\
& \quad+N_{c-} M C_{4 \times 4 \times 4}^{g m, 5}(2,3,2,2)=0+0+0+1+0=1
\end{aligned}
$$

The rest cells in $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4}}^{(2)}$ are set to 0 . There are four similar blocks $[1,2],[1,4],[2,1]$ and $[3,4]$ at the third position (i.e., $x=3$ ). Therefore, we can also get $M C_{4 \times 4 \times 4}^{g m}(3,1,2)=1, M C_{4 \times 4 \times 4}^{g m}(3,1,4)=2$, $M C_{4 \times 4 \times 4}^{g m}(3,2,1)=1$, and $M C_{4 \times 4 \times 4}^{g m}(3,3,4)=1$, respectively. Because the information of similar blocks in the last position has already been saved in the previous position, each element in $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4}}^{(4)}$ can be set to 0 . Therefore, according to Eq. (13), the hierarchical structure of the matrix cube $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4}}^{(2)}$ can be obtained, which is shown in Fig. 3.

Obviously, it can be seen that both the order of jobs and the job blocks with their exact positions (i.e., ordinal numbers) can be preserved in $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m}$. That is, the similar blocks in the different positions of superior solutions can be learned and saved. Nevertheless, as for the
![img-2.jpeg](img-2.jpeg)

Fig. 3. Illustration of the hierarchical structure of $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4}}^{(2)}$.
two-dimensional EDAs, the position information of the similar blocks is ignored. For example, though the job block [2,3] appears in the second position in $\boldsymbol{x}_{\text {Shest }}^{\text {gen.1 }}$ and also in the first position in $\boldsymbol{x}_{\text {Shest }}^{\text {gen.2 }}$, this block information can only be saved in one element of a two-dimensional matrix. Hence, the shortcoming of the two-dimensional EDAs is that the sampling procedure cannot determine the suitable positions to place similar blocks. However, in the proposed matrix cube $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m}$, all blocks can be reserved in the different layers of $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m}$ in accordance with their respective positions. As can be seen from Fig. 3, the job block [2,3] in $\boldsymbol{x}_{\text {Shest }}^{\text {gen.1 }}=[1,2,3,4]$ is reserved in $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4}}^{(2)}$ (2) (i.e., the second layer of $\left.\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4}}^{(2)}\right)$ and the same block $[2,3]$ in $\boldsymbol{x}_{\text {Shest }}^{\text {gen.2 }}=[2,3,1,4]$ is recorded in $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4}}^{(2)}$ (1) (i.e., the first layer of $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4}}^{(2)}$ ). In this way, the job blocks or similar blocks with their corresponding positions and the total order information can be learned and reserved properly in different layers of the three-dimensional matrix cube $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m}$, which is helpful for effectively guiding the search to promising regions and avoiding the promising patterns being destroyed or inappropriately fused.

### 3.2.2. Matrix-cube-based probabilistic model

Different from the existing research works, a three-dimensional probability model-based evolutionary mechanism is developed to accumulate the valuable information (i.e., the similar blocks with their corresponding positions and the total order information) from the superior solutions by the matrix cube $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m}$. The proposed learning strategy not only achieves self-learning from the matrix cube, but also has a significant effect on the searching behavior of EDA. Let $\operatorname{Pro}_{,}, \mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m}$ be the matrix-cube-based probabilistic model, and $\operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}(x, y, z)$ the element in $\mathbf{P r o}_{,}, \mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m}$. The $x$ th layer of $\mathbf{P r o}_{,}, \mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m}$ is defined as follows:

$$
\begin{aligned}
& \operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}(\mathbf{x})=\left[\begin{array}{c}
\operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}(\mathbf{x}, \mathbf{1}) \\
\operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}(\mathbf{x}, \mathbf{n}) \\
\hline
\end{array}\right]_{\left[\begin{array}{c}
\left.-\mathrm{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}\right)(\mathbf{x}, \mathbf{1}, 1) \\
\left[\begin{array}{c}
\operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}(\mathbf{x}), \mathbf{1}, 1, n \\
\operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}(\mathbf{x}), \mathbf{n}, 1)
\end{array}\right]_{\left[\begin{array}{c}
\operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}(\mathbf{x}), \mathbf{n}, n)
\end{array}\right]_{\text {is. } \times \mathbf{1}} \quad \text { For } \quad \operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}(x, n, n) \quad \begin{array}{c}
\text { is. } \times \mathbf{1} \\
\text { for } \end{array} \\
& \text { Furthermore, let } \operatorname{Sum}_{,}, \mathrm{MC}^{\text {gen }}(x)=\sum_{y=1}^{n} \sum_{z=1}^{n} M C_{\text {is. }}^{\text {gen }}(x, y, z) \text { and } \\
& \operatorname{Sum}_{,}, \operatorname{Pro}_{,}, \mathrm{MC}^{\text {gen }}(x)=\sum_{y=1}^{n} \sum_{z=1}^{n} \operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}(x, y, z)(x=1, \ldots, n-1) \text { be } \\
& \text { the total summation of all elements in } \mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m} \mathbf{( x )} \text { and } \mathbf{P r o}_{,}, \mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m} \mathbf{( x )} \text {, } \\
& \text { respectively. Then the update procedure of } \mathbf{P r o}_{,}, \mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m} \text { is designed as } \\
& \text { follows: }
\end{aligned}
$$

Step 0: Initialize the matrix-cube-based probabilistic model, i.e.,

$$
\operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\text {gen }}(x, y, z)=\left\{\begin{array}{l}
1 / n, x=1, y, z=1, \ldots, n \\
1 / n^{2}, x=2,3, \ldots, n-1, y, z=1, \ldots, n
\end{array}\right.
$$

Step 1: Calculate $\mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4} \times \mathbf{4} \times 4}^{g m}$ and set

$$
\begin{aligned}
& \operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\mathrm{gen} \times \mathrm{ca}}(x, y, z) \\
& \quad=\left\{\begin{array}{l}
M C_{\text {is. }}^{\mathrm{gen} \times \mathrm{ca}}(x, y, z) / \operatorname{Sum}_{,}, \mathrm{MC}^{\mathrm{cl}}(x), x=1, y, z=1, \ldots, n \\
\left\{\operatorname{Pro}_{,}, \mathrm{MC}_{\text {is. }}^{\mathrm{gen} \times \mathrm{ca}}(x, y, z)+M C_{\text {is. }}^{\mathrm{cl}}(x, y, z)\right\} / \\
\left\{\operatorname{Sum}_{,}, \operatorname{Pro}_{,}, \mathrm{MC}^{\mathrm{cl}}(x)+\operatorname{Sum}_{,}, \mathrm{MC}^{\mathrm{cl}}(x)\right\}, x=2, \ldots, n-1, y, z=1, \ldots, n
\end{array}\right.
\end{aligned}
$$

![img-3.jpeg](img-3.jpeg)

Fig. 4. Illustration for the hierarchical structure of $\operatorname{Pro}_{n} \mathbf{M C}_{4 \times 4 \times 4}^{4}$.

Step 2: Set gen $=1$.
Step 3: Calculate $\mathbf{M C}_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }}$ and update $\mathbf{P r o}_{n} \mathbf{M C}_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }}$ by using

$$
\begin{aligned}
& \operatorname{Pro}_{n} M C_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }+1}(x, y, z)=(1-r) \times \operatorname{Pro}_{n} M C_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }}(x, y, z) \\
& +r \times M C_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }}(x, y, z) / \operatorname{Sum}_{n} M C^{\text {gen }}(x) \\
& x=1, \ldots, n-1, y, z=1, \ldots, n
\end{aligned}
$$

Step 4: Set gen $=$ gen +1 . If gen $<$ maxgen, then go to Step 3.
Step 0 is used to set all elements in $\mathbf{P r o}_{n} \mathbf{M C}_{4 \times 4 \times 4}^{0}$ to $1 / n$ instead of $1 / n^{2}$, which can increase the selection probability of blocks in superior individuals at initial stage. Steps 1 and 3 are utilized to accumulate valuable information from $\mathbf{M C}_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }}$, which is helpful for achieving a tradeoff between the current and the historical information. Fig. 4 shows the update process of the probabilistic model at generation one by using the superior individuals considered in Section 3.2.1. It can be seen from Fig. 4 that the subscripts of the larger values in $\mathbf{P r o}_{n} \mathbf{M C}_{4 \times 4 \times 4}^{1}$ correspond with the ordinal relationships and the similar blocks in these superior individuals. This means that $\operatorname{Pro}_{n} \mathbf{M C}_{\mathbf{4} \times \mathbf{4} \times \mathbf{4}}^{\text {gen }}$ can accumulate valuable information more accurately.

### 3.2.3. New population generation method

The global search is performed by sampling the probabilistic model to generate new individuals. In order to guarantee the initial population with certain quality and diversity, half of the individuals in the population are generated via the simple heuristics $\mathrm{H}_{21}$ and $\mathrm{H}_{22}$ presented by Hatami et al. [17], and the remaining individuals are randomly generated. Let $\boldsymbol{\pi}^{\text {gen }, \mathbf{k}}=\left[\pi^{\text {gen }, k}(1), \pi^{\text {gen }, k}(2), \ldots, \pi^{\text {gen }, k}(n)\right]$ be the $k$ th ( $k=1, \ldots$, popsize $)$ individual in $\operatorname{Pop}(\mathbf{g e n}), l\left(J_{c}, \boldsymbol{\pi}^{\text {gen }, \mathbf{k}}\right)$ be the number of occurrences for $J_{c}$ and SelectJob( $\boldsymbol{\pi}^{\text {gen, } \mathbf{k}}, i$ ) $(i>1)$ be a selection function. Because the probability value of the occurrence of job block or similar block $\left[\pi^{\text {gen }, k}(i-1), \pi^{\text {gen }, k}(i)\right]$ is stored in the submatrix $\operatorname{Pro}_{n} \mathbf{M C}_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }}(i-1)$, SelectJob $\left(\boldsymbol{\pi}^{\text {gen }, \mathbf{k}}, i\right)$ determines the candidate job $J_{c}$ at the $i$ th position in $\boldsymbol{\pi}^{\text {gen }, \mathbf{k}}$ by using $\mathbf{P r o}_{n} \mathbf{M C}_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }}(i-1, \boldsymbol{\pi}^{\text {gen }, \mathbf{k}}(i-1))$. Then, the details of SelectJob $\left(\boldsymbol{\pi}^{\text {gen }, \mathbf{k}}, i\right)$ is described as follows:

Step 1: Randomly generate a probability $r$ for roulette selection, $r \in$ $\{0, \sum_{k=1}^{n} \operatorname{Pro}_{n} M C_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }-1}(i-1, \pi^{\text {gen }, k}(i-1), h))$.
Step 2: Get $J_{c}$ by the roulette selection method.
Step 2.1: If $r \in\left\{0, \operatorname{Pro}_{n} M C_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }-1}(i-1, \pi^{\text {gen }, k}(i-1), 1)\right.$, then set $J_{c}=1$ and go to Step 3.
Step 2.2: If $r \in\left\{\sum_{k=1}^{n} \operatorname{Pro}_{n} M C_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }-1}(i-1, \pi^{\text {gen }, k}(i-1), h)\right.$, $\sum_{k=1}^{n+1} \operatorname{Pro}_{n} M C_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }}(i-1, \pi^{\text {gen }, k}(i-1), h))$ and pos $\in\{1, \ldots, n-1\}$, then set $J_{c}=$ pos +1 .
Step 3: Return $J_{c}$.
Since SelectJob $\left(\boldsymbol{\pi}^{\text {gen }, \mathbf{k}}, i\right)$ cannot be used to obtain the first job in the new individual, a special sampling method, namely the first position limited selection strategy (FPLSS), is provided to reasonably determine the first job. The details of FPLSS is given as follows:

Step 1: Calculate SumPro, $M C_{\text {init }}^{\text {gen }-1}(z)=\sum_{i=1}^{n} \operatorname{Pro}_{i} M C^{\text {gen }-1}(1, y, z)$;
Obtain the cumulative probability of the $y$ th row of $\mathbf{P r o}_{n} \mathbf{M C}_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }-1}(1)$.
Step 2: Determine the job $J_{c}$ at the first position in $\boldsymbol{\pi}^{\text {gen }, \mathbf{k}}, k=$ $1, \ldots$, popsize by roulette method.
Step 2.1: Randomly generate a $r^{\prime}, \quad r^{\prime} \in$ $\{0, \sum_{k=1}^{n} \operatorname{Sum} \operatorname{Pro}_{n} M C_{\text {init }}^{\text {gen }-1}(h))$.
Step 2.2: If $r^{\prime} \in\left\{0, \operatorname{SumPro}_{n} M C_{\text {init }}^{\text {gen }-1}(1)\right.$, then set $J_{c}=1$ and go to Step 3.
Step 2.3: If $r^{\prime} \in\left\{\sum_{k=1}^{n} \operatorname{Sum} \operatorname{Pro}_{n} M C_{\text {init }}^{\text {gen }-1}(h), \sum_{k=1}^{n+1}\right.$ $\operatorname{SumPro}_{n} M C_{\text {init }}^{\text {gen }-1}(h))$ and pos $\in\{1, \ldots, n-1\}$, then set $J_{c}=$ pos +1 .
Step 3: Return $J_{c}$ as the job in the first position.
Then, the new population generation method is given as follows:
Step 1: Set $k=1$.
Step 2: Generate a new individual $\boldsymbol{\pi}^{\text {gen }, \mathbf{k}}$.
Step 2.1: Set $\boldsymbol{\pi}^{\text {gen }, \mathbf{k}}$ as an empty sequence. Select the first job $J_{c}$ according to the above FPLSS.
Step 2.2: Set $\pi^{\text {gen }, k}(1)=J_{c}$ and $i=2$.
Step 2.3: Set $J_{c}=$ SelectJob( $\boldsymbol{\pi}^{\text {gen }, \mathbf{k}}, i$ ).
Step 2.4: If $l\left(J_{c}, \boldsymbol{\pi}^{\text {gen }, \mathbf{k}}\right)=2$, then go to Step 2.3.
Step 2.5: Set $\pi^{\text {gen }, k}(i)=J_{c}$.
Step 2.6: Set $i=i+1$.
Step 2.7: If $i \leq n$, then go to Step 2.3.
Step 3: Set $k=k+1$.
Step 4: If $k \leq$ popsize, then go to Step 2.
Step 5: Output Pop(gen).
It is noted that steps 2.3-2.5 are used to build the job block (i.e., $\left[\pi^{\text {gen }+1, k}(i-1), \pi^{\text {gen }+1, k}(i)\right]$ ) at positions $i-1$ and $i$ by means of sampling from the probabilistic submatrix $\mathbf{P r o}_{n} \mathbf{M C}_{\text {isca } \times \mathbf{4} \times \mathbf{4}}^{\text {gen }}(i-1)$. Meanwhile, step 2 can link each job block or similar block located at different positions together to generate a new solution, which is a key step of global exploration of the proposed MCEDA.

### 3.3. Problem-dependent local search

It has been generally recognized that incorporating effective local exploitation into a meta-heuristic can increase its search depth in solution space, thereby enhance its performance [1,33,38,39]. In this subsection, four critical path-based neighborhood searches and eight problem-specific neighborhood searches are first designed, and then a problem-dependent variable neighborhood descent (VND) search is proposed based on these neighborhood searches to execute deep exploitation around the promising regions or superior solutions.

### 3.3.1. Neighborhood searches

For the combinatorial optimization problem, each global optimal solution is a local optimal solution under all neighborhood structures, and

high-quality solutions close to a global optimal solution are often local optimal solutions under multiple neighborhood structures. The repeated greedy search process (RGSP) with one single neighborhood operator is easy to reach and trap into a local optimal solution of the corresponding neighborhood structure, but the quality of this solution is usually not good enough. Meanwhile, the DAPFSP further considers multiple parallel flow shops and one assembly shop on the basis of the traditional flow shop, which makes its solution space huge and complex. That is, many high-quality local optimal solutions are scattered in the very deep regions of its solution space. It is difficult to find high-quality solutions for the DAPFSP. Therefore, we design twelve neighborhood searches based on different neighborhood structures to enrich search behavior and avoid the algorithm falling into a local optimal solution with common or low quality.

### 3.3.1.1. Four critical path-based neighborhood searches.

The first four neighborhood searches are based on the so-called critical path in the solution's Gantt chart. The critical path refers to a continuous and longest path from the start to end of a schedule (i.e., a solution) without idle time between any two jobs [40]. For the DAPFSP, the makespan of a schedule is determined by the length of the critical path and it cannot be decreased without changing the scheduling of jobs in the critical path. In other words, it is possible to obtain better solutions by changing the jobs on the critical path. Let $f_{c}$ be the critical factory, $n_{f_{c}}$ the total number of jobs assigned to $f_{c}$, and $n_{c}$ the number of the critical jobs in $f_{c}$. The details of these four critical path-based neighborhood searches are described as follows.
(1) Critical_Job_ $N_{\text {Severe }}^{i n}$-Search( $\boldsymbol{\pi}$ ): Generate $n_{f_{c}}-n_{c}$ new solutions or neighbors by swaping a randomly selected critical job $x_{f_{c}}(\alpha)$ $\left(u \in\left(1,2, \ldots, n_{c}\right)\right)$ and each non-critical job $x_{f_{c}}(v)\left(v=n_{c}+1, \ldots, n_{f_{c}}\right)$ in $\boldsymbol{\pi}$, and then return the best neighbor.
(2) Critical_Job_ $N_{\text {Severe }}^{i n}$-Search( $\boldsymbol{\pi}$ ): Generate $n_{f_{c}}-n_{c}+1$ new neighbors by inserting a randomly selected critical job $x_{f_{c}}(\alpha)\left(u \in\left(1,2, \ldots, n_{c}\right)\right)$ before each non-critical job $x_{f_{c}}(v)\left(v=n_{c}+1, \ldots, n_{f_{c}}\right)$ and after the non-critical job $x_{f_{c}}\left(n_{f_{c}}\right)$ in $\boldsymbol{\pi}$, and then return the best neighbor.
(3) Critical_Job_ $N_{\text {Severe }}^{i n}$-Search( $\boldsymbol{\pi}$ ): Generate $F-1$ new neighbors by swaping a randomly selected critical job $x_{f_{c}}(\alpha)\left(u \in\left(1,2, \ldots, n_{c}\right)\right)$ in $\boldsymbol{\pi}$ and a randomly selected job in each non-critical factory of $\boldsymbol{\pi}$, and then return the best neighbor.
(4) Critical_Job_ $N_{\text {Severe }}^{i n}$-Search( $\boldsymbol{\pi}$ ): Generate $F-1$ new neighbors by inserting a randomly selected critical job $x_{f_{c}}(\alpha)\left(u \in\left(1,2, \ldots, n_{c}\right)\right)$ in $\boldsymbol{\pi}$ before or after a randomly selected job in each non-critical factory of $\boldsymbol{\pi}$, and then return the best neighbor.

The neighborhood operations performed in these critical path-based neighborhood searches are illustrated in Fig. 5, where the jobs 3, 18, 17 , and 16 are on the critical path and the job 18 is selected to perform swap and insert operations within the critical factory or between the factories.

### 3.3.1.2. Eight non-critical path-based neighborhood searches.

The remaining eight non-critical path-based neighborhood searches can be classified into two types: four product-based neighborhood searches and four job-based neighborhood searches. Let $S$ be the total number of products, $\lambda(h)(h=1,2, \ldots, S)$ one product of $\boldsymbol{\pi}, \lambda$ the product sequence of $\boldsymbol{\pi}$, and $\boldsymbol{\pi}_{\lambda(h)}$ the product subsequence $\left[\pi_{\lambda(h)}(1), \pi_{\lambda(h)}(2), \ldots, \pi_{\lambda(h)}\left(o_{h}\right)\right]$ of $\boldsymbol{\pi}$.

Three product-based neighborhood searches and three job-based neighborhood searches are realized by Algorithm 1 and Algorithm 2, respectively. The input parameter Neighborhood determines the type of neighborhood search. Moreover, one product-based neighborhood search and one job-based neighborhood search are realized by Algorithm 3 and Algorithm 4, respectively. Each of these neighborhood searches consecutively scans new neighbors (i.e., solutions) of the current $\boldsymbol{\pi}$ via a special neighborhood operator until a local optimal solution under the corresponding neighborhood structure is found. During the
search, the current $\boldsymbol{\pi}$ is updated by its best neighbor if this best neighbor is better than it, which is helpful in concentrating the search on more promising regions. Obviously, each neighborhood search works like a drill bit, constantly digging down to reach a local optimum in solution space.

### 3.3.2. Perturbation and exploitation

In the VND search, the perturbation is needed to escape from the current local optimal solution reached by the exploitation. Because each of the critical path-based neighborhood searches in Section 3.3.1 can quickly find a promising but different solution near the local optimal one, all of them are utilized to execute perturbation in our VND search (see Section 3.3.3). The details of the designed perturbation are provided in Algorithm 5.

The non-critical path-based neighborhood searches in Section 3.3.1 can reach a larger number of neighbors in the quite different regions of solution space, which is beneficial to guiding the search toward high-quality local optima. Thus, the exploitation in our VND search is performed via these production-based and job-based neighborhood searches. The details of the designed exploitation are given in Algorithms 6 and 7, respectively. To accelerate the search process in Algorithms 5-7, the speed-up strategies based on the general property of the permutation-based model for scheduling problem [41] are utilized to calculate the makespan of each neighbor.

### 3.3.3. Variable neighborhood descent search

The variable neighborhood descent (VND) search is used as the local search in MCEDA. The VND method is proposed by Hansen and Mladenovic [42], which has been widely utilized to detect high-quality solutions or potential regions in solution space. The VND method systematically exploits a set of predefined neighborhood structures both in the descent to get different local optimal solutions and in the perturbation to escape from these local optimums. Obviously, the VND method provides a general framework for addressing different combinatorial optimization problems. The key to ensuring VND's performance on the specific problem is to design the problem-dependent neighborhood searches to effectively execute exploitation.

Based on the above designed neighborhood searches (Algorithms 17), the VND search is presented in Algorithm 8, where Line 4 executes perturbation to escape from the current local optimal solution, Lines 11 and 15 perform exploitation or neighborhood searches, Lines 12 and 16 ensure that the search direction is descent during the exploitation phase (Lines 10-25), and Lines 28-30 update the best neighbor found at the exploitation phase. Moreover, $\boldsymbol{\pi}^{\prime}=\boldsymbol{\pi}^{\prime \prime}$ at Line 13 and it at Line 17 guarantee that the perturbation at Line 4 always performs on the best neighbor obtained at the last exploitation phase. The VND search process (Lines 3-34) consists of a series of repeated greedy search processes (RGSPs). Each RGSP (Lines 4-25) is that $\boldsymbol{\pi}^{\prime \prime}$ driven by the production-based neighborhood searches at Line 11 and the job-based neighborhood searches at Line 15 continuously searches down from the perturbation region generated at Line 4 until it reaches a common local optimal solution of the designed neighborhood structures. Since there are four critical path-based neighborhood searches for perturbation (Line 4) and eight non-critical path-based neighborhood searches for exploitation (Lines 11 and 15), the proposed VND search has the ability to perform deep exploitation from different promising regions.

### 3.4. Outline of MCEDA

With the aforementioned design, we give the main framework of MCEDA shown in Fig. 6. It can be seen that the presented scheme can not only apply the matrix-cube-based probabilistic model to estimate the probability distribution of superior solutions and to guide the global exploration for finding promising regions in search space, but also adopt the problem-dependent VND search to perform in-depth local exploitation around these promising regions. Since the global and local searches

# Algorithm 1 

Product_Search $(\pi$, Neighborhood).
Algorithm 1 Product_Search $(\pi$, Neighborhood $)$
Input: $\pi$, Neighborhood
Output: $\pi$

1. Set $h=1$
2. While $(h \leq S)$
3. Extract each product $\lambda(h)$ from product sequence $\lambda$
4. Case Neighborhood
5. Swap: Swap $\lambda(h)$ with every other product in $\lambda$
6. Insert: Insert $\lambda(h)$ at every possible position of $\lambda$
7. Interchange: Interchange $\lambda(h)$ with its adjacent product in $\lambda$
8. End Case
9. $\pi^{*}=$ The best one among the solutions or neighbors generated at lines 4-8
10. If $C_{\max }\left(\pi^{*}\right)<C_{\max }(\pi)$ then
11. $\pi=\pi^{*}, h=1$
12. Else
13. $h=h+1$
14. End If
15. End While
16. Return $\pi$

Algorithm 2
Job_Search( $\pi$, Neighborhood).
Algorithm 2 Job_Search( $\pi$, Neighborhood)
Input: $\pi$, Neighborhood
Output: $\pi$

1. Set $h=1$
2. While $(h \leq S)$
3. Set $j=1$
4. While $\left(j \leq \omega_{h}\right)$
5. Extract each job $\pi_{\lambda(h)}(j)$ from $\pi_{\lambda(\mathbf{h})}$
6. Case Neighborhood
7. Swap: Swap $\pi_{\lambda(h)}(j)$ with every other job in $\pi_{\lambda(\mathbf{h})}$

8 .
Insert: Insert $\pi_{\lambda(h)}(j)$ at every possible position of $\pi_{\lambda(\mathbf{h})}$
9. Interchange: Interchange $\pi_{\lambda(h)}(j)$ with its adjacent job $\pi_{\lambda(h)}(j+1)$ in $\pi_{\lambda(\mathbf{h})}$
10. End Case
11. $\pi^{*}=$ The best one among the solutions or neighbors generated at lines 6-10
12. If $C_{\max }\left(\pi^{*}\right)<C_{\max }(\pi)$ then
13. $\pi=\pi^{*}, h=1, j=1$
14. Else
15. $j=j+1$
16. End If
17. End While
18. $h=h+1$
19. End While
20. Return $\pi$

![img-4.jpeg](img-4.jpeg)

Fig. 5. An example of four critical path-based neighborhood searches.

Algorithm 3
Product_Search_Inverse $(\pi)$.
Algorithm 3 Product_Search_Inverse $(\pi)$
Input: $\quad \pi$
Output: $\pi$

1. Inverse the product subsequence between every two different product $s$ in $\lambda$
2. $\pi^{*}=$ The best one among the solutions or neighbors generated at line 1
3. If $C_{\text {max }}\left(\pi^{*}\right)<C_{\text {max }}(\pi)$ then
4. $\pi=\pi^{*}$
5. End If
6. Return $\pi$

# Algorithm 4 

Job_Search_Inverse $(\boldsymbol{\pi})$.
Algorithm 4 Job_Search_Inverse $(\boldsymbol{\pi})$
Input: $\quad \pi$
Output: $\pi$

1. Set $h=1$
2. While $(h \leq S)$
3. Inverse the job subsequence between every two different jobs in $\pi_{i(h)}$
4. $\pi^{*}=$ The best one among the solutions or neighbors generated at line 3
5. If $C_{\text {max }}\left(\pi^{*}\right)<C_{\text {max }}(\pi)$ then
6. $\pi=\pi^{*}, h=1$
7. $\quad$ Else
8. $h=h+1$
9. End If
10. End While
11. Return $\pi$

# Algorithm 5 

Perturbation $(\boldsymbol{\pi}, \text { Neighborhood } \_$Num).
Algorithm 5 Perturbation( $\boldsymbol{\pi}$, Neighborhood _Num)
Input: $\pi$, Neighborhood _Num
Output: $\pi$

1. Case Neighborhood _Num
2. 
3: Critical _Job _N $_{\text {Swap }}^{i n}$ _Search $(\boldsymbol{\pi})$ // (1) in Subsubsection 3.3.1
4. 
5: Critical _Job _N $_{\text {Insert }}^{i n}$ _Search $(\boldsymbol{\pi})$ // (2) in Subsubsection 3.3.1
6. 
7. Critical _Job _N $_{\text {Swap }}^{b t}$ _Search $(\boldsymbol{\pi})$ // (3) in Subsubsection 3.3.1
8. 
9. Critical _Job _N $_{\text {Insert }}^{b t}$ _Search $(\boldsymbol{\pi})$ // (4) in Subsubsection 3.3.1
10. End Case
11. Return $\pi$

## Algorithm 6

Exploitation_Product_Search( $\boldsymbol{\pi}$, Neighborhood_Num).
Algorithm 6 Exploitation _Product_Search( $\boldsymbol{\pi}$, Neighborhood _Num)
Input: $\quad \pi$, Neighborhood _Num
Output: $\pi$

1. Case Neighborhood _Num
2. 
3: Product _Search( $\boldsymbol{\pi}$, Swap)
// Algorithm 1
4. 
5. Product _Search( $\boldsymbol{\pi}$, Insert)
// Algorithm 1
6. 
7. Product _Search( $\boldsymbol{\pi}$, Interchange)
// Algorithm 1
8. 
9. Product _ $N_{\text {Inverse }}$ _Search( $\boldsymbol{\pi}$ )
// Algorithm 2
10. End Case
11. Return $\pi$

## Algorithm 7

Exploitation_Job_Search( $\boldsymbol{\pi}$, Neighborhood_Num).
Algorithm 7 Exploitation _Job _Search( $\boldsymbol{\pi}$, Neighborhood _Num)
Input: $\quad \pi$, Neighborhood _Num
Output: $\pi$

1. Case Neighborhood _Num
2. 
3: Job _Search( $\boldsymbol{\pi}$, Swap)
// Algorithm 3
4. 
5. Job _Search( $\boldsymbol{\pi}$, Insert)
// Algorithm 3
6. 
7. Job _Search( $\boldsymbol{\pi}$, Interchange)
// Algorithm 3
8. 
9. Job _ $N_{\text {Inverse }}$ _Search( $\boldsymbol{\pi}$ )
// Algorithm 4
10. End Case
11. Return $\pi$
are well stressed and balanced, the proposed MCEDA can be expected to achieve better results for addressing the DAPFSP. In next section, we will investigate the performance of MCEDA.

### 3.5. Convergence analysis of MCEDA

Although empirical evidence indicates that EDA has effectiveness and efficiency for solving complex optimization problems [30-36,38], there are few theoretical results concerning its convergence proper-
ties. The theoretical investigation on evolutionary algorithms can provide more insight into the principles and mechanism of the optimizer [43-45]. In this subsection, the convergence properties of our proposed MCEDA is theoretically analyzed by means of homogeneous finite Markov model. For convenience, some preliminaries are provided as follows.

Definition 1. The set of $N$ finite and feasible individuals or solutions constitutes the population $\operatorname{Pop}=\left\{I_{1}, I_{2}, \ldots, I_{N}\right\}$. Individual state is de-

# Algorithm 8 VND Search. 

## Algorithm 8 VND Search

Input: $\quad \pi_{\text {best }}, l_{\text {max }}^{p}=4, l_{\text {max }}^{J}=4, N_{\text {max }}^{c}=4$
Output: $\pi_{\text {best }}$
1: Obtain the corresponding product sequence $\lambda_{\text {best }}$ according to the $\pi_{\text {best }}$
2: $\pi^{\prime}=\pi_{\text {best }}, k=1$, flag $=$ true
3: While $k<N_{\max }^{c}$ do
4: $\quad \pi^{\prime}=$ Perturbation $\left(\pi^{\prime}, k\right), l^{p}=1, l^{J}=1 / /$ Perturbation Algorithm 5
5: $\quad$ ExploitBest_ $C_{\max }=C_{\max }\left(\pi^{\prime}\right)$, Perturbation_ $C_{\max }=C_{\max }\left(\pi^{\prime}\right)$
6: If flag $=$ true then
7: $\quad$ TotalExploitBest_ $C_{\max }=C_{\max }\left(\pi^{\prime}\right), \pi_{\text {TotalExploitBest }}=\pi^{\prime}$
8: End If
9: flag $=$ flase
10: While $l^{p}<l_{\text {max }}^{p}$ do //Exploitation phase
11: $\pi^{\prime}=$ Exploitation_Product_Search $\left(\pi^{\prime}, l^{p}\right) / /$ Algorithm 6
12: If $C_{\max }\left(\pi^{\prime}\right)<$ ExploitBest_ $C_{\max }$ then
13: $\quad$ ExploitBest_ $C_{\max }=C_{\max }\left(\pi^{\prime}\right), \pi^{\prime}=\pi^{\prime}, l^{p}=1, l^{J}=1$
14:
15:
16: $\quad$ While $l^{J}<l_{\text {max }}^{J}$ do
$\pi^{\prime}=$ Exploitation _Job_Search $\left(\pi^{\prime}, l^{J}\right) / /$ Algorithm 7
17: If $C_{\max }\left(\pi^{\prime}\right)<$ ExploitBest_ $C_{\max }$ then
18: $\quad$ ExploitBest_ $C_{\max }=C_{\max }\left(\pi^{\prime}\right), \pi^{\prime}=\pi^{\prime}, l^{J}=1$
19:
20:
21:
22:
Else
23:
24:
25:
End While
If ExploitBest_ $C_{\max }<$ Perturbation_ $C_{\max }$ then
26: $\quad k=1$
27: If ExploitBest_ $C_{\max }<$ TotalExploitBest_ $C_{\max }$ then
29: TotalExploitBest_ $C_{\max }=$ ExploitBest_ $C_{\max }, \pi_{\text {TotalExploitBest }}=\pi^{\prime}$
End If
Else
30: $\quad k=k+1$
31: End If
32: End While
35: If TotalExploitBest_ $C_{\max }<C_{\max }\left(\pi_{\text {best }}\right)$ then
36: $\quad \pi_{\text {best }}=\pi_{\text {TotalExploitBest }}$
37: End If
38: Return $\pi_{\text {best }}$

![img-5.jpeg](img-5.jpeg)

Fig. 6. The main framework of MCEDA for DAPFSP.
termined by the vector $\mathbf{x}$ and all individual states of the population form the population state $\mathbf{S}^{\mathbf{P}}=\left(x_{1}, x_{2}, \ldots, x_{N}\right)$, where $x_{k}$ is the state of $I_{k}(k=1,2, \ldots, N)$.

Definition 2. The individual state space is denoted as $\Phi$. The population state space $\Omega$ consists of all possible states of the population, i.e., $\Omega=$ $\mathbf{S}_{\mathbf{i}}^{\mathbf{P}} \cup \mathbf{S}_{\mathbf{i}}^{\mathbf{P}} \cup \ldots \cup \mathbf{S}_{\mathbf{N}^{\prime}}^{\mathbf{P}}$, where $\mathbf{S}_{\mathbf{i}}^{\mathbf{P}}=\left(x_{i 1}, x_{i 2}, \ldots, x_{i N}\right)\left(i=1,2, \ldots, N^{\prime}\right), \mathbf{S}_{\mathbf{i}}^{\mathbf{P}} \cap$ $\mathbf{S}_{\mathbf{j}}^{\mathbf{P}}=\emptyset$ for $\forall i, j \in \mathbf{N}^{\prime} \wedge i \neq j$, and $\Omega=\Phi^{N}$.

Definition 3. In MCEDA, the state transition probability of individuals or solutions from two randomly selected states $x_{i}$ to $x_{j}$ in one step is denoted by $p\left(T_{\Phi}\left(x_{i}\right)=x_{j}\right)$, where $T_{\Phi}$ is the transition function in the state space $\Phi$. Similarly, the state transition probability of the population from $S_{i}^{\mathrm{P}}=\left(x_{i 1}, x_{i 2}, \ldots, x_{i N}\right)$ to $S_{j}^{\mathrm{P}}=\left(x_{j 1}, x_{j 2}, \ldots, x_{j N}\right)$ is represented as $p\left(T_{\Omega} \mid S_{i}^{\mathrm{P}}\right)=S_{j}^{\mathrm{P}}$ ), where $T_{\Omega}$ is the transition function in the population state space $\Omega$.

Definition 4. In MCEDA, the optimal population state set is defined as $\mathbf{S} \Leftrightarrow=\left(x_{1}, x_{2}, \ldots, x_{N}\right)$, where $x_{i}{ }^{\mathrm{T}} \in \mathbf{B}^{+}$and $\mathbf{B}^{+}$is the set of the global optima of the considered optimization problem.

Definition 5. Let $\{\mathbf{S P}(\mathbf{t}), t=0,1,2, \ldots\}$ be a sequence of solutions generated by the population-based meta-heuristic algorithm. The stochastic sequence $\{\mathbf{S P}(\mathbf{t}), t=0,1,2, \ldots\}$ weakly converges in the sense of probability to the global optimum, if and only if $\lim _{t \rightarrow \infty} p\left\{\mathbf{S P}(\mathbf{t}) \cap \mathbf{B} * \neq \emptyset\right\}=1$.

Lemma 1. In MCEDA, the individual state $x_{i}$ is essentially shifted in one step to another state $x_{j}$, and its state transition probability is given by
$p\left(T_{\Phi}\left(x_{i}\right)=x_{j}\right)=\prod_{l=1}^{n} P_{x_{i} \rightarrow x_{j}}^{(l)}$
where $\quad P_{x_{i} \rightarrow x_{j}}^{(l)}=\left\{\begin{array}{l}\sum_{i=1}^{n}\left(\frac{\sum_{i \rightarrow x_{j}} \text { Pro_MC( } 1, i^{\prime}, z)}{\sum_{i=1}^{n} \sum_{i \rightarrow 1} \text { Pro_MC( } 1, y, z)}\right) \times \operatorname{Sel}\left(i^{\prime}\right), l=1 \\ \sum_{i=1}^{n}\left(\frac{\text { Pro_MC( } i-1, x_{i j} \mid(i-1), i^{\prime})}{\sum_{i=1}^{n} \text { Pro_MC( } i-1, x_{i j} \mid(i-1), z)}\right) \times \operatorname{Sel}\left(i^{\prime}\right), l>1\end{array}\right.$, and
$\operatorname{Sel}(x)=\left\{\begin{array}{l}1, \text { if } x \text { is selected } \\ 0, \text { else }\end{array}\right.$.
Proof. According to the Section 3.2, our proposed three-dimensional probability model employs an incremental learning mechanism to accumulate the valuable information from the superior solutions during the searching process. The valuable information can be accumulated into the three-dimensional probability model of MCEDA if and only if the individual corresponding to the state $x_{i}$ is a superior solution. The next offspring is generated by sampling from this probability model. Let $\boldsymbol{\alpha}_{\mathbf{x}_{\mathbf{j}}}$ be the job sequence of the $j$ th individual state $x_{j}$, and the element $x_{i j}(l)(l=1,2, \ldots, n)$ the $l$ th job in $\boldsymbol{\alpha}_{\mathbf{x}_{j}}$. For the selection function $S_{i}$ (ext.Iob) $\left(\boldsymbol{\alpha}_{\mathbf{x}_{j}}, l\right)$ with roulette selection method, the probability to determine the $l$ 'th job selected and placed in the first position $(l=1)$ of sequence $\boldsymbol{\alpha}_{\mathbf{x}_{\mathbf{j}}}$ is $\sum_{i=1}^{n} \operatorname{Pro}_{i} M C\left(1, i^{\prime}, z\right) / \sum_{i=1}^{n} \sum_{i=1}^{n} \operatorname{Pro}_{i} M C(1, y, z)$. The selection event of all jobs is a mutually exclusive event. The selection probability is independent of each job. Then the selection probability $\sum_{i^{\prime}=1}^{n}\left(\frac{\sum_{i=1}^{n} \operatorname{Pro}_{i} M C\left(1, i^{\prime}, z\right)}{\sum_{i=1}^{n} \sum_{i=1}^{n} \operatorname{Pro}_{i} M C(1, y, z)}\right) \times \operatorname{Sel}\left(i^{\prime}\right)$ of the selected job at the first position in the sequence $\boldsymbol{\alpha}_{\mathbf{x}_{\mathbf{j}}}$ can be calculated. Similarly, the probability of all possible selected jobs located in the $l$ th $(l>1)$ position of $\boldsymbol{\alpha}_{\mathbf{x}_{\mathbf{j}}}$ is given by $\sum_{i^{\prime}=1}^{n}\left(\frac{\operatorname{Pro}_{i} M C\left(i-1, x_{i j} \mid(i-1), i^{\prime}\right)}{\sum_{i=1}^{n} \operatorname{Pro}_{i} M C\left(i-1, x_{i j} \mid(i-1), j\right)}\right) \times \operatorname{Sel}\left(i^{\prime}\right)$. Therefore, the state transition probability from $x_{i}$ to $x_{j}$ can be expressed in the form of joint probability $p\left(T_{\Phi}\left(x_{i}\right)=x_{j}\right)=\prod_{l=1}^{n} P_{x_{i} \rightarrow x_{j}}^{(l)}$. This completes the proof.

Lemma 2. In the iterative process of MCEDA, the state transition probability of the population from $\mathbf{S}_{\mathbf{i}}^{\mathbf{P}}$ to $\mathbf{S}_{\mathbf{j}}^{\mathbf{P}}$ in one step is the joint probability
$p\left(T_{\Omega}\left(\mathbf{S}_{\mathbf{i}}^{\mathbf{P}}\right)=\mathbf{S}_{\mathbf{j}}^{\mathbf{P}}\right)=\prod_{l=1}^{N} p\left(T_{\Phi}\left(x_{i k}\right)=x_{j k}\right)$
where $N$ is the number of the population.
Proof. $\quad T_{\Omega}\left(\mathbf{S}_{\mathbf{i}}^{\mathbf{P}}\right)=\mathbf{S}_{\mathbf{j}}^{\mathbf{P}}$ indicates that all individual states of population state $\mathbf{S}_{\mathbf{i}}^{\mathbf{P}}$ are simultaneously transferred to the corresponding individual states of population state $\mathbf{S}_{\mathbf{i}}^{\mathbf{P}}$, i.e., $T_{\Phi}\left(x_{i k}\right)=x_{j k}$ for $k=1,2, \ldots, N$. Since the state transfer processes among individuals are just independent events that aren't related to each other, Eq. (16) holds. This completes the proof.
Lemma 3. In MCEDA, the population state sequence $\{\mathbf{S P}(\mathbf{t}), t \geq 0\}$ is a finite homogeneous Markov chain on the state space $\Omega$.

Proof. Because both the population size and the number of iterations are finite, the search space of any meta-heuristic algorithms is finite during the whole evolutionary process. According to Definition 2, the MCEDA's population state $\mathbf{S}^{\mathbf{P}}=\left(x_{1}, x_{2}, \ldots, x_{N}\right)$ at each generation consists of the state of $N$ individuals and the state of each individual is finite, which leads to the fact that the population state space $\Omega$ is finite. Moreover, the next population state of MCEDA is independent from the past generation or state and only depends on the current state. Hence, the population state sequence $\{\mathbf{S P}(\mathbf{t}), t \geq 0\}$ is a finite homogeneous Markov chain on the state space $\Omega$.

According to the Lemma 2, the state transition probability in one step for any two states transforming from $\mathbf{S P}(\mathbf{t})$ to $\mathbf{S P}(\mathbf{t}+\mathbf{1})$ in $\{\mathbf{S P}(\mathbf{t})$, $t \geq 0\}$ is the joint probability
$p\left(T_{\Omega}\left(\mathbf{S}^{\mathbf{P}}(\mathbf{t})\right)=\mathbf{S}^{\mathbf{P}}(\mathbf{t}+\mathbf{1})\right)=\prod_{i=1}^{N} p\left(T_{\Phi}\left(x_{i}^{\prime}\right)=x_{i}^{\prime+1}\right)$
From Lemma 1, for each individual state $x_{i}$ of the population state $\mathbf{S}^{\mathbf{P}}$, the state transition probability of going from time $t$ to $t+1$ is determined

by $p\left(T_{\emptyset}\left(x_{i}^{\prime}\right)=x_{i}^{(+1}\right)=\prod_{i=1}^{n} P_{x_{i}^{\prime}=x_{i}^{(+1)}}^{(i)}$. Since the state transition probability is only related to the population state at time $t$ and independent of the state before time $t$, Lemma 3 holds.

Theorem 1. MCEDA can converge to global optimum with the probability $I$, i.e., $\lim _{t \rightarrow \infty} p\left\{\mathbf{S P}(\mathbf{t}) \cap \mathbf{B} \circ \neq \emptyset\right\}=1$.
Proof. Without loss of generality, we assume that the $i$ th population state at generation or iteration times $t$ is $\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}) \in \mathbf{S P}(\mathbf{t})$, and then the state $\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t})$ is transferred to the $j$ th state $\mathbf{S}_{j}^{\mathbf{P}}(\mathbf{t}+\mathbf{1}) \in \mathbf{S P}(\mathbf{t}+\mathbf{1})$ at time $t+1$. For the $t$ th generation, let $p_{t}(t)$ be the probability of $i$ th state of the population state set $\mathbf{S P}(\mathbf{t})$. If $\operatorname{Pop}(\mathbf{t})$ does not contain the optimal solution, then the probability of all states of the population is $\tilde{p}_{t}=\sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o})} p_{t}(t)$.
According to the Lemma 3, we have

$$
\begin{aligned}
\tilde{p}_{t+1} & =\sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}) \mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1}) \in \mathbf{B} \leftrightarrow \mathbf{o}} p_{t}(t) p_{\emptyset}(t) \\
& =\sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o}) \mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1} \in \mathbf{B} \leftrightarrow \mathbf{o})} p_{t}(t) p_{\emptyset}(t)+\sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o}) \mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1} \in \mathbf{B} \leftrightarrow \mathbf{o})} p_{t}(t) p_{\emptyset}(t)
\end{aligned}
$$

According to the non-aftereffect property of Markov chain, we have

$$
\begin{aligned}
& \sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o}) \mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1}) \in \mathbf{B} \leftrightarrow \mathbf{o}} p_{t}(t) p_{\emptyset}(t)+\sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o}) \mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1}) \in \mathbf{B} \leftrightarrow \mathbf{o})} \sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o}) \mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1} \in \mathbf{B} \leftrightarrow \mathbf{o})} p_{t}(t) p_{\emptyset}(t) \\
& =\sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o})} p_{t}(t)=\tilde{p}_{t} .
\end{aligned}
$$

After performing conversion in Eq. (19), we have

Hence, we can get

$$
\begin{aligned}
0 \leq \tilde{p}_{t+1}= & \sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o}) \mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1} \in \mathbf{B} \leftrightarrow \mathbf{o})} p_{t}(t) p_{t j}(t)+\tilde{p}_{t} \\
& -\sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o}) \mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1} \in \mathbf{B} \leftrightarrow \mathbf{o})} \sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o}) \mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1} \in \mathbf{B} \leftrightarrow \mathbf{o})} p_{t}(t) p_{t j}(t) \\
& <\sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o}) \mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1} \in \mathbf{B} \leftrightarrow \mathbf{o})} p_{t}(t) p_{t j}(t)+\tilde{p}_{t}
\end{aligned}
$$

In the above formula, it is obvious that $\sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o})}$ $\sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t}+\mathbf{1} \in \mathbf{B} \leftrightarrow \mathbf{o})} p_{t}(t) p_{t j}(t)=0$. Since $0 \leq \tilde{p}_{t+1}<\tilde{p}_{t}$, we have $\lim _{t \rightarrow \infty} \tilde{p}_{t}=0$. That is, $\lim _{t \rightarrow \infty} p\left\{\mathbf{S P}(\mathbf{t}) \cap \mathbf{B} \circ \neq \emptyset\right\}=1-\lim _{t \rightarrow \infty} \sum_{\mathbf{S}_{i}^{\mathbf{P}}(\mathbf{t} \in \mathbf{B} \leftrightarrow \mathbf{o})} p_{t}(t)=1-\lim _{t \rightarrow \infty} \tilde{p}_{t}=1$. According to the above analyses, it is concluded that MCEDA can converge to the global optimum with the probability 1 .

## 4. Experimental comparisons and statistical analysis

This section describes the experimental settings and results obtained by MCEDA and other compared algorithms for solving the DAPESP with the objective of minimizing makespan. The experimental setup and the tested data sets are provided in Section 4.1. The computational results are organized according to the following aspects: calibration parameters of the proposed MCEDA, assessment of the contribution of components in MCEDA, and comprehensive comparison of the effectiveness of MCEDA with some existing well-performing algorithms.

### 4.1. Experimental setup

In order to reasonably demonstrate the performance of the proposed MCEDA for the DAPESP, we use two benchmark sets (the data are derived from http://soa.iti.es) presented by Hatami et al. [17] to make experimental comparisons among MCEDA and other algorithms. The first
set consists of 900 small-scaled instances, where $n=\{8,12,16,20,24\}$, $m=\{2,3,4,5\}, F=\{2,3,4\}$, and $S=\{2,3,4\}$. The second set is composed of 810 large-scaled instances, where $n=\{100,200,500\}, m=$ $\{5,10,20\}, F=\{4,6,8\}$, and $S=\{30,40,50\}$. For each combination of $\{n, m, F, S\}$, there are five different test instances in the first set and ten different test instances in the second set. To make a fair comparison, we use the maximum elapsed CPU time $n \times(m / 2) \times \rho$ (milliseconds) as the stopping criterion for each compared algorithm. The runtime factor $\rho$ is set as three values: 1,5 and 10 . Considering the problem scale, each compared algorithm is executed 30 and 5 times independently for the first and second sets, respectively. All algorithms have been coded in Delphi XE8 and experiments have been executed on an Intel 2.6 GHz PC server with 64 GB RAM.

To verify the efficiency and effectiveness of the compared algorithms, the experimental results are evaluated by using a statistical metric, namely the average relative percentage deviation (ARPD), which is calculated as follows:

$$
\operatorname{ARPD}=\frac{1}{R} \sum_{i=1}^{R}\left(\frac{C_{i}-C_{a p t}}{C_{a p t}}\right) \times 100 \%
$$

where $C_{a p t}$ is the best-known solution provided in SOA website, and $C_{i}$ is the solution obtained by a specific algorithm in the $i$ th experiment for each instance. The ARPD is widely used to measure the gap between the solution obtained by the algorithm and the best solution found so far [19,20,33]. The lower the value of ARPD is, the higher the performance of algorithm is. Obviously, if the value of ARPD is less than zero, it means that the best-known solution is improved.

For saving space, the test results in the following Tables 6-9 and 1214 are grouped according to the main instance characteristics, i.e., $n, m$, $F$ and $S$. Each result in these tables is the average of the ARPD values of some corresponding instances. That is, there are 270 ARPD values ( $3 \times$ $3 \times 3 \times 10=270$ instances) for each result in these tables except Table 7, and 60 ARPD values ( $4 \times 3 \times 5=60$ instances) for each result in Table 7. In addition, the best, the second-best, and the third-best values in each row of Tables 7-8 and 12-14 are represented by using the bold, the bold and underlined, and the underlined fonts, respectively.

To verify whether the compared algorithms in Section 4.5 were reprogrammed correctly, we ran some of our reprogramming algorithms (i.e., EDAMA [19], HBBO [20], BS-HH [21], IG $\mathrm{I}_{2}$ [22], IGA [23] and HDIWO [24]) on the test sets in [19-24]. These test sets were chosen because only their download links are given in the literature. The test results of both the algorithms in [18-24] and our reprogramming algorithms were summarized in the attached tables A-F, which can be downloaded from https://pan.baidu.com/s/16cWZJFuwALMOvXEpexXmQQ (password: c6qv). It can be seen from each of these attached tables that the two types of test results are very similar. This manifests that our reprogramming algorithms correctly retain the performance of the algorithms in the literature.

### 4.2. Parameter calibration

It's known that the appropriate parameter calibration has a remarkable effect on the performance of the stochastic meta-heuristics, in terms of solution quality and computational efficiency. In this subsection, to decide desirable parameter configurations, the parameters of MCEDA and other compared algorithms are calibrated by means of design of experiment (DOE) technique [46]. We only detail the calibration of MCEDA because of the space limitation, and all experimental results are available upon request from the authors. According to the procedure of MCEDA described in Section 3.2.2, three parameters are included in MCEDA, i.e., the population size (popsize), the percentage of superior sub-population $(\varphi)$, and the learning rate $(\gamma)$. In consideration of the essential differences of the two benchmark sets, the calibrated experiments are separately executed on two different scale sets. Besides, to avoid the risk of over-fitting or biased results, our experiments are conducted by using randomly selected instances as the test bed [33]. For the

Table 3
Combinations of parameter values for MCEDA.

Table 4
Orthogonal array and RV values.
small-scaled instances, one instance $1,16,5,3,2,1$ is used for calibration, where $16,5,3,2$ indicates the combination of $(n=16, m=5, F=3, S=2)$ and the last number 1 means that it is the first instance under this combination. Similarly, another case $1,200,5,6,40,7$ is selected from the largescaled instances. After the preliminary experiments, four potential levels of the three factors or parameters are explicitly listed in Table 3, and the orthogonal array $L_{16}\left(4^{3}\right)$ is selected to arrange these different combinations. That is, the number of parameters is 3 , the number of factor levels is 4 , and the total number of treatments is 16 . Each configuration is conducted 30 independent replications with a predefined elapsed CPU time $n \times(m / 2) \times 10$ (milliseconds). The ARPD value under each configuration is set as a response variable (RV). The orthogonal array and the obtained results are given in Table 4. According to Table 4, the values of average RV (ARV) for all factor levels are figured out to analyze the significance
![img-6.jpeg](img-6.jpeg)
(a) Factor level trends for small-scaled instances

Table 5
The ARV and significant rank of each parameter.
rank, where the Delta value as well as the significance rank are reported in Table 5. To investigate the effects of the key factors for different scale cases, the trend plots of each factor are illustrated in Fig. 7.

From Table 5, it can be seen that popsize results in the largest Delta values, which indicates that popsize has the most important significant impact on the performance of MCEDA. It can also be clearly observed from Fig. 7 that MCEDA with the smallest population size can obtain the lowest ARV for both the small-scaled instances and the large-scaled instances. The performance of the MCEDA degrades significantly with the increase of popsize. This finding suggests that we should set a relatively small value for the population size (i.e., popsize $=50$ ). The reason is that a large value of popsize may be helpful to increase the population diversity, but meanwhile the high computational efforts are needed in the global exploration. When the total running time is limited, the depth of local exploitation cannot be guaranteed. The learning rate $\gamma$ is the second most significant parameter. The learning rate controls the learning speed of the probabilistic model. To be specific, a small value of $\gamma$ slows down the updating process of the probability model and reduces the speed of convergence, while a large value may lead to premature convergence. Therefore, the value of $\gamma$ should be determined by considering the trade-off among the convergence, prematurity and solution quality.

It is clear from Fig. 7(a) and Fig. 7(b) that $\gamma=0.3$ provides the best results. The significance of $\varphi$ ranks the third. Based on the trend curves of $\varphi$ in Fig. 7(a) and Fig. 7(b), $\varphi=0.1$ and $\varphi=0.2$ are suitable for the small-scaled and large-scaled instances, respectively. This indicates that the smaller value of $\varphi$ can focus the search on better regions, and it should be appropriately increased as the problem scale increases to keep a suitable search range. Considering both computational efficiency and solution quality, the suggested parameter values of MCEDA are determined as follows: popsize $=50, \varphi=0.1, \gamma=0.3$ for the small-scaled cases, and popsize $=50, \varphi=0.2, \gamma=0.3$ for the large-scaled instances.
![img-7.jpeg](img-7.jpeg)
(b) Factor level trends for large-scaled instances

Fig. 7. Factor level trends plots for parameters.

Table 6
Comparison results of MCEDA and its two variants on large-scaled instances.

Table 7
Comparison results of MCEDA and twelve heuristics on small-scaled instances.

Table 8
Comparison results of MCEDA and twelve heuristics on large-scaled instances.

### 4.3. Performance analysis of key components in mceda

In this subsection, the influence of the speedup strategy and the VND method proposed in Section 3.3 on MCEDA are investigated to demonstrate their contributions. For this purpose, two variants MCEDA $_{v 1}$ and MCEDA $_{v 2}$ are compared with MCEDA under three stopping criteria. MCEDA $_{v 1}$ removes both the speedup strategies and the perturbation phase from MCEDA, while MCEDA $_{v 2}$ eliminates both the speedup strategies and the VND method from MCEDA. The test results given in Table 6 show that MCEDA is superior to its two variants on most instances in terms of both ARPD and SD. For the runtime factor $\rho=1,5,10$, MCEDA yields the lowest ARPD for all instances.

Furthermore, the analysis of variance (ANOVA) technique is used to analyze the results. The three hypotheses (i.e., normality, homogeneity of variance and independence of the residuals) of ANOVA are accepted in the experiments. Following Pan and Ruiz [33] and many others, we conduct a multifactor ANOVA to examine whether the differences between MCEDA and its variants are statistically significant. The means
plots with $95 \%$ Tukey's HSD confidence intervals for the three compared algorithms are drawn in Fig. 8. As shown in Fig. 8, MCEDA significantly outperforms its two variants, which testifies the effectiveness and efficiency of both the proposed VND method and the speedup strategies.

### 4.4. Comparisons of mceda with twelve effective heuristics

This subsection provides the comparison results of MCEDA with twelve state-of-the-art constructive heuristics (i.e., $\mathrm{H}_{11}-\mathrm{H}_{22}$, and VND $_{011}$ - VND $_{022}$ ) developed by Hatami et al. [17] on two sets of instances. Each of $\mathrm{H}_{11}-\mathrm{H}_{22}$ constructs a complete job sequence by using the priority rule or heuristic rule, i.e. the smallest processing time (SPT) rule or the Framinan and Leisten (FL) heuristic, and then all jobs in the sequence are assigned to the specific factories by using the NR1 or NR2 rules. In addition, each of VND $_{011}$ - VND $_{022}$ further employs some local searches to improve the performance of the corresponding heuristic. The comparison results are listed in Tables 7-9, where Tables 7 and 8 provides the results on small-scaled and large-scaled instances respectively

Table 9
CPU times (second) of MCEDA and twelve heuristics on large-scaled instances.

Table 10
Pair-wise $t$-test results of MCEDA and three best heuristics on two scaled sets.
![img-8.jpeg](img-8.jpeg)

Fig. 8. Means plots with 95\% Tukey's HSD confidence intervals for MCEDA and its two variants on large-scaled instances.
and Table 9 shows the CPU time of each algorithm. It can be seen from Tables 7 and 8 that MCEDA outperforms all the others by a considerable margin and VND $_{\text {H12 }}$, VND $_{\text {H22 }}$ and VND $_{\text {H32 }}$ perform better than the other heuristics. The common feature of these better algorithms is the rational use of VND-based local search to perform further exploitation in solution space. Note that the average CPU time of MCEDA is 37.73 s which is acceptable in real-life environments (see Table 9).

To further check whether the differences between the test results obtained in Tables 7 and 8 are indeed statistically significant, the hypothesis tests ( $t$-test) with $95 \%$ Tukey's HSD confidence interval are executed between MCEDA and each of three best heuristics, respectively. The statistic results are given in Table 10, where if the value of "Significance" in Table 10 is smaller than 0.05 , the difference between the two algorithms is significant. Furthermore, the ANOVA statistical tests are carried out to analyze the results of MCEDA and several better heuristics
![img-9.jpeg](img-9.jpeg)

Fig. 9. Means plots with 95\% Tukey's HSD confidence intervals for MCEDA and several better heuristics on small-scaled instances.
on small-scaled and large-scaled instances, respectively. The means plots with 95\% Tukey's HSD confidence intervals are shown in Figs. 9 and 10, where the non-overlapping intervals indicate that the two algorithms are significantly different in statistical significance. From Table 10 and Figs. 9 and 10, it is clear that MCEDA is statistically better than the compared heuristics.

### 4.5. Comparisons of mceda with eleven state-of-the-art meta-heuristics

In this subsection, to further investigate the efficiency and effectiveness of the proposed MCEDA, comprehensive comparison experiments are conducted on MCEDA and eleven state-of-the-art meta-heuristics, i.e., GA [18], IG $_{3}$ [22], EDAMA [19], HBBO [20], BS-HH [21], HDIWO [24], IGA [23], HVNS [47], HGA [47], HDDE [47], and CMA [48]. The parameters of these compared algorithms are properly calibrated by using the DOE technique and their setting values are listed in Table 11.

![img-10.jpeg](img-10.jpeg)

Fig. 10. Means plots with $95 \%$ Tukey's HSD confidence intervals for MCEDA and several better heuristics on large-scaled instances.

Table 11
The parameter settings of the compared algorithms.

The test results under $\rho=1,5,10$ (see Section 4.1) are obtained and reported in Tables 12-14, respectively. It can be observed from Tables 12-14 that the proposed MCEDA achieves the best results for all instances. The reason is that MCEDA's global search guides the search direction more effectively and its local search further utilizes twelve specific neighborhoods to execute more efficient exploitation.

To make the test results more convincing, a multifactor ANOVA is executed to verify whether the observed differences are statistically significant. The controlled factor are the type of algorithms and the running time factor $\rho$. The means plots with $95 \%$ Tukey's HSD confidence intervals for MCEDA and the compared algorithms under $\rho=1,5,10$ are shown in Fig. 11. These confidence intervals in Fig. 11 suggest that MCEDA is statistically better than the other algorithms regardless of the different values of $\rho$.
![img-11.jpeg](img-11.jpeg)

Fig. 11. Means plots with $95 \%$ Tukey's HSD confidence intervals for MCEDA and the compared algorithms under $\rho=1,5,10$.

The Gantt chart of the obtained best solution for the large-scaled instance $1,100,10,4,30,5$ is depicted in Fig. 12. As can be seen from Fig. 12, the assembly operation of the first product is performed as early as possible and the assembly operations of all products on the assembly machine $M_{A}$ are seamlessly connected, which manifests that MCEDA can obtain high-quality solutions. Moreover, MCEDA has updated the best-known solutions of 91 small-scaled instances and 123 large-scaled instances (see Appendix A). Based on the test results of Sections 4.4 and 4.5 , it can be concluded that the proposed MCEDA is a new state-of-theart algorithm for tackling the DAPFSP.

## 5. Conclusions

This paper proposed a novel matrix-cube-based estimation of distribution algorithm (MCEDA) to address the DAPFSP with makespan criterion. The considered problem has many real-practice applications in modern industries. To the best of our knowledge, this is the first work on the application of multidimensional EDA to such an important problem. Firstly, a matrix cube was designed to reserve the valuable information of excellent individuals. Each two-dimensional matrix in it was utilized to record the ordinal numbers of jobs and the corresponding blocks at each position, and the hierarchical structure of it was used to save the whole order information. This design is more reasonable than those in the existing literature. Secondly, a probabilistic model based on the designed matrix cube and a special sampling method were proposed to generate new individuals and guide global search to promising regions. Thirdly, a fast VND constructed with twelve neighborhood operators and two speed-up strategies was devised to perform rich and efficient

Table 12
Comparison results of MCEDA and eleven state-of-the-art meta-heuristics on large-scaled instances ( $n \times(m / 2) \times 1$ milliseconds).

Table 13
Comparison results of MCEDA and eleven state-of-the-art meta-heuristics on large-scaled instances ( $n \times(m / 2) \times 5$ milliseconds).

Table 14
Comparison results of MCEDA and eleven state-of-the-art meta-heuristics on large-scaled instances ( $n \times(m / 2) \times 10$ milliseconds).

![img-12.jpeg](img-12.jpeg)

Fig. 12. Gantt chart of the new best solution obtained by MCEDA for instance $1,100,10,4,30,6$.
exploitation from the promising regions found by global search, which can improve the performance of MCEDA. Finally, computational comparisons and numerical results on 1710 benchmark instances demonstrated that our proposed MCEDA not only statistically outperforms the existing state-of-the-art algorithms but also can improve the current best
solutions of 91 small-scaled instances and 123 large-scaled instances. Our future research is to improve the global search ability of MCEDA by considering additional machine learning schemes and to apply MCEDA to solve the energy-saving assembly scheduling problem and other kinds of scheduling problems.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## CRediT authorship contribution statement

Bin Qian: Funding acquisition, Investigation, Writing - review \& editing, Writing - original draft, Supervision, Project administration. Rong Hu: Investigation, Writing - review \& editing, Supervision, Project administration. Huai-Ping Jin: Writing - review \& editing. Ling Wang: Supervision, Project administration.

## Acknowledgment

This research is partially supported by National Natural Science Foundation of China (51665025, 61963022, 60904081), and National Natural Science Fund for Distinguished Young Scholars of China (61525304). In addition, the authors would also like to thank the anonymous reviewers for their insightful comments and suggestions that substantially improved the quality of the paper.

## Appendix A

The new best-known solutions obtained by the MCEDA for two sets of benchmark instances are as follows.

Table A1 and A2.

Table A1
New best solutions for 91 small-scaled instances.

Table A2
New best solutions for 123 large-scaled instances.