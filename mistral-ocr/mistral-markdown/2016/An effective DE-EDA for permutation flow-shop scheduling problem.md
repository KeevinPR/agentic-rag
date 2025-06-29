# An Effective DE-EDA for Permutation Flow-shop Scheduling Problem 

Zuo-cheng Li<br>Institute of Industrial Engineering \& Logistics Optimization Northeastern University Shenyang, China zuocheng_li@163.com

Qingxin Guo<br>Institute of Industrial Engineering \& Logistics Optimization
Northeastern University Shenyang, China guoqingxin@ise.neu.edu.cn

Lixin Tang<br>Institute of Industrial Engineering \& Logistics Optimization Northeastern University Shenyang, China
lixintang@mail.neu.edu.cn


#### Abstract

Aiming at the permutation flow-shop scheduling problem (PFSSP) with makespan criterion, a combination algorithm based on differential evolution (DE) and estimation of distribution algorithm (EDA), namely DE-EDA, is proposed. Firstly, DE-EDA combines the probability-dependent macro information extracted by EDA and the individual-dependent micro information obtained by DE to execute the exploration, which is helpful in guiding the global search to explore promising solutions. Secondly, in order to make DE well suited to solve PFSSP, a convert rule named smallest-ranked-value (SRV) is designed to generate the discrete job permutations from the continuous values. Thirdly, a sequence-learning-based Bayes posterior probability is presented to estimate EDA's probability model and sample new solutions, so that the global information of promising search regions can be learned precisely. In addition, a simple but effective two-stage local search is embedded into DE-EDA to perform the exploitation, and thereafter numerous potential solution(s) with relative better fitness can be exploited in some narrow search regions. Finally, simulation experiments and comparisons based on 29 well-known benchmark instances demonstrate the effectiveness of the proposed DE-EDA.


Keywords-differential evolution; estimation of distribution algorithm; probability model; permutation flow-shop scheduling problem; makespan

## I. INTRODUCTION

With rapid and competitive global economy, production scheduling plays a crucial role in both industrial engineering and logistics optimization fields. This paper deals with the permutation flow-shop scheduling problem (PFSSP) with makespan criterion, which expresses a certain kind of flow shop with simplified technological constraints [1]. As a wellknown problem in the area of scheduling, it has been proved that the PFSSP is NP-hard [2]. Owing to its widespread engineering backgrounds and theoretical values, PFSSP has become one of the hottest issues in the production scheduling fields.

Since Johnson's pioneering work [3], many methods have been developed for solving PFSSP. In all of these approaches, exact algorithms such as the mathematical programming [4], are only suitable for small-size cases. For this reason, constructive heuristic algorithms and evolutionary algorithms have been widely applied to solve PFSSP. In [5], a self-
adaptive iterated local search algorithm was presented for solving PFSSP with total flow time criterion, which utilized a novel strategy to evaluate the neighborhoods around the local optimum and adjust the perturbation strength. Yahyaoui et al. [6] reported an iterated local search (ILS) with a certain kind of variable neighborhood descent (VND) hyper-heuristic, and the objectives of PFSSP to be optimized were the makespan and the total flow time. In [7], a differential evolution hybridized with a problem-dependent local search mechanism was proposed to deal with both single objective and multi-objective PFSSP. Xu et al. [8] aimed at the PFSSP under considering the total flow time objective, and an improved memetic algorithm based on dynamic neighborhood was developed. In their work, the best known Nawaz-Enscore-Ham (NEH) [9] heuristic was used to construct the dynamic neighborhood, and thereafter a diversity index strategy is developed to enhance the ability associated with overcoming the local optima. And meanwhile, the enhanced particle swarm optimization (PSO), such as PSO with variable neighborhood search (PSOVNS) [10], PSObased memetic algorithm (PSOMA) [11], also performed well in obtaining PFSSP's approximately optimal solution. Recently, relevant attentions have been captured to extend the latest newborn evolutionary algorithm to solve PFSSP. Lin et al. [12] reported a hybrid evolutionary algorithm that is the hybrid backtracking search algorithm (HBSA), which was proposed for PFSSP to minimize the makespan.

As important branches of evolutionary algorithms, differential evolution (DE) [13, 14] and estimation of distribution algorithm (EDA) have been applied to solve a wide set of optimization problems successfully. The individualdependent micro information of promising solutions can be obtained by DE's mutation and crossover operations, but the global information is somewhat insufficient to be considered. Fortunately, EDA provides a powerful tool to characterize the distribution of the promising search regions, and the probability-dependent macro information can be captured to guide the exploration. Thus, not only does the DE-EDA extract the macro information to estimate the probability distribution of the solution space, but it also considers the micro information to create new individuals. That is, combining the DE and EDA is helpful in balancing the micro and macro information of the search space. Based on such a reasonable idea, DE-and-EDA-based algorithms have been proposed to

deal with some certain kinds of optimization problems. Sun et al. [15] firstly put forward a combination framework of DE and EDA, namely DE/EDA for addressing the continuous optimization problem. Zhou et al. [16] presented a combination of DE and EDA for continuous bi-objective optimization. Song and Tang [17] proposed a novel hybrid DE-EDA for dynamic optimization problem. Bai et al. [18] proposed a DE-EDA with feasibility rules for the nonlinear programming (NLP) and mixed integer nonlinear programming (MINLP) models in the area of engineering optimization. To our best knowledge, relevant works associated with applying DE-EDA for scheduling problem is quite scarce, and there is no published works on DE-EDA for PFSSP.

This paper proposes a DE-EDA for PFSSP with makespan criterion. To begin with, DE-EDA combines the probabilitydependent macro information extracted by EDA and the individual-dependent micro information obtained by DE reasonably to execute the exploration. A smallest-ranked-value (SRV) is designed for converting the continuous values to job permutations to make DE suitable for discrete encoded PFSSP. Moreover, a special sequence-learning-based Bayes posterior probability is presented to serve as the probability model of DE-EDA, owing to which the global information of promising search regions can be learned precisely. In addition, a simple but effective two-stage local search is embedded into DE-EDA to perform the exploitation.

The remainder of this paper is organized as follows. In Section II, PFSSP with makespan criterion is briefly introduced and formulated. In Section III, DE-EDA is proposed and described in detail. The experiments and comparisons are provided in Section IV. Finally, we end this paper with some conclusions and future works in Section V.

## II. BRIfe InTRODUCTION to PFSSP

In PFSSP with $n$ jobs and $m$ machines, each job should be processed in a given and defined sequence, every job should visit all machines only once and the job permutation is the same for each machine. Denote $\boldsymbol{\pi}=\left[\pi_{1}, \pi_{2}, \ldots, \pi_{n}\right]$ the sequence or permutation of jobs to be processed, $p\left(\pi_{i}, k\right)$ the processing time of job $\pi_{i}$ on machine $k, C\left(\pi_{i}, k\right)$ the completion time of job $\pi_{i}$ on machine $k$. Without loss of generality, we assume that each job is processed according to the sequence $1,2, \ldots, m$. Then, $C\left(\pi_{i}, k\right)$ can be calculated as follows [2]:

$$
\begin{gathered}
C\left(\pi_{1}, 1\right)=p\left(\pi_{1}, 1\right) \\
C\left(\pi_{i}, 1\right)=C\left(\pi_{i-1}, 1\right)+p\left(\pi_{i}, 1\right), i=2, \ldots, n \\
C\left(\pi_{i}, k\right)=C\left(\pi_{1}, k-1\right)+p\left(\pi_{1}, k\right), k=2, \ldots, m \\
C\left(\pi_{i}, k\right)=\max \left\{C\left(\pi_{i-1}, k\right), C\left(\pi_{i}, k-1\right)\right\}+p\left(\pi_{i}, k\right) \\
i=2, \ldots n, k=2, \ldots, m
\end{gathered}
$$

Hence, the makespan can be defined as

$$
C_{\max }(\pi)=C\left(\pi_{n}, m\right)
$$

The PFSSP with the makespan criterion is to find a schedule in the set of all permutations $\Pi$ as

$$
\boldsymbol{\pi}^{*}=\arg \left\{C_{\max }(\boldsymbol{\pi})\right\} \rightarrow \min , \forall \boldsymbol{\pi} \in \boldsymbol{\Pi}
$$

## III. DE-EDA FOR PFSSP

In this section, we will propose the procedure of DE-EDA after introducing the solution representation and SRV rule, DE with the first stage local search, EDA with sequence-learning mechanism, and the second stage local search.

## A. Solution Representation and SRV Rule

Due to the distinct characters of the individuals in DE and EDA, a central premise should be considered that is to design personalized solution representations for them. In this paper, we utilize a job-based solution representation [1] for EDA, and a continuous representation to represent the individuals of DE. In order to make continuous individuals in DE suitable for discrete encoded PFSSP, we design a named SRV rule for converting the continuous values to job permutations. Let $\boldsymbol{X}_{i}=\left[\begin{array}{c}x_{i, 1}, \cdots, x_{i, n} \\ x_{i, 1}\end{array}\right]$ denote the $i$ th individual in DE's population, and $\boldsymbol{\pi}_{i}=\left[\pi_{i, 1}, \cdots, \pi_{i, n}\right]$ denote its corresponding job permutation. Then, the procedure of SRV is described as follows:

Step 1: Rank $\boldsymbol{X}_{i}$ by ascending order to obtain a new sequence

$$
\tilde{\boldsymbol{X}}_{i}=\left[\tilde{x}_{i, 1}, \ldots, \tilde{x}_{i, n}\right]
$$

Step 2: Calculate the intermediate sequence $\boldsymbol{\psi}_{i}=\left[\psi_{i, 1}, \ldots, \psi_{i, n}\right]$;

$$
\begin{aligned}
& \text { For } l=1 \text { to } n \text { do } \\
& \text { For } l l=1 \text { to } n \text { do } \\
& \text { If } \boldsymbol{X}_{i, 1}=\tilde{\boldsymbol{X}}_{i, l l} \text { then } \\
& \quad \boldsymbol{\psi}_{i l}=l l ; \\
& \quad \text { Break; } \\
& \text { End; } \\
& \text { End; } \\
& \text { End. }
\end{aligned}
$$

Step 3: Obtain final permutation $\boldsymbol{\pi}_{i}$;

$$
\begin{aligned}
& \text { For } l=1 \text { to } n \text { do } \\
& \quad \pi_{i, \psi_{i, l}}=l \text {; } \\
& \text { End. }
\end{aligned}
$$

Obviously, the conversion process of SRV is very simple to be addressed, which will be useful to convert the discrete job permutation to DE's continuous sequence.

## B. DE with the First Stage Local Search (DE_FSLS)

In DE-EDA, the role of DE lies in obtaining the individualdependent micro information to guide the global search to promising solution regions. In this paper, we adopt the mutation and crossover approaches presented in [7], and the so-called DE/rand-to-best/1/exp is used to perform the parallel search. And, in order to refine the solutions obtained by DE's mutation and crossover, an Interchange-based local search with first move strategy (i.e., the first stage local search) is

embedded into DE. This means that the Interchange-based local search needs to be applied for each individual before executing DE's selection operation.

Denote FirstStageLS $\left(\boldsymbol{X}_{i}(\right.$ gen $\left.))$ the procedure of first stage local search at generation gen, Interchange $\left(\boldsymbol{\pi}_{i}(\right.$ gen $\left.), u, v\right)$ the interchange of the job at the $i$ th dimension and the job at the $v$ th dimension. Then, the procedure of FirstStageLS $\left(\boldsymbol{X}_{i}(\right.$ gen $\left.))$ is given as follows:

Step 1: Set $l=0$.
Step 2: Convert individual $\boldsymbol{X}_{i}$ (gen) to a schedule $\boldsymbol{\pi}_{i}$ (gen) via the SRV rule.
Step 3: Set $\boldsymbol{\pi}_{i_{-} 0}=\boldsymbol{\pi}_{i}$ (gen).
Step 4: Set $l=l+1$ and $\boldsymbol{\pi}_{i_{-} 1}=\boldsymbol{\pi}_{i_{-} 0}$; if $l>(n(n-1)) / 2$, then go to Step 7.
Step 5: Randomly select $u$ and $v, \boldsymbol{\pi}_{i_{-} 1}=\operatorname{Interchange}\left(\boldsymbol{\pi}_{i_{-} 0}, u, v\right)$, where $u \neq v$.
Step 6: If $f\left(\boldsymbol{\pi}_{i_{-} 1}\right) \geq f\left(\boldsymbol{\pi}_{i_{-} 0}\right)$, then go to Step 4.
Step 7: Output $\boldsymbol{\pi}_{i}$ (gen) $=\boldsymbol{\pi}_{i_{-} 1}$.
Step 8: Convert $\boldsymbol{\pi}_{i}$ (gen) to $\boldsymbol{X}_{i}$ (gen) according to the conversion process of SRV's.

Denote $\boldsymbol{p o p}($ gen $)$ the DE's population with size $P S$ at generation gen, $\boldsymbol{X}^{\text {fhen }}$ (gen) the local best individual of current population $\boldsymbol{p o p}(\mathrm{gen})$, and $\boldsymbol{T}_{i}(\mathrm{gen})=\left[t_{i, 1}, \ldots, t_{i, n}\right]$ the $i$ th trial individual at generation gen. Then, the procedure of DE_FSLS is given as follows:
Step 1: Set $i=1$.
Step 2: Execute DE's mutation and crossover and create the $i$ th trial individual $\boldsymbol{T}_{i}$ (gen).
Step 3: Perform DE's Selection;
Step 3.1: Set $\boldsymbol{T}_{i_{-} 0}=\operatorname{FirstStageLS}\left(\boldsymbol{T}_{i}(\right.$ gen $\left.)) ;\right.$
Step 3.2: If $f\left(\boldsymbol{T}_{i_{-} 0}\right)<f\left(\boldsymbol{T}_{i}(\right.$ gen $\left.))\right.$, then $\boldsymbol{T}_{i}(\mathrm{gen})=\boldsymbol{T}_{i_{-} 0}$;
Step 3.3: If $f\left(\boldsymbol{T}_{i}(\right.$ gen $\left.)\right)<f\left(\boldsymbol{X}_{i}(\right.$ gen $\left.-1)\right)$, then $\boldsymbol{X}_{i}(\mathrm{gen})$
$=\boldsymbol{T}_{i}(\mathrm{gen})$; else $\boldsymbol{X}_{i}(\mathrm{gen})=\boldsymbol{X}_{i}(\mathrm{gen}-1)$;
Step 3.4: If $f\left(\boldsymbol{X}_{i}(\right.$ gen $\left.))<f\left(\boldsymbol{X}^{\text {fhen }}(\right.\right.$ gen $\left.\left.))\right)$, then set

$$
\boldsymbol{X}^{\text {fhen }}(\text { gen })=\boldsymbol{X}_{i}(\text { gen })
$$

Step 4: Set $i=i+1$; if $i \leq P S$, then go to Step 2.
Step 5: Output $\boldsymbol{X}^{\text {fhen }}$ (gen), pop(gen), and their makespan.
Obviously, the initial population $\boldsymbol{p o p}(0)$ is randomly generated from a uniform distribution $U[L B, U B]$, where $L B$ and $U B$ denotes the lower bound and upper bound of the DE's individuals respectively.

## C. EDA with Sequence-learning Mechanism (EDA_SLM)

As mentioned, DE-EDA extracts the probability-dependent macro information according to the unique operations of EDA. In this subsection, we will propose the EDA_SLM in detail.

1) Probability Model, Initialization, and Updating Method

The probability model is a key element of EDA for executing global exploration. In this paper, the probability matrix is designed as [19]

$$
\boldsymbol{P}_{\text {matrix }}(\text { gen })=\left(\begin{array}{ccc}
p_{11}(\text { gen }) & \ldots & p_{1 n}(\text { gen }) \\
\vdots & \ddots & \vdots \\
p_{n 1}(\text { gen }) & \cdots & p_{n n}(\text { gen })
\end{array}\right)_{n \in n}
$$

where $\sum_{u=1}^{n} p_{n i j}(\text { gen })=1$, and $p_{n i j}(\text { gen })$ is the probability of job $w$ appearing in the $j$ th position of $\boldsymbol{\pi}$ at generation gen. It is important to note that the probability matrix can be initialized (when gen $=0$ ) or restarted (when gen $>0$ ) by setting $p_{n i j}(\text { gen })=1 / n$.

Denote $\boldsymbol{\pi}^{\text {fhen }}(\text { gen })=\left[\pi_{1}^{\text {fhen }}, \pi_{2}^{\text {fhen }}, \ldots, \pi_{n}^{\text {fhen }}\right]$ the local best individual (permutation) at generation gen, $L R$ the learning rate. The matrix $\boldsymbol{P}_{\text {matrix }}(\mathrm{gen}+1)$ is updated according to $\boldsymbol{\pi}^{\text {fhen }}(\mathrm{gen})$ by the following two steps:
Step 1: Set $x=\pi_{j}^{\text {fhen }}(g e n)$ and $p_{i j}(g e n+1)=p_{i j}(g e n)+L R$ for $j=1, \ldots, n$.
Step 2: Set $p_{n i j}(\text { gen }+1)=p_{n i j}(\text { gen }+1) / \sum_{j=1}^{n} p_{i j}(\text { gen }+1)$ for $w=1, \ldots, n$, and $j=1, \ldots, n$.

## 2) Sequence-learning Mechanism

Unlike other types of combinatorial optimization problems (such as assignment problems [20]), the objective values of PFSSP inherently depend on the sequence and dependency relationships among these jobs. Thus, to define and extract the interactions or dependencies of jobs is helpful in obtaining more valuable and precise global information of promising solutions. In this paper, the sequence-learning matrix is defined to record the sequence and dependency relationships.

$$
\boldsymbol{T}_{\text {matrix }}(g e n)=\left(\begin{array}{ccc}
t_{11}(\text { gen }) & \ldots & t_{1 n}(\text { gen }) \\
\vdots & \ddots & \vdots \\
t_{n 1}(\text { gen }) & \cdots & t_{n n}(\text { gen })
\end{array}\right)_{n \in n}
$$

where the element $t_{n i j}$ (gen) denotes the accumulation times of job $w$ right before job $j$. Obviously, $\boldsymbol{T}_{\text {matrix }}(g e n)$ can be initialized or restarted by setting $t_{n i j}(\text { gen }=0)=0$ or $t_{n i j}(\text { gen }>0)=0$. And, the $\boldsymbol{T}_{\text {matrix }}(g e n)$ is updated according to $\boldsymbol{\pi}^{\text {fhen }}(g e n)$ as follows:
Step 1: Set $j=1$.
Step 2: Set $x_{1}=\pi_{j}^{\text {fhen }}(g e n), x_{2}=\pi_{j+1}^{\text {fhen }}(g e n)$.
Step 3: Set $t_{x_{1} x_{2}}(\text { gen })=t_{x_{2} x_{1}}(\text { gen })+1$ and $j=j+1$; if $j<n$, then go to Step 2.
Setup 4: Output $T_{\text {matrix }}$ (gen).
Then, we can obtain the two-dimensional joint distribution law of job $w$ right before job $j$ as

$$
\boldsymbol{Q}_{\text {matrix }}(g e n)=\left(\begin{array}{ccc}
q_{11}(\text { gen }) & \ldots & q_{1 n}(\text { gen }) \\
\vdots & \ddots & \vdots \\
q_{n 1}(\text { gen }) & \cdots & q_{n n}(\text { gen })
\end{array}\right)_{n \in n}
$$

where

$$
q_{s i j}(g e n)=t_{s i j}(g e n) / \sum_{i=1}^{n} \sum_{j=1}^{n}\left(t_{s i j}(g e n) / g e n\right)
$$

## 3) New Population Generation Method

In DE-EDA, we utilize a sequence-learning-based Bayes posterior probability to estimate the probability and then sample new solutions. Based on Bayes posterior probability, each random variable's probability value can be seen as the condition probability of its previous variable or variables. Denote $r_{s i j}$ the condition distribution law (CDL) of the $j$ th dimension random variable, which satisfying the condition that the $(j-1)$ th position of $\pi$ has been filled by new generated job $\pi_{j-1}$. Then, $r_{s i j}$ can be calculated as follow:

$$
r_{s i j}(g e n)=\frac{p_{s i j}(g e n) \cdot q_{w \pi_{j-1}}(g e n)}{p_{\pi_{j-1} j}(g e n)}, w=1, \ldots, n, j=2, \ldots, n
$$

where $r_{w 1}=p_{w 1}$, for $w=1, \ldots, n$.
Based on above analysis, the new population of EDA can be generated as follows:
Step 1: Set $i=1$.
Step 2: Generate a new individual $\pi_{i}(g e n+1)$;
For $j=1$ to $n$ do
For $w=1$ to $n$ do
Calculate $r_{s i j}(g e n)$;
End;
For $w=1$ to $n$ do

$$
r_{s i j}(g e n)=r_{s i j}(g e n) / \sum_{j=1}^{n} r_{s i j}(g e n)
$$

End;
Randomly create a probability $r \sim[0,1)$;
If $r \sim\left[0, r_{1 j}(g e n)\right)$ then
Set $C J=1$;
End;
For $w=1$ to $n$ do
If $r \sim\left[\sum_{j=1}^{n} r_{s i j}(g e n), \sum_{j=1}^{n+1} r_{s i j}(g e n)\right)$ then
Set $C J=w+1$;
End;
End;
For $l=j+2$ to $n$ do
$p_{C J l}=0$;
End;
Set $\pi_{l j}(g e n+1)=C J$;
End.
Step 3: Set $i=i+1$.
Step 4: If $i \leq P S$, then go to Step 2.

## 4) Restarting Strategy

Let $\boldsymbol{R S T}=\{1 / s p, \ldots, t / s p, \ldots, s p-1 / s p\}$ denote the restarting index and genMax denote the maximum generation. That is, if gen $=\operatorname{trunc}((t / s p) \cdot g e n M a x)$, then we
restart $P_{\text {matrix }}(g e n)$ and $T_{\text {matrix }}(g e n)$ by utilizing the restarting method mentioned in subsection III-C-1 and III-C-2. Denote $T C$ the training constant, and thereafter the procedure of restarting strategy is presented as follows:
Step 1: Restart $\boldsymbol{P}_{\text {matrix }}(g e n)$ and $\boldsymbol{T}_{\text {matrix }}(g e n)$ respectively.
Step 2: Training $P_{\text {matrix }}(g e n)$;
For $i=1$ to $T C$ do
Update $\boldsymbol{P}_{\text {matrix }}(g e n)$ according to $\boldsymbol{\pi}^{\text {theor }}(g e n)$;
End.
Step 3: Output $\boldsymbol{P}_{\text {matrix }}(g e n)$ and $\boldsymbol{T}_{\text {matrix }}(g e n)$.

## D. The Second Stage Local Search

As mentioned in [7], an Insert-based local search (i.e., the second stage local search) is designed and introduced into DEEDA to perform a wider and deeper local exploitation. Denote Insert $\left(\pi_{i}(g e n, u, v)\right)$ the function associated with inserting the job at the $v$ th dimension to the $u$ th dimension, where $u<v$. Denote $\boldsymbol{X}_{\text {random }}(g e n)$ a randomly selected individual from current DE's population. Then, the procedure of Insert-based local search is given as follows:
Step 1: Set $l=0$.
Step 2: Set $\boldsymbol{\pi}_{i, 0}=\boldsymbol{\pi}^{\text {theor }}(g e n)$.
Step 3: Set $l=l+1$ and $\boldsymbol{\pi}_{i, 1}=\boldsymbol{\pi}_{i, 0}$; if $l>10 \cdot n$, then go to Step 6.
Step 4: Randomly select $u$ and $v$, where $u<v$;

$$
\boldsymbol{\pi}_{i, 1}=\operatorname{Insert}\left(\boldsymbol{\pi}_{i, 0}, u, v\right)
$$

Step 5: If $f\left(\boldsymbol{\pi}_{i, 1}\right) \geq f\left(\boldsymbol{\pi}_{i, 0}\right)$, then go to Step 3.
Step 6: Output $\boldsymbol{\pi}^{\text {theor }}(g e n)=\boldsymbol{\pi}_{i, 1}$.
Step 7: Randomly select $\boldsymbol{X}_{\text {random }}(g e n)$.
Step 8: Convert $\boldsymbol{\pi}^{\text {theor }}(g e n)$ to $\boldsymbol{X}^{\text {theor }}(g e n)$ according to $\boldsymbol{X}_{\text {random }}(g e n)$ by using SRV's conversion process.

## E. Procedure of DE-EDA

Denote $\boldsymbol{\pi}^{\text {gheor }}$ the global best individual, pop' (gen) the EDA's population, Then, we present the procedure of DE-EDA as follows:
Step 1: Initialization;
Step 1.1: Set gen $=0$;
Step 1.2: Randomly generate DE's initial population pop(0) and obtain the schedules by using SRV in III-A; and calculate their makespan;
Step 1.3: Obtain $\boldsymbol{\pi}^{\text {theor }}(0)$ and $\boldsymbol{X}^{\text {theor }}(0)$, and set $\boldsymbol{\pi}^{\text {gheor }}$

$$
=\boldsymbol{\pi}^{\text {theor }}(0)
$$

Step 1.4: Initialize $\boldsymbol{P}_{\text {matrix }}(0)$ and $\boldsymbol{T}_{\text {matrix }}(0)$ by using the initialization method in subsection III-C.
Step 2: Set gen $=$ gen +1 .
Step 3: Determine whether or not to execute the restarting strategy via the restarting strategy in III-C.

Step 4: Perform EDA;
Step 4.1: Update the probability matrix by using the update methods in III-C;
Step 4.2: Generate new population pop'(gen) by using the new population generation methods in III-C, and calculate their objective values;
Step 4.3: Update $\boldsymbol{\pi}^{\text {phot }}$ (gen);
Step 4.4: Update $\boldsymbol{X}^{\text {phot }}$ (gen) according to $\boldsymbol{\pi}^{\text {phot }}$ (gen) and a randomly selected $\boldsymbol{X}_{\text {random }}$ (gen-1) by using SRV's conversion process.
Step 5: Perform DE_FSLS mentioned in III-B, and update $\boldsymbol{\pi}^{\text {phot }}$ (gen) and $\boldsymbol{X}^{\text {phot }}$ (gen).
Step 6: Perform the Insert-based local search by using the method in subsection III-D, and update $\boldsymbol{\pi}^{\text {phot }}$ (gen) and $\boldsymbol{X}^{\text {phot }}$ (gen).
Step 7: Update $\boldsymbol{\pi}^{\text {phot }}$
Step 8: If gen $<$ genMax, then go to Step2.
Step 9: Output $\boldsymbol{\pi}^{\text {phot }}$.

## IV. SIMULATION EXPERIMENTS AND COMPARISONS

## A. Experimental Setup

In this paper, 29 well-known benchmark instances are used to test the proposed DE-DEA. Among them, the first eight instances, namely Car1, Car2 through to Car8 designed by Carlier [21], and the other 21 instances are named Rec01, Rec03 through to Rec41 proposed by Reeves [22]. So far, these instances have been utilized as benchmarks for a wide set of algorithms by many researchers.

The proposed DE-EDA is coded with Visual studio 2008, $C++$ language, and executed on PC Intel Core-15 3.30GHz processor with 4 GB memory. For each instance, DE-EDA is run 20 times independently, and the maximum generation genMax is set to 1000 serving as the terminal condition. In order to carry out relatively fair comparisons, three widespread evaluation metrics are referenced [12], as follows:

$$
\begin{aligned}
& B R E=\frac{\min (\text { solutions })-C^{*}}{C^{*}} \times 100 \%, \\
& A R E=\frac{\text { average }(\text { solutions })-C^{*}}{C^{*}} \times 100 \%, \\
& W R E=\frac{\max (\text { solutions })-C^{*}}{C^{*}} \times 100 \%
\end{aligned}
$$

where $C^{*}$ denotes the best known solution, and $B R E, A R E$, and $W R E$ denotes the best relative error, average relative error, and worst relative error to $C^{*}$ respectively.

## B. Parameters Analysis and Setting

In DE-EDA, there exist eight parameters, i.e., the scaling factor $F$, the crossover parameter $C R$, the learning rate $L R$,
population size $P S$, the training constant $T C$, the restarting constant $s p$, and the lower (upper) bound $L B(U B)$. Obviously, $s p$ is closely related to genMax, and $L B(U B)$ can be set to well-known values in previous woks. Hence, we set $s p=5$, $L B=0$, and $U B=4$ without any discussion. For the first five key parameters (i.e., $F, C R, L R, P S$, and $T C$ ), we carry out the design-of-experiment (DOE) by using all the test instances mentioned in subsection IV-A. Different combinations of these parameters are listed in Table I.

TABLE I. Different COMBINATIONS of PARAMETERS

| Parameters | Factor levels |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | $\mathbf{1}$ | $\mathbf{2}$ | $\mathbf{3}$ | $\mathbf{4}$ |  |
| $F$ | 0.3 | 0.5 | 0.7 | 0.9 |  |
| $C R$ | 0.05 | 0.1 | 0.15 | 0.2 |  |
| $L R$ | 0.01 | 0.02 | 0.03 | 0.04 |  |
| $P S$ | 30 | 50 | 70 | 100 |  |
| $T C$ | 20 | 50 | 80 | 100 |  |

In the DOE, we choose the orthogonal array. That is, the total number of experiments is 16 , the number of parameters is 5 , and the number of factor levels is 4 . The evaluation criteria is the $\overline{A R E}$ (i.e., the average value of $A R E$ ). The orthogonal array and the obtained are listed in Table II.

TABLE II. Orthogonal ARRAY and the Obtained $\overline{A R E}$

| No. | Parameter combinations |  |  |  |  | $\overline{A R E}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | $\boldsymbol{F}$ | $\boldsymbol{C R}$ | $\boldsymbol{L R}$ | $\boldsymbol{P S}$ | $\boldsymbol{T C}$ |  |
| 1 | 1 | 1 | 1 | 1 | 1 | 1.083 |
| 2 | 1 | 2 | 2 | 2 | 2 | 1.129 |
| 3 | 1 | 3 | 3 | 3 | 3 | 1.196 |
| 4 | 1 | 4 | 4 | 4 | 4 | 1.243 |
| 5 | 2 | 1 | 2 | 3 | 4 | 1.146 |
| 6 | 2 | 2 | 1 | 4 | 3 | 1.158 |
| 7 | 2 | 3 | 4 | 1 | 2 | 1.370 |
| 8 | 2 | 4 | 3 | 2 | 1 | 1.220 |
| 9 | 3 | 1 | 3 | 4 | 2 | 1.219 |
| 10 | 3 | 2 | 4 | 3 | 1 | 1.306 |
| 11 | 3 | 3 | 1 | 2 | 4 | 1.223 |
| 12 | 3 | 4 | 2 | 1 | 3 | 1.328 |
| 13 | 4 | 1 | 4 | 2 | 3 | 1.391 |
| 14 | 4 | 2 | 3 | 1 | 4 | 1.447 |
| 15 | 4 | 3 | 2 | 4 | 1 | 1.284 |
| 16 | 4 | 4 | 1 | 3 | 2 | 1.325 |

From Table II, we can obtain the response values $(R V)$ of each parameter in Table III, and the trend of each factor level can be illustrated by Fig. 1.

TABLE III. THE $R V$ OF EACH PARAMETER

| Parameters | $\boldsymbol{R} \boldsymbol{V}$ |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | $\boldsymbol{F}$ | $\boldsymbol{C R}$ | $\boldsymbol{L R}$ | $\boldsymbol{P S}$ | $\boldsymbol{T C}$ |
| 1 | 1.163 | 1.210 | 1.197 | 1.307 | 1.223 |
| 2 | 1.224 | 1.260 | 1.222 | 1.241 | 1.261 |
| 3 | 1.269 | 1.268 | 1.271 | 1.243 | 1.268 |
| 4 | 1.362 | 1.279 | 1.328 | 1.226 | 1.265 |
| range | 0.199 | 0.069 | 0.131 | 0.081 | 0.045 |
| grade | 1 | 4 | 2 | 3 | 5 |

![img-0.jpeg](img-0.jpeg)

Fig. 1 The trend of each factor level
![img-1.jpeg](img-1.jpeg)

Fig. 2. The trend of makespan during the iteration (The horizontal and vertical axis represent the generation and makespan respectively)

Based on the above analysis, the conclusion can be drawn that DE-EDA is less sensitive to its parameters. And, the parameters of DE-EDA are set as follows: $F=0.3, C R=0.05$, $L R=0.01, P S=100$, and $T C=20$.
B. Comparisons of DE-EDA, PSOVNS, PSOMA, HGA, and NEH

In this subsection, we compare DE-EDA with other three state-of-the-art PFSSP solvers, i.e. PSOVNS [10], PSOMA [11], and HGA [2]. Besides, we carry out a comparison with NEH (reported in [7]), which is one of the best deterministic heuristics for PFSSP known so far. For NEH, only the relative error $(R E)$ values to $C^{*}$ are given. We accept the results reported by relevant papers, and do not code and execute these algorithms. The comparison results are listed in Table IV. Also, in order to analyze the convergence feature of DE-EDA, we make an observation on the trend of makespan during its
iteration. The trends of makespan for 4 instances (i.e., Rec09, Rec21, Rec35, and Rec39) are shown in Fig. 2.

From Fig.2, we can draw a conclusion that the proposed DE-EDA has a faster convergence associated with obtaining high-quality solution (see Rec09 and Rec35). Meanwhile, it has a potential ability to perform a wider and deeper search to avoid falling into local optimum at the last phase of iteration (see Rec21 andRec39).

Seeing from Table IV, it is shown that the solution quality of DE-EDA is acceptable, and it is quite competitive among the five compared algorithms. The values of NoB (number of best) obtained by DE-EDA are much better than PSOVNS, PSOMA, HGA, and NEH with respect to ARE, WRE, and RE respectively. Thus, DE-EDA is an effective algorithm for the permutation flow-shop scheduling problem.

TABLE IV. COMPARISONS OF DE-EDA, PSOVNS, PSOMA, HGA, AND NEH

| Ins. | n, $\boldsymbol{m}$ | $\boldsymbol{C}^{\mathbf{x}}$ | PSOVNS |  |  | PSOMA |  |  | HGA |  |  | NEH |  | DE-EDA |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  | BRE | ARE | WRE | BRE | ARE | WRE | BRE | ARE | WRE | RE | BRE | ARE | WRE |
| Car1 | 11,5 | 7038 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Car2 | 13,4 | 7166 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 2.93 | 0.00 | 0.00 | 0.00 |
| Car3 | 12,5 | 7312 | 0.00 | 0.42 | 1.19 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.79 | 0.00 | 0.00 | 0.00 |
| Car4 | 14,4 | 8003 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.39 | 0.00 | 0.00 | 0.00 |
| Car5 | 10,6 | 7720 | 0.00 | 0.04 | 0.39 | 0.00 | 0.02 | 0.38 | 0.00 | 0.00 | 0.00 | 4.24 | 0.00 | 0.00 | 0.00 |
| Car6 | 8,9 | 8505 | 0.00 | 0.08 | 0.76 | 0.00 | 0.11 | 0.76 | 0.00 | 0.04 | 0.76 | 3.62 | 0.00 | 0.00 | 0.00 |
| Car7 | 7,7 | 6590 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 6.34 | 0.00 | 0.00 | 0.00 |
| Car8 | 8,8 | 8366 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 1.09 | 0.00 | 0.00 | 0.00 |
| Rec01 | 20,5 | 1247 | 0.16 | 0.17 | 0.32 | 0.00 | 0.14 | 0.16 | 0.00 | 0.14 | 0.16 | 8.42 | 0.00 | 0.02 | 0.16 |
| Rec03 | 20,5 | 1109 | 0.00 | 0.16 | 0.18 | 0.00 | 0.19 | 0.72 | 0.00 | 0.09 | 0.18 | 6.58 | 0.00 | 0.00 | 0.00 |
| Rec05 | 20,5 | 1242 | 0.24 | 0.25 | 0.42 | 0.24 | 0.25 | 0.40 | 0.00 | 0.29 | 1.13 | 4.83 | 0.00 | 0.23 | 0.24 |
| Rec07 | 20,10 | 1566 | 0.70 | 1.10 | 1.41 | 0.00 | 0.99 | 1.15 | 0.00 | 0.69 | 1.15 | 5.36 | 0.00 | 0.00 | 0.00 |
| Rec09 | 20,10 | 1537 | 0.00 | 0.65 | 1.37 | 0.00 | 0.62 | 1.69 | 0.00 | 0.64 | 2.41 | 6.77 | 0.00 | 0.01 | 0.26 |
| Rec11 | 20,10 | 1431 | 0.07 | 1.15 | 2.66 | 0.00 | 0.13 | 0.98 | 0.00 | 1.10 | 2.59 | 8.25 | 0.00 | 0.00 | 0.00 |
| Rec13 | 20,15 | 1930 | 1.04 | 1.79 | 2.64 | 0.26 | 0.89 | 1.50 | 0.36 | 1.68 | 3.06 | 7.62 | 0.00 | 0.58 | 1.04 |
| Rec15 | 20,15 | 1950 | 0.77 | 1.49 | 2.26 | 0.05 | 0.63 | 1.08 | 0.56 | 1.12 | 2.00 | 4.92 | 0.15 | 0.57 | 0.82 |
| Rec17 | 20,15 | 1902 | 1.00 | 2.45 | 3.37 | 0.00 | 1.33 | 2.16 | 0.95 | 2.32 | 3.73 | 7.47 | 0.37 | 1.08 | 2.10 |
| Rec19 | 30,10 | 2093 | 1.53 | 2.10 | 2.53 | 0.43 | 1.31 | 2.10 | 0.62 | 1.32 | 2.25 | 6.64 | 0.91 | 1.43 | 1.86 |
| Rec21 | 30,10 | 2017 | 1.49 | 1.67 | 2.03 | 1.44 | 1.60 | 1.64 | 1.44 | 1.57 | 1.64 | 4.56 | 1.14 | 1.55 | 1.64 |
| Rec23 | 30,10 | 2011 | 1.34 | 2.11 | 2.88 | 0.60 | 1.31 | 2.04 | 0.40 | 0.87 | 1.69 | 10.00 | 0.80 | 1.20 | 1.74 |
| Rec25 | 30,15 | 2513 | 2.39 | 3.17 | 3.78 | 0.84 | 2.09 | 3.23 | 1.27 | 2.54 | 3.98 | 6.96 | 1.23 | 2.25 | 3.22 |
| Rec27 | 30,15 | 2373 | 1.73 | 2.46 | 3.20 | 1.35 | 1.61 | 2.40 | 1.10 | 1.83 | 4.00 | 8.51 | 1.22 | 1.69 | 2.19 |
| Rec29 | 30,15 | 2287 | 1.97 | 3.11 | 4.07 | 1.44 | 1.89 | 2.49 | 1.40 | 2.70 | 4.20 | 5.42 | 1.62 | 2.32 | 2.89 |
| Rec31 | 50,10 | 3045 | 2.59 | 3.23 | 4.24 | 1.51 | 2.25 | 2.69 | 0.43 | 1.34 | 2.50 | 10.28 | 1.84 | 2.71 | 3.65 |
| Rec33 | 50,10 | 3114 | 0.84 | 1.01 | 1.48 | 0.00 | 0.65 | 0.83 | 0.00 | 0.78 | 0.83 | 4.75 | 0.35 | 0.77 | 0.87 |
| Rec35 | 50,10 | 3277 | 0.00 | 0.04 | 0.09 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 5.01 | 0.00 | 0.00 | 0.00 |
| Rec37 | 75,20 | 4951 | 4.38 | 4.95 | 5.74 | 2.10 | 3.54 | 4.04 | 3.75 | 4.90 | 6.18 | 9.14 | 3.98 | 5.09 | 6.14 |
| Rec39 | 75,20 | 5087 | 2.85 | 3.37 | 3.95 | 1.55 | 2.43 | 2.83 | 2.20 | 2.79 | 4.48 | 8.65 | 2.32 | 3.37 | 4.44 |
| Rec41 | 75,20 | 4960 | 4.17 | 4.87 | 5.59 | 2.64 | 3.68 | 4.05 | 3.64 | 4.92 | 5.91 | 10.69 | 3.75 | 5.19 | 6.29 |
| NoB |  |  | 11 | 5 | 5 | 22 | 15 | 12 | 20 | 10 | 12 | 1 | 17 | 19 | 22 |

## V. CONCLUSIONS AND FUTURE WORKS

This paper proposes a DE-EDA for PFSSP with makespan criterion. In DE-EDA, the probability-dependent macro information and the individual-dependent micro information are combined reasonably to execute the exploration. To make DE suitable for discrete encoded PFSSP, a smallest-rankedvalue is designed for converting the continuous values to job permutations. Moreover, a special sequence-learning-based Bayes posterior probability is presented to serve as the probability model of DE-EDA. In addition, a simple but effective two-stage local search is embedded into DE-EDA to improve the exploitation. Simulation experiments and comparisons based on 29 benchmark instances verify that the proposed DE-EDA is a competitive and effective algorithm for PFSSP. Our future work is to develop effective hybrid algorithm based on DE and EDA for other production scheduling problem.

## ACKNOWLEDGEMENTS

This research is supported by the 111 Project (B16009), the National Natural Science Fund of China for Major International (Regional) Joint Research Project (Grant No. 71520107004), the Fund for the National Natural Science Foundation of China(Grant No. 61374203)

## REFERENCES

[1] L. Wang, "Shop scheduling with genetic algorithms," Tsinghua University Press \& Springer, 2003,Beijing, China.
[2] L. Wang and D. Z. Zheng, "An effective hybrid heuristic for flow shop scheduling," International Journal of Advanced Manufacturing Technology, vol. 21, pp. 38-44, 2003.
[3] S. M Johnson, "Optimal two- and three-stage production schedules with setup times included," Naval Research Logistics Quarterly, vol. 1, pp. 6168,1954 .
[4] B. J. Lageweg, J. K. Lenstra, and A. H. G. Rinnooy Kan, "A general bounding scheme for the permutation flow-shop problem," Operations Research, vol. 26, pp. 53-67, 1978.
[5] X. Dong, M. Nowak, P. Chen, and Y. Lin, "A self-adaptive iterated local search algorithm on the permutation flow shop scheduling problem," IEEE International Conference Informatics in Control, Automation and Robotics (ICINCO), pp. 378-384, 2014.
[6] H. Yahyaoui, S. Krichen, B. Derbel, and E. G. Talbi, "A hybrid ILSVND based hyper-heuristic for permutation flowshop scheduling problem," Procedia Computer Science, vol. 60, pp. 632-641, 2015.
[7] B. Qian, L. Wang, R. Hu, W. L. Wang, D. X. Huang, and X. Wang, "A hybrid differential evolution method for permutation flow-shop scheduling," International Journal of Advanced Manufacturing Technology, vol. 38, pp. 757-777, 2008.
[8] J. Xu, Y. Yin, T. C. E. Cheng, C. C. Wu, and S. Gu, "An improved memetic algorithm based on a dynamic neighbourhood for the permutation flowshop scheduling problem," International Journal of Production Research, vol. 52, pp. 1188-1199, 2014.
[9] M. Nawaz, E. Jr. Enscore, and I. Ham, "A heuristic algorithm for the m machine, n -job flow-shop sequencing problem," Omega, vol. 11, pp. 9195, 1983.
[10] M. F. Tasgetiren, Y. C. Liang, M. Sevkli, and G. Gencylmaz, "A particle swarm optimization algorithm for makespan and total flowtime minimization in the permutation flowshop sequencing problem," European Journal of Operational Research, vol. 177, pp. 1930-1947, 2007.
[11] B. Liu, L. Wand, and Y. H. Jin, "An effective PSO-based memetic algorithm for flow shop scheduling," IEEE Transactions on Systems Man \& Cybernetics, vol. 37, pp. 18-27, 2007.
[12] Q. Lin, L. Gao, X. Li, and C. Zhang, "A hybrid backtracking search algorithm for permutation flow-shop scheduling problem," Computers \& Industrial Engineering, vol. 85, pp. 437-446, 2015.
[13] L. X. Tang, Y. Dong, and J. Liu, "Differential Evolution With an Individual-Dependent Mechanism," IEEE Transactions on Evolutionary Computation, vol. 19, pp. 560-574, 2015.
[14] L. X. Tang, Y. Zhao, and J. Liu, "An Improved Differential Evolution Algorithm for Practical Dynamic Scheduling in SteelmakingContinuous Casting Production," IEEE Transactions on Evolutionary Computation, vol. 18, pp. 209-225, 2014.
[15] J. Y. Sun, Q. F. Zhang, and E. P. K. Tsang, "DE/EDA: A new evolutionary algorithm for global optimization," Information Sciences, vol. 169, pp. 249-262, 2005.
[16] A. Zhou, Q. F. Zhang, Y. C. Jin, and B. Sendhoff, "Combination of EDA and DE for continuous biobjective optimization," IEEE World Congress on Computational Intelligence, pp. 1447-1454, 2008.
[17] X. M. Song and L. X. Tang, "A novel hybrid differential evolutionestimation of distribution algorithm for dynamic optimization problem," IEEE Congress on Evolutionary Computation, pp. 1710-1717, 2013.
[18] L. Bai, J. Y. Wang, Y. H. Jiang, and D.X. Huang, "Improved hybrid differential evolution-estimation of distribution algorithm with feasibility rules for NLP/MINLP engineering optimization problems," Chinese Journal of Chemical Engineering, vol. 20, pp. 1074-1080, 2012.
[19] Z. C. Li, B. Qian, R. Hu, C. S. Zhang, and K. Li, "A self-adaptive hybrid population-based incremental learning algorithm for M-machine reentrant permutation flow-shop scheduling," Lecture Notes in Computer Science, vol. 7995, pp. 8-20, 2013.
[20] Q. F. Zhang, J. Y. Sun, E. P. K. Tsang, and J. Ford, "Estimation of distribution algorithm with 2-opt local search for the quadratic assignment problem," Towards a New Evolutionary Computation, pp. 281-292, 2006:.
[21] J. Carlier, "Ordonnancements a contraintes disjonctives," Operations Research, vol. 12, pp. 333-351, 1978.
[22] C. R. Reeves, "A genetic algorithm for flowshop sequencing," Computers \& Operations Research, vol. 22, pp. 5-13, 1995.