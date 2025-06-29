# Article 

## Estimation of Distribution Algorithm for Energy-Efficient Scheduling in Turning Processes

Fang Wang ${ }^{1,2}$, Yunqing Rao ${ }^{1, *}$, Chaoyong Zhang ${ }^{1}$, Qiuhua Tang ${ }^{3}$ and Liping Zhang ${ }^{3}$<br>1 State Key Lab of Digital Manufacturing Equipment and Technology, Huazhong University of Science and Technology, Wuhan 430074, China; wangfang79@wust.edu.cn (F.W.); zcyhust@mail.hust.edu.cn (C.Z.)<br>2 School of Management, Wuhan University of Science and Technology, Wuhan 430081, China<br>3 School of Machinery and Automation, Wuhan University of Science and Technology, Wuhan 430081, China;<br>tangqiuhua@wust.edu.cn (Q.T.); luck2005net@126.com (L.Z.)<br>* Correspondence: ryq@mail.hust.edu.cn; Tel.: +86-27-8755-9417

Academic Editor: Andrew Kusiak
Received: 29 May 2016; Accepted: 27 July 2016; Published: 15 August 2016


#### Abstract

With the increasing concern for the environment, energy-efficient scheduling of the manufacturing industry is becoming urgent and popular. In turning processes, both spindle speed and processing time affect the final energy consumption and thus the spindle speed and scheduling scheme need to be optimized simultaneously. Since the turning workshop can be regarded as the flexible flow shop, this paper formulates a mixed integer nonlinear programming model for the energy-efficient scheduling of the flexible flow shop. Accordingly, a new decoding method is developed for the optimization of both spindle speed and scheduling scheme simultaneously, and an estimation of the distribution algorithm adopting the new decoding method is proposed to solve large-size problems. The parameters of this algorithm are determined by statistics from a simplified practical case. Validation results of the proposed method show that the makespan is shortened to a large extent, and the consumed energy is significantly saved. These results demonstrate the effectiveness of the proposed mathematical model and algorithm.


Keywords: energy-efficiency scheduling; flexible flow shop; estimation of distribution algorithm; turning processing

## 1. Introduction

With the increasing attention on global warming and climate change, energy-efficient scheduling is becoming an important objective in the process of production [1]. Since about one-half of energy consumption is industrial [2], the reduction of the energy consumption in the manufacturing process is a global concern. Two methods are often used to reduce energy consumption: developing power-efficient machines [3,4] and designing energy-saving manufacturing system frameworks [5,6]. After long-term endeavors, the first method has maintained a good momentum on the single equipment with manufacturing process improvement, material savings, and waste reduction [7-9]. As for the second method, energy-saving through optimization the manufacturing system faces great challenges due to changeable market demand, diversified product structure, and flexible processing routes [10-12], as well as insufficient accurate data of energy consumption [13,14], so researchers still struggle to break down these technical and theoretical barriers.

With respect to the energy-efficient scheduling, the well-known machine turn-on and turn-off scheduling framework has been proposed by Mouzon et al. [15] and further explored by Mouzon and Yildirim [16]. Then Dai et al. [17] applied this framework to the flexible flow shop scheduling problem, and Tang et al. [18] adopted it to solve an energy-efficient dynamic scheduling. Since some machines

and appliances cannot be switched off during the manufacturing process in some workshops [19], a new method of speed scaling framework has been developed by Fang et al. [20]. Under this framework, Fang et al. [20] researched a flow shop scheduling problem with a restriction on peak power consumption, and Liu and Huang [21] studied a batch-processing machine scheduling problem and a hybrid flow shop problem.

The turning workshop typically involves two processes, i.e., rough turning and fine turning, and each process usually can be completed at any one of parallel lathes, and thus the ordinary turning workshop can be regarded as the flexible flow shop. Salvador [22] originally has proposed the flexible flow shop scheduling problem (FFSP) in oil industry, and this problem is also known as hybrid flow shop scheduling problem (HFSP) [23]. For traditional optimization of the flexible flow shop scheduling, Linn and Zhang [24] pointed out that HFSP is a non-deterministic polynomial (NP) problem after they reviewed computational complexities, scheduling objectives, and solving methods. Aiming at solving the NP problem, Kis and Pesch [25] put forward a method to determine the lower bounds, and they also developed a new branch and bound method which is faster than the method of Azizoglu et al. [26]. However, for large-scale scheduling problems, these optimal methods are inefficient due to high demand for computational time and storage space. Therefore, a lot of heuristics and meta-heuristics were put forward, such as the NEH algorithm [27], Palmer algorithm [28], CDS algorithm [29], and genetic algorithm [30]. More new methods were developed, including artificial immune algorithm [31], particle swarm optimization algorithm (PSO) [32], water-flow algorithm [33], quantum-inspired immune algorithm [34], iterated greedy algorithm [35], and intelligent hybrid meta-heuristic [36].

To our best knowledge, most researchers study process parameters and scheduling schemes in turning processing separately except for the work of Lin et al. [37], who proposed a two-stage optimization method to successively find out the optimum process parameters and scheduling scheme for the single-machine scheduling in a turning shop. Obviously, more mathematic models and more methods targeting at the synchronous optimization are necessary to be developed. Aiming at this target, this paper approaches the energy-efficient scheduling of the flexible flow shop in the following ways. First, a mixed integer nonlinear programming model of the energy-efficient scheduling is established and this model can be solved with a GAMS/Dicopt solver. Second, a new decoding method is proposed and integrated into the estimation of distribution algorithm (EDA) to solve the problem, which is an effective and promising algorithm based on the statistical learning theory. Thirdly, the model and EDA are verified in a real case.

The paper is organized as follows. In Section 2, research problem and energy consumption of lathes in the turning process are analyzed in detail. In Section 3, the mixed integer programming nonlinear model of the research problem is put forward. Section 4 presents a new decoding method and adopts an estimation of distribution algorithm to solve the energy-efficient scheduling. The verification of the model and algorithm is reported in Section 5, and conclusions are arrived in Section 6.

# 2. Problem Statement 

### 2.1. Motivating Example

A simplified case of a real turning processing is used as the motivating example for the current research. This case involves two types of processes: rough turning and fine turning. Eleven C630 lathes are employed, five of which are applied for the rough turning and six for the fine turning. Each athe has 12 levels of spindle speed for processing jobs. The transport times among these lathes derive from a statistical survey on the spot. The detailed layout of the turning workshop is shown in Figure 1. According to the production plan, there are 60 rolls of 12 types to be processed. The materials of these rolls may be Cr12MoV, 4Cr5MoSiV1, GCr15, 45\# steel, 3Cr2W8V, or 40Cr. There is a great difference among these rolls in diameter ranging from 66 mm to 550 mm , and in the length varying from 1520 mm to 1846 mm . All the relative data of this real case are provided in Appendix A.

![img-0.jpeg](img-0.jpeg)

Figure 1. Layout of the roll turning shop.

Since environment-friendly and energy saving manufacturing is an urgent requirement, it is highly necessary to both adjust the parameters of rough turning and fine turning like spindle speed and optimize the processing scheme so as to reduce energy consumption effectively.

# 2.2. Problem Description 

Since the fine turning begins only after the rough turning completes, and there is usually more than one lathe for each turning process, this workshop can be regarded as a two-stage flexible flow shop. Meanwhile, energy saving is a new focus in this workshop.

Thus, the problem under consideration can be regarded as a flexible flow shop scheduling problem with two objectives: production efficiency and energy saving. Makespan noted as Cmax, is chosen as the production index evaluator. The energy consumption is evaluated by the total energy consumption noted as TEC.

Utilizing the three-field notation proposed by Graham et al. [38], we express the above problem as $F F_{m}(r) \mid \mid C \max +T E C$, where $F F$ represents the flexible flow shop, $m$ the number of stages, $r$ unrelated parallel machine, || no special constraints, and $C \max +T E C$ the optimization goals.

For the convenience of mathematical modeling of this problem, the turning operations and energy consumption are analyzed in the following.

### 2.3. Analysis of Turning Operations

A turning operation $\left(O_{i k}\right)$ can be defined as: job $i$ is handled on lathe $k$, and it generally needs to pass five steps which are job-loading, lathe starting, job cutting, lathe stopping, and job-unloading. Because a turning operation of $O_{i k}$ contains five sub-operations, the total processing time is the summation of them. Therefore, the total processing time of $O_{i k}$ can be achieved with Equation (1).

$$
T_{i k l}^{c}=t_{i k}^{l}+t_{k l}^{S}+t_{i k l}^{c}+t_{k l}^{D}+t_{i l}^{u}
$$

where, $t_{i k}^{l}$ is the loading time of job $i$ onto machine $k, t_{k l}^{S}$ the time for speeding up the spindle of lathe $k$ to $l$ level, $t_{i k l}^{c}$ the cutting time of job $i$ is processed on the lathe $k$ at the speed level $l, t_{k l}^{D}$ the time for stopping lathe, and $t_{i k}^{u}$ the unloading time of job $i$ from machine $k$.

When job $i$ and machine $k$ are known, $t_{i k}^{l}, t_{k l}^{S}, t_{k l}^{D}$ and $t_{i k}^{u}$ can be seen as parameters, and the total processing time of any turning operation can be expressed by Equation (2) according to Equation (10) in Section 2.4.

$$
T_{i k l}^{s}=t_{i k}^{l}+t_{k l}^{s}+\frac{60 V_{i k}^{c}}{\pi \times a p_{i k} \times f_{i k} \times d_{i}^{0} \times n_{k l}^{c}}+t_{k l}^{D}+t_{i l}^{u}
$$

where, $V_{i k}^{c}$ is the total removed volume from the semi-product of job $i$ by lathe $k$, $a p_{i k}$ the depth of cutting, $f_{i k}$ the feed rate, $d_{i}^{0}$ the semi-product diameter of job $i$, and $n_{k l}^{c}$ the spindle speed of level $l$ of the lathe $k$.

### 2.4. Analysis of Energy Consumption

Lathes are responsible for energy consumption of the turning process [39]. If job loading and unloading are accomplished automatically, their power consumption is fixed. If they are done manually,

the power consumption is not needed. Therefore, alterable energy consumption mainly results from the power consumption of other three operational steps: lathe starting, job cutting, and lathe stopping. $E_{k l}^{s}$ is the power consumed by speeding up the spindle of lathe $k$ to the designated speed level $l$ and that by running without loads before turning jobs. $E_{i k l}^{c}$ is the power consumption by the lathe $k$ handling the job $i$ at the speed level $l$, and it is the total of the power for running the lathe and that for material removal, which is expressed with Equation (3) [40] and Equations (4)-(10) [41], respectively. $E_{k l}^{D}$ is the power consumption of lathe $k$ for braking or stopping the spindle of speed level $l$ after completing jobs.

$$
E_{i k l}^{c}=\left(P_{k l}^{0}+K_{i k l}^{c} \dot{v}_{i k}\right) t_{i k l}^{c}
$$

where $P_{i k}^{0}$ is the power for lathe $k$ of spindle speed level $l$ running without load, $K_{i k l}^{c}$ the energy coefficient of lathe $k$ of spindle speed level $l$ cutting job $i, v_{i k}$ material removal rate of job $i$ on the lathe $k$.

$$
K_{i k l}^{c} v_{i k}=P_{i k l}^{m}=\frac{F_{i k l}^{m} \times v_{i k l}^{c}}{10^{3}}
$$

where $P_{i k l}^{m}$ is the power consumed to remove the extra material of processing job $i$ by the lathe $k$ of spindle speed level $l, F_{i k l}^{m}$ the cutting force of the processing, and $v_{i k l}^{c}$ the linear cutting velocity of the same processing. The definition and evaluation function of $F_{i k l}^{m}$ is similar to that in Machinery Handbook [41], and can be described with Equation (5).

$$
F_{i k l}^{m}=C^{F} \times a p_{i k}^{x_{F m}} \times f_{i k}^{y_{F m}} \times v_{i k l}^{n_{F m}} \times K^{F}
$$

Under general cutting conditions, $x_{F^{m}} \approx 1, y_{F^{m}} \approx 0.75, n_{F^{m}} \approx 0$, and $C^{F}$ is a coefficient related to materials and cutting conditions. $K^{F}$ is also a coefficient for cutting force. The cutting force can be obtained with Equation (6) since the value of these coefficients can be found in Machinery Handbook.

$$
F_{i k l}^{m}=C^{F} \times a p_{i k} \times f_{i k}^{0.75} \times K^{F}
$$

The additional load-loss energy of $P_{i k}^{n}$ will be required in the cutting process [42], and it can be calculated by Equation (7).

$$
P_{i k l}^{n}=b_{k}^{m} \times P_{i k l}^{m}
$$

where $b_{k}^{m}$ is the additional load-loss coefficient, and its value can be adjusted between 0.10 and 0.20 according to the state of lathe $k$ [43]. In the cutting process, the linear velocity of $v_{i k l}^{c}$ can be calculated by Equation (8) [37].

$$
v_{i k l}^{c}=\frac{\pi \times d_{i}^{0} \times n_{k l}^{c}}{60}
$$

If $V_{i k}^{s}$ represents the total removed volume from the semi-product of job $i$ on lathe $k$, the cutting time can be calculated by Equation (9), and combined with Equation (8), it conducts Equation (10).

$$
\begin{gathered}
t_{i k l}^{c}=\frac{V_{i k l}^{s}}{a p_{i k} \times f_{i k} \times v_{i k l}^{c}} \\
t_{i k l}^{c}=\frac{60 V_{i k l}^{s}}{\pi \times a p_{i k} \times f_{i k} \times d_{i}^{0} \times n_{k l}^{c}}
\end{gathered}
$$

Based on the above five Equations (3)-(10), the total power consumption can be calculated by Equation (11).

$$
E_{i k l}=E_{k l}^{s}++\frac{60 V_{i k}^{s} P_{i k l}^{0}}{\pi a p_{i k} f_{i k} d_{i}^{0} n_{k l}^{c}}+\left(1+b_{k}^{m}\right) C^{F} f_{i k}^{-0.25} K^{F} V_{i k}^{s} \times 10^{-3}+E_{k l}^{D}
$$

where the values of $E_{k l}^{s}, E_{k l}^{D}$, and $P_{k l}^{0}$ can be obtained by experimental tests. Since the lathe and spindle speed level are certain, these values are deterministic and thus can be used as parameters.

# 3. Modeling 

From the Equation (11), we can find that the energy consumption for completing a turning operation is inversely proportional to the spindle speed. From Equation (2), we can also find that the completion time is an inverse function of the spindle speed, so the weighted method is suitable for dealing with the two objectives of energy consumption and makespan. Considering this multi-objective optimization problem, the complexity of weighted method is lower than that of Pareto non-dominated method. In the scheduling optimization, except for spindle speeds, all processing parameters are known and certain. Therefore, optimization variables are machine allocation, job sequence, and spindle speed. The presented formulation is based on the following assumptions. Firstly, all of the $n$ jobs and $m$ machines are available for processing at the initial time. Secondly, one machine can process only one job at a time and one job can be processed by only one machine at a time. Thirdly, the spindle speed must be selected among several alternative levels.

## Indices


## Parameters

## Binary Variables

$x_{i k t}=\left\{\begin{array}{l}1, \text { if job } i \text { is processed at event } t \text { on the machine } k \\ 0, \text { otherwise }\end{array}\right.$
$y_{i k l}=\left\{\begin{array}{l}1, \text { if job } i \text { is processed at speed level } l \text { on the machine } k \\ 0, \text { otherwise }\end{array}\right.$

# Positive Variables 

### 3.1. Mathematical Model

$$
\min Z=a \times \frac{T E C}{T E C_{0}}+(1-a) \times \frac{C \max }{C \max _{0}}
$$

$$
\left\{\begin{array}{l}
\sum_{t} \sum_{k \in K_{j}} x_{i k t}=1, \quad \forall i, j \\
\sum_{l \in N_{i k}} \sum_{k \in K_{j}} y_{i k t}=1, \quad \forall i, j \\
\sum_{l \in N_{i k}} y_{i k l}=\sum_{t} x_{i k t}, \quad \forall i, j, k \in K_{j} \\
\sum_{t=1}^{n} x_{i k t} \leqslant 1, \quad \forall j, k \in K_{j}, t \\
\sum_{t=1}^{n} x_{i k t} \geqslant \sum_{t^{\prime}=1}^{n} x_{t^{\prime} k t+1}, \quad \forall k, t<n \\
F_{k t}=S_{k t}+\sum_{t} \sum_{k^{\prime}} {\left[\left(f_{i k}^{l}+t_{k l}^{S}+\frac{60 V_{i k}^{c}}{\pi \times a p_{i k} \times f_{i k} \times d_{i j}^{p} \times n_{k j}^{p}}+t_{k l}^{D}+t_{i l}^{u}\right) \times x_{i k t} \times y_{i k l}\right], \forall k, t} \\
S_{k^{\prime} t^{\prime}} \geqslant F_{k t}+T_{k k^{\prime}}^{d}-M^{o} \times\left(2-x_{i k t}-x_{i k^{\prime} t^{\prime}}\right), \forall i, j<S, j^{\prime}=j+1, k \in K_{j}, k^{\prime} \in K_{j^{\prime}}, t, t^{\prime} \\
F_{k t} \leqslant S_{k, t+1} \forall k, t<n \\
T E C=\sum_{k} \sum_{k^{\prime}} \sum_{l}\left\{\left[E_{k l}^{s}+\frac{60 V_{i k}^{c} f_{i k}^{p}}{\pi a p_{i k} f_{i k} d_{i k}^{p} n_{k j}^{p}}+\left(1+b_{k}^{m}\right) C_{i k}^{T} f_{i k}^{-0.25} K_{i k}^{T} V_{i k}^{c}+E_{k l}^{D}\right] \times y_{i k l} \times \sum_{t} x_{i k l}\right\} \\
C \max \geqslant F_{k, S} \quad \forall k
\end{array}\right.
$$

Equation (12) is the objective function to minimize the normalized total energy consumption and makespan simultaneously, where $a$ is the weight of energy consumption obtained by such methods as the analytical hierarchy process (AHP), and fuzzy clustering method after investigating the preference of management. $T C E_{0}$ and $C \max _{0}$, are applied as two normalizing parameters, and they are obtained by a heuristic rule in this paper. Equations (13) and (14) both ensure each job is processed once at any stage. Equation (15) ensures that one of the available spindle speeds is selected when a job is assigned to a machine. Equation (16) controls that, at most, one job is processed in an event point. Equation (17) controls that one machine is available at an event point only after its previous jobs are completed. Equation (18) ensures the completion time of an event point is equal to the sum of the start time and processing time. Equation (19) limits that the starting time of each job in any stage is at least equal to the total time of the completion time in the previous stage and the transport time. Equation (20) controls that the completion time of any event point on a machine is at most equal to the start time of the subsequent event point on the same machine. Equation (21) ensures that TCE is the summation of energy consumption of all turning operations. Equation (22) controls that the Cmax is greater than or equal to the completion times of the last event point on all machines.

### 3.2. Heuristic Rule for Normalizing Parameters

As pointed out above, normalizing parameters $T C E_{0}$ and $C \max _{0}$ are obtained by the heuristic rule, which can be described as follows.

- Step 1: The theoretical linear cutting velocity $v_{i k}^{*}$ is calculated with Equation (23), the theoretical spindle speed is obtained with Equation (8), and then the real level of spindle speed noted as $l^{*}$ is determined according to machine operating instructions.

- Step 2: The total processing time of one turning operation $\left(T_{i k l *}^{Z}\right)$ is calculated by Equation (2), the average processing time $\left(\bar{T}_{i}\right)$ of job $i$ in all stages is calculated with Equation (24), and then the scheduling scheme is obtained by the following three-step circulation.
- Step 2.1: Set $j=1$ and sequence jobs by the ascending order of $\bar{T}_{i}$, denote the sequence as $\pi_{t}$ and set $T_{\pi_{1}, 1}^{c}=0$.
- Step 2.2: Assign the first free machine noted as $k *$ to process jobs in stage $j$, and calculate the completion time of jobs $T_{\pi_{1}, j}^{c}$ according to Equation (25). Then, calculate the consumed energy for cutting each job in stage $j$ with Equation (11), and calculate the total energy consumption of stage $j$ by $C_{j}^{c}=\sum_{k \in K_{j}} \sum_{i} C_{i k l *}^{c}$.Terminate this circulation when stage $j$ is the last stage or go on to step 2.3.
- Step 2.3: Reorder jobs and update $\pi_{t}$ in the ascending order of $T_{\pi_{1}, j}^{c}$, then set $j=j+1$ and return to step 2.2.
- Step 3: $T E C_{0}$ can be obtained by $\sum_{j} C_{j}^{c}$, and $C \max _{0}$ can be determined by $\max _{i} \bar{T}_{i}^{c}$. Detailed explanations are described with Equations (23)-(25)

$$
\begin{gathered}
v_{i k}^{*}=\frac{C_{v}}{T^{z_{v}} a p_{i k}^{z_{v}} f_{i k}^{y_{v}}} \\
\bar{T}_{i}=\sum_{j}\left(\sum_{k \in K_{j}} T_{i k l *}^{c} / m_{j}\right) / S \\
T_{\pi_{1}, j}^{c}=\left\{\begin{array}{l}
\max \left\{T_{\pi_{1}, j-1}^{c}, T_{\pi_{1,-1}, j}^{c}\right\}+T_{\pi_{1}, k * l *}^{c}, \forall t>1, j>1, \\
\max \left\{T_{\pi_{1}, j-1}^{c}, 0\right\}+T_{\pi_{1}, k * l *}^{c}, \quad \forall t=1, j>1 \\
\max \left\{0, T_{\pi_{1,-1}, j}^{c}\right\}+T_{\pi_{1}, k * l *}^{c}, \quad \forall t>1, j=1
\end{array}\right.
\end{gathered}
$$

In Equation (23), $v_{i k}^{*}$ is the theoretical linear cutting speed of job $i$ on the machine $k, a p_{i k}$ is the depth of cutting, $f_{i k}$ is the feed rate, $C_{v}$ is the durability coefficient of cutting tool, $T$ is the durability of cutting tool, and $z_{v}, x_{v}, y_{v}$ are coefficients whose values are set according to the processed materials and conditions. In Equations (24) and (25), $T_{i k l *}^{c}$ is the total processing time of job $i$ processed on machine $k$ at spindle speed level $l, S$ is the number of stages, $m_{j}$ is the number of parallel machines in stage $j$, and $K_{j}$ is the set of machines.

The above model of $F F_{m}(r) \mid T C E+C \max$ can be solved accurately by the GAMS/Dicopt solver for small-scale problems, but the solver will fail for large-size problems due to limited computer memory and a long running time. Therefore, it is necessary to develop efficient intelligent algorithms to assign parallel machines, select optimal spindle speeds, and sequence jobs simultaneously.

# 4. EDA Algorithm 

The estimation of distribution algorithm (EDA) is a population evolutionary algorithm based on probabilistic model [44-46], which guides the population evolution utilizing the probability of the dominant individuals. This algorithm employs the statistical probability to describe the distribution of solutions, and generates new populations by sampling probability. A large number of research groups have paid efforts to improve the performance of EDA algorithm [47-49]. The algorithm has been successfully applied to solve flow shop scheduling problems [50-52] and flexible flow shop scheduling problems, and it has obtained promising scheduling results. For its advantages, EDA is used to solve the energy-efficient scheduling problems in flexible flow shops in this paper. A novel decoding method is developed to optimize machine allocation, speed selection, and job sequence.

As for the process of EDA, the initialized population is randomly generated first, and the dominant individuals are selected according to their fitness. Then, the probability model is constructed from the dominant individuals to generate new ones. After the new population is generated, the termination criterion works to determine whether to stop this algorithm or not. This process is depicted in Figure 2.

![img-1.jpeg](img-1.jpeg)

Figure 2. Flowchart of EDA.

# 4.1. Encoding, Decoding, and Dominant Individuals 

The frequently utilized encoding method for solving FFSP is the arrangement-based encoding approach, in which only job sequence in the first stage is encoded and the jobs in the next stages are sorted according to dispatching rules like FCFS and SPT. Suppose that there are four jobs with an examplified code of [1 342 ], the first job is firstly processed and the third job is processed secondly. This encoding approach is simple to understand and complement, and thus is applied in this paper.

In regard to the population initialization, we adopt the random initialization method to ensure the population diversity. The computational complexity of this initialization method is $O\left(P_{\text {size }} n\right)$, where $P_{\text {size }}$ is the population size and $n$ the number of jobs.

On the ground of job sequence of the first stage, machine allocation, spindle speed, and job sequence at other stages are determined by decoding. In order to generate a feasible scheduling scheme, a dispatching rule is embedded in decoding to specify the job with the earliest completion time to be first processed, and any individual in the population can be decoded with Steps 1-3.

- Step 1: Choose an individual from the population, obtain its job sequence in the first stage, and set $t=1, T E C^{*}=0, T_{\pi_{1}, 1}^{c}=0$ and $T_{\pi_{t}, k}^{m}=0$.
- Step 2: Determine the processing machine and the spindle speed of all the jobs in current stage.
- Step 2.1: Calculate the processing time $\left(T_{\pi_{t} k l}^{c}\right)$ and energy consumption $\left(E_{\pi_{t}, k, l}\right)$ of the current job $\left(\pi_{t}\right)$ at all alternative speed levels on all available machines by Equations (2) and (11), respectively.
- Step 2.2: Calculate the completion time $\left(T_{\pi_{t}, k, l}^{o}\right)$ of the job at all alternative speed levels on all available machines by Equation (26). Set $C \max _{\pi_{t}, k, l}=T_{\pi_{t}, k, l}^{o}$ and $T E C_{\pi_{t}, k, l}=T E C^{*}+E_{\pi_{t}, k, l}$.

$$
T_{\pi_{t}, k, l}^{o}=\left\{\begin{array}{l}
\max \left\{T_{\pi_{t}, j-1}^{c}+T_{k^{k} k^{r}}^{d}, T_{\pi_{t-1}, k}^{m}\right\}+T_{\pi_{t} k l}^{c}, \forall t>1, j>1, k \in K_{j}, l \in N_{\pi t, k} \\
\max \left\{T_{\pi_{t}, j-1}^{c}+T_{k^{k} k^{r}}^{d}, 0\right\}+T_{\pi_{t} k l}^{c}, \quad \forall t=1, j>1, k \in K_{j}, l \in N_{\pi t, k} \\
\max \left\{0, T_{\pi_{t-1} k}^{m}\right\}+T_{\pi_{t} k l}^{c}, \quad \forall t>1, j=1, k \in K_{j}, l \in N_{\pi t, k}
\end{array}\right.
$$

- Step 2.3: Calculate the weighted target value using Equation (12), select the machine and the speed level with the smallest weighted target value for the job, and mark the index of the machine and corresponding speed level with $k^{*}$ and $l^{*}$.
- Step 2.4: Set $T_{\pi_{1}, k *}^{m}=T_{\pi_{1}, j}^{c}=T_{\pi_{1}, k *, l *}^{a}, T E C^{*}=T E C^{*}+E_{\pi_{1}, k *, l *}$. If $t=n$, go to Step 3. Otherwise, set $t=t+1$ and return to Step 2.1.
- Step 3: If $j=S$, the decoding process terminates. Otherwise, determine the job sequence in ascending order of the completion times, set $j=j+1, t=1, T_{\pi_{1}, k}^{m}=0$, and return to Step 2. Calculate the final weighted target values of this individual using Equation (12).

Next, several dominant individuals are to be selected from the population so that the probability model can be applied. Based on the weighted target values, we sort all individuals in the ascending order of the target values, and then select the top $\eta \%$ of individuals.

# 4.2. Population Updating Based on Probability Model 

For the convergence, EDA applies an indicator function to extract the sequence characteristics of dominant individuals, and then constructs a probability model to guide the further population updating. Utilizing indicator functions, the position of a job in a dominant individual is signified and then the probability of this job arranged at all positions is statistically calculated. If the probability is higher, there is more chance for this job to stay at its previous position, and thus the population is updated gradually according to the mechanism of the roulette. The detailed steps of population updating based on probability model are as follows.

- Step 1: Set the indicator function $\left(I S_{I i}^{l}(0)\right)$ to zero, and set all elements in the probability matrix $\left(\operatorname{Pr}_{I i}(0)\right)$ to $1 / n$.
- $\quad$ Step 2: At the $g$ th generation, if job $i$ is on position $t$ of dominant individual $l$, set $\left(I S_{I i}^{l}(g)\right)$ to 1 . Repeat this process till all dominant individuals, all jobs and all positions have been iterated. Calculate the total value of job $i$ on position $t$ and then yield the probability $\left(\operatorname{Pr}_{I i}(g+1)\right)$ by using Equation (27).

$$
\operatorname{Pr}_{I i}(g+1)=\left(1-a^{s}\right) \times \operatorname{Pr}_{I i}(g)+a^{s} \times \sum_{l \in S p} I S_{I i}^{l}(g) /|S p|, \forall g<G, t, i
$$

- $\quad$ Step 3: Update the population according to $\operatorname{Pr}_{I i}(g+1)$ by the roulette approach. Terminate the algorithm if termination criterion is met; otherwise, set $g=g+1$ and return to Step 2.


## 5. Verification and Discussion

Computational experiments are conducted to verify the validity of the proposed mathematical model, and the effectiveness of the proposed EDA algorithm. All the experiments are performed on the computer with an Intel Core i5 processor running at 2.8 GHz and a main memory of 4G Bytes. The employed operating system is Windows 7 Professional. Note that the proposed mathematical model is programmed in GAMS/Dicopt and the proposed EDA is encoded in the programming language of MATLAB R2010a (The MathWorks, Inc., Natick, MA, USA).

To compare the performance of the proposed mathematical model and EDA, two smaller size turning cases are designed. Thus, there are three types of problems: a small-scale problem with four rolls, a medium-scale problem with 12 rolls, and a large scale problem with 60 rolls.

Before experiment, the weight of energy consumption was set to 0.8 , which derived from Analytic Hierarchy Process (AHP) on the spot. Meanwhile, normalizing parameters of $C \max _{0}$ and $T E C_{0}$ were determined for the three size experiments utilizing the heuristic rule in Section 3.2. Their values under small-scale, medium-scale, and large-scale circumstances were ( $3420 \mathrm{~s}, 29.07 \mathrm{MJ}),(18,652 \mathrm{~s}, 289.17 \mathrm{MJ})$, and $(26,763 \mathrm{~s}, 1294.1 \mathrm{MJ})$ respectively.

# 5.1. Parameter Calibration of EDA 

EDA has three main parameters, namely population size noted as $P_{\text {size }}$, the ratio of dominant population noted as $\eta \%$ which is equal to $|S p| /\left|P_{\text {size }}\right|$, and learning rate noted as $a^{x}$. In this research, each factor has three levels: Psize $(30,50,80), \eta \%(10 \%, 20 \%, 30 \%)$, and $a^{x}(10 \%, 20 \%, 30 \%)$. We adopt an orthogonal experiment whose size is $\mathrm{L} 9\left(3^{3}\right)$ to calibrate these parameters, and the stopping criterion is the elapsed time of 80 s . The numerical results are obtained through the heurisitc rule. Then $T E C_{0}$ and $\mathrm{Cmax}_{0}$ are used as parameters to calculate weighted goals according to Equation (12), where $a=0.8$. Finally, the AOV of each experiment is obtained as shown in Table 1, where AOV is the average value of the weighted targets for 30 tests.

Table 1. Orthogonal experiment of EDA.

Table 1 shows under the third combination of $(0,10 \%, 0.3)$, the AOV value is the smallest, and thus the third combination is the best. However, when these parameters are invetsigated independently in Figure 3, we note that the best population size is 50 , the best rate of dominant population $10 \%$ and the best learning rate $10 \%$ or $30 \%$. The above results are not in accordance with that in the third combination. Considering the incompleteness of the orthogonal experiment, two more tests of the combinations of $(50,10 \%, 0.1)$ and $(50,10 \%, 0.3)$ are performed, and their AOVs are 0.9229 and 0.9228 . Taking these 11 experiments into account, we draw the conclusion that the optimal parameter combination is $(50,10 \%, 0.3)$ for the population size, rate of dominant population, and the learning rate.
![img-2.jpeg](img-2.jpeg)

Figure 3. Estimated marginal means of AOG on three parameters.

The EDA is applied to schedule 12 rolls, and the termination criterion is that the elapsed time reached 80 s . These jobs are completed in $14,594 \mathrm{~s}$, and 4058 s is saved compared with $18,652 \mathrm{~s}$ which is the makespan of the original scheduling by the heuristic rule. The total energy is 280.08 MJ , and 9.09 MJ is saved compared with the original scheduling. The results of the heuristic rule are depicted in Figures 4a, 5a and 6a, and the results of EDA are shown in Figures 4b, 5b and 6b.

![img-3.jpeg](img-3.jpeg)

Figure 4. Gantt charts by heuristic rule and DEA. (a) By the heuristic rule; (b) By EDA.
![img-4.jpeg](img-4.jpeg)

Figure 5. Energy consumption by the heuristic rule and EDA. (a) By the heuristic rule; (b) By EDA.
![img-5.jpeg](img-5.jpeg)

Figure 6. TEC by the heuristic rule and EDA. (a) By heuristic rule; (b) By EDA.

# 5.2. Experimental Results of the Motivating Example 

Figure 7a,b compare the Gantt charts of 60 rolls by heuristic rule and by EDA. Apparently, the derived maximum completion time by EDA is shortened by 6749 s or by $25.22 \%$ compared with that by heuristic rule. Only tiny idle times remain in the Gantt chart by EDA.

With respect to the consumed energy, Figure 8 b shows that the peak value of energy comsumption of 60 rolls by EDA is less than 250 MJ , while that by heuristic rule is nearly 300 MJ . The total energy consumed by the proposed EDA and the heuristic rule is 1223.2 MJ and 1294.1 MJ. In other words, 70.9 MJ or $5.48 \%$ of the total energy is saved by the proposed EDA. Note that, the energy consumptions of all lathes are reported in Figures A1 and A2 in Appendix.

Figure 9 reports the Pareto frontier of the population. We can see the siginificant improvement of the Pareto frontier from the first to the final generation, which clearly demonstrates a bidirectional and synchronous optimization of the two objectives. Obviously, the optimal solution of the proposed mathematical model, in which both the total energy consumption and makespan are weighted, lies on the curve of Pareto frontier.

![img-6.jpeg](img-6.jpeg)

Figure 7. Gantt chart of 60 rolls by the heuristic rule and EDA. (a) By heuristic rule; (b) By EDA.
![img-7.jpeg](img-7.jpeg)

Figure 8. TEC for 60 rolls by heuristic rule. (a) By the heuristic rule; (b) By EDA.

![img-8.jpeg](img-8.jpeg)

Figure 9. Pareto optimal solutions.

Table 2 compares the results obtained by the proposed EDA and that solved by GAMS/Dicopt solver for the MINLP model. It shows that, for small-scale problems, Dicopt solver outperforms the proposed EDA in both objectives during the acceptable time. For medium scale cases, the Dicopt solver takes much more time than the proposed EDA, but it produces a tiny improvement in the weighted target. For large-scale cases, the proposed EDA is absolutely superior over the Dicopt solver which cannot provide a feasible solution for the limited memory of the computer.

Table 2. Comparison of results.
In summary, using the proposed EDA, energy-efficient scheduling can be achieved effectively. Moreover, makespan and the total energy consumption can be reduced simultaneously, and hence production efficiency improvement and energy saving are realized.

# 5.3. Discussion 

The weight used in this paper is determined by AHP after investigating the preferences of managers in the real case. In order to clarify the weight range, sensitivity analysis experiments are conducted. Experiments show that when the weight is 1 , the makespan is 13.41 h and the TEC is 1218.2. Although this TEC is slightly better than that under other circumstances, the makespan is particularly worse. Actually, this result originates from the single-objective optimization of the total energy consumption and the ignorance of makespan under this circumstance. Therefore, the weight value of 1 is excluded from the weight range and then the weight range is limited by $(0,0.8)$. Table 3 shows the results after this adjustment. It demonstrates that the relative difference of total energy consumption is $2.03 \%$, and that of makespan is $2.76 \%$. Therefore, a conclusion can be reached that the two objectives are not sensitive to the weight when it ranges from 0 to 0.8 .

Table 3. Two objectives under different weights.
Besides, in order to find out the underlying reasons, three different optimization goals and two optimization methods are analyzed and compared. Three optimization goals are given: (1) the comprehensive goal by weighting the consumed energy and completion time (Obj_C); (2) the single target only considering the consumed energy (Obj_e); and (3) the single target only considering makespan (Obj_t). The two different optimization methods are given as follows: (1) optimizing the scheduling scheme and spindle speed synchronously (Opt_S); and (2) optimizing the scheduling scheme after determining the appropriate spindle speed (Opt_o). The following experiments contain six combinations of the above optimization goals and methods. For testing the robustness of the proposed EDA, it is run 30 times for each combination. The stopping criterion is fixed to a given maximum elapsed CPU time of 180 s . To evaluate the different optimization goals and methods, firstly Cmax, TCE, and the weighted objective of the best scheduling for each experiment are recorded; secondly the objectives are respectively analyzed by the repeated measures in IBM SPSS 19, in which optimization goals are set as within-subject effects and optimization methods as between-subject effects. The results are shown in Tables 4-6.

Table 4. Descriptive statistics.

Table 5. Multivariate tests of weighted objectives.

Note: (Objs * methods) means the interactions between optimization goals and optimization methods.

Table 6. Between-subjects effects on weighted objectives.
From Table 4, we note that in the columns of weighted objective and Cmax, Obj_C yield the means of 0.9474 and 22,232.57 which are both better than that of Obj_e and Obj_t. In TEC, the mean of $1,107,939.02$ obtained by Obj_C is lower than that of Obj_t. Therefore, adopting the weighted goal to measure energy-efficient scheduling is suitable for optimizing the comprehensive objective and makespan. In TEC, the means of $1,091,556.00$ is the lowest; however, the Obj_e is not often used in real production due to the long makespan, which is $123,687.13 \mathrm{~s}$, more than four times longer than that

of Obj_C and Obj_t. The reason is that all the jobs are assigned on the most efficient machine while the other machines are idle. Therefore, among the three optimization goals, the weighted objective is the best measure method for energy-efficient scheduling. Table 4 also shows that Opt_S yields lower means than Opt_o, no matter which of the three optimization goals is adopted. Therefore, optimizing the scheduling scheme and spindle speed synchronously not only saves the consumed energy but also shortens the makespan. Optimizing the scheduling scheme and turning parameters synchronously has a great effect on environment protection and production efficiency.

Table 5 also shows the multivariate tests of weighted objectives. Since all the differences are significant ( $0.000<0.05$ ), the optimization goals can affect the weighted objective significantly. The interactions between optimization goals and optimization methods also affect the weighted objective significantly. The differences of multivariate tests of Cmax and TEC are also significant, so the optimization goals and the interactions can affect Cmax and TEC, too. The data of the multivariate tests of Cmax and TEC are not reported here since they are similar to Table 5.

Table 6 shows the tests of between-subjects effects on weighted objectives. Since the difference is significant $(0.000<0.05)$, the optimization method can affect the weighted objective significantly. The differences of between-subjects effects on Cmax and TEC are significant, so the optimization methods can also affect Cmax and TEC significantly.

All in all, we find that different optimization goals and methods affect the Cmax and TEC significantly, so both environmental and production benefits can be enhanced simultaneously by optimizing the spindle speed and scheduling scheme, which is the first realization in this regard.

# 6. Conclusions 

Reducing the energy consumption is increasingly believed to be an effective environment protection measure in manufacturing industry. The optimization of the energy-efficiency scheduling in flexible flow shops with parallel machines can contribute to energy consumption redution and production efficiency improvement synchronously. In this paper, the following achievements have been obtained towards the energy-efficient scheduling in turning shops:
(1) A mixed integer nonlinear programming model is established by optimizing the spindle speed and scheduling scheme simultaneously, and subsequently, small-scale and medium-scale problems are solved by the GAMS/Dicopt;
(2) For large-scale problems, an effective EDA algorithm is proposed in which a dispatching rule is embedded in decoding to specify the job with the earliest completion time to be first processed, and the population is updated utilizing the probability of the dominant individuals;
(3) The experiment results show that: (1) the proposed algorithm can reduce the energy consumption to a certain extent and shorten the makespan to a large degree; and (2) there is a positive correlation between the energy consumption and makespan.

In future research, other turning parameters such as cutting depth and feed rate will also be taken into consideration so as to further improve the energy efficiency. More types of production shops, such as no-wait or no-idle flow shops, as well as other constraints such as due date will be studied.

Acknowledgments: The authors would like to thank the anonymous reviewers for their helpful comments. This work is supported by Research Foundation of Hubei Education Bureau (No. 15Q027), National Program on Key Basic Research Project (973 Program) of China (No. 2014CB046705), and by National Natural Science Foundation of China (No. 51275366, No. 51305311, No. 51575211). Gratitude also goes to Li Zou for her work in the improvement of the language and style of the paper.
Author Contributions: Fang Wang, Yunqing Rao, and Chaoyong Zhang designed the algorithm and analyzed experimental results; Fang Wang and Qiuhua Tang built the mathematical model; Liping Zhang provided the real turning shop case; Fang Wang and Chaoyong Zhang wrote the algorithm section and the experimental section of the paper; Yunqing Rao and Qiuhua Tang organized the structure of the paper. All authors have read and approved the final manuscript.
Conflicts of Interest: The authors declare no conflict of interest.

# Appendix A 

Table A1. Parameters of machine.

Note: Speeds of machine are from Machinery Handbook, and the other parameters are the experimental data. Additional load-loss energy coefficient $\left(b^{\text {in }}\right)$ is determined by the vibration noise, and the values of lathes R1, R2, F1, and F2 are 0.1 ; those of lathes R3, R4, F3, and F4 are 0.13 ; and the rest are 0.15 .

Table A2. Transport time (s).
Table A3. Parameters of rolls.

Table A4. Parameters of rough turning.

Note: $a p$ and $f$ are determined by the specific technological specification of the machine; $v^{*}$ is a linear cutting velocity obtained by Equation (23).

Table A5. Parameters of fine turning.

Note: $a p$ and $f$ are determined by the specific technological specification of the machine; $v^{*}$ is a linear cutting velocity obtained by Equation (23).
![img-9.jpeg](img-9.jpeg)

Figure A1. Total energy consumption of each machine by heuristic rule.

![img-10.jpeg](img-10.jpeg)

Figure A2. Total energy consumption of each machine by EDA.
