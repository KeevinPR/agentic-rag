# Combining a hybrid prediction strategy and a mutation strategy for dynamic multiobjective optimization 

Ying Chen ${ }^{\mathrm{a}, \mathrm{b}}$, Juan Zou ${ }^{\mathrm{a}, \mathrm{b}, \mathrm{c}}$, Yuan Liu ${ }^{\mathrm{a}, \mathrm{b}}$, Shengxiang Yang ${ }^{\mathrm{a}, \mathrm{d}}$, Jinhua Zheng ${ }^{\mathrm{a}, \mathrm{b}, \mathrm{e}}$, Weixiong Huang ${ }^{\mathrm{a}, \mathrm{b}}$<br>${ }^{a}$ Key Laboratory of Intelligent Computing and Information Processing, Ministry of Education, School of Computer Science and School of Cyberspace Science of Xiangtan<br>University, Xiangtan, Hunan Province, China<br>${ }^{b}$ Faculty of School of Computer Science and School of Cyberspace Science of Xiangtan University, Xiangtan, 411105, China<br>${ }^{c}$ Hunan Provincial Key Laboratory of Intelligent Information Processing and Application, Hengyang, 421002, China<br>${ }^{d}$ School of Computer Science and Informatics, De Montfort University, Leicester LEI 9RH, U.K

## A R T I C L E I N F O

Keywords:
Dynamic multiobjective optimization problems Evolutionary algorithms
Change response mechanism

## A B STR A C T

The environments of the dynamic multiobjective optimization problems (DMOPs), such as Pareto optimal front (POF) or Pareto optimal set (POS), usually frequently change with the evolution process. This kind of problem poses a higher challenge for evolutionary algorithms because it requires the population to quickly track (i.e., converge) to the position of a new environment and be widely distributed in the search space. The prediction-based response mechanism is a commonly used method to deal with environmental changes, but it's only suitable for predictable changes. Moreover, the imbalance of population diversity and convergence in the process of tracking the dynamically changing POF has aggravated. In this paper, we proposed a new change response mechanism that combines a hybrid prediction strategy and a precision controllable mutation strategy (HPPCM) to solve the DMOPs. Specifically, the hybrid prediction strategy coordinates the center point-based prediction and the guiding individual-based prediction to make accurate predictions. Thus, the population can quickly adapt to the predictable environmental changes. Additionally, the precision controllable mutation strategy handles unpredictable environmental changes. It improves the diversity exploration of the population by controlling the variation degree of solutions. In this way, our change response mechanism can adapt to various environmental changes of DMOPs, such as predictable and unpredictable changes. This paper integrates the HPPCM mechanism into a prevalent regularity model-based multiobjective estimation of distribution algorithm (RM-MEDA) to optimize DMOPs. The results of comparative experiments with some state-of-the-art algorithms on various test instances have demonstrated the effectiveness and competitiveness of the change response mechanism proposed in this paper.

## 1. Introduction

Dynamic multiobjective optimization problems (DMOPs) [1] exist in numerous real-world applications, such as greenhouse control [2], scheduling jobs [3], intelligent robot navigation [4] and industrial design [5]. DMOPs are characterized by some changes that may occur in the Pareto-optimal set in the decision space (POS) or Pareto-optimal front in the objective space (POF). Researchers are committed to finding a set of feasible decision variables to satisfy multiple conflicting objective functions changing over time.

Without loss of generality, to minimize the multiobjective problem as the research object, the mathematical model of a DMOP with $n$ decision

[^0]variables and $M$ objective functions can be described as:

$$
\begin{gathered}
\text { Minimize } \quad \mathbf{F}(\mathbf{x}, t)=\left(f_{1}(\mathbf{x}, t), f_{2}(\mathbf{x}, t), \ldots, f_{M}(\mathbf{x}, t)\right)^{\tau} \\
\text { s.t. } \mathbf{x} \in \Omega
\end{gathered}
$$

where $x=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ is an $n$-dimensional decision variable vector from the decision space $\Omega . F(x, t)$ is the objective function vector that evaluates solution $x$ at time period $t . f_{i}(x, t) \in\left\{=1,2, \ldots, M\right\}$ refers to the $i$ th objective function of $x$ at time period $t . \Omega=\left\{L_{1}, U_{1}\right\} \times\left\{L_{2}, U_{2}\right\} \times \ldots \times$ $\left\{L_{n}, U_{n}\right\}$, where $L_{i}$ and $U_{i}$ are the lower limit and upper limit of the $i$ th decision variable respectively. The descrete time parameter $t$ is defined as the following mathematical form:

$$
t=\frac{1}{n_{1}}\left\lfloor\frac{\tau}{r_{1}}\right\rfloor
$$

[^1]
[^0]:    * Corresponding author at: Key Laboratory of Intelligent Computing and Information Processing, Ministry of Education, School of Computer Science and School of Cyberspace Science of Xiangtan University, Xiangtan, Hunan Province, China.

    E-mail address: zoujuan@xtu.edu.cn (J. Zou).

[^1]:    * Corresponding author at: Key Laboratory of Intelligent Computing and Information Processing, Ministry of Education, School of Computer Science and School of Cyberspace Science of Xiangtan University, Xiangtan, Hunan Province, China.

    E-mail address: zoujuan@xtu.edu.cn (J. Zou).

![img-0.jpeg](img-0.jpeg)

Fig. 1. General framework of DMOEA.

Table 1
Different types of a DMOP.
where $r$ is the iteration counter, $n_{i}$ is the number of distinct time steps in $t_{1}$ and $r_{t_{i}}$ is the number of iterations where $t$ remains the same. $t$ controls the dynamics via $n_{t}$ and $r_{t}$ where $n_{t}$ governs the severity level and $r_{t}$ determines the frequency value.

According to whether POF or POS changes or not, DMOPs can be divided into four types, as shown in Table 1. Type I means that POS changes, but POF remains fixed. Type II illustrates that POF and POS both change. Type III means that POF changes, but POS remains unchanged. Type IV presents that both POF and POS remain unchanged, although the problem may change. Here, no attention is given to Type IV, although we recognize that the Type IV change may also occur in some exceptional cases. In addition, there are problems with a mixed type of change, such as JY9 [6]. According to the changes of POF or POS are predictable or not, DMOPs can be divided into problems with predictable changes and problems with unpredictable changes. Predictable change means that the POF or POS changes at least somewhat regularly according to some rules, rather than changing with no pattern between successive environments. Unpredictable changes mean changes of the POF or POS are dramatic or irregular.

Evolutionary algorithms (EAs) simulate natural selection and evolution of organisms and has been widely used to solve highly complex nonlinear problems [7]. Multiobjective evolutionary algorithms (MOEAs) [8-10] are capable of solving various static multiobjective optimization problems (MOPs). Because MOEAs use a multi-point simultaneous search mechanism, which can approximate the entire POS in one run. In recent years, dynamic multiobjective optimization evolutionary algorithms (DMOEAs) to address DMOPs have come into being. Some researchers assumed that a DMOP could be divided into a sequence of MOPs over time and directly migrated and adopted the techniques from static MOEAs [11]. However, environmental changes often take only a few iterations. Techniques directly from static MOEAs tend to fail in most DMOPs due to the lack of a quick change response mechanism.

An excellent DMOEA not only has a good MOEA optimizer but also designs a mechanism that can respond to changes quickly and well. Fig. 1 presents the flowchart of a typical DMOEA. The first key step of a classic DMOEA is change detection, assuming that the dynamics are detectable [12]. Re-evaluating the fitness of a solution is the most common method used to detect changes, provided that incorporated noise handling techniques [13]. Change response is the second key step. Because when a change is detected, the current evolutionary population is required to track and converge to a new POF within very few iterations. Moreover, the imbalance of population diversity and convergence
in the process of tracking the dynamically changing POF has aggravated. In other words, the previously obtained optimal solution cannot remain optimal in the new environment. At this time, an excellent change response mechanism to obtain solutions with good convergence and diversity seems particularly important. Earlier methods for change response include memory-based [14] and diversity maintenance [15] [16]. The former directly reuses historical POS to accelerate convergence, while the latter focuses on addressing diversity loss when change occurs. In recent years, prediction-based methods have gained much more attention. They usually adopt the promising historical information as the input to different prediction models (e.g., AR [17], KF [18] and SVR [19]) to predict future optimalities. The third key step is optimization using MOEA regardless of whether environmental changes occur, here we employ RM-MEDA [20] as the underlying MOEA optimizer. As is well known to us, the change response mechanism is the most pivotal, although the three steps mentioned above contribute to efficient problem-solving. Without loss of generality, the contribution of this paper focuses on the second step, that is, change response.

There are limitations in most existing change response mechanisms. Prediction-based methods can speed up convergence, but they may not be effective anymore in responding to unpredictable changes. Sometimes the environmental change may lead to severe diversity loss, so diversity-based methods are also indispensable. However, blindly focusing on diversity in most diversity-based methods will impact the convergency of the evolutionary population. Almost majority of methods are designed only to increase the speed of convergence or only to improve diversity. Can we combine the advantages of prediction-based methods and diversity-based methods to develop a hybrid response mechanism that can converge quickly and maintain diversity? Based on the question in mind, this paper proposes a new change response mechanism that combines a hybrid prediction strategy and a precision controllable mutation strategy (HPPCM).

The hybrid prediction strategy in this paper is good at responding to predictable changes, which coordinates the center point-based prediction and the guiding individual-based prediction to cooperate and complement each other. The center point-based prediction can respond well and quickly to varying degrees of linear changes. In contrast, the guiding individual-based prediction is better at solving nonlinear changes (such as periodic changes). The two in the hybrid prediction strategy make full use of their strengths to make more accurate predictions and accelerate responding to different types of predictable changes. In addition, the precision controllable mutation strategy can respond to unpredictable changes and improve the diversity exploration of the population. The experimental results on various test instances have proved that the HPPCM mechanism proposed in this paper is very competitive in solving DMOPs with different dynamic characteristics. The technical contributions of this paper are summarized as follows.
(1) The center point-based prediction strategy proposed could not only quickly respond to the same two consecutive environmental changes but also flexibly respond to the situation where the degree of the new

change is different from the last one. It employs a revised first-order difference linear prediction model to predict the new locations of current solutions when a change is detected.
(2) The guiding individual-based prediction strategy utilizes the evolutionary direction obtained by the autonomous evolution of the population for several generations to guide future search process and ensure the evolutionary population to approximate the new optimal solutions. It generates some guiding individuals along the evolutionary direction so as to cope with nonlinear (such as periodic) changes and explore the most promising optimization area in the decision space.
(3) The precision-controllable mutation strategy proposed could respond well to unpredictable changes by improving the diversity exploration of the population. It generates mutated solutions according to the required precision, which can not only increase the appropriate diversity but also reduce computational costs.

The remainder of this paper is organized as follows. Section 2 introduces the related work and motivation. The core strategies of HPPCM are presented in Section 3. Section 4 briefly introduces the comparison algorithm, test instances, performance indicators and experimental design. A series of experimental results are presented and analyzed in Section 5. Finally, Section 6 concludes this paper.

## 2. Preliminaries

In this section, some background knowledge related to our work and the motivation of this paper is introduced.

### 2.1. Related work

One common idea of prediction-based methods is that given predefined moving step size, the initial solutions to the new environment are obtained by moving the POS of the last time period along with the moving direction [21]. The moving direction is normally estimated by the first-order or second-order difference of some representative points from the previous POS. These representative points usually be the center points [22-25]; special points like knee points and extreme points [26,27]; and clustering centers of the POS [28]. After that, with the development and popularity of statistical machine learning, it gradually becomes the mainstream that utilizes historical information, such as the previous optimal solution sequence or the center point of the POS, to train the prediction model. Muruganantham et al. [18] proposed two variants of the Kalman filter (KF) predictor, which also performed the first-order and second-order difference prediction. In [19], the support vector regression (SVR) was employed to conduct nonlinear prediction. FPS proposed by Hatzakis and Wallace [29] and PPS proposed by Zhou et al. [17] both adopted autoregressive (AR) models. A mixture-of-experts-based ensemble framework [30] was introduced to conduct multiple predictors in a single run.

Generally, diversity-based methods use mutation of selected old solutions or random generation of some new solutions to improve diversity (such as [15], [31]), maintain diversity throughout the optimization process (such as [32]), or employ multipopulation mechanisms (such as [33]). For example, Vavak et al. [34] employed a mutation operator (VLS) to increase the diversity of their algorithm. In a triggered hypermutation method given by Woldesenbet and Yen [35], the mutation rate would increase immediately when an environmental change is detected. Goh and Tan [16] added randomly generated individuals into the competition pool to increase diversity. In [36], Camara et al. used nondominated individuals specifically for selection and mutation and applied crowding mechanisms to maintain diversity. Ruan et al. [37] proposed a stochastic diversity preservation strategy for diversity maintenance.

To summarize, prediction-based methods have been the dominant techniques for change response in solving DMOPs [21]. Diversity-based methods are widely used due to their simple implementation and effectiveness in addressing severe diversity loss. However, they are subject
to the limitations that we have mentioned in the previous section. It is desirable to develop more efficient methods for change response in DMOPs.

### 2.2. Motivation

The high frequency (need to be quickly responded to) and drastic (may cause severe diversity loss) environmental changes sometimes happen during the evolution process, bringing great challenges to DMOEAs. As we all know, prediction-based methods predict the state of the changing environment, typically using various predictors to adapt to changes in advance. Although the prediction-based methods have significant advantages over other methods in accelerating the response (convergence) speed, they tend to perform poorly when the POF or POS of a DMOP changes sharply and/or irregularly. Proper diversity increased by diversity-based methods helps explore promising search regions. However, some existing diversity-based methods either increase excessive diversity, which may cause evolutionary stagnation (e.g., reinitialize randomly), or are only effective for local search (e.g., Gaussian perturbation). As both prediction-based approaches and diversity-based approaches have strengths and weaknesses, a natural question arises: How can we leverage these strengths together to design a better change response mechanism to solve various types of DMOPs? To the end, this paper proposes an enhanced change response mechanism named HPPCM by combining a hybrid prediction strategy with a precision controllable mutation strategy.

In the hybrid prediction strategy, we redefine the movement step size $\alpha$ instead of predefining it as 1.0 like that in the general first-order linear prediction model. In addition, we find out the most promising decision space as the exploration space. In this way, we can quickly respond to different types of predictable changes by considering the varying degrees of adjacent environmental changes and exploring the most promising decision space. In the precision controllable mutation strategy, a Gaussian distribution with controllable precision is added to $\Delta \alpha$ against the original formula of PCM in [38]. Under the premise of setting the same accuracy $r$, the PCM in this paper can search for more solutions within the required precision with a more uniform probability, thus improving the population's diversity exploration ability.

## 3. Proposed algorithm

In this section, we elaborate on the specific HPPCM proposed in this paper. It consists of three sub-strategies, namely the center point-based prediction strategy, the guiding individual-based prediction strategy and the precision controllable mutation strategy. Finally, the overall framework of the algorithm is introduced, which integrates the change response mechanism named HPPCM into a regularity model-based multiobjective estimation of distribution algorithm (RM-MEDA) [20].

### 3.1. Center point-based prediction strategy

Environmental changes present linear and regularity in many cases, and the current environment may have the same or similar degree of change with the previous last environment. In these cases, we assume that the center points moving trend represents the population's moving trend. In other words, the other members of the population are supposed to have a similar moving trend with the center point. Therefore, the prediction for the moving trend of the center point is vital. At the same time, we should take into consideration that similar degree of change but not totally the same between the current environment and the previous last one. So when an environmental change is detected, we should use the useful information (the center point's moving trend) from the previous environmental change with varying degrees.

In this subsection, we follow the principle that the moving direction between the two consecutive environments is the same, but the moving

![img-1.jpeg](img-1.jpeg)

Fig. 2. Schematic diagram of the predicted population generation of population when $\alpha=0.5,1.0$ and 1.5 .
step size is different due to the degree of change between two consecutive environments to develop the prediction strategy. The center pointbased prediction strategy uses two populations, $P_{i}^{1}$ and $P_{i}^{2}$, respectively, to implement prediction with the same moving direction but different moving step sizes.
$P_{i}^{1}$ completely follows the step size of the center point's movement trend in the last environmental change, namely $\alpha=1$. It means that our algorithm can accurately respond to very similar changes to the previous last environmental change. Because of its simplicity and clarity, this usage is widespread in many existing first-order difference linear prediction models in DMOEAs.
$P_{i}^{2}$ is specifically designed for situations where the current environmental change is similar to but different from the previous last one. Because the similarity between continuous environmental changes has not been accurately measured, the moving step size of $P_{i}^{2}$ along the moving direction is uncertain. The current change is normally smoother or more drastic than the previous last one. The moving step size $(\alpha)$ is therefore defined as a random number between 0.5 (refers to more slightly change) and 1.5 (refers to more drastic change). Fig. 2 represents the schematic diagram of the predicted population generation when $\alpha$ is $0.5,1.0$ and 1.5 respectively in the population search process after the occurrence of new environmental changes.

The process is given in Algorithm 1. First, the moving direction $V_{t}$ is

## Algorithm 1 Center Point-based Prediction.

Input: $P_{i}$ (population at time period $t$ ), $C_{t-1}$ (center point of $P$ at time period $t-1$ ), $C_{t}$ (center point of $P$ at time period $t$ ), $m$ (the number of initial individuals), $t$ (time period)
Output: $P_{1}$

```
\(V_{t}=C_{t}-C_{t-1} ; \quad / /\) refer to Formula 3
\(P_{i}^{1}, P_{i}^{2} \leftarrow\) divide \(P_{i}\) into two randomly;
\(P_{t+1}^{1}, P_{t+1}^{2} \leftarrow\) generate new solutions at time period \(t+1 ; \quad / /\) refer to
```

Formula 5
4: $P_{1}=P_{t+1}^{1} \cup P_{t+1}^{2}$;
5: Return $P_{1}$
calculated by the moving direction of the center point from time period $t-1$ to $t$. Then the algorithm will randomly divide current population $P_{i}$ into two, named $P_{i}^{1}$ and $P_{i}^{2}$. According to Formula (5), it will generate some solutions to predict the new locations at time period $t+1$ of
old solutions (in $P_{i}^{1}$ and $P_{i}^{2}$ ). Finally, the algorithm will return the combination of the prediction solutions in $P_{t+1}^{1}$ and $P_{t+1}^{2}$ as $P_{1}$. The related definitions and formulas in the process will be introduced next.

The moving direction of center point at time period $t$ (denoted by $V_{t}$ ) is calculated as follows:
$V_{t}=C_{t}-C_{t-1}$
The formula for generating the predicted solutions at time period $t+1$ is as follows:
$x_{t+1}=x_{t}+\alpha V_{t}$
where $\alpha$ represents the moving step size, which means the step size of moving the old solutions of the $P_{i}$ along the center point's movement direction $V_{t}$.

Based on the solution $x_{t}$ at time period $t$, the prediction solution $x_{t+1}$ at time period $t+1$ is generated as follows:

$$
\left\{\begin{array}{ll}
x_{t+1}=x_{t}+V_{t} & x_{t} \in P_{1}^{1} \\
x_{t+1}=x_{t}+\text { random }(0.5,1.5) \times V_{t} & x_{t} \in P_{i}^{2}
\end{array}\right.
$$

### 3.2. Guiding individual-based prediction strategy

Some environmental changes of DMOPs are predictable but not linear (such as periodic). At this time, the prediction for the evolutionary direction of the population in the new environment is significant. If it is still assumed that the current population is moving in the same direction as the last time period like that in the first-order difference linear prediction model, it is likely to cause the prediction to fail. Therefore, how to accurately predict the evolutionary direction is the first key point. To this end, we let the current population spontaneously evolve some generations $(\Delta t)$ when an environmental change is detected. Then the center point's moving direction of the nondominated solutions will serve as a rough reference direction for future predictions.

The main idea of the guiding individual-based prediction strategy is as shown in Algorithm 2. First it will retrieve the nondominated so-

## Algorithm 2 Guiding Individual-based Prediction.

Input: $P_{i}$ (population at time period $t$ ), $m$ (the number of initial individuals), $t$ (time period)
Output: $P_{2}$

1: Iter (iteration counter) $\leftarrow 0$;
2: $\operatorname{POS}_{t} \leftarrow$ retrive the nodominated solutions at time period $t$;
3: $C_{t} \leftarrow$ calulate the center point of $P O S_{t}$;
4: while Iter $\leq \Delta t$ do
5: $\quad P_{\text {eff }} \leftarrow$ GetOffspring $\left(P_{\text {t+Iter }}\right)$;
6: $\quad P_{\text {t+Iter }} \leftarrow$ EnvironmentalSelection $\left(P_{\text {t+Iter }} \cup P_{\text {eff }}\right)$; // use the environmental selection operator of RM-MEDA
7: Iter $=$ Iter +1 ;
8: end while
9: $\operatorname{POS}_{t+\Delta t} \leftarrow$ retrive the nodominated solutions in $P_{t+\Delta t}$;
10: $C_{t+\Delta t} \leftarrow$ calulate center point of $\operatorname{POS}_{t+\Delta t}$;
11: $\operatorname{dir}$ (evolutionary direction) $\leftarrow C_{t+\Delta t}-C_{t}$;
12: $\operatorname{Pop}_{\text {init }}$ (initial individuals) $\leftarrow$ select $m$ solutions from $\operatorname{POS}_{t+\Delta t}$ with the largest crowding distance;
13: $\operatorname{Pop}_{\text {guide }}$ (guiding individuals) $\leftarrow$ generate $N-m$ new solutions; // refer to Formula 7
14: $P_{2}=P o p_{\text {init }} \cup P o p_{\text {guide }}$;
15: Return $P_{2}$;
lutions at time period $t\left(P O S_{t}\right)$ and the nondominated solutions after evolving for $\Delta t$ generations $\left(P O S_{t+\Delta t}\right)$, thus calculating the center point of $P O S_{t}$ and $P O S_{t+\Delta t}$ separately. Then a center point's moving direction of the nondominated solutions will be obtained by the vector difference from $C_{t}$ to $C_{t+\Delta t}$. The evolutionary direction (dir) for further prediction can be obtained according to Formula (6), also can be find in lines from 2 to 11 of Algorithm 2. Then $m$ initial individuals with the largest

crowding distance will be selected after sorting $\operatorname{POS}_{i}$ by crowding distance in ascending order. A bunch of guiding individuals are generated uniformly along the most promising decision space composed of current extreme points and boundary points according to the judgment of $d i r$ 's direction. These guiding individuals are stored to $P_{2}$, and the algorithm returns $P_{2}$.

Assume that $\operatorname{POS}_{i}=\left\{x_{i j}\right\}=\left\{x_{i}^{1}, x_{i}^{2}, \ldots, x_{i}^{n}\right\}$ represents all the nondominated individuals at time $t$ and $C_{i}$ is the center point of the nondominated solution set at time period $t .\left[\operatorname{POS}_{i}\right]$ is the cardinality of all nondominated individuals at time $t . i=1,2, \ldots, n$ represents the number of dimension of the decision variable. The definition of relevant variables in Algorithm 2 are as follows:
$d i r=\left\{d i r_{1}, d i r_{2}, \ldots, d i r_{t}, \ldots, d i r_{n}\right\}, \quad i=1,2,3, \ldots, n$,
where

$$
\begin{gathered}
d i r_{t}=C_{i+\Delta t}^{t}-C_{i}^{t} \\
C_{i}^{t}=\frac{\sum_{j, i \in \operatorname{POS}_{i}} x_{j}^{t}}{\left[\operatorname{POS}_{i}\right]}
\end{gathered}
$$

where $d i r$ represents evolutionary direction vector of population in decision space. $d i r_{i} \quad i=1,2, \ldots, n$ ) represents the $i$ th dimension decision variable's direction vector. $C_{i}$ is the population center pointat time period $t, C_{i+\Delta t}$ is the population center point after population evolving spontaneously for $\Delta t$ generations.

The selection of the initial individual and the determination of the evolutionary direction $d i r$ are all to generate some influential guiding individuals. According to $d i r$, every time the environment changes, our algorithm will predict a set of guiding individuals close to the new POS as possible based on $m$ initial individuals. The way we generate guiding individuals is not to randomly sprinkle points without purpose. Instead, we obtain the current population's extreme points (i.e., maximum point and minimum point). Two vectors are connected from current extreme points to the corresponding boundary points (i.e., the maximum point of the boundary and the minimum point of the boundary). Specifically, the current minimum point is connected to the maximum point of the boundary, and the current maximum point is connected to the minimum point of the boundary. We select the boundary points and the current extreme point to search the most potential (i.e., promising) decision space as thoroughly as possible.

When a certain dimensional direction vector $d i r_{i}$ is positive, the vector $D_{i}^{*}$ formed by the $i$ th dimension of minimum point and the $i$ th dimension of maximum boundary point of the current population is equally divided into $\frac{n}{m}$ parts. Each initial individual generates $\frac{n}{i}-1$ level individuals uniformly along the vector $D_{i}^{*}$. Otherwise, the vector $D_{i}^{-}$composed of the $i$ th dimension of maximum point and the $i$ th dimension of minimum boundary point of the current population is divided into $\frac{\pi}{m}$ parts. The $m$ initial individuals uniformly generate $\frac{\pi}{m}-1$ layers of individuals along the vector $D_{i}^{-}$. Finally, the $N-m$ guiding individuals combined with $m$ initial individuals are nondominated sorted. Fig. 3 shows the process of the operator evenly dividing the decision space and generating guiding individuals when $d i r$ is positive.

The specific methods of generating $N-m$ guiding individuals are as follows:
$y_{j \in k}^{i}= \begin{cases}x_{j}^{i}+\frac{\left|J R_{i}-l o u_{j}^{i}\right|}{N} \times k & \text { if } d i r_{i}>0 \\ x_{j}^{i}-\frac{\log \left|y_{j}^{i}-L R_{i}\right|}{N} \times k & \text { if } d i r_{i}<0\end{cases}$,
where

$$
\begin{aligned}
& i=1,2, \ldots, n \\
& j=1,2, \ldots, m_{j} \\
& k=1,2, \ldots, \frac{\pi_{j}}{m}-1
\end{aligned}
$$

where $y_{j \in k}^{i}$ means the $i$ th dimension of the $j \times k$ th solution. $x_{j}^{i}$ means the $i$ th dimension of the $j$ th solution. $U R_{i}$ is the largest and $L R_{i}$ is the smallest boundary of the $i$ th dimension. $\log h_{j}^{i}$ and $l o u_{j}^{i}$ are the $i$ th dimension values of the current maximum point and minimum point in
![img-2.jpeg](img-2.jpeg)

Fig. 3. When evolutionary direction $d i r>0$, the schematic diagram of the process of generating guiding individuals.
the decision space at $t$ time period. $n$ is the dimension of the decision variable, $m$ is the number of initial individuals, and $N$ is the population size. $d i r_{i}$ represents the $i$ th dimension decision variable's direction vector.

### 3.3. Precision controllable mutation strategy

In the process of tracking new POF or POS, the imbalance between convergence and diversity has increased. Especially when the environmental changes are unpredictable, the diversity-based strategy is widely used in DMOEAs. However, some existing methods like reinitialization randomly will increase excessive diversity, which may cause evolutionary stagnation. Other methods like Gaussian perturbation where Gaussian distribution is similar to the simulated binary crossover (SBX) [39] in that it generates offspring near the parent value with a high probability, so it is only effective for local search. Hence, it's desirable to design a more efficient diversity-based strategy.

This paper refers to the precision controllable mutation operator by Zhang et al. [38] and proposes another version of precision controllable mutation (PCM). The PCM operator formula in [38] is as follows:
$x_{i+1}^{i}=x_{i}^{i}+\Delta \alpha$,
$x_{i+1}^{i}=x_{i}^{i}-\Delta \alpha$,
where

$$
\Delta \alpha=\frac{1}{\operatorname{LipRandom}(r)} \times \text { Random }(9)
$$

Take $r=2$ and $x=3$ as an example, the mutation precision $\frac{1}{\operatorname{LipRandom}(r)}=\{0.1,0.01\}$. Random (9) can be regarded as a random integer coefficient from 1 to 9 . $\Delta \alpha$ could be $\{0.1,0.2, \ldots, 0.9,0.01,0.02, \ldots, 0.09\}$, the value of $x$ maybe $\{2.1,2.2, \ldots, 2.9,2.91,2.92, \ldots, 2.99,3.01,3.02, \ldots 3.09,3.1,3.2, \ldots, 3.9\}$. Obviously, Formula (8) and (9) can generate all the neighboring solutions of 3.0 within the precision of 0.01 and 0.1 .

The mutation operator formula of another version of PCM proposed in this paper is as follows:
$x_{i+1}^{i}=x_{i}^{i}+\Delta \beta$,
$x_{i+1}^{i}=x_{i}^{i}-\Delta \beta$,

where

$$
\begin{aligned}
& \Delta \beta=\Delta \alpha+\frac{\text { Gaussian }(0, s t d)}{\text { Diffimited }(r)} \\
& s t d=\sqrt{\frac{\sum_{i=1}^{n}\left(x_{i}^{2}-z\right)^{2}}{p-1}} \\
& \bar{x}=\frac{\sum_{i=1}^{n} x_{i}}{y}
\end{aligned}
$$

where $x_{i}^{2}$ is the $i$ th dimension decision variable at time period $t$, and $x_{i+1}^{t}$ is the new solution of the $i$ th dimension decision variable mutated by $x_{i}^{t}, i=1,2, \ldots, n$ represents the number of dimension of the decision variable. The Random $(r)$ function randomly generates an integer from 1 to $r$. std is the variance of each dimension decision variable $x_{i}, \bar{x}$ is the mean value of the decision variable $x_{i}$ and $y$ is the number of decision variables.
$\Delta \alpha$ and $\Delta \beta$ are used to control the precision of the variation to ensure that the range of the mutation is diverse. If the required precision needs to reach $0.0001, r$ can be set to 4 . Random $(r)$ might be $1,2,3$ and 4. $\frac{1}{\text { Diffimited }(r)}=\{0.1,0.01,0.001,0.0001\}$. When the accuracy is 0.001 and smaller, the population can search for the optimal solution locally in the decision space with small steps. When the required precision is 0.1 , the population can jump out of the local optimum and search in the global decision space with large strides.

From Algorithm 3 we can see that PCM in this paper is simple and

```
Algorithm 3 Precision Controllable Mutation.
Input: \(P_{i}\) (population at time period \(t), \(t\) (time period)
Output: \(P_{3}\)
    \(p=\operatorname{Random}(2)\)
    \(\Delta \alpha=\frac{1}{\text { Diffimited }(r)} \times \operatorname{Random}(9)\)
    \(\Delta \beta=\Delta \alpha+\frac{\text { Gaussian }(0, s t d)}{\text { Diffimited }(r)}\)
    if \(p==1\) then
        \(P_{i+1}=P_{i}+\Delta \beta ;\)
    else
        \(P_{i+1}=P_{i}-\Delta \beta ;\)
    end if
    \(P_{3} \leftarrow P_{i+1}\)
10: Return \(P_{3}\)
```

easy to implement. First, it will randomly initialize an integer $p$ between 1 to 2 . If $p$ is 1 , the mutation operator will follow Formula (10), otherwise it will be implemented according to Formula (11). Then those mutated solutions at time period $t+1\left(P_{i+1}\right)$ from the old solutions at time period $t\left(P_{i}\right)$ are stored to $P_{3}$. Finally, the algorithm returns $P_{3}$.

Take $r=2$ and $x=10$ as an example, let the original solution $x$ mutate 10,000 times according to the Formulas (8) and (9) and Formulas (10) and (11), respectively. Fig. 4(a) and (b) show the frequency diagram of the mutation solution distribution with PCM in [38] and PCM in this paper, respectively. By comparing the two figures, we find that taking the variation solution of $x=10.4$ as an example, the frequency in Fig. 4(a) has reached almost 600, and there is no value larger or smaller than 10.4 within the precision 0.01 . However, in Fig. 4(b), the frequency of 10.4 is no more than 8 , while the frequency of values around it within the precision 0.01 (e.g., 10.38 and 10.46) presents a Gaussian distribution. It means the mutation solutions (obtained by PCM in this paper) in Fig. 4(b) have better diversity and more uniform distribution. Under the premise of setting the same precision $r$, the mutation solution generated by PCM in this paper can search for the finer solution with a more uniform probability. It's because PCM in this paper adds precision controllable Gaussian distribution based on the original PCM in [38]. In the process of algorithm execution, the decision space under each required precision can be fully searched. In this way, the diversity exploration of the evolutionary population can be enhanced.

### 3.4. Algorithm framework

The algorithm combines HPPCM proposed in this paper (detailed in Sections 3.1, 3.2 and 3.3) with RM-MEDA to optimize DMOPs. RMMEDA is adopted as the evolutionary optimizer in Algorithm 4, while

## Algorithm 4 The overall framework of the algorithm.

Input: $N$ (population size), $\tau_{i}$ (the number of iterations where $t$ remainsthe same), $n_{t}$ (the severity of change), the stopping criterion
Output: $P$

1: Initialize a population $P$, the discrete time parameter $t \leftarrow 0$, iteration counter Iter $\leftarrow 0$;
2: while the stopping criterion is not met do
3: if change is detected then
4: $\quad t=t+1$;
5: $\quad C_{t} \leftarrow$ calulate the center point of $P$ at time period $t$; // the sub-strategies in HPPCM (change response mechanism) are the center point-based prediction strategy (line 6), the guiding individualbased prediction strategy (line 7) and the precision controllable mutation strategy (line 8)
6: $\quad P_{1} \leftarrow$ Center Point-based Prediction $\left(P^{t}:, \operatorname{dir}, C_{t}, t\right) ; \quad / /$ refer to Algorithm-1
$7: \quad P_{2} \leftarrow$ Guiding Individual-based Prediction $\left(P, C_{t}, V_{t}, t\right) ; \quad / /$ refer to Algorithm-A2
8: $\quad P_{3} \leftarrow$ Precision Controllable Mutation $(P, t) ; \quad / /$ refer to Algorithm-A3
9: $\quad P_{\text {in. }}$ Enice $\leftarrow$ BoundaryCorrection $\left(P_{1} \cup P_{2} \cup P_{3}\right)$
10: $\quad P \leftarrow$ EnvironmentalSelection $\left(P_{\text {in. } \text { bice }} \cup P\right) ; \quad / /$ use the environmental selection operator of RM-MEDA
11: else
12: $\quad P_{o f f} \leftarrow$ GetOffspring $(P) ; \quad / /$ use the reproduction operator of RMMEDA
13: $\quad P \leftarrow$ EnvironmentalSelection $\left(P \cup P_{o f f}\right) ; \quad / /$ perform environment selection operation of RM-MEDA
14: end if
15: Iter $=$ Iter +1
16: end while
17: Return $P$;
other evolutionary solvers can also be employed. It models a promising area in the search space by a probability model whose center point is a piecewise continuous manifold [20]. The Local PCA [40] algorithm was employed for building such a model. New candidate solutions are sampled from the model thus built. According to Algorithm 4, the algorithm starts with randomly generating $N$ initial solutions with a uniform distribution (line 1 of Algorithm 4). In each evolution generation Iter, Iter $=1,2, \ldots, \tau_{i}$ of each time period $t, t=1,2, \ldots$, the executive process are as follows. On the one hand, if an environmental change is detected, the center point $C_{t}$ of the population at period $t$ is calculated, and the change response mechanism HPPCM is triggered. The originality of this paper exactly lies in the change response mechanism HPPCM which consists three sub-strategies (lines 6-8 of Algorithm 4), where three subpopulations obtained by them $P_{1}, P_{2}, P_{3}$ are generated respectively by Algorithms 1-3. The key components of HPPCM are described in detail in the previous subsections. A merged population $P_{\text {in. }}$ bice consists of the three subpopulations $P_{1}, P_{2}$ and $P_{3}$ after boundary correction operation. Then we select $N$ solutions from the combination of $P_{\text {in.bice }}$ and $P$ by the environmental selection operators in RM-MEDA (line 10 of Algorithm 4), which is based on the nondominated sorting of NSGA-II [41] called NDS-Selection. On the other hand, if no environmental change is detected, it uses reproduction operators of RM-MEDA (i.e., modeling and sampling) to generate the offspring population $P_{o f f}$ (line 12 of Algorithm 4). Then the algorithm will use the environment selection operator named NDS-Selection mentioned above to select $N$ solutions between $P$ and its offspring population $P_{o f f}$ (line 13 of the

![img-3.jpeg](img-3.jpeg)

Fig. 4. Take $r=2$ and $x=10$ as an example, let the original solution $x$ mutate 10,000 times, the frequency diagram of the mutation solutions obtained by two versions of PCM.

Algorithm 4). Finally, the $N$ solutions are stored to $P$. The algorithm will terminate when the stopping criterion is met and return $P$.

As for change detection(line 3 of Algorithm 4), the algorithms used in this paper uniformly randomly select $5 \%$ of the individuals in the current population for re-evaluation. If the objective value changes, it proves that the current generation environment has changed.

It is worth noting that the boundary correction operator (line 10 of Algorithm 4) is applied to check whether the generated solution is within the given boundary of the decision space and if not, it will be corrected. The procedure of the boundary correction is described in detail as follows:
$x_{i+1}^{t}= \begin{cases}y & \text { if } L B_{i} \leq y \leq U B_{i} \\ 0.5 \times\left(x_{i}^{t}+U B_{i}\right) & \text { if } y<L B_{i} \\ 0.5 \times\left(x_{i}^{t}+U B_{i}\right) & \text { if } y>U B_{i}\end{cases}$
where $x_{i+1}^{t}$ is the corrected solution, and $y$ is the new solution generated by the change response mechanism in the algorithm proposed. $x_{i}^{t}$ is the value of the decision variable of the $i$ th dimension at time $t$, where $U B_{i}$ is the maximum boundary of the $i$ th dimension, and $L B_{i}$ is the minimum boundary of the $i$ th dimension.

## 4. Experimental setup

### 4.1. Test instances

Eighteen test instances are used in our proposed algorithm to compare with other algorithms. It contains three dMOP issues (dMOP1dMOP3) [16], four FDA issues (FDA1-FDA4) [1], five ZJZ issues (F5-F9)
[31] and six JY issues (JY1-JY6) [6]. The modified hypervolume difference (MHVD) and the modified inverted generational distance (MIGD) are used to test the performance of HPPCM and other popular algorithms. FDA test suit origins from ZDT [42] and DTLZ [43], while dMOP [1] and ZJZ [31] test suit origins from FDA [1]. The problem type of FDA and dMOP include Type I, II and III, while the ZJZ test suite only belongs to Type II, where there's no linkage between their variables. There exists nonlinear, time-varying and monotonic linkage between variables of the ZJZ test suite. JY test suite includes mixed type in addition to Type I, II and III, where there's nonlinear, time-varying and nonmonotonic linkage between variables. Among them, JY6 is a time-varying multimodal problem, where not only does the number of local optima change over time but also the POS is dynamically shifted.

### 4.2. Comparison algorithms

Five popular algorithms are used for comparison in this paper. They are DNSGA-II [15], PPS [17], PMS [44], PBDMO [11], and DVA [45] respectively, with different dynamic change response mechanisms. Among them, the DVA method is our previous work about solving DMOPs. It is worth reminding everyone that the work in this article is not an improved version based on the research of the DVA method. They are two quite different response mechanisms for solving DMOPs. The overview of DVA and the specific difference between DVA and HPPCM will be mentioned in the last two paragraphs of this section.

NSGA-II [41] is a classical algorithm for solving multi-objective problems. There are two versions of DNSGA-II: NSGA-II-A and NSGAII-B. In the DNSGA-II-A, the population is replaced by some individuals with

new randomly created solutions, while in the DNSGA-II-B, diversity is maintained by replacing a percentage of the population with mutated solutions.

PPS is representative of a prediction-based method. It models the trajectory of POF or POS in a dynamic environment and then uses the model to predict the new position of POS in PPS. The POS history information is divided into two parts, which are population center and manifold. When historical information is sufficient in the later stages of environmental changes, PPS has apparent advantages.

The overall framework of PMS is similar to our algorithm. It also uses RM-MEDA to optimize the population. But the change response mechanisms between it and our algorithm are quite different, especially in exploitation operators and diversity-based strategies.

Whenever a change is detected, the PBDMO proposed by Zhang et al. generated three subpopulations to reinitialize the population effectively. The three subpopulations were generated according to prediction, sampling and shrinking strategies.

The DVA method first analyzes the influence of each decision variable on individuals to distinguish between distribution-related decision variables and convergence-related decision variables in the new environment. Then for distribution-related decision variables, a hybrid prediction strategy combining Latin hypercube sampling [46] and random sampling is adopted to enhance the exploration ability of the population in the new environment. Otherwise, for convergence-related decision variables, the central point prediction method is used to accelerate the convergence speed of the population in the new environment. After the analysis of decision variables and the different prediction strategies based on the analysis, several solutions are generated and merged into a new population. Finally, an angle-based adaptive selection method is applied to the new merged population. Therefore, the DVA method can obtain the solutions with good convergence and diversity to make the initial population more adaptable to the new environment.

There is some obvious difference between DVA and HPPCM as follows. Firstly, DVA relies on the decision variable analysis method and executes different prediction strategies for different decision variables according to whether the decision variables are related to convergence or diversity. However, HPPCM does not distinguish the differences of decision variables and uses the same response strategy for each dimension of an individual's decision variables. Secondly, DVA generates the merged population based on a hybrid strategy combining Latin hypercube sampling and random sampling and the central point prediction method. However, HPPCM combines a hybrid prediction strategy and a precision controllable mutation strategy to generate a merged population. Finally, DVA proposes an angle-based adaptive selection method while HPPCM uses the classic NDS-Selection method to select better convergence and distribution solutions from the merged population.

### 4.3. Performance metrics

There are two typical comprehensive indicators for judging MOEAs in the field of multi-objective optimization, hypervolume difference (HVD) [22] and Inverted Generational Distance (IGD) [47], [48]. These two indicators are so typical that they can evaluate both the convergence and the distribution of an algorithm. Unfortunately, the particularity of the DMO makes the original IGD and HVD inappropriate as an evaluation indicator. So we adopt the modified hypervolume difference (MHVD) and the modified inverted generational distance (MIGD).

HVD measures the gap between the hypervolume of the approximate POF obtained by the algorithm and the hypervolume of the true POF. The definition of this indicator is described as:
$H V D\left(P O F_{t}, P_{t}\right)=H V\left(P O F_{t}\right)-H V\left(P_{t}\right)$,
where $\mathrm{HV}(s)$ is the hypervolume of the set $s$. MHVD is defined as the average value of HVD for some time steps in an environmental change under one operation. The formula to determine this indicator is calcu-
lated as:
$M H V D=\frac{\sum_{t \in T} H V D\left(P O F_{t}, P_{t}\right)}{|T|}$,
where $T$ is some time periods under one run. $|T|$ is the cardinality of $T$. The reference point is $\left(z_{1}+0.5, z_{2}+0.5, \ldots, z_{M}+0.5\right)$. Among them, $z_{j}$ is the maximum value of the $j$ th dimension objective value of the true POF, and $M$ is the objective dimension. Like HVD, MHVD evaluates the convergence and distribution of the algorithm at the same time. The larger the MHVD value, the better the algorithm performance.

Zhou et al. [17] modified the IGD metric and adopted the average of the IGD values in some time steps over a run as a performance indicator for DMOEA, which is computed as:
$I G D\left(P O F_{t}, P_{t}\right)=\frac{\sum_{t \in P O F_{t}}|P O F_{t} d\left(v, P_{t}\right)}{\left|P O F_{t}\right|}$,
where
$d\left(v, P_{t}\right)=\min _{n \in P_{t}} \sqrt{\sum_{j=1}^{N}\left(f_{j}^{v}-f_{j}^{n}\right)^{2}}$,
where $n$ is the dimensionality of the decision variable. $\mathrm{d}\left(v, P_{t}\right)$ is the minimum Euclidean distance between $v$ and $P_{t} . P O F_{t}$ is a set of Pareto optimal solutions obtained by a uniform sampling at time $t .\left|P O F_{t}\right|$ is the cardinality of $P O F_{t} . P_{t}$ is a set of solutions approximate to $P O F_{t}$ obtained by the algorithm.

MIGD is defined as the average value of IGD at some time steps in an environmental change under one operation. This index can comprehensively evaluate algorithm performance like IGD, including evaluation of convergence and distribution. The specific calculation formula is as follows:
$M I G D=\frac{\sum_{t \in T} I G D\left(P O F_{t}, P_{t}\right)}{|T|}$,
where $T$ is some time periods under one run. $|T|$ is the cardinality of T. Like IGD, MIGD evaluates the convergence and distribution of the algorithm at the same time. The smaller the MIGD value, the better the algorithm performance.

### 4.4. General parameter settings

The parameter settings for the test instances and comparison algorithms are as follows. RM-MEDA was adopted as the evolutionary optimizer of all comparison algorithms. In addition, the change detection method in all comparison algorithms was the same as that used in our work. That is, $5 \%$ of the population was randomly selected and re-evaluated to detect environmental changes. We fixed the change detection method and the static evolutionary optimizer to compare the performance of the response mechanism of the used algorithm more fairly and objectively.

General parameter settings in all test instances: Except for FDA4 and F8, which are tri-objective problems, all other test cases are bi-objective problems. We set the population capacity $N=100$ for all test problems. Decision variable dimension $D$ was set to 20 . We fixed the environmental change frequency $\tau_{c}$ to 30 and set $\sigma_{c}$ to 5,10 and 20 , representing severe, gentle and slight environmental changes, respectively. Each algorithm ran 20 times independently for each test instance. Every simulation experiment was carried out for 3600 generations, and 120 environmental changes were tracked.

Specific parameter settings in each algorithm: All the parameters in the compared algorithms used the same settings as in their original studies.
(1) Parameters in PPS: The order in $\operatorname{AR}(\rho)$ model was $\rho=3$, the number of cluster was set 5 and the maximum length of history center point sequence was $M=23$.

Table 2
MIGD indicators of six algorithms on dMOP and FDA test suites.
(2) Parameters in PMS: The number of guide individual in exploration operator was $O b s i z e=10$, the number of initial individual was $O P=$ 10, the number of aliquots was $O B=9$, and the time of evolving independently was $\delta t=2$. The number of selected optimal individuals from memory pool was $M$ size $=5$ (three objectives: 10 ).
(3) Parameters in PBDMO: The maximum memory size of the two archive sets $D$ and $C$ was set to 50 . The threshold $c$ introduced in Algorithm 2 of PBDMO was empirically set to $10^{-4}$.
(4) Parameters in DVA: $N 2=0.8 N, N 3=0.2 N$ in the prediction strategy and $\delta=0.9998$ in the adaptive selection strategy.
(5) Parameters in this paper(HPPCM): The algebra $\Delta t$ of autonomous evolution in Section 3.3 is set to 2 ; the parameter $r$ in Section 3.4 is set to 2 .

## 5. Experimental results and analysis

Under parameter configurations described in the previous subsection, HPPCM is evaluated on four test suites summed up to eighteen test instances, including dMOP1-dMOP3, FDA1-FDA4, F5-F9 and JY1-JY6. The algorithm is independently run 20 times and terminated on each test instance when the number of function evaluations reaches 360,000 for each run. The statistics (the mean and standard deviation, where standard deviation displays in brackets) of each metric (MIGD and MHVD) over 20 runs compared with other state-of-the-art dynamic multiobjective algorithms are computed and listed in Tables 2 - 7. Those compete algorithms include DNSGA-II [15], PPS [17], PMS [44], PBDMO [11], and DVA [45] respectively. To intuitively compare the performance of HPPCM and its competitors, the evolution curve of the MIGD value and approximate POF under the first 30 time periods are plotted in Figs. 510 , with $\left(n_{i}, r_{i}\right)=(10,30)$. Table 8 represents the results of the competition between HPPCM and two outstanding multi-modal MOEAs. Discussion on the three components of the proposed algorithm HPPCM are shown in Table 9 and analyzed in Section 5.6. To make the comparison results in Tables 2-9 much clearer and obvious, the best results for the performance of each test instance are bolded, and the background color is filled with gray, while the second-best ones are only bolded. To scientifically assess each algorithm, the multiple comparisons test(Friedman test in this paper) combined with a set of post hoc analysis tests(Holm, Hochberg, and Bonferroni adjustment used in this paper) is applied to the obtained results in Tables 2-9. In the end, the average rankings of each method on all test instances and the unadjusted/adjusted $p$ - values obtained by the application of post hoc procedures are listed in Tables 10-12.

### 5.1. Results on dMOPs and FDAs

It is shown by Tables 2 and 3 that HPPCM is very competitive compared to DNSGA-II, PPS, PMS, PBDMO and DVA, concerning the number of the cases where it obtains the best and the second-best results. dMOP1-dMOP3, FDA1- FDA4 sums up to 7 test instances. Each problem corresponds to 3 cases where the value of $n_{i}$ differs, so there are 21 cases altogether for each algorithm. Among 21 cases for each algorithm presented in Table 2, HPPCM obtains the best MIGD results in 13 cases and the second-best ones in 5 cases. Table 3 shows that HPPCM obtains the best MHVD results in 16 cases and the second-best in 3 cases. We know that MIGD and MHVD distinguish algorithms more reliably in terms of overall performance. Despite the changes in $n_{i}$, other algorithms lost to HPPCM on these two metrics. It demonstrates that HPPCM can better adapt to the drastic changes in different environments to obtain better distribution and convergence solutions.

There is no connection between the decision variables of dMOP1-dMOP3. The statistics of 20 runs on these three simple test issues show that HPPCM is the best in most cases, and if not, the gap with the best method is extremely small. When $n_{i}=5$, PPS has the best performance on dMOP2 and FDA1. PPS accumulates and makes full use of rich historical information in the later stage, which significantly improves prediction accuracy. At this time, PPS reacts very quickly to environmental changes, and the population is evenly distributed after converging to the new POS.

DNSGA-II has the smallest MIGD and biggest MHVD on FDA2. HPPCM proposed in this paper is second only to DNSGA-II, which introduces random individuals in response to change. From the performance of the six algorithms used in this paper on these two indicators, except for the fixed POS problem FDA2, they can accurately approximate the true POF. In addition, HPPCM is better at tracking the POS (or POF) with major changes. On the FDA4 issue of the three objectives, the statistics of each algorithm running 20 times are relatively poor.

### 5.2. Results on ZJZs

It is shown by Tables 4 and 5 that HPPCM is the most competitive one on the ZJZ test suite (F5-F9) compared to other well/known algorithms because it almost always obtains the best MIGD and MHVD no matter what the value of $n_{i}$ is large or small. It indicates that the POF obtained

![img-4.jpeg](img-4.jpeg)

Fig. 5. Evolution curve of MIGD value of six algorithms on representative test cases for time period $t$ from 0 to 30 , with $\left(n_{t}, \tau_{t}\right)=(10,30)$.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Scatter plots of the population obtained by HPPCM and the other peer algorithms (mean MIGD value) on dMOP2 for time period $t$ from 0 to 30 . The green line is POF in different environments. Red dots represent solutions obtained by five algorithms.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Scatter plots of the population obtained by HPPCM and the other peer algorithms (mean MIGD value) on dMOP3 for time period $t$ from 0 to 30 . The green line is POF in different environments. Red dots represent solutions obtained by five algorithms.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Scatter plots of the population obtained by HPPCM and the other peer algorithms (mean MIGD value) on FDA1 for time period $t$ from 0 to 30 . The green line is POF in different environments. Red dots represent solutions obtained by five algorithms.

Table 3
MHVD indicators of six algorithms on dMOP and FDA test suites.
Table 4
MIGD indicators of six algorithms on ZJZ test suites.
Table 5
MHVD indicators of six algorithms on ZJZ test suites.
by the algorithm proposed in this paper is close to the true POF, showing its excellent tracking ability. From the tables, with the decrease of $n_{i}$ (that is, the dramatic increase in environmental changes), the performance of other algorithms except for HPPCM significantly deteriorates. It proves that HPPCM has significant advantages in the ZJZ test suite, and the ability to solve problems does not change considerably with the drastic changes in the environment.

We know that there are nonlinear, time-varying and monotonic links between the decision variables of F5-F9, which are more complicated than the FDA and dMOP issues. Therefore, even though our algorithm performs significantly better than other algorithms on these problems, the statistics of MIGD and MHVD are worse than those on the FDA and dMOP issues.

Table 6
MIGD indicators of six algorithms on JY test suites.

Table 7
MHVD indicators of six algorithms on JY test suites.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Scatter plots of the population obtained by HPPCM and the other peer algorithms (mean MIGD value) on F9 for time period $t$ from 0 to 30 . The green line is POF in different environments. Red dots represent solutions obtained by five algorithms.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Scatter plots of the population obtained by HPPCM and the other peer algorithms (mean MIGD value) on JY3 for time period $t$ from 0 to 30 . The green line is POF in different environments. Red dots represent solutions obtained by five algorithms.

Table 8
MIGD and MHVD indicators of MO_Ring_PSO_SCD and MOAGDE on dMOP, FDA, ZJZ and JY test suites.

# 5.3. Results on JYs 

Tables 6 and 7 imply the statistical data (MIGDand MHVD) of each algorithm running 20 times on the JY test suite (JY1-JY6). JY1- JY6 sums up to 6 test instances. For each problem, they correspond to 3 cases where the value of $n$, differs, so there are 18 cases altogether for each algorithm. Among 18 cases for each algorithm, HPPCM obtains the best MIGD results in 8 cases and the second-best ones in 8 cases. Table 6 displays that HPPCM receives the best MHVD results in 9 cases and the second-best ones in 4 cases. As far as MIGD is concerned, there are 8 cases PMDMO performs best. As far as MHVD is concerned, it obtains the best MHVD results in 8 cases. Judging from the indicators of MIGD and MHVD, the convergence and distribution performance of HPPCM and PBDMO on the JY test suite is $50 / 50$

Table 9
Performance comparison of different HPPCM variants on MIGD for $\left(n_{i}, \tau_{i}\right)=(10,30)$.

### 5.4. Other comparative experiments

In addition to the tabular format, we also provide the evolution curve of the IGD value under the first 30 time periods of most test cases. We find from Fig. 5 that for most of the test problems, the MIGD curve of HPPCM is relatively flat and as low as close to the coordinate axis. It suggests that compared with other algorithms, HPPCM responds more stably to changes and recovers faster. The only exception is dMOP2. PPS performed poorly because of insufficient historical information accumulation before $t=6$, but it performed best after $t=16$. Thence comprehensively, the average IGD (MIGD) value was worse than HPPCM under the 30 time periods.

By observing Fig. 5, it is not difficult to find that the MIGD value of the algorithm fluctuates greatly on most problems, such as dMOP2, dMOP3 and FDA3. Nevertheless, compared with other algorithms, HPPCM has the smallest fluctuation range and more stable performance. To understand the tracking ability of these algorithms intuitively, we also plot the approximate POF obtained by each algorithm on dMOP2, dMOP3, FDA1, F9, JY3, for $\left(n_{i}, \tau_{i}\right)=(10,30)$, in Figs. 6-10. Compared with the data table and the index value change curve, the approximate POF graph can more intuitively reflect the excellent tracking ability of HPPCM. Figs. 6-10 clearly shows that in addition to HPPCM, the approximate POF obtained by other algorithms on most test cases cannot accurately fit the true POF. It shows that HPPCM has a powerful ability to respond to environmental changes. For the two fixed POF test cases, FDA2 and dMOP3, HPPCM has the defect that it is relatively difficult for some solutions (including boundary solutions) to converge. Therefore, it also affects the MIGD and MHVD index values that reflect convergence on these issues.

In our previous work, the comparison algorithm used is always the classic DMOEA, such as DNSGA-II, PPS, etc. We found that multimodal MOEAs mainly design operators in the decision space, such as the dominance relationship in the decision space and the special crowding distance [49]. Dynamic MOEAs are also usually operated in the decision space, such as the analysis of decision variables [45], the crowding distance ranking in the decision space [38]. It is precisely because of this commonality that we finally added a powerful and another newest multi-modal MOP algorithm as a competitor. They are MO_Ring_PSO_SCD [49] and MOAGDE [50] respectively. The MIGD and MHVD indicators of MO_Ring_PSO_SCD and MOAGDE on dMOP, FDA, ZJZ and JY test suites can be found in Table 8. Obviously, HPPCM wins over these two no matter judging by MIGD metric and MHVD metric.

### 5.5. Component analysis

The proposed framework in this paper has three key components and it has shown competence. Here, we use ablation studies to verify the effectiveness of each component separately. The ablation experiment is similar to the "controlled variable method." Suppose that a certain system used A, B and C, and has achieved good results. We could keep two of the three and remove one to verify whether the deleted one plays a role in the entire system. In this subsection, we modify HPPCM to three variants. The first variant, HPPCM-V1, only discards the center point-based prediction strategy we proposed and retains the guiding individual-based prediction strategy and the precision controllable mutation strategy. It's not difficult to find that HPPCM-V1 is designed to verify whether the center point-based prediction strategy plays a decisive role in HPPCM. The guiding individual-based prediction strategy is switched off to study its importance to the framework in this paper, and this variant is called HPPCM-V2. Similarly, we also deactivate the precision controllable mutation strategy to study the role it plays in our proposed algorithm, resulting in another variant named HPPCM-V3.

These three variants are all compared with the original HPPCM, and their MIGD values on eighteen test instances for $\left(n_{i}, \tau_{i}\right)=(10,30)$ are presented in Table 9. It is evident from the results of the experimental comparison that the overall performance of the original version of HPPCM is better than other variants. This also reflects from the side that each component is indispensable for the overall performance of HPPCM. Removing any of them causes somewhat performance degradation in general. Thus, it is a good way to combine them in one algorithm, as done by HPPCM. It is not surprising to see that HPPCM-V1 performs worse than HPPCM. The reason may be due to the fact that the center point-based prediction strategy in HPPCM would generate many nondominated solutions closer to new optima. The lack of this strategy in HPPCM-V1 is not good for population convergence. For those periodic problems, the evolution direction at a certain time step may be completely opposite to the direction of the previous time step. The guiding individual-based prediction strategy can accurately predict the evolution direction in the current environment, thereby adjusting the area where the predicted solution is generated. This is why the performance of HPPCM-V2 after removing this strategy has significantly decreased on periodic problems such as dMOP1, dMOP2, F5, F6, F7, F9. The precision controllable mutation strategy proposed in this paper is contributed to ensuring the diversity of our algorithm. Thus the lack of this strategy in HPPCM-V3 will definitely make the performance of indicators worse than HPPCM.

Table 10
Average rankings and adjusted $p$-values obtained of each algorithm through Friedman test on all test problems (HPPCM is the control method whose average ranking is 1.3889 ).
Table 11
Average rankings and adjusted $p$-values obtained of multi-model MOEAs through Friedman test on all test problems (HPPCM is the control method whose average ranking is 1.0 ).

Table 12
Average rankings and adjusted $p$-values obtained of different HPPCM variants through Friedman test on all test problems (HPPCM is the control method whose average ranking is 1.0 ).
### 5.6. Statistical analysis

One of the most frequent situations for statistical tests is in multidata analysis, where the experimental results achieved by multiple algorithms in computational intelligence are required to be tested. We have the result of every algorithm for each test problem, but we are not allowed to make a pairwise comparison for each pair of algorithms without losing the control on the Family-Wise Error Rate (FWER) [51]. Statistical tests can perform two classes of analysis: pairwise comparisons and multiple comparisons. Both belong to non-parametric tests, and they are more robust and less sensitive to dirty data. Pairwise statistical procedures compare a pair of algorithms performance in several benchmarks. Therefore, multiple comparisons tests should be used to carry out a comparison that involves more than two algorithms. In this paper, a multiple comparisons test known as Friedman test [52] is performed to investigate the results obtained by different algorithms, with $\left(n_{i}, \tau_{i}\right)=(10,30)$. In the Friedman test, two hypotheses, the null hypothesis $H_{0}$ and the alternative hypothesis $H_{1}$ are defined. The null hypothesis is a statement of no significant differences between algorithms, whereas the alternative hypothesis represents the presence of a significant difference between algorithms [52]. One more critical term in the Friedman test is the $p$-value, which is the probability of obtaining a result at least as extreme as the one that was actually observed, assuming that $H_{0}$ is true [53]. We compute the $p$-value of every hypothesis using a normal approximation for a statistic that depends on the non-parametric test used. However, as we previously stated, singular $p$-values should not be used for multiple comparisons due to the loss of control over the FWER, so an adjustment is made to obtain the adjusted $p$-values [54]. Several post hoc procedures are available for the computation of the adjusted $p$-values. We finally choose Holm, Hochberg and Bonferroni [55].

To scientifically assess the performance of HPPCM and other state-of-the-art dynamic MOEAs, the Friedman test is applied to the obtained results, and the associated $p$-value is 0.005 , indicating that there exit significant differences over the whole multiple comparisons among all algorithms. The average rankings of each algorithm on all test instances are listed in Table 10. Table 10 shows that our HPPCM gets the best average ranking (1.3889) outperforming PMS (2.6667), which are fol-
lowed by DVA (3.4444) and PBDMO (3.8333), while DNSGA-II (4.7778) and PPS (4.8889) get worse rankings compared to their counterparts. As we can see in this table, the Friedman test shows a significant improvement of HPPCM over PMS, DVA, PBDMO, DNSGA-II and PPS for all considered post hoc procedures, with a level of significance of 0.05 . The proposed algorithm is significantly better than other competitors with a level of significance of 0.005 for the Holm and Hochberg tests. In comparison with multi-modal MOEAs, It is shown by Tables 11 that HPPCM gets the best average ranking (1.0) outperforming MOAGDE (2.2778) followed by MO_Ring_PSO_SCD (2.7222). From the table, HPPCM is far better than MOAGDE and MO_Ring_PSO_SCD for all considered post hoc procedures, with a level of significance of 0.00005 .

In addition, Tables 12 displays the average ranking of all HPPCM variants and the adjusted $p$-value with the application of three post hoc methods. Not surprisingly, HPPCM obtains the best average ranking (1.0) outperforming HPPCM-V3 (2.667) followed by HPPCM-V1 (2.889), while HPPCM-V3 (3.444) get the worse rankings compared to other variants. From the table, HPPCM is far better than its three variants for all considered post hoc procedures, with a level of significance $=0.00001$. It shows the effect of the combination of the three sub-strategies is considerable to improve the algorithm's performance comprehensively. However, the ranking of the three variants also reflects the difference in their contribution to HPPCM. In particular, HPPCM's hybrid prediction strategy is more effective than the mutation strategy. Among them, the hybrid prediction strategy's second strategy (guiding individual-based prediction strategy) may be the most effective. The second strategy that improves the overall performance is its first strategy (center point-based prediction strategy). The role of the precision controllable mutation strategy is relatively minimal.

## 6. Conclusion

Responding quickly to the new environment and converging to the new POS while maintaining good distribution is the standard for evaluating the performance of a DMOEA. This paper proposes a new change response mechanism called HPPCM, consisting of a hybrid prediction strategy and a precision controllable mutation strategy. The hybrid prediction strategy focuses on convergence and responds quickly to predictable changes. The mutation strategy responds to unpredictable changes well and increases the diversity exploration of the population. Experimental results on several test suits have demonstrated that HPPCM combined with the RM-MEDA framework have obtained a set of well-distributed solutions which could converge to the POF or POS of most DMOPs in the new environment efficiently.

HPPCM has shown promising performance on various benchmark problems, but there is still room for further improvement. Our current actual algorithm version is not able to address combinatorial problems,

HPPCM can only handle continuous problems. In the center point-based prediction strategy, the moving step size (a) can be determined by detecting the intensity of environmental changes. If the intensity of new environmental changes detected is the same as the last one, then the moving step size (a) can be set to be 1.0 definitely. If the former is much larger than the latter, then $a$ will be $r$ more than 1.0 , like 1.5 . Otherwise, we can set $a$ less than 1 , like 0.5 . In this way, the solutions predicted by the center point-based prediction strategy will be more close to the new optima.

## Declaration of Competing Interest

We declare that we have no financial and personal relationships with other people or organizations that can inappropriately influence our work, there is no professional or other personal interest of any nature or kind in any product, service, and company that could be construed as influencing the position presented in, or the review of, the manuscript entitled "Combining a Hybrid Prediction Strategy and a Mutation Strategy for Dynamic Multiobjective Optimization."

## Acknowledgements

The authors wish to thank the support of the National Natural Science Foundation of China (Grant No. 61876164, 61772178), The MOEA Key Laboratory of Intelligent Computing and Information Processing, the Science and Technology Plan Project of Hunan Province (Grant No. 2018TP1020), the Provinces and Cities Joint Foundation Project (Grant No. 2017JJ4001), Science and Technology Planning Project of Guangdong Province of China (Grant No. 2017B010111005), the Hunan province science and technology project funds (Grant No. 2018TP1036).
