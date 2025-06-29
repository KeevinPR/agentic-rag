# Random mask-based estimation of the distribution algorithm for stacked auto-encoder one-step pre-training 

Qingyang Xu ${ }^{\mathrm{a}, *}$, Anbang Liu ${ }^{\mathrm{a}}$, Xianfeng Yuan ${ }^{\mathrm{a}}$, Yong Song ${ }^{\mathrm{a}}$, Chengjin Zhang ${ }^{\mathrm{a}}$, Yibin $\mathrm{Li}^{\mathrm{b}}$<br>${ }^{a}$ School of Mechanical, Electrica \& Information Engineering, Shandong University, Shandong 264209, China<br>${ }^{\mathrm{b}}$ School of Control Science and Engineering, Shandong University, Shandong 250100, China

## A R TICLE INFO

Keywords:
Deep neural network
Stacked auto-encoder
Estimation of distribution algorithm
Random mask
One-step pre-training

A B STR A C T

The deep learning techniques have received great achievements in computer vision, natural language processing, etc. The success of deep neural networks depends on the sufficient training of parameters. The traditional way of neural network training is a gradient-based algorithm, which suffers the disadvantage of gradient disappearing, especially for the deeper neural network. Recently, a heuristic algorithm has been proposed for deeper neural network optimization. In this paper, a random mask and elitism univariate continuous estimation of distribution algorithm based on the Gaussian model is proposed to pre-train staked auto-encoder, and then a Stochastic Gradient Descent (SGD) based fine-tuning process is carried out for local searching. In the improved estimation of the distribution algorithm, two individual update strategies are defined; one group of individuals is generated according to the constructed probabilistic model, and another is updated according to the statistics of advanced individuals that aim to reduce the probability of combination explosion and time consumption according to the mask information. In the simulations, different architectures, different mask ratios and different promising individual ratios are adopted to testify the effectiveness of the improved algorithm. According to simulation results, the estimation of thr distribution algorithm has a steady optimization ability for the shallow and stacked autoencoder by one-step pre-training combining SGD based fine-tuning for the MNIST dataset. The proposed model will achieve a state-of-the-art performance on Fashion-MNIST.

## 1. Introduction

Artificial intelligence (AI) has developed fast recently, driven by deep learning technology. Deep learning is an extension of the classic Artificial Neural Network that takes advantage of the current computational capability of the computer as well as the big data technology. Deep Neural Network (DNN), which is a nonconvex model, has become a powerful and extremely popular technique widely used for various nonlinear problems, such as computer vision and image recognition (LeCun et al., 2015), time series forecasting (Kuremoto et al., 2014; Wang et al., 2017) and video recognition (Martín et al., 2018). Back-propagation algorithm is widely used in neural network training, which relies on gradient information. It is effective for the shallow neural network. However, the gradient-based algorithms have several limitations, i.e., the algorithms suffer from gradient disappearing, easily affected by the initial hyper-parameters and easily trapped in local optima (Ye, 2017). Some improved algorithms are proposed, such as Stochastic Gradient Descent (SGD), AdaGrad, RMSProp, AdaDelta, etc. Hinton (Hinton and

Salakhutdinov, 2006) proposed that with the pre-training technique, a deep neural network can be trained better based on the current and follow-up research. However, it is also based on the gradient algorithm, and the pre-training strategy only provides a better initial weight of deep architectures.

The successful applications of deep neural networks drive researchers to develop new methods and tools for parameters and architecture optimization. The topologies and training hyper-parameters are traditionally solved by manual initialization and the weights are trained by the gradient methodology. The training of deep neural networks depends crucially on the specifications of hyper-parameters, such as architecture, learning rate, regularization parameter, weight and many others (Hinz et al., 2018). The parameter optimization of a deep neural network can be described as an Eq. (1).
$\mathrm{A}=\arg \min _{m_{n, \mathrm{~A}, \mathrm{c}}}\left(m_{n, \mathrm{~A}, \mathrm{c}}\right)+R(w)$
where A is an optimal deep neural network, $m_{n, \mathrm{~A}, \mathrm{w}}$ is the set of general

[^0]
[^0]:    ${ }^{\text {a }}$ Corresponding author.
    E-mail address: qingyangxu@sdu.edu.cn (Q. Xu).

Table 1
Different heuristic algorithm-based deep neural network optimization.
deep neural networks, $\alpha$ is hyper-parameter of training, $\Lambda$ is the architecture of a deep neural network, $w$ is the weight and $R(w)$ is regularization term. $L()$ is a loss function which is negative cross-entropy for classification problem. Therefore, the optimization of deep neural networks completely or partially includes $\alpha, \Lambda, w$ optimization, which is a large-scale optimization problem.

Some recent results indicate that some automated approaches can find better hyper-parameters and achieve better results than humans (Assunção et al., 2019, Junior and Yen, 2019, Bergstra and Bengio, 2012, Sun et al., 2019, Zhang et al., 2019; , 2020). However, it is a challenging work for large-scale weight optimization, resulting in highdimensional searching space. Estimation of distribution algorithm is a kind of evolutionary algorithm. Although there are some researches about higher dimensional problems optimization based on estimation of distribution algorithm, the scale of the problem is limited and doesn't reach the scale of deep neural network's parameters. However, the global optimization capability of estimation of distribution algorithm is in accordance with the concept of Hinton's layer-wise pre-training. Therefore, we proposed an estimation of the distribution algorithm based on the deep neural network weights training algorithm. In order to improve the large-scale optimization capability of estimation of distribution algorithm, a random strategy is introduced into the estimation of the distribution algorithm, and the individuals of estimation of distribution algorithm are updated by two strategies which may speed up the training and reduce the combinational explosion probability. The largescale optimization capability of estimation of distribution algorithm is enhanced. A comparison between the two steps (layer by layer) and onestep (pre-training all of the hidden layers) pre-training is done in the experiments, and the one-step pre-training is proved as effective and convenient for stacked auto-encoder pre-training based on the improved estimation of distribution algorithm. After the one-step pre-training, a fine-tuning process is carried out for local optimization. Compared with state-of-the-art results, the proposed algorithm is promising.

The rest of this paper is organized as follows: A literature review is presented in Section 2. The stacked auto-encoder is presented in Section 3. The proposed algorithm is described in Section 4. The experimental design is presented in Section 5. Finally, Section 6 presented the conclusion.

## 2. Literature review

Grid search and random search are two of the most widely-used approaches in parameter optimization (Ma et al., 2020). In grid search, a pre-determined range of hyper-parameters is defined to construct every possible combination of hyper-parameter. However, the grid grows exponentially with the number of parameters. On the other
hand, random search generates a random value from a pre-defined distribution of the parameter. Bergstra and Bengio (Ma et al., 2020) show that random search performs almost or equally well as the grid search empirically in higher dimensional spaces and is much quicker. Heuristic methods are also introduced for parameter optimization (Guo et al., 2020; Oong and Isa, 2011). Evolutionary algorithms (EAs) have good global search capabilities that are likely to provide the most promising solution, especially for nonconvex problems (Al-Dabbagh et al., 2015, Al-Dabbagh et al., 2015, Yao and Liu, 1997, Hussain et al., 2019, Lv et al., 2019, Hu and Yang, 2019, Wu et al., 2020, Wu et al., 2016, Wu et al., 2016, Wu et al., 2018, Cheng et al., 2020, Stanley and Miikkulainen, 2002). Table 1 is the deep neural network optimization approaches based on EA recently. According to Table 1, the studies mostly aim to evolve the topologies of the deep neural network due to the challenges of determining its complexity. The topologies of artificial neural networks are encoded as a chromosome in the evolutionary algorithm, and then some operators are adopted for evolution. Therefore, the choice of variable is defined by some common or hand-crafted architectures, such as convolution, pooling, skip connections, etc. However, the optimization of weights is always based on a gradient algorithm due to the scale of the problem.

According to Table 1, these researches are almost based on a genetic algorithm, which makes use of various kinds of operators, such as selection, crossover, and mutation, to produce offspring. The population modeling-based evolutionary algorithms are rarely seen in Table 1, such as estimation of distribution algorithms (Dong et al., 2013), which makes use of promising individuals from the current population to construct a probabilistic model (instead of using crossover or mutation operators) for offspring generation. Genetic algorithms allow a direct operation of individuals and obtain the gene of the best solutions found so far, whereas the estimation of distribution algorithms have indirect operations of offspring that make use of the probabilistic model as guidance for population reproduction to find better solutions (Sun et al., 2020). This operation grasps the trend of population evolution. The estimation of distribution algorithms has been shown to experimentally outperform other existing algorithms on many benchmarks and has been applied to various fields (Wang et al., 2015, Pérez-Rodríguez and Hernández-Aguirre, 2019, Arin and Rabadi, 2017, Wang et al., 2012, Chen et al., 2010). The performance of estimation of distribution algorithm depends on how well is the probabilistic model learned (Mishra and Gallagher, 2014). However, there were experimental observations that estimation of distribution algorithms did not scale well to largescale problems since probabilistic model construction is the foundation of estimation of distribution algorithms. As the truncation selection is always adopted in the estimation of distribution algorithms (Hansen and Ostermeier, 2001), they must suffer from the well-known curse of

dimensionality (Sun et al., 2020). According to the curse of dimensionality theory, the quantity of data will increase exponentially with the dimensionality of search space in order to maintain a proper spatial density. The estimation of distribution algorithms tries to learn the global statistical information from some promising samples. Therefore, the population size of estimation of distribution algorithms has to grow quickly with the problem size in order to maintain a good performance. This is a challenge for the large-scale problem and optimal probabilistic model learning, such as weights of deep neural networks. Therefore, the performance of estimation of distribution algorithm on higher dimensional problems (e.g., 500-D) is rarely studied (Sun et al., 2020). There have been only a few attempts on large-scale ( $\geq 500-\mathrm{D}$ ) problems. Gaussian model suffers less from the curse of dimensionality than the histogram model, because the Gaussian model usually has fewer degrees of freedom. CMA-ES (Wang et al., 2008) adopted a covariance matrix adaptation (CMA) for population generation. The diagonal covariance matrix relies on the cumulation of the evolutional population, which can reduce the population size. Wang and Li (Bielza et al., 2009) proposed a univariate model-based estimation of distribution algorithm LSEDA-gI for large-scale optimization benchmarks. Mixed Gaussian and Levy probability distribution, standard deviation control strategy and restart strategy were adopted for sampling. However, the general performance of broader types of high-dimensional problems is still unknown. Bielza et al. (Karshenas et al., 2013) made use of larger genes and smaller samples for the classification problem using logistic regression regularizers. In ref. (Bosman, 2009), regularization techniques were introduced into the estimation of the distribution algorithm, which displayed the ability to solve high dimensional problems with a comparable quality of solutions and a smaller population. Bosman (Kabán et al., 2016) proposed a Gaussian estimation of distribution algorithm AMaLGaM which was used for 1000-D problems, and the memory techniques were adopted. EDA Model Complexity Control EDA-MCC (Sun et al., 2020) is the first attempt at scaling up the multivariate model-based estimation of distribution algorithm for large-scale continuous optimization (up to 500-D problems) by weakly dependent variable identification and subspace modeling. RP-EDA (Omidvar et al., 2017), assemble random projection to the estimation of distribution algorithm to find approximate solutions, generate a random projection matrix and project the center point into k dimensions to estimate the $\mathrm{k}^{*} \mathrm{k}$ sample covariance for new sample generation. DECC-DG (Hauschild and Pelikan, 2011) adopted differential grouping decomposition for largescale global optimization problems, which is a type of Cooperative Coevolution approach, and DG2 found a reliable threshold value by estimating the magnitude of round off errors, reused the sample points detecting interactions, and saved up to half of the computational resources on fully separable functions. However, the general performance of these studies on large-scale problems is still unknown, such as for the 10,000-D, 100,000-D and 1,000,000-D.

We built upon the univariate model-based estimation of the distribution algorithm, and incorporated the random strategy for the population updating, which is used for deep neural network weights optimization. The population updating strategy aims to improve the optimization efficiency and reduce the probability of a combinational explosion. In summary, the contribution of this paper is as following: (1) the proposed model in this study is used for deep neural network weight optimization which is a huge large-scale optimization problem; (2) compared with the existing estimation of distribution algorithm, the proposed model makes use of random updating strategy for population generation; (3) based on the proposed model, the one-step pre-training strategy is effective for the deep neural network pretraining.

## 3. Stacked Auto-encoder

Hinton proposed the layer-wised weight initialization method to gather a rough region of the weight, and then a fine-tuning process is carried out to search the solution accurately. If the initial weights are
![img-0.jpeg](img-0.jpeg)

Fig. 1. Diagram of the Auto-encoder.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Principle of stacked auto-encoder training.
close to a good solution, the gradient descent algorithm works well. Auto-encoder is a simple network for deep neural network pre-training. It is exemplified in Fig. 1.

The auto-encoder takes an input $x \in R^{d}$ and maps it to a latent representation space $h \in R^{c}$ by a single-layer neural network. The encoder transforms input $x$ into latent representation $h$ by equation (2):
$h=\sigma(W X)$
where $W$ is the weight matrix between input and output neurons and $\sigma$ is a sigmoid function.

For the decoding procedure, the hidden representation $h$ is then mapped back to a reconstructed vector $y$ by $g(h)=\sigma(W h)$. This affine mapping is called a decoder. In general, $y$ is not to be interpreted as an exact reconstruction of $x$, but rather in probabilistic terms, as the parameter of a distribution $p(X \mid Y=y)$ that may generate $x$ with high probability.

The deep neural network has an input layer, two or more hidden layers, and an output layer. The hidden layers can be pre-trained in an unsupervised way using an auto-encoder, starting from the first hidden layer, and then going layer by layer. Once a given auto-encoder has been trained to reconstruct the input successfully, the output layer is no longer needed and the corresponding hidden layer becomes the input layer of the next hidden one as shown in formula (3). The next hidden layer is also pre-trained as an independent auto-encoder, and the process is repeated until there are no more hidden layers. The clf() is the classification function, such as Softmax. This is also called a stacked autoencoder as shown in Fig. 2.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Diagram of stacked auto-encoder optimization by EDA.

$$
\left\{\begin{array}{l}
h_{1}=f\left(W_{1} X\right) \\
h_{2}=f\left(W_{2} h_{1}\right) \\
\cdots \\
h_{i}=f\left(W_{i} h_{i-1}\right) \\
h_{n}=f\left(W_{n} h_{n-1}\right) \\
o=c l f\left(h_{n}\right)
\end{array}\right.
$$

The goal of unsupervised pre-training is to initialize the weights to a better region of parameter space than random initialization. Once a stacked auto-encoder has been built, the final hidden layer output representation can be used as input of a stand-alone supervised learning algorithm, for example, a Support Vector Machine classifier, a Softmax classifier, or a (multi-class) logistic regression. In this context, a subsequent supervised training process called fine-tuning can be achieved by conventional gradient descent. The classical squared error (MSE) loss function is used to minimize the error of practical output and target output as equation (4).
$M S E=\frac{1}{n} \sum(x-y)^{2}$
In addition, some regularization terms can be adopted. Thus, the loss function turns out to be as shown in equation (5).
$L=\frac{1}{n} \sum(x-y)^{2}+\beta \sum \operatorname{Sparse}\left(\rho \mid \hat{\rho}\right)+\lambda \sum W^{2}$
$\operatorname{Sparse}(\rho \mid \hat{\rho})=\rho \log \frac{\rho}{\hat{\rho}}+(1-\rho) \log \frac{1-\rho}{1-\hat{\rho}}$
where $\operatorname{Sparse}(\rho \mid \hat{\rho})$ is a sparse penalty term, $\hat{\rho}$ is average activation of hidden unit, $\rho$ is a sparsity value, and $\beta$ is the weight of sparsity penalty term. $\lambda$ is the coefficient of weight regularization. The pseudocode of auto-encoder training is shown in algorithm 1.

```
Algorithm 1: Pseudocode of auto-encoder training
Initialization: Input data \(x\), the labels \(t\), and other hyper parameters.
    Pre-training:
    Create the first auto-encoder \(\boldsymbol{A} \boldsymbol{E}^{1}\) with the input layer and the first hidden layer
    Train \(\boldsymbol{A} \boldsymbol{E}^{1}\) by input data \(x\) and the reconstructed datay
    Finish pre-training the first hidden layer
```

(continued on next column)
(continued)

```
Algorithm 1: Pseudocode of auto-encoder training
    Pre-train the remaining hidden layer
    Fine-tuning:
    Add the output layer
    Train stack \(\boldsymbol{A} \boldsymbol{E}\) by backpropagation according to \(\boldsymbol{E}=\frac{1}{n} \sum(\boldsymbol{x}-\boldsymbol{t})^{2}\)
```


## 4. Improved EDA based pre-training for stacked auto-encoder

For estimation of distribution algorithm based stacked auto-encoder training, the weight of the neural network is encoded as an individual of estimation of distribution algorithm. The statistical information of each weight can be calculated to construct a probabilistic model according to the advanced individual. Then, the new individuals are generated by probabilistic model sampling. Finally, the pre-trained parameters can be obtained for the stacked auto-encoder. The diagram of optimization is shown in Fig. 3.

### 4.1. Estimation of distribution algorithm

Estimation of distribution algorithm is a kind of evolutionary algorithm based on population modeling. The central idea of estimation of distribution algorithm is to maintain an explicit probabilistic model to represent the distribution and subsequent generation of better candidate solutions, at the next step by probabilistic sampling (Li et al., 2012). A typical estimation of distribution algorithm pseudo code is shown in algorithm 2 .

```
Algorithm 2: Pseudocode of traditional estimation of distribution algorithm
    Initialization: Set iteration \(=0\), generate initial population
    Evaluation: Evaluate objective function \(\boldsymbol{E}(\boldsymbol{x})\) for individuals
    Selection: Select promising individuals
    Modeling: Build probabilistic model \(\boldsymbol{P}(\boldsymbol{x})\) based on promising individuals
    New population generation: Generate new population by sampling \(\boldsymbol{P}(\boldsymbol{x})\)
    Iteration \(=\) Iteration +1
    Go to step 2 until a stopping criterion
```

$N$ represents the population size, and $B N$ is number of promising individuals. The initial population of estimation of distribution algorithm is always initialized with a random variable $z_{i} \in\left|a_{i}, b_{i}\right|$ as shown in equation (7).
$x_{i}^{\mathrm{a}}=L_{i}+\frac{H_{i}-L_{i}}{b_{i}-a_{i}}\left(z_{i}-a_{i}\right)$
where $x_{n}^{i}$ is $i$-th variable of $n$-th individual, $z_{i}$ is a random variable, $a_{i}$ and $b_{i}$ are the bounds of $i$-th random variable, $L_{i}$ and $H_{i}$ are the bounds of $i$-th optimized variable.

The most important and crucial step of estimation of distribution algorithm is to construct a probabilistic model of an optimized variable. However, for the large-scale optimization problem, the computational cost of the multivariable joint probabilistic model is too high for the large-scale optimized variables and numerous individuals for each variable (Ahmed et al., 2018; Lu et al., 2019). The univariate model supposes that the variables have independent and identically distribution, and obey normal distribution. The probabilistic model of individuals for the estimation of distribution algorithm $P\left(x_{1}, x_{2}, \cdots x_{D}\right)$ is as following:
$P\left(x_{1}, x_{2}, \cdots x_{D}\right)=\prod^{D} N\left(x_{i} \mid \mu_{i}, \sigma_{i}\right)$
$\left(x_{1}, x_{2}, \cdots x_{D}\right)$ are variables to be solved, $\mu_{i}$ and $\sigma_{i}$ are the mean and standard deviation of $i$-th variable, $N\left(x_{i} \mid \mu_{i}, \sigma_{i}\right)$ is normal probabilistic distribution model as following:
$N\left(x_{i} \mid \mu_{i}, \sigma_{i}\right)=\frac{1}{\sigma_{i} \sqrt{2 \pi}} e^{-\frac{\left(x_{i}-x_{i}\right)^{2}}{2 \sigma_{i}^{2}}}$

![img-3.jpeg](img-3.jpeg)

Fig. 4. Flowchart of improved EDA.
$P\left(x_{1}, x_{2}, \cdots x_{D}\right)$ can be described further as shown in equation (10).
$P\left(x_{1}, x_{2}, \cdots x_{D}\right)=\prod_{i=1}^{D} \frac{1}{\sigma_{i} \sqrt{2 \pi}} \frac{\left(x_{i}-x_{2}\right)^{T}}{\sum_{i}^{D}}$
$\left(\mu_{i}, \sigma_{i}\right)$ can be computed in a common way as follows:
$\mu_{i}=\frac{1}{B N} \sum_{n=1}^{B N} x_{i}^{n}$
$\sigma_{i}^{2}=\frac{1}{B N} \sum_{n=1}^{B N}\left(x_{i}^{n}-\mu_{i}(k)\right)\left(x_{i}^{n}-\mu_{i}\right)^{T}$
where $B N$ is the number of promising individuals, and $n$ is the promising individual. At the final stage, the new population can be generated by sampling the model $P(x)$.

### 4.2. Improved estimation of distribution algorithm

### 4.2.1. Random mask strategy

For traditional univariate estimation of distribution algorithms, the new population is completely generated by sampling the probabilistic model of the corresponding variable. Therefore, the optimal solution is the combination of the optimum value of each variable, which is a continuous process (Srivastava et al., 2014). However, for a large-scale optimization problem, huge time consumption and combinatorial explosion maybe occur. Therefore, it is a challenge for traditional estimation of distribution algorithms. Kabán et al. (Omidvar et al., 2017) introduced random projections and a low dimensional fittest solution strategy to improve the large-scale optimization capability of estimation of the distribution algorithm. Moreover, inspired by the theory of dropout (Ahn and Ramakrishna, 2003), which deactivates neurons in
![img-4.jpeg](img-4.jpeg)

Fig. 5. Diagram of individual updating.
the output layer of a neural network, a different individual updating strategy is adopted for variables. In this way, the problem of huge time consumption and combinatorial explosion can be reduced. The flowchart of the proposed estimation of the distribution algorithm is shown in Fig. 4.

According to the flowchart of the improved estimation of distribution algorithm, individual updating is different from the traditional estimation of distribution algorithm. For this improvement, two variable updating strategies are proposed. Firstly, a mask vector is generated randomly within the number of variables, which is used to divide the variables set into $M$ and $\bar{M}$ as reference for variable updating. $M$ is defined according to the mask vector which is an integer set corresponding to the index of variables. Other variables outside of set $M$ are defined as set $\bar{M}$.
$P= \begin{cases}P_{i}(k) & x_{i} \in M \\ P_{i}(k-1) & x_{i} \in \bar{M}\end{cases}$
where $k$ is current iteration steps, $x_{i}(k)$ is $i$-th variable of individuals, $P_{i}(k)$ is the new probabilistic model of variable $x_{i}$ which is updated by current promising individuals as equation (14), and $P_{i}(k-1)$ is the previous probabilistic model of variable $x_{i}$.
$P_{i}(k)=\frac{1}{\sigma_{i}(k) \sqrt{2 \pi}} e^{-\frac{\left(\text { a } x_{i}-\mu_{i}\right)^{2}}{2\left(\sigma_{i}^{2}\right)^{2}}}$
The new population is generated by sampling the new probabilistic model partially, and others are replaced by the statistical value of promising individuals' variable as shown in formula (15).
$x_{i}^{n}(k)= \begin{cases}\operatorname{Sam}\left(P_{i}^{n}(k)\right) & x_{i} \in M \\ \mu_{i} & x_{i} \in \bar{M}\end{cases}$
$x_{i}^{n}(k)$ is $i$-th variable of $n$-th individual, $\mu_{i}$ is mean value of promising individual of $i$-th variable, $\operatorname{Sam}_{i}^{n}$ is a sampling function. The diagram of individual updating is shown as Fig. 5, and the pseudocode of improved estimation of distribution algorithm is shown in algorithm 3 .

```
Algorithm 3: Improved estimation of distribution algorithm
    Initialization: Set iteration \(=0\), generate initial population
    Evaluation: Evaluate objective function \(\boldsymbol{E}(\boldsymbol{x})\) for individuals
    Selection: Select promising individuals and construct an elite set
    1. Calculation: Calculate the statistical information \(\left(\boldsymbol{a}_{i}, \boldsymbol{\sigma}_{i}\right)\) of promising individuals
    \(\boldsymbol{P}_{i}=\frac{1}{B N} \sum_{k=1}^{B N} \frac{\boldsymbol{p}_{i}^{n} \boldsymbol{\sigma}_{i}^{2}}{\sigma_{i}^{2}}-\frac{1}{B N} \sum_{k=1}^{B N}\left(x_{i}^{n}-\mu_{i}(k)\right)\left(x_{i}^{n}-\mu_{i}\right)^{T}\)
    2. Mask vector: Generate random vector randomly, and define \(M\) and \(\bar{M}\) set
    3. Probabilistic model updating: Update probabilistic model \(P(x)\) by different
        strategies according to \(M\) and \(\bar{M}\) set
    \(P=\left\{\begin{array}{c}
P_{i}(k) \\
P_{i}(k-1) \\
\boldsymbol{x}_{i} \in \overline{\mathbf{M}}
\end{array}\right.\)
    4. New population generation: Generate new population by different strategies
```

(continued on next page)

![img-5.jpeg](img-5.jpeg)

Fig. 6. Sample of MNIST and Fashion-MNIST.
(continued)

```
Algorithm 3: Improved estimation of distribution algorithm
\(z_{i}^{\alpha}(\boldsymbol{k})=\left\{\begin{array}{c}\operatorname{Sum}\left(\boldsymbol{P}_{i}^{\alpha}(\boldsymbol{k})\right) \\ \boldsymbol{p}_{i} \in \mathbf{M} \\ \boldsymbol{x}_{i} \in \overline{\mathbf{M}}\end{array}\right.\)
5. Elite maintaining
6. Iteration \(=\) Iteration +1
Go to step 2 until a stopping criterion (such as max iteration steps)
```


### 4.2.2. Random mask strategy analysis

The weight optimization of stacked auto-encoder can be described as the minimization of energy function $L$.
$\Lambda_{\alpha}=\underset{\alpha}{\operatorname{argmin}} L\left(\Lambda_{\alpha}\right)$
where $\boldsymbol{w}$ is the weight of stacked auto-encoder, $\Lambda$ is the neural network, and $L$ is the energy function.

Supposing $X$ is the input of a certain layer, and $W$ is the weight of the hidden layer, Net, is the sum of hidden layer input and $f$ is the activation function. Therefore, the output of $L$-th layer and $i$-th neuron can be defined as follows:
$a_{i}^{L}=f\left(\right.$ Net $\left._{i}\right)$
Net $_{i}=g_{c}(W)=W X$
where,
$W=\left(\begin{array}{ccc}w_{11} & \cdots & w_{3 m} \\ \vdots & \ddots & \vdots \\ w_{n 1} & \cdots & w_{n m}\end{array}\right)$
For the weight optimization problem, variable $W$ is the optimization parameters and $X$ is the given data.

According to the assumption of estimation of distribution algorithm, $w_{\mathrm{ij}}$ obeys normal distribution. Therefore, Net ${ }_{i}$ can be described as Eq. (20).
$N e t_{i}=\left[\begin{array}{c}N e t_{1} \\ \vdots \\ N e t_{n}\end{array}\right]=\left[\begin{array}{c}\sum_{i=1}^{m} w_{1 i} * x_{i} \\ \vdots \\ \sum_{i=1}^{m} w_{n i} * x_{i}\end{array}\right]\left[\begin{array}{c}N\left(\sum_{i=1}^{m} \mu_{1 i} * x_{i}, \sum_{i=1}^{m} \sigma_{1 i} * x_{i}\right) \\ \vdots \\ N\left(\sum_{i=1}^{m} \mu_{n i} * x_{i}, \sum_{i=1}^{m} \sigma_{n i} * x_{i}\right)\end{array}\right]$
$\mu_{\mathrm{ij}}$ and $\sigma_{\mathrm{ij}}$ are mean and standard deviation of weight $w_{\mathrm{ij}}$.
Two updating strategies are adopted for weight $w_{\mathrm{ij}}$ in improved EDA. For example, $5 \%$ of weight $w_{\mathrm{ij}}$ is updated by probabilistic model sampling, and random mask strategy for others. Therefore, Net ${ }_{i}$ can be described as Eq. (21).
$N e t_{i}=\left[\begin{array}{c}N e t_{1} \\ \vdots \\ N e t_{n}\end{array}\right]\left[\begin{array}{c}N\left(\sum_{i \in \bar{M}} w_{1 i} * x_{i}+\sum_{i \in \bar{M}} \mu_{1 i} * x_{i}, \sum_{i \in \bar{M}} \sigma_{1 i} * x_{i}\right) \\ \vdots \\ N\left(\sum_{i \in \bar{M}} w_{n i} * x_{i}+\sum_{i \in \bar{M}} \mu_{n i} * x_{i}, \sum_{i \in \bar{M}} \sigma_{n i} * x_{i}\right)\end{array}\right]$
For set $\bar{M}, \boldsymbol{w}$ is a scalar, whereas $\boldsymbol{w}$ is a variable in set $M$ that is generated by the sampling of a probabilistic model. When the elements of the set $M$ and $\bar{M}$ are infinite, the mean value of Net ${ }_{i}$ and Net ${ }_{i}$ are equivalent, and standard deviation of Net ${ }_{i}$ is reduced to $5 \%$ of Net ${ }_{i}$. Therefore, the risk of combination explosion is reduced. Additionally, in the sampling of a probabilistic model partially, the time consumption is reduced accordingly.

### 4.2.3. Elitism strategy

Elitism strategy is an effective strategy to ensure that the best individual(s) is selected as the next generation in evolutionary algorithms because the best individual(s) maybe include the genes of optimal solution (Purshouse and Fleming, 2002). Therefore, elitism strategy can improve the convergence performance of evolutionary algorithms in many cases (Gao and de Silva, 2018). It is achieved by simply copying the best individual(s) directly to the new generation (Rumelhart et al., 1986). However, the number of best individuals selected as the next generation must be handled properly and carefully; otherwise, it may lead to premature convergence or cannot improve the performance of the algorithm.
$\operatorname{Pop}(k)=\operatorname{Elite}(d) \leftrightarrow \operatorname{rand}(\operatorname{PopTemp}(n), d)$
where $\operatorname{Elite}(d)$ is an elitism maintaining function to select $d$ elites, $d$ is the elitism number, $\operatorname{Pop}(\boldsymbol{k})$ is the $k$-th population, $n$ is the population size, rand(PopTemp $(n), d)$ indicates the selection of $d$ random individuals from the current population PopTemp. $\leftrightarrow$ is a replacement operation to replace the $d$ random individuals by $d$ elites.

### 4.3. Fine-tuning of stacked auto-encoder

The pertaining process achieves rough region searching. However, the final solution should be fine-tuned in another way due to the weak local optimization capability of estimation of distribution algorithm (Wang et al., 2012). A fine-tuning process is carried out based on the gradient algorithm for a stacked auto-encoder. The gradient information is calculated and used for weight tuning as following equation (Xiao et al., (2017) arXiv/1708.07747.).
$w=w-\eta \frac{\partial E}{\partial w}$

![img-6.jpeg](img-6.jpeg)

Fig. 7. Comparison of the effect of data resolution and pre-training on MNIST.
$\frac{\partial E}{\partial w}=\frac{\partial E}{\partial m x_{j} x_{j}}$
where $\eta$ is the learning rate, $w$ is the weight, $E$ is the loss value, $x_{j}$ is the $j$-th neuron input from the previous layer, and $n e t_{j}$ is the $j$-th neuron sum of input.

## 5. Experimental studies

To study the performance of the proposed algorithm in stacked autoencoder training and to see how the proposed strategy works, the algorithm is tested on MINIST and Fashion-MINIST as Fig. 6. MINIST data set is first used to train and test deep neural networks, which contains 60,000 training images and 10,000 testing images of digital handwriting (0-9) with a size of $28 * 28$. In order to evaluate the model adequately, Fashion-MNIST (Ledesma et al., 2019) is adopted, which is a fashion product images dataset as shown in Fig. 6, whilst providing a more challenging classification model. Some experiments (after section 4.3) are based on Fashion-MINIST.

The experiments are implemented on three levels. First, the computing environment is tested, especially the effects of parameter quantization. Second, the effectiveness of the improved estimation of the distribution algorithm is evaluated by different stacked autoencoders and then a deeper stacked auto-encoder is adopted to testify the optimization capability of improved estimation of the distribution algorithm. In the experiments, the population size is set as 100 . The architecture of the neural network is defined as 784-120-10, which contains 784 input neurons, 120 hidden neurons and 10 output neurons. Other architectures, such as 784-300-100-10 and 784-1000-500-250-3010 are adopted. The following sections give more details about the experimental design and results.

### 5.1. The effects of parameter quantization

In order to accelerate the calculation process, NVIDIA GPU is adopted. However, the single-precision data is used in the GPU and the double-precision data is always used in MATLAB based on the CPU. Additionally, the output data precision of the probabilistic sampling function in MATLAB is limited with 4 decimal places resolution. Therefore, a comparison is carried out to exhibit the affection of data precision for the optimization on MNIST dataset. First, a traditional SGD algorithm is adopted to exhibit the effect of data precision, and the validation of pre-training is tested. The first architecture of the neural network is $784-120-10$. The parameters with the double resolution are compared with the data with 4 decimal places of resolution as indicated
![img-7.jpeg](img-7.jpeg)

Fig. 8. Comparison of improved EDA with traditional EDA on MNIST.
in Fig. 8 which denotes that a better result is obtained when the parameters are with high precision. An additional test is carried out under the situation of with or without pre-training. According to Fig. 7, the neural network without pre-training has a worse result. The layer-bylayer pre-training can search a better region for the neural network parameters, and then the fine-tuning process will optimize the solutions accurately. Therefore, the pre-training is effective for the SGD algorithm.

### 5.2. Effectiveness of improved estimation of distribution algorithm \& one-step pre-training

For traditional estimation of distribution algorithm, all the individuals are generated by the sampling of probabilistic model, which was constructed based on the statistical information of promising individuals. For large-scale optimization problems, the probability sampling will increase the calculation time and there will be a serious combination explosion problem. In the improved estimation of the distribution algorithm, the population is updated by two different strategies instead of single probability sampling. Namely, some individuals are generated by probability sampling and the rest of them are replaced by the mean of corresponding advanced individuals. The architecture of the neural network is also 784-120-10, and the pre-training procedure is also adopted. The number of parameters can be optimized with a size of $784 * 120$ (weights between input and hidden layer) $+120 * 784$ (weights
![img-8.jpeg](img-8.jpeg)

Fig. 9. Diagram of pre-training for SGD and EDA on MNIST.

![img-9.jpeg](img-9.jpeg)

Fig. 10. Comparison of fine-tuning result for SGD and EDA pre-training on MNIST.
![img-10.jpeg](img-10.jpeg)

Fig. 11. Comparison of EDA pre-training and without pre-training on MNIST.
between the hidden layer and output layer) +120 (bias of hidden layer) +784 (bias of output layer) $=189,064$, which is a large-scale one for estimation of distribution algorithm. Therefore, it is convincing to describe the large-scale optimization ability of the improved algorithm. The comparison of the optimization result is shown in Fig. 8. The improved estimation of the distribution algorithm has a better performance than the traditional one.

The deeper neural network architecture is 784-300-100-10. The parameter of the deep neural network is also trained layer-by-layer with the estimation of the distribution algorithm and then a fine-tuning is carried out to search the accurate parameters by the SGD algorithm. According to the principle of pre-training, the first hidden layer is trained and then the second hidden layer is trained by the first hidden layer output. The loss value of pre-training by SGD and improved estimation of the distribution algorithm are shown in Fig. 10. The pretraining of two hidden layers has a similar convergent performance by improved estimation of the distribution algorithm. For the SGD algorithm, the first hidden layer has a better performance. However, the performance is worse in the second hidden layer pre-training as displayed in Fig. 9.

In order to analyze the layer-wise pre-training effectiveness, the second procedure of fine-tuning is carried out. The SGD based layer-wise pre-training has worse classification performance than the EDA

Table 2
No. of parameters in pre-training on MNIST.
![img-11.jpeg](img-11.jpeg)

Fig. 12. Comparison of convergence error under different architectures on MNIST.
algorithm-based layer-wise pre-training as shown in Fig. 10, which looks like trapped into the local minima (twice repeated procedures are carried out for SGD algorithm).

In order to analyze the search ability of improved estimation of distribution algorithm further, the parameters of the whole neural network are optimized by improved estimation of distribution algorithm without layer-wise pre-training. The performance of the optimization is shown in Fig. 11, denoting that the improved estimation of the distribution algorithm has a similar performance for the whole neural network parameter optimization as the layer-wise pre-training. It means that the improved estimation of the distribution algorithm has a promising search efficiency and accuracy to search the whole neural network directly based on the improved estimation of the distribution algorithm. The layer-wise pre-training procedure can be replaced with the one-step pre-training.

A deeper architecture, which is a typical one, is adopted as a reference (Hinton and Salakhutdinov, 2006) to verify the search ability of the improved algorithm further. The architecture of the neural network is 784-1000-500-250-30-10. Table 2 shows the number of parameters for pre-training. It can be seen that there is a huge large-scale optimization problem. According to the convergent process of improved estimation of distribution algorithm (Fig. 12), the performance of improved estimation of distribution algorithm is stable for a deeper neural network. The convergent speed and classification error are also similar to the shallower one. Therefore, the depth of the neural network has limited influence on the convergence of the algorithm.

After the one-step pre-training, a fine-tuning process is carried out. The classification accuracy is about $99.9 \%$ for MNIST which has been reached to $100 \%$, and there are no intervals for comparison. Therefore, the Fashion-MNIST dataset is adopted for the following verifications.

### 5.3. Effectiveness of one-step estimation of distribution algorithm pre-training \& gradient fine-tuning

The local optimization capability of estimation of distribution algorithm is limited. And, conversely, the gradient-based algorithm has

![img-12.jpeg](img-12.jpeg)

Fig. 13. The descent of loss for two models on Fashion-MNIST.
![img-13.jpeg](img-13.jpeg)

Fig. 14. The classification accuracy comparison of two models on Fashion-MNIST.
better local optimization capability. Therefore, estimation of distribution algorithm-based pre-training combination of the gradient-based fine-tuning procedure is adopted. In order to verify the effectiveness of this strategy, a comparing experiment is carried out. The baseline of the neural network is also 784-1000-500-250-30. The complete model in one-step pre-training is 784-1000-500-250-30-784, and then the model in fine-tuning is 784-1000-500-250-30-10. A direct classification model of 784-1000-500-250-30-10 is trained by the estimation of the distribution algorithm, which removes the pre-training process. Fig. 13 compares the loss for two algorithms. They have the same tendency of loss. The loss value is small in the direct classification model, which is the classification loss instead of reconstruction error in the pre-training process. Fig. 14 is the classification accuracy comparison. Although the classification accuracy goes up with the iterations as the gradient finetuning strategy (accuracy $92.36 \% \& 98.24 \%$ ), the direct classification optimization model has lower classification accuracy than using the pretraining way. In the two figures, the two models have a different x-y axis. Therefore, estimation of distribution algorithm-based one-step pretraining combines with gradient fine-tuning strategy is effective.

### 5.4. Different mask ratio and promising individual testifying

### 5.4.1. Model evaluation based on different mask ratio

The mask ratio (MR) affects the population updating strategy. In
![img-14.jpeg](img-14.jpeg)

Fig. 15. The pre-training process under different MR on Fashion-MNIST.
![img-15.jpeg](img-15.jpeg)

Fig. 16. The fine-tuning process under different MR on Fashion-MNIST.
![img-16.jpeg](img-16.jpeg)

Fig. 17. Amplification of local region of Fig. 16.

![img-17.jpeg](img-17.jpeg)

Fig. 18. Time consumption under PIR $=60$ on Fashion-MNIST.
order to analyze the influence of different mask ratios on the performance of estimation of distribution algorithm, experiments are carried out. Some typical mask ratios, such as $0.3 \%, 1 \%, 5 \%, 10 \%$ and $40 \%$ are adopted for updating the population when the promising individual ratio (PIR) is $60 \%$ and $100 \%$. The promising individual ratio will affect $\mu$ and $\sigma$ of probabilistic model. The convergent performance under PIR $=$ 100 and 60 are different in the pre-training as shown in Fig. 15. A bigger promising individual ratio slows down the convergence speed of the algorithm. Therefore, the convergent speed under PIR $=100 \%$ is worse than PIR $=60 \%$. For PIR $=60 \%$, the convergent performance is promising. As a whole, a bigger MR goes against the convergent performance. The fine-tuning process is shown in Fig. 16 and Fig. 17. Fig. 17 is the amplification of the local region given in Fig. 16. According to the two figures, the pre-training is valid under smaller MR (Fig. 16). A larger MR increases the probability of combination explosion. Therefore, the pre-training is invalid when MR is $10 \%, 40 \%$ and $80 \%$ as Fig. 17, which means the parameters gathered by pre-training are the same as random values. According to Fig. 18, the fine-tuning results are similar under the parameters of (PIR $=100, \mathrm{MR}=0.3 \%$ ), (PIR $=100, \mathrm{MR}=1 \%$ ) and (PIR $=60, \mathrm{MR}=0.3 \%)$. Considering the efficiency of the algorithm (a bigger PIR and MR will consume much time as Fig. 19), the parameter of (PIR $=60, \mathrm{MR}=0.3 \%$ ) is a better choice.

According to Fig. 17, it is interesting to note that the convergent performance of pre-training is worse for PIR $=100$. Nevertheless, the pre-training effect is promising in case of the satisfactory initial value. Fig. 19 may explain this vividly. The estimation of the distribution algorithm based on pre-training is shown in Fig. 19(a). Supposing estimation of distribution algorithm has found the region (3) instead of local minimal region (5) and (7). However, the probabilistic model under PIR $=100$ has a bigger $\sigma$ as Fig. 19(a), the randomness of probabilistic
sampling will be stronger. Although the estimation of the distribution algorithm has found region (3), it isn't easy to get the valley point. Conversely, SGD has better local optimization ability than the estimation of the distribution algorithm. Therefore, it can realize the accurate solution searching under region (3) which was found by estimation of distribution algorithm.

### 5.4.2. Model evaluation based on the different promising individual ratios

The promising individual ratio (PIR) will affect the construction of the probabilistic model. A smaller promising individual ratio will increase the convergence speed. However, it leads to the early maturing of the algorithm. A bigger promising individual ratio slows down the convergence speed of the algorithm. A different promising individual ratio is adopted for testing the influence of promising individuals when MR $=0.3 \%$ and $5 \%$. Fig. 20 shows the estimation of distribution algorithm-based pre-training loss. We can see that a smaller promising individual ratio accelerates the convergence speed of the algorithm. The convergence speed is very slow than others when PIR $=100 \%$. However, in the fine-tuning process diagram as Fig. 21, the pre-training is invalid when the PIR is small (MR $=5 \%, \mathrm{PIR}=10 \%$ or MR $=5 \%, \mathrm{PIR}=40 \%$ ), even though the pre-training process is promising. Although, the pretraining process is bad when PIR $=100 \%$, the fine-tuning process is promising as Fig. 22. According to Figure 23, PIR $=60 \%, \mathrm{MR}=0.3 \%$ are the better parameters for comprehensive consideration.
![img-18.jpeg](img-18.jpeg)

Fig. 20. The pre-training process under different PIR on Fashion-MNIST.
![img-19.jpeg](img-19.jpeg)

Fig. 19. Pre-training and fine-tuning based optimization diagram.

![img-20.jpeg](img-20.jpeg)

Fig. 21. The fine-tuning process under different PIR on Fashion-MNIST.
![img-21.jpeg](img-21.jpeg)

Fig. 22. The amplification of the local region of Fig. 21.

### 5.5. Compared with state-of-the-art

Fashion-MNIST dataset is a challenging benchmark for classification models. The stacked auto-encoder with the architecture of 784-1000-500-250-30-10 is also used for classification, PIR $=60 \%$ and $\mathrm{MR}=$ $0.3 \%$. The same procedures, one-step pre-training and fine-tuning, are carried out. The proposed model is compared with state-of-the-art models on Fashion-MNIST as Table 3. Compared with traditional MINIST, the classification accuracy is lower, and our model can achieve a result of $98.38 \%$. The references with the mark ${ }^{[* 1}$ come from the automatic benchmarking system for Fashion-MNIST, which covers various kinds of classifiers based on the convolution neural network. This network is popular in image processing. Therefore, the studies are always based on the convolution neural network, such as evoCNN ( Xu et al., 2019) is based on the evolutionary algorithm, psoCNN (Junior and Yen, 2019) adopts particle swarm optimization algorithm, etc. However, it is not possible to make a direct comparison with our algorithm due to the different structures. Evolving unsupervised deep neural network (EUDNN) (Sun et al., 2019) is the only study for deep neural network optimization in which direct comparison can be made. The neural network structure of EUDNN (784-400-202-106-88-10) is adopted for testifying. The proposed algorithm gets a similar accuracy ( $98.92 \mathrm{~g}$ ) as EUDNN. However, the SGD-based model has a lower accuracy ( $95.74 \%$ ),

Table 3
Comparison of state-of-the-arts.

which means that the heuristic algorithm has played an active role in the weights' optimization. Due to the complexity of Fashion-MNIST, the structure of 784-400-202-106-88-10 is not enough for classification, even though, the performance of the algorithm is better than SGD based algorithm.

## 6. Conclusion

As a heuristic algorithm, the estimation of the distribution algorithm has been proposed for different kinds of applications. However, the capability of large-scale optimization is limited due to the curse of dimensionality. The weight training of deep neural networks is a largescale optimization problem. Although the traditional gradient-based algorithm can achieve this goal, some inherent weaknesses are leading to failure in training, such as gradient disappearing. The heuristic algorithm doesn't make use of a gradient to evaluate and update individuals. Therefore, a new attempt is proposed to optimize the weight of the deep neural network based on an improved estimation of the distribution algorithm. This paper explores the capability of the improved EDA and demonstrates that it is effective for deep neural network parameter searching and time reduction. In addition, it is a universal framework, which can be extended to other deep neural networks. However, the optimization is only for weights, and the architecture is exclusive. This will be our future work.

# CRediT authorship contribution statement 

Qingyang Xu: Conceptualization, Methodology, Writing - review \& editing. Anbang Liu: Investigation, Software. Xianfeng Yuan: Formal analysis. Yong Song: Funding acquisition. Chengjin Zhang: Formal analysis. Yibin Li: Project administration.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This work was supported by the National Key Research and Development Plan of China under Grant (2017YFB1300205, 2020AAA0108903), National Natural Science Foundation of China under Grants (61803227, 61573213, 61603214, 61673245), Natural Science Foundation of Shandong Province (ZR2020MD041, ZR2020MF077).
