# An Adaptive Estimation of Distribution Algorithm for Multipolicy Insurance Investment Planning 

Wen Shi, Student Member, IEEE, Wei-Neng Chen ${ }^{\ominus}$, Senior Member, IEEE, Ying Lin, Member, IEEE, Tianlong Gu, Sam Kwong ${ }^{\oplus}$, Fellow, IEEE, and Jun Zhang ${ }^{\ominus}$, Fellow, IEEE


#### Abstract

Insurance has been increasingly realized as an important way of investment and risk aversion. Fruitful insurance products are launched by insurers, but there is little research on how to make a proper insurance investment plan for a specific policyholder given different kinds of policies. In this paper, we aim to propose a practical approach to multipolicy insurance investment planning with a data-driven model and an estimation of distribution algorithm (EDA). First, by making use of the insurance data accumulated in the modern financial market, an optimization model about how to choose endowment and hospitalization policies is built to maximize the yearly profit of insurance investment. With the model parameters set according to the real data from insurance market, the resulting plan is practical and individualized. Second, as the optimal solution cannot be achieved by mathematical deduction under this datadriven model, an EDA is introduced. To adapt the EDA for the considered problem, the proposed EDA is mixed with both the continuous and discrete probability distribution models to handle different kinds of variables. In addition, an adaptive scheme for choosing suitable distribution models and an efficient constraint handling strategy are proposed. Experiments under different conditions confirm the effectiveness and efficiency of the proposed model and method.


Index Terms-Data-driven, endowment insurance, estimation of distribution algorithm (EDA), hospitalization insurances, mixed-variable optimization.

## I. INTRODUCTION

INSURANCE is an important way for people to cope with risk. With the development of modern economy, more and more people realize the significance of insurance and consider

[^0]it a key part of their investment plan [1], [2]. As the insurance industry grows rapidly in recent years, insurance products and behaviors become more diverse and sophisticated. It becomes increasingly important and challenging to study the actuarial models of insurance.

In the literature, various mathematical models for insurance have been developed, most of which focused on insurance pricing on behalf of the insurers, e.g., insurance companies. In the 1970s, Brennan and Schwartz [3] proposed the first pricing model that considered the equity-linked life insurance policies with an asset value guaranteed. Since then, researchers have developed a plethora of models to address the problem of insurance pricing under different circumstances. Some of the representative works include the pricing of an endowment insurance policy paid by annual premium [4], the models for equity-linked life insurance policies [5]-[7] and fixed income linked life insurance policies [8]. Also, there are dozens of researchers studying the pricing model of nonlife policies. Please refer to [9] for a detailed survey on such pricing models.

In contrast to the pricing models for insurers, the research into insurance investment models on behalf of the policyholders is far less matured. In the literature, the investments of insurance were mostly considered as a complementary part of the entire property investment plan. The first insurance investment model was proposed by Hakansson [1], which considered life insurance as a part of the property investment plan and established a discrete model to calculate the return of life insurance. Later the model was extended to a continuous form for enhancing its practical value [2], as the investment process into insurance is actually a continuous procedure. Based on these two models, a number of improved models have been developed. Pliska and Ye [10] studied the optimal investment strategy for a wage earner with uncertain lifetime. The model was then extended to take risky assets [11]-[13] and different kinds of life insurance products [14] into account. Besides the above models that consider the investment strategy of a single person, investment models for the collective situation [15], [16] were also developed. However, all the above models share a vital defect. That is, only one type of insurance policies, i.e., life insurance, is considered. In fact, to fulfill desires of different policyholders, the modern insurance market offers many different types of insurance policies, including but not limited to endowment policies, hospitalization policies, property policies, auto policies, etc. To make the insurance investment models better suit the modern insurance

[^1]
[^0]:    Manuscript received September 9, 2017; revised November 20, 2017; accepted November 24, 2017. Date of publication December 12, 2017; date of current version January 28, 2019. This work was supported in part by the National Natural Science Foundation of China under Grant 61332002, Grant 61622206, and Grant 61772569, and in part by the Hong Kong RGC General Research Fund under Grant 9042038 (CityU 11205314). (Corresponding authors: Wei-Neng Chen; Jun Zhang.)
    W. Shi, W.-N. Chen, and J. Zhang are with the School of Computer Science and Engineering, South China University of Technology, Guangzhou 510006, China, and also with the Guangdong Provincial Key Laboratory, Computational Intelligence and Cyberspace Information, Guangzhou 510006, China (e-mail: cwnrau634@aliyun.com; junzhang@ieee.org).
    Y. Lin is with the Department of Psychology, Sun Yat-sen University, Guangzhou 510006, China.
    T. Gu is with the School of Computer Science and Engineering, Guilin University of Electronic Technology, Guilin 541004, China.
    S. Kwong is with the Department of Computer Science, City University of Hong Kong, Hong Kong.

    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
    Digital Object Identifier 10.1109/TEVC. 2017.2782571
[^1]:    1089-778X (C) 2017 IEEE. Translations and content mining are permitted for academic research only. Personal use is also permitted, but republication/ redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

market and better satisfy the practical need of policyholders, it is necessary to take more types of policies into account.

In order to overcome the above deficiency, this paper intends to establish an insurance investment model that considers different kinds of endowment and hospitalization policies. However, the fact that different insurance policies calculate their premiums and profits in different ways increases the complexity of the proposed model and brings up the following two challenges.

On the one hand, in the case that only life insurance is considered, it is possible to use mathematical expressions to deduce the price and the profit of an insurance policy [10]-[14]. As for the case of multipolicy insurance investment, since many factors (e.g., wealth condition, health condition, age, etc.) must be taken into account, it is difficult or even impossible to deduce the price and the profit of each policy mathematically. For instance, to mathematically model a multipolicy insurance investment plan that considers the health condition of a policyholder, a mathematical expression of the health condition is needed at first. However, since it is hard to establish an accurate mathematical expression to assess the health condition of the policyholder, the establishment of the mathematical model for the multipolicy insurance plan becomes difficult. With the rapid development of insurance business, a wealth of insurance data (settings of insurance policies, demographic information of policyholders, real insurance cases, etc.) has been accumulated. Instead of using mathematical expressions, it might be more practical and promising to build the insurance investment model based on data. Inspired by this idea, this paper proposes a data-driven multipolicy insurance investment model.

On the other hand, the simplicity of the existing investment models for life insurance makes it possible to derive the optimal investment plan by mathematical deduction. However, the proposed multipolicy insurance investment model becomes so complex that it may not have the mathematical properties (e.g., continuity or differentiability) required by traditional optimization methods based on mathematical deduction. Therefore, this paper proposes the use of estimation of distribution algorithms (EDAs) [17], a simple yet effective evolutionary algorithm [18]-[22], to address the proposed multipolicy insurance investment model. There are two advantages of utilizing EDA. First, EDA is a stochastic optimization algorithm based on statistical learning theory, and thus has inherent coherence with the proposed insurance investment model established based on statistical data. Second, it has been shown that EDA has good global search capability, which makes it promising for optimization of the investment plan involving multiple insurance policies.

In order to tailor the original EDA to the proposed insurance investment model, the following improvements are made. First, since the multipolicy insurance investment model has both of continuous and discrete decision variables, a mixed variable framework that enables EDA to handle different types of variables simultaneously is proposed in this paper. Second, to avoid the premature convergence, an adaptation strategy that can choose the probabilistic model in EDA according to the performance is developed. Third, to ensure that the
insurance investment plan obtained is feasible, a novel constraint handling strategy is designed and embedded. Finally, a local search strategy is utilized to further improve the search efficiency. Experiments under different conditions confirm the effectiveness and efficiency of the proposed model and method.

The rest of this paper is organized as follows. Section II briefly introduces the background of insurance investment models and EDAs. Section III formally defines the proposed multipolicy insurance investment model. Section IV introduces the details of the proposed EDA for optimization of the proposed model. Section V presents a series of experiments to prove the effectiveness and efficiency of the proposed model and method. Finally, the conclusion of this paper is drawn in Section VI.

## II. BACKGROUND

## A. Insurance Investment Model

Insurance is a kind of investment strategy that can help the policyholder to avoid risks. In particular, life insurance takes the life expectancy of the insured as the subject of insurance, and the payment condition is the survival or death of the insured. Most existing works about insurance investment only considered a single life insurance policy [10]-[13], in which a continuous investment model is employed and the return of the life insurance, $Z(t)$, is calculated according to the following formula:

$$
Z(t)=\frac{I(t)}{\eta(t)}
$$

where $I(t)$ is the amount that the policyholder purchases at time $t$ and $\eta(t)$ is the premium-payout ratio at time $t$.

With the rapid development of insurance business, a variety of life insurance policies with different characteristics have been developed. The necessity of studying the investment strategy involving more than one life insurance policy thus becomes more and more obvious. Mousa et al. [14] proposed the first and, so far, the only one insurance investment model that considered different kinds of life insurance policies. Yet the difference in different policies was limited to their premium-payout ratios. The model considering $k$ life insurance policies was thus extended to

$$
Z(t)=Z_{1}(t)+\cdots+Z_{k}(t)=\frac{I_{1}(t)}{\eta_{1}(t)}+\cdots+\frac{I_{k}(t)}{\eta_{k}(t)}
$$

Here, $Z_{i}(t), I_{i}(t)$, and $\eta_{i}(t), i=1,2, \ldots k$, denote the return of the $i$ th policy, the amount of purchasement of the $i$ th policy at time $t$, and the premium-payout ratio of the $i$ th policy at time $t$, respectively. With the model, it is obvious that the policy with the lowest premium-payout ratio at time $t$ would be chosen, while the purchase amount of the other policies would be zero.

From the above, it can be known that the previous models have many limitations on the type and the amount of insurance policies in consideration. In fact, nowadays, few companies offer life insurance policies that only have death compensation. Most companies provide endowment policies that add

![img-0.jpeg](img-0.jpeg)

Fig. 1. Flowchart of insurance investment model for endowment policies.
the function of saving to life insurance [23]. As the calculation of the return of endowment policies is more complex, the previous models are no longer suitable for studying. To show the insurance investment model for endowment policies, the flowchart is given in Fig. 1.

Besides the endowment policies, this paper also takes a kind of popular nonlife insurances, the hospitalization policies [24], into account. A hospitalization policy is an insurance contract that helps the policyholder to avoid the risk of incurring medical expenses when getting certain kind of diseases. Suppose that the premium of a hospitalization policy is $z(t)$, if the policyholder gets sick with certain disease specified in the policy at time $t$, the medical expenses $Y(t)$ will be reimbursed by the insurer, that is, the policyholder can get a return of $Y(t)$. If the policyholder remains healthy, he will get no return. In summary, the total return $R(t)$ can be calculated as

$$
R(t)= \begin{cases}-z(t), & \text { if the policyhoder is fine } \\ Y(t)-z(t), & \text { otherwise }\end{cases}
$$

Taking multiple endowment and hospitalization policies into account significantly improves the practicality of the insurance investment model. However, it also makes the model more complex, which increases the difficulty of finding the optimal investment plan of the model. Considering that the model may not have the mathematical properties required by traditional optimization methods, usage of a new kind of optimizer, the EDA, is proposed.

## B. Estimation of Distribution Algorithm

EDA [17] is an evolutionary algorithm based on statistical learning theory. As shown by the flowchart in Fig. 2, EDA starts from initializing a population, in which each individual represents a candidate solution to the problem. Based on the existing population, it utilizes the statistical learning method to estimate a probability model for describing the distribution of promising solutions in the search space. Then the
![img-1.jpeg](img-1.jpeg)

Fig. 2. Flowchart of EDAs.
probability model is sampled to generate a new population. By repeating the steps of estimating and sampling the probability model of promising solutions, EDA can evolve the population toward the optimum of the problem.

Building a probability model that can accurately describe the distribution of promising solutions in the search space is the key to enhance the efficiency of EDAs. Considering the characteristics of different kinds of problems, EDAs with different model estimation methods are developed. Population-based incremental learning (PBIL) [25], univariate marginal distribution algorithm (UMDA) [26], and compact genetic algorithm (cGA) [27] are proposed to deal with the optimization of variable independent binary coding problems. Mutual information maximization for input clustering [28], combining optimizers with mutual information trees [29], and bivariate marginal distribution algorithm [30] are proposed to solve the optimization problems of bivariate correlation binary coding. Factorized distribution algorithms [31], extended cGA [32], and Bayesian optimization algorithm [33] are proposed to deal with the optimization of multivariate correlation binary coding problems. PBILc [34], UMDAc [35], and stochastic hill climbing with learning by vectors of normal distributions [36] are proposed for variable independent real-number coding problem. Estimation of multivariate normal algorithm [37] and IDEA [38] are proposed to solve the multivariate correlation real-number coding problem. In recent years, many EDA variants have been proposed [39]-[44] and it is extensively applied to solve many problems, such as multimodal problems [45], [46] and multiobjective problems [47].

However, none of the above EDAs are sufficiently suitable for the insurance investment problem considered in this paper. The reasons are as follows. First, the multipolicy insurance investment model proposed in this paper consists of both discrete and continuous variables. To ensure precision and efficiency of optimization, instead of encoding all of the variables into a binary vector or a real-number vector, it is more desired to adopt a mixed coding scheme. Yet all the above EDAs are designed using a single (either binary or real-number) coding scheme. Second, there are specific constraints among the

variables. The problem cannot be easily transformed into any multivariate correlation problems dealt by the above EDAs. In order to conquer the above problems, this paper develops an adaptive EDA (AEDA) to address the proposed multipolicy insurance investment model, which will be elaborated in Section IV.

## III. Multipolicy Insurance Investment Model

This paper focuses on optimization of insurance investment plan that involves endowment and hospitalization policies. For simplicity, we only consider the situation that the policyholder is also the insured.

In the proposed model, different kinds of endowment and hospitalization policies are considered. One can purchase as many kinds of endowment policies and invest as much as he wants, but the investment for each payment period must fulfill the minimum request. As for the hospitalization policies, the premium is determined based on the coverage scope as well as the holder's situation. Only one hospitalization policy can be purchased, and to keep the policy effective, the policyholder must pay the same amount of premium every year. In exchange, he no longer needs to pay the medical expenses incurred by the diseases covered by the policy.

Given the initial wealth and the policyholder's initial age, the optimization objective is to maximize the statistical value of the yearly profit by tuning the amount of investment for each payment period of the endowment policies and the choice of hospitalization policy.

## A. Parameters of the Model and Their Settings

From the above description, it can be seen that a number of parameters must be defined at first to make the proposed model work. The parameters are listed as follows.

1) Parameters Related to Endowment Policies: The following parameters are needed to compute the profit of the $i$ th endowment policy with the $j$ th payment period ( $i=$ $1,2, \ldots, n_{1}, j=1,2, \ldots, m_{i}$ ):
1) $\eta_{1 i j}\left(t_{0}, t\right)$ return rate at time $t$ if invested at $t_{0}$;
2) $\eta_{2 i j}\left(t_{0}, t\right)$ death compensation rate at time $t$ if invested at $t_{0}$;
3) $q_{i j}$ latest time to purchase;
4) $l_{i j t}$ minimum amount of investment;
5) $T_{1}$ guarantee period.
6) Parameters Related to Hospitalization Policies: The following parameters are needed to analyze the investment efficiency of the hospitalization policies:
1) $\delta_{k}\left(t_{0}\right)$ premium of policy $k$ at time $t_{0}, k=1,2, \ldots, n_{2}$;
2) $A_{k}$ coverage scope of policy $k, k=1,2, \ldots, n_{2}$;
3) $z_{s}$ medical expense for diseases with the sth serious degree;
4) $T_{2}$ latest time to buy a hospitalization policy.
5) Parameters Related to the Policyholder: The following parameters are needed to design an individualized investment plan:
1) $I_{0}$ initial wealth;
2) $I(t)$ annual income at time $t$;
3) $t_{0}$ initial age;
4) $p(t)$ mortality rate at time $t$;
5) $p_{x}(t)$ incident rate for diseases with the sth serious degree at time $t$.
For a policyholder who wants to utilize the proposed model to derive the optimal investment plan, the parameters related to endowment policies and hospitalization policies should be given in advance. Some of the parameters related to the policyholder, i.e., $I_{0}, I(t), t_{0}$, should also be given to obtain an individualized insurance investment plan. The remaining parameters, i.e., $p(t)$ and $p_{x}(t)$, should be set based on the statistical data as below.

Let $T(x)$ be the number of years a person at the age of $x$ can live. The probability for the person to survive after $\tau$ years, which is denoted as ${ }_{\tau} p_{x}$, is calculated as

$$
{ }_{\tau} p_{x}=\operatorname{Pr}(T(x)>\tau)=\operatorname{Pr}(X>x+\tau \mid X>\tau)=\frac{s(x+\tau)}{s(x)}
$$

where $\operatorname{Pr}(A)$ indicates the probability that $A$ will occur, while $\operatorname{Pr}(A \mid B)$ is the probability that $A$ will occur given that event $B$ has occurred. $s(x+\tau)$ is the number of survivors at time $(x+\tau)$ and $s(x)$ is the total number of survivors at $x$. Based on the above, the mortality rate at time $(x+\tau)$ for a person at the age of $x$ can be computed as

$$
p(x+\tau)={ }_{\tau+1} p_{x}-{ }_{\tau} p_{x}=\frac{s(x+\tau+1)-s(x+\tau)}{s(x)}
$$

To complete the above derivation, $s(\cdot)$ must be known in advance. Therefore, it is necessary to estimate the age distribution of mortality over the people whose health conditions and health habits are similar with the policyholder. Such estimation can be achieved by collecting and analyzing historical data.

The incidence rates for diseases of the sth serious degree are derived as

$$
p_{x}(x+\tau)=\frac{i_{x}(x+\tau)}{s(x+\tau)}
$$

where $i_{x}(x+\tau)$ is the number of survivors who have diseases of degree $s$ at $x+\tau$. To conduct the above derivation, $i_{x}(\cdot)$ and $s(\cdot)$ must be known in advance. It is thus necessary to estimate the incident age distribution of patients whose health conditions and health habits are similar to the policyholder. Such estimation can also be achieved based on historical data.

In the literature, only death compensation rate and mortality rate are considered as parameters of the insurance investment models [10]-[16]. The difference in insurance policies and the policyholder's specific situations is largely neglected. In this paper, we propose to consider all of the parameters mentioned above. By doing so, the insurance investment model becomes more realistic, and the insurance investment plan can be optimized in an individualized way.

## B. Premises and Assumptions

To facilitate the establishment of the optimization model, the following premises and assumptions are made according to

existing literatures of insurance investment and some insurance policies in real life [10]-[14], [48].

1) Suppose that there are $n_{2}$ hospitalization policies. All of the diseases in concern are classified into $n_{2}$ groups regarding their serious degrees, and the groups are indexed in descending seriousness. Assume that the coverage scope of the $i$ th hospitalization policy includes all the diseases in the first $i$ group(s) $\left(i=1,2, \ldots, n_{2}\right)$. In other words, the first policy only covers the most serious diseases, whilst the $n_{2}$ th policy covers all the diseases in concern. The more diseases a policy covers, the higher its premium is. Note that the premium of a hospitalization policy is determined at the time of purchase. The policyholder must pay the same amount of premium every year till the payment period is completed.
2) The cash values of endowment policies cannot be cashed in to purchase new endowment policies or to pay the medical expense for the diseases outside the coverage of the selected hospitalization policy. However, the cash values can be used to pay the premium of the hospitalization policy.
3) Assume that the policyholder does not need to withdraw any money from his investment into insurance. Surrender policies are thus not considered in the proposed model. Each insurance policy purchased by the policyholder will stay effective until its guarantee period is completed.
4) Assume that the policyholder's death always occurs at the beginning of a year. Therefore, the cash value of the endowment policies and the possible medical expenses in the year of the policyholder's death are not considered when computing the yearly profit.
5) Assume that the medical expenses for the diseases with the same degree of seriousness are constant, irrespective of age or general health conditions. The more serious a disease is, the higher the medical expense will be.
6) The policyholder begins to profit from the purchased endowment policies one year afterwards.

## C. Objective Function

Suppose that there are $n_{1}$ endowment policies and $n_{2}$ hospitalization policies in the market. Each endowment policy $i$ has $m_{i}$ payment periods $\left(i=1,2, \ldots, n_{1}\right)$. According to the previous sections, the optimization problem of the insurance investment plan can be formulated as

$$
\max J(t ; \boldsymbol{X}, \beta)
$$

where $J(t ; \boldsymbol{X}, \beta)$ is the statistical value of the profit at time $t$ given the investment plan $\boldsymbol{X}$ of endowment policies and the selected hospitalization policy $\beta$. More specifically, $\boldsymbol{X}$ is an irregular matrix, in which each element $x_{i j}$ indicates the amount of investment for the $j$ th payment period of the $i$ th endowment policy. $J(t ; \boldsymbol{X}, \beta)$ is calculated as

$$
J(t ; \boldsymbol{X}, \beta)=[1-p(t)] V(t)+p(t) Z(t)+C(t)
$$

where $p(t)$ is the mortality rate of the policyholder at time $t, V(t), Z(t)$, and $C(t)$ denote the cash value, the death
compensation (if occur), and the cash on hand at time $t$, respectively.

The cash value at time $t$ is the sum of the current cash values of all the endowment policies, i.e.,

$$
V(t)=\sum_{i=1}^{n_{1}} \sum_{j=1}^{m_{i}} V_{i j}(t)
$$

where $V_{i j}(t)$, as calculated by (10), is the cash value of the $i$ th endowment policy with the $j$ th payment period at time $t$

$$
\begin{aligned}
& V_{i j}(t) \\
& \quad= \begin{cases}x_{i j} \eta_{1 i j}\left(t_{0}, t\right), & \text { if } t=t_{0}+1 \\
V_{i j}(t-1)+x_{i j}\left[\eta_{1 i j}\left(t_{0}, t\right)-\eta_{1 i j}\left(t_{0}, t-1\right)\right], & \text { otherwise. }\end{cases}
\end{aligned}
$$

In (10), $t_{0}$ is the initial age of the policyholder and $\eta_{1 i j}\left(t_{0}, t\right)$ is the return rate of the $i$ th endowment policy with the $j$ th payment period. Note that the cash values will be used to pay the premium of the selected hospitalization policy, as long as the policyholder's age has not passed the latest investment time $T_{2}$ (i.e., $t \leq T_{2}$ ). In that case, the cash values $V_{i j}(t)$ are taken out in descending order to pay the premium $\delta_{\beta}(t)$ of the hospitalization policy $\beta$ till $\delta_{\beta}(t)$ is paid off. If $\delta_{\beta}(t)$ cannot be fulfilled with all the cash values taken out [i.e., $\delta \beta(t)>V(t)$ ], the hospitalization policy is considered unaffordable. The investment strategy thus becomes infeasible. For each endowment policy whose cash value has been taken out, $V_{i j}(t)$ is set as zero. That is, the accumulation of the cash value restarts from time $(t+1)$.

Likewise, the death compensation at time $t$ is the sum of the death compensations of all the endowment policies. Let $\eta_{2 i j}\left(t_{0}, t\right)$ be the death compensation rate of the $i$ th endowment policy with the $j$ th payment period. The death compensation at time $t$ is computed as

$$
Z(t)=\sum_{i=1}^{n_{1}} \sum_{j=1}^{m_{i}} x_{i j} \eta_{2 i j}\left(t_{0}, t\right)
$$

The cash value at time $t$ is equal to the balance at time $(t-1)$ plus the policyholder's income $I(t)$, and minus the total medical expenses. Let $p_{s}(t)$ be the incidence rate for diseases in the $s$ th group at time $t$ and $z_{s}$ be the medical expense for the diseases in the $s$ th group. The cash value at time $t$ can be computed as

$$
\begin{aligned}
& C(t) \\
& \quad= \begin{cases}t_{0}, & \text { if } t=t_{0} \\
C(t-1)+I(t)-\sum_{i=1}^{n_{1}} \sum_{j=1}^{m_{i}} v_{i j} x_{i j}-\sum_{s=1}^{n_{2}-\beta} p_{s}(t) z_{s}, & \text { otherwise }\end{cases}
\end{aligned}
$$

where $v_{i j} \in\{0,1\}$ is an indicator of whether or not the policyholder has finished the payment for the $i$ th endowment policy with the $j$ th payment period.

## D. Constraints of the Model

In reality, investing insurance has some constraints. Such constraints are also manifested in the proposed model.

1) There is a latest time to invest in the $j$ th payment period of the $i$ th endowment policy, denoted as $q_{i j}$. That is, for

a policyholder whose age is greater than $q_{i j}$, it is not available for him to invest in the $j$ th payment period of the $i$ th endowment policy.
2) There is a minimum amount of the investment to the $j$ th payment period of the $i$ th endowment insurance at time $t$, denoted as $l_{i j t}$. That is, the investment amount to the $j$ th payment period of the $i$ th endowment insurance at time $t$ should not be less than $l_{i j t}$.
3) There is a guarantee period for all the endowment policies, denoted as $T_{1}$. That is, after $T_{1}$, the insurance coverage period of the endowment policies is over, the cash value and the death compensation would not be accumulated any more.
4) There is a latest time to buy hospitalization policies, denoted as $T_{2}$. That is, the policyholder cannot buy any hospitalization policies after age $T_{2}$ if he has not bought any hospitalization policies before. But for a policyholder who has bought a hospitalization policy before $T_{2}$, he can continue to buy it after $T_{2}$.
5) In no case can a policyholder choose an investment plan that the total amount of cash value is not able to cover the premium of the hospitalization policy at any time.
6) The policyholder's cash in hand cannot be negative at any time otherwise the policyholder will go bankrupt.

## IV. Adaptive EDA Approach

The definition in Section III shows that the multipolicy insurance investment model is a complex optimization problem with multiple constraints and mixed variables. It is unlikely that the optimal solution can be obtained through traditional optimization methods based on mathematic computation. This paper proposes an AEDA to approximate the optimal solution of the problem. To ensure that the solution obtained is feasible, a novel constraint handling strategy is embedded into AEDA. To deal with the continuous and discrete variables in the problem simultaneously, AEDA adopts a mixed-variable framework to treat different types of variables separately. Besides, AEDA employs an adaptation strategy that can choose probability models automatically regarding their performances to avoid premature. A local search strategy is also employed to further improve the search efficiency. Detailed design of AEDA is illustrated in the following sections.

## A. Initialization With Constraint Handling

Each individual in the population of AEDA represents a candidate insurance investment plan, which, according to Section II, can be written as $\boldsymbol{S}=<\boldsymbol{X}, \beta>$. In order to promote the search efficiency, it is better that the search starts from feasible solutions with adequate variety. To achieve this goal, AEDA initializes each individual by assigning random values to the variables in $\boldsymbol{S}$ such that the resulting investment plan satisfies the following constraints.

1) The value of $\beta$ is an integer in the range of $\left[0, n_{2}\right]$.
2) For each element $x_{i j}$ in $\boldsymbol{X}$, the value of $x_{i j}$ is not smaller than $l_{i j t_{0}}$, i.e., the minimum amount of investment
requested by the $i$ th endowment policy with the $j$ th period at time $t_{0}$.
3) For the endowment policies whose latest purchasing time $q_{i j}$ is earlier than $t_{0}, x_{i j}$ must be zero.
4) The sum of the elements in $\boldsymbol{X}$, that is, the total amount of investment to endowment policies, cannot exceed the cash that the policyholder has on hand at any time.
Among the above four constraints, the first two can be satisfied by setting the ranges from which $\beta$ and $x_{i j}$ are sampled accordingly. The third constraint can be satisfied by comparing $t_{0}$ with $q_{i j}$ before assigning a nonzero value to $x_{i j}$. The fourth constraint, on the other hand, is more difficult to deal with, as the amount of the cash on hand is uncertain except at time $t_{0}$.

To deal with the fourth constraint, a novel constraint handling process is proposed. In this process, the investment amount to each endowment policy and each payment period is initialized in sequence. To ensure that the total amount of investment does not exceed the cash the policyholder has, once the investment amount to a payment period of an endowment policy is decided, a corresponding amount should be subtracted from the cash the policyholder has in the following years. To avoid the situation that all the cash is invested to the first several policies for all individuals, the order of the policies is randomly perturbed for each individual. The detailed description of this constraint handling strategy is given below.

First, one of the endowment policy $a$ and its payment period $b$ is selected randomly from $a \in\left[1, n_{1}\right], b \in\left[1, m_{a}\right]$.

Second, the upper bound of $x_{a b}$ is computed as

$$
u_{a b}\left(t_{0}\right)=\min \left\{\hat{C}\left(t_{0}\right), \hat{C}\left(t_{0}+1\right) / 2, \ldots, \hat{C}\left(t_{0}+y_{a b}\right) / y_{a b}\right\}
$$

where $y_{a b}$ is the length of the payment period and $\widehat{C}(t)$, initialized by (14), is the expectation of the cash on hand at time $t$

$$
\hat{C}(t)= \begin{cases}I_{0}, & \text { if } t=t_{0} \\ \hat{C}(t-1)+I(t)-E_{x}\left(z_{s}\right), & \text { otherwise }\end{cases}
$$

Herein, $I_{0}$ is the policyholder's initial wealth, $I(t)$ is his income at time $t$, and $E_{x}\left(z_{s}\right)$ is the expectation of the policyholder's medical expense at time $t$. By setting $x_{a b}$ as a random value not larger than $u_{a b}\left(t_{0}\right)$, the investment should be affordable at any time during the payment period. Note that the cash for $t=t_{0}, t_{0}+1, \ldots, t_{0}+y_{a b}$ must be updated accordingly after setting $x_{a b}$. That is, after the value of $x_{a b}$ is determined, the cash in hand should be taken out to pay that premium at each time $t$. Therefore, $\widehat{C}\left(t_{0}\right)$ should minus $x_{a b}, \widehat{C}\left(t_{0}+1\right)$ should minus $2 x_{a b}$, and so on till the last year of the payment period when the cash in hand $\widehat{C}\left(t_{0}+y_{a b}\right)$ should minus $y_{a b} x_{a b}$. The above steps are repeated until the cash in hand can afford no more endowment policies.

The above initialization procedure for each individual $\boldsymbol{S}^{(k)}$ in the population is summarized in Algorithm 1, where $k=$ $1,2, \ldots, N P$ and $N P$ is the population size.

## B. Estimation of Probability Models

In each generation of the proposed AEDA, the best $N P_{\text {best }}$ individuals in the current population are used to estimate the

```
Algorithm 1: Initialization
    for \(k=1\) to \(N P\) do
        \(\beta^{(k)}=\) Uniform_int \(\left(0, n_{2}\right)\)
        Initialize \(\widehat{C}^{(k)}(t)\)
        \(A=\left\{1,2, \ldots n_{1}\right\}\)
        for \(i=1\) to \(n_{1}\) do
            randomly choose \(a\) from \(A\)
            \(A=A \backslash\{a\}\)
            \(B=\left\{1,2, \ldots m_{a}\right\}\)
            for \(j=1\) to \(m_{a}\) do
                randomly choose \(b\) from \(B\)
            \(B=B \backslash\{b\}\)
            if \(t_{0} \leq q_{a b}\) and \(u_{a b}\left(t_{0}\right) \geq l_{a b t_{0}}\)
            \(x_{a b}^{(k)}=\) Uniform \(\left(l_{a b t_{0}}, u_{a b}\right)\)
            else
                \(x_{a b}^{(k)}=0\)
            end if
            for \(t_{1}=t_{0}\) to \(t_{0}+y_{a b}-1\) do
                \(\widehat{C}^{(k)}\left(t_{1}\right)=\widehat{C}^{(k)}\left(t_{1}\right)-x_{a b}^{(k)} \times\left(t_{1}-t_{0}+1\right)\)
            end for
            for \(t_{1}=t_{0}+y_{a b}\) to \(T_{1}\) do
                \(\widehat{C}^{(k)}\left(t_{1}\right)=\widehat{C}^{(k)}\left(t_{1}\right)-x_{a b}^{(k)} \times y_{a b}\)
            end for
        end for
    end for
25: end for
```

probability models from which new individuals are sampled. The probability models of the continuous variables $x_{i j}$ and the discrete variable $\beta$ are built separately. In detail, for the investment amount $x_{i j}$ of the $j$ th payment period of the $i$ th endowment policy, the probability model is established using the mean $\mu_{i j}$ and the standard deviation $\sigma_{i j}$ calculated as

$$
\begin{aligned}
\mu_{i j} & =\frac{\sum_{k=1}^{N P_{\text {best }}} x_{i j}}{N P_{\text {best }}} \\
\sigma_{i j} & =\sqrt{\frac{\sum_{k=1}^{N P_{\text {best }}}\left(x_{i j}-\mu_{i j}\right)^{2}}{N P_{\text {best }}}}
\end{aligned}
$$

The probability model can be the Gaussian distribution or the Cauchy distribution. An adaptation strategy is proposed to select between the two models according to their performances in the previous generations, as will be illustrated in the next section.

As for the choice $\beta$ of hospitalization policies, a histogram method is used. For each available value $i$ of $\beta$ $\left(i \in\left\{0,1, \ldots, n_{2}\right\}\right)$, let count ${ }_{i}$ be the number of individuals whose value of $\beta$ equals $i$ in the current population and count_best ${ }_{i}$ be the number of individuals whose value of $\beta$ equals $i$ among the best $N P_{\text {best }}$ individuals. The probability $\beta_{i_{-}} p$ for a new individual to assign $i$ to $\beta$ is calculated as

$$
\beta_{i_{-}} p=\left[\sum_{k=0}^{n_{2}} \frac{\text { count_best }_{k}}{\text { count }_{k}}\right]^{-1} \frac{\text { count_best }_{i}}{\text { count }_{i}}
$$

By doing so, the choices that induce larger fitness in the current population are more likely to be used in the next generation.

Using the above strategy, AEDA can handle the continuous variables and the discrete variable in the proposed insurance investment model simultaneously. Besides, in this algorithm, the estimation of the probability model is based on statistical data. Thus, it is in accordance with the proposed model which is established based on statistical data as well.

## C. Adaptive Model Selection

The probabilistic function of Gaussian distribution is a bellshaped curve with thin tails on both sides. As a result, if the Gaussian distribution is used to model the distribution of promising solutions in the search space, most of the new individuals sampled from the model will be closed to the mean, causing decrease in the population diversity and thus early convergence. In contrast, the Cauchy distribution has relatively fat tails. Using the Cauchy distribution can therefore relieve the problem of early convergence, but also stems a new problem: slow convergence speed. In order to achieve a better balance between exploitation and exploration, this paper proposes an adaptation strategy, which chooses between the Gaussian distribution and the Cauchy distribution according to their performances in previous search.

The performance of each distribution is determined by the proportion of the promising individuals that use a kind of distribution to the total of individuals that use this kind of distribution. The distribution with the better performance should be utilized more when sampling the new population. In the first generation, since no information about the performance of the distribution can be obtained, half of the population uses the Gaussian distribution to generate offspring while the other half uses the Cauchy distribution. Therefore, the probability of choosing the Gaussian distribution to sample new population $g_{-} p$ is initialized as 0.5 and updated as follows:

$$
g_{-} p=\left[\sum_{k=0}^{1} \frac{\text { top_ } d_{k}}{\text { count_ } d_{k}}\right]^{-1} \frac{\text { top_ } d_{0}}{\text { count_ } d_{0}}
$$

In (18), top_ $d_{0}$ and top_ $d_{1}$ is the number of individuals sampled from Gaussian distribution and Cauchy distribution in the best $N P_{\text {best }}$ individuals, respectively. count_ $d_{0}$ and count_ $d_{1}$ is the number of offspring sampled from Gaussian distribution and Cauchy distribution, respectively. To avoid the situation that the probability of choosing one distribution becomes too large or too small, the value of $g \_p$ is confined to $[0.1,0.9]$.

## D. New Population Generation

After the probability models are determined as in Sections IV-B and IV-C, a new population is generated by sampling these models. In this process, the individuals in new population must also satisfy the constraints listed in Section IV-A. Therefore, a constraint handling strategy similar to the initialization process is applied to ensure that the new individual is feasible. The detail process of generating a new individual is given below.

Step 1: Determine the value of $\beta$ according to the histogram model built by (17). Initialize the cash value in hand according to (14).

Step 2: Randomly select an endowment policy $a$ and its payment period $b$. Sample the corresponding model $N\left(\mu_{a b}, \sigma_{a b}\right)$ (if the Gaussian distribution is selected) or $C\left(\mu_{a b}, \sigma_{a b}\right)$ (if the Cauchy distribution is selected) to generate the investment $x_{a b}$ for the new individual.
Step 3: Examine whether $x_{a b}$ fulfills the related constraints. That is, $x_{a b}$ cannot be less than the minimum request $l_{a b t_{0}}$ or exceed the cash in hand $u_{a b}\left(t_{0}\right)$. If $x_{a b}$ exceeds $u_{a b}\left(t_{0}\right)$, it is set as $u_{a b}\left(t_{0}\right)$. If $x_{a b}$ is in the range of $\left[l_{a b t_{0}} / 2, l_{a b t_{0}}\right)$, it is set as $l_{a b t_{0}}$. If $x_{a b}$ is less than $l_{a b t_{0}} / 2$, it is set as 0 .
Step 4: Update the amounts of the cash in hand in the following years accordingly. More specifically, the maximum amount of investment for the other endowment policies should be recalculated using (13).

Step 5: Repeat steps 2-4 until the investment plan $\boldsymbol{X}$ for the endowment policies is fully determined. Then in combination with the choice of hospitalization policy determined in step 1, a feasible new individual is generated.
Repeat the above process till $N P$ new solutions are generated. Algorithm 2 gives the pseudocode of generating a new population.

## E. Local Search Strategy

To further improve the efficiency of the proposed AEDA, a local search strategy is employed. In this process, several individuals are generated by sampling the neighborhood around the best-so-far individual. The sampling operation is similar to the one developed in Section IV-D, which samples a new individual from the probability model built in advance.
For each individual generated in the local search process, the value of $\beta$ is decided according to the histogram model built in Section IV-C. As for the value of $\boldsymbol{X}=\left(x_{i j}\right),(i=$ $1,2, \ldots, n_{1}, j=1,2, \ldots, m_{i}$ ), it is generated by sampling the following distribution:

$$
X \sim N\left(X^{\text {best }}, \sigma_{l}\right)
$$

where $X^{\text {best }}$ denotes the best-so-far individual and is updated per generation. $\sigma_{l} \in\left(0, x_{i j}^{\text {best }}\right)$ is the scale factor of this distribution and set as 10 according to the magnitude of the solution in this paper. $N(\mu, \sigma)$ is a normal distribution with expectation $\mu$ and standard deviation $\sigma$.

## F. Overall Procedure

Based on the above operators, the overall procedure of AEDA can be described as follows.

Step 1 (Initialization): This process generates an initial population, in which each individual represents a feasible insurance investment plan.

Step 2: (Estimation of the Probability Models): This process estimates the probabilistic models of all the decision variables by learning from the best $N P_{\text {best }}$ individuals in the current population.

Step 3 (Adaptive Model Selection): For each individual in the population, this process automatically decides whether the

## Algorithm 2: New Population Generation

```
for \(k=1\) to \(N P\) do
        Choose \(\beta^{(k)}\) according to \(\beta_{i \_p}\)
        Decide index \({ }^{(k)}\) according to \(g \_p\)
        Initialize \(\widehat{C}^{(k)}(t)\)
        for \(i=1\) to \(n_{1}\) do
            randomly choose \(a\) from \(A\)
            \(A=A \backslash\{a\}\)
            \(B=\left\{1,2, \ldots m_{a}\right\}\)
            for \(j=1\) to \(m_{a}\) do
                randomly choose \(b\) from \(B\)
                \(B=B \backslash\{b\}\)
                if \(\operatorname{index}^{(k)}=0\)
                \(x_{a b}^{(k)}=N\left(\mu_{a b}, \sigma_{i j}\right)\)
                else
                \(x_{a b}^{(k)}=C\left(\mu_{a b}, \sigma_{i j}\right)\)
            end if
            if \(x_{a b}^{(k)}>u_{a b}\left(t_{0}\right)\)
            \(x_{a b}^{(k)}=u_{a b}\left(t_{0}\right)\)
            else if \(x_{a b}^{(k)}<l_{a b t_{0}}\) and \(x_{a b}^{(k)} \geq l_{a b t_{0}} / 2\)
                \(x_{a b}^{(k)}=l_{a b t_{0}}\)
            else if \(x_{a b}^{(k)}<l_{a b t_{0}} / 2\)
                \(x_{a b}^{(k)}=0\)
            end if
            for \(t_{1}=t_{0}\) to \(t_{0}+y_{a b}-1\) do
                \(\widehat{C}^{(k)}\left(t_{1}\right)=\widehat{C}^{(k)}\left(t_{1}\right)-x_{a b}^{(k)} \times\left(t_{1}-t_{0}+1\right)\)
            end for
            for \(t_{1}=t_{0}+y_{a b}\) to \(T_{1}\) do
                \(\widehat{C}^{(k)}\left(t_{1}\right)=\widehat{C}^{(k)}\left(t_{1}\right)-x_{a b}^{(k)} \times y_{a b}\)
            end for
        end for
        end for
    end for
2. end for
```

probabilistic models of continuous variables should follow the Gaussian distribution or the Cauchy distribution. The decision is made based on the performances of the two models in the previous generation.

Step 4 (New Population Generation): This process generates a new population of $N P$ feasible individuals by sampling from the probabilistic models built in steps 2 and 3.

Step 5 (Local Search): This process fine-tunes the best-sofar individual by sampling its neighborhood using the Gaussian distribution.

Step 6 (Termination Check): If the termination criterion is satisfied, the best-so-far solution is returned as the result. Otherwise, return to step 2 and start a new generation.

## V. Simulations and DisCussion

A specific example will be given in this section to help better understand how the optimization strategy given in Section IV can get a profitable insurance investment plan regarding the model given in Section III. To validate the effectiveness and efficiency of the proposed model and method, comparisons are made among different investment plans and different EDAs.

TABLE I
Settings of Policyholder's Income

TABLE II
Detailed Settings of the Endowment Policies


TABLE III
DETAILED SETTINGS OF THE HOSPITALIZATION POLICIES

## A. Experimental Settings

1) Settings of the Policyholder: We consider the situations that the policyholder has different initial age ( $t_{0}=$ $0,10,20,30,40,50,60)$ and different initial wealth ( $I_{0}=$ 100 000, 200 000, 500 000). The policyholder's yearly income, as shown in Table I, is set according to an investigation on the average salary of common wage-earners.

Assume that the policyholder is a male without the habit of smoking, and has not been diagnosed with any serious diseases that will affect his health in the future. Therefore, the mortality rate and the incidence rates of diseases with different serious degrees are set in accordance with the regular patterns.
2) Settings of Insurance Policies: In the simulation, five endowment policies and three hospitalization policies are considered. Detailed settings of the policies are tabulated in Tables II and III.

Here, the minimum of face amount $c_{i}$ is a factor that decides the minimum amount of investment $l_{i j t}$. For each endowment policy, the minimum face amount is the same while the minimum amount of investment is different: it is the investment amount in accordance with the face amount $c_{i}$.

As can be seen, the five endowment policies have different payment periods, latest purchasing time, and face amounts. Except the endowment policy B and D, all the other endowment policies focus on deposit, whose return is thus not related
![img-2.jpeg](img-2.jpeg)

Fig. 3. Comparison between different numbers of individuals during the local search process with situation $t_{0}=0$ and $I_{1}=200000$ (the fitness value in the figure is the mean value for 30 runs while the time is the total time for 30 runs).
to the purchasing time. The hospitalization policies have different coverage scopes. To be more exact, from policy A to policy C, the coverage scope expands from critical diseases, critical and serious diseases, to all types of diseases. Their premium also increases accordingly.
3) Settings of Algorithm Parameters: For each experiment, each algorithm is run for 30 independent times with 1000 generations. The population size $N P$ is set to be 300 [34]-[36]. The number of individuals selected for model estimation, $N P_{\text {best }}$, is set as $45 \%$ of the whole population, i.e., $N P_{\text {best }}=$ 135 (the comparison of different settings of $N P_{\text {best }}$ is given in Table IV and shown that $45 \% N P$ is most suitable for this optimization problem). The number of individuals generated during the local search is set as 10 (this is the most suitable number with relatively high performance and reasonable running speed according to Fig. 3).

## B. Comparison of Different Investment Plans

To illustrate the effectiveness and efficiency of the proposed insurance investment model, we compare its results with the yearly profit obtained by the traditional investment plans that purchase only a single policy (either an endowment policy with a specific payment period or a hospitalization policy). In this way, we can analyze whether it is necessary to consider investing multiple insurance policies.

The comparisons are shown in Fig. 4. With the horizontal axis indicating the time and the vertical axis indicating the amount of yearly profit, the curves in this figure show how the yearly profit of the investment plans generated by different strategies evolve over time. Note that for the proposed model, the results vary in different runs due to the influence of randomness. As such, the figure displays its results over 30 independent runs in the form of box plot.

As can be seen, the yearly profits obtained by the proposed model outperform all the other strategies for different initial ages. Moreover, the result of AEDA is so stable that its box plot is narrowed down to a line.

The effectiveness of the proposed method can also be observed by interpreting the insurance investment plans obtained. The following sections discuss the comparisons

TABLE IV
Comparisons Between Different Settings of $N P_{\text {best }}$ With Situation $T_{0}=10$ and $I_{0}=200000$


![img-3.jpeg](img-3.jpeg)

Fig. 4. Comparison of different investment plans for the situation $t_{0}=0$ and $I_{1}=200000$.

TABLE V
Investment Plans Under Different Initial Ages


under two situations: 1) different initial age with a fixed initial wealth and 2) different initial wealth with a fixed initial age. By doing so, the advantage of the proposed model can be analyzed in a comprehensive way.

1) Comparison Under Different Initial Ages: The comparison of the results obtained for policyholders with $t_{0}=0,10,20,30,40,50,60$ and $I_{0}=200000$ are
given in Table V. Situations for the other initial wealth are similar, which are not shown here due to the page limit.

To obtain the optimal yearly profit, the policyholder at age 0 is suggested to buy endowment policy A with 5- and 10-year payment periods, but not to buy any hospitalization policy. This is reasonable because the probability for

TABLE VI
Investment Plans Under Different Initial Wealth

TABLE VII
COMPARISON OF THE AEDA AND OTHER EDAS WITH DIFFERENT INITIAL AGE

a 0-year-old baby to get ill is low. Besides, if the policyholder purchased any hospitalization policy, he has to pay the premium for an extremely long period. At other initial ages, the policyholder is suggested to buy the endowment policy A with 5- and 10-year payment periods and the endowment policy E with one-time premium payment. This is probably because the policyholder has not been diagnosed with any serious diseases and maintained a healthy living style. Therefore, the possibility of his death is relatively low so that this policyholder is not suggested to buy any endowment policy focusing on life insurance. Note that the proposed method also suggests that the optimal amount of investment varies depending on the policyholder's initial age. In terms of the hospitalization policies, the proposed method suggests to choose policy B over the others. The reason is that this policyholder is currently in a good health condition and is unlikely to have general illnesses frequently. Therefore, it is
not necessary to buy hospitalization policy C. But the coverage of hospitalization policy A may not be secure enough, because as a common wage-earner, the medical expense will be a large burden for the policyholder once he gets some serious illness.
2) Comparison Under Different Initial Wealth: The comparison for 30-year old policyholders with $I_{0}=$ 50 000, 100 000, 200 000, and 500 000, are given in Table VI. The situations with other initial wealth are similar and thus not shown here due to the page limit.

It can be seen that for a 30-year old policyholder, when the initial wealth is 50000 , endowment policy A with a 10-year payment period and endowment policy D with a 6-year payment period should be chosen. With the augment of the initial wealth, no matter how much money the policyholder has at the beginning, he should choose endowment policy A with 5 - and 10-year payment period and endowment policy E with

TABLE VIII
CompAriSON OF the AEDA and Other EDAs With Different Initial WeAlth

one-time premium payment policy. In terms of the hospitalization policy, when the initial wealth is 50000 , the policyholder is suggested legible to buy policy A because he does not have enough economic strength to buy a more expensive one. As the initial wealth increases, he is suggested to buy policy B. However, even though the initial wealth is 500000 , he is not suggested to buy insurance C. This may be because that we make a hypothesis that the health condition of this policyholder is good so that policy B is sufficient and it is not necessary to buy policy $C$.

From the results above, it can be found that the proposed data-driven insurance investment strategy considers multi polices outperforms each of the single-policy strategy. Therefore, the necessity of considering different kinds of policies has been proven.

## C. Comparisons of Different EDAs

To validate the performance of the proposed AEDA, experiments are performed to compare it with following EDAs.

1) EDA that samples new population with Cauchy distribution only (EDA-C) [49].
2) EDA that samples new population with Gaussian distribution only (EDA-G) [34].
3) EDA that samples half of new population with Cauchy distribution and the other half with Gaussian distribution (EDA-H) [50].
4) EDA that samples the value of $\beta$ using Cauchy or Gaussian distribution like $x_{i j}$ and then round down to the nearest integer (EDA-R).
5) EDA without local search strategy (EDA-L).

For the sake of fairness, all the six EDAs are executed with the same parameter settings. The maximum value, median value, and standard deviation that each EDA obtained in 30 independent runs are reported for comparison. To examine the significance of the difference between the proposed AEDA and the other five EDAs, the Wilcoxon
rank sum test [51] is performed and the $p$-value is also reported.

The proposed AEDA and the above five EDAs are first compared with the initial age $t_{0}$ varying in the range of $\{0,10$, $20,30,40,50,60\}$ and the same initial wealth $I_{0}$ fixed at 200000 . The results are tabulated in Table VII. Then the six EDAs are compared with the initial age $t_{0}$ fixed at 30 and the initial wealth $I_{0}$ varying in the range of $\{50000,100000$, 200 000, 500 000\}. The results are shown in Table VIII.

Tables VII and VIII show that AEDA significantly outperforms EDA-C and EDA-D in all cases. It also significantly outperforms EDA-H in 7 out of the 11 cases. Therefore, the effectiveness of the adaptive model selection strategy for choosing sampled distribution has been confirmed. The comparison of AEDA with EDA-R shows that AEDA outperforms EDA-R in 10 out of the 11 cases, which shows the effectiveness of modeling different types of variables using different methods. The comparison of AEDA with EDA-L shows that AEDA outperforms EDA-L for some initial ages and some initial wealth, meaning that it is necessary to employ the local search strategy for some situations.

## VI. CONCLUSION

In this paper, a data-driven model is defined for optimization of the insurance investment plan that involves endowment and hospitalization policies. An AEDA is proposed to address the model, offering an individualized way to derive the optimal insurance investment plan that maximizes the yearly profit given the policyholder's initial age and wealth.

The use of evolutionary algorithms in the field of insurance investment optimization is a new attempt. This paper explores the possibility and rationality of such an attempt, and shows that evolutionary algorithms can be an efficient tool for optimizing insurance investment plans. This paper offers a new perspective and an effective way for realizing intelligentization and individualization of insurance investment.
