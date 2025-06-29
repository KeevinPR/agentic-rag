# Non-Gaussian System Identification Based on Improved Estimation of Distribution Algorithm 

Jinglin Zhou, Yiqing Jia, Han Zhang, Jing Wang, Haijiang Zhu<br>College of Information Science \&Technology, Beijing University of Chemical Technology, Beijing, 100029, China<br>E-mail: jinglinzhou@mail.buct.edu.cn; jwang@mail.buct.edu.cn; zhuhj@mail.buct.edu.cn


#### Abstract

In this paper, an improved estimation of distribution algorithm (EDA) is proposed and applied to the identification of ARMA model parameters. The system parameter identification problem is transformed into the optimization problem in high dimensional parameter space. Based on the traditional EDA algorithm, the parameters of preliminary estimation and data selection are added to improve the speed of searching and optimization precision. Because the mean and the variance are not enough to describe the uncertainty of non-Gaussian system, the entropy is regarded as fitness value to achieve the parameter identification of non-Gaussian system. Finally, an example of improved EDA identification is given to illustrate the effectiveness of the proposed approach.


Key Words: Non-Gaussian System, EDA, Parameter Estimation

## 1 Introduction

Considering the unpredictability of the control system model under non-Gaussian disturbance in advance, the estimation of the system model from the data of daily operation becomes difficult and challenging to some extent. Solving the problem of the accuracy of model identification requires an appropriate criterion, which is an indicator of system model identification. The model identification based on the mean square error (MSE) criterion and the corresponding least squares method has been widely applied to the model parameter identification of Gaussian system. However, in practice the realization of disturbance may not confirm to the Gaussian distribution, the information gathered by the low order statistics is not sufficient for the non-Gaussian system parameter identification. Unlike Gaussian variables, all distributions of random variables are included in the first and second moments. So the MSE method is inadequate to cope with the non-Gaussian system identification. To solve the stochastic systems with non-Gaussian disturbance, the stochastic distribution control theory was proposed [1]. Then, a more general measure of uncertainty, namely the entropy, should be used to characterize the uncertainty of the tracking error. It is known that all the stochastic information is included in the complete probability density function (PDF). Therefore, by minimizing the entropy instead of the mean square error, all higher order moments (not only the second one) can be minimized. Entropy has been widely used in information, thermodynamics and control theory [2], [3], [4]. In [5], entropy was used as a measure for the average information contained in the PDF of the estimation errors using the filters.

In recent years, with the development of science and deepening of the advanced control theory research,

[^0]optimization methods and intelligent control theory are in-depth application to the control field. Some intelligent optimization algorithms, such as genetic algorithms [6],[7], neural networks [8],[9], particle swarm optimization [10],[11], differential evolution algorithms [12] and distribution estimation algorithms [13] have been used in system parameter identification, which are characterized by concise programming and facile application. These methods can be used to deal with the nonlinear and non-Gaussian system parameter identification, which is superior to the traditional optimization algorithm for parameter identification of linear system and Gaussian system. Thus, the non-Gaussian system identification based on the intelligent optimization algorithms is valuable. In this paper, the estimation of distribution algorithm is improved to enhance its global optimization ability and to accelerate the convergence speed. Then, it is applied to ARMA model parameter optimization estimation. Based on the initial parameter space, the optimal ARMA model parameters and unknown noise distribution are obtained by global search. The paper is organized as follows: In Section 2, review the traditional EDA algorithm and point out the defects. In Section 3, the improvement measures are put forward. In Section 4, a simulation case is conducted.

## 2 Estimation of Distribution Algorithm

The concept of Estimation of Distribution Algorithm (EDA) was first proposed by the scholars in 1996 [14]. In the following few years, the algorithm developed rapidly, which became the hotspot in the field of evolutionary computation. There is a significant difference between the EDA algorithm and the genetic algorithm (GA). EDA predicts the optimal region by searching spatial sampling and statistical learning, and then produces excellent new individuals, which differs from GA uses crossover and mutation to generate new individuals. Compared with GA's evolutionary approach based on micro-level of gene, EDA adopts the evolutionary method of macro-level based on search space and has stronger global searching ability and faster convergence speed. The probability distribution model is used to describe


[^0]:    * This work was supported in part by NSFC (Grant No. 61473025, and 61573050), the open-project grant funded by State Key Laboratory of Management and Control for Complex System at Institute of Automation, CAS (20160107).

the distribution of candidate solutions in the search space. The statistical model is used to construct a probability model to describe the solution distribution from the macroscopic point of view and then, the probability model is randomly sampled to generate new population of evolution. Under this situation, the population is initialized with distribution estimation algorithm. In each iteration the fitness value of each individual is obtained and sorted according to the evaluation function. Then a part of individuals with better fitness value are selected to make up the advantage group. And the probability distribution model which the subject obeyed is estimated according to the dominant group, such as the Gaussian distribution model. Furthermore, a random sampling of the estimated probability distribution model is used to generate some new individuals to replace some of the individuals with poor fitness values in the initial population to form a new generation population. When satisfying the iteration termination condition, the iteration of this algorithm will be terminated and finally the optimal outcomes obtained by employing EDA are the best fitness value of the current population.

The specific process shown as follows.
Step 1: Initialize the population.
Step 2: Select the dominant group.
Step 3: Construct the probability model.
Step 4: Random sampling.
Step 5: Generate new populations.
Step 6: Judge the termination condition. If yes, end; otherwise, turn to Step 2.

However, it is worth noting that process of parameter identification is still affected by many factors in practical applications of the estimation of distribution algorithm.

1) The setting of the initialization parameter space triggers a great impact on the recognition effect. In the case of unknown parameters, the initial value will affect the convergence rate if it is too large, especially for high-dimensional space cannot guarantee uniform sampling. Therefore, before initializing the parameter space, a preliminary estimation of the model parameters is required to ensure that the parameter space covers the real parameters as much as possible.
2) Owning to the non-uniformity of the high-dimensional space sampling, randomly generated seeds are likely to deviate from the real parameters even diverge the system. In order to obtain more appropriate seeds, the abnormal value needs to be filtered out before the fitness value is calculated to accelerate the convergence rate.
3) The error entropy is regarded as the fitness value. When the entropy is calculated, the entropy of two generations cannot be subtracted or the minimum entropy value is not unique because of the mean shift. In order to avoid this situation, a unified standard is needed to make the entropy calculation more normalized.

From the above discussions it is clear that the estimation of distribution algorithm should be improved.

## 3 Improvement Measures

### 3.1 Preliminary Estimation

Since the initialization parameter space has a pivotal role on the parameter identification, it is necessary to make a
preliminary estimation of the model parameters before initializing the population to ensure that the parameter space covers the real parameters as much as possible.

For non-Gaussian systems, there is no better parameter initialization method at present and so we adopt the method of parameter initialization for Gaussian system. The parameter estimation method of ARMA model is used to initialize the range of parameters to be estimated. In order to illustrate the process at length, we will elaborate the parameter estimation method of ARMA model for the Gaussian systems summarized as below.

Consider an ARMA time series described as follows.

$$
A\left(z^{-1}\right) y(k)=D\left(z^{-1}\right) v(k)
$$

where $y(k)$ is the output of the system, the disturbance $v(k)$ is an uncorrelated random noise sequence with zero mean and variance $\sigma_{v}^{2}$.

And

$$
\left\{\begin{array}{l}
A\left(z^{-1}\right)=1+a_{1} z^{-1}+a_{2} z^{-2}+\cdots+a_{n_{a}} z^{-n_{d}} \\
D\left(z^{-1}\right)=1+d_{1} z^{-1}+d_{2} z^{-2}+\cdots+d_{n_{d}} z^{-n_{d}}
\end{array}\right.
$$

defined

$$
\theta=\left[a_{1}, a_{2}, \cdots a_{n_{a}}, d_{1}, d_{2}, \cdots d_{n_{d}}\right]^{T}
$$

In this paper, a recursive maximum likelihood (RML) [15] estimation method is used to estimate the parameters. Thus the maximum likelihood problem of the model parameter is to find the parameter $\theta$ to make the objective function reach the minimum.

$$
\left.J(\theta)\right|_{\theta_{M E}}=\left.\frac{1}{2} \sum_{t=1}^{L} v^{2}(k)\right|_{\theta_{M E}}=\min
$$

In which $\hat{\theta}_{M E}$ is the estimate of $\theta$, and $v(k)$ satisfying

$$
v(k)=\left[D\left(z^{-1}\right)\right]^{-1}\left[A\left(z^{-1}\right) y(k)\right]
$$

If $v(k)$ is Taylor-expanded at the $\hat{\theta}_{M E}$ point, it can be approximated as

$$
v(k) \approx v\left(\left.k\right|_{\theta_{M E}}\right)+\left.\frac{\partial v(k)}{\partial \theta}\right|_{\theta_{M E}}\left(\theta-\hat{\theta}_{M E}\right)
$$

Then the filter value of $y(k)$ and $\hat{v}(k)$ is $y_{f}(k)$ and $\hat{v}_{f}(k)$, respectively.

$$
\begin{gathered}
\left\{\begin{array}{l}
y_{f}(k)=\left[\hat{D}\left(z^{-1}\right)\right]^{-1} y(k) \\
\hat{v}_{f}(k)=\left[\hat{D}\left(z^{-1}\right)\right]^{-1} \hat{v}(k)
\end{array}\right. \\
h_{f}(k)=\left[-y_{f}(k-1), \cdots-y_{f}\left(k-n_{a}\right)\right. \\
\left.\hat{v}_{f}(k-1), \cdots \hat{v}_{f}\left(k-n_{a}\right)\right]^{T}
\end{gathered}
$$

The recursive maximum likelihood estimation algorithm can be described as formula (9).

Based on the estimation of the parameters of the Gaussian system, we can get the estimate of variance $\hat{\sigma}_{r}$ and the estimated value of the parameter $\hat{\theta}$, and then we use the $\hat{\theta} \pm 3 \hat{\sigma}_{r}$ as the initialized range of the parameter space.

$$
\begin{aligned}
& \left\{\begin{array}{l}
\dot{\theta}=\dot{\theta}(k-1)+K(k) \hat{v}(k) \\
K(k)=P(k-1) h_{f}(k)\left[h_{f}^{T}(k) P(k-1) h_{f}(k)\right. \\
\left.+I\right]^{-1} \\
P(k)=\left[I-K(k) h_{f}^{T}(k)\right] P(k-1) \\
\dot{v}(k)=y(k)-h^{T}(k) \dot{\theta}(k-1) \\
h(k)=\left[-y(k-1), \cdots,-y\left(k-n_{a}\right)\right. \\
\left.\hat{v}(k-1), \cdots, \hat{v}\left(k-n_{a}\right)\right]^{T} \\
h_{f}(k)=\left[-y_{f}(k-1), \cdots,-y_{f}\left(k-n_{a}\right)\right. \\
\left.\hat{v}_{f}(k-1), \cdots \hat{v}_{f}\left(k-n_{a}\right)\right]^{T} \\
y_{f}(k)=\left[\hat{D}\left(z^{-1}\right)\right]^{-1} y(k) \\
\hat{v}_{f}(k)=\left[\hat{D}\left(z^{-1}\right)\right]^{-1} \hat{v}(k)
\end{array}\right.
\end{aligned}
$$

### 3.2 Data Selection

Since the range of parameter estimation and parameter space dimension are relatively large, the data generated by using the uniform distribution of each subspace directly may result in large estimation bias. In the identification of the distribution estimation algorithm, we adopt the unknown parameters as seeds. In order to obtain appropriate seeds, adding the screening conditions is an effective measure to eliminate the seeds with large deviations.

Because the mean of the noise is assumed to be zero, the mean of the residuals can be regarded as the screening condition. It can be described as follows.

$$
\begin{gathered}
e_{k}=y_{k}-h^{T} \theta \\
\operatorname{mean}\left(e_{k}\right)<\varepsilon(\varepsilon \rightarrow 0)
\end{gathered}
$$

If the mean value is less than $\varepsilon$, it will be retained as good seed and becomes a member of the new parameter space.

### 3.3 Selection of Fitness Value

If $X$ is a random variable with length $M$ discrete values, and corresponding distribution probability $P=\left(p_{1}, p_{2}, \ldots, p_{M}\right)$, then the Renyi's entropy denoted by $H_{n}(X)$ is

$$
H_{n}(X)=\frac{1}{1-\alpha} \ln \sum_{i=1}^{M} p_{i}^{\alpha}
$$

In this paper, we take the error entropy as the fitness value, when the error entropy reaches the minimum while the parameter reaches the optimum.

It can be expressed as

$$
\Phi^{\text {opt }}=\arg \min _{\Phi \in \Psi} H(e)
$$

where $\Psi$ denotes the parameters space.
When computing the probability, we assume that $X$ is sampled at a fixed time and $N$ valid data are collected. All of these points fall within the interval $S=\left[W_{1}, W_{M}\right], W_{1}$ and $W_{M}$ are the left and right boundaries respectively. We divide the interval uniformly into $M$ consecutive and non-overlapping subintervals $\left(s_{1} \cup s_{2} \cup s_{3} \ldots \cup s_{M}\right)$. The central value of each interval is denoted as $w_{i}(i=1,2, \ldots, M)$. And $s_{(i<i<M)}=\left[w_{i}-\delta_{i} w_{i}+\delta\right],\left(w_{i}-\delta=w_{i-1}+\delta_{i} w_{i}+\delta=w_{i+1}-\delta\right)$. Then statistics the number of sampled data falling into each
subinterval, $N=\left(I_{1}, I_{2}, \ldots, I_{M}\right)$ and these frequencies are approximated as the probability of $w_{i}(i=1,2, \ldots M)$, the corresponding probability distribution is as follows,

$$
\begin{gathered}
P_{i}=\left(\frac{I_{i}}{N}, \frac{I_{2}}{N}, \ldots, \frac{I_{M}}{N}\right)=\left(p_{1}, p_{2}, \ldots, p_{M}\right) \\
(i=1,2, \ldots, M)
\end{gathered}
$$

In the EDA identification process, we take the error entropy as the fitness value. Since the selection of seeds during the iteration is random, the range of residuals for each generation may be different. If the interval is divided into $M$ sub-intervals to calculate the value of the entropy, the central value of the deviation will cause that the calculation of entropy is not uniform and the entropy between adjacent generations cannot be subtracted or cannot even converge under such circumstances. In order to solve this problem, we set a uniform interval range and partition the subinterval with the same interval so that the center value is fixed, which ensures the consistency of the entropy calculation.

### 3.4 Algorithm Summary

Combined with EDA algorithm and the proposed improvement measures, the improved EDA algorithm is summarized as follows.
(1) Preliminary estimation. Rough estimation parameters are obtained by recursive maximum likelihood method. Then the task of initializing the parameters space can be accomplished with a uniform distribution using the initial value of parameter as the value range.
(2) Screen seeds. From the first generation randomly select $R$ group seed from the parameter space and calculate the mean value of the residuals. Remove the seeds whose mean value is more than $\varepsilon$, and keep the seeds whose mean value is less than $\varepsilon$. If the number of reserved seeds is less than $R$, resampling is performed until the number of seeds retained is not less than $R$, and then the seeds reserved are collected in new parameter spaces $\Psi^{(i)}(Q) \quad(Q \geqslant R)$.
(3) Calculate fitness. Randomly create $R$ individuals from the
parameter space $\Psi^{(i)}(Q), A_{i}=\left\{\Phi^{(i)}(1), \Phi^{(i)}(2), \ldots, \Phi^{(i)}(R)\right\}$. For each parameter vector in $A_{i}$, estimate the corresponding error entropy based on the training data set $\left\{y_{i}\right\}$.
(4) Select

$$
N \quad \text { superior }
$$

individuals $B_{i}=\left\{\Phi^{(1)}, \Phi^{(2)}, \ldots, \Phi^{(N)}\right\}$ based on the cost function and estimate probability density function based on the statistical information extracted from the selected $N$ individuals.
(5) Calculate the estimated average value of the selected $N$ parameters and establish the probability models.
(6) Set $l \leftarrow l+1$, and resample $R$ individuals from the updated PDF.

(7) Go to step2 until the stopping criterion is met.

This process can be represented by Figure 1.
![img-0.jpeg](img-0.jpeg)

Fig 1. The process of the improved distribution estimation algorithm

## 4 Simulation

In this section two experiments are given using the improved EDA method and the results are compared with the EDA introduced in the section 2. In order to illustrate the effectiveness of the improved method, consider the following system

$$
y(k)=\frac{1+1.5 z^{-1}+0.9 z^{-2}}{1-1.7 z^{-1}+0.7 z^{-2}} v(k)
$$

The simulation is carried out under different noise disturbance. In all testing cases, the parameters of the two methods are $\mathrm{N}=80, \mathrm{R}=200$. And a Gaussian model with diagonal covariance matrix is utilized as the probabilistic model. Let $H^{(i)}=H\left(\bar{e}^{(i)}\right)$ denote the error entropy obtained at $l$ based on the estimated average parameters. The stopping criteria of two methods can be set to $\left|H^{(i)}-H^{(i-1)}\right|<0.001$. The selection criteria of the improved EDA algorithm is $\bar{e}_{k}<0.1$.
(1) $v(k) \sim N\left(0,0.255^{2}\right)$, after using the RML algorithm, the preliminary estimate of model parameters are $\hat{\theta}=[-1.7510,0.7520,0.9201,0.0572]^{T}$.
![img-1.jpeg](img-1.jpeg)

Fig 2. The normal probability plots of the actual and estimated disturbances of the system with Gaussian disturbance.
![img-2.jpeg](img-2.jpeg)

Fig 3. PDF of the actual and estimated disturbance using improved EDA algorithm and EDA algorithm.
![img-3.jpeg](img-3.jpeg)

Fig 4. The iterative curve of $H^{(i)}$ using improved EDA and EDA algorithm.

![img-4.jpeg](img-4.jpeg)

Fig 5. System output curve and its fitting curve under Gaussian disturbance

Table 1: The results of system parameters identification under Gaussian disturbance are obtained according to two methods.

|  | $a_{1}$ | $a_{2}$ | $b_{1}$ | $b_{2}$ | $\sigma_{v}^{2}$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| true value | -1.7 | 0.7 | 1.5 | 0.9 | 0.2474 |
| EDA | -0.4651 | -0.5384 | 1.4831 | 0.9104 | 0.6676 |
| improved <br> EDA | -1.7739 | 0.7736 | 1.3185 | 0.6914 | 0.2732 |

In the first case, the system with the Gaussian disturbance is identified by the two methods. As shown in Fig.4, after 105 seconds and 15 generations, the error entropy for the population is converged by using the improved EDA algorithm. The estimated variance of the noise sequence is 0.2732 , which is close to the real variance 0.2474 . To make comparisons, the original EDA identification is also applied here. After 90 seconds and 47 generations, the error entropy for the population is converged, and the estimated variance of the noise sequence is 0.6676 . The normal probability plot is a graphical technique to identify substantive departures from normality. If the set of real numbers follows a normal distribution, the normal probability plot will be a straight line. The Fig. 2 shows that the both results are Gaussian distributions, but the result of improved EDA algorithm is closer to the true distribution than the original method. For better clarity, regard the disturbance and error sequence as a continuous random variable with their respective nonnegative probability density function. And the kernel density function is used to fit the PDF in Fig.3. Although the original EDA algorithm also estimates the Gaussian distribution, it is clear that there is a big gap from the true distribution. Fortunately, as shown in the Fig. 3 the result of improved EDA identification is almost completely coincident with the actual distribution. Organize the above simulation results into Table 1. It can be summarized that the improved EDA method can improve the accuracy of parameter identification and avoid the premature convergence of EDA after the rough estimation parameters are obtained.
(2) $v(k)-f(x ; \alpha, \beta)=\frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha+\beta)} x^{n-1}(1-x)^{\beta-1}$
where $\alpha=2, \beta=9$, after using the RML algorithm, the preliminary estimate of model parameters are $\hat{\theta}=[-1.7502,0.7498,0.7729,-0.0484]^{T}$.
![img-5.jpeg](img-5.jpeg)

Fig 6. The normal probability plots of the actual and estimated disturbances of the system with $\beta$ disturbance.
![img-6.jpeg](img-6.jpeg)

Fig 7. The iterative curve of $H^{(i)}$ using improved EDA and EDA algorithm.
![img-7.jpeg](img-7.jpeg)

Fig 8. PDF of the actual and estimated $\beta$ disturbance using improved EDA algorithm and EDA algorithm.

![img-8.jpeg](img-8.jpeg)

Fig 9. System output curve and its fitting curve under the $\beta$ disturbance.

Table 2: The results of system parameters identification under $\beta$ disturbance are obtained according to two methods.

|  | $a_{1}$ | $a_{2}$ | $b_{1}$ | $b_{2}$ | $\sigma_{\mathrm{c}}^{2}$ |
| :--: | :--: | :--: | :--: | :--: | :--: |
| true value | -1.7 | 0.7 | 1.5 | 0.9 | 0.0128 |
| EDA | -0.3044 | -0.6892 | 1.6657 | 0.9463 | 0.0578 |
| improved <br> EDA | -1.7154 | 0.7189 | 1.2706 | 0.6243 | 0.0139 |

In the second case, by using the improved EDA method, the system with the non-Gaussian disturbance is identified after the 24 iterations with 59 seconds. Compared with EDA method ended in 53 generations with 100 seconds, the number of iterations is reduced and the convergence speed is accelerated shown in Fig.7. The normal probability plot is also used here to check the identification effect. It is noticed that the disturbance in the tails of the plots bends away from the straight line shown in Fig.6, which illustrates the effectiveness of the algorithm for non-Gaussian distribution identification. But it is clear that the result of the improved EDA method is less deviate from the actual value than the previous method. The Fig. 8 shows the PDF of actual and estimated disturbance. Green line depicts that although the EDA algorithm terminates, the effect is not optimal. And through the improved EDA algorithm, the estimation effect shown in Fig. 8 has been significantly improved. As shown in Table 2, the real variance of the disturbance is 0.0128 , and the estimated values by the two methods are 0.0139 and 0.0578 , respectively. From the above description, it can be seen that the improved EDA method enhances the effectiveness of parameter identification for non-Gaussian systems.

The Fig. 5 and Fig. 9 show that the parameters obtained by this method are optimal and have good fitting effect.

## 5 Conclusions

This paper briefly introduces an improved method based on the traditional identification method with the estimation of distribution algorithm. The simulation results show that the proposed algorithm can accelerate the convergence speed and enhance the recognition effect through parameter
preliminary estimation and data filtering. For the system with non-Gaussian noise, the parameter estimation could achieve a relatively high level of data accuracy and at the same time, the convergence process becomes more stable and rapid. Before initializing the parameter space, a preliminary estimation and data filtering of the model parameters are required to ensure that the parameter space is closer to the real parameters and improve the algorithm's computational efficiency. The error entropy is calculated more standardized by the fixed interval length and the subinterval length. This paper provides a new method for the study of non-Gaussian system identification. In the future, the identification of non-Gaussian nonlinear systems will be further studied and discussed.

## References

[1] H. Wang, Bounded Dynamic Stochastic Systems: Modeling and Control, Springer-Verlag, London, UK, 2000.
[2] X. B. Feng and K. A. Loparo, Active probing for information in control system with quantized state measurements: A minimum entropy approach, IEEE Trans. Automat. Control, vol. 42, no. 2, pp. 216-238, Feb. 1997.
[3] A. Papoulis, Probability, Random Variables and Stochastic Processes, 3rd ed. New York: McGraw-Hill, 1991.
[4] A. Renyi, A Diary on Information Theory. New York: Wiley, 1987.
[5] L. Guo and H. Wang, Minimum entropy filtering for multivariate stochastic systems with non-gaussian noises, IEEE Trans. Automat. Control, vol. 51, no. 4, pp. 695-700, Apr. 2006.
[6] Goldberg D E. Genetic Algorithms in Search, Optimization and Machine Learning. 1989, xiii.
[7] Kristinsson K, Dumont G A. System identification and control using genetic algorithms. IEEE Transactions on Systems Man \& Cybernetics, 1992, 22(5):1033-1046.
[8] Lu Y, Sundararajan N, Saratchandran P. Performance evaluation of a sequential minimal radial basis function (RBF) neural network learning algorithm, IEEE Transactions on Neural Networks, 1998, 9(2):308-318.
[9] Ye G, Li W, Wan H. Study of RBF Neural Network Based on PSO Algorithm in Nonlinear System Identification. International Conference on Intelligent Computation Technology and Automation IEEE, 2015:852-855.
[10] Eberhart R C, Shi Y. Particle swarm optimization: Development, applications and resources. Evolutionary Computation, Proceedings of the 2001 Congress on. 2001:81-86 vol. 1.
[11] Trelea I C. The particle swarm optimization algorithm: convergence analysis and parameter selection. Information Processing Letters, 2003, 85(6):317-325.
[12] Qin A K, Huang V L, Suganthan P N. Differential evolution algorithm with strategy adaptation for global numerical optimization. IEEE Transactions on Evolutionary Computation, 2009, 13(2):398-417.
[13] Hauschild M, Pelikan M. An introduction and survey of estimation of distribution algorithms. Swarm and Evolutionary Computation, 2011, 1(3):111-128.
[14] Larranaga P, Lozano J A. Estimation of distribution algorithms: A new tool for evolutionary computation. Boston: Kluwer Press, 2002.
[15] Tjalling J. Ypma, Historical development of the Newton-Raphson method, Society for Industrial and Applied Mathematics, 1995.