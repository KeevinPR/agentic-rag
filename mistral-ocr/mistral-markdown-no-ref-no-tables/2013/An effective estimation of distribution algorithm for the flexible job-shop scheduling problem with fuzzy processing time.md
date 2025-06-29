# An effective estimation of distribution algorithm for the flexible job-shop scheduling problem with fuzzy processing time 

Shengyao Wang*, Ling Wang, Ye Xu and Min Liu<br>Tsinghua National Laboratory for Information Science and Technology (TNList), Department of Automation, Tsinghua University, Beijing 100084, China

(Received 14 April 2012; final version received 25 December 2012)


#### Abstract

Considering the fuzzy nature of the data in real-world scheduling, an effective estimation of distribution algorithm (EDA) is proposed to solve the flexible job-shop scheduling problem with fuzzy processing time. A probability model is presented to describe the probability distribution of the solution space. A mechanism is provided to update the probability model with the elite individuals. By sampling the probability model, new individuals can be generated among the search region with promising solutions. Moreover, a left-shift scheme is employed for improving schedule solution when idle time exists on the machine. In addition, some fuzzy number operations are used to calculate scheduling objective value. The influence of parameter setting is investigated based on the Taguchi method of design of experiment, and a suitable parameter setting is suggested. Numerical testing results and comparisons with some existing algorithms are provided, which demonstrate the effectiveness of the proposed EDA.


Keywords: flexible job-shop scheduling problem; fuzzy processing time; fuzzy completion time; estimation of distribution algorithm; probability model; design of experiment

## Notation

$n$ : the number of the jobs to be processed;
$m$ : the number of the total machines;
$J=\left\{J_{1}, J_{2}, \ldots, J_{n}\right\}$ : the set of $n$ jobs to be processed;
$M=\left\{M_{1}, M_{2}, \ldots, M_{m}\right\}$ : the set of $m$ machines;
$O_{i, j}$ : the $j$ th operation of $J_{i}$;
$n_{i}$ : the number of the operations of $J_{j}$;
$m_{i, j}$ : the number of the capable machines for $O_{i, j}$;
$T_{O}$ : the number of total operations of all the $n$ jobs;
$t_{i, j, k}=\left(t_{i, j, k}^{1}, t_{i, j, k}^{2}, t_{i, j, k}^{3}\right)$ : the fuzzy processing time of $O_{i, j}$ on machine $M_{k}$;
$C_{i, j}=\left(C_{i, j}^{1}, C_{i, j}^{2}, C_{i, j}^{3}\right)$ : the fuzzy completion time of $O_{i, j}$;
$C_{\text {max }}$ : the maximum fuzzy completion time of a schedule;
$S_{i, j}$ : the fuzzy starting time of $O_{i, j}$;
$t_{k}^{S}$ : the beginning time of a time interval;
$t_{k}^{E}$ : the ending time of a time interval;
$P$ : the population size;
$S P$ : the size of the superior population;
$A_{1}$ : the operation probability matrix;
$A_{2}$ : the machine probability matrix;
$p_{i j}(l)$ : the element of $A_{1}$ at generation $l$;
$q_{i j k}(l)$ : the element of $A_{2}$ at generation $l$;
$\alpha$ : the learning rate of $A_{1}$;
$\beta$ : the learning rate of $A_{2}$;
$\eta$ : the percentage of the superior population from the whole population.

[^0]
[^0]:    *Corresponding author. Email: wangshengyao@tsinghua.org.cn

# 1. Introduction 

The flexible job-shop scheduling problem (FJSP) is an extension of the classical job-shop scheduling problem (JSP) for the flexible manufacturing systems, which is very close to the real manufacturing situation. In the FJSP, some machines can perform more than one type of operations. The FJSP consists of two sub-problems: the routing sub-problem that assigns each operation to a machine among a set of capable machines, and the scheduling sub-problem that sequences the assigned operations on all the machines to obtain a feasible schedule. The FJSP is more difficult to solve than the classical JSP since it needs to determine the assignment of operations to the related machines.

The first work to address the FJSP was by Bruker and Schlie (1990), where a polynomial algorithm was presented for the problem with only two jobs and identical machines. Later, Brandimarte (1993) presented a hybrid tabu search (TS) algorithm with some existing dispatching rules. Dauzere-Peres and Paulli (1997) also presented a TS algorithm based on an integrated approach, which was improved by two developed neighbourhood functions (Mastrolilli and Gambardella 2000) in terms of computational time and solution quality. Gao, Sun, and Gen (2008) designed a genetic algorithm (GA) hybridising with variable neighbourhood search (VNS), and Pezzella, Morganti, and Ciaschetti (2008) developed a GA integrating different strategies. Besides, Amiri et al. (2010) developed a VNS algorithm based on six neighbourhood structures, Yazdani, Amiri, and Zandieh (2010) developed a parallel VNS algorithm, and Xing et al. (2010) developed a knowledge-based ant colony optimisation algorithm. Recently, a bi-population based estimation of distribution algorithm (BEDA) (Wang et al. 2012c) and a novel artificial bee colony (ABC) algorithm (Wang et al. 2012d) were presented to solve the FJSP. As for the multi-objective flexible job-shop scheduling (MFJSP), relevant algorithms include heuristic algorithm (Wang, Zhou, and Xi 2008), GA (Frutos, Olivera, and Tohme 2010; Wang et al. 2010), genetic programming (Tay and Ho 2008), TS algorithm (Li, Pan, and Liang 2010), particle swarm optimisation (PSO) (Xia and Wu 2005; Moslehi and Mahnam 2011), and ABC algorithm (Li, Pan, and Gao 2011; Wang et al. 2012a).

In the literature, it often assumes that the processing time and completion time are deterministic values. In real-world scheduling, however, the processing time of an operation cannot be known precisely and the completion time can be obtained ambiguously. Thus, it may be more appropriate to consider fuzzy processing time and fuzzy completion time (Sakawa and Kubota 2000). The fuzzy job-shop scheduling problem (fJSP) extends the JSP by considering the processing time or the due-date to be fuzzy variable. Relevant results include following. Sakawa and Mori (1999) presented a GA to maximise the minimum agreement index. Then Sakawa and Kubota (2000) improved the GA (Sakawa and Mori 1999) to maximise the minimum agreement index, to maximise the average agreement index, and to minimise the maximum fuzzy completion time. Lei (2008) designed a Pareto archive PSO for the multi-objective fJSP to obtain a set of Pareto optimal solutions. González-Rodríguez, Vela, and Puente (2010) presented a GA to search possible active schedules. Recently, Hu, Yin, and Li (2011) presented a modified differential evolution (DE) algorithm for the fJSP, and Lei (2010b, 2011) presented a random key GA and a swarm-based neighbourhood search with availability constraints.

Introducing fuzzy constraints to the FJSP makes the problem much closer to the real applications, such as the textile industry, automobile assembly and semiconductor manufacturing. The FJSP with fuzzy processing time is regarded as the combination of the FJSP and the fJSP, namely fuzzy flexible job-shop scheduling problem (fFJSP). Lei (2010a) presented an efficient decomposition-integration genetic algorithm (DIGA), in which the main population was decomposed as two sub-populations that evolved independently and the new main population was formed by sub-population integration. Recently, Lei (2012) developed an effective co-evolutionary genetic algorithm (CGA) to minimise the fuzzy makespan. The study on this topic is still in its infancy, and it is important to develop novel algorithms for the problem.

As a novel kind of evolutionary algorithm based on statistical learning, estimation of distribution algorithm (EDA) (Larranaga and Lozano 2002) has gained increasing studies and wide applications during recent years. Due to different kinds of the relationships among variables, the EDA has different models. Accordingly, it can be classified as univariate model, bivariate model or multivariate model. Univariate model assumes that the variables are independent with each other, e.g. the population-based incremental learning (Baluja 1994), the univariate marginal distribution algorithm (Mäuhlenbein and Paass 1996) and the compact GA (Harik, Lobo, and Goldberg 1998). Bivariate model assumes that each variable is associated with another one, e.g. the mutual information maximisation for input clustering (De Bonet, Isbell, and Viola 1997), the combining optimisers with mutual information trees (Baluja and Davies 1997) and the bivariate marginal distribution algorithm (Pelikan and Mühlenbein 1999). Multivariate model considers the relationship between all the variables, e.g. the factorised distribution algorithms (Mühlenbein and Mahnig 1999), the extended compact GA (Harik 1999) and the Bayesian optimisation algorithm (Pelikan, Goldberg, and Cantú-Paz 1999). For more details about the EDA, please refer Larranaga and Lozano (2002).

The EDA has been applied to a variety of academic and application problems, such as feature selection (Saeys et al. 2003), inexact graph matching (Cesar et al. 2005), software testing (Sagama and Lozano 2005), flow-shop scheduling

(Jarboui, Eddaly, and Siarry 2009), resource-constrained project scheduling (Wang and Fang 2012), multi-dimensional knapsack problem (Wang, Wang, and Fang 2012b), and so on. However, to the best of our knowledge, there is no research work about the EDA for solving the fFJSP. Inspired by the successful applications of the EDA, we shall propose an effective EDA to enrich the tool-kit for solving the fFJSP. To be specific, we build a probability model to generate population and provide a mechanism to update the model, and we employ a left-shift scheme to improve solutions. The influence of parameter setting is investigated based on the design of experiment. Numerical testing results and comparisons are provided to show the effectiveness of the proposed EDA.

The remainder of the paper is organised as follows: In Section 2, the fFJSP is described, and some operations on fuzzy processing time are introduced. In Section 3, the basic EDA is described briefly. Then, in Section 4 the EDA for the fFJSP is proposed in details. The influence of parameter setting is investigated and computational results and comparisons are provided in Section 5. Finally we end the paper with some conclusions and future work in Section 6.

# 2. Flexible job-shop scheduling problem with fuzzy processing time 

### 2.1 Problem description

The FJSP with fuzzy processing time (fFJSP) is commonly defined as follows. There are a set of $n$ jobs $J=\left\{J_{1}, J_{2}, \ldots, J_{n}\right\}$ to be processed on $m$ machines $M=\left\{M_{1}, M_{2}, \ldots, M_{m}\right\}$. Each job $J_{i}$ consists of a sequence of $n_{i}$ operations $\left\{O_{i, j}, j=1,2, \ldots, n_{i}\right\}$. Each routing has to be determined to complete a job. The execution of $O_{i, j}$ requires one machine out of a set of $m_{i, j}$ capable machines out of $M$. The processing time of $O_{i, j}$ on machine $M_{k}$ is represented as a triangular fuzzy number (TFN) $t_{i, j, k}=\left(t_{i, j, k}^{1}, t_{i, j, k}^{2}, t_{i, j, k}^{3}\right)$, where $t_{i, j, k}^{1}$ is the best processing time, $t_{i, j, k}^{2}$ is the most probable processing time and $t_{i, j, k}^{3}$ is the worst processing time. Similarly, the fuzzy completion time of $O_{i, j}$ is represented as a TFN $C_{i, j}=\left(C_{i, j}^{1}, C_{i, j}^{2}, C_{i, j}^{3}\right)$, where $C_{i, j}^{1}$ is the best completion time, $C_{i, j}^{2}$ is the most probable completion time and $C_{i, j}^{3}$ is the worst completion time.

Typically, it assumes that:

- All the jobs are independent and available to be processed at the initial time.
- One machine can process only one operation and one job can be processed on only one machine at a time.
- The releasing time of all machines is not considered or set as 0 .
- The transfer time between different machines is included in the processing time and the buffer size is infinite.
- Once an operation is started, it cannot be interrupted (Lei 2010a; 2012).

The fFJSP is to determine both the assignment of machines and the sequence of operations on all the machines to minimise the maximum fuzzy completion time, $C_{\max }=\max _{i=1,2, \ldots n} C_{i, j}$.

### 2.2 Operations on fuzzy processing time

In fuzzy context, it requires to define certain fuzzy number operations (Bortolan and Degani 1985) to produce a schedule. These operations include addition operation, max operation of two fuzzy numbers and the ranking method of fuzzy numbers. Addition operation is used to calculate the fuzzy completion time of operation. Max operation is used to determine the fuzzy beginning time of operation and the ranking method is to compare the maximum fuzzy completion time.

For two TFNs $X=\left(x_{1}, x_{2}, x_{3}\right)$ and $Y=\left(y_{1}, y_{2}, y_{3}\right)$, their addition is shown by the following formula: $X+Y=\left(x_{1}+y_{1}, x_{2}+y_{2}, x_{3}+y_{3}\right)$.

In this paper, the following criterion (Sakawa and Kubota 2000) is adopted to rank fuzzy numbers to build a feasible schedule.

Step 1: The greatest number $Z_{1}(X)=\frac{x_{1}+2 x_{2}+x_{3}}{4}$ will be chosen as the first criterion to rank two TFNs.
Step 2: If two TFNs have the same $Z_{1}, Z_{2}(X)=x_{2}$ is used as a second criterion.
Step 3: If $Z_{1}$ and $Z_{2}$ are identical, $Z_{3}(X)=x_{3}-x_{1}$ will be chosen as a third criterion.
Compared with the criterion by Sakawa and Mori (1999), this criterion can perform better on fuzzy scheduling (Lei 2010b). Thus, in this paper, the max of two TFNs $X$ and $Y$ is approximated by the criterion (Lei 2010a, 2012). That is, if $X>Y$, then $X \vee Y=X$; else $X \vee Y=Y$.

![img-0.jpeg](img-0.jpeg)

Figure 1. The general flowchart of the EDA.

Table 1. Processing time table.

# 3. Estimation of distribution algorithm 

Estimation of distribution algorithm (EDA) is a relatively new paradigm in the field of evolutionary algorithms, which employs explicit probability distributions in optimisation (Larranaga and Lozano 2002). Different from the GA that reproduces a new population with the crossover and mutation operators, the EDA does it implicitly. With the tool of statistical analysis, the EDA tries to estimate the underlying probability distribution of the potential individuals and builds a probability model of the most promising area by statistical information based on the search experience. The probability model is used for sampling to generate the new individuals and is updated in each generation with the elite individuals of the new population. In such an iterative way, the population evolves, and finally satisfactory solutions can be obtained.

The general flowchart of the EDA is illustrated in Figure 1.
The critical step of the above procedure is to estimate the probability distribution. The EDA makes use of the probability model to describe the distribution of the solution space. The probability model built by the superior individuals helps the algorithm focus on the region with promising solutions. The updating process reflects the evolution trend of the population. Therefore, a proper probability model and a suitable updating mechanism are crucial to the EDA and should be well developed.

## 4. The EDA for fFJSP

### 4.1 Solution representation

Every individual of the population denotes a solution of the fFJSP, which is a combination of operation scheduling decision and machine assignment. Thus, a solution can be expressed by the processing sequence of operations and the assignment of operations on the machines. In this paper, a solution consists of two vectors corresponding to the two sub-problems of the fFJSP, i.e. operation sequence vector and machine assignment vector.

![img-2.jpeg](img-2.jpeg)

Figure 2. Illustration of the representation of a feasible solution.

For the operation sequence vector, the number of elements equals to the number of total operations $T_{O}$. The job number denotes the operation of each job, and the $k$ th occurrence of a job number refers to the $k$ th operation in the sequence of this job. For the machine assignment vector, each element represents the corresponding selected machine for each operation. So, the number of the elements is also $T_{O}$.

Given the operation sequence vector and machine assignment vector for a solution, the processing order on each machine is obtained. With the max operation on TFNs introduced in Section 2.2, the fuzzy starting time of $O_{i, j}$ can be calculated. With the addition operation on TFNs, the fuzzy completion time of $O_{i, j}$ can be calculated based on its fuzzy starting time and the fuzzy processing time. To further explain the representation, we provide an example by considering a problem with three jobs and three machines as shown in Table 1.

In Figure 2, it illustrates the representation of a feasible solution. The representation has the following operation sequence and machine assignment: $\left(O_{2,1}, M_{2}\right),\left(O_{3,1}, M_{3}\right),\left(O_{1,1}, M_{1}\right),\left(O_{1,2}, M_{1}\right),\left(O_{3,2}, M_{2}\right),\left(O_{2,2}, M_{2}\right),\left(O_{3,3}, M_{3}\right)$. Thus, the processing orders on each machine are as follows: $M_{1}: O_{1,1}-O_{1,2} ; M_{2}: O_{2,1}-O_{3,2}-O_{2,2} ; M_{3}: O_{3,1}-O_{3,3}$. Then, the fuzzy completion time can be obtained.

The fuzzy Gantt chart (Lei 2010a, 2010b, 2012) of this solution is shown in Figure 3. The TFN under the line is the fuzzy beginning time of the operation and the TFN on the line is the fuzzy completion time of the operation.

# 4.2 Left-shift scheme 

Due to the precedence constraint among operations of the same job, idle time may occur between the consecutive operations on the machine. For the schedule generated in Section 4.1, idle time interval exists between $O_{2,1}-O_{3,2}$ as shown in Figure 3. Considering the criterion of makespan, the left-shift scheme is employed to improve the schedule by shifting the operations to the left as compact as possible. Given a time interval $\left[t_{k}^{S}, t_{k}^{E}\right]$ beginning from $t_{k}^{S}$ and ending at $t_{k}^{E}$ on the machine $M_{k}$ to allocate operation $O_{i, j}, O_{i, j}$ can be started only after its immediate job predecessor $O_{i, j-1}$ is completed. So, the starting time of $O_{i, j}$ can be described as follow. If the operation has no predecessor, $C_{i, j-1}$ is replaced with $(0,0,0)$.

$$
S_{i, j}=\max \left\{t_{k}^{S}, C_{i, j-1}\right\}
$$

When operation $O_{i, j}$ is assigned on machine $M_{k}$, it checks the idle time intervals between operations that have already been scheduled on machine $M_{k}$ from left to right to find the earliest available time $S_{i, j}$. If there is enough time span from $S_{i, j}$ until $t_{k}^{E}$ to complete $O_{i, j}$, i.e.
![img-2.jpeg](img-2.jpeg)

Figure 3. Fuzzy Gantt chart of the solution shown in Figure 2.

![img-3.jpeg](img-3.jpeg)

Figure 4. Fuzzy Gantt chart after left shifting to the schedule in Figure 2.

$$
\max \left\{t_{k}^{S}, C_{i, j-1}\right\}+t_{i, j, k} \leq t_{k}^{E}
$$

Then we say that time interval $\left[t_{k}^{S}, t_{k}^{E}\right]$ is available for $O_{i, j}$. That is, $O_{i, j}$ can be left shifted. For each operation following the operation sequence vector of the representation, the above left-shift scheme is used to allocate it on its assigned machine from left to right. In this way, a representation is decoded to a detailed schedule.

For the example shown in Table 1 and Figure 3, according to the operation sequence vector and the machine assignment vector in Figure 2, operation $O_{2,2}$ is assigned on machine $M_{2}$ behind operation $O_{3,2}$. It checks the idle time intervals between operations that have already been scheduled on the machine from left to right. And then it gets $S_{i, j}=(5,6,8)$ and $t_{k}^{E}=(16,19,22)$. According to the ranking criteria of fuzzy numbers, Equation (2) is satisfied as $t_{i, j, k}=(5,9,12)$. Thus, $O_{2,2}$ can be left shifted. The fuzzy Gantt chart after left shifting is shown in Figure 4.

# 4.3 Probability model and updating mechanism 

The EDA produces new population by sampling a probability model. In this paper, the probability model is designed as two probability matrixes, i.e. operation probability matrix and machine probability matrix.

The element $p_{i j}(l)$ of operation probability matrix $A_{1}$ represents the probability that job $J_{j}$ appears before or in position $i$ of the operation sequence vector at generation $l$. The value of $p_{i j}$ implies the importance of a job when scheduling the operations on machines. For every $i\left(i=1,2, \cdots, T_{n}\right)$ and $j(j=1,2, \cdots, n), p_{i j}$ is initialised as $p_{i j}(0)=1 / n$, which ensures that the whole solution space can be sampled uniformly.

The element $q_{i j k}(l)$ of machine probability matrix $A_{2}$ represents the probability that operation $O_{i, j}$ is processed on machine $M_{k}$ at generation $l$. The value of $q_{i j k}$ indicates the rationality of an operation processed on a certain machine. The probability matrix $A_{2}$ is initialised as follows:

$$
q_{i j k}(0)=\left\{\begin{array}{l}
\frac{1}{m_{i, j}}, \text { if } O_{i, j} \text { can be processed on machine } k, \forall i, j, k \\
0, \text { else }
\end{array}\right.
$$

via sampling the probability matrixes $A_{1}$ and $A_{2}$, it generates new individuals. In particular, to generate a new solution it first generates the operation sequence vector from the first position to the last by sampling the probability matrix $A_{1}$. For every position $i$ of the operation sequence vector, job $J_{j}$ is selected with a probability of $p_{i j}$. If job $J_{j}$ has already appeared $n_{j}$ times, it means the processing procedure of job $J_{j}$ is completed. Then, the whole column $p_{1 j}, p_{2 j}, \cdots, p_{T_{n} j}$ of the probability matrix $A_{1}$ will be set as zero and all the elements of $A_{1}$ will be normalised to maintain that each row sums up to 1 . Similarly, the machine assignment vector is generated by sampling the probability matrix $A_{2}$. For every operation $O_{i, j}$, machine $M_{k}$ is selected with a probability of $q_{i j k}$. In such a way, a population with $P$ individuals are generated.

Next, it determines the superior sub-population with the best $S P$ solutions of the population according to the ranking criteria of fuzzy numbers. And then, the probability matrices $A_{1}$ and $A_{2}$ are updated according to the following equations:

$$
\begin{aligned}
& p_{i j}(l+1)=(1-\alpha) p_{i j}(l)+\frac{\alpha}{i \times S P} \sum_{s=1}^{S P} I_{i j}^{s}, \forall i, j \\
& q_{i j k}(l+1)=(1-\beta) q_{i j k}(l)+\frac{\beta}{S P} \sum_{s=1}^{S P} \tilde{I}_{i j k}^{s}, \forall i, j, k
\end{aligned}
$$

where $I_{i j}^{s}, \tilde{I}_{i j k}^{s}$ are the following indicator functions of the $s$ th individual in the superior sub-population.

$$
\begin{aligned}
& \tilde{I}_{i j}^{s}=\left\{\begin{array}{l}
1, \text { if job } J_{j} \text { appears before or in position } i \\
0, \text { else }
\end{array}\right. \\
& \tilde{I}_{i j k}^{s}=\left\{\begin{array}{l}
1, \text { if operation } O_{i, j} \text { is processed on machine } M_{k} \\
0, \text { else }
\end{array}\right.
\end{aligned}
$$

The above updating process can be regarded as a kind of increased learning, where the second terms on the right hand side of Equations (4) and (5) represent learning information from the superior sub-population.

# 4.4 Procedure of the EDA 

With the above design, the flowchart of the EDA for solving the fFJSP is illustrated in Figure 5.
In the flowchart, it generates $P$ individuals by sampling the probability matrices after the matrices are initialised. Then, the best $S P$ individuals are selected to update the probability model. If a stopping condition is met, it will stop the algorithm and output the optimal solution; otherwise, it will generate $P$ new individuals for the next generation of evolution. Since the probability model is updated with elite individuals, it is helpful for the algorithm to track the search region with promising solutions. With left-shift scheme, solutions can be improved as possible. So, it is expected to solve the fFJSP effectively.

### 4.5 Computational complexity analysis

For each generation of the EDA, its computational complexity can be roughly analysed as follows.
For the updating process, first it is with the computational complexity $O(P \log P)$ by using the quick sorting method to select the best $S P$ individuals from population; then, it is with the complexity $O\left(T_{o} \times S P+T_{o} \times n\right)$ to update all the $T_{o} \times n$ elements of $A_{1}$ by the operator sequence vectors and with the computational complexity $O\left(T_{o} \times S P+T_{o} \times m\right)$ to update $A_{2}$ by the machine assignment vectors. Thus, the computational complexity for updating process is $O\left[T_{o}(S P+m\right.$ $+n)+P \log P]$.
![img-4.jpeg](img-4.jpeg)

Figure 5. The flowchart of the EDA for the fFJSP.

For the sampling process, every gene is generated with the roulette strategy by sampling $A_{1}$ and $A_{2}$ to obtain a new individual. To generate an operation sequence vector, it is with the complexity $O\left(T_{o} \times n\right)$. To generate a machine assignment vector, it is with the complexity $O\left(T_{o} \times m\right)$. Thus, the computational complexity for generating $P$ individuals is $O$ $\left[P T_{o}(m+n)\right]$.

Table 2. Combinations of parameter values.
Table 3. Orthogonal array and ARV values.
![img-5.jpeg](img-5.jpeg)

Figure 6. Factor level trend of the EDA.

It can be seen that the complexity of the proposed EDA is not large. In the next section we will further verify its efficiency by numerical test.

# 5. Computational results and comparisons 

To test the performance of the proposed EDA, numerical simulations are carried out based on the instances from Lei (2010a, 2012). We code the algorithm in $\mathrm{C}++$ and run it on Thinkpad T420 with a 2.3 GHz processor/2 GB RAM. For each instance, the algorithm is run 20 times independently with the same number of evaluations as Lei (2012), i.e. $150,000$.

### 5.1 Parameters setting

In our EDA, it contains four key parameters: $P$ (population size), $\eta$ (percentage of superior sub-population from population, $\eta=S P / P \times 100$ ), $\alpha$ (learning rate of $A_{1}$ ), and $\beta$ (learning rate of $A_{2}$ ). To investigate the influence of these

Table 4. Response value and rank of each parameter.

Table 5. Results of the five instances.
parameters on the performance of the EDA, we implement the Taguchi method of design of experiment (DOE) (Montgomery 2005) by using Instance 1. Combinations of different values of these parameters are listed in Table 2.

For each combination, the EDA is run 20 times independently. The response variable value (RV) is the defined as $\left(x_{1}+2 x_{2}+x_{3}\right) / 4$ for a triangular fuzzy number $X=\left(x_{1}, x_{2}, x_{3}\right)$ of the makespan. The average response variable (ARV) value is the average of RV values obtained in 20 times. Clearly, the smaller the ARV is, the better the combination is. Considering four factor levels for each parameter, we get an orthogonal array $L_{16}\left(4^{4}\right)$, which is shown in Table 3 together with the obtained ARV values.

According to the orthogonal table, we illustrate the trend of each factor level in Figure 6. Then, we figure out the response value of each parameter to analyse the significance rank of each parameter. The results are listed in Table 4.
![img-6.jpeg](img-6.jpeg)

Figure 7. The best solution of Instance 1 obtained by the EDA.

![img-7.jpeg](img-7.jpeg)

Figure 8. The best solution of Instance 2 obtained by the EDA.
From Table 4 it can be seen that the learning rate $\alpha$ of $A_{1}$ is the most significant one among the four parameters. That is, the learning rate of the matrix for operator sequence is crucial to the EDA. A small value of $\alpha$ could lead to slow convergence while a large value could lead to premature convergence. The significance of the learning rate $\beta$ of $A_{2}$ ranks the second. A large value of $\beta$ could lead to premature convergence. Besides, the population size $P$ ranks the third. A large population size ensures that the whole solution space can be sampled sufficiently. With a fixed maximum number of evaluations, however, a larger population size leads to fewer generations which may cause an insufficient evolution. As for $\eta$, it has the slightest influence while a moderate value is preferable. According to the above analysis, the parameter setting for the EDA is suggested as $P=150, \eta=20, \alpha=0.3$ and $\beta=0.1$, which will be used for the following tests.

![img-8.jpeg](img-8.jpeg)

Figure 9. The best solution of Instance 3 obtained by the EDA.

# 5.2 Testing results and comparisons 

With the five instances (Lei 2010a, 2012), we compare the EDA with four existing algorithms, including CGA (Lei 2012), DIGA (Lei 2010a), PEGA (Pezzella, Morganti, and Ciaschetti 2008), and PSO+SA (Xia and Wu 2005). The results are listed in Table 5, where the results of the existing algorithms are directly from literature (Lei 2012).

From Table 5, it can be seen that the EDA is the best one among all the algorithms in solving the five instances. Compared with other algorithms, the EDA can obtain the best values in terms of the average value, the best value and the worst value, which implies that the EDA is the most effective. For example, when solving Instance 4, the average value $(24.8,37.2,51.9)$, the best value $(21,36,50)$ and the worst value $(24,39,57)$ obtained by EDA are better than

![img-9.jpeg](img-9.jpeg)

Figure 10. The best solution of Instance 4 obtained by the EDA.
those values obtained by the other four algorithms in the fuzzy sense. In Figures 7-11, the fuzzy Gantt charts of the best solutions obtained by the EDA for Instance $1-5$ are illustrated.

In addition, the average CPU time of 20 different runs is listed in Table 6. It can be seen that the EDA is the most efficient one among all the algorithms. Even for Instance 5 with the largest scale, the EDA only spends an average of 9.83 s .

So, it is concluded that the EDA is an efficient and effective algorithm for solving the fFJSP. The superiority of the EDA owes to the following aspects.

![img-10.jpeg](img-10.jpeg)

Figure 11. The best solution of Instance 5 obtained by the EDA.

Table 6. CPU time (s) of the five instances.
Notes: ${ }^{\mathrm{a}}$ Core i5 2.3 GHz CPU. ${ }^{\mathrm{b}} 1.7 \mathrm{GHz}$ CPU.

(1) With the well-designed probability model and the suitable updating mechanism, it is helpful to explore the search space effectively.
(2) With the left-shift scheme, it is helpful to refine a schedule with a smaller fuzzy makespan.
(3) With the investigation of parameter setting, suitable values are determined to achieve good performance.

# 6. Conclusions 

In this paper, an effective estimation of distribution algorithm was proposed for solving the flexible job-shop scheduling problem with fuzzy processing time. A specific probability model was designed for the EDA to solve the problem. And a mechanism was provided to update the model reasonably. The model was used for generating promising solutions among the search space, and a left-shift scheme was used to improve the solutions. The influence of parameter setting was investigated and suitable setting was recommended. Numerical testing results demonstrated the effectiveness of the proposed EDA in comparing with the existing algorithms. The future work is to study the EDA for other kinds of fuzzy scheduling problems. We also will carry out some research of the EDA for multi-objective scheduling problems.

## Acknowledgments

This research is partially supported by the National Key Basic Research and Development Program of China (2013CB329503), the National Science Foundation of China (61174189 and 61025018), the Doctoral Program Foundation of Institutions of Higher Education of China (20100002110014), and the National Science and Technology Major Project of China (No. 2011ZX02504-008).
