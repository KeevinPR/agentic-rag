# Research of Batch Scheduling with Arrival Time Based on Estimation of Distribution Algorithm 

Dong Li<br>Shenyang Institute of Automation<br>ShenYang, China<br>lidong1@sia.cn<br>Feifei Peng<br>University of California, San Diego, America<br>kelloggpeng@live.cn


#### Abstract

Estimation of distribution has been used to solve the batch scheduling problem with job release problem, which minimizing the makespan as the objective function. According to the characteristic of the batch scheduling problem with job release time and the estimation of distribution algorithm, this paper builds the probabilistic model based on the characteristic of batching process and designs the mechanism of personal sampling and probability update, then proposes a new estimation of distribution algorithm to solve the batch scheduling problem with job release time. The mechanism of population generation and probability updating has been improved in the standard compact genetic algorithm (a kind of EDA) which accelerate the convergence rate of algorithm. Moreover, the influence of parameter setting is investigated based on design of experiment and suitable parameter values are suggested. Simulation results based on some instances and comparisons with some exiting algorithms demonstrate the effectiveness and robustness of the proposed algorithm.


Key words-Estimation of distribution algorithm (EDA); Probability Model; Batch Scheduling

## I. INTRODUCTION

Batch scheduling is a type of optimization problem with important application background that emerged in 1990s. The basic assumption is that machines can process multiple workpieces simultaneously. Batch machines are widely used in the manufacturing industry, such as heat treatment in the metal-processing industry, shiplock scheduling with multiple stages, cargo handling in port and presintering in the manufacturing of semiconductor integrated circuit ${ }^{[1]}$. In this paper, the single parallel batch scheduling problem with compatible workpiece group is taken as an example. The object function is to minimize the maximum processing time in parallel batch scheduling with arrival time.

The traditional solutions for batch scheduling problem are the exact algorithms ${ }^{[2-3]}$ and heuristic algorithms ${ }^{[4-6]}$. In the theory of exact algorithm, optimal solution can be obtained. However, due to the long computing time, it is only suitable for small-size problems. In the heuristic algorithm, the solution for problems can be obtained with low time complexity. But the accuracy of solutions cannot be ${ }^{1}$ guaranteed. Because of the drawbacks of traditional algorithms, swarm intelligence algorithm for solving the batch scheduling problem is being studied by many researchers, and good results have been achieved

[^0]Xiaofeng Zhou<br>Shenyang Institute of Automation<br>ShenYang, China<br>zhouxiaofeng@sia.cn<br>Chang Liu<br>Shenyang Institute of Automation<br>ShenYang, China<br>changl@sia.cn

The estimation of distribution algorithm (EDA) is a probability modeling evolutionary algorithm. A brand-new evolutionary model is used in the algorithm. There are no intersection and mutation operations in genetic algorithms. However, statistical learning is used to establish a probability model that describes the distribution of solutions from the macroscopic point of view. Evolution of samples ${ }^{[10]}$ is realized through repeated sampling for generating new groups in the probability model. EDA can effectively realize the mixing and recombination of building blocks through establishing the mutual relationship between descriptive variables of probability model. Hence problems that are difficult to be solved by the existing swarm intelligence algorithm can be solved. Nonlinear and high-dimensional problems can be processed much more effectively ${ }^{[11]}$. Currently, EDA has already been widely used in the field of engineering optimization, machine learning, pattern recognition and operations research ${ }^{[12-16]}$.

Literature research shows that the EDA algorithm has not been used in the batch scheduling problem yet. In this paper, addressing the batch scheduling problem and EDA algorithm, a variable-related probability model based on workpiece group is proposed. The method of initializing the probability model, individual sampling and updating the model are designed. Moreover, the cGA (compact genetic algorithm) in EDA is improved, and then an IcGA (improved compact genetic algorithm) that can solve the batch scheduling problem with arrival time for workpieces is proposed.

## II. Problem Description

In this paper, the research object is the single parallel batch scheduling problem of compatible workpiece group with finite batch capacity and unequal arrival times, and the object function is to minimize the maximum processing time. In the batch scheduling model, the capacity of each batch is limited. It cannot be larger than the maximum processing capability $S$ of batch machines, and neither can it be smaller than the lower bound $L$ of batch machines out of the consideration of energy conservation and other reasons. The job release times of different workpieces are unequal. There is only one batch machine in the model. Before system modeling, relevant parameters are presented as follows.
(1) The workpieces in the same batch are processed simultaneously.
(2) Interruption is not allowed in the processing procedure of a batch of workpieces.


[^0]:    ${ }^{1}$ Grant by: Liaoning Province doctor startup funds 20131126

(3) No extra workpieces can be added to or removed from a batch of workpieces that are being processed.
(4) The sizes of all workpieces in the model are unit sizes. The number of workpieces is denoted by n , and the i-th workpiece to arrive is denoted by $\mathrm{j}_{\mathrm{i}}$. The set of workpiece groups is J , and the k -th batch is $\mathrm{P}_{\mathrm{k}}$. The set of all batches is shown by B .
(5) There is only one batch machine in the model. The processing time of workpiece $j_{i}$ on the batch machine is $\mathrm{O}_{\mathrm{i}}$.
(6) Each workpiece $j_{i}$ has its own arrival time $R_{i}$.
(7) The number of workpieces that are contained in a batch $\mathrm{P}_{\mathrm{k}}$ is $\mathrm{c}_{\mathrm{k}} \in[\mathrm{S}, \mathrm{L}]$.
(8) The processing time of $\mathrm{P}_{\mathrm{k}}$ on the batch machine is shown by $\mathrm{O}_{\mathrm{P}_{\mathrm{k}}}$, which is equal to the maximum processing time of the workpiece in batch $\mathrm{P}_{\mathrm{k}}$ on the batch machine. That is,

$$
\mathrm{O}_{\mathrm{P}_{\mathrm{k}}}=\max \left(\mathrm{O}_{\mathrm{i}}\right), \quad \mathrm{j}_{\mathrm{i}} \in \mathrm{P}_{\mathrm{k}}
$$

(9) The start time of $\mathrm{P}_{\mathrm{k}}$ on the batch machine is $\mathrm{R}_{\mathrm{P}_{\mathrm{k}}}$. It is equal to or greater than the maximum arrival time $\max \left(\mathrm{R}_{\mathrm{i}}\right)$ of the workpiece in batch $\mathrm{P}_{\mathrm{k}}$ and the maximum job release time $\mathrm{t}_{\mathrm{k}-1}$ of a batch of workpieces on the batch machine.

$$
\mathrm{R}_{\mathrm{P}_{\mathrm{i}}} \geq \max \left(\max \left(\mathrm{R}_{\mathrm{i}}\right), \mathrm{t}_{\mathrm{k}-1}\right)
$$

(10) The decision variable $\mathrm{X}_{\mathrm{j}_{\mathrm{i}}, \mathrm{P}_{\mathrm{k}}}$ is described as follows.
$\mathrm{X}_{\mathrm{j}, \mathrm{i}, \mathrm{P}_{\mathrm{k}}}=1, \text { if workpiece } \mathrm{j}_{\mathrm{i}}$ is in the same batch as $\mathrm{j}_{\mathrm{i}}$ 0 , otherwise
(11) The completion time of batch $\mathrm{P}_{\mathrm{k}}$ on the batch machine is $\mathrm{E}_{\mathrm{P}_{\mathrm{k}}}$

$$
\mathrm{E}_{\mathrm{P}_{\mathrm{k}}}=\mathrm{R}_{\mathrm{P}_{\mathrm{k}}}+\mathrm{O}_{\mathrm{P}_{\mathrm{k}}}, \mathrm{P}_{\mathrm{k}} \in \mathrm{~B}
$$

According to the constraints above, the mathematical model of parallel batch scheduling problem discussed in this paper is shown as follows.

$$
\begin{aligned}
& \min \mathrm{C}_{\max }=\max \left(\mathrm{E}_{\mathrm{P}_{\mathrm{k}}}\right), \quad \mathrm{P}_{\mathrm{k}} \in \mathrm{~B} \\
& \text { S.T. } \sum_{\mathrm{P}_{\mathrm{k}} \in \mathrm{~B}} \mathrm{X}_{\mathrm{j}_{\mathrm{i}}, \mathrm{P}_{\mathrm{k}}}=1, \forall \mathrm{j}_{\mathrm{i}} \in \mathrm{~J} \\
& \sum \mathrm{X}_{\mathrm{j}_{\mathrm{i}}, \mathrm{P}_{\mathrm{k}}} \leq \mathrm{S}, \forall \mathrm{j}_{\mathrm{i}} \in \mathrm{~J}, \forall \mathrm{P}_{\mathrm{k}} \in \mathrm{~B} \\
& \mathrm{O}_{\mathrm{P}_{\mathrm{i}}}=\max \left(\mathrm{O}_{\mathrm{i}}\right), \forall \mathrm{P}_{\mathrm{k}} \in \mathrm{~B}, \mathrm{i} \in \mathrm{P}_{\mathrm{k}} \\
& \mathrm{R}_{\mathrm{P}_{\mathrm{i}}} \geq \max \left(\max \left(\mathrm{R}_{\mathrm{i}}\right), \mathrm{t}_{\mathrm{k}-1}\right) \\
& \mathrm{E}_{\mathrm{P}_{\mathrm{k}}}=\mathrm{R}_{\mathrm{P}_{\mathrm{k}}}+\mathrm{O}_{\mathrm{P}_{\mathrm{k}}} \\
& \mathrm{X}_{\mathrm{j}_{\mathrm{i}}, \mathrm{P}_{\mathrm{k}}}=\{0,1\}, \forall \mathrm{j}_{\mathrm{i}} \in \mathrm{~J}, \forall \mathrm{P}_{\mathrm{k}} \in \mathrm{~B}
\end{aligned}
$$

Formula (5) shows that the objective function of the model is to minimize the maximum production cycle. Formula (6) ensures that each workpiece can only be distributed to one batch. Moreover, formula (7) defines that the overall size of workpieces that are distributed to one batch cannot be larger than the maximum capacity of batch machine. Formula (8) shows that the processing time of each batch on the m-th parallel machine is equal to the longest processing time of workpiece in this batch. Furthermore, formula (9) shows that the start time of processing of each batch on each batch machine is equal to or greater than the lastest arrival time and maximum job release time of the workpiece in the batch on the parallel machine. Finally, formula (10) shows that the completion time of one batch on a certain parallel machine is equal to the sum of start time and processing time on the machine.

## III. IcGA

cGA is a type of EDA. It does not directly operate on the individuals of the group but represents the change of individuals through statistical probability distribution of the group, which is different from the genetic algorithm. This processing method is derived from random walk model and the mechanism of poplulation-based incremental learning.

The operation process of cGA is simple and clear, and it only requires saving the probability distribution on different gene positions of the individual. However, when complicated problems are solved with cGA, the probability model is likely to premature since the group size of each generation is only 2 , and then the model easily generates the local minimum. Moreover, in cGA, each generation will give up the original individual to generate new groups according to the probability model. Hence the superior individuals in the system cannot be preserved. That is to say, the superior individual may contribute to the probability model for only once, and the optimal solution that the algorithm solves is not necessarily the best individual during the searching process of algorithm. Therefore, addressing the drawback of cGA in the process of solving complicated problem, the algorithm is improved as follows by keeping the algorithm simple and clear.

1. The group size is increased, and two individuals are still generated by the probability matrix each time. The fitness values of the individuals are compared. The superior individual is preserved and the inferior one is rejected. Then another new individual is generated by the probability model to be compared with the original superior one. The superior one is reserved, and the inferior one is rejected. In this way, the process does not stop until the generated individual satisfies the assumed group size, and then the superior ones are selected to update the probability model. The process can guarantee that the individuals of each generation used to update the probability model are superior ones in the group (not the superior ones between two individuals). Then the probability model can converge in the right direction.
2. The superior individuals in each generation are preserved to be compared with the next generation. Two new individuals are generated in the standard cGA. In this way, the contributions of superior individual and ordinary individual to the probability model are the same, and the algorithm will be affected. Moreover, the final individual solved by the algorithm may not necessarily be the best one during the searching process. Therefore, combining the advantages of traditional genetic algorithm, the superior individuals in each generation are preserved to be compared with the next generation.

The flow chart of improved cGA is shown as Figure 1 .

![img-0.jpeg](img-0.jpeg)

Figure 1 Flow Chart of Improved cGA
IV. CGA FOR SOLVING THE PARALLEL BATCH SCHEDULING

## A. Probabilistic Model

In the EDA, new individuals are generated by establishing the probability model and through sampling. Hence whether the probability model is reasonable is crucial to the performance of EDA. In this section, the probability model based on the workpiece batches is proposed to fully represent the relationship whether the workpieces belong to the same batch.

The probability model of algorithm is a $\mathrm{n} \times \mathrm{n}$ lower triangular matrix Z , where the row and column represent the workpiece. The sequence of workpieces ranked by the arrival time is $\mathrm{q}:\left(\mathrm{j}_{1}, \mathrm{j}_{2} \ldots \mathrm{j}_{\mathrm{n}}\right) . \mathrm{Z}(\mathrm{i}, \mathrm{j})(0 \leq$ $\mathrm{j}<i \leq \mathrm{n})$ is the probability that the i-th workpiece is from the same batch as the j -th workpiece during the sampling process. $\mathrm{Z}(\mathrm{i}, \mathrm{j})(0 \leq \mathrm{i} \leq \mathrm{n}, \mathrm{j}=\mathrm{i})$ is the probability that the i-th workpiece is from different batches from the workpiece in $(0,1,2, \ldots, \mathrm{i}-1)$ of q . The matrix Z reflects the probability relationship of workpiece batches numerically. The larger the $\mathrm{Z}(\mathrm{i}, \mathrm{j})$ is, the higher the probability that the i-th workpiece is in the same batch as the j -th workpiece is. The quality of solution will be improved if the i-th one and the j-th one are in the same batch.

Since each element $\mathrm{Z}(\mathrm{i}, \mathrm{j})(0 \leq \mathrm{j} \leq \mathrm{i} \leq \mathrm{n})$ in matrix Z represents the probability that an event occurs, $\mathrm{Z}(\mathrm{i}, \mathrm{j}) \in[0,1]$. For a certain workpiece $\mathrm{j}_{\mathrm{i}}$, the sum of probabilities that it belongs to the same batch as some workpiece in $(0,1,2, \ldots, \mathrm{i}-1)$ before i in q and that it belongs to different batches from the workpiece in ( $0,1$, $2, \ldots, \mathrm{i}-1)$ is equal to or greater than 1 . To make the sampling convenient, when the probability model is initialized, each row in the matrix of probability model needs to be normalized to make the probability model to be a random matrix. Moreover, the sum of probabilities of each row is ensured to be 1 in the process of updating the probability model.

$$
\forall \mathrm{i}, \sum_{\mathrm{i}=1}^{\mathrm{i}} \mathrm{Z}(\mathrm{i}, \mathrm{j})=1,(0 \leq \mathrm{j} \leq \mathrm{i} \leq \mathrm{n})
$$

## B. Initializing the Probability Model

To promote the accuracy of initial probability model, the model is established by using statistical methods. The main procedures are as follows.

Step 1 Establishing the Probability Model for Statistical Sampling

The probability model A is a probability model established for obtaining the statistical samples. The distribution of samples should be guaranteed to be uniform. The row of model represents the workpiece, and the column represents the batch. For the workpiece group, the largest batch is $\operatorname{Max}=\left[\binom{2}{1}\right]$. Hence the probability model A is a $\mathrm{n} \times$ Max matrix, where $\mathrm{A}(\mathrm{i}, \mathrm{k})$ represents the probability that workpiece $\mathrm{j}_{\mathrm{i}}$ is distributed to $\mathrm{P}_{\mathrm{k}}$.

Since each element $\mathrm{A}(\mathrm{i}, \mathrm{k})$ in matrix A represents the probability that an event occurs, $\mathrm{A}(\mathrm{i}, \mathrm{j}) \in[0,1]$. For a certain workpiece located at i , it will be processed in some batch. Hence $\forall \mathrm{i}, \sum_{\mathrm{i}=1}^{\mathrm{Max}} \mathrm{A}(\mathrm{i}, \mathrm{k})=1$, that is, the sum of elements in each row of matrix A , is 1 . To ensure that the solution space is sampled uniformly in the initial phase of algorithm, the probability matrix A is initialized according to the following method.

$$
\mathrm{A}(\mathrm{i}, \mathrm{k})=\frac{1}{\operatorname{Max}}
$$

In the probability model, the probability relationship between different workpieces in the group is not established. Moreover, the probabilities that a certain workpiece is distributed to any batch are equal during sampling. In this way, the uniformity of sampling is guaranteed.

Step 2 Statistical Sampling
Statistical sampling is a process to obtain a certain number of samples through sampling according to the probability model. The sampling is performed according to the arrival sequence of the workpieces during the process. For a certain workpiece, the batch to which it belongs is determined through roulette wheel selection. In the sampling process, if batch $\mathrm{P}_{\mathrm{k}}$ has already reached the maximum capacity S , then all the elements in the k -th column in matrix A are set as 0 (that is, no new workpieces are included in the batch.), and the rest columns are normalized. After the distributions of all workpieces are accomplished, the latest arrival time $\max \left(\mathrm{R}_{\mathrm{i}}\right)$ of the workpiece in each batch can be obtained. According to the sequence of $\max \left(\mathrm{R}_{\mathrm{i}}\right)$, each batch is processed on the batch machine.

N individuals are obtained according to the procedures above, and the longest completion times of each individual are obtained. The first $\delta(0<\delta<1$, which indicates the proportion of the chosen superior individuals in the whole group) individuals with the highest fitness values are selected as the superior individual BetterGroup.

Step 3 Initializing the Probability Model
For workpiece $\mathrm{j}_{\mathrm{i}}$, the numbers $\left(\mathrm{c}_{1}, \mathrm{c}_{2}, \ldots, \mathrm{c}_{\mathrm{i}-1}\right)$ of the workpieces $\left(\mathrm{j}_{1}, \mathrm{j}_{2}, \ldots, \mathrm{j}_{\mathrm{i}-1}\right)$ in superior group BetterGroup belonging to the same batch as workpiece $\mathrm{j}_{\mathrm{i}}$ are calculated. Moreover, $\left(\mathrm{c}_{1} /(\delta \times \mathrm{N}), \mathrm{c}_{2} /(\delta \times \mathrm{N}), \ldots\right.$, $\left.\mathrm{c}_{\mathrm{i}-1} /(\delta \times \mathrm{N})\right)$ are assigned to $(\mathrm{Z}(\mathrm{i}, 1), \mathrm{Z}(\mathrm{i}, 2) \ldots \mathrm{Z}(\mathrm{i}, \mathrm{i}-$ 1) ), respectively. They represent the initial probabilities that workpiece $\mathrm{j}_{\mathrm{i}}$ is in the same batch as $\left(\mathrm{j}_{1}, \mathrm{j}_{2}, \ldots\right.$, $\mathrm{j}_{\mathrm{i}-1}$ ). In addition, the numbers $c_{i}$ of the workpieces $\left(j_{1}\right.$,

$\left.\mathrm{j}_{2}, \ldots, \mathrm{j}_{\mathrm{i}-1}\right)$ in superior group BetterGroup belonging to different batches as $\mathrm{j}_{\mathrm{i}}$ are calculated. Then $\mathrm{c}_{\mathrm{i}} /(\tilde{n} \times \mathrm{N})$ is assigned to $\mathrm{Z}\left(\mathrm{j}_{\mathrm{i}} \mathrm{j}\right)$, which represents the initial probability that workpiece $\mathrm{j}_{\mathrm{i}}$ is from different batches as $\left(\mathrm{j}_{1}, \mathrm{j}_{2}, \ldots, \mathrm{j}_{\mathrm{i}-1}\right)$. The rest rows are assigned with the initial values according to the procedures above, and each row of the probability model is normalized to obtain the initialized probability model.

## C. Individual Sampling

The process of obtaining a new individual through the probability model is called sampling. In the algorithm proposed in this paper, sampling is performed according to the arrival sequence of workpieces. For the first arriving workpiece $\mathrm{j}_{1}$ in the group, it can choose any batch from $\left(\mathrm{P}_{\mathrm{i}}, \mathrm{P}_{\mathrm{e} . .}, \mathrm{P}_{\text {Max }}\right)$. For the workpiece $\mathrm{j}_{\mathrm{i}}$ ( $\mathrm{i} \neq$ 1 ), it can choose the same batch as a certain workpiece in $\left(\mathrm{j}_{1}, \mathrm{j}_{2} \ldots \mathrm{j}_{\mathrm{i}-1}\right)$ through roulette wheel selection or a different batch from $\left(\mathrm{j}_{1}, \mathrm{j}_{2} \ldots \mathrm{j}_{\mathrm{i}-1}\right)$ in $\left(\mathrm{P}_{\mathrm{i}}, \mathrm{P}_{\mathrm{e} . .}, \mathrm{P}_{\text {Max }}\right)$ if the batch is still vacant. If there is no such batch, then a vacant batch is randomly chosen. For the batch without any vacant positions, since no new workpieces can be added to it, the probability that the workpiece to be sampled is in the same batch as the workpiece is supposed as 0 . Then the model is normalized again. In this way, the process is performed until all the workpieces are distributed. After all the compatible groups are distributed, the latest arrival time $\max \left(\mathrm{R}_{\mathrm{i}}\right)$ of the workpiece in each batch can be obtained. Each batch is processed on the batch machine according to $\max \left(\mathrm{R}_{\mathrm{i}}\right)$.

## D. Updating the Probability Model

The final winner x in each generation is chosen as the superior individual, and the probability model is updated by using the following incremental learning method.
$\mathrm{Z}_{(1+1)}(1, \mathrm{j})=(1-\beta) \mathrm{Z}_{(1)}(1, \mathrm{j})+\frac{\beta}{n} \mathrm{~L}_{\mathrm{ij}}(1)$ (where 1 is the number of iterations) $(1 \leq \mathrm{j} \leq \mathrm{i})$
where n is the number of workpieces that $\left(\mathrm{j}_{1}, \mathrm{j}_{2} \ldots \mathrm{j}_{\mathrm{i}-1}\right)$ are in the same batch as $\mathrm{j}_{\mathrm{i}}$. If all workpieces $\left(\mathrm{j}_{1}, \mathrm{j}_{2} \ldots \mathrm{j}_{\mathrm{i}-1}\right)$ are in different batches as $\mathrm{j}_{\mathrm{i}}$, then $\mathrm{n}=1 . \beta \in(0,1)$ is the learning speed, and $\mathrm{L}_{\mathrm{ij}}(\mathrm{l})$ is the function defined as follows.
If $(1 \leq \mathrm{j}<i)$ :
$\mathrm{L}_{\mathrm{ij}}(\mathrm{l})=\left\{\begin{array}{c}1, \text { if workpiece } \mathrm{j}_{\mathrm{i}} \text { is in the same batch as } \mathrm{j}_{\mathrm{i}} \\ 0, \text { otherwise }\end{array}\right.$
If $(\mathrm{j}=\mathrm{i})$ :

$$
\mathrm{L}_{\mathrm{ij}}(\mathrm{l})=\left\{\begin{array}{c}
1, \text { if workpiece } \mathrm{j}_{\mathrm{i}} \text { is in the different batches } \\
\text { workpieces }\left(\mathrm{j}_{1}, \mathrm{j}_{2} \ldots \mathrm{j}_{\mathrm{i}-1}\right) \\
0, \text { otherwise }
\end{array}\right.
$$

It can be proved that the sum of each rows in the probability matrix after updating is still 1 through formula (14). The randomness of the matrix of probability model is guaranteed. Through iterations for many times, the probability matrix tends to be mature. The maximum
number of iterations (MaxGen) is supposed as the termination condition of algorithm in this paper.

## E. Time Complexity Analysis of the Algorithm

The time complexity of workpiece grouping by roulette wheel selection during the sampling process is $\mathrm{O}\left(\mathrm{n}^{2} / 2\right)$. The time complexity of arranging the sequence of each batch is $\mathrm{O}\left(\mathrm{Max}^{2}\right)$. Max is the largest number of batches in practice, and Max $\leq \mathrm{n}$. Moreover, the time complexity of updating the probability model is $\mathrm{O}\left(\mathrm{n}^{2} / 2\right)$. For the key processes such as comprehensive sampling and updating the probability model, the complexity is not high by using the improved cGA. In addition, since the algorithm only preserves two individuals at any moment during the operational process, the space complexity is greatly decreased in comparison with the swarm intelligence algorithm.

## V. SIMULATION TESTING AND COMPARISON

## A. Simulation Examples

The test cases proposed in literature [8] are used. The processing time $O_{i}$ of workpiece is randomly distributed in the interval $[1,50]$. The arrival time of workpiece $R_{i}$ is distributed randomly, and the distribution interval is between 0 and $\mathrm{rC}^{*}$, where $\mathrm{C}^{*}$ is the optimal $\mathrm{C}_{\max }$ value under the condition that all workpieces are supposed to arrive at the same time. $\mathrm{C}^{*}$ can be obtained through the heuristic rule of full batch longest processing time (FBLPT). Moreover, r is the range parameter of the arrival time of workpiece, and it determines the relative frequency that the workpiece arrives. When $\mathrm{r}=0$, all the workpieces arrive at the same time. When r gradually increases, the time interval between the arrivals of workpieces increases, and the number of workpieces processed in the same batch decreases.

Table 1 Grade Classification of Cases

| Factors | Grades |
| :--: | :--: |
| n (number of workpieces) | $20,40,60,80,100$ |
| r (range of arrival time of workpiece) | $0.5,1.0,1.5,2.0$ |
| S (machine capacity) | 5 |

The algorithm is compared from three dimensions, which are the number of workpieces C , the maximum capacity S of machines and the range parameter r of arrival time. See Table (1). The number of workpiece n has 5 grades $(20,40,60,80,100)$. The maximum capacity S of machine is S , and the range of arrival time r has 4 grades ( $0.5,1.0,1.5,2.0$ ). 20 different types of test problems can be generated in total. For each type of problem, 50 cases are generated randomly. Each case is run for 10 times to obtain the average.

## B. Experimental Statistical Result and Comparison

In this study, the simulation environment is the AMD Dual-Core CPU 2.6 GHz with 64bits and memory of 2 GB . Each simulation program of the algorithm is written by C\#. In the following simulation experiment, the improved compact genetic algorithm IcGA $(\beta=0.01, \mathrm{np}=$ $25, \operatorname{MaxGen}=750$ ) is compared with the standard

cGA algorithm $\left(\beta=0.001\right.$, MaxGen $=15000$ ), MMAS-BSJR algorithm, MMAS1 algorithm, MMAS2 algorithm and standard ant colony algorithm AS, respectively [8].

To evaluate the algorithm performance objectively, $\mathrm{I}_{\mathrm{A}}=\frac{\mathrm{C}_{\mathrm{A}}}{\mathrm{LB}}$ is defined as the lower bound (LB) of relative case of algorithm A (represents each algorithm). $\mathrm{C}_{\mathrm{A}}$ shows that the smaller the longest completion time $\mathrm{C}_{\max } \cdot \mathrm{I}_{\mathrm{A}}$ obtained by algorithm A , the nearer the solution obtained by algorithm A is close to the lower bound under the same case, and the better the optimization effect of the algorithm is. The lower bound used in this study has been improved based the lower bound LB3 proposed by LEE. The condition of $R_{j}+O_{j}<R_{C}$ is taken into consideration. Then the LB is much closer to the optimal solution [14] in comparison with LB3. The calculation method for LB is shown as lemma 1.

Lemma (1) The arrival times $R_{i}$ of workpieces are arranged in a non-decreasing order. Suppose that set $B=$ $\left\{\mathrm{j} \mid \mathrm{R}_{\mathrm{j}}+\mathrm{O}_{\mathrm{j}}<\mathrm{R}_{\mathrm{C}}\right\}$.

When $\mathrm{B}=\emptyset$, lower bound $\mathrm{LB}=\mathrm{R}_{\mathrm{n}}+\mathrm{O}_{\mathrm{n}}$.
When $B \neq \emptyset$, lower bound $L B=\max \llbracket \min \llbracket R_{n}+$ $\max \left\{O_{n}, O_{j}\right\}, R_{n}+O_{n}+O_{j}\}$ \.

The average solution quality of each algorithm is shown as Table 5. The ratios of relative lower bound under each condition are the averages of $\mathrm{I}_{\mathrm{A}}$ with each algorithm in 50 test cases, and * represents the quality of optimal solution in this row. It can be found that the result of standard cGA algorithm is not satisfactory, and it can be proved that there is a large drawback when complicated problems are solved with the algorithm. The simulation results in most cases are best by using the improved compact genetic algorithm IcGA. The results are improved to some extent in comparison with other algorithms, which proves the validity of algorithm.

Table 2 Comparison of Solution Qualities of Each Algorithm

| n | R | IcGA | cGA | MMAS-BSJR | MMAS1 | MMAS2 | AS |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 0.5 | $1.481^{*}$ | 2.6 | 1.504 | 1.597 | 1.518 | 1.953 |
|  | 1.0 | $1.170^{*}$ | 2.06 | 1.179 | 1.202 | 1.196 | 1.292 |
| 20 | 1.5 | $1.012^{*}$ | 1.49 | 1.028 | 1.080 | 1.056 | 1.135 |
|  | 2.0 | $1.001^{*}$ | 1.28 | 1.007 | 1.071 | 1.033 | 1.140 |
|  | average | $1.166^{*}$ | 1.857 | 1.179 | 1.237 | 1.200 | 1.380 |
|  | 0.5 | $1.790^{*}$ | 4.171 | 1.820 | 1.938 | 1.794 | 2.000 |
|  | 1.0 | $1.201^{*}$ | 2.4 | 1.215 | 1.228 | 1.203 | 1.330 |
| 40 | 1.5 | $1.017^{*}$ | 1.92 | 1.057 | 1.066 | 1.056 | 1.129 |
|  | 2.0 | $1.006^{*}$ | 1.58 | 1.014 | 1.036 | 1.025 | 1.082 |
|  | average | $1.256^{*}$ | 2.517 | 1.277 | 1.317 | 1.270 | 1.385 |
|  | 0.5 | $2.004^{*}$ | 5.309 | 2.008 | 2.034 | 2.007 | 2.218 |
|  | 1.0 | $1.206^{*}$ | 3.099 | 1.247 | 1.258 | 1.248 | 1.320 |
| 60 | 1.5 | $1.022^{*}$ | 2.066 | 1.029 | 1.039 | 1.028 | 1.059 |
|  | 2.0 | $1.002^{*}$ | 1.653 | 1.010 | 1.022 | 1.013 | 1.053 |
|  | average | $1.309^{*}$ | 3.031 | 1.324 | 1.338 | 1.324 | 1.413 |
|  | 0.5 | 2.137 | 5.349 | 2.117 | 2.297 | $2.091^{*}$ | 2.249 |
|  | 1.0 | $1.236^{*}$ | 3.099 | 1.253 | 1.265 | 1.250 | 1.298 |
| 80 | 1.5 | $1.024^{*}$ | 2.066 | 1.031 | 1.030 | 1.026 | 1.067 |
|  | 2.0 | $1.003^{*}$ | 1.636 | 1.010 | 1.015 | 1.012 | 1.051 |
|  | average | $1.350^{*}$ | 3.038 | 1.353 | 1.402 | 1.345 | 1.416 |
|  | 0.5 | 2.255 | 5.431 | $2.238^{*}$ | 2.324 | 2.246 | 2.404 |
|  | 1.0 | $1.260^{*}$ | 3.257 | 1.267 | 1.297 | 1.279 | 1.337 |
| 100 | 1.5 | $1.019^{*}$ | 2.153 | 1.035 | 1.041 | 1.032 | 1.054 |
|  | 2.0 | $1.005^{*}$ | 1.752 | 1.005 | 1.011 | 1.007 | 1.024 |
|  | average | $1.384^{*}$ | 3.148 | 1.386 | 1.418 | 1.391 | 1.455 |

The variation trends of ratios of relative lower bounds in IcGA with different grades of arrival time $r$ of workpieces and number n of workpieces are shown in

Figure (2) and Figure (3). It can be seen from Figure (4) and Figure (5) that as $r$ increases, the ratio of relative lower bound decreases. This is mainly because when $r$ increases, the time interval between the arrivals of two

workpieces increases. The relationship between workpieces in terms of time weakens. That is to say, the probability relationship between workpieces becomes more clear, and the number of local minimums in the solution space decreases. The convergence direction of algorithm is stable during the convergence process. Hence approximate optimal solution can be easily found by the proposed algorithm. Moreover, the distance between the lower bound obtained by the calculation method introduced in this paper and the actual optimal solution are negatively correlated with the arrival time $R_{n}$ of the latest workpiece. Hence when $r$ increases, the arrival time $R_{n}$ of last workpiece increases. The distance between the lower bound and the optimal solution becomes smaller, and the ratio of relative lower bound decreases as well. It is shown in Figure (5) that when the number n of workpiece increases, the ratio of relative lower bound increases. This is because as the size of problem increases, the increase of lower bound of the case is polynomial, and the increase of solution space is exponential. Therefore, under the same parameter configuration, the ratio of relative lower bound in large-scale case is larger than that in small-scale case. The learning speed can be reduced by increasing the number of iterations to enhance the algorithm, and then the searching ability for large-scale problem can be increase.
![img-2.jpeg](img-2.jpeg)

Figure 2 Variation Trend of the Solution Quality by IcGA with the Variation of $r$
![img-2.jpeg](img-2.jpeg)

Figure 3 Variation Trend of the Solution Quality by IcGA with the Variation of n

## VI. CONCLUSION

A new approach for solving the batch scheduling problem with arrival time by using the estimation of distribution algorithm is proposed in this paper. For unequal arrival time of workpieces and the characteristics of batches, the probability model based on the workpiece groups is designed. The model effectively reflects the probability relationship whether different workpieces are
from the same batch. The searching speed and ability of searching for the optimal solution of the algorithm have been improved. Moreover, the probability model is initialized through statistical sampling performed using the sampling probability model that is irrelevant to variables. In this way, the accuracy of initialized probability model is promoted. The mechanism of generating and evolving groups by cGA in the estimation of distribution algorithm is improved by referring to the characteristics of other algorithms. The drawback that the cGA algorithm is easy premature is overcome. On this basis, the corresponding individual sampling and probability updating method are designed. Then the estimation of distribution algorithm for solving the batch scheduling problem with arrival time of workpiece is proposed. Finally, the validity and robustness of the algorithm are proved through experimental verification and comparison. Future research is to design reasonable probability model for the batch scheduling problems in other conditions such as workpiece with different sizes, interruptible process of workpieces and different workpiece groups. Moreover, local search strategies should be introduced by referring to good mechanism of other algorithms to further expand the application of estimation of distribution algorithm in the field of batch scheduling.

## REFERENCES

[1] Li Xiao Lin. Research on Scheduling Batch Processing Machines in Paralled[D]. University of Science and Technology of China,2011.
[2] S. Wbster and K.R. Baker. Scheduling groups of jobs on a single machine. Operations Research[J], 43(1995),692-703.
[3] S..Albersand P. Brueker. The complexity of one machine batching problem. Discrete Applied Mathematics [J], 46(1993),87-107.
[4] P. Baptiste. Batching identical jobs[J]. Mathematical Methods of Operations Research, 52(2000),355-367.
[5] C.Y. Lee, R. Uzsoy and L.A. Martin-Vega, Efficient algorithms for scheduling semiconductor burn in operations. OperationsResearch[J], 40(1992),764-775.
[6] Ikura Y, Gimple M. Efficient scheduling algorithms for a single batch processing machine [J]. Operations Research Letters, 1986, 5(2): 61-65.
[7] WANG Shuan-shi, CHEN Hua-ping, CHENG Ba-yi. Minimizing makespan on a single batch processing machine with non-identical job sizes using ant colony optimization. Journal of Management Science In China,2009,12(6): 72-82.
[8] Xu R, Chen H P, Li X P. Makespan minimization on single batch-processing machine via ant colony optimization[J]. Computers \& Operations Research, 2012, 39(3): 582-593.
[9] XU Rui, CHEN Hua-ping, ZHU Jun-hong. Research on batch scheduling problem with job release time based on max-minant system. Journal of Systems Engineering,2001,26(4):474-484.
[10] ZHOU Shu-De, SUN Zeng-Qi. A Survey on Estimation of Distribution Algorithms[J]. Acta Automation Sinica, 2007,33(2):113-121.
[11] He Xiao-juan. Estimation of Distribution Algorithm and It's Application in Scheduling Problem Solving[D]. Lanzhou University of Technology.
[12] Naeem M, Lee D. Estimation of Distribution algorithm for sensor selection problems[C].Radio and Wireless Symposium, 2010 IEEE. Washington, DC: IEEE, 2010:388-391.
[13] LIUXin-liang, ZHANG Tao, GUO Bo. Model of spare parts optimization based on estimation of distribution algorithms[J]. SYSTEMS ENGINEERING-THEORY \&PRACTICE, 2009(2).
[14] DOU Li-Hua, WANG Gao-peng, Chen Jie etc. A hybrid algorithm of computing cannonball dispersion evenness[J]. CONTROL THEROY \& APPLICATION,2009, 26(6):624-628.