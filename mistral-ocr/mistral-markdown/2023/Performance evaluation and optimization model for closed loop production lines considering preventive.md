# Performance evaluation and optimization model for closed-loop production lines considering preventive maintenance and rework process 

Proc IMechE Part E:<br>J Process Mechanical Engineering 2024, Vol. 238(5) 2438-2455<br>© IMechE 2023<br>Article reuse guidelines:<br>agepub.com/pournals-permissions<br>DOI: 10.1177/09544089231160514<br>journals.agepub.com/home/pie<br>\$ Sage

## Bingham Zhou ${ }^{1}$ and Wenfei Zha ${ }^{1}$


#### Abstract

Closed-loop production lines with a constant number of carriers are widely encountered in today's production systems. In this paper, a production performance evaluation and optimization model is proposed for a closed-loop production line taking into account the degradation-level-dependent quality and rework process. Based on a two-machine-one-buffer decomposition method and the system state transition, a production performance evaluation method is presented. Due to the emphasis on quality management, preventive maintenance (PM) is used to ensure the reliability of the machines in the production line, increasing the effective output at minimum cost. A hybrid particle swarm optimization and estimation of distribution algorithm (PSO-EDA) is proposed to efficiently develop the optimal PM strategy. Finally, numerical experiments are performed to verify the effectiveness of the model. With the objective of maximizing the system profit, the optimization of the machines and pallets number is also explored.


## Keywords

Closed-loop production line, preventive maintenance, degradation, quality, rework

## Introduction

Production lines in large-volume production environments often have parts transported on carriers (such as pallets, skids, etc.), from one operation to the next. ${ }^{1} \mathrm{~A}$ constant number of available carriers impose a limit on the number of parts that can be in production systems at any given time. This type of production lines is a closed-loop system with respect to carriers. ${ }^{2}$ Nowadays, closed-loop production lines have many industrial applications and are common in factories. ${ }^{3}$ In practice, most production lines suffer increasing degradation with the usage and ageing process. The production precision loss caused by degradation will damage the products quality, reducing the effective output of the system. ${ }^{4}$ Due to the importance of closed-loop production lines, it is desirable to improve the system reliability and products quality with the PM strategy and rework process. However, most existing researches just focus on machine failures and buffer allocation. Degradation-level-dependent quality has been rarely investigated and the impact of maintenance on production performance remains mainly unexplored. Therefore, this paper is presented to try to fill some existing research gaps. With the objective of maximizing system profit, a novel model is proposed to evaluate production performance and optimize the PM strategy
and number of pallets for a closed-loop production line with a rework process.

In recent years, continuous research efforts have been devoted to studying performance evaluation and optimization methods for closed-loop production systems. ${ }^{5-9}$ Bouhchouch et al. ${ }^{10}$ first developed an analytical approximation method for the performance evaluation of a closed-loop production system. Biller et al. ${ }^{11}$ maximized the production rate of the closed-loop production line by determining the number of pallets and the buffer capacity in the system. Later, with the same optimization objectives, Biller et al. ${ }^{1}$ analyzed closed Bernoulli production lines with different distributions of failure rates and repair rates. Gershwin and Werner ${ }^{12}$ presented an approximate analytical decomposition method for evaluating the production rate and distribution of inventory of a closed-loop production system. Shi and Gershwin ${ }^{3}$ proposed two modifications to eliminate the discontinuities and improve

[^0]
[^0]:    ${ }^{1}$ School of Mechanical Engineering, Tongji University, Shanghai, PR China

    ## Corresponding author:

    Binghai Zhou, School of Mechanical Engineering, Tongji University, Shanghai 201804, PR China.
    Email: bhzhou@tongji.edu.cn

the performance evaluation accuracy of the algorithm developed by Gershwin and Werner. ${ }^{12}$ Feng et al. ${ }^{13}$ introduced an iteration method to evaluate the key performance indicator of closed-loop production lines with geometric reliability machines. Jia et al. ${ }^{14}$ studied real-time performance evaluation of the closed Bernoulli production lines with finite buffers and finite carriers, proposing an approximation method with high accuracy and computational efficiency. However, the above-mentioned studies only optimize the buffer capacity or the number of carriers. Although some of the studies have introduced the concept of reliability and failure into the closed-loop production lines, little work has been conducted on the integration of performance evaluation and maintenance strategies, especially PM strategies. Therefore, it is of great theoretical and practical significance for further research.

To develop the joint performance evaluation and maintenance model, researchers have made assumptions that all operations performed by the machines are of acceptable quality. ${ }^{15-17}$ For example, Fitouhi et al. ${ }^{18}$ considered a two-machine continuous flow system with a buffer, where the machines are subjected to failures, minimal repairs, and condition-based preventive maintenance (CBM). Maggio et al. ${ }^{19}$ described an approximate analytical method for evaluating the average values of throughput and buffer levels of the closed-loop production lines with finite buffers. The failures of unreliable machines are operation-dependent and maintenance time is geometrically distributed. Ruifeng and Subramaniam ${ }^{20}$ investigated PM in Kanban controlled assembly lines and developed an analytical model for such systems, providing estimates of production rate and work-in-process (WIP). However, the unqualified products are not taken into consideration, making the performance evaluation quite inaccurate. More performance evaluation models considering maintenance can be found in Zhou et al., ${ }^{21}$ Cheng et al., ${ }^{22}$ Zhou et al., ${ }^{23}$ and You. ${ }^{24,25}$

In the literature mentioned above, there is a common assumption that the production quality remains perfect during the production horizon. However, in practice, it is not always the case. ${ }^{26-28}$ Production systems with rework loops are commonly seen in contemporary industries, such as steel, pharmaceutical, semiconductor, garment, glass and food. ${ }^{29}$ Helber and Jusic ${ }^{30}$ presented a decomposition technique for a production system with multistage rework loops. The defective products were sent back to the same workstation for rework. Hadjinicola ${ }^{31}$ proposed a modelling framework integrating the Markov chain and systems with rework loops to estimate the production cost. In their study, the movement of unfinished products to preceding production stages for rework is indicated as backward transitions between states. Rabbani et al. ${ }^{32}$ proposed a robust optimization approach to production systems with failure in rework and breakdown under uncertainty. Zhou and Lin ${ }^{33}$ proposed a new mechanism for the rework system of a Bernoulli serial production line based on the principles of quality management and lean production. However, the above-mentioned literature only studied system
structures of multi rework loops or a single rework loop for the entire production system. Besides, in models of multistage production systems with a single rework loop, processing machines are usually assumed to randomly generate unqualified products at a constant rate. ${ }^{34}$ The degradation process and PM actions are rarely considered. There exists a need to develop a production model, jointing the PM policy and rework to reduce the defective rate and production cost.

In this paper, a production performance evaluation and optimization model is proposed for the closed-loop production line taking into account the degradation-level-dependent quality and rework process. The production system consists of a serial production line with an intermediate rework site. The production lines before and after the rework site are called the minor production line and the major production line, respectively. Considering the heterogeneity of returned unqualified products, the machines of the major production line degrade gradually, and the degradation process is modelled by the state transition which is widely used in PM models for degrading systems. The machines of the minor production line receive homogeneous raw materials and are assumed to be not affected by the degradation. ${ }^{35}$ The proportion of unqualified products depends on the degradation level monitored, that is, more unqualified products are produced when the degradation reaches a higher level. PM actions are performed to control the system degradation and improve the product quality when the degradation level reaches the threshold which is a decision variable of the model. In the closed-loop production line, the number of pallets travelling in the closed-loop is another decision variable. The objective of this paper is to maximize system profit by optimizing the PM strategy and number of pallets. The production cost model is formally developed and the optimal joint strategy is obtained numerically.

In comparison with the existing works, the main contributions of this study are summarized as follows:

1. This is the first study of production performance evaluation and optimization model for the closed-loop production line with an intermediate rework site. The condition of the machine in the closed-loop production line is first modelled as a discrete multi-state degradation process, in which maintenance decisions are made based on the degradation level of the machine.
2. This study captures the significance of product quality degradation in the closed-loop production line. The rework process of unqualified products is incorporated into the production model to effectively improve product quality.
3. The impact of PM actions on production performance is first introduced into the performance evaluation for the closed-loop production line considering rework.
4. Since the state space of the system is too large, the optimization problem is extremely difficult to be solved analytically. Therefore, a novel hybrid PSOEDA optimization algorithm is proposed to obtain optimal solutions more efficiently. Its effectiveness

and competitiveness are proved by comparison with the traditional PSO algorithm.

The remainder of this paper is organized as follows. In Section "Problem description," the problem statements and the fundamental assumptions are described. In Section "Production performance evaluation," the modelling development of the production rate evaluation is presented for both major and minor production lines. In Section "Hybrid PSO-EDA optimization," the main steps of the hybrid PSO-EDA optimization algorithm are built. In Section "Numerical example," a numerical example is given to illustrate the validity of the proposed model and carry out some sensitivity analysis. Finally, concluding remarks are offered in Section "Conclusion."

## Problem description

In the closed-loop production line with the rework process in Figure 1, there is an intermediate buffer $B_{i}$ between two machines. Jobs are transferred between various machines through the pallets, the total number of which in the system is $N_{0}$. There is an inspection area at the end of the production line, and the defective products after inspection are temporarily stored in the buffer $B_{0}$, where they will be repaired in a unified manner. The overall production line is divided into two parts based on the rework site, including the minor production line of machines $M_{1}, M_{2} \ldots M_{j-1}$ and the major production line of machines $M_{j}, M_{j+1} \ldots M_{k}$, respectively.

To describe the problem domain more effectively, the following assumptions are made.

Assumption 1: When the buffer $B_{0}$ is full, the defective products are uniformly reworked, and all the products become qualified products after rework.
Assumption 2: The machines $M_{j}, M_{j+1} \ldots M_{k}$ will produce unqualified products in different states $\delta_{i}$ with the probability $p d_{i, \delta_{i}}$. Compared with the major production line, unqualified products produced by machines $M_{1}, M_{2} \ldots M_{j-1}$ can be neglected.
Assumption 3: Machine degradation states are known and finite. ${ }^{36}$ Machines $M_{j}, M_{j+1} \ldots M_{k}$ contain $n_{i}+$

2 different states. The PM action is carried out only when the machine reaches a certain state $\delta_{i j \mathrm{~h}}=$ $\operatorname{arc}_{\delta_{i}}\left(p t_{i, \delta_{i}}=1\right)$, where $p t_{i, \delta_{i}}\left(\sum_{h_{i}=1}^{n_{i}} p t_{i, \delta_{i}}=1\right)$ is the PM decision variable.
Assumption 4: The buffer capacities of $B_{1} \ldots B_{k-1}$ are infinite. The buffer capacities of the reworking buffer $B_{0}$ is set to be $S_{0}$.
Assumption 5: The total number of WIP in the system cannot exceed the number of pallets, ${ }^{37}$ that is $\sum_{i=1}^{k-1} x_{i} \leq N_{0}$.
Assumption 6: State transitions will not occur for more than one machine at the same time.
Assumption 7: The average degradation time and repair time of the machines follows exponential distribution. ${ }^{38}$

## Production performance evaluation

## Performance evaluation of minor production line

The decomposition method is used to solve the production rate of machines $M_{1}, M_{2} \ldots M_{j-1}$ in the minor production line, which is decomposed into a two-machine-one-buffer system. The main idea of this decomposition method is to decompose the serial production line containing $j-1$ machines into $j-2$ serial production lines $L(i)(i=$ $1,2, \ldots, j-2)$ containing two machines. Each serial production line $L(i)$ consists of an upstream machine $M_{u}(i)$ and a downstream machine $M_{d}(i)$, separated by a buffer $B_{i}$. Assuming that each machine has only two states, state 0 indicates that the machine is in failure, and at the same time adopts a corrective maintenance strategy to repair; state 1 indicates that the machine is operating.

For each production line $L(i)$, it is defined that $\mu_{u}(i)$ and $\mu_{d}(i)$ are the operating rates of the equivalent upstream and downstream machines $M_{i}^{u}$ and $M_{i}^{d}$, respectively; $f r_{u}(i)$ and $f r_{d}(i)$ are the failure rate of the upstream and downstream machines; $r_{u}(i)$ and $r_{d}(i)$ are the parameters of exponential distribution of repair time; $P(i)$ is the actual production rate of the production line $L(i) ; p_{i}\left(x_{i}, a, b\right)$ represents the probability line $L(i)$ being in the state $\left(x_{i}, a, b\right)$, where $x_{i}$ represents the number of products in
![img-0.jpeg](img-0.jpeg)

Figure 1. An illustrative chart of the closed-loop production line with rework.

the buffer, and $a, b$ represent the status of the equivalent upstream and downstream machines respectively.

It can be shown that the single machine production efficiency of the equivalent upstream and downstream machines $M_{i}^{u}$ and $M_{i}^{d}$ in each production line $L(i)$ are given by ${ }^{39}$ :

$$
\begin{aligned}
& e_{u}(i)=\frac{r_{u}(i)}{r_{u}(i)+f r_{u}(i)} \\
& e_{d}(i)=\frac{r_{d}(i)}{r_{d}(i)+f r_{d}(i)}
\end{aligned}
$$

The parameters above can only reflect the system status inside the production line $L(i)$. However, for a single production line $L(i)$, its production may be affected by the failure of the production line itself or the failure of the adjacent production line. Downtime can be transferred between adjacent production lines, therefore $L(i)$ model should take the state information of adjacent production lines into consideration. To solve this problem, the following definitions and theorems are proposed.

Definition 1: "Failure transition rate" $\Psi(i)$ represents the proportion of the failure of the production line $L(i)$ caused by the failure of the adjacent production line in all failures.

Theorem 1: In a two-machine-one-buffer system, the failure transition rate of the equivalent upstream and downstream machines $M_{i}^{u}$ and $M_{i}^{d}$ are calculated as:

$$
\begin{gathered}
\Psi_{u}(i)=\frac{p_{i-1}\left(0,0,1\right) \mu_{u}(i) r_{u}(i-1)}{f r_{u}(i) P(i-1)} \\
\Psi_{d}(i)=\frac{p_{i+1}\left(x_{i+1}, 1,0\right) \mu_{d}(i) r_{d}(i+1)}{f r_{d}(i) P(i+1)}
\end{gathered}
$$

Proof: For the upstream machine $M_{u}(i)$, the average number of failures per unit time caused by the failure of its adjacent machine $M_{u}(i-1)$ can be presented as:

$$
F N^{\prime}{ }_{u}(i)=\frac{p_{i-1}(0,0,1)}{m_{u}^{e}(i-1)}
$$

Where $m_{u}^{e}(i-1)$ is the average failure duration of machine $M_{u}(i-1)$, that is $m_{u}^{e}(i-1)=1 / r_{u}(i-1)$. The average number of failures per unit time of machine $M_{u}(i)$ is obtained as:

$$
F N_{u}(i)=\frac{\phi_{u}(i)}{m_{u}^{e}(i)}
$$

where $\phi_{u}(i)$ is given by:

$$
\phi_{u}(i)=\left(\frac{1}{e_{u}(i)}-1\right) \frac{P(i-1)}{\mu_{u}(i)}
$$

According to the above definition,

$$
\Psi_{u}(i)=\frac{F N^{\prime}{ }_{u}(i)}{F N_{u}(i)}=\frac{p_{i-1}\left(0,0,1\right) \mu_{u}(i) r_{u}(i-1)}{f r_{u}(i) P(i-1)}
$$

With

$$
\Psi_{d}(i)=\frac{F N^{\prime}{ }_{d}(i)}{F N_{d}(i)}=\frac{p_{i+1}\left(x_{i+1}, 1,0\right) \mu_{d}(i) r_{d}(i+1)}{f r_{d}(i) P(i+1)}
$$

Based on the "failure transition rate" in the abovementioned definition and theorem, each parameter expression of the equivalent upstream and downstream machines can be given. The repair time parameter, failure rate, and operation rate of the equivalent upstream machine $M_{i}^{u}$ are expressed as follows:

$$
\begin{gathered}
r_{u}(i)=\frac{1}{\frac{\Psi_{u}(i)}{r_{u}(i-1)}+\frac{1-\Psi_{u}(i)}{r_{i}}} \\
f r_{u}(i)=\left(1+\frac{p_{i-1}\left(0,1,1\right) \mu_{u}(i)}{P(i-1)}\left(\frac{\mu_{u}(i-1)}{\mu_{d}(i-1)}-1\right)\right) f r_{i} \\
+\left(\frac{p_{i-1}\left(0,0,1\right) \mu_{u}(i)}{P(i-1)}\right) r_{u}(i-1) \\
\frac{1}{\mu_{u}(i)}=\frac{e_{u}(i)}{\frac{1}{P(i-1)}+\frac{1}{e_{i} \mu_{i}}-\frac{1}{e_{d}(i-1) \mu_{d}(i-1)}}
\end{gathered}
$$

Similarly, the repair time parameter, failure rate, and operation rate of the equivalent downstream machine $M_{i}^{d}$ are expressed as follows:

$$
\begin{gathered}
r_{d}(i)=\frac{1}{\frac{\Psi_{d}(i)}{r_{u}(i+1)}+\frac{1-\Psi_{d}(i)}{r_{i+1}}} \\
f r_{d}(i)=\left(1+\frac{p_{i+1}\left(x_{i+1}, 1,1\right) \mu_{d}(i)}{P(i+1)}\left(\frac{\mu_{d}(i+1)}{\mu_{u}(i+1)}-1\right)\right) f r_{i+1} \\
+\left(\frac{p_{i+1}\left(x_{i+1}, 1,0\right) \mu_{d}(i)}{P(i+1)}\right) r_{d}(i+1) \\
\frac{1}{\mu_{d}(i)}=\frac{e_{d}(i)}{\frac{1}{P(i+1)}+\frac{1}{e_{i+1} \mu_{i+1}}-\frac{1}{e_{u}(i+1) \mu_{u}(i+1)}}
\end{gathered}
$$

According to equation (10)-(15), there is a functional relationship between $\mu_{u}(i), f r_{u}(i), r_{u}(i)$, also between $\mu_{d}(i), f r_{d}(i), r_{d}(i)$ similarly. Then, equations (10)-(15) are decomposed to extract the parts that are not directly related to each other to obtain an iterative algorithm for solving the production rate. The main steps are shown as follows.

Step 1: Initialize part of parameters in the model.

$$
\mu_{u}(1)=\mu_{1} ; f r_{u}(1)=f r_{1} ; r_{u}(1)=r_{1}
$$

$$
\begin{gathered}
\mu_{d}(i)=\mu_{i+1} ; \quad f r_{d}(i)=f r_{i+1} ; \quad r_{d}(i)=r_{i+1} \\
i=1, \ldots, j-2
\end{gathered}
$$

Step 2: For $i=2,3, \ldots, j-2$, the values of parameters of production line $L(i-1)$ are used to update the parameters of the upstream machine $M_{u}(i)$.

$$
\begin{gathered}
\mu_{u}(i)=\frac{U_{4}\left(f r_{i}+r_{i}\right)}{U_{2} U_{4}+r_{i}-U_{3} U_{4}} \\
f r_{u}(i)=f r_{i}+U_{3} \mu_{u}(i) \\
r_{u}(i)=\frac{1}{\frac{1}{r_{i}}+\frac{U_{1} U_{4} \mu_{u}(i)}{\mu_{u}(i)-U_{4}}} \\
U_{1}=\frac{p_{i+1}(0,0,1)}{P(i-1)\left(\frac{1}{r_{u}(i-1)}-\frac{1}{r_{i}}\right)} \\
U_{2}=\frac{p_{i-1}(0,0,1)}{P(i+1)\left(r_{u}(i-1)-r_{i}\right)} \\
U_{3}=f r_{i} \frac{p_{i-1}(0,1,1)}{P(i-1)}\left(\frac{\mu_{u}(i-1)}{\mu_{d}(i-1)}-1\right) \\
+\frac{p_{i-1}(0,0,1)}{P(i-1)} r_{u}(i-1) \\
U_{4}=\frac{1}{\frac{1}{P(i-1)}+\frac{1}{e_{i} \mu_{i}}-\frac{1}{e_{d}(i-1) \mu_{d}(i-1)}}
\end{gathered}
$$

where $U_{1}, U_{2}, U_{3}, U_{4}$ are not functions of $\mu_{u}(i), f r_{u}(i), r_{u}(i)$, which makes iterative algorithm possible in order of $i=2,3, \ldots, j-2$.

Step 3: For $i=j-3, \ldots, 1$, the values of parameters of production line $L(i+1)$ are used to update the parameters of the downstream machine $M_{d}(i)$.

$$
\begin{gathered}
\mu_{d}(i)=\frac{D_{4}\left(f r_{i+1}+r_{i+1}\right)}{D_{2} D_{4}+r_{i+1}-D_{3} D_{4}} \\
f r_{d}(i)=f r_{i+1}+D_{3} \mu_{d}(i) \\
r_{d}(i)=\frac{1}{\frac{1}{r_{i+1}}+\frac{D_{1} D_{4} \mu_{d}(i)}{\mu_{d}(i)-D_{4}}} \\
D_{1}=\frac{p_{i+1}\left(n_{i+1}, 1,0\right)}{P(i+1)\left(\frac{1}{r_{d}(i+1)}-\frac{1}{r_{i+1}}\right)}
\end{gathered}
$$

$$
\begin{gathered}
D_{2}=\frac{p_{i+1}\left(n_{i+1}, 1,0\right)}{P(i+1)\left(r_{u}(i+1)-r_{i+1}\right)} \\
D_{3}=f r_{i+1} \frac{p_{i+1}\left(n_{i+1}, 1,1\right)}{P(i+1)}\left(\frac{\mu_{d}(i+1)}{\mu_{u}(i+1)}-1\right) \\
+\frac{p_{i+1}\left(n_{i+1}, 1,0\right)}{P(i+1)} r_{d}(i+1) \\
D_{4}=\frac{1}{\frac{1}{P(i+1)}+\frac{1}{e_{i+1} \mu_{i+1}}-\frac{1}{e_{u}(i+1) \mu_{u}(i+1)}}
\end{gathered}
$$

Similarly, $D_{1}, D_{2}, D_{3}, D_{4}$ are not functions of $\mu_{d}(i), f r_{d}(i), r_{d}(i)$.

Step 4: The algorithm ends when the unknown parameters converged, otherwise go to Step 2.

The algorithm can finally obtain the production rate of the minor production line, that is $P(j-1)$. On condition that the uniform rework is not performed, the products produced by the minor production line will directly enter the major production line for further processing.

## Performance evaluation of major production line

For the production lines $M_{i}, M_{j+1} \ldots M_{k}$, the state of the machine $M_{i}$ is expressed as $\delta_{i}$, and different states of the machine can transfer between each other. The illustrative chart of machine state transitions is presented in Figure 2. When machine state $\delta_{i} \leq n_{i}$, the machine $M_{i}$ deteriorates at the rate $p_{i, \delta_{i}}$. The average deterioration time is determined by the degradation exponential distribution. In addition, machine $M_{i}$ performs PM action when $p t_{i, \delta_{i}}=1$, with the PM complete rate $p_{i}$. When $\delta_{i}=n_{i}$, further degradation will result in the machine failure, that is entering the state $\delta_{i}=n_{i}+1$. At this time, the repair is triggered,
![img-1.jpeg](img-1.jpeg)

Figure 2. Machine state transitions.

with the repair rate $\lambda_{i}$. All machines in the major production line carry out random state transitions according to the above-mentioned rate. A machine will remain in the previous state if the state transfer does not occur.

Based on the above description, the status of the machine $M_{i}$ can be separated into the following four categories.
(A) When $\delta_{i}=0$, machine $M_{i}$ is in the best state.
(B) When $\delta_{i}=1,2 \ldots n_{i}$, machine $M_{i}$ is in normal operation with degradation.
(C) When $\delta_{i}=n_{i}+1$, machine $M_{i}$ is in failure, waiting for repair.
(D) When $\delta_{i}=n_{i}+2$, machine $M_{i}$ is under PM.

Therefore, the state condition of the two-machine-onebuffer system can be obtained from the single machine state transitions. The status of the two-machine-one-buffer system includes three aspects, namely the degradation state of the equivalent upstream machine and the equivalent downstream machine $\delta_{1}, \delta_{2}$, and the number of WIPs in the intermediate buffer $x_{1}$. The condition $x_{1}>0$, $\delta_{1}=1,2 \ldots n_{1}, \delta_{2}=1,2 \ldots n_{2}$ is used as an example to illustrate the development of state balance equations. The state transition is shown in Figure 3.

$$
\begin{aligned}
& P\left(x_{1}, \delta_{1}, \delta_{2}\right)\left(u_{1}+u_{2}+p_{1, \delta_{1}}+p_{2, \delta_{2}}\right)=P\left(x_{1}-1, \delta_{1}, \delta_{2}\right) u_{1} \\
& \quad+P\left(x_{1}+1, \delta_{1}, \delta_{2}\right) u_{2}+P\left(x_{1}, \delta_{1}-1, \delta_{2}\right) p_{1, \delta_{1}-1} \\
& \quad+P\left(x_{1}, \delta_{1}, \delta_{2}-1\right) p_{2, \delta_{2}-1}
\end{aligned}
$$

The state transition rates of the two-machine-one-buffer system depend on the operating rate $u_{1}, u_{2}$ and the
degradation rate $p_{1}, p_{2}$ of the equivalent upstream and downstream machines. Through the above analysis, multiple sets of balance equations can be obtained, so as to obtain the steady-state probability $P\left(x_{i}, \delta_{i}^{\mu}, \delta_{i}^{d}\right)$ of the system in each state.

According to the serial production line decomposition method, the major production line is decomposed into two-machine-one-buffer systems. However, if the upstream machine in the system suffers from starvation, it will be unable to produce, which will affect the normal processing of the next machine. Definition 2 and Theorem 2 modify the system state and steady-state probability for this problem.

Definition 2: A production line is decomposed into a set of subsystems consisting of a two-machine-onebuffer system. Between each subsystem, "failure connection" exists due to the flow of WIPs. The state of the upstream machine can thus affect the processing of the adjacent downstream machine. Introduce additional state parameter $\Omega$ into the two-machine-one-buffer system, the system state parameter is modified to $\mathrm{SYS}_{i}=\left(x_{i}, \delta_{i}^{\mu}, \delta_{i}^{d}, \Omega_{i}\right)$. When $\Omega_{i}=0$, the equivalent upstream machine $M_{i}^{\mu}$ operates normally, with no failure connection. When $\Omega_{i}=1$, failure connection exists between the equivalent upstream machine $M_{i}^{\mu}$ and its upstream machine, making $M_{i}^{\mu}$ down, that is the original machine represented by the equivalent upstream machine is starving.

Theorem 2: The production status of the two-machine-one-buffer system depends on its "failure
![img-2.jpeg](img-2.jpeg)

Figure 3. An example of state transitions in the two-machine-one-buffer system.

connection" state with the upstream two-machine-onebuffer system.

$$
u_{n}(t)= \begin{cases}f\left(u_{i}^{u}, n_{i}^{u}, d r_{i, \delta_{i}}^{u}, r_{i}^{u}\right) & \Omega_{i-1}=0 \\ f^{\prime}\left(u_{i}^{u}, n_{i}^{u}, d r_{i, \delta_{i}}^{u}, r_{i}^{u}\right) & \Omega_{i-1}=1\end{cases}
$$

Proof: For the upstream machine $M_{i}^{u}$, the failure connection of $M_{i}^{u}$ will occur only when the machine finishes processing a WIP. Therefore, when $M_{i}^{u}$ passes a WIP to the buffer $B_{i}$, a failure connection will occur with a probability $p_{i}^{\Omega}$, which is the probability of the state transferring from $\Omega_{i}=0$ to $\Omega_{i}=1$ :

$$
\operatorname{Prob}\left(\Omega_{i}(t+\Delta t)=1 \mid \Omega_{i}(t)=0, \delta_{i}^{u} \leq n_{i}^{u}\right)=p_{i}^{\Omega} u_{i}^{u} \Delta t
$$

where $p_{i}^{\Omega} u_{i}^{u}$ refers to the probability of a failure connection after the machine $M_{i}^{u}$ finishes processing a WIP.

Similarly, the probability that the machine $M_{i}^{u}$ state transfers from $\Omega_{i}=1$ to $\Omega_{i}=0$ to return to the normal state is given by:

$$
\operatorname{Prob}\left(\Omega_{i}(t+\Delta t)=0 \mid \Omega_{i}(t)=1\right)=\lambda_{i}^{\Omega} \Delta t
$$

The above $p_{i}^{\Omega}$ and $\lambda_{i}^{\Omega}$ can be calculated by the probability of starvation. The frequency at which the equivalent downstream machine $M_{i}^{d}$ produces a product is calculated as:

$$
\mathrm{FR}_{i}=\sum_{\Omega_{i}} \sum_{\delta_{i}^{u} \leq n_{i}^{u}} \sum_{\delta_{i}^{u}} \sum_{x_{i} \geq 1} P\left(x_{i}, \delta_{i}^{u}, \delta_{i}^{d}, \Omega_{i}\right) \cdot u_{i}^{d}
$$

The starvation probability of the downstream machine is obtained by:

$$
g_{i}^{d}=\frac{\mathrm{FR}_{i}^{d}}{\mathrm{FR}_{i}}=\frac{\sum_{\Omega_{i}} \sum_{\delta_{i}^{u} \leq n_{i}^{u}} \sum_{\delta_{i}^{u}} P\left(1, \delta_{i}^{u}, \delta_{i}^{d}, \Omega_{i}\right)}{\sum_{\Omega_{i}} \sum_{\delta_{i}^{u} \leq n_{i}^{u}} \sum_{\delta_{i}^{u}} \sum_{x_{i} \geq 1} P\left(x_{i}, \delta_{i}^{u}, \delta_{i}^{d}, \Omega_{i}\right)}
$$

With $h_{i}^{d}$ being defined as the probability that the equivalent downstream machine $M_{i}^{d}$ recovers from starvation, the following equation can be obtained.

$$
\begin{gathered}
\left(\sum_{\Omega_{i}} \sum_{\delta_{i}^{u}} \sum_{\delta_{i}^{d}} P\left(0, \delta_{i}^{u}, \delta_{i}^{d}, \Omega_{i}\right)\right) \\
h_{i}^{d}=\sum_{\delta_{i}^{u}} \sum_{\delta_{i}^{u} \leq n_{i}^{u}} P\left(0, \delta_{i}^{u}, \delta_{i}^{d}, 0\right) \cdot u_{i}^{u}
\end{gathered}
$$

Therefore, the probability that the downstream machine recovers from starvation is given by:

$$
h_{i}^{s}=\frac{\sum_{\delta_{i}^{u}} \sum_{\delta_{i}^{u} \leq n_{i}^{u}} P\left(0, \delta_{i}^{u}, \delta_{i}^{d}, 1\right) u_{i}^{u}}{\sum_{\Omega_{i}} \sum_{\delta_{i}^{u}} \sum_{\delta_{i}^{u}} P\left(0, \delta_{i}^{u}, \delta_{i}^{d}, \Omega_{i}\right)}
$$

According to the principle of system decomposition, the equivalent upstream machine of the production line $L(i)$ is the equivalent downstream machine of the production line $L(i-1)$. Therefore, the failure connection state will be passed to the downstream subsystem, that is $p_{i}^{u}=g_{i-1}^{d}$, $\lambda_{i}^{u}=h_{i-1}^{d}$.

Based on the above "failure connection" theory and formula, the state transition probability of every
subsystem $P\left(x_{i}, \delta_{i}^{u}, \delta_{i}^{d}, \Omega_{i}\right)$ can be obtained in turn, starting from the production line $L(j)$.

$$
\begin{aligned}
& P\left(x_{i}, \delta_{i}^{u}, \delta_{i}^{d}, 0\right)=\frac{1 /\left(p_{i}^{\Omega} u_{i}^{u}\right)}{1 / \lambda_{i}^{\Omega}+1 /\left(p_{i}^{\Omega} u_{i}^{u}\right)} \cdot P\left(x_{i}, \delta_{i}^{u}, \delta_{i}^{d}\right) \\
& P\left(x_{i}, \delta_{i}^{u}, \delta_{i}^{d}, 1\right)=\frac{1 / \lambda_{i}^{\Omega}}{1 / \lambda_{i}^{\Omega}+1 /\left(p_{i}^{\Omega} u_{i}^{u}\right)} \cdot P\left(x_{i}, \delta_{i}^{u}, \delta_{i}^{d}\right)
\end{aligned}
$$

The average WIP in the buffers can be obtained by:

$$
W_{i}=\sum_{\Omega_{i}} \sum_{\delta_{i}^{u}} \sum_{\delta_{i}^{u}} \sum_{x_{i}}\left(x_{i} \cdot P\left(x_{i}, \delta_{i}^{u}, \delta_{i}^{d}, \Omega_{i}\right)\right)
$$

Without considering the rework process, the production rate of the major production line is obtained by:

$$
\mathrm{PR}=\sum_{\Omega_{k-1}} \sum_{\delta_{k-1}^{u} \leq n_{k-1}^{u}} \sum_{\delta_{k-1}^{u}} \sum_{x_{k-1} \geq 1} P\left(x_{k-1}, \delta_{k-1}^{u}, \delta_{k-1}^{d}, \Omega_{k-1}\right) u_{k-1}^{d}
$$

The overall production rate of the closed-loop production line can be obtained using the production rate of major and minor production lines.

## Performance evaluation of the overall production line considering the rework process

In Sections "Performance evaluation of minor production line" and "Performance evaluation of major production line," the modelling and production rate evaluation of the major and minor production lines are studied, respectively. In this section, the two parts of the production line and the rework site are combined to obtain the overall production rate of the production line.

For the production line $M_{j}, M_{j+1} \ldots M_{k}$, the probability $\mathrm{pd}_{i, \delta_{i}}$ that the machine $M_{i}$ produces unqualified products is different in different states. Therefore, PM actions under different conditions will affect the average defective rate of machine $M_{i}$, which can be calculated by:

$$
\operatorname{pdef}_{i}=\sum_{\delta_{i}=1}^{\operatorname{arc}_{i, \delta} \operatorname{arc}_{i, \delta_{i}}=1} \operatorname{Pr}\left(\delta_{i}\right) \mathrm{pd}_{i, \delta_{i}}
$$

where $p t_{i, \delta_{i}}=1$ represents that the PM action is carried out when the machine reaches the state $\delta_{i}$, and $\operatorname{Pr}\left(\delta_{i}\right)$ is the probability that the degradation state of $M_{i}$ is $\delta_{i}$.

In the closed-loop production line, the unqualified products produced by different machines will flow to downstream machines without inspection. Considering the rework process, the production rate of qualified products in the major production line is given by:

$$
\begin{aligned}
& \mathrm{PR}^{\prime}=\sum_{\Omega_{k-1}} \sum_{\delta_{k-1}^{u} \leq n_{k-1}^{u}} \sum_{\delta_{k-1}^{u}} \sum_{x_{k-1} \geq 1} P\left(x_{k-1}, \delta_{k-1}^{u}, \delta_{k-1}^{d}, \Omega_{k-1}\right) u_{k-1}^{d} \\
& \cdot \frac{\left(S_{0} /\left(\operatorname{pdef}_{j} \cup \operatorname{pdef}_{j+1} \cup \cdots \cup \operatorname{pdef}_{k}\right)\right)}{\left(S_{0} /\left(\operatorname{pdef}_{j} \cup \operatorname{pdef}_{j+1} \cup \cdots \cup \operatorname{pdef}_{k}\right)\right)+\left(S_{0} / u_{k-1}^{d}\right)}
\end{aligned}
$$

The uniform rework is performed when the number of unqualified products reaches the capacity of the repair site buffer. Therefore, the major production line has two different product input sources. The first source is the products from the minor production line. In this case, the final production rate is denoted as $\mathrm{PR}_{a}$, with the initial parameter $\mu_{a}(j)=P(j-1)$. The second source is the products accumulated in the rework site, which is independent of the production rate of the minor production line. In this case, the final production rate is denoted as $P R_{b}$, with the initial parameter $\mu_{a}(j)=\mu_{j}$. The final qualified production rate of the overall production line can be obtained by:

$$
\begin{gathered}
T H=P R_{a} *\left(1-\prod_{i=j}^{i=k}\left(1-p d e f_{i}\right)\right) \\
+P R_{a} * \prod_{i=j}^{i=k}\left(1-p d e f_{i}\right) * P R_{b}
\end{gathered}
$$

## Cost model

The corrective maintenance policy is adopted for the production line $M_{1}, M_{2} \ldots M_{j-1}$ during the planning time horizon $T$. Therefore, the maintenance cost $C_{\mathrm{m} 1}$ for the minor production line is calculated by:

$$
\begin{gathered}
C_{\mathrm{m} 1}=\sum_{i=1}^{i=j-1} C_{\mathrm{icm} 1} \frac{T}{\mathrm{MTTR}_{i}+\mathrm{MTBF}_{i}} \\
=\sum_{i=1}^{i=j-1} C_{\mathrm{icm} 1} \frac{T}{(1 / \operatorname{fr}(i))+(1 / r(i))}
\end{gathered}
$$

where $C_{\mathrm{icm} 1}$ is the single repair cost of $M_{i}(i=1,2 \ldots j-1)$.
The maintenance cost $C_{\mathrm{m} 2}$ for the major production line consists of PM cost $C_{\mathrm{pm} 2}$, corrective maintenance $C_{\mathrm{cm} 2}$ and rework cost $C_{\mathrm{r}}$.

$$
C_{\mathrm{m} 2}=C_{\mathrm{pm} 2}+C_{\mathrm{cm} 2}+C_{\mathrm{r}}
$$

When the corrective maintenance policy is adopted for the production line $M_{j}, M_{j+1} \ldots M_{k}$, the corrective maintenance $C_{\mathrm{cm} 2}(i)$ is calculated by:

$$
\begin{gathered}
C_{\mathrm{cm} 2}(i)=\frac{T}{\mathrm{MTTR}_{i}+\mathrm{MTBF}_{i}} \\
C_{\mathrm{icm} 2}=\frac{T}{\left(1 / \lambda_{i}\right)+\sum_{\delta_{i}=0}^{\delta_{i m}}\left(1 / p_{i, \delta_{i}}\right)} C_{\mathrm{icm} 2}
\end{gathered}
$$

where $C_{\mathrm{icm} 2}$ is the single corrective maintenance cost of $M_{i}(i=j, j+1 \ldots k)$, and the PM cost is $C_{\mathrm{pm} 2}(i)=0$.

When the PM policy is adopted for the production line $M_{j}, M_{j+1} \ldots M_{k}$, the PM cost $C_{\mathrm{pm} 2}(i)$ is calculated by:

$$
\begin{aligned}
& C_{\mathrm{pm} 2}(i)=\frac{T}{\mathrm{MTTR}_{i}+\mathrm{MTBF}_{i}} C_{\mathrm{ipm}}\left(\delta_{i}\right) \\
& =\frac{T}{\left(1 / m_{i}\right)+\sum_{\delta_{i}=0}^{\delta_{i m}-1} 1 / p_{i, \delta_{i}}} C_{\mathrm{ipm}}\left(\delta_{i}\right)
\end{aligned}
$$

where $C_{\mathrm{ipm}}\left(\delta_{i}\right)$ is the single PM cost of $M_{i}(i=j$, $j+1 \ldots k$ ) in case that machine state is at $\delta_{i}$, and the corrective maintenance cost is $C_{\mathrm{cm} 2}(i)=0$.

Therefore, the PM cost $C_{p m 2}$ and corrective maintenance cost $C_{c m 2}$ of the major production line are given by:

$$
\begin{aligned}
& C_{p m 2}=\sum_{i=j}^{k} C_{p m 2}(i) \\
& C_{c m 2}=\sum_{i=j}^{k} C_{c m 2}(i)
\end{aligned}
$$

When the buffer $B_{0}$ is full, a uniform rework is performed for unqualified products detected at the end of the production line. The rework cost $C_{r}$ is calculated by:

$$
C_{r}=C_{u v} \cdot T \cdot \frac{S_{0}}{\frac{S_{0}}{p d e f_{j} \cup p d e f_{j+1} \cup \cdots \cup p d e f_{k}}+\frac{S_{0}}{u_{j-1}^{d}}}
$$

where $C_{u v}$ represents the rework cost per unit product.
The pallet cost $C_{p}$ and WIP holding cost $C_{w}$ are also taken into consideration.

$$
C_{p}=N_{0} \times C_{\mathrm{up}}
$$

$$
C_{w}=T \times C_{\mathrm{uw}} \times \sum_{i=j}^{k} W_{i}
$$

where $C_{\text {up }}$ is the cost of a single pallet, and $C_{\text {uw }}$ is the WIP holding cost per unit of time.

In summary, the system total cost in the planning time horizon $T$ can be given by:

$$
C=C_{m 1}+C_{p m 2}+C_{c m 2}+C_{r}+C_{p}+C_{w}
$$

This model aims to find the optimal PM strategy and the optimal number of pallets to maximize system profit. The objective function and constraints are described as follows:

$$
\max Q=\max \left[T H \times T \times \text { Price }-\left(C_{m 1}+C_{m 2}+C_{p}+C_{w}\right)\right]
$$

s.t.

$$
\begin{gathered}
\sum_{i=1}^{k} x_{i} \leq N_{0} \\
\sum_{y_{i}=1}^{y_{i}} p t_{i, \delta_{i}}=1 \\
0 \leq p d_{i, \delta_{i}}<p d_{i, \delta_{i}+1} \leq 1 \\
p d_{i, \delta_{i}+1}=1 \\
\sum_{\Omega_{i}} \sum_{\delta_{i}^{d}} \sum_{\delta_{i}^{u}} \sum_{x_{i}} P\left(x_{i}, \delta_{i}^{u}, \delta_{i}^{d}, \Omega_{i}\right)=1
\end{gathered}
$$

where $Q$ is the system total profit, Price is the income of a single product.

## Hybrid PSO-EDA optimization

From the above analysis, it can be seen that the machines in the major production line have multi-stage degradation, and the machine status will affect the qualified product output rate of the production line. Therefore, PM is used to ensure the reliability of the machines of the production line and reduce total cost and increase effective output. However, the PM strategy of the major production line is difficult to solve with traditional analytical methods, and a meta-heuristic algorithm is required.

Particle swarm optimization (PSO) is a swarm intelligence based numerical optimization algorithm, inspired by birds' flocking or fish schooling for the solution of nonlinear, nonconvex or combinatorial optimization problems that arise in many science and engineering domains. ${ }^{40}$ Its main idea is that each particle learns from other particles and it also learns from its own experience during the movement, to make it move towards the optimal solution. However, only the optimal particle can affect the subsequent movement of other particles, so it is easy to fall into the local optimal situations. In recent years, as a new evolutionary algorithm, the estimation of distribution algorithm (EDA) has received increasing attention from scholars. ${ }^{41}$ EDA does not adopt the mutation or crossover operation of traditional evolutionary algorithms such as the genetic algorithm. Instead, it accumulates historical information of multiple optimal individuals by establishing probabilistic models, and then generates new individuals based on probabilistic models to guide the evolutionary direction of the population. As a result, EDA shows an outstanding performance in global optimization.

In this section, the characteristics of the PSO and EDA are combined, and a hybrid PSO-EDA optimization method is proposed. By making use of the advantages of global and local optimization, the algorithm's ability to seek an optimal PM strategy is improved. The main steps of the algorithm are described as follows. The flowchart of the algorithm can be found in Figure 4.

## Encoding

Based on the idea of a discrete particle swarm optimization algorithm, binary encoding is used for the individuals. The individuals are described as follows:

$$
\begin{aligned}
X & =\left[X^{1}, X^{2}, \ldots, X^{N}\right], X^{j} \\
& =\left[x_{1}^{j}, x_{2}^{j}, \cdots, x_{\sum n_{i}}^{j}\right] \\
x_{j}^{j} \in\{0,1\} & (l=1,2, \cdots, \sum n_{i} i=1,2, \cdots \\
k j & =1,2, \cdots, N)
\end{aligned}
$$

where $N$ is the number of individuals, $x_{j}^{j}$ is the position value of $j$ th position in $j$ th individual.

In Figure 5, an individual $X^{j}$ represents a feasible solution $G$, the dimension of which is $\sum n_{k}$. The particle segment with dimension $n_{i}$ is the gene for PM decision of machine $M_{i}$. When $x_{j k}^{j} \sum_{n_{i-1}}=1\left(\sum_{l=1}^{n_{i}} x_{j k}^{j} \sum_{n_{i-1}}=1\right)$, machine $M_{i}$ performs PM in state $l$, that is $\delta_{i n k}=l$.

## Initialization

To obtain the distribution information of the solution space, the diversity of the initial population must be guaranteed. Therefore, the algorithm uses random initialization to generate $N$ particles as the initial population, that is $X_{\text {ini }}=\left[X^{1}, X^{2} \ldots, X^{N}\right]$.

## Fitness evaluation

All particles are used in the model to solve the fitness value of each feasible solution, which is the total profit $f(G)=Q$. Then the individual historical optimal value of all particles $X_{\text {gene }}^{\text {phasic }}\left(j=1,2, \cdots, N\right)$, the individual historical suboptimal value $X_{\text {gene }}^{\text {phasic }}(j=1,2, \cdots, N)$ and the global optimal value $X_{\text {gene }}^{\text {ghoof }}$ are recorded, respectively.

## Population division

The population is randomly divided into two subpopulations $A$ and $B$, in which the number of individuals is $N A$ and $N B=N-N A$. Then the new offspring of subpopulations $A$ and $B$ are generated according to the probabilistic model ofEDA and the individual flying model of PSO, respectively.

## Probabilistic model

The EDA collects the historical information of outstanding individuals through the probability model, guiding the evolution direction of the population. Therefore, the selection of the probability model is the key to the performance of the algorithm. In this section, a probability matrix $P$ with the dimension $\sum n_{i} \times 2$ is used to represent the probability model of the solution space distribution, where is the element of the matrix, which represents the probability that the value of position $l$ of the particle at generation gene is $m$.

Particles in subpopulation $A$ are sorted according to fitness value, and the best $M P$ individuals are defined as a superior subpopulation. Then the matrix $P$ is initialized based on the following equation:

$$
p_{m i}(1)=\frac{1}{M P} \sum_{j=1}^{M P} l_{m i}^{(j)}(1), \forall m, l \in \sum n_{i}
$$

where the indicator function in the superior subpopulation is given as $l_{m i}^{(j)}$ (gene) $=$ $\left\{\begin{array}{ll}1, & \text { if position } l \text { of particle } j \text { is } m \\ 0, & \text { else }\end{array}\right\}$.

## Probability matrix sampling method

In each generation of the EDA, new individuals are generated via sampling the solution space according

![img-3.jpeg](img-3.jpeg)

Figure 4. The flowchart of the proposed PSO-EDA algorithm.
to the probability matrix $P$. A new particle is generated using roulette sampling from the 1 st to the $\sum n_{i}$ th sequentially. When $x_{I x}^{I} \sum n_{i-1}=1$, let $x_{I I x}^{I} \sum n_{i-1}=$ $0(l l=1,2, \cdots, n_{i} ; l l \neq l)$ to ensure the feasibility
of the solution generated by sampling, preventing PM activities in the two different states of the machine. Finally, a population of $N A$ individuals is generated.

![img-4.jpeg](img-4.jpeg)

Figure 5. Binary encoding method of a feasible solution.

## Update of individual flying model

For the subpopulation $B, N B$ particles are updated using an individual flying model. The particle velocity is encoded as follows:

$$
\begin{gathered}
V=\left[\begin{array}{lll}
V^{1}, & V^{2} \ldots, V^{N B}
\end{array}\right], V^{j}=\left[\begin{array}{llll}
v_{1}^{j}, & v_{2}^{j}, & \cdots, & v_{n}^{j}
\end{array}\right] \\
0 \leq v_{i}^{j} \leq 1\left(l=1,2, \cdots, \sum n_{i} ; i=1,2, \cdots, k ; j=1,2, \cdots, N B\right)
\end{gathered}
$$

In the first generation of iterations, the speed of the subpopulation $B$ needs to be initialized randomly. The $v_{j}^{j}$ indicates the probability of $x_{j}^{j}$ taking the value 0 .

To avoid premature convergence, the velocity and position of each individual in the subpopulation $B$ are updated according to the following equations:

$$
\begin{aligned}
v_{\text {gene }}^{\text {phest }, j} & =\alpha x_{\text {gene }}^{\text {phest }, j}+\beta\left(1-x_{\text {gene }}^{\text {phest }, j}\right) \\
v_{\text {gene }}^{\text {phest }} & =\alpha x_{\text {gene }}^{\text {phest }}+\beta\left(1-x_{\text {gene }}^{\text {phest }}\right) \\
v_{\text {gene }}^{\text {abest }, j} & =\alpha x_{\text {gene }}^{\text {abest }, j}+\beta\left(1-x_{\text {gene }}^{\text {abest }, j}\right) \\
v_{\text {gene }+1}^{j} & =\omega v_{\text {gene }}^{j}+c_{1} v_{\text {gene }}^{\text {abest }, j}+c_{2} v_{\text {gene }}^{\text {abest }}+c_{3} v_{\text {gene }}^{\text {abest }, j}
\end{aligned}
$$

where $v_{\text {gene }}^{j}$ is the velocity vector of the $j$ th particle at generation gene. $\omega$ is the inertia weight, and $0<\alpha<\beta<1$ represent coefficients for velocity control. Let $x_{\text {gene }+1}^{j}\left(l+\sum n_{i-1}\right)=1$, with $x_{\text {gene }+1}^{j}\left(l l+\sum n_{i-1}\right)=$ $0(l l=1,2, \ldots, n_{i} ; l l \neq l)$, where $v_{\text {gene }+1}^{j}\left(l+\sum n_{i-1}\right)$ is the minimum value of $v_{\text {gene }+1}^{j}$ between position $\sum n_{i-1}$ and $\sum n_{i}$.

To avoid the disadvantages of the fixed parameters in the PSO, the inertia weight is adaptively adjusted according to the fitness value, which is given by:

$$
\omega=W(f)= \begin{cases}\omega_{\min }-\frac{\left(\omega_{\max }-\omega_{\min }\right)\left(f-f_{\min }\right)}{f_{\text {avg }}-f_{\min }}, & f \leq f_{\text {avg }} \\ \omega_{\max }, & f>f_{\text {avg }}\end{cases}
$$

where $\omega_{\max }$ and $\omega_{\min }$ are the maximum and minimum values of $\omega$, respectively; $f$ is the fitness value of the particle; $f_{\text {avg }}$ and $f_{\text {min }}$ are the average fitness value and minimum fitness value of all particles.

## Population merging

The two subpopulations $A$ and $B$ obtained by using the probability model and the individual flying model are merged. And all particles are sorted according to the fitness value to obtain a new population containing $N$ particles.

## Mutation method

To avoid premature convergence, the exchange mutation is performed to maintain the diversity of the population. The $l_{1}$ position of the $j$ th particle segment is randomly selected in a particle, then the value in position $l_{1}$ and $l_{2}=\operatorname{arc}_{l}$ $\left(x_{l+}^{j} \sum_{n_{i-1}}=1\right)$ are exchanged as the following equations.

$$
\begin{aligned}
& x_{l_{1}+}^{j} \sum_{n_{i-1}}=1-x_{l_{1}+}^{j} \sum_{n_{i-1}} \\
& x_{l_{2}+}^{j} \sum_{n_{i-1}}=1-x_{l_{2}+}^{j} \sum_{n_{i-1}}
\end{aligned}
$$

## Update of probabilistic model

In the next generation, the subpopulation $A$ with $N A$ individuals determines the superior subpopulation that consists of $M P$ individual historical optimal particles in the new population. Then the probability matrix $P$ is updated according to the following equation:

$$
\begin{aligned}
& p_{\mathrm{ml}}^{A}(\text { gene }+1)=(1-\gamma) p_{\mathrm{ml}}^{A}(\text { gene }) \\
& \quad+\frac{\gamma}{M P} \cdot \sum_{j=1}^{M P} l_{\mathrm{ml}}^{A j}(\text { gene }+1)
\end{aligned}
$$

where $\gamma(0<\gamma<1)$ is the learning rate of matrix $P$.

## New solutions acceptance method

To increase the local search efficiency of the PSO-EDA, an acceptance probability of simulated annealing is introduced for updating the individual historical optimal value. The specific steps of the new solutions acceptance method are described as follows:

Step 1: Initialize the temperature $t$ and get the initial feasible solution $G$.
Step 2: Get the new feasible solution $G^{\prime}$ after the iteration update.
Step 3: Calculate the fitness value differential $\Delta g=$ $f(G^{\prime})-f(G)$, where $f(G)$ is the fitness function.
Step 4: If $\Delta g>0$, accept $G^{\prime}$ as the new historical optimal solution; otherwise, accept it with the probability of $\exp (\Delta g / T)$.

Initializing $X, P, V, X_{\text {gene }}^{p b e s t, j}(j=1,2, \cdots, N), X_{\text {gene }}^{n b e s t, j}(j=1,2, \cdots, N), X_{\text {gene }}^{g b e s t}$ $T \leftarrow T_{0} ;$
while $\{T>1\}$ do
$G \leftarrow X$;
for $\{j=1$ to $N A\}$ do
subpopulation $\mathrm{A} \leftarrow$ implement roulette sampling according to $P$
if $\left\{x_{l+\sum n_{i-1}}^{j}=1\right\}$

$$
x_{l l+\sum n_{i-1}}^{j} \leftarrow 0\left(l l=1,2, \cdots, n_{i} ; l l \neq l\right)
$$

end
end
for $\{j=1$ to $N B\}$ do
$\omega \leftarrow W(f(j))$;
$v_{\text {gene }+1}^{j} \leftarrow \omega v_{\text {gene }}^{j}+c_{1} v_{\text {gene }}^{p b e s t, j}+c_{2} v_{\text {gene }}^{g b e s t}+c_{3} v_{\text {gene }}^{n b e s t, j}$;
$x_{\text {gene }+1}^{j}\left(l+\sum n_{i-1}\right) \leftarrow 1: l+\sum n_{i-1}=\arg _{\sum n_{i-1} \text { to } \sum n_{i}} v_{\text {gene }+1}^{j} ;$
$x_{\text {gene }+1}^{j}\left(l l+\sum n_{i-1}\right) \leftarrow 0\left(l l=1,2, \ldots, n_{i} ; l l \neq l\right)$;
update subpopulation B;
end
$G^{\prime} \leftarrow$ merging subpopulations A and B ;
population mutation;
update $P$ and $G^{\prime}$;
for $\{i=1$ to $N\}$ do
$\Delta \mathrm{t}^{\prime}=f\left(G^{\prime}\right)-f(G)$;
if $\left\{\Delta \mathrm{t}^{\prime}>0\right\}$

$$
X(i) \leftarrow G^{\prime}(i)
$$

elseif $\left\{\operatorname{rand}() \geq \exp \left(\Delta \mathrm{t}^{\prime} / T\right)\right\}$

$$
X(i) \leftarrow G^{\prime}(i)
$$

else

$$
X(i) \leftarrow G(i)
$$

end
end
$T \leftarrow d \times T$
end

Figure 6. The pseudo code of the PSO-EDA algorithm.

![img-5.jpeg](img-5.jpeg)

Figure 7. The effect of the number of machines and pallets on production rate, profit, and cost.

Step 5: The temperature $t$ gradually decreases in each iteration until the termination condition is satisfied, otherwise go to Step 2.

## Pseudo code of PSO-EDA algorithm

Based on the above analysis, the pseudo code of the hybrid PSO-EDA optimization is presented in Figure 6.

## Numerical example

This section takes a closed-loop production system as an example to analyze and verify the models and algorithms in this paper. For the convenience of numerical calculation and analysis, ${ }^{42}$ the repair time of the machines $M_{1}, M_{2}, \ldots, M_{j-1}$ in minor production line follows

Table I. Machine parameters in the closed-loop production line.

| Machines | $\mu_{i}$ | $1 / f_{i}\left(n_{i} / p_{i, \lambda}\right)$ | $1 / r_{i}\left(1 / \lambda_{i}\right)$ | $1 / p_{i}$ |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 0.89 | 29 | 9 | 19 |
| 2 | 1.11 | 24 | 6 | 17 |
| 3 | 1.11 | 29 | 10 | 15 |
| 4 | 0.91 | 30 | 7 | 19 |
| 5 | 1.22 | 17 | 9 | 9 |
| 6 | 1.13 | 21 | 8 | 9 |
| 7 | 0.88 | 29 | 6 | 10 |
| 8 | 0.76 | 25 | 8 | 13 |
| 9 | 0.88 | 15 | 6 | 10 |
| 10 | 1.12 | 22 | 5 | 10 |
| 11 | 0.70 | 16 | 7 | 13 |
| 12 | 0.90 | 23 | 8 | 15 |
| 13 | 1.01 | 23 | 6 | 9 |
| 14 | 0.85 | 19 | 9 | 11 |
| 15 | 1.36 | 25 | 7 | 12 |
| 16 | 1.19 | 25 | 6 | 10 |
| 17 | 1.27 | 20 | 6 | 20 |
| 18 | 1.04 | 17 | 9 | 19 |
| 19 | 1.11 | 22 | 7 | 8 |
| 20 | 1.14 | 18 | 6 | 19 |
| 21 | 1.38 | 24 | 10 | 19 |
| 22 | 0.94 | 17 | 10 | 12 |
| 23 | 1.33 | 17 | 10 | 19 |
| 24 | 1.10 | 19 | 5 | 12 |
| 25 | 0.95 | 15 | 10 | 13 |
| 26 | 0.48 | 15 | 5 | 13 |
| 27 | 1.19 | 28 | 10 | 17 |
| 28 | 0.51 | 15 | 9 | 13 |
| 29 | 0.76 | 25 | 8 | 10 |
| 30 | 0.96 | 22 | 5 | 13 |

an exponential distribution, where $j=k / 2$. The model parameters are set to be $T=300, S_{0}=30$, Price $=$ $40, C_{\mathrm{icm} 1}=4, C_{\mathrm{icm} 2}=4, C_{\mathrm{ipm}}=6, C_{\mathrm{up}}=5, C_{\mathrm{ur}}=20$, $C_{\mathrm{uw}}=0.1$. The number of the state of machines $M_{j}, M_{j+1} \ldots M_{k}$ in the major production line is $n_{i}=5$. The parameters of 30 machines are listed in Table 1. The parameters in brackets indicate the parameters of the machine as it is in the major production line. The number of populations in the hybrid PSO-EDA algorithm is $N=20$. The algorithm parameters are set to be $\mathrm{NA}=$ $N / 2, \alpha=0.3, \beta=0.7, c_{1}=0.3, c_{2}=0.7, c_{3}=0.2$, $\omega_{\max }=0.8, \omega_{\min }=0.3, \gamma=0.2, t_{0}=300, d=0.95$.

In the numerical example, the proposed model is evaluated by the sensitivity analysis method. Figure 7 describes the effect of different numbers of machines and pallets on the total profit, total cost, and production rate. In Figure 7(a), the number of pallets is fixed at 60. In Figure 7(b), the number of machines is fixed at 15. Figure 7 shows that the production rate and total profit will increase with the increase in the number of pallets, but decrease with the increase in the number of machines.

Based on the above experimental analysis, it can be seen that the difference in the number of machines and the number of pallets will cause the production rate to change accordingly. Figure 8 shows the combined
impact of different numbers of machines and different numbers of pallets on the system. It can be seen from Figure 8 that when the number of machines is fixed, the system profit increases with the increase in the number of pallets; and when the number of pallets is fixed, the profit decreases with the increase in the number of machines.

Figure 9 shows the effect of rework site location on production rate, profit, and cost. In this case, the numbers of machines and pallets are set to be 30 and 60 , respectively. The proportion of the minor production line is the value of $j / k$, which becomes higher when the location of the rework site in the production line is relatively backward. It can be seen that as the location of the rework site moves backwards, the length of the major production line is shortened, and the probability of producing unqualified products in the production line will be reduced, increasing the final production rate. The cost of the rework and PM has decreased, causing a reduction in the total cost and an increase in total profit.

To verify the performance of the proposed PSO-EDA algorithm, the following experiment compares the effect of the PSO-EDA algorithm with the standard PSO algorithm. In the experiment in Figure 10(a), the number of machines and pallets are set to be 20 and 60 , respectively. Figure 10(a) shows the cost and profit comparison results of the PSO-EDA and PSO algorithms. It can be seen that the PSO algorithm leads to higher rework cost and lower profit, which means the PM strategy obtained by the PSO algorithm is not optimal, increasing the output of unqualified products.

Figure 10(b) explores the difference in the production rate between the PM strategy obtained by the PSO-EDA and PSO algorithm, under different numbers of machines and machine states in the major production line. It shows that the production rate corresponding to the PSO-EDA algorithm is always higher than the production rate corresponding to the PSO algorithm. The difference in production rate has increased significantly with the increase in the number of machines. In this experiment, the number of machine states after the rework is set to be constant. As the number of machine states increases, the difference in production rate slowly increases. As expected, the experiment proved that the PSO-EDA algorithm is more efficient than the substandard PSO algorithm with a lower maintenance cost and a higher total profit. The difference between the production rate of the two algorithms under different conditions is about $4 \%$ to $9 \%$. And as the number of machines and the number of machine states increase, the advantages of the PSO-EDA algorithm become even more outstanding.

To comprehensively evaluate the efficiency of each algorithm, an analysis of variance (ANOVA) at a $95 \%$ confidence level is carried out to detect a significant difference in the performance of the algorithms. Table 2 shows the ANOVA results to compare the average profit of two algorithms under three different problem

![img-6.jpeg](img-6.jpeg)

Figure 8. The joint effect of numbers of machines and pallets on total profit.
![img-7.jpeg](img-7.jpeg)

Figure 9. The effect of rework site location on production rate, profit and cost.
scales, which are small scale with 5 machines and 3 states, medium scale with 15 machines and 5 states, and large scale with 30 machines and 10 states. It can be seen that all the $p$-value are less than 0.05 at a $95 \%$ confidence
level, indicating that there exist significant differences among the means of the objective function value. The results prove that the performance of PSO-EDA is better under different circumstances.

![img-8.jpeg](img-8.jpeg)

Figure 10. The comparison of PSO-EDA and PSO algorithms.

## Conclusion

This paper proposes the performance evaluation and optimization model considering the product quality and PM policy for the closed-loop production line to maximize the system total profit. Degradation and rework processes are also taken into consideration which improves the
industrial applicability. The performance optimization problem is formulated based on the two-machine-onebuffer decomposition method and the degradation state transition. Since it is extremely difficult to solve the original problem, the authors developed a hybrid PSO-EDA algorithm to obtain the optimal solution. In the numerical example, sensitivity analysis and comparison experiments

Table 2. Analysis of variance of different algorithms performance.

| Problem <br> scale | Source | df | Adj. SS | Adj. |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  |  |  | MS | F-Value | $p$-Value |
| Small | Factor | I | 121.1 | 121.1 | 12.81 | 0.002 |
|  | Error | 19 | 179.6 | 9.4 |  |  |
|  | Total | 20 | 300.7 |  |  |  |
| Medium | Factor | I | 1161.3 | 1161.3 | 13.76 | 0.0015 |
|  | Error | 19 | 1603.5 | 84.4 |  |  |
|  | Total | 20 | 2764.8 |  |  |  |
| Large | Factor | I | 3990.9 | 3990.9 | 36.59 | 0.000 |
|  | Error | 19 | 2072.4 | 109.8 |  |  |
|  | Total | 20 | 6063.3 |  |  |  |

are studied in order to explore the effect of decision variables and the proposed PSO-EDA algorithm.

Based on the findings of the numerical example, the following remarks can be concluded. (1) The numerical example demonstrates that the proposed model can improve product quality, optimize the production processes, and enable the enterprises to obtain more profit than ever before. (2) It shows that the number of machines, the number of pallets, and PM policy have a comprehensive influence on the performance of the system. Consequently, it is necessary and sensible to optimize these variables simultaneously by trading off their effects. (3) The system's output under the PM strategy based on the PSO-EDA algorithm is higher than the general PM strategy based on traditional PSO algorithm. When comparing the total profit and production rate, the PM strategy based on the PSO-EDA algorithm shows better performance, outperforming the general PM strategy by $20.9 \%$ and $6.77 \%$, respectively, under 20 machines and 60 pallets.

As future work, some assumptions can be relaxed. A straightforward relaxation consists to consider the economic efficiency of rework. It is assumed that the only solution for the unqualified products is to process them again. However, in practical production systems, due to the high cost of rework, unqualified products can be discarded unless necessary or economic, which complicates the model. Other future works can consider imperfect inspections and how to deal with inspection errors, which makes the model more realistic.

## Declaration of conflicting interests

The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article.

## Funding

The author(s) disclosed receipt of the following financial support for the research, authorship, and/or publication of this article: the National Natural Science Foundation of China (grant number 71471135).

## ORCID iD

Binghai Zhou (s) https://orcid.org/0000-0002-6599-9033

## References

1. Biller S, Marin SP, Meerkov SM, et al. Closed Bernoulli production lines: analysis, continuous improvement, and leanness. IEEE Trans Autom Sci Eng 2009; 6: 168-180.
2. Li J, Blumenfeld DE, Huang N, et al. Throughput analysis of production systems: recent advances and future topics. Int J Prod Res 2009; 47: 3823-3851.
3. Shi C and Gershwin SB. Improvement of the evaluation of closed-loop production systems with unreliable machines and finite buffers. Comput Ind Eng 2014; 75: 239-256.
4. Chen KS, Chen DF, Huang MC, et al. Analyzing processing quality of machine tools via processed product: example of ball valve processing machine. Proc Inst Mech Eng Part E J Process Mech Eng 2020; 234: 331-341.
5. Ferreira LP, Gómez EA, Lourido GCP, et al. Analysis and optimisation of a network of closed-loop automobile assembly line using simulation. Int J Adv Manuf Technol 2012; 59: $351-366$.
6. Yang S, Riggs RJ and Hu SJ. Modeling and analysis of closed loop manufacturing systems using parameter coupling. J Manuf Syst 2013; 32: 817-824.
7. Park CW and Lee HS. Performance evaluation of a multiproduct CONWIP assembly system with correlated external demands. Int J Prod Econ 2013; 144: 334-344.
8. Hajej Z, Rezg N and Bouslikhane S. A joint production and maintenance optimization of closed-loop production system under carbon emission with a switching subcontractor consideration. Appl Sci 2019; 9: 1105.
9. Li X, Ran Y, Zhang G, et al. Selective maintenance of multistate series systems considering maintenance quality uncertainty and failure effects. Proc Inst Mech Eng Part E J Process Mech Eng 2021; 235: 1363-1374.
10. Bouhchouch A, Frein Y and Dallery Y. Analysis of a closed-loop manufacturing system with finite buffers. Appl Stoch Model Data Anal 1993; 9: 111-125.
11. Biller S, Marin SP, Meerkov SM, et al. Closed production lines with arbitrary models of machine reliability. 4th IEEE Conf Autom Sci Eng CASE 2008 2008: 466-471.
12. Gershwin SB and Werner LM. An approximate analytical method for evaluating the performance of closed-loop flow systems with unreliable machines and finite buffers. Int J Prod Res 2007; 45: 3085-3111.
13. Feng Y, Zhong X, Li J, et al. Closed-loop production lines with geometric reliability machines: modeling, analysis, and application. IEEE Robot Autom Lett 2018; 3: 704-711.
14. Jia Z, Dai Y and Chen J. Closed Bernoulli lines with finite buffers: real-time performance analysis, completion time bottleneck and carrier control. Int J Control 2021; 94: 1994-2007.
15. Gu X, Guo W and Jin X. Performance evaluation for manufacturing systems under control-limit maintenance policy. J Manuf Syst 2020; 55: 221-232.
16. Li X, Ran Y and Zhang G. Optimization of equal-cycle maintenance strategy considering imperfect preventive maintenance. Proc Inst Mech Eng Part E J Process Mech Eng 2022; 236: 1392-1402.
17. Dui H, Yang X and Fang Y. Evaluation methodology for preventive maintenance in multi-state manufacturing systems considering different costs. Int J Prod Res 2022. Epub ahead of print. DOI: 10.1080/00207543.2022.2127163.

18. Fitouhi MC, Nourelfath M and Gershwin SB. Performance evaluation of a two-machine line with a finite buffer and condition-based maintenance. Reliab Eng Syst Saf 2017; 166: 61-72.
19. Maggio N, Matta A, Gershwin SB, et al. A decomposition approximation for three-machine closed-loop production systems with unreliable machines, finite buffers and a fixed population. IIE Trans (Institute Ind Eng) 2009; 41: 562-574.
20. Ruifeng C and Subramaniam V. Increasing production rate in Kanban controlled assembly lines through preventive maintenance. Int J Prod Res 2012; 50: 991-1008.
21. Zhou B, Yu J, Shao J, et al. Bottleneck-based opportunistic maintenance model for series production systems. J Qual Maint Eng 2015; 21: 70-88.
22. Cheng G, Zhou B and Li L. Geometric process repair model for an unreliable production system with an intermediate buffer. Proc Inst Mech Eng Part E J Process Mech Eng 2017; 231: 747-759.
23. Zhou B, Qi F and Tao H. Condition-based maintenance modeling for a two-stage deteriorating system with random changes based on stochastic process. J Qual Maint Eng 2017; 23: 383-399.
24. You MY. An integrated optimization framework for multicycle environmental stress screening tests and preventive maintenance scheduling. Proc Inst Mech Eng Part E J Process Mech Eng 2017; 231: 1037-1044.
25. You MY. A generalized three-type lifetime probabilistic models-based hybrid maintenance policy with a practical switcher for time-based preventive maintenance and condition-based maintenance. Proc Inst Mech Eng Part E J Process Mech Eng 2019; 233: 1231-1244.
26. Chiu YSP, Tseng CY, Liu WC, et al. Economic manufacturing quantity model with imperfect rework and random breakdown under abort/resume policy. Proc Inst Mech Eng Part B J Eng Manuf 2009; 223: 183-194.
27. Kang Y, Yan H and Ju F. Performance evaluation of production systems using real-time machine degradation signals. IEEE Trans Autom Sci Eng 2020; 17: 273-283.
28. Cui PH, Wang JQ and Li Y. Data-driven modelling, analysis and improvement of multistage production systems with predictive maintenance and product quality. Int $J$ Prod Res 2021; 60: 6848-6865.
29. Liu N, Kim Y and Hwang H. An optimal operating policy for the production system with rework. Comput Ind Eng 2009; 56: 874-887.
30. Helber S and Jusić H. A new decomposition approach for non-cyclic continuous material flow lines with a merging flow of material. Ann Oper Res 2004; 125: 117-139.
31. Hadjinicola GC. Manufacturing costs in serial production systems with rework. J Oper Res Soc 2010; 61: 342-351.
32. Rabbani M, Manavizadeh N and Aghozi NSH. Robust optimization approach to production system with failure in rework and breakdown under uncertainty: evolutionary methods. Assem Autom 2015; 35: 81-93.
33. Zhou B and Lin S. A novel analysis model for optimization performance of Bernoulli serial production system considering rework processes. Proc Inst Mech Eng Part B J Eng Manuf 2020; 234: 295-309.
34. Cao Y, Subramaniam V and Chen R. Performance evaluation and enhancement of multistage manufacturing systems with rework loops. Comput Ind Eng 2012; 62: 161-176.
35. Ouaret S, Kenné JP and Gharbi A. Production and replacement planning of a deteriorating remanufacturing system in a closed-loop configuration. J Manuf Syst 2019; 53: 234-248.
36. Ghaleb M, Taghipour S, Sharifi M, et al. Integrated production and maintenance scheduling for a single degrading machine with deterioration-based failures. Comput Ind Eng 2020; 143: 106432.
37. Jia Z and Zhang L. Transient performance analysis of closed production lines with Bernoulli machines, finite buffers, and carriers. IEEE Robot Autom Lett 2017; 2: 1893-1900.
38. De Koster MBM. Estimation of line efficiency by aggregation. Int J Prod Res 1987; 25: 615-625.
39. Gershwin SB and Burman MH. A decomposition method for analyzing inhomogeneous assembly/disassembly systems. Ann Oper Res 2000; 93: 91-115.
40. Bansal JC. Particle swarm optimization. In: Evolutionary and Swarm Intelligence Algorithms. Berlin, Germany: Springer-Verlag Berlin, pp. 143-167.
41. Yang Q, Chen WN, Li Y, et al. Multimodal estimation of distribution algorithms. IEEE Trans Cybern 2017; 47: 636-650.
42. De Koster MBM. Capacity analysis of two-stage production lines with many products. Eng Costs Prod Econ 1987; 12: $175-186$.