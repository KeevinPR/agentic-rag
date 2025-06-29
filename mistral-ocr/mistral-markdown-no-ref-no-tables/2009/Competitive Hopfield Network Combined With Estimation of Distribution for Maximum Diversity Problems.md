# Competitive Hopfield Network Combined With Estimation of Distribution for Maximum Diversity Problems 

Jiahai Wang, Member, IEEE, Yalan Zhou, Jian Yin, and Yunong Zhang, Member, IEEE


#### Abstract

This paper presents a discrete competitive Hopfield neural network (HNN) (DCHNN) based on the estimation of distribution algorithm (EDA) for the maximum diversity problem. In order to overcome the local minimum problem of DCHNN, the idea of EDA is combined with DCHNN. Once the network is trapped in local minima, the perturbation based on EDA can generate a new starting point for DCHNN for further search. It is expected that the further search is guided to a promising area by the probability model. Thus, the proposed algorithm can escape from local minima and further search better results. The proposed algorithm is tested on 120 benchmark problems with the size ranging from 100 to 5000. Simulation results show that the proposed algorithm is better than the other improved DCHNN such as multistart DCHNN and DCHNN with random flips and is better than or competitive with metaheuristic algorithms such as tabu-search-based algorithms and greedy randomized adaptive search procedure algorithms.


Index Terms-Combinatorial optimization problem, competitive Hopfield neural network (HNN), estimation of distribution, maximum diversity problem (MDP).

## I. INTRODUCTION

CIVEN A SET of $n$ elements and a diversity measure or pairwise difference $d_{i j}$ between elements $i$ and $j\left(d_{i j}=\right.$ $\left.d_{j i}\right)$, with $d_{i j}>0$ for $j \neq i$ and $d_{i j}=0$ if otherwise, the maximum diversity problem (MDP) consists in selecting a subset of given cardinality $m$ from $n$ elements, such that the sum of the pairwise differences between the elements of the selected subset is maximized. Let $\nu_{i}=1$ if element $i$ belongs to the

Manuscript received June 5, 2008; revised August 27, 2008 and November 4, 2008. First published March 24, 2009; current version published July 17, 2009. This work was supported in part by the National Natural Science Foundation of China under Grants 60805026, 60573097, and 60773198, by the Guangdong Provincial Natural Science Foundation of China under Grant 07300630, by the Specialized Research Fund for the Doctoral Program of Higher Education under Grant 20070558052, by the Scientific Research Foundation for the Returned Overseas Chinese Scholars, State Education Ministry under Grant 2007-1108, and by the Program for New Century Excellent Talents in University under Grant NCET-07-0887.
J. Wang and J. Yin are with the Department of Computer Science, School of Information Science and Technology, Sun Yat-Sen University, Guangzhou 510275, China (e-mail: wjiahai@hotmail.com).
Y. Zhou is with the Information Science School, Guangdong University of Business Studies, Guangzhou 510320, China.
Y. Zhang is with the Department of Automation, School of Information Science and Technology, Sun Yat-Sen University, Guangzhou 510275, China.
Digital Object Identifier 10.1109/TSMCB.2008.2010220
subset and $\nu_{i}=0$ if otherwise. The MDP can be formulated as follows:

$$
f(V)=\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} d_{i j} \nu_{i} \nu_{j}
$$

subject to

$$
\sum_{i=1}^{n} \nu_{i}=m
$$

The problem is also known as maximum dispersion [1], MAX-AVG dispersion [2], edge-weighted clique [3], remote clique [4], maximum edge-weighted subgraph [5], and dense $k$-subgraph [6].

There are several different applications of this model, for example, the allocation of available resources to preserve biological diversity [7], medical treatments, the scheduling of final exams, very large scale integration design, and data mining [8]. Duarte and Marti [9] proposed an interesting application of the MDP for evolutionary algorithms. The MDP would be solved to help the scatter search (SS) algorithm obtain a good solution set with a balance between quality and diversity. Furthermore, it is also a particularly complex and important issue in multiobjective evolutionary optimization to keep the diversity of the population. More details on the applications can be found in [4], [7]-[9].

The MDP is strong NP-hard [10]. The proposed exact algorithms [3], [11], [12] are able to solve only instances of size less than 50 variables in reasonable computation time. Several approximation algorithms with guaranteed performance ratios [2], [6], [13] were proposed for the MDP. However, numerical results for such algorithms are usually not provided. Thus, they are not compared to other algorithms to show how well they perform in practice.

Metaheuristics have shown to be very successful in solving many combinatorial optimization problems. Kincaid [14] firstly proposed a simulated annealing (SA) and a tabu search (TS) for the MDP. Simulation results on three sets of problem instances of size 25 show that the TS performs somewhat better than the SA. Following the general guidelines provided in [15], Macambira [5] proposed another TS algorithm, named multiple TS (MTS), for MDP instances with up to 100 vertices and found that the most difficult problem instances were obtained by taking $m=n / 2$ from a computational standpoint. Alidaee et al. [16] proposed a different implementation of TS

using strategic oscillation for the MDP. However, simulation only for very small instances $(n<50)$ is given in [16].
A lot of greedy randomized adaptive search procedure (GRASP) methods were proposed for the MDP. In general, GRASP has two phases: solution construction phase and solution improvement or local search (LS) phase. The first GRASP was proposed by Ghosh [17] for MDP instances up to 40 elements. Andrade et al. [18] developed a new GRASP which can solve instances up to 250 elements and find better solutions on Ghosh's benchmark problems. Silva et al. [19] developed a series of GRASP algorithms by combining different constructions and LSs. These GRASPs were tested on a set of instances randomly generated up to 500 elements and obtained better solutions than previous GRASPs. In [20], Silva et al. further combined one of the GRASP algorithms with pathrelinking (PR) technique. This hybrid, named KLD + PR, produced good solutions for instances of size up to 500. However, the KLD + PR requires a long computation time (e.g., about 10 h for $n=500$; see [20]). Another GRASP with PR was also proposed by Andrade et al. [21].
GRASPs often mainly focus on the randomized generation of high quality starting solutions by very refined construction phases and sophisticated management of the solutions, while the subsequent solution improvement phase is usually performed by a rather simple LS. To explore an opposite method with respect to the GRASPs, i.e., to refine the LS phase while keeping a very simple initialization procedure, Aringhieri et al. [22] proposed a TS-based GRASP algorithm, named GRASP-TS in this paper. In the GRASP-TS, TS is initialized by a trivial constructive procedure, but it adds the tabu mechanism and suitable intensification and diversification devices to enhance the search in the improvement phase. Their simulation results show that the GRASP-TS achieves both better results and much shorter computational time with respect to those reported for the previous GRASPs [22]. They also extended their work by introducing further metaheuristics, such as variable neighborhood search (VNS) and SS [23], to enrich the improvement phase and yield a better exploration of the solution space. Simulation results show that the TS-based algorithm appears to be the best compromise between solution quality and performance.
Furthermore, Duarte and Martí [9] proposed a TS-based algorithm in which memory structures from the TS methodology are incorporated into both construction and improvement phase. Specifically, Duarte and Martí [9] proposed two new types of constructive algorithms (the first one is based on a GRASP construction, and the second one is based on memory structures) and combined them with three iterative improvement procedures: simple LS by Ghosh [17], improved LS, and shortterm memory TS. They tested their algorithms on problem instances with up to 2000 vertices and compared the performance of 18 construction or improvement algorithms for the MDP. In particular, good performance was achieved by combining a constructive method based on the TS methodology with the shortterm memory TS procedure. This hybrid algorithm, named Tabu_D2+LS_TS, outperforms previous methods in [9].
More recently, Palubeckis [24] proposed an iterated TS (ITS) for the MDP. The ITS also has two phases: solution perturbation
and TS phases. Computational results for problem instances involving up to 5000 vertices show that the ITS provides a significantly better performance than previous algorithms. In particular, the ITS finds new best solutions for 69 test problems appearing in the literatures.

One possible and very promising approach to combinatorial optimization problems is to apply Hopfield neural networks (HNNs) [25]. In general, the HNN has two versions: continuous [26] and discrete [27] HNNs. For the continuous HNN, neurons have continuous values within $(0,1)$, and for the discrete HNN (DHNN), the neurons have only binary values-0 or 1 . Takefuji, Funabiki, and their coworkers [28]-[32] found discrete neurons computationally more efficient than continuous neurons and therefore applied the DHNN to solve a variety of combinatorial optimization problems. The DHNN has an advantage over the continuous HNN in terms of the iteration of updating required to converge to a local minimum and the speed of executing each iteration.

Previous studies using neural network for the MDP are surprisingly scarce. Therefore, we propose a discrete competitive HNN (DCHNN) for the MDP in this paper. Adopting $k$-out-of- $N$ rule, the DCHNN always provides a valid solution, and search space is greatly reduced without a burden on the parameter tuning. As the past research has expressed [28]-[32], however, the discrete form of the solution search can easily bring on the problem of the local minimum convergence. The neural network in the local minimum cannot move to other states, although the current state is not a good solution state. In order to deal with the local minima of the DHNN, some modified DHNN is proposed such as multistart DHNN [33], [34] and DHNN with random flips [35].

In the last decade, more and more researchers tried to overcome the drawbacks of usual recombination operators of evolutionary computation algorithms. Therefore, the estimation of distribution algorithms (EDAs) [36]-[45] have been developed. These algorithms, which have a theoretical foundation in probability theory, are also based on populations that evolve as the search progresses. The EDAs attempt to model the distribution of promising solutions and then produce the next generation by sampling the estimated distribution modeling. After every iteration, the distribution is reestimated.

In order to overcome the local minimum problem of DCHNN, the idea of EDA is combined with DCHNN, and a DCHNN-EDA is proposed for the MDP in this paper. Once the network is trapped in local minima, the perturbation based on EDA can generate a new starting point for the HNN for further search. It is expected that the further search is guided to a promising area by the probability model. Thus, the proposed DCHNN-EDA can escape from local minima and further search better results. The performance of the DCHNN-EDA is tested and evaluated by simulating a large number of benchmark instances. First, the proposed DCHNN-EDA is compared with other improved DHNNs. Simulation results show the superior performance of the DCHNN-EDA. We also mention the transiently chaotic neural network (TCNN) [46] and noisy chaotic neural network (NCNN) [47] proposed recently to deal with the local minima of the continuous HNN and discuss the similarities and differences between the chaotic neural models

and the DCHNN-EDA. Second, the proposed DCHNN-EDA is compared with metaheuristic algorithms. Simulation results show that the proposed DCHNN-EDA is better than or competitive with other metaheuristic algorithms such as ITS, MTS, GRASP-TS, Tabu_D2+LS_TS, and KLD+PR.

The contributions of this paper are as follows: 1) A novel competitive HNN method combined with EDA is proposed for the MDP and very good results are obtained, which is the contribution to the available literature on the MDP; 2) the probabilistic modeling/EDA idea is applied to HNN training and thus helps the network escape from local minima, which is the contribution to the HNN literature; and 3) a comprehensive experimental comparison of the proposed algorithm with other methods is also provided.

The remaining sections of this paper are organized as follows. In Section II, we propose a DCHNN for the MDP. In Section III, we propose a DCHNN combined with EDA for the MDP. In Section IV, benchmark data sets are used to evaluate the proposed DCHNN-EDA. The last section concludes this paper.

## II. DCHNN FOR MDP

The MDP with an $n \times n$ symmetric matrix $\mathbf{D}=\left(d_{i j}\right)$ can be mapped onto the HNN with $n$ neurons. The $i$ th neuron has input $u_{i}$ and output $\nu_{i}$. The output $\nu_{i}=1$ if element $i$ belongs to the subset, and $\nu_{i}=0$ if otherwise. The energy function of the MDP can be written as

$$
E=A\left(\sum_{i=1}^{n} \nu_{i}-m\right)^{2}-\frac{B}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} d_{i j} \nu_{i} \nu_{j}
$$

where $A$ and $B$ are the weighting factors.
The quality of the final solution is very sensitive to the values of these weighting factors ( $A$ and $B$ ). Therefore, a DCHNN is proposed to relieve this burden, in which the penalty term [the first term on the right-hand side of (3)] is handled in an explicit manner. In the DCHNN, a $k$-out-of- $N$ competitive rule is imposed for the neuron updating. The $k$-out-of- $N$ rule leads to a stable state with exactly $k$ active neurons among $N$. Therefore, the neurons within the same row compete with one another to be fired. In other words, the input-output function for the neurons within the $i$ th row is given by

$$
\nu_{i}(t+1)=\left\{\begin{array}{ll}
1, & \text { if } u_{i}(t) \geq u_{m \mathrm{th}}(t) \\
0, & \text { otherwise }
\end{array}\right.
$$

where $u_{m \mathrm{th}}(t)$ is the $m$ th largest value within $\left\{u_{1}(t), \ldots\right.$, $\left.u_{n}(t)\right\}$. The inputs $u_{i}$ of all $n$ neurons are sorted in a nonascending order. Then, from the beginning, $m$ neurons among $n$ neurons are selected as winner neurons. The outputs of those selected winner neurons are set to 1 , and the outputs of other neurons are set to 0 . If more than $m$ neurons satisfy $u_{i}(t) \geq$ $u_{m \mathrm{th}}(t)$, neurons which have previously output 0 are selected with priority to be fired. This mechanism contributes to the blocking of continuous firings, encourages other neurons to be eventually fired, and ultimately assists the system to escape from a fixed point. Thus, search space is expanded by the state changes. The monotonicity property of the competitive neuron
model (4) is equivalent to a MacCulloch-Pitts neuron model with a dynamic threshold equal to $u_{m \mathrm{th}}(t)$.

By adopting this competitive model, the constraint of this problem described by (2) can always be satisfied. Therefore, the energy function consists of only one term that represents the sum of the pairwise differences between the elements of the selected subset since the constraint term is always satisfied

$$
E=-\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} d_{i j} \nu_{i} \nu_{j}
$$

According to the update rule of the DHNN [4], the inputs of the neurons for the MDP are computed by

$$
\frac{d u_{i}}{d t}=-\frac{\partial E}{\partial \nu_{i}}=\sum_{j=1}^{n} d_{i j} \nu_{j}
$$

However, in practice, they are approximated by the first-order Euler method in the form

$$
\Delta u_{i}=\sum_{j=1}^{n} d_{i j} \nu_{j}
$$

Thus, the input $u_{i}$ for each neuron of the DHNN is updated iteratively using the following equation based on the first-order Euler method [7]:

$$
u_{i}(t+1)=u_{i}(t)+\Delta u_{i}
$$

One updating iteration means that all the $n$ neurons have been updated once. The system with this kind of group updating way has a high convergence speed.

The DCHNN can thus be summarized as follows.

## DCHNN for MDP

initialize $\mathbf{u}$ (randomly around zero);
calculate $\mathbf{v}$ using (4);
$t=0 ;$
repeat
for $i=1$ to $n$ do /'HNN descent procedure'/ compute $u_{i}(t+1)$ with motion equation (8);
end for
for $i=1$ to $n$ do
update $\nu_{i}(t+1)$ using (4);
end for
$t=t+1$
until ( $t>$ iterations or stability criteria are satisfied)
The discrete model has an advantage over the continuous model in terms of the number of updating required to converge to a local minimum and the speed of executing each iteration. However, the discrete form of the solution search can easily bring on the problem of the local minimum convergence. The neural network in the local minimum cannot move to other states. In the next section, we will propose a DCHNN combined with EDA for the MDP in order to overcome the local minimum problem of the DCHNN.

## III. DCHNN COMBINED WITH EDA FOR MDP

This DCHNN can make significant advances in the earlier stages of optimization procedures (i.e., the energy function decreases rapidly and dramatically in the earlier stages), and improvements slow thereafter, until after several iterations, for example, ten iterations, a local minimum is encountered; thus, the energy function no longer decreases [34]. The local minimum problem is caused by the gradient descent dynamics of the update rule of the DHNN.

When the network is trapped in a local minimum, a perturbation operator is applied to the local minimum to generate a new starting point for the HNN. It is desirable that the generated starting point should be in a promising area in the search space. Therefore, in this section, we propose an EDA mutation operator as the perturbation operator in the HNN. The EDA mutation operator can generate a new starting point for the further HNN search. It is expected that the further search is guided to a promising area by the probability model. In the proposed algorithm, the solution mutation or perturbation is always applied to the current local minima.

In the following section, we first briefly review the EDA, and then, the DCHNN combined with the EDA is proposed.

## A. EDA

EDA is a new area of evolutionary computation. In EDAs, there is neither crossover nor mutation operator. Instead, new population is generated by sampling the probability distribution which is estimated from the selected promising solutions or individuals of previous generation. Thus, these algorithms have a theoretical foundation in probability theory.

An algorithmic framework of most EDAs can be described as follows.

## Framework of EDA

Pop $=$ InitializePopulation $($ ) /'Initialization* $/$ while Stopping criteria are not satisfied do /'Main Loop* $/$ $P o p_{\text {sel }}=\operatorname{Select}(P o p) \quad /{ }^{\prime} \operatorname{Selection}^{*} /$
Prob $=$ Estimate $\left(P o p_{\text {sel }}\right) \quad /{ }^{\prime} \text { Estimation } * /$
Pop $=\operatorname{Sample}(P r o b) \quad /{ }^{\prime}$ Sampling $^{*} /$
endwhile
An EDA starts with a solution population Pop and a solution distribution model Prob. The main loop consists of three principal stages. The first stage is to select the best individuals (according to some fitness criteria) from the population. These individuals are used in the second stage in which the solution distribution model $P r o b$ is updated or recreated. The third stage consists of sampling the updated solution distribution model to generate new solution offspring. There has been a growing interest for EDAs in the last year. A more comprehensive presentation of the EDA field can be found in [37] and [38].

## B. DCHNN Combined With EDA

The EDA is a novel optimization tool and is primarily used in evolutionary algorithms which are population-based and multi-
point search methods. However, a single EDA technique is hard for solving complicated optimization problems because the location information of solutions found so far (the actual positions of these solutions in the search space) is not directly used for the generation of offspring in the original EDA [41], [42]. Therefore, how to combine EDAs with other techniques represents an important research direction [43]. Recently, Zhang et al. [41]-[44] proposed several works on EDA hybrids for hard optimization problems. In particular, a new operator, called guided mutation, was proposed for generating new solutions. The guided mutation can be regarded as a combination of conventional mutation and EDA offspring generating scheme, and it was used both in population-based methods [41], [42] and single-point-based method [44]. Considering the local minima problem of the HNN and these successes recently reported in effectively combining EDA and other techniques [41]-[45], the EDA is introduced into the DCHNN, which is a singlepoint search method, to help the DCHNN escape from the local minima in this paper. The DCHNN combined with the EDA (DCHNN-EDA) can thus be summarized as follows.

## DCHNN-EDA for MDP

initialize $\mathbf{u}$ (randomly around zero);
calculate $\mathbf{v}$ using (4);
initialize best-so-far solution $\mathbf{g b}$ and probability model $\boldsymbol{P}$;
for $k=1$ to descents do
$t=0 ;$
repeat
for $i=1$ to $n$ do /'HNN descent procedure*/ compute $u_{i}(t+1)$ with motion equation (8);
end for
for $i=1$ to $n$ do
update $\nu_{i}(t+1)$ using (4);
end for
$t=t+1$
until ( $t>$ iterations or stability criteria are satisfied); update and keep track for the best-so-far solution gb; update probability model using $\mathbf{v}$;
reset $\boldsymbol{P}$ to $1-\boldsymbol{P}$ after a specified number of descents; perturb the current solution $\mathbf{v}$ using EDA mutation to generate a new starting point $\mathbf{v}$ for the HNN;
reset $\mathbf{u}$ using (10);
end for
During the descents of HNN, the HNN will visit a number of locally optimal solutions. Statistical information of these optimal solutions can be extracted for building a probability model.

Several different probability models have been introduced into EDAs for modeling the distribution of promising solutions. The univariate marginal distribution (UMD) model is the simplest one and has been used in UMD algorithm [36], population-based incremental learning (PBIL) [39], and compact genetic algorithm [40]. Therefore, in this paper, the UMD model is adopted to estimate the distribution of good regions over the search space based on the locally optimal solutions. The proposed algorithm uses a probability vector $\boldsymbol{P}=\left(p_{1}, \ldots\right.$, $\left.p_{i}, \ldots, p_{n}\right)$ to characterize the distribution of promising

solutions in the search space, where $p_{i}$ is the probability that the value of the $i$ th position of a promising solution is 1 .

Then, an EDA mutation mutates current solution based on the probability vector $\boldsymbol{P}$, which characterizes distribution of promising solutions. It can be expected that offspring falls in or close to a promising area in the search space. The EDA mutation perturbs the current solution or local minimum $\mathbf{v}$ and guides the HNN to search in binary $0-1$ solution space in the following way.

## Perturb the current solution using EDA mutation

for $i=1$ to $n$ do
If rand() $<\beta \quad /{ }^{\wedge}$ Sample from probability vector ${ }^{\star} /$ if rand( $)<p_{i}$, set $\nu_{i}(t+1)=1$, otherwise set $\nu_{i}(t+1)=0$
Otherwise, $\nu_{i}(t+1)=\nu_{i}(t) \quad /{ }^{\wedge}$ Copy from current solution $\mathbf{v}^{*} /$
end for
where rand( ) produces a random number distributed uniformly on $[0,1]$. In the EDA mutation, a bit is sampled from the probability vector $\boldsymbol{P}$ randomly or directly copied from the current solution $\mathbf{v}$, which is controlled or balanced by the parameter $\beta$. The larger the $\beta$, the more elements of the new starting point are sampled from the vector $\boldsymbol{P}$. Since some elements of offspring are sampled from the probability vector $\boldsymbol{P}$, it can be expected that they fall in or close to the promising area. The random sampling mechanism can also provide diversity for the search afterward.

The parameter $\beta$ controls the strength of the perturbation or mutation. The mutation (kick move) implemented by the EDA mutation should be chosen adequately strong to allow one to leave the current local minimum and to enable the HNN to find new and possibly better solutions. If the kick move is too weak, the HNN may return after very few steps to the local minimum to which the kick move has been applied. On the other hand, the kick move should be adequately weak to keep the characteristics of the current local minimum, since part of the solution may already be close to optimal. A major problem for too strong kick move is that the resulting algorithm would be very similar to repeating the HNN search from the randomly generated solutions. Applying only rather small mutations has an additional advantage that the HNN requires only a few steps to reach the next local optimum, i.e., new local optima can be identified very fast-typically much faster than when starting from a randomly generated solution. Hence, for the same given computation time, more HNN searches can be performed than when starting from the randomly generated solutions.

In the proposed algorithm, the probability vector $\boldsymbol{P}$ is initialized as $\boldsymbol{P}=(0.5, \ldots, 0.5, \ldots, 0.5)$. The probability vector can be learned and updated at each descent of the HNN for modeling the distribution of promising solutions in the same way as in the PBIL algorithm [39]

$$
p_{i}(t+1)=(1-\lambda) p_{i}(t)+\lambda \nu_{i}(t)
$$

where $\lambda \in(0,1]$ is the learning rate.

The main loop of the framework of EDA consists of three principal stages: selection, estimation, and sampling. In the DCHNN-EDA, current locally optimal solution $\mathbf{v}$ generated by the HNN descent procedure is selected; then, $\mathbf{v}$ is used in the estimation stage in which the probability model $\boldsymbol{P}$ is updated according to the rule defined by (9). The sampling process is described in the EDA mutation operator. However, there are several differences between the DCHNN-EDA and the most usual population-based EDA algorithms. First, in the sampling process of the DCHNN-EDA, the probability model is not sampled directly as in the pure or original EDA but rather used as part of the EDA mutation. Second, although the DCHNN-EDA uses a univariate probability model in the style of PBIL, only one solution is sampled from the probability model, and only one solution is used to update the model. Thus, the DCHNN-EDA is more akin to other EDA hybrids [41]-[45], particularly similar to the guided mutation used in iterated LS (ILS) for quadratic assignment problems (QAPs) [44]. The novelty of the DCHNN-EDA consists in applying the probabilistic modeling/EDA idea to train HNN and thus help the network escape from the local minima. In the future, we can also apply the DCHNN-EDA to the QAP and make a full comparison of the DCHNN-EDA with the ILS with guided mutation.

Guided by a probability model which characterizes the distribution of promising solutions in the search space, the EDA mutation mutates the current solution $\mathbf{v}$ to generate a new starting point. The EDA mutation operators provide a mechanism for combining global statistical information about the search space and the information of the current solution found during the previous search and thus generate new starting points for further search.

Before invoking the next HNN search, all the inputs of neurons $u_{i}$ are renormalized or reset to 0 or 1 based on the current $u_{i}$ values as follows [35]:

$$
u_{i}= \begin{cases}1, & \text { if } u_{i}>0 \\ 0, & \text { otherwise }\end{cases}
$$

This prevents the inputs $u_{i}$ of neurons from decreasing or increasing to too small or too large values according to (8) during successive evolution and therefore helps the states of neurons to be changed according to (4) in the next HNN search. Furthermore, after a specified number of descents, for example, five, without improvement of the best solution, it is possible to sample new solutions which are far from the current searching area by means of $1-\boldsymbol{P}$.

The proposed algorithm repeatedly invokes two procedures-HNN search and EDA mutation-to construct a good starting solution for further HNN search. Parameter descents can be seen as an upper bound on the number of HNN invocations and then can be seen as a stopping criterion. One updating iteration is defined as one complete update of all $n$ neurons according to (8) and (4). The total iteration number of the proposed algorithm is descents $\times$ iterations.

For the MDP with a symmetric rational $n \times n$ matrix $\mathbf{D}=$ $\left(d_{i j}\right)$, the HNN uses $n$ neurons. According to the motion function (6), the calculation in each neuron takes time $O(n)$.

TABLE I
COMPARISON OF THE RESULTS ObTAINED BY THE MULTISTART DCHNN, DCHNN WITH RANDOM FLIPPING PERTURBATION, AND DCHNN-EDA FOR SILVA INSTANCES

Therefore, sequential traversal of all $n$ neurons takes time $O\left(n^{2}\right)$ in the proposed algorithm. Updating the probability model takes time $O(n)$. Therefore, the whole complexity of the proposed algorithm is $O\left(n^{2}\right)$.

## IV. SimULATION RESULTS AND DiscuSSIONS

In order to assess the performance of the proposed algorithm, simulations were implemented in C on a PC (Pentium4 $2.80 \mathrm{GHz})$. In this section, we describe the benchmark data sets and the parameter setting, and present the results of the DCHNN-EDA on the benchmark data sets. We also compare the results with those HNN algorithms with different modifications to demonstrate the effect of the EDA perturbation and compare the results with other metaheuristics such as the ITS, MTS, GRASP-TS, Tabu_D2 + LS_TS, and KLD + PR.

## A. Benchmark Data Sets

We tested the proposed algorithm on five data sets with a total of 120 instances. The size of the instances ranges from (small scale) 100 to (large scale) 5000 . The name of instances and the best known solutions of 120 problems are shown in Tables I-XII. The details of the instance sets are described as follows [9], [24].

1) Silva instances: $20 n \times n$ matrices with random integers generated from a $[0,9]$ uniform distribution with $n \in$ $[100,500]$ elements and $m \in[0.1 n, 0.2 n, 0.3 n, 0.4 n]$. These 20 instances are the largest instances first intro-
duced by Silva et al. [19] and can be downloaded from http://www.ic.uff.br/ $\sim$ psilva/instSilva.zip.
2) Random type 1 instances: matrices with real numbers generated from a $(0,10)$ uniform distribution. There are 20 instances (Type1_55) with $n=500$ and $m=50$, 20 instances (Type1_52) with $n=500$ and $m=200$, and 20 instances (Type1_22) with $n=2000$ and $m=200$.

Note that instances Type1_55 are equal to instances Type1_52. They only differ in the amount of selected elements $m$. In other words, both instances are matrices of distances of 500 elements. In Type1_55, 50 elements are selected from 500 (i.e., $m=50$ ), and in Type1_52, 200 elements are selected from 500 (i.e., $m=200$ ).
3) Random type 2 instances: matrices with real numbers generated from a $(0,1000)$ uniform distribution. There are 20 instances with $n=500$ and $m=50$.

Random type 1 and 2 instances are first introduced in [9] and can be downloaded from http://www.uv.es/ $\sim$ rmarti/paper/mdp.html.
4) Beasley instances: instances taken from the Operations Research (OR)-Library [48]. These test instances were originally introduced for the unconstrained binary quadratic optimization problem. Recently, these instances were adopted for testing algorithms for the MDP by Palubeckis [24]. In the case of MDP, the diagonal elements of these instances are ignored. All the instances have $10 \%$ density. In each case, the matrix contains both positive and negative numbers from $[-100,100]$. There are ten instances with $n=2500$ and $m=1000$.

TABLE II
Comparison of the Results Obtained by the Multistart DCHNN, DCHNN With Random Flipping Perturbation, and DCHNN-EDA FOR TYPE1_55 Instances ( $n=500 ; m=50$ )

TABLE III
Comparison of the Results Obtained by the Multistart DCHNN, DCHNN With Random Flipping Perturbation, and DCHNN-EDA FOR TYPE1_52 InSTANCES $(n=500 ; m=200)$

TABLE IV
Comparison of the Results Obtained by the Multistart DCHNN, DCHNN With Random Flipping Perturbation, AND DCHNN-EDA FOR TYPE1_22 INSTANCES $(n=2000 ; m=200)$

TABLE V
Comparison of the Results Obtained by the Multistart DCHNN, DCHNN With Random Flipping Perturbation, AND THE DCHNN-EDA FOR TYPE2 INSTANCES $(n=500 ; m=50)$

TABLE VI
COMPARISON OF THE RESULTS ObTAINED BY THE DCHNN-EDA AND OTHER METAHEURISTIC ALGORITHMS FOR SILVA INSTANCES

TABLE VII
COMPARISON OF THE RESULTS ObTAINED BY THE DCHNN-EDA AND OTHER METAHEURISTIC ALGORITHMS FOR TYPE1_55 INSTANCES $(n=500 ; m=50)$

TABLE VIII
COMPARISON OF THE RESULTS Obtained by the DCHNN-EDA and Other MEtaHEUristic Algorithms FOR TYPE1_52 INSTANCES $(n=500 ; m=200)$

TABLE IX
COMPARISON OF THE RESULTS Obtained by the DCHNN-EDA and Other MEtaHEUristic Algorithms FOR TYPE1_22 INSTANCES $(n=2000 ; m=200)$

TABLE X
COMPARISON OF THE RESULTS ObTAINED BY THE DCHNN-EDA AND OTHER METAHEURISTIC ALGORITHMS FOR TYPE2 INSTANCES $(n=500 ; m=50)$

TABLE XI
COMPARISON OF THE RESULTS ObTAINED BY THE DCHNN-EDA AND OTHER METAHEURISTIC ALGORITHMS FOR BEASLEY INSTANCES $(m=1000)$

In [24], Palubeckis introduced an MDP where constrain (2) was extended as follows:

$$
m_{1} \leq \sum_{i=1}^{n} \nu_{i} \leq m_{2}
$$

In the MDP defined by (1) and (11), the coefficients $d_{i j}$ can be positive, negative, or zero. When all the coefficients $d_{i j}$ are nonnegative, then (11) can be replaced by (2), where, obviously, $m_{1}=m_{2}$. In [24], two experi-
ments were conducted. In the first one, $m=m_{1}=m_{2}=$ 1000 was set, whereas in the second, $m_{1}=1620$ and $m_{2}=1655$ were set. In this paper, only the MDP defined by (1) and (2) is considered, and therefore, we follow the first experiment in [24] when the Beasley instances are simulated. That is, the matrix $\mathbf{D}$ that contained both positive and negative elements is directly used in the DCHNN-EDA, as in [24], although we expect $d_{i j}>0$, as stated in the MDP model defined by (1) and (11), which also facilitates the fair and direct comparison of

TABLE XII
COMPARISON OF THE RESULTS Obtained by the DCHNN-EDA and OTHER Metahuristic Algorithms FOR RANDOM LARGER PROBLEMS $(n=3000,5000 ; m=0.5 n)$

the results produced by the DCHNN-EDA with those produced by the ITS from [24].
5) Random larger instances: matrices with integer numbers generated from a $[0,100]$ uniform distribution. The densities of the matrix are $10 \%, 30 \%, 50 \%, 80 \%$, and $100 \%$. There are five instances with $n=3000$ and $m=0.5 n$ and five instances with $n=5000$ and $m=0.5 n$. These larger instances are first introduced in [24]. The sources of the generator and input files to replicate these problem instances can be found at http://www.soften.ktu.It/ gintaras/max_div.html.

## B. Parameter Setting

The DCHNN-EDA has two main parameters, which are parameter $\beta$ and $\lambda$, to be tuned. The parameter $\beta$ controls the strength of the mutation, and the learning rate $\lambda$ balances the contributions between the old statistical information extracted from historical local minima and the information of the current local minimum to the new probability vector. The bigger the $\lambda$, the greater is the contribution of current local minimum.

To assess the effects of these parameters, the DCHNNEDA is tested as a preexperimental tuning on a representative subset of problems with different sizes and densities from Tables I-XII. These selected problems include Silva_500_200, Type1_55.1, Type1_52.1, Type1_22.1, Type2.1, b2500-1, p3000-1, and p5000-5.

First, $\beta$ and $\lambda$ are defined to take values within the following discrete range $\{0.1,0.2, \ldots, 0.9\}$, respectively. In the preliminary tests, we found that the parameter combinations $\beta \in\{0.1,0.2,0.3\}$ and $\lambda \in\{0.1\}$ can obtain good results, and there is no significant difference in the results using these parameter combinations. This suggests that relatively small mutation strength and contribution of the current local minimum are adequate for the MDP. The problem for too strong mutation strength and too big contribution of the current solution or local minimum is that the resulting algorithm is very similar to repeating the HNN search from randomly generated or initialized starting point like the multistart HNN [33].

Second, in order to further investigate the effect or sensitivity of parameter $\lambda$, we fix the parameter $\beta=0.2$ and then vary parameter $\lambda$ within the range $\{0.01,0.02, \ldots, 0.09\}$. We find no significant difference in the results using different values of the parameter $\lambda$ within the range, which suggests that the range of reasonable values of the parameter $\lambda$ is rather large only if $\lambda$ is set to a very small value. In fact, there is a more general reason for $\lambda$ to be that low. Typically, in the PBIL, the probability vector is updated based on a histogram of solution variable values taken over a population of size larger than one, and thus, the potential increments to the probability vector are small (often smaller than one); therefore, $\lambda$ is set on the order of $10^{-1}$, for example, $\lambda$ is set to 0.7 or 0.3 in [41] and [42]. However, in the DCHNN-EDA, since only one solution at a time is used to update to the probability vector according to (9), thus the potential increments to the probability vector are either 1 or 0 , depending on the value of the current local minimum. Thus, the value of $\lambda$ in the DCHNN-EDA should be smaller than that in the PBIL or, else, the new probability model will "forget" the old information extracted from the historical local minima quickly. Therefore, $\lambda$ in the DCHNN-EDA can be recommended to set to the order of $10^{-2}$.

Finally, $\beta$ is randomly drawn from the interval $[0.1,0.3]$, and $\lambda$ is randomly drawn from the interval $[0.01,0.1]$; we also find no significant difference in the results.

Based on the preliminary computational experiments and analysis in theory on the parameters, we select a parameter combination $\beta=0.2$ and $\lambda=0.04$ for all test benchmark problems in the whole simulation. Certainly, the parameters are chosen experimentally, and the tuning of these parameters may be necessary when solving different optimization problems. In the future, we will research self-adaptive control strategy for these parameters.

The DCHNN for the MDP works hardest and most productively, measured by a rapidly decreasing energy, during the first ten iterations. Therefore, each descent in the DCHNN-EDA ends after ten iterations, and each test run invokes 500 times HNN search, i.e., descents $=500$. The total iteration number of the DCHNN-EDA is thus $10^{*} 500=5000$. This is a tradeoff between solution quality and computation time. If given more

computation time, the DCHNN-EDA can implement or invoke more times HNN search and therefore can be expected to produce better results.

## C. Comparison With Other Modified DCHNN Algorithms

In this section, we first describe two modified DHNN algorithms proposed for combinatorial optimization problems [33], [35], and then, we compare the DCHNN-EDA with them to show how the EDA process can improve the performance of the DCHNN. Finally, we also mention the TCNN and NCNN proposed recently to deal with the local minima of the continuous HNN and point out similarities and differences between the chaotic neural models and the DCHNN-EDA.

He et al. [33] proposed a multistart HNN which repeats the random initial solution and HNN search mechanism a number of times and finally returns the best solution. He et al. applied the multistart DHNN to two-page crossing number and outerplanar drawing problems and obtained better results than other neural networks [33], [34]. We also propose a modified DCHNN which repeats the random initial solution and HNN search mechanism a number of times like in [33]. The structure of the multistart DCHNN algorithm is as follows.

## Multistart DCHNN for MDP

initialize the best-so-far solution gb;
for $k=1$ to descents do
initialize $\mathbf{u}$ (randomly around zero);
calculate $\mathbf{v}$ using (4);
$t=0 ;$
repeat
for $i=1$ to $n$ do /*HNN descent procedure'/ compute $u_{i}(t+1)$ with motion equation (8); end for
for $i=1$ to $n$ do
update $\nu_{i}(t+1)$ using (4);
end for
$t=t+1$
until ( $t>$ iterations or stability criteria are satisfied); update and keep track for the best-so-far solution gb; end for

In the multistart DCHNN, HNN descent procedure is restarted with different initial states of the neurons for several times, and finally, the best solution is output. In other words, the best local minimum among the local minima produced by several different descents of the HNN is selected as the best solution.

Smith et al. [35] proposed a modified HNN where random perturbation (random flip mutation) is used to help the network escape from local minima, and therefore, the HNN is called DHNN with random flips. The simulation results on timetabling problems showed that the DHNN with random flips is comparable to or better than the SA, TS, and greedy search methods [35]. We also introduce the random perturbation to the DCHNN. To avoid losing good solution during the evolution of the network, we add an additional step, update, and keep track
for the best-so-far solution gb. DCHNN with random flips can thus be summarized by the following.

## DCHNN with random flips for MDP

initialize $\mathbf{u}$ (randomly around zero);
calculate $\mathbf{v}$ using (4);
initialize best-so-far solution gb;
for $k=1$ to descents do
$t=0$;
repeat
for $i=1$ to $n$ do /*HNN descent procedure'/ compute $u_{i}(t+1)$ with motion equation (8); end for
for $i=1$ to $n$ do update $\nu_{i}(t+1)$ using (4); end for
$t=t+1$
until ( $t>$ iterations or stability criteria are satisfied); update and keep track for the best-so-far solution gb; randomly choose a neuron, and flip according to threshold; reset $\mathbf{u}$ using (10);
end for
In the DCHNN with random flips, the stochasticity at the end of each iteration is created by randomly choosing a neuron and assigning its state value of 0 or 1 . A threshold is used to control the stochasticity, so that if the threshold is 0.5 , then there is an equal chance of a neuron state becoming 0 or 1 . However, if the threshold is increased to, for example, 0.7 , then there is only a $30 \%$ chance that the neuron will be assigned a value of 1 . Thus, the modifications to the network dynamics described earlier contribute to an efficient wandering of the search space in short bursts of gradient descent, using random perturbations to escape local minima. In this paper, the threshold to control the stochasticity is set to 0.85 , as in [35], and can obtain good performance of the method. Note that the stochasticity should be interpreted as a bias toward a neuron taking a value of 0 rather than a probability of a flip taking place.

The two modified HNNs mentioned earlier all invoke several times HNN search, which is similar to the DCHNN-EDA. Therefore, we compare the DCHNN-EDA with them in order to determine how much the EDA process contributes to the search.

Tables I-V show the best, average, and standard deviations produced by the multistart DCHNN, DCHNN with random flips, and the DCHNN-EDA, respectively, for the first three sets of test problem instances (including Silva instances and type 1 and 2 instances) in 30 independent runs. The best known values of these test problem instances are also shown in Tables I-V. From Tables I-V, we find that the DCHNN with random flips gets better, best, and average results than the multistart DCHNN. Furthermore, most of the average results of the DCHNN with random flips are better than the best results of the multistart DCHNN. It is apparent that the DCHNN-EDA performs better than the multistart DCHNN and DCHNN with random flips in all instances in terms of best and average values. Furthermore, most of the average results of the DCHNN-EDA are better than the best results of the multistart DCHNN and DCHNN with random flips.

TABLE XIII
Estimated PERFORMANCES of COMPUTERS

The multistart DCHNN cannot find any best known value. The DCHNN with random flips can find best known value in 9 out of 100 instances. The DCHNN-EDA can obtain a best known value in 77 out of 100 instances. Bold figures indicate the best known value obtained by all the algorithms.

In order to know whether the differences in performance showed in Tables I-V between the proposed DCHNN-EDA and DCHNN with random flips are statistically significant, unpaired $t$-tests (sample size $=30$ and degrees of freedom $=58$ ) were performed. From the two-tailed $p$ value derived from the unpaired $t$-tests (for conciseness, $p$ values are not shown in the tables because they can be easily obtained using TDIST function in Excel), we find that the difference of the average solution values between the two algorithms for all instances is extremely significant ( $p<0.0001$ ) except for instance Type1_52.18 in Table III. For instance Type1_52.18, the difference of the average solution values between the two algorithms is not significant $(p=0.7864)$.

In the multistart DCHNN, random initialization is a random sampling mechanism in the search space. That is, the starting solutions are generated completely randomly. If it is lucky enough to start from a good initial point, the multistart DCHNN can converge to a good solution. The DCHNN with random flips uses random perturbations to escape local minima. However, which neuron state is chosen to be flipped is decided in a completely random way, and therefore, it is somewhat "blind." In the DCHNN-EDA, the DCHNN is guided by global search information extracted from the EDA model and therefore can search better solution in the promising region, which is the main reason that the DCHNN-EDA can obtain better results than the multistart DCHNN and the DCHNN with random flips.

The multistart DCHNN, DCHNN with random flips, and the DCHNN-EDA use the same DHNN descent procedure, and they are different only in the construction of the starting point for each HNN descent. In the multistart DCHNN, the input and output of each neuron are randomly initialized at the beginning of each HNN descent. In the DCHNN-EDA, the probability model is updated, and the new starting point for further search is sampled from the probability model at the end of each descent. In the DCHNN with random flips, a bit is randomly chosen to flip at the end of each descent. Therefore, we can conclude that the three algorithms have about the same performance in running time. The computation time in terms of real CPU time of the DCHNN-EDA for all test instances is summarized in Tables XIII-XV.

In order to deal with the local minima of the continuous HNN, Chen and Aihara [46] proposed a TCNN by adding a decaying negative self-feedback to continuous HNN and
thus introducing chaotic dynamics. Recently, Wang et al. [47] proposed a NCNN by adding decaying stochastic noise into the TCNN. In contrast to the TCNN and NCNN, the DCHNN-EDA does not introduce the stochastic or chaotic dynamics into the original HNN gradient descent dynamics and therefore does not attempt to prevent the system getting stuck at local minima. Rather, once the network converges to a local minimum, it aims to generate a new better starting point by EDA mutation for further HNN search. One advantage of this approach is that it has no effect on the energy minimization or original HNN gradient descent dynamics until the network converges to a stable point. In contrast to the TCNN and NCNN based on continuous HNN, the algorithm is based on DHNN and therefore is more efficient, fast, and simple. Furthermore, the DCHNN always provides a valid solution, and search space is greatly reduced without a burden on the parameter tuning. The DCHNN-EDA has also deterministic dynamics like in the TCNN and is not guaranteed to converge to a global optimum. However, from our simulation, the DCHNN-EDA can obtain good solutions within reasonable computation time.

## D. Comparison With Metaheuristic Algorithms

In order to show the effectiveness of the DCHNN-EDA, we now present a comparative performance against other metaheuristic algorithms, including the ITS, MTS, Tabu_D2 + LS_TS, GRASP-TS, and KLD + PR. These algorithms are among the most accurate algorithms for the MDP. In particular, the ITS finds new best solutions for 69 test problems appearing in the literature and is the best algorithm for the MDP so far. Therefore, the ITS can be used as the benchmark algorithm to evaluate the performance of the DCHNN-EDA.

The main ingredients of the ITS include solution perturbation procedure, get start point, for construction of a starting solution, and a simple TS (STS) for iterative improvement of this solution. The ITS repeatedly invokes this two procedures. In the ITS for the MDP, the STS procedure contains only the main ingredient of TS, which is a short-term memory tabu list without an aspiration criterion. The STS consists of a best improvement LS and a short-term memory to escape from local minima and avoid cycles. The short-term memory is implemented as a tabu list that keeps track of the most recently visited solutions and forbids moves toward them, which is a good way of taking advantage of the history of the search. The complexity of the STS procedure in the ITS is $O\left(n^{2}\right)$. The perturbation procedure is to select variables and flip their values. These variables are randomly selected from a candidate list. The complexity of the perturbed operator in the ITS is

TABLE XIV
COMPARISON OF COMPUTATIONAL TIMES FOR SILVA INSTANCES

TABLE XV
COMPARISON OF COMPUTATIONAL TIMES FOR TYPE1-2, bqp2500, AND RANDOM LARGER INSTANCE


$O\left(n^{3}\right)$. However, if the number of the selected variables satisfies a condition, then the complexity of perturbed operator decreases to $O\left(n^{2}\right)$. There are six parameters to be tuned in the ITS.

Tables VI-X display the name of the instances, the best known solution value, and the results of the DCHNN-EDA and the competitors. Similar to [24], we report the relative values of the solutions, i.e., "Best" means the deviation from the best known solution value of the best solution value found over 30 runs, and "Av." means the deviation from the best known solution value of the average solution value found over 30 runs.

The results of the competitors are directly adopted from the original papers of the competitors.

From Table VI for Silva instances, we can find that the DCHNN-EDA obtains better solutions than the MTS, Tabu-D2 + LS-TS, and KLD + PR. The DCHNN-EDA, ITS, and GRASP-TS all can find the best known solutions for all Silva instances.

From Tables VII-X, we can find that the DCHNN-EDA outperforms the MTS and Tabu-D2 + LS_TS significantly and consistently. For Type1_55 (Table VII) and Type2 instances (Table X), the DCHNN-EDA is slightly worse than the ITS

in terms of both best and average solutions on the whole. For Type1_52 instances (Table VIII), the DCHNN-EDA is slightly better than the ITS in terms of best solution but slightly worse in terms of average solution on the whole. For Typ1_22 instances (Table IX), the DCHNN-EDA is better than the ITS in terms of both best and average solutions on the whole. Note that, in Tables VIII and X, some results for the Tabu-D2 + LS_TS are negative, which can be explained due to rounding errors in floating-point computations [24]. In the DCHNN-EDA, ITS, and MTS, all the real numbers are stored in variables of type "double."

## E. Test for Larger Size Instances

In order to further show the performance of the DCHNNEDA, the DCHNN-EDA is also tested on some larger size problems and compared with the ITS and MTS.

Tables XI and XII display the name of the instances, the best known solution value, and the results of the ITS, MTS, and DCHNN-EDA. For lager size instances, the absolute values of the solutions are very large. Therefore, we report the relative values of the solutions like in Tables V-X.

From Tables XI and XII, we can find that the DCHNN-EDA outperforms the MTS significantly and consistently for all the instances like in Tables VI-X. For Beasley and random larger instances, the DCHNN-EDA is worse than the ITS in terms of both best and average solutions. However, for random larger instances, the performance in terms of best solution seems to be very close to the ITS. Specially, the DCHNN-EDA can obtain better performance than the ITS in terms of best solution for p3000-4, p5000-1, p5000-3, and p5000-4 instances.

## F. Comparison of Computation Time

A comparison of computation times for different heuristic algorithms is difficult because the different heuristic algorithms were tested on different computers. The computational efficiency of the heuristic algorithms is affected not only by the CPU but also by the implementation language, the complier, RAM, operating system, and even the programmer's skills. As done in many works [49], [50], the actual computation time from different computers is often converted or normalized to that on a benchmark computer for an approximate comparison. An indication of the machine's relative speed may be derived from the Mflop/s measure obtained by Dongarra [51]. Thus, the Mflop/s ratios called Dongarra's factors may be used to convert the CPU time of different machines. In this paper, we considered the same computer family for which performances are reported in Dongarra's paper. Table XIII presents the estimated performances and the Dongarra's factors that will be used to compare the computation time.

In Table XIII, we give the same factor for the Intel Pentium 4 Mobile 2.8 GHz with 512-MB RAM as our PC (Pentium4 2.80 GHz ). We also test our algorithm on a Pentium M 1733 MHz notebook and obtain the similar performance as on our PC (Pentium4 2.80 GHz ). Therefore, we give the same factor for the Pentium M 1733 MHz notebook as our PC (Pentium4 2.80 GHz ).

Certainly, such factors lead to a crude computation time approximation. Lan and DePuy [49] pointed out that the average error associated with using the Dongarra conversion could exceed $50 \%$ in some cases. Furthermore, Johnson and McGeoch [52] pointed out that it is common that an algorithm may scale up with problem size differently, depending on machine types. Thus, Dongarra's factors, often used in OR, have to be considered as a rough normalization method and considered better than no normalization method at all. In this paper, we report both the actual computation time in different computers and the transformed or normalized time in second to our PC (Pentium4 2.80 GHz ) in Tables XIV and V.

From Table XIV for Silva instances, we can find that the DCHNN-EDA is faster than other algorithms except for the Tabu_D2 + LS_TS. For Silva instances with 400 and 500 variables, the DCHNN-EDA is slightly slower than the Tabu_D2 + LS_TS. The KLD + PR is the most time-consuming algorithm and therefore cannot be used to solve larger problems. The GRASP + TS is also time consuming and thus difficult to be used to solve larger problems.

From Table XV, we can find that the DCHNN-EDA is faster than the ITS and MTS except for Type1_22 instances. The DCHNN-EDA is slower than the Tabu_D2 + LS_TS for Type1-2 instances.

In the ITS, the stopping criterion is based on the CPU clock. However, given a fixed execution time for the whole program, an open problem of the ITS is how to get optimal tradeoff between the number of TS restarts and the number of iterations of a TS run [24]. In the DCHNN-EDA, HNN search procedure can quickly reach a stable state within a constant number of iterations; therefore, the DCHNN-EDA can get good balance between the number of HNN searches and the solution quality more easily.

From all the results mentioned earlier, we can conclude that the DCHNN-EDA can obtain better or competitive results than metaheuristic algorithms within reasonable computation time.

## G. Further Discussion in Multistart Framework

In this section, we discuss the DCHNN-EDA in the multistart algorithm framework and clarify the similarities and differences between the DCHNN-EDA and other metaheuristic algorithms.

The ITS, Tabu_D2 + LS_TS, GRASP-TS, KLD + PR, and the DCHNN-EDA can all be seen as multistart-based methods. In general, these methods have two phases: the solution construction phase in which the solution is generated and the solution improvement phase in which the solution is improved. Then, each global iteration produces a solution (usually local optima), and the best solution overall is the output of the algorithms [53]. In the solution construction phase, a simple strategy, for example, the random generation of a starting solution, can be used. Similarly, a simple solution improvement method can be applied, for example, simple LS. Furthermore, the solution improvement phase can be performed with a complex metaheuristic algorithm, for example, SA and TS.

The solution improvement phases of the ITS and GRASP-TS are all based on TS. In the Tabu_D2 + LS_TS, TS mechanism

is introduced into both solution construction and solution improvement phases to implement an explorative strategy. The KLD + PR combines the GRASP and PR strategy to improve the performance of the algorithm. As described in the previous sections, all these metaheuristic algorithms use more sophisticated procedures specifically tailored for the MDP. Misevièius et al. [54] pointed out that such "tailored" algorithms, like the ITS, Tabu_D2 + LS_TS, GRASP-TS, and KLD + PR, succeed in search if only they involve the specific problem knowledge. The algorithm designer must be very careful by implementing both the improvement and perturbation (construction) procedures. These procedures should be as much problem-oriented as possible. That is, these multistart-based algorithms are problem dependent, and the ideas and strategies implemented are difficult to apply directly to different problems.

In the DCHNN-EDA, the solution construction phase is based on EDA, and the solution improvement phase is based on HNN, which is a kind of simple and general LS. Thus, the DCHNN-EDA is based on a simple and efficient framework that can be used directly to design solving methods for other combinatorial optimization problems. In summary, the DCHNN-EDA is based on a much simpler and more generalpurpose approach.

On the other hand, the motion equation of HNNs is based on gradient descent, but HNNs should not be viewed as naive gradient descent machines. They can be viewed as a machine which consists of a large number of simple interconnected processing units and therefore can implement complex computational task. Thus, the advantage of HNNs for combinatorial optimization problems is their inherently parallel structure and simple computational requirements, and therefore, HNNs are suitable for direct hardware implementation using analog or digital integrated circuit or optical computers [55], [56]. Considering the speed advantage, it is foreseeable that neural networks will soon become a rapid solution technique for large and complex combinatorial optimization problems [35].

Therefore, the DCHNN-EDA has the advantages of inherently parallel structure and simple computational requirements. In some cases, the DCHNN-EDA is not competitive with designer algorithms such as the ITS. Nevertheless, the aforementioned experimental results show that the DCHNN-EDA can obtain good results within reasonable computation time.

In order to further improve the performance of the DCHNNEDA, we can borrow some ideas from the competitors or other metaheuristic algorithms by the following ways.

1) Adaptive perturbations. One possible method is to adopt the idea of the reactive search, which advocates the use of simple subsymbolic machine learning to automate the parameter tuning process and make it an integral part of the algorithm [57]. Another way of adapting the perturbation is to change deterministically its strength during the search, just as done in VNS [58].
2) Adaptive memory or mechanism to escape from local minima in the HNN descent. In the DCHNN-EDA, the solution improvement phase is based on a simple HNN search, and no history of the search or other mechanism is used to escape from local minima. Therefore, the tabu
mechanism explicitly using the history of the search or other mechanism of escaping from local minima can also be incorporated into the HNN to further improve the performance of the DCHNN-EDA. Thus, the modified versions share similarities to the TS-based algorithms such as the ITS, Tabu_D2 + LS_TS, and GRASP-TS.
3) Population-based DCHNN-EDA extensions. Maintaining a population of solutions provides an alternative way to improve the exploration performance because the solutions in the population can explore different regions of the search space. In the simplest case, no interaction among the solutions or individuals of the population takes place. Certainly, variants that allow interaction among solutions or individuals can be introduced, which can further improve the performance of the algorithm. Thus, the population-based DCHNN-EDA extensions share similarities to the memetic algorithm [59].

## V. CONCLUSION

In this paper, we have presented a novel DCHNN based on EDA as a competitive approach for the MDP compared with existing HNN algorithms and metaheuristic approaches. In order to overcome the local minimum problem of the DCHNN, the idea of EDA is incorporated into the DCHNN. In the DCHNNEDA, the perturbation based on the EDA can generate a new starting point for the DCHNN for further search. Therefore, the DCHNN-EDA can escape from local minima and further search better results. Simulation results on the MDP show that the DCHNN-EDA is better than the other HNN algorithms such as multistart DCHNN and DCHNN with random flips and is better or competitive with metaheuristic algorithms such as the ITS, MTS, Tabu_D2 + LS_TS, GRASP-TS, and KLD + PR.

We also mention the TCNN and NCNN, and point out the similarities and differences between the chaotic neural models and the DCHNN-EDA. Furthermore, we discuss the DCHNNEDA in the multistart algorithm framework and clarify the similarities and differences between the DCHNN-EDA and other metaheuristic algorithms. Based on these discussions, we highlight the characteristics of the DCHNN-EDA and propose some ways to further improve the performance of the DCHNNEDA. At the same time, two future research lines can be followed. First, the DCHNN-EDA is a general optimization algorithm framework and therefore can be applied to other combinatorial optimization problems, for example, channel assignment [60], bipartite subgraph, maximum clique, maximum cut, and polygonal approximation [61] problems. Second, the perturbation based on EDA in the DCHNN-EDA can also be incorporated into other DHNN models, for example, hysteretic [62] and quantized [63], [64] HNNs, for solving different kinds of combinatorial optimization problems.

## ACKNOWLEDGMENT

The authors would like to thank the anonymous associate editor and reviewers for the valuable suggestions and constructive comments.
