# Research Article 

## Restricted Boltzmann Machine-Assisted Estimation of Distribution Algorithm for Complex Problems

Lin Bao, ${ }^{1,2}$ Xiaoyan Sun $\otimes,{ }^{1}$ Yang Chen, ${ }^{1}$ Guangyi Man, ${ }^{1}$ and Hui Shao ${ }^{1}$<br>${ }^{1}$ School of Information and Control Engineering, China University of Mining and Technology, Xuzhou, Jiangsu, China<br>${ }^{2}$ School of Electronics and Information, Jiangsu University of Science and Technology, Zhenjiang, Jiangsu, China<br>Correspondence should be addressed to Xiaoyan Sun; xysun78@126.com

Received 24 May 2018; Revised 17 August 2018; Accepted 19 August 2018; Published 1 November 2018
Academic Editor: Diyi Chen
Copyright © 2018 Lin Bao et al. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

A novel algorithm, called restricted Boltzmann machine-assisted estimation of distribution algorithm, is proposed for solving computationally expensive optimization problems with discrete variables. First, the individuals are evaluated using expensive fitness functions of the complex problems, and some dominant solutions are selected to construct the surrogate model. The restricted Boltzmann machine (RBM) is built and trained with the dominant solutions to implicitly extract the distributed representative information of the decision variables in the promising subset. The visible layer's probability of the RBM is designed as the sampling probability model of the estimation of distribution algorithm (EDA) and is updated dynamically along with the update of the dominant subsets. Second, according to the energy function of the RBM, a fitness surrogate is developed to approximate the expensive individual fitness evaluations and participates in the evolutionary process to reduce the computational cost. Finally, model management is developed to train and update the RBM model with newly dominant solutions. A comparison of the proposed algorithm with several state-of-the-art surrogate-assisted evolutionary algorithms demonstrates that the proposed algorithm effectively and efficiently solves complex optimization problems with smaller computational cost.

## 1. Introduction

Evolutionary computation (EC) has attracted considerable research attention in recent decades because of its ability to handle optimization problems [1]. EC methods, e.g., genetic algorithms (GAs), estimation of distribution algorithm (EDA), particle swarm optimization (PSO), ant colony optimization (ACO), and differential evolution (DE), have been empirically shown to perform well for a wide variety of real-world applications including load scheduling [2], energy management systems [3, 4], robotics [5], parameter control [6, 7], classification [8], and community detection [9]. These optimization problems usually have different types of decision variables, e.g., binary, integer, real, and mixed integer, and do not assume any convexity or differentiability of the objective functions and/or constraints involved. Despite the advantages, EC methods are often criticized because they have a relative slow convergence and a large amount of function evaluations (FEs), which present a serious challenge when
applying EC for computationally expensive optimization problems, e.g., fluid dynamic optimization, aerodynamic optimization, hybrid car controller optimization, or structural optimization. In solving such computationally expensive optimization problems, the heavy computational cost has a major impact on the effectiveness and efficiency of traditional ECs. To address this challenge, surrogate-assisted evolutionary algorithms (SAEAs) [10-12], such as surrogate-assisted GA [13, 14], surrogate-assisted PSO [15-17], and surrogateassisted DE [18, 19], are receiving increasing attention in the EC community.

SAEAs have been developed to solve computationally expensive optimization problems, and they reduce the computational cost to a relatively low budget by using the computationally inexpensive surrogate models to replace the part of the expensive FEs. In the literature, common surrogate models include polynomial regression (PR) models [20], support vector machines (SVMs) [21], radial basis functions (RBFs) [16, 22, 23], artificial neural networks (ANNs) [24],

and kriging [25, 26]. Sun et al. [16] proposed a surrogateassisted cooperative swarm optimization algorithm for high-dimensional expensive optimization problems, in which an RBF network is employed as the surrogate model. Akhtar and Shoemaker [23] proposed a parallel response surface-assisted evolutionary algorithm approach for multiobjective optimization, using RBFs to calculate surrogate response surfaces as an approximation of the computationally expensive objective function. Liu et al. [18] proposed a Gaussian process surrogate model to assist DE in solving computationally expensive optimization problems, named the surrogate model-aware evolutionary search (SMAS). However, the SMAS are trapped in local optima for computationally expensive optimization problems with discrete variables. Furthermore, Liu et al. [19] proposed a SAEA to solve expensive design optimization problems with discrete variables. Chugh et al. [25] proposed a krigingbased surrogate-assisted reference vector-guided evolutionary algorithm to approximate the computationally expensive objective function to reduce the computational cost. Min et al. [27] presented an adaptive knowledge reuse framework based on the novel idea of multiproblem surrogates and proposed a transfer evolutionary multiobjective optimization to solve multiobjective expensive optimization problems. Yang et al. [28] proposed a self-evaluation evolution algorithm to address high-dimensional computationally expensive optimization problems with the aid of metamodels.

Most existing SAEAs focus on constructing the surrogate model to accurately estimate the individual fitness by approximating the exact expensive function as closely as possible. Accordingly, these methods are limited in that they only apply the surrogate as a fitness estimation and do not adequately extract other relevant information or latent knowledge to further guide the evolution. The performance of surrogate-assisted ECs in solving complex problems will be greatly enhanced if the surrogate is designed to provide fitness estimation and evolutionary knowledge. Motivated by this, we propose a surrogate based on restricted Boltzmann machine (RBM) that can learn the distribution of the input data to implicitly describe the interactions among the variables and present an energy function to represent the relationships between the dependent and independent variables. The distribution or interactions of the variables are used to guide the evolution by using it as a probability model for EDA, and the energy function is applied to estimate the values of the complicated optimization objectives.

An RBM-assisted EDA (RBMAEDA) is proposed to solve computationally expensive optimization problems with discrete variables. First, the EDA is the evolutionary frame of the proposed RBMAEDA. An RBM model is constructed and trained by the distributed representative information of promising solutions. The probability model based on the RBM is then designed as the probability model in the EDA. Second, the fitness evaluation strategy based on the RBM energy function is developed as the surrogate model to estimate the individual fitness and reduce the computational cost. Third, model management is conducted to further improve the effectiveness of the RBMAEDA. Finally, the proposed RBMAEDA is validated by a series of benchmark
problems, and the experimental results demonstrate that the RBMAEDA can achieve satisfying performance with fewer FEs for complex optimization problems.

The main contributions of this paper are as follows:
(1) An improved EDA based on an RBM is designed to generate new potential better individuals with discrete variables for guiding the evolutionary progress in the search space
(2) The surrogate model based on an RBM is proposed to partly replace FEs to estimate the individual fitness and reduce the computational cost
(3) The model management is presented to further enhance the effectiveness of the RBMAEDA by considering the relative rank of the promising individuals

The remainder of this paper is organized as follows. Section 2 briefly reviews the related techniques, including EDA and RBM. Section 3 describes the proposed RBMAEDA in detail. Section 4 demonstrates the comparative experimental results. Finally, Section 5 summarizes the paper and presents conclusions along with the scope of future extensions of this work.

## 2. Related Work

2.1. EDA. EDA [29-31] is a stochastic optimization algorithm based on statistical theory, which establishes the probability model from the macro perspective and describes the distributed information of the candidate solutions in the search space. Then, it predicts the promising region by statistical learning and produces new individuals by random sampling of the probability model. Meanwhile, the probability model is gradually updated with the increasing information on the better solutions. This process continues to realize the evolutionary progress and achieve excellent solutions until the termination conditions are met. Compared with GA methods, EDA makes full use of the global information of the solution space and the historical information of the promising region to explore and exploit better solutions in the evolutionary process, which effectively and efficiently improves the searching ability to solve the nonlinear optimization and the variable coupling problems. It has become a hot topic and has been successfully applied in many engineering fields.

EDA forms an effective parallel search framework based on building and sampling the probability model. According to the structure of the probability model and the relationship between the variables, probabilistic modelling techniques can be classified into univariate, bivariate, and multivariate methods. Univariate modelling methods are simple and easy to implement but do not fully utilize the linkage information of the decision variables to guide the evolutionary process. Bivariate and multivariate modelling methods can make use of the linkage information in the decision space to improve the searching ability of EDA but are generally more complex and difficult. Generally, the difficulty arises from the solution space of a problem expanding exponentially

![img-0.jpeg](img-0.jpeg)

Figure 1: Structure of RBM.
with dimensionality so that the expanded solution space quickly exceeds the searching ability of existing EDA methods. In addition, EDA can easily overfit the distribution of the candidate solutions in the evolutionary process, which leads to an inaccurate representation of the promising region and failure of the searching process. Meanwhile, the population diversity will be gradually weakened to cause premature convergence in the EDA evolutionary process. Therefore, it is necessary to design appropriate probability models to describe the relationship between variables and the distributed information of the promising region for complex optimization problems. Researchers have proposed novel EDAs based on machine learning methods [32] and other techniques. Most EDAs are used for continuous optimization problems, whereas relatively few studies have focused on discrete combinatorial optimization problems. In addition, researches on surrogate-assisted EDA are relevant less mainly because of the difficulties in designing an appropriate probability model and surrogate model in EDA [33].
2.2. RBM. The RBM is an energy-based stochastic neural network with unsupervised learning, which has a twolayer network structure with symmetric connections and no self-feedback. The structure of an RBM is presented in Figure 1.

In the network structure, $v$ is the visible layer with $N$ visible units, which indicates the input data, and $h$ is the hidden layer with $M$ hidden units, which is the feature extractor. The RBM can learn the multivariate dependencies between the decision variables. Assuming that all the neurons in the RBM are binary variables, the energy function of the state $\{v, h\}$ is used as the measure of the whole network state and is formulated as follows:

$$
E_{\theta}(v, h)=-\sum_{i=1}^{N} \sum_{j=1}^{M} v_{i} W_{i j} h_{j}-\sum_{i=1}^{N} a_{i} v_{i}-\sum_{j=1}^{M} b_{j} h_{j}
$$

where $v_{i}$ is the state of the $i$ visible unit; $h_{j}$ is the state of the $j$ hidden unit; $\theta=\left\{W_{i j}, a_{i}, b_{j}\right\}$ represents the model parameters; $W_{i j}$ is the symmetric interaction weight between the visible unit $i$ and hidden unit $j ; a_{i}$ is the bias of the visible unit $i$; and $b_{j}$ is the bias of the hidden unit $j$.

The stability of the RBM network is measured through the energy function. Given the state of the visible unit, the activation state of each hidden unit is independent, and the activation probability of the $j$ hidden unit is as follows:

$$
P_{\theta}\left(h_{j}=1 \mid v\right)=\sigma\left(b_{j}+\sum_{i} v_{i} W_{i j}\right)
$$

where $\sigma(x)=1 /(1+\exp (-x))$ is the logistic function.
Given the state of the hidden unit, the activation state of each visible unit is also independent, and the activation probability of the $i$ visible unit is as follows:

$$
P_{\theta}\left(v_{i}=1 \mid h\right)=\sigma\left(a_{i}+\sum_{j} W_{i j} h_{j}\right)
$$

As for the training of RBM, Hinton [34] proposed a fast learning algorithm for RBM, i.e., the contrastive divergence (CD) algorithm, which greatly improves the learning efficiency of RBM. Subsequently, researches on RBM have been boomed, and RBM has been widely used in speech recognition [35], signal processing [36], imagery classification [37], high-dimensional time series modelling [38], etc.

## 3. RBM-Assisted EDA

The general framework of the RBM-assisted EDA is shown in Figure 2.
3.1. Construction of Softmax RBM Based on Dominant Solutions. RBM is an effective feature extraction technique that has self-organization, self-learning, nonlinear approximation ability, and better fault tolerance. In this paper, the visible units of RBM adopt softmax units [39] to further improve the feature extraction ability, which can increase the sparsity of input data so that the hidden units can only be activated in limited cases. The RBM model has a twolayer network structure. The visible layer $V$ has $N$ visible softmax units, which indicate $N$ decision variables. Each visible softmax unit consists of $K$ binary units. The hidden layer $h$ has $F$ hidden units (binary units) and indicates feature information. The architecture diagram of the softmax RBM network model is illustrated in Figure 3.

The visible softmax units of the input data are $V=\left\{v_{1}^{k}\right.$, $\left.v_{2}^{k}, \cdots, v_{N}^{k}\right\}, k \in\{1,2, \cdots, K\}$, which form a $K \times N$ matrix. If the $v_{i}^{k}$ (in the $k$ row and $i$ column) of the $i$ softmax unit is $v_{i}^{k}=1$, then the value of the $i$ decision variable in the input data is $k$ and the rest of the $i$ softmax unit is $v_{i}^{k}=0, k^{\prime} \neq k$. For example, if the number of decision variables in a problem is 6 and each decision variable contains ten integer values from 0 to 9 , the total search space of the problem is $10^{6}$. Therefore, the input data of a feasible solution (signed an individual $X$ ) is composed of 6 decimal coding sequences, and the coding sequence corresponding to the individual $X$ is as follows:

$$
\text { Individual } X
$$


The alleles of the individual $X$ correspond to the values of the decision variables. The code sequence of individual $X$ is

![img-2.jpeg](img-2.jpeg)

Figure 2: Flow diagram of the RBM-assisted EDA.
converted to softmax units consisting of a $10 \times 6$ binary matrix $V$ :

![img-2.jpeg](img-2.jpeg)

Figure 3: Architecture diagram of softmax RBM.

Mathematically, the conditional distribution probabilities of the visible unit $v_{i}^{h}$ and the hidden unit $h_{j}$ are formulated as (6) and (7), respectively.

$$
p_{i t}\left(h_{j}=1 \mid V\right)=\sigma\left(b_{j}+\sum_{i=1}^{m} \sum_{k=1}^{K} v_{i}^{h} W_{i j}^{h}\right)
$$

$$
p_{\theta}\left(v_{i}^{k}=1 \mid h\right)=\frac{\exp \left(a_{i}^{k}+\sum_{j=1}^{F} h_{j} W_{i j}^{k}\right)}{\sum_{i=1}^{K} \exp \left(a_{i}^{k}+\sum_{j=1}^{F} h_{j} W_{i j}^{k}\right)}
$$

where $W_{i j}^{k}$ is the connection weight between the $k$ binary unit of the $i$ visible softmax unit $v_{i}$ and the $j$ hidden unit $h_{j} ; a_{i}^{k}$ is the bias of the visible softmax unit $v_{i}^{k}$, and $b_{j}$ is the bias of the hidden unit $h_{j}$.

The population of the RBMAEDA is $\operatorname{Pop}(g)=\left\{X_{i}, i=\right.$ $1,2, \cdots, M\}$, and the population size is $M$. Each individual $X_{i}$ is represented by $N$ decision variables, which corresponds to the visible softmax units of the input data $V_{i}$ in the softmax RBM model. Subsequently, the individual fitness in the initial $\operatorname{Pop}(g)$ is calculated according to exact expensive function. The dominant subset $\operatorname{Sub}(g)$ is formed by selecting $S(S \leq M)$ better individuals $X_{i} \in\left\{X_{1}, X_{2}, \cdots, X_{S}\right\}$ according to the truncation selection strategy. Then, $\operatorname{Sub}(g)$ is used as training data for the softmax RBM model by using a CD learning algorithm [39].
3.2. Probability Model Based on Softmax RBM. When the training process of the softmax RBM has been finished, the probabilistic distribution is constructed by clamping the distributed information of the alleles of the dominant individuals into the marginal probability of each decision variable in the softmax RBM model. According to (7), the activation probability $p_{\theta}\left(v_{i}^{k}=1 \mid h\right)$ of the visible softmax units $V=$ $\left\{V_{1}, V_{2}, \cdots, V_{N}\right\}$ is calculated by using the activation probability $p_{\theta}\left(h_{j}=1 \mid V\right)$ of the hidden units $h=\left\{h_{1}, h_{2}, \cdots, h_{F}\right\}$ in the trained softmax RBM model. The probability model $P(V)$ based on the softmax RBM is designed as follows:
$P(V)=\left[\begin{array}{llll}p_{\theta}\left(v_{1}^{1}=1 \mid h\right) & p_{\theta}\left(v_{2}^{1}=1 \mid h\right) & \cdots & p_{\theta}\left(v_{N}^{1}=1 \mid h\right) \\ p_{\theta}\left(v_{1}^{2}=1 \mid h\right) & p_{\theta}\left(v_{2}^{2}=1 \mid h\right) & \cdots & p_{\theta}\left(v_{N}^{2}=1 \mid h\right) \\ \vdots & \vdots & \vdots & \vdots \\ p_{\theta}\left(v_{1}^{K}=1 \mid h\right) & p_{\theta}\left(v_{2}^{K}=1 \mid h\right) & \cdots & p_{\theta}\left(v_{N}^{K}=1 \mid h\right)\end{array}\right]$
The pseudocode for the probabilistic modelling is presented in Algorithm 1.

The probability model $P(V)$ is constructed and calculated based on the softmax RBM model. By sampling $P(V)$ with the roulette, $(M-S)$ new potential individuals, which have the distributed representative information of the decision variables of the promising solutions, are subsequently generated for the next generation $\operatorname{Pop}(g+1)$.

The roulette sampling technique is formulated as follows:
$x_{i}= \begin{cases}1, & \text { if random }(0,1) \leq p_{\theta}\left(v_{i}^{k}=1 \mid h\right), \\ 2, & \text { if } p_{\theta}\left(v_{i}^{k}=1 \mid h\right)<\operatorname{random}(0,1) \leq \sum_{j=1}^{S} p_{\theta}\left(v_{j}^{k}=1 \mid h\right), \\ \vdots & \\ N, & \text { if } \sum_{j=1}^{N-1} p_{\theta}\left(v_{i}^{k}=1 \mid h\right)<\operatorname{random}(0,1) \leq \sum_{j=1}^{N} p_{\theta}\left(v_{i}^{k}=1 \mid h\right),\end{cases}$
where $x_{i}$ is the $i$ decision variable of the new individual and random $(0,1)$ is a random value ranging from $[0,1]$.
3.3. Surrogate Model Based on Softmax RBM. According to Section 3.2, a softmax RBM model with the distributed representative information of the decision variables of the promising solutions is trained and obtained, which models the topology of the better solutions in the search space. Assuming that an individual $X_{i}=\left\{x_{i 1}, x_{i 2}, \cdots, x_{i N}\right\}$ is transformed into the softmax units $V_{i}=\left\{v_{i 1}^{k}, v_{i 2}^{k}, \cdots, v_{i N}^{k_{i j}}\right\}$ for the softmax RBM model, the energy value $E_{\theta}\left(V_{i}, h\right)$ of the individual $X_{i}=\left\{x_{i 1}, x_{i 2}, \cdots, x_{i N}\right\}$ is formulated as follows:

$$
E_{\theta}\left(V_{i}, h\right)=-\sum_{n=1}^{N} \sum_{f=1}^{F} \sum_{k=1}^{K} W_{n f}^{k} h_{f} v_{n}^{k}-\sum_{n=1}^{N} \sum_{k=1}^{K} v_{n}^{k} a_{n}^{k}-\sum_{f=1}^{F} h_{f} b_{f}
$$

The energy value $E_{\theta}\left(V_{i}, h\right)$ of the individual $X_{i}$ indicates the adaptation level to the RBM topology of the promising solutions. The lower the energy value, the better is the stability of the RBM. It may be considered that the feature of the individual $X_{i}$ is consistent with that of the promising solutions, and the individual $X_{i}$ is superior others. Consequently, we can utilize the energy value $E_{\theta}$ $\left(V_{i}, h\right)$ of the individual $X_{i}$ in the softmax RBM to estimate the individual fitness of $X_{i}$. The surrogate model based on the softmax RBM estimates the individual fitness of $X_{i}$ and is defined as follows:

$$
\widehat{f}\left(V_{i}\right)=-\frac{E_{\theta}\left(V_{i}, h\right)-\min \left(E_{\theta}\left(V_{i}, h\right)\right)}{\sum_{i=1}^{M} E_{\theta}\left(V_{i}, h\right)}
$$

where $\min \left(E_{\theta}\left(V_{i}, h\right)\right)$ represents the minimum value in all of the $E_{\theta}\left(V_{i}, h\right)$.

In addition, because the softmax RBM model is trained by unsupervised learning, the implicit distributed information extracted from the training data is relatively rough at the early stages of the EDA evolutionary process. To better obtain the distributed representative information of the decision variables of the promising solutions, the surrogate model based on the softmax RBM needs to be dynamically updated with the change of the dominant solutions in the evolutionary process.

In this paper, the top $50 \%$ individuals are selected from the current $\operatorname{Sub}(g)$ as the subset $D_{\text {top }}$ by the surrogate model, while the top $50 \%$ individuals are also selected from $\operatorname{Sub}(g)$ as the subset $D_{\text {top }}{ }^{\prime}$ by the real fitness function. The proportional similarity coefficient $\gamma$ defined in (12) is used:

$$
\gamma=\frac{\text { Num }_{\text {intersection }}}{\text { Num }_{\text {real }}}
$$

where Num $_{\text {intersection }}$ is the size of the intersection between $D_{\text {top }}$ and $D_{\text {top }}{ }^{\prime}$; and Num $_{\text {real }}$ is the number of $D_{\text {top }}{ }^{\prime}$.

Accordingly, the $\gamma$ threshold is set to $\gamma_{\text {th }}$. If $\gamma$ is greater than $\gamma_{\text {th }}$, then the surrogate model based on the softmax

```
Begin
Do while (maximum number of training epochs is not reached)
    #Positive Phase
    1. Construct the conditional probability of the hidden units \(p_{\theta}\left(h_{j} \mid V\right)\) given the visible softmax values according to (6)
    2. From \(p_{\theta}\left(h_{j} \mid V\right)\), sample the states of the hidden units \(\left\langle h_{j}\right\rangle_{0}\)
    \#Negative Phase
    3. Construct the conditional probability of the visible softmax units \(p_{\theta}\left(v_{i}^{k} \mid h\right)\) given the states of the hidden units according to (7).
    Reconstruct the states of the visible softmax units \(\left\langle v_{i}\right\rangle_{1}\) by sampling the constructed conditional probability \(p_{\theta}\left(v_{i}^{k} \mid h\right)\)
    4. Construct the conditional probability of the hidden units \(p_{\theta}\left(h_{j} \mid V\right)\) given the sampled visible softmax values according to (6).
    Reconstruct again the states of the hidden units \(\left\langle h_{j}\right\rangle_{1}\) by sampling the constructed conditional probability \(p_{\theta}\left(h_{j} \mid V\right)\)
    \#Updating of weights
    5. Update the weights and biases
End Do
\#Construction of the probability model
6. Calculate the Probability Model \(P(V)\) according to (8).
End
```

Algorithm 1: Pseudocode of the probabilistic modelling.

```
Begin
    1. Initialization: at generation \(g=0\), randomly generate \(M\) candidate solutions to form the initial population \(\operatorname{Pop}(g)\)
Do while (Termination conditions are not met)
2. Evaluation: According to the real fitness function, calculate the individual fitness of all solutions in \(\operatorname{Pop}(g)\), and preserve the best solution in the current population
3. Selection: Select \(S\) better individuals by using the truncation selection strategy and rank in order to form the dominant subset \(\operatorname{Sub}(g)\)
4. Modelling: Train a softmax RBM model based on \(\operatorname{Sub}(g)\), and then build a probability model \(P(V)\) based on the softmax RBM according to (8)
5. Surrogate model: Construct the surrogate model based on the softmax RBM. The \(y\) value is calculated according to (12) to manage the surrogate model, and then the surrogate model estimates the individual fitness according to (10) and (11) to participate in the evolutionary process.
6. Sampling: Produce \((M-S)\) offspring by sampling the probability model \(P(V)\) with roulette sampling according to (9)
7. Updating population: Merge the \((M-S)\) offspring into \(\operatorname{Sub}(g)\) to form the new population \(\operatorname{Pop}(g+1) \cdot g=g+1\)
End Do
End
```

Algorithm 2: Pseudocode of RBMAEDA.

RBM can effectively replace the real fitness function and estimate the individual fitness to guarantee most of better solutions selected from the population. Meanwhile, the estimated individuals in $D_{\text {top }}$ are reevaluated by using the real fitness function. Otherwise, the real fitness function is still used. Subsequently, the better individuals and their real fitness are added to the dominant subset $\operatorname{Sub}(g)$ to replace some worse individuals for updating $\operatorname{Sub}(g)$. Therefore, the model management of the surrogate model based on the softmax RBM guarantees the accuracy and reliability of the individual fitness estimated by the surrogate model, which will dynamically track the feature information of the promising solutions and effectively provide support for guiding the evolutionary optimization progress.
3.4. Implementation of RBM-Assisted EDA. The pseudocode of the proposed RBMAEDA is presented in Algorithm 2.

Along with the softmax RBM training process and the EDA evolutionary progress alternately, the distributed
representative information learned by the softmax RBM sufficiently and accurately represents the probabilistic distribution of the decision variables of the promising solutions at later stages of the evolutionary process. Knowledge of superior solutions effectively and efficiently guides the exploration of the search space and yields the optimization progress by combining evolutionary optimization with machine learning.

## 4. Experiments and Results

In these experiments, the computing platform is Python 3.5 on a Dell computer with an Intel Core i5-4590 CPU 3.30 GHz and 4 GB RAM. To comprehensively analyze the performance of the proposed RBMAEDA, the experiments are tested with a series of benchmark tests [40, 41] shown in Table 1.

All these benchmark problems have continuous functions with discrete variables and different characteristics with discontinuous landscapes (dimensions from 6 to 30). They are all minimization problems. The number of decision

Table 1: Benchmark test problems.
Table 2: Experimental parameters.
variables and other characteristics is presented in Table 1. In this section, we conduct three series of experiments to verify the effectiveness of the probability model based on the softmax RBM, the surrogate model based on the softmax RBM, and the proposed RBMAEDA for complex optimization problems in Subsections 4.1, 4.2, and 4.3, respectively.
4.1. Performance of the Probability Model Based on Softmax RBM. To verify the effectiveness of the probability model based on the softmax RBM, EDA based on the soft$\max$ RBM (denoted by softmaxRBM-EDA) is compared with the traditional EDA and REDA-E [32] with the same common parameters. Three algorithms are different from each other in their different probability model and model updating strategy. The comparative experiments are conducted to evaluate the performance of the three algorithms using 9 benchmark problems in Table 1. In the comparative experiments, 10 independent runs are performed for each algorithm. The experimental parameters are shown in Table 2.

A series of performance indicators, including the average optimal solution, the standard deviation, the success rate, and the search time, are used to measure the performance of each algorithm. These performance indicators in the experiments are described as follows:
(1) Avg. $\pm$ St: the average and standard deviation of the best solutions for 10 trials
(2) Rate (\%): the success rate of reaching the global optimal solution in 10 trials, reflecting the effectiveness of each algorithm
(3) Time (s): the total search time until reaching the best solution, reflecting the efficiency of each algorithm

The comparative experimental results for the three algorithms are shown in Table 3.

By observing the results in Table 3, the following conclusions can be obtained:
(1) The average and standard deviation of the softmaxRBM-EDA are the smallest among the three algorithms in most of the test problems, and the success rate of the softmaxRBM-EDA is the highest among the three algorithms. The traditional EDA and REDA-E have very lower success rate and completely trapped in the local optima for F4 and F5, mainly because this type of problems has very rugged landscapes and obtains the optimal solutions at nonzero point. In particular, note that Rosenbrock function is a multimodal problem with narrow valley. EDA and REDA-E have never reached the global optimal solution for F5 in the 10 independent executions, so they are not appropriate for handling these multimodal problems with the very rugged landscapes or the narrow valley. However, softmaxRBM-EDA can be better able to solve this kind of problems
(2) SoftmaxRBM-EDA shows a substantial improvement of solution quality and searching efficiency for those very challenging problems in terms of the very rugged landscapes and the narrowness of the optimal valley. Specifically, the softmaxRBM-EDA performed 122 iterations (approximately 153.50 s ) on average to obtain the best solution with an average of 7.40 and a standard deviation of 16.94 and had an $80 \%$ success rate in reaching the global optimum for F4. EDA executed approximately 27 iterations (approximately 2.77 s ) on average and reached the local optimal solution with an average of 9.0 and a standard deviation of 1.94 , which had not reached the global optimum for F4 even once. REDA-E performed 87 iterations (approximately 177.51 s ) on average and obtained the optimal solution with only $40 \%$ success rate for F4, which had an average of 21.0 and a standard deviation of 20.73
(3) Regarding the search time, softmaxRBM-EDA is faster than REDA-E but slower than EDA for those problems partly because it spends time extracting the feature information to construct the probability model based on the RBM for guiding the evolutionary progress. However, softmaxRBM-EDA does not cause too much computational burden. That computational cost is deserved for jumping out of the local optima and achieving the global optima. In addition, the probability model based on statistics in EDA does not contribute to design the appropriate surrogate model in the EDA framework

In summary, the proposed softmaxRBM-EDA improves the quality of the best solutions and the efficiency of

Table 3: Comparative experimental results.

searching process and outperforms the other algorithms for complex problems with discontinuous landscapes. It is mainly because the probability model based on the softmax RBM in softmaxRBM-EDA can extract the distributed representative information of the decision variables of the promising solutions to participate in the evolutionary process. Then, softmaxRBM-EDA can generate new solutions with the gene information of the better solutions by sampling the probability model based on the softmax RBM. Furthermore, with the increase of solutions, the probability model based on the softmax RBM will be updated by the increasing feature information of the promising solutions to continually optimize the candidate solutions and comprehensively guide the evolutionary progress. SoftmaxRBMEDA enhances the exploration and exploitation abilities to adaptively adjust the optimal direction for the solution quality and the population diversity. Therefore, softmaxRBM-EDA has the better solution quality, convergence rate, and stability for complex problems. For dynamically illustrating the evolutionary progress, the iteration evolutionary processes of the EDA, REDA-E, and softmaxRBM-EDA approaches are presented for solving F1, F4, F5, and F8 test problems. For the fairness of the comparative experiments, each algorithm will be executed and evolved sufficiently. The convergence profiles of the three algorithms for F1, F4, F5, and F8 are plotted in Figure 4.

In Figure 4, the horizontal coordinates indicate the number of iterations, and the vertical coordinates indicate the fitness of the best solution for each generation. As can be seen from Figure 4, EDA can reach the global optima of F4 and F5 along with the evolutionary progress, and REDA-E does not succeed in obtaining the global optima of F1, F5, and F8, falling into the local optima. Accordingly, softmaxRBM-EDA has achieved the best solutions for all of the problems. Although REDA-E requires less iterations than softmaxRBM-EDA to reach the final solutions, REDA-E spends much more search time in each generation and has more total time than softmaxRBM-EDA. The main reason is that the computational cost for sampling mechanism and training RBM in REDA-E is too large with increasing dimensions. Nevertheless, softmaxRBM-EDA emphasizes the exploitation of the promising regions and offers a predictive guidance on the exploration of optimal solutions. It is verified that the probability model based on
the softmax RBM is feasible and effective as a probability model of EDA in softmaxRBM-EDA for solving complex optimization problems. Therefore, softmaxRBM-EDA performs more effectively and efficiently than the other algorithms in most of the test problems.
4.2. Performance of the Surrogate Model Based on Softmax $R B M$. In this subsection, investigations are carried out to analyze the proposed surrogate model based on the softmax RBM in RBMAEDA. If the relative order relationship of the dominant individuals can be guaranteed during the surrogate model used in EDA, the individual selection based on the surrogate model and the updating of the probabilistic model will not have harmful effect on the evolutionary progress. So we can consider that the surrogate model in EDA is feasible and effective. In this experiment, one evolutionary process of RBMAEDA for the Griewank function with 10 dimensions is recorded, and the results show that RBMAEDA finds the optimal solution in the 11th generation, where $\gamma_{\text {th }}=0.6$. The real individual fitness and the estimated individual fitness of the dominant subset $\operatorname{Sub}(g)$ will be calculated for comparison in RBMAEDA and are shown at the 2nd, 3rd, and 7 th generations in Figure 5.

In Figure 5, the horizontal coordinate indicates the index of individuals, and the vertical coordinate indicates the real individual fitness and the estimated individual fitness. Figure 5 shows that the individual fitness estimated by the surrogate model based on the softmax RBM can mainly follow the trajectory of the real individual fitness. Meanwhile, the threshold of the proportional similarity coefficient $\gamma_{\text {th }}=$ 0.6 means that $60 \%$ better solutions of $\operatorname{Sub}(g)$ can be selected by the surrogate model. The surrogate model and the real fitness function have high similarity ranking in individual evaluation, so the relative rank of individuals in $\operatorname{Sub}(g)$ can be generally represented by the surrogate model based on the softmax RBM. Therefore, it is feasible and effective to estimate the individual fitness by the surrogate model based on the softmax RBM in RBMAEDA.
4.3. Performance of the RBMAEDA. To illustrate the performance of the proposed RBMAEDA, RBMAEDA is compared with the committee-based active learning for surrogateassisted particle swarm optimization (CAL-SAPSO) algorithm [17] presented in 2017 on a series of benchmark

![img-3.jpeg](img-3.jpeg)

Figure 4: Comparative results of the EDA, REDA-E, and SoftmaxRBM-EDA.
problems for a limited computation budget. The comparison algorithm is an algorithm with outstanding performance at present, using the same comparison function to compare with the results provided in [17]. In the experiment, the average value and the standard deviation in 10 trials are used to measure the performance of these algorithms. The experimental results on benchmark problems of different dimensions are presented in Table 4.

As shown in Table 4, the following conclusions can be obtained:
(1) RBMAEDA outperforms the CAL-SAPSO algorithm on most of the test problems. Furthermore, with the increase of the dimension of those problems, RBMAEDA has still the stable average values of the final solutions to reach close to the optima. For example, the average value and the standard deviation of RBMAEDA are $1.0 E-01 \pm 3.16 E-01$ for the 10 dimension Rastrigin, while those of the 20 - and 30 dimension Rastrigin are $5.0 E-01 \pm 8.50 E-01$ and $4.0 E-01 \pm 6.99 E-01$, respectively
(2) However, RBMAEDA performs worse than CALSAPSO on the Rosenbrock function. The main reason is that Rosenbrock function has a very narrow
and deep peak of the fitness landscape around the global optimum. In addition, the CAL-SAPSO algorithm can deal with computationally expensive optimization problems with continuous variables, which will help CAL-SAPSO reach closer to the optimum. Nevertheless, RBMAEDA is specially designed for computationally expensive optimization problems with discrete variables, for which it is more difficult to find the optimum

The experimental results demonstrate the advantages of RBMAEDA over the compared algorithm on the benchmark problems with different dimensions. Therefore, RBMAEDA can effectively solve medium-scale complex computationally expensive optimization problems with discrete variables.

To further verify the performance of the RBMAEDA, RBMAEDA is compared with two popular SAEAs, the SMAS algorithm [18] and the SMDN algorithm [19] presented in 2016, on a series of benchmark problems with a limited computation budget. In particular, the SMDN algorithm is a state-of-the-art algorithm for complex computationally expensive optimization problems with discrete variables, using the same comparison function to compare with the results provided in [19]. In the experiment, three indicators are used to measure the performance of these algorithms:

![img-4.jpeg](img-4.jpeg)

Figure 5: Comparative results of the real individual fitness and the estimated individual fitness.
the average value, the standard deviation, and the success rate in the 10 trials. The experimental results for benchmark problems of different dimensions are presented in Table 5.

By observing the results in Table 5, the following conclusions can be obtained:
(1) RBMAEDA outperforms the other algorithms on most of the test problems. For example, RBMAEDA has the highest success rate in reaching optimality for the Rastrigin function and the Griewank function in three algorithms, and RBMAEDA has the best average value and the lowest standard deviation for those problems in three algorithms. The average values of the final solutions are also stable and close to the optimal of those problems
(2) RBMAEDA has a relative lower success rate for the Rosenbrock function. It is mainly because that the Rosenbrock function has the very narrow valley of the fitness landscape, which enhances the difficulty of complex optimization problems with discrete variables in the searching process
(3) With the increase of the dimension of these problems, RBMAEDA is still able to obtain comparable high quality solutions with a limited budget of FEs, but the success rate is gradually declining. The main reason is that the computational cost and complexity for training the softmax RBM model in RBMAEDA will increase with the dimension increasing of the problems, which leads to some trouble for the surrogate to learn the fitness landscape and estimate the individual fitness in the evolutionary process

In summary, the proposed RBMAEDA utilizes the probability model based on the softmax RBM and the surrogate model based on the softmax RBM, which makes full use of the knowledge and information of the promising solutions, to enhance the exploration and exploitation abilities in the evolutionary process. Meanwhile, RBMAEDA performs well on unimodal and multimodal problems or problems with the rugged landscapes by using a limited computing budget when the number of decision variables changes from 5 to 30 . For these problems, RBMAEDA only consumes about $20 \%$ to $40 \%$ of the number of FEs of

Table 4: Experimental results comparing with CAL-SAPSO.
Table 5: Experimental results comparing with SMAS and SMDN.

softmaxRBM-EDA to get comparable high quality solutions. Furthermore, RBMAEDA has a better solution quality, stability, convergence rate, and scalability for solving computationally expensive optimization problems with complex discontinuous landscapes.

## 5. Conclusions

In this paper, a novel RBMAEDA algorithm is proposed to solve complex computationally expensive optimization problems with discrete variables. The RBM probability model and its dynamic updating mechanism take full advantage of the feature information of the better solutions to guide the evolutionary progress. In addition, the surrogate model based on the RBM and model management are adopted to replace FEs, which enhances the searching efficiency and reduces the computational cost. The experimental results demonstrate that the proposed RBMAEDA outperforms other algorithms for most of the test problems and is effective to deal with complex computationally expensive optimization problems. These researches will further deepen and enrich the theoretical research and practical application of SAEAs. For future investigations, there is considerable development
potential in the combination of deep learning and intelligent optimization algorithms to solve complex problems.

## Data Availability

The data used to support the findings of this study are included within the article.

## Conflicts of Interest

The authors declare that they have no conflicts of interest.

## Acknowledgments

This work was jointly supported by the National Natural Science Foundation of China under grant no. 61473298 and no. 61473299 .
