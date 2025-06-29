# Cash flow prediction using artificial neural network and GA-EDA optimization 

Mohsen Sadegh Amalnik ${ }^{a}$, Hossein Iranmanesh ${ }^{a *}$, Atabak Asghari ${ }^{a}$, Ali Mollajan ${ }^{a}$, Vahed Fadakar ${ }^{b}$ and Reza Daneshazarian ${ }^{c}$<br>${ }^{a}$ Department of Industrial Engineering, College of Engineering, University of Tehran(U.T), Tehran, Iran<br>${ }^{b}$ Faculty of Electrical Engineering, Iran University of Science and Technology, Tehran, Iran<br>${ }^{c}$ Renewable Energy Department, Faculty of New Sciences and Technologies, University of Tehran, Tehran, Iran

CHRONICLE

Article history:
Received: January 102018
Received in revised format: April 12018
Accepted: June 82018
Available online:
June 92018
Keywords:
Cash flow
Neural network
Genetic algorithm
Estimation of distribution algorithm

## ABSTRACT

Cash flow models are one of the spotlights for evaluating a project. The actual data should be modeled then it could be used for the prediction process. In this paper, 996 airplane maintenance basis data are used as a database, and 119 similar data are chosen after clustering. The project is divided into 20 equal periods and first three periods are used for simulating the next point. The predicted data for each point is achieved by using of previous points from the beginning. The model is based on artificial neural network, and it is trained by three algorithms which are Genetic Algorithm (GA), Estimation of Distribution Algorithm (EDA), and hybrid GA-EDA method. Two dynamic ratios are used which are dividing the population into two halves, and the other is a ratio without dividing. The ratio would give a proportion to GA and EDA models in the hybrid algorithm, and then the hybrid algorithm could model the system more accurately. For each algorithm, three main errors are calculated which are mean absolute percentage error (MAPE), mean square error (MSE), and root means square error (RMSE). The best result is achieved for hybrid GA-EDA model without dividing the population and the MAPE, RMSE, and MSE values are $\% 0.022$, 28944.59 Dollars, and 837789503.79 Dollars, respectively.

## Nomenclature


[^0]
[^0]:    * Corresponding author. Tel.: +98-9123855616

    E-mail address: h.iranmanesh@ut.ac.ir (H. Iranmanesh)

# 1. Introduction 

One of the critical parameters in the designing of a system is considering its cash flow. More than $60 \%$ of the failures in the construction section is caused by economic factors (Russell, 1991). Cash flow model would have a significant influence on the project. Dynamic cash flow models could forecast the crucial parameters, and it would have an effect on the business plans. Almond and Remer (1979) presented sixth various cash flow models for an industrial economic applications. The two levels were modified, and it was shown that the cash flow model for the project level would be easier than company level. Chen et al. (2005) presented a cost-schedule integration (CSI) by combining pattern-matching logic and factorial experiments. They used the payment lags, separate tracking of material and payment frequency. Khosrowshahi and Kaka (2007) represented the cash flow model which included a mathematical model and estimating models. Their result showed that financial estimating models should be used for determination of the cash flow of the project. S curves are used for forecasting the cash flow, and it is the primary method in the cash flow projects (Touran, et al., 2004).

Artificial intelligence networks are used widely by the scholars. It is an alternative method for controlling the project costs. Cheng et al. (2009) used artificial intelligence methods for forecasting the cash flow models. They used K-mean clustering, genetic algorithm and artificial neural network (ANN). Blanc and Seltzer (2015) analyzed the cash flow for a corporation, and their results represented rectifiable biases. Also, they used debasing by employing selected statistical correction models for enhancing the estimating accuracy. Li et al. (2015) investigated the cash flow for South African firms which are listed on the Johannesburg Stock Exchange. According to their results, the inclusion of explanatory variable does not enhance the models, and they represented the application of moving the average model. Son et al. (2012) investigated the hybrid principal components analysis (PCA) and super vector machine (SVM) for the cash flow estimation in the commercial building projects. Their model was based on 84 data sets from commercial buildings. The hybrid PCA-SVM method was more accurate than single PAC and SVM methods. Kao et al. (2013) studied the cash flow for the stock price using nonlinear independent component analysis and SVM. They used two data sets including Japan, China, Shanghai Exchange Stock and Nikkei 225 stock indexes. Hwee and Tiong (2002) represented the cash flow model for contracting firms. They analyzed five various risk factors such as under/over measurement risk, duration, variation risk, and material cost variances, and estimated the cash flow considering these risks. Bec and Mogliani (2015) proposed a study for nowcasting French GDP using forecast combination and information pooling. The information pooling results were accurate regarding the forecast combination scheme. Ghysels and Ozkan (2015) estimated the US federal government budget. They used frequency data regression method for predicting the annual federal expenditures and receipts.

Artificial neural network is one of the prediction methods which are in the spotlight of the researchers of this field. Andrawis et al. (2011) introduced a new forecasting model for NN5 forecasting competition. The competition considered the estimation of 111-time series which represented the daily cash withdrawal values at ATMs. Xiong et al. (2013) performed a study on the crude oil price over long periods. They used a revised hybrid model empirical mode decomposition (EMD) and feed-forward neural network (FNN). They used the weekly report from West Texas Intermediate crude oil prices. Venkatesh et al. (2014) used the clustering and artificial neural networks for cash demand estimation in ATMs. After clustering the ATMs, they used four different neural networks on them which are general regression neural network (GRNN), multi-layer feed-forward neural network (MLFF), group method of data handling (GMDH), and wavelet neural network (WNN). The GRNN has the best outlet among the four networks with the yield of $18.44 \%$. Cheng and Roy $(2010,2011)$ represented the cash flow model by time-dependent support vector machines (TDSVM). They used the evolutionary fuzzy decision model for the SVM method by focusing on the time series management. Cheng et al. (2010) developed a fuzzy neural network for improving the cash flow prediction. Namazi et al. (2016) analyzed the cash flow risk factors by using artificial neural network. Their results showed that the profitability is the highest risk, and the second and third elements are debt policy and company size.

In this paper genetic algorithm (GA), estimation distribution algorithm (EDA), and hybrid GA-EDA method are used for training the artificial neural network (ANN) to predict the cash flow model. The data of 996 airplane maintenance basis are used for the database. First, the data is clustered and the similar data is chosen. The 996 data were decreased to 119 similar data. Then this data is used for the algorithms - GA, EDA, and hybrid GA-EDA - which are used for training the ANN method. In the previous studies the data was divided into two halves, then they combined the results from different algorithms, but in the present study the whole data is investigated in the GA, EDA, and hybrid GAEDA methods and the best result is chosen in every step. Using this approach would enhance the training path in the ANN method, and this functionalized method leads to precise results.

# 2. Methodology 

The mixed method of the trained neural network and the hybrid genetic algorithm (GA) - estimation of distribution algorithm (EDA) is used for the forecasting the cash flow model. The clustering is used by the fuzzy C-means clustering method for preventing the data tolerances and increasing the accuracy then the final clustered data is utilized for the neural network input. The clustering has been done in three steps and 996 airplane maintenance bases construction projects by considering nine parameters; in this case, 119 projects are selected according to their similarity to training the neural network. This approach would lead to enhance the performance of the network, and the outliers are not used. After selecting the data which is used for training the neural network, the data is used as input for the hybrid GA-EDA method. The scheme of the proposed method is shown in Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Schematic of the prediction method

### 2.1. GA

Genetic algorithms are widely used in the optimization projects by the Darwinian fundamentals of natural selection and genetic replication (Holland \& Goldberg, 1989) and this algorithm is heuristic

one. This algorithm includes an individual population and they represent a path to the results. The individuals play the chromosome role and they are series of bits. In the problem optimizations, the representations would be complicated. The results should show the entire search to examine. The size of the representation must be optimized so the performance of the genetic algorithm (GA) would decrease.

# 2.2. $E D A$ 

Estimation of distribution algorithms uses stochastic and heuristic search procedure (Larrañaga \& Lozano, 2001; Mühlenbein, 1997). The main difference between the GA and EDA methods are in their search processes, GA uses this strategy in which the evolution and reproduction in one step would be finished up to next one and it would require probability distribution for the fittest individuals. Mutation operators would be ignored by this strategy and the required parameter for EDA would decrease. EDA use the following strategy which contains four fundamental levels:
a. The initial population P0 of N individuals are created at the start point.
b. A number of individuals are chosen and the fittest ones would be considered.
c. The $n$-parametric probabilistic graphical model explains the degrees of freedom and the reliance of the $n$ variables.
d. The new population would have N new individuals and it would be obtained by modeling the probability learned distribution.

### 2.3. Hybrid GA-EDA

The aim of hybrid GA-EDA algorithm is to use the advantages of both Genetic Algorithm (GA) and Estimation of Distribution Algorithm (EDA). The EDA and GA algorithms do not have any absolute privilege on each other. The main difference between the methods is on the creating crossovers. The GA method selects the best population by considering crossover and mutation, on the other hand, the EDA process creates a probability distribution model then the new population would be available by reviewing the individual which has the best fittest with the model. In the hybrid model, a participation function should be used which employs the gained population from both EDA and GA models. In each step, this function identifies the fraction of the GA and the EDA algorithms. This population ratio could be dynamic or constant. The value of the participation function could be achieved by considering the following situations:

- Constant ratio: In this approach, the ratio has a specific value and it is given to each GA and EDA methods. It would not change in the next steps.
- Odd and even ratio: The even ratio would be given to one of EDA or GA algorithms, and the other algorithm would obtain the odd ratio.
- Incremental ratio: This ratio correlation is as follow:
I. R. $=\frac{\text { gen }}{M+\text { gen }}$,
where; gen is the iteration number and the $M$ is the mid-point. The use of mid-point is for preventing the growth of ratio be more than $50 \%$. In this equation, the amount of ratio would be increased in each iteration.
- Dynamic ratio: In this method, the ratio between the GA and EDA algorithms would be obtained by considering the both algorithm average scores and each algorithm would gain its score.
- Exact value: This ratio is used to reduce the tolerance of the calculated predicted value. The calculated value for each step is different because as it shown in Eq. (23) this ratio is obtained by errors during the training period.

In this paper, two different kinds of the dynamic ratio are used with and without dividing the population. The dynamic ratio by dividing the population, the population is divided into half for both GA and EDA algorithms. The ratio would change in each step would be modified and improved. This process would be continued to the end of the process.

The EDA ratio of population $=\frac{\text { MSEtr }_{i+3}^{E D A}}{\text { MSEtr }_{i+3}^{E D A}+\text { MSEtr }_{i+3}^{G A}} \times$ population
The GA ratio of population $=\frac{M S E t r_{i+3}^{G A}}{M S E t r_{i+3}^{E D A}+M S E t r_{i+3}^{G A}} \times$ population

$$
P C F t r_{i+3}=\left(\frac{M S E t r_{i+3}^{E D A}}{M S E t r_{i+3}^{E D A}+M S E t r_{i+3}^{G A}}\right) * P C F t r_{i+3}^{G A}+\left(\frac{M S E t r_{i+3}^{G A}}{M S E t r_{i+3}^{E D A}+M S E t r_{i+3}^{G A}}\right) * P C F t r_{i+3}^{E D A}
$$

The second dynamic ratio is without the dividing the population, and in this approach, the population would be integrated, and each algorithm would advance the training of the ANN individually. At the end of the training session in each iteration, the effectiveness would be achieved from the artificial neural network coefficients.

$$
P C F t s_{i+3}=\left(\frac{M S E t r_{i+3}^{E D A}}{M S E t r_{i+3}^{E D A}+M S E t s_{i+3}^{G A}}\right) * P C F t s_{i+3}^{G A}+\left(\frac{M S E t r_{i+3}^{G A}}{M S E t r_{i+3}^{E D A}+M S E t r_{i+3}^{G A}}\right) * P C F t s_{i+3}^{E D A}
$$

# 2.4. Training the $A N N$ 

For training the ANN the three algorithms as mentioned above - GA, EDA, and hybrid GA-EDA methods - could be used. The ratios which are obtained from the training would be used as final ratios in the ANN algorithm if each of the algorithms used individually. But in the hybrid algorithm, each model would have a fraction of the dynamic ratio which could be changed according to their accuracy. The mean square error (MSE) method has been used for the portion of each algorithm. After training the ANN model and achieving the optimum ratios, the next step would be prediction the new data according to their similarity with the ANN input data and put them in one cluster.

In this paper, the project is divided into 20 equal parts, and the cash flow model prediction would be achieved by using of artificial neural network method in these 20 parts. The cost of the project in three first periods ( $5 \%, 10 \%$, and $15 \%$ physical progress) would be considered to the start point. The cost of these first periods is used for the estimation of the cost of $20 \%$ physical progress. In the next step, for prediction $25 \%$ point, the prior four points $(5 \%, 10 \%, 15 \%$, and $20 \%$ ) are used. In each progress, the previous points from the beginning are considered in the calculations. It would lead to precise prediction results, and it would have lower errors in comparison with previous prediction models. The prediction algorithm is presented and i parameter is used as a counter for the cost of each part of the project:

$$
\begin{aligned}
& \operatorname{PCF}_{i+3}^{G A}=\operatorname{EHNN}^{G A}\left(\operatorname{ACFtr}_{1}, \operatorname{ACFtr}_{2}, \ldots, \operatorname{ACFtr}_{i+2}\right) \\
& \operatorname{PCFtr}_{i+3}^{G A}=\operatorname{EHNN}^{G A}\left(\operatorname{ACFtr}_{1}, \operatorname{ACFtr}_{2}, \ldots, \operatorname{ACFtr}_{i+2}\right) \\
& \operatorname{PCFts}_{i+3}^{G A}=\operatorname{EHNN}^{G A}\left(\operatorname{ACFtr}_{1}, \operatorname{ACFtr}_{2}, \ldots, \operatorname{ACFtr}_{i+2}\right) \\
& \operatorname{MSEtr}_{i+3}^{G A}=\left\langle\sum_{i=1}^{\operatorname{tr}}\left(\left(\operatorname{ACFtr}_{i+3}-\operatorname{PCFtr}_{i+3}^{G A}\right) / \operatorname{ACFtr}_{i+3}\right)^{\wedge} 2\right) / \mathrm{N}_{\mathrm{tr}}\right) \\
& \text { Error_PCFtr }_{i+3}^{G A}=\operatorname{PCFtr}_{i+3}^{G A}-\operatorname{ACFtr}_{i+3} \\
& \operatorname{PCF}_{i+3}^{\text {EDA }}=\operatorname{EHNN}^{\text {EDA }}\left(\operatorname{ACFtr}_{1}, \operatorname{ACFtr}_{2}, \ldots, \operatorname{ACFtr}_{i+2}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \operatorname{PCFtr}_{i+3}^{\mathrm{EDA}}=\mathrm{EHNN}^{\mathrm{EDA}}\left(\mathrm{ACFtr}_{1}, \mathrm{ACFtr}_{2}, \ldots, \mathrm{ACFtr}_{\mathrm{i}+2}\right) \\
& \mathrm{PCFts}_{i+3}^{\mathrm{EDA}}=\mathrm{EHNN}^{\mathrm{EDA}}\left(\mathrm{ACFtr}_{1}, \mathrm{ACFtr}_{2}, \ldots, \mathrm{ACFtr}_{\mathrm{i}+2}\right) \\
& \mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}=\left(\sum_{i=1}^{\operatorname{tr}}\left(\left(\mathrm{ACFtr}_{\mathrm{i}+3}-\mathrm{PCFtr}_{\mathrm{i}+3}^{\mathrm{EDA}}\right) / \mathrm{ACFtr}_{\mathrm{i}+3}\right)^{\wedge} 2\right) / \mathrm{N}_{\mathrm{tr}} \text { ) } \\
& \text { Error_PCFtr }_{\mathrm{i}+3}^{\mathrm{EDA}}=\mathrm{PCFtr}_{\mathrm{i}+3}^{\mathrm{EDA}}-A C F t r_{\mathrm{i}+3} \\
& \mathrm{PCFtr}_{\mathrm{i}+3}=\left(\frac{\mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}}{\mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}+\mathrm{MSEtr}_{i+3}^{\mathrm{EA}}}\right) * \mathrm{PCFtr}_{\mathrm{i}+3}^{\mathrm{GA}}+\left(\frac{\mathrm{MSEtr}_{i+3}^{\mathrm{GA}}}{\mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}+\mathrm{MSEtr}_{i+3}^{\mathrm{GA}}}\right) * \mathrm{PCFtr}_{\mathrm{i}+3}^{\mathrm{EDA}} \\
& \mathrm{PCFts}_{\mathrm{i}+3}=\left(\frac{\mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}}{\mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}+\mathrm{MSEtr}_{i+3}^{\mathrm{GA}}}\right) * \mathrm{PCFts}_{\mathrm{i}+3}^{\mathrm{GA}}+\left(\frac{\mathrm{MSEtr}_{i+3}^{\mathrm{GA}}}{\mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}+\mathrm{MSEtr}_{i+3}^{\mathrm{GA}}}\right) \\
& * \mathrm{PCFts}_{\mathrm{i}+3}^{\mathrm{EDA}} \\
& \text { Error }_{\mathrm{PCFtr}_{\mathrm{i}+3}}=\left(\frac{\mathrm{MSEtr}_{\mathrm{i}+3}^{\mathrm{EDA}}}{\mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}+\mathrm{MSEtr}_{i+3}^{\mathrm{GA}}}\right) * \text { Error }_{\mathrm{PCFtr}_{\mathrm{i}+3}}^{\mathrm{GA}}+\left(\frac{\mathrm{MSEtr}_{\mathrm{i}+3}^{\mathrm{GA}}}{\mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}+\mathrm{MSEtr}_{i+3}^{\mathrm{GA}}}\right) \\
& * \text { Error }_{\mathrm{PCFtr}_{\mathrm{i}+3}} \\
& \text { Mean_error_PECFtr }_{\mathrm{i}+3}=\left(\sum_{t r} \text { Error_PECFtr }\right) / N t r \\
& \text { PCF_New_Data }_{\mathrm{i}+3}=\left(\frac{\mathrm{MSEtr}_{\mathrm{i}+3}^{\mathrm{EDA}}}{\mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}+\mathrm{MSEtr}_{i+3}^{\mathrm{GA}}}\right) * \mathrm{EHNN}^{\mathrm{GA}}\left(\mathrm{ACF}_{1}^{\text {new data }}, \mathrm{ACF}_{2}^{\text {new data }}, \ldots, \mathrm{ACF}_{\mathrm{i}+2}^{\text {new data }}\right) \\
& +\left(\frac{\mathrm{MSEtr}_{\mathrm{i}+3}^{\mathrm{GA}}}{\mathrm{MSEtr}_{i+3}^{\mathrm{EDA}}+\mathrm{MSEtr}_{i+3}^{\mathrm{GA}}}\right) * \mathrm{EHNN}^{\mathrm{EDA}}\left(\mathrm{ACF}_{1}^{\text {new data }}, \mathrm{ACF}_{2}^{\text {new data }}, \ldots, \mathrm{ACF}_{\mathrm{i}+2}^{\text {new data }}\right) \\
& \mathrm{P}_{\mathrm{ACF}_{\mathrm{i}+3}}=\text { PCF_New_Data }_{\mathrm{i}+3}+\text { Mean_error_PCFtr }_{\mathrm{i}+3}
\end{aligned}
$$

# 2.5. ANN 

The artificial neural network moles are based on the human's biological neural system. The human's body neural system has single nodes which are neurons. Each of these neurons receives the information from the other neurons or external environment, then they process the data with an activation function, and a processes output would be provided for next neurons or nodes. This property of the information processing system in the neural networks makes them be a critical method for training from examples which could be used in the future case even not represented ones.

Assume that $x_{1}, x_{2}, \ldots, x_{n}$ are the input neurons and the $w_{1}, w_{2}, \ldots, w_{n}$ are their weights. These inputs with their weight could be used as vectors. The overall input signal is called as NETinput and it defines as follows:

$$
N E T=\sum w_{i} x_{i}
$$

The activation process on the NETwould be done by the activation function $(F)$ and the output signal would be as $F(N E T)$. One of the activation functions which is used in this paper is sigmoid function and it is illustrated as follow equation:

$$
F(N E T)=\frac{1}{1+e^{-\text {net }}} .
$$

The other activation functions are hyperbolic tangential function $\left(F(x)=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}\right)$, sinusoidal/cosine function $(F(x)=\sin x$ or $F(x)=\cos x)$, and liner function $(F(x)=x)$.

![img-1.jpeg](img-1.jpeg)

Fig. 2. The data input and output mapping in the cash flow
Table 1
The algorithm's parameters

# 3. Results and discussion 

The cash flow model is carried out by four different methods for training the artificial neural network. The methods are the genetic algorithm (GA), estimation of distribution algorithm (EDA), hybrid GAEDA model and the population is divided into these three methods, and the last one is hybrid GA-EDA without dividing the population. The error values are low and for better analyzing the accuracy of each method the logarithm value of the errors is shown in their related figures (Figs. 5, 8, 11, and 14)

### 3.1 Cash flow model by ANN method trained with the Genetic Algorithm

The cash flow estimation chart has two columns, the first one is the cash flow of the system and the second column is the hybrid algorithm with dividing the population. The cash flow prediction is shown in Fig. 3. The horizontal axis is the physical progress percentage of the project, and the vertical axis is the cost of the project. The mean absolute percentage error for the 17 periods is $\% 0.040$ and the mean absolute percentage error for the last period of the system is $\% 0.046$. The prediction error for the various percentage of physical progress is shown in Fig. 4. This point should be mentioned that each period error would have an effect on the other period's error. The calculated error for the first three periods is zero because these three points were the real values and they were used for the cash flow prediction. The logarithmic value of estimation errors is shown in Fig. 5.

![img-4.jpeg](img-4.jpeg)

Fig. 3. The cost of the project for each period using GA
![img-3.jpeg](img-3.jpeg)

Fig. 4. Cash flow prediction error using GA
![img-4.jpeg](img-4.jpeg)

Fig. 5. Logarithmic error of cash flow prediction using GA

# 3.2. Cash flow model by $A N N$ method trained with $E D A$ 

The cash flow model is represented by estimation of distribution algorithm with dividing the population.
![img-5.jpeg](img-5.jpeg)

Fig. 6.The cost of the project for each period using EDA
In Fig. 6, the prediction of the cash flow and the real cost of the project is shown for 20 portions of the physical progress. The mean absolute percentage error for the last 17 points is $\% 0.059$ and for the whole project is $\% 0.051$. The mean absolute percentage error and the percentage of the physical progress of the project are shown in Fig. 7 and Fig. 8.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Cash flow prediction error using EDA
![img-7.jpeg](img-7.jpeg)

Fig. 8. Logarithmic error of cash flow prediction using EDA

# 3.3. Cash flow model by ANN method trained with hybrid GA-EDA with diving the population 

In Fig. 9, the results of the hybrid GA-EDA prediction against and the cost of the project for 20 parts are shown. The population is divided and the average estimation error is $\% 0.047$ for the last 17 points and the mean error for the cost of the project is $\% 0.049$. The estimation errors are shown in Fig. 10. and the logarithmic value of the prediction errors are shown in Fig. 11.
![img-8.jpeg](img-8.jpeg)

Fig. 9. The cost of the project for each period using hybrid GA-EDA with dividing the population
![img-9.jpeg](img-9.jpeg)

Fig. 10. Cash flow prediction error using hybrid GA-EDA with dividing the population
![img-10.jpeg](img-10.jpeg)

Fig. 11. Logarithmic error of cash flow prediction using hybrid GA-EDA with dividing the population

# 3.4. Cash flow model by ANN method trained with hybrid GA-EDA without diving the population 

The hybrid GA-EDA algorithm is used for the prediction of the cash flow model in this section. The population is being considered without dividing it. The results of the hybrid algorithm are shown in Fig. 12, for 20 studied percentages. The mean estimation error for the cost of the 17 points is 0.022 and for the whole project is $\% 0.035$. The estimation errors are shown in Fig. 13 and Fig. 14 Modeling the cash flow without dividing the population has the best results, and it would be more realistic for further studies.
![img-11.jpeg](img-11.jpeg)

Fig. 12.The cost of the project for each period using hybrid GA-EDA without dividing the population
![img-12.jpeg](img-12.jpeg)

Fig. 13. Cash flow prediction error using hybrid GA-EDA with dividing the population
![img-13.jpeg](img-13.jpeg)

Fig. 14. Logarithmic error of cash flow prediction using hybrid GA-EDA with dividing the population

The results of the hybrid GA-EDA trained ANN method without dividing the population has the best performance by considering three main criteria which are mean absolute percentage error (MAPE), mean square error (MSE), and root means square error (RMSE). The results of the ANN method which is trained by GA model are in the second-place due to the aforementioned three parameters. The results of the EDA trained ANN method to have the lowest accuracy among the four training methods. The results of the MAPE, MSE, and RMSE are given in Tables 2-7.

Table 2
The MAPE, MSE, and RMSE parameters for GA (without exact value) trained ANN

Table 3
The MAPE, MSE, and RMSE parameters for GA (with exact value) trained ANN

Table 4
The MAPE, MSE, and RMSE parameters for EDA (without exact value) trained ANN

Table 5
The MAPE, MSE, and RMSE parameters for EDA (with exact value) trained ANN

Table 6
The MAPE, MSE, and RMSE parameters for hybrid GA-EDA trained ANN with diving the population with exact value
Table 7
The MAPE, MSE, and RMSE parameters for hybrid GA-EDA trained ANN without diving the population with exact value

# 4. Conclusion 

The cost of every project should be evaluated, and the spending features should be determined. The project could be influenced by cash flow estimation. The cash flow prediction is gained by studying the actual data and simulation it with appropriate algorithms such as the genetic algorithm. In this paper, artificial neural network (ANN) is chosen to be used in the forecasting path. Three algorithms are used for training the ANN model which are the genetic algorithm (GA), estimation distribution algorithm (EDA), and hybrid GA-EDA method. 996 airplane maintenance bases data are used as actual data, and after clustering them, 119 similar data is chosen. The best results from three algorithms are chosen to improve the performance. In the hybrid GA-EDA method, there should be a ratio between two algorithms to improve the model. The dynamic ratio is chosen in two forms. First one is the ratio with dividing the population into half and the second one is without dividing. For the second one, the ratio could be enhanced in each step. The project is divided into 20 equal parts, and the first three steps are used for predicting the fourth one. For instance, to predict the $30 \%$ point, five previous points are used $(5 \%, 10 \%, 15 \%, 20 \%$, and $25 \%)$. The best result is chosen by calculating three error amounts which are MAPE, MSE, and RMSE. The output of hybrid GA-EDA without dividing the population has the best result, and the values of MAPE, MSE, and RMSE are \%0.022, 28944.59 Dollars, and 837789503.79 Dollars, respectively. The accuracy of the GA, hybrid GA-EDA with dividing the population, and the EDA are lower than hybrid GA-EDA without dividing the population, respectively, by determining the three error amounts.
