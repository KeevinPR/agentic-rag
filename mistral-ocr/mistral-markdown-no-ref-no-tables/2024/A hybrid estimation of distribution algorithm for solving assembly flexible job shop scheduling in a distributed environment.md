# A hybrid estimation of distribution algorithm for solving assembly flexible job shop scheduling in a distributed environment 

Baigang $\mathrm{Du}^{a, b}$, Shuai Han ${ }^{\mathrm{a}, \mathrm{b}}$, Jun Guo ${ }^{\mathrm{a}, \mathrm{b}, \mathrm{c}}$, Yibing $\mathrm{Li}^{\mathrm{a}, \mathrm{b}}$<br>${ }^{a}$ School of Mechanical and Electronic Engineering, Wuhan University of Technology, Wuhan, 430070, China<br>${ }^{\mathrm{b}}$ Hubei Digital Manufacturing Key Laboratory, Wuhan, 430070, China

## A R TICLE INFO

Keywords:
Distributed assembly flexible job shop scheduling problem
Estimation of distribution algorithm
Differential evolution
Variable neighborhood search

## A B STR A C T

This paper proposes a novel distributed assembly flexible job shop scheduling problem (DAFJSP), which involves three stages: production stage, assembly stage, and delivery stage. The production stage is accomplished in a few flexible job shops, the assembly stage is accomplished in a few single-machine factories, and the delivery stage is to deliver the obtained products to the corresponding customers. To address the problem, a hybrid estimation of distribution algorithm based on differential evolution operator and variable neighborhood search (HEDA-DEV) is proposed with the goal of minimizing the total cost and tardiness. Firstly, a new multidimensional coding method is designed based on the features of the DAFJSP. Secondly, two mutation operators and the similarity coefficient based on the probability matrix are put forward to implement the dynamic mutation. Thirdly, five types of neighborhood structures satisfying cooperative search strategies are employed to adequately improve the local exploitation ability. Finally, the comparison experiment results suggest that the proposed HEDA-DEV has competitive performance compared to the selected efficient algorithms. Moreover, a real case study is used to demonstrate that HEDA-DEV is an effective method for solving DAFJSP.

## 1. Introduction

As economic globalization becomes popular, the conventional singlefactory production mode is unable to meet the increasing market demand. So, more and more enterprises have begun to set up multiple factories in different places to improve their production efficiency (Naderi and Azab, 2014; Hsu et al., 2016; Hamzadayi, 2020; Behnamian and Fatemi Ghomi, 2016). Different from the single-factory production mode, a distributed manufacturing system must address two interrelated decisions, i.e., the allocation of jobs among factories and the scheduling of production within each factory (Zhang et al., 2018). It is much more complex than the conventional single-factory production mode because it has to deal with the problem of optimizing the scheduling across multiple factories simultaneously (Zhang and Xing, 2018).

Recently, the problem of distributed scheduling has attracted extensive attention from many scholars due to its theoretical significance and practical applications. Most researchers focus on the distributed scheduling optimization problem under various processing modes: distributed parallel machine scheduling system (Lei et al., 2021; Mönch and Shen, 2021), distributed job shop scheduling system (Şahman, 2021; Hsu et al., 2016), distributed flow-shop scheduling system (Cai
et al., 2020; Huang et al., 2021; Rifai et al., 2016; Shao et al., 2020; Ying and Lin, 2018), distributed flexible manufacturing system (Chang and Liu, 2017; Lin et al., 2020; Wu et al., 2017; Guo et al., 2020). These distributed systems can be regarded as the extension of classical production systems. However, in practice, most practical products are assembled from multiple components which need to be processed first. And the actual manufacturing process includes two stages: production and assembly (Pan et al., 2019). Therefore, it is of significant relevance to study the distributed assembly scheduling problem (DASP).

The research of DASP has focused on the distributed assembly permutation flow-shop scheduling problem (DAPFSP) in recent years. The DAPFSP was first proposed by Hatami et al. (2013), combining distributed manufacturing with conventional PFSP. In the subsequent research, Hatami et al. (2015) extended the problem and combined the sequence-dependent setup times with DAPFSP. Subsequently, many scholars have put forward many effective algorithms to solve DAPFSP. Maria Gonzalez-Neira et al. (2017) designed a metaheuristic approach that integrated biased randomization and simulation techniques to solve DAPFSP with stochastic processing times. Zhang et al. (2022) designed a new three-dimensional probability model for the estimation of distribution algorithm to better handle the DAPFSP with an energy-saving

[^0]
[^0]:    ${ }^{a}$ Corresponding author. School of Mechanical and Electronic Engineering, Wuhan University of Technology, Wuhan, 430070, China.
    E-mail address: junguo@whut.edu.cn (J. Guo).

![img-0.jpeg](img-0.jpeg)

Fig. 1. The main flow chart of DAFJSP.

Table 1
Notations.
strategy. Compared to the DAPFSP, the assembly flexible job shop scheduling in a distributed environment (DAFJSP) is more complicated because it needs to deal with the arrangement of operations with variable processing sequences and the selection of multiple assembly factories simultaneously. However, few studies have been done on the

DAFJSP. Wu et al. (2019) presented an improved differential evolution algorithm combined with the simulated annealing algorithm to address the DAFJSP. In the research of DAFJSP, few literatures consider the delivery of products to the customers after the completion of the assembly stage. However, in reality, we should not only consider producing the required products as quickly as possible but also consider delivering these products to customers with minimum delay and cost (Yang and Xu, 2021). Therefore, this paper proposes a novel DAFJSP considering the delivery of products to customers.

Given that FJSP is an NP-hard problem, DAFJSP, as an extension of FJSP is NP-hard. In the past few years, there has been an increasing trend of using meta-heuristic algorithms to address multi-objective optimal scheduling problems (He et al., 2019, 2021; Li et al., 2021; L. Sun et al., 2019; X. Sun et al., 2019). Among various meta-heuristic algorithms, the estimation of distribution algorithm (EDA) attracts our attention. It adopts the ideas of statistics and evolutionary algorithms for reference, updates the probability model by making up the dominant population in the previous generation, and uses the established probability model to guide the generation of the next generation (Hao et al., 2017). So far, many scholars have applied EDA to solve a variety of job shop scheduling problems and obtained good results, such as flow-shop scheduling (Wang et al., 2015), flexible job shop scheduling (Ge et al., 2016), etc. The differential evolution (DE) algorithm (Storn and Price, 1997) can disturb the population by information exchange between individual vectors and is widely applied for the advantages of easy implementation and high local search ability. Many scholars have applied DE to various shop scheduling areas. For example, He et al. (2022a) applied an improved adaptive DE algorithm to the energy-efficient open shop scheduling problem (EOSSP). Subsequently, they proposed an improved population-based DE algorithm to solve the EOSSP with multiple AGVs and deteriorated operations (He et al., 2022b). EDA has good global search ability but is poor at localized searching. It is easy to fall into local optimization in the later stages of the algorithm due to the reduction of population diversity. While DE can make up for the shortage of local searching ability of EDA. In addition, variable neighborhood search (VNS) is also used in conjunction with EDA because it can improve the quality of the solutions obtained by EDA (Liu et al., 2019). Inspired by these works, we propose a HEDA-DEV algorithm for the addressed problem. As far as we know, it is the first attempt to apply HEDA-DEV to DAFJSP. Firstly, we establish a mathematical model for the DAFJSP with the goal of minimizing the total cost and tardiness. Secondly, based on the problem characteristics, a novel multidimensional coding method is proposed. Thirdly, for enhancing the exploitation ability and operational efficiency of the algorithm, two mutation operators and a similarity coefficient are designed to achieve the dynamic mutation within the EDA framework. Then, considering both the characteristics of the problem and the two objectives, five neighborhood structures that satisfy the cooperative search strategies are designed. Finally, comparison experiments between HEDA-DEV and the selected efficient

![img-1.jpeg](img-1.jpeg)

Fig. 2. The framework of the proposed HEDA-DEV.
algorithms are carried out to verify the efficiency of HEDA-DEV.
The rest of the paper is structured as follows: The DAFJSP is described in Section 2. Section 3 proposes a HEDA-DEV to solve the DAFJSP. Section 4 gives the algorithm comparison experiment and the result analysis. Finally, the study is summarized, and future research is prospected in Section 5.

## 2. The formulation of DAFJSP

### 2.1. Problem description

The main flow chart of DAFJSP is shown in Fig. 1. It consists of the following three stages: production stage, assembly stage, and delivery stage.

At first, the manufacturer received orders from $s$ customers $\left\{S_{1}, S_{2}, \ldots\right.$.
$\left.S_{s}\right\}$ with a total of $q$ products $\left\{P_{1}, P_{2}, \ldots, P_{q}\right\}$. The assembly structure of the products is the single-layer tree structure and they are assembled from $n$ jobs $\left\{J_{1}, J_{2}, \ldots, J_{n}\right\}$. All jobs need to be assigned to each processing factory before starting processing. In the production stage, each processing factory is a regular FJSP. A job $J_{i}$ consists of a series of operations $\left\{O_{i 1}, O_{i 2}, \ldots, O_{i k}\right\}$ that need to be processed in a certain sequence on the available machines. In the assembly stage, each assembly factory can be
considered as a single-machine factory. A product can only be assembled when all of its jobs are finished in the production factory and transported to the assembly factory. In the delivery stage, the finished products will be delivered to the corresponding customers.

In addition, according to the characteristics of DAFJSP, the following assumptions should be made.

1) Each job/product can be assigned to only one available processing/ assembly factory.
2) Job/product shall not be transferred between factories during processing/assembly.
3) Once the job starts processing, it cannot be interrupted until the end of the process.
4) One job can only be processed on one machine simultaneously, and one machine can only process one job at a time.
5) Buffer capacity is infinite, and machine start time is not considered.

The notations employed in the paper are displayed in Table 1.

### 2.2. Mathematical formulation

The mathematical model of DAFJSP is presented as follows.
$\min \quad C=\sum_{i=1}^{n} \sum_{k=1}^{N} \sum_{t=1}^{T} \sum_{j=1}^{m} t_{d c j}^{p s} \times C_{d c j}^{p t} \times X_{d c j}+\sum_{i=1}^{T} \sum_{i=1}^{n} \sum_{i=1}^{n} \sum_{k=1}^{q} t_{t o}^{p t} \times C_{t i}^{p t} \times Y_{i t} \times Z_{t c} \times W_{i t}+$ $\sum_{k=1}^{q} \sum_{t=1}^{T} t_{t c}^{p_{k}} \times C_{t c}^{p_{k}} \times Z_{t c}+\sum_{k=1}^{q} \sum_{d=1}^{1} \sum_{c=1}^{c} t_{d c c}^{p_{k}} \times C_{c d}^{p_{k}} \times Z_{t c} \times V_{b d}$

![img-4.jpeg](img-4.jpeg)

Fig. 3. An example of chromosome.
![img-3.jpeg](img-3.jpeg)

Fig. 4. An example of factory internal scheduling.
![img-4.jpeg](img-4.jpeg)

Fig. 5. An example of DE/rand/1.
$\min T D=\sum_{h=1}^{q} \max \left\{T_{h}-D_{h}, 0\right\}$
$s . t$
$S_{d e j}-S_{(k-1) p}-t_{(k-1) p}^{p p} \geq M \times\left(X_{d e j}+X_{(k-1) p}-2\right), \forall i, k>1, j, p, r$
$S_{d e j}-S_{h g e j}-t_{h g e j}^{p p} \geq M \times\left(X_{d e j}+X_{h g e j}+H_{d d e g}-3\right), \forall k \in\left[1, O_{i}\right], g \in\left[1, O_{h}\right], i$
$\neq h, j, r$
$H_{d d e g}+H_{h g h} \geq 1+M \times\left(X_{d e j}+X_{h g e j}-2\right), \forall k \in\left[1, O_{i}\right], g \in\left[1, O_{h}\right], i \neq h, j, r$
(2) $\quad H_{d d e g}+H_{h g h} \leq 1-M \times\left(X_{d e j}+X_{h g e j}-2\right), \forall k \in\left[1, O_{i}\right], g \in\left[1, O_{h}\right], i \neq h, j, r$
$s . t$
$S_{d e j}-S_{(k-1) p}-t_{(k-1) p}^{p p} \geq M \times\left(X_{d e j}+X_{(k-1) p}-2\right), \forall i, k>1, j, p, r$
$S_{d e j}-S_{h g e j}-t_{h g e j}^{p p} \geq M \times\left(X_{d e j}+X_{h g e j}+H_{d d e g}-3\right), \forall k \in\left[1, O_{i}\right], g \in\left[1, O_{h}\right], i$
$\neq h, j, r$
$H_{d d e g}+H_{h g h} \geq 1+M \times\left(X_{d e j}+X_{h g e j}-2\right), \forall k \in\left[1, O_{i}\right], g \in\left[1, O_{h}\right], i \neq h, j, r$


Fig. 6. An example of crossover.
![img-5.jpeg](img-5.jpeg)

Fig. 7. Neighborhood structure 1.

Table 2
Details of the example.

$S_{t e}-S_{t h / t j}-t_{t h / t}^{t h}-t_{t e}^{t t} \geq M \times\left(V_{t e}+Z_{t e}+W_{t h}+X_{t h / t j}-4\right), \forall b, c, i, r, j$
$S_{t e}-S_{e c}-t_{t c}^{P A} \geq M \times\left(Z_{t e}+Z_{e c}+H_{t e c}-3\right), \forall b, e, c, b \neq e$
$H_{t e c}+H_{c b c} \geq 1+M \times\left(Z_{t e}+Z_{e c}-2\right), \forall b, e, c, b \neq e$
$H_{t e c}+H_{c b c} \leq 1-M \times\left(Z_{t e}+Z_{e c}-2\right), \forall b, e, c, b \neq e$
$T_{b}=\sum_{c=1}^{n}\left(S_{t e}+t_{t e}^{P A}\right) \times Z_{t e}+\sum_{d=1}^{n} \sum_{c=1}^{n} t_{t d e}^{P A} \times Z_{t e} \times V_{b d}, \forall b$
Equation (1) and equation (2) are two objective functions of the DAFJSP. Equation (1) is designed to minimize the total cost, including the total processing cost of all jobs, the cost of transportation between
the processing and assembly factories, the total assembly cost of all products, and the cost of transportation between the assembly factories and the customers. Equation (2) is formulated to minimize the total tardiness. Equation (3) ensures the job can only be processed according to its process route. Equation (4) guarantees that a machine can only process one job simultaneously. Equations (5) and (6) limit the processing sequence of the different jobs. Equations (7) and (8) limit one job/product can only be assigned to one processing/assembly factory. Equation (9) limits a job to be processed on only one machine at a time. Equation (10) guarantees that the assembly start time for each product is behind the arrival time of all jobs for this product at the assembly factory. Equation (11) guarantees that an assembly factory can only assemble one product simultaneously. Equations (12) and (13) limit the assembly sequence of the different products. Equation (14) calculates the arrival time of the product.

![img-6.jpeg](img-6.jpeg)

Fig. 8. Neighborhood structure 2.

Table 3
The parameters of Test Set 1.
Table 4
The parameters of Test Set 2.

Table 5
The parameter value and their levels.
## 3. Proposed HEDA-DEV for DAFJSP

### 3.1. Framework of HEDA-DEV

The framework of the HEDA-DEV is shown in Fig. 2. The detailed steps of the HEDA-DEV are as follows.

Step 1. Input the problem data, such as the number of jobs and factories, processing and assembly time, processing and assembly cost, etc. Set the parameters of the DAFJSP, such as the size of population, the learning rate of probability matrices, the mutation and crossover probability, etc. The details are in Section 4.1.

Step 2. Initialize the probability model. It is initialized with uniform

Table 6
Orthogonal array and Response values.

distribution. The details are in Section 3.3.1.
Step 3. Generate populations by sampling probability matrices and the generation method. After sampling the probability matrix, we can get the factory assignment scheme of the jobs and products, and then the detailed operation scheduling sequence in the factory can be obtained through the population generation method. For details, see Sections 3.3 and 3.4 .

Step 4. Evaluate and rank. Evaluate the total cost and tardiness of the population, and record the rank of each individual after non-dominance sorting.

Step 5. Dynamic mutate. Calculate the similarity coefficient of the probability matrices between the two successive generations. Infer the stage of the algorithm through the similarity coefficient to choose different mutation operations. The details are shown in Section 3.4.

Step 6. Crossover. The new individual can be obtained by exchanging information between the mutated individual and the original individual. The details are shown in Section 3.5.

Step 7. Evaluate and rank. Make a new non-dominated sorting of the population after the dynamic mutate and crossover.

Step 8. Local search. Four targeted neighborhood operators and a random operator are designed, which can work together according to a search strategy. Repeat the procedure until the stop condition is met.

Step 9. Save the Pareto. If gen $\leq G$, go to step 10. Otherwise, set gen $=$ gen +1 and update the probability matrices through the superior individuals. Then, return to the step 3.

Step 10. Output the Pareto Set.

### 3.2. Multi-dimensional coding method

The DAFJSP contains three sub-problems, including factory assignment, machine selection, and operations scheduling. Therefore, we design a new multi-dimensional coding method, which is composed of two parts according to the manufacturing stage. The first part is job processing, and the second part is product assembly. Assuming that there are nine jobs, three processing factories, and two assembly factories, a feasible solution is shown in Fig. 3.

In Fig. 3, $v_{1}, v_{2}$, and $v_{3}$ represent the sequence of operations and machines in processing factories 1,2 , and 3 respectively. In the first part

Table 7
Means response table for each parameter.

![img-7.jpeg](img-7.jpeg)

Fig. 9. Factor level trend for MK07 and LR5.

Table 8
Parameter setting of algorithms.
Table 9
Pareto solution for CPLEX and HEDA-DEV.

of $v_{I}$, the number corresponds to the job index, i.e., jobs 3,5 , and 9 are allocated to factory 1 . The occurrence sequence of the job represents the sequence of operations. For example, the first " 5 " refers to the first operation of job $5\left(O_{51}\right)$, and the second " 5 " refers to the $O_{52}$. The second part of $v_{I}$ is the list of machines, which corresponds to the operations in the first part one by one. For example, the first " 1 " of the Machine list corresponds to $O_{51}$ in the first part, indicating that $O_{51}$ is processed on machine $M_{I}$. In addition, $a_{I}$ and $a_{2}$ represent the products allocated to assembly factories 1 and 2, respectively. The products " $P_{2}$ " and " $P_{3}$ " are allocated to assembly factory 1 , and products " 1 " and " 4 " are allocated to assembly factory 2. Take products " $P_{1}$ " and " $P_{2}$ " for example, the subproducts of " $P_{1}$ " are jobs 5 and 9 , and the sub-products of " $P_{2}$ " are jobs 3 , 1 , and 6 .

In addition, it is very hard to guarantee a high quality of the initial population by random initialization. Therefore, we design two heuristic rules which act simultaneously to improve the quality of the initial population. Meanwhile, in consideration of maintaining the diversity of
the population, the following rules affect only $50 \%$ of randomly selected individuals.

## (1) Machine adjustment rule

According to the optimization goal, this paper generates individuals equally according to two strategies: for $50 \%$ of individuals, traverse the list of available machines in the factory, and give priority to the shortest processing time. If the machine is not the only one, choose the machine with the lowest processing cost. For the remaining $50 \%$ of individuals, the lowest processing cost is given priority, and the machine with the shortest processing time should be chosen when the machine is not unique.

## (2) Factory assignment adjustment rule

Selecting the nearest assembly factory closest to the customer will reduce the transportation time and the total tardiness. After the productassembly factory assignment is obtained by sampling probability matrix $\sigma$, it is adjusted and assigned to the nearest assembly factory according to the customer's location where the product is to be sent.

### 3.3. Probability model and updating mechanism

The probability model and its updating mechanism are the core steps of EDA (Wang et al., 2013a). Two matrixes are used as probability model in this paper: the probability matrix $\rho$ which represents the matching

Table 10
The IGD results of HEDA-DEV and its two variants on each instance.

Table 11
The HV results of HEDA-DEV and its two variants on each instance.

Table 12
Wilcoxon Signed-Rank Test results of HEDA-DEV and its two variants on IGD.

degree between jobs and processing factories; the probability matrix $\boldsymbol{\sigma}$ which represents the matching degree between product and assembly factory.

### 3.3.1. Initialization and sampling method

Initialize the probability matrices $\rho$ and $\sigma$ with a uniform distribution, as shown in Equations (15) and (16). The element $\rho_{i, j}(g)$ in probability matrix $\rho$ denotes the probability that job $i$ is allocated to processing factory $j$ in the $g$-th iteration. Similarly, the element $\sigma_{i, j}(g)$ in probability matrix $\sigma$ indicates the probability that product $i$ is allocated to assembly factory $j$ in the $g$-th iteration.
$\rho_{i, j}(0)=\frac{1}{f} \forall i=1,2, \ldots, n ; \forall j=1,2, \ldots, f$
$\sigma_{i, j}(0)=\frac{1}{A} \forall i=1,2, \ldots, q ; \forall j=1,2, \ldots, A$
In the subsequent iteration process, the algorithm generates new individuals by sampling probability matrices $\rho$ and $\sigma$. Specifically, the sampling process is similar to roulette selection. Taking probability matrix $\rho$ as an example, each row of the matrix is calculated by Equation (17).

Table 13
Wilcoxon Signed-Rank Test results of HEDA-DEV and its two variants on HV.

Table 14
The comparative results of the total cost.

$\operatorname{prob} . \rho_{i j}(g)=\frac{\sum_{i=1}^{d} \rho_{i v}(g)}{\sum_{i=1}^{d} \rho_{i v}(g)} \cdot \forall i=1,2, \ldots, n ; \forall j=1,2, \ldots, f$
where $\operatorname{prob} . \rho_{i j}(g)$ indicates the selection probability of the job $i$ assigned to the processing factory $j$ in the $g$-th iteration.

Then, a random number $δ$ between 0 and 1 is generated to compare with $\operatorname{prob} . \rho_{i j}(g)$. If $\delta \leq \operatorname{prob} . \rho_{i 1}(g), \operatorname{job} i$ is assigned to processing factory " 1 ". Otherwise, if $\operatorname{prob} . \rho_{i j-1}(g) \leq \delta \leq \operatorname{prob} . \rho_{i j}(g), \operatorname{job} i$ is assigned to processing factory $j$.

### 3.3.2. Updating mechanism of the probability model

To make the probability model properly represent the evolution trend of the population, the $\eta$ superior individuals in the population are selected in each iteration to update the probability model. The superior individuals are selected as follows.

First, a non-dominant sorting of the population is conducted to determine the level of each individual. Rank (1) is Pareto solutions. If the number of Pareto solutions is larger or equal to $\eta$, then the first $\eta$ individuals in Pareto solutions are selected. If the number of Pareto solutions is smaller than $\eta$, the individuals in rank (2) or lower level are supplemented in turn.

Table 15
The comparative results of the total tardiness.

![img-8.jpeg](img-8.jpeg)

Fig. 10. Pareto solution set of six algorithms on Test Set 1.

To be determined by the superior individuals, the probability model is updated by means of incremental learning, as in Equations (18)-(20): $\eta=\mu$-Popsize
$\rho_{i, j}(g+1)=(1-\alpha) \rho_{i, j}(g)+\frac{\alpha}{\eta} \sum_{i=1}^{n} I_{i, j}^{c}(g), \forall i, j$
$\sigma_{i, j}(g+1)=(1-\beta) \sigma_{i, j}(g)+\frac{\beta}{\eta} \sum_{i=1}^{n} L_{i, j}^{c}(g), \forall i, j$
In the above formulas, $\mu \in(0,1)$, Popsize is the population size, $\alpha, \beta \in$ $(0,1)$ are the learning rate, $I_{i, j}^{c}(g)$ and $L_{i, j}^{c}(g)$ are respectively the indicative variables corresponding to the z-th elite individual in the g-th iteration of the algorithm, which are defined as following Equations (21)

![img-9.jpeg](img-9.jpeg)

Fig. 11. Pareto solution set of six algorithms on Test Set 2.

Table 16
The IGD results of six algorithms on each instance.

and (22):
$F_{i j}(\mathrm{~g})=\left\{\begin{array}{l}1, \text { if } j \circ b j \text { is assigned to profeccing factory } i \\ 0, \text { otherwise }\end{array}\right.$
$L_{i j}^{*}(\mathrm{~g})=\left\{\begin{array}{l}1, \text { if product } j \text { is assigned to assembly factory } i \\ 0, \text { otherwise }\end{array}\right.$
3.4. Population generation method

After sampling the probability model, we can get the factory assignment scheme for jobs and products, and then we can obtain the detailed operation scheduling sequence in the factory through the factory internal scheduling (FIS).

Table 17
The HV results of six algorithms on each instance.

![img-10.jpeg](img-10.jpeg)

Fig. 12. The box plots of IGD obtained by the six algorithms.

The example in Section 3.2 is used again, i.e., 9 jobs, 3 processing factories, and 2 assembly factories. An example of FIS is given in Fig. 4. First, all the operations are randomly arranged into a sequence vector, and the occurrence sequence of the number represents the operation of the job. Then through sampling probability matrix, we can get the assignment scheme of the job-processing factory. The jobs "2, 3, 9" are allocated to factory $F_{1}$, and the operations of jobs " $2,3,9$ " will be taken out from the vector in sequence. Then we can get the operation scheduling sequence $v 1-O$ in factory $F_{1}$ by putting these numbers together. After assigning machines, the complete operation-machine scheduling sequence can be obtained.

### 3.5. Dynamic mutation strategy

At present, various mutation strategies have been presented, including DE/rand/1 with an outstanding global search capability, and

DE/best/1 with an outstanding local search capability (Wu et al., 2016). According to the characteristics of EDA, we design a similarity coefficient based on the probability matrices $\rho$ and $\sigma$ to judge the stage of the algorithm and then choose the mutation strategy suitable for different stages. In addition, due to the features of the coding scheme, the crossover and mutation only work on the processing part and do not involve the assembly part. The variable neighborhood search contains neighborhood structures specifically for the assembly part, as detailed in Section 3.6.

### 3.5.1. Similarity coefficient

Because the probability matrix of EDA describes the distribution of the populations, we propose a method to compare the similarity of the two generations by calculating the similarity coefficient of the probability matrix between the two generations. Then we infer the stage of the algorithm to choose different mutation operations. The similarity coef-

![img-11.jpeg](img-11.jpeg)

Fig. 13. The box plots of HV obtained by the six algorithms.

Table 18
The significant differences of IGD obtained by Wilcoxon Signed-Rank Test.

ficient similar is calculated as follows:
$\operatorname{similar}_{p}=\left(\sum_{i=1}^{n} \sum_{j=0}^{r}\left|\sigma_{i j}(g)-\rho_{i j}(g-1)\right|\right) / n$
$\operatorname{similar}_{n}=\left(\sum_{i=1}^{n} \sum_{j=0}^{1}\left|\sigma_{i j}(g)-\sigma_{i j}(g-1)\right|\right) / q$
$\operatorname{similar}=\left(\operatorname{similar}_{p}+\operatorname{similar}_{n}\right) / 2$
In the later stage of the algorithm, there should be a strong local search ability to increase the accuracy and convergence speed. As the convergence slows down in the later stage, the probability model tends to be stable gradually and the value of similar will become smaller and smaller. Therefore, the mutation strategy is chosen as below:
$e=\left\{\begin{array}{lr}D E / \operatorname{rand} / 1, & \text { if } \operatorname{rand}(0,1)<\text { similar } \\ D E / \text { best } / 1, & \text { otherwise }\end{array}\right.$

# 3.5.2. Mutation operator 

Step 1. After the non-dominated sorting, an elite individual " $X_{h}$ " and a poor individual " $X_{b}$ " are taken out from the front $50 \%$ and back $50 \%$ of the population respectively, and then take a different individual " $X_{c}$ " randomly.

Step 2. By subtracting the sequence of " $X_{h}$ " from that of " $X_{b}$ ", we can get " $\left(X_{a}-X_{b}\right)$ ", and then we can get $V_{g}$ with " $X_{c}$ " according to Equation (27).

Step 3. The final variant can be obtained by eliminating the negative number in $V_{g}$. This operation process is shown in Equation (28).

Table 19
The significant differences of HV obtained by Wilcoxon Signed-Rank Test.

![img-12.jpeg](img-12.jpeg)

Fig. 14. Gantt Chart of LIO3 instance.
$V_{i j}=\left\{\begin{array}{cl} \left(\left(X_{i i j}-X_{k k}\right)+X_{c j}\right) \% n+1, & \text { rand }<F \\ X_{c l}+1, & \text { rand } \geq F\end{array}\right.$
$V_{i j}=\left\{\begin{array}{cl}V_{i j}, & V_{i j} \geq 0 \\ 0, & V_{i j}<0\end{array}\right.$
The above steps are the operation process of DE/rand/1. The process of DE/best/1 is the same as that of DE/rand/1, except that " $X_{i j}$ " is no longer randomly selected but Pareto solution of population. Among

Equations (24) and (25), subscript $j$ is the $j$-th dimensional element of the individual, rand is a random number, and $F$ is the mutation probability. In Fig. 5, we illustrate a small instance with nine jobs for ease of understanding, assuming that the mutation probability $F$ is 0.5 .

### 3.6. Crossover

In HEDA-DEV, a new individual can be obtained by exchanging information between mutated individuals and original individuals. The

Table 20
Brief information on products and key components.
![img-13.jpeg](img-13.jpeg)

Fig. 15. Pareto solution set of six algorithms on the real case.
example in Section 3.2 is used again, as shown in Fig. 6. Assuming that the crossover probability $C R$ is $0.6, V_{i}$ is the mutation individual obtained from the above mutation operation, and $U_{i}{ }^{\prime}$ can be obtained through the selection of $C R$. Then we carry out the de-duplication operation on $U_{i}{ }^{\prime}$, only the first occurrence gene will be reserved (shown in green color), and the duplicate gene will be deleted. Then randomly select individual $X_{i}$ from the original population. Delete the green part of $X_{i}$ to get $X_{i}{ }^{\prime}$. Finally, the remaining genes of $X_{i}{ }^{\prime}$ are sequentially inserted into $U_{i}{ }^{\prime \prime}$ to generate the final test sequence $U_{i}$.

### 3.7. Multi-neighbor structures and search strategy

In this paper, four targeted neighborhood operators and a random operator are designed, which can work together according to the cooperative search strategy.

### 3.7.1. Neighborhood structures

(1) Reduce maximum tardiness

NS1: Select product $b$ with the largest delay time and locate job $i$ that arrives at the assembly factory the latest among all jobs of product $b$. Give job $i$ priority scheduling within the factory where job $i$ is processed,
thereby speeding up the start of the assembly for product $b$ and possibly reducing the delay time. To explain it more clearly, an example is presented in Fig. 7. Table 2 shows the details of the example. Jobs "1, 2, 3" are assigned to this processing factory and $v$ is the process scheduling scheme. Assume that job " 1 " should be processed firstly. First, determine the position of the last operation of job " 1 ". This position (index) is 10 (blue part in figure). Then we need to cut this gene to the fifth position in the operation sequence (index/2), as well as the machine part. When we execute this neighborhood structure, the completion time for job " 1 " decreases from 67 to 49.

NS2: Select product $b$ with the largest delay time and locate job $i$ that arrives at the assembly factory the latest among all jobs of product $b$, then find processing factory $a$ which has the earliest completion time. If job $i$ is processed in factory $a$, turn to NS1 search; otherwise, transfer job $i$ to factory $a$ and schedule randomly. As shown in Fig. 8, it is still assumed that job " 1 " needs to be transferred and the completion time of processing factory " 2 " is the shortest. First, remove all gene " 1 " and their corresponding machine genes (blue part in figure) from $v_{f}$. Then insert these genes randomly into $v_{2}$ and available machines are randomly selected in the machine sequence.

NS3: Select product $b$ with the largest delay time and re-select the assembly factory closest to its customer.
(2) Reduce total cost

NS4: Select the processing factory with the highest processing cost and find the operation with the highest processing cost. Then traverse all the processing machines in the factory and select the machine with the least processing cost for the operation.
(3) Random Neighborhood Structure

NS5: Select a processing factory at random, and randomly select $20 \%$ of the operations processed by the factory and reselect machines for them.

### 3.7.2. Cooperative search strategy

To fully exploit the potential of the population and improve the efficiency of the search, the object set PSet of neighborhood search is set as follows: all the Pareto solutions (set $S$ ), $10 \%$ of the single objective optimal individuals (set $S_{C_{1}}$, set $S_{T D}$ ). If the individuals belong to the set $S$, we apply all five neighborhood operators sequentially. For individuals in set $S_{C}$, the neighborhood operator NS4 which is designed to reduce total cost and the random neighborhood operator NS5 are applied. For individuals in set $S_{T D}$, the neighborhood operators NS1, NS2, NS3 which are designed to reduce total tardiness and the random neighborhood operator NS5 are applied. By using different neighborhood operators for individuals in different sets, we further optimize the objectives of individuals and find better non-dominated solutions. The pseudo-code for the specific process is as follows.

![img-14.jpeg](img-14.jpeg)

Fig. 16. The box plots of IGD and HV obtained by the six algorithms on the real case.

Table 21
The results of IGD and HV obtained by Wilcoxon Signed-Rank Test.
![img-15.jpeg](img-15.jpeg)

Fig. 17. Gantt Chart of the real case.

Algorithm 1. The presentation of Local Search
input: PSet, gen, n = PSet.size(, $\}$
output: new PSet

1. for $i=1$ to $n$ do
2. for $j=1$ to gen do
3. for $\mathrm{k}=1$ to 5 do
4. if $\operatorname{PSet}[i] \in S$, then
5. Generate $\mathrm{X}^{\prime}$ through Neighborhood structure k
6. if $\mathrm{X}^{\prime}$ is not dominated by PSet[i], then
7. $\operatorname{PSet}[i] \leftarrow \mathrm{X}^{\prime}$
8. end
9. else if $\operatorname{PSet}[i] \in S_{0}$, then
10. if $\mathrm{k}=+4\|\mathrm{k}==5$, then
11. Generate $\mathrm{X}^{\prime}$ through Neighborhood structure k
12. if $\mathrm{X}^{\prime}$ is not dominated by PSet[i], then
13. $\operatorname{PSet}[i] \leftarrow \mathrm{X}^{\prime}$
14. end
15. end
16. else
17. if $\mathrm{k}=+1\|\mathrm{k}==2\|\mathrm{k}==3\|\mathrm{k}==5$, then
18. Generate $\mathrm{X}^{\prime}$ through Neighborhood structure k
19. if $\mathrm{X}^{\prime}$ is not dominated by PSet[i], then
20. $\operatorname{PSet}[i] \leftarrow \mathrm{X}^{\prime}$
21. end
22. end
23. end
24. end
25. end
26.end

## 4. Experimental study

The computational experiments of the algorithms are demonstrated in this section. HEDA-DEV and five other comparison algorithms are carried out in JAVA(JDK1.8) on an Intel Core i5 2.3 GHz PC with 8 GB of RAM. This section is presented according to the following aspects: the determination of test data sets, parameter determination of the algorithms, validation of the mathematical model, ablation experiments, comparison of HEDA-DEV with five other algorithms, and a real case study.

### 4.1. Data sets and evaluating indicator

Since the proposed problem is a new one, there is no benchmark data set in the existing literature. Therefore, two test sets are constructed to prove the performance of the HEDA-DEV for DAFJSP. Test Set 1 is modified from the instance set proposed by Wu et al. (2019). In order to make the test results more convincing, we add five instances of MK11-MK15. The detailed parameters of Test Set 1 are shown in Table 3. The " $10,6,3,2,3,2$ " represents that there are 10 jobs, 6 machines, 3 processing factories, 2 assembly factories, 3 products, and 2 customers in this instance. The values of the other parameters are generated randomly according to their value ranges. Moreover, to further validate the effectiveness of HEDA-DEV for large-scale problems, we expand the number of jobs and machines in benchmark instances proposed by Brandimarte (1993) to construct Test Set 2. The detailed parameters of Test Set 2 are listed in Table 4. Considering the characteristics of the DAFJSP, we add the following parameters: assembly time, transportation time, processing cost, assembly cost, transportation cost, and the due date of products. The values of each parameter are randomly generated from its range.

In addition, the inverted generational distance (IGD) and hypervolume (HV) are used as metrics to evaluate the performance of algorithms. IGD and HV are calculated as shown below:
$I G D=\frac{\sum_{i=0}^{n} \min _{x \in \Omega_{i}} \operatorname{dis}(x, y)}{\left|\Omega^{\prime}\right|}$
$\mathrm{HV}=\cup_{i=1}^{N_{s}} v_{i}$
In Equation (29), $\Omega^{\prime}$ denotes the real Pareto frontier solution set, $\Omega_{i}$ is the calculated Pareto frontier solution set, and dis $(x, y)$ is the Euclidean distance between $x$ to $y$. In Equation (30), $N_{s}$ denotes the number of nondominated solutions obtained by the algorithm, and $v_{i}$ denotes the volume/area formed by the $i$-th solution in the non-dominated solutions with the reference point. Based on the characteristics of the problem, the reference point is set to $(1,1)$.

### 4.2. Parameters setting

The value of the key parameters will influence the performance of the algorithm. The key parameters of the HEDA-DEV are the size of the population: Popsize, the learning rate of the probability matrix $\rho: \alpha$, the learning rate of the probability matrix $\sigma: \beta$. the mutation probability: $F$, the crossover probability: $C R$ and the proportion of superior individuals: $\mu$. To obtain a set of ideal experimental parameters, the Taguchi method (Montgomery, 2005) is used for calibrating the parameters of HEDA-DEV and the other five comparison algorithms. Depending on the number of key parameters described above, the orthogonal experiment is determined as $L_{25}\left(5^{6}\right)$. Different combinations for the orthogonal experiments are listed in Table 5. Considering the difference between the two test sets, the parameter setting experiment is carried out for Test Set 1 and Test Set 2, respectively. The Taguchi method is performed on instance MK07 and instance LI05. All parameter combinations are performed 20 times on HEDA-DEV, and the average of the obtained IGD is used for the average response variable (ARV). Table 6 lists the orthogonal arrays and the obtained results. Table 7 shows the average responses for each parameter. The factor level trend for MK07 and LI05 is presented in Fig. 9.

The Popsize is the most significant parameter for both MK07 and LI05. It is also clear from Fig. 9 that the average value of IGD decreases obviously with the increase of Popsize. The reason is that a large Popsize can improve the population variety. As for $\mu$, a small value will lead to few elite populations participating in updating the probability model, while a large value will lead to updating the probability model with some poor individuals. For the learning rate $\alpha$ and $\beta$, the larger the value is, the faster the convergence speed will be. However, if the value is too large, it will lead to premature convergence. As for $F$ and $C R$, appropriate values can balance the population diversity and convergence rate.

According to the trend plots of the factor levels in Fig. 9, the parameter values of HEDA-DEV for the two test sets can be obtained. In the same way, we determined the parameters of the five comparison algorithms. The parameter settings of the six algorithms are listed in Table 8. The number of iterations is set to 300 for Test Set 1 and 500 for Test Set 2.

### 4.3. Validation of the proposed model

The software CPLEX 12.9.0 is used to verify the correctness of the proposed model. First, the nonlinear variables are linearized. Then, to implement multi-objective optimization for DAFJSP, the $\varepsilon$-constraint method (Mavrotas, 2009) is adopted for the transformed linear model. Finally, since the true Pareto front cannot be obtained within 4 h for solving instance MK01 (10_6_3_2_3_2), a tiny-scale instance 6_4_2_2_3_3_2 is generated for model validation. Table 9 shows the comparison result of CPLEX and HEDA-DEV. The result shows that the true Pareto front obtained by CPLEX verifies the correctness of the proposed model. Moreover, the Pareto front obtained by HEDA-DEV is close to the true Pareto front.

### 4.4. Ablation experiment

In this section, we conduct ablation experiments to evaluate the

contribution of DE-based evolutionary operators and VNS to HEDADEV. To validate the effectiveness of the two proposed components, two variants are designed, i.e., HEDA-VNS which removes both the dynamic mutation strategy and crossover from HEDA-DEV, and HEDADE which eliminates the variable neighborhood search from HEDA-DEV. These algorithms are run 20 times on all instances with the same parameter settings. The average (Avg), standard deviation (SD), and median (Med) of IGD and HV obtained by three algorithms on each instance are in Tables 10 and 11, respectively.

To further check whether statistically significant differences existed between the experimental results, the Wilcoxon Signed-Rank Test is used to analyze the statistical significance of the HEDA-DEV over the two variants. The results of the Wilcoxon Signed-Rank Test for IGD and HV are given in Tables 12 and 13, respectively. If the P-Value is less than 0.05 , we can assume that the results are significantly different. From Tables 12 and 13, we can conclude that HEDA-DEV significantly outperforms the two variants, which demonstrates the effectiveness of the DE-based evolutionary operators and VNS.

### 4.5. Comparisons of HEDA-DEV with five other algorithms

In order to further validate the performance of the HEDA-DEV for DAFJSP, five algorithms: Estimation of Distribution Algorithm (EDA) (Wang et al., 2013b), Differential Evolution (DE) (Cao et al., 2017), Artificial Bee Colony (ABC) (Li et al., 2011), NSGA-II (Wang et al., 2020) and MOEA/D (Li and Liu, 2018) are employed as comparison. The six algorithms are run 10 times independently on all sets. The comparative results of the total cost and total tardiness are listed in Table 14 and Table 15, respectively. The total cost and total tardiness obtained by HEDA-DEV always have the smallest average value and minimum value in all instances.

Furthermore, the Pareto front of the six algorithms obtained on the two test sets are illustrated in Fig. 10 and Fig. 11, respectively. It can be seen that the quality of the solution obtained by HEDA-DEV obviously outperforms the other algorithms.

Table 16 and Table 17 list the Avg and Med of IGD and HV obtained by six algorithms, respectively. The HEDA-DEV obtains the minimum Avg and Med of IGD and the maximum Avg and Med of HV among all instances, which demonstrates the effectiveness of HEDA-DEV compared to other algorithms. Taking MK01-Mk03 and LI01-LI03 as examples, Fig. 12 and Fig. 13 show the box plots of IGD and HV for the six algorithms, respectively.

In addition, the Wilcoxon Signed-Rank Test is used to test whether the difference between HEDA-DEV and other algorithms is significant. The results are listed in Table 18 and Table 19, respectively. It can be seen that HEDA-DEV statistically outperforms the other five algorithms in all instances. Moreover, to facilitate the understanding of the problem, the Gantt chart of the LI03 instance is shown in Fig. 14. The conclusion can be drawn that the HEDA-DEV is a more effective method for solving DAFJSP.

### 4.6. A real case study

To further validate the effectiveness of our proposed algorithm, an interview is conducted with a decision-maker from Tianjin Cement Industry Design \& Research Institute Co., Ltd, a cement equipment company located in Tianjin, China. This company primarily specializes in EPC (Engineering, Procurement, and Construction) projects and equipment design. It operates two mainframe manufacturing and assembly plants, with one located in Tianjin, China, and the other located in Tangshan, a city in Hebei Province, China. After receiving customer orders, they will be assigned to the two enterprises. To ensure the successful execution of projects and meet customer demands, these two enterprises may choose to outsource specific manufacturing tasks to external manufacturing companies. Subsequently, they will bring the manufactured components back to their own factory for the assembly
process. This scenario closely aligns with the research background discussed in the article. Therefore, we have considered a real-life case study from this enterprise, which involves five different products. The brief product information is presented in Table 20. And the detailed dataset can be downloaded from https://github.com/21xiaohui/Case-data.

To verify the effectiveness of HEDA-DEV, six algorithms are run 10 times on the real case. The Pareto front of the six algorithms obtained is illustrated in Fig. 15.

It can be seen from Fig. 15 that HEDA-DEV has a better solution than the other five algorithms. Furthermore, Fig. 16 shows the box plots of IGD and HV for the six algorithms in the real case.

As can be seen from Fig. 16, HEDA-DEV yields the best IGD and HV. In addition, the Wilcoxon Signed-Rank test is used to investigate whether the differences in IGD and HV between HEDA-DEV and other algorithms are significant. The result is displayed in Table 21. All PValues are less than 0.05 and it can be concluded that there is a significant difference between the results of IGD and HV.

To facilitate a better understanding of the problem, the Gantt chart of the real case obtained by HEDA-DEV is shown in Fig. 17. By solving the real case obtained from the survey, we further validate the effectiveness of the proposed HEDA-DEV.

## 5. Conclusion and future work

This paper proposes a hybrid distribution estimation optimization algorithm based on DE operator and VNS for solving the DAFJSP with the goal of minimizing the total cost and tardiness simultaneously. And the efficient performance of HEDA-DEV is verified through comparison experiments with five efficient algorithms on two test sets. The main work of this paper are as below: (1) a multi-objective optimization model for the DAFJSP is established; (2) a novel multidimensional coding method is proposed, which is consistent with the characteristics of the problem; (3) two mutation operators and a similarity coefficient based on probability matrix are designed to implement the dynamic mutation; (4) considering both the characteristics of the problem and the objective features, the multiple neighborhood structures which satisfy the cooperative search strategies are developed.

In future research, we will consider the unexpected situations in actual production, such as machine failure and transportation accident, so as to be closer to reality. In addition, we are ready to consider the integration of batch scheduling into DAFJSP.

## CRediT authorship contribution statement

Baigang Du: Writing - review \& editing, Supervision, Investigation, Funding acquisition. Shuai Han: Writing - original draft, Methodology. Jun Guo: Writing - review \& editing, Validation, Funding acquisition. Yibing Li: Supervision.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China (No. 51705386); China Scholarship Council (No. 2016 06955091).
