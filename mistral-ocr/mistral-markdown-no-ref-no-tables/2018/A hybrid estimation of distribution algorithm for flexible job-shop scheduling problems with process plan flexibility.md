# A hybrid estimation of distribution algorithm for flexible job-shop scheduling problems with process plan flexibility 

Ricardo Pérez-Rodríguez ${ }^{1} \cdot$ Arturo Hernández-Aguirre ${ }^{2}$

(C) Springer Science+Business Media, LLC, part of Springer Nature 2018


#### Abstract

The flexible job-shop environments have become increasingly significant because of rapid improvements on shop floors such as production technologies, manufacturing processes and systems. Several real manufacturing and service companies have had to use alternative machines or processes for each operation and the availability of alternative process plans for each job in order to achieve good performance on the shop floor where conflicting objectives are common, e.g. the overall completion time for all jobs and the workload of the most loaded machine. In this paper, we propose a Pareto approach based on the hybridization of an estimation of distribution algorithm and the Mallows distribution in order to build better sequences for flexible job-shop scheduling problems with process plan flexibility and to solve conflicting objectives. This hybrid approach exploits the Pareto-front information used as an input parameter in the Mallows distribution. Various instances and numerical experiments are presented to illustrate that shop floor performance can be noticeably improved using the proposed approach. In addition, statistical tests are executed to validate this novel research.


Keywords Multiobjective optimization $\cdot$ Evolutionary optimization $\cdot$ Estimation of distribution algorithm $\cdot$ Flexible job-shop scheduling $\cdot$ Mallows distribution $\cdot$ Routing flexibility $\cdot$ Process plan flexibility

## 1 Introduction

The flexible job-shop scheduling problem (FJSP) is commonly defined as follows: there are $n$ jobs $J=$ $\left\{J_{1} J_{2}, \ldots, J_{n}\right\}$ to be processed on $m$ machines $M=$ $\left\{M_{1} M_{2}, \ldots, M_{m}\right\}$. A job $J_{i}$ is formed by a sequence of $n_{i}$ operations $\left\{O_{i, 1} ; O_{i, 2} ; \ldots ; O_{i, n_{i}}\right\}$ performed one after another according to a given sequence. The execution of $O_{i, j}$ requires one machine out of a set of $m_{i, j}$ given machines $M_{i, j} \subseteq M$. Preemption is not allowed, i.e., every operation must be completed without interruption once it starts. For each job, the corresponding operations have to be processed in the given order, that is, the starting

[^0]time for an operation must not be earlier than the point at which the preceding operation is completed. This constraint is imposed simultaneously on all appropriate pairs of operations. The most common objective is to minimize the overall completion time for all the jobs. The FJSP assumes only one feasible process plan for each job. Although it is common in real-world manufacturing and service environments, a wider space for choices exists. Normally, there is more than one option to construct schedules among alternative machines in which to perform an operation and from alternative process plans of a job, i.e. routing flexibility and process plan flexibility respectively. In order to make the flexible jobshop scheduling problem more understandable, there is an example of the inner ring grinding process plan for a spherical roller bearing, whose process plan flexibility is typical in the bearing manufacture industry. The process plan is detailed below and involves eleven operations. It does not matter if the second operation is processed after the third, so the processing sequence can be rearranged. The eighth and ninth operations have the same situation. In addition, the sixth operation can be placed in any position between the fifth and the eleventh operation. In this example, we have three alternative process plans for an inner ring.


[^0]:    $\boxtimes$ Ricardo Pérez-Rodríguez ricardo.perez@cimat.mx

    Arturo Hernández-Aguirre artha@cimat.mx

    1 CONACYT - CIMAT A.C., Bartolomé de las Casas 314, Barrio la Estación, 20259, Aguascalientes, Ags, México
    2 CIMAT A.C., Jalisco s/n, Valenciana, 36240, Guanajuato, Gto, México

![img-0.jpeg](img-0.jpeg)

## Outside Surface Rough Grinding

Fig. 1 A graphical description of a process plan flexibility
Figure 1 illustrates a graphical description for the second operation and the third operation. Both operations can be rearranged without affecting the overall process.

Operation number
1
2
3
4
5
6
7
8
9
10
11

Operation name
ring face grinding
outside surface rough grinding
inside surface rough grinding
raceway rough grinding
temper treatment
chamfer brightening
outside surface fine grinding
inside surface fine grinding
raceway fine grinding
rib grinding
surface brightening

The FJSP incorporates the routing flexibility component. However the FJSP with process plan flexibility (FJSPPPF) is a more complicated combinatorial optimization problem Özgüven, Özbakır, and Yavuz [40]. The FJSP-PPF considers multiple process plans for the jobs by excluding the assumption of only one feasible process plan for each job. The FJSP-PPF consists of a set of $n$ jobs, each having a set of $P$ process plans. The process plan $p_{k}$ of job $j\left(p_{k j}\right)$ is an ordered list of $n_{i}$ operations. It is assumed that the process plans are known in advance. The execution of the operation $i$ of job $j$ in the process plan $p_{k j}\left(O_{i, j, p_{k j}}\right)$ requires one machine out of a set of $m_{i, j}$ given machines $M_{i, j} \subseteq M$. Only one of the alternative plans is adopted for each job. The FJSP-PPF not only deals with routing and sequencing sub-problems but also the process plan selection sub-problem: choosing a process plan for each
![img-1.jpeg](img-1.jpeg)

## Inside Surface Rough Grinding

job $j$ from a given set of $P_{j}$ process plans, assigning each operation $\left(O_{i, j, p_{k j}}\right)$ to a machine selected from the set $M_{i, j}$ and ordering operations in the machines so that conflicting objectives are optimized such as the overall completion time for all the jobs and the maximum working time spent on any machine.

A complete formulation of the mathematical integer linear programming model for the FJSP-PFF was developed by Özgüven et al. [40]. Figure 2 shows a scheduling example with four jobs $J=\left\{J_{1}, J_{2}, J_{3}, J_{4}\right\}$. Each job $J_{i}$ is formed by a sequence of three operations $\left\{O_{i, 1} ; O_{i, 2} ; O_{i, 3}\right\}$ performed one after the other. Table 1 details the alternative machines for each operation with two different process plans. The scheduling scheme, shown in Fig. 2, satisfies the set of constraints for the traditional FJSP-PPF, i.e., it ensures that all the operations are assigned to a single machine. Furthermore, it takes care of the requirement that the operations must respect precedence, i.e., the precedence relationships between the operations of a job are not violated. In addition, the solution depicted in Fig. 2 guarantees that multiple operations cannot be executed at the same time on any possible machine. Finally, the schedule determines the completion times (of the final operations) of the jobs, the makespan, and determines the maximal workload. Additionally, Fig. 2 presents the alternative process plan B for the aforementioned program. Based on Fig. 2, the performance is improved using the second process plan, and choosing alternative machines.

Any solution to the FJSP-PPF should be a combination of process plan selection, operation scheduling decision, and machine assignment. Thus, the selection of a process plan for each job, the processing sequence of operations on the

Fig. 2 Illustration of a schedule for the FJSP-PPF

Process Plan A
![img-2.jpeg](img-2.jpeg)

Processo Plan B ( $\dagger$ )
![img-3.jpeg](img-3.jpeg)
machines and the assignment of operations on machines should express a solution. The processing sequence of operations in the machines can be constructed using a permutation-based representation. In this context, an operation sequence vector is a permutation for the FJSPPPF and a set of permutations is a set of operation sequence vectors. In this research, we intend to characterize the space of possible solutions explicitly, i.e., to characterize a feasible subset of permutations by listing them based on the constraints of the problem. The proposal is to use a probability distribution associated with the space of possible solutions. An example is shown in Fig. 3 in order to understand how a probability distribution is sensitive to solutions. Different possible solutions are provided at the beginning of Fig. 3, i.e., different feasible permutations are used as an input parameter in order to build probability distributions. Each position, i.e., each column from the set of permutations is considered as an independent variable X. Based on Fig. 3, we have five independent variables, i.e., five positions (or columns) X1, X2, and so on. Therefore, we can build five probability distributions using the set of permutations in Fig. 3. After that, we select a subset of permutations, the best hypothetical solutions, and build the corresponding updated probability distributions. These are shown at the lower part of Fig. 3. The updated probability distributions are different from the previous probability distributions because they are sensitive to solutions used in the example.

In order to obtain an explicit probability distribution over the FJSP-PPF, we use an Estimation of Distribution Algorithm (EDA). The EDA is another paradigm in the field of evolutionary computation. Introduced by Mühlenbein and $\operatorname{Paa} \beta$ [39] and compared to other evolutionary algorithms, the EDA reproduces a new population implicitly instead of using traditional evolutionary operators. To create an EDA, a probability model of the most promising area is generated by statistical information based on the search experience, and then the probability model is used for sampling to generate new individuals. The EDA makes use of the probability model to describe the distribution of the solution space while the updating process reflects the evolutionary trend of the population. To describe the distribution of the solution space mentioned above, the EDA tries to determine the relationship or interaction between the variables of the problem. However, how can we improve the estimation of the relationships between the variables of the problem? How influential is the estimation mentioned in the performance of the algorithm? We use the Mallows distribution in this research to obtain a better estimate of the relationships between the variables. The Mallows model was initially proposed by Mallows [35] and later was improved by Fligner and Verducci [18] through the generalized Mallows distribution (GMD). A more extensive explanation of the GMD characteristics is found in Fligner and Verducci [18] and Fligner and Verducci [19]. More recently, Ceberio et al. [8] contributed to an

Table 1 An FJSP-PPF example
initial application of the GMD to solve the flow-shop scheduling problem (FSP) coupled with an EDA.

The GMD is a popular exponential model on the rankings [37]. Based on Fligner and Verducci [19], the GMD is suitable when there is a need to rank a fixed set of $k$ items according to some judgment. The process of ranking the items is decomposed into $k-1$ stages, i.e., $k-1$ positions (or columns) as shown in Fig. 3. The general problem is to characterize the population based on a random sample of rankings. Historically, models for random rankings emerged from the literature on paired comparisons, where the probability that one item is being preferred to another is as specified by a given model. Fligner and Verducci [19]. A basic model can be built to rank the items, i.e., the most preferred item is selected in the first stage, the best of the remaining items is selected in the second stage, and so on until the least preferred item is
selected by default. In this research the items mentioned above are operations to sequence in machines. Whatever the nature of these operations, each processing sequence of operations in the machines produces a ranking. Previous research uses probability models for adoption at each stage, and the properties of the resulting models for randomly sampled rankings have been investigated for years. Some probability models assume that each item $i$ is thought to have an intrinsic value $\theta_{i}$, and the probability of choosing a particular item $i$ at any stage, depends on the set of items not previously chosen. Other models add interaction terms that theoretically extend the usefulness of previous approach when the basic model does not adequately describe the data. The major difficulty with these formulations is the analytic intractability of the models [19], especially when the number $k$ of items under consideration is more than a few. The GMD avoids the analytical difficulties by assuming that the accuracy of the choice made at any stage is independent of the accuracies in the other stages. The accuracy is assessed with respect to a central ranking that indicates the general consensus, obtained from the population of vectors with respect to the ordering of the items, i.e., operations to sequence in machines for the FJSP-PPF. Given a set of rankings (permutations), over $n$ items (operations), the central ranking (central permutation) is the ranking that minimizes the total number of disagreements with rankings contained in the set of rankings [2]. Various measures of agreement have been proposed such as Kendall's metric [18]. The Kendall's metric has been the measure of choice in many recent applications centered on the analysis of ranked data [13]. In the GMD such as Mallows model, the probability of observing any ranking $\pi$ decreases as the distance (Kendall-tau metric) between $\pi$ and the central ranking increases. Finding the central ranking is unfortunately a computational challenge, since the problem is NP-hard even for only four items [5, 13]. Since the problem is important across a variety of fields, many researchers across these fields have converged on finding good and practical algorithms for its solution [2]. Once a central ranking has been determined, the GMD creates a multistage model that is parameterized by the probabilities of the different degrees of accuracy in each stage.

Although the EDA was originally designed to solve integer or real-valued domain problems, it cannot produce a feasible solution from a probability model built on a permutation-based representation [29]. Furthermore, the EDA requires being adapted to deal with permutationbased problems by means of a modification in the algorithm process. Then, the implementation of a specific probability model for this issue would be more competitive against other models. The Mallows model [35] is a distance-based exponential probabilistic model considered analogous to the Gaussian probability distribution over the space of

Solution vectors (permutations)
![img-4.jpeg](img-4.jpeg)

Fig. 3 An example of a probability distribution associated with the space of possible solutions
permutations. In the Mallows distribution, the probability value of each permutation $\sigma \in T_{n}$ (where $T_{n}$ stands for the set of $n$ ! permutations of $n$ items) depends on just two parameters: a spread parameter $\theta$ and the distance to a central permutation $\sigma_{0}$. This model assigns to each permutation $\sigma$ a probability that decays exponentially with respect to its distance to the central permutation $\sigma_{0}$. In this way, $P(\sigma)$ can be considered as an exponential non-uniform distance-based ranking model [8]. Both parameters, i.e., the spread parameter $\theta$ and the central permutation $\sigma_{0}$, are estimated. Therefore, different estimates of the parameters mentioned should be considered in order to get a better performance to solve combinatorial optimization problems such as FJSP-PPF.

Contrary to current research where diverse techniques and approaches have been proposed in order to solve the problem that is being examined, this paper contributes to the state of the art as follows:

- To introduce the GMD, detailed in Fligner and Verducci's [18] research, for the FJSP-PPF as a way of estimating an explicit probability distribution in the domain of permutations for any EDA.
- To apply the GMD coupled with an EDA, called MEDA (Mallows Estimation of Distribution Algorithm), for solving the FJSP-PPF on a multi-objective perspective.
- To propose a different way of improving the estimation of the central permutation $\sigma_{0}$ in the GMD process using

a Pareto-front approach to help the MEDA to find better solutions for the FJSP-PPF.

- The purpose of this research is to propose a different experimental technique to enhance the performance of the algorithm mentioned above for solving the FJSPPPF using a Pareto-front approach.

The proposed algorithm has a wide range of applications for automotive, aerospace, chemical, metallurgical, pharmaceutical, and food industries among others. The users of this contribution are academics, engineers, managers and practitioners related to the scheduling of manufacturing operations.

The remainder of this paper is organized as follows: in Section 2, the related work is depicted. In Section 3, the proposed MEDA is detailed. In Section 4, computational results and comparison with other multiobjective and recent algorithms are presented. The concluding remarks are made in Section 5.

## 2 Related work

### 2.1 Mathematical programming

Özgüven et al. [40] detail the mathematical models for jobshop scheduling problems with routing and process plan flexibility. These are mixed-integer linear programming models. Fattahi et al. [16] compared the first model with the randomly generated test problems. The instances mentioned divides into two categories: small and medium size. The results achieved in the same test problems indicate that the overall performance of the Özgüven et al. model is superior to that of the Fattahi et al. model. For small size instances the makespan and the overall completion time for all the jobs, obtained by the Özgüven et al. model and Fattahi et al. model overlap, and both models find optimal solutions. However, a significant difference occurs between the two models for medium-large size problems. Although the Özgüven et al. model significantly dominates the Fattahi et al. model in terms of the makespan results, it cannot find optimal solutions for medium-large size instances. The Özgüven et al. model is extended to enable it to handle the process plan flexibility component. According to the research of Özgüven et al. [40], there is no comparable mathematical model in the literature. Therefore, the outcome is a second model that was presented with computational results on hypothetically generated test problems. The second model finds the optimal solutions for a few small size problems. For the remaining ones, as the size of the problem increases, the gap between the best linear solution, in terms of the makespan results, and the best integer solution widens. Also, Özgüven et al. [41] explains an advanced form of the FJSP-PPF that
considers separable and non-separable sequence dependent setup times using two mixed-integer goal programming models. In the first model, the sequence dependent setup times are non-separable and in the second model the sequence dependent setup times are separable. In addition, minimizing the makespan is the primary goal while balancing the workloads of the machines is the secondary goal for both models. In Özgüven et al.'s [41] research about the literature for the mathematical modeling approaches, all except one of the models they came across have different variations of the scheduling problems either with routing or with process plan flexibility, but not both. The only exception is the model of Lee et al. [31]. Since Özgüven et al. [41] came across no test problem that addresses the models developed in their paper the computational results are obtained on small size instances. Although the models do not find optimal solutions based on the results, the authors analyze the significance of the differences between the effects of non-separable and separable setup times on the performance of scheduling system. The results denote that there is a significant difference between the performance values of the problems with non-separable and separable setup times. Although the models mentioned above require assumptions to satisfy from an industrial perspective, these are used to continue research on the problem.

### 2.2 Evolutionary algorithms

Lee et al. [31] proposed a genetic algorithm-based heuristic approach for scheduling in a manufacturing supply chain. The approach considers industrial real features, such as outsourcing, customer due dates and alternative process plans for job types. The objective is to minimize the makespan for the due date of each order. The authors focused on the finite capacity and resource capacity of a flow shop and studied the strength of integrated process, planning, and scheduling, with specific due dates for orders. In numerical experiments, the GA-based approach efficiently solved the problem and produced the best process plans (operation sequence and machine selection with outsourcing) and schedules for all the orders in order to minimize the makespan. The mentioned experiments were tested on small instances, ranging from one or two customers, less than ten jobs and machines. In addition, the experiments were tested on the data from Sundaram and Fu [49] with only five jobs and five machines. There is no information on experiments with large size problems.

There are other papers that considered the process plan flexibility concept using evolutionary algorithms such as the Kim et al. [28] research. The authors presented an artificially intelligent search technique, called symbiotic evolutionary algorithm to address the integrated problem of process planning and scheduling in job-shop flexible

manufacturing systems where it is possible to generate many feasible process plans for each job. This approach is characterized by its ability to perform the effective and simultaneous search of the solution space formed by the two problems and then the scheduling problem is considered under the constraint of the solution. For the process planning problem, minimizing the absolute deviation of machine loads is used as an objective in this paper. That is, minimize $\sum_{i}\left|w_{i}-\bar{w}\right|$, where $w_{i}$ is the load of machine $i$ and $\bar{w}$ is the mean of machine loads. The scheduling objectives of both minimizing the makespan and minimizing mean flow time involve the maximum utilization of the machines. The performance of the proposed algorithm was compared with those of a traditional hierarchical approach and an existing cooperative coevolutionary algorithm. Twenty-four test problems were constructed by the authors. The test problems range between 6 and 18 jobs. The number of operations, corresponding to the jobs, ranges between 8 and 22 . The experimental results show that the proposed algorithm outperforms the compared algorithms. Although there is no information about the optimal solutions with respect to the test problems used in the comparison, the main contribution of the authors is to adopt the strategies of localized interactions, steady-state reproduction, and random symbiotic partner selection to improve the algorithm, i.e., to enhance population diversity and search efficiency.

Park and Choi [43] also focused on the integration problem of process planning and scheduling in a job-shop environment. In their research, a GA-based scheduling method was considered to minimize the makespan of all of the jobs in the integration problem with alternative machines and alternative operations sequences. In order to evaluate the performance of the suggested GA, the authors used an instance of an injection molding company with multiple process plans. Through this real case, the authors compared two kinds of scheduling results, that is, the integrated scheduling considering the alternative machines and operations sequences and the traditional scheduling considering them sequentially. Based on the results, the integrated scheduling reduces the makespan for the real case. In addition, a couple of benchmark cases were tested for performance evaluation. The first benchmark case was based on Chambers and Barnes [9] using the Fisher and Thompson [17] 10x10 instance for making an alternative machine problem. The criterion is the sum of processing times required for each machine. The second benchmark case was based on Tan [50]. The instance mentioned has five jobs with twenty operations. In this problem, most jobs and operations have more than four operations sequences and alternative machines. Additionally, each job has a different release time. For both cases, the integrated scheduling reduces the makespan. A good contribution of the authors is
the chromosome representation. It can maintain feasibility after a genetic operator and easily handle the integration problem. Although there is no information about the optimal solutions with respect to the test problems used in the comparison, Park and Choi's [43] research is another example of implementing evolutionary algorithms in real manufacturing processes.

Rossi and Dini [46] proposed an ant colony optimizationbased software system for solving flexible manufacturing systems scheduling in a job-shop environment with routing flexibility, sequence-dependent setup and transportation time. The algorithm was tested using standard benchmarks and problems instances belong to the following datasets: Fisher and Thompson [17] instances, Lawrence [30] instances, and Applegate and Cook [3] instances. The effectiveness of the proposed system was verified by comparison with alternative approaches such as ant colony algorithm, genetic algorithm, and local search algorithm. Based on the results, the ant colony approach proposed outperforms the others with respect to the average makespan. Also, the approach mentioned outperforms the others with respect to the mean relative error between the average makespan and the optimal solution. The key point of their research is to use an effective pheromone trail coding and tailored ant colony operators for improving solution quality. In addition, the flexible manufacturing system (FMS) layout is being considered in this research.

### 2.3 The multi-objective approach

Gao et al. [20] addressed the FJSP with three objectives: the makespan, the maximal machine workload i.e., the maximum working time spent in any machine and the total workload, which represents the total working time assigned to all machines. A hybrid GA with variable neighborhood descent (VND) is detailed in their research. Several sets of problem instances were considered for the computational study of the experiment. One of the sets is from Fisher and Thompson [17], and another set is from Lawrence [30]. Almost $50 \%$ of the instances, 87 out of 181 of the proposed hybrid GA outperforms others with respect to optimal solutions. Although the Gao et al. [20] research contributes to the use of an advanced crossover and mutation operators to adapt to the special chromosome structure and the characteristics of the problem, the hybrid approach was not implemented in the industrial environments.

Huang et al. [23] presented a multi-objective particle swarm optimization integrating with variable neighborhood search for the FJSP to optimize three objectives, i.e., the makespan, the total workload and the critical machine workload. Four Kacem et al. [26] instances, ranging from 4 jobs x 5 machines to 15 jobs x 10 machines and ten Brandimarte [7] instances, ranging from 10 jobs x

6 machines to 20 jobs $\times 15$ machines were used to evaluate the performance of their algorithm and several published algorithms were applied in comparison with the proposed algorithm. Based on the results reported, the proposed algorithm obtains more high-quality solutions for the instances mentioned. Their contribution is to use cognitive memory and social memory strategies to update and preserve the non-dominated individuals. The industrial perspective with the process plan flexibility was not considered in this research.

Dauod et al. [14] contributed to a GA-based approach to an order-scheduling problem in a mail-order pharmacy automation system. The objectives were to minimize the makespan and the collation delays, i.e., the completion time difference between the first and the last medications within the same order was defined as the order collation delay. The objective of this analysis is to understand how machine flexibility and multi-medication orders proportion affect the system performance, mainly in terms of collation delays. Therefore, the authors built three scenarios to compare the GA proposed with the CPLEX tool optimization software and two industry heuristics: the longest processing time (LPT) and the least total workload (LTW). However, no standard instances were used in the comparison and no similar algorithms were considered in this research.

### 2.4 The Pareto approach

New research is considering the use of the Pareto approach for scheduling problems. Pareto is hybridized with other evolutionary algorithms. Kacem et al. [26] show a Pareto approach based on the hybridization of fuzzy logic (FL) and an evolutionary algorithm (EA) to solve the FJSP. The objective is to minimize the makespan, the total workload of machines and the workload of the most loaded machine. In the research, many examples are presented to illustrate some theoretical considerations and to show the efficiency of the suggested methodology. The authors use numerous instances that have been simulated to test the efficiency of the suggested approach. In addition, the authors present the lower-bound values to give a precise evaluation of the solution quality. However, no algorithms have been used for a comparison with respect to the simulated instances. The hybridization proposed by Kacem et al. [26] exploits the knowledge representation capabilities of FL and the adaptive capabilities of EA. The industrial perspective is out of scope for this research.

Yue et al. [56] proposed the hybridization Pareto approach with an artificial bee colony algorithm for a single machinescheduling problem with sequence-dependent setup times. The aim is to minimize the makespan and the total weighted tardiness simultaneously. The authors illustrate computational experiments and results over five different
categories of problems. All test problems consider setup times and due dates for each job. These test problems are much closer to real-world problems. The authors make comparisons of results among three famous multiobjective optimization algorithms, i.e., the non-dominated sorting genetic algorithm II (NSGAII) Deb et al. [15], the improved strength Pareto evolutionary algorithm (SPEA2) Zitzler et al. [57] and particle swarm optimization algorithm (PSO) Kennedy and Eberhart [27]. The performance of the proposed algorithm is based on different metrics including diversity and quality of solutions, inverted generational difference and spacing of Pareto points on the Pareto fronts. The hybridization approach gives better results and number of Pareto points as compared to the other algorithms for medium and large size test problems. Similar results are obtained for the other metrics. Their contribution considers that the actual processing time of jobs may be reduced due to the "learning effect" of manual workers performing repetitive production operations. However, the research does not consider more than one machine.

### 2.5 Recent work

As a state of the art, recent authors have used wellrecognized and published methodologies with some modifications to solve the FJSP. Phanden and Jain [45] offer a simulation-based genetic algorithm approach to solve the FJSP-PPF and assess the effect of flexible process plan of a part-type in a production order on a makespan performance measure. Two case studies of varying sizes are considered to assess the effect of changing the flexible process plans of a part-type in a production order. For these case studies, a shop floor consists of 15 machines. The results indicate that selecting the best process plan among flexible process plans on the basis of a minimum total production time criterion for a part-type may not yield optimal schedule. However, no other algorithms are used for a comparative section.

Li and Gao [32] proposed an effective hybrid algorithm (HA) that hybridizes the genetic algorithm and tabu search, well-recognized and published methodologies for the FJSP with the objective of minimizing the makespan. In order to solve the FJSP effectively, effective encoding method, genetic operators and neighborhood structure are used in this study. As the authors explain, six famous benchmark set of instances (including 201 open problems) of FJSP have been used to evaluate the performance of the proposed HA. The set data were adopted from Fattahi et al. [16], Kacem et al. [26], Barnes and Chambers [4], Brandimarte [7], among others. Comparisons among proposed HA and other ten state-of-the-art reported algorithms are also provided to show the effectiveness and efficiency of the proposed method. From the results of each experiment, the proposed HA can obtain the best results for most

problems. In addition, some of them are new solutions to some benchmark problems which were not previously found. Also, the computational time of the proposed HA has been compared with other algorithms, and the proposed HA seems to cost less computational time than other algorithms. However, scheduling problems in the manufacturing field are neither the aim of this research nor the multi-objective perspective.

Xu et al. [53] established a mathematical model for the FJSP-PPF, and an improved bat algorithm was proposed to solve the mathematical model mentioned. The objective was to seek an appropriate schedule that costs minimum time to complete all operations, i.e., the makespan. A crossover and a mutation operation, well-recognized and published operators, were designed to strengthen the searching ability of the algorithm. The authors carried out experiments on actual examples, i.e., this paper uses the actual data of a manufacturing enterprise. The data consists of 6 jobs of 27 operations that can be implemented on 8 machines. It can be seen from the experimental results that the robustness and optimization ability of the algorithm proposed are better than the genetic algorithm and the Discrete Particle Swarm Optimization algorithm (DPSO) used for comparison. For the purposes of overcoming the shortcomings of the fixed parameters in bat algorithm, the value of the inertia weight was adjusted, and a linear decreasing inertia weight strategy was proposed. However, no standard instances were used in the comparative section.

Yin et al. [55] detailed a new low-carbon mathematical scheduling model for the flexible job-shop environment. The authors select productivity, energy consumption and noise emission as the three low-carbon scheduling optimization objectives. A multi-objective genetic algorithm based on a simplex lattice design was proposed to solve the mathematical model effectively. The wellrecognized and published operators such as the corresponding encoding/decoding method, fitness function, and crossover/mutation operators were designed specifically for the features of this problem. Three problem instances with different scales and one engineering case study illustrate and evaluate the performance of this method. The instances mentioned considered 4 jobs x 5 machines, 10 jobs x 6 machines and 20 jobs x 5 machines respectively. The engineering case study is related to a cooling system. The cooling system is an important component of any automotive engine. This automotive part requires seven main steps to build a whole cooling system. The operations for each step of the process range from 13 to 15 tasks. Eight machines are available for execution of these operations. It is a classical FJSP configuration. To test the efficiency of the proposed algorithm, it was compared with the NSGA-II for the aforementioned cases. Based on the results the proposed algorithm outperforms NSGA-II with regard to all metrics.

No standard instances were used in this research. It is because there is no information about energy consumption and noise emission for standard instances.

The review mentioned above clearly underlines several gaps in the actual state of the art. The current research mentioned above does contain greedy procedures to obtain promising solutions. The performance of the algorithms mentioned above is implicit in the greedy procedures. For example, the traditional evolutionary operators, used by the genetic algorithms, produce a new population entirely, i.e., performing two main processes (crossing and mutation) to different solutions (parents) in order to build a new offspring (child). The processes mentioned have an implicit contribution to the performance of the genetic algorithms. However, the works mentioned above do not permit to have control in characterizing the solution space explicitly. Therefore, the greedy procedures are replaced by an explicit probability distribution over the FJSP-PPF in this research. With this change, we have control to characterize the solution space explicitly. Although the EDA has successfully been used to solve complex combinatorial optimization problems (with or without hybridization with other algorithms), there are currently no publications that use an EDA for the FJSP-PPF. We can cite some studies such as Chen et al. [10-12], Liu et al. [34], Peña et al. [44], Jarboui et al. [25], Wang et al. [51], and Pan and Ruiz [42]. These studies have tackled different scheduling problems by means of EDA. A new research using EDA for scheduling is reported in Wang et al. [52]. The authors address distributed permutation flow shop scheduling problems by a fuzzy logic-based hybrid EDA. In order to explore more promising search space, the proposed algorithm hybridizes the probabilistic model of EDA with crossover and mutation operators of a genetic algorithm to produce new offspring. The Mallows distribution is reported in Irurozki et al. [24]. The authors address the problems of sampling and learning of such distributions using the Cayley distance as a distance metric between permutations. Finally, Table 2 depicts the state of the art on the FJSP-PPF with other related problems.

## 3 MEDA - for the FJSP-PPF

A feasible solution representation for the FJSP-PPF uses three different vectors. The first vector is named the process plan vector: its length equals the total of jobs, where each element shows the corresponding chosen process plan for each job. The second vector is named the operation sequence vector: its length equals the total number of operations, where every element contains a non-repeated integer value, i.e. the vector is a permutationbased representation. The third vector is named the machine assignment vector: each element represents the

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

Table 3 An instance of the FJSP-PPF

corresponding selected machine for each operation. To explain the representation, we provide an example by considering a problem with at most 4 process plans, 6 jobs and 3 machines as shown in Table 3. The example mentioned above is an extension of the example shown in Table 1 and Fig. 2. Figure 4 illustrates the representation of a feasible solution.

The solution representation mentioned above, depicted in Fig. 4 starts with the process plan vector. The mentioned vector is located in the upper left corner of Fig. 4. Each element shows the corresponding chosen process plan for each job, i.e., $P=\left\{\begin{array}{lllllllll}1 & 3 & 2 & 1 & 1 & 2\end{array}\right\}$. Based on Table $3, P(1)=$ 1 corresponding to operation sequence $3 \prec 1 \prec 2$. These three operations, from job number one, correspond to the
![img-7.jpeg](img-7.jpeg)

Fig. 4 Illustration of the representation of a feasible solution

Fig. 5 a A sample of process plan vectors. b A sample of operation sequence vectors. c A sample of machine assignment vectors
a
Pseudocode 1(a). Population initialization for process plan vectors
$\mathrm{n} \leftarrow$ jobs
$\mathrm{M} \leftarrow$ Individuals
for $\mathrm{i}=1$ to M
for $\mathrm{j}=1$ to n
Process plan vector $[i][j]=$ choose randomly a possible process plan for the job j
endfor
endfor
![img-8.jpeg](img-8.jpeg)

Job 1
![img-9.jpeg](img-9.jpeg)
total operations per job $[j]=$ identify the number of operations for the job j
endfor
index $:=1$
while (index $\leq \mathrm{m}$ ) do
job = choose randomly a job
if(total operations per job[job] $>0$ ) then
//pending operations to be sequenced
tentative sequence vector[i][index] = job
total operations per job[job] $=$ total operations per job[job] - 1
index $=$ index +1
endif
endwhile
for $\mathrm{j}=1$ to n
total operations per job $[j]=$ identify the number of operations for the job j
endfor
operation $:=1$
job $:=1$
while[job $\leq \mathrm{n}$ ) do
index $:=1$
while(index $\leq \mathrm{m}$ ) do
if(entative sequence vector[i][index] == job) then
if(total operations per job [job] $>0$ ) then
sequence vector[i][index] = operation
total operation per job[job] $=$ total operations per job[job] - 1
operation $=$ operation +1
endif
endif
index $=$ index +1
endwhile
job $=$ job +1
endwhile
endfor

# Population initialization 

Operation sequence vectors

Fig. 5 (continued)
![img-10.jpeg](img-10.jpeg)
values $1-2-3$ in the operation sequence solution vector $\sigma$. $P(2)=3$ corresponds to operation sequence $1 \prec 3 \prec 2 \prec$ 4. These four operations, from job number two, correspond to the values $4-5-6-7$ in the operation sequence solution vector $\sigma$, and so on. Although each element in $\sigma$ can be located in any position along the solution vector, as any permutation-based representation, the precedence between operations of each job must be kept in $\sigma$. For example, the values $1-2-3$, from job number one, must appear in the same order in $\sigma$, from left to right. If the vector solution of the operation sequence satisfies the precedence mentioned above, it satisfies the corresponding original operation sequence from the job mentioned. This representation is based on Gen et al. [21]. Therefore, the operation sequence vector located next to the process plan vector of Fig. 4 contains non-repeated integer values and is feasible, i.e., $\sigma=\{141215168912134173181051167\}$. Finally, the machine assignment vector, located next to the operation sequence vector of Fig. 4, represents the corresponding selected machine for each operation, i.e., $A=\{223311223222122321\}$. Based on Table 3, $A(1)=2$ considers using machine number two, for the first value in $\sigma$, i.e., $\sigma(1)=14$. The value 14 in $\sigma(1)$ represents the first operation of job number five.

The initialization of the population is implemented as an array of $M$ vectors of size $n$ jobs for the process plan vectors. Another array of $M$ vectors of size $m$, where $m$ represents the total number of operations to sequence for the operation sequence vectors and another array of $M$ vectors of size $m$, where $m$ represents the total number of operations to assign for the machine assignment vectors. Initial population
members are generated randomly in order to enable a wide range of solutions [22]. Figure 5a shows different process plan vectors obtained with the corresponding Pseudocode 1(a). Figure 5b details different operation sequence vectors obtained with the corresponding Pseudocode 1(b). Finally, Fig. 5c depicts different machine assignment vectors obtained with the corresponding Pseudocode 1(c).

### 3.1 Pareto-front construction phase

In each generation, a Pareto-front approach is built with the population. A Pareto-front approach is considered in this research based on Kacem et al. [26]. The optimality notion in the Pareto approaches can be formulated as follows: the Pareto-optimal set is formed by non-dominated solutions. $x$ vector dominates $y$ vector if $\forall 1 \leq q \leq L, f_{q}(x) \leq f_{q}(y)$ where $f_{q}($.$) is the q$ th objective function, $L$ is the number of objective functions and at least one index $r$ exists such that $f_{r}(x)<f_{r}(y)$. A solution is non-dominated if it is not dominated by any other solution. Figure 6a details the fitness of two feasible solutions, i.e., the makespan and the maximal workload. Figure 6b depicts a Pareto-optimality approach example. A non-dominated set of solutions in each generation is found and used for the selection process, as well as for the improvement of the central permutation estimate $\sigma_{0}$ in the GMD process.

The selection process takes the subset $N$ from $M$ parents (where $N<M$ ) are chosen by a tournament selection which is executed based on where the candidate solutions are located on the Pareto-front approach. Different cases are possible as follows: if a solution is feasible and another is

Fig. 6 a A graphical representation fitness of two feasible solutions. b Pareto-optimality approach
![img-11.jpeg](img-11.jpeg)
![img-12.jpeg](img-12.jpeg)

infeasible, the feasible solution is preferable. If a solution is non-dominated and another is dominated, the nondominated solution is preferable. If both solutions are nondominated, the solution that belongs to a better Pareto-front layer is preferable.

In order to determine which Pareto-front layer belongs to each non-dominated solution, we calculate two entities: 1) domination count $n_{p}$, the number of solutions which dominate the solution $p$, and 2) $S_{p}$, a set of solutions that the solution $p$ dominates. All solutions in the first non-dominated front will have their domination count as zero. Now, for each solution $p$ with $n_{p}=0$ we visit each member $(q)$ of its set $S_{p}$ and reduce its domination count by one. In doing so, if for any member $q$ the domination count becomes zero, we put it on a separate list $Q$. These members belong to the second non-dominated front. Now, the above procedure is continued with each member and the third front is identified. This process continues until all fronts are identified.

### 3.2 Probability model proposed

### 3.2.1 Probability model for process plan vectors

Unlike GA which produces offspring through crossover and mutation operators, EDA does it by sampling according to a probability model. Therefore, the probability model has a great effect on the performance of EDA. MEDA contains three probability models. The first probability model aims to determine an estimate of a distribution model

Process plan vectors
![img-13.jpeg](img-13.jpeg)

Fig. 7 Building an estimation of distribution model for the process plan vectors
to generate new offspring (process plan vectors) using a subset of $N$ chosen process plan vectors in the previous step. To obtain the estimate we use the UMDA algorithm introduced by Mühlenbein [38]. The algorithm mentioned uses the simplest approach to estimate the joint probability distribution of the selected individuals in each generation, $p(\mathbf{x})$. This joint probability distribution is factorized as a product of univariate marginal distributions, $p(\mathbf{x})=$ $p(x \mid N)=\prod_{i=1}^{n} p\left(x_{i}\right)$.

Every univariate marginal distribution is estimated from marginal frequencies, $p\left(x_{i}\right)=\frac{\sum_{j=1}^{N} \delta_{j}\left(X_{i}=x_{i} \mid N\right)}{N}$ where $\delta_{j}\left(X_{i}=x_{i} \mid N\right)=\left\{\begin{array}{l}1, \text { if the jth case of } \mathrm{N}, \mathrm{X}_{\mathrm{i}}=\mathrm{x}_{\mathrm{i}} \\ 0, \text { otherwise }\end{array}\right.$

Figure 7 contains an example to realize how the probability distribution is built in a subset of $N$ process plan vectors. The element $p_{k j}(l)$ of the process plan probability matrix called B1 matrix represents the probability that process plan $k$ be selected for the job $j$ of the process plan vector at generation $l$. The value of $p_{k j}$ refers to the importance of a process plan for a specific job. For all $k\left(k=1,2, \ldots, P_{j}\right)$ and $j(j=1,2, \ldots, n)$

### 3.2.2 Probability model for operation sequence vectors

The second probability model aims to determine an estimate of an explicit probability distribution in the domain of permutations by the GMD to generate new offspring (operation sequence vectors) using a subset of $N$ previous sequence vectors. The GMD can be used to solve permutation-based optimization problems. Formally, the Mallows model is defined as:
$P(\sigma)=\psi(\theta)^{-1} \exp \left(-\theta D\left(\sigma, \sigma_{0}\right)\right)$
where $\theta$ is a spread parameter, and $D\left(\sigma, \sigma_{0}\right)$ is the distance from $\sigma$ to the central permutation $\sigma_{0}$, where $\psi(\theta)$ is a normalization constant. In the present work, Kendall's $-\tau$ is the distance metric with which the Mallows model is coupled. Let's consider $\sigma_{0}=\left\{\begin{array}{llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

$D\left(\sigma, \sigma_{0}\right)=D_{\tau}\left(\sigma, \sigma_{0}\right)=\sum_{q=1}^{m-1} V_{q}\left(\sigma, \sigma_{0}\right)$. The GMD is given as follows
$P(\sigma)=\psi(\theta)^{-1} \exp \left(\sum_{q=1}^{m-1}-\theta_{q} V_{q}\left(\sigma, \sigma_{0}\right)\right)$


The same procedure to identify the Kendall's $-\tau$ distance metric in $\sigma_{2}$, i.e., the $V_{q}\left(\sigma_{2}, \sigma_{0}\right)$ for the $q t h$ position is detailed below:


Instead of a single spread parameter $\theta$ as in the Mallows distribution, the GMD uses $m-1$ spread parameters $\theta=$ $\left(\theta_{1}, \theta_{2}, \ldots, \theta_{m-1}\right)$, every $\theta_{q}$ affecting a particular position $q$ of the permutation. Based on Fligner and Verducci [19], it is possible to determine any permutation $\left(\sigma, \sigma_{0}\right)$ with the $m-1$ integers $V_{1}\left(\sigma, \sigma_{0}\right), \ldots, V_{m-1}\left(\sigma, \sigma_{0}\right)$ in which Kendall's- $\tau$ distance $D_{\tau}\left(\sigma, \sigma_{0}\right)$ decomposes. Under the uniform distribution, the $V_{q}\left(\sigma, \sigma_{0}\right)$ variables that define a permutation are independent [18] and as a consequence, the probability distribution of the random variables $V_{q}\left(\sigma, \sigma_{0}\right)$ under the GMD given by (2) can be written as:
$P\left(V_{q}\left(\sigma, \sigma_{0}\right)=r_{q}\right)=\frac{\exp \left(-\theta_{q} r_{q}\right)}{\psi_{q}\left(\theta_{q}\right)} \quad r_{q} \in\{0, \ldots, m-q$

The normalization constant $\psi(\theta)$ in the GMD can be simplified as the product of $m-1$ terms
$\psi(\theta)=\prod_{q=1}^{m-1} \psi_{q}\left(\theta_{q}\right)=\prod_{q=1}^{m-1} \frac{1-\exp \left(-\theta_{q}(m-q+1)\right)}{1-\exp \left(-\theta_{q}\right)}$
where $m$ is the total of items in the permutation. When the GMD considers Kendall's- $\tau$ distance, it can be expressed as a multi-stage ranking model [19]. Therefore, the probability distribution of a given permutation $\sigma$ is given as
$P(\sigma)=\prod_{q=1}^{m-1} P\left(V_{q}\left(\sigma, \sigma_{0}\right)=r_{q}\right)$
where $r_{q}$ is a possible value for the $q$ position on the $V_{q}$.
The first stage consists of computing an approximation of the central permutation $\sigma_{0}$. Although the behavior of the GMD depends on the spread vector $\theta$ that determines the shape of the distribution Ceberio et al. [8], future research work is aimed at improving the estimation of the central permutation $\sigma_{0}$ to enhance the performance of the algorithm. To avoid losing diversity through the modification in the central permutation is the goal. In this research, when a non-dominated set of solutions is
where $V_{q}\left(\sigma, \sigma_{0}\right)$ is the number of positions on the right of $q$ with values smaller than the current position on the permutation $\left(\sigma, \sigma_{0}\right)$. Based on the example above for $\sigma_{1}$, the $V_{q}\left(\sigma_{1}, \sigma_{0}\right)$ for the $q t h$ position is detailed below:


found in the Pareto-front approach mentioned above, the corresponding operation sequence vectors of the nondominated set of solutions are used as an input parameter by the Borda algorithm [6] to get a better approximation to the central permutation $\sigma_{0}$. To the best of our knowledge, a modification on the parameter described has not been developed for these kind of algorithms. The following procedure details an example in order to estimate the central permutation $\sigma_{0}$ with the Borda algorithm using the corresponding operation sequence vectors of the nondominated set of solutions

## Pseudocode 2 Central permutation computation $\sigma_{0}$

$\mathrm{m} \leftarrow$ number of positions (total operations)
$\mathrm{M} \leftarrow$ Individuals
from the non - dominated set of permutations $\left\{\sigma_{1}, \ldots, \sigma_{M}\right\}$
for $\mathrm{j}=1$ to m
Compute $\pi(\mathrm{j})=\sum_{\mathrm{i}=1}^{\mathrm{M}} \sigma_{\mathrm{i}}(\mathrm{j}) / \mathrm{M}$
Endfor
visited $=\{\varnothing\}$, auxiliary array
for $\mathrm{j}:=1$ to m
Find the lowest value from $\pi(\mathrm{i})$
index $\leftarrow \arg \min _{\mathrm{i}}\{\pi(\mathrm{i})\} \mathrm{i} \notin$ visited $\}$
Building $\sigma_{0} \ldots$
$\sigma_{0}($ index $)=\mathrm{j}$
visited $=$ visited $U$ index
Endfor
Once the central permutation $\sigma_{0}$ is approximated using the Pareto-front approach, the second stage consists of computing the dispersion parameters $\theta_{j}$ by solving
$\bar{V}_{j}=\frac{1}{\exp \left(\theta_{q}\right)-1}-\frac{m-q+1}{\exp \left(\theta_{q}(m-q+1)\right)-1}, q=1: m-1$
where $\bar{V}_{q}=\frac{1}{N} \sum_{i=1}^{N} V_{q}\left(\sigma_{i} \sigma_{0}\right)$

Fig. 8 A visual representation of the Kendall's $-\tau$ distance metric

Central Permutation
Permutation 1
Permutation 2


![img-14.jpeg](img-14.jpeg)

With the spread parameter vector generated $\theta$ and the central permutation estimated $\sigma_{0}$, it is possible to create the operations sequence probability matrix called B2 to obtain new $\mathbf{V}\left(\sigma, \sigma_{0}\right)$ vectors by (3). The element $p_{i j q}(l)$ of the operation sequence probability matrix B2 represents the probability that operation $O_{i, j}$ requires $r$ number of adjacent transpositions required to match the operation $O_{i, j}$ in the same $q$ th position as the central permutation $\sigma_{0}$ at generation $l$.

Figure 9 depicts a visual example for only two positions on the sequence, in the operation sequence probability matrix B2. Based on the previous example above, the $r_{q}$ possible values for a new $\mathbf{V}\left(\sigma, \sigma_{0}\right)$ vector will be between 0 and $m-q$, where $q$ represents the positions on the operation sequence.

For each $q t h$ position, the probability for each $r_{q}$ value i.e., $p_{i j q}$, refers to the importance of an operation for a specific position of the permutation-based representation. For all $\left(i=1,2, \ldots, n_{i}\right), j(j=1,2, \ldots, n)$ and $q(q=1,2, \ldots, m-1)$.

In this way, this research characterizes the space of possible solutions explicitly through the estimation of the probability that an operation for a specific position of the permutation-based representation is selected.

The process of generating the new valid permutations (operations sequence vectors) is decoding the $\mathbf{V}\left(\sigma, \sigma_{0}\right)$ vectors. This research uses the Meilă et al. [37] algorithm for transforming the vectors mentioned above in valid permutations. The following procedure represents an example to get a valid permutation.

## Pseudocode 3 Meilă et al. (2007) procedure

$\mathrm{m} \leftarrow$ number of positions (total operations)
Let a sample vector $\mathbf{V}\left(\sigma, \sigma_{0}\right)=2,0,1$
therefore $\mathrm{m}:=4$
insert m in $0 \rightarrow\left(\sigma, \sigma_{0}\right)^{-1}=4$
insert j := 3 in $V_{2}:=1 \rightarrow\left(\sigma, \sigma_{0}\right)^{-1}=4,3$
insert $\mathrm{j}:=2$ in $V_{2}:=0 \rightarrow\left(\sigma, \sigma_{0}\right)^{-1}=2,4,3$
insert $\mathrm{j}:=1$ in $V_{1}:=2 \rightarrow\left(\sigma, \sigma_{0}\right)^{-1}=2,4,1,3$
Every permutation $\sigma$ is obtained by inverting a composing with the central permutation $\sigma_{0},\left(\left(\sigma, \sigma_{0}\right)^{-1}\right)^{-1} \sigma_{0}=\sigma \sigma_{0}^{-1} \sigma_{0}=\sigma$

Fig. 9 An operation sequence probability matrix B2

Operation sequence probability matrix
$\mathrm{q}=1$, i.e., first position on the sequence
![img-15.jpeg](img-15.jpeg)
$\mathrm{q}=2$, i.e., second position on the sequence
![img-16.jpeg](img-16.jpeg)

Fig. 10 GMD process for the FJSP-PPF problem

Finally, Fig. 10 details the overall process for GMD process mentioned above.

### 3.2.3 Probability model for machine assignment vectors

The third probability model aims to determine an estimate of a distribution model to generate new offspring (machine assignment vectors) using a subset of $N$ selected assignments. To obtain the estimate we also use the UMDA algorithm. The element $p_{i j m}(l)$ of the machine probability matrix called B3 represents the probability that operation $O_{i, j}$ is processed on machine $m$ at generation $l$. The value of $p_{i j m}$ indicates the rationality of an operation processed on a certain machine.

### 3.3 Sampling process

The sampling process is made according to the probability matrices B1, B2 and B3. New promising solutions may be generated. In particular, to generate a new solution

Table 4 Comparison of results with standard benchmarking datasets
the process plan vector should be generated first, then the operation sequence vector and finally the machine assignment vector. The MEDA procedure to solve the FJSPPPF is illustrated below

```
Pseudocode 4 MEDA framework for the FJSP-PPF
\(D_{p} \leftarrow\) Generate M individuals
\(\mathrm{t}:=1\)
Do
    \(\mathrm{D}_{\mathrm{s}-1} \leftarrow\) Evaluate individuals (makespan and max workload)
    \(\mathrm{P}_{\mathrm{s}-1} \leftarrow\) Compute Pareto front from \(\mathrm{D}_{\mathrm{t}-1}\)
    \(\mathrm{Ds}_{\mathrm{s}-1} \leftarrow\) Select N individuals from \(\mathrm{Ds}_{\mathrm{t}-1}\)
    Compute B1 matrix from \(\mathrm{Ds}_{\mathrm{t}-1}\)
    Compute B2 matrix from \(\mathrm{Ds}_{\mathrm{t}-1}\)
        Estimate central permutation \(\sigma_{0}\) from \(\mathrm{P}_{\mathrm{t}-1}\)
        Estimate spread parameters \(\boldsymbol{\theta}\) from \(\mathrm{Ds}_{\mathrm{t}-1}\) and \(\sigma_{0}\)
    Compute B3 matrix from \(\mathrm{Ds}_{\mathrm{t}-1}\)
    \(\mathrm{Ds}_{\mathrm{t}} \leftarrow\) Sample M individuals from \(\mathrm{B} 1, \mathrm{~B} 2, \mathrm{~B} 3\), matrices
    \(\mathrm{D}_{\mathrm{t}} \leftarrow\) Find best individuals from \(\mathrm{Ds}_{\mathrm{t}-1} \cup \mathrm{Ds}_{\mathrm{t}}\)
    \(\mathrm{t}:=\mathrm{t}+1\)
Until (stopping criterion is met)
```


# 4 Computational results and comparison 

### 4.1 Comparison with standard benchmarking datasets

In order to validate the scientific relevance of this paper, we compare the MEDA results with others in some general and standard benchmarking datasets such as the Adams, Balas and Zawack [1] instances, called abz, taking five instances

Table 5 A systematical approach used for determining an instance of the FJSP-PPF
from abz5 to abz9 specifically; the Fisher and Thompson [17] instances, called ft , taking three instances, $\mathrm{ft} 06, \mathrm{ft} 10$, and ft 20 ; the Lawrence [30] instances, called la, taking forty instances from la01 to la40; the Applegate and Cook [3] instances, called orb, taking ten instances from orb01 to orb10; the Storer, Wu and Vaccari [48] instances, called swv, taking twenty instances from swv01 to swv20; finally, the Yamada and Nakano [54] instances, called yn, taking four instances from yn1 to yn4.

The instances mentioned above are used as input data for the mentioned comparison. The experiments are executed in a Lanix ${ }^{\circledR}$ Titan HX 4200 computer, Intel ${ }^{\circledR}$ Core ${ }^{\mathrm{TM}} \mathrm{i} 7$ processor, $3.4 \mathrm{GHz}, 8 \mathrm{~GB}$ of RAM, Windows ${ }^{\circledR} 10$ for 64 bits to run every instance. $\mathrm{C}++$ language is used for the implementation for all the comparisons. To account for the stochastic nature of the MEDA, we run 30 trials for all the datasets. Each trial contains 50 generations, 1000
![img-17.jpeg](img-17.jpeg)

Fig. 11 First Pareto-front of the seventh instance obtained by the MEDA for the FJSP-PPF

Table 6 Comparison of the results
solution vectors belonging to each generation. We measure the relative percentage increase (RPI) as:
$\operatorname{RPI}\left(c_{i}\right)=\left(c_{i}-c^{*}\right) / c^{*}$
where $c_{i}$ is the makespan obtained in the $i$ th replication, and $c^{*}$ is the best makespan found and reported in the literature. The distribution of the experimental results in every interval is presented in Table 4. It is clear from the table that the results of the MEDA algorithm are comparatively concentrated, which is mainly in the range of $[0,0.05]$, over the best solution found, i.e., makespan, for all the datasets. In addition, Table 4 describes the outliers, i.e., deteriorations produced by MEDA. Based on the results the MEDA is a suitable approach for solving real flexible manufacturing processes.

### 4.2 Comparison with multi-objective algorithms

Furthermore, in order to enhance the novelty of the MEDA, we consider evaluating the MEDA with the same characteristics of the industrial environment. A hundred flexible job-shop instances have been developed replicating real flexible manufacturing processes, to analyze the solution capability of the MEDA on the FJSP-PPF. The instances contain a different number of jobs, machines, operations, process plans for each job and alternative machines for performing each operation.

An estimation of distribution algorithm coupled with the GMD process without using the Pareto-front approach, called w-EDA, is proposed as a benchmark for comparison with the MEDA scheme. In addition, the multiobjective algorithms proposed by Srinivas and Deb [47] called NSGA

Fig. 12 Comparison of results using boxplots
![img-18.jpeg](img-18.jpeg)

Table 7 Distribution of the results
and by Deb et al. [15] called NSGA-II are proposed as a benchmark for comparison with the MEDA scheme. The code of the proposed algorithms are obtained from the Kanpur Genetic Algorithms Laboratory web. The instances mentioned above are used as input data for the algorithms. The experiments are executed in the same computer and language specification. To account for the stochastic nature of the shop floor, we run the same number of trials, i.e., 30 for all the algorithms. Each trial contains the same number of generations, i.e., 50 , and the same size of the population, i.e., 1000 solution vectors. Table 5 presents the systematical approach used for determining the jobs, machines, operations, process plans for each job, alternative machines for operations and processing times of operations for each job in order to replicate this experiment and get similar results. Although the systematical approach
mentioned above is detailed in Table 5, the instances are available at https://goo.gl/1JeHDr

Two conflicting objectives are analyzed; the makespan and the maximal machine workload, i.e., the maximum working time spent on any machine. The aim is to prevent a solution from assigning too much work on a single machine and to keep the balance of work distribution over the machines. The makespan and the maximal machine workload are conflicting objectives in nature when there exist dominant machines with regard to processing times of the operations. In addition, while the number of available machines in the process is greater, the average utilization of every machine is lower. Therefore, the aim is to determine the balance between both objectives. The objectives mentioned above are used as input data to find the response variable for the experiment, i.e., we compute the
![img-19.jpeg](img-19.jpeg)

Fig. 13 Statistical test

Table 8 Component parts of an automotive instrument panel
area obtained from the best Pareto-front after running every algorithm. As an example, Fig. 11 shows the area computed by the first Pareto-front in the seventh instance.

We measure the relative percentage increase (RPI) using the same (7), i.e., $c_{i}$ is the area obtained from the best Pareto-front obtained in the $i$ th replication by a given algorithm configuration, and $c^{*}$ is the best area found by any of the algorithm configurations. Note that for this problem, there are no known effective or exact techniques and comparison with an optimal solution is not possible. Table 6 depicts the mean and standard deviation metrics for all the algorithms used for the comparison of over 30 independent runs per instance.

Figure 12 includes four box plots: the NSGA, the NSGAII, the MEDA, and the w-EDA performance after running all the instances. As we can see, the EDA coupled with the GMD process without using the Pareto-front approach,

Fig. 14 Instrument panel manufacturing
![img-20.jpeg](img-20.jpeg)

Table 9 Comparison of results between recent algorithms

Table 10 Distribution of the results for the instrument panel manufacturing case

Fig. 15 Comparison of results between recent algorithms using boxplots
![img-21.jpeg](img-21.jpeg)

![img-22.jpeg](img-22.jpeg)

Fig. 16 The Dunnett test
i.e., the w-EDA, is competitive in order to identify the bestperforming ones. Although the GMD process is enough to find suitable solutions, the Pareto-approach helps to improve the results when the non-dominated solutions are considered in the GMD process. The MEDA results report how the performance of the algorithm is improved.

The distribution of the experimental results in each interval is presented in Table 7. It is clear from the table
that the results of the MEDA algorithm are comparatively concentrated, which is mainly in the range of $[0,3]$, whereas the results of the other algorithms are relatively distributed. In addition, we analyze whether there is a statistically significant difference between the averages of the algorithms. Figure 13 depicts the statistical test, i.e., the Dunnett test. As we can see, the proposed MEDA is competitive. There is a difference between the MEDA with

Fig. 17 Computational time comparative
![img-23.jpeg](img-23.jpeg)

the other algorithms for the FJSP-PPF. We confirm that the hybridization between the GMD process and the Paretofront approach is suitable for the EDA scheme. Thus, the MEDA algorithm in terms of solving the FJSP-PPF is more robust than the other algorithms.

### 4.3 Comparison with recent algorithms for the FJSP

Based on the previous results in the last comparison mentioned above, recent algorithms are proposed as a benchmark for comparison with the MEDA scheme. Because MEDA is built to be functional in flexible manufacturing processes, the recent algorithms mentioned above are the simulation-based genetic algorithm presented by Phanden and Jain [45], the improved bat algorithm proposed by Xu et al. [53], the hybrid algorithm that hybridizes the genetic algorithm and tabu search detailed by Li and Gao [32], and the genetic algorithm designed by Li et al. [33]. All the algorithms mentioned are considered recent algorithms for the FJSP. These algorithms have been implemented by the authors. The experiments are executed with the same parameters and specification detailed above. Furthermore, a real-life problem is considered for comparison with the MEDA scheme. It is related to the instrument panel manufacturing. An automotive supplier located in the middle of Mexico receives different automotive parts for assembling instrument panels every day. Those parts are enlisted in Table 8. All the parts mentioned are depicted in Fig. 14.

Multiple machines are available to process all the parts, and the processing times vary for different machines and operating procedures. As we can see in Fig. 14, there is more than one process plan for the instrument panel manufacturing, i.e., the main assemblies (cluster panel, facia panel, glove box, and lower cover) can be built independently between them. Thus, the shop floor represents a typical flexible job-shop with process plan flexibility. We established a workload to evaluate and find the best schedule. Our experiments are based on the production of 10,000 assemblies. The workload mentioned contains different orders, due dates, and the kinds of instrument panels produced in the manufacturing process mentioned above, replicating the actual manufacturing process.

As in the previous comparison, we measure the relative percentage increase (RPI) detailed in (7). Table 9 describes the mean and standard deviation metrics for the recent algorithms used for the comparison of over 30 independent runs per instance. Based on Table 9, there is no significant difference between the performance of the algorithms, i.e, the global performance is the same. The differences are only in thousandths. Therefore, the MEDA is competitive in the same industrial environment.

The distribution of the experimental results in each interval is presented in Table 10. It is clear from the table that the results of all the algorithms are relatively distributed at the same intervals. Moreover, most results are concentrated in the first interval for whatever algorithm. The difference between the worst and the best performance is only $0.007 \%$, i.e., 2799/3000 vs 2822/3000. The MEDA is a suitable approach for solving real flexible manufacturing processes.

Figure 15 includes five boxplots: the Phanden and Jain [45] algorithm, the Xu et al. [53] algorithm, the MEDA, the Li and Gao [32] algorithm, and the Li et al. [33] algorithm performance after running all the instances. As we can see, the performance of the MEDA is competitive in the same characteristics of the industrial environment. We emphasize that the real problem used for analyzing the solution capability of the MEDA on the FJSP-PPF replicates a real flexible manufacturing process.

In addition, we analyze whether there is a statistically significant difference between the averages of the algorithms. Figure 16 depicts the statistical test, i.e., the Dunnett test. As we can see, the proposed MEDA is competitive and there is no difference between the algorithms for the FJSP-PPF.

Finally, the computational time comparison is shown in Fig. 17.

## 5 Conclusions and future research

This paper discusses the FJSP-PPF, which considers multiple process plans for jobs by excluding the assumption of only one feasible process plan for each job of FJSP. To solve this problem, we propose the EDA application scheme. By means of numerical experiments, this approach generates competitive solutions.

This novel research concludes that the GMD can be coupled with the EDA scheme in order to solve combinatorial optimization problems such as the FJSP-PPF from a multi-objective perspective. By using the Paretofront approach it is possible to obtain better solutions for the FJSP-PPF. The computational results establish that the different probability models used for the FJSP-PPF with large data sets are suitable. The Pareto-front approach is not only used for obtaining the best solutions for the MEDA scheme, it is also used to propose a different way of improving the estimation of the central permutation $\sigma_{0}$ in the GMD process. The MEDA provides an effective estimate of the operations at the positions in the sequence vector for the FJSP-PPF.

Explicit probability distributions in the domain of permutations for the FJSP-PPF should be considered in future research. Estimating relationships for other related

dynamic job-shop issues, e.g., shutdown, maintenance, new products, and online environments, should be reconsidered in light of these results. Since the MEDA presents stability, it appears very suitable for implementation in software systems for practical purposes. Further research directions may deal with an extension of the MEDA for building effective modules for specific users in the industry. Finally, the MEDA might be used in other types of job-shop systems.

Acknowledgments We would like to express our gratitude to all the reviewers for their comments in improving the manuscript.
