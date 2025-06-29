# Estimation of Distribution Algorithm with Discrete Hopfield Neural Network for GRAN3SAT Analysis 

Yuan, Y.G, Gao<br>School of Medical Information Engineering, Chengdu<br>University of Traditional Chinese Medicine, Chengdu<br>611137, China; School of Mathematical Sciences, Universiti<br>Sains Malaysia, Penang 11800, Malaysia<br>gaoyuan@student.usm.my

Ju, J.C, Chen ${ }^{\star}$<br>School of Medical Information Engineering, Chengdu<br>University of Traditional Chinese Medicine, Chengdu<br>611137, China; School of Mathematical Sciences, Universiti<br>Sains Malaysia, Penang 11800, Malaysia<br>chenju@cdutcm.edu.cn


#### Abstract

The Discrete Hopfield Neural Network introduces a G-Type Random 3 Satisfiability logic structure, which can improve the flexibility of the logic structure and meet the requirements of all combinatorial problems. Usually, Exhaustive Search (ES) is regarded as the basic learning algorithm to search the fitness of neurons. To improve the efficiency of the learning algorithm. In this paper, we introduce the Estimation of Distribution Algorithm (EDA) as a learning algorithm for the model. To study the learning mechanism of EDA to improve search efficiency, this study focuses on the impact of EDA on the model under different proportions of literals and evaluates the performance of the model at different phases through evaluation indicators. Analyze the effect of EDA on the synaptic weights and the global solution. From the discussion, it can be found that compared with ES, EDA has a larger search space at the same efficiency, which makes the probability of obtaining satisfactory weights higher, and the proportion of global solutions obtained is higher. Higher proportions of positive literals help to improve the model performance.


## CCS CONCEPTS

- CCS CONCEPT Computing methodologies $\rightarrow$ Artificial intelligence.


## KEYWORDS

Hopfield Neural Network, Exhaustive Search, Estimation of Distribution Algorithm, Meta-heuristic

[^0]Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
CACML 2023, March 17-19, 2023, Shanghai, China
(c) 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 978-1-4503-9944-9/23/03... $\$ 15.00$
https://doi.org/10.1145/3590003.3590021

Chengfeng, C.Z, Zheng<br>School of Mathematical Sciences, Universiti Sains<br>Malaysia, Penang 11800, Malaysia<br>1002953832@qq.com

## Yueling, Y.G, Guo

School of Mathematical Sciences, Universiti Sains
Malaysia, Penang 11800, Malaysia
guoyueling1982@163.com

## ACM Reference Format:

Yuan, Y.G, Gao, Chengfeng, C.Z, Zheng, Ju, J.C, Chen, and Yueling, Y.G, Guo. 2023. Estimation of Distribution Algorithm with Discrete Hopfield Neural Network for GRAN3SAT Analysis. In 2023 2nd Asia Conference on Algorithms, Computing and Machine Learning (CACML 2023), March 17-19, 2023, Shanghai, China. ACM, New York, NY, USA, 6 pages. https: //doi.org/10.1145/3590003.3590021

## 1 INTRODUCTION

The principle of Hopfield neural network (HNN) simulating human memory, proposed by J. J. Hopfield [1] in 1982, can solve pattern recognition problems and combinatorial optimization problems. HNN guarantees convergence to a local minimum, but it is possible to converge to a non-global minimum. Discrete Hopfield neural network (DHNN) is the earliest proposed binary neural network. The input and output of the neuron only take $[0,1]$ or $[-1,1]$. In 1990, W. McCulloch and W. Pitts [2] proposed that the relationship between neurons can be handled by propositional logic. In 1992, Wan Abdullah [3] proposed the model of introducing the satisfiability problem into DHNN. Since then, the DHNN based on Satisfiability (SAT) logic programming has undergone a series of developments, including 3SAT [4], MAX3SAT [5], RAN3SAT [6], YRAN2SAT [7], r2SAT [8] combination with DHNN. In 2022, Gao Yuan proposed G-Type Random 3 Satisfiability (GRAN3SAT) [6] so that all combination problems can be satisfied. As the number of clauses increases, the model's task of finding consistent explanations becomes more complex. The exhaustive search (ES) is used as the learning algorithm in the learning phase [9]. ES is less efficient when the search space is large. Estimation of Distribution Algorithm (EDA), also known as the genetic algorithm based on the probability distribution model, was first proposed in 1996 [10]. In 2010, Peralta [11] evaluated methods for evolving neural network architectures using EDA. In 2013, Donate [12] used EDA to introduce the automatic design of artificial neural networks for forecasting time series to improve the final forecast accuracy. According to these related works, we can deduce that the EDA can be combined with the neural network to obtain faster convergence. Based on this, EDA can be considered a promising algorithm to


[^0]:    *Corresponding author.
    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
    CACML 2023, March 17-19, 2023, Shanghai, China
    (c) 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 978-1-4503-9944-9/23/03... $\$ 15.00$
    https://doi.org/10.1145/3590003.3590021

facilitate the learning phase. However, no attempt has been made to exploit the EDA algorithm as an optimal learning method in Discrete Hopfield Neural Networks (DHNN), especially in optimizing GRAN3SAT logic representation and analysis.

In this paper, the GRAN3SAT logic structure is applied in DHNN. To efficiently find a consistent solution to the satisfiability problem, EDA is used as a learning algorithm to search the fitness of neurons. EDA achieves the search and convergence of satisfactory solutions through continuous updating and testing. This study focuses on different proportions of positive and negative literals, analyzes the performance improvement of EDA as a learning algorithm for GRAN3SAT compared with ES, and evaluates the behavior changes of the model at different phases through evaluation indicators.

## 2 EDA IN THE DHNN BASED ON GRAN3SAT

### 2.1 Logic Rules of GRAN3SAT.

GRAN3SAT is a novel non-systematic SAT logic structure represented in conjunctive normal form. Logic consists of a set of different literals and clauses. GRAN3SAT mainly consists of third-order, second-order, and first-order logic clauses randomly. Each literal value is of the form $\{-1,1\}$. The general formula of GRAN3SAT is $P_{G}$, detailed as follows.
a) A set of $N N$ literals: $A_{1}, A_{2}, A_{3}, \ldots \ldots, A_{N N}$. Randomly generated for each literal state.
b) The number of clauses $\left\{x_{i}, y_{i}, z_{i}\right\}$ is randomly generated. $x_{i}$ is the number of third-order logic clauses, $y_{i}$ is the number of second-order logic clauses, and $z_{i}$ is the number of first-order logic clauses.
c) The representation of a clause:

Third-order logic clause: $C_{1}^{(3)}, C_{2}^{(3)}, \ldots \ldots, C_{x_{j}}^{(3)}$, whereby $C_{m_{j}}^{(3)}=\left(A_{m} \vee A_{n} \vee A_{k}\right), m, n, k \in N *$.

Second-order logic clause: $C_{1}^{(2)}, C_{2}^{(2)}, \ldots \ldots, C_{y_{j}}^{(2)}$, whereby $C_{n_{j}}^{(2)}=\left(A_{m} \vee A_{n}\right), m, n \in N *$.

First-order logic clause: $\quad C_{1}^{(1)}, C_{2}^{(1)}, \ldots \ldots, C_{z_{j}}^{(1)}$, whereby $C_{k_{j}}^{(1)}=A_{m}, m \in N *$.

$$
P_{G}=\wedge_{i=1}^{x_{j}} C_{i}^{(3)} \wedge_{i=1}^{y_{j}} C_{i}^{(2)} \wedge_{i=1}^{z_{j}} C_{i}^{(1)}
$$

### 2.2 DHNN

The bipolar neurons of DHNN used in this study are represented by $\{-1,1\}$, and the update equation of neuron state of DHNN is as follows:

$$
S_{i}=\left\{\begin{array}{cl}
1, & \sum_{j k} W_{i j k} S_{j} S_{k} \geq \theta_{i} \\
-1, & \sum_{j k} W_{i j k} S_{j} S_{k}<\theta_{i}
\end{array}\right.
$$

whereby $S_{i}$ is the neuron state, $W_{i j}$ is the synaptic weight in the two neurons. $\theta_{i}$ is the threshold. The cost function of GRAN3SATDHNN is $\operatorname{Cost}_{P_{G}}$, and the formula is as follows:

$$
\begin{gathered}
\operatorname{Cost}_{P_{G}}=\frac{1}{2^{3}} \sum_{j=1}^{x_{i}} \delta_{j_{i}}^{(3)} \delta_{j_{i}}^{(3)} \delta_{j_{i}}^{(3)}+\frac{1}{2^{2}} \sum_{j=1}^{y_{i}} \delta_{j_{i}}^{(2)} \delta_{j_{i}}^{(2)}+\frac{1}{2} \sum_{j=1}^{z_{i}} \delta_{j_{i}}^{(1)} \\
\delta_{j_{x}}^{(k)}=\left\{\begin{array}{lll}
1+S_{A_{j x}}, & \text { when } & A_{j_{x}} \\
1-S_{A_{j_{x}}}, & \text { when } & \neg A_{j_{x}}
\end{array}\right.
\end{gathered}
$$

Whereby $k=1,2,3$. The value of $\eta_{P_{G}}$ describes the logical consistency of $P_{G}$. When the logical inconsistency reaches the minimum value, the weight can be obtained through the Wan Abdullah method [5]. The probability formula for consistent interpretation is as follows:

$$
\lambda\left(\eta_{P_{G}}=0\right)=\left(1-\frac{1}{2^{3}}\right)^{x_{i}}\left(1-\frac{1}{2^{2}}\right)^{y_{i}}\left(1-\frac{1}{2}\right)^{z_{i}}
$$

In the testing phase, the Formula (6)(7) represent the local field formula and the update neuron state. The activation function is the Hyperbolic Tangent Activation Function (HTAF) [7].

$$
\begin{gathered}
h_{i}=\sum_{k \neq i, j} \sum_{j \neq i,} W_{i j k} S_{j} S_{k}+\sum_{j \neq i} W_{i j} S_{j}+W_{i} \\
S_{u_{i}}=\left\{\begin{array}{cl}
1, & \sum_{k \neq i, j} \sum_{j \neq i,} W_{i j k} S_{j} S_{k}+\sum_{j \neq i} W_{i j} S_{j}+W_{i} \geq 0 \\
-1, & \sum_{k \neq i, j} \sum_{j \neq i,} W_{i j k} S_{j} S_{k}+\sum_{j \neq i} W_{i j} S_{j}+W_{i}<0
\end{array}\right.
\end{gathered}
$$

$S_{i}$ and $S_{u_{i}}$ represent the initial state and the update state. $W_{i j k}, W_{i j}$, and $W_{i}$ represent the weights of the third, second and first order of DHNN. The Lyapunov energy function $E n_{P_{G}}$ is obtained by formula(8), and the minimum energy $E n_{P_{G}}^{\min }$ is obtained by formula(9).

$$
\begin{gathered}
E n_{P_{G}}=-\frac{1}{3} \sum_{i} \sum_{j \neq i} \sum_{k \neq i, j} W_{i j k} S_{i} S_{j} S_{k}-\frac{1}{2} \sum_{i} \sum_{j \neq i} W_{i j} S_{i} S_{j}-\sum_{i} W_{i} S_{i} \\
E n_{P_{G}}^{\min }=-\left(\frac{x_{i}}{2^{3}}+\frac{y_{i}}{2^{2}}+\frac{z_{i}}{2}\right)
\end{gathered}
$$

The current DHNN convergence formula (10) is as follows, $t v$ means tolerance value.

$$
\left|E n_{P_{G}}-E n_{P_{G}}^{\min }\right| \leq t v
$$

Introduce GRAN3SAT into DHNN to become GRAN3SAT $D_{D H N N}$.

### 2.3 EDA

The EDA is a population evolution algorithm based on statistical theory. By establishing a probability formula to describe the distribution information of satisfiable solutions in the search range, a new population is generated by random sampling. The evolution of the population is achieved through repeated iterations. The EDA flow is as follows:

Step 1: Initialization.
Initialize the number of populations $N_{p}$. The dimension of each individual is $N_{n}$. The initial population is $X_{\mathrm{i}}=$ $\left\{x_{i j} \mid i=1,2 \ldots, N_{p} ; j=1,2 \ldots, N_{n}\right\}$, where $x_{i j} \in\{1,-1\}$.

Step 2: Calculate the fitness function.
The neuron fitness of the above $X_{i}$ is calculated using the following formula:

$$
\begin{gathered}
f\left(X_{i}\right)=N C-\left(\sum_{m} C_{i}^{(3)}+\sum_{n} C_{i}^{(2)}+\sum_{k} C_{i}^{(1)}\right) \\
C_{i}^{(x)}= \begin{cases}1, & \text { if clauseissatisfied } \\
0, & \text { otherwise }\end{cases}
\end{gathered}
$$

where $N C$ is the number of clauses. The larger the $f\left(X_{i}\right)$, the greater the number of unsatisfied clauses.

Step 3: probability model.
Select dominant populations based on $f\left(X_{i}\right)$. Construct a probability model [13] based on $N$ dominant population, where $N<$

Table 1: Main parameters of GRAN3SAT $T_{D H N N}$.

| Parameter | Value |
| :--: | :--: |
| Different proportions of negative literals $\left(P_{N}\right)$ | $0.1,0.3,0.5,0.7,0.9$ |
| Number of neurons( $N N$ ) | $6 \leq \mathrm{NN} \leq 100$ |
| Activation function | HTAF [7] |
| Number of neuron combination | 100 |
| Relaxation rate | 2 [7] |
| Number of learn and test trial | 100 |
| Tolerance value | 0.001 [7] |

Table 2: List of main parameters in the indicator.

| Parameter | Explanation. |
| :--: | :--: |
| $f_{N C}$ | Maximum fitness achieved |
| $f_{i}$ | Current fitness achieved |
| $W_{W A N}$ | Satisfactory synaptic weights |
| $W_{t}$ | Number of local minimum solution |
| $v_{w}$ | Current number of weights |
| $v_{w c}$ | $v_{w c}=v_{\text {comb }}$ |
| $\varepsilon_{\text {min }}$ | Minimum energy value |
| $\varepsilon_{f}$ | Final energy function value |
| $v_{G}$ | Number of global solutions |
| $v_{t}$ | Number of testing trials |
| $v_{t c}$ | $v_{t c}=v_{t} \cdot v_{\text {combmax }}$ |

$N_{P}$, the formulais as follows.

$$
\begin{gathered}
P\left(x_{j}\right)=\frac{1}{N} \sum_{i=1}^{N} \chi_{i j} \\
\chi_{i j}= \begin{cases}1, & x_{i j}=1 \\
0, & x_{i j}=-1\end{cases}
\end{gathered}
$$

Step 4: Update data.
Randomly generate a new population with a size of $N_{p}$ according to the probability model.

Step 5: Judgment.
Judging whether the conditions for ending the loop are met, if not, jump to Step 2.

Introduce EDA into GRAN3SAT $T_{D H N N}$ to become GRAN3SAT $T_{D H N N}^{E D A}$.

## 3 EXPERIMENTAL SETTINGS

This section introduces the experimental parameters and evaluation metrics of GRAN3SAT $T_{D H N N}$. In the system, the main experimental parameters involved are defined in Table 1. This experiment mainly uses MATLAB 2021a for the simulation.

This paper uses four performance indicators to evaluate the effectiveness of the GRAN3SAT $T_{D H N N}$. These metrics are evaluated by Mean Absolute Error (MAE) for learning error analysis, weight analysis, energy analysis, and global solution analysis. Table 2 describes the parameters used for evaluation in the testing and learning phases. The formula for the learning phase and testing
phase is as follows.:

$$
\begin{gathered}
M A E_{\text {learn }}=\sum_{i=1}^{n} \frac{\left|f_{N C}-f_{i}\right|}{v_{l}} \\
M A E_{\text {weight }}=\frac{\sum_{i=1}^{v_{w c}}\left|W_{W A N}-W_{t}\right|}{v_{w c}} \\
M A E_{\text {energy }}=\frac{\sum_{i=1}^{v_{t c}}\left|e_{m i n}-e_{f}\right|}{v_{t c}} \\
Z M_{\text {test }}=\frac{v_{G}}{v_{t c}}
\end{gathered}
$$

## 4 RESULT AND DISCUSSION

The purpose of this work is to analyze the impact of EDA as a learning algorithm on the overall behavior of GRAN3SAT $T_{D H N N}$ in the learning phase, testing phase. In GRAN3SAT $T_{D H N N}$, the MAE index is used for evaluation. Compared with ES, EDA improves neuron fitness through update iterations and narrows down the search space. This paper discusses the advantages of EDA in the learning phase and testing phase.

Figure 1 and 2 show the performance changes of EDA and ES when the neuron states have different proportions under indicators $R M S E_{\text {learn }}$ and $R M S E_{\text {weight }} . R M S E_{\text {learn }}$ and $R M S E_{\text {weight }}$ respectively quantify the fitness and weight error of neurons. It can be seen that the error of each index of EDA is better than that of ES. There is no obvious difference between GRAN3SAT $T_{D H N N}^{E D A}$ and $G R A N 3 S A T_{D H N N}^{E S}$ under different $P_{N}$, different proportions of literals do not affect the fitness of neuron states of different

![img-0.jpeg](img-0.jpeg)

Figure 1: Changes in $M A E_{\text {learn }}$ of EDA and ES under different $P_{N}$.
![img-1.jpeg](img-1.jpeg)

Figure 2: Changes in $M A E_{\text {weight }}$ of EDA and ES under different $P_{N}$.
models, $R M S E_{\text {weight }}^{E S}$ generally shows a steady state after rising, and $R M S E_{\text {weight }}^{E D A}$ shows a linear rise. This is because as the NN increases, the solution search space of EDA expands, the fitness of neurons decreases, and satisfactory weights can no longer be obtained. To sum up, it is easier to find the optimal weight value for $G R A N 3 S A T_{D H N N}^{E D A}$ than ES in the learning phase. When adjusting the state ratio of neurons, different proportions of neuron states have no significant impact on $G R A N 3 S A T_{D H N N}^{E D A}$.

Figures 3 and 4 show the $G R A N 3 S A T_{D H N N}^{E D A}$ energy error distribution $M A E_{\text {energy }}$ and the global solution proportion $Z M_{\text {test }}$ under different $P_{N}$ during the test phase. It can be obtained that the average energy distribution of $G R A N 3 S A T_{D H N N}^{E S}$ with different
$P_{N}$ is between 4.6 and 5.0. With the decrease of $P_{N}$ under EDA, the energy distribution decreases gradually decreases from 4.5 to 2.8. The energy distribution of ES is generally higher than that of EDA. It can be seen that as the positive state of neurons increases, a is easier to obtain a smaller energy error and $G R A N 3 S A T_{D H N N}^{E D A}$ larger global solution ratio than $G R A N 3 S A T_{D H N N}^{E S}$. It is mainly due to two factors, the first is that it is easier to obtain satisfactory synaptic weights in the learning phase, and the second is that as $P_{N}$ becomes larger, the generated clauses are easier to increase the number of global solutions.

![img-2.jpeg](img-2.jpeg)

Figure 3: Changes in $M A E_{\text {energy }}$ of EDA and ES under different $P_{N}$.

![img-3.jpeg](img-3.jpeg)

Figure 4: Changes in $Z M_{\text {test }}$ of EDA and ES under different $P_{N}$.

## 5 CONCLUSIONS

The learning mechanism of GRAN3SAT ${ }_{D H N N}$ based on the EDA algorithm has the following conclusions: Compared with ES, it has a larger search space at the same efficiency, so the probability of obtaining satisfactory weights in the learning phase is higher, and the proportion of global solutions obtained in the testing phase is higher. As the $N N$ increases, the advantages of EDA become more obvious. Different proportions of negative literals $P_{N}$ has no significant impact on neuron fitness and weight error in the learning phase, and a smaller $P_{N}$ in the testing phase helps to reduce the energy distribution and increase the proportion of the global solution, thereby improving GRAN3SAT ${ }_{D H N N}^{E D A}$ performance.

## ACKNOWLEDGMENTS

Chengdu University of Traditional Chinese Medicine Xinglin Scholar Project.ZRQN2018013,QNXZ2018042.

## REFERENCES

[1] Atul Adya,Hopfield, J. J. 1982. Neural networks and physical systems with emergent collective computational abilities. Proceedings of the national academy of sciences, 79(8), 2554-2558. https://doi.org/10.1073/pnas.79.8.2554
[2] McCulloch W S, Pitts W. 1990. A logical calculus of the ideas immanent in nervous activity. Bulletin of mathematical biology, 52(1), 99-115.W. A. T. W. Abdullah, International journal of intelligent systems. 7, 513-519 (1992). https :/doi.org/10.1007/BF02459570
[3] Abdullah, W. A. T. W. 1992. Logic programming on a neural network. International journal of intelligent systems, 7(6), 513-519. https://doi.org/10.1002/int. 4550070604

[4] Mansor M A, Sathasivam S. 2016. Accelerating activation function for 3satisfiability logic programming. International Journal of Intelligent Systems and Applications, 8(10), 44. https://doi.org/10.5815/ijisa.2016.10.05
[5] Kasihmuddin M S M, Mansor M A, Sathasivam S. 2018. Discrete Hopfield neural network in restricted maximum k-satisfiability logic programming[J]. Sains Malaysiana, 47(6): 1327-1335. htpe://dx.doi.org/10.17576/jsm-2018-4706-30
[6] Karim, S. A., Zamri, N. E., Alway, A., Kasihmuddin, M. S. M., Ismail, A. I. M., Mansor, M. A., Hassan, N. F. A. 2021. Random satisfiability: A higher-order logical approach in discrete Hopfield Neural Network. IEEE Access, 9, 50831-50845. https://doi.org/10.1109/ACCESS.2021.3068998
[7] Gao, Y., Kasihmuddin, M. S. M., Gao, Y., Mansor, M. A., Wahab, H. A., Zamri, N. E., \& Chen, J. 2022. YRAN2SAT: A novel flexible random satisfiability logical rule in discrete hopfield neural network. Advances in Engineering Software, 171, 103169. https://doi.org/10.1016/j.advengsoft.2022.103169
[8] Zamri, N. E., Azhar, S. A., Mansor, M. A., Alway, A., \& Kasihmuddin, M. S. M. (2022). Weighted Random k Satisfiability for $\mathrm{k}=1,2$ (r2SAT) in Discrete Hopfield Neural Network. Applied Soft Computing, 109312. https://doi.org/10.1016/j.asoc. 2022.109312
[9] Gao, Y., Guo, Y., Romli, N. A., Kasihmuddin, M. S. M., Chen, W., Mansor, M. A., Chen, J. 2022. GRAN2SAT: Creating Flexible Higher-Order Logic Satisfiability in the Discrete Hopfield Neural Network. Mathematics, 10(11), 1899. https://doi. org/10.3390/math10111899
[10] Mühlenbein, H., Paass, G. 1996. From recombination of genes to the estimation of distributions I. Binary parameters. In International conference on parallel problem solving from nature. 178-187. Springer, Berlin, Heidelberg. https://doi. org/10.1007/3-540-61723-X_982
[11] Peralta, J., Gutierrez, G., Sanchis, A. 2010. Time series forecasting by evolving artificial neural networks using genetic algorithms and estimation of distribution algorithms. In The 2010 international joint conference on neural networks (IJCNN) (pp. 1-8). IEEE. https://doi.org/10.1109/IJCNN.2010.5596892
[12] Donate, J. P., Li, X., Süncher, G. G., de Miguel, A. S. 2013. Time series forecasting by evolving artificial neural networks with genetic algorithms, differential evolution and estimation of distribution algorithm. Neural Computing and Applications, 22(1), 11-20. https://doi.org/10.1007/s00521-011-0741-0
[13] Mühlenbein, H. 1997. The equation for response to selection and its use for prediction. Evolutionary computation, 5(5), 303-346. https://doi.org/10.1162/evco. 1997.5.3.303