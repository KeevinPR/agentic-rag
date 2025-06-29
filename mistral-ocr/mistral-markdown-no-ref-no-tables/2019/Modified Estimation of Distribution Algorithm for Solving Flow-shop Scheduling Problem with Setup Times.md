# Modified Estimation of Distribution Algorithm for Solving Flow-shop Scheduling Problem with Setup Times 

Mengxuan Feng<br>School of Automation<br>Nanjing University of Science and<br>Technology<br>Nanjing, China<br>fmx0268@163.com<br>Guodong Liu<br>Automatic Control<br>Northern Institute of Automatic Control<br>Technology<br>Taiyuan, China<br>liugd2003@163.com

Jianshou Kong<br>School of Automation<br>Nanjing University of Science and<br>Technology<br>Nanjing, China<br>kongjs77@163.com<br>Shanshan Zhao<br>School of Automation<br>Nanjing University of Science and<br>Technology<br>Nanjing, China<br>Shans_zhao@163.com

Lingyan Liu<br>School of mechanical engineering<br>Nanjing University of Science and<br>Technology<br>Nanjing, China<br>llylgy01@163.com

Yue Zhang<br>School of Automation<br>Nanjing University of Science and<br>Technology<br>Nanjing, China<br>zhang_y@njust.edu.cn


#### Abstract

To solve the flow-shop scheduling problem with sequence dependent setup times, the modified estimation of distribution algorithm was proposed. Considering the setup times dependent on sequence, multi-probability matrixes are employed in the probability model to denote the relative information about jobs in this problem. Meanwhile, the updating mechanism and an automatically adjusting method are improved to adapt to the new probability. A local search is designed to be able to jump out of the local optimum and improve the global optimization ability. Finally, simulation results are compared with other algorithms to demonstrate the effectiveness of the modified EDA.


Keywords-flow-shop scheduling, setup times, the estimation of distribution algorithm, minimizing makespan.

## I. INTRODUCTION

Setup times in general are either ignored or considered as a part of processing time by existing algorithms of the flowshop scheduling problem. In actual production, it is necessary to carry out some operations such as replacing tools, setting machines and sweeping up. The time spent on these operations is independently called setup time, and should not be contained in processing time. As stated above, it is important to research the flow-shop scheduling problem with sequence dependent setup times (FSP/SDST) in theory and practice .

The most study the FSP/SDST by genetic algorithm. Ruiz and Maroto[1] surveyed the flow-shop with sequence dependent setup times and machine eligibility, proposing a hybrid genetic algorithm(HGA). Kaweegitbundit[2] presented a genetic algorithm embedding the NEH heuristic in order to study the FSP/SDST. Ciavota, Minella and Ruiz[3] presented an iterated pareto greedy algorithm with restarting mechanism minimizing the makespan for the FSP/SDST. Sioud and Gagne[4] proposed an enhanced migrating birds optimization(EMBO) based on the STH heuristic, and verified the effectiveness of the algorithm for the FSP/SDST.

Estimation of Distribution Algorithm(EDA) is a population evolution based on statistics theory[5]. The EDA

[^0]employs a probability model for good characteristics of the population. By sampling the probability model to produce new solutions, the EDA insures a direction of evolution. Currently, EDA has been adopted to obtain various shop scheduling solutions. Jarboui, Eddaly and Siarry[6] proposed an EDA added a variable neighborhood search to obtain the flow-shop scheduling solution. Wang et al.[7] surveyed the flexible flow-shop scheduling problem, proposing an effective EDA. While sampling to generate new solutions, it can be hard to continue to sample with the sum of the probability model getting smaller. Tang et al.[8] surveyed the flexible flow-shop scheduling problem, designing an automatically adjusting method for the probability model to solve this problem in sampling.

Based on these analyses, this paper put forward a modified estimation of distribution algorithm (MEDA) to study the flow-shop scheduling problem with sequence dependent setup times with makespan criterion (FSP/SDST-Cmax). Sequence dependent setup times mean, for each job, the setup times depend not only on the machines but also on the job right before. Therefore, the probability model is designed into multi-probability matrixes to replace a single probability matrix. Accordingly, the updating mechanism and the automatically adjusting method are improved to adapt to the new probability model. In this condition, a roulette wheel employs conditional probability instead of total probability in sampling to produce new solutions. Besides, a local search is designed to be able to jump out of the local optimum with some probability. Finally, simulation results are compared with other algorithms to demonstrate the effectiveness of the MEDA in the FSP/SDST-Cmax.

## II. Flow-SHOP SCHEDULing MODEL WITH SETUP Times

## A. Problem Description

FSP/SDST-Cmax can be described as follows: There are n jobs, which are in a specific sequence, to be processed by m machines. It is necessary to consider a setup time before continuing the next job. This setup time is not only related to the machines but also to the job sequence. The objective is to determine the job processing sequences to minimize the


[^0]:    This paper is supported by the National Science Foundation for Young Scientists of China (Grant NO.51705256).

maximum completion time of all jobs. Meanwhile, it assumes beforehand: In the very initial moment, jobs and machines are unoccupied; There is an infinite buffer between any two machines; Any operation is uninterruptible; The job sequence is the same on each machine; Each machine can only process jobs one after another. Similarly, a job cannot be on multiple machines at one time.

## B. Variable Definitions

$i$ : the job number.
$k$ : the machine number.
$n$ : the total number of jobs.
$m$ : the total number of machines.
$\pi$ : one sequence of jobs.
$l$ : the sequence position number of jobs.
$\pi(l)$ : job with position number $l$.
$S_{\pi(l), k}$ : starting time of job $\pi(l)$ on k machine.
$P_{\pi(l), k}$ : processing time of job $\pi(l)$ on k machine.
$C_{\pi(l), k}$ : completion time of job $\pi(l)$ on k machine.
$S_{l} \pi(l-1) \pi(l), k$ : setup time of job $\pi(l)$ on k machine right after job $\pi(l-1)$.
$C_{\max }(\pi)$ : the maximum completion time of the job sequence $\pi$.

## C. Mathematical Model

The optimization objective is minimizing makespan. The mathematical model can be formulated:

$$
\text { Makespan }=C_{\max }(\pi)
$$

Minimize makespan:

$$
\min \left(C_{\max }(\pi)\right)=\min \left(\max \left(C_{\pi(l), m}\right)\right)
$$

Subject to:

$$
\begin{gathered}
C_{\pi(l), \mathrm{k}}=S_{\pi(l), k}+P_{\pi(l), k} \\
S_{\pi(l), 1}=0, l=1, k=1 \\
S_{\pi(l), k}=C_{\pi(l), k-1}, l=1, k=2,3, \ldots, m \\
S_{\pi(l), 1}=C_{\pi(l-1), 1}+S t_{\pi(l-1) \pi(l), 1} \\
k=1, l=2,3, \ldots, n \\
S_{\pi(l), k}=\max \left(C_{\pi(l-1), k}+S t_{\pi(l-1) \pi(l), k}, C_{\pi(l), k-1}\right)
\end{gathered}
$$

$$
\begin{gathered}
l=2,3, \ldots, n, k=2,3, \ldots, m \\
\max \left(C_{\pi(l), m}\right)=C_{\pi(n), m}
\end{gathered}
$$

Equation (3) defines the completion time of job $\pi(l)$ on k machine; Equation (4) (5) define the starting time of job $\pi(1)$ on machine 1 and machine k , and ensure a job cannot be on multiple machines at one time; Equation (6) (7) define the starting time of job $\pi(l)$ on machine 1 and machine k , and indicate each machine can only process jobs one after another; Equation (8) indicates that makespan is equal to the completion time of job $\pi(n)$ on machine m .

## III. The Modified Estimation of Distribution Algorithm

This section presents a MEDA to solve the FSP/SDSTCmax, and explains the solution representation, the population initialization, the probability model, the updating mechanism and the automatically adjusting method, and the probabilisticjumping local search.

## A. Brief Introduction of the basic EDA

EDA is a population evolution based on statistics theory. The EDA updates the probability model from promising subpopulation, then the model is sampled to produce new solutions. It models the distribution of promising subpopulation to avoid destroying good patterns like the traditional evolution algorithm does. The basic working principle of EDA illustrates as follows:

Step 1: Initialize a population contains N solutions.
Step 2: Sort the solutions by fitness values in descending order.

Step 3: Select the top E solutions. Get the statistics about the positions in these solutions, and update the probability matrixes.

Step 4: Sample the updated probability matrixes, and generate new solutions.

Step 5: Arrange the new solutions in descending order of fitness values.

Step 6: Select the top E solutions for the local search.
Step 7: If the termination condition is not met, return to step 2; Otherwise, output optimal solution.

## B. Solution Representation and Initialization Mechanism

The population is composed by the solutions of the FSP/SDST-Cmax. Equation (9) illustrates that each solution can be constructed by an order of n jobs. The order indicates the sequence of processing jobs on each machine.

$$
\pi=\{\pi(1), \pi(2), \ldots, \pi(n)\}
$$

NN-MNEH heuristic algorithm and random generation method are used for initialization. The NN-MNEH heuristic[9] obtains a part of the initial population to guarantee the quality of solutions. And the random generation method generates the rest randomly to ensure the diversity of population.

## C. Probability Model

It is critical to construct an appropriate probability model for the EDA. The probability model represents the characteristics of distribution and affects the sampling result. Considering sequence dependent setup times, the probability model employs n probability matrixes. Each probability matrix reflects a specific position and contains relative information about the jobs in this position and the jobs in the former position. Therefore, a probability model is designed as n probability matrixes as follows:
(1) Job $\pi(1)$ without the previous job:

$$
P_{1}(g)=\left[\rho_{1}(g), \rho_{2}(g), \ldots, \rho_{n}(g)\right]
$$

where $P_{1}(g)$ symbolizes a probability matrix which is at the first position in the $g$-th generation. Besides, in the equation $\rho_{i}(g)=p(\pi(1)=i), \rho_{i}(g)$ represents the probability that the job $i$ is selected at the first position. The initial probability of $\rho_{i}(g)$ is $\rho_{i}(0)=1 / n$. It represents each job has the equal probability to be selected at the first position and the sum of probabilities is 1 in the initial.
(2) Job $\pi(l)$ with the previous job $\pi(l-1)$ :

$$
P_{l}(g)=\left[\begin{array}{ccc}
0 & \cdots & \cdots, g \\
\vdots & \ddots & \vdots \\
\rho_{n l l}(g) & \cdots & \\
& &
\end{array}\right] \leq n
$$

where $P_{l}(g)$ symbolizes a probability matrix which is at the $l$-th position in the $g$ th generation. Besides, in the equation $\rho_{i j l}(g)=p(\pi(l-1)=j, \pi(l)=i), \rho_{i j l}(g)$ represents the probability that the job $i$ is selected at the $l$-th position and right after job $j$. The initial probability of $\rho_{i j l}(g)$ is $\rho_{i j l}(0)=\frac{1}{n(n-1)}$. It represents each job has the equal probability to be selected at the $l$-th position and the sum of probabilities is 1 in the initial.

## D. Updating Mechanism

The elite solutions, which are ranked in the front, are employed to update the probability model in each generation. The updating mechanism is critical to the direction of evolution. To adapt to the new probability model, the updating mechanism is improved accordingly as follows:
(1) Updating $P_{1}(g)$ :

$$
\rho_{i}(g+1)=(1-\alpha) \rho_{i j}(g)+n_{i}(g) \times \frac{\alpha}{E}
$$

where $\alpha$ represents a learning rate, E represents the number of elite solutions, $n_{i j}(g)$ represents the count of the case that job $i$ is at the first position in elite solutions.
(2) Updating $\rho_{i j l}(g)$ :

$$
\rho_{i j l}(g+1)=(1-\alpha) \rho_{i j l}(g)+n_{i j l}(g) \times \frac{\alpha}{E}
$$

where $\alpha$ represents a learning rate, E represents the number of elite solutions, $n_{i j l}(g)$ represents the count of the case that job $i$ is at the $l$-th position and right after job j at the time.

## E. Generating Solutions

The MEDA employs a roulette wheel to sample the updated probability matrixes. The roulette wheel is designed to adapt to the probability model. While one job is determined in a position, it is necessary to adjust the probability matrixes. Otherwise, the sum of the probabilities will reduce and be hard to continue sampling. The way to generate new solutions is conducted as follows:

Step 1: Sampling the probability matrixes by the roulette wheel.
(1) Sampling to select job $\pi(1)$ :

In fact, $P_{1}(g)$ is a $1 \times n$ dimensional matrix, just employing the traditional roulette wheel to sample.
(2) Sampling to select job $\pi(l)$ :
$\rho_{i j l}(g)$ is an $n \times n$ dimensional matrix, the roulette wheel is designed as follows:
$\rho_{i j l}(g)$ indicates the probability of job $i$ is at the $l t h$ position and right after job $j$. Therefore, it can be represented as the joint probability $p(\pi(l-1)=j, \pi(l)=i)$.

According to Bayes theorem:

$$
\begin{gathered}
p(\pi(l)=i \mid \pi(l-1)=j)=\frac{p(\pi(l-1)=j, \pi(l)=i)}{p(\pi(l-1)=j)} \\
p(\pi(l-1)=j)=\sum_{l} p(\pi(l-1)=j, \pi(l)=i)
\end{gathered}
$$

Transform equation (14) (15):

$$
p(\pi(l-1)=j)=\sum_{l} \rho_{i j l}(g)
$$

$$
p(\pi(l)=i \mid \pi(l-1)=j)=\frac{\rho_{i j l}(g)}{\sum_{l} \rho_{i j l}(g)}
$$

Except using the conditional probability ( $p(\pi(l)=i \mid \pi(l-1)=j)$ ) in the equation (17), other operations are same to the traditional roulette wheel, which normally uses a total probability.

Step 2: Automatically adjusting the probability matrixes.
To ensure the sum of the probabilities of the rest jobs is 1 , the $n-l$ matrixes are adjusted as follows:

$$
\rho_{s r t}^{\prime}(g)=\frac{\rho_{s r t}(g) \times p(\pi(t-1)=r)}{p(\pi(t-1)=r)-\rho_{l r t}(g)}
$$

$$
s \neq i, r \in U, s \in U
$$

where job $s$ is the rest unselected, job $i$ is selected by step 1 , $\rho_{\text {srt }}(g)$ represents the probability that job $s$ is selected at the $t$-th position and right after job $r, \mathrm{U}$ is the set of the rest jobs.

Meanwhile, in order to avoid job $i$ reselected, the columns of job $i$ are set to 0 in the $n-l$ matrixes as follows:

$$
\rho_{i r t}^{\prime}(g)=0, r \in U
$$

Equation (18)(19) launch $\sum_{s} \sum_{r} \rho_{s r t}^{\prime}(g)=1$. While sampling to select jobs, it ensures the sum of the probabilities is always 1 by adjusting the probability matrixes.

## F. Probabilistic-jumping Local Search

The local search is able to jump out of the local optimum by some probability to accept an inferior solution. During the initial search, the convergence rate is fast with a small probability to accept that. And then the probability is increasing gradually when search for neighborhood solutions. Whereas, it is able to jump out of the local optimum by accepting the inferior solution with a high probability at the end of the search. The specific method is constructed as follows:

Step 1: Parameters initialization. System state $T=T_{0}$, initial system solution $\pi=\pi_{0}$, initial system target value $c=c_{0}$, system parameter $\varepsilon>1$, number of outer iterations iter $=0$, and neighborhood length $L=$ len.

Step 2: If iter < iter $_{m a x}$ and $T<T_{\text {end }}$, number of inner iterations $i t=0$; Otherwise, jump to step 3.

Step 2.1: If $i t<L$, continue; Otherwise, iter $=$ iter +1 , $T=\varepsilon T$ and jump to step 2.

Step 2.2: Perform the search operations to get a new solution $\pi_{1}$ and a target value $c_{1}$. Calculate $\Delta=c_{1}-c$. If $\Delta \leq 0$, continue; Otherwise, jump to step 2.4.

Step 2.3: Accept the new solution $\pi=\pi_{1}, c=c_{1}$. $i t=i t+1$, jump to step 2.1.

Step 2.4: Calculate $r=\exp \left(-\frac{\Delta}{T}\right)$. Generate $\xi$ randomly in $[0,1)$. If $r>\xi$, accept the new solution $\pi=\pi_{1}, c=c_{1}$. $i t=i t+1$, and jump to step 2.1.

Step 3: Output $\pi_{\min }$, whose target value is $c_{\min }$ in the search history.

Moreover, Step 2.2 employs 3 search operations to generate new solutions. They are swap, inset and reverse.
(1) Swap:

Select two jobs in the job sequence $\pi$ randomly and swap.
(2) Insert:

Select two jobs, $\pi(u)$ and $\pi(v) \quad(1 \leq u<v \leq n)$, in the job sequence $\pi$ randomly. Insert $\pi(v)$ in front of $\pi^{q}(u)$.
(3) Reverse:

Select a block of the job sequence $\pi$ randomly (block $=\left\{\pi^{q}(u), \ldots, \pi^{q}(v)\right\}, 1 \leq u<v \leq n$ ). Reverse the job sequence of the block.

## G. The Flow of the MEDA

The flow chart of the MEDA is illustrated in Figure 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. The flow chart of the MEDA.

## IV. SIMULATION EXAMPLES EXPERIMENT

To verify the effectiveness of the MEDA, the test set consists of 100 instances improved the benchmarks of Taillard[10], where $n=\{20,50,100\}$ and $m=\{5,10,20\}$. The processing times are integers evenly distributed in $[1,99]$, and the setup times are integers evenly distributed in $[0,10]$.

All algorithms are coded in C++. Independent 20 times simulations must be performed to run for each algorithm with 50 iterations.

## A. Parameters Setting

The MEDA has 4 key parameters: population size $N$, learning rate $\alpha$, parameter of the number of elite solutions $\delta$ and neighborhood length $L$, where the number of elite solutions is represented as $E=\delta \times N$.

To analyze the impact of the four parameters on the MEDA, Design of Experiment (DOE) is performed on the SDST10_ta001 instance adopting four factor levels as Table I.

TABLE I. FACTOR LEVEL

Choosing the orthogonal array $L_{16}\left(4^{4}\right)$, the MEDA runs 20 times independently for every parameters combination. The orthogonal array and the response values are demonstrated in Table II.

TABLE II. RESPONSE VALUES

From Table III, the population size is on the first rank, therefore it is the most important effect, while the neighborhood length has less effect than it. The last rank is the learning rate with the least effect. Besides, the performance of the MEDA is better, when the population size is level 3, the learning rate is level 3 , the parameter of the number of elite solutions is level 2, and the neighborhood length is level 3.

Accordingly, the parameters are set as follows: $N=90$, $\alpha=0.1, \delta=0.2, L=12$.

TABLE III. RESPONSE TABLE


## B. Results Comparing

To verify the performance of the MEDA, it is compared with EDA-IG[11], EMBO-STH[4] and HGA[1] in the FSP/SDST. The computational results are scored by the average of relative percentage deviation (ARPD) as follows:

$$
\begin{gathered}
R P D=\frac{M E-\text { Best }}{\text { Best }} \times 100 \% \\
A P R D=\sum R P D / \text { num }
\end{gathered}
$$

Equation (20) defines relative percentage deviation (RPD), where ME is the result of the algorithm, Best is the optimum already known. Equation (21) defines APRD, where num is the size of a set of instances.

From Table IV, the MEDA has the best average of ARPD among all the algorithms. Comparing the MEDA with EDAIG, it is noticed that the EDA is improved except the instances of $100 \times 5$. It can be explained that it is the MEDA which employs the new probability model and automatically adjusting method, and replaces the IG operation to the probabilistic-jumping local search which improve the global search.

Among the MEDA, EMBO-STH and HGA, the MEDA performs the better effective than the others. EMBO-STH provides a better result than HGA, but the difference between EMBO-STH and the MEDA is noticeable. Meanwhile, it is indicated that the MEDA is robustness with a smaller standard deviation.

TABLE IV. COMPARISON OF MEDA, EDA-IG, EMBO-STH AND HGA

## V. CONCLUSION

In this paper, a modified estimation of distribution algorithm (MEDA) is constructed to solve the flow-shop scheduling problem with sequence dependent setup times (FSP/SDST). Considering the setup times relied on sequence, multi-probability matrixes are employed in the probability model to denote the relative information about jobs in this problem. In order to adapt to the new probability model, the updating mechanism is improved. Meanwhile, a roulette wheel and an automatically adjusting method are designed to ensure sampling successfully. Besides, a probabilisticjumping local search is designed to enhance the global search by a probability to help the local search jump out of the local optimum. Comparing the MEDA with three other algorithms, it verifies the MEDA is effective to solve the FSP/SDST, and has the better performance than other algorithms. It is significance to conduct to plan the practical shop scheduling.
