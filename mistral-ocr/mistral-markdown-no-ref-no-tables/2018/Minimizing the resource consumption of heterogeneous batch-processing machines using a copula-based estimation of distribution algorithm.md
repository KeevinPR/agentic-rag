# Minimizing the resource consumption of heterogeneous batch-processing machines using a copula-based estimation of distribution algorithm 

Chuang Liu ${ }^{\mathrm{a}}$, Huaping Chen ${ }^{\mathrm{a}}$, Rui Xu ${ }^{\mathrm{b}, *}$, Yu Wang ${ }^{\mathrm{a}}$<br>${ }^{a}$ School of Management, University of Science and Technology of China, Hefei 230026, China<br>${ }^{\mathrm{b}}$ School of Business, Hohai University, Nanjing 210098, China

## H I G H L I G H T S

- A flow shop scheduling problem on batch-processing machines is considered.
- The objective is to minimize resource consumption under the deadline constraint.
- An attempt is made to solve the scheduling problem by using the copula-based EDA.
- An advanced dynamical adjustment to correction algorithm is developed.
- Computational results show that the copula-based EDA outperforms GA, PSO and MIMIC ${ }_{\mathrm{c}}$.


## ARTICLE INFO

## Article history:

Received 9 May 2017
Received in revised form 2 August 2018
Accepted 29 August 2018
Available online xxxx

## Keywords:

Flow shop
Batch-processing machines
Estimation of distribution algorithm
Resource consumption

## A B S T R A C T

The two-stage flow-shop scheduling problem investigated in this work aims minimize the resource consumption of non-identical job sizes. The flow shop consists of two batch-processing machines (BPMs): a parallel batch BPM and a sequential BPM. The makespan and resource consumption are considered together in this study, the makespan is the constraint condition, and the resource consumption is the objective. A copula-based Estimation of Distribution Algorithm (cEDA) is used to solve the problem. In this study, the individuals are coded by the allocated resource sequences of all jobs in two machines, and the convex resource consumption function is adopted to simulate the relationship between the processing time of the jobs and the resources allocated to the jobs. A Gaussian distribution is adopted as the marginal probabilistic distribution of all the components. The proposed copula function $C_{1}$ assumes independence among the components, whereas the Clayton copula function $C_{2}$ assumes that all components are interrelated and introduced for comparison. The computational experiments and comparisons verify the effectiveness of the proposed cEDA. In addition, the copula functions $C_{1}$ and $C_{2}$ adopted in the proposed cEDA approach are compared.
(c) 2018 Elsevier B.V. All rights reserved.

## 1. Introduction

Resource conservation and green manufacturing have become critical in the sustainable development of modern industrial companies. A higher resource efficiency result in less expenses cost and less environmental pollution. Production systems that consider resource allocation and enhance resource efficiency, have attracted the attention of researchers in the context of manufacturing industries, such as the steel industry Müller et al. [1], Dahlström and Ekins [2], the food processing industry Henningsson et al. [3], Pagotto and Halog [4], textile industries Martínez [5], chemical industries García et al. [6] and the coating/painting industry Alkaya

[^0]and Demirer [7]. Jia et al. [8] investigated the problem of minimizing the makespan and the total electric power resource cost on a set of parallel identical batch-processing machines (BPMs). In problems that consider resource consumption, the processing time is generally determined by the amount of resources allocated.

In this work, the flow-shop scheduling problem treats resource consumption as the objective. The flow shop consists of two machines: the first machine, $M_{1}$, is a parallel BPM, and the second machine, $M_{2}$, is a sequential BPM. All of the jobs may have different sizes, and all of the jobs are ready to be processed at time zero. Each job must be processed successively on two machines. The processing time of each job on one machine depends on the amount of allocated resources. More resources, results in a shorter processing time for each job. The same amount of resources may result in different processing times for different jobs. On machine $M_{1}$, all of the jobs in the same batch can be processed simultaneously, and


[^0]:    * Corresponding author.

    E-mail addresses: chuang@mail.ustc.edu.cn (C. Liu), hpchen@ustc.edu.cn (H. Chen), rxu@hhu.edu.cn (K. Xu), raimw@mail.ustc.edu.cn (Y. Wang).

each job can share the resource allocated to the jobs belonging to the same batch. On machine $M_{2}$, the setup time is considered. The setup operation can be performed only after the batch arrives at $M_{2}$. The setup time $\left(T^{*}\right)$ is determined by the allocated resource $\left(u^{i}\right)$. The batch cannot wait between two machines(i.e., no-wait). If $M_{2}$ is busy, the batch that has been processed completely on $M_{1}$ must be blocked. In addition, the scheduling scheme must follow the rule that the constituents of each batch and the batch processing sequence on the two machines are identical. The objective of this problem is the amount of resource consumed, and the makespan $C_{\text {max }}$ is a constraint condition that cannot be greater than the deadline $D^{i}$. If $C_{\max }$ is greater than $D^{i}$, more resources must be invested to reduce the processing time and $C_{\max }$. Lower resource consumption typically results in higher resource utilization.

Practical applications of the problem addressed in this work can be easily found in industry. For example, Muthuswamy et al. [9] described a cleaning process observed at a sensor manufacturing facility. There is a boning operation, which establishes the electronic circuitry in a wire bonding machine. The substrates used for sensors are made of ceramic. Because residuals in the substrate could lead to defects in subsequent operations, the residuals must be removed. A substrate with residuals requires two cleaning operations in two sets of baths. In the first bath, because multiple parts that are attached to the same fixture can be cleaned at the same time, the cleaning time of a fixture is equal to the time required to clean the part with the longest cleaning time. Next, all parts belonging to the same batch move across a water jet to wash the chemicals and any additional residuals on the substrate in the second bath. Because one jet can wash only one part, a batch's cleaning time is equivalent to the sum of all of the parts in that batch. Similar practical applications can be found in [10], [11], [12]. In the manufacturing industry, optimizing resource consumption objective can reduce the cost of production, including the financial outlay, cost of manpower, cost of equipment and cost of fossil fuels. Decreasing the cost of manpower means that the manufactured products have greater competitiveness in the market, and a lower consumption of fossil fuel can result in fewer pollutants and lower waste gas purification costs [13], [14], [15], [16].

The remainder of this study is organized as follows. Section 2 reviews the flow shop with BPMs, the resource consumption function (RCF) and the resource allocation policy of resources in a batch. We define and formulate the problem in Section 3. In Section 4, the solution representation and population initialization, the marginal probabilistic model, the proposed copula function, and the copula updating approach are explained in succession. Next, the approach for forming and sequencing batches as well as the correction algorithm for individuals are presented as well. In addition, the algorithm representation of the copula-based estimation of distribution algorithm (cEDA) is described. Computational experiments and comparisons among the different algorithms are provided in Section 5. Finally, the conclusions of this work are provided in Section 6.

## 2. Literature review

### 2.1. Flow shop with BPMs

Batch-processing problems began from the research that Lee et al. [17] initially introduced in their study of the batch-processing problem. This problem was abstracted from an industrial model of a burn-in oven in a semiconductor burn-in operation. The batchprocessing operation aims to reduce the amount of resources consumed in the economic production procedure. Since then, BPMs have been widely applied in various industry sectors, ranging from traditional manufacturing to electronic chip processing. Lee et al. [17] examined the BPM of scheduling semiconductor burnin operations. Tang et al. [18] presented a single BPM scheduling
problem considering transportation and deterioration in a steel production setting. Zhou et al. [19] considered a parallel BPM scheduling problem in the presence of non-identical job sizes and arbitrary release times.

There are two BPMs: a parallel BPM (p-BPM), which can process jobs simultaneously in the same batch and a sequential BPM (s-BPM), which can process jobs serially in the same batch. The notations p-BPM and s-BPM are adopted from Oulamara [12] to represent the type of BPM. More specially, p-BPM means that the first machine, $M_{1}$, is a parallel BPM, and s-BPM means that the second machine, $M_{2}$, is a sequential BPM. The aforementioned BPMs are all p-BPMs. Mathirajan and Sivakumar [20] reviewed p-BPM and s-BPM problems in the semiconductor manufacturing industry.

The studies described above seldom considered the controllable processing time of jobs with resource constraints. In addition, batch processing with a controllable processing time is more complex than normal single-machine scheduling due to the resource consumption involved. However, resource consumption, which is an economically influential factor related to the processing cost, plays an increasingly significant role in making economic and industrial decisions.

The two types of BPMs (p-BPM and s-BPM) have distinct practical applications in many fields of industrial production. The two type of BPMs have different approaches to allocating resources to jobs: p-BPM typically adopts an even resource allocation policy (ERA, such as Ng et al. [21]), whereas a s-BPM employs a manually controllable resource allocation policy (MCRA, such as Oron [22]). Batch-processing scheduling problems, which consider resource consumption, will lead to the machines' controllable processing time or setup time. In addition, the controllable processing time may increase the complexity of the problem.

There are more significant and practical multi-stage flow-shop scheduling problems that are more complex than scheduling problems with a single machine. Flow-shop scheduling problems require consideration of the flow operation from the upstream machine to the downstream machine. Multi-stage flow-shop scheduling problems are widely used in the production procedure environment.

The work in this paper can be regarded as an extension of the classical two-machines flow-shop scheduling problems with two BPMs that do not consider controllable processing time, such as [9], [12], [23], [24]. It is easily verified that the extended problem addressed in this work can be reduced to the classical problem after affixing a resource allocation to all jobs. Once the resource allocation to all jobs is fixed, an optimal job-processing order must be determined from all possible job orders to obtain the minimum value of the makespan. In other words, the problem in this work has been converted to the classical scheduling problem, which is similar to the studies above. Those studies all addressed the twostage flow shop, in which one machine was a parallel BPM and the other machine was a sequential BPM. However, they examined only the objective of makespan, not resource consumption. In addition, only a few researchers studied problems that consider resource consumption, and they typically treated resource consumption in the problem as the constraint, not as an objective. For example, Shabtay et al. [25] considered a no-wait two-machine flow-shop scheduling problem with convex resource-dependent processing times. Janiak et al. [26] presented a survey of resource management in machine-scheduling problems.

Some researchers have studied the resource-related objectives. For instance, Vickson [27] studied the linear combination of jobprocessing cost and flow cost in a single machine, where the job-processing cost was related to the amount of resources consumed. Vickson [28] analyzed a similar problem involving a tardiness criterion in two single machines. Nowicki and Zdrzałka

[29] considered both the makespan and resource consumption in a two-machine flow shop. However, the two machines were not BPMs, and the RCF was a linear function; thus, the function did not obey the law of diminishing marginal returns. Janiak [30] addressed the problem of minimizing resource consumption in the two flow-shop scheduling problem. Ng et al. [31] examined both earliness/tardiness and the amount of resources consumed in a single machine. Shabtay [32] optimized traditional scheduling objectives and considered the resource constraint.

In scheduling problems that consider resource consumption, job-processing times can be affected by the amount of resources used, such as manpower and nonrenewable fossil resources. Therefore, the processing times of jobs are not constant. The introduction of resource consumption increases the level of complexity of this type of problem Janiak et al. [26].

### 2.2. Resource consumption function

Traditional scheduling problems with controllable processing times generally require the RCF to be selected, because different types may not only influence the processing time of jobs and the setup time of machines, but also impact the minimization of scheduling problem objective. For example, over-simplified RCFs may not fit practical production well. In the remainder of this section, we provide a general review of the various RCFs.

Researchers typically adopt a linear resource function or a convex resource function, when examining scheduling problems in a manner that considers the resource constraint. Some researchers [31,33-35], have addressed scheduling problems with a controllable processing time, which was a linear decreasing function of the amount of resources allocated to the jobs.

Vickson [28] presented an approach to solve two singlemachine sequencing problems with a processing time that was influenced by a linear RCF. Janiak [30] developed a two-processor flow-shop problem with a linear resource function, which had the form
$p_{j v}=p_{j v}\left(u_{j v}\right)=b_{j v}-a_{j v} u_{j v}, \quad 0 \leq u_{j v} \leq \bar{u}_{j v}$,
$j=1,2, \ldots, n, \quad v=1,2$,
where $a_{j v}, b_{j v}$ are known parameters and $u_{j v}$ is the amount of resources allocated to job $J_{j}$ in machine $M_{v} . \bar{u}_{j v}$ is the upper bound on the amount of resources that can be allocated to task $T_{j v}$. These types of RCFs have been proposed in many papers. However, the linear RCFs have limited applicability for practical physical and economic procedures, because they fail to reflect the law of diminishing marginal returns.

To overcome that defect, some researches, [36-38], introduced a convex resource function. The convex resource function considers the law of diminishing marginal returns, an economic law that is often applied in practical production. The form of convex resource functions that are generally used in the literature is as follows:
$p_{j}\left(r_{j}\right)=\left(\frac{w_{j}}{r_{j}}\right)^{k}, \quad r_{j}>0, k>0$,
where $w_{j}\left(w_{j}>0\right)$ is a parameter related to the workload of job $J_{j}$, and $r_{j}\left(r_{j}>0\right)$ is the amount of resources allocated to job $J_{j}$, $k$ is a constant positive parameter that can take a value of 1 or 0.5 , for example. Monma et al. [36] noted that different k values may be applicable in different problems. For example, (1) $\mathrm{k}=1$ is applicable when the processing time of a job is inversely proportional to money or manpower resources, as in many practical government or industrial projects, and (2) $\mathrm{k}=0.5$ corresponds to the application extracted from very large scale integration (VLSI) circuit design, where the product of silicon area resources $\left(r_{j}\right)$ and the square of the time spent is a constant.

Yedidsion et al. [39] presented a general type of convex resource function that was more suitable for practical applications, and proposed four properties that the convex resource function should obey. Liang et al. [40] extended the properties proposed by Yedidsion et al. [39], and then discarded Property 4 (the job-processing time is infinite, if no resources are allocated) and proposed a new Property 5 that imposed a constraint of an initial processing time and an incompressible time for each job.

### 2.3. Allocation policy of resource in a batch

In a parallel BPM, all of the jobs in the same batch are processed simultaneously, and all jobs can share their entire resources allocated to each job in the same batch. The allocation approach to resources can affect the quality of the solution and thus the objective.

Three allocation policies for resources have been presented in the literature: the manually controllable resource allocation policy (MCRA, such as Oron [22], even resource allocation (ERA, such as Ng et al. [21] policy and proportional resource allocation (PRA, such as Biskup and Jahnke [41]. The essential difference between ERA and MCRA is the level of arbitrary resource allocation. MCRA can permit the resource allocation scheme, provided that the sum of the resource allocated to each job in same batch is equal to the total batch resources. However, ERA is strict in that each job in same batch receives equal resources. This means that each job belonging to the same batch shares the resources assigned to that batch in the ERA policy equally.

### 2.4. Copula theory

The term copula was first presented by Sklar [42]. Schweizer and Wolff [43] first studied the dependence among random variables and presented the classical Schweizer and Wolff's $\sigma$, which can measure the level of dependence among variables. In copula theory, the copula function can be viewed as a multivariate function. The formal definition of the copula function is provided in Nelsen [44]. The copula function can comprehensively reflect a multivariate relationship. Many copula functions can be used according to the definition of the copula function. Examples include the t copula function Demarta and McNeil [45], the Clayton copula and the Archimedean copula Whelan [46].

In addition, Nelsen [44] proved Sklar's Theorem in n dimensions, which is the essential to the theory of the copula-based estimation of distribution algorithm (cEDA). The n-dimensional Sklar's theorem can be described as follows Nelsen [44]:

Theorem 2.1. Let $H$ be an n-dimensional distribution function with margins $F_{1}, F_{2}, \ldots, F_{n}$. Then there exists an n-copula $C$ such that for all $\mathbf{x}$ in $\mathbf{R}^{n} / R$ is the closed set $[-\infty,+\infty]$ ),
$H\left(x_{1}, x_{2}, \ldots, x_{n}\right)=C\left(F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \ldots, F_{n}\left(x_{n}\right)\right)$
If $F_{1}, F_{2}, \ldots, F_{n}$ are all continuous, then $C$ is unique; otherwise, $C$ is uniquely determined on $\operatorname{RanF}_{1} \times \operatorname{RanF}_{1} \times \ldots \times \operatorname{RanF}_{n}$. $\left(\operatorname{RanF}_{n}\right.$ denotes the Range of $F_{n}$ )

According to Theorem 2.1, a multivariate joint distribution can be divided into two parts, each random variable marginal distribution function and a copula function. Therefore, each random variable marginal distribution and the proposed copula function to be used in this work can be determined separately. Introducing the copula function to EDAs can simplify the process of building the probability distribution model and reduce its performing time. A more detailed description of copula theory can be found in Nelsen [44].

Table 1
Notations.

## 3. Problem formulation

A resource allocation vector of all jobs on two machines and a job processing order are required to be found, such that the total resource consumption is minimized under the constraint of a given deadline $D^{j}$. For a given resource allocation vector $(\pi)$, there are many available job orders to be selected, but a different jobprocessing order will yield a different a $C_{\max }$. If the $C_{\max }$ is larger than deadline $D^{j}$, that resource allocation vector $(\pi)$ will be not valid, and should be amended by the correction algorithm.

The problem is formulated in this section. To formulate the problem to be addressed, we will first provide all of the notations employed in this work and then formulate the objective, constraints, decision variables and proposed RCF function. Next, the mathematical formulation of the addressed problem can be obtained.

### 3.1. Notations

The notations used in this work, such as the subscripts and variables, are summarized in Table 1.

### 3.2. Hypotheses of the problem

To clearly describe the problem to be addressed in this work, the following hypotheses will be stated in detail:

1. There are $n$ independent and non-identical jobs. $J_{j}$ denotes the $j$ th $(j=1,2, \ldots, n)$ job, and $s_{j}$ denotes the size of job $J_{j}$. For job $J_{j}$, the processing procedure thus consists of two tasks, $T_{j 1}$ on $M_{1}$ and $T_{j 2}$ on $M_{2}$.
2. The allocation unit of the resource is task $T_{j v}$; the amount of resources assigned to task $T_{j v}$ is $u_{j v}$. The processing time of task $T_{j v}$ on machine $M_{v}$ is $p_{j v}\left(u_{j v}\right)$. Therefore, the total amount of resources assigned to job $J_{j}$ is $r_{j}$, which is the sum of $u_{j 1}$ and $u_{j 2}$.
3. The capacity of the first machine, $M_{1}$, is denoted by $\Theta$, and machine $M_{1}$ can process a batch of jobs provided that the total size of all jobs assigned to the batch does not exceed its capacity. Once the job is processed in the machine, it cannot be preempted. After finishing processing the batch on machine $M_{1}$, that batch can either block machine $M_{1}$ àr go to machine $M_{2}$ directly for processing, based on whether machine $M_{2}$ is busy.
4. The processing time of batch $B_{i}$ on machine $M_{1}$ is equal to the longest job-processing time among all of the jobs in that batch. The processing time of batch $B_{i}$ on $M_{1}$ can be calculated by $P_{i 1}=\max \left\{p_{j 1} \mid J_{j} \in B_{i}\right\}$. On machine $M_{2}$, the processing time of batch $B_{i}$ is equivalent to the sum of the processing times of all jobs in the same batch.
5. The ERA policy is adopted on machine $M_{1}$, and the MCRA policy is adopted on machine $M_{2}$ in this work.
6. The objective of the problem in this work is the total amount of the resource consumed in the scheduling process.
7. The amount of resources allocated to each batch on machine $M_{2}$ for the setup operation is the constant $u^{2}$, and the corresponding time is $T^{2}$.
8. The makespan $C_{\max }$ should not exceed the given deadline $D^{j}$.

### 3.3. Proposed resource consumption function

Considering the law of diminishing marginal returns in the production and processing environment, the RCF adopted in this work can be expressed as follows Yedidsion et al. [39]:
$p_{j v}\left(u_{j v}\right)=\left(\frac{w_{j v}}{u_{j v}}\right)^{k}, u_{j v}>0$
where $w_{j v}$ is the parameter related to the workload of job $J_{j}$ on machine $M_{v}$, and $u_{j v}$ is the resources allocated to job $J_{j}$ on machine $M_{v}$. The proposed RCF obeys all four properties from Yedidsion et al. [39].

![img-0.jpeg](img-0.jpeg)

Fig. 1. RCF and resource sensitivity.

The concept of resource sensitivity from Liang et al. [40], which is the derivative of the processing time $p_{j v}\left(u_{j v}\right)$ on resource $\left(u_{j v}\right)$, is introduced as
$e_{j v}=\frac{\mathrm{d} p_{j v}\left(u_{j v}\right)}{\mathrm{d} u_{j v}}, u_{j v}>0$
where $e_{j v}$ denotes the derivative of $p_{j v}\left(u_{j v}\right)$ on $u_{j v}$.
The curves of the $\operatorname{RCF}\left(p_{j v}\left(u_{j v}\right)\right)$ and resource sensitivity $\left(e_{j v}\right)$ are illustrated in Fig. 1. A larger value of $u_{j v}$, is associated with less diminishing marginal returns.

### 3.4. Mathematical model

According to the 3-field problem classification scheme, $\alpha|\beta| \gamma$, for scheduling problems Graham et al. [47], the problem in this work can be described as follows:
$F_{2}\left|p-B P M, s-B P M\right.$, no - wait, $s_{j}, p_{j v}\left(u_{j v}\right)$
$=\left(\frac{w_{j v}}{u_{j v}}\right)^{k}, C_{\max } \leq D^{l} \mid \sum_{j=1}^{n} r_{j}+m u^{s}$,
where $D^{l}$ is the deadline assigned by the scheduler. Based on the introduction of the parameters and the detailed description of the problem set forth above, the mathematical model of the problem in this work is formulated as follows:
Minimize $\quad \sum_{j=1}^{n} r_{j}+m \cdot u^{s}$
Subject to:

$$
\begin{aligned}
\sum_{i=1}^{m} X_{\beta}=1, & j=1, \ldots, n \\
\sum_{j=1}^{n} s_{j} X_{j i} \leq \Theta, & i=1, \ldots, m \\
C_{\max } \leq D^{l}, & i=1, \ldots, m \\
\psi_{i 1}=C_{i-1,1}, & i=2, \ldots, m \\
C_{i 1} \geq \psi_{i 1}+P_{i 1}, & i=1, \ldots, m \\
C_{i 2} \geq C_{i 1}+P_{i 2}+T^{s}, & i=1, \ldots, m \\
C_{\max } \geq C_{i 2} \geq C_{i 1} \geq \Psi_{i 1} \geq 0, & i=1, \ldots, m
\end{aligned}
$$

Objective (7) minimizes the amount of resource consumed. Constraint (8) ensures that each job is assigned to only one batch. Constraint (9) ensures that the total size of jobs in the same batch does not exceed the machine's capacity. Constraint (10) ensures that makespan $C_{\text {max }}$ is not greater than deadline $D^{l}$. Constraint (11) requires that the starting time of batch $B_{i}$ on machine $M_{1}$ is equal to the department time of batch $B_{i-1}$ on machine $M_{1}$. Constraint (12) indicates that the department time of the batch $B_{i}$ on machine $M_{1}$ is greater than the sum of starting time and its processing time on machine $M_{1}$. Constraint (13) determines the completion time of each batch on machine $M_{2}$. Constraint (14) determines the makespan $C_{\text {max }}$.

Because $r_{j}=u_{j 1}+u_{j 2}$ and $U_{i}=\sum_{i_{j} \in \mathcal{X}_{i}} u_{j v}$, the objective in Eq. (7) can be deduced as the following formulations:

$$
\begin{aligned}
& \text { Min } \sum_{j=1}^{n} r_{j}+m \cdot u^{s} \\
& =\operatorname{Min} \sum_{j=1}^{n} u_{j 1}+\sum_{j=1}^{n} u_{j 2}+m \cdot u^{s} \\
& =\operatorname{Min} \sum_{i=1}^{m} U_{i 1}+\sum_{i=1}^{m} U_{i 2}+m \cdot u^{s}
\end{aligned}
$$

## 4. Proposed cEDA

In reality, the cEDA is a novel improved Estimation of Distribution Algorithm (EDA) based on the copula function for addressing optimization problems.

EDA approaches can be divided into two categories, the discrete EDA for discrete optimization problems, and the continuous EDAs for continuous optimization problems. Ceberio et al. [48] gave a review on EDAs in permutation-based combinatorial optimization problems. On the one hand, discrete EDAs can be classified as univariate, bivariate and multivariate according to the probabilistic model employed. Univariate EDAs assume that all of the variables are independent; examples include the PBIL Baluja [49], Sebag and Ducoulombier [50] and the UMDA Larrañaga [51]. Bivariate EDAs consider dependencies between pairs of variables; examples include the BMDA Pelikan and Muehlenbein [52] and the MIMIC De Bonet et al. [53]. Multivariate EDAs consider multivariate correlations, such as the Bayesian optimization algorithm Pelikan et al. [54]. And Ceberio et al. [55] proposed a distance-based ranking model EDA for the flowshop scheduling problem. On the other hand, the continuous EDAs are developed on the basis of discrete EDA, the idea of many algorithms from discrete EDA. The UMDAc approach Larrañaga et al. [56] is extended from the UMDA approach above. The PBILc approach Sebag and Ducoulombier [50] is developed from the PBIL approach above. The MIMIC ${ }_{c}$ approach Larraanaga and Lozano [57] is derived from the MIMIC approach above.
cEDAs can address the marginal distribution and the correlation among all components separately. Wang et al. [58] proved that cEDAs can simplify the parameter learning operation and sampling procedure by incorporating the copula function into the EDA. The related studies that consider EDAs based on the copula function are described here. Ye et al. [59] proposed a cEDA based on a class of nested Archimedean copulas constructed with Lery subordinators. Cuesta-Infante et al. [60] investigated the use of empirical and Archimedean copulas in EDAs. De Mello et al. [61] proposed a cEDA based on a multivariate extension of the Archimedean with parameter updating for number optimization problems. Salinas-Gutiérrez et al. [62] presented the use of copula functions and graphical models in EDAs. Gao et al. [63] considered multi-objective optimization problems by incorporating the multivariate Archimedean copulas function into EDAs.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Illustration of the solution representation.

Considering the complexity of the correlations among all of the components in this problem, and the fact that few studies treat resource consumption as the objective, the cEDA approach is employed in this study to fill this gap in the literature. The key cEDA procedures Wang et al. [58] can be described as follows:

- Randomly initialize the population.
- Calculate the fitness value of all individuals.
- Select the better individuals according to the fitness function and selection policy.
- Construct the copula distribution model.
- Sample new individuals from the constructed distribution model.

In this section, the solution representation and population initialization will be introduced first. The proposed marginal probabilistic model and two different copula functions used in this work can be illustrated successively. In addition, to calculate the makespan $C_{\max }$ of each scheduling scheme, this section describes the proposed approach for forming and sequencing batches and the correction algorithm for individuals. Finally, the detailed algorithm representation of cEDA is given.

### 4.1. Solution representation and population initialization

The solution to this problem can be described as follows. A solution is a resource vector allocated to each job in two machines ( $M_{1}$ and $M_{2}$ ). The amount of the component in a resource vector is equal to 2 n , which is the product of the number of machines $(v=2)$ and the number of jobs $(n)$. In other words, the solution can be denoted as $\left(u_{11}, u_{21}, \ldots, u_{n 1} ; u_{12}, u_{22}, \ldots, u_{n 2}\right)$, where the top n components are the resources allocated to the $n$ jobs in machine $M_{1}$ and the last $n$ components are the resources allocated to the $n$ jobs in machine $M_{2}$. The representation of the solution is illustrated in Fig. 2.

The initial population can impact the convergence speed of the cEDA and the solution quality of the problem. Considering the diversity of the initial population, the initial population ( $N$ individuals) is generated randomly from a uniform distribution in the solution space.

### 4.2. Marginal distribution function and copula function

The marginal distribution functions represent the distribution of the components, and the copula function represents the correlation among all components. In the literature related to probabilistic models of EDA, the Gaussian distribution is easily found, such as Lu and Yao [64], Yuan and Gallagher [65], Wang et al. [58] and Su and Chow [66].

The Gaussian distribution is adopted as the marginal distribution function for all components $u_{j v}\left(j=1,2, \ldots, n, v=1,2\right.$ ). For two proposed distinct copula functions, the proposed marginal distribution functions are all Gaussian distributions. In particular, each component in the resource vector $\left(u_{11}, u_{21}, \ldots, u_{n 1} ; u_{12}, u_{22}\right.$, $\ldots, u_{n 2}$ ) obeys the Gaussian distribution $N\left(\mu_{j v}, \sigma_{\mu_{j}}^{2}\right)$. For component $u_{j v}$, its marginal distribution function $F_{j v}\left(u_{j v}\right)$ can be formulated as follows:
$F_{j v}\left(u_{j v}\right)=\int_{-\infty}^{u_{j v}} \frac{1}{\sqrt{2 \pi} \sigma_{j v}} \exp \left(-\frac{\left(x-\mu_{j v}\right)^{2}}{2 \sigma_{j v}^{2}}\right) d x$

For resource vector $\left(u_{11}, u_{21}, \ldots, u_{n 1} ; u_{12}, u_{22}, \ldots, u_{n 1}\right)$ in this work, the interrelationship among $2 n$ components is considered independent, and the non-independent relationship among all components is adopted as a comparison.

Theorem 4.1. Let $x_{1}, x_{2}, \ldots, x_{n}$ be continuous random variables. Then $x_{1}, x_{2}, \ldots, x_{n}$ are independent if and only if $C_{x_{1}, x_{2}, \ldots, x_{n}}=$ $\prod\left(F_{1}\left(x_{1}\right), \ldots, F_{n}\left(x_{n}\right)\right)$.

According to Theorem 4.1 from Nelsen [44] set forth above, the proposed copula function $C_{1}$, which assumes that all variances are independent, can be described as follows:

$$
\begin{aligned}
C_{1} & =C_{x_{11}, \ldots, u_{n 2}} \\
& =\prod\left(F_{11}\left(u_{11}\right), \ldots, F_{n 1}\left(u_{n 1}\right), F_{12}\left(u_{12}\right), \ldots, F_{n 2}\left(u_{n 2}\right)\right)
\end{aligned}
$$

From Eq. (17), copula function $C_{1}$ is the product of the independence univariate marginal distribution functions.

To compare the effectiveness of different copula functions in this scheduling problem, another copula function $C_{2}$, in which all components are non-independent, is introduced. Copula function $C_{2}$ is a nested Clayton copula function that is the product of two Clayton copula functions. In copula function $C_{2}$, the interrelation between the components in machines $M_{1}$ and $M_{2}$ is independent. Function $C_{2}$ can be described as follows:
$C_{2}=\prod\left(C_{a}, C_{b}\right)$,
where $C_{a}$ and $C_{b}$ are both Clayton copula functions. Copula functions $C_{a}$ and $C_{b}$ handle the resource components in machines $M_{1}$ and $M_{2}$, respectively. The Clayton copula functions $C_{a}$ and $C_{b}$ that are introduced from Schweizer and Sklar [67] are formulated in Eq. (19). The generator $\varphi$ for Clayton copula functions $C_{a}$ and $C_{b}$ are $\varphi(t)=t^{-\theta}-1(\theta \geq 0)$.

$$
\left\{\begin{array}{l}
C_{a}=\left(1+\sum_{j=1}^{n}\left(u_{j v}^{-c_{a}}-1\right)\right)^{-\frac{1}{c_{a}}}, v=1 \\
C_{b}=\left(1+\sum_{j=1}^{n}\left(u_{j v}^{-c_{b}}-1\right)\right)^{-\frac{1}{c_{b}}}, v=2
\end{array}\right.
$$

The definition and related details of Clayton copula function $C_{a}$ and $C_{b}$ are provided in Alsina et al. [68], Nelsen [44].

Next, copula function $C_{2}$ in Eq. (18) can be deduced as follows:

$$
\begin{aligned}
C_{2} & =\prod\left(C_{a}, C_{b}\right) \\
& =\left(1+\sum_{j=1}^{n}\left(u_{j 1}^{-c_{a}}-1\right)\right)^{-\frac{1}{c_{a}}}\left(1+\sum_{j=1}^{n}\left(u_{j 2}^{-c_{b}}-1\right)\right)^{-\frac{1}{c_{b}}}
\end{aligned}
$$

Marshall and Olkin [69] proposed a sampling approach for copula functions $C_{a}$ and $C_{b}$, and the details of the sampling approach for the Clayton copula function are provided in Section 4.3. The cEDA approach with copula function $C_{1}$ is denoted by $c E D A_{c 1}$, and the cEDA approach with copula function $C_{2}$ is denoted by $c E D A_{c 2}$. In the remaining sections, $c E D A_{c 1}$ is abbreviated as cEDA, if not explicitly specified.

### 4.3. Copula updating approach: learning and sampling

As noted above, the cEDA approach generates new individuals by sampling from the copula distribution model, potentially influencing the performance of the proposed cEDA approach. This section discusses the learning of the parameters of the copula distribution model and sampling from the constructed copula distribution model.

Table 2
Details of $S$ individuals.

Note: $u_{j k}^{k}$ is $u_{j c}$ of the $k$ th individual.

The truncation selection policy is employed to select $S$ individuals with the best objective values out of $N$ individuals in each generation. The fitness function adopted to evaluate all of the individuals can be formulated as follows:

$$
\sum_{j=1}^{n} r_{j}+m \cdot u^{s}
$$

where $r_{j}$ is the amount of the resources allocated to job $J_{j}, m$ is the number of batches formed in the algorithm, and $u_{s}$ is the amount of resources consumed for a constant setup time $T^{s}$ in machine $M_{2}$.
$S$ selected individuals in the current generation can be used to determine the $2 n$ parameters $\left(\mu_{11}, \sigma_{11} ; \ldots ; \mu_{n 2}, \sigma_{n 2}\right)$. The details of $S$ individuals (samples) are summarized in Table 2.

The parameters ( $\mu_{j c}$ and $\sigma_{j c}^{2}$ ) of all marginal distributions can be estimated individually in the cEDA approach. More specially, the first column $\left(u_{11}\right)$ in Table 2, which consists of $S$ components $\left(u_{11}^{\prime}, u_{11}^{\prime \prime}, \ldots, u_{11}^{\prime}\right)$ from the different $S$ individuals, can be used to estimate the parameters $\mu_{11}$ and $\sigma_{11}^{2}$ using the Maximum Likelihood Estimate (MLE) approach; thus, the other columns are the same.

For component $u_{j c}$ in the resource vector, there are $S$ values $\left(u_{j c}^{\prime}, u_{j c}^{2}, \ldots, u_{j c}^{S}\right)$ from $S$ selected individuals, which can be used to learn the parameters $\left(\mu_{j c}\right.$ and $\left.\sigma_{j c}^{2}\right)$ of the marginal distribution of component $u_{j c}$. To simplify the equation, $u_{j c}^{\prime}(i=1,2, \ldots, S)$ is denoted by $x_{i}$. The following equation can be obtained according to the MLE approach:

$$
\begin{aligned}
L\left(\mu_{j c}, \sigma_{j c}^{2}\right) & =\prod_{i=1}^{S} \frac{1}{\sqrt{2 \pi} \sigma_{j c}} \exp \left(-\frac{\left(x_{i}-\mu_{j c}\right)^{2}}{2 \sigma_{j c}^{2}}\right) \\
& =\left(\frac{1}{\sqrt{2 \pi} \sigma_{j c}}\right)^{S} \exp \left(-\sum_{i=1}^{S} \frac{\left(x_{i}-\mu_{j c}\right)^{2}}{2 \sigma_{j c}^{2}}\right)
\end{aligned}
$$

where $u_{j c}$ and $\sigma_{j c}^{2}$ are the mean and variance of the distribution function of component $u_{j c}$, respectively, and the results can be derived as follows:

$$
\left\{\begin{array}{l}
\hat{\mu}_{j c}=\frac{1}{S} \sum_{i=1}^{S} x_{i}=\bar{x} \\
\hat{\sigma}_{j c}^{2}=\frac{1}{S} \sum_{i=1}^{M}\left(x_{i}-\bar{x}\right)^{2}
\end{array}\right.
$$

Through the analysis above, the procedure of learning the parameters $\left(\mu_{j c}\right.$ and $\left.\sigma_{j c}^{2}\right)$ using the MLE approach for the problem in this study can be summarized as follows:

1. Prepare the data $\left(u_{j c}^{\prime}, u_{j c}^{2}, \ldots, u_{j c}^{S}\right)$.
2. Calculate $\hat{\mu}_{j c}=\bar{x}=\frac{1}{S} \sum_{i=1}^{S} u_{j c}^{\prime}$.
3. Calculate $\hat{\sigma}_{j c}^{2}=\frac{1}{S} \sum_{i=1}^{S}\left(u_{j c}^{\prime}-\bar{x}\right)^{2}$.

After learning the parameters of all marginal distributions, the copula distribution model can be obtained according to the copula
function in Eq. (17). Next, the copula function can be used to generate new individuals, i.e., the point $\left(x_{11}, x_{21}, \ldots, x_{n 1} ; x_{12}, x_{22}\right.$, $\ldots, x_{n 2}$ ) in $2 n$ dimensions, can be gained. Then, a new individual $\left(u_{11}^{\text {new }}, u_{21}^{\text {new }}, \ldots, u_{n 1}^{\text {new }}, u_{12}^{\text {new }}, u_{22}^{\text {new }}, \ldots, u_{n 2}^{\text {new }}\right)$ can be obtained according to the equation $u_{j c}^{\text {new }}=F_{j c}^{-1}\left(x_{j c}\right)$. The generated new individuals belong to the next generation.

The individuals of the next-generation population consist of 3 parts:

1. $M$ better individuals (elites), which have the best objective values from the current generation.
2. $L$ new individuals formed by a uniform distribution in the solution space;
3. $N-M-L$ new individuals sampled from the copula function.

In this work, the $S$ individuals selected to construct the copula probability model are only partly reserved for the next generation, which means that $M \leq S$. The number $M$ of the best individuals can be selected from the most recent generation according to the fitness function. To increase the diversity of the population, $L$ new individuals are sampled randomly from a uniform distribution in the solution space. The remaining $N-M-L$ new individuals are sampled from the copula function, which can guarantee the global exploration ability of the proposed cEDA approach.

More specifically, the sampling approach Marshall and Olkin [69] for the Clayton copula function $C_{a}$ is illustrated in Algorithm 1. $\theta_{a}$ is a parameter, and $\hat{\mu}_{j c}$ and $\hat{\sigma}_{j c}$ are the parameters obtained from the marginal distribution function of component $u_{j c}$. Function $F(v)$ in Algorithm 1 is the product of two Gamma $\Gamma(\alpha, \beta)$ distribution functions, in which $\alpha$ is equal to $1 / \theta$ and $\beta$ is equal to 1 , i.e., $v \sim$ $\Gamma\left(\frac{1}{\theta}, 1\right)$. The sampling approach for the Clayton copula function $C_{b}$ is the same as that for $C_{a}$.

The difference between copula functions $C_{1}$ and $C_{2}$ is the manner in which the dependencies among all of the components are handled. In $C_{1}$, all of the components are independent. In $C_{2}$, the correlation among all of the components are non-independent and complex, and the components $\left(u_{11}, u_{21}, \ldots, u_{n 1}\right)$ and $\left(u_{12}, u_{22}\right.$, $\ldots, u_{n 2}$ ) are independent. However, the correlation among $u_{11}$, $u_{21}, \ldots, u_{n 1}$ is non-independent, and this complex correlation is addressed by Clayton copula function $C_{a}$. The non-independent correlation among $u_{12}, u_{22}, \ldots, u_{n 2}$ is addressed by Clayton copula function $C_{b}$. Therefore, the sampling operation of copula function $C_{S}$ can be achieved by the sampling operation of copula function $C_{a}$ and $C_{b}$.

```
Algorithm 1 Sampling Algorithm for the Clayton copula function
    for \(k=1 \rightarrow N-M-L\) do
        Randomly generate \(v\) according to the distribution function;
        \(F(v)=\frac{1}{1+\left(v_{0}\right)} e^{-v} \cdot v^{1 / \theta_{a}-1}\);
        for \(i=1 \rightarrow n\) do
            Randomly generate independent \(v_{i}\) from the uniform dis-
                tribution of interval \([0,1]\);
            \(x_{i}=\Phi^{-1}\left(\left(-l n v_{i}\right) / v\right)=\left(1-\frac{\hat{\sigma}_{i} \ln v_{i}}{v}\right)^{-1 / \theta_{a}}\);
        end for
        Calculate \(u_{i}^{k}=F_{i}^{-1}\left(x_{i} ; \hat{\mu}_{i}, \hat{\sigma}_{i}\right)\);
    end for
```


# 4.4. Forming batches and batches sequencing decision 

The next fit (NF) approach, which is adopted for the bin-packing problem, can be applied to BPMs because of the similarity between bin packing and batch generating. The NF approach employed by Muthuswamy et al. [9] is used to generate batches in this study.

The jobs sorting operation and the general procedure of the NF approach are described in Algorithm 2.

## Algorithm 2 Next Fit Algorithm

1: Arrange jobs in some random order;
$2: i \leftarrow 1$;
$3: B_{i} \leftarrow$ Create an initial batch;
4: ResidualCap $\leftarrow$ Define the residual capacity of batch $B_{i}$;
5: ResidualCap $\leftarrow \Theta$;
6: for $j=0 \rightarrow n$ do
7: if $s_{j} \leq$ ResidualCap then
8: Pack the job $J_{j}$ to batch $B_{i}$;
9: ResidualCap $\leftarrow$ ResidualCap $-s_{j}$;
10: else
$i \leftarrow i+1$;
12: Create a new batch $B_{i}$;
13: end if
14: end for

After the operation of forming batches is complete, each job belongs to only one batch. Next, based on the approach from Muthuswamy et al. [9] and the specific character in our problem, we develop a heuristic, called the Least machine Idle Time Heuristic (LITH), for sequencing the formed batches. The fundamental idea is as follows:

1. Randomly determine the first batch to be processed.
2. Calculate the idle time of all residual unscheduled batches.
3. Choose the next batch that can result in the least idle time on two machines.
4. Repeat the three procedures above until all batches are scheduled.
The pseudo code of the LITH algorithm is described in Algorithm 3; $C_{k i}$ and $C_{i v}$ in Algorithm 3 represent the complete time of batches $B_{k}$ and $B_{i}$, respectively, on machine $M_{v}$, and the total idle time of the two machines is denoted by $Q_{i}$.

## Algorithm 3 LITH Algorithm

1: Sequence all batches randomly;
2: Rename all batches by their sequence index: $B_{1}, B_{2}, B_{3}, \ldots$;
3: Determine the head $\left(B_{1}\right)$ in the batch sequence as the batch to be processed first;
4: Calculate $C_{11}$ and $C_{12}$ of batch $B_{1}$;
5: Delete batch $B_{1}$ from the batch sequence;
6: for $k=1 \rightarrow m-2$ do
7: for $i=1 \rightarrow m-k$ do
$C_{i 1} \leftarrow \max \left\{C_{k 1}+P_{i}, C_{k 2}\right\}$
$Q_{i} \leftarrow\left(C_{i 1}-P_{i}-C_{k 1}\right)+\left(C_{i 1}-C_{k 2}\right)$;
8: end for
9: Select batch $B_{i}$ with the lowest value of $Q_{i}$;
10: Delete batch $B_{i}$ from the batch sequence;
11: Calculate $C_{k+1,1}$ and $C_{k+1,2}$;
12: end for

Fig. 3 provides an example illustrating the LITH approach. The related batch-processing times on the two machines are displayed in Table 3. The shadow parts in Fig. 3 are the idle time on the two machines. The first batch to be processed is assumed to be batch $B_{1}$. Then, the next batch to be processed must be chosen from the batch set $\left\{B_{2}, B_{3}, B_{4}\right\}$. According to Fig. 3, the idle time of schedule $S 1$ is 2 , the idle time of schedule $S 2$ is 1 , and the idle time of schedule $S 3$ is 2 . Therefore, batch $B_{3}$ is selected to be processed after batch $B_{1}$, according to the LITH algorithm.

Table 3
Batch-processing time on the two machines.

${ }^{a}$ Note: All batch-processing times contain the setup time on $M_{2}$.

### 4.5. Correction algorithm for individuals

Some of the initial individuals in each generation may not obey the deadline $\left(D^{i}\right)$ constraint. Therefore, these individuals must be amended. Based on the correction procedure from Liang et al. [70], a new advanced correction algorithm is proposed to amend the individuals that disobey the scheduling constraint $C_{\max } \leq D^{i}$. This advanced correction algorithm can dynamically adjust the component to be amended in an individual, according to the change of $e_{j v}$. The correction algorithm must be executed before the selection operation in each generation. The procedure for the correction algorithm is described in Algorithm 4.

## Algorithm 4 Correction Algorithm

1: Calculate $\left|e_{j v}\right|$ of all components in one individual;
while $C_{\max }>D^{i}$ do
Determine the maximum value of $\left|e_{j v}\right|$ among all components;
Task $T_{j v} \leftarrow$ Select the task corresponding to the maximum $\left|e_{j v}\right|$;
Add a certain amount of resources to the task $T_{j v}$;
Update $e_{j v}$ of task $T_{j v}$;
Calculate $C_{\max }$;
end while

### 4.6. Algorithm representation of cEDA

Based on the details set forth above, the pseudo code of the cEDA algorithm can be presented in Algorithm 5. In the remainder of this subsection, the computational cost of cEDA is analyzed following the steps in Algorithm 5.

The initial solutions are generated at random with the time complexity of $O(N n)$, where the $N$ is the population size and the $n$ is the number of jobs. For calculating the makespan of each individual, the forming batches and batches sequencing operation need to be done. The forming batches costs $O(n)$ time, and the batches sequencing operation takes $O(m \log m)$ time, where $m$ is the number of batches. Thus, for the population which has $N$ individuals, the time complexity is $O(N(n+m \log m))$. For the individual which violates the deadline constraint, the time complexity of the correction procedures is $O(n k)$, where the $k$ is the number of iterations of the loop in Algorithm 4. In the selection operation, all individuals are sorted by objective value. So the time complexity is $O(N \log N)$. In the copula learning process, 2 n pairs of $\mu_{j v}$ and $\sigma_{j v}^{2}$ need to learn. The learning operation has a close complexity of $O(n S)$, where $S$ is the number of better individuals selected from the population. The sampling operation from uniform distribution has a complexity of $O(\lambda n)$, where the $\lambda$ is the number of new generating individuals. In the sampling procedure from copula joint probability model, generating new individuals can be done in $O(N n)$ time. And confirming that whether each individual satisfies the deadline constraint takes $O(n+m \log m)$ time.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Example for the LITH approach.

## Algorithm 5 General framework of cEDA

1: Initialize parameters $p_{1}$ and $p_{2}$;
2: $5 \leftarrow p_{1} \cdot N ; \mathrm{M} \leftarrow p_{2} \cdot N ; L \leftarrow 5 \% \cdot N$;
3: $0 \leftarrow$ Generation counter of population $l$;
4: $l_{\max } \leftarrow$ Maximum value of generation;
5: $G_{0} \leftarrow$ Generate N initial individuals, according to the uniform distribution in the solution space;
6: while Stopping condition is not met do
for $k=1 \rightarrow N$ do
Calculate the $C_{\max }$ of the $k$ th individual in the current population;
if $C_{\max }>D^{l}$ then
Use the correction algorithm to amend the $k$ th individual;
end if
end for
$G_{l}^{\text {better }} \leftarrow$ Select $S$ better individuals from $G_{l}$ according to the selection policy;
for $k=1 \rightarrow 2 n$ do
Learn the $k$ th marginal probability distribution of $G_{l}^{\text {better }}$;
end for
Build the copula joint probability model;
Sample $L$ new individuals from the uniform distribution in the solution space;
Sample $N-M-L$ new individuals from the copula joint probability model;
$G_{l+1} \leftarrow$ Merge $G_{l}^{\text {better }}$ with the individuals sampled from Line 18 and Line 19;
$l \leftarrow l+1$;
22: end while

## 5. Computational experiments

### 5.1. Experimental design

The experiment is divided into four parts. First, $c E D A_{c 1}$ and $c E D A_{c 2}$ are compared. Second, the genetic algorithm (GA), which is a classical evolutionary algorithm, is introduced to compare with the proposed $c E D A_{c 1}$ approach. Third, the particle swarm optimization (PSO) approach, which is a computational swarm intelligence approach, is adopted for comparison with the $c E D A_{c 1}$ approach.

Table 4
Parameter settings of the experiment.
Fourth, an EDA approach, named MIMIC, algorithm, is adopted and compared for demonstrating the advantages of the proposed $c E D A_{c 1}$. Finally, the convergence trends of the four algorithms are also given in this section. In this section, $c E D A_{c 1}$ is abbreviated as cEDA, if not explicitly specified. All of the algorithms are executed in MATLAB R2017a(9.0.0.341360) using a PC(Win10, 64bit) with an Intel(R) Core(TM)i7-6700 3.4 GHz CPU and 16.00 GB RAM.

The initial population including $N$ individuals, is generated randomly from the uniform distribution in the solution space. The problem instances are generated by following the approach of Muthuswamy et al. [9], and the parameters settings employed for cEDA are determined: the number of jobs, the size of the jobs, the workload of jobs, the setup time $T^{s}$ on machine $M_{2}$, the resource consumed for setup and the capacity of the first machine. The parameter settings are presented in Table 4. For each number of jobs, 8 configurations that consider different job sizes (small and large), workloads (low and high) and deadlines (short and long) are taken into account. For the small-scale instances ( 10 and 20 jobs), medium-scale instances ( 50 and 100 jobs) and large-scale instances (200 jobs), 3 instances are generated in each configuration. Each algorithm is executed 10 times for each instance.

The value of $k$ in Eq. (4) is equal to $\frac{1}{2}$. Next, the proposed RCF can be presented as follows:
$p_{j c}\left(u_{j c}\right)=\left(\frac{w_{j c}}{u_{j c}}\right)^{k}=\sqrt{\frac{w_{j c}}{u_{j c}}}, u_{j c}>0$,
where $s_{j}$ is the size of job $J_{j} . e_{j c}$ can be deduced from Eq. (24) as follows:
$e_{j c}\left(u_{j c}\right)=-\frac{1}{2} \sqrt{\frac{w_{j c}}{u_{j c}^{k}}}, u_{j c}>0$

![img-3.jpeg](img-3.jpeg)

Fig. 4. $c E D A_{c 1}$ vs. $c E D A_{c 2}$, the size of jobs obeys $U[1,5]$, the workload obeys $U[1,8]$.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Comparison of improvement of solution and reduction of running time under different number of jobs. The definition of improvement of solutions and reduction of RTs can be found in Eqs. (33) and (34), respectively.

### 5.2. Parameter settings

Unless stated specifically, the default settings of the cEDA approach used in the following experiments are as follows:

1. The population size is set to $N=6 n$.
2. The truncation selection policy is adopted, and the selection ratio is set to $p_{1}$, which means that the best $S\left(S=p_{1} \cdot N\right)$ individuals in the current generation can be selected to learn the parameters of the marginal distribution function. The value of $p_{1}$ can be determined by preliminary experiments in this section.
3. $M=p_{2} \cdot N$. The value of $p_{2}$ can be determined through a preliminary experiment in this section.
4. $L(L=5 \% N)$ individuals can be sampled from the uniform distribution in the solution space.
5. The stopping criterion is set to be the maximum generation. For the configuration of $n$ jobs, the maximum generation is set to 18 n . Meanwhile, when the best individual is not updated in five consecutive generations, the algorithm is terminated early.
In the proposed $c E D A$, except for the parameters determined above, there are two important parameters ( $p_{1}$ and $p_{2}$ ) to be determined: $p_{1}$, which determines the number of better individuals selected from the current population for studying the parameters
of the probability model, and $p_{2}$, which decides the number of the best individuals to reserve for the next generation. A preliminary numerical experiment is conducted to determine the two parameters. $p_{1}$ for testing is from the set $\{0.05,0.10,0.20,0.40\}$, and $p_{2}$ is from the set $\{0.01,0.05,0.10,0.20\}$.

In the preliminary experiments, the number of jobs is set to 20 , the $c E D A$ is performed 5 times, and the amount of resources consumed is recorded each time. After completing the experiments, the average amount of resources consumed is calculated. The computational results are shown in Table 5. The combination $p_{1}=0.20$ and $p_{2}=0.20$ yields the optimal resource consumption.

### 5.3. Comparative approaches

### 5.3.1. Comparison of $c E D A_{c 1}$ and $c E D A_{c 2}$

In this section, two cEDAs that adopt different copula functions ( $C_{1}$ and $C_{2}$ ) are compared. The parameters of $c E D A_{c 2}$ are the same as those of $c E D A_{c 1}$ set forth above. In $c E D A_{c 2}$, the unique parameters $\theta_{a}$ and $\theta_{b}$ are equal to 1 and 1.05 , respectively. In each execution of $c E D A_{c 1}$ and $c E D A_{c 2}$, the solution and the running time obtained are recorded. In order to speed up all the algorithms involved in this paper under the configuration of 200 jobs, the following rule is implemented. When the best individual is not updated in three consecutive generations, the algorithm is terminated.

The meaning of columns in Tables 6 to 10 can be described as follows. Columns 1, 2 and 3 represent the size of the jobs, the workload of the jobs and the deadline, respectively. Columns 4 to 7 are the statistics of the amount of resources consumed in the ten runs of $c E D A_{c 1}$, which are mean, SD, best and worst values. Columns 9 to 12 report the average, SD, best value and worst value of the amount of resource consumed among the 10 runs of $c E D A_{c 2}$, respectively. Columns 8 and 13 report the running time (RT, s) of two approaches. Column 14 reports the degree of improvement (as shown in Eq. (26)) of $c E D A_{c 1}$ compared to $c E D A_{c 2}$ in terms of solution quality. And Column 15 in Table 10 represents the average reduction (as shown in Eq. (27)) obtained by using $c E D A_{c 1}$ compared to $c E D A_{c 2}$ in terms of RT.

The comparison results in Tables 6 to 9 illustrate that the $c E D A_{c 1}$ is better than $c E D A_{c 2}$ for the problem in small-scale and mediumscale instances. Compared to $c E D A_{c 2}$ in terms of solution quality, the degree of improvement of $c E D A_{c 1}$ is $74.90 \%$ for 10 jobs, $84.32 \%$ for 20 jobs, $83.25 \%$ for 50 jobs and $89.48 \%$ for 100 jobs. In largescale instances ( 200 jobs), $c E D A_{c 1}$ can obtain satisfactory solutions at the cost of $16 \%$ of the time, compared to $c E D A_{c 2}$. The reason

Table 5
Results of the preliminary experiments.
Table 6
Performance comparisons between $c E D A_{11}$ and $c E D A_{12}$ for 10 jobs.

Table 7
Performance comparisons between $c E D A_{11}$ and $c E D A_{12}$ for 20 jobs.

Table 8
Performance comparisons between $c E D A_{c 1}$ and $c E D A_{c 2}$ for 50 jobs.

Table 9
Performance comparisons between $c E D A_{c 1}$ and $c E D A_{c 2}$ for 100 jobs.

maybe that the conciseness of copula function in $c E D A_{c 1}$ make it run fast. And this ability make it more suitable for large-scale timesensitive instances.

Improvement $=\frac{\text { Average }\left(c E D A_{c 2}\right)-\text { Average }\left(c E D A_{c 1}\right)}{\text { Average }\left(c E D A_{c 2}\right)} \cdot 100 \%$
Reduction $=\frac{R T\left(c E D A_{c 2}\right)-R T\left(c E D A_{c 1}\right)}{R T\left(c E D A_{c 2}\right)} \cdot 100 \%$
To further study the effectiveness of different copula functions in the $c E D A$, a computational experiment and comparison are conducted using $c E D A_{c 1}$ and $c E D A_{c 2}$. In this experiment, the size of the jobs follows a uniform distribution $U[1,5]$; the workload of
the jobs follows a uniform distribution $U[1,8]$; and the deadline is equal to 2 times the number of jobs. $c E D A_{c 1}$ and $c E D A_{c 2}$ are performed 30 times each for the same instances. The stopping criterion of two cEDAs is only the maximum generation. Fig. 4 shows the results of the comparative experiment in terms of solution quality. The average, best and worst values as well as the SD obtained by $c E D A_{c 1}$ are all better than those obtained by $c E D A_{c 2}$ in small-scale instances. However, in small-scale instances, the running time of the two cEDAs is not much different. Those results indicate that Clayton copula function $C_{1}$ in $c E D A_{c 1}$ fits the correlation better than Clayton copula function $C_{2}$ in $c E D A_{c 2}$ in small-scale instances.

Table 10
Performance comparisons between $c E D A_{c 1}$ and $c E D A_{c 2}$ for 200 jobs.

Table 11
Performance comparisons between the cEDA and GA for 10 jobs.

# 5.3.2. Comparison of the cEDA and GA 

In this section, a comparison between the GA proposed by Caraffa et al. [71] and cEDA is conducted. The parameters of the GA (except for the selection operator) are introduced in Caraffa et al. [71]. The proposed selection operator in our experiment is tournament selection. In addition, the number of individuals in the population and the stopping criterion are the same as for the cEDA.

Tables 11 to 15 show the experimental results obtained by the cEDA and GA for these instances in the case of $10,20,50$, 100 and 200 jobs, respectively. Columns 4, 5, 6, 7 and 8 report the average, standard deviation (SD), best and worst value of the amount of resource consumed, and running time (RT) among the 10 runs of the cEDA, respectively. Columns 9, 10, 11, 12 and 13
report the average, SD, and best value and worst value of the amount of resource consumed, and RT among the 10 runs of the GA, respectively. Column 14 reports the average improvement (as shown in Eq. (28)) obtained by using the cEDA compared to the GA in terms of solution quality. In Table 15, the meaning of the first 14 columns is in accordance with Table 14. And Column 15 in Table 15 represents the average reduction (as shown in Eq. (29)) obtained by using cEDA compared to GA in terms of RT.
Improvement $=\frac{\text { Average }(\mathrm{GA})-\text { Average }(\mathrm{cEDA})}{\text { Average }(\mathrm{GA})} \cdot 100 \%$
Reduction $=\frac{R T(G A)-R T(c E D A)}{R T(G A)} \cdot 100 \%$

Table 12
Performance comparisons between the cEDA and GA for 20 jobs.

Table 13
Performance comparisons between the cEDA and GA for 50 jobs.

As shown in Tables 11 to 15, the solutions obtained by the cEDA are generally better than those obtained by the GA in terms of solutions quality. In addition, compared to GA, cEDA has prominent advantages on small-scale and medium-scale instances. And on large-scale instances, cEDA can obtain satisfactory solutions in much less time, compared to GA. The reason is that there are very time consuming crossover and mutation operators in GA.

### 5.3.3. Comparison of cEDA and PSO

The proposed cEDA is compared to PSO in this section. The parameters of the PSO algorithm are adopted from Muthuswamy
et al. [9]. PSO algorithm is a swarm intelligent search algorithm, in which the individuals are referred to as particles. The velocity-updating approach for the particles can be described as follows:

$$
\begin{aligned}
& v_{p i}(t+1)=w(t) \cdot v_{p i}(t)+c_{1} r_{1} \\
& \quad\left(\text { LBest }_{p i}-u_{p i}(t)\right)+c_{2} r_{2} \cdot\left(\text { GBest }-u_{p i}(t)\right),
\end{aligned}
$$

where $r_{1}$ and $r_{2}$ follows a uniform distribution $U(0,1)$ and, $w(t)$, $c_{1}$ and $c_{2}$ are parameters in the PSO approach. And $w(t)$ is updated using $w(t+1)=\alpha \cdot w(t)$, where $\alpha$ is the decrement factor. In this comparison of experiments, parameter $w$ is initially set to 0.9 and, $c_{1}$ and $c_{2}$ are equal to 1 [9].

Table 14
Performance comparisons between the cEDA and GA for 100 jobs.

Table 15
Performance comparisons between the cEDA and GA for 200 jobs.

Tables 16 to 20 provide the experimental results obtained by the cEDA and PSO for these instances in the case of $10,20,50$, 100 and 200 jobs, respectively. Column 14 reports the average improvement (as shown in Eq. (31)) obtained using the cEDA compared to the PSO in terms of solution quality. And Column 15 in Table 20 represents the average reduction (as shown in Eq. (32)) obtained by using cEDA compared to PSO in terms of RT.

Improvement $=\frac{\text { Average }(\text { PSO })-\text { Average }(\text { cEDA })}{A \text { verage }(\text { PSO })} \cdot 100 \%$
Reduction $=\frac{R T(P S O)-R T(C E D A)}{R T(P S O)} \cdot 100 \%$

Tables 16 to 19 show that the solutions obtained by the cEDA are better than those obtained by PSO in small-scale and medium-scale instances. However, the running time of cEDA is more than PSO in small-scale and medium-scale instances. In large-scale instances, cEDA can obtain the solutions which are only $1.28 \%$ less than the quality of solutions obtained by PSO in only half the time.

### 5.3.4. Comparison of cEDA and MIMIC $_{c}$

The proposed cEDA is compared to the MIMIC $_{c}$ algorithm in this section. The MIMIC $_{c}$ algorithm proposed by Larraanaga and Lozano [57] can address the continuous optimization problem. The parameters of the MIMIC $_{c}$ algorithm are identical to the proposed cEDA.

Table 16
Performance comparisons between the cEDA and PSO for 10 jobs.

Table 17
Performance comparisons between the cEDA and PSO for 20 jobs.

Tables 21 to 25 provide the experimental results obtained by the cEDA and MIMIC ${ }_{c}$ for these instances in the case of 10, 20, 50, 100 and 200 jobs, respectively. Column 14 reports the average improvement (as shown in Eq. (33)) obtained using the cEDA compared to the MIMIC ${ }_{c}$ in terms of solution quality. And Column 15 in Table 25 represents the average reduction (as shown in Eq. (34)) obtained by using cEDA compared to MIMIC ${ }_{c}$ in terms of RT.
$\begin{aligned} & \text { Improvement }=\frac{\text { Average }(\text { MIMIC }_{c})-\text { Average }(\text { cEDA })}{\text { Average }(\text { MIMIC }_{c})} \cdot 100 \% \\ & \text { Reduction }=\frac{R T\left(\text { MIMIC }_{c}\right)-R T(c E D A)}{R T\left(\text { MIMIC }_{c}\right)} \cdot 100 \%\end{aligned}$
As can be observed from Table 21, the solutions obtained by the cEDA are better than those obtained by MIMIC ${ }_{c}$ in all of 24 instances for 10 jobs instance. Specifically, the degree of improvement of cEDA, compared to MIMIC ${ }_{c}$ in terms of solution quality, is an average of $33.36 \%$ in much less running time. In addition, the SD values of the solutions produced by the cEDA are smaller in 20 of the 24 configurations when compared to MIMIC ${ }_{c}$. Table 22 presents that the solutions obtained by the cEDA are better than those obtained by the MIMIC ${ }_{c}$ in 23 of the 24 configurations for 20 jobs instance. Compared to MIMIC ${ }_{c}$, cEDA achieves a $15.89 \%$ average improvement rate in terms of solution quality, and cEDA takes only about half the running time of MIMIC ${ }_{c}$. In addition, the SD values of the solutions produced by the cEDA are smaller in

Table 18
Performance comparisons between the cEDA and PSO for 50 jobs.

Table 19
Performance comparisons between the cEDA and PSO for 100 jobs.

19 of the 24 configurations when compared to MIMIC $_{C}$. Table 23 shows that the solutions obtained by the cEDA are better than those obtained by the MIMIC $_{C}$ in 17 of the 24 configurations for 50 jobs instance. Compared to MIMIC $_{C}$, cEDA achieves a $1.31 \%$ average improvement rate in terms of solution quality, and the average running time of cEDA is reduced by $57.75 \%$. As can be observed from Table 24, there is no significant difference between cEDA and MIMIC $_{C}$ in terms of solutions' quality. On the quality of solutions, MIMIC $_{C}$ is only $0.8 \%$ better than cEDA. However, compared with MIMIC $_{C}$, the proposed cEDA approach reduces the running time by $47.95 \%$.

From Tables 21 to 25, it can be concluded that the proposed cEDA approach outperforms MIMIC $_{C}$ in small-scale instances in terms of quality of solutions and running time. And in mediumscale and large-scale instances, the proposed cEDA approach can obtain the solutions, which are very close to the solutions produced by MIMIC $_{C}$, in much less time. In other words, the proposed cEDA approach can reduce greatly the running time, at the expense of a little bit of the quality of solutions.

Fig. 5 illustrates that with the number of jobs increasing, the reduction of RT generally becomes larger. Meanwhile, the quality of solutions cEDA obtained is still very close to MIMIC $_{C}$.

Table 20
Performance comparisons between the cEDA and PSO for 200 jobs.

Table 21
Performance comparisons between the cEDA and MIMIC, for 10 jobs.

The benchmarks of well-known shop scheduling problems in Taillard [72] are all combinatorial optimization problems. For demonstrating the effectiveness of cEDA in well-known problems, the cEDA is tested in three benchmark optimization functions, such as Sphere function $\left(f_{1}\right)$, Ackley function $\left(f_{2}\right)$, etc. And the dimensions of all three functions are set to 10,20 and 30 in this experiment. The definition of the three functions are given in Eq.(35). The experimental results are in Table 26. And the results show that the cEDA outperforms MIMIC ${ }_{c}$. The running time of cEDA can be gret if compared to $M I M I C_{c}$. This result is consistent with the experimental result in this paper. The reduction in the running
time of cEDA can be attributed to its simple structure.
$f_{1}(\mathbf{x})=f_{1}\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\sum_{i=1}^{n} x_{i}^{2}, \quad x_{i} \in[-100,100]$
$f_{2}(\mathbf{x})=f_{2}\left(x_{1}, \ldots, x_{n}\right)=-20 e^{-0.2 \sqrt{\frac{1}{n}} \sum_{i=1}^{n} x_{i}^{2}}-e^{\frac{1}{n} \sum_{i=1}^{n} \cos (2 \pi x_{i})}$
$+20+e, x_{i} \in[-5,5]$
$f_{3}(\mathbf{x})=f_{3}\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\sum_{i=1}^{n}\left[\left(x_{1}-x_{i}^{2}\right)^{2}+\left(x_{i}-1\right)^{2}\right]$,
$x_{i} \in[-10,10]$

Table 22
Performance comparisons between the cEDA and MIMIC, for 20 jobs.

Table 23
Performance comparisons between the cEDA and MIMIC, for 50 jobs.

### 5.4. Analysis of convergence trends

In this section, the convergence profiles of cEDA, GA, PSO and MIMIC, on five different scale instances are given. For all instances, the job size comes from the uniform distribution of intervals [1,5], the workload comes from the uniform distribution of intervals [1,8], and the deadline is equal to 20. As can be seen from Fig. 6, compared with cEDA and MIMIC, GA and PSO converge prematurely especially for small-sized instances. Although both cEDA and MIMIC, can maintain the diversity of the population well, the proposed cEDA approach can greatly reduce the running time as we stated before in Section 5.3.4.

## 6. Conclusion and future work

This paper examines a scheduling problem with a convex RCF. The aim of this paper is to determine an approximate optimal resource allocation vector $\mathcal{R}$ of all jobs with the constraint $C_{\text {max }} \leq$ $D$, to minimize the total amount of resources consumed. A mathematical model is implemented for the problem. To address the problem, a cEDA approach is used, and a new, advanced correction algorithm is proposed to amend the individuals that do not satisfy the deadline constraint.

The cEDA approach is rarely used in flow-shop scheduling problems in the literature even, though it can improve the learning efficiency of the EDA and reduce running time. A computational experiment is performed to study the effectiveness of different

Table 24
Performance comparisons between the cEDA and MIMIC, for 100 jobs.

Table 25
Performance comparisons between the cEDA and MIMIC, for 200 jobs.
Table 26
Performance comparison between the cEDA and MIMIC, for well-known benchmark optimization functions.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Convergence trends of cEDA, GA, PSO and MIMIC, on the five different scale instances. Note that MIMIC, is abbreviated as MIMIC.
copula functions in the cEDA approach. The results illustrate that copula function $C_{1}$, is more effective than copula function $C_{2}$ in small-scale and medium-scale instances in terms of the quality of solutions and running time. To evaluate the performance of the cEDA approach in this problem, the GA, PSO and MIMIC ${ }_{c}$ approaches are adopted for comparison. Computational results demonstrate that the cEDA has a competitive advantage over the GA, PSO and MIMIC, in small-scale instances in terms of the quality of solutions. In medium-scale instances, cEDA still outperforms GA and PSO, but the solution obtained by MIMIC ${ }_{c}$ is very close to cEDA. The competitive advantage of cEDA decreases in largescale instances. And MIMIC ${ }_{c}$ and PSO can even obtain a little better solutions in some large-scale instances. However, the running time of cEDA can be greatly reduced in large-scale instances, compared to GA, PSO and MIMIC ${ }_{c}$. The cEDA can give researchers more choices to balance the quality of solution and the running time in flowshop scheduling problems.

The literature has rarely addressed flow-shop scheduling problems in which the resource consumption is the objective and the deadline is the constraint. However, the meaning of this type of problem is of great significance. The research of this problem can help to reduce resource costs (such as fossil fuel costs, financial outlays and manpower costs) of production and improve the efficiency of resource consumption. Considering the fact that few studies treat resource consumption as the objective in the flow shop scheduling problems, this research may fill this gap in the literature.

The cEDA approach proposed for the problem in this work can be extended to other flow-shop scheduling problems considering resource consumption. One possible direction for future study is to adapt cEDA to flow-shop scheduling problems with more than two machines, and the constraint of dynamic job arrival. Both problem settings are derived from reality and the complexity of the problem is greatly increased. Furthermore, it is necessary to find a copula function suitable for the problem characteristics, so as to achieve an expected performance.

## Acknowledgment

The authors are very grateful to the Editor-in-Chief and the anonymous reviewers for their constructive comments and suggestions that have further helped to improve the quality and presentation of this paper. This research was supported by the National Natural Science Foundation of China grant number 71671168 and the Fundamental Research Funds for the Central Universities of China grant number 2013B18020204.
