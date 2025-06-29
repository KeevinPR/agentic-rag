# An Improved Estimation of Distribution Algorithm for Cloud Computing Resource Scheduling 

$1^{\text {st }}$ Haisheng Sun<br>School of Computer Science and Technology<br>University of Science and Technology of China<br>Hefei, China<br>haisheng@mail.ustc.edu.cn<br>2 $2^{\text {nd }}$ Chuang Liu and $4^{\text {th }}$ Huaping Chen<br>School of Management<br>University of Science and Technology of<br>China Hefei, China<br>chuang@mail.ustc.edu.cn, hpchen@ustc.edu.cn<br>$3^{\text {rd }}$ Rui Xu<br>School of Business<br>Hohai University<br>Nanjing, China<br>rxu@hhu.edu.cn


#### Abstract

This paper focuses on cloud computing resource scheduling on the Soft as a Service layer and aims at minimizing the user costs by regarding the deadline as a constraint for scheduling independent tasks. Existing works with evolutionary computation approaches fail to describe the interactions among independent tasks. To overcome this problem, an improved Markov-chain-based estimation of distribution algorithm is proposed, and the concept of virtual machine selection diversity is created to construct the probabilistic model rationally. Moreover, one heuristic rule related to the investigated problem is created to keep the population maintaining a high diversity in the evolution process. The experiment results show that the proposed algorithm not only obtains the best solution quality but also has competitive convergence among all compared algorithms.


Keywords-estimation of distribution algorithm; markov chain; cloud computing; resource scheduling

## I. INTRODUCTION

As a novel mode of resource utilization in the form of Soft as a Service (SaaS), Platform as a Service, and Infrastructure as a Service, cloud computing offers considerable value to scientific research and real-world applications [1]. This technology enables end-users to easily purchase services on demand in the pay-per-use model, and the user's demand for cloud computing resource has dramatically increased recently. Therefore, achieving an optimal scheme for cloud computing resources scheduling (CCRS) that satisfies the various requirements of users and cloud providers has become a significant and valuable topic in cloud computing.

Under the pay-per-use model, researches in CCRS problem need to meet the user's requirements of Quality of Service (QoS), which has been seen as a significant issue [2]. So far, many related works have presented various user QoS including single or multiple QoS [3]-[5]. However, the previous works satisfying the user QoS still have certain shortcomings. For example, the various QoS levels expected by different users cannot be met when only single QoS is considered [6]. Moreover, most of the multiple QoS works weight and combine different QoS to form pseudo multi-objective optimization [7] so that the optimization results excessively

[^0]depend on adjusting the weights. Different from the above studies, literature [8] considers multiple QoS by aiming at minimizing the user cost while ensuring the makespan meet deadline constraint for scientific workflows, and the results show that the scheduling scheme can be produced with a lower execution cost. Following aforementioned ideas, the particular problem investigated in this paper aims at minimizing the user costs by regarding the deadline as a constraint for scheduling independent tasks on the SaaS layer.

CCRS problem can be regard as a many-to-one mapping relation between the required tasks (cloudlets) and the available virtual machines (VMs). Author [9] indicates that the CCRS problem has been considered as an NP-hard problem. Evolutionary computation (EC) which have efficiency and effectiveness in tackling complex optimization problems are widely used to address CCRS issues [10]. Some related works adopting EC approaches are reviewed in the following. For minimizing the makespan, [4] schedules independent and divisible tasks adapting to different computation and memory requirements via the genetic algorithm (GA) in early time, but there is not much improvement in the GA, and concurrently, the simulation is conducted without a cloud environment. Additionally, [11] proposes a hybrid ant colony optimization (ACO) based particle swarm optimization (PSO) to minimize the makespan, but the comparative experiment in this article is not sufficient.

However, the apparent deficiency of previous works such as [3], [4], [11] is assuming that each independent task is entirely irrelevant to its adjacent neighbors when allocating them to virtual machines (VMs). In practice, the arrangement for the current task $i$ will certainly have a certain impact on the VM selection for its subsequent tasks $i+1$. If task $i$ is first assigned to VM $j$ and then task $i+1$ is scheduled to the same $\mathrm{VM} j$, the completion time of the latter will be increased because of waiting in the queue. Attempting to capture the dependence information among components of a candidate, this study adopts estimation of distribution algorithm (EDA) [12] whose behaviour is characterized by the probabilistic model applied. EDA which is also a stochastic optimization algorithm shares the advantages of EC approaches and is considered effective at dealing with multi-constraints and multi-criteria decision making processes [13]. Note that, the existing EDA


[^0]:    This work was support in part by the National Natural Science Foundation of China (No. 71671168 / No.71433003), the China Postdoctoral Science Foundation (No.2015M581707), the Jiangsu Planned Projects for Post-doctoral Research Funds (No.1501006B).

for tackling CCRS in the literature [14], [15] pertains to the particular EDA that assumes the problem variables are independent. Thus these existing EDA approaches fail to consider the interactions among independent tasks. Inspired by the Markov chain model that can well describe the interactions among variables [16], [17], an improved EDA based on a 1order Markov chain model (MCEDA) is constructed to cope with the investigated problem efficiently. Moreover, several heuristic rules are created to keep the population maintaining a high diversity in evolution process. Finally, an extremely comprehensive experiment is conducted to prove the effectiveness of the MCEDA. The results show that our MCEDA obtains the best solution quality and has competitive convergence among all the compared algorithms.

The remainder of this paper is organized as follows: Section 2 presents the problem formulation. Section 3 gives the design of the MCEDA in detail. The comparative experiment is provided in Section 4. Finally, we end the paper with conclusions and future work in Section 5.

## II. Problem Formulation

This section describes the problem investigated by defining the notation used before presenting the associated mathematical equations in detail. In the following section, the VMs and cloudlets represent resources and tasks, respectively.

## A. Notations

## B. Constraints

Our scheduling is subject to the VMs allocation and time constraints. Then, the decision vector V need to be identified, which is also the solution for the problem. Note that the cloudlet scheduling sequence is irrelevant to the solution. Therefore, the natural increment sequence $(1,2, \ldots, n)$ is adopted in each solution for convenience. The following notations and explanation are employed in the following parts.

- This paper agrees that a static pool of heterogeneous resources that are available to process the tasks is provided.

$$
v_{i} \in\{1,2, \ldots, m\}, i=1,2, \ldots, n
$$

- We designate a pre-configured processing capability to each VM by floating point operations per second (FLOPS); thus, the actual processing time of each cloudlet is determined according to the VM to which it is assigned.

$$
P T_{i}^{v_{i}}=L_{i} / P_{v_{i}}, i=1,2, \ldots, n
$$

where $L_{i}$ represents the size of cloudlet $i$ in terms of floating point operations (FLOP).

- Each VM executes the cloudlets according to the FIFO rule. Whenever a new cloudlet $i$ is scheduled on a particular VM $j$, the cloudlet needs to enter the waiting queue of VM $j$. Naturally, the queue waiting time for new cloudlet $i$ can be calculated by equation (3).

$$
W T_{i}=\sum_{k=1}^{i-1} P T_{k}^{v_{i}}, 2 \leq i
$$

where $k$ represents the number of previous cloudlets before current new cloudlet $i$.

- The completion time for each VM equals the completion time for the last cloudlet of its waiting queue.

$$
M T_{j}=\sum_{i=1}^{s} P T_{i}, i \in Q_{j}, j=1,2, \ldots, m
$$

Where, $s$ is the size of the waiting queue. Thus, the completion time for all cloudlets is equal to the longest completion time of all the VMs. Each solution will give a scheduling program, and only if the maximum completion time $T$ is not more than deadline $D$ can we state that the solution is feasible.

$$
T=\max \left\{M T_{j}\right\} \leq D, j=1,2, \ldots, m
$$

## C. Objective

The objective is to minimize the user (execution) cost for processing independent tasks with the deadline constraint on the SaaS layer.

$$
\boldsymbol{m i n} \quad O b j(V)=\sum_{j=1}^{m} M T_{j} \cdot C_{j}
$$

## III. PROPOSED MCEDA

In this section, we elaborate the MCEDA proposed to tackle the problem investigated.

## A. Markov-EDA Framework

This paper adopts a 1-order Markov-EDA [12], [16] in which the configuration of the variable $z^{n+1}$ depends on the configuration of the previous variable, which can be formulized as equation (7). Note that, our proposed MCEDA without variables permutation is different from mutual information maximing input clustering (MIMIC) [18] whose main

Algorithm 1 General Framework for EDAs

```
\(Z_{0} \leftarrow\) Generate \(N\) individuals (the initial population)
    randomly;
for \(l=0 \rightarrow\) stopping criterion do
    \(Z_{l-1}^{a} \leftarrow\) Select \(M(M \leq N)\) individuals from \(Z_{l-1}\);
    Compute the marginal and conditional probabilities
        corresponding to each factor of factorization;
        \(Z_{l} \leftarrow\) Sample \(N\) individuals from \(p_{l}(x)\);
    end for
```

idea is to choose the optimal permutation to produce the lowest pairwise entropy with respect to the true distribution, although, both of them belong to a chain topology. The pseudo code of the Markov-EDA is shown in Algorithm 1.

$$
p\left(z^{n+1} \mid z^{1}, z^{2}, \ldots, z^{n}\right)=p\left(z^{n+1} \mid z^{n}\right)
$$

## B. Encoding Scheme

The integer (decimal) encoding scheme is employed in this article. There are $m$ kinds of resource allocation options for each component of a candidate, which can be seen from equation (1).

## C. Probabilistic Model

The primary idea of the MCEDA is to construct a probabilistic model to take full advantage of the interaction among independent tasks. We suppose that each cloudlet (variable) in the problem follows the 1-order Markov chain model and regard equation (7) as a factorization of the univariate marginal. In this sense, the joint probability distribution in the MCEDA can be factorized as follows:

$$
p(V)=p\left(v_{1}\right) \cdot \prod_{i=2}^{n} p\left(v_{i} \mid v_{i-1}\right)
$$

First, to make the VM allocation process more rational and enrich the population diversity during the evolution, this paper tactfully presents the concept of VM selection diversity $\rho_{l-1}(x)$, which means that a different VM $x$ assigned to execute the current $i$ th cloudlet has a diverse effect on the VM selection of the following $(i+1)$ th cloudlet in the $l$ th generation. Considering the significance of the first component and its unrestricted VM selection space, the first variable is chosen as the sample space to count the number denoted as $N(x)$ of the first variable from $S_{l}^{x}$ when $v_{1}=x$. Then, we add up the number denoted by $d(x)$ of variant VMs in the second component under the premise of $v_{1}=x$. In the case that no $v_{1}=x$ exists, a greater value tolerated is assigned. Thus, we measure the VM selection diversity by the equation (9). The smaller $\rho_{l-1}(x)$ is, the stronger the influence of VM $x$ is and the greater the probability value for the appearance of $x$ in the $l$ th generation.

$$
\rho_{l-1}(x)= \begin{cases}N(x) / d(x), & x \in V_{l-1,1} \\ \mu_{1} \cdot \max \{N(x) / d(x) \mid x \in V_{l-1,1}\}, \text { otherwise }\end{cases}
$$

Second, the relative frequency is considered to compute the marginal probabilities $p\left(v_{1}\right)$. The frequencies based on the statistics of the selected individuals about the first component stand for the marginal probabilities. Here, $f_{l, 1}\left(v_{1}=x\right)$ means the frequencies of the first variable $x$, and $p_{l, 1}\left(v_{1}=x\right)$ is the normalization probability in the $l$ th generation.

$$
\begin{aligned}
& f_{l, 1}\left(v_{1}=x\right)= \\
& \begin{cases}N(x) / M, & x \in V_{l-1,1} \\
\mu_{2} \cdot \min \left\{N(x) / M \mid x \in V_{l-1,1}\right\}, & \text { otherwise }\end{cases} \\
& p_{l, 1}\left(v_{1}=x\right)=f_{l, 1}\left(v_{1}=x\right) / \sum_{x=1}^{m} f_{l, 1}\left(v_{1}=x\right)
\end{aligned}
$$

Next, considering the characteristics of the studied problem, the approach for calculating the conditional probabilities need to be ameliorated. According to the diverse conditions of the current variable (component) in $S_{l}^{x}$, the traditional conditional probabilities are separately divided into three cases: 1) both $v_{i-1}=x_{2}$ in $V_{l, i-1}$ and $v_{i}=x_{1}$ in $V_{l, i}^{x_{2}}$ are available, $\mathrm{i}=2,3, \cdots, n ; 2$ ) there is no $v_{i-1}=x_{2}$ existing in $V_{l, i-1} ; 3$ ) otherwise. Accordingly, the improved conditional probability denoted by $f_{l, i}\left(v_{i}=x_{1} \mid v_{i-1}=x_{2}\right)$ can be expressed as

$$
f_{l, i}\left(v_{i}=x_{1} \mid v_{i-1}=x_{2}\right)=
$$

$$
\begin{cases}N\left(x_{1}\right) / N\left(x_{2}\right), & \\ 1 / m, & x_{2} \notin V_{l-1, i-1} \\ \mu_{3} \cdot \min \left\{N\left(x_{1}\right) / N\left(x_{2}\right) \mid \psi\right\}, & \text { otherwise }\end{cases}
$$

where $\psi=x_{2} \in V_{l-1, i-1} \& x_{1} \in V_{l, i}^{x_{2}} i=2,3, \ldots, n$
Furthermore, a real-time heuristic information is introduced to help define the conditional probabilities $p\left(v_{i} \mid v_{i-1}\right)$ appropriately and to precisely select the available resources. As described, the problem noted in this paper is limited by deadline $D$ such that the total processing time needs to be minimized as much as possible. Let $F_{l, i}(x)$ expresses the inverse queue waiting time expressed as equation (11). Thus, the larger $F_{l, i}(x)$ is, the shorter $W T_{i}$ is, and the greater the probability value for assigning to VM $x$ in the $l$ th generation is.

$$
F_{l, i}(x)=1 / W T_{i}, v_{i}=x \& i=2,3, \ldots, n
$$

Finally, the normalized transition probability can be determined by combining $p_{l, 1}\left(v_{1}=x\right), F_{l, i}(x)$ and $f_{l, i}\left(v_{i}=\right.$ $\left.x_{1} \mid v_{i-1}=x_{2}\right)$ using a set of exponents, which is expressed as follows:

$$
\begin{aligned}
& p_{l, i}\left(v_{i}=x_{1} \mid v_{i-1}=x_{2}\right)= \\
& f_{l, i}\left(v_{i}=x_{1} \mid v_{i-1}=x_{2}\right)^{a} \cdot p_{l, 1}\left(v_{1}=x\right)^{b} \cdot F_{l, i}(x)^{c} / \eta
\end{aligned}
$$

where $\eta=\sum_{x_{i}=1}^{m} f_{l, i}\left(v_{i}=x_{1} \mid v_{i-1}=x_{2}\right)^{a} \cdot p_{l, 1}\left(v_{1}=x\right)^{b}$. $F_{l, i}(x)^{c}$ and parameters $a, b$ and $c$ are the importance of each item to the selection of the offspring and are all positive.

## D. Population Sampling

From the above, the marginal probabilities $p\left(v_{1}\right)$ of the proposed model can be acquired by equation (11), and the conditional probabilities $p\left(v_{i} \mid v_{i-1}\right)$ can be obtained by using equation (14). Then, the sampling processing for each component in the solution can be conducted with a straightforward approach from these probability model. In order to enhance the exploration capacity of the proposed algorithm, a small part of new individuals will be generated by cross and mutation of the best superior individual of the last generation.

## E. Algorithm Presentation

The infeasible solutions, which appear because of the deadline constraint, should be corrected after the sampling processing is performed. Consequently, a correction algorithm (CA), whose main idea is to migrate the most time-consuming cloudlet of each solution to the most unoccupied VM, rises in response to the proper time and conditions. Here, the most unoccupied VM indicates that the reborn $M T_{j}$ can be calculated by equation (15) and is at a minimum while scheduling cloudlet $k$ to VM $j$. Note that, in the following simulation experiments, the parameter $D$ will be set by considering both the processing capability of VMs and the length of cloudlets to ensure that there is at least one feasible solution can be corrected by CA. The pseudo code of CA is presented in Algorithm 2.

```
Algorithm 2 CA
Begin
    for \(i=1 \rightarrow N\) do
        while \(D \leq T[i]\) do
            Order all VMs in the \(M T_{i}\) in non-increasing order;
            Select the cloudlet with maximal \(P T_{i}\) from the first
            VM;
            Migrate it to the optimal VM obtained with equation
            (15);
            Calculate \(T[i]\).
        end while
    end for
End
```

$$
M T_{j}=\min \left\{M T_{j}+P T_{k} \mid v_{k}=j\right\}
$$

With the declarative probabilistic model and sampling procedure, our MCEDA is proposed as Algorithm 3. As for the time complexity, $Z_{0}$ is generated with the time complexity of $O(N n)$ and the time complexity of Algorithm 2 for each individuals is $O(n+m \log m)$. Computing the objective of all solutions costs $O(N n)$ time and sequencing all the solutions requires $O(N \log N)$ time. The operation of constructing equation (9) has a time comlpexity of $O(M m)$. Calculating the probability values by equation (11) or (14) can be done in $O(n m M)$ and the time complexity of sampling step is $O(N n)$ and the elitism criterion only need $O(1)$ time. Therefore the total time complexity of all steps in Algorithm 3 is $O(N(n+m \log m)+n m M)$.

## Algorithm 3 MCEDA

## Begin

1: Set the initial population $Z_{0}=\emptyset$, selected population $Z_{0}^{*}=\emptyset$, generation counter $l=0$;
2: Generate $Z_{0}=\left\{V_{1}, V_{2},, V_{N}\right\}$ at random;
3: Applying Algorithm 2 to make correction procedure;
4: for $l=1 \rightarrow l_{\max }$ do
5: Calculate (6) for each solution $V$;
6: Sequence all the solutions in term of objective values in non-decreasing order;
7: $Z_{l-1}^{*} \leftarrow$ select the top $M$ individuals;
8: Construct (9);
9: for $i=1 \rightarrow n$ do
10: if $i==1$ then
11: Construct and solve (11);
12: else
13: Construct and solve (14);
14: end if
15: end for
16: Sample new population and applying Algorithm 2;
17: elitism criterion
18: end for
19: The best individual in $Z_{l}$ is the final solution.

## End

The specific parameter settings employed for MCEDA are as follows. The rational population size of MCEDA is set to $N=n \times m$, and $n \times m$ represents the assignation that schedules $n$ cloudlets to $m$ VMs. Then, the truncation selection strategy is applied, which chooses the top $M=20 \times N$ individuals. Furthermore, an improved elitism criterion is employed, which converts the worst individual worst $_{l}$ in this generation to the best individual best $_{l-1}$ in the last generation after sampling. Finally, the maximum iteration $l_{\max }=5 \times n$ is seen as a termination criterion.

## IV. Performance Evaluation

In this section, the CloudSim framework [19] was used to simulate a cloud environment that has a single data center. In the following experiments, the policy that determines the share of processing power among cloudlets in every VM is space-shared stated in CloudSim. Research [20] states that there is no optimal algorithm for CCRS because of its NPhard complexity and EC algorithms are the most powerful of heuristic methods. Therefore, abundant experiments are conducted to compare the proposed MCEDA with several existing related ECs and EDAs.

## A. Parameter Settings

The VM configurations are based on the most recent computation and optimization resources of the current Amazon elastic compute cloud and are given in Table I. The method proposed by the [21] is employed to estimate the VM processing capacity based on the number of ECUs. We specify the unit time on which the pay-per-use model is based as one

hour, which means that any partial utilization of the leased VM is charged as if the full one-hour period was occupied.

TABLE I. CONFIGURATIONS OF VM


Because of having no benchmark for CCRS, the size of cloudlets is generated from a discrete uniform distribution ranging from $5 \times 10^{5}$ to $1 \times 10^{6}$ gigaflops. Given the provisions that the total number of VMs in the experiment is $K(K \leq 10)$, then the top $K$ types of VM in Table I are selected and the deadline parameter $D$ is set by equation (16) with $\omega=0.5$ unless otherwise indicated, where $P_{\max }$ and $P_{\min }$ represent the maximum and minimum processing capability of all VMs, respectively. Meanwhile, the top $t$ cloudlets are chosen in term of the size of $L_{i}$ to obtain $D$.

$$
D=\sum_{i=1}^{t} \frac{L_{i}}{P_{\max }}+\omega \cdot\left(\sum_{i=1}^{t} \frac{L_{i}}{P_{\min }}-\sum_{i=1}^{t}\right) \frac{L_{i}}{P_{\min }}, t=\left\lceil\frac{n}{m}\right\rceil
$$

## B. Comparative Algorithms

1) EC Approaches: First, the most commonly used GA was selected. To maintain the diversity of the population, we use the concept of "generation gap" and set the $G a p=10 \%$. The GA parameter settings in [22] are employed. The next EC approach is the ACO and the special parameter settings in [23] are employed.
2) $E D A$ : First, the earliest population based incremental learning (PBIL) recognized as initially solving the binary optimization is selected. Our experiment takes the top $20 \% \times N$ individuals to learn the model and sets the learning rate $\alpha l p h \alpha=0.01$. MIMIC [18] is selected as the second comparative method, in which the conditional probabilities are obtained from simple statistics on dominant population.

## C. Cost Evaluation

In this section, the average user costs obtained for each instance of all algorithms are compared on various configurations: (A) $20 \times 4$, (B) $50 \times 6$, (C) $80 \times 8$, (D) $80 \times 10$, (E) $100 \times 10$, (F) $150 \times 10$. For each configuration, three instances are generated and all algorithms are executed ten times for each instance. The parameters recorded are $A D \pm S D$, where $A D=\sum_{i=1}^{10}\left(O b j_{i}-O p t\right) / 10$ stands for the average deviation and Opt represents the optimal (best) solution obtained during all the executions for each instance. The standard deviation of the solution is denoted as $S D$. Table II shows that the comparative results varies with instances. The results in bold indicate
the algorithm that obtains $O p t$; the results with strikethrough denote that the algorithm that achieves the lowest $A D$; the results marked with * represent that the corresponding algorithm obtains the solution in the optimal region $(O R)$ at least once during ten executions, where $O R=[\text { Opt }, \text { Opt } \times(1+2 \%)]$

TABLE II. Cost EVALUATION ON VARIOUS SCALE InSTANCES


For obtaining Opt, the MCEDA had significant superiority over the other algorithms, achieving 15 Opts out of the total 18 instances. In contrast, only 2 Opts were obtained by GA and one by ACO. Compared to the other algorithms, the MCEDA still maintained a clear advantage regarding the lowest $A D$, acquiring 13 best $A D$ s of all the instances. Remarkably, the $A D$ of MIMIC is lower than any other algorithm except MCEDA as a whole. which means that EDA with dependance is more efficient. Moreover, the MCEDA satisfied the $O R$ for all the instances, i.e., the MCEDA obtained all solutions in $O R$ within ten repetitions. In addition, ACO and MIMIC have more ability of acquiring the $O R$ than GA and PBIL. Note that MCEDA and MIMIC show better performance when the instances are large-scale and have abundant VMs, which can be validated by analyzing the $A D$ values.

In conclusion, most of $O p t s$ were obtained by the MCEDA, and over half of the lowest $A D$ s were also contributed by the MCEDA. Additionally, the MCEDA appeared to be strongly capable of obtaining all the solutions in the $O R$ within ten executions. Accordingly, these distinct advantages indicate that the MCEDA should be seen as an effective alternative and applicable to solve the investigated problem in this paper.

## D. Convergence Analysis

This section is devoted to the analysis of the convergence of the comparative algorithms under configurations $50 \times 6$ and $100 \times 10$. Ten instances were generated for each configuration, and each algorithm was executed ten times for each instance.

This experimentation was carried out with three deadline parameters $D_{1}, D_{2}$ and $D_{3}$, which are generated with $\omega=0.25$, $\omega=0.5$, and $\omega=0.75$ by equation (16).

The generation in which the final result first appeared was recorded for each execution and could reflect the convergence speed since all algorithms share the same termination criterion for each instance. The span of each box represents the stability of the corresponding algorithm.

1) Convergence Speed: As seen in Fig. 1, it is clear that MIMIC has the fastest convergence speed and MCEDA had a lower median generation than the corresponding result of either the GA or PBIL. As to the $50 \times 6$ instance, the median generation of the MCEDA was not inferior to that of the ACO. However, for the more-VMs instance $100 \times 10$, the convergence speed of the MCEDA was similar to that of the ACO. Furthermore, the deadline parameters had less effect on the MCEDA when the scale of instance increases.
2) Convergence Stability: When compared on the $50 \times 6$ instances, the MCEDA did not have the advantage of convergence stability. For the $100 \times 10$ instances, the MCEDA can achieve a smaller box span than the others. Moreover, the deadline parameters had also less influence on the MCEDA than the others.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Box plots of convergence analysis
In conclusion, the MCEDA achieved a competitive convergence speed and performed relatively stable among the comparative algorithms on two configurations.

## V. CONCLUSION

In this paper, a cloud computing resource scheduling problem for minimizing the user costs for processing independent tasks with a deadline constraint on the SaaS layer was analyzed and addressed. To solve the problem, an improved variabledependent approach MCEDA was proposed. The experiment showed that the MCEDA has significant superiority over other algorithms for minimizing the user cost, particularly for largescale and more-VM instances. In addition, MCEDA was also competitive on convergence speed and stability.

There are still many valuable research points worth addressing to improve the solving algorithm or the CCRS problem in this paper, i.e., the way to construct and solve the marginal probability of the first component can be improved. At the present stage, CCRS is still a front-burner issue, and the design of the scheduling algorithm that has outstanding performance is also a challenge faced by researchers.
