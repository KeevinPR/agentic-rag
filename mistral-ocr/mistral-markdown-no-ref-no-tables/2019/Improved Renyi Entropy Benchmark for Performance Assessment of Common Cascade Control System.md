# Improved Renyi Entropy Benchmark for Performance Assessment of Common Cascade Control System 

QIAN ZHANG*, YA-GANG WANG, FEIFEI LEE, QIU CHEN, AND ZHEN SUN<br>National School of Optical-Electrical and Computer Engineering, University of Shanghai for Science and Technology, Shanghai 200093, China<br>Corresponding author: Ya-Gang Wang (ygwang@usst.edu.cn)

This work was supported by the National Natural Science Foundation under Grant 11502145, Grant 61074087, and Grant 61703277.


#### Abstract

To deal with the inconsistency of the minimum variance (MV) benchmark in evaluating non-Gaussian disturbance systems, this paper proposed a new benchmark, which combined entropy with output mean value. For a cascade control system, the new benchmark was constructed by analyzing the weakness of the MV benchmark and the pure Renyi entropy benchmark. In order to estimate the more accurate performance of the unknown system, an improved estimation of distribution algorithm based on entropy criterion is given. It can identify the disturbance distribution and calculate the new index evaluation value. Finally, different disturbance distributions were used to verify the consistency of the new index. The experimental results show that the proposed index and algorithms are consistent and effective in evaluating the performance of the unknown systems with non-Gaussian disturbance.


#### Abstract

INDEX TERMS Cascade control system, Renyi entropy, performance assessment, non-Gaussian disturbance, EDA.


## I. INTRODUCTION

System performance assessment is an effective tool to building high quality control loops. It can give health assessment, diagnostics, even the corresponding improvement methods [1]. In 1989, Harris proposed a system performance evaluation index based on minimum variance. The minimum variance control(MVC) laid the foundation for the research and development of loop assessment. Later some scholars applied the MVC method to feed-forward control loop [2], unstable and non-minimum phase system [3], time-varying system [4], and multiple-input multiple-output system [5]. However, the minimum variance control law has some serious shortcomings, such as the high-gain, wide-bandwidth, and large control signal deviation. Thus Grimble proposed a generalized minimum variance control(GMVC) benchmark to evaluate system performance [6]. The GMVC achieves the benchmark by adding the error and control weighted coefficient to the control loop, but the weight selection is difficult if the system belongs to cascade control loop. The literature [7] used a linear quadratic Gaussian(LQG) method to replace the MVC algorithm. Because the LQG needs to calculate both the input and output minimum variance, LQG benchmark can illustrate the gap between the current performance and the
ideal performance. However, the CPA based on LQG is too complex to realize in realistic industrial processes than the traditional MVC benchmark.

Although the current loop evaluation indicators are relatively mature in related fields, most loop evaluation methods assume that the system noise is subject to Gaussian distribution. In actual industrial processes, the actual noise distribution does not satisfy this prerequisite due to the cross-impact of different Gaussian interference or other factors. In order to solve this problem, Guo and Wang [8] proposed a linear matrix inequality based on convex optimization algorithm. It can be applied to non-Gaussian system error detection and control law design. However, it is unnecessary to calculate the output probability distribution function frequently. Instead, a minimum entropy strategy which can reflect the tracking error for all moments is proposed [9], [10]. The literature [11] gives a method to estimate the theoretical performance value of the system by using the minimum entropy. The consistency of this method is better than the minimum variance index, but it cannot achieve the estimated value of model parameter and the distribution of unknown noise. The literature [12], [13] proposed a method to evaluate the performance of discrete systems by using Renyi entropy. However, there are some

defects in the calculation of entropy theoretical values [14], he ignored the coefficient transformation of continuous variables. Since then, the literature [15] proposed a system performance evaluation index based on rational entropy for continuous systems. However, this indicator is insensitive to the mean shift.

In reality, control processes such as chemical process and stream turbine process are often accompanied by nonGaussian disturbances. Sometimes the output will have a mean shift because of non-system internal structure. Thus the goal of this paper is to construct a new benchmark which can reflect the mean shift of non-Gaussian system. It based on the minimum entropy and system mean value. It can be used for non-Gaussian cascade control system which has unknown models. In order to achieve this goal, in section 1, this paper analyzes the shortcomings of the minimum variance index in the cascade system, and then derives the minimum entropy of cascade control system according to the feedback invariant theory in section 2. This index uses the output mean to obtain the improved minimum entropy benchmark. In section 3, an improved distributed estimation algorithm is then presented to estimate the disturbance distribution and to calculate a system performance index based on the new benchmark. Finally, in section 4, a series of experiments are carried out to illustrate the consistency of the new benchmark. In section 5, the conclusion is given.
![img-0.jpeg](img-0.jpeg)

FIGURE 1. Cascade control system.

## II. THE ANALYSIS OF MVC FOR CASCADE SYSTEM

Comparing with the single loop system, cascade control system can significantly reduce the maximum deviation and integral error. Thus cascade control strategy has been widely used in industrial process. Considering a discrete cascade control system with time delay which is shown in Fig-1, where the primary and secondary loop can be expressed as,

$$
\begin{aligned}
& C_{1}(k)=G_{1} C_{2}(k)+G_{L 11} a_{1}(k)+G_{L 12} a_{2}(k) \\
& C_{2}(k)=G_{2} u_{2}(k)+G_{L 21} a_{1}(k)+G_{L 22} a_{2}(k)
\end{aligned}
$$

In the above Equation, $C_{1}(k)$ and $C_{2}(k)$ are the process output of the primary and secondary loops at sampling instant $k$, respectively. $G_{c_{1}}$ and $G_{c_{2}}$ are the controller of system loops; $u_{1}(k), u_{2}(k)$ are the output of outer and inner controllers; $G_{1}, G_{2}$ are the transfer model of the primary and secondary loops, respectively. If the $q^{-1}$ is defined as the backward shift operator, then $G_{1}, G_{2}$ can be written as $G_{1}=G_{1}^{*} q^{-d_{1}}$, $G_{2}=G_{2}^{*} q^{-d_{2}}$ where $d_{1}, d_{2}$ are the time delay of two loops. The unknown disturbance of inner and outer loops can be defined as $a_{1}(k)$ and $a_{2}(k)$. They can be added to the primary and secondary loops by the filter model $G_{L 11}, G_{L 12}, G_{L 21}$ and $G_{L 22}$.

Through the Diophantine equation, the above parameter can be done the following replacement,

$$
\begin{aligned}
G_{L 11} & =Q_{11}+R_{11} q^{-d_{1}-d_{2}} \quad G_{L 12}=Q_{12}+R_{12} q^{-d_{1}-d_{2}} \\
G_{L 21} & =Q_{21}+R_{21} q^{-d_{2}} \quad G_{L 22}=Q_{22}+R_{22} q^{-d_{2}} \\
G_{1}^{*} G_{L 21} & =S_{1}+T_{1} q^{-d_{2}} \quad G_{1}^{*} G_{L 22}=S_{2}+T_{2} q^{-d_{2}}
\end{aligned}
$$

where the $Q_{11}$ and $Q_{12}$ are the polynomials with order of $d_{1}+d_{2}-1 ; Q_{21}, Q_{22}, S_{1}, S_{2}$ are the polynomials with order of $d_{2}-1 ; R_{i j}, T_{i j}(i, j=1,2)$ are the conversion equations which meet the requirements of their respective equations. Thus the Eq.(1) can be simplified by using the Eq.(1) to Eq.(3),

$$
\begin{aligned}
C_{1}(k)=\left(Q_{11}+S_{1} q^{-d_{1}}\right) a_{1}(k)+\left(Q_{12}+S_{2} q^{-d_{1}}\right) a_{2}(k) \\
+\underbrace{q^{-d 1-d 2}\left(M_{1} a_{1}(k)+M_{2} a_{2}(k)\right)}_{D_{2}}
\end{aligned}
$$

where the $M_{1}$ and $M_{2}$, shown at the bottom of this page, are the appropriate conversion equations; $D_{1}$ is the feedback invariant variable and $D_{2}$ is feedback dependent variable. According to the theory of feedback invariant control, the variance of outer output can be expressed as,

$$
\begin{aligned}
\sigma_{C_{1}}^{2} & \geq \operatorname{var}\left[\left(\underline{Q_{11}+S_{1} q^{-d_{1}}}\right) a_{1}(k)+\left(\underline{Q_{12}+S_{2} q^{-d_{1}}}\right) a_{2}(k)\right] \\
& =\operatorname{trace}\left[\left(\sum_{i=0}^{d_{1}+d_{2}+1} N_{i}^{T} N_{i}\right) \cdot \sum a\right]
\end{aligned}
$$

where the $N_{i}(i=0,1, \ldots, d_{1}+d_{2}-1)$ is the two-dimensional vector consisting of the polynomial $D_{3}$ and $D_{4}$; the $\sum a$ is the co-variance matrix of two noises. Thus there is no restriction on whether the two noises have correlation. If $M_{1}=0$, $M_{2}=0$, the equal sign in the formula (7) is established. The optimal control law can be obtained under the MVC method.

$$
\begin{aligned}
& M_{1}=q^{-d_{1}-d_{2}}\left[\frac{\left(1+G_{2} G_{c_{2}}\right) R_{11}+C_{1}^{*} R_{21}+T_{1}-Q_{11} G_{1}^{*} G_{2}^{*} G_{c_{1}} G_{c_{2}}-S_{1} G_{2}^{*} G_{c_{2}}\left(1+G_{1} G_{c_{1}}\right)}{1+G_{2} G_{c_{2}}+G_{1} G_{2} G_{c_{1}} G_{c_{2}}}\right] \\
& M_{2}=q^{-d_{1}-d_{2}}\left[\frac{\left(1+G_{2} G_{c_{2}}\right) R_{12}+C_{1}^{*} R_{22}+T_{2}-Q_{12} G_{1}^{*} G_{2}^{*} G_{c_{1}} G_{c_{2}}-S_{2} G_{2}^{*} G_{c_{2}}\left(1+G_{1} G_{c_{1}}\right)}{1+G_{2} G_{c_{2}}+G_{1} G_{2} G_{c_{1}} G_{c_{2}}}\right]
\end{aligned}
$$

It can be written as,

$$
\eta_{m v}=\frac{\sigma_{m v}^{2}}{\sigma_{C_{1}}^{2}}
$$

where the $\sigma_{c_{1}}^{2}$ is the actual variance of primary loop output; $\sigma_{\mathrm{MV}}^{2}$ is the theoretical minimum variance.

Although the MVC benchmark can accurately evaluate the performance of the Gaussian system, there is an inconsistency in evaluating the performance of non-Gaussian system. For example, considering the following system,

$$
\left\{\begin{array}{l}
C_{1}(k)=\frac{1}{1-0.9 q^{-1}} C_{2}(k-2)+\frac{1}{1-0.8 q^{-1}} a_{1}(k) \\
C_{2}(k)=\frac{1}{1-0.5 q^{-1}} u_{2}(k-1)+\frac{1}{1-0.3 q^{-1}} a_{2}(k) \\
G_{C_{1}}=\frac{0.48-0.46 q^{-1}}{1-q^{-1}} G_{C_{2}}=0.7
\end{array}\right.
$$

Assume that the disturbances are subject to Gaussian distribution where $a_{1}, a_{2} \sim N(0,1)$ and the noises are independent, we can achieve 1000 groups data from the main loop output. Then the actual variance can be obtained as $\sigma_{c_{1}}^{2}=3.7432$ and the minimum variance is $\sigma_{\mathrm{mv}}^{2}=3.0496$. According to the Eq.(8), the MVC index is $\eta_{\mathrm{mv}}=0.8147$. From the index we can find that the performance of system is well. But considering the non-Gaussian disturbances where $a_{1}, a_{2}$ are subject to $\beta$ and Gaussian bi-modal distributions respectively, their probability density functions can be given as,

$$
\begin{aligned}
a_{\beta}(\alpha, \beta) & \sim \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)} x^{\alpha-1}(1-x)^{\beta-1} \\
a_{B}\left(r, \mu_{1}, \sigma_{1}, \mu_{2}, \sigma_{2}\right) & \\
& \sim \frac{r}{\sqrt{2 \pi \sigma_{1}}} e^{\left(-\frac{\left(r-\mu_{1}\right)^{2}}{2 \sigma_{1}^{2}}\right)}+\frac{1-r}{\sqrt{2 \pi \sigma_{2}}} e^{\left(-\frac{\left(r-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}}\right)}
\end{aligned}
$$

We can make $F(a)=a-\operatorname{mean}(a)$ to adjust the mean of disturbance $a$ to zero. Then the disturbances satisfy $a_{1}=$ $r_{1} F\left(a_{\beta}\right), a_{2}=r_{2} F\left(a_{B}\right)$ where $r_{1}, r_{2}$ are the constant. Thus the normal probability plots can be shown as, Notes that if the curves in the Normal probability plots deviate from straight lines, the curves can be thought satisfy the non-Gaussian properties. Then the system output can be shown in Fig.3, It is obviously that main areas of two experiments are roughly with [ -1.41 .4$]$. Although the fluctuation of second group is smaller than first group, the index of two groups are $\eta_{m v, 1}=$ 0.7156 and $\eta_{m v, 2}=0.6203$. It means the results of MVC index are inconsistent with the actual system performance. Thus the MVC is no suitable for performance assessment of non-Gaussian system.

## III. IMPROVED RENYI ENTROPY

Since entropy is a functional of probability density function, including the statistical characteristics of whole output sequence, entropy is an better optimal benchmark for performance assessment of non-Gaussian system than minimum variance.
![img-2.jpeg](img-2.jpeg)

FIGURE 2. Normal probability plots for two experiments.
![img-2.jpeg](img-2.jpeg)

FIGURE 3. Primary output of two experiments.

## A. THE CALCULATION OF RENYI ENTROPY

Due to the calculation of entropy is based on the probability distribution instead of the distance, the outlier has no

significant impact on the result. In this paper, the second order Renyi entropy is used to construct the system performance benchmark. For refined discrete random variable $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$, the entropy can be expressed as,

$$
H_{2}(X)=-\ln \sum_{i=0}^{n} p_{i}^{2}
$$

where the $p_{i}$ is the probability of each parameter $x_{i}(i=$ $1,2, \ldots, n)$ and $\sum_{i=0}^{n} p_{i}=1$. When calculate the entropy of discrete variables, the output value will be divided into several non-overlapping regions. Then we can calculate the respective probabilities of each interval regions by counting the number of each interval to obtain the Renyi entropy. Considering the cascade control system which is shown in Fig.1, the Renyi entropy of the primary loop is expressed as,

$$
\begin{aligned}
H_{2}\left(C_{1}\right)=H\left(\left(Q_{11}\right.\right. & \left.\left.+S_{1} q^{-d_{1}}\right) a_{1}(k)+\left(Q_{12}+S_{2} q^{-d_{1}}\right) a_{2}(k)\right. \\
& \left.+q^{-d 1-d 2}\left(M_{1} a_{1}(k)+M_{2} a_{2}(k)\right)\right)
\end{aligned}
$$

Similar to MVC method, the optimal control law can be obtained when the feedback dependent variable is zero. Thus,

$$
\begin{aligned}
H_{m e}\left(C_{1}\right)=H\left(\left(Q_{11}+S_{1} q^{-d_{1}}\right) a_{1}(k)\right. & \\
& \left.+\left(Q_{12}+S_{2} q^{-d_{1}}\right) a_{2}(k)\right)
\end{aligned}
$$

In literature [10], [11], he used the criterion of information theory to expand and decompose the polynomials of feedback invariants. He ignored the expanded coefficients of $a_{1}(k), a_{2}(k)$ when calculated the minimum entropy. While it has been proved that the entropy and coefficients are closely related in literature [14], [15], so the pure benchmark of Renyi entropy is,

$$
\eta_{m e}=\frac{H_{m v}\left(C_{1}\right)}{H_{2}\left(C_{1}\right)}
$$

But according to the research, entropy is the index to describe the shape of the distribution, the pure entropy cannot reflect the shift of the output mean value. Thus in this paper the Renyi entropy benchmark is combined with the mean benchmark to evaluate the performance of non-Gaussian system. The mean benchmark is,

$$
\eta_{M}= \begin{cases}\left\{1-\frac{\left|\operatorname{mean}\left(C_{1}-R\right)\right|}{W} \quad \left|\operatorname{mean}\left(C_{1}-R\right)\right|<W\right. \\ 0 & \left|\operatorname{mean}\left(C_{1}-R\right)\right| \geq W\end{cases}
$$

where the $W$ is the maximum allowed mean offset and $R$ is the relaxation variable which is used to control the deviation amplitude when the W is given. Commonly, the $R$ is set to zero. If the mean offset exceeds this value, the system performance is considered to be worst. $\eta_{M} \in[0,1]$, the closer to 1 the system offset is, the better the control performance is. Thus the improved benchmark for Renyi entropy is,

$$
\eta_{\text {final }}=\eta_{m e} \times \eta_{M}
$$

TABLE 1. Configure of different disturbances.

TABLE 2. The result of four experiments.


## B. THE ESTIMATED OF MODEL UNKNOWN SYSTEM

When the system model and disturbance are all known, the minimum variance benchmark and minimum entropy benchmark can be calculated easily. But for the model unknown system, we need to identified their model and time delay firstly. The traditional minimum mean square based on the least square algorithm(LS) is not ideal. Considering the property of entropy, in this paper, we use the minimum entropy criterion rather than the minimum mean square to calculate the benchmark. The Eq.(1) can be expressed as the sliding auto-regressive model,

$$
\begin{aligned}
& \left(1+\alpha_{1}^{(1)} q^{-1}+\alpha_{2}^{(1)} q^{-2}+\ldots+\alpha_{n_{1}}^{(1)} q^{-n_{1}}\right) C_{1}(k) \\
& \quad=\left(\beta_{1}^{(1)} q^{-1}+\beta_{2}^{(1)} q^{-2}+\ldots+\beta_{n_{1}}^{(1)} q^{-n_{2}}\right) C_{2}(k) \\
& \quad+\left(1+\gamma_{1}^{(1)} q^{-1}+\gamma_{2}^{(1)} q^{-2}+\ldots+\gamma_{n_{1}}^{(1)} q^{-n_{3}}\right) a_{1}(k)
\end{aligned}
$$

where $\alpha_{j}^{(1)} \beta_{j}^{(1)} \gamma_{j}^{(1)}$ are the parameter which needs to be identified; $n_{j}(j=1,2,3)$ is the order of the system polynomials, it can be obtained by AIC criterion. Then we can define,

$$
\begin{aligned}
\theta= & {\left[\alpha_{1}^{(1)} \quad \ldots \quad \alpha_{n_{1}}^{(1)} \beta_{1}^{(1)} \quad \ldots \quad \beta_{n_{2}}^{(1)} \gamma_{1}^{(1)} \quad \ldots \quad \gamma_{n_{3}}^{(1)}\right]^{T} } \\
h^{T}= & {\left[-C_{1}(k-1) \ldots-C_{1}\left(k-n_{1}\right) \quad C_{2}(k-1) \ldots\right.} \\
& \left.\quad C_{2}\left(k-n_{2}\right) a_{1}(k-1) \quad \ldots \quad a_{1}\left(k-n_{3}\right)\right]^{T}
\end{aligned}
$$

![img-3.jpeg](img-3.jpeg)

FIGURE 4. The estimation of primary loop disturbances for 4 sets of experiments.
where the vector $h^{T}$ can be obtained from the observed data and $a_{1}$ can be estimated. According to the Eq.(18), the residual can be shown as,

$$
e(k)=C_{1}(k)-h^{T}(k) \theta
$$

The goal of this method is to achieve,

$$
\begin{aligned}
\theta^{\text {opt }} & =\arg \min H_{2}(\boldsymbol{e}) \theta \in \Omega_{\theta} \\
H_{2}(\boldsymbol{e}) & =-\ln \sum_{i=1}^{L} \hat{p}_{i}^{2}
\end{aligned}
$$

where the residual sequence is $\boldsymbol{e}=\left\{e_{1}, e_{2}, \ldots, e_{L}\right\}, L$ is the length of data. The $\Omega_{\theta}$ is the parameter space.

## C. IMPROVED EDA ALGORITHM

Due to the $H_{2}(e)$ is not microscopic, it is impossible to search the optimal parameters by using the gradient method. Thus the estimated distribution algorithm(EDA) is adopted. EDA is evolutionary algorithm based on the statistical theory.

The probability model is used to obtain the distribution of the system solutions. It first presents a probabilistic model for describing candidate solution distribution information in search space by using the statistical learning method [1], [16]. Then it will use the new model to generate the new solution. The poor fitness value will be replaced by those new solutions. After several iterates, the algorithm will be end if the criterion is met. The optimal solution will be obtained. But the search speed of traditional EDA algorithm is too slower, this paper uses the Recursive Expanded Least Square (RELS) to achieve the roughly estimation of model parameter $\theta_{R E L S}$ and the standard deviation of disturbance $\sigma_{\text {RELS }}$. The condition for iterate termination is

$$
\boldsymbol{m e a n}\left(\left(C_{1}-h^{T} \theta\right)^{2}\right)<\varepsilon \quad(\varepsilon>0)
$$

Thus the improved EDA algorithm can be described as following,
(1) Firstly, the $l$ means the count of iterations. The rough parameter model can be obtained by using

![img-4.jpeg](img-4.jpeg)

FIGURE 5. The primary output of four experiments.
the RELS method, we choose R solutions $A^{(l)}=$ $\left\{\theta_{1}^{(l)}, \theta_{2}^{(l)}, \ldots, \theta_{R}^{(l)}\right\}, l=0$, where the $A^{(l)}$ is parameter space.
(2) Calculate whether these R solutions satisfy the termination condition (24), then remove those solutions which does not satisfy the condition and regenerate the new solution until the number of them is not less than R.
(3) Calculate the residual sequence $e_{i}^{(l)}=\left\{e_{i, 1}^{(l)}, e_{i, 2}^{(l)}, \ldots\right.$, $\left.e_{i, L}^{(l)}\right\},(i=1,2, \ldots, R)$ and the entropy $H_{2}\left(e_{i}^{(l)}\right)$. Select the N solutions $(N \leq R)$ with smallest residual entropy as the optimal solutions of current iteration, expressed as $B^{(l)}=\left\{\phi_{1}^{(l)}, \phi_{2}^{(l)}, \ldots, \phi_{N}^{(l)}\right\}$.
(4) The new probability model can be established from the $B^{(l)}$. Then regenerate R-N solutions and combine them into $B^{(l)}$ to achieve the $l t h(l=l+1)$ parameter space $A^{(l)}$.
(5) Go to the step (2).

From the improved EDA algorithm, we can obtain the optimal parameter model and the PDF of the disturbance.
![img-5.jpeg](img-5.jpeg)

Then the improved Renyi benchmark can be calculated by suing the Eq.(12) to Eq.(15).

## IV. SIMULATION

In order to illustrated the effectiveness of the proposed method, the system in section 1 is used based on the MATLAB platform. In all following experiments, the parameters in improved EDA were set to $N=80, R=200$. The Gaussian model is used as the probability model for the new solutions. It is expressed as,

$$
\left\{\begin{array}{l}
f\left(\theta_{i, j}^{(l+1)}\right)=\frac{1}{\sqrt{2 \pi} \sigma_{j}} e^{-\left(\left(\theta_{i, j}^{(l+1)}-\mu_{j}\right)^{2}\right) / 2 \sigma_{j}^{2}} \quad i=1,2, \ldots, N \\
\mu_{j}=\frac{1}{R} \sum_{i=1}^{R} \theta_{i, j}^{(l)} \quad \sigma_{j}=\frac{1}{R} \sum_{i=1}^{R}\left(\theta_{i, j}^{(l)}-\mu_{j}\right)
\end{array}\right.
$$

where the $\theta_{i, j}^{(l)}$ is the $j$ th parameter of the parameter vector $\theta_{i}^{(l)}$. The terminated condition is set as $\left|H_{2}^{(l)}-H_{2}^{(l-1)}\right| \leq 0.001$.

To fully explain the accuracy of the simulation, we choose four sets of experiments,
To verify the accuracy of the improved EDA algorithm, the disturbances $a_{1}$ of the above table-1 are compared with the actual value and estimated value based on the least square(LS) algorithm. The results are shown in Fig.4.
It can be seen from the four figures that the EDA algorithm performs better than LS algorithm for both Gaussian disturbances and non-Gaussian disturbances. The main reason is that the least square algorithm cannot reflect the statistical characteristics of the whole system, so the result of LS algorithm has large deviation.
To simulate the mean shift of the system output, a zero offset of amplitude 1 is added to the system output of the third experiment. The output plot is shown in Fig.5,
To illustrate the performance of system output, the intervals are chosen as triple the standard deviation which is shown as the horizontal lines in the Fig-5. The output intervals of 4 experiments are $0.8831,0.8092,0.6503,0.7353$. The following table-2 shows the theoretical values and estimated values of MVC benchmark, minimum entropy benchmark (the method which is proposed in literature [15]) and the improved Renyi entropy benchmark which is proposed in this paper.
From the table we can find that the theoretical value of both minimum entropy and improved Renyi entropy is very close to estimated value. It illustrates the effectiveness of improved EDA algorithm. Moreover, compared with other two benchmark, the improved Renyi entropy is more accurate to reflect the mean shift. It reflect the fluctuation of the system output. However, the MVC benchmark and pure minimum entropy benchmark are slow to the fluctuation of output. Thus we can say that the improved entropy benchmark has better robust, accuracy and consistency for non-Gaussian system. The improved EDA algorithm perform well in estimating the parameter space and disturbances.

## V. CONCLUSION

In this paper, the routinely MVC method is reviewed and its defects are illustrated by using the experiment in section 1. The shortcomings of traditional Renyi entropy is illustrated in Section 2. Considering the characteristic of entropy, the improved benchmark based on the mean offset and improved Renyi entropy is proposed. From the simulations in section 4, the improved Renyi entropy can reflect the current performance of a non-Gaussian system with mean shift well. A serious of experiments with mixture disturbances validated the accuracy, robust and consistency of the improved Renyi entropy benchmark. It lays the theoretical foundation for practical engineering. But there still some problems, such as the efficiency of the EDA algorithm is poor. The next step is to improved the efficiency of the proposed method.
