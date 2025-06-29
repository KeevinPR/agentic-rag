# Solving Multi-Objective Semiconductor Assembly and Test Manufacturing Scheduling Problem Based on Estimation of Distribution Algorithm 

Xincheng Zhong ${ }^{1,2}$, Chang Liu ${ }^{1}$, Jun Zhu ${ }^{1}$, Dongbin Han ${ }^{3}$, Zhiling Yuan ${ }^{4}$<br>1. Key Laboratory of Networked Control System, Shenyang Institute of Automation, Chinese Academy of Sciences, Shenyang ,China;<br>2. University of Chinese Academy of Sciences, Beijing, China<br>3. Liaoyang Steel Tube Works of Baoji Steel Tube, Liaoyang,China<br>4. Bohai Shipbuilding Heavy Industry Co., Ltd, Huludao,China


#### Abstract

In order to solve the problem that, from the current practical perspective of semiconductor assembly and test manufacturing (ATM), the traditional multi-objective optimization algorithm is difficult to realize the practical decision of the enterprise, this paper proposes a new multi-objective estimation of distribution algorithm (EDA) to solve the ATM scheduling problem. According to the demand of the ATM enterprise, based on sub-module using two modeling ideas, objectives were divided into two categories: constrained objective and optimized objective, and the different objective had the different searching process. Finally, it used the new algorithm to solve the multi-objective ATM scheduling problem. The result shows that the novel algorithm has the good feasibility and it also has an obvious advantage, the better practicability and maneuverability, compared with the traditional multi-objective optimization methods.


Keywords-ATM; multi-objective; EDA; sub-module; constrained objective;optimized objective

## I. INTRODUCTION

Semiconductor Assembly and Test Manufacturing (ATM) [1], as the focus of China's semiconductor industry, whose production process is complex and equipment is expensive, has high requirements for production operations management and process control. To survive and develop in today's increasingly competitive market environment, ATM enterprise decision-makers want to complete the delivery date of product on time, at the same time, in order to reduce inventory or goods due to limited shelf life itself, and hope that the ahead of schedule time should not be too early and use existing resources as far as possible. Moreover, ATM is a typical MTO manufacturing, whether to meet the delivery date or tardiness rate can directly affect the enterprise's credit. As the most basic indicators of scheduling decisions, completion time can reflect the efficiency of workshop and it is also one of the most widely used performance indicators in workshop scheduling. In addition, it's necessary to consider the cost of production which is an important part of profit-maximizing. However, there are connections and constraints between each objective of ATM scheduling, and different decision-makers hope to meet different objective. For the production scheduling, it should be possible to meet the objective requirements of decision-makers

[^0]to give reasonable scheduling scheme.
Multi-objective optimization problem in theory has made a good research, literature $[2,3,5,13,14]$ are representative of multi-objective problem solving method in recent years. Summarizing the previous multi-objective optimization methods, algorithms basically belong to the following two: Pareto method and non-Pareto method. Pareto method, whose algorithm design is complex and calculation is large, generates the weights randomly during the search, and ultimately produces a set of non-inferior solutions. However, the final result, which need to be selected again by decision-makers, is not conducive to the realization of advance decision. NonPareto method change multi-objective into single objective, its algorithm design is simple and easy to implement, but the objective weight is given by the needs of enterprise decisionmakers with experience in advance, but general linear weighting will result in an alternative between each sub-goal and contrary to indispensability of sub-goals and inevitably exist unreasonable. As one of today's most complex manufacturing systems, the logic between manufacturing resources and products of ATM is complex, and the production scheduling has been always a hot issue. Commonly used for production scheduling algorithms, such as branch and bound method, method based on the bottleneck heuristic, algorithm based on the rules of priority in the allocation of positive or inverted displacement, although they can get a good performance in terms of an index, but in the pursuit of a different objective tends to produce a conflicting result.

According to the actual needs of ATM enterprise and the properties of different objectives, this paper classified objective and brought about a new multi-objective EDA. Decisionmakers should have the objective classified firstly and then new proposed algorithm can give the satisfied result according to these objectives so that the multi-objective scheduling problem of ATM enterprise can be solved.

## II. PROBlem STATEMENT

## A. Scheduling problem description

The ATM production line scheduling considered in this paper can be described graphically as in Fig1 [6, 9]. In this environment, there are six main stages, (including saw, die


[^0]:    This work was supported by The National Key Technology R\&D Program (2011ZX02601-005).

attach, wire bond, mold, de-flux, electro-plating) in which a special operation is processed. At any stage $j(1 \leq j \leq 6)$, the number of parallel machines is $M_{j}$. There are $n$ jobs, each of them requires all the six different operations, and can be processed on any one of the $M_{j}$ machines at stage $j$. For all the $n$ jobs, the processing time on each machine are known in advance. According to the given objective, scheduling must determine the ranking of each job and the distribution of the machines on each stage, and make it meet the requirements of scheduling indicators.
![img-0.jpeg](img-0.jpeg)

Fig. 1. An example of ATM scheduling problem
The ATM scheduling problem can be formulated as follows:

$$
\begin{gathered}
\sum_{i=1}^{n} x_{i j}=1, l=1,2, \ldots, n \\
\sum_{i=1}^{n} x_{i j}=1, i=1,2, \ldots, n \\
\sum_{k=1}^{M_{j}} y_{i j k}=1, i=1,2, \ldots, n ; j=1,2, \ldots, m \\
C_{i j} \leq S_{i(j+1)}, i=1,2, \ldots, n ; j=1,2, \ldots, m \\
C_{i j}=S_{i j}+P_{i j}, i=1,2, \ldots, n ; j=1,2, \ldots, m \\
\sum_{i \in I_{j}} x_{i j}^{l} S_{i j} \leq x_{i j+1 j}^{l} S_{i j}, j=1,2, \ldots, n ; j=1,2, \ldots, m \\
\sum_{i=1}^{n} x_{i j_{1}} y_{i j k} C_{i j} \leq \sum_{i=1}^{n} x_{i j_{1}} y_{i j k} S_{i j}+\left(1-\sum_{i=1}^{n} x_{i j_{2}} y_{i j k} S_{i j}\right) \times L \\
j=1,2, \ldots, m ; l_{1}, l_{2}=1,2, \ldots, n ; l_{1 i} l_{2} ; k=1,2, \ldots, M_{j}
\end{gathered}
$$

As for the above formulation: (1) and (2) ensure that a full array of all jobs; (3) ensures that one job can be processed exactly on one machine at each stage; (4) means that one job cannot be processed until its preceding job is finished; (5) describes the completion time is equal to the start time and processing time at the same stage; (6) means that the more front position the more advanced processing; (7) means that job rearward can begin process after the processing of the front rank job is completed at the same stage on the same machine.

## B. Nomenclature

$n$ : the number of jobs to be processed;
$m$ : the number of processing stages;
$M_{j}$ : the number of the machines at stage $j$;
$C_{i j}$ : the completing time of job $i$ at stage $j$;
$C_{\text {ost }}^{w a r k}$ : the machine working cost;
$C_{\text {ost }}^{\text {wait }}$ : the machine waiting cost;
$C_{\text {ost }}^{\text {storage }}$ : the machine storage cost;
$P_{i j}$ : the processing time of job $i$ at stage $j$;
$S_{i j}$ : the starting time of job $i$ at stage $j$;
$d_{i}$ : the delivery date of job $i$;
$\alpha_{i}$ : the penalty factor of early completion;
$\beta_{i}$ : the penalty factor of tardy completion;
$E_{i}$ : the delayed completion time;
$x_{i j}$ : a binary variable which is equal to 1 if job $i$ is assigned to the $l$-th position and is equal to 0 otherwise;
$y_{i j k}$ : a binary variable which is equal to 1 if the stage $j$ of job $i$ is assigned to the machine $k$ and is equal to 0 otherwise;
$L$ : a very large constant;

## C. Scheduling index discription

The performance indicators of ATM enterprise scheduling problem are similar with other workshop model enterprise, which mainly given by business decision-makers. Different decision-makers may give different indicators, as well as different enterprises have different indicators necessary. Next, several kinds of typical common performance indicators in ATM enterprise will be given their mathematical description.

## 1) Indicators based on completion time

Completion time refers to the final completion time of the last job. The smaller the maximum completion time, the better the performance of the scheduling time, so the completion time can be expressed as follows:

$$
\min \max _{i=1,2, \ldots, n}\left\{C_{i m}\right\}
$$

2) Indicators based on delivery date

The closer the job completion time to delivery time, the better the performance of the delivery date, so here are two objective function based on the delivery date.
a) Objective fuction 1: number of tardiness

$$
\min \left\{\sum_{i=1}^{n} U_{i}\right\}
$$

If $C_{i m} \leq d_{i}, U_{i}=0$; else $U_{i}=1$.
b) Objective fuction 2: sum of penalty

$$
\min \sum_{i}^{n}\left(\alpha_{i} E_{i}+\beta_{i} T_{i}\right), i \in\{1,2, \ldots, n\}
$$

Where $E_{i}=\max \left(0, d_{i} \cdot C_{i m}\right), T_{i}=\max \left(0, C_{i m}-d_{i}\right)$.

## 3) Indicators based on production cost

The cost of production in the process of production can be summed up in the following three parts:

$$
\min \left\{C_{\text {out }}^{\text {work }}+C_{\text {out }}^{\text {wait }}+C_{\text {out }}^{\text {storage }}\right\}
$$

## III. THE ObJective FUNCTION CLASSIFICATION

Generally speaking, the specific requirements of the objective depend on the actual needs of enterprise. According to the demand of the enterprise, based on sub-module using two modeling ideas, objectives were fallen into two categories: constrained objective and optimized objective.

## A. Constrained objective

In the actual production of enterprises, for decision-makers, not all objectives need to achieve the optimal solution, there may be some objectives that need reach a certain value, while some other objectives just need to meet certain qualifications. These objectives in the final analysis are just a kind of objectives which have constraint, so define it constrained objective. According to the requirements of the different quantization value, the constrained objectives are divided into the absolute objective and bounded objective. Absolute objective means a fixed value after being quantized, such as the number of tardiness while bounded objective means the requirements of performance must be in a limited range, such as the production cost and sum of penalty, etc.

## B. Optimized objective

The objective of traditional multi-objective optimization scheduling are basically optimized objective. The main characteristic of optimized objective is that decision-makers can't give any constraint condition. Using some methods directly to generate scheduling scheme makes the scheduling indicator optimize. Formula (8)-(10) can be used as the optimized objective.

## IV. Multi-Objective EDA BASED ON CLASSIFICATION

This article is based on the idea of objective classification, a new multi-objective EDA $[10,12]$ was brought to solve the ATM production line scheduling problem.

## A. The basic idea of the algorithm

In this study, objectives will be divided into two layers by multi-objective EDA, including constrained objective and optimized objective. This method focuses on the goal of decision-makers who need to divide the objectives first and then depend on experience to provide qualification to constrained objective, and the remaining as the optimized objective. Algorithm is based on a given objective conditions and searches automatically to find out the priori solution which should meet the objective conditions.

In the process of algorithm search, constrained objective use the way of loop body transformation and it has feasible solutions and infeasible solutions. For the infeasible solutions, search will continue in circulation in the body until a feasible
solution is found and then jump out of the loop. Using traditional multi-objective to search in optimization objective which nested loops forward with constraint objective and they form a good closed-loop control.

Multi-objective EDA based on classification has a good effectiveness in addressing single objective problem. When there are multiple optimization objectives, we can use traditional optimization method, such as method of Pareto or method of non-Pareto, to optimize. For non-Pareto method, decision-makers need to set the weight of each objective.

## B. Algorithm operating

In consideration of specificity of the ATM production line, the operation of multi-objective EDA based on classification has its own specificity. This paper uses the improved MIMIC algorithm $[7,8]$, one of the EDA, to simulate.

1) The encoding of algorithm should use decimal encoding which is more appropriate for this program, for example, for the problem with 3 jobs and 2 stages, individual $[[2,1,3],[1$, $2,3]]$ is a processing order and a solution which represents that at the first stage job 2 is processed first, next is job 1 , and job 3 is the last job to be processed while at the second stage job 1 is processed first, next is job 2 , and job 3 is the last job to be processed. For the parallel machine at each stage, we will select them according to some rules which derived from the objective we tend to. To decode a sequence is to assign the jobs to the machines at each stage so as to form a feasible schedule. For the ATM schedule problem, the decoding stage is to decide the jobs order and the machines assignment. Initial population of individuals is the sequence of each job at each stage and there is a chain dependency between them as shown in figure 2. For each stage, combined with the actual production, the algorithm should add some certain priori rules to select the machine, such as first come, first processing (FCFS) precedence rules. For another, in order to make the tardiness job zero, we should select the machine processing time of the corresponding parallel machine as early as possible.
![img-1.jpeg](img-1.jpeg)

Fig. 2. An example of bivariate chain dependency
2) The initialization of populations samples according to the uniform distribution probability matrix $L_{u} \pi_{w}$. To avoid repetitive sampling, when taken to a job, it is about to set the rest of the elements in the column or row to zero, and then let the matrix normalize. Each individual in the population is then calculated adaptation value which decides $M$ priori individuals would be used to build jobs distribution matrix $C_{u} \pi_{u}$ according to the number of two adjacent of each job. What need points out is that there is a matrix $C_{u} \pi_{u}$ at each stage.

Among them, $C_{i j}$ means the number of job $i$ followed job $j$. It's impossible that job $i$ will follow behind itself, so $C_{i j}=0$ if and only if $i=j$.

$$
\begin{aligned}
& L_{n^{*} n}=\left[\begin{array}{cccc}
1 / n & 1 / n & \ldots & 1 / n \\
1 / n & 1 / n & \ldots & 1 / n \\
\ldots & \ldots & \ldots & \ldots \\
1 / n & 1 / n & \ldots & 1 / n
\end{array}\right] \\
& \mathrm{C}_{n^{*} n}=\left[\begin{array}{cccc}
0 & C_{12} & \ldots & C_{1 n} \\
C_{21} & 0 & \ldots & C_{2 n} \\
\ldots & \ldots & \ldots & \ldots \\
C_{n 1} & C_{n 2} & \ldots & 0
\end{array}\right]
\end{aligned}
$$

3) Building a probability model is divided into two part including starting job probability model and the rest jobs probability model. Building starting job distribution vectors is to count up the number of hit counts $p=\left\{c_{11}, c_{21}, \ldots, c_{n}\right\}$ in the first position of each job and then update the probability distribution $p=\left\{c_{i} / M, c_{j} / M, \ldots, c_{n} / M\right\}$. According to the principle of correction, count up the number of $p_{i}=0(i=1,2, \ldots, \mathrm{n})$ and denoted by $t$. If $p_{i}>0, p_{i}=\alpha / t$, else $p_{i}=(1-\alpha) / t$. Among them $p_{i}$ means the probability of job $i$ in the first position. According to the probability distribution matrix $C_{n^{* n}}$ of the jobs, we build the probability distribution matrix $C_{i j}=C_{i j} / M$ of the jobs. For each job, not all of them has two adjacent relationship, so it's not necessary for job $x_{i}(j=1,2, \ldots, \mathrm{n})$ appearing behind job $x_{i}(i=1,2, \ldots, \mathrm{n})$ and there may be $C_{i j}=0$ resulting in a zero probability event that job $x_{i}$ will never next to job $x_{j}$ in the next sampling. To avoid the optimal value is filtered out during evolution, probability $C_{i j}=0$ should be modified with parameter $\alpha$. Modification principle as follows: count up the number of $C_{i j}=0(i=1,2, \ldots, \mathrm{n} ; l=j)$ and denoted by $t$. If $C_{i j}=0(l!=j), C_{i j}=\alpha / t$, else $C_{i j}=(1-\alpha)^{*} C_{i j}(l!=j)$;
4) Using probability matrix and the Monte Carlo method to sample probability model for a new generation population. In order to make the solution better and the convergence rate faster, of course, appropriate crossover operator and mutation operator and so on can be added in. Termination strategy in this paper is that algorithm achieves the maximum evolution times.

## C. Algorithm flow chart

The flow chart of multi-objective EDA based on classification has a multi-closed loop process control link, as the flow chart shown in Figure 3. What need points out is that $k$ is iteration variable of the outer layer and $i$ is iteration variable of the inner layer.

## V. SIMULATION AND EXPERIMENT

In this paper, using the proposed algorithm based on multiobjective classification to compare with the traditional method based on weights setting. The simulation involves three types of objective which, including job tardiness objective, sum of penalty objective and production cost objective, involved
formula (8)-(11). In this example, there are eight jobs, and each job has six stages which corresponding with parallel machines and delivery date of each job are respectively shown in Table 1 and Table 2.

Generally believed that the processing time of all machines on the same stage should be the same, but here considering the different processing performance of each machine, the processing time is different from different machine on the same stage. In the simulation experiment, the processing time of a job is automatically generated, as shown in Table 5. The objective parameters related in the example are shown in Table 3 and Table 6.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Multi-objective EDA based on classification
In this paper, using software Visual Studio 2010 to program. The parameters setting of EDA is that population size equals 100 , the number of iteration equals 50 and the correction factor equals 0.3 . The objective setting of the new algorithm is that the number of tardiness job equals 0 , sum of penalty is less than 400 , and the production cost should be minimized. Traditional multi-objective algorithm based on weight setting is shown in Table 4.

At the end of the program, the results of each objective and the resulting Gantt chart are respectively shown in Table 7, Figure 4 and Figure 5. The iterative curve of direct production cost objective during the search is shown in Figure 6.

TABLE I. Parallel Machine of Each Stage

TABLE II. Delivery Date of Each Job

TABLE III. Related Parameters

TABLE IV. Weight of Each ObJective

![img-3.jpeg](img-3.jpeg)

Fig. 4. Gantt chart of multi-objective EDA based on classification
![img-4.jpeg](img-4.jpeg)

Fig. 5. Gantt chart of multi-objective EDA based on weight setting

TABLE V. WORR Time of Each Job on Parallel Machine at Each Stage

TABLE VI. Cost Rate


TABLE VII. Results COMPARATON of Two Algorithm


All kinds of symbols in Figure 6 respectively represent the optimization objective iteration curve of multi-objective EDA
based on classification, multi-objective EDA based on weight setting. As can be seen from Figure 6, the search value of the algorithm proposed in this paper is always superior to the traditional algorithm corresponding to optimization objective, and the search speed of new algorithm is also faster than the traditional EDA.

Randomly generated initial population, the remaining parameters do not make any change and do the simulation again. Comparison of iterative curve shown in Figure 7.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Iteration curve comparation 1
![img-6.jpeg](img-6.jpeg)

Fig. 7. Iteration curve comparation 2
After changing the parameters, continue to experiment, all results show that the optimization objective of the proposed multi-objective algorithm based on classification gets a better solution than the traditional multi-objective algorithm under satisfied constrained objective. The result shows that the novel algorithm has the good feasibility, and it also has an obvious advantage, the better practicability and maneuverability, compared with the traditional multiobjective optimization methods. It can provide a good solution for ATM multi-objective scheduling problems.

## VI. CONCLUSION

Large numbers of practical engineering problems are multi-objective optimization problems, and production scheduling problem is no exception. In academic community, the production scheduling of multi-objective optimization problem has been done a lot of research, but the practical application of actual engineering is very few. This paper introduces a new multi-objective EDA based on classification for the ATM production scheduling problem. For the requirement of the ATM, the actual objectives were divided into constrained objective and optimized objective. According to the needs of decision-makers, objective decision given in advance, finally, this algorithm was used to
produce a feasible scheduling which satisfied the corresponding conditions. Results confirm that the proposed method showed its superior performance for solving multiobjective ATM scheduling problem in contrast to traditional multi-objective optimization methods, yields excellent feasibility, practicability and maneuverability, and should thus be helpful in the actual business.
