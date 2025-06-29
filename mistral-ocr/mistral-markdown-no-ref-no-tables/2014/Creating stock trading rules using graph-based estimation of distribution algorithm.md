# Creating Stock Trading Rules Using Graph-Based Estimation of Distribution Algorithm 

Xianneng Li, Wen He, and Kotaro Hirasawa<br>Graduate School of Information, Production and Systems, Waseda University, Japan<br>Email: \{sennou@asagi., hewen@toki., and hirasawa@\}waseda.jp


#### Abstract

Though there are numerous approaches developed currently, exploring the practical applications of estimation of distribution algorithm (EDA) has been reported to be one of the most important challenges in this field. This paper is dedicated to extend EDA to solve one of the most active research problems - stock trading, which has been rarely revealed in the EDA literature. A recent proposed graph-based EDA called reinforced probabilistic model building genetic network programming (RPMBGNP) is investigated to create stock trading rules. With its distinguished directed graph-based individual structure and the reinforcement learning-based probabilistic modeling, we demonstrate the effectiveness of RPMBGNP for the stock trading task through real-market stock data, where much higher profits are obtained than traditional non-EDA models.


## I. INTRODUCTION

In recent years, there has been a significant development of Estimation of Distribution Algorithm (EDA) [1], [2], [3], [4]. Different from the traditional evolutionary computation (EC) techniques which simulate the biological evolution for generating the new population stochastically, EDA focuses on building a probabilistic model from the perspective of machine learning (ML). The probabilistic model estimates the probability distribution of the current population, and is used to sample the new population. Currently, it has been demonstrated that EDA is capable of realizing significant speed-up of evolution efficiency comparing with traditional EC techniques when applying to solve many problems, i.e., function optimization [5], [6], bioinformatics [7], [8], multiobjective optimization [9], [10], scheduling [11], dynamic problems [12], continuous optimization [13], [14], program generation [15], [16], [17], [18], [19], information retrieval [20], etc.

Recently, a new type of EDA techniques called probabilistic model building genetic network programming (PMBGNP) [21], [22], [23] has been developed. Different from the existing EDA techniques which apply the concept of probabilistic modeling into bit-string structure based GA [24] and tree structure based GP [25], PMBGNP is dedicated to estimate the probability distribution of a more complex solution structure graph structure. Accordingly, it can be viewed as a graph-based EDA. PMBGNP applies a recent proposed EC technique, i.e., genetic network programming (GNP) [26], [27], [28], as the base model to construct its individuals. Following the research directions of EDA, the univariate [22], pairwise [29] and continuous PMBGNP [30] were proposed previously, which have also been studied in both theory [31] and applications [32], [33]. Different from the conventional EDA techniques,

PMBGNP is dedicated to solve a different sort of problems, that is, the intelligent agent control. In the previous research, it has been successfully applied to the benchmark problems [23] of the intelligent agent control, as well as the real mobile robot control [34], [35], where its superiority has been demonstrated in comparison with the traditional state-of-the-art techniques.

Beyond the much success of EDA in the past studies, it has been reported and accepted that one of its most important challenges is to explore its applications to solve wider range of problems [36], especially its real-world practical usage. Particularly, there have been numerous studies in applying the soft computing techniques to the stock trading task, such as GA [37], GP [38], [39], GNP [40], neural network (NN) [41], etc., which soon becomes one of the most active research problems. However, this problem has been rarely addressed in the EDA literature, where a gap remains to be filled.

In this paper, we are dedicating to develop an EDAbased stock trading model using PMBGNP. Particularly, an advanced version of PMBGNP called Reinforced PMBGNP (RPMBGNP) [23], [42] is utilized as the base technique to efficiently evolve the stock trading rules. RPMBGNP developed a reinforcement learning (RL)-based probabilistic modeling approach to estimate the probability distribution of its directed graphs, which showed efficient evolution ability for generating compact programs with decision-making rules.

The fundamental basis of the proposed model arises from that when developing an intelligent trading system, a large number of technical indices should be considered to track the movement of the real stock market which sometimes causes the dramatic expansion of the search space. However, due to its efficient scalability and evolution ability under large search space, EDA may provide significant improvement of evolution efficiency when comparing with standard EC techniques.

In the next section, the basic framework of the stock trading task is described. Section III introduces the proposed stock trading model based on RPMBGNP. The experimental studies using the real stock data are carried out in section IV. Finally, the conclusions are drawn in section V.

## II. BASIC FRAMEWORK OF Sтоск TRADING

Generally, the stock trading task has been focused on in two different aspects. One is the fundamental analysis, which focuses on analyzing the stock prices based on the overall state of macroeconomic markets. Another is the technical analysis which assumes that any factor that truly influences the market

will immediately show up in the movement of the stock prices. Though there are some theories addressing that no investor can achieve more than average trading advantages based on the historical information, i.e., the efficient-market hypothesis [43], it has been empirically verified that analyzing a large amount of historical data based on the technical indices can relatively capture the movement of the market [44], [45]. In this paper, we are focusing on the technical analysis to determine the timing of buying/selling signals of the stocks by creating trading rules using RPMBGNP.

## A. Technical Indices

The foundation of the technical analysis arises from the technical indices, each of which is a series of data points that are derived by applying a mathematical equation to the price data of the real market. The public price data of the stock market generally includes the following 5 types, that is, each day's open price, close price, high price, low price and the volume of trades. The technical indices are capable of offering different perspectives from which the underlying movement of prices is analyzed. Among many available choices, this paper applies 9 major technical indices for the stock trading task based on the empirical experience.

1) Rate of deviation (BIAS): BIAS is the rate of deviation from the average price over a period of time, which can estimate the possible correction or rebound of the price volatility. It can be calculated by

$$
B I A S(n)=(p-M A(n)) / M A(n)
$$

where $p$ is today's close price, and $M A(n)$ is the moving average of the last $n$ days computed by $M A(n)=\left(p+p_{-1}+\right.$ $\left.\ldots+p_{-(n-1)}\right) / n$, and $p_{-i}$ is the close price of $i$ days before.
2) Relative strength index (RSI): RSI focuses on capturing how strongly the stock is moving towards its current direction

$$
R S I(n)=\frac{\sum_{j=0}^{n-1} p_{-j}^{\prime}}{\sum_{i=0}^{n-1}\left|p_{-i}-p_{-(i+1)}\right|}
$$

where

$$
p_{-j}^{\prime}= \begin{cases}\left(p_{-j}-p_{-(j+1)}\right) & p_{-j}>p_{-(j+1)} \\ 0 & \text { otherwise }\end{cases}
$$

3) Rate of change (ROC): ROC measures the speed at which the stock price is changing

$$
R O C(n)=p / p_{-n}
$$

4) Volume ratio (VR): VR is a powerful metric to identify whether or not the stock is under accumulation

$$
V R(n)=\sum_{j=0}^{n-1} v_{-j}^{\prime} / \sum_{i=0}^{n-1} v_{-i}
$$

where $v_{-i}$ is the volume of $i$ days before, and

$$
v_{-j}^{\prime}= \begin{cases}v_{-j} & p_{-j}>p_{-(j+1)} \\ v_{-j} / 2 & p_{-j}=p_{-(j+1)} \\ 0 & p_{-j}<p_{-(j+1)}\end{cases}
$$

5) Rank correlation index (RCI): RCI focuses on the ranking and date of the stock prices to determine whether it is low or high. Let $d_{-i}$ denotes the differences between the rank of the stock price of $i$ days before and its date over a period of time, we can compute

$$
R C I(n)=1-\frac{6 \sum_{i=0}^{n-1} d_{-i}^{2}}{n\left(n^{2}-1\right)}
$$

6) Stochastic: Stochastic shows the location of each day's close price relative to the high-low range over several periods

$$
\text { Stochastic }(n)=\left(K_{0}(n)+K_{-1}(n)+K_{-2}(n)\right) / 3
$$

where $K_{-i}(n)=\left(p_{-i}-L O W\right) /(H I G H-L O W)$. LOW and $H I G H$ are the lowest and highest price of period from $i$ days before to $i+n$ days before.
7) Golden/Dead cross: It uses two MAs of the short-term and long-term periods to indicate the significant signals of buying and selling.
8) Moving average convergence and divergence (MACD): MACD is one of the most famous indices to spot the changes in the strength, direction and momentum of the price trend.
9) Candlestick chart: Candlestick chart has been widely used to indicate the fluctuation of the stock prices, which is utilized by the candles. 8 candlestick chart patterns introduced in [46] are utilized in this paper, which have shown attractive performance to predict the movement of the stock prices.

## B. Problem Formulation

The objective of the stock trading task is to maximize the profits by a given initial fund.

The input can be represented by the above described technical indices, while the output is the buying or selling action.

The target of this paper is to develop an intelligent trading model to recommend the most remunerative action for an perceived market situation. In other words, we are dedicating to provide the appropriate timing of buying and selling signals, where the recent advanced EDA named RPMBGNP is applied to construct and evolve the model.

## III. RPMBGNP-BASED STOCK TRADING MODEL

Inspired by original GNP, RPMBGNP represents the candidate stock trading models by its individuals with directed graph structures, which are subject to evolution to find the optimal ones to maximize the profits.

## A. Individual Structure

One of the main features of RPMBGNP different from traditional EDA techniques is its individual structures, where a distinguished directed graph of GNP is utilized.

The directed graph ensures strong expression ability to allow RPMBGNP to efficiently model the complex systems. The directed graph is composed of two kinds of nodes

- Judgment nodes: simulate the sensory functions to judge the environment.

![img-0.jpeg](img-0.jpeg)

Fig. 1: Directed graph structure

TABLE I: Judgment functions for stock trading


- Processing nodes: include the processing functions for the action determination.
Each node $i$ includes a set of parameters: $N T_{i} \in\{0,1\}$ is the node type ( 0 for judgment nodes and 1 for processing nodes); $N F_{i}$ denotes the node function read from a problem specific LIBRARY; $C_{i 1}, C_{i 2}, \ldots$ denotes the connected node from branch $1,2, \ldots$ of node $i ; T D_{i}$ and $t d_{i}$ represents the time delays spent on executing node $i$ or transiting its branches, respectively.

Each judgment node consists of multiple branches, each of which corresponds to a specific input perceived from the environment, while processing node does not consist of conditional branches, in other words, with only $C_{i 1}$.
$T D$ and $t d$ play the roles to model the agents with human like brain that needs the time for thinking. With time delays, the program can count the needed time units of executing its directed graph. In this paper, $T D=5$ or 1 for judgment or processing nodes, respectively, and $t d=0$. A trading day ends when 5 or more time units reached. In other words, the programs can execute " 5 judgment nodes" or "less than 5 judgment nodes with 1 processing node" per each trading day.

## B. LIBRARY (Judgment/Processing Functions)

In order to develop the stock trading model, the LIBRARY is prepared to define the judgment and processing functions based on the descriptions of section II.

The judgment functions are defined based on the listed 9 technical indices. However, as for the first 6 technical indices, $n$ is set to $5,13$ and 26 to track the relatively short-, medium-, and long-term movements of the stock prices, respectively. The number of branches in judgment nodes are determined based on the corresponding judgment functions and their perceived sensory results from the stock prices. Accordingly, they are total 21 judgment functions as listed in Table I.

Two processing functions are existed in the model, corresponding to the actions of buying or selling, respectively.

## C. Performance Component (Workflow of the Directed Graph)

Each stock trading model, represented by a directed graph, works as an intelligent agent. Initially, the model starts its execution from a predefined start judgment node, and the transition of the model continues depending on the judgment results and node connections.

When a judgment node is executed, it applies its judgment function to judge the current situation of the stock prices, and transits to another node by selecting a branch based on the
perceived value matching with Table I. After a number of judgment nodes, a processing node might be executed, leading to the trading behavior. During the transition of the directed graph, the time units are incrementally counted based on the time delays, which simulates the stream of trading days. The model is terminated if the final trading day arrives. Afterwards, the fitness value can be evaluated.

1) Importance Index: Since different technical indices have different ranges, Importance Index (IMX) [47] is used to transform the returned judgment values of the technical indices to a normalized interval $[-1,1]$. The IMX functions for each technical index used in this paper is based on the ones described in [47].
2) Creating trading actions: The processing nodes consist of the candidate trading actions, i.e., buying and selling, which are executed based on the node transitions and judgment results.

Each processing node $i$ consists of a processing function $N F_{i}$ and a numerical variable $v_{i} . N F_{i}$ could be 1 (buying) or 2 (selling), while $v_{i}$ denotes the trading signal of node $i$.

When processing node $i$ is transited, the strategy of stock trading of our model is carried out as follows:

1) First, we calculate the average IMX value $A$ of the judgment nodes transited from the previous processing node to the current processing node $i$ (the set of these judgment nodes is denoted by $I$ ). That is,

$$
A=\sum_{j \in I} I M X(j) /|I|
$$

2) Second, if $N F_{i}=1$ (buying),

- if $A \geq v_{i}$, buy stocks as much as possible.
- otherwise, just do nothing.

3) But, if $N F_{i}=2$ (selling),

- if $A<v_{i}$, sell stocks as much as possible.
- otherwise, just do nothing.


## D. Evolution Space

Each directed graph is encoded with set $N_{j}$ of judgment nodes and set $N_{p}$ of processing nodes, where the nodes can be connected arbitrarily to model complicated combinations of judgment and processing. In other words, it searches the optimal combination of technical indices to construct the stock trading model generated by a sequence of decision-making trading rules.

In this problem, evolution bias is applied to evolve the node connections and trading signal of each processing node. In other words, $C_{i 1}, C_{i 2}, \ldots$ for each node $i \in N_{j} \cup N_{p}$ and $v_{j}$ for each processing node $j \in N_{p}$ are subject to evolution to determine the optimal stock trading models. Accordingly,
Definition 1: The number of search variables $\Theta$ of GNP is defined by

$$
\Theta=\mathcal{B}+\mathcal{V}
$$

where $\mathcal{B}$ is the total number of branches of the directed graph, and $\mathcal{V}$ is the number of processing nodes, that is, $\left|N_{p}\right|$.
It is clear that the $\mathcal{B}$ variables are discrete ones, while $\mathcal{V}$ variables are in a continuous range, which result in a mixed optimization problem.

## E. Evolving $\mathcal{B}$ by RPMBGNP

In order to evolve the $\mathcal{B}$ discrete variables, a reinforcement learning (RL)-based EDA proposed in [23] is utilized. The proposed technique, named Reinforced PMBGNP (RPMBGNP ), is dedicated to learn knowledge/experience, i.e., $Q$ values, using RL [48] to measure the quality of node connections of the directed graph, where the $Q$ values are used to construct the probabilistic model of EDA to estimate a precise model with implicit multivariate interactions.
In RPMBGNP, each candidate stock trading model, i.e., a directed graph, is viewed as a policy of RL, where the node transitions are defined as an episode. We define a branch of the directed graph as the state of RL, where the action of RL is denoted as the selection of a node to be connected by a given branch (state). Accordingly, each model can be factorized by a sequence of state-action pairs (node connections)

$$
(S, A)=\left\{\left(s_{1}, a_{1}\right),\left(s_{2}, a_{2}\right), \ldots,\left(s_{L}, a_{L}\right)\right\}
$$

where $L$ is the length of the episode.
Each candidate model $n$ can be substituted to the above form $(S, A)_{n}$ of state-action pairs after its execution. An onpolicy RL technique called Sarsa Learning (Sarsa) is applied to update the $Q$ values of state-action pairs. Suppose the current state and action at time step $t$ are $b(i)$ and $j$, respectively, which means the current state-action pair $\left(s_{t}, a_{t}\right)$ is formed by node connection $(b(i), j)^{1}$, and the state-action pair in the next time step is $\left(s_{t+1}, a_{t+1}\right)=(b(j), k)$. Then, the $Q$ value of $(b(i), j)$ is updated by:

$$
Q(b(i), j) \leftarrow Q(b(i), j)+\alpha\left[r_{j}+\gamma Q(b(j), k)-Q(b(i), j)\right]
$$

where,
$\alpha, \gamma$ : learning rate and discount factor.
$r_{j}$ : reward of choosing node $j$ at branch $b(i)$ of node $i$, and,

1) In the case of judgment nodes, $r_{j}=0$.
2) In the case of processing nodes, $r_{j}$ is given after processing node $j$. Particularly, $r_{j}$ is given when a selling action is carried out,

$$
r_{j}=\text { selling price }- \text { buying price }
$$

[^0]
## Algorithm 1 Updating of $Q$ values

1: $n \leftarrow 1$;
2: for $n \leq N$ do
3: execute candidate model $n$, and obtain the episode (sequence of state-action pairs) $(S, A)_{n}$;
4: update the corresponding $Q$ values of $(S, A)_{n}$ using Eq. (10);
5: $\quad n \leftarrow n+1$;
6: end for
which shows the profit of one buying-selling pair. If the selling action is not executed, $r_{j}=0$.
The procedure of updating $Q$ values in each generation is shown in Algorithm 1. The $Q$ values are updated based on the execution of the best individuals (truncation selection with size $N$ ). As a result, we can collect the experience of the promising individuals into one $Q$ table which consists of all $Q(S, A)$ values. It is expected that the good state-action pairs will be rewarded with high $Q$ values, and vice-versa. Accordingly, the quality of node connections can be explicitly captured, which is used to estimate the probabilistic model of RPMBGNP.

RPMBGNP constructs its probabilistic model by a set of connection probabilities. For example, $P(b(i), j)$ denotes the probability that branch $b(i)$ is connected to node $j$. As a result, the optimal directed graph structures can be sampled if we learn the accurate connection probabilities. Each $P(b(i), j)$ is calculated by

$$
P(b(i), j)=\frac{\exp \left(\frac{Q(b(i), j)}{T}\right)}{Z(b(i))}
$$

The normalization function $Z(b(i))$ is calculated by

$$
Z(b(i))=\sum_{j^{\prime} \in N_{j} \cup N_{p}} \exp \left(\frac{Q\left(b(i), j^{\prime}\right)}{T}\right)
$$

and temperature parameter $T$ is obtained by Eq. (14).

$$
T=\frac{\tau}{t+1}
$$

where $\tau$ is a coefficient, and $t$ is the current generation number.

## F. Evolving $\mathcal{V}$ by Continuous RPMBGNP

As for the trading signals $\mathcal{V}$ in the processing nodes with continuous intervals, the continuous RPMBGNP proposed in [30] is applied. In our model, Gaussian distribution is used to model the continuous variables, where each trading signal $v_{i}$ is represented by a unidimensional Gaussian distribution $\mathcal{N}\left(\mu_{i}, \sigma_{i}^{2}\right)$. The mean value $\mu_{i}$ and standard deviation $\sigma_{i}^{2}$ of each $v_{i}$ is subject to evolution. Continuous RPMBGNP develops a RL-based probabilistic modeling approach using Actor-Critic (AC) technique [48] combined with gradient search to evolve the probability density function (pdf) of each $v_{i}$.

In order to update the pdf of each trading signal $v_{i}$, the following steps are carried out sequentially.


[^0]:    ${ }^{1} b(i)$ denotes branch $b(i)$ of node $i$, and $j$ is $C_{i B(i)}$ based on the description of individual structure.

## Step 1: Calculate gradients

Lemma 1: Given a sampled value $x_{i}$ of trading signal $v_{i}$, the gradients of $\mu_{i}$ and $\sigma_{i}$ are calculated by

$$
\begin{gathered}
\nabla\left(\mu_{i} ; x_{i}\right)=x_{i}-\mu_{i} \\
\nabla\left(\sigma_{i} ; x_{i}\right)=\frac{\left(x_{i}-\mu_{i}\right)^{2}}{\sigma_{i}^{2}}-1
\end{gathered}
$$

The proof of Lemma 1 can be found in [30]. The gradients denote the updating directions of $\mu_{i}$ and $\sigma_{i}$ given a sampled value $x_{i}$.

## Step 2: Calculate scalar reinforcement signal

After obtaining the gradient of each parameter, continuous RPMBGNP incorporates a RL technique named AC to guide the updating direction.

Similarly to the concept of RL in discrete RPMBGNP, the quality of sampled value $x_{i}$ from a given variable $v_{i}$ can be measured by RL. In this case, we define a trading signal of a processing node, i.e., $v_{i}$, as the state, where the action is represented by a sampled value from the pdf of $v_{i}$, i.e., $x_{i}$. Accordingly, we are capable of incorporating AC efficiently, where the Gaussian distribution is known as the actor since it is used to select actions, and the state-value function can be formulated as the critic.

Each time processing node $i$ is executed, AC evaluates the next new processing node $j$ to determine whether the current sampled value is better or worse than expected. The evaluation is formulated by a temporal-difference (TD)-error $\delta$ as

$$
\delta_{i}=r_{i}+\gamma_{A C} V(j)-V(i)
$$

where,
$V(i)$ : state value function of processing node $i$.
$\gamma_{A C}$ : discounted factor of AC.
After obtaining the TD-error, it is sent back to update the state-value function $V$ by:

$$
V(i) \leftarrow V(i)+\alpha_{A C} \delta_{i}
$$

where $\alpha_{A C}$ is the learning rate of AC.
If $\delta_{i}$ is positive, it suggests that the tendency to sample $x_{i}$ should be strengthened, and vice-versa. Accordingly, $\delta_{i}$ can be used to formulate a scalar reinforcement signal $\theta_{i}$ to indicate whether the updating direction of this sampled value should be strengthened or weakened.

$$
\theta_{i}= \begin{cases}-1, & \text { for } \delta_{i}<0 \\ 0, & \text { for } \delta_{i}=0 \\ 1, & \text { for } \delta_{i}>0\end{cases}
$$

## Step 3: Update the Gaussian distribution

Combining the scalar reinforcement signal with the gradient search, continuous RPMBGNP updates the pdf of Gaussian distribution for each variable as follows

$$
\begin{aligned}
& \mu_{i} \leftarrow \mu_{i}+\alpha_{\mu} \nabla\left(\mu_{i} ; x_{i}\right) \theta_{i} \\
& \sigma_{i} \leftarrow \sigma_{i}+\alpha_{\sigma} \nabla\left(\sigma_{i} ; x_{i}\right) \theta_{i}
\end{aligned}
$$

where $\alpha_{\mu}$ and $\alpha_{\sigma}$ are the learning rates.

## IV. EXPERIMENTAL STUDY

The proposed RPMBGNP-based stock trading model is applied to 9 real stock data obtained from the Tokyo Stock Exchange market. The stock data is divided into two periods: training and testing. The training data are used to evolve the stock trading models represented by the directed graph of RPMBGNP, while the best model obtained in the last generation of the training period is applied to the testing data. The experimental data used in this paper are as follows

- Training data: January 4, 2001 - December 30, 2003
- Testing data: January 5, 2004 - December 30, 2004

Initial funds with 5 million Japanese Yen are provided to the trader, where the final fitness value for each candidate model is the total profits obtained during the training period. All the results reported in this paper are the average values of 30 independent experiments.

## A. Parameter Settings

Since our purpose is to demonstrate the effectiveness of EDA for the stock trading task, the comparisons are mainly carried in comparison with the EC techniques with standard crossover and mutation, i.e., standard GNP [40].

The directed graph of RPMBGNP is defined as follows: $\left|N_{j}\right|=42$ ( 2 nodes for each judgment function listed in Table I), and $N_{p}=10$ ( 5 nodes for each processing function, i.e., buying/selling).

In standard GNP, uniform crossover and mutation with their rates of $p_{c}=0.1$ and $p_{m}=0.02$ are performed. On the other hand, RPMBGNP neglects these parameters of genetic operators. Instead, the parameters of RPMBGNP for its probabilistic modeling are defined as follows: $\alpha=0.2$ and $\gamma=0.9$ for Sarsa; $\tau=1000 ; \alpha_{A C}=0.1$ and $\gamma_{A C}=0.9$ for $\mathrm{AC} ; \alpha_{\mu}=0.05$ and $\alpha_{\gamma}=0.05$ for Gaussian distribution. The population size of GNP is set at 300 with 1 elite individual, 120 crossover individuals and 179 mutation individuals. On the other hand, RPMBGNP requires a relatively large population size in order to avoid its local convergence [23]. Therefore, the population size of 1500 is used in this paper. Truncation selection with size $N=750$ is used. The terminal condition for each experiment is based on the maximal number of fitness evaluations, where 450,000 is used in this paper.

## B. Experimental Results in the Training Period

1) Evolution efficiency: The fitness curves of RPMBGNP for the training period are plotted in Fig. 2 for the comparison with standard GNP, which are represented by the profits obtained by the best individuals at each generation. It is found that the directed graph is suitable for constructing the stock trading model, where high profits can be obtained through evolution. On the other hand, the results of 9 studied stocks confirm that RPMBGNP can achieve the significant improvement of the evolution efficiency to find better stock trading models than standard GNP with crossover and mutation.

![img-2.jpeg](img-2.jpeg)

Fig. 2: Comparison of fitness (profit) curves over 9 selected stocks in the training period
2) Statistical analysis: Two-tailed/paired $t$-test is applied to analyze the fitness values obtained by GNP and RPMBGNP in the training period. We calculate the $p$-values between the two algorithms for the 9 stocks, where the $p$-value smaller than 0.05 indicates a statistically significant difference between them. Fig. 2 includes the $t$-test result calculated for each stock. It is confirmed that RPMBGNP outperforms the standard GNP in all experiments with statistical meaning.
3) Change of holding funds: In a micro-level aspect, Fig. 3 shows the typical trajectories of the change of the holding funds during the training period of Mitsubishi stock. The dramatic decrease of holding funds indicates a buying action, while the significant increase of holding funds is caused by the selling action. It is shown that RPMBGNP has different buying/selling timing when comparing with GNP, which causes the different profits obtained in the final trading day.

## C. Experimental Results in the Testing Period

1) Amount of profits: After the training period, the best model obtained in the last generation of the evolution is
![img-2.jpeg](img-2.jpeg)

Fig. 3: Typical trajectories of holding funds on each trading day in the training period (Mitsubishi stock)
applied to make trading in the testing period. Table II reports the profits obtained by different algorithms ${ }^{2}$. The testing profits demonstrate that RPMBGNP can evolve better stock trading

[^0]
[^0]:    ${ }^{2} \mathrm{GA}$ and Buy\&Hold are selected as the baselines to evaluate this study. GA denotes the method that applies GA to evolve the continuous variables $\mathcal{V}$, while Buy\&Hold is a strategy that buys as much stocks as possible on the start day and sells them all on the last day.

TABLE II: Profits (unit: yen) obtained in the testing period (profit rate [unit:\%])


![img-3.jpeg](img-3.jpeg)

Fig. 4: Change of holding funds on each trading day in the testing period (Mitsubishi stock)
models than the other compared algorithms. Comparing with standard GNP, RPMBGNP can obtain higher profits, though in some stocks, i.e., Toyota and Meiji Seika, worse results are obtained which might be due to the overfitting problem.
2) Change of holding funds: Fig. 4 shows the change of the holding funds during the testing period of Mitsubishi stock, which shows that RPMBGNP has different buying/selling timing when comparing with GNP to obtain higher profits in the final trading day.
3) Timing of buying/selling: Fig. 5 shows a typical example of the buying/selling timing made by RPMBGNP which is plotted in the stock movement of the testing period. It is found that in most cases, RPMBGNP can buy stocks at lower prices and make selling decision at relatively higher prices.

Considering the results of the training and testing periods as a whole, we demonstrate the effectiveness of the proposed RPMBGNP-based stock trading model comparing with the other non-EDA models, which clarifies the superiority of the EDA-based probabilistic modeling in this problem.

## V. Conclusions and Future Work

In this paper, an EDA-based stock trading model has been proposed, where a recent proposed algorithm called RPMBGNP is applied. With its directed graph structure and RL-based probabilistic modeling, RPMBGNP shows attractive expression and evolution ability to create stock trading rules. The experimental results clarified that the proposed model can obtain better evolution efficiency and higher profits when comparing with the traditional non-EDA models. In the future, further improvements of the research using variable size GNP
![img-4.jpeg](img-4.jpeg)

Fig. 5: Timing of buying/selling recommended by RPMBGNP in the testing period (Mitsubishi stock)
[49], [50] and rule-based systems [51], [52] will be studied. Self-adaptive method to reduce the parameters is also an another direction.
