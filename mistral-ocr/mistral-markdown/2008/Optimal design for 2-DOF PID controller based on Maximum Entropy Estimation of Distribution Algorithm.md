# Optimal Design for 2-DOF PID Controller Based on Maximum Entropy Estimation of Distribution Algorithm 

Lu Lin<br>School of Management, Guilin University of Electronic Technology, Guilin, 541004, China<br>E-mail: lulin355@163.com


#### Abstract

Estimation of Distribution Algorithms (EDAs) is new kinds of colony evolution algorithms. It produces its new generation by constructing probability distribution model through counting excellent information of individuals of present colony EDAs first, and then sampling the model. To solve the NP-Hard question as EDAs searching optimum network structure, a new Maximum Entropy Estimation of Distribution Algorithm (MEEDA) is proposed; and the paper puts forward the MEEDA to optimize two degree of freedom PID controller parameters. The simulation results show that the optimal 2-DOF PID controller has simultaneously both the characteristics of command tracking and disturbance rejection, so we can see the simulation verifies the effectiveness of the EDA algorithm.


## 1. Introduction

In the industrial control system design process, interference suppression characteristics and target tracking features are two main concern problems. The traditional PID (single degree of freedom PID) controller has only a group of adjustable PID parameters, if tuning PID parameters according to the interference suppression, the target tracking features will be disappointing; if tuning PID parameters according to the target tracking features, the interference suppression will be disappointing. People often use a compromise approach in the practical design process to tune PID parameters, which is also difficult to get the best control. In order to resolve this contradiction, people raised the 2-degree-of-freedom PID controller design ideas which achieved good results in practical applications. Though the2-degree-of-freedom PID controller is not two independent freedom PID controllers, yet it can set up two independent PID parameters to maximize the
interference suppression characteristics and target tracking features at the same time.

At present, the optimal design study of 2-DOF PID focused on the following three aspects: (1) incomplete self-stereotyping 2-DOF PID, whose feature is to reduce the optimization parameters of the question to optimize the parameters, and cut two groups 6 parameters to two groups 5 or 4 parameters; for example, the P-PID, PI-PID, etc; (2) semiselfstereotyping 2-DOF PID, whose feature is to use the simulation methods or prior experience to get a group of fixed parameters, while the other set of which is established by the setting scene; (3) self-stereotyping 2DOF PID, characterized by the optimized design of all parameters, is the most advanced 2-DOF PID; for example, the parameters of self-tuning PID based on neural networks ${ }^{[1]}$, the parameters of self-tuning PID based on genetic algorithm ${ }^{[2]}$, and so on. However, the PID parameters entire set is a complex optimization process, which usually adopts the following two methods: (1) the indirect method of setting in accordance with the Ziegler-Nichols rules; (2) the direct tuning method which map from the transient response characteristics vector directly to the Correction Magnitude of controller setting parameters. The direct tuning method is directly based on the response curve approximation to set the control parameters, without the need for other intermediate steps. Based on this idea, we can convert the controller parameters tuning process to the optimization process.

Estimation of Distribution Algorithms (EDAs) is new kinds of colony evolution algorithms. It produces its new generation by constructing probability distribution model through counting excellent information of individuals of present colony EDAs first, and then sampling the model. The method is relatively simple, its convergence can reach a certain degree of assurance in theory ${ }^{[3]}$, and it has achieved good results in the continuous function optimization and the application of combinatorial optimization. Larranaga

has proved EDA is superior to other evolutionary algorithms in the set of parameters, the global search capability and many other aspects. This paper applies EDA into the2-DOF PID controller optimized design, and proposes appropriate parameters and evolutionary strategies to improve efficiency. It also has a simulation test according to the typical lag control system. The result shows that the method is valid.

## 2. Maximum entropy estimation of distribution algorithm

### 2.1 the principle of MEEDA

EDA is generated from genetic algorithm (GA). Although GA can be applied to many combinatorial optimization problems, yet they all need some prior knowledge to determine the evolution operator, therefore, it is difficult to find an appropriate set of parameters in coding and combined with the operation for a particular problem, which is the inherent defect of GA. Furthermore, in evolutionary terms, the crossover and mutation operator are used to the realization of and the exchange of individual information in group, and select operator is used to the guidance of the evolutionary process, both of them did not consider the relevant information of the same generation individuals, so they did not fully make use of the existing information and reduced the operating efficiency of GA; furthermore, crossover and mutation operator can not guarantee the establishment of building blocks assumptions in theory, as a result, GA demonstrates very poor performance for some of the issues (such as misleading).

To improve these deficiencies, H. Muhlenbein and G. Paa $\beta^{[4]}$ proposed the estimation of distribution algorithm in 1996, which quickly aroused the concern of extensive researches. And it has been a hotspot of evolutionary computation at present. EDA does not use crossover and mutation operator, but uses probability distribution of higher degree individuals in the group as the evolutionary model, and then produces the next generation of subgroups; with the use of tracking advanced method to replace the recombination of the GA modes, and it has expanded the applied space of EDA.

As evolution model is derived from the statistical probability distribution of information, thus it shows the main characteristics of groups in making the best use of existing information and reflecting more accurately the relationship between variables. Theoretical study shows that in the iterative process, EDA may get interaction information of individuals between group and different bit of individuals, identify
and manipulate the model of important blocks, therefore it can effectively solve the optimization problems in which the decision-making variables are interactive ${ }^{[3]}$.

EDA makes use of the distribution of random vector to characterize its internal probability of dependence, therefore how to find a n-dimensional probability model which can fully reflect the interaction between random variables is the key of EDA. Probability distribution model directly determines the performance of EDA. Precise probability distribution model ensures a good outcome, and vice versa.

Currently, the more common practice is the application of probability map model (discrete EDA uses bayes network to express the relationship between variables, continuous EDA uses gauss network ${ }^{[5]}$ ). However, how to determine the network parameters which in turn determine the optimal network structure is proved to be a NP-Hard problem, and the complicated calculation has greatly reduced the computing performance of EDA and limited the application of EDA. This paper proposes a new method of maximum entropy estimation of distribution algorithm which takes Jaynes principle as the basis, makes use of the maximum entropy of random variables to estimate the minimum bias probability distribution of random variables, and then regards it as the evolution model of the algorithm. As a result, it has reduced the complexity degrees of calculation effectively.

### 2.2 MEEDA principle

Maximum entropy method estimates the probability distribution of random variables on the basis of the entropy of random variables, the theory of which is based on the principle of Jaynes, that is "the most realistic probability of distribution gives the maximum entropy of bound information" ${ }^{[6]}$. To the continuous random variables, entropy can be definition from the following equation:

$$
H(x)=-\int_{R} P(x) \log (x) d x
$$

In the equation, $P(x)$ is the function of probability density of random variable $X, R$ is the definition domain of $P(x)$. Maximum entropy distribution gets the maximum entropy $H(x)$ by adjusting $P(x)$ on the conditions of statistical sample. According to the varying points, the author uses Lagrange indefinite multipliers to act as functional objectives:

$$
L=\int_{0}^{1}(-P(x) \ln P(x)+\left(\lambda_{0}+1\right) P(x)+
$$

$$
\sum_{i=1}^{m} \lambda_{i} x^{i} P(x)] d x
$$

The density function is:

$$
P(x)=\exp \left(\lambda_{0}+\sum_{i=1}^{m} \lambda_{i} x^{i}\right)
$$

$P(x)$ can be fully identified by further defining parameters $\lambda$. Through the derivation of the mathematics, $\lambda_{0}$ is calculated as follows:

$$
\begin{gathered}
\lambda_{0}=-\ln \left[\int_{0}^{\lambda} \exp \left(\sum_{i=1}^{m} \lambda_{i} x^{i}\right) d x\right] \\
\lambda_{1}(i=1,2, \cdots, m) \text { can be obtained from value(5): } \\
\delta_{i}=1-\frac{\int_{0}^{\lambda} x^{i} \exp \left(\sum_{i=1}^{m} \lambda_{i} x^{i}\right) d x}{\mu_{i} \int_{0}^{\lambda} \exp \left(\sum_{i=1}^{m} \lambda_{i} x^{i}\right) d x}
\end{gathered}
$$

The approximate solution of $\lambda_{i}$ can be got by calculating the minimum $\min \delta^{2}$ of square of residuals $\delta_{i}$ of value(5).

### 2.3 the calculation steps of MEEDA

Step1: randomly generate $N$ initial solutions; calculate initial fitness of these initial solutions.

Step2: choose $S_{c}$ individuals which have higher adaptation degree $\left(S_{c} \leq N\right)$.

Step3: take these $S_{c}$ individuals values into the equation (4), (5), calculate values of parameters $\lambda_{0}$ and $\lambda_{1}$.

Step4: calculate the probability density function $P(x)$ of these $S_{c}$ individuals under equation (3) .

Step5: calculate the maximum entropy distribution function of these $S_{c}$ individuals under equation (1), establish optimal $n$ victories probability model that reflects the interaction of random variables.

Step6: produce $N$ new entity by $n$ victories probability model.

Step7: calculate the adapt degree of these new individuals, and replace the parent populations with new ones.

Step8: if the termination of the conditions is met, you can put out the result; otherwise you can turn to Step2.

### 2.4 the performance analysis of MEEDA

The main calculation of MEEDA focuses on the set of network structure. At present, the computing amount of the common use of greedy to search network structure is $o\left(n^{2}\right)$; through covariance matrix to get gauss network parameters is $o\left(n^{2}\right)$ computing amount. They are index, only suitable for small networks. From the above MEEDA, the computing amount of steps3 is $o(n \log n)$, steps 4 is $o(n)$, steps 5 is $o(n)$. Therefore, the time complexity of MEEDA is polynomial which is $o(n \log n+n+n)$, compared to the computing complexity of $o\left(n^{2}\right)$ of greedy and $o\left(n^{2}\right)$ of covariance matrix method, it has greatly reduced the computation amount.

## 3. The optimized design of 2-DOF PID controller based on MEEDA

### 3.1 2-DOF PID controller

In 1963, the American ISSAC.M.Horowitz introduced the concept of 2-DOF into PID control system first, and proposed 8 kinds of 2-DOF PID control structure, among them four kinds were considered to have industrial applications value, that is given value filtering type (type filter), given the value of feedforward (FF type), feedback-based compensation (FB type), and loop compensation(loop type). Jiang shan, Yoshikawa ${ }^{[7]}$ demonstrated the equivalent of the four kinds of control structure and gave the transformation relations. Based on this equivalence relation, the paper chooses feed forward (FF-type) 2-DOF PID controller as its research object, the diagram of the structure is shown in Figure $1^{[8]}$.
![img-0.jpeg](img-0.jpeg)

Figure1. Feed forward type expression of the 2-DOF PID control

In figure $1, P(s)$ is the planted object, $C_{s}(s)$ is the feed-forward compensation, $C(s)$ is the main controller, $R(s)$ is the input signal of control system, $\gamma(s)$ is the output signal of control system, $D(s)$ is the jamming signal of the control system.

The transfer function of main controller $C(s)$ is

$$
F_{1}(s)=K_{p}\left(1+\frac{1}{T_{c} s}+T_{p} s\right)
$$

The transfer function of feedforward compensation $C_{s}(s)$ is

$$
F_{s}(s)=-K_{s}(\alpha+\beta T_{c} s)
$$

The transfer function from input signal $R(s)$ to output $\gamma(s)$ is

$$
P_{R Y}(s)=\frac{\left(F_{1}(s)+F_{2}(s)\right) P(s)}{1+F_{1}(s) P(s)}
$$

The transfer function from jamming signal $D(s)$ to output $\gamma(s)$ is

$$
P_{D Y}(s)=\frac{P(s)}{1+F_{2}(s) P(s)}
$$

Thus, if we adjust $P_{D Y}(s)$ to the ideal value, that is to make the characteristics of interference suppression get its maximum, we only set the parameters $K_{p}, T_{1}, T_{2}$ of $F_{1}(s)$; if $F_{2}(s)$ is remained the same, we only need to adjust the parameters $\alpha, \beta$ of $F_{2}(s)$ to make $P_{D}(s)$ get its maximum, which in turn can guarantees the given target tracking features achieve its maximum, and this is the advantage of 2-DOF.

### 3.2 the optimization design steps of 2-DOF controller based on MEEDA

(1) Identification of the necessary parameters of MEEDA. The set of parameters and operator strategy of MEEDA are as follows: $N=1000, S_{c}=500$, the highest adaptation individual in $S_{c}$ can directly get into the next offspring, to compute the remaining 499 individuals to construct the probability distribution model.
(2) Determine parameters to be optimized and its range. From figure 1, there are five parameters of this type of feed-forward 2-DOF controller need to be set, they are $K_{p}, T_{1}, T_{2}, \alpha, \beta \quad$ Let
$1<K_{c}<100,0.001<T_{i}<10,0.001<T_{c}<10$,
$0<\alpha<2,0<\beta<2$.
(3) Determine the objective function. We use the same objective function as in literature [9]:

$$
J[\lambda, p, H(s)]=\int_{0}^{1}\left|\lambda(\omega)\left\{\frac{d^{n} H(s)}{d s^{n}}\right\}_{s=\rho o}^{1}\right|^{2} d \omega
$$

Here $H(s)$ is the response of Step input error in Laplacian domain, such as $G_{p d}(s) / s$ or $G_{p c}(s) / s$. When $\lambda(\omega)=1$, through Parseval's formula we can get the following:

$$
J[1, p, H(s)]=\pi \int_{0}^{1}\left\{t_{p} e_{\text {step }}(t)\right\}^{2} d t
$$

This objective function of square based on time integral weighted error has been used in many literature of PID set. The notable feature of equation (10) is the introduction of the frequency weight $\lambda(\omega)$. Using bigger $\lambda(\omega)$ in high-frequency domain can inhibit the feedback in high-frequency, and it can inhibit the system from oscillation in most cases of PID control applications. Take a lot of different $\lambda(\omega), p$ and values to do test, the literature [10] take:

$$
\lambda(\omega)=\omega^{1 / 4}, p=2
$$

It can make common PID control system be optimal in the traditional sense, that is, the overshoot can be less than 20 percent, stability time can be the same or less than the optimal system of CHR set.

This paper takes equation (10) under the conditions of equation (12) as function to turn 2-DOF controller system.

## 4. Simulation

Take a typical first order pure delay controlled plant in the industrial course as an example, let the transfer function of controlled object is

$$
H(s)=\frac{1}{5 s+1} e^{-2 s}
$$

The setting parameters results of 2-DOF controller after the adoption of MEEDA are:

$$
\begin{aligned}
& K_{p}=8.6539, T_{i}=0.0438, T_{p}=0.1263 \\
& \alpha=0.0679, \beta=1.325
\end{aligned}
$$

While the traditional design method of 2-DOF controller, first used the conventional method of setting PID parameters to adjust $K_{p}, T_{1}, T$, so as to get best interference suppression, and then selected two degree of freedom of the coefficient $\alpha, \beta$ (general admission $\alpha=0.4, \beta=0.15$ ) based on the experience to meet the requirment of tracking the value of the

target tracking features, the results of the setting parameters are: $K_{s}=6.2547, T_{t}=0.0575, T_{e}=0.0341$,

$$
\alpha=0.4, \beta=0.15
$$

Combine the two degree of freedom PID controller coming from the two methods with the model system into a closed-loop system, through MATLAB simulation, the output response are shown in figure 2 and figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 2. System simulation curve of unit step response
![img-2.jpeg](img-2.jpeg)

Figure 3. System simulation curve of step interference response

It can be seen from figure 2 that there are some limitations in the method of selecting the2-DOF PID controller parameters on the basis of experience. Though we can get satisfied interference performance by tuning PID parameters on the basis of the interference suppression and then selected $\alpha, \beta$ by the value of experience, yet the track characteristics are not optimal. However, the 2-DOF controller that based on the MEEDA has not only excellent anti-jamming performance and good track characteristics at the same time, but also has greatly improved the robust of the whole system, and made the algorithm easy to be achieved.

## 5. Conclusion

This paper presents a 2-DOF PID controller parameters optimization method based on the maximum entropy estimation of distribution algorithm, which has solved the difficult problems of traditional 2DOF PID regulator parameter setting. The simulation tests show that the designed 2-DOF PID controller distribution based on MEEDA, has not only the satisfied tracking performance and the ability of well inhibiting the outside interference, but also greatly improved the robust stability of the whole system, which proves that the designed method that proposed in this paper is feasible and effective.

## References

[1] Kung YS, Liaw CM, Ouyang M S, "Adaptive Speed control for induction motor drives using neural net works ". IEEE Trans Ind Electron,1995, 42 (1):pp.25-32.
[2] Wang Qiang, Ma Liang, "Design for 2-DOF PID controller based on hybrid genetic algorithm and its application". Control and decision-making, 2001,16 (2):pp.195-198.
[3] Zhang Q, Miihliebei H, "On the convergence of a class of estimation of distribution algorithms". IEEE Trans on Evolutionary Computation, 2004,8 (2):pp. $127-136$.
[4] Muhlenbein, H., Paa; G., From Recombination of Genes to the Estimation of Distribution Algorithms I. Binary Parameters, HMVoigt, et al. (Eds.): Lecture Notes in Computer Science1411: Parallel Problem Solving from Nature - PPSN IV (1996) :pp.178-187.
[5] Larrañaga, P., Etxeberria, R., Lozano, JA, Peña, JM, "Optimization by learning and simulation of Bayesian and Gaussian networks". Technical Report EHU-KZAA-IK-4/99, University of the Basque Country, December 1999.
[6] Siddall, JN, Probabilistic engineering design. Principles and Applications. New York: Marcel Dekker, 1983.
[7] Jiang Shan, Yoshikawa (Japan), "PID control freedom of the composition , features and applications". Liao Chun-kan translation. Automation technology applications, 1987 (4) :pp.61-66.
[8] Gorezr R, "New design relations for 2-DOF PIDlike control systems". Automatica, 2003,39 (5) :pp.901-908.
[9] Araki M, Hidefumi T, "Two-degree-of-freedom PID controllers ". International Journal of Control, Automation, and Systems, 2003,1 (4) :pp.401-410.
[10] Taguchi H, Doi M, Araki M, "Optimal parameters of two-degree-of-freedom PID control systems". Trans SICE, 1987,23 (5) :pp.889-895.