# An elitist nondominated sorting hybrid algorithm for multi-objective flexible job-shop scheduling problem with sequence-dependent 

setups

Z.C. Li ${ }^{\mathrm{a}}$, B. Qian ${ }^{\mathrm{a}, *}$, R. Hu ${ }^{\mathrm{a}}$, L.L. Chang ${ }^{\mathrm{b}}$, J.B. Yang ${ }^{\mathrm{c}}$<br>${ }^{a}$ School of Information Engineering and Automation, Kunming University of Science and Technology, Kunming 650500, China<br>${ }^{\mathrm{b}}$ High-Tech Institute of Xi'an, Xi'an 710025, China<br>${ }^{\mathrm{c}}$ Manchester Business School, University of Manchester, Manchester, M15 6PB, UK

## A R T I C L E I N F O

Article history:
Received 28 June 2018
Received in revised form 31 December 2018
Accepted 21 February 2019
Available online 2 March 2019

Keywords:
Multi-objective optimization
Nondominated sorting method
Estimation of distribution algorithm
Flexible job shop scheduling problem
Sequence-dependent setups


#### Abstract

In this paper, an elitist nondominated sorting hybrid algorithm, namely ENSHA, is proposed to solve the multi-objective flexible job-shop scheduling problem (MOFJSSP) with sequence-dependent setup times/costs (MOFJSSP_SDST/C). The objectives to be minimized are the maximal completion time (i.e., makespan) and the total setup costs (TSC). The makespan is an efficiency-focused objective whereas the TSC is an economic focused one. Existing works mainly consider the efficiency-focused multiple criteria. The main highlights of this paper are threefold, i.e., the operation-based sequence model, the problem-dependent job assignment rules and the novel evolutionary framework of ENSHA. For the operation-based sequence model, this is the first time that the sequence model of MOFJSSPs has been proposed and the TSC has been treated as an independent objective in MOFJSSPs. For the job assignment rules, the solution representation is first proposed, and then three job assignment rules are specifically designed to decode solutions or sequences into feasible scheduling schemes. For the novel evolutionary framework, it works with two populations, i.e., the main population (MP) and the auxiliary population (AP). First, ENSHA adopts the elitist nondominated sorting method for evolving MP to maintain high-quality solutions regarding both the convergence and diversity. Next, a machine learning strategy based on the estimation of distribution algorithm (EDA) is proposed to learn the valuable information from nondominated solutions in MP for building a probabilistic model. This model is then used to generate the offspring of AP. Furthermore, a simple yet effective cooperation-based refinement mechanism is raised to combine MP and AP, so as to generate MP of the next generation. Finally, experimental results on 39 benchmark instances and a real-life case study demonstrate the effectiveness and application values of the proposed ENSHA.


(c) 2019 Elsevier B.V. All rights reserved.

## 1. Introduction

In modern competitive and global markets, the production scheduling plays a vital role in the manufacturing and flow industry systems. The flexible job-shop scheduling problem (FJSSP), which divides each job into several operations, is concerned with arranging multiple operations to suitable parallel machines (assignment problem) and determining the sequences of operations on all machines (sequencing problem). FJSSP is different from the classical job shop scheduling problem (JSSP) in the sense that its operations are allowed to be assigned to any machine of a given set instead of a prescribed one. Therefore, FJSSP is a generalized version of the conventional JSSP. Since JSSP is already known to

[^0]be NP-hard [1-3], it can be naturally concluded that FJSSP belongs to NP-hard.

In real-life applications, managers always desire to enhance the overall performance of the production systems, such that the philosophy of the multi-objective optimization has been extensively advocated in many practical areas. In this trend, several seminal works on multi-objective flexible manufacturing system (MOFMS) [4-6] are pioneered. Afterwards, its simplified and general form, i.e., the multi-objective FJSSP (MOFJSSP), has gradually gained much attention in the field of production scheduling [712]. As we know, success in practical production systems depends largely on the ability to reasonably balance the efficiency and economic profit, which in turn requires managers to adjust their ideas in routine decision making. These facts motivate us to consider the MOFJSSP where the efficient and economic criteria are optimized simultaneously.


[^0]:    * Corresponding author.

    E-mail address: bin.qian@vip.163.com (B. Qian).

Table 1
Example of processing constraints ${ }^{a}$.
${ }^{a} \mathrm{~A}$ symbol "-"denotes that the operation is not required for the corresponding product.

Setups are another important feature of MOFJSSP and have aroused wide concerns of researchers [13-18]. In practical factories, frequent adjustments of processing environments and parameters are usually unavoidable which may result in many setups, especially for chemical and pharmaceutical plants. For example, in the process of batch productions, setups are often needed to clean the device (machine) or change its temperature to a certain range for two different and consecutive products. Setups are of two types: sequence-independent setups and sequence-dependent setups. The latter one is of absolute necessity for both continuous and discrete production processes. This is because, in most cases, setups are not only determined by the job itself but also strongly depend on its predecessor on the same machine [15]. Generally, there are two primary kinds of sequence-dependent setups, i.e., sequence-dependent setup times (SDSTs) and sequence-dependent setup costs (SDSCs). SDSTs represent the time used for setup, which directly affects the efficiency-focused objective. SDSCs measure the material and labor costs as well as the production loss of setup, which belongs to the economic focused objective. Very often, there is no positive correlation between SDSTs and SDSCs. Smaller SDSTs may correspond to larger SDSCs due to the potential conflict between them. In many cases, undesirable SDSCs appear to be remarkable for the overall profits of enterprises. Thus, it is meaningful to consider both SDSTs and SDSCs in the production scheduling problems.

In view of the above considerations, this paper deals with the MOFJSSP considering both SDSTs and SDSCs (MOFJSSP_SDST/C), in which the objectives are to minimize the maximum completion time (makespan) and the total setup costs (TSC). The former objective usually reflects the efficiency rates of machines, and the latter is associated with the economic costs of setups. Obviously, MOFJSSP_SDST/C is quite different from the other existing MOFJSSPs in that it treats the TSC as a separate objective. Thereby, the decision making of MOFJSSP_SDST/C is related to more difficult scenarios compared with the existing MOFJSSPs. The considered MOFJSSP_SDST/C arises from many industrial applications. Next, we will share a real word implementation that can be modeled by MOFJSSP_SDST/C.

In recent years, the authors visited several real-life factories and observed that the basic model of MOFJSSP_SDST/C has been widely adopted in production management practices. For instance, the crystallization process (CP) for crude materials is a very common chemical process in pharmaceutical industry. When selecting machines for processing certain products (crude materials), it not only depends on the capacity constraints of machines, but also relies on the physicochemical properties of these products. Each product may have multiple operations. Each operation can be processed by using any machine of the given set that satisfies the processing constraints. Hence, there exists a typical partial flexibility feature in CP. The processing time of a product is determined not only by the current operation that belongs to, but also by the assigned machine of the operation. As shown in Fig. 1, we illustrate a feasible scheduling scheme for the CP while considering the processing constraints listed in Table 1.

Apparently, some products are produced through a single CP (e.g., Product 2 in Fig. 1), and the others are produced through repetitive CPs (e.g., Products 1, 3, and 4 in Fig. 1). To prevent cross-contamination among different materials, when one operation is completed on one machine, it should take certain setup time to clean or adjust such machine before performing successive operations. The setup time depends on both the current and the immediately performing operations on each machine. Meanwhile, the industrial wastes or the losses of materials on each machine are inevitable. For example, in Fig. 2, the cleaning and adjustment of a machine should be performed before executing the next operation on the machine, so the setup cost of each operation on this machine is not only proportional to the height of fluid level (i.e., $h$ ), but also depends on the corresponding materials of the current operation and its successive one. In this paper, SDSTs as well as SDSCs among operations that belong to the same product are set to 0 , which is also one of the basic assumptions in production scheduling problems [13-18].

To date, many efforts have been devoted to addressing MOFJSSP with different optimization objectives, such as the makespan, total workload (TW), total workload of critical machine (TWCM), and maximal workload (MW). Due to the NPhardness of MOFJSSP, some solution methods based on evolutionary algorithms (EAs) have been widely adopted. Shahsavari-Poura and Ghasemishabankarehb [7] reported a hybrid evolutionary algorithm that efficiently combined GA and simulated annealing (SA) for MOFJSSP with the objective to minimize the makespan, TWCM and TW. Besides, the other EA-based approaches are also developed to solve MOFJSSP, including artificial bee colony algorithm (ABC) [8], estimation of distribution algorithm (EDA) [9], harmony search (HS) [10], and particle swarm optimization (PSO) [11,12]. Nevertheless, the previous works primarily consider the efficiency-oriented criteria, which may be not suitable for the case of MOFJSSP_SDST/C. To the best of our knowledge, studies that simultaneously consider SDSTs and SDSCs are still relatively unexplored. Therefore, it is both meaningful and practical to design an effective solution method for MOFJSSP_SDST/C.

Solution methods based on the multi-objective evolutionary algorithm (MOEA) have become one of the most important techniques for solving MOFJSSP. On the one hand, the parallel search framework of MOEA can obtain a number of nondominated solutions in reasonable computational time. On the other hand, the evolutionary model of MOEA is helpful in maintaining the diversity of population as well as avoiding undesirable local optima. Therefore, it is highly advisable to utilize MOEAs for solving MOFJSSP_SDST/C. Based on fitness assignment strategies, MOEA can be divided into two categories: dominance-based MOEA and decomposition-based MOEA. Among the state-of-theart MOEAs, strength Pareto evolutionary algorithm II (SPEAII) [19] and non-dominated sorting genetic algorithm II (NSGAII) [20] belong to the dominance-based MOEA, whereas MOEA based on decomposition (MOEA(D) [21] and multiple-objective genetic local search (MOGLS) [22] are classified as the decomposition-based MOEA. According to our previous tests, these state-of-the-art algorithms have strong ability to explore the solution space of multi-objective problems and can obtain very satisfactory solutions for MOFJSSP_SDST/C. Moreover, as pointed out by Cai et al. [23], the elitist nondominated sorting method can be used to maintain better solutions with good diversity. Meanwhile, they suggested that utilizing the machine learning approaches to extract information from the previous search is useful for guiding the search to promising regions. These facts motivate us to develop an elitist nondominated sorting hybrid algorithm (ENSHA) that would be more effective than the above state-of-the-art algorithms for MOFJSSP_SDST/C.

The main features of ENSHA lie in two aspects: the problemdependent job assignment rules and the novel evolutionary

![img-0.jpeg](img-0.jpeg)

Fig. 1. Feasible scheduling scheme for the CP.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Illustration of cleaning the machine.
framework of ENSHA. As for job assignment rules, after giving the operation-based solution representation, three specific job assignment rules are proposed to arrange operations in solutions or sequences to suitable parallel machines, which can locally optimize given sequences found by ENSHA. Then, they are embedded into ENSHA as decoding schemes. As for ENSHA, it uses an improved bi-population evolutionary model which consists of a main population (MP) as well as an auxiliary population (AP). In ENSHA, the genetic operators with the elitist nondominated sorting method are adopted for evolving MP with the aim to keep solutions with better convergence and diversity. Moreover, a machine learning mechanism based on the estimation of distribution algorithm (EDA) is used to build a probabilistic model for generating new individuals in AP. Furthermore, an effective cooperation-based refinement strategy is designed to combine

MP and AP to generate MP of the new generation. In such a way, MP and AP can supplement and promote each other during the search process. The novelties of this work are summarized in Table 2.

The remaining contents of the paper are organized as follows. In the next section, the operation-based sequence model of MOFJSSP_SDST/C is formulated. In Section 3, the solution representation and three problem-dependent job assignment rules are introduced. In Section 4, ENSHA is proposed and described in detail. In Section 5, experimental results and comparisons are presented and discussed. Finally, we end the paper with some conclusions and future work in Section 6.

Table 2

![img-2.jpeg](img-2.jpeg)

Fig. 3. Illustration of solution representation.

## 2. MOFJSSP_SDST/C

The researches on the evolutionary algorithms for the flow shop scheduling problems always give the corresponding jobbased or operation-based sequence models, which consist of several equations to calculate the start or complete time of each job or operation on each machine. The optimization variables of a sequence model are represented as a job or operation sequence. However, due to the complexity of representation, the studies on the job shop scheduling problems and their variants (e.g., FJSSPs and MOFJSSPs) seldom propose the sequence models. For example, many studies on the evolutionary algorithms for the MOFJSSPs like to provide mixed-integer or nonlinear mathematical models [7], [8], [9], [10], [12], [32], but in fact the individual or solution in each evolutionary algorithm corresponds to the variables of the unprovided sequence model, rather than the decision variables of the established mathematical model. That is, evolutionary algorithms actually optimize the variables of the sequence models and they are independent of the mathematical models. This phenomenon is easy to confuse new researchers. Thus, this section not only gives the concept description of MOFJSSP_SDST/C but also proposes an operation-based sequence model of it.

The MOFJSSP_SDST/C can be described as follows. There are $n$ products (or jobs), $m$ machines, and each product $i(i=1, \ldots, n)$ needs opr $_{i}$ operations to complete the processing. The scheduling environment is partially flexible, so that the opr, operations of product $i$ can only be processed by certain machines that satisfy the processing constraints. Different operations of the same product must satisfy the sequencing priority. That is, only if a previous operation is completed can the current operation be processed. The processing time of each operation depends on the assigned machine. At any time, preemption is forbidden and each machine can process at most one job at the same time. There exist SDSTs and SDSCs between the completion time of one operation and the start time of another consecutive operation on each machine.

When two operations belong to the same product, the SDSTs and SDSCs between them are set to 0 . The problem is to find the sequence of products on all machines, so as to minimize the given criteria (i.e., makespan and TSC). Next, we propose the operationbased sequence model of MOFJSSP_SDST/C based on the real-life CP mentioned in Section 1.

Let $T O=\sum_{i=1}^{n} \operatorname{opr}_{i}$ denote the total number of operations, $\pi=\left\{\pi_{1}, \ldots, \pi_{k}, \ldots, \pi_{T O}\right\}\left\{\pi_{k} \in\{1, \ldots, n\}\right.$ for $\left.k=1, \ldots, T O\right)$ the operation-based sequence or schedule of the products (the operations in $\pi$ are assigned to different machines from left to right by using the proposed job assignment rules in Section 3.2), $T_{j}$ $\left(T O=\sum_{j=1}^{m} T_{j}\right)$ the total number of the operations performed on machine $j, \pi^{T(j)}=\left\{\pi_{1}^{T(j)}, \ldots, \pi_{l}^{T(j)}, \ldots, \pi_{T_{j}}^{T(j)}\right\}$ the sequence of the operations performed on the $j$ th machine $\left(\pi_{i}^{T(j)} \in\{1, \ldots, n\}\right.$ for $\left.l=1, \ldots, T_{j}\right), P\left(\pi_{i}^{T(j)}\right)$ the processing time of operation $\pi_{i}^{T(j)}(l=$ $0, \ldots, T_{j}, P\left(\pi_{0}^{T(j)}\right)=0), S_{t}\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right)$ the setup time between $\pi_{l-1}^{T(j)}$ and $\pi_{l}^{T(j)} .\left(S_{t}\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right)=0\right.$ when $\left.l=1, S_{t}\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right)=\right)$ 0 when $\pi_{l-1}^{T(j)}=\pi_{l}^{T(j)}$ for $\left.l=2, \ldots, T_{j}\right), \operatorname{Start}\left(\pi_{l}^{T(j)}\right)$ the start time of $\pi_{l}^{T(j)}\left(l=0, \ldots, T_{j}, \operatorname{Start}\left(\pi_{0}^{T(j)}\right)=0\right), \operatorname{prod}\left(\pi_{l}^{T(j)}\right)$ the product owning $\pi_{l}^{T(j)}$, pre_ $m\left(\pi_{l}^{T(j)}\right)$ the machine that processes the operation of prod $\left(\pi_{l}^{T(j)}\right)$ right before machine $j\left(l=1, \ldots, T_{j}\right.$, $\left.\operatorname{pre} \_m\left(\pi_{l}^{T(j)}\right)=0\right.$ when machine $j$ is the first machine to process $\operatorname{prod}\left(\pi_{l}^{T(j)}\right)$ ), pre_ $k\left(\pi_{l}^{T(j)}\right)$ the position of $\pi_{l}^{T(j)}$ in $\pi^{T(\text {pre_m } \left(\pi_{l}^{T(j)}\right.}) \text { ) from }$ its left side $\left(l=1, \ldots, T_{j}\right.$, pre_ $k\left(\pi_{l}^{T(j)}\right)=0$ when machine $j$ is the first machine to process $\left.\operatorname{prod}\left(\pi_{l}^{T(j)}\right)\right)$. Then, the makespan can be calculated as follows:

$$
\begin{aligned}
C_{\max }(\pi)= & \max \left\{\operatorname{Start}\left(\pi_{T_{1}}^{T(1)}\right)+P\left(\pi_{T_{1}}^{T(1)}\right), \operatorname{Start}\left(\pi_{T_{2}}^{T(2)}\right)\right. \\
& +P\left(\pi_{T_{2}}^{T(2)}\right), \ldots \\
& \left.\operatorname{Start}\left(\pi_{T_{m}}^{T(m)}\right)+P\left(\pi_{T_{m}}^{T(m)}\right)\right\} \\
\operatorname{Start}\left(\pi_{l}^{T(j)}\right)= & \operatorname{Start}\left(\pi_{l-1}^{T(j)}\right)+P\left(\pi_{l-1}^{T(j)}\right)+S_{t}\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right) \\
& \left.\operatorname{pre} \_k\left(\pi_{l}^{T(j)}\right)=0, l=1, \ldots, T_{j}, j=1, \ldots, m\right\} \\
\operatorname{Start}\left(\pi_{l}^{T(j)}\right)= & \max \left\{\operatorname{Start}\left(\pi_{l-1}^{T(j)}\right)+P\left(\pi_{l-1}^{T(j)}\right)+S_{t}\left(\pi_{l}^{T(j)}, \pi_{l}^{T(j)}\right)\right. \\
& \left.\operatorname{Start}\left(\pi_{\text {pre_ } k\left(\pi_{l}^{T(j)}\right)}^{T(\text {pre_m } \left(\pi_{l}^{T(j)}\right.}\right)+P\left(\pi_{\text {pre_ } k\left(\pi_{l}^{T(j)}\right.}^{T(\text {pre_m } \left.\pi_{l}^{T(j)}\right.}\right)\right\} \\
& \text { pre_ } k\left(\pi_{l}^{T(j)}\right) \neq 0, l=1, \ldots, T_{j}, j=1, \ldots, m
\end{aligned}
$$

Let $S_{c}\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right)$ denote the setup cost between $\pi_{l-1}^{T(j)}$ and $\pi_{l}^{T(j)}, h\left(\pi_{l}^{T(j)}\right)$ the average height of fluid level in terms of processing prod $\left(\pi_{l}^{T(j)}\right)$ on all satisfied machines, var_c $\left(h\left(\pi_{l}^{T(j)}\right)\right)$ the variable cost of waste disposal and product loss per unit $h\left(\pi_{l}^{T(j)}\right)$

![img-3.jpeg](img-3.jpeg)

Fig. 4. Gantt charts of $\pi=[2,4,3,1,4,3,4,4,1,3]$ using proposed job assignment rules.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Illustration of adopted crossover operator.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Illustration of adopted mutation operator.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Illustration of nondominated sorting method.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Illustration of crowding distance.
$\left(\right.$ var_ $c\left(h\left(\pi_{l}^{T(j)}\right)\right)=0$ when $l=0$ or $T_{j}$ ), fix_c $\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right)$ the fixed cost of adjusting machine $j$ and performing the chemical wash between $\pi_{l-1}^{T(j)}$ and $\pi_{l}^{T(j)}\left(f i x_{-} c\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right)=0\right.$ when $l=1$, and $f i x_{-} c\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right)=0$ when $\pi_{l-1}^{T(j)}=\pi_{l}^{T(j)}$ for $l=2, \ldots, T_{j}$, and $w\left(\operatorname{prod}\left(\pi_{l}^{T(j)}\right)\right)$ the cost coefficient of var_c $\left(h\left(\pi_{l}^{T(j)}\right)\right)$. The TSC can be calculated as follow:

$$
\begin{aligned}
& \text { TSC }=\sum_{j=1}^{m} \sum_{l=1}^{T_{j}} S_{c}\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right) \\
& S_{c}\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right)=w\left(\operatorname{prod}\left(\pi_{l-1}^{T(j)} i\right) \cdot \operatorname{var}_{-} c\left(h\left(\pi_{l-1}^{T(j)} i\right)\right.\right. \\
& \left.\left.+f i x_{-} c\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right)\right)
\end{aligned}
$$

where $S_{c}\left(\pi_{l-1}^{T(j)}, \pi_{l}^{T(j)}\right)=0$ when $l=1$ and $\pi_{l-1}^{T(j)}=\pi_{l}^{T(j)}$ for $l=2, \ldots, T_{j}$. For MOFJSSP_SDST/C, the makespan and TSC need to be considered simultaneously, however, they are often conflicting with each other. That is, an improvement in one objective may worsen another. Since there is usually no such a solution that is the best to all objectives, it is required to find a set of nondominated solutions in decision making [36,37]. When each operation of $\pi$ has been assigned to one machine, the computational complexity (CC) of calculating $C_{\max }(\pi)$ and TSC is $O(2 * T O)$, where 2 is the number of objectives.

Unlike the mathematical models of production scheduling problems, the sequence models of these problems have no explicitly expressed constraints. As for the sequence model of MOFJSSP_SDST/C, the operational constraints are implicitly included in its equations and an operation assignment table. These constraints can be divided into two groups. The first group contains the general constraints for both the JSSPs and the FJSSPs. These general constraints are included in the Eqs. (2) and (3), which determine that each operation $\pi_{l}^{T(j)}$ can only be executed after the operations $\pi_{l-1}^{T(j)}$ and $\pi_{\text {pre }, k\left(\pi_{l}^{T(j)}\right)}^{T(j)}$ are completed. The second group contains the specific processing constraints for the FJSSPs. These specific constraints are usually given in an operation assignment table (see Table 1), which requires that each operation must be executed on one of several specified machines. The difference between JSSPs and FJSSPs is that the latter one needs to assign each operation to a machine (selected from the set of specified machines in Table 1) before calculating the start times of all the operations. By adding the appropriate processing constraints, the sequence model can represent not only the common FJSSPs but also the reentrant FJSSPs (see Table 1), which widely exist in process industries and microelectronic industries. Hence, the specific processing constraints can extend the application scope of the model.

Compared with the mathematical model, the constraints of the sequence model are easy to handle. To the operation-based sequence or solution $\pi\left(\pi=\left[\pi_{1}, \ldots, \pi_{k}, \ldots, \pi_{T 0}\right]\right)$, the new solution or child is still feasible as long as the search operators (e.g., crossover and mutation) do not change the total number of each job's operations in the new solution. In the following proposed ENSHA, the adopted crossover and mutation can keep the total number of each job's operations unchangeable (see Section 4.1). When an operation-based sequence $\pi^{T(j)}(j=1, \ldots, m)$ on each machine is determined by applying a decoding scheme (i.e., a job assignment rule) to $\pi$, the start time of each operation is calculated with the equations of the sequence model and no constraints are violated. This means that any solution $\pi$ generated in ENSHA is feasible. In fact, almost all the existing evolutionary scheduling algorithms choose to optimize the variables of the sequence model, since the researchers adopting the sequence model can focus on the algorithm design rather than the constraint handling.

## 3. Problem-dependent job assignment rules

### 3.1. Solution representation

Based on MOFJSSP_SDST/C's features, the operation-based encoding scheme is adopted. For example, a sequence $\pi=\left[\pi_{1}, \ldots\right.$, $\pi_{T 0=10}]=[2,4,3,1,4,3,4,4,1,3]$ is a solution or individual of ENSHA, when the problem size $n \times m$ and $\left[\right.$ opr $\left._{1}, \ldots, o p r_{4}\right]$ are set to $4 \times 4$ and $[2,1,3,4]$. As shown in Fig. 3, $\pi$ denotes that the unique operation of job 2 is firstly assigned to a machine based on certain job assignment rules, and then the first operation of job 4 is assigned, and so on. Apparently, the objectives of individuals are determined by both the sequence and the job assignment

![img-8.jpeg](img-8.jpeg)

Fig. 9. Histograms of ENSHAs with different job assignment rules.
rule. Arguably, a suitable assignment rule may result in highquality scheduling scheme. Therefore, we will put forward three problem-dependent job assignment rules in Section 3.2. And the Gantt charts for the solution $\{2,4,3,1,4,3,4,4,1,3\}$ in Fig. 3 are then given in Fig. 4, in terms of the proposed three job assignment rules.

### 3.2. Proposed job assignment rules

As mentioned in Section 3.1, ENSHAS solution should be converted into the feasible scheduling scheme by using job assignment rules. Nevertheless, due to the intractable partial flexibility and sequence-dependent setups in MOFJSSP_SDST/C, it may be a challenge to design effective decoding rules for such a problem. Here, the decoding rule is referred to as the job assignment rule, which is important for evaluating the objectives and improving the search quality. In existing papers, traditional job assignment rules including RANDOM [33] (select an operation at random), SPT [33-35] (shortest processing time), EST (earliest start time) [34,35] and ECT [34,35] (earliest completion time) are widely used for various kinds of scheduling problems. However, for MOFJSSP_SDST/C, the makespan and TSC are considered simultaneously, so the traditional ones may lead to poor performances. In this work, three new job assignment rules are presented to decode the solution or sequence.

For an operation $\pi_{k}(k=1, \ldots, T O)$ of solution $\pi$, the set $A V A\left(\pi_{k}\right)=\left\{j_{1}, \ldots, j_{l} \ldots, j_{\left(\pi_{k}\right)}\right\}\left(j_{l} \in\{1, \ldots, m\}\right.$ for $l=$ $1, \ldots, l\left(\pi_{k}\right)$ ), which is constituted by $l\left(\pi_{k}\right)$ machines that satisfy the processing constraints for $\pi_{k}$, needs to be identified first. Thereafter, the sub-criteria of completing time ( $C T$ ) and setup cost (SC) associated with $\pi_{k}$ on each machine of $A V A\left(\pi_{k}\right)$ can be calculated. Let $C T_{\pi_{k}}=\left\{C T_{\pi_{k}, j_{1}}, \ldots, C T_{\pi_{k}, j_{\left(\pi_{k}\right)}}\right\}$ and $S C_{\pi_{k}}=$
$\left(S C_{\pi_{k}, j_{1}}, \ldots, S C_{\pi_{k}, j_{\left(\pi_{k}\right)}}\right)$ denote the obtained sub-criteria of $C T$ s and SCs respectively. The principles of proposed Rules 1 to 3 are given as follows:

Rule 1 (CT + SC): Select one machine $j^{*} \in A V A\left(\pi_{k}\right)$ for processing $\pi_{k}$ that satisfies $\neg \exists j_{l} \in A V A\left(\pi_{k}\right):\left(C T_{\pi_{k}, l_{l}}+S C_{\pi_{k}, l_{l}}\right)<$ $\left(C T_{\pi_{k}, j^{*}}+S C_{\pi_{k}, j^{*}}\right), l=1, \ldots, l\left(\pi_{k}\right)$;

Rule 2 (CT * SC): Select one machine $j^{*} \in A V A\left(\pi_{k}\right)$ for processing $\pi_{k}$ that satisfies $\neg \exists j_{l} \in A V A\left(\pi_{k}\right):\left(C T_{\pi_{k}, l_{l}} * S C_{\pi_{k}, l_{l}}\right)<$ $\left(C T_{\pi_{k}, j^{*}} * S C_{\pi_{k}, j^{*}}\right), l=1, \ldots, l\left(\pi_{k}\right)$;

Rule 3 (DOMINANCE): Select one machine $j^{*} \in A V A\left(\pi_{k}\right)$ for processing $\pi_{k}$ that satisfies $\neg \exists j_{l} \in A V A\left(\pi_{k}\right):\left(\left(C T_{\pi_{k}, l_{l}}<C T_{\pi_{k}, j^{*}}\right) \wedge\right.$ $\left.\left.\left\langle S C_{\pi_{k}, l_{l}}<S C_{\pi_{k}, j^{*}}\right)\right\rangle \vee$
$\left(\left(C T_{\pi_{k}, l_{l}}=C T_{\pi_{k}, j^{*}}\right) \wedge\left(S C_{\pi_{k}, l_{l}}<S C_{\pi_{k}, j^{*}}\right)\right) \vee$
$\left(\left(C T_{\pi_{k}, l_{l}}<C T_{\pi_{k}, j^{*}}\right) \wedge\left(S C_{\pi_{k}, l_{l}}=S C_{\pi_{k}, j^{*}}\right)\right), l=1, \ldots, l\left(\pi_{k}\right)$.
Rules 1 to 3 are all in pursuit of finding a tradeoff between $C T_{\pi_{k}}$ and $S C_{\pi_{k}}$ when selecting machines, since these two subcriteria may locally influence the objectives of MOFJSSP_SDST/C. The performance of these rules will be tested in Section 5, due to the complexity of MOFJSSP_SDST/C. The pseudo code of decoding a solution $\pi=\left[\pi_{1}, \ldots, \pi_{k}, \ldots, \pi_{T O}\right]$ by using any one of the proposed rules is given in Algorithm 1. Since the maximum number of machines that can process each operation $\pi_{k}$ is $m$, the CC of calculating $C_{\max }(\pi)$ and TSC with one proposed job assignment rule is $O(2 * m * T O)$, where 2 is the number of objectives. That is, the CC of Algorithm 1 is $O(2 * m * T O)$.

Here, we illustrate the proposed assignment rules through the example mentioned in Fig. 3, where the operation processing constraints, processing times, and setup times/costs are listed in Tables 1, 3, and 4, respectively. For example, by using $C S^{*} T C$, we can get $T_{1}=4, T_{2}=4, T_{3}=2, \pi^{T(1)}=[4,4,4,3], \pi^{T(2)}=$ $\{2,3,3,1\}$, and $\pi^{T(3)}=[1,4]$. The Gantt charts of $\pi$, in terms of

![img-9.jpeg](img-9.jpeg)
a) $\mathrm{CT}+\mathrm{SC}$
![img-10.jpeg](img-10.jpeg)
b) DOMINANCE
![img-11.jpeg](img-11.jpeg)
c) $\mathrm{CT}^{3} \cdot \mathrm{SC}$
![img-12.jpeg](img-12.jpeg)
d) Overall trend

Fig. 10. $95 \%$ CI's and overall trend for proposed assignment rules.
![img-13.jpeg](img-13.jpeg)
![img-14.jpeg](img-14.jpeg)
![img-15.jpeg](img-15.jpeg)

Fig. 11. Level trends of each parameter.
the three assignment rules, are illustrated in Fig. 4, in which the objectives ( $C_{\max }, T S C$ ) are $(73,5.3),(85,4.3)$ and $(85,4.3)$.

## 4. ENSHA for MOFJSSP_SDST/C

In this section, we will detail the proposed ENSHA for MHPMSP_MOSST/C after explaining the genetic operators, the elitist nondominated sorting method, the EDA-based machine learning mechanism, and the cooperation-based refinement strategy.

### 4.1. Genetic operators

ENSHA uses a novel bi-population evolutionary framework to guide the search to the promising regions in solution space, so it needs a suitable crossover to execute search nearby these regions for finding better neighbors. A two-point crossover method known as Partial-mapped crossover (PMX) [35] has been widely used in the fields of combinatorial optimization problems [3841]. PMX is good at preserving long subsequences (i.e., building blocks) of parents [42], which means it can effectively search the

![img-16.jpeg](img-16.jpeg)

Fig. 12. Average CPU time of NSGAII, ENSHA_V and ENSHA. (ENSHA is highlighted in shadow).
![img-17.jpeg](img-17.jpeg)

Fig. 13. Box plots of NSGAII, ENSHA_V and ENSHA for 39 instances (mean values of $\gamma$ ).

Table 3
Setup times/costs.
Table 4
Processing times ${ }^{a}$.
${ }^{a}$ A symbol "-"denotes that the operation is not required for the corresponding product.
regions nearby the parents. Moreover, due to its simple repairing scheme of infeasibility, PMX can quickly search new regions (i.e., generating children) without increasing computation complexity. Hence, PMX is adopted in ENSHA. Let $\pi^{p 1}$ and $\pi^{p 2}$ denote the parent individuals selected from the current population with crossover probability $P c$. To ensure the feasibility of newly recombined children, we need to distinguish operations of the same product (or job) in an individual. To do so, we label all operations of the same product in $\pi^{p 1}$ and $\pi^{p 2}$ with symbols "a, b, c, ..." according to their order from left to right. Thereby, the labeled $\boldsymbol{\beta}^{p 1}$
and $\boldsymbol{\beta}^{p 2}$ of $\pi^{p 1}$ and $\pi^{p 2}$ can be obtained. Note that the labeled $\boldsymbol{\beta}^{p 1}$ and $\boldsymbol{\beta}^{p 2}$ are only used to distinguish the operations that belong to the same product.

As shown in Fig. 5, for $\pi^{p 1}=[2,4,3,1,4,3,4,4,1,3]$ and $\pi^{p 2}=[1,3,4,1,4,3,4,2,3,4]$, we can get $\boldsymbol{\beta}^{p 1}=[2-a, 4-a$, $3-a, 1-a, 4-b, 3-b, 4-c, 4-d, 1-b, 3-c]$ and $\boldsymbol{\beta}^{p 2}=[1-a, 3-a, 4-a, 1-b$, $4-b, 3-b, 4-c, 2-a, 3-c, 4-d]$. Thereafter, two different genes $r 1$ and $r 2(r 1<r 2)$ are randomly selected, and the elements in $\boldsymbol{\beta}^{p 2}$ that belong to the subset $\left\{\beta_{r 1}^{p 1}, \ldots, \beta_{r 2}^{p 1}\right\}$ should be locked (marked by crosses) to avoid infeasibility. Then, the subsequence $\left[\pi_{r 1}^{p 1}, \ldots, \pi_{r 2}^{p 1}\right]$ of $\boldsymbol{\beta}^{p 1}$ is directly copied to the corresponding positions of the child individual, and in turn, the active operations of $\boldsymbol{\beta}^{p 2}$ (i.e., $3,4,1,2$ and 3 ) are copied to the empty positions of the child from left to right.

Besides, a simple Interchange-based mutation operator is applied in ENSHA, so as to perform perturbations for the offspring and avoid trapping into local optima in the search process. After performing the crossover operation, an individual is selected (i.e., $\pi^{x}$ ) according to the mutation probability Pm to execute mutation operator. The mutation operator is illustrated in Fig. 6. From Figs. 5 and 6, it can be seen that both the PMX and the Interchange-based mutation keep the total number of each job's operations unchangeable. Therefore, the adopted crossover and mutation can avoid the infeasibility of solutions.

### 4.2. Elitist nondominated sorting method

In ENSHA, MP and the cooperation-based refinement strategy are all related to the elitist nondominated sorting method. Next, we will introduce the elitist nondominated sorting method, including the nondominated sorting and the crowding distance assignment.

![img-18.jpeg](img-18.jpeg)

Fig. 14. Box plots of NSGAII, ENSHA_V and ENSHA.
![img-19.jpeg](img-19.jpeg)

Fig. 15. Average CPU time of MOPSO, MOEA/D, MOGLS, SPEAII and ENSHA. (ENSHA is highlighted in shadow.)

![img-20.jpeg](img-20.jpeg)

Fig. 16. Box plots of MOPSO, MOEA/D, MOGLS, SPEAII and ENSHA (mean values of $\gamma$ ).

### 4.2.1. Nondominated sorting

Let $P S$ be the population size of MP, $\pi_{s}^{\text {MP }}$ the $i$ th individual of MP at generation gen, $\pi^{\text {MP }}(g e n)=\left\{\pi_{1}^{\text {MP }}, \ldots, \pi_{P S}^{\text {MP }}\right\}$ the population of MP at generation gen, $n_{i}$ the number of individuals that dominate the individual $\pi_{i}^{\text {MP }}$, $L$ the total number of nondominated levels of MP, $R_{i}\left(R_{i} \in\{1, \ldots\}\right)$ the nondominated level to which the $i$ th individual is assigned, $\boldsymbol{F}_{i}(l=1, \ldots, L)$ the set of individuals that belong to the $l$ th nondominated level, $\pi_{i, j}^{\text {NP }}(g e n)\left(j=1, \ldots,\left|\boldsymbol{F}_{i}\right|\right)$ the $j$ th individual of $\boldsymbol{F}_{i}$ at generation gen, $n\left(\pi_{i, j}^{\text {NP }}(g e n)\right)$ the number of individuals in $\pi^{\text {MP }}(g e n)$ that dominates individual $\pi_{i, j}^{\text {NP }}(g e n)$. Then, by means of the "fast nondominated sorting method" [20], the individual $\pi_{i}^{\text {MP }}(g e n)$ can be assigned to the corresponding nondominated level $R_{i}$ according to the value of $n_{i}$. Moreover, we can obtain a set $\boldsymbol{F}_{1}=\left\{\pi_{1, j}^{\text {NP }}(g e n), \pi_{1, 2}^{\text {NP }}(g e n), \ldots, \pi_{1, j \cdot j}^{\text {NP }}(g e n)\right\}$ from MP, where the individual $\pi_{1, j}^{\text {NP }}(g e n)\left(j \in\left\{1, \ldots,\left|F_{1}\right|\right\}\right)$ absolutely satisfies the condition that $n\left(\pi_{1, j}^{\text {NP }}(g e n)\right)=0$.

For example, there are 14 individuals in MP with the objectives $f_{1}\left(C_{\max }, T S C\right)$, i.e., $f_{1}(7.4,9.5), f_{2}(5.0,6.3), f_{3}(2.9,1.2)$, $f_{4}(8.0,9.0), f_{5}(9.0,8.2), f_{6}(1.5,3.0), f_{7}(10.1,9.9), f_{8}(3.5,7.9)$, $f_{9}(7.0,5.4), f_{10}(1.0,4.0), f_{11}(9.4,10.9), f_{12}(0.5,5.0), f_{13}(4.0,6.9)$, and $f_{14}(2.0,2.0)$. As illustrated in Fig. 7, these individuals can be divided into four nondominated levels (i.e., levels 1 to 4) via the fast nondominated sorting method. Then, the nondominated set $\boldsymbol{F}_{1}$ that includes nondominated individuals $\pi_{1,1}^{\text {NP }}(g e n)=\pi_{2}^{\text {NP }}(g e n)$, $\pi_{1,2}^{\text {NP }}(g e n)=\pi_{23}^{\text {NP }}(g e n), \pi_{1,3}^{\text {NP }}(g e n)=\pi_{6}^{\text {NP }}(g e n), \pi_{1,4}^{\text {NP }}(g e n)=$ $\pi_{10}^{\text {NP }}(g e n)$ and $\pi_{1,5}^{\text {NP }}(g e n)=\pi_{12}^{\text {NP }}(g e n)$ can be identified. Obviously, individuals of the same nondominated level are nondominated, and individuals in the higher nondominated levels ( $l \geq 2$ ) are dominated by ones that belong to the lower nondominated levels. According to [20], the worst-case CC of the nondominated sorting method is $O\left(M * P S^{2}\right)$, where $M$ is the number of objectives.

### 4.2.2. Crowding distance assignment

To achieve a good performance, we need to consider both the convergence and the diversity of offspring when evolving MP. Since individuals in the same nondominated level $l$ are all nondominated, a crowding distance $d_{i j}$ needs to be assigned to individual $j$. That is, if $d_{i j}>d_{i k}\left(j, k \in\left\{1, \ldots,\left|\boldsymbol{F}_{i}\right|\right\}\right)$, one can regard that the individual $j$ is "more promising" than the individual $k$. As illustrated in Fig. 8, the value of $d_{i j}$ can be calculated by using the average side length of the dashed box, and more details can be found in [20].

Based on the above definitions, the crowded-comparison operator $\left(\prec_{n}\right)$ [20] is used to compare the individuals distributed in different nondominated levels for performing selection operation. In doing so, a partial order is defined as $j \prec_{n} k$, if and only if $\left(R_{j}<\right.$ $\left.R_{k}\right)$ or $\left(\left(R_{j}=R_{k}\right) \wedge\left(d_{i j}>d_{i k}\right)\right)$. For instance, in Fig. 7, if the binary tournament selection operation is adopted, we prefer individual

3 to individual 8 since $R_{3}=1<R_{8}=2$. Besides, individual 2 is better than individual 13 because the former locates in a lesser crowded box than the latter and it holds $\left(\left(R_{2}=R_{13}\right) \wedge\left(d_{2,2}>\right.\right.$ $\left.d_{2,13}\right)$ ). According to [20], the worst-case CC of calculating the crowding distance is $O(M * P S * \log P S)$, where $M$ is the number of objectives.

### 4.3. EDA-based machine learning mechanism

The machine learning technique has been extensively regarded as an effective tool for guiding the search behavior of evolutionary algorithms [43-46]. Generally, the main methodology of machine learning follows two aspects: (1) Learning a probabilistic model to depict variable distribution from training samples; (2) Generating or predicting the testing samples from the probabilistic model. At this point, the ideas behind the machine learning are very similar to the search behavior of EDA [9,47-49], which undergoes two operations, i.e., estimating (learning) the probabilistic model and sampling (generating) new individuals from the model. Thus, an EDA-based machine learning mechanism is embedded into the framework of ENSHA to generate AP and search different promising regions. To be specific, the probabilistic model of the nondominated solutions of MP is estimated first, and then the candidate individuals of AP can be produced by sampling the probabilistic model. Finally, the AP of ENSHA can be obtained by utilizing the PMX-based method presented below.

### 4.3.1. Probabilistic model and estimating approach

For MOFJSSP_SDST/C, the marginal probability density of discrete random variables can be described by a set of marginal distribution laws, and in turn the corresponding marginal distribution functions could be obtained. Let $\boldsymbol{p r}_{1}(g e n), \ldots, \boldsymbol{p r}_{d}(g e n), \ldots$, $\boldsymbol{p r}_{d}(g e n)$ denote the marginal distribution laws of the $D$-dimensional discrete random variables at generation gen, and then we have
$\boldsymbol{p r}_{d}(g e n)=\left[p r_{1 d}(g e n), \ldots, p r_{n d}(g e n)\right]^{T}, d=1, \ldots, D$,
where $D=T O, \sum_{v=1}^{n} p r_{v d}(g e n)=1$, and $p r_{v d}(g e n)$ is the probability of operation $w$ appearing at the $d$ th dimension at generation gen. Then, the marginal distribution functions can be calculated from Eq. (7).
$F_{d}^{\text {gen }}(z)= \begin{cases}0 & 0 \leq z<1 \\ \sum_{v=1}^{v} p r_{v d}(g e n) & v \leq z<v+1, \text { for } v=1, \ldots, n-1 \\ 1 & z \geq n .\end{cases}$

![img-21.jpeg](img-21.jpeg)

Fig. 17. Box plots of MOPSO, MOEA/D, MOGLS, SPEAII and ENSHA.

Note that the matrix $\boldsymbol{P M}(\text { gen }) \mathrm{i}$ is used to record the marginal distribution laws of solution variables along with the iteration of ENSHA and it can be written as
$\boldsymbol{P M}(\text { gen })=\left(\begin{array}{ccc}p r_{11}(\text { gen }) & \cdots & p r_{1 T O}(\text { gen }) \\ \vdots & \ddots & \vdots \\ p r_{n 1}(\text { gen }) & \cdots & p r_{n T O}(\text { gen })\end{array}\right)_{n=10}$.
In ENSHA, $\boldsymbol{P M}(\text { gen })$ accumulates useful information from excellent individuals by using the incremental learning mechanism. That is, at each generation, an individual included in $\boldsymbol{F}_{1}$ of MP (i.e., $\boldsymbol{F}_{1}=\left\{\pi_{1 j}^{(g i} \mid g e n\right), \ldots, \pi_{1 j}^{(g)} \mid \text { gen })\}$ ) is randomly selected as the excellent individual for updating $\boldsymbol{P M}(\text { gen })$. Let $L R$ denote the learning rate and $\pi_{1 j}^{(g i, g i g e n)}$ the $d$ th element in $\pi_{1 j}^{(g i j g e n)} \mid j=$ $1, \ldots,\left|\boldsymbol{F}_{1}\right|$ ). Then, $\boldsymbol{P M}(\text { gen })$ can be estimated (updated) in Algorithm 2. When gen $=0$, each element in $\boldsymbol{P M}(0)$ is set to $1 / n$.

After doing so, the marginal distribution functions $F_{d}^{g e n+1}(z)$ for $d=1, \ldots, D$ can be obtained from $\boldsymbol{P M}(\text { gen })$ by using Eq. (7). The CC of Algorithm 2 is $O(T O * n)$.

### 4.3.2. Generating candidate individuals of $A P$

After estimating the probabilistic model of excellent individuals of MP, the next step is to sample it for generating candidate individuals of $A P$. We define the quasi-inverses of marginal distribution function as
$\left[F_{d}^{g e n}(u)\right]^{-1}= \begin{cases}v \\ \min \left\{v \mid F_{d}^{g e n}(v) \neq 0\right\} & u \in\left(F_{d}^{g e n}(v-1), F_{d}^{g e n}(v)\right]\end{cases}$
where $d=1, \ldots, D, v=1, \ldots, n$, and $D=T O$. The inverse function $\left[F_{d}^{g e n}(u)\right]^{-1}$ utilizes roulette wheel selection scheme to

![img-22.jpeg](img-22.jpeg)
c) Group 2 (SI_1)
![img-23.jpeg](img-23.jpeg)
b) Group 1 (SI_2)
![img-24.jpeg](img-24.jpeg)
d) Group 2 (SI_2)

Fig. 18. Comparisons of APFs and PFs for two groups.
generate output value, in which the variable $u$ simulates a spin of the wheel. The larger interval of $\left(F_{d}^{g e n}(v-1), F_{d}^{g e n}(v)\right]$ means the corresponding $v$ can be selected and outputted with a higher probability. According to Eq. (7), the steps 3, 4 and 8 of Algorithm 2 determine the interval size of each $\left(F_{d}^{g e n}(v-1), F_{d}^{g e n}(v)\right]$ by the selected individual's element $\pi_{1, j}^{A P, d}(g e n)$. Since excellent individuals are selected to update $\boldsymbol{P M}(g e n)$, their corresponding interval sizes are enlarged during the evolutionary process. This means that candidate individuals can inherit similar structures from excellent ones.

Let $\pi^{c A P}(g e n)=\left\{\pi_{1}^{c A P}(g e n), \ldots, \pi_{1 N}^{c A P}(g e n), \ldots, \pi_{1 N}^{c A P}(g e n)\right\}$ be the candidate population of AP, $\pi_{1, J}^{c A P}(g e n)$ the $d$ th element in $\pi_{1}^{c A P}(g e n)$, and $\left.\left(\int J, \pi_{1}^{c A P}(g e n)\right)\right)$ the repeat times of product $\boldsymbol{J}$ in $\pi_{1}^{c A P}(g e n)$. Then, the sampling method of $\pi^{c A P}(g e n)$ is proposed in Algorithm 3, which generates individuals directly from $\left[F_{d}^{g e n}(u)\right]^{-1}$. In Algorithm 3, the times that the condition $\left.\left(\int J, \pi_{1}^{c A P}(g e n)\right)=o p r_{j}\right)$ in Line 9 is met for generating a new individual, is $n$ times. Thus, the CC of Algorithm 3 is $O\left(P S * n^{2} * T O\right)$.

### 4.3.3. PMX-based method for generating AP

In population-based evolutionary algorithms, individuals are used to search different solution regions. Since the candidate individuals of AP totally follow the probabilistic distribution of the nondominated individuals in $\boldsymbol{F}_{1}$ (see Algorithm 3), they can search the regions nearby the promising individuals or regions $\pi_{1,1}^{A P}(g e n), \ldots$, and $\pi_{1, N_{1}}^{A P}(g e n)$. To further guide the search direction, a PMX-based method is added into ENSHA for producing AP, which executes the PMX on the individuals of $\pi^{c A P}(g e n)$ and $\boldsymbol{F}_{1}$ to preserve partial orders within them. Let $\pi^{A P}(g e n)=$ $\left\{\pi_{1}^{A P}(g e n), \ldots, \pi_{1 N}^{A P}(g e n)\right\}$ be the population of AP, and $\pi_{1}^{A P}(g e n)$ the $i$ th individual in $\pi^{A P}(g e n)$. The PMX-based method is given in Algorithm 4. Both algorithms 3 and 4 are utilized to increase the
search ability of ENSHA. Because only Lines 2 and 3 in Algorithm 4 exist computation, the CC of Algorithm 4 is $O(P S)$.

### 4.4. Cooperation-based refinement strategy

When generating MP of the next generation, a cooperationbased refinement mechanism is raised to combine MP and AP for reserving more promising regions or better individuals. Denote $\pi^{L P}(g e n)=\left\{\pi_{1}^{L P}(g e n), \ldots, \pi_{1, P S}^{L P}\right\}$ the union of MP and AP at generation gen, and $\pi_{1}^{L P}(g e n)$ the $j$ th individual in the $I$ th nondominated level set of $\pi^{L P}(g e n)$. The refinement strategy can be illustrated in Algorithm 5. In Algorithm 5, the worst-case CCs of Lines 2-6, Lines 18-20, and Lines 21 are $O\left(M *(2 P S)^{2}\right), O\left(M *\right.$ $(2 P S) * \log (2 P S)$ ), and $O\left((2 P S)^{2}\right)$, respectively. So, the worst-case CC of Algorithm 5 is $O\left(M *(2 P S)^{2}\right)$.

### 4.5. Procedure of ENSHA

On the basis of Sections 4.1 to 4.4, the procedure of ENSHA can be proposed. Let $\boldsymbol{\beta}^{A P P}(g e n)=\left\{\boldsymbol{\beta}_{1}^{A P}(g e n), \ldots, \boldsymbol{\beta}_{1 N}^{A P}(g e n)\right\}$ denote the offspring (children) of $\pi^{A P P}(g e n)$ during performing genetic operations (i.e., selection, crossover, and mutation) at generation gen, genMax the maximum generation, and ParetoSet the final set of nondominated individuals found by ENSHA. Then, the detail of ENSHA is given in Algorithm 6.

The detailed analyses of the CCs of one generation in Algorithm 6 are given in Table 5. From Algorithm 6 and Table 5, it can be concluded that the overall CC of ENSHA is $O\left(\right.$ genMax $*$ $\left(P S^{2}+P S * n^{2} * T O+P S * m * T O\right)$ ), where the coefficients $M$ $(M=2)$ and 2 are omitted. Obviously, the computational cost of ENSHA is not high, since the highest degree of the polynomial $\operatorname{genMax} *\left(P S^{2}+P S * n^{2} * T O+P S * m * T O\right)$ is only two.

![img-25.jpeg](img-25.jpeg)
b) $\Delta$
![img-26.jpeg](img-26.jpeg)

Fig. 19. Comparisons of NB associated with Group 1.

From Algorithm 6, it can be seen that ENSHA's evolutionary process is driven by the supplement and promotion of MP and AP. Through using the genetic operations with the elitist nondominated sorting scheme (Lines 17 to 38), MP can preserve the high-quality individuals in terms of both the convergence and diversity. Meanwhile, the marginal probabilistic model and the PMX-based method are applied to generate AP (Lines 13 to 16) for exploring different promising individuals nearby the nondominated individuals found so far. Furthermore, the cooperation-based refinement strategy (Lines 7-9) is used to preserve the excellent individuals in both MP and AP for generating the next generation of MP, which makes MP and AP possible to supplement and promote each other during the search process.

## 5. Experimental results and comparisons

### 5.1. Experimental design

Due to the lack of benchmark data for MOFJSSP_SDST/C, a number of instances based on well-known benchmark data for FJSSP are used to test the performance of ENSHA. In this study, we adopt two data sets of FJSPLIB ${ }^{1}$ widely used in previous literatures, i.e., Dauzère-Pérés and Paulli [50] and Chambers and Barnes [51], and randomly generate SDSTs and SDSCs from a uniform distribution [1,50]. The original data sets of Dauzère-Pérés

[^0]
[^0]:    ${ }^{1}$ The original resource of these data sets is available at http://people.idsia. ch/monaldo/fjspresults/TextData.zip.

```
Algorithm 1: Decoding a Solution
Input: assignment rule, solution \(\boldsymbol{\pi}\)
Output: makespan, TSC
    For \(k:=1\) to \(T O\) do
        For \(j:=1\) to \(m\) do
            If \(\left(\pi_{k}\right.\) satisfies processing constraints on machine \(j\) ) then
                Calculate \(C T\) and \(S C\) for \(\pi_{k}\) on machine \(j\);
                End If
            End For \(j\)
            If (there is a tie for assignment rule) then
                Arbitrarily select one machine \(j^{*}\) from \(A V A\left(\pi_{k}\right)\);
            Else
            Select one machine \(j^{*}\) from \(A V A\left(\pi_{k}\right)\) by using adopted assignment rule;
            End If Else
            Assign \(\pi_{k}\) to the selected machine \(j^{*}\);
        End For \(k\)
        Calculate makespan and TSC based on the model mentioned in Section 2;
        Return makespan and TSC
Algorithm 2: Estimate Marginal Probability Matrix
Input: \(\pi_{i, j}^{S P}(\) gen \() \mid j=1, \ldots,|F|), L R, P M(\operatorname{gen}-1)\)
Output: \(P M\) (gen)
    Set \(r>r_{\text {random }}\left[1,|F|] ;\right) /\) randomly select a nondominated individual
    For \(d:=1\) to \(D\) do
        Set \(x:=\boldsymbol{\pi}_{i, j}^{S P-d} \text { (gen) } ;\)
        Set \(p r_{s d}(\) gen \() \mid=\operatorname{pr}_{s d}(\) gen -1 \()+L R ; / /\) accumulate information with the learning rate
    End for \(d\)
    For \(d:=1\) to \(D\) do
        For \(w:=1\) to \(R\) do
            Set \(p r_{w d}(\) gen \() \mid=\operatorname{pr}_{w d}(\) gen \() /(1+L R) ; /\) normalize the probability values
            End for \(w\)
    End for \(d\)
    Return \(P M(\operatorname{gen})\)
```

and Barnes contain 18 instances ( 01 a to 18 a ) and 21 instances (mt10c1 to seti5xyz), respectively, so that there are a total of 39 instances $^{2}$ used in this paper. In all results, Worst, Best, Mean, and $S D$ denote the worst value, best value, average value, and standard derivation of relevant performance metrics, respectively. And $N B$ denotes the total number of the best statistic values (i.e., Worst, Best and Mean) of each performance metric obtained by the related algorithms. The experiments and comparisons are performed using fixed numbers of function evaluations (FES) for each instance for all algorithms. All algorithms are coded in Delphi7.0 and executed on Intel Core i7-6700 3.40 GHz processor with 16 GB memory.

### 5.2. Performance metrics

For multi-objective optimization problems, decision makers desire to find a satisfied solution from a number of candidate ones. According to [20,52,53], basically two main aspects should

[^0]be considered to evaluate the obtained nondominated solutions: (1) The distance of the obtained nondominated solutions to the true Pareto front (PF) or approximate Pareto front (APF); (2) The diversity and distribution of the obtained nondominated solutions. Some performance metrics were proposed in existing literature. Although the names of these metrics are different, they can be basically divided into the L1-norm-based metrics and the L2-norm-based metrics. Each L1-norm-based metric has a L1norm item (i.e., $\|x\|_{1}=\sum\left|s_{i}\right|$ ) in its numerator, and similarly each L2-norm-based metric has a L2-norm item (i.e., $\|x\|_{2}=$ $\sqrt{\sum\left|s_{i}\right|^{2}}$ ) in its numerator. The frequently used L1-norm-based metrics are the distance metric $\gamma$ (also called the convergence metric $\gamma$ ) and the diversity metric $\Delta$ [20,54,55]. Meanwhile, the frequently used L2-norm-based metrics contain the generational distance (GD) metric [56], the inverted generational distance (IGD) metric [57,58], and the diversity or spacing (SP) metric [57, 59]. Both those L1-norm-based metrics and L2-norm-based metrics can better evaluate the obtained nondominated solutions in most situations. Here, two L1-norm-based metrics (i.e., $\gamma$ and $\Delta$ ) are adopted to evaluate the performance of each compared algorithm. Moreover, since MOEAs for multi-objective scheduling


[^0]:    2 These 39 instances used in this study can be downloaded at http://dx.doi. org/10.17632/vtnt28cc7s.2.

```
Algorithm 3: Generate Candidate Individuals of AP
Input: \(\boldsymbol{P M}(g e n)\)
Output: \(\pi^{c A P}(g e n)\)
    Set \(\Psi(g e n):=\boldsymbol{P M}(g e n) ; / /\) save the marginal probability matrix
    For \(i:=1\) to \(P S\) do
        Set \(\boldsymbol{P M}(g e n):=\boldsymbol{\Psi}(g e n) ; / /\) ensure all individuals are sampled from \(P M(\) gen \()\)
        For \(d:=1\) to \(D\) do
            Calculate \(F_{d}^{g e n}(z)\) by using Eq. (7);
            Set \(u:=\) random \([0,1] ; / /\) generate a random value from \([0,1]\)
            Set \(J:=\left[F_{d}^{g e n}(u)\right]^{-1} ; / /\) select a job by using Eq. (9)
            Set \(\pi_{i d}^{c A P}(g e n):=J ; / /\) assign a sampling job
            If \(l\left(J, \pi_{i}^{c A P}(g e n)\right)\right)=\alpha p r_{j}\) then
            For \(w:=d+1\) to \(D\) do
                Set \(p r_{j_{w}}(g e n):=0\);
                For \(k:=1\) to \(\pi\) do
                    Set \(p r_{j_{w}}(g e n):=p r_{j_{w}}(g e n) /\left(1-p r_{j_{w}}(g e n)\right)\);
                End for \(k\)
                End For \(w\)
            End If
        End For \(d\)
        End For \(i\)
        Set \(\boldsymbol{P M}(g e n):=\boldsymbol{\Psi}(g e n) ; / /\) recover the marginal probability matrix
    Return \(\pi^{c A P}(g e n)\)
```

```
Algorithm 4: PMX-based Method for Generating AP
    Input: \(\pi^{c A P}(g e n), \pi_{i, j}^{N P}(g e n)\left(j=1, \ldots,|F| \mid\right)\)
    Output: \(\pi^{A P}(g e n)\)
        For \(i:=1\) to \(P S\) do
        Set \(r_{1}:=\operatorname{random}\left[1,|F| \mid\right] ; / /\) randomly select a nondominated individual
        Set \(r_{2}:=\operatorname{random}[1, P S] ; / /\) randomly select a candidate individual of AP
        Set \(\pi^{p 1}:=\pi_{i, 1}^{N P}(g e n)\) and \(\pi^{p 2}:=\pi_{i, 2}^{c A P}(g e n) ; / /\) randomly select the parents
        Perform the PMX crossover on \(\pi^{p 1}\) and \(\pi^{p 2} ; / /\) subsection 4.1
        Set \(\pi_{i}^{A P}(g e n)\) to the child of \(\pi^{p 1}\) and \(\pi^{p 2}\);
    End For \(i\)
    Return \(\pi^{A P}(g e n)\)
```

problems often only get several nondominated solutions, the number of them also needs to be considered in the comparisons. Thus, a dominance metric (i.e., $\Omega$ ) is added for performance evaluation.

Note however, that the PF of MOFJSSP_SDST/C is not known and it might be intractable when calculating the performance metrics of compared algorithms. Same as previous studies [54, 55], we first combine the sets of nondominated solutions of $K$ algorithms (or parameter combinations, or assignment rules) $S_{1}, \ldots, S_{K}$ together. And then the nondominated solutions are identified from $S_{1} \cup, \ldots, \cup S_{K}$ to construct an APF. Afterwards, the performance metrics of algorithms are calculated according to APF. Nevertheless, how to guarantee that APF is a good approximation of PF is still short of common conclusions. Hence, we perform further discussions on the approximations of APF and PF in Section 5.7, on the basis of two small instances for which the PFs can be determined exactly.

### 5.2.1. Convergence metric $(\gamma)$

Suppose that nondominated solution sets $S_{1}, \ldots, S_{K}$ are obtained by $K$ algorithms (or parameter combinations, or assignment rules). Since the Pareto front of MOFJSSP_SDST/C is not known, we combine the sets $S_{1}, \ldots, S_{K}$ together and identify the nondominated solutions from $S_{1} \cup \ldots, \cup S_{k}, \ldots, \cup S_{K}$ to approximate the Pareto front $S^{*}$. Let $d_{s y}\left(S_{k}\right)$ denote the shortest Euclidean distance from a solution $x$ of $S_{k}$ to the nearest solution $y$ of $S^{*}$, and $\left|S_{k}\right|$ the number of solutions in $S_{k}$. Then, the convergence metric $\gamma_{k}$ can be defined in Eq. (10). Obviously, a smaller $\gamma_{k}$ corresponds to a better approximation to the Pareto front.
$\gamma_{k}=\sum_{s=1}^{\left|S_{k}\right|} d_{s y}\left(S_{k}\right) /\left|S_{k}\right|, k=1, \ldots, K$.
Though the values of $\gamma_{k}$ and the L2-norm-based metric $\mathrm{GD}_{k}$ $\left(\mathrm{GD}_{k}=\sqrt{\sum_{s=1}^{\left|S_{k}\right|}}\left(d_{s y}\left(S_{k}\right)\right)^{2} /\left|S_{k}\right|\right)$ are different, the same ordinal

```
Algorithm 5: Cooperation-based Refinement Strategy
Input: \(\pi^{A P}(g e n-1), \pi^{A P P}(g e n-1)\)
Output: \(\pi^{A P}(g e n)\)
    Set \(\pi^{L P}(g e n)>\pi^{A P}(g e n-1) \cup \pi^{A P}(g e n-1) ; / /\) construct the union of MP and AP
    For \(i:=1\) to \(2 P S\) do
        Calculate \(n_{j}\) for \(\pi_{i, j}^{L P}(g e n) ; / /\) subsection 4.2
        Assign \(\pi_{i}^{L P}(g e n)\) to its nondominated level \(\bar{R}_{i} ; / /\) subsection 4.2
    End For \(i\)
        Obtain \(L\) nondominated sets \(\boldsymbol{F}_{i}=\left\{\boldsymbol{\pi}_{i, j}^{N P}(g e n), \ldots, \boldsymbol{\pi}_{i, j}^{N P}(g e n), \ldots, \boldsymbol{\pi}_{i, j L_{i}}^{N P}(g e n)\right\} \quad(l=1, \ldots, L)\)
        of \(\pi^{L P}(g e n)\) via the nondominated sorting method; //subsection 4.2
    Set \(w>1\);
    For \(l:=1\) to \(L\) do
        If \(w>P S\) then
            Break;
        End If
        If \(w+\left|\boldsymbol{F}_{j}\right| \leq P S+1\) then
            For \(j:=1\) to \(\left|\boldsymbol{F}_{j}\right|\) do
                \(\pi_{w}^{A P P}(g e n)>\pi_{i, j}^{N P}(g e n) ;\)
                \(w:=w+1 ;\)
            End For \(j\)
        Else
            For \(j:=1\) to \(\left|\boldsymbol{F}_{j}\right|\) do
                Calculate the crowding distance \(d_{i j}\) for \(\pi_{i, j}^{N P}(g e n)\);
            End For \(j\)
            Rank individuals in \(\boldsymbol{F}_{j}\) in descending order according to crowding distances
                and obtain the ranked \(\boldsymbol{F}_{j}=\pi_{i, j L_{i}}^{N P}(g e n), \ldots, \pi_{i, j L_{i}}^{N P}(g e n), \ldots, \pi_{i, j j_{i L_{i}}}^{N P}(g e n) ;\)
                //subsection 4.2
            Repeat
                Set \(v:=1\);
                \(\pi_{w}^{A P P}(g e n)>\pi_{i, j L_{i}}^{N P}(g e n) ;\)
                \(w:=w+1\) and \(v:=v+1\);
            Until \((w=P S+1)\)
            End If Else
        End For \(l\)
        Return \(\pi^{A P}(g e n)\)
```

relationship among the compared sets $S_{1}, \ldots, S_{K}$ can be obtained by using these two metrics. For example, if the ordinal relationship $\gamma_{3}<\gamma_{1}<\gamma_{2}$ is obtained, the same ordinal relationship $\mathrm{GD}_{3}<\mathrm{GD}_{1}<\mathrm{GD}_{2}$ also can be obtained. This means that there is no essential difference between $\gamma_{k}$ and $\mathrm{GD}_{k}$.

### 5.2.2. Diversity metric $(\Delta)$

Let $d_{i, k}$ denote the Euclidean distance between the highest solution of $S_{k}$ and it of $S^{*}$ on the vertical axis, $d_{v k}$ the Euclidean distance between the furthest solution of $S_{k}$ and it of $S^{*}$ on the horizontal axis, $d_{i, k}$ the Euclidean distance between the two consecutive solutions $\lambda$ and $\lambda+1$ of $S_{k}, d_{k}$ the average Euclidean distance among all solutions of $S_{k}$. The diversity metric is given in Eq. (11). It is clear that the smaller the $\Delta_{k}$ is, the better the diversity is.
$\Delta_{k}=\frac{d_{i, k}+d_{v k}+\sum_{i, v 1}^{\left|S_{k}\right|-1}\left|d_{i, k}-\bar{d}_{k}\right|}{d_{i, k}+d_{v k}+\left(\left|S_{k}\right|-1\right) \bar{d}_{k}}, k=1, \ldots, K$.
Obviously, the revised $\Delta_{k}^{\text {revised }}\left(\Delta_{k}^{\text {revised }}=\sum_{i, v 1}^{\left|S_{k}\right|-1}\left|d_{i, k}-\bar{d}_{k}\right|\right.$ $\left./\left|\left|S_{k}\right|-1\right) \bar{d}_{k}\right)$ and the L2-norm-based metric $\mathrm{SP}_{k}\left(\mathrm{SP}_{k}=\right.$ $\left.\sqrt{\sum_{j=1}^{\left|S_{k}\right|-1} /\left|d_{i, k}-\bar{d}_{k}\right|^{2}}\left(\left|S_{k}\right|-2\right)\right]$ can obtain the same ordinal relationship among the compared sets $S_{1}, \ldots, S_{K}$. By adding $d_{i, k}$ and
$d_{v k}, \Delta_{k}$ can evaluate not only the diversity but also the spread of $S_{k}$. Therefore, $\Delta_{k}$ is a more suitable metric.

### 5.2.3. Dominance metric (12)

A dominance metric is concerned with the number of solutions in $S_{k}$ that are not dominated by any solutions of $S^{*}$. This metric is written as
$\Omega_{k}=\left|S_{k} \backslash\left\{x \in S_{k} \mid \exists y \in S^{*}:\left.y \prec x\right\}\right\} /\left|S_{k}\right|\right.$,
where $y \prec x$ denotes the solution $x$ is dominated by solution $y$. Apparently, the larger the value of $\Omega_{k}$ is, the better the set $S_{k}$ is.

### 5.3. Effectiveness of proposed job assignment rules

To test the effectiveness of the proposed job assignment rules (i.e., $C T+S C, C T^{*} S C$ and DOMINANCE), we compare them with 4 well-known assignment rules reported in existing literatures, including RANDOM [33], SPT [33-35], EST [34,35] and ECT [34,35]. Since the parameters of ENSHA have not been tuned before this comparison, we here adopt the mean values of all candidate levels of each parameter listed in Table 6. The parameters are as follows: $P S=125, P c=0.50, P m=0.375$ and $I R=0.04$. ENSHAs with different job assignment rules are independently run 21

```
Algorithm 6: ENSHA for MOFJSSP_SDST/C
Input: genMax, \(P S, P c, P m, L R\)
Output: ParetoSet
    For gen: \(=0\) to genMax +1 do
        If gen \(=0\) then
            Randomly initialize \(\pi^{M P}(g e n=0)\) and \(\pi^{A P}(g e n=0)\);
            Evaluate the individuals of \(\pi^{M P}(g e n=0)\) and \(\pi^{A P}(g e n=0) ; / /\) Algorithm 1
            Initialize the marginal probability matrix \(P M(\operatorname{gen}=0)\) where
            \(p r_{n d}(\operatorname{gen}=0)=1 / n, d=1, \ldots, T O\) and \(w=1, \ldots, n\);
        Else
            /* cooperation-based refinement strategy*/
            Perform cooperation-based refinement and obtain \(\pi^{M P}(g e n) ; / /\) Algorithm 5
            Identify \(\pi_{1, j}^{A P}(g e n)\) of \(\pi^{M P}(g e n), j=1, \ldots, \mid \boldsymbol{F}_{1} \mid ; / /\) Section 4.2
            If gen \(=\) genMax +1 then Break the main loop;
            End If
            /*EDA-based machine learning mechanism*/
            Estimate the marginal probability matrix \(P M(\operatorname{gen}) ; / /\) Algorithm 2
            Generate the candidate population \(\pi^{c A P}(g e n) ; / /\) Algorithm 3
            Perform the PMX-based method to \(\pi^{c A P}(g e n)\) and \(\pi_{1, j}^{A P}(g e n)\) for
            generating \(\pi^{A P}(g e n) ; / /\) Algorithm 4
            Evaluate the individuals of \(\pi^{A P}(g e n) ; / /\) Algorithm 1
            /* genetic operations for MP*/
            Calculate the crowding distance of each individual in \(\pi^{M P}(g e n)\);
            For \(i:=1\) to \(P S\) do //binary tournament selection
            Set \(r_{1}, r_{2}:=\operatorname{random}[1, P S]\) where \(r_{1} \neq r_{2} \neq i\);
            If \(\pi_{c}^{M P}(g e n) \prec_{n} \pi_{c}^{M P}(g e n)\) then //Section 4.2
            Set \(\boldsymbol{\beta}_{i}^{M P}(g e n):=\pi_{c 1}^{M P}(g e n) ;\) Else Set \(\boldsymbol{\beta}_{i}^{M P}(g e n):=\pi_{c 2}^{M P}(g e n) ;\)
        End If Else
        End For \(i\)
        For \(i:=1\) to \(P S\) do //PMX-based crossover
            If \(\operatorname{random}[0,1] \leq P c\) then
                Apply crossover to \(\boldsymbol{\beta}^{M P}(g e n)\) for producing \(\boldsymbol{\beta}_{i}^{c M P}(g e n) ; / /\) Section 4.1
                Evaluate the individual \(\boldsymbol{\beta}_{i}^{c M P}(g e n) ; / /\) Algorithm 1
                Set \(\boldsymbol{\beta}_{i}^{M P}(g e n):=\boldsymbol{\beta}_{i}^{c M P}(g e n) ;\)
                End If
            End For \(i\)
            For \(i:=1\) to \(P S\) do //Interchange-based mutation
                If random \([0,1] \leq P m\) then
                    Apply mutation to \(\boldsymbol{\beta}_{i}^{M P}(g e n) ; / /\) Section 4.1
                    Evaluate the individual \(\boldsymbol{\beta}_{i}^{M P}(g e n) ; / /\) Algorithm 1
                End If
            End For \(i\)
            Set \(\pi^{M P}(g e n):=\boldsymbol{\beta}^{M P}(g e n) ; / /\) update MP
        End If Else
        End For \(i\)
        Return ParetoSet \(:=\left\{\pi_{1, j}^{A P}(g e n M a x+1), \ldots, \pi_{1, P_{i}}^{A P}(g e n M a x+1)\right\}\)
```

times and the maximum FES (MaxFES) is adopted as the stopping condition. The MaxFES is set to 500,000. In terms of 39 instances, the histograms considering the mean values of dominance metric are shown in Fig. 9.3

From Fig. 9, it is clear that the proposed $C T+S C, C T^{*} S C$ and DOMINANCE are able to gain the top 3 performances for almost all instances. These results indicate that the proposed job assignment rules can provide relatively effective local optimization for individuals during the search process of ENSHA. This is because,

[^0]in our proposed job assignment rules, we not only consider $C T$ but also $S C$ which may directly impact the quality of obtained individuals. That is, our job assignment rules can find relatively better tradeoff between the multiple objectives, and, in turn, good performance can be achieved. Thus, we should consider $C T$ and $S C$ simultaneously for MOFJSSP_SDST/C, since conventional assignment rules (such as RANDOM, SPT, ECT and EST) concentrating on single objectives may lead to poor performances. Indeed, the design of the problem-dependent job assignment rule is important for production scheduling problem, which would be significant for the overall performance of the underlying solution methods. For multi-objective production scheduling problems with both the efficiency and economic criteria, sub-indicators


[^0]:    3 Details of the comparisons associated with the convergence, diversity and dominance metric can be downloaded at http://dx.doi.org/10.17632/hrv2d8bprb.

Table 5
Detailed analyses of the CCs of one generation in Algorithm 6.
$C T$ and $S C$ may inherently determine the basic structures of job assignment rules. Therefore, the philosophy of the presented job assignment rules may be also useful for the other kinds of multi-objective scheduling problems. However, this research issue obviously beyond the scope of this paper.

It should be additionally note that $C T * S C$ outperforms, related to 27 instances, $C T+S C$ and DOMINANCE as shown in Fig. 9. Say that $C T * S C$ tends to get more reasonable tradeoff between $C T$ and $S C$. Relevant observations on the $95 \%$ confidence interval (CI) of $\Omega$ are put forward in Fig. 10, in which the overall trend of the mean value of $\Omega$ is illustrated as well. It is clear that $C T * S C$ can obtain more effective and reliable solutions than the other two rules, in terms of both the $95 \%$ CI and the overall trend. Hence, this paper will adopt $C T * S C$ as the job assignment rule and embed it into the global search framework of ENSHA. We also execute ENSHA (with different rules) by using different parameter combinations; nevertheless, the conclusions are very similar to ones mentioned above.

### 5.4. Parameter settings

To find a suitable parameter combination for ENSHA, three performance metrics (i.e., $\gamma, \Delta$ and $\Omega$ ) should be considered simultaneously because they are all related to ENSHA's performance. In this paper, the Taguchi method is used for parameter tuning [60-63], in which the response is the sum of normalized values of performance metrics and the factors are the parameters of ENSHA. In the Taguchi method, we consider two kinds of
factors (i.e., controllable factors $S$ and noise factors $N$ ), and the ultimate goal is to control $N$ and reduce the variation around the response associated with orthogonal arrays. Note that the design that is impressed less by $N$ is selected as the robust design. As suggested by previous works [60-63], the signal to noise ratio $(S / N)$ is used for performing the analysis on experimental results.

In the implementation of the Taguchi method, we carry out the design-of experiment (DOE) [64] based on the instance "12a". To be specific, 4 factor levels are considered for parameters PS, Pc, Pm and $L R$ on the performance of ENSHA, as shown in Table 6. The orthogonal array $L_{16}\left(4^{4}\right)$ with a total of 16 parameter combinations is adopted, which is generated by IBM SPSS Statistics 20 (the seed value is set to 1), as listed in Table 7. For all combinations, ENSHA is independently run 21 times with the stopping condition MaxFES $=500,000$. After running ENSHA one time, the corresponding metrics $\gamma, \Delta$ and $\Omega$ of each combination is calculated and recorded. The obtained metrics of each combination in the first run are listed in Table 7.

As mentioned earlier, parameter combinations having the larger $\Omega$ yet the smaller $\gamma$ and $\Delta$ indicate better solution quality. However, there may be a large difference among the values of three metrics, so we need to normalize them after each run. To be specific, the best result of certain metrics is assigned to 1 while the other results are assigned among $[0,1]$. It should be noted that some values of metrics may be equal to 0 . Therefore, we set $\gamma_{k}=\gamma_{k}+\delta_{1}, \Delta_{k}=\Delta_{k}+\delta_{2}$ and $\Omega_{k}=\Omega_{k}+\delta_{3}$ $(k=1, \ldots, 16, \delta_{1}=\delta_{2}=\delta_{3}=0.001$ ). We normalize the values of the performance metrics of Table 7 in Table 8, where $\operatorname{Sum}_{k=1}$

![img-27.jpeg](img-27.jpeg)
a) $\gamma$
![img-28.jpeg](img-28.jpeg)
b) $\Delta$
![img-29.jpeg](img-29.jpeg)
c) $\Omega$

Fig. 20. Comparisons of $N B$ associated with Group 2.

Table 6
Different combinations of parameters.
is the sum of normalized metrics in the first run. In terms of 21 runs, the sums of normalized metrics $\operatorname{Sum}_{k}(k=1, \ldots, 21)$ for each parameter combination are given in Table 9.

Table 7
Orthogonal array and obtained values of metrics (the first run).
Table 8
Normalized values of metrics (the first run).
The aim of the Taguchi method is to find the maximum $S / N$. Based on the sum of normalized metrics $\operatorname{Sum}_{k}(k=1, \ldots, 21)[60$, 63], $S / N$ can be calculated as
$S / N=-10 \log \left(\frac{1}{n} \sum_{i=1}^{n} \operatorname{Sum}_{i}^{2}\right)$
where $n=21$ is the number of replications of ENSHA. The values of $S / N$ for all combinations are given in Table 9. Obviously, the larger the value of $S / N$ is, the better the parameter combination is. Based on Table 9, the level trends of parameters are given in Fig. 11. Thereby, ENSHA's parameters are as follows: $P S=50$, $P c=0.60, P m=0.45$ and $L R=0.07$.

### 5.5. Comparisons with NSGAII and variant algorithms

For the purpose of investigating the effectiveness of ENSHA's components, we compare ENSHA with its variant (denoted as ENSHA_V). ENSHA_V is the same to ENSHA except that the genetic operators and the cooperation-based refinement strategy are not used. In ENSHA_V, we introduce an external archive to record the nondominated solutions during the search process, and the EDA-based machine learning mechanism is performed through such an external archive. That is to say, in ENSHA_V, the marginal probability matrix is estimated by using a randomly selected solution from the current external archive. Furthermore, the comparisons of ENSHA and NSGAII [20] are carried out to verify the effectiveness of the embedded EDA-based machine

Table 9
Sum of normalized metrics for each parameter combination.
Table 10
Comparisons of NSGAII, ENSHA_V and ENSHA $(\gamma)$.

learning mechanism as well as the cooperation-based refinement strategy. Note that NSGAII's parameters are the same as ENSHA.

For each instance, each algorithm is run 21 times independently and the MaxFES is adopted as the stopping conditions. Based on our previous analysis, ENSHA may require a little more CPU time than NSGAII in a single iteration. To make a fair comparison, we set MaxFES $=500,000$ for ENSHA while 600,000 for NSGAII and ENSHA_V. The average CPU time (s) for three
algorithms are shown in Fig. 12, in which ENSHA's trend is highlighted in shadow. From Fig. 12, it is clear that ENSHA's average CPU time is very similar to that of NSGAII for almost all the instances. Especially, ENSHA takes less CPU time than ENSHA_V for 38 instances. The comparison results related to $\gamma, \Delta$ and $I 2$ are listed in Tables 10 to 12.

It can be seen from Tables 10 to 12 that ENSHA outperform NSGAII and ENSHA_V regarding three performance metrics. As

Table 11
Comparisons of NSGAII, ENSHA_V and ENSHA ( $\Delta$ ).

for $\gamma$ and $\Delta$, it shows that ENSHA can obtain more competitive nondominated solutions than NSGAII and ENSHA_V. As for $\Omega$, it is clear that ENSHA can achieve good performance and the obtained nondominated solutions are closer to APF than NSGAII and ENSHA_V. Therefore, the proposed EDA-based machine learning mechanism and the cooperation-based refinement strategy are helpful in enhancing the overall search ability of ENSHA.

To make a reliable conclusion on the performance of ENSHA, the single factor analysis of variance (ANOVA) [65,66] is used to analyze the significant differences among NSGAII, ENSHA_V and ENSHA at $95 \%$ CI. In doing so, we are interesting in the significant differences among algorithms in terms of three performance metrics. The results of ANOVA associated with $\gamma, \Delta$ and $\Omega$ are given in Table 13.

As shown in Table 13, the $p$-values for $\gamma, \Delta$ and $\Omega$ are all less than 0.05 , so there are significant differences among NSGAII, ENSHA_V and ENSHA at $95 \%$ CI. Since there are three algorithms in the comparisons, a post hoc analysis using Tukey's multiple comparison tests $[65,66]$ is conducted to further show the significant difference of the pairwise comparisons of algorithms. Note here that we perform Tukey's tests based on the mean values of performance metrics for all instances at $95 \% \mathrm{CI}$. The results of Tukey's multiple cooperation tests are given in Table 14.

From Table 14, the $p$-values for three pairwise comparisons are less than 0.05 in terms of $\Delta$ and $\Omega$, implying the significant differences between ENSHA and other algorithms for such two

Table 12
Comparisons of NSGAII, ENSHA_V and ENSHA $(\Omega)$.

Table 13
Results of ANOVA for three metrics (NSGAII, ENSHA_V and ENSHA).
metrics. However, as for $\gamma$, the $p$-values for the first two pairwise comparisons are less than 0.05 , while for the last comparison is 0.79 that is larger than 0.05 . Therefore, the difference between ENSHA and NSGAII is somewhat not significant associated with $\gamma$. The potential reason might be that both of ENSHA and NSGAII can achieve aching the most common results of Table 10. Further, we draw the box plots based on the mean values of $\gamma$ for 39 instances in Fig. 13. It is then clear that both ENSHA and NSGAII perform well regarding $\gamma$ while ENSHA has a relatively better performance than NSGAII. Accordingly, the $p$-value for "NSGAII vs. ENSHA" is larger than 0.05 in fact verify the better convergence performance of ENSHA.

In view of the above analysis, ENSHA outperforms NSGAII and ENSHA_V related to three performance metrics. ENSHA is able to provide more efficient nondominated solutions with better diversity and convergence metrics. Moreover, we draw the box plots

Table 14
Results of Tukey's tests (NSGAII, ENSHA_V and ENSHA).
${ }^{a}$ Upper bound of 95\% CI.
${ }^{\text {b }}$ Lower bound of 95\% CI.

Table 15
Comparisons of MOPSO, MOEA/D, MOGLS, SPEAII and ENSHA ( $\gamma$ ).

associated with $\gamma, \Delta$ and $\Omega$ for NSGAII, ENSHA_V and ENSHA for instances 01a, mt10c1, setb4c9 and seti5cc in Fig. 14. We can see from these plots that ENSHA can obtain more robust search performance and reliable statistical distributions than NSGAII and ENSHA_V.

### 5.6. Comparisons with other state-of-the-art algorithms

To further demonstrate the effectiveness of ENSHA, we carry out comparisons with the other state-of-the-art algorithms for MOEAs, including MOPSO [67], MOEA(D [21], MOGLS [22] and SPEAII [19]. The parameters for the above four algorithms are as follows: (1) MOPSO: the number of particles, repository size, divisions for the adaptive grid and mutation rate are set to 100, 20, 30 and 0.5; (2) MOEA/D: the number of the sub-problems and the number of neighboring vectors are set to 100 and 20;
(3) MOGLS: the size of temporary elite population and the size of initial population are set to 150 and 20; (4) SPEAII: the population size, archive size, crossover probability, mutation probability are set to $95,5,0.8$ and 0.6 . The original framework of MOPSO was presented for optimization problems in the continuous domain, so it cannot be directly used for MOFJSSP_SDST/C. Thus, we map each continuous individual of MOPSO to the related permutation $\pi^{p o r}=\left[\pi_{p}^{p o r}, \ldots, \pi_{p}^{p o r}, \ldots, \pi_{l 0}^{p o r}\right](\pi_{p}^{p o r} \in$ $(1, \ldots, T 0))$ by using the well-known largest-order-value (LOV) rule [37,53]. Thereafter, $\pi^{p o r}$ can be transformed to a legal solution $\pi=[\pi_{1}, \ldots, \pi_{k}, \ldots, \pi_{T 0}]$ of MOFJSSP_SDST/C based on a formula $\pi_{k}=[j+1 \mid \pi_{k}^{p o r} \in[\sum_{k=1}^{k} \sigma p r]+1, \quad \sum_{k=0}^{k} \sigma p r] .]=$ $0, \ldots, n-1$ and $\sigma p r)_{0}=0]$, where $\sigma p r)_{1}$ is the number of operations of product $l$. For example, for a case with $n=m=4 \times 2, \pi^{p o r}=$ $[8,3,6,10,9,1,2,5,4,7]$, and $\left[\sigma p r_{1}, \ldots, \sigma p r_{k}\right]=[2,4,1,3]$, we can easily obtain a legal solution $\pi=[4,2,2,4,4,1,1,2,2,3]$

Table 16
Comparisons of MOPSO, MOEA/D, MOGLS, SPEAII and NSHA ( $\Delta$ ).

by using the above formula. In the comparisons, all algorithms are independently executed 21 times for all instances. To be fair, these compared algorithms adopt the same termination condition with MaxFES $=500,000$. The average CPU time of algorithms are given in Fig. 15, where the trend of ENSHA is highlighted in shadow. The comparison results associated with $\gamma, \Delta$ and $\Omega$ are given in Tables 15 to 17.

From Fig. 15, we can see that the average CPU time of ENSHA is similar to that of MOEA/D and SPEAII but is less than that of MOPSO and MOGLS for almost all the instances. In this sense, the overall efficiency of ENSHA is very acceptable compared with the state-of-the-art algorithms. It also can be seen from Tables 15 to 17 that almost all the performance metrics of ENSHA are much better than those of MOPSO, MOEA/D, MOGLS, and SPEAII. These results show that ENSHA is a more effective algorithm than the state-of-the-art algorithms and is significant for obtaining high-quality solutions of MHPMSP_MOSST/C. Moreover, to make a reliable assessment on ENSHA's performance metrics for 39 instances.

As shown in Table 19, in terms of $\Delta$ and $\Omega$, the $p$-values for all pairwise comparisons are less than 0.05 , which implies the significant differences between ENSHA and the state-of-the-art algorithms. As for $\gamma$, the $p$-value for "ENSHA vs. MOGLS" is less than 0.05 , whereas the $p$-values for "ENSHA vs. MOEA/D" and "ENSHA vs. SPEAII" are larger than 0.05. Thus, we need to go further to analyze the convergence performance of ENSHA. The box plots considering the mean values of $\gamma$ for 39 instances are given in Fig. 16. We can see that ENSHA, MOEA/D and SPEAII can achieve good performance with respect to $\gamma$, and these algorithms can obtain the preponderant median values trending to 0 . Therefore, regarding $\gamma$, the $p$-values for "ENSHA vs. MOEA/D" and "ENSHA vs. SPEAII" are larger than 0.05, which indicates the good convergence performance of ENSHA. Besides, the $p$-values of $\Omega$ are less than 0.05 for "ENSHA vs. MOEA/D" and "ENSHA vs. SPEAII", so that ENSHA can obtain more efficient nondominated solutions than MOEA/D and SPEAII. Hence, ENSHA has better performance than the other four algorithms. Furthermore, we draw the box plots of MOPSO, MOEA/D, MOGLS, SPEAII and ENSHA in terms of instances 01a, mt10c1, setb4c9 and seti5cc, as shown in Fig. 17. These plots verify the robustness and effectiveness of our ENSHA.

Table 17
Comparisons of MOPSO, MOEA/D, MOGLS, SPEAII and NSHA ( $\Omega$ )
Table 18
Results of ANOVA for three metrics (state-of-the-art algorithms and ENSHA).
Metric $F$-value $p$-value Rank
$\gamma \quad 116.70 \quad 0.00 \quad 3$
$\Delta \quad 398.74 \quad 0.00 \quad 2$
$\Omega \quad 490.83 \quad 0.00 \quad 1$

### 5.7. Discussions

In this subsection, we will conduct discussions on two issues: (1) The approximations of $A P F$ and $P F$; (2) The trends of the values of NB obtained by ENSHA and other compared algorithms. The aim of the former is to show the reasonability of constructing the APF from the union of $K$ sets of nondominated solutions $S_{1} \cup, \ldots, \cup S_{k}$. And the latter is to systematically
assess the solution quality of the proposed ENSHA. Specially, all algorithms in the following discussions are classified into two groups: (1) Group 1: NSGAII\&ENSHA_V\&ENSHA; (2) Group 2: MOPSO\&MOEA/D\&MOGLS\&SPEAII\&ENSHA.

### 5.7.1. Approximations of APF and PF

The enumeration method is first executed to obtain the true PFs of two randomly generated small-sized instances, i.e., SI_1 and SI_2. ${ }^{4}$ And then we compare the PFs of SI_1 and SI_2 with the APFs identified from the unions of nondominated solutions of the corresponding algorithms. Noted that the size of SI_1 is $n \times m=$ $6 \times 3$ and $\left[\alpha p r_{1}, \ldots, \alpha p r_{k}\right]=[2,1,2,2,1,2]$, and the size of SI_2 is $n \times m=5 \times 2$ and $\left[\alpha p r_{1}, \ldots, \alpha p r_{k}\right]=[2,2,2,2,2]$. The solution

4 The small-sized instances SI_1 and SI_2 can be downloaded at http://dx. doi.org/10.17632/7xvtnjn3df.1.

Table 19
Results of Tukey's multiple tests (state-of-the-art algorithms and ENSHA).
${ }^{a}$ Upper bound of $95 \%$ CI.
${ }^{b}$ Lower bound of $95 \%$ CI.

![img-30.jpeg](img-30.jpeg)

Fig. 21. Production process of the 6-Ethylchenodeoxycholic acid (C26H44O4).
![img-31.jpeg](img-31.jpeg)

Fig. 22. Box plots for MOPSO, MOEA/D, MOGLS, SPEAII and ENSHA (case study).
spaces of SI_1 and SI_2 contain 226,800 and 113,400 solutions, respectively. For SI_1 and SI_2, we calculate the objectives for each solution and thereby obtain the true PFs ${ }^{5}$ of them. The numbers of solutions in SI_1'PF and SI_2'PF are 4 and 11, respectively.

Using the same stopping conditions and parameters in Sections 5.5 and 5.6, the APFs of SI_1 and SI_2 associated with Groups 1 and 2 can be obtained. The comparisons of APFs and PFs are shown in Fig. 18, which demonstrate that the APF of each group for each instance is a good approximation of the true PF for all instances. Therefore, it is reasonable to use APF for calculating the performance metrics of adopted algorithms.

[^0]5.7.2. Trends of NB regarding Group 1 and Group 2

Based on the comparison results in Sections 5.5 and 5.6, we summarize the trends of the values of NB with regard to Group 1 and Group 2 in Figs. 19 and 20, respectively. We can see that, in terms of Worst, Best and Mean, the values of NB obtained by ENSHA are much better than those of the other algorithms. To sum up, our ENSHA is capable of good performance for solving MOFJSSP_SDST/C.

### 5.8. Real-life case study

A real-life case study is provided to verify the application values of ENSHA. In this case study, we focus on the production process of the 6-Ethylchenodeoxycholic acid (C26H44O4) for a cooperative pharmaceutical enterprise in Kunming, Yunnan,


[^0]:    5 The PFs of SI_1 and SI_2 can be downloaded at https://data.mendeley.com/ datasets/c74ymmgxkp/draft?a=488168aa-20ee-460e-ad68-489c5b2f21ef.

![img-32.jpeg](img-32.jpeg)

Fig. 23. Value paths for MOPSO, MOEA/D, MOGLS, SPEAII and ENSHA (case study).

Table 20
Comparison results based on case study.
China. In the production process of C26H44O4 (see Fig. 21), the CP, which is utilized for purifying the crude materials, can provide the materials with the satisfied purity for its downstream process, i.e., the high-purity preparation (HPP). Based on our survey, the CP is a bottleneck for improving the production efficiency and the quality of final products. The CP for C26H44O4 is a typical kind of MOFJSSP_SDST/C, since the optimization of the makespan and TSC is significant for the overall benefits.

However, in this cooperative enterprise, the decision making of CP is mainly conducted by manual operations since its launch in 2016. Indeed, it is an intractable work for schedulers due to the expensive labor consume. For example, for a practical case with $n \times m=30 \times 5$, it will take about one hour for making the final scheduling scheme. In addition, manual operations may encounter difficulties for multi-objective optimization problem, because of the conflicting features of multiple objectives. Hence, it is both necessary and practical to introduce effective MOEAs in the decision making.

The factory data ${ }^{6}$ of CP from the cooperative enterprise are collected, where there are 30 batches (i.e., products) of crude materials for the C26H44O4 and 5 crystallizers (i.e., machines) with different capacities and working modes. Using the same termination condition and parameters mentioned in Section 5.6, we independently run ENSHA as well as MOPSO, MOEA/D, MOGLS and SPEAII 21 times, and the comparison results are reported in Table 20. Moreover, we draw the box plots of ENSHA and the other four algorithms in Fig. 22. Comparison results and box plots demonstrate that ENSHA is an effective and robust solution method for practical applications. Note that the average CPU time of ENSHA is 131.48 s which is acceptable in real-life environments.

In addition, to show the distributions of obtained nondominated solutions, we draw the multiple objectives on the value paths for MOPSO, MOEA/D, MOGLS, SPEAII and ENSHA in Fig. 23. It is clear from these paths that ENSHA is able to obtain better diversity and convergence of nondominated solutions than the other four algorithms.

Moreover, we have invited three experienced schedulers to independently make the schemes for this case in thirty minutes. ${ }^{7}$ The results of ENSHA and three schedulers are illustrated in Fig. 24. From Fig. 24, it is clear that ENSHA can obtain a number of nondominated solutions with higher diversity and convergence in terms of both the makespan and TSC. Hence, the overall solution quality of ENSHA is obviously better than those manual results. In practical applications, the managers can flexibly select a desirable nondominated solution to serve as their final scheduling scheme. For example, to improve production efficiency, the managers can select a nondominated solution having relative smaller makespan (corresponding to relative larger TSC). On the contrary, to pursue more profit, they can select a nondominated solution with smaller TSC.

From the test results of Sections 5.5 to 5.8, it can be drawn that MCEDA has a powerful search engine for tackling the multiobjective scheduling problems. Unlike the traditional MOEAs (e.g., the above compared algorithms), ENSHA utilizes an EDAbased machine learning mechanism to reserve promising patterns of excellent individuals, which is helpful for effectively guiding the search to promising regions and avoiding the promising patterns being destroyed or inappropriately fused [68,69]. Hence, ENSHA's novel bi-population-oriented evolutionary framework combining both the genetic operators and an EDA-based machine learning mechanism can effectively perform the search in different promising regions of solution space. This is the main reason why ENSHA outperforms those famous MOEAs.

[^0]![img-33.jpeg](img-33.jpeg)

Fig. 24. Results of ENSHA and three schedulers.

## 6. Conclusions and future work

This paper presented an elitist nondominated sorting hybrid algorithm (ENSHA) for solving the multi-objective flexible job-shop scheduling problem with sequence-dependent setup times/costs (MOFJSSP_SDST/C). The objectives of the problem are the minimization of the maximal completion time (i.e., makespan) and the total setup costs (TSC). This is the first report on the application of multi-objective evolutionary algorithm (MOEA) for MOFJSSP with both efficiency-focused and economic focused objectives. Firstly, on the basis of the problem-dependent features of MOFJSSP_SDST/C, the solution representation and three specific job assignment rules were designed. Secondly, a novel and effective bi-population framework was developed to find promising regions in the solution space, in which the main population (MP) was generated by means of the genetic operations with the elitist nondominated sorting scheme. The auxiliary population (AP) was obtained through using a specific EDA-based machine learning mechanism and a PMX-based method. The next generation MP containing excellent individuals in both MP and AP was then achieved via a well-designed cooperation-based refinement strategy. Thirdly, the simulation results and comparisons demonstrated that ENSHA outperforms the state-of-the-art algorithms including NSGAII, MOEA/D, MOGLS and SPEAII. Finally, a real-life case study verified the application values of ENSHA.

In the future, our work is to develop general scheduling software based on ENSHA for pharmaceutical enterprises and investigate the applications of the presented method to the multiobjective scheduling problems with energy consumption.

## Acknowledgments

This research was partially supported by National Science Foundation of China (No. 51665025, No. 71601180, and No. 60904081), Applied Basic Research Key Project of Yunnan, China, and National Key Research and Development Program of China (No. 2017YFB120700).
