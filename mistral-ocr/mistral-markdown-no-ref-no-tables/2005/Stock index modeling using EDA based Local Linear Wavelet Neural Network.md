# Stock Index Modeling using EDA based Local Linear Wavelet Neural Network 

Yuehui Chen<br>School of Information Science and Engineering<br>Jinan University<br>Jiwei road 106, Jinan 250022, P.R.China<br>E-mail: yhchen@ujn.edu.cn<br>Xiaohui Dong<br>School of Information Science and Engineering<br>Jinan University<br>Jiwei road 106, Jinan 250022, P.R.China<br>E-mail: nicop2@ujn.edu.cn<br>Yaou Zhao<br>School of Information Science and Engineering<br>Jinan University<br>Jiwei road 106, Jinan 250022, P.R.China<br>E-mail: yaou_zhao@yahoo.com.cn


#### Abstract

The use of intelligent systems for stock market predictions has been widely established. In this paper, we investigate how the seemingly chaotic behavior of stock markets could be well represented using Local Linear Wavelet Neural Network (LLWNN) technique. To this end, we considered the Nasdaq-100 index of Nasdaq Stock Market ${ }^{\text {TM }}$ and the S\&P CNX NIFTY stock index. We analyzed 7 -year Nasdaq-100 main index values and 4 -year NIFTY index values. This paper investigates the development of novel reliable and efficient techniques to model the seemingly chaotic behavior of stock markets. The LLWNN are optimized by using Estimation of Distribution Algorithm (EDA). This paper investigates whether the proposed method can provide the required level of performance, which is sufficiently good and robust so as to provide a reliable forecast model for stock market indices. Experiment results shown that the model considered could represent the stock indices behavior very accurately.


## I. INTRODUCTION

Prediction of stocks is generally believed to be a very difficult task - it behaves like a random walk process and time varying. The obvious complexity of the problem paves the way for the importance of intelligent prediction paradigms. During the last decade, stocks and futures traders have come to rely upon various types of intelligent systems to make trading decisions [1][2]. Several intelligent systems have in recent years been developed for modeling expertise, decision support and complicated automation tasks [3][4]. In this paper, we analyzed the seemingly chaotic behavior of two well-known stock indices namely the Nasdaq-100 index of Nasdaq ${ }^{\text {int }}$ [5] and the S\&P CNX NIFTY stock index [6]. The Nasdaq-100 index reflects Nasdaq's largest companies across major industry groups, including computer hardware and software, telecommunications, retail/wholesale trade and biotechnology [5]. The Nasdaq-100 index is a modified capitalization weighted index, which is designed to limit domination of the Index by a few large stocks while generally retaining the capitalization ranking of companies. Through an investment in the Nasdaq-100 index tracking stock, investors can participate in the collective performance of many of the Nasdaq stocks that are often in the news or
have become household names. Similarly, S\&P CNX NIFTY is a well-diversified 50 stock index accounting for 25 sectors of the economy [6]. It is used for a variety of purposes such as benchmarking fund portfolios, index based derivatives and index funds. The CNX Indices are computed using market capitalization weighted method, wherein the level of the Index reflects the total market value of all the stocks in the index relative to a particular base period. The method also takes into account constituent changes in the index and importantly corporate actions such as stock splits, rights, etc. without affecting the index value.

In our previous work, the neural network ( NN ) and flexible neural tree (FNT) have been employed for stock index modeling [7][9]. This research is to investigate the performance analysis of LLWNN for modeling the Nasdaq-100 and the NIFTY stock market indices. The parameters of the LLWNN model are optimized by EDA. We analyzed the Nasdaq-100 index value from 11 January 1995 to 11 January 2002 [5] and the NIFTY index from 01 January 1998 to 03 December 2001 [6]. For both the indices, we divided the entire data into almost two equal parts. No special rules were used to select the training set other than ensuring a reasonable representation of the parameter space of the problem domain [2].

## II. LOCAL LINEAR WAVELET NEURAL NETWORK

In terms of wavelet transformation theory, wavelets in the following form

$$
\begin{gathered}
\Psi=\left\{\Psi_{i}=\left|\mathbf{a}_{i}\right|^{\frac{1}{2}} \phi\left(\frac{\mathrm{x}-\mathrm{b}_{\mathrm{i}}}{\mathrm{a}_{\mathrm{i}}}\right): \mathrm{a}_{\mathrm{i}}, \mathrm{~b}_{\mathrm{i}} \in \mathrm{R}^{\mathrm{n}}, \mathrm{i} \in \mathrm{Z}\right\} \\
\mathrm{x}=\left(x_{1}, x_{2}, \ldots, x_{n}\right) \\
\mathrm{a}_{\mathrm{i}}=\left(a_{i 1}, a_{i 2}, \ldots, a_{i n}\right) \\
\mathrm{b}_{\mathrm{i}}=\left(b_{i 1}, b_{i 2}, \ldots, b_{i n}\right)
\end{gathered}
$$

are a family of functions generated from one single function $\psi(x)$ by the operation of dilation and translation. $\psi(x)$,

which is localized in both the time space and the frequency space, is called a mother wavelet and the parameters $a_{i}$ and $\mathrm{b}_{i}$ are named the scale and translation parameters, respectively. The x represents inputs to the WNN model.

In the standard form of wavelet neural network, the output of a WNN is given by

$$
f(x)=\sum_{i=1}^{M} \omega_{i} \Psi(x)=\sum_{i=1}^{M} \omega_{i}\left|a_{i}\right|^{-\frac{i}{2}} \psi\left(\frac{x-b_{i}}{a_{i}}\right)
$$

where $\psi_{i}$ is the wavelet activation function of $i$ th unit of the $\omega_{i}$ is the weight connecting the $i$ th unit of the hidden layer to the output layer unit. Note that for the $n$-dimensional input space, the multivariate wavelet basis function can be calculated by the tensor product of $n$ single wavelet basis functions as follows

$$
\psi(x)=\prod_{i=1}^{n} \psi\left(x_{i}\right)
$$

Obviously, the localization of the $i$ th units of the hidden layer is determined by the scale parameter $a_{i}$ and the translation parameter $b_{i}$. According to the previous researches, the two parameters can either be predetermined based upon the wavelet transformation theory or be determined by a training algorithm. Note that the above wavelet neural network is a kind of basis function neural network in the sense of that the wavelets consists of the basis functions.

Note that an intrinsic feature of the basis function networks is the localized activation of the hidden layer units, so that the connection weights associated with the units can be viewed as locally accurate piecewise constant models whose validity for a given input is indicated by the activation functions. Compared to the multilayer perceptron neural network, this local capacity provides some advantages such as the learning efficiency and the structure transparency. However, the problem of basis function networks is also led by it. Due to the crudeness of the local approximation, a large number of basis function units have to be employed to approximate a given system. A shortcoming of the wavelet neural network is that for higher dimensional problems many hidden layer units are needed.

In order to take advantage of the local capacity of the wavelet basis functions while not having too many hidden units, here we propose an alternative type of wavelet neural network. The architecture of the proposed LLWNN [8] is shown in Fig.1. Its output in the output layer is given by

$$
y=\sum_{i=1}^{M}\left(\omega_{i 0}+\omega_{i 1} x_{1}+\ldots+\omega_{i n} x_{n} \Psi_{i}(x)\right.
$$

$$
=\sum_{i=1}^{M}\left(\omega_{i 0}+\omega_{i 1} x_{1}+\ldots+\omega_{i n} x_{n}\right)\left|a_{i}\right|^{-\frac{i}{2}} \psi\left(\frac{x-b_{i}}{a_{i}}\right)
$$

where $x=\left[x_{1}, x_{2}, \ldots, x_{n}\right]$. Instead of the straightforward weight $\omega_{i}$ (piecewise constant model), a linear model

$$
v_{i}=\omega_{i 0}+\omega_{i 1} x_{1}+\ldots+\omega_{i n} x_{n}
$$

is introduced. The activities of the linear models $v_{i}(i=1,2, \ldots M)$ are determined by the associated locally active wavelet functions $\psi_{i}(x)(i=1,2, \ldots M)$, thus $v_{i}$ is only locally significant. The motivations for introducing the local linear models into a WNN are as follows: (1) Local linear models have been studied in some neurofuzzy systems and shown good performances [18], [19]; and (2) Local linear models should provide a more parsimonious interpolation in high-dimension spaces when modeling samples are sparse.

The scale and translation parameters and local linear model parameters are randomly initialized at the beginning and are optimized by a EDA discussed in the following section.
![img-0.jpeg](img-0.jpeg)

Fig. 1. A local linear wavelet neural network

## III. LLWNN TRAINING

Estimation of distribution algorithms (EDAs) [11] [12] [14] [16] [17] are a new class of evolutionary algorithms. Like other evolutionary algorithms, EDAs maintain and successively improve a population of potential solutions until some stopping condition is met. However, EDAs do not use crossover or mutation. Instead, they select the best solutions from the current population and explicitly extract global statistical information from the selected solutions. A

posterior probability distribution model of promising solutions is built, based on the extracted information. Then new solutions are sampled from the model thus built and fully or in part replace solutions in the current population. More precisely, EDAs work as follows:

S0 Randomly pick a set of solutions to form the initial population.
S1 Select some solutions from the current population according to a selection method. Build the probability model of the selected solutions.
S2 Replace some or all of the members of the current population by new solutions sampled from the probability model.
S3 If the stopping condition are not met, go to Step 1.
Several EDAs have been proposed for solving global optimization problems. In these existing algorithms, the probability distribution of the promising solutions are modeled by a Gaussian distribution, a Gaussian mixture or a histogram. Since many points are needed to build a good probability model, these algorithms are often very time-consuming in practice.

One of the major issues in EDAs is how to select parents. A widely used selection method in EDA is the truncation selection. In the truncation selection, individuals are sorted according to their objective function values. Only the best individuals are selected as parents.

Another major issue in EDAs is how to build a probability distribution model $p(x)$. In EDAs for the global continuous optimization problem, the probabilistic model $p(x)$ can be a Gaussian distribution [13], a Gaussian mixture [14][11], a histogram [15], or a Gaussian model with diagonal covariance matrix (GM/DCM) [14].

GM/DCM is used in our algorithm. In GM/DCM, the joint density function of the $k$-th generation is written as follows:

$$
p_{k}(x)=\prod_{i=1}^{n} N\left(x_{i}, \mu_{i}^{k}, \sigma_{i}^{k}\right)
$$

where

$$
N\left(x_{i}, \mu_{i}^{k}, \sigma_{i}^{k}\right)=\frac{1}{\sqrt{\left(2 \pi \sigma_{i}\right)}} \exp \left(-\frac{1}{2}\left(\frac{x_{i}-\mu_{i}}{\sigma_{i}}\right)^{\frac{1}{2}}\right)
$$

In (2), the $n$-dimensional joint probability distribution is factorized as a product of $n$ univariate and independent normal distributions. There are two parameters for each variable required to be estimated in the $k$-th generation: the mean, $\mu_{i}^{k}$, and the standard deviation, $\sigma_{i}^{k}$. They can be estimated as follows:

$$
\hat{\mu}_{i}^{k}=\bar{x}_{i}^{k}=\frac{1}{M} \sum_{j=1}^{M} x_{j i}^{k}
$$

$$
\hat{\sigma}_{i}^{k}=\sqrt{\frac{1}{M} \sum_{j=1}^{M}\left(x_{j i}^{k}-\bar{x}_{j}^{k}\right)^{2}}
$$

Before describing details of the algorithm for training LLWNN, the issue of coding is presented. Coding concerns the way the weights, dilation and translation parameters of LLWNN are represented by individuals or particles. A float point coding scheme is adopted here. For LLWNN coding, suppose there are $M$ nodes in hidden layer and $n$ input variables, then the total number of parameters to be coded is $(2 n+n+1) * M=(3 n+1) M$. The coding of a LLWNN into an individual or particle is as follows:

$$
\begin{aligned}
& \left|a_{11} b_{11} \ldots a_{1 n} b_{1 n} \omega_{10} \omega_{11} \ldots \omega_{1 n}\right| a_{21} b_{21} \\
& \ldots a_{2 n} b_{2 n} \omega_{20} \omega_{21} \ldots \omega_{2 n} \mid \ldots \\
& \left|a_{n 1} b_{n 1} \ldots a_{n n} b_{n n} \omega_{n 0} \omega_{n 1} \ldots \omega_{n n}\right|
\end{aligned}
$$

The simple loop of the proposed training algorithm for local linear wavelet neural network is as follows.

S1 Initial population is generated randomly.
S2 Parameter optimization with EDA;
S3 If the satisfactory solution is found or maximum number of generations is reached then stop; otherwise goto step S2.

TABLE I
THE RMSE RESULTS OF LLWNN AND WNN MODELS FOR TEST DATA SETS


TABLE II
STATISTICAL ANALYSIS OF THE LEARNING METHODS (TEST DATA)


## IV. EXPERIMENTS

We considered 7-year stock data for the Nasdaq-100 Index and 4-year for the NIFTY index. Our target is to develop efficient forecast models that could predict the index value of the following trade day based on the opening, closing and maximum values of the same on a given day. The assessment of the prediction performance of the different ensemble paradigms were done by quantifying the

prediction obtained on an independent data set. The Root Mean Squared Error (RMSE), Maximum Absolute Percentage Error (MAP) and Mean Absolute Percentage Error (MAPE) and Correlation Coefficient (CC) were used to study the performance of the trained forecasting model for the test data. MAP is defined as follows:

$$
M A P=\max \left(\frac{P_{\text {actual } i}-P_{\text {predicted } i}}{P_{\text {predicted } i}}\right) \times 100)
$$

where $P_{\text {actual } i}$ is the actual index value on day $i$ and $P_{\text {predicted } i}$ is the forecast value of the index on that day. Similarly MAPE is given as

$$
M A P E=\frac{1}{N} \sum_{i=1}^{N}\left(\frac{P_{\text {actual } i}-P_{\text {predicted } i}}{P_{\text {predicted } i}}\right) \times 100)
$$

where N represents the total number of days.
We used LLWNN with architecture $\{3-8-1\}$ for modeling the Nasdaq-100 index and a LLWNN with architecture $\{5-8-1\}$ for modeling the NIFTY index. For comparison purpose, two WNNs trained by EDA are also employed to predict the same stock indices.

Table 1 summarizes the test results achieved for the two stock indices using the proposed approach. Performance analysis of the trained forecasting models for the test data was shown in Table 2. Figures 2 and 3 depict the test results for the one day ahead prediction of the Nasdaq 100 index and the NIFTY index respectively.
![img-2.jpeg](img-2.jpeg)

Fig. 2. Test results showing the performance of the LLWNN for modeling the Nasdaq-100 index
![img-2.jpeg](img-2.jpeg)

Fig. 3. Test results showing the performance of the LLWNN for modeling the NIFTY index

## V. CONCLUSIONS

In this paper, we have demonstrated how the chaotic behavior of stock indices could be well represented by local linear wavelet neural networks. Empirical results on the two data sets using LLWNN models clearly reveal the efficiency of the proposed techniques. In terms of RMSE values, for the Nasdaq-100 index and the NIFTY index, LLWNN performed marginally better than other models. For both index (test data), LLWNN also has the highest correlation coefficient and the lowest value of MAPE and MAP values. A low MAP value is a crucial indicator for evaluating the stability of a market under unforeseen fluctuations. In the present example, the predictability assures the fact that the decrease in trade is only a temporary cyclic variation that is perfectly under control. Our research was to predict the share price for the following trade day based on the opening, closing and maximum values of the same on a given day. Our experiment results indicate that the most prominent parameters that affect share prices are their immediate opening and closing values. The fluctuations in the share market are chaotic in the sense that they heavily depend on the values of their immediate forerunning fluctuations. Long-term trends exist, but are slow variations and this information is useful for long-term investment strategies. Our study focus on short term, on floor trades, in which the risk is higher. However, the results of our study show that even in the seemingly random fluctuations, there is an underlying deterministic feature that is directly enciphered in the opening, closing and maximum values of the index of any day making predictability possible.

## ACKNOWLEDGMENT

This research was partially supported by the National High Technology Development Program of China (863 Program) under contract number 2002AA4Z3240, and The Provincial Science and Technology Development Program of Shandong under contract number SDSP2004-0720-03.
