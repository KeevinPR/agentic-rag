# Environment identification-based memory scheme for estimation of distribution algorithms in dynamic environments 

Xingguang Peng $\cdot$ Xiaoguang Gao $\cdot$ Shengxiang Yang

Published online: 11 February 2010
(c) Springer-Verlag 2010


#### Abstract

In estimation of distribution algorithms (EDAs), the joint probability distribution of high-performance solutions is presented by a probability model. This means that the priority search areas of the solution space are characterized by the probability model. From this point of view, an environment identification-based memory management scheme (EI-MMS) is proposed to adapt binary-coded EDAs to solve dynamic optimization problems (DOPs). Within this scheme, the probability models that characterize the search space of the changing environment are stored and retrieved to adapt EDAs according to environmental changes. A diversity loss correction scheme and a boundary correction scheme are combined to counteract the diversity loss during the static evolutionary process of each environment. Experimental results show the validity of the EI-MMS and indicate that the EI-MMS can be applied to any binary-coded EDAs. In comparison with three state-of-the-art algorithms, the univariate marginal distribution algorithm (UMDA) using the EI-MMS performs better when solving three decomposable DOPs. In order to understand the EI-MMS more deeply, the sensitivity analysis of parameters is also carried out in this paper.


[^0]Keywords Estimation of distribution algorithm $\cdot$
Dynamic optimization problem
Environment identification $\cdot$ Memory scheme $\cdot$
Diversity compensation

## 1 Introduction

In the real world, optimization problems are usually time-varying and it is very important to get the optimum in a short and acceptable time. Many researchers have contributed to this challenging issue of solving dynamic optimization problems (DOPs). Evolutionary algorithms (EAs) are inspired by the evolutionary process in nature. From the evolutionism point of view, the nature process simulated by EAs is changing, random, and uncertain in itself. Therefore, it is very reasonable to use EAs to solve DOPs. The simplest way to react to an environmental change is to regard each change as the arrival of a new optimization problem, and solve it from scratch. However, the time between every two environmental changes is usually rather short in most DOPs. Hence, the restart approach cannot satisfy most of real-world DOPs. In recent years, researchers have developed many methods to maintain a sufficient diversity level for EAs to continuously adapt to the changing landscape. They can be classified into four categories (Jin and Branke 2005): (1) generating diversity after a change, such as the hyper-mutation method (Cobb 1990); (2) maintaining the diversity throughout the run, such as the random immigrants (Grefenstette and Fitzpatrick 1992), sharing or crowding mechanisms (Cedeno and Vemuri 1997), and the thermodynamical genetic algorithm (GA) (Mori et al. 1996); (3) memory-based approaches (Branke 1999), and (4) multi-population approaches, such as the


[^0]:    X. Peng $(\boxtimes) \cdot$ X. Gao

    School of Electronics and Information, Northwestern
    Polytechnical University, Xi’an, Shaanxi 710129, China
    e-mail: pxg0510@gmail.com
    X. Gao
    e-mail: xggao@nwpu.edu.cn
    S. Yang

    Department of Computer Science, University of Leicester, University Road, Leicester LE1 7RH, UK
    e-mail: s.yang@mcs.le.ac.uk

self-organizing scouts GA (Branke et al. 2000), the multi-national GA (Ursem 2000), and the shift balance GA (Wineberg and Oppacher 2000). Comprehensive surveys on EAs applied to dynamic environments can be found in (Branke 2001; Jin and Branke 2005; Morrison 2004).

The essence of DOPs is to search the optimum in the solution space dynamically. For such a dynamic process, the historic information generated in the previous search process is very useful. An intuitional method is to store the high-performance historic solutions and reuse them later so as to improve the search process. But this method involves a large memory space and a complex memory management scheme. Estimation of distribution algorithms (EDAs) are a class of probability model based EAs, where the processes of learning and sampling the probability model replace the genetic operations (e.g., crossover and mutation) in conventional GAs. A probability model indicates the joint probability distribution of high-performance solutions. That is, it characterizes the set of good solutions. If the historic information could be stored as probability models, we would not only save the memory space but also simplify the memory management scheme. Consequently, EDAs are suitable for being extended to be memoryenhanced EAs to solve DOPs.

To this end, an environment identification-based memory management scheme (EI-MMS) is proposed in this paper. Within this scheme, a probability model is regarded as the learning result of the probability distribution of high-performance solutions in an environment. A probability model together with the best individual in the solutions from which the probability model is learnt are stored as a memory element. In order to retrieve the memory elements in EI-MMS, an environment identification method is proposed to select the suitable element according to a special environment. The EI-MMS can be used to extend any binary-encoded static EDA to its dynamic version and we name the corresponding algorithm as EDA with environment identification based memory scheme (EI-MEDA).

Considering the fact that the diversity of conventional EDAs will loss gradually while the learning and sampling processes of the probability models are executed alternately, in this paper, the reason to diversity loss is briefly analyzed and an effective diversity compensation method is introduced into EI-MEDA to enhance its performance in dynamic environments.

The rest of this paper is organized as follows. Section 2 presents the description of the proposed EI-MEDA. In Sect. 3, the diversity loss reason is first analyzed and some diversity loss counteracting methods are then introduced into EI-MEDA. Section 4 presents the experimental results and analysis. Finally, conclusions are drawn in Sect. 5.

## 2 Description of the EI-MEDA

In this section, we present the details about the EI-MEDA. Any static binary-coded EDA can be extended to its corresponding EI-MEDA using EI-MMS. From this point of view, an EI-MEDA is composed of two main parts: the basic EDA and EI-MMS. The former aims at searching optimum in each environment and the latter aims at adapting to the environment changes.

### 2.1 Introduction of EDAs

The concept of EDAs was firstly proposed in 1996 (Mühlenbein and Paaß 1996). In an EDA, the probability distribution of high-performance solutions is estimated and is used to generate new candidate solutions. There are five main steps in EDAs: selection, learning, sampling, replacement, and evaluation which is shown in Fig. 1. It can be seen that the learning and sampling steps replace the crossover and mutation operations in simple GAs.

### 2.2 The EI-MMS

This EI-MMS scheme uses additional memory and the elements stored are the probability models learnt from the population. Before giving the details, we assume that the environmental changes are detectable. In all the algorithms below, the environmental change is detected in each generation by checking whether there is at least one memory element whose evaluation value has changed.

In order to utilize the intervals between every two environmental changes to learn a high-quality probability model, EI-MEDA updates its memory just after the

```
begin
    t:=0
    Randomly initialize first population P
        repeat
        select promising solutions S from P (selection)
        estimate the probability distribution of S (learning)
        generate offspring O using the estimate (sampling)
        create a new population P P by replacing some
            solutions from P with O (replacement)
        evaluate the individuals in P P (evaluation)
        t:=t+1;
    until terminated = true;
end;
```

Fig. 1 Pseudocode for EDAs

environment changes. As shown in Fig. 2, the whole dynamic optimization process is divided into many static optimization processes. In each static process, EDA searches the optimum in its conventional way. When the $e$ th environment comes at generation $t$, EI-MMS manages its memory $\mathbf{M}$ in three major steps. First, it stores the probability model obtained from the generation just before the environmental change, i.e., $\operatorname{PM}(t-1)$, into the memory. Then, it finds a memory element $M\left(k_{e}\right)\left(k_{e}=1,2, \ldots, m\right)$ which best fits the new environment to retrieve using an environment identification method. Finally, the probability model of this memory element, i.e., $m \mathrm{PM}\left(k_{e}\right)$, is sampled to generate the first generation of population in the new environment.

### 2.3 The environment identification method

The environment identification method is very important due to its role of linking between the memory and the dynamic environment. A key aspect of EI-MMS is to find the suitable memory element to retrieve according to the new environment. An intuitive way of achieving this is to consider the average fitness of the solutions sampled from a special element. Considering the computational complexity and the accuracy, we propose a samples averaging plus best individual (SA + BI) method to evaluate the elements in the memory and select the suitable one.

### 2.3.1 The samples averaging (SA) method

The idea of this method is to evaluate a memory element by averaging the fitness of solutions sampled from it. For each memory element $M(k)(k=1, \ldots, m), N_{\mathrm{S}}$ solutions are sampled from it and the average fitness of these sampled solutions is calculated in the current environment as the evaluation value of $M(k)$ as follows.
$f_{M}(k)=\frac{1}{N_{\mathrm{S}}} \sum_{i=1}^{N_{\mathrm{S}}} f_{m d(i)}^{k}$
where $f_{m d(i)}^{k}$ denotes the fitness of the $i$ th solution sampled from the probability model, i.e. $m \mathrm{PM}(k)$ of $M(k)$. This
![img-0.jpeg](img-0.jpeg)

Fig. 2 Illustration of the EI-MMS
method is the most intuitive way to evaluate a memory element but its computational complexity is high.

### 2.3.2 The best individual (BI) method

In this method, each memory element consists of two parts: a probability model and the best individual of the population from which the probability model is learnt. Here, we denote the memory element by $M(k)=\langle\mathrm{BM}(k)$, $m \mathrm{PM}(k)\rangle(k=1,2, \ldots, m)$, where $\mathrm{BM}(k)$ denotes the best individual. The evaluation of the memory element $M(k)$ is defined as follows:
$f_{M}(k)=f(\mathrm{BM}(k))$
where $f(\mathrm{BM}(k))$ denotes the fitness of $\mathrm{BM}(k)$ in the current environment. This method is similar to the method used in (Yang 2005b, 2006).

In contrast with the SA method, the accuracy is sacrificed for the sake of the computational complexity. The BI method uses the fitness of the best individual to evaluate the probability model learning from a set of individuals. This may lead to inaccuracy. For example, it is impossible to differentiate two elements when the fitness of their best individuals is equal.

### 2.3.3 The SA + BI method

In order to balance the accuracy and the computational complexity, we combine the above two methods, resulting in the SA + BI method. For comparing two memory elements, if the fitness of the best individuals are different, the BI method is applied; otherwise, the SA method is applied to differentiate the memory elements. Figure 3 shows how to select a memory element with the SA + BI method, where a maximization problem is assumed. The pseudocode of the proposed EI-MEDA with the SA + BI method is shown in Fig. 4, where $N_{\text {pop }}$ denotes the population size and $p_{\mathrm{s}}$ denotes the truncation selection rate (i.e., for each generation, the $p_{\mathrm{s}} \times N_{\text {pop }}$ best samples generated from the current model $\mathrm{PM}(t)$ are selected to build up the model $\mathrm{PM}(t+1)$ for the next generation).

## 3 Diversity loss and counteracting methods

The conventional EDA is likely to search the space where it has visited, just like the GA without a mutation operation. When the probability distribution of a decision variable is close to 1 or 0 , it is difficult to change its value anymore. This is the so-called fixed-point problem and it may mislead the search process to a local optimum. Some researchers have contributed to this challenge (Branke et al. 2007; Shapiro 2003, 2005, 2006).

Input: $M(i)=\langle B M(i), m P M(i)\rangle,(i=1,2, \ldots, m)$
Output: The suitable memory element $M$ (index)
$\max$ fit $:=0$ and index $:=1$;
for $i:=1$ to $m$ do
Calculate $f_{M}(i)$ by Eq. (2);
if $f_{M}(i)>\max$ fit then
$\max$ fit $:=f_{M}(i)$ and index $:=i$;
else if $f_{M}(i)=\max$ fit then
Calculate $f_{M}(i)$ and $f_{M}($ index $)$ by Eq. (1);
if $f_{M}(i)>f_{M}($ index $)$ then index $:=i$;
endfor;
return $M($ index $)$;
Fig. 3 Pseudocode for the SA + BI method

```
begin
P M(0,i):=0.5, mP M(j,i):=0.5, i \in[1, l], j \in[1, m]
Randomly generate BM(j), t:=0, k:=0;
Randomly initialize first population P
repeat
    if an environment change is detected then
        \(\langle B M(k), m P M(k)\rangle:=\langle B(t-1), P M(t-1)\rangle\);
        Update the fitness value of each \(B M(j), j \in[1, m]\);
        Select a proper \(m P M(k)\) using the SA+BI method;
        \(P M(t):=m P M(k)\);
        Sample \(P M(t)\) to generate \(P_{\mathrm{t}}\);
    else
        Evaluate \(P_{\mathrm{t}}\);
        Select the \(p_{\mathrm{a}} \times N_{\text {pop }}\) best individuals from \(P_{\mathrm{t}}\)
        Learn \(P M(t)\);
        Compensate the diversity for \(P M(t)\) by the method
            described in Section 3;
            Sample \(P M(t)\) to generate the \(t\)-th offspring \(O_{t}\);
            Evaluate \(O_{t}\) and replace the worst individuals in \(P_{\mathrm{t}}\);
            \(B(t):=\) BestIndividual \() P_{\mathrm{t}}\);
        \(t:=t+1\);
    until terminated \(=\) true;
end;
```

Fig. 4 Pseudocode for the proposed EI-MEDA

### 3.1 The reason to the diversity loss

It is well known that the variance of a sample of size $N$ has an expected value of $\sigma^{2}(1-1 / N)$ where $\sigma^{2}$ is the variance in the parent distribution. Most EDAs do not compensate
for this. When the new probability model is produced, it attempts to model the new population, and therefore, has a reduced variance. When this is iterated repeatedly, the variance of the sampled population gets smaller and smaller and decays to zero. The probability model evolves to one which can only generate identical configurations. In Shapiro (2005) analyzed the dynamics of EDAs in terms of Markov chains and declared that the general EDAs cannot satisfy two necessary conditions for being effective search algorithms. Hence, we must counteract the diversity loss to improve the efficiency of an EDA.

### 3.2 Basic diversity compensation methods

As mentioned above, EI-MMS is in fact a diversity maintaining method according to the environmental changes. It is also important to counteract the diversity loss in static EDA which searches the optimum in each environment. Here, we introduce some basic diversity compensation methods for binary EDAs. According to the experimental study in Branke et al. (2007), the method that combines the loss correction and boundary correction methods, denoted $\mathrm{LC}+\mathrm{BC}$ in this paper, is outstanding to counteract the diversity loss. Hence, we use the LC + BC method as the basic diversity compensation method in EI-MEDA. The details are given below and the experimental results are shown in the next section.

### 3.2.1 The loss correction (LC) method

Let $l$ be the length of a chromosome and $\gamma_{i}(i=1, \ldots, l)$ be the probability that the allele of the $i$ th gene is equal to $1, \gamma_{i}$ is transformed to $\gamma_{i}^{\prime}$ to counteract the diversity loss as follows:
$\gamma_{i}^{\prime}= \begin{cases}\frac{1-\sqrt{1-4\left(1-\gamma_{i}\right) / L_{s}}}{2}, & \gamma_{i} \leq \frac{1}{2}\left(1-\sqrt{1-L_{\mathrm{S}}}\right) \\ \frac{1+\sqrt{1-4\left(1-\gamma_{i}\right) / L_{s}}}{2}, & \gamma_{i} \geq \frac{1}{2}\left(1+\sqrt{1-L_{\mathrm{S}}}\right) \\ 0.5, & \text { otherwise }\end{cases}$
where $L_{\mathrm{S}}=\frac{p_{\mathrm{a}} \times N_{\text {pop }}-1}{p_{\mathrm{a}} \times N_{\text {pop }}-p_{\mathrm{s}}}$.

### 3.2.2 The boundary correction (BC) method

For the BC method, $\gamma_{i}$ is transformed to $\gamma_{i}^{\prime}$ to counteract the diversity loss as follows:
$\gamma_{i}^{\prime}= \begin{cases}\beta, & \gamma_{i}<\beta \\ 1-\beta, & \gamma_{i}>1-\beta \\ \gamma_{i}, & \text { otherwise }\end{cases}$
where $\beta$ is a preset parameter to prevent the distribution from converging to 1 or 0 . To guarantee the minimal diversity level, $\beta$ is set to $1 / l$ in this paper unless stated otherwise.

### 3.2.3 The $L C+B C$ method

For the LC + BC method, LC and BC are applied in turn. In other words, LC is first applied to $\gamma_{i}$, then the resulting $\gamma_{i}^{\prime}$ is taken as the input to the BC method. As shown in Fig. 5a, at the beginning of the searching process, i.e., $\gamma_{i}$ is close to 0.5 , the effect of LC is the strongest because it always returns $\gamma_{i}$ to 0.5 . At the early searching stage, this effect that LC counteracts $\gamma_{i}$ from evolving towards 0 or 1 enables the population search more widely in the solution space. But, LC cannot prevent the population from converging because it does not guarantee the minimal diversity level. On contrast, as shown in Fig. 5b, BC can prevent a distribution from converging by forcing the distribution with a minimal diversity level. Therefore, the combination of LC and BC, as shown in Fig. 5c, cannot only enable the algorithm to search widely but also prevent the population from converging when the distributions are close to their extreme value, i.e., 0 or 1 .

## 4 Experimental study

### 4.1 Dynamic test environments and measurement

Here, we present a bitwise exclusive-or (XOR) DOP generator, which was first proposed in Yang (2003) and Yang and Yao (2005) and then finalized in Yang (2005a) and Yang and Yao (2008). This DOP generator can construct three types of dynamic environment (cyclic, cyclic with noise, and random environment) from any binary-encoded function $f(\mathbf{x}), \mathbf{x} \in\{0,1\}^{l}$ by an XOR operator. For each environmental period $k$, a XORing mask $\mathbf{M}(k)$ is incrementally generated as follows:
$\mathbf{M}(k)=\mathbf{M}(k-1) \oplus \mathbf{T}(k)$
where " $\oplus$ " is the XOR operator and $\mathbf{T}(k)$ is an intermediate binary template randomly created with $\rho \times l$ ones for the environmental period $k$. With this DOP generator, the random environment can be constructed. The parameter $\rho$ controls the severity of the environmental changes while $\tau$ controls the change speed. It is worth noting that the environment changes at every $\tau$ fitness evaluations in this paper. This is different from Yang and Yao (2005, 2008), where the environment changes every $\tau$ generations.

With the DOP generator, cyclic dynamic environments are constructed as follows. First, we can generate $2 K$ XORing masks as the base states in the search space randomly (see Yang 2005a; Yang and Yao 2005 for details). Then, the environment can cycle among these base states in a fixed logical ring. Furthermore, for constructing cyclic with noise environment, each time the XORing mask $\mathbf{M}(k)$ moves to the next state after bitwise flipping with a small
![img-1.jpeg](img-1.jpeg)

Fig. 5 The effect of LC, BC, and LC + BC on $\gamma^{\prime}$, assuming $N_{\text {pop }}=$ $20, \beta=0.05$, and $p_{\mathrm{s}}=0.5$. a LC, b BC, c LC + BC
probability $p_{\mathrm{n}}$, called the noise rate in this paper. For the first period $k=1, \mathbf{M}(1)$ is set to a zero vector. Then, the population at generation $t$ is evaluated as follows:

$f\left(\mathbf{x}, t_{\mathrm{e}}\right)=f(\mathbf{x} \oplus \mathbf{M}(k))$
where $t_{\mathrm{e}}$ is the fitness evaluation number and $k=\left\lceil t_{\mathrm{e}} / \tau\right\rceil$ is the environmental period index.

In order to measure the performance of algorithms, the collective mean fitness (Morrison and De Jong 1999) is used in this paper. This measurement calculates the average of the best-of-generation fitness across the whole generations. Suppose each experiment is performed $N_{\mathrm{E}}$ times independently with the same experimental settings, the collective mean fitness $\left(F_{\mathrm{CMF}}\right)$ is formulated as follows:
$F_{\mathrm{CMF}}=\frac{1}{\mathrm{G}} \sum_{i=1}^{G}\left(\frac{1}{N_{\mathrm{E}}} \sum_{j=1}^{N_{\mathrm{E}}} F_{\mathrm{BOG}}(i, j)\right)$
where $G$ is the total generation number and $N_{\mathrm{e}}$ denotes the quantity of the environment periods in each run and $F_{\mathrm{BOG}}(i, j)$ denotes the best-of-generation fitness of the $i$ th generation in the $j$ th run.

In order to understand the effect of memory scheme and diversity compensation measures on the population diversity during the running of an algorithm, we also recorded the diversity of the population every generation. The diversity of the population at time $t$ in the $k$ th run of an algorithm on a DOP is defined as
$\operatorname{Div}(k, t)=\frac{1}{l \times N_{\text {pop }}\left(N_{\text {pop }}-1\right)} \sum_{i=1}^{N_{\text {pop }}} \sum_{j \neq i}^{N_{\text {pop }}} \mathrm{HD}(i, j)$
where $l$ is the encoding length, $N_{\text {pop }}$ is the population size, and $\mathrm{HD}(i, j)$ is the Hamming distance between the $i$ th and $j$ th individual in the population. The mean population diversity of an algorithm on a DOP at time $t$ over $N_{\mathrm{E}}$ runs is calculated as follows:
$\overline{\operatorname{Div}}(k, t)=\frac{1}{N_{\mathrm{E}}} \sum_{k=1}^{N_{\mathrm{E}}} \operatorname{Div}(k, t)$

### 4.2 Test functions

Decomposable unitation-based functions (DUFs), such as trap and deceptive functions, have been widely studied in the EA community in the attempt to understand what constructs difficult problems for EAs, especially for GAs (Goldberg 2002). In this paper, in order to analyze the performance of investigated algorithms in dynamic environments, three DUFs (denoted DUF1, DUF2, and DUF3) are selected as the stationary test functions. Each DUF consists of 25 copies of 4-bit building blocks and each building block contributes a maximum value of 4 to the total fitness, as shown in Fig. 6. The building block of the three DUFs are defined in Eqs. (10), (11), and (12), respectively.
![img-2.jpeg](img-2.jpeg)

Fig. 6 The building block of the three DUFs
$f_{\mathrm{DUF} 1}(x)=u(x)$
$f_{\mathrm{DUF} 2}(x)= \begin{cases}4, & \text { if } u(x)=4, \\ 2, & \text { if } u(x)=3, \\ 0, & \text { otherwise }\end{cases}$
$f_{\mathrm{DUF} 3}(x)= \begin{cases}3-u(x), & \text { if } u(x)<4, \\ 4, & \text { otherwise }\end{cases}$
where $u(x)$ denotes the number of ones in a building block.
DUF1 is, in fact, the OneMax function, which aims to maximize the number of ones in a chromosome. OneMax functions are usually taken as easy functions for EAs. For DUF2, in the search space of the 4-bit building block, the unique optimal solution is surrounded by only four suboptimal solutions, while all the other 11 solutions form a wide plateau with zero fitness. The existence of this wide gap makes it much more difficultly for EAs to search on DUF2 than on DUF1. DUF3 is a fully deceptive function (Goldberg 2002). Fully deceptive functions are usually considered hard problems for EAs because the low-order building blocks inside the functions do not combine to form the higher order optimal building block: instead they combine into deceptive sub-optimal building blocks (Whitley 1991). Generally, the three DUFs form an increasing difficulty for EAs in the order from DUF1 to DUF2 to DUF3.

In this paper, the dynamic test problems are constructed by applying the XOR DOP generator to the three DUFs and the corresponding dynamic DUFs are denoted DDUF1, DDUF2, and DDUF3, respectively.

### 4.3 Experimental results and analysis

In this section, we present the results of four groups of experiments. The first group of experiments shows the validity of EI-MEDA by comparing it with EDAs without the environment identification based memory method. The second group of experiments compares the performance of EI-MEDA with some state-of-the-art algorithms for DOPs.

Table 1 The $F_{\mathrm{CMF}}$ value of UMDA, UMDA(LC + BC), EI-MUMDA, RUMDA, and RUMDA(LC + BC) over 50 runs on DDUFs in three types of dynamic environments
The third group of experiments aims to show that EIMEDA can fit for any binary-coded EDAs. Finally, in order to deeply understand the proposed EI-MEDA, the sensitivity analysis of the effect of key parameters in EI-MEDA is also carried out in the fourth group of experiments.

In the experiments, some common settings are given as follows. Each algorithm was run 50 times in each experiment (i.e., $N_{\mathrm{E}}=50$ ). The total number of environmental changes $N_{\mathrm{e}}$ was set to 200 . The dimension of each DDUF is 100 (i.e., each DDUF is encoded with 100 bit binary strings). The memory size $m$ was set to 20 and the truncation selection rate $p_{\mathrm{s}}$ was set to 0.5 .

### 4.3.1 Validation of EI-MEDA

The purpose of this group of experiments is to verify the validity of EI-MEDA. In EI-MEDA, the LC + BC and EIMMS schemes work together to maintain the population diversity. The former works when the algorithm searches in a static environment while the latter works to respond to an environmental change. From this point of view, we compare EI-MEDA with several variants of EDAs, using the univariate marginal distribution algorithm (UMDA) (Mühlenbein and Paaß 1996) as an example EDA. We compare the following four algorithms: the original UMDA (denoted by UMDA), UMDA with LC + BC [denoted by UMDA(LC + BC)], UMDA with both EI-MMS and LC + BC (i.e., EI-MUMDA), UMDA with restart method (denoted by RUMDA), and UMDA with restart and LC + BC methods [denoted by RUMDA(LC + BC)]. The parameters are set as follows: $\tau=1,000, \rho=0.2, p_{\mathrm{n}}=$ 0.01 , and $N_{\text {pop }}=100$.

Table 1 shows the performance of each algorithm. From Table 1, it can be seen that by introducing LC + BC into the conventional UMDA, the performance of the algorithm UMDA(LC + BC) is enhanced a lot since the population diversity loss is compensated in each generation. In addition, if the EI-MMS scheme which reacts to environmental
changes is applied to reuse memory information, the performance of the algorithm can be further enhanced. Therefore, it is obvious that no matter how the environment changes, EI-MUMDA benefits from both LC + BC and EI-MMS and performs the best on all DDUFs.

In contrast to EI-MUMDA, the algorithms that use the restart method [RUMDA and RUMDA(LC + BC)] compensate the population diversity in a totally blind way and hence, their performance is worse. Since RUMDA and RUMDA(LC + BC) do not use any historic information and restart from scratch when the environment changes, their performance is not greatly affected by the environmental dynamics type (i.e., cyclic, cyclic with noise, or random).

Another noticeable result is that although both the restart and LC + BC schemes improve the performance of UMDA [i.e., both RUMDA and UMDA(LC + BC) beats UMDA], it is not good to use them together in UMDA [i.e., the performance of RUMDA(LC + BC) is worse than both RUMDA and UMDA(LC + BC)]. This happens because the effect of enhancing the diversity level by the restart and LC + BC schemes may be too strong for RUM$\mathrm{DA}(\mathrm{LC}+\mathrm{BC})$ to perform efficient search in a new environment.

Figure 7 shows the average dynamic population diversity of four algorithms in the first $100 \times 100$ fitness evaluations (i.e. ten environmental changes). From Fig. 7, it can be seen that UMDA poorly maintains its population diversity and can not adapt for the environmental changes. UMDA(LC + BC) can maintain its population diversity at a minimal diversity level using the LC + BC method. In each generation, at least $1 / l \times N_{\text {pop }}$ individuals are randomly generated by the LC + BC method. When the environment changes, the population has to converge to the new optimum using the learning and sampling operations of the conventional UMDA. This leads to the small fluctuations in the population diversity level of UMDA(LC + BC).

![img-3.jpeg](img-3.jpeg)

Fig. 7 The average dynamic population diversity of algorithms over 50 runs in the first $100 \times 100$ fitness evaluations on DDUF1 (left column), DDUF2 (middle column), and DDUF3 (right column) in
three types of environments: cyclic environment (top row), cyclic environment with noise (middle row), and random environment (bottom row)

The LC + BC method is originally designed for compensating diversity in static environment and is lack of efficiency to track the moving optimum. If the information in the past optimization process could be used to infer the distribution of the new optimum and the population could be heuristically generated, the efficiency of dynamic optimization would be enhanced greatly.

According to this idea, EI-MUMDA stores the past probability models and reuse them to generate the initial population in a new environment. In the environment with cyclic or cyclic with noise environments, a probability model in the memory will be refined if it is retrieved back. In addition, by using the environment identification, the initial population in an environment can be generated around the possible optimum according to the memory. This is more efficient than the conventional evolutionary operators.

From the first two rows in Fig. 7, it can be seen that the diversity level of EI-MUMDA is lower and more smooth than that of UMDA(LC + BC). In the randomly changing
environment, from the bottom row of Fig. 7, it can be seen that the diversity level curves of EI-MUMDA and UMDA(LC + BC) overlap with each other. This is because the memory in EI-MUMDA can not refine its elements (probability models) properly due to the randomly changing environment. Therefore, one can say that EI-MEDA performs well in dynamic environments, especially in dynamic environments with cyclic characteristic. As for RUMDA and RUMDA(LC + BC), although the restart method enables the original UMDA to react to environmental changes, these two algorithms are still defeated by EI-MUMDA. Because the restart method compensates population diversity in a blind and random way. As shown in Fig. 7, when environment changes (at every 1,000 fitness evaluations), the population is regenerated randomly and the diversity level goes up to about 0.5 . In such a blind diversity compensation way, no useful information can be used to guide the population to track the optimum.

### 4.3.2 Comparison with the state-of-the-art algorithms

In this group of experiments, we compare EI-MUMDA with the following three algorithms: memory enhanced population-based incremental learning algorithm (MPBIL) (Yang 2005b), MPBIL with two populations and restart scheme (MPBIL2r) (Yang and Yao 2008), and random immigrants GA (RIGA) (Grefenstette and Fitzpatrick 1992). For MPBIL, an explicit memory is applied, which is randomly initialized and regularly updated. For MPBIL2r, a second population with restart method is added based on MPBIL. The population sizes of the two populations in MPBIL2r are adjustable according to their performance. When the environment changes, the first population searches associated with the memory while the second population searches from scratch. For RIGA, it differs from standard GA only in that in each generation, a set of worst individuals in the population are replaced by random immigrants. In the following experiments, the learning rate and memory size for MPBIL and MPBIL2r were set to 0.25 and 20 , respectively. The crossover probability, mutation probability, and immigrant rate for RIGA were set to 0.6 , 0.1 , and 0.1 , respectively. The population size of each algorithm was set to 100 .

Figure 8 plots the performance ( $F_{\mathrm{CMF}}$ ) of each algorithm over 50 runs on different DDUFs, and the Wilcoxon rank sum test results of comparing EI-MUMDA with MPBIL, MPBIL2r, and RIGA are presented in Table 2, where " + ", " - ", or " $\sim$ " mean that the first algorithm is significantly better than, significantly worse than, or statistically equivalent to the second algorithm, respectively. The sample size and significant level of the Wilcoxon rank sum test are 50 and 0.05 , respectively.

From the experimental results in Fig. 8 and Table 2, it can be seen that EI-MUMDA performs significantly better than RIGA and defeats MPBIL and MPBIL2r in most situations. The main reason lies in that EI-MUMDA updates its memory when an environmental change takes place. In this way, the probability models stored in the memory are improved as far as possible during two environmental changes. High-quality probability models can characterize the environments better and more likely represent the probability distribution of the optimum. As a result, saving and retrieving these high-quality probability models enable algorithms to track the optimum better.

### 4.3.3 Testing the effect of EI-MMS for binary-coded EDAs

In order to verify that the EI-MMS scheme can work effectively for binary-coded EDAs, we apply EI-MMS to the binary-coded UMDA and Bayesian optimization algorithm (BOA) (Pelikan 2002), respectively. The former is the simplest EDA, where the decision variables are
independent to each other. In contrast, the latter is a complex EDA, where the relationships between the decision variables are modelled by a Bayesian network. The corresponding algorithms are denoted by EI-MUMDA and EI-MBOA respectively. Here, EI-MUMDA is compared with restart UMDA (RUMDA) and EI-MOBA is compared with restart BOA (RBOA) on DDUF2. In all of the above four algorithms, the LC + BC scheme is also used to compensate the diversity loss in the population. The relevant parameters were set as follows: the population size $N_{\text {pop }}=100, \tau=1,000, \rho=0.2$, and $p_{\mathrm{n}}=0.01$.

Figure 9 shows the best fitness obtained by each algorithm in the first 50 environments. It can be seen that EIMUMDA and EI-MBOA outperform RUMDA and RBOA respectively in all situations. This means that EI-MMS works effectively for both simple and complex binarycoded EDAs.

In addition, from Fig. 9 it can be seen that the variation of the performance of EI-MMS enhanced algorithms (EIMUMDA and EI-MBOA) in each environment is affected by the environment type. The performance variation is small when the environment changes cyclically. When noise is added into the cyclic environment, the performance variation goes larger. The performance changes violently, e.g., the performance of restart algorithms (RUMDA and RBOA), in the random environment. The reason is that in a cyclic environment EI-MMS can perform very well to guide the EDA and reduce the blindness when a new environment comes. This is good for reducing the performance variation. When noise is added into the cyclic environment or the environment changes randomly, it becomes more difficult to correctly retrieve and update the memory. The inaccurate memory management increases the variation of the performance of EI-MUMDA and EIMBOA.

### 4.3.4 Sensitivity analysis on the effect of parameters

In order to further understand EI-MEDA, in this group of experiments, we perform the sensitivity analysis of the effect of key parameters, including the environmental dynamics parameters, population size, and memory size, on the performance of EI-MEDA in dynamic environments. EI-MUMDA and RUMDA were used as example EDAs and, in order to draw some fair and general conclusions, the DDUF1 function was used as the test function in this group of experiments.
4.3.4.1 Effect of the environmental change speed First, we investigate how the environmental parameter $\tau$ affects the performance of EI-MEDA in the environments with different values of $\rho$. Table 3 presents the comparison between EI-MUMDA and RUMDA. Each element in the

![img-4.jpeg](img-4.jpeg)

Fig. 8 The $F_{\mathrm{CMF}}$ values of EI-MUMDA, RIGA, MPBIL and MPBIL2r over 50 runs on DDUF1 (left column), DDUF2 (middle column), and DDUF3 (right column) in three types of environments:
cyclic environment (top row), cyclic environment with noise (middle row), and random environment (bottom row)
table is the average performance difference between EIMUMDA and RUMDA, i.e., $F_{\mathrm{CMF}}(E I-M U M D A)-$ $F_{\mathrm{CMF}}(R U M D A)$, over 50 runs. Figure 10 shows the $F_{\mathrm{CMF}}$ value of EI-MUMDA under the environments with different $\tau$ and $\rho$. In the experiments, the population size $N_{\text {pop }}$ was set to 100 and the noise rate $p_{\mathrm{n}}$ was set to 0.01 .

From Fig. 10, it can be seen that the slower the environment changes (i.e., the larger the value of $\tau$ ), the better EI-MUMDA can track the optimum dynamically. This is because a slowly changing environment involves a long static period between every two changes. Hence, EIMUMDA can perform a better search during the static period and a memory element can be correctly selected according to the new environment.

As shown in Table 3, in the environments with cyclic characteristic (i.e., cyclic and cyclic with noise), the advantage of EI-MUMDA is more significant while the value of $\tau$ decreases. This means that EI-MMS enhances
the algorithm to track the optimum more effectively in comparison with the restart scheme, especially in fast changing environments. For random environments, EIMUMDA still outperforms RUMDA in general but is defeated when $\rho$ is 0.5 . The reason lies in that the environment with $\rho=0.5$ is the most difficult to identify. If the algorithm can not correctly select a suitable memory element to retrieve, the new population sampled from it may miss the possible optimum.

In other words, the inaccurate environment identification may misguide the search in the new environment. This can also be demonstrated by Fig. 10c where EI-MUMDA performs the worst when the environmental dynamics parameter $\rho$ is 0.5 . When $\rho$ is less or more than 0.5 , the difficulty for environment identification is less. Extremely, when the environment changes completely every time, i.e., $\rho=1.0$, the algorithm works well in a cyclic environment of two complementary states.

Table 2 The Wilcoxon rank sum test results of comparing EI-MUMDA with MPBIL, MPBIL2r, and RIGA on DDUFs in different environments, where " + " means significantly better, " - " means significantly worse, and " $\sim$ " means statistically equivalent

![img-5.jpeg](img-5.jpeg)

Fig. 9 The average best fitness of EI-MUMDA, EI-MBOA, RUMDA and RBOA in the first 50 environments over 50 runs on DDUF2 in cyclic environment (left column), cyclic environment with noise (middle column), and random environment (right column)
4.3.4.2 Effect of the noise rate $p_{\mathrm{n}}$ Second, we analyze how the noise rate $p_{\mathrm{n}}$ affects the performance of EIMUMDA in dynamic environments. The parameters $N_{\text {pop }}$ and $\tau$ were set to 100 and 1,000 respectively in the following experiments. Figure 11 shows $F_{\mathrm{CMF}}\left(E I-M U M D A\right)$ in the dynamic environments with different $p_{\mathrm{n}}$ and $\rho$. Table 4 gives the comparison results between EI-MUMDA and RUMDA.

From Fig. 11, it can be observed that the performance of EI-MUMDA becomes better while the noise rate goes down. This reveals that noise is harmful for the algorithm. This is because noise makes the environment unable to return its previous base state exactly and hence no memory element can match a new environment exactly. In the XOR DOP generator (Yang 2005a; Yang and Yao 2008), for a cyclic with noise environment, before the problem moves

Table 3 The average difference of the $F_{\mathrm{CMF}}$ values between EIMUMDA and RUMDA over 50 runs in three types of environments with different $\tau$ and $\rho$

to a next environment, noise is added to an initial XORing mask that represents the base state of the new environment. This weakens the cyclic characteristic of the dynamic environment and hence is not good for the EI-MMS. Therefore, the larger the noise rate, the less likely that a memory element matches a new environment.

Observing the plots in Fig. 11 regarding $\rho=0.1,0.5$, and 1.0, EI-MUMDA performs better when the environmental change severity increases. The main reason is that the environmental change severity can offset the harmful effect caused by noise. Suppose the $k$ th memory element is relevant to the new environment and its evaluation value should be the highest one. When $\rho$ is large enough or $p_{\mathrm{H}}$ is relatively small, the fluctuation of the evaluation of the elements caused by the noise is slight in relative to the severity of environmental changes. Such slight fluctuation cannot affect the environment identification result much. This is demonstrated in Fig. 12a, where the current evaluation values (dashed line) of the elements are around the values according to the initial XORing mask (solid line). When $\rho_{1}$ is large enough in relative to $p_{\mathrm{H}}$, the evaluation value of the proper element is still significantly higher than others and a correct environment identification can still be made.

However, when the environmental change severity is not large enough, the harmful influence caused by noise may not be effectively offset. In this condition, a larger environmental change severity makes the algorithm perform even worse. This is shown in Fig. 11 where the performance decreases when $\rho$ changes from 0.1 to 0.2 . This can be explained by Fig. 12b, when $\rho_{2}$ is not large enough, the
![img-6.jpeg](img-6.jpeg)
(b) Cyclic environment with noise
![img-7.jpeg](img-7.jpeg)
(c) Random environment

Fig. 10 The $F_{\text {CMF }}$ value of EI-MUMDA over 50 runs in three types of environments with different $\tau$ and $\rho$
proper element is confused with other elements due to the evaluation fluctuation. If the memory element can not be selected correctly, a larger environmental change severity means a larger gap between the optimum and the sampled population.

Besides, it can be seen from Table 4 that the advantage of EI-MUMDA over RUMDA decreases while the environmental noise rate rises. This reveals the fact that

![img-8.jpeg](img-8.jpeg)

Fig. 11 The $F_{\mathrm{CMF}}$ value of EI-MUMDA over 50 runs in cyclic environments with noise with different $p_{\mathrm{n}}$ and $\rho$

Table 4 The average difference of $F_{\mathrm{CMF}}$ values between EI-MUMDA and RUMDA over 50 runs in cyclic environments with noise with different $p_{\mathrm{n}}$ and $\rho$
![img-9.jpeg](img-9.jpeg)

Fig. 12 Illustration of how $\rho$ and $p_{\mathrm{n}}$ affect the environment identification: a $\rho_{1}$ is relatively large enough to offset the noise, $\mathbf{b}$ $\rho_{2}$ is not relatively large enough to offset the noise

EI-MUMDA is more sensitive to the environmental noise than RUMDA. Nevertheless, EI-MUMDA still outperforms RUMDA in all situations. That is, the EI-MMS still effectively enhances EI-MUMDA to react to environmental changes.
![img-10.jpeg](img-10.jpeg)
(a) Cyclic environment
![img-11.jpeg](img-11.jpeg)
(b) Cyclic environment with noise
![img-12.jpeg](img-12.jpeg)
(c) Random environment

Fig. 13 The $F_{\mathrm{CMF}}$ value of EI-MUMDA over 50 runs in three types of environments with different $N_{\text {pop }}$ and $\rho$
4.3.4.3 Effect of the population size This set of experiments was performed to analyze the sensitivity of the effect of the population size to the performance of EI-MUMDA. The environmental dynamics parameters were set as follows: $\tau=1,000$ and $p_{\mathrm{n}}=0.01$.

Figure 13 shows that in most situations EI-MUMDA performs worse when its population size increases. This is because a larger population size means more fitness evaluations in each generation. Therefore, within the same number of fitness evaluations, a smaller population will evolve more generations and the probability model will be

Table 5 The average difference of $F_{\mathrm{CMP}}$ values between EI-MUMDA and RUMDA over 50 runs in three types of environments with different $N_{\text {pop }}$ and $\rho$

refined more times. This enables the EI-MMS to draw a better memory element from the corresponding environment and react to environmental changes better.

Table 5 shows the comparison between EI-MUMDA and RUMDA. It can be seen that, in most situations, the advantage of EI-MUMDA over RUMDA becomes more significant while the population size rises. This means that the heuristic effect of EI-MMS is important for the algorithm to react to the changing environment. When the computational burden for evolving the population is heavy, the EI-MMS is more effective than the restart method to help the algorithm track the changing optimum.
4.3.4.4 Effect of the memory size Finally, we investigate how the memory size affects the performance of EIMEDA. The following experiments were carried out to test the performance of EI-MUMDA with different memory sizes $m \in\{5,10,20,40\}$. Some other parameters were set as follows: $\tau=1,000, \rho=0.1, p_{\mathrm{n}}=0.01$, and $N_{\text {pop }}=100$.

Figure 14 shows the performance of EI-MUMDA with different memory sizes in different environments on the three DDUFs. It can be seen that in cyclic environments, when the memory size $m \leq 20$, the performance of EIMUMDA improves as the value of $m$ increases. However, when $m>20$ (i.e., $m=40$ ), the performance of EIMUMDA does not change significantly. This is because in this experiment, there are 20 (i.e., $2 / \rho$ ) intermediate binary templates in the bitwise XOR DOP generator, which means the environment re-cycles after it changes 20 times.
(a)
![img-13.jpeg](img-13.jpeg)
(b)
![img-14.jpeg](img-14.jpeg)
(c)
![img-15.jpeg](img-15.jpeg)

Fig. 14 The $F_{\mathrm{CMP}}$ value of EI-MUMDA with different memory sizes over 50 runs in different environments on a DDUF1, b DDUF2, and c DDUF3

Therefore, the algorithm needs at most 20 memory elements to store the probability models obtained in each environment. The redundant memory elements when $m=$ 40 cannot significantly enhance the performance any more.

For the cyclic with noise environment, if $p_{\mathrm{n}}$ is large or the environmental change severity is small, the memory elements may be close to each other. As a result, the environment identification method cannot work properly. For example, from Fig. 14, it can be seen that when the environment is cyclic with noise, the memory size seems not a sensitive parameter to affect the performance of EIMUMDA. In a similar way, a randomly changing environment may also weaken the positive effect of memory. Therefore, it can be seen from Fig. 14 that when the

environment changes randomly, the memory size does not affect the performance of EI-MUMDA significantly.

In summary, several conclusions can be drawn from the above experiments on the sensitivity analysis of parameters: (1) a slowly changing environment is good for EI-MEDA to track the moving optimum; (2) noise is a negative factor for EI-MEDA and the severity of the environmental changes can offset this factor to some degree. If noise can be effectively offset, a severely changing environment is good for the environment identification; otherwise, a large environmental change severity may make the situation worse. (3) A large population needs more computational effort to evolve and this degrades the performance of EI-MEDA. Nevertheless, the EI-MMS helps an EDA track dynamic optimum more effectively than the restart method. (4) If the environment is easy to identify and the memory size is smaller than $2 / \rho$, a large memory size is positive to enhance the performance of EI-MEDA; otherwise, the memory size may not affect the performance of EI-MEDA significantly.

## 5 Conclusions

In this paper, an environment identification based memory management scheme (EI-MMS) is proposed to enhance the performance of binary-coded estimation of distribution algorithms (EDAs) for dynamic optimization problems (DOPs). In EDAs with the EI-MMS (i.e., EI-MEDA), probability models are taken as memory elements due to their ability to characterize each environment. When the environment changes, the probability model generated in the previous generation is stored. Then, a suitable element in the memory is used to generate the initial population that may be near the possible optimum in the new environment. In order to retrieve a suitable memory element which matches a new environment, an environment identification method which combines the sample averaging and best individual schemes is proposed in the EIMMS. Since the diversity of conventional EDAs will loss gradually during the learning and sampling processes of the probability models, an effective diversity compensation method which combines the loss correction and boundary correction schemes is also introduced into EIMEDA to further enhance its performance in dynamic environments.

In order to test the validity of the EI-MMS, several groups of experiments have been carried out based on three dynamic decomposable unitation-based functions (DDUFs) in three types of environments. The experimental results show that the EI-MMS is valid to improve the performance of EDAs for DOPs and that EI-MEDA is suitable for any binary EDAs to track moving optimum, especially in the environments with cyclic characteristics (i.e., cyclic environments and cyclic environments with noise). In the experiments, EI-MEDA is also applied to the univariate marginal distribution algorithm (UMDA) and the results show its advantage over other three peer algorithms, i.e., the memory enhanced population-based incremental learning algorithm (MPBIL) (Yang 2005a), MPBIL with two populations and restart scheme (MPBIL2r) (Yang and Yao 2008), and random immigrants GA (RIGA) (Grefenstette and Fitzpatrick 1992), on most cases. In order to understand the proposed method more deeply, the sensitivity analysis on how the key parameters (such as the environmental change speed and severity, the noise rate in cyclic environments, the population size, and the memory size) affect the performance of EI-MEDA has also been carried out in this paper.

Generally, the experimental results indicate that the proposed EI-MMS is efficient in enhancing the performance of EDAs for DOPs and the corresponding EI-MEDAs are good choices for DOPs.

Acknowledgments The authors would like to thank the anonymous associate editor and reviewers for their thoughtful suggestions and constructive comments. This work was supported by the National Nature Science Foundation of China (NSFC) under Grant 60774064, the Engineering and Physical Sciences Research Council (EPSRC) of UK under Grant EP/E060722/01.
