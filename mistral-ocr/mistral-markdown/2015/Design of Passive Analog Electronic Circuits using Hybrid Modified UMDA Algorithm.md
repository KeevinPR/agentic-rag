# Design of Passive Analog Electronic Circuits using Hybrid Modified UMDA Algorithm 

Josef SLEZAK, Tomas GOTTHANS<br>Dept. of Radio Electronics, Brno University of Technology, Technická 12, 61600 Brno, Czech Republic<br>xsleza08@stud.feec.vutbr.cz, gotthans@feec.vutbr.cz


#### Abstract

Hybrid evolutionary passive analog circuits synthesis method based on modified Univariate Marginal Distribution Algorithm (UMDA) and a local search algorithm is proposed in the paper. The modification of the UMDA algorithm which allows to specify the maximum number of the nodes and the maximum number of the components of the synthesized circuit is proposed. The proposed hybrid approach efficiently reduces the number of the objective function evaluations. The modified UMDA algorithm is used for synthesis of the topology and the local search algorithm is used for determination of the parameters of the components of the designed circuit. As an example the proposed method is applied to a problem of synthesis of the fractional capacitor circuit.


## Keywords

Evolutionary algorithm, optimization, estimation of distribution algorithm, EDA, fractional capacitor

## 1. Introduction

In many areas of the engineering applications Estimation of Distribution Algorithms (EDA) have proved excellent capabilities of dealing with various kinds of problems of different nature. However, in the area of the evolutionary electronics utilization of the EDA algorithms has not been sufficient. Several papers focused on the evolutionary design of the whole analog circuit (the topology and the parameters of the components) have been published. In [2] Zinchenko published method of synthesis of the passive analog circuits using Univariate Marginal Distribution Algorithm (UMDA) algorithm however the method has two drawbacks. Parallel connection of the components in the branches of the circuits is not possible and with increasing number of the nodes of the designed circuit the number of the components is increasing more than necessary. Another paper focused on the evolutionary synthesis of the passive analog circuits using EDA algorithms was published by Torres [3] however the method employs UMDA algorithm only for determination of the number of the resistors, capacitors and inductors in the designed circuit. Minimal Switching Graph Problem solved using hybrid EDA algorithm method was presented in [4]. The method employs the UMDA to sample start search
points and a hill-climbing algorithm to find local optimum of the search space.

The proposed EDA algorithm solves the drawbacks of the method [2] mentioned above. The maximum number of the nodes and the maximum number of the components of the synthesized circuit can be set independently. Also encoding of the parallel components is possible. Furthermore the proposed method employs efficient hybrid approach which significantly reduces the number of the objective function evaluations. For the same optimization problem the number of the evaluations of the objective function of the proposed method is almost four times lower than for simulated annealing algorithm [12].

## 2. Hybrid Modified UMDA Algorithm

![img-0.jpeg](img-0.jpeg)

Fig. 1. Principal flowchart of the proposed method [1].
The flowchart of the proposed method is presented in Fig. 1. Population $P$ is formed of binary vectors of length 135 bits which are initialized randomly with seeding of 10 bits $\left(n_{c}=10\right)$. Parameters storage $e_{p s}$ is formed of a vector of length 135 consisting of real numbers in the range $\langle 0,1\rangle$. Parameters storage $e_{p s}$ is dynamically optimized during the whole synthesis process and it is adapted to the selected topologies in the selection phase of the algorithm. The vector includes a component value for every single admittance of the used expanded fully connected ad-

mittance network (see Sec. 6). During initialization phase $e_{p s}$ is set randomly with uniform distribution.

In the next step selected population $P_{s}$ is formed of the good individuals of the previous population $P$.

Probabilistic model $M$ of selected population $P_{s}$ is built. For more information on building of the probabilistic model in UMDA algorithm please refer to [5].

Probabilistic model $M$ built in the previous step is used for generation of new samples of solutions $P_{g}$. The new samples are generated using Stochastic Universal Sampling method (SUS) and are repaired using the repairing method described in Sec. 3.

The generated samples are evaluated using the topological information stored in the individuals of $P_{g}$ and the parameters of the components stored in $e_{p s}$. If the condition of execution of the local search algorithm is fulfilled, the local search algorithm tries to optimize the parameters of the current solution. If the accuracy of the current solution is improved, then storage of the parameters $e_{p s}$ is updated according to the results of the local search algorithm. Detailed description of the cost evaluation phase and the local search algorithm is presented in Sec. 4.

In the next step new population $P$ is formed of the best individuals of $P_{g}$ and selected population $P_{s}$. The described process is repeated until one of the termination criteria of the algorithm is met.

## 3. The Unitation Constraints

Generally desired specifications of an analog circuit are easier to reach using an analog circuit of higher complexity. Due to the fact the evolutionary analog circuits synthesis methods tend to evolve analog circuits with complexity as large as possible. Without restriction of the number of the components of the evolved circuit its complexity becomes higher than necessary.

Therefore the number of the components of the evolved circuit should be restricted to a user define value. Since in the proposed encoding method (section 6) the number of the components of the encoded circuit is determined by the number of the "ones" of the binary characteristic vector $c$ the restriction of the number of the components leads to a problem with unitation constraints [6].

Definition 1. Let's define vector $x=\left(x_{1}, x_{2}, \ldots, x_{n}\right) \in$ $\Omega$. Then the unitation value of $x$ is defined as

$$
u(x):=\sum_{i=1}^{n} x_{i}
$$

Value of unitation function $u(x)$ depends only on the number of the "ones" in an input binary vector $x$. The unitation values of two vectors with the same numbers of "ones" are equal.

A problem with unitation constraints is defined as solution $e$ in which unitation value $u(e)$ (the number of the "ones" in solution $e$ ) is restricted to a defined number [6].

As was described above the analog circuit synthesis problem has to be viewed as a problem with unitation constraints [6]. Modification of Factorized Distribution Algorithm (FDA) [7] which enables solving problems with unitation constraints was described in [6]. Modification of the UMDA algorithm which is able to handle the problems with unitation constraints is proposed in the text bellow. Pseudocode of the original UMDA algorithm [5] is presented in Fig. 2 .
step0: Set $k=1$. Generate $n_{i} \gg 0$ points randomly.
step1: Select $n_{s} \leq n_{i}$ points. Compute the marginal frequencies $r_{k ; i}\left(x_{i}\right)$ of the selected set.
step2: Generate $n_{i}$ new points according to the distribution $q_{k+1}(x)=\prod_{i=1}^{n} r_{k ; i}\left(x_{i}\right)$. Set $k=k+1$.
step3: If not terminated, go to step1.
Fig. 2. Pseudo-code of the original UMDA algorithm [1].

In [6] to handle unitation constraints problems only generation phase (sampling) of FDA algorithm was modified. The presented approach was adopted also in the proposed modification of the UMDA algorithm. The UMDA algorithm was implemented using toolbox MATEDA 2.0 [8]. Pseudo-code of the modified UMDA algorithm is presented in Fig. 3.
step0: Set $k=1$. Generate $n_{i} \gg 0$ points randomly.
step1: Select $n_{s} \leq n_{i}$ points. Compute the marginal frequencies $r_{k ; i}\left(x_{i}\right)$ of the selected set.
step2: Generate $n_{i}$ new points according to the distribution $q_{k+1}(x)=\prod_{i=1}^{n} r_{k ; i}\left(x_{i}\right)$. Set $k=k+1$.
step3: With regard to unitation constraints repair generated points.
step4: If not terminated, go to step1.
Fig. 3. Pseudo-code of the modified UMDA algorithm [1].
One additional step (step3) was added to the original UMDA algorithm. In step3 the generated samples are repaired to satisfy the desired unitation constraints.

The repairing function is applied to every single individual of the population of the generated samples in step2. Only $n_{c}$ "ones" with the highest marginal frequencies $r_{k ; l}$ of every generated sample are accepted. The rest of the "ones" of the samples are set to zero. If the number of the "ones" of the sample is equal or lower than $n_{c}$ then the sample is accepted without any modification and no repairing is performed. This way the number of the "ones" (which corresponds to the number of the components of the encoded analog circuit) of every generated sample never exceeds $n_{c}$.

Note that the repairing function is applied only for the part of the encoding vector $e$ which encodes the topology of the solution (characteristic vector $c$ in Fig. 13).

## 4. The Local Search Algorithm

Evaluation of the cost values and using of the local search algorithm will be discussed in the section. Principal flowchart of this phase is presented in Fig. 4.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Evaluation of the cost value and employing of the local search algorithm [1].

The following procedure which is described bellow is performed for every single individual $P_{g}(i)$ of the population of the generated samples $P_{g}$.

Based on the topology information stored in the binary vector of individual $P_{g}(i)$ appropriate set of parameters $P_{1}$ is loaded from parameters storage $e_{p s}$ and cost value $c_{1}$ of individual $P_{g}(i)$ is evaluated.

If the condition of execution of the local search algorithm (LSA) is fulfilled (rand $<P_{L S A}$ ) the LSA tries to improve accuracy of individual $P_{g}(i)$. The probability of execution of the LSA is set to $P_{L S A}=0.02$. The initial point of the search of the LSA is set to parameters set $P_{1}$. The number of the objective function evaluations of the LSA is set to MaxFunEvals $=100$. The results of the LSA are the cost value of the optimized solution $c_{2}$ and set of the optimized parameters $P_{2}$.

If the LSA is successful in improving of the accuracy of individual $P_{g}(i)$ and its cost value was improved $\left(c_{2}<c_{1}\right)$ then value cost of individual $P_{g}(i)$ is set to $c_{2}\left(\right.$ cost $\left.:=c_{2}\right)$ and the appropriate parameters of parameters storage $e_{p s}$ are updated according to parameters set $P_{2}$.

If the condition of execution of the LSA was not fulfilled ( $r$ and $>P_{L S A}$ ) or the LSA was not able to improve the cost value of individual $G(i)\left(c_{2} \geq c_{1}\right)$ the resulting value cost of individual $P_{g}(i)$ is set to $c_{1}\left(\right.$ cost $\left.:=c_{1}\right)$.

After performing of the described process cost value cost of individual $P_{g}(i)$ and updated parameters storage $e_{p s}$ are obtained. During the run of the algorithm the parameters stored in $e_{p s}$ are adapted to the topological information of the good individuals selected in the selection phase of the algorithm (Fig. 1). This way the information about the topology stored in $P_{g}$ and the information about the parameters stored in $e_{p s}$ are mutually optimized and the whole synthesis process is directed towards the promising areas of the solution space.

## 5. Application of the Method

A problem of synthesis of a fractional capacitor circuit was adopted from [9] and will be used for demonstration of the synthesis capabilities of the proposed method. The goal is to synthesize a circuit with input impedance (2)

$$
Z_{i n}=s^{-0.6}
$$

In Fig. 5 there is a circuit realization of function (2) as presented in [9]. For the rest of the section, the circuit will be called original approximation circuit.
![img-3.jpeg](img-3.jpeg)

Fig. 5. Schematic of the original approximation circuit [1].
Comparison of the magnitude and the phase of $Z_{i n}$ of the original approximation circuit and (2) is presented in Fig. 6 and Fig. 7 respectively. Deviation of the magnitude and the phase of $Z_{i n}$ of the original approximation circuit and (2) is presented in Fig. 8 and Fig. 9 respectively.
![img-3.jpeg](img-3.jpeg)

Fig. 6. Comparison of the magnitude characteristics of $Z_{i n}$ regarding (2) and the original approximation circuit [1].

![img-4.jpeg](img-4.jpeg)

Fig. 7. Comparison of the phase characteristics of $Z_{\mathrm{m}}$ closer (2) and the original approximation circuit [1].
![img-5.jpeg](img-5.jpeg)

Fig. 8. Deviation of the magnitude of $Z_{m}$ of the original approximation circuit [1].
![img-6.jpeg](img-6.jpeg)

Fig. 9. Deviation of the phase of $Z_{\mathrm{m}}$ of the original approximation circuit [1].

The highest deviations of the magnitude and the phase of $Z_{\mathrm{m}}$ of the original approximation circuit are presented in Tab. 1.

| Magnitude |  |  |  |
| :--: | :--: | :--: | :--: |
| $\omega[\mathrm{rad} / \mathrm{s}]$ | 0.01 | 100 | 0.33 |
| $\Delta_{\mathrm{m}}[\mathrm{dB}]$ | 0.71 | 0.46 | 0.61 |
| Phase |  |  |  |
| $\omega[\mathrm{rad} / \mathrm{s}]$ | 0.01 | 100 | 0.14 |
| $\Delta_{\mathrm{p}}[\circ]$ | 26.3 | 7.98 | 5.2 |

Tab. 1. The highest deviations of the magnitude and the phase of $Z_{\mathrm{m}}$ of the original approximation circuit.

The following sections will be focused on synthesis of the fractional capacitor circuit problem using the proposed hybrid modified UMDA method.

## 6. The Encoding Method

The used encoding method is based on the idea of fully connected admittance network. For chosen number of the nodes the fully connected admittance network is formed by connecting the admittances between all combinations of the nodes of the network. The number of the admittances of the fully connected admittance network with $n_{n}$ nodes can be calculated according to (3)

$$
n_{\text {adm }}=\binom{n_{n}}{2}=\frac{n_{n}!}{2!\left(n_{n}-2\right)!}
$$

Every single admittance of the fully connected admittance network can be replaced by resistor, capacitor, inductor or their parallel combination. Therefore the largest circuit which can be for chosen number of the nodes $n_{n}$ obtained is the circuit where every single admittance of the fully connected admittance network is replaced by parallel combination of resistor, capacitor and inductor. In this paper such circuit is denoted as expanded fully connected admittance network and includes $3 n_{\text {adm }}$ components. Example of the expanded fully connected admittance network is presented in Fig. 10.
![img-7.jpeg](img-7.jpeg)

Fig. 10. Expanded fully connected admittance network $N_{c}\left(n_{c}=\right.$ 4) [1].

The expanded fully connected admittance network can be represented using complete multigraph with three multiple edges at the most [10]. Complete multigraph $G_{c}$ corresponding to expanded fully connected admittance network

$N_{c}$ is presented in Fig. 11. Nodes $n_{0}$ to $n_{3}$ of network $N_{c}$ correspond to vertices $v_{0}$ to $v_{3}$ of complete multigraph $G_{c}$. Branches of network $N_{c}$ correspond to edges of complete multigraph $G_{c}$. For example edges $e_{5}(1), e_{5}(2), e_{5}(3)$ (on complete multigraph $G_{c}$ ) correspond to components $L_{5}, R_{5}, C_{5}$ (in network $N_{c}$ ) respectively. Then the problem of searching of the topology of the analog RLC circuits can be defined as searching of subgraph $G_{s}$ on complete multigraph $G_{c}[10]$.
![img-8.jpeg](img-8.jpeg)

Fig. 11. Complete multigraph $G_{c}$ representing expanded fully connected admittance network $N_{c}[1]$.

Subgraph $G_{s}$ can be encoded using binary characteristic vector $c$ of length $3 n_{\text {adm }}$. Every single bit of characteristic vector $c$ represents including or not including of the corresponding edge of the complete multigraph $G_{c}$ in subgraph $G_{s}$. For example complete multigraph $G_{c}$ is encoded using characteristic vector $c$ of length 18 bits where $c(i)=1$ for $i \in\{1,2, \ldots, 18\}$. Example of subgraph $G_{s}$, corresponding analog circuit and its characteristic vector $c$ are presented in Fig. 12.
![img-9.jpeg](img-9.jpeg)

Fig. 12. a) Example of subgraph $G_{s}$ b) analog circuit corresponding to $G_{s}$ c) characteristic vector $c$ of $G_{s}[1]$.

Encoding vector $e$ of every single solution is formed of two parts. The first one represents the topology and is encoded using characteristic graph $c$ approach as described above. The number of the nodes of the expanded fully connected admittance network was experimentally chosen $n_{n}=10$. To enable direct comparison of the accuracy of the circuits synthesized using the proposed method and the original approximation circuit presented in [9] the maximum number of the components of the synthesized circuit was set to the number of the components of the original approximation circuit $\left(n_{c}=10\right)$. According to (3) the topology is encoded using binary characteristic vector $c$ of length 135 bits $\left(3 n_{\text {adm }}\right)$.

The second part of encoding vector $e$ represents information about the parameters of the components and is represented by vector of real numbers $p$ of length $n_{c}$.

Schematic of the used encoding vector $e$ is presented in Fig. 13. The topological information is encoded using binary characteristic vector $c=\{\mathrm{b} 1, \mathrm{~b} 2, \mathrm{~b} 3, \ldots, \mathrm{~b} 135\}$ and the parameters (the values of the components) are encoded using vector of real numbers $p=\{\mathrm{dbl} 1, \mathrm{dbl} 2, \mathrm{db} 3, \ldots, \mathrm{dbl} 10\}$.

$$
\begin{aligned}
& e=\left[\begin{array}{llllllllll}
\mathrm{b} 1 & \mathrm{~b} 2 & \mathrm{~b} 3 & \ldots & \mathrm{~b} 135
\end{array}\right]\left[\begin{array}{llllllllllll}
\mathrm{dbl} 1 & \mathrm{dbl} 2 & \mathrm{dbl} 3 & \ldots & \mathrm{dbl} 10
\end{array}\right] \\
& \text { Fig. 13. Schematic diagram of encoding vector } e[1]
\end{aligned}
$$

Based on the components selected in the topological part of the information (characteristic vector $c$ ) corresponding values of the parameters are loaded from storage of the parameters $e_{p s}$ and copied to vector $p$. For example let's assume that the topology is encoded using characteristic vector $c(j)=1$ for $j \in\{1,3,15,18,28,52,78,92,107,115\}$. Based on the information in characteristic vector $c$ corresponding parameters of storage of the parameters $e_{p s}$ will be loaded to vector of the parameters $p$ as follows: $p(k)=e_{p s}(j)$ for $k \in$ $\left\{1,2, \ldots, N_{c}\right\}$ and $j \in\{1,3,15,18,28,52,78,92,107,115\}$.

Based on the parameters in vector $p$ the values of the components are calculated using formula (4)

$$
v=\frac{2 \times 10^{6}}{1+e^{(-1.4[10 r-14])}}
$$

where $r$ are values of the parameters loaded from vector of the parameters $p$. Formula (4) was formed to map the values of the parameters stored in vector $p$ to suitable range of the values of the components. Since the parameters in vector $p$ are set in the range $<0,1>$ corresponding values of the components for the lowest $r=0$ and for the highest $r=1$ are $v_{\min }=0.0061$ and $v_{\max }=7.3685 \times 10^{3}$ respectively. Note that formula (4) is used for all three types of components RLC. Since the used angular frequency range is from 0.01 $\mathrm{rad} / \mathrm{s}$ to $100 \mathrm{rad} / \mathrm{s}$, the values of the components are set to non-realistic values.

## 7. The Objective Function

Cost value cost is according to (7) computed as weighted summation of the magnitude and the phase differences. Difference of magnitude $\Delta_{m}$ is according to (5) calculated as weighted absolute value of differences of desired magnitude function $f_{m d}$ and magnitude of current solution $f_{m c}$ over $m=101$ frequency points in the range $0.01 \mathrm{rad} / \mathrm{s}$ to $100 \mathrm{rad} / \mathrm{s}$. Similarly difference of phase $\Delta_{p}$ is according to (6) calculated as weighted absolute value of differences of desired phase function $f_{p d}$ and phase of current solution $f_{p c}$.

$$
\begin{gathered}
\Delta_{m}=\frac{1}{m} \sum_{i=1}^{m} w_{d m}(i)\left|f_{m d}(i)-f_{m c}(i)\right| \\
\Delta_{p}=\frac{1}{m} \sum_{i=1}^{m} w_{d p}(i)\left|f_{p d}(i)-f_{p c}(i)\right| \\
\text { cost }=\Delta_{m} w_{c m}+\Delta_{p} w_{c p}
\end{gathered}
$$

Weights $w_{c m}$ and $w_{c p}$ were set to 1 and 2 respectively. Setting of weights $w_{d m}, w_{d p}$ is presented in Tab. 2. All weight coefficients were set experimentally.

| angular frequency range: | $w_{d m}$ | $w_{d p}$ |
| :-- | :--: | :--: |
| $0.01 \mathrm{rad} / \mathrm{s}$ to $0.0398 \mathrm{rad} / \mathrm{s}$ | 1.3 | 1.3 |
| $0.0437 \mathrm{rad} / \mathrm{s}$ to $20.8930 \mathrm{rad} / \mathrm{s}$ | 1 | 1 |
| $22.9087 \mathrm{rad} / \mathrm{s}$ to $100 \mathrm{rad} / \mathrm{s}$ | 1.3 | 1.3 |

Tab. 2. Setting of weights $w_{d m}$ and $w_{d p}$.
Frequency responses of the current solution $f_{m c}$ and $f_{p c}$ are obtained using nodal analysis method implemented in Matlab.

## 8. Settings of the Proposed Algorithm

The goal of the synthesis is to design a circuit which approximates function (2). The only information supplied to the system is desired magnitude and phase characteristics (2), maximum number of the used components $\left(n_{c}=10\right)$, maximal number of the nodes $\left(n_{n}=10\right)$ and types of the used components (resistors, capacitors, inductors).

The number of the objective function evaluations (evals) required by the proposed algorithm consists of the number of the evaluations required for calculation of the cost values of all individuals of the population (PopEvals) and the number of the evaluations required by the used local search algorithm (LSevals). Population size was set PopSize $=200$ and number of generations was set MaxGen $=200$. Therefore PopEvals $=40 \mathrm{e} 3$. The local search method requires MaxFunEvals $=100$ evaluations in each its run and it is executed with probability $P_{L S A}=0.02$ ( $2 \%$ Lamarckian approach [11]). The condition of execution of LSA is tested during every single objective function evaluation. Therefore LSevals $=80 \mathrm{e} 3$ and the total number of the objective function evaluations required by the proposed algorithm is 120e3 (PopEvals + LSevals). Local search algorithm was realized using Matlab function fmincon.

All parameters of the synthesized problem and settings of the proposed algorithm are summarized in Tab. 3.

| maximum number of the nodes $\left(n_{n}\right)$ | $10(0$ to 9$)$ |
| :--: | :--: |
| maximum number of the components $\left(n_{c}\right)$ | 10 |
| used types of the components | R.L.C |
| negative resistors | not allowed |
| angular frequency range | $0.01 \mathrm{rad} / \mathrm{s}$ to $100 \mathrm{rad} / \mathrm{s}$ |
| number of the points ( $m$ ) | $101(25$ points/decade) |
| population size (PopSize) | 200 |
| number of generations (MaxGen) | 200 |
| probability of execution of LSA $\left(P_{L S A}\right)$ | 0.02 |
| $w_{c m}$ | 1 |
| $w_{c p}$ | 2 |

Tab. 3. Settings of the proposed algorithm.
The algorithm UMDA is realized using Matlab toolbox MATEDA 2.0 [8]. MATEDA initialization file is presented in Fig. 14

PopSize $=200 ; n=135 ;$ cache $=[0,0,0,0,0] ;$
Card $=2 *$ rows $(1, n) ;$ MaxGen $=200 ;$ MaxVal $=-1 \mathrm{e}-2 ;$
stop considérée params $=$ (MaxGen,MaxVal);
Cliques $=$ CreateMarkovModel ( $n, 0$ );
edaparares(1) = ('seemling_pop_method','seemlingfract',25);
edaparares(2) = ('learning_method','LearnFDR',(Cliques));
edaparares(3) = ('sampling_method','SampleFDMendl','(PopSize));
edaparares(4) = ('stop_cond_method','maxgen_maxval','stop_cond_params);
[AllStat, Cache]=KusdDAfractal (PopSize, n, F, Card, cache, edaparares);
Fig. 14. Configuring of MATEDA 2.0 toolbox for realization of the proposed algorithm [1].

The whole program flow of the UMDA algorithm is realized using the functions of MATEDA 2.0 toolbox. The only exception is the sampling phase of the algorithm which is modified to enable dealing with the problems with unitation constraints. All the parameters in Tab. 2 and Tab. 3 were set experimentally after high number of experiments. The experiments were performed on a computer with processor AMD Athlon II X2 245, 6GB RAM and operational system Centos 6.5.

## 9. Experiments and The Solutions

There were executed 20 instances of the proposed algorithm. Average running time of a single execution was 11 min . The cost values of the solutions are presented in Tab. 4.

| id of run | 1 | 2 | 3 | 4 | 5 |
| :-- | --: | --: | --: | --: | --: |
| cost value | 3.805 | 2.442 | 3.805 | 2.431 | 2.428 |
| id of run | 6 | 7 | 8 | 9 | 10 |
| cost value | 2.437 | 2.443 | 3.653 | 2.433 | 2.436 |
| id of run | 11 | 12 | 13 | 14 | 15 |
| cost value | 2.432 | 3.662 | 5.197 | 5.663 | 5.353 |
| id of run | 16 | 17 | 18 | 19 | 20 |
| cost value | 6.071 | 3.805 | 5.691 | 6.072 | 2.429 |

Tab. 4. Results of 20 runs of the proposed algorithm.
As can be seen in Tab. 4 the best solution was achieved in run 5 with cost value 2.428 . The schematic diagram is presented in Fig. 15. Schematic diagrams of another three good solutions (run 4, run 11, run 20) are presented in Fig. 16 to Fig. 18.

![img-10.jpeg](img-10.jpeg)

Fig. 15. Schematic of the circuit synthesized in run 5 [1].
![img-11.jpeg](img-11.jpeg)

Fig. 16. Schematic of the circuit synthesized in run 4 [1].
![img-12.jpeg](img-12.jpeg)

Fig. 17. Schematic of the circuit synthesized in run 11 [1].
![img-13.jpeg](img-13.jpeg)

Fig. 18. Schematic of the circuit synthesized in run 20 [1].
Comparison of the magnitude and the phase characteristics of $Z_{\text {in }}$ of the best found approximation circuit and desired function (2) are presented in Fig. 19 and Fig. 20 respectively.
![img-14.jpeg](img-14.jpeg)

Fig. 19. Comparison of the magnitude of $Z_{\text {in }}$ of the best found approximation circuit and (2) [1].
![img-15.jpeg](img-15.jpeg)

Fig. 20. Comparison of the phase of $Z_{\text {in }}$ of the best found approximation circuit and (2) [1].

Absolute values of the deviations of the magnitude and the phase of $Z_{\text {in }}$ of the best synthesized circuit are presented in Fig. 21. and Fig. 22 respectively.
![img-16.jpeg](img-16.jpeg)

Fig. 21. Deviation of the magnitude of $Z_{\text {in }}$ of the best found approximation circuit [1].
![img-17.jpeg](img-17.jpeg)

Fig. 22. Deviation of the phase of $Z_{\text {in }}$ of the best found approximation circuit [1].

Three highest deviations of the magnitude and the phase characteristics of $Z_{\text {in }}$ of the best synthesized circuit are summarized in Tab. 5.

| Magnitude |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: |
| $\omega[\mathrm{rad} / \mathrm{s}]$ | 0.01 | 100 | 3.02 |  |
| $\Delta_{\mathrm{m}}[d B]$ | 0.9 | 0.78 | 0.30 |  |
| Phase |  |  |  |  |
| $\omega[\mathrm{rad} / \mathrm{s}]$ | 0.01 | 100 | 17.4 |  |
| $\Delta_{\mathrm{p}}[\mathrm{o}]$ | 2.78 | 3.97 | 1.64 |  |

Tab. 5. The highest deviations of the magnitude and the phase of $Z_{\text {in }}$ of the best synthesized approximation circuit.

As can be seen in Fig. 19 to Fig. 22 the maximum deviations of the magnitude and phase responses are located at the boundaries of the used frequency range. At these frequencies the unoptimized areas of the frequency response ( 0 to $10^{-2} \mathrm{rad} / \mathrm{s}$ and $10^{2}$ to $\infty \mathrm{rad} / \mathrm{s}$ ) affect behavior of the circuit in the area where the optimization was performed. The zeros and poles diagram of the synthesized circuit is presented in Fig. 23. All coefficients of the denominator of the approximation function of $Z_{\text {in }}$ are positive therefore stability of the synthesized circuits is guaranteed.
![img-18.jpeg](img-18.jpeg)

Fig. 23. The zeros and poles diagram of the best synthesized circuit [1].
Although the probability of using of all three component types (resistors, capacitors, inductors) was equal during the synthesis process, none of the circuits presented in Fig. 15 to Fig. 18 include any inductors. As the proposed algorithm was constrained to use only $n_{c}=10$ components, it seems that using only capacitors and resistors allows the method to reach lower cost values than in solutions where inductors are included.

## 10. Comparison of The Results

In the section the best synthesized approximation circuit obtained using the proposed algorithm will be compared to the original approximation circuit designed in [9] by a classical method of the analog circuits design.

Since the proposed evolutionary synthesis method was configured to use the same circuit complexity ( 10 components at the most) as the original approximation circuit, accuracy of both circuits can be directly compared.

Except the deviations at the boundaries of the used frequency range (as was commented above) for the original approximation circuit the highest deviation of the magnitude is $\Delta_{\mathrm{m}}=0.61 \mathrm{~dB}$ at angular frequency $0.33 \mathrm{rad} / \mathrm{s}$. For the best solution of the proposed method the highest deviation of the magnitude is $\Delta_{\mathrm{m}}=0.27 \mathrm{~dB}$ at angular frequency $0.30 \mathrm{rad} / \mathrm{s}$. Thus in terms of deviation of the magnitude the accuracy of the synthesized circuit is more than twice better than the original approximation circuit. Comparison of the deviations of the magnitude of $Z_{\text {in }}$ for both circuits is presented in Tab. 6.

| original <br> circuit | $\omega[\mathrm{rad} / \mathrm{s}]$ | 0.01 | 100 | 0.33 |
| :--: | :--: | :--: | :--: | :--: |
| $\Delta_{\mathrm{m}}[\mathrm{dB}]$ | 0.71 | 0.46 | 0.61 |  |
| synthesized <br> circuit | $\omega[\mathrm{rad} / \mathrm{s}]$ | 0.01 | 100 | 0.30 |
| $\Delta_{\mathrm{m}}[\mathrm{dB}]$ | 0.93 | 0.92 | 0.27 |  |

Tab. 6. Comparison of the deviations of the magnitude of $Z_{\text {in }}$ of the original approximation circuit and the best synthesized circuit.

The highest phase deviation inside the used frequency range is for original circuit $\Delta_{\mathrm{p}}=5.2^{\circ}$ at angular frequency $0.14 \mathrm{rad} / \mathrm{s}$ and for the synthesized circuit it is $\Delta_{\mathrm{p}}=1.5^{\circ}$ at angular frequency $0.58 \mathrm{rad} / \mathrm{s}$. Thus phase accuracy of the best synthesized circuit is more than three times better than the original approximation circuit. Comparison of the maximum deviations of the phase of $Z_{\text {in }}$ is presented in Tab. 7.

| original | $\omega[\mathrm{rad} / \mathrm{s}]$ | 0.01 | 100 | 0.14 |
| :--: | :--: | :--: | :--: | :--: |
| circuit | $\Delta_{\mathrm{p}}[\mathrm{o}]$ | 26.3 | 7.98 | 5.2 |
| synthesized | $\omega[\mathrm{rad} / \mathrm{s}]$ | 0.01 | 100 | 0.58 |
| circuit | $\Delta_{\mathrm{p}}[\mathrm{o}]$ | 3.0 | 4.2 | 1.5 |

Tab. 7. Comparison of the deviations of the phase of $Z_{\text {in }}$ of the original approximation circuit and the best synthesized circuit.

In [12] the same problem of synthesis of the fractional capacitor circuit was solved using simulated annealing method. The method was able to reach solutions of the same accuracy however the number of required evaluations of the objective function was almost four times higher. Comparison of accuracy of the best solutions and numbers of evaluations of the objective function of the proposed EDA method and simulated annealing method [12] is presented in Tab. 8.

| simulated annealing <br> method [12] | best cost | evals |
| :--: | :--: | :--: |
| the proposed | best cost | evals |
| EDA method | 2.43 | $120 \mathrm{e} 3$ |

Tab. 8. Comparison of the proposed EDA method and simulated annealing method presented in [12].

## 11. Conclusion

Automated analog circuit synthesis approach based on hybrid evolutionary method employing modified UMDA algorithm and a local search algorithm was presented in the paper. Used hybrid approach enables to employ specialized methods for both sub problems of different nature (synthesis of the topology and determination of the parameters).

Synthesis of the topology which is combinational optimization problem was solved using modified UMDA algorithm. Determination of the parameters which is continuous optimization problem was solved using a local search algorithm. The principle of the method is based on mutual interaction of synthesis of the topology phase (modified UMDA algorithm) and determination of the parameters phase (the local search algorithm) of the desired solution. Modification of the UMDA algorithm which allows solving problems with unitation constrains was proposed in the paper.

The proposed method was verified on the problem of synthesis of the fractional capacitor circuit introduced in [9]. Presented experiments have shown that the proposed algorithm is capable to synthesize solutions with accuracy overperforming solutions obtained using a classical method of the analog circuit design given in [9]. Accuracy of the magnitude of $Z_{\mathrm{in}}$ of the best obtained solution was more than twice better than the original approximation circuit. Accuracy of the phase of $Z_{\text {in }}$ of the best obtained solution was more than three times better than the original approximation circuit.

In [12] the problem of fractional capacitor circuit realization was solved using simulated annealing method (SA). The accuracy of the circuits synthesized using SA was the same as the solutions produced using the proposed EDA method.

However SA required much higher number of the objective function evaluations. While the proposed EDA method required 120 e 3 objective function evaluations for synthesis of the same problem SA required 440 e 3 objective function evaluations.

For demonstration purposes the presented algorithm was verified using nodal analysis circuit simulator implemented in Matlab. Another improvement of the efficiency of the algorithm can achieved using Model Order Reduction Techniques [13].

## Acknowledgements

The presented research was financed by the Czech Ministry of Education in frame of the National Sustainability Program, the grant LO1401 INWITE. For the research, infrastructure of the SIX Center was used.

## References

[1] SLEZÁK, J. Evolutionary Synthesis of Analog Electronic Circuits Using EDA Algorithms. Ph.D. Thesis, Brno: Brno University of Technology, The Faculty of Electrical Engineering and Communication, 2014. 123 pages.
[2] ZINCHENKO, L., MÜHLENBEIN, H., KUREICHIK, V., MAHNING, T. Application of the univariate marginal distribution algorithm to analog circuit design. In Proceedings of NASA/DoD Conference on Evolvable Hardware, 2002, p. 93-101. DOI: 10.1109/EH.2002.1029871
[3] TORRES, A., PONCE, E. E., TORRES, M. D., DIAZ, E., PADILLA, F. Comparison of two evolvable systems in the automated analog circuit synthesis. In Proceedings of Eighth Mexican International Conference on Artificial Intelligence (MICAI 2009) Mexico, 2009, p. 3-8, ISBN 978-0-7695-3933-1. DOI: 10.1109/MiCAI.2009.25
[4] TANG, M., LAU, R. Y. K. A hybrid estimation of distribution algorithm for the minimal switching graph problem. In Proceedings of International Conference on Computational Intelligence for Modelling, Control and Automation and International Conference on Intelligent Agents, Web Technologies and Internet Commerce, Austria 2005, p. 708-713. DOI: 10.1109/CIMCA.2005.1631347
[5] MÜHLENBEIN, H., PAAB, G. From recombination of genes to the estimation of distributions I. Binary parameters. Lecture Notes in Computer Science 1411: Parallel Problem Solving from Nature PPSN IV, p. 178-187. DOI: 10.1007/3-540-61723-X_982
[6] SANTANA, R., OCHOA, A., SOTO, M. R. Factorized distribution algorithms for functions with unitation constraints. In Proceedings of the Third Symposium on Adaptive Systems (ISAS-2001), 2001, p. $158-165$.
[7] MÜHLENBEIN, H., MAHNIG, T., OCHOA, A. Schemata, distributions and graphical models in evolutionary optimization. Journal of Heuristics, 1999, p. 215-247.
[8] SANTANA, R., ECHEGOYEN, C., MENDIBURU, A., BIELZA, C., LOZANO, J. A., LARRAÑAGA, P., ARMAÑANZAS, R., SHAKYA, S. MATEDA: A suite of EDA programs in Matlab. Technical Report EHU-KZAA-IK-2/09, University of the Basque Country, 2009.
[9] CARLSON, G. E., HALIJAK, C. A. Approximation of fractional capacitors $(1 / s)^{(1 / s)}$ by a regular Newton process. IEEE Transactions on Circuit Theory, 1964, vol. 11, no. 2, p. 210-213, ISSN 0018-9324. DOI: 10.1109/TCT.1964.1082270
[10] BALAKRISHNAN, V. K. Graph Theory, McGraw-Hill, 1997, ISBN $0-07-005489-4$.
[11] EL-MIHOUB, T. A., HOPGOOD, A. A., NOLLE, L., BATTERSBY, A. Hybrid genetic algorithms: A review. Engineering Letters, 2006, vol. 13, no. 2, p. 124-137, ISSN: 1816-093X.
[12] SLEZAK, J., GOTTHANS, T., DRINOVSKY, J. Evolutionary Synthesis of Fractional Capacitor Using Simulated Annealing Method. Radioengineering, 2012, vol. 21, no. 4, p. 1252-1259, ISSN 12102512.
[13] FELDMANN, P. Model order reduction techniques for linear systems with large numbers of terminals. In Proceedings of Design, Automation and Test in Europe Conference and Exhibition, 2004, vol. 2.1, p. 944-947. DOI: 10.1109/DATE.2004.1269013

## About the Authors...

Josef SLEZAK was born in Zlin, Czech Republic, in 1982. He received the MSc. degree at the Brno University of Technology in 2007. In 2014 he received Ph.D. degree from the Brno University of Technology. His research interests include evolutionary synthesis of analog electronic circuits, design automation and optimization.

Tomas GOTTHANS was born in Brno, Czech Republic,
in 1985. He received the MSc. degree at the Brno University of Technology (BUT) in 2010. In 2014 he received Ph.D. degree from the Université Paris-Est (UPE) and from the Brno University of Technology. He was working in the École Supérieure d'Ingénieurs en Électronique et Électrotechnique de Paris (ESIEE) in the ESYCOM Laboratory. He is presently a researcher in the Sensor, Information and Communication Systems (SIX) research laboratory, BUT. His research interests include programming, wireless communications and non-linear phenomenons.