# Enhanced Interactive Estimation of Distribution Algorithms with Attention Mechanism and Restricted Boltzmann Machine 

Lin Bao<br>School of Information and Control Engineering China University of Mining and Technology<br>Xuzhou, China<br>School of Electronics and Information<br>Jiangsu University of Science and Technology<br>Zhenjiang, China<br>baolin_zj@163.com<br>Dunwei Gong<br>School of Information and Control Engineering<br>China University of Mining and Technology<br>Xuzhou, China<br>dwgong@vip.163.com<br>Biao Xu<br>Department of Electronic Engineering<br>Shantou University<br>Shantou, China<br>xubiao@stu.edu.cn


#### Abstract

Interactive Estimation of Distribution Algorithm (IEDA), by integrating users interactions with Estimation of Distribution Algorithm, is powerful for efficient personalized search when the probability model and fitness function are well designed. We here propose an improved IEDA by using attention mechanism strengthened Restricted Boltzmann Machine (RBM). An attention mechanism assisted RBM model is constructed to approximate the user preferences by inputting item features and user generated contents. Then the attention-enhanced probability model of EDA and the fitness function are developed based on the RBM. In the evolutionary process, the attention-based RBM together with the probability model and fitness function are managed according to new interactions and corresponding information. The proposed algorithm is applied to real-world Amazon data sets usually used in the personalized search or recommendation, and its performance is experimentally demonstrated in better predicting the user preferences to improve the searching efficiency and accuracy.


Index Terms-Interactive Evolutionary Computations, Estimation of Distribution Algorithms, Personalized Search, Restricted Boltzmann Machine, Attention Mechanism

## I. INTRODUCTION

In recent years, with the rapid development of big data, cloud computing and other technologies, information has

This work was jointly supported by the National Natural Science Foundation of China under grants No. 61876184 and No. 61473298.

Xiaoyan Sun<br>School of Information and Control Engineering<br>China University of Mining and Technology<br>Xuzhou, China<br>xysun78@126.com

Yong Zhang<br>School of Information and Control Engineering<br>China University of Mining and Technology<br>Xuzhou, China<br>yongzh401@126.com

intelligence evaluations with traditional evolutionary optimization methods [3], [4]. Although IECs have been widely applied in many fields, these algorithms require users to participate in the interactive optimization process and perform explicit evaluations, which easily leads to user fatigue. Sun et al. [3] proposed a surrogate-assisted interactive genetic algorithms (IGAs) for handling complex design problems. Ashlock et al. [5] utilized the fertility technology to automatically generate the contents for alleviating user fatigue in IEC. Guo et al. [6] proposed interactive preference-based multi-objective evolutionary optimization for bolt supporting networks. As a result, IECs can only adopt smaller population and fewer evolutionary generations. Therefore, the reliability and accuracy of the evolutionary process and optimization results are not high, which limits the capability of IECs to solve the practical optimization problems in complex environments.

Restricted Boltzmann Machine (RBM) is an unsupervised stochastic neural network model with two-layer network, and has symmetrical connection and no self-feedback [7], [8]. In 2002, Hinton [9] proposed a fast learning algorithm for RBM, namely the Contrastive Divergence (CD) algorithm, which greatly improves the learning efficiency of RBM. RBM has been successfully applied in many fields. Salakhutdinov et al. [7] first used RBM to model users rating for movies, and proposed an efficient algorithm for movie recommendation. Shim et al. [10] presents an RBM-based Estimation of Distribution Algorithms (EDA) to enhance the scalability of multi-objective optimization. Bao et al. [11] proposed an EDA based on the RBM model to solve expensive optimization problems with discrete decision variables, but this method is not suitable for optimization problems with qualitative indicators. According to the strong representation learning and feature extraction of the improved RBM, we will further consider combing human intelligence with EDA to handle practical qualitative optimization problems such as personalized search. On the other hand, compared with Deep Neural Network (DNN), RBM has shorter training time and is easier to update dynamically. Therefore, it is feasible and efficient to apply RBM to extract users preference features in the complex environments of personalized search.

However, UGC in the big data environment has complex characteristics such as sparseness, incompleteness and dynamics, which makes it impossible for the UGC-oriented personalized search to obtain better recommendation results through simple data mining methods and traditional intelligent optimization algorithms. Combining user preference models and IECs is an effective method to deal with the personalized search [12], [13]. According to users interaction behaviors and the relevant information, a user interest model is built to obtain the user preferences and then provides the quantitative evaluation values for the searched objects, which drives the IECs evolutionary searching process. It will help users search for satisfactory solutions as soon as possible from the dynamical evolution space of massive data. Among them, building a user interest model that meets users potential needs and describes users personalized preferences is a key to effectively handle
the personalized search.
The commonly used methods that construct users interest models include Bayesian model [14], [15], RBM [7], [16], Convolutional Neural Network (CNN) [17], [18], and Autoencoder (AE) [19], [20], etc. Nguyen et al. [16] proposed the use of homogeneity to integrate social networks and RBMbased preference models to learn the potential representations of user preferences. Wu et al. [19] proposed a Collaborative Denoising Auto-encoder (CDAE) for top-N recommendation. These methods use UGC to build users interest models and have achieved good recommendation results. However, these algorithms assume that UGC is known and sufficient. The training complexity of the interest model is relatively large by integrating all the obtained UGC for model training. It is not conducive to tracking the dynamical changes of users preferences. In addition, UGC is relatively less used so that the trained interest model does not fully express users preferences. Therefore, considering effective interest modeling and designing efficient evolutionary strategies are of great significance for improving the performance of personalized search.

Inspired by the mechanism of human vision, Attention Mechanism (AM)-based neural networks have been successfully applied in image processing, natural language understanding, pattern generation and other fields [21]-[23]. Traditional neural network models have equal input weights for all inputs, and the models cannot make full use of important regional information. Nevertheless, AM can use weights to indicate the important degree of information and select more critical information in the model training process, which makes neural networks focus on these information and features. Zhou et al. [24] proposed an attention-based user behavior modeling framework (ATRank) for recommendation. Wang et al. [25] proposed a double most relevant attention network (DMRAN) to capture fine-grained user preferences for recommendation. These methods prove the effectiveness of the combination of AM and neural network in solving the personalized search and recommendation.

Motivated by these observations, using an RBM enhanced with AM to build a user preference model, this paper proposes an AM-based RBM-driven IEDA by combining with the IECs evolutionary optimization for personalized search, which is denoted as AtRBMIEDA. An AM-based RBM user preference model is constructed to extract user preference features by using users history behaviors and the related information. In the IEDA framework, a probability model from the RBM is presented to generate new individuals with the user preferences. Meanwhile, a surrogate model formed according to the energy of RBM is designed to estimate the individual fitness of the feasible solutions and alleviate users evaluation burden by partially replacing interactive evaluations. Considering the dynamical characteristics of users preferences, the AM-based RBM user preference model is updated with the increasing UGC. It guides the personalized evolutionary search process to efficiently and accurately search for users satisfaction solutions.

The main contributions of our work are as follows:

- The IEC is first designed here to solve the personalized search with user generated contents. Such an application is novel for the EC family, which will practically expand EC in the big data field.
- For effectively searching the UGC-based items, an AMbased RBM trained with UGC is built to model the dynamical evolution of user preferences, which can enhance the accuracy on user preference extraction and representation. This model is the foundation of the following IEDA implementation.
- The probability model and fitness surrogate used by EDA are obtained from the AM-based RBM. The probability of the input layer is employed to form the EDAs probability model and the energy function of the RBM is adapted to calculating the fitness surrogate. Apparently, the AM-based RBM not only provides a fitness surrogate but also an evolutionary operator for the EDA, which greatly improves the performance of IEDA in effectively searching the UGC described items.
The remainder of the paper is organized as follows. Section 2 introduces the related notations. The proposed AM-based RBM-driven IEDA is detailed in Section 3. Section 4 presents the comparative experiments and experimental analysis. The conclusion is then followed.


## II. Methodology

## A. Definition of Personalized Search Optimization Problem

The personalized search is to quickly search for users satisfaction solutions in the search space according to users potential requirements and interest preferences, and then make effective item recommendations. It is a kind of complex qualitative index optimization problems in essence, and can be defined as follows:

$$
\left\{\begin{array}{l}
f_{u}(\mathbf{x}) \\
\text { s.t. } u \in U, \mathbf{x} \in X
\end{array}\right.
$$

where $U=\left\{u_{1}, u_{2}, \cdots, u_{|U|}\right\}$ expresses the user set and $|U|$ is the number of users, and $X=\left\{\mathbf{x}_{1}, \mathbf{x}_{2}, \cdots, \mathbf{x}_{|X|}\right\}$ indicates the item set and $|X|$ is the number of items. The item (solution) $\mathbf{x}=\left[x_{1}, x_{2}, \cdots, x_{n}\right]$ has $n$ decision variables. $f_{u}(\mathbf{x})$ represents the preference degree of user $u$ for item $\mathbf{x}$, which cannot be accurately expressed by specific mathematical functions.

The personalized search is to generate a Top $N$ item recommendation list that meets users preferences, i.e., the set of $N$ items with higer $f_{u}(\mathbf{x})$. However, the item searching space is generally very large. It is the difficulty of the personalized search that how to accurately predict $f_{u}(\mathbf{x})$ and efficiently find out users satisfied solutions.

## B. User Preference Model: AM-based RBM

The AM-based RBM is designed here to accurately estimate the user preference model, and has 3 modules: RBM-based attention weight module, attention layer and AM-based RBM module. The structure of the proposed AM-based RBM user preference model is shown in Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. AM-based RBM User Preference Model
(1) RBM-based Attention Weight Module

The RBM-based attention weight model has a two-layer network: $\mathbf{v}_{1}$ is the visible layer and has $n$ visible units, which expresses the category features of items; $\mathbf{h}_{1}$ is the hidden layer and has $m_{1}$ hidden units, which indicates the user preference features. Among them, the layers are fully connected, and no connections exist in the layers. The visible units are binary values while the hidden ones are real values. The RBM model can produce effective learning representations even when processing sparse data.

According to users historical behaviors in UGC, the rating data of users for items is expressed as a matrix $\mathbf{R}$ :

$$
\mathbf{R}=\left[r_{i j}\right]_{|U| \times|X|}
$$

where $r_{i j}$ is the rating of user $u_{i}$ for item $\mathbf{x}_{j}$.
Users rating data clearly expresses the user preferences. The rating threshold $\delta$ is set. According to the historical ratings of the current user, the items more than $\delta$ are selected to form a dominant group $D(D \in X)$ with the user preference. $|D|$ is the number of $D$.

According to items category tags, the items in $X$ are represented as a vector $\mathbf{x}_{i}$,

$$
\mathbf{x}_{i}=\left[x_{i 1}, x_{i 2}, \cdots, x_{i j}, \cdots, x_{i n}\right]
$$

where $x_{i j}$ is the $j$-th tag of item $\mathbf{x}_{i}$. If $x_{i j}=1$, it means that $\mathbf{x}_{i}$ has the $j$-th tag; otherwise $x_{i j}=0 . n$ is the number of category tags in all items.

Items category tags describe some specific item features, and it indicates the user preferences to a certain extent. Ac-

cording to the coding mode of items, $|D|$ items (individuals) can be expressed as a $|D| \times n$ feature matrix $\mathbf{X}$ :

$$
\mathbf{X}=\left[\mathbf{x}_{1}, \mathbf{x}_{2}, \cdots, \mathbf{x}_{|D|}\right]^{T}, \mathbf{X} \in R^{|D| \times n}
$$

where $\mathbf{x}_{i}(i=1,2, \cdots,|D|)$ is the vector representation of item $\mathbf{x}_{i}$.

A set of training dataset $\mathbf{X}$ is the vector representations of the dominant group $D$. The RBM-based attention weight model is trained by the CD learning algorithm [9]. The active probabilities of the hidden and visible units are calculated:

$$
\begin{aligned}
P_{\theta_{1}}\left(h_{1 j}=1 \mid \mathbf{x}\right) & =\sigma\left(b_{1 j}+\sum_{i=1}^{n} x_{i} w_{1 i j}\right) \\
P_{\theta_{1}}\left(v_{1 i}=1 \mid \mathbf{h}_{1}\right) & =\sigma\left(a_{1 i}+\sum_{j=1}^{m_{1}} w_{1 i j} h_{1 j}\right)
\end{aligned}
$$

where $h_{1 j}$ and $v_{1 i}$ are the states of the $j$-th hidden unit in $\mathbf{h}_{1}$ and the $i$-th visible unit in $\mathbf{v}_{1}$, respectively. $w_{1 i j}$ is the connection weight between the visible unit $i$ and the hidden unit $j . b_{1 j}$ and $a_{1 i}$ is the bias vectors of the hidden unit $j$ and the visible one $i . \sigma(x)=1 /(1+\exp (-x))$ is the active function.

After training the RBM-based attention weight model, the model parameters $\theta_{1}=\left\{\mathbf{w}_{1}, \mathbf{a}_{1}, \mathbf{b}_{1}\right\}$ have the preference features of the current user.
(2) Attention Layer

The training dataset $\mathbf{X}$ is input into the trained RBM-based attention weight model again, and the output $V_{r b m_{1}}(\mathbf{x})$ of visible units is calculated,

$$
V_{r b m_{1}}(\mathbf{x})=\sigma\left(a_{1 i}+\sum_{j=1}^{m_{1}} w_{1 i j} \sigma\left(b_{1 j}+\sum_{i=1}^{n} x_{i} w_{1 i j}\right)\right)
$$

where $w_{1 i j}$ and $a_{1 i}$ are the parameters of the trained RBMbased attention weight model.

According to the self-attention mechanism mentioned in [18], the attention weight $A(\mathbf{x})$ of individual $\mathbf{x}$ is calculated:

$$
A(\mathbf{x})=\operatorname{softmax}\left(a\left(V_{r b m_{1}}(\mathbf{x}), \mathbf{w}_{1}\right)\right)
$$

where $\operatorname{softmax}()$ guarantees that the sum of all parts is 1 . The function $a\left(V_{r b m_{1}}(\mathbf{x}), \mathbf{w}_{1}\right)$ measures the attention weights of the user preferences on individual $\mathbf{x}$, and is calculated as follows:

$$
a\left(V_{r b m_{1}}(\mathbf{x}), \mathbf{w}_{1}\right)=V_{r b m_{1}}(\mathbf{x}) \cdot \mathbf{w}_{1}^{T}
$$

The attention weight $A(\mathbf{x})$ expresses the preference degree of the current user for decision variables in individual $\mathbf{x}$. The attention layer considers the attention weight $A(\mathbf{x})$ to obtain the integrated attention weights $A \mathbf{t}(\mathbf{x})$ of the individual $\mathbf{x}$ in $\mathbf{X}$.

$$
A \mathbf{t}(\mathbf{x})=\left[a t\left(\mathbf{x}_{1}\right), a t\left(\mathbf{x}_{2}\right), \cdots, a t\left(\mathbf{x}_{|D|}\right)\right]^{T}
$$

where at $\left(\mathbf{x}_{i}\right)$ is the AM-based attention weights of individual $\mathbf{x}_{i}(i=1,2, \cdots,|D|)$,

$$
a t\left(\mathbf{x}_{i}\right)=\mathbf{x}_{i}+A\left(\mathbf{x}_{i}\right) \times \mathbf{x}_{i}
$$

The current user has different preferences for the attribution features of items so that she/he expresses a preference dependency on the decision variables of individuals. The attention layer extracts and integrates the attention weight $A(\mathbf{x})$ of users on the decision variables of items. The AM-based attention weights $A \mathbf{t}(\mathbf{x})$ will be used as the input of the AM-based RBM module.
(3) AM-based RBM Module

The structure of the AM-based RBM model is similar to that of the RBM-based attention weight model, but the visible and hidden units in the AM-based RBM model are both real values. Integrating the AM by the attention layer, the AMbased representations $A \mathbf{t}(\mathbf{x})$ of the individuals in $D$ are used as the training data to train the AM-based RBM use preference model. It will focus on important features to precisely express the user preference features.

The active probabilities of the hidden and visible units are calculated as follows:

$$
\begin{aligned}
& P_{\theta_{2}}\left(h_{2 j}=1 \mid \mathbf{x}\right)=\sigma\left(b_{2 j}+\sum_{i=1}^{n} x_{i} w_{2 i j}\right) \\
& P_{\theta_{2}}\left(v_{2 i} \mid \mathbf{h}_{2}\right)=N\left(a_{2 i}+\sum_{j=1}^{m_{2}} w_{2 i j} h_{2 j}, 1\right)
\end{aligned}
$$

The AM-based RBM user preference model integrates the attention weights of user preferences to enhance the importance of effective information in building a user preference model, which effectively focuses on valuable features to extract the user preferences. The parameters of the trained AMbased RBM user preference model are $\theta_{2}=\left\{\mathbf{w}_{2}, \mathbf{a}_{2}, \mathbf{b}_{2}\right\}$, which contains the user preferences for next evolutionary optimization.

## C. RBM-based Probability Model of IEDA

A RBM-based probability model is designed as the probability model of EDA to generate new individuals with the user preferences in the IEDA framework. According to the AMbased RBM user preference model, a RBM-based probability model $P_{u}(\mathbf{x})$ is calculated,

$$
P_{u}(\mathbf{x})=\sigma\left(\sum_{i=1}^{|D|}\left(V_{r b m_{2}}\left(\mathbf{x}_{i}\right)+\operatorname{softmax}\left(\mathbf{x}_{i} \cdot \mathbf{w}_{2}{ }^{T}\right)\right)\right)
$$

where $V_{r b m_{2}}(\mathbf{x})=\sigma\left(a_{2 i}+\sum_{j=1}^{m_{2}} w_{2 i j} \sigma\left(b_{2 j}+\sum_{i=1}^{n} x_{i} w_{2 i j}\right)\right)$.
$P_{u}(\mathbf{x})$ represents the user preferences on items from the perspective of the probability. During the IEAD process, Pop new individuals with the user preferences are generated by randomly sampling $P_{u}(\mathbf{x})$. Then, according to the Pearson correlation coefficient, the same items or similar to new individuals in the search space are screened out to form a set of feasible individuals $S$. It greatly reduces the searching scope for further searching users satisfied solutions.

## D. RBM-based Surrogate Model

In IEDA, the individual fitness of items represents the preference degree of the current user on items, and cannot be exactly defined by mathematical functions. The user need provide inaccurate values to express the user preferences by cognitive experiences and interest preferences, and the given values are used as the individual fitness of the user on items. In general, the number of individuals in EDA is large so as to aggravate the evaluation burden and psychological fatigue of the current user. It may be make the user feel tired of interactive evaluations and thus give up the personalized search. Therefore, we will propose a quantitative transformation model of the qualitative evaluation indicators, called as a RBM-based surrogate model, to estimate the individual fitness and predict the ratings of users on items. It will partially alleviate users evaluation burden by replacing the real ratings of users for items in the interactive evolution process.

The surrogate input is the decision variables $\mathbf{x}=$ $\left[x_{1}, x_{2}, \cdots, x_{n}\right]$ of individual $\mathbf{x}$. Its output is the estimated value $\hat{f}_{u}(\mathbf{x})$ of the current user for individual $\mathbf{x}$, indicating the preference degree of the user on item $\mathbf{x}$. According to the energy function $E_{\theta_{2}}\left(\mathbf{x}, \mathbf{h}_{2}\right)$ [13], the RBM-based surrogate model $\hat{f}_{u}(\mathbf{x})$ is designed to estimate the individual fitness.

$$
\hat{f}_{u}(\mathbf{x})=\sigma\left(\frac{\max \left(E_{\theta_{2}}\right)-E_{\theta_{2}}\left(\mathbf{x}, \mathbf{h}_{2}\right)}{\max \left(E_{\theta_{2}}\right)-\min \left(E_{\theta_{2}}\right)}\right)
$$

where $\max \left(E_{\theta_{2}}\right)$ and $\min \left(E_{\theta_{2}}\right)$ are the maximum and minimum values of the energy function of all individuals in the feasible itemset $S$, respectively.

According to the RBM-based surrogate model $\hat{f}_{u}(\mathbf{x})$, the individual fitness in $S$ is estimated to predict the ratings of the user on new unrated items. Then, $N$ excellent individuals are selected by the elite selection strategy to generate a TopN item recommendation list that the current user may be interested in.

In the early stages of IEDA, users preference information is insufficient and the extracted user preference features are relatively rough. On the other hand, users requirements and preferences become clearer or may even dynamical change along with increasing information and complex environment. In order to accurately obtain the dynamic of users interest preferences, the AM-based RBM user preference model and other corresponding models are updated by new UGC to track the user preferences for guiding the IEDA evolutionary direction. The proposed algorithm gradually helps the current user to search for satisfied solutions to implement the personalized search.

## E. Implementation of the Proposed Algorithm

The pseudocode of the proposed AtRBMIEDA algorithm is presented in Algorithm 1.

## III. EXPERIMENTS AND RESULTS

## A. Experimental Settings

In order to verify the comprehensive performance of the proposed algorithm, Some real-world datasets in different

## Algorithm 1 Pseudocode of AtRBMIEDA

Input: UGC and the current user $u$
Output: TopN item list for user $u$

1: Initialization: The items in historical behaviors are screened out to form the dominant group $D$.
2: Data Preprocessing: The item category tags in $D$ are coded to build the training dataset $\mathbf{X}$.
3: User Preference Model: The AM-based RBM user preference model is constructed and trained with the method in Section 2.2.
4: Probability Model: The RBM-based probability model $P_{u}(\mathbf{x})$ is designed by the method in Section 2.3.
5: while Termination conditions are not met do
6: Population Updating: New individuals are generated by sampling $P_{u}(\mathbf{x})$, and the feasible itemset $S$ is formed in the searching space.
7: Surrogate Model: The RBM-based surrogate model $\hat{f}_{u}(\mathbf{x})$ is designed by the method in Section 2.4 to estimate the individual fitness in $S$.
8: Recommendation List: $N$ excellent individuals are selected by the elite selection strategy to generate a TopN item list.
9: Interactive Evaluations: The TopN list is submitted to user $u$ for interactive evaluations. Then, the dominant group $D$ is updated by new UGC.
10: Model Management: The surrogate model is evaluated. If the average accuracy does not meet the requirements, go to the step 3 for updating the corresponding models.
11: return TopN item list
fields are used, such as MovieLens-latest-small in MovieLens datasets, Kindle_Store and CDs_and_Vinyl in Amazon datasets [26], for the personalized search. The experimental environment is a Dell computer with an Intel Core i5-4590 CPU 3.30 GHz and 4 GB RAM, and the experimental platform is developed using Python 3.6. Evaluation indicators, such as Root Mean Square Error (RMSE), Hit Ratio (HR), Average Precision (AP) and Mean Average Precision (MAP), are used to demonstrate the comprehensive performance of the algorithms.

In the experiments, Random, Popularity, BPRMF [14], ConvMF [17], ATRank [24] and RBMEDA [11] algorithms are used as comparative algorithms. Both Random and Popularity are non-personalized methods, which can be used as benchmarks to measure the performance of other personalized search algorithms. BPRMF, ConvMF, and ATRank are recommendation algorithms based on supervised learning, while RBMEDA is an unsupervised learning method. The parameters of our algorithm are listed in Table 1.

## B. Performance of AM-based RBM user preference model

We have conducted a large number of experiments to verify the feasibility and effectiveness of the AM-based RBM user preference model and the RBM-based surrogate model.

TABLE I
EXPERIMENTAL PARAMETERS OF OUR ALGORITHM

| Parameter | Value |
| :--: | :--: |
| \# of visible units | Number of tags |
| \# of hidden units | $(0.8-1.2)$ Number of visible units |
| Learning rate | 0.1 |
| Momentum | $0.5-0.9$ |
| \# of training epochs in RBM | 20 |
| Population size | 60 |
| Top/N | 10 |

Our algorithm designed for recommendations is denoted as AtRBM while our algorithm without AM is signed as RBM. Ten users are randomly selected from the dataset and the corresponding ratings are sorted by the timestamp. Then, the train and test datasets are divided into $70 \%$ and $30 \%$ respectively. Various popular recommendation algorithms are used to conduct the personalized search for test users. Each algorithm is independently run for 10 times, and the average results are recorded to show in Table 2. The best values are bolded.

In Table 2, the results marked with * represent that the corresponding algorithm is significantly from the best result with confidence level 0.95 under the Mann-Whitney U test. From Table 2, the following observations can be obtained:
(1) The proposed AtRBM has obtained the optimal results in most datasets, which is superior to all other algorithms for recommendations. For example, AtRBM reaches the best RMSE 1.286 in Kindle_Store, which is $43.70 \%$ lower than BPRMF. Meanwhile, the HR and MAP values of AtRBM get the optimal values of 0.0310 and 0.950 respectively, which is $10.32 \%$ and $9.79 \%$ higher than BPRMF.
(2) AtRBM is a personalized search algorithm based on unsupervised learning, and has attained better than these supervised learning methods. In addition, ConvMF is extremely time consuming because it is a DNN-based algorithm. In comparison, the proposed algorithm utilizes the RBMbased method to greatly shorten the time cost of personalized searching while ensuring better prediction accuracy and recommendation results.
(3) AtRBM is significantly better than RBMEDA in all the datasets. It indicates that considering AM into the user preference model is beneficial for extracting users preference features to improve the performance of the personalized search algorithm.

In general, our algorithm outperforms other comparative algorithms and achieves a good prediction and recommendation accuracy for the personalized search.

## C. Performance of the Proposed Algorithm

In order to demonstrate the comprehensive performance of the proposed AtRBMIEDA, a user is randomly selected to participate in the interactive personalized search. The rated items of the user are sorted by the timestamp. The first $50 \%$ of these items is built as a training dataset, of which the first $20 \%$ is used as the initial historical interactions and the last
$30 \%$ is divided into 10 copies as new UGC for each iteration. The remaining $50 \%$ of those is regarded as the feasible searching space for the personalized search. The AtRBM and AtRBMIEDA algorithms conduct the personalized search for the user, respectively. The experimental results in Kindle_Store are shown in Fig. 2.

As can be seen from Figure 2, the HR and AP values of AtRBMIEDA have been greatly improved compared with AtRBM. Therefore, by combining IEDA, AtRBMIEDA is obviously superior to AtRBM for the personalized search.

Furthermore, AtRBMIEDA is compared with four IECs algorithms, such as traditional IEDA, RBM-assisted IGA (RBMIGA), RBMEDA [11], and RBMIEDA without AM (denoted as RBMIEDA). Each algorithm evolves 10 generations, and gives 10 predictions and recommendations for the current user. All the algorithms are independently run 10 times. The average results are shown in Table 3, and the best results are marked in bold.

In Table 3, the results marked with * represent that the corresponding algorithm is significantly from the best result with confidence level 0.95 under the Mann-Whitney U test. IEDA does not have the RMSE values since no surrogate model is built to predict the ratings of items. The following observations can be obtained from Table 3.
(1) RBMIGA generates new individuals in the IGA framework and uses the RBM-based surrogate model to estimate the individual fitness to guide the evolutionary optimization. Compared with RBMIGA, RBMEDA replaces IGA by IEDA to produce the suitable items with users preferences to get better searching results.
(2) AtRBMIEDA achieves the best results in all of the datasets. For example, AtRBMIEDA achieves the best RMSE 1.421 in CDs_and_Vinyl, which is $5.52 \%$ lower than RBMIEDA. The HR and MAP values get the optimal values 0.00510 and 0.982 respectively, which is $10.15 \%$ and $7.32 \%$ higher than RBMIEDA. It indicates that integrating AM enhances the performance of extracting the user preferences of the RBMbased user preference model and improves the prediction and recommendation accuracy of AtRBMIEDA.

In order to further demonstrate the performance of the proposed algorithm, each IECs algorithm iterates 10 times with 10 times of the rating prediction and item recommendations. The personalized searching processes of a user in Kindle_Store and CDs_and_Vinyl are shown in Fig. 3 and Fig. 4 respectively.

As can be seen from Fig. 3 and Fig. 4, AtRBMIEDA significantly outperforms other compared algorithms and achieves better prediction accuracy and recommendation results in the personalized search. For example, its RMSE is lower than other IECs methods, and the HR and AP values are both higher than these methods. The evaluation indicators are better and better along with iterations, which indicates the performance of AtRBMIEDA is gradually improved with the increasing UGC information. In addition, AtRBMIEDA has reached a high level of HR and AP after an iterative search. It means that the user may be have found satisfactory solutions and thus implements the personalized search. Since the experiments show 10

TABLE II
EXPERIMENTS COMPARED WITH POPULAR RECOMMENDATION ALGORITHMS

| Algorithm | MovieLens-latest-small |  |  |  | Kindle_Store |  |  |  | CDs_and_Vinyl |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | RMSE | HR | MAP | Time(s) | RMSE | HR | MAP | Time(s) | RMSE | HR | MAP | Time(s) |
| Random | - | 0.0238 | 0.479 | 0.023 | - | 0.0298 | 0.914 | 0.014 | - | 0.0119 | 0.847 | 0.016 |
| Popularity | 2.309 | 0.0343 | 0.518 | 0.625 | 4.319 | 0.0222 | 0.922 | 0.761 | 4.218 | 0.0123 | 0.825 | 3.833 |
| BPRMF | 1.425 | 0.0246 | 0.426 | 7.897 | 2.264 | 0.0278 | 0.857 | 1.205 | 2.182 | 0.0101 | 0.826 | 5.406 |
| CunMF | 3.023 | 0.0256 | 0.589 | 123.67 | 4.317 | 0.0221 | 0.833 | 416.532 | 4.217 | 0.0107 | 0.817 | 884.519 |
| ATRank | 2.256 | 0.0287 | 0.603 | 2.356 | 2.213 | 0.0301 | 0.900 | 8.745 | 2.694 | 0.0108 | 0.844 | 32.307 |
| RBMEDA | 1.016 | 0.0261 | 0.428 | 0.546 | 1.433 | 0.0292 | 0.909 | 10.060 | 1.480 | 0.0110 | 0.837 | 5.345 |
| RBM | 1.020 | 0.0266 | 0.517 | 1.068 | 1.397 | 0.0299 | 0.876 | 23.052 | 1.247 | 0.0111 | 0.816 | 1.224 |
| AtRBM | 1.015 | 0.0373* | 0.583* | 1.136 | 1.286* | 0.0310* | 0.950* | 26.467 | 1.224* | 0.0127* | 0.913* | 2.173 |

![img-1.jpeg](img-1.jpeg)

Fig. 2. Experiment in Kindle_Store

TABLE III
EXPERIMENTAL RESULTS AMONG COMPARED IECs

| Algorithm | MovieLens-latest-small |  |  |  | Kindle_Store |  |  | CDs_and_Vinyl |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | RMSE | HR | MAP | RMSE | HR | MAP | RMSE | HR | MAP |  |  |
| IEDA | - | 0.00761 | 0.547 | - | 0.00756 | 0.752 | - | 0.00396 | 0.818 |  |  |
| RBMARGA | 0.970 | 0.00865 | 0.567 | 0.823 | 0.00767 | 0.754 | 1.506 | 0.00447 | 0.897 |  |  |
| RBMEDA | 0.968 | 0.00807 | 0.510 | 0.819 | 0.00778 | 0.755 | 1.504 | 0.00463 | 0.915 |  |  |
| RBMIEDA | 1.001 | 0.00763 | 0.524 | 0.759 | 0.00789 | 0.783 | 1.476 | 0.00430 | 0.872 |  |  |
| AtRBMIEDA | $0.992^{*}$ | 0.01027* | 0.660* | 0.689* | 0.00809* | 0.814* | 1.421* | 0.00510* | 0.982* |  |  |

times of interactive searching for simulating the personalized search of the current user, the HR and AP of AtRBMIEDA are relatively high after an iteration. Sometimes the HR and AP of AtRBMIEDA decrease after two or three iterations. This is because users interests and preferences are dynamically changing along with interactive behaviors. Meanwhile, the dynamical evolution of the user preference model requires the accumulation of a certain amount of available information so that the HR and AP values fluctuate in the iteration process of the personalized search. However, the general trend of these metrics of AtRBMIEDA is getting better and better along with interactive iterations. Therefore, the proposed algorithm is superior to other comparative methods.

In summary, the proposed algorithm effectively extracts the user preference features and efficiently tracks the dynamic of users preferences to achieve the personalized search. At the same time, it alleviates users evaluation burden and psychological fatigue to obtain better experiences.

## IV. Conclusions

This paper proposes an AM-based RBM-driven IEDA algorithm for the personalized search. By exploiting users
interactive behavior data in UGC, an AM-based RBM user preference model is constructed to focus on the important attribution features to effectively extract users preferences. Then, the corresponding RBM-based probability and surrogate models are presented to generate the feasible solutions with users preferences to estimate the individual fitness of the feasible solutions for guiding the evolution of personalized search. For verifying the feasibility and effectiveness of the proposed algorithm, a large number of experiments are conducted for personalized search in various real-world datasets. It further deepens and enriches the theory and application of evolutionary optimization. In the future research, integrating model-based recommendation method into intelligent evolutionary optimization, it is expected to take advantage of text comments, images and other information to improve the performance of personalized search.

## ACKNOWLEDGMENT

This work was jointly supported by the National Natural Science Foundation of China under grants No. 61876184 and No. 61473298.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Metric Variations v.s. Iterations on Kindle_Store
![img-3.jpeg](img-3.jpeg)

Fig. 4. Metric Variations v.s. Iterations on $\mathrm{CDs} \_$and_Vinyl

## REFERENCES

[1] J. Lu, D. S. Wu, M. S. Mao, W. Wang, and G. Q. Zhang, "Recommender system application developments: A survey," Decision Support Systems, vol. 74, pp. 12-32, 2015.
[2] Z. Batmaz, A. Yurekli, A. Bilge, and C. Kaleli, "A review on deep learning for recommender systems: challenges and remedies," Artificial Intelligence Review, vol. 52, no. 1, pp. 1-37, 2019.
[3] X. Y. Sun, D. W. Gong, Y. C. Jin, and S. S. Chen, "A new surrogateassisted interactive genetic algorithm with weighted semisupervised learning," IEEE Transactions on Cybernetics, vol. 43, no. 2, pp. 685-698, 2013.
[4] Y. Chen, X. Y. Sun, D. W. Gong, and X. J. Yao, "DPM-IEDA: Dual Probabilistic Model Assisted Interactive Estimation of Distribution Algorithm for Personalized Search," IEEE Access, vol. 7, pp. 4100641016, 2019.
[5] D. Ashlock, J. Alexander Brown, and L. Sultanaeva, "Exploiting Fertility to Enable Automatic Content Generation to Ameliorate User Fatigue in Interactive Evolutionary Computation," 2018 IEEE Congress on Evolutionary Computation (CEC), 2018, pp. 1-7.
[6] Y. N. Guo, X. Zhang, D. W. Gong, Z. Zhang, and J. J. Yang, "Novel Interactive Preference-based Multi-objective Evolutionary Optimization for Bolt Supporting Networks," IEEE Transactions on Evolutionary Computation, in press.
[7] R. Salakhutdinov, A. Mnih, and G. Hinton, "Restricted Boltzmann machines for collaborative filtering," In Proceedings of the 24th International Conference on Machine learning (ICML 07), 2007, pp. 791C798.
[8] M. Probst, F. Rothlauf, and J. Grahl, "Scalability of using Restricted Boltzmann Machines for combinatorial optimization," European Journal of Operational Research, vol. 256, no. 2, pp. 368-383, 2017.
[9] G. E. Hinton, "Training products of experts by minimizing contrastive divergence," Neural Computation. vol. 14, no. 8 pp. 1771C1800, 2002.
[10] V. A. Shim, K. C. Tan, C. Y. Cheong, and J. Y. Chia, "Enhancing the scalability of multi-objective optimization via restricted Boltzmann machine-based estimation of distribution algorithm," Information Sciences, vol. 248, pp. 191-213, 2013.
[11] L. Bao, X. Y. Sun, Y. Chen, G. Y. Man, and H. Shao, "Restricted Boltzmann Machine-Assisted Estimation of Distribution Algorithm for Complex Problems," Complexity, in press.
[12] Y. Chen, X. Y. Sun, D. W. Gong, Y. Zhang, J. Choi, and S. Klasky, "Personalized Search Inspired Fast Interactive Estimation of Distribution

Algorithm and Its Application," IEEE Transactions on Evolutionary Computation, vol. 21, no. 4, pp. 588-600, 2017.
[13] X. Y. Sun, Y. Chen, L. Bao, and R. D. Xu, "Interactive genetic algorithm with implicit uncertainty evaluation for application in personalized search," 2017 IEEE Symposium Series on Computational Intelligence (SSCI), Honolulu, HI, 2017, pp. 1-8.
[14] S. Rendle, C. Freudenthaler, Z. Gantner, and L. Schmidt-Thieme, "BPR: Bayesian personalized ranking from implicit feedback," In Proceedings of the 25th Conference on Uncertainty in Artificial Intelligence, 2012, pp. 452-461.
[15] H. Wang, N. Y. Wang, and D. Yeung, "Collaborative Deep Learning for Recommender Systems," In Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 15), 2015, pp. 1235C1244.
[16] T. T. Nguyen and H. W. Lauw, "Representation Learning for Homophilic Preferences," In Proceedings of the 10th ACM Conference on Recommender Systems (RecSys 16), 2016, pp. 317C324.
[17] D. Kim, C. Park, J. Oh, S. Lee, and H. Yu, "Convolutional Matrix Factorization for Document Context-Aware Recommendation," In Proceedings of the 10th ACM Conference on Recommender Systems (RecSys 16), 2016, pp. 233C240.
[18] G. Y. Pang, X. M. Wang, F. Hao, J. H. Xie, X. Y. Wang, Y. G. Lin, et al., "ACNN-FM: A novel recommender with attention-based convolutional neural network and factorization machines," Knowledge-Based Systems, vol. 181, 2019, in press.
[19] Y. Wu, C. DuBois, A. X. Zheng, and M. Ester, "Collaborative Denoising Auto-Encoders for Top-N Recommender Systems," In Proceedings of the Ninth ACM International Conference on Web Search and Data Mining (WSDM 16), 2016, pp. 153C162.
[20] D. Liang, R. G. Krishnan, M. D. Hoffman, and T. Jebara, "Variational Autoencoders for Collaborative Filtering," In Proceedings of the 2018 World Wide Web Conference (WWW 18), 2018, pp. 689C698.
[21] V. Mnih, N. Heess, A. Graves, and K. Kavukcuoglu, "Recurrent Models of Visual Attention," Advances in neural information processing systems, 2014.
[22] K. Xu, J. Ba, R. Kiros, K. Cho, A. Courville, R. Salakhutdinov, et al., "Show, attend and tell: Neural image caption generation with visual attention," Computer Science, pp. 2048-2057, 2015.
[23] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, et al., "Attention is all you need," In Proceedings of the 31st Conference on Neural Information Processing Systems, 2017, pp. 1-11.

[24] C. Zhou, J. Z. Bai, J. S. Song, X. F. Liu, Z. C. Zhao, X. S. Chen, et al., "ATRank: An attention-based user behavior modeling framework for recommendation," In Thirty-Second AAAI Conference on Artificial Intelligence, 2018.
[25] H. Z. Wang, G. F. Liu, A. Liu, Z, X. Li, and K. Zheng, "DMRAN: a hierarchical fine-grained attention-based network for recommendation," In Proceedings of the 28th International Joint Conference on Artificial Intelligence (IJCAI-19), 2019, pp. 3698-3704.
[26] R. He and J. McAuley, "Ups and Downs: Modeling the Visual Evolution of Fashion Trends with One-Class Collaborative Filtering," In Proceedings of the 25th International Conference on World Wide Web (WWW 16), 2016, pp. 507C517.