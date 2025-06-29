# A Gaussian Process Assisted Offline Estimation of Multivariate Gaussian Distribution Algorithm 

Xin-Xin Ma<br>School of Computers Science \& Engineering<br>South China University of Technology<br>GuangZhou, China<br>maxinxinscut@163.com

Wei-Neng Chen<br>School of Computers Science \& Engineering<br>South China University of Technology<br>GuangZhou, China<br>cwnraul634@aliyun.com

Qiang Yang<br>School of Artificial Intelligence<br>Nanjing University of Information<br>Science and Technology<br>Nanjing, China


#### Abstract

Surrogated assisted evolutionary algorithms are commonly used to solve real-world expensive optimization problems. However, in some situations, no online data is available during the evolution process. In this situation, we have to build surrogate models based on offline historical data, which is known as offline data-driven optimization. Since no new data can be used to improve the surrogate models, offline data-driven optimization remains a challenging problem. In this paper, we propose a Gaussian process assisted offline estimation of multivariate Gaussian distribution algorithm to address the offline data-driven optimization problem. Instead of using surrogate models to predict the fitness values of individuals, we utilize a surrogate model to predict the rankings of individuals based on the frequently used lower confidence bound. In this way, the robustness of the proposed algorithm could be enhanced. Experiments are conducted on five commonly used benchmark problems. The experimental results demonstrate that the proposed offline surrogate model and the multivariate Gaussian estimation of distribution algorithm are able to achieve competitive performance.


Keywords-offline data-driven optimization, surrogate models, Gaussian Regression Process, multivariate Gaussian distribution, estimation of distribution algorithms

## I. INTRODUCTION

Evolutionary algorithms (EAs) have become one of the most important optimization techniques and have been successfully applied to solve many complex optimization problems in real world[1-5]. As EAs involve a population of individuals evolving generation by generation to approximate the global optimum of an optimization problem, it usually requires a lot of objective function evaluations. However, in many real-world optimization problems, the evaluation of objective function is complicated and time-consuming, or even requires physical simulations. Such problems are called computational expensive optimization problems. In these

[^0]problems, it becomes impossible for EAs to perform objective function evaluations for all individuals during all generations. To address these problems more efficiently, surrogate assisted evolutionary algorithms (SAEAs) have been proposed [6-8]. Different from traditional EAs, SAEAs use historical data to build surrogate models and use these models to estimate the fitness of individuals instead of using the computational expensive objective function, thus the search efficiency of SAEAs can be significantly improved [6].

Generally speaking, SAEAs consist of two parts, namely an optimizer and a surrogate model. In the literature, a variety of EAs have been used as the optimizer, such as genetic algorithms (GA) [9], differential evolution (DE) [10], particle swarm optimization (PSO) [11], etc.

Recently, estimation of distribution algorithms (EDAs) have emerged as a promising EA[12, 13]. Different from traditional EAs, EDAs work by building probability distributions based on the spatial distribution of some good individuals in the search space, and sampling a new generation of individuals based on these probability distributions. With this characteristic, EDAs are also classified as a type of model-based optimization algorithms. Traditionally, Gaussian distributions, Cauchy distributions, histogram, etc. are used as the probability model in EDAs. The covariance matrix adaptation-evolution strategy (CMA-ES) is also a kind of state-of-the-art EDAs [14]. Particularly, CMAES is a ranking-based search algorithm.

As a type of optimizer, EDAs can also be utilized in SAEAs. Compared with other EAs, EDAs may have the following additional advantages in SAEAs. First, since the objective function evaluation in SAEAs is based on surrogate models instead of the real objective function, it is usually not very accurate and includes some uncertainty. Meanwhile, probability distribution is an important tool for handling uncertainty. Hence, EDAs may have advantages to cope with the problems without accurate objective function evaluations. Second, while the surrogate models in SAEAs are used to model the landscape of the fitness function of the problem, the probability distribution models in EDAs are used to model the distribution of promising individuals in the search space. It is possible to investigate the relationship of these two types of models to further improve performance of EAs. Third, the probability distributions built in an EDA is actually a kind of


[^0]:    This work was supported in part by the Key Project of Science and Technology Innovation 2030 supported by the Ministry of Science and Technology of China (Grant No. 2018AAA0101300), in part by the National Natural Science Foundation of China under Grants 61976093 and 61772142, in part by the Science and Technology Plan Project of Guangdong Province 2018B050502006, and in part by Guangdong Natural Science Foundation Research Team 2018B030312003. Corresponding author: Wei-Neng Chen (cwnraul634@aliyun.com)

search memory of the individuals. In some specific problems, it is also possible to incorporate prior knowledge with principled techniques to modify the distribution. In this way, EDAs have shown promising performance on some complex optimization problems [12, 13].

Though EDAs may be promising to be incorporated as the optimizer in SAEAs, only a few studies considered the use of EDA in SAEAs. In the literature, CMA-ES has been used as the optimizer in SAEAs, combining with either a global or some local surrogate models [15]. For example, Kern et al. proposed a local meta-model CMAES (lmm-CMA) [16], which uses a set of local quadratic models. Hansen [17] designed a relatively simple global linear-quadratic surrogate approach for CMA-ES.

Most researches on SAEAs treat the optimizer and the surrogate model as two independent parts. In fact, the model in EDAs can provide information for the surrogate model in principle. Besides, exploring deep connections between the optimizer and the surrogate model can balance these two parts naturally and save computational cost by sharing some parameters of models. To this end, in this paper we intend to design a Gaussian process assisted offline estimation of multivariate Gaussian distribution algorithm. Specifically, we adopt the multivariate Gaussian distribution algorithm as the optimizer and use the Gaussian process (GP) modeling [18, 19] as the surrogate to solve offline data-driven optimization problems. In particular, instead of using the surrogate model to predict the fitness value of individuals, we utilize the surrogate model to predict the ranking of individuals based on the commonly-used lower confidence bound. In this way, the robustness of the EDA-based SAEAs can be improved.

The remainder of this paper is organized as follows. In Section 2, we provide the background of offline data driven optimization. In Section 3, we introduce our proposed method in detail. Section 4 conducts extensive experiments to validate the proposed algorithm. Finally, we draw a conclusion in Section 5.

## II. BACKGROUND

## A. Offline Data-Driven Optimization

In traditional EAs, the evaluation of objective function is called for every individual in every generation. However, in many real-world applications, the evaluation of objective function is usually very computationally expensive. Even worse, in some situations, there is no exact mathematical model to characterize the optimization problems and only data can be used to build a model to evaluate the fitness values of individuals.

Generally, the methods that build surrogate models based on data to characterize the optimization problems are named data-driven evolutionary algorithms [20]. According to whether to use new data in the evolution process to improve surrogate models, data-driven evolutionary algorithms can be divided into 1) online data-driven algorithms and 2) offline data-driven algorithms. The former usually utilize the new generated data in the evolution process to improve the quality of surrogate models, while the latter have no access to use new data to update the agent model in the iterative process of
evolutionary algorithms. Since offline data-driven algorithms are unable to improve the surrogate models, they are generally more challenging.

Since many practical problems only have historical data and are unable to update data in real time, offline data-driven optimization is more common in real-world applications. The main challenge of offline data-driven optimization is how to effectively make use of limited data to build high-quality surrogate models. A recent work [21] by Wang et al. designed an offline data-driven evolutionary algorithm using the ensemble learning method in machine learning area. The ensemble learning method aims to improve the accuracy of the surrogate model to assist the evolutionary algorithm to evolve efficiently.

## B. Gaussian Process Modeling

The Gaussian regression process, also known as Kriging interpolation, is a stochastic approximation method [12]. A universal Kriging model assumes that the fitness function can be approximated as:

$$
Y(\boldsymbol{x})=\mu(\boldsymbol{x})+\epsilon(\boldsymbol{x})
$$

where $\mu(\boldsymbol{x})$ is the trend function and $\epsilon(\boldsymbol{x})$ is the error term with mean $\mathbf{0}$ and covariance matrix $\sigma^{2} \boldsymbol{\phi}$.

The covariance is computed as follows:

$$
\operatorname{cov}(Y(\boldsymbol{x}+\boldsymbol{h}), Y(\boldsymbol{x}))=\sigma^{2} \boldsymbol{\phi}(\boldsymbol{h})
$$

where $\operatorname{cov}(Y(\boldsymbol{x}+\boldsymbol{h}), Y(\boldsymbol{x}))$ is the correlation function.
In general, the parameters above can be determined by maximizing the likelihood function for input datapoints.

$$
\frac{1}{\left(2 \pi \sigma^{2}\right)^{K / 2} \sqrt{\operatorname{det}(C)}} \exp \left[-\frac{(y-\mu)^{T} C^{-1}(y-\mu)}{2 \sigma^{2}}\right]
$$

where $\boldsymbol{C}=\boldsymbol{\sigma}^{\mathbf{2}} \boldsymbol{\phi}$ is the covariance matrix.

1) Ordinary Kriging: In reality, the trend function $\mu(\boldsymbol{x})$ is very difficult to capture. Therefore, the following special case is widely used and known as the ordinary kriging:

$$
Y(x)=\mu_{0}+\epsilon(x)
$$

2) Blind Kriging: The blind kriging is a modified variant of the universal kriging. As often, the trend function is not prior in the blind kriging. Therefore, it usually tries to select variables to construct the trend function through forward Bayesian process [11].

$$
Y(\boldsymbol{x})=v(\boldsymbol{x})^{\top} \mu_{m}+\epsilon(\boldsymbol{x})
$$

where $(\boldsymbol{x})^{\top}=\left(\mathbf{1}, \boldsymbol{v}_{\mathbf{1}}, \ldots, \boldsymbol{v}_{\mathbf{m}}\right), \boldsymbol{\mu}_{\boldsymbol{m}}=\left(\boldsymbol{\mu}_{0}, \boldsymbol{\mu}_{\mathbf{1}}, \ldots, \boldsymbol{\mu}_{\mathbf{m}}\right)$ and m is the number of selected variables.

## III. THE PROPOSED METHOD

## A. Multivariate Gaussian Distribution Estimation

To accommodate with the Gaussian regression model, we adopt the multivariate Gaussian distribution algorithm as the search engine in our proposed SAEA. In particular, the Gaussian distribution is widely observed in nature and the central limit theorem provides the theoretical basis for the applicability of the multivariate Gaussian distribution. Inspired by CMA-ES which is also based on the Gaussian distribution, we utilize the estimated multivariate Gaussian distribution model to generate new candidate solutions for EDA.

```
Algorithm 1 Pseudo-Code of Multivariate Gaussian
    Distribution Estimation algorithm for generating
    offspring
```

Input: $\boldsymbol{D}$ : database; $\lambda$ : the number of offspring; $n$ : the number of all data points in the dataset
1: Sort the dataset items according to their fitness;
$2: \bar{x}_{D}=\frac{\sum_{i=1}^{n} x_{i}}{\sum_{i=1}^{n} n}$;
3: $\omega_{i}=\frac{\ln (\mu+1)-\ln i}{\mu \ln (\mu+1)-\sum_{j=1}^{n} \ln i} ; / /$ the weight function
4: For $j=1$ to $\mu$ do
5: $\quad y_{j}=x_{j}-\bar{x}_{D}$
6: $\quad C=y_{1: \mu} \times \operatorname{diagonal}\left(\omega_{1: \mu}\right) \times y_{1: \mu}^{\top}$;
7: End For
8: For $k=1$ to $\lambda$ do
9: $\quad S_{k}=\bar{x}_{\mu}+N(0, C)$;
10:End For
Output: 5: the offspring set

Specifically, a multivariate Gaussian distribution model can be estimated by a mean vector $\boldsymbol{m}$ and a covariance matrix $\boldsymbol{C}$ as Eq. (6).

$$
\boldsymbol{N}(\boldsymbol{m}, \boldsymbol{C})
$$

where $\boldsymbol{m}$ is the modal value of the distribution, and $\boldsymbol{C}$ is the covariance matrix that determines the orientation of the distribution.

In order to generate more promising offspring, the modal value of the constructed Gaussian distribution is determined by the first ranked $\mu$ points, and the covariance matrix is computed based on the difference vectors between the $\mu$ points and the mean vector $\overline{\boldsymbol{x}}_{\boldsymbol{D}}$ of the input dataset. The construed multivariate Gaussian distribution provides a heuristic search for the promising area. The details of the multivariate Gaussian distribution estimation algorithm are presented in Algorithm 1. For the input database, it is first sorted according to the fitness values of items. The mean value $\overline{\boldsymbol{x}}_{\boldsymbol{D}}$ of the whole database is calculated and the weight vector $\boldsymbol{\omega}$ is set. Then, the first ranked $\mu$ data points are combined via the weight vector $\boldsymbol{\omega}$. The covariance matrix is then calculated as shown in lines 4-7. After the estimation of the mean vector and the covariance matrix, $\lambda$ offspring are generated by the constructed multivariate Gaussian distribution model.

## B. The Proposed Framework

For the accuracy of the surrogate model, only the data with real fitness is used to build the surrogate model. To initialize the database, we sample enough offline data points via the multivariate Gaussian distribution. For example, for the Ddimension Griewank function with a search space [- 600, 600], we sample points by the normal distribution with mean vector $[10, \ldots, 10]$, standard deviation 600 and the identity matrix as the covariance matrix. Particularly, $11 \times \mathrm{D}$ points are sampled and evaluated by the real objective function to initialize the database. Considering that the minimum function value of the Griewank function is 0 , we use $[10, \ldots, 10]$ as the mean vector to reduce bias. In this work, we do not use the popular Latin hypercube sampling (LHS) method because 1) the estimation of multivariate Gaussian distribution works better on a prior normal distribution; and 2) the offline data in the real-world is hardly evenly distributed.

The specific algorithm flow is shown in Fig. 1 and the main steps are listed as follows:
Step 1: Use the normal distribution sampling to get $11 \times D$ points and use the real objective function to evaluate these points. These points constitute the initial database.

Step 2: Establish a global GP surrogate model based on the initial database.

Step 3: Add all the points in the initial database to the hybrid database.

Step 4: Estimate the multivariate Gaussian distribution of the hybrid data set and generate $\boldsymbol{\lambda}$ offspring.
Step 5: Evaluate the offspring using the surrogate model and add the most promising solutions into the hybrid database.

Step 6: Repeat Steps 4 and 5 until the convergence condition is satisfied.
![img-0.jpeg](img-0.jpeg)

Fig. 1.The flow diagram of the proposed framework
There are two remarks for the proposed framework: 1) the prediction of the Gaussian process regression model gives the estimated distribution of prediction value at the evaluated

point. Specifically, it is a normal distribution with mean value $\overline{\boldsymbol{f}}(\boldsymbol{x})$ and variance $\boldsymbol{s}(\boldsymbol{x})$. The commonly used lower confidence bound (LCB) presented below is employed to evaluate the quality of the solutions. The more promising region has a low predicted mean value while the less explored region has a high variance. Indexed by LCB, the algorithm can realize the trade-off between the exploitation and exploration in the evolution process.

$$
\boldsymbol{f}_{l c b}(\boldsymbol{x})=\overline{\boldsymbol{f}}(\boldsymbol{x})-\omega s(\boldsymbol{x})
$$

where is $\boldsymbol{\omega}$ set as 2 in this paper; 2) the evaluation of the surrogate model is only used for sorting the solutions. Therefore, this increases the robustness of the algorithm.

## IV. EXPERIMENTS

In this section, the performance of the developed offline algorithm is assessed via experiments conducted on five commonly used benchmark problems. Particularly, all the benchmark problems in the experiments contain 10 dimensions. The number $(\lambda)$ of offspring generated by the estimation of multivariate Gaussian distribution is set as 50 and the number $(\mu)$ of elite solutions used to estimate multivariate Gaussian distribution is set as 10 . As for the surrogate model implementation, we utilize the welldocumented blind dace toolbox to build surrogate model [4]. In the following, we will first introduce the used five benchmark problems and then we will investigate the performance of the proposed offline algorithm in four aspects: 1) convergence curves of the blind kriging assisted offline algorithm, 2) comparison between different surrogates (the ordinary kriging and the blind kriging) on convergence curves, 3) comparison between different surrogates on the performance of the five benchmark problems, and 4) comparison between two version GPEME on the Five Benchmark Problems

## A. Benchmark Problems

In this paper, we utilize the following five widely used benchmark problems to validate the proposed offline algorithm:

1) Ellipsoid Problem

$$
\begin{gathered}
\min f(x)=\sum_{i=1}^{n} i x_{i}^{2} \\
x \in[-5.12,5.12], n=10 \\
\text { minimum: } f\left(x^{*}\right)=0
\end{gathered}
$$

2) Rosenbrock Problem

$$
\begin{gathered}
\min f(x)=\sum_{i=1}^{n}\left[100\left(x_{i+1}-x_{i}^{2}\right)^{2}+\left(a-x_{i}\right)^{2}\right] \\
x \in[-2.048,2.048], n=10 \\
\text { minimum: } f\left(x^{*}\right)=0
\end{gathered}
$$

3) Ackley Problem

$$
\begin{gathered}
\min f(x)=-a \times \exp \left(-b \sqrt{\frac{1}{n} \sum_{i=1}^{n} x_{i}^{2}}\right) \\
-\exp \left(\frac{1}{n} \sum_{i=1}^{n} \cos \left(c x_{i}\right)\right)+a+\exp (1) \\
x \in[-32.768,32.768], n=10, a=20, b=0.2 \\
\text { minimum: } f\left(x^{*}\right)=0
\end{gathered}
$$

4) Griewank Problem

$$
\begin{gathered}
\min f(x)=1+\sum_{i=1}^{n} \frac{x_{i}^{2}}{4000}-\prod_{i=1}^{n} \cos \left(\frac{x_{i}}{\sqrt{i}}\right) \\
x \in[-600,600], n=10 \\
\text { minimum: } f\left(x^{*}\right)=0
\end{gathered}
$$

5) Rastrigin Problem

$$
\begin{gathered}
\min f(x)=10 n+\sum_{i=1}^{n}\left(x_{i}^{2}-10 \cos \left(2 \pi x_{i}\right)\right) \\
x \in[-5,5], n=10 \\
\text { minimum: } f\left(x^{*}\right)=0
\end{gathered}
$$

## B. Convergence Curve of the Blind Kriging

Firstly, experiments are carried out to verify whether the offline algorithm can converge to a reasonable solution. We conduct experiments on the 10-dimension Ellipsoid and Griewank problems. The convergence curves of the proposed algorithm are shown in Figss. 2-5. The first 110 black points in the figures (Figs. 2 and 4) are those in the initial database, while the red points are the solutions that are selected into the hybrid database during the iterations of the proposed algorithm.

From these figures, we can see that the proposed offline algorithm converges in less than 120 iterations and the final converged solution has a reasonable real objective value for the two tested problems.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Convergence curve of the blind kriging assisted offline algorithm on the Ellipsoid problem with points in the initial dataset included.

![img-6.jpeg](img-6.jpeg)

Fig. 3. Convergence curve of the blind kriging assisted offline algorithm on the Ellipsoid problem with points in the initial dataset excluded.
![img-5.jpeg](img-5.jpeg)

Fig. 4. Convergence curve of the blind kriging assisted offline algorithm on the Griewank problem with points in the initial dataset included.
![img-6.jpeg](img-6.jpeg)

Fig. 5. Convergence curve of the blind kriging assisted offline algorithm on the Griewank problem with points in the initial dataset excluded.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Convergence curve comparison between the blind kriging and the ordinary kriging assisted offline algorithms on the Ellipsoid problem.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Convergence curve comparison between the blind kriging and the ordinary kriging assisted offline algorithms on the Griewank problem

## C. Comparison Between Different Surrogates on Convergence Curves

In this section, we observe the performance on the proposed offline algorithm with different surrogate models. Particularly, we utilize the ordinary kriging model and the blind kriging model to assist the proposed offline algorithm to optimize the Ellipsoid problem and the Griewank problem respectively.

The convergence curves of the offline algorithm with the above two kriging models are presented in Figs. 6-7. From these two figures, we can see that the final converged solution of the blind kriging assisted offline algorithm is much better than that of the ordinary kriging assisted one because the final converged solution of the blind kriging assisted offline algorithm is much closer to the optimal solution of the problems.

The above comparison results indicate that the surrogate model plays a vital role in the offline data-driven optimization algorithms. Specifically, a suitable surrogate model can optimize the search process while a poor surrogate model may mislead the search process.

TABLE I. OPTIMIZATION RESULTS OF THE ORDINARY KRIGING ASSISTED OFFLINE ALGORITHM ON THE 5 BENCHMARK PROBLEMS.


TABLE II. OPTIMIZATION RESULTS OF THE BLIND KRIGING ASSISTED OFFLINE ALGORITHM ON THE 5 BENCHMARK PROBLEMS


TABLE III. COMPARISON WITH TWO VERSION GPEME ON THE FIVE BENCHMARK PROBLEMS

## D. Comparison Between Different Surrogates on the Five Benchmark Problems

Finally, we execute the offline algorithm with different surrogates on all the five problems to make a comprehensive comparison. It should be noted that all algorithms are executed independently for 20 times.

The statistical results are summarized in Table I and Table II. It should be noted that in the evolution process of the offline algorithm, no new data is available and used to improve the surrogates. When the algorithm stops, the final solution is evaluated by the real objective function to assess the performance of the offline algorithm.

Comparing Table I with Table II, we can see that 1) on the Griewank, Ellipsoid and Rosenbrock problems, the quality of the final solution of the offline algorithm assisted by the blind kriging is much better than that by the ordinary kriging.; 2) on the Rosenbrock problem, the solution quality of the offline algorithms assisted by the two surrogates is not high, because the Rosenbrock problem has a very narrow valley, leading to that the Gaussian regression process is unable to capture this feature well; 3) although the performance of the offline algorithm using the ordinary kriging on most functions is not satisfied, the algorithm is more robust; 4) on the Rastrigin problem, the blind kriging assisted offline algorithm is unable to converge to a good solution. In fact, the real objective value of the obtained solution during iterations is getting worse and worse. But the ordinary kriging assisted one can still converge to a reasonable solution. This comparison reflects that the accuracy of the surrogate model is problem
dependent. There is hardly a general suitable single global surrogate model. Therefore, we need to select an appropriate surrogate model for specific problems.

## E. Comparison with two version GPEME on the Five Benchmark Problems

Most offline data driven algorithms use ensemble-based model. For example, DDEA-SE proposed by Wang et al. is a state-of-art ensemble-based offline data-driven EAs whose ensemble consists of 2000 RBF models. Since our method is single surrogate-assisted, comparisons to the existed ensemble-based offline data-driven EAs may not be fair. Here we choose an online data-driven EA: GPEME, which use the same Gaussian process surrogate model as ours. Online datadriven EAs can be transferred into offline versions by initializing the surrogate using all allowed computational budget and stop once the first real fitness evaluation is required. The reference paper [14] has provided the optimization result of GPEME online version and GPEME offline version on the five benchmark problems. Here we use the provided data for comparison presented in Table III. From Table III, we can conclude that our method achieve much better results on Griewank and Ellipsoid problem. These verifies the Multivariate Gaussian Distribution Estimation algorithm can capture the characteristic of Griewank and Elliposid problem thus achieve a better performance. Also, our method does not perform well on Rosenbrock and Rastrigin problems, this enlighten us to design some strategies to improve the robustness of our method.

## V. CONCLUSIONS

In this paper, we have proposed a blind kriging assisted offline estimation of multivariate Gaussian distribution algorithm to tackle expensive optimization problems. Instead of using surrogate models to predict the fitness values of individuals in existing studies, we employ the blind kriging model to predict the rankings of individuals based on the commonly used lower confidence bound. In this way, the robustness of the proposed algorithm could be enhanced. Extensive experiments conducted on five commonly used benchmark problems demonstrate that the proposed offline algorithm assisted by the blind kriging model could achieve competitive or even better performance than another commonly used offline surrogate model (namely the ordinary kriging model) assisted offline algorithm.

In this paper, we have taken the relation between the Multivariate Gaussian Distribution algorithm and the blind kriging model into consideration to optimize problems. However, the considered relation is just a shallow combination of the two models. In the future, we can explore the internal relationship by sharing some hyper parameters of two models. In addition, advanced machine learning methods like transfer learning, are also under consideration to boost the performance of offline data-driven methods.

In future study, it would be interesting to consider EDAs for large-scale data-driven optimization [22]-[24] and complex optimization problems under uncertainty [25].
