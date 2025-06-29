# An Estimation of Distribution Algorithm for energy-aware Steelmaking Continuous Casting Scheduling 

Guirong WANG ${ }^{1,2, a}$, Qiqiang $\mathrm{LI}^{1, b}$ and Maorong YUAN ${ }^{2, \mathrm{c}}$<br>${ }^{1}$ School of Control Science and Engineering, Shandong University, Jinan, China<br>${ }^{2}$ School of Thermal Energy Engineering, Shandong Jianzhu University, Jinan, China<br>${ }^{a}$ wgrsherry@sdjzu.edu.cn, ${ }^{\mathrm{b}}$ qqli@sdu.edu.cn, ${ }^{\mathrm{c}}$ snownyg@163.com

Keywords: Steelmaking Continuous Casting Scheduling; Estimation of Distribution Algorithm; power consumption.


#### Abstract

This paper addresses the Steelmaking Continuous Casting production scheduling problem(SCC) with power consumption as the main objective. An encoding and decoding scheme is proposed and an effective Estimation of Distribution Algorithm (EDA) is presented to solve it. Simulation experiments indicate that EDA can solve the SCC problem efficiently and has fast speed of convergency.


## Introduction

Steelmaking continuous casting (SCC) is the critical process in steel production. It consists of three stages: steelmaking, refining and continuous casting. Since the process runs in a continuous high-temperature material flow with complicated technological processes and has high energy consumption, the scheduling of the process needs to coordinate the rhythm of steelmaking, refining and casting operations to subject to the limits of temperature dropping, waiting time and to meet the requirements of production continuity. Now, faced with the situation of energy shortages the steel plant considers more enery consumption than productive efficiency. Effective scheduling of this process can save plenty of energy and reduce productive cost.

Most researchers were interested in the SCC scheduling problem. Some of them established the mathematical model and solved it using mathematical programming ${ }^{[1,2]}$, others applying intelligence algorithm ${ }^{[3]}$. Also, various heuristic algorithm or hybrid algorithm are used ${ }^{[4,5]}$. These study think more of productive efficiency and cost. In literature ${ }^{[3,5]}$, the authors think about reducing energy consumption through decreasing wait time of the charges between the process of steelmaking and casting, rather than regarding energy consumption as the objective directly. In our paper, we do just that and with energy consumption of idle of device taken into account as well, it can be extended to solving normal hybrid flow shop problem. In addition, we adopted an effective estimation of distribution algorithm (EDA), it can generate an satisfactory solution in a short time. Details on EDA are described in the following.

## Problem description

Steelmaking continuous casting (SCC) production scheduling problem is to determine in what sequence, at what time and on which machine molten steel should be arranged at various production stages from steelmaking to continuous casting. In the SCC process, the products being processed are handled at high temperature and converted from liquid (molten steel) into solid (drawn billets). There are extremely strict requirements on material continuity and flow time, and special requirements of steel production process have to meet. In this paper we assume that the start casting time of a cast is given by planning department, the cast machines for the casts and cast sequences and charge sequences in each cast are known. The problem to study is determining a charge will be processed by which machine at steelmaking and refining stage and the start time and finish time on the machine. Other assumptions can refer to literature ${ }^{[1,3]}$. The objective function is to minimize the total power consumption of processing $\left(\sum_{E_{e}}\right)$, waiting $\left(\sum_{E_{c}}\right)$ of charges and idle $\left(\sum_{E_{i}}\right)$ of machines.

Coding and Decoding. In this paper, we take the presentation of matrix coding for the SCC scheduling problem. The matrix element $x_{i j}$ indicates that charge $i$ is assigned to machine $j$ to process. There is $x_{i j}=1$ if it is true, and $x_{i j}=0$ if it is false. Row indicates charge and column indicates machine, and the number of columns equals to the total number of machines. For example, in some enterprise, there are two stages of the production process and two identical machines at each stage; four charges will be processed on these machines, so the matrix $X$ can be defined as Eq.1.

$$
X=\left(\begin{array}{lll}
x_{11} & x_{12} & x_{13} & x_{14} \\
x_{21} & x_{22} & x_{23} & x_{24} \\
x_{31} & x_{32} & x_{33} & x_{34} \\
x_{41} & x_{42} & x_{43} & x_{44}
\end{array}\right) \sum_{j=1}^{2} x_{i j}=1 ; \sum_{j=3}^{4} x_{i j}=1 ; \forall i=1,2,3,4
$$

For example, $X=\left(\begin{array}{llll}1 & 0 & 1 & 1 & 0 \\ 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1\end{array}\right)$ indicates that three charges(that is $1,3,4$ ) are assigned to machine 1 at stage 1 ; one charge(that is 2 ) is assigned to machine 2 at stage 1 ; two charges(that is 1,2 ) are assigned to machine 3 (that is the machine 1 at stage2); two charge(that is 3,4 ) are assigned to machine 4 (that is the machine 2 at stage2).

As for the order of the charges on the same machine, it can be obtained according to the start time of the charges on the machine which can be calculated backward from the following stage. According to this, if know the machine assignment of all charges at every stage and their start time at last stage, a whole schedule will be constructed. It's just true for the SCC scheduling problem. Further, we eliminate machine conflicts, and then a feasible schedule will be generated, this is the decoding process.
![img-0.jpeg](img-0.jpeg)

Fig. 1 The general flowchart of the EDA

Table1. A group instance data of process time for 18 charges
![img-1.jpeg](img-1.jpeg)

Fig. 2 Convergence of the EDA

# Estimation of distribution algorithm 

Estimation of distribution algorithm (EDA) is a comparatively novel kind of evolutionary algorithm based on statistical learning. Via statistical analysis, the EDA tries to estimate the underlying probability distribution of the potential individuals and builds a probability model for the promising area by statistical information based on the search experience. Then, the probability model is used for sampling to generate new individuals and is updated in each generation with the elite individuals of the new population. In such an iterative way, the population evolves, and finally satisfactory solutions can be obtained ${ }^{[6]}$. Fig. 1 shows the general flowchart of the EDA. The EDA have been applied to many problems, such as inexact graph matching ${ }^{[7]}$, flow-shop scheduling ${ }^{[8]}$ and so on. To solve the

steelmaking continuous casting problem, we primarily use the EDA to generate the solution of equipment assignment for charges in each iteration.

Corresponding to the encoding scheme for the SCC, the probability model is designed as a probability matrix $P$. The element $P_{k}^{i}$ indicates the probability that charge $i$ is assigned to machine $j$, $k$ indicates the $k i$ iteration and $k=0$ indicates the initial value. For all $i$ and $j, P_{k}^{i}$ is initialized to $P_{k}^{0}=1 / 40$, which ensures that the whole solution space can be sampled uniformly. The probability matrix $P$ is defined as Eq.2. Here, $m_{s}$ indicates the number of machine at stage $s$.

$$
\begin{aligned}
& P=\left(\begin{array}{cccccccccc}
p_{11} & \cdots & p_{1 m_{1}} & p_{1, m_{1}+1} & \cdots & p_{1, m_{1}+m_{2}} & p_{1, m_{1}+m_{2}+\cdots+m_{s-1}+1} & \cdots & p_{1, m_{1}+m_{2}+\cdots+m_{s}} \\
\vdots & \ddots & \vdots & \vdots & \ddots & \vdots & \cdots & \vdots & \ddots & \vdots & \cdots \\
p_{n 1} & \cdots & p_{n m_{1}} & p_{n, m_{1}+1} & \cdots & p_{n, m_{1}+m_{2}} & p_{n, m_{1}+m_{2}+\cdots+m_{s-1}+1} & \cdots & p_{n, m_{1}+m_{2}+\cdots+m_{s}}
\end{array}\right), p_{i, j} \in[0,1] \\
& \sum_{j=1}^{m_{1}} p_{i j}=1, i=1,2, \cdots, n ; \sum_{j=m_{1}+1}^{m_{1}+m_{2}} p_{i j}=1, i=1,2, \cdots, n ; \sum_{j=m_{1}+m_{2}+\cdots+m_{s-1}+1}^{m_{1}+m_{2}+\cdots+m_{s}} p_{i j}=1, i=1,2, \cdots, n ; \cdots
\end{aligned}
$$

In each iteration of the EDA, the new individuals are generated via sampling the solution space according to the probability matrix $P$. For every charge $i$, machine $j$ is selected with a probability $P_{i j}^{i}$. If machine $j$ has already been assigned to a charge, the corresponding probability will be set to 1 , that is $p_{i j}^{k}=1$, then other machines at the same stage can not be assigned to the charge, so the corresponding probability will be set to 0 , that is $p_{i j}^{k}=0$, where $j, j^{\prime} \in s \& j \neq j^{\prime}$. In such a way, an individual is generated until all the charges are assigned to a machine. Then, the objective value of the individual is calculated. Similarly, all $N$ individuals are generated.

Next, we will determine the elite population that consists of the best $e N$ solutions. And then, the probability matrix $P$ is updated according to the following Eq.3.

$$
p_{i j}^{k}=(1-\alpha) \cdot p_{i j}^{k-1}+\alpha \cdot \frac{1}{N} \sum_{i=1}^{e N} I_{i j}^{i}, \forall i, j
$$

Where $\alpha \in(0,1)$ is the learning rate of $P$, and $I_{i j}^{i}$ is the indicator function of the $k i$ individual in the elite population which is defined as Eq. 4 .

$$
I_{i j}^{i}=\left\{\begin{array}{l}
1, \text { if charge } i \text { is assigned to machine } j \\
0, \text { else }
\end{array}\right.
$$

# Numerical simulation 

Instance data. For practical production data cannot acquired easily, and there are no data about the power consumption during the SCC production process, 15 groups data were generated randomly on the basis of practical production in a steel plant. These data were used to test the performance of the EDA in solving the SCC problem. There are three stages and three identical machines at every stage. Table 1 is a group data which includes 3 casts and 6 charges in each cast. Start casting time for the three casts is $95,140,190$ respectively. The processing time was randomly generated from a uniform distribution [30,50]. The power consumption for LD, LF and CC was randomly generated respectively from the uniform distribution [10,20], [45,60] and [15,25]. The power consumption during the waiting period of charge and the idle period of the machine was randomly generated from the uniform distribution $[3,10]$. The planning horizon was set to be 480 minutes.

Parameter design. The parameters of the EDA have important influence to the performance of the algorithm. We use the Taguchi method of design of experiment ${ }^{[9]}$ to find the optimal combination of the following parameters, population size $N$, the proportion $\rho$ of elite population size $e N$ to the whole population size $N$, the learning rate $\alpha$ of probability matrix $P$. According to the experiments and analysis, a better choice of the parameter combination is $N=300, \rho=0.05, \alpha=0.8$ and we set the stopping criterion as 100 iterations or computational results are invariant for continuous 15 iterations.

Results and analysis. The simulation was carried out using Matlab7.0 and run on a PC with 2.6 GHz processor/2 GB RAM. Simulation results manifested that the EDA can generate an optimal schedule for the SCC problem with faster convergence speed, and for every group data the EDA runs 10 times respectively, the average CPU times are all smaller than 10s. Fig. 2 shows the curve of convergence of the EDA. Fig. 3 and Fig. 4 shows respectively the Gantt chart for the same group data. For Fig. 3 the objective value is minimum power consumption, while for Fig. 4 the objective value is minimum makespan. Their corresponding power consumption and makespan are ( $66190 \mathrm{kw}, 393 \mathrm{~min})$ and ( $66515 \mathrm{kw}, 390 \mathrm{~min}$ ). Obviously, by power consumption is regarded as the objective value, the makespan increases 3 min , but the power consumption decreases more. While, we can see that the balanced use of equipments is not very good.
![img-2.jpeg](img-2.jpeg)

Fig. 3 Gantt chart of scheduling solution of EDA(Obj: Power Consumption)
![img-3.jpeg](img-3.jpeg)

Fig. 4 Gantt chart of scheduling solution of EDA(Obj: makespan)

# Conclusions 

In this paper, we studied the SCC problem. The objective is to find a reasonable schedule to minimize the power consumption. Using the EDA, we designed an encoding scheme and a probability matrix model, through updating the probability matrix for each iteration, the optimal solution was finally generated with small time. Testing results showed that the EDA was effective. While, the EDA pays more attention to global exploration, its exploitation capability is relatively limited. In the further study, we will add some appropriate search strategies to the algorithm, so as to balance its exploration and the exploitation abilities.

## References

[1] L.X. Tang, P.B. Luh, J.Y. Liu, et al: International Journal of Production Research, Vol.40(2002), pp.55-77
[2] I. Harjunkoski and I. E. Grossmann: Computers and Chemical Engineering, Vol.25(2001), pp.1647-1660
[3] T.K. Li and Z.X. Su: Chinese Journal of Management Science, Vol.17(2009), pp.68-74
[4] G.H. Liu and T.K. Li: Systems Engineering, Vol.20(2002), pp.44-48
[5] Z.X. Su, T.K. Li and W.L. Wang: Computer Engineering and Applications, Vol.47(2011), pp.242-245
[6] S.Y. Wang, L. Wang and M. Liu: The International Journal of Advanced Manufacturing Technology, 2013, pp.1-14
[7] R.M. Cesar, E. Bengoetxea, I. Bloch, P. Larranaga: Pattern Recognit, Vol.38(2005), pp.2099-2113
[8] Y. Zhang, X.P. Li: Computers \& Industrial Engineering, Vol.61(2011), pp.706-718
[9] J.A. Ghani, I.A. Choudhury, H.H. Hassan: Journal of Materials Processing Technology, Vol.145(2004), pp.84-92

# Machinery Electronics and Control Engineering III 

10.4028/www.scientific.net/AMM. 441

## An Estimation of Distribution Algorithm for Energy-Aware Steelmaking Continuous Casting Scheduling

10.4028/www.scientific.net/AMM.441.1077

## DOI References

[1] L.X. Tang, P.B. Luh, J.Y. Liu, et al: International Journal of Production Research, Vol. 40(2002), pp.5577 .
http://dx.doi.org/10.1080/00207540110073000
[2] I. Harjunkoski and I. E. Grossmann: Computers and Chemical Engineering, Vol. 25(2001), pp.1647-1660. http://dx.doi.org/10.1016/S0098-1354(01)00729-3
[7] R.M. Cesar, E. Bengoetxea, I. Bloch, P. Larranaga: Pattern Recognit, Vol. 38(2005), pp.2099-2113. http://dx.doi.org/10.1016/j.patcog.2005.05.007
[9] J.A. Ghani, I.A. Choudhury, H.H. Hassan: Journal of Materials Processing Technology, Vol. 145(2004), pp.84-92 Fig. 4 Gantt chart of scheduling solution of EDA(Obj: makespan) Fig. 3 Gantt chart of scheduling solution of EDA(Obj: Power Consumption).
http://dx.doi.org/10.1016/S0924-0136(03)00865-3