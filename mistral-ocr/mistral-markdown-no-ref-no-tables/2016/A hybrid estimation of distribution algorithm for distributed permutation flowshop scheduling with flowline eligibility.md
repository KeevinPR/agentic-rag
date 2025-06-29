# A Hybrid Estimation of Distribution Algorithm for Distributed Permutation Flowshop Scheduling with Flowline Eligibility 

Wenzhe Duan, Zhengyang Li, Mengchen Ji, Yixin Yang, Shouyang Wang, Bo Liu<br>Academy of Mathematics and Systems Science<br>Chinese Academy of Sciences<br>Beijing 100190, China<br>duanwenzhe14@mails.ucas.ac.cn (WZD), liub01@mails.tsinghua.edu.cn (BL)


#### Abstract

This paper studies a new extension of distributed permutation flow shop scheduling problem (DPFSP) referred to as the DPFSP with flowline eligibility. Under this extension, the problem contains two stages. At the first assignment stage, a set $N$ of $n$ jobs is distributed among $F$ factories with flowline eligibility constraint, i.e., not all the factories are available for every job. Then each factory can be regarded as a regular permutation flow shop scheduling problem (PFSP) in which jobs assigned to each factory have to be processed on $m$ machines according to the given permutation. The objective is to minimize the maximum completion time or makespan of all the factories. The flowline eligibility constraint adds asymmetry and complexity to the regular DPFSP. In the proposed hybrid estimation of distribution algorithm (hybrid EDA), a heuristic of Framinan and Leisten (FLH) based solution-generate method (FLHSGM), two novel factory-based operators are proposed, and an effective local search based on variable neighborhood search (VNS) is employed and incorporated into EDA. Numerical simulations with comprehensive computational and statistical analysis are carried out. The experimental results and comparisons with existing algorithms show that the FLHSGM and the VNS-based local search enhances the search ability of EDA and the effectiveness of the hybrid EDA in solving both small-scale and large-scale DPFSP with flowline eligibility.


Keywords-DPFSP with flowline eligibility constraint, EDA, VNS

## I. INTRODUCTION

Production scheduling plays an important role in the decision making of a manufacturing system. Significant research efforts in the development of optimization approaches have been made, and some optimization frameworks and algorithms have been proposed [1-3]. The distributed permutation flow-shop scheduling (DPFSP) has been a very active and prolific combinatorial problem proposed by Naderi and Ruiz [4]. The regular DPFSP is a two-stage problem. In the first assignment stage, a set of $n$ jobs are distributed among $F$ factories each of which contains $m$ machines. All factories are available for processing all jobs. Then each factory can be regarded as a permutation flow-shop scheduling problem (PFSP) where jobs assigned to each factory have to be

[^0]processed on $m$ machines according to the given permutation. Many extensions of regular DPFSP have be proposed. For instances, Hatami et al. proposed the distributed assembly permutation flow shop scheduling problem (DAPFSP) in 2013 with the background of complex supply chains [5]. This extension added an assembly stage on DPFSP where all the jobs have to be assembled into final products after being produced in the factory. An extended DPFSP model was designed by Li et al in 2016, which considers transportation times and loading capacities of factories [6].

As mentioned above, there is a common and universal assumption of the regular DPFSP and of all the extension model of DPFSP: all the factories, production centers or shops are available for all of jobs [4]. This assumption means that each job can be processed in any factory with no restriction. However, this situation is less common. Due to technological or transportation constraints, machines cannot be utilized for some jobs and the cost for transporting some jobs to some factories may be unacceptable. Thus some jobs must be processed only in certain factories which is described as eligibility constraint. The eligibility constraint on parallel machine scheduling has already been studied by Hwang and Chang [7], and Kellerer [8]. In 2015, Hatami et al. proposed DAPMSP with eligibility constraint [9]. In this paper, we studies a new extension of distributed permutation flow-shop scheduling problem referred to as DPFSP with flowline eligibility. This extension adds a constraint to the first assignment stage. For each job $i$ there is a set $M_{i}$ which denotes the unavailable factories of job $i$. All jobs must be assigned to the factory they are allowed to. The second processing stage of DPFSP with flowline eligibility is the same as the regular DPFSP.

The regular DPFSP is a kind of NP-hard problem [9]. After the pioneer work of Naderi and Ruiz, many intelligent optimization algorithms have been utilized for the DPFSP and its extensions. For example, a modified iterated greedy algorithm [10] and a scatter search algorithm [11] was proposed for regular DPFSP. Wang and Wang proposed an EDA-based memetic algorithm which performed well in


[^0]:    This research is partially supported by National Natural Science Foundation of China (Grant No. 71101139 and 71390331), as well as Defense Industrial Technology Development Program.

DAPFSP [12]. Because of the flowline eligibility constraint, the asymmetric nature of the DPFSP with flowline eligibility is stronger than the regular DPFSP. This asymmetry adds much complication upon problem solving. In this paper, a hybrid estimation of distribution algorithm (EDA) is proposed for DPFSP with flowline eligibility constraint. As a populationbased evolutionary algorithm, EDA draws much attention in the field of intelligent optimization [13]. Due to the ability of solving high-dimensional optimization problems, EDA has become an essential asset in the algorithmic toolbox [14]. The main characteristic of EDA is its probability model, which is updated with the evolution of the population and adds the search probability of promising solutions. Besides, to execute the searching operator efficiently, decrease the scale of the searching space and adapt to the constraint of flowline eligibility, a novel factory-based method is proposed to represent a solution for the DPFSP with flowline eligibility constraint. This method uses only one layer encoding which is denoted as a vector $s$. The $i$ th element of $s$ is the assigned factory of $i$ th job. Then the permutation of jobs in each factory is generated by a heuristic first proposed by Framinan and Leisten [15]. Since variable neighborhood search (VNS) is the most preferred algorithm in the literature with which hybridize [16] , in the hybrid EDA, an effective local search based on VNS [17] is put forward to balance the exploration and exploitation. And two novel factory-based operators are employed and incorporated into VNS in order to avoid invalid searching operators.

The remainder of this paper is organized as follows: In Section II, the DPFSP with flowline eligibility constraint is described; Then the hybrid EDA for DPFSP with flowline eligibility constraint is introduced in Section III; In Section IV, experimental results on benchmarks together with comparisons are presented and analyzed; Finally, the conclusion is given in Section V.

## II. DPFSP WITH FLOW LINE ELIGIBILITY CONSTRAINT

The DPFSP with flowline eligibility constraint can be defined as a two-stage problem. a set $N$ of $n$ jobs, denote as $\left\{j o b_{i}, j o b_{j}, \cdots, j o b_{n}\right\}$, have to be processed on a set $G$ of $F$ factories, each one of them contains the same set $M$ of $m$ machines. The unavailable factory set of $j o b_{i}$ is denotes as $M_{i}:$

- Factory $f$ belongs to $M_{i}, f \in M_{i}$, means that the $f$ th factory is not available for $j o b_{i}$;
- The set $M_{i}$ is empty means that all factories is capable for $i$ th job;
- $M_{i}$ cannot be the set of all factories, i.e., $M_{i} \neq G$.

At the first assignment stage, all jobs are distributed among $F$ factories and each job must be assigned to its available factors. Once $j o b_{i}$ is assigned to factory $f$, it cannot be transferred to another factory as it must be completed in one factory during the second processing stage. The processing
times of the $j o b_{i}$ 's operation on $j$ th machine of all the factory are the same, i.e., $T_{i j}^{j_{1}}=T_{i j}^{j_{2}}=\cdots=T_{i j}^{F}=T_{i j}$. Besides, the following assumptions for the regular DPFSP scheduling are adopted: all the jobs are independent and available at time 0 . Each machine can process only one job at a time and each job can be processed by only one machine at a time. Each operation must be completed without interruption once it is started. The DPFSP with flowline eligibility constraint is to assign jobs to factories under constraint and to determine the job permutation for all machines of each factory to optimize a certain scheduling objective. In this paper, the objective is to minimize the maximum completion time of each factories.

Denote $h^{f}=\left(j o b^{f}(1), j o b^{f}(2), \cdots, j o b^{f}\left(n_{f}\right)\right)$ as the job permutation in factory $f$ in the processing stage where $n_{f}$ is the total number of jobs which is assigned to factory $f$. For any $j o b^{f}(i) \in h^{7}$, the factory $f$ must be available for it, i.e., $f \notin M_{j o b^{f}(i)}$. A feasible solution $h$ of DPFSP with flowline eligibility constraint can be represented as a list of $n_{f}$ job permutation vectors. Denotes $C_{i j}$ as the completion time that $j o b_{i}$ finishes the operator on $j$ th machine. For a feasible solution $h$, the total completion time or makespan is calculated as follows:

$$
\begin{gathered}
C_{j o b^{f}(1), 1}=T_{j o b^{f}(1), 1} \\
C_{j o b^{f}(0,1}=C_{j o b^{f}(i-1), 1}+T_{j o b^{f}(0), 1} \\
C_{j o b^{f}(1), j}=C_{j o b^{f}(1), j-1}+T_{j o b^{f}(1), j} \\
C_{j o b^{f}(0, j}=\max \left(C_{j o b^{f}(0, j-1}, C_{j o b^{f}(i-1), j}\right)+T_{j o b^{f}(0, j}
\end{gathered}
$$

where $f=1,2, \ldots, F, i=1,2, \ldots, n_{f}, j=1,2, \ldots, m$.
The objective of solving the DPFSP with flowline eligibility constraint is to find a feasible solution $h$ with the minimum makespan. However, as an NP-hard problem, this problem cannot be solved by any polynomial time algorithms. Therefore, the objective of the solution methods is to obtain an approximate optimal feasible solution within an acceptable computing time.

## III. HYBRID EDA FOR DPFSP WITH FLOWLINE ELIGIBILITY CONSTRAINT

## A. Brief Review of EDA

Estimation of distribution algorithm (EDA) is a populationbased evolutionary optimization algorithm which explores the space of solutions by sampling an explicit probabilistic model constructed from promising solutions found so far [13]. It has already been successfully applied to solve different kinds of academic and practical problems. In scheduling field, the EDA

has been utilized to solve the flow-shop problem [19], hybrid flow-shop scheduling problem [20], flexible job-shop scheduling problem [21] and so on. The EDA based MA has also solved the regular DPFSP successfully [12].

EDA works with a population of candidate solutions to the problem, starting with the population generated according to the uniform distribution over all admissible solutions. The population is then scored using a fitness function. In DPFSP with flowline eligibility constraint, this fitness function is the maximum completion time of a feasible solution. Then the population is sorted by their scores. From this ranked population, a subset of the most promising solutions are selected by the selection operator. A simple but useful selection operator is truncation selection with threshold $\tau=$ $50 \%$, which selects the $50 \%$ best solutions among all the feasible solutions in one generation. The probability model then can be updated according to the information obtained from these superior solutions. Once the model is constructed, new solutions of the next generation are generated by sampling the distribution encoded by this model. These new solutions are then incorporated back into the old population, possibly replacing it entirely. This process is repeated until a solution of sufficient quality is reached or the number of iterations reaches some threshold, with each iteration of this procedure usually referred to as one generation of the EDA.

## B. Solution Representation

Solution representation is a key issue for every metaheuristic method. In the regular DPFSP, a set of $F$ lists or the two layer encoding based method is the most widely used representation. In the DPFSP with flowline eligibility constraint, we represent every feasible solution as a set $h$ as same as DPFSP and a factory assignment vector $s$, each list of $h$ contain a job permutation vector with the order in which jobs will be processed at each factory. This kind of representation is the most straightforward method, for instance, if there is a problem with 10 jobs ( $n=10$ ) and three factories $(F=3)$, and $M_{1}=\{1,3\}, M_{2}=\{2\}$, the sets of unavailable factories of the other jobs are empty. One feasible solution is :

$$
h=\left\{\begin{array}{c}
10,4,2,8 \\
1,9,6 \\
5,3,7
\end{array}\right.
$$

and

$$
s=\{2,1,3,1,3,2,3,1,2,1\}
$$

In order to execute the searching operator efficiently and decrease the scale of searching space, in this paper we proposed a novel solution-generate method, which makes it possible to generate a new feasible solution $h$ from a given factory assignment vector $s$. This novel method is based on a heuristic for total flow time minimization in permutation flow shops, which is first proposed by Framinan and Leisten (FLH) [15]. The details of FLH based solution-generate method will be described as follows:

Step 1: For each factory $f$, let

$$
S^{f}=\left\{j o b_{i}^{f}, j o b_{i}^{f}, \ldots, j o b_{i}^{f}\right\}
$$

represents the set of jobs assigned to factory $f$ and is calculated from the factory assignment vector $s$;

Step 2: For job $j o b_{i}^{f}$ each set $S^{f}$, calculate the total processing time $T_{i}^{f}$ which is given by:

$$
T_{i}^{f}=\sum_{j=1}^{M} T_{i j}
$$

then sort all jobs of $S^{f}$ in ascending order of $T_{i}^{f}$;
Step 3: Set $k=2$, Select the first two jobs from the sorted list and choose the better between the two feasible sequences as the best partial sequence so far.

Step 4: let $k=k+1$. Choose the $k$ th job from the sorted list and insert it into the $k$ possible positions of the temporary best partial sequence. The one with minimum completion time is selected as the best partial sequence obtained so far;

Step 5: If $k=n$, stop, let $f=f+1$ and go to Step 1; else, go to Step 4.

## C. Probability Model

The most important part of the EDA is its probability model that describes the distribution of the searching space. Generally, the construction of the probability model is a statistical learning process based on the information of superior feasible solutions. Besides, the EDA generates new solutions by sampling the distribution which is obtained from the probability model. Therefore, a proper and explicit probability model is critical to the performance of EDA-based algorithms.

In this paper, the optimization objective is to minimize the complement time of the DPFSP with flowline eligibility. Both factory assignment vector and permutation of jobs in each factory play an important role in completion time. However, according to above solution representation, the permutation of jobs in each factory can be obtained by the factory assignment vector. To decrease the scale of probability model, the probability model is designed as a probability matrix, which is related to the factory assignment vector of a feasible solution:

$$
p(g)=\left(\begin{array}{cccc}
p_{1: i}(g) & p_{1: j}(g) & \cdots & p_{1: F}(g) \\
p_{2: i}(g) & p_{2: j}(g) & \cdots & p_{2: F}(g) \\
\vdots & \vdots & & \vdots \\
p_{n: i}(g) & p_{n: j}(g) & \cdots & p_{n: F}(g)
\end{array}\right)
$$

Element $p_{i j}(g)$ of the probability matrix $P$ represents the probability that the $i$ th job is assignment to the $j$ th factory during the $g$ th generation, i.e., $i$ th element of a feasible factory

assignment vector appears. At the initialization stage of the hybrid EDA, the elements in matrix $P$ are initialized as:

$$
p_{i j}(0)=\left\{\begin{array}{cl}
\frac{1}{N-\# M_{i}} & , j \in M_{i} \\
0 & , j \notin M_{i}
\end{array}\right.
$$

for all $i$ and $j$, where $\# M_{i}$ denotes the size of set $M_{i}$. It implies a uniform distribution in the searching space and no useful prior knowledge is available.

The probability model must be well adjusted to make the search procedure tract the promising searching region. An updating mechanism based on the information of the superior feasible solutions is employed to adjust the probability model during each generation. This updating mechanism can be regarded as a kind of learning process as follows:

$$
p_{i j}(g+1)=(1-\alpha) p_{i j}(g)+\frac{\alpha}{S \_P O P} \sum_{k=1}^{K \_P O P} I_{i j}^{k}(g)
$$

where, $\alpha \in\{0,1\}$ denotes the constant learning rate of the probability model, $S_{-} P O P$ is the number of superior feasible solutions and $S_{-} P O P=\tau \times P O P . I_{i j}^{k}(g)$ is the indicator function of $k$ th superior solutions in $g$ th generation. $I_{i j}^{k}(g)=1$ means that $i$ th job of $k$ th superior solutions is assigned to the $j$ th factory; $I_{i j}^{k}(g)=0$, otherwise.

## D. EDA-based Search

In this paper, the distribution information of superior feasible solutions can be evolved by EDA-based searching operator, (9), (10) and (11) are employed to initialize and construct the probability model of EDA and to describe the distribution of the searching space. Note the, the DPFSP with flowline eligibility constraint is a complex problem with strong asymmetry. Aimed at executing the searching operator efficiently and decreasing the scale of searching space, a FLHbased solution-generate method is incorporated into EDA. In the following contents, we will present the VNS-based local search that is incorporated in EDA to propose a hybrid EDA.

## E. VNS-based Local Search

Variable neighborhood search (VNS) is a metaheuristic, or a framework for building heuristics, based upon systematic changes of neighborhoods both in descent phase, to find a local minimum, and in perturbation phase to emerge from the corresponding valley. It was first proposed in 1997 by Mladenovic and Hansen and has since then rapidly developed both in its methods and its applications. VNS heavily relies on the following three facts [17]:

- A local minimum with respect to one neighborhood structure is not necessarily a local minimum for another neighborhood structure;
- A global minimum is a local minimum with respect to all possible neighborhood structures;
- For many problems local minima with respect to one or several neighborhoods are relatively close to each other.

A variety of scheduling problems has been efficiently solved with VNS approach. Lin and Ying proposed a hybrid Tabu-VNS approach for single machine tardiness problem with sequence-dependence setup times [22]. A VNS-based PSO was applied by Liu et al. to tackle the multi-objective flexible jobshop scheduling problems [23]. Zobolas et al. designed a hybrid GA-VNS approach to minimize the total completion time in PFSP [24].VNS method has been employed in the regular DPFSP and its extension problems and has performed well. For example, Naderi and Ruiz applied VNS for solving the DPFSP firstly [4]. VNS was used in Hatami et al. to find the optimal solutions in distributed assembly permutation flowshop scheduling problem (DAPFSP) [5].

In this paper, three job-based operators and two novel factory-based operators are employed and incorporated into VNS as different neighborhood of a feasible solution. The jobbased operators are aimed at changing the job sequence inside each factory. Details of three job-based operators will show as follows:

1) Job-Swap: Swap the priorities of $j o b^{f}(i)$ and $j o b^{f}(j)$ in the job permutation vector of factory $f$;
2) Job-Invert: Invert the partial permutation between the positions of $j o b^{f}(i)$ and $j o b^{f}(j)$ in the job permutation vector of factory $f$;
3) Job-Insert: Partial permutation vector is obtained by removing one single $j o b^{f}(i)$ from the job sequence of factory $f$, insert $j o b^{f}(i)$ into all possible positions of the partial permutation vector and choose the feasible solution $h$ with minimum completion time of factory $f$;
where, $j o b^{f}(i)$ and $j o b^{f}(j)$ denote the labels of jobs in factory $f$.

The two factory-based operators adjust both the job permutation vector in each factory and the factory assignment vector of a feasible solution. Most of the existing factory-based operators, such as the one designed by Naderi and Ruiz [4], change only one job's factory during an operation. It is possible that all the offspring solutions generated by these factory-based operators are worse than their parents. However, maybe one of the offspring solutions sits on the "key path" to the optimal solution, i.e., the optimal solution will be obtained from one of the offspring solutions during more than one operations. Unfortunately, all these offspring solutions are abandoned by VNS algorithm. In this paper, two novel factorybased operators are designed to avoid this. These two operators are able to change more than one jobs' factory in one operations. We pay much attention on the critical factory, which is the factory with maximum completion time. The critical path of DPFSP with flow line eligibility depends on the permutation of jobs in the critical factory. Thus an effective way to improve the solution of DPFSP with flow line

eligibility is to remove or change one job in critical factory. Details of two factory-based operators will show as follows:
4) Factory-Cycle: Generate a job vector $\left(\right.$ job $\left.^{f_{1}}\left(i_{1}\right), j o b^{f_{2}}\left(i_{2}\right), \ldots, j o b^{f_{m_{n}}}\left(i_{m_{n}}\right)\right)$, in which $f_{1} \notin M_{j o b^{f_{1}}\left(i_{1}\right)}, f_{2} \notin M_{j o b^{f_{2}}\left(i_{2}\right)}, \ldots, f_{m_{n}} \notin M_{j o b^{f_{1}}\left(i_{1}\right)}$ and $f_{1} \neq f_{2} \neq \cdots \neq f_{m_{n}}, f_{1}=f^{c}$. Then for each job permutation vector of factory $f_{k}$, remove $j o b^{f_{k}}\left(i_{k}\right)$, insert $j o b^{f_{k+1}}\left(i_{k+1}\right)$ into all the possible positions and choose the job permutation vector with minimum completion time.
5) Factory-Sequence: Generate a factory label $f_{0}$ and a job vector $\left(j o b^{f_{1}}\left(i_{1}\right), j o b^{f_{2}}\left(i_{2}\right), \ldots, j o b^{f_{m_{n}}}\left(i_{m_{n}}\right)\right)$, in which $f_{1} \notin M_{j o b^{f_{1}}\left(i_{1}\right)}, \ldots, f_{m_{n, 1}} \notin M_{j o b^{f_{m_{n}}}\left(i_{m_{n}}\right)}$ and $f_{2} \notin M_{j o b^{f_{1}}\left(i_{2}\right)}, f_{2} \neq f_{1} \neq \cdots \neq f_{m_{n}}, f_{2}=f^{c}$. Then for each job permutation vector of factory $f_{k}, k=1,2, \ldots, m_{k}$, remove $j o b^{f_{k}}\left(i_{k}\right)$, insert $j o b^{f_{k+1}}\left(i_{k+1}\right)$ into all the possible positions and choose the job permutation vector with minimum completion time. Similarly, insert $j o b^{f_{1}}\left(i_{1}\right)$ into all the possible positions of the job permutation vector of factory $f_{0}$ and choose the one with minimum completion time.
where, $j o b^{f}(i)$ denotes the labels of jobs in factory $f, f^{c}$ denotes the critical factory of the feasible solution. $m^{c}$ and $m^{s}$ denote as the length of cycle length and sequence length, respectively.

A solution h executes all the operators step by step. VNS based local search can be described as follows:

Step 1: Set $k=1$ and $k_{\max }=5$;
Step 2: Execute the $k$ th operator on solution $h$;
Step 3: If the new feasible solution $h^{\prime}$ obtained by Step 2 is accepted under some acceptance criteria, then the old solution is replaced and let $k=1$; else let $k=k+1$;

Step 4: If $k \leq k_{\max }$, go to Step 2; else, stop.
The acceptance criteria is not the same between these two kinds of operators. We say a new feasible solution $h^{\prime}$ obtained by a job-based operator is acceptable if the $f$ th factory's completion time of $h^{\prime}$ is shorter than $h$; on the other hand, a new feasible solution $h^{\prime}$ obtained by factory based operators is regarded as a better solution than $h$ if total completion time of $h^{\prime}$ is shorter than the old solution $h$.

## F. Hybrid EDA

In this sub-section, the Hybrid EDA is proposed for the DPFSP with flow line eligibility, where a novel solutiongenerate method based on FLH is applied to generate feasible solution from factory assignment vector, EDA and VNS-based local search are used for exploration and exploitation in search space respectively. The procedure of hybrid EDA is described as follows:

Step 1: Initialize the probability matrix $P$;
Step 2: Sample the probability matrix $P$ and generate $P O P$ factory assignment vectors, denotes as $S$.

Step 3: For any $s \in S$, generate a feasible solution $h$ with the FLH based solution-generate method;

Step 4: Evaluate all the feasible solutions, determine the best solution and the superior population;

Step 5: VNS-based local search on the best solution;
Step 6: Update the probability matrix $P$ by the information of the superior population;

Step 7: If the best solution keep fixed at consecutive $L$ steps, then output the best solution; else, go to Step 2.

## IV. NUMERICAL RESULTS AND COMPARISONS

To test the performance of the hybrid EDA, numerical tests are carried out by using two sets of benchmark instances of regular DPFSP with new flowline-eligibility constraint. All the benchmarks used in this paper are available at http://soa.iti.es. To evaluate the performance of the hybrid EDA, experimental results are evaluated by relative percentage deviation (RPD) as follows:

$$
R P D=\frac{\text { alg }- \text { opt }}{\text { opt }} \times 100
$$

where, opt is the solution of DPFSP with flowline eligibility constraint found by the comparing algorithms below and alg denotes to the makespan of the solution obtained by a certain algorithm. We also use BRE denote the relative error of the best with respect to the optimal solution of DPFSP with flowline eligibility constraint found so far.

## A. Result and Comparsion of Small-scale Instances

In this section, by using 10 small-scale instances, we compare the hybrid EDA, the pure EDA and hybrid EDA2 in which the pure EDA is equipped with NEHSGM and VNSbased local search. The different between hybrid EDA and hybrid EDA2 is that the solution-generate method of hybrid EDA2 is NEHSGM instead of FLHSGM. In the solutiongenerate method based on NEH (NEHSGM), the job permutation vector of each factory is created by the wellknown heuristic NEH instead of FLH. The following parameters are used: population size of EDA $P O P=20$; percentage of the superior sub-population $\tau=50 \%$; learning rate of probability matrix $\alpha=0.1$ and the stop parameter $L=40$. Each instance run 10 times independently for every algorithms for comparison. The statistical performances of 10 independent

benchmarks are listed in Table I, including the best relative error (BRE) and relative percentage deviation (RPD) to the optimal solution of DPFSP with flow line eligibility constraint found so far.

TABLE I. COMPARISON OF HYBRID EDA, PURE EDA AND HYBRID EDA2

From Table II, it can be seen that the proposed hybrid EDA provides the better optimization performance than other algorithms for all small-scale benchmarks. The optimal results obtained by the proposed hybrid EDA are all the same to the optimal solution of DPFSP with flowline eligibility found so far (that is to say, the BRE values are 0 ), which demonstrates the effective searching quality of the proposed hybrid EDA. On the other hand, the Average RPD values resulted by hybrid EDA are also zero, which demonstrates the robustness of the proposed algorithm in dealing with small-scale searching space. Simulation results and comparisons between hybrid EDA, pure EDA and hybrid EDA2 demonstrate that the FLH based solution-generate method (FLHSGM) and VNS-based local search are able to enhance the searching ability and balance between global search and local search of EDA.

## B. Result and Comparison of Large-scale Instances

Next, hybrid EDA is tested by using large-scaled instances. The following parameters are used: population size of EDA $P O P=20$; percentage of the superior sub-population $\tau=50 \%$; learning rate of probability matrix $\alpha=0.1$ and the stop parameter $L=40$. Considering number of factories, products, and jobs, a summarized result of average RPD and BRE is shown in Table II.

TABLE II. COMPARISON OF HYBRID EDA, PURE EDA AND HYBRID EDA2

Form Table III, it can be seen that hybrid EDA outperforms the other algorithms in solving all the groups of large-scaled instances. All the BRE values of Hybrid EDA are all 0 and the average RPD values are also very small, which demonstrates the effectiveness and robustness of the proposed hybrid EDA on large-scale searching space. In order to show the effectiveness of FLHSGM, we carry out simulation to compare our proposed hybrid EDA with the hybrid EDA2 which is defined above. In our simulation, the parameters of the two algorithms are the same and simulation results show that the proposed hybrid EDA outperforms hybrid EDA2 both in average RPD and BRE. On the other hand, the comparison between the proposed hybrid EDA and pure EDA demonstrates that the VNS-based local search are able to enhance the searching ability and balance between global search and local search of EDA.

## C. Wilcoxon Tests

In this section, the pair-wise Wilcoxon test is used to compare the performance obtained by the proposed Hybrid EDA and the other two algorithms.

Table III shows the result of the comparisons of the our approach with both the Pure EDA and Hybrid EDA2 using 10 small-scale instances. Table IV shows the same comparison using 10 large-scale instances.

TABLE III. WILCOSON TEST OF SMALL-SCALE INSTANCES


TABLE IV. WILCOSON TEST OF LARGE-SCALE INSTANCES


In both cases we can observe that there is a significant difference between the proposed Hybrid EDA and the other two algorithms.

## V. CONCLUSION

In this paper we have studied an extension of the conventional distributed permutation flow shop scheduling problem (DPFSP) referred to as the DPFSP with flowline eligibility constraint. More specifically, we have proposed a new eligibility constraint on the first assignment stage of DPFSP. Under the flowline eligibility constraint, not all the factories are available for every jobs. Each job must be assigned to its feasible factory. Then each factory can be regarded as a regular permutation flow shop scheduling problem (PFSP) where jobs assigned to each factory have to be processed on $m$ machines according to the given permutation. The objective is to minimize the maximum completion time, i.e., makespan of all the factories.

An effective hybrid EDA has been proposed for the DPFSP with flowline eligibility constraint. In the proposed algorithm, the EDA-based exploration and local search-based exploitation were well integrated. For the exploration phase, a probability model has been built to describe the probability distribution of superior feasible solutions. Besides, a heuristic of Framinan and Leisten based solution-generate method has been built in order to execute the searching operator efficiently, decrease the scale of the searching space and adapt to the constraint of flowline eligibility constraint. The effectiveness of the proposed FLHSGM has been shown by comparing with the NEH based solution generation and random order based solution generation. For the exploitation phase, two novel factory-based operators have been proposed and incorporated into the VNS based local search. Simulation results and comparisons with other algorithms have demonstrated that the VNS-based local search are able to enhance the searching ability of EDA both in small and large scale searching space. The results and comparison with existing algorithms have shown the effectiveness and efficiency of the proposed hybrid EDA.

## ACKNOWLEDGMENT

The authors would like to thank the anonymous referees for their constructive comments on the earlier version of this paper. The last author BL is very grateful to Prof. Yew-Soon Ong (Nanyang Technological University, Singapore), Prof. Yihui Jin, Prof. Ling Wang (Tsinghua University), Prof. Jikun Huang (Peking University) and Royal Honored Prof. M.A. Keyzer (SOW-VU, Vrije Universiteit Amsterdam, The Netherlands) for their support.
