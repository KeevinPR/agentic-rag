# Discrete Hopfield network combined with estimation of distribution for unconstrained binary quadratic programming problem 

Jiahai Wang<br>Department of Computer Science, Sun Yat-sen University, No. 132, Waihuan East Road, Guangzhou Higher Education Mega Center, Guangzhou 510006, PR China


#### Abstract

A R T I C L E I N F O

Keywords:
Discrete Hopfield neural network Estimation of distribution Unconstrained binary quadratic programming problem Combinatorial optimization problem


## A B S T R A C T

Unconstrained binary quadratic programming problem (UBQP) consists in maximizing a quadratic 0-1 function. It is a well known NP-hard problem and is a unified model for a variety of combinatorial optimization problems. This paper presents a discrete Hopfield neural network (DHNN) combined with estimation of distribution algorithm (EDA) for the UBQP. The idea of EDA is combined with the DHNN in order to overcome the local minima problem of the network. Once the network is trapped in local minima, the perturbation based on EDA can generate a new starting point for the DHNN for further search, which is in a promising area characterized by a probability model. Thus, the proposed algorithm, named DHNN-EDA, can escape from local minima and further search better results. The DHNN-EDA is tested on a large number of benchmark problems with size up to 7000 variables. Simulation results on the UBQP show that the DHNN-EDA is better than the other improved DHNN algorithms such as multi-start DHNN and DHNN with random flips, and is better than or competitive with metaheuristic algorithms such as simulated annealing, tabu search, scatter search and memetic algorithm.
(c) 2010 Elsevier Ltd. All rights reserved.

## 1. Introduction

In the unconstrained binary quadratic programming problem (UBQP), a symmetric rational $n \times n$ matrix $Q=\left(q_{i j}\right)$ is given, and a binary vector $X=\left\{x_{1}, \ldots, x_{i}, \ldots, x_{n}\right\}, x_{i} \in\{0,1\}$ is searched, such that the objective function
$f(X)=\sum_{i=1}^{n} \sum_{j=1}^{n} q_{i j} x_{i} x_{j}$,
is maximized. Since for each binary variable $x_{i}=\left(x_{i}\right)^{2}\left(\right.$ as $x_{i} \in\{0,1\}$ ), the objective function Eq. (1) can be written as:
$f(X)=\sum_{i=1}^{n} \sum_{j=1}^{n} q_{i j} x_{i} x_{j}+\sum_{i=1}^{n} q_{i j} x_{i}$,
where $q_{i j}(j \neq i)$ is the coefficient of the quadratic term and $q_{i j}$ is the coefficient of the linear term. This problem is also known as the (unconstrained) quadratic bivalent programming problem, the (unconstrained) quadratic $0-1$ programming problem, or the (unconstrained) quadratic (pseudo-) boolean programming problem (Beasley, 1998; Merz \& Katayama, 2004).

The UBQP is known to be NP-hard (Garey \& Johnson, 1979). It is a unified model for a variety of combinatorial optimization problems (Kochenberger, Glover, Alidaee, \& Rego, 2004). The model (1), sometimes with some constraints added (which, however,

[^0]can be reformulated as the model (1) (Kochenberger et al., 2004)), is of considerable practical significance. Numerous hard problems in many diverse areas have been formulated as the UBQP, including VLSI design, manufacturing, computer aided design, statistical mechanics, economics and finance, traffic management, molecular conformation, reliability theory and statistics, and so on. Moreover, many graph problems can be converted to the UBQP including the maximum clique problem, maximum cut problem, maximum vertex packing problem, minimum covering problem, and graph coloring problem (Kochenberger et al., 2004). Algorithms for the UBQP can be utilized to solve these problems as well. Therefore, solution approaches for the UBQP have been an active research area for many years due to the computational challenge and the vast potential applications (Beasley, 1998; Garey \& Johnson, 1979; Kochenberger et al., 2004).

Several exact methods have been developed for the UBQP in the literature (Helmberg \& Rendl, 1998; Palubeckis, 1995). Since however, the UBQP is known to be NP-hard (Garey \& Johnson, 1979), large problems are proved to be intractable for these exact approaches. Several heuristic algorithms, local search (LS) methods, were proposed for the UBQP. These LS heuristic methods include one-pass LS (Boros, Hammer, \& Tavares, 2007; Glover, Alidaee, Rego, \& Kochenberger, 2002), 1-opt and $k$-opt LS methods (Merz \& Freisleben, 2002).

Different kinds of metaheuristic algorithms were also proposed recently to find good solutions for the large UBQP problems. In 1998, Glover, Kochenberger, \& Alidaee (1998) proposed a tabu search (TS) algorithm based on a flexible memory


[^0]:    E-mail address: wjiahai@hotmail.com

system for UBQP instances with up to 500 variables. Beasley (1998) proposed another TS and a simulated annealing (SA), and tested the proposed TS and SA on several series of instances of size up to 2500 variables. Alkhamis, Hasab, \& Ahmed (1998) also proposed a SA for the UBQP. Lodi, Allemand, \& Liebling (1999) proposed an evolutionary algorithm (EA) for the small and medium size UBQP. Merz \& Freisleben (1999) proposed a hybrid genetic algorithm incorporating 1-opt or $k$-opt LS and found new best solutions for several large Beasley problems. This hybrid genetic algorithm can also be called memetic algorithm (MA). Hasab, Alkhamis, \& Ali (2000) presented a comparison among SA, GA and TS for the UBQP. Amini, Alidaee, \& Kochemberger (1999) proposed a scatter search (SS). Katayama \& Narihisa (2001) proposed a SA based on the 1-opt LS and multiple annealing processes. In 2004, Merz \& Katayama (2004) proposed a very powerful MA with an innovative variation operator and a randomized $k$-opt LS. Palubeckis (2004) proposed five different multi-start tabu search (MSTI-5) algorithms for UBQP instances with up to 6000 variables. Recently, Palubeckis (2006) proposed an iterated tabu search (ITS) for UBQP instances with up to 7000 variables.

When designing a heuristic algorithm for combinatorial optimization, it is preferable that it be simple, both conceptually and in practice. Further, it should be effective, and if possible, general purpose. One possible and very promising approach to combinatorial optimization problems is to apply Hopfield neural networks (HNNs) (Hopfield, 1982, 1984; Hopfield \& Tank, 1985). For solving combinatorial optimization by the HNN, the desired objective function of the combinatorial optimization problem being optimized firstly is formulated as the energy function of the network, and then a neural updating rule is employed to guide the time evolution of the states of the network as it automatically seeks a minimum energy state of the energy function. Therefore, the HNN is a simple, effective and general-purpose heuristic algorithm for combinatorial optimization. Furthermore, the HNN is intrinsically easy to parallelize, especially on SIMD parallel computers (Blas, Jagota, \& Hughey, 2005). In general, the HNN has two versions: continuous HNN (Hopfield, 1984) and discrete HNN (DHNN) (Hopfield, 1982). For the continuous HNN, neurons have continuous values within $(0,1)$, and for the DHNN the neurons have only binary values, 0 or 1 . Takefuji, Funabiki, and their co-workers (Funabiki, Takefuji, \& Lee, 1993; Funabiki \& Kitamichi, 1999; Funabiki \& Nishikawa, 1997a, 1997b) found discrete neurons computationally more efficient than continuous neurons and therefore, applied the DHNN to solve a variety of combinatorial optimization problems. The DHNN has an advantage over the continuous HNN in terms of the iteration of updates required to converge to a local minimum and the speed of executing each iteration.

The motivations of this research stem from two aspects. From previous review, we can find that different kinds of metaheuristic algorithms were proposed for the UBQP. However, previous studies using neural network (NN) for the UBQP are surprisingly scarce. This observation motivates our effort to propose a DHNN for the UBQP in this paper. As the past research has expressed (Funabiki et al., 1993; Funabiki \& Kitamichi, 1999; Funabiki \& Nishikawa, 1997a, 1997b), however, the discrete form of the solution search can easily bring on the problem of the local minimum convergence. The NN in the local minimum cannot move to other states, although the current state is not a good solution state. In order to deal with the local minima of the DHNN, some modified DHNN are proposed such as multi-start DHNN (He, Sykora, \& Makinen, 2006; He \& Sykora, 2006) and DHNN with random flips (Smitha, Abramsonb, \& Duke, 2003). How to help the DHNN escape from local minima and further improve the performance of network is a key issue in the HNN field, which motivates our effort to propose
new idea or method to deal with the local minima problem of the network.

In the last decade, more and more researchers tried to overcome the drawbacks of usual recombination operators of evolutionary computation algorithms. Therefore, estimation of distribution algorithms (EDAs) (Baluja, 1994; Harik, Lobo, \& Goldberg, 1999; Larranaga \& Lozano, 2001; Muhlenbein \& Paaß, 1996; Pelikan, Goldberg, \& Lobo, 2002; Zhang, Sun, \& Tsang, 2004, 2005; Zhang, Sun, Xiao, \& Tsang, 2007; Zhang \& Sun, 2006) have been developed. These algorithms, which have a theoretical foundation in probability theory, are also based on populations that evolve as the search progresses. EDAs use probabilistic modeling of promising solutions to estimate a distribution over the search space, which is then used to produce the next generation by sampling the search space according to the estimated distribution. After every iteration, the distribution is re-estimated.

In order to overcome the local minima problem of the DHNN, the idea of EDA is combined with DHNN and a DHNN-EDA is proposed for the UBQP in this paper. Once the network is trapped in local minima, the perturbation based on EDA can generate a new starting point for the HNN for further search, which is in a promising area characterized by a probability model. Thus, the DHNNEDA can escape from local minima and further search better results. The performance of the DHNN-EDA is tested and evaluated by simulating a large number of benchmark instances. Firstly, the DHNN-EDA is compared with other improved DHNN algorithms. Simulation results show the superior performance of the DHNNEDA. Secondly, the DHNN-EDA is compared with metaheuristic algorithms. Simulation results show that the DHNN-EDA is better than or competitive with other metaheuristic algorithms such as TS, SA, SS and MA. Finally, we mention the transiently chaotic neural network (TCNN) (Chen \& Aihara, 1995) and noisy chaotic neural network (NCNN) (Wang, Li, Tian, \& Fu, 2004, 2008) proposed recently to deal with the local minima of the continuous HNN, and discuss the similarities and differences between the chaotic neural models and the DHNN-EDA. Further, we discuss the DHNN-EDA in the multi-start algorithm framework and clarify the similarities and differences between the DHNN-EDA and other metaheuristic algorithms, which suggests or enlightens several ideas to further improve the performance of the DHNN-EDA.

The contributions of this paper thus consist in several aspects: Firstly, since previous studies using NN for the UBQP are surprisingly scarce, a novel NN based algorithm, named DHNN-EDA, is proposed for the UBQP and very competitive results are obtained, which is the contribution to the available literature on the UBQP. Though the DHNN-EDA is not the best algorithm for the UBQP so far, it can be improved further in the future, and now can be seen as the first step or meaningful attempt of adopting the NN method to deal with the UBQP. Secondly, the probabilistic modeling/EDA idea is applied to HNN training and helps the network escape from local minima. Thus, a novel NN model is proposed and can be applied to other combinatorial optimization problems, which is the contribution to the HNN literature. Finally, a comprehensive experimental comparison of the DHNN-EDA with other methods is also provided.

The remaining sections of this paper are organized as follows. In Section 2, we propose a DHNN for the UBQP. In Section 3, we propose a DHNN combined with EDA (DHNN-EDA) for the UBQP. In Section 4, benchmark data sets are used to evaluate the proposed DHNN-EDA. Last section gives several research lines in the future and concludes this paper.

## 2. DHNN for UBQP

The UBQP with a symmetric rational $n \times n$ matrix $Q=\left(q_{0}\right)$ can be mapped onto the DHNN with $n$ neurons. The $i$ th neuron has

input $u_{i}$ and output $v_{i}$. According to objective function Eq. (2), the energy function of the UBQP can be written as:
$E=-\sum_{i=1}^{n} \sum_{j=1, j \neq n}^{n} q_{i j} v_{i} v_{j}-\sum_{i=1}^{n} q_{i i} v_{i}$.
According to the update rule of the DHNN (Hopfield, 1982), the inputs of the neurons are computed by the following motion equation:
$u_{i}=-\frac{\partial E}{\partial v_{i}}=\sum_{j=1, j \neq i}^{n} q_{i j} v_{j}+q_{i i}$.
The binary input/output function of the $i$ th neuron is given by:
$v_{i}(t+1)=\left\{\begin{array}{ll}1 & \text { if } u_{i}(t)>0 \\ 0 & \text { otherwise }\end{array}\right.$
At the beginning, the network is randomly given an initial input $u_{i} \in(-1,1)$. Correspondingly, the neuron states of the network are randomly initialized with 0 or 1 . The DHNN can thus be summarized as follows:

## DHNN for UBQP

initialize $\mathbf{u}$ (randomly around zero);
calculate $\mathbf{v}$ using Eq. (5);
$t=0$;
repeat
copy the state array of neurons $\mathbf{v}$ to lastv;
for $i=1$ to $n$ do/"HNN descent procedure"/
compute $u_{i}(t+1)$ with motion Eq. (4);
update $v_{i}$ using Eq. (5);
end for
$t=t+1$;
until ( $t>$ iterations or stability criteria is satisfied);

The neurons in the network are updated in a sequential update. The stability criterion is to see if the current state $\mathbf{v}$ is equal to last state of the neuron array lastv.

This DHNN can make significant advances in the earlier stages of optimization procedures but slow down significantly as they get close to the optimal solution. That is, the discrete form of the solution search can easily bring on the problem of the local minimum convergence. The NN in the local minimum cannot move to other states. In the next section, we will propose a DHNN combined with EDA for the UBQP in order to overcome the local minima problem of the DHNN.

## 3. DHNN combined with EDA for UBQP

This DHNN can make significant advances in the earlier stages of optimization procedures (that is, the energy function decreases rapidly and dramatically in the earlier stages), and improvements slow thereafter, until after several iterations, for example 10 iterations, a local minimum is encountered and thus the energy function no longer decreases (Smitha et al., 2003). The local minima problem is caused by the gradient descent dynamics of the update rule of the DHNN.

When the network is trapped in a local minimum, a perturbation operator is applied to the current local minimum to generate a new starting point for the HNN. It is desirable that the generated starting point should be in a promising area in the search space. Therefore, in this section, we propose an EDA mutation operator as the perturbation operator in the HNN. The EDA mutation operator can generate a new starting point for the further HNN search, which is in a promising area
characterized by a probability model. In the following subsections, we first briefly review the EDA, and then the DHNNEDA is proposed. Finally, complexity analysis of the DHNNEDA is given.

### 3.1. Estimation of Distribution Algorithm (EDA)

Estimation of Distribution Algorithm (EDA) is a new area of evolutionary computation. In EDAs, there is neither crossover nor mutation operator. Instead, new population is generated by sampling the probability distribution which is estimated from selected promising solutions or individuals of previous generation. Thus these algorithms have a theoretical foundation in probability theory. An algorithmic framework of most EDAs can be described as:

## Framework of EDA

Pop $=$ InitializePopulation() $/ " \text { Initialization" } /$
while Stopping criteria are not satisfied do /"Main Loop"/
Pop ${ }_{\text {ref }}=$ Select $($ Pop $) /$ "Selection" $/$
Prop = Estimate $\left(\right.$ Pop $\left._{\text {ref }}\right) /$ "Estimation" $/$
Pop $=$ Sample $($ Prob $) /$ "Sampling" $/$
endwhile

An EDA starts with a solution population Pop and a solution distribution model Prob. The main loop consists of three principal stages. The first stage is to select the best individuals (according to some fitness criteria) from the population. These individuals are used in the second stage in which the solution distribution model Prob is updated or recreated. The third stage consists of sampling the updated solution distribution model to generate new solution offspring. There has been a growing interest for EDAs in the last year. More comprehensive presentation of the EDA field can be found in Larranaga \& Lozano (2001), Pelikan et al. (2002).

### 3.2. DHNN combined with EDA (DHNN-EDA)

The EDA is a novel optimization tool and primarily used in evolutionary algorithms which are population-based search methods. However, a single EDA technique is hard for solving complicated optimization problems because the location information of solutions found so far (the actual positions of these solutions in the search space) is not directly used for generation of offspring in original EDA (Zhang et al., 2004, Zhang, Sun, \& Tsang, 2005; Zhang et al., 2007; Zhang \& Sun, 2006). Therefore, how to combine EDAs with other techniques represents an important research direction (Zhang et al., 2004). Recently, Zhang et al. (2004, 2005), Zhang et al. (2007), Zhang \& Sun (2006) proposed several works on EDA hybrids for hard optimization problems. Especially, a new operator, called guided mutation, was proposed for generating new solutions. The guided mutation can be regarded as a combination of conventional mutation and EDA offspring generating scheme (Zhang et al., 2004, 2005; Zhang et al., 2007; Zhang \& Sun, 2006). Considering the local minima problem of the DHNN and these successes recently reported in effectively combining EDA and other techniques (Zhang et al., 2004, 2005; Zhang et al., 2007; Zhang \& Sun, 2006), the EDA is introduced into the DHNN, which is a single point search method, to help the DHNN escape from local minima in this paper. The DHNN-EDA for the UBQP can thus be summarized as follows:

## DHNN-EDA for UBQP

initialize $\mathbf{u}$ (randomly around zero);
calculate $\mathbf{v}$ using Eq. (5);
initialize best-so-far solution $\mathbf{g b}$ and probability model $P$;
for $k=1$ to descents do
$t=0$;
repeat
copy the state array of neurons $\mathbf{v}$ to lastv;
for $i=1$ to $n$ do/ "HNN descent procedure"/
compute $u_{i}(t+1)$ with motion Eq. (4);
update $v_{i}$ using Eq. (5);
end for
$t=t+1$
until ( $t$ >iterations or stability criteria is satisfied);
update and keep track for the best-so-far solution $\mathbf{g b}$;
update probability model using $\mathbf{v}$;
perturb the current solution $\mathbf{v}$ using EDA mutation to generate
a new starting point $\mathbf{v}$ for the HNN;
end for

The descents of HNN will visit a number of locally optimal solutions. Statistics information of these optimal solutions can be extracted for building a probability model. Several different probability models have been introduced into EDAs for modeling the distribution of promising solutions. The univariate marginal distribution (UMD) model is the simplest one and has been used in UMD algorithm (Muhlenbein \& Paaß, 1996), population-based incremental learning (PBIL) (Baluja, 1994), compact GA (Harik et al., 1999). Therefore, in this paper the UMD model is adopted to estimate the distribution of good regions over the search space based on the locally optimal solutions. The DHNN-EDA uses a probability vector $P=\left\{p_{1}, \ldots, p_{t}, \ldots, p_{n}\right\}$ to characterize the distribution of promising solutions in the search space, where $p_{i}$ is the probability that the value of the $i$ th position of a promising solution is 1 .

Then an EDA mutation mutates current solution based on the probability vector $P$, which characterizes distribution of promising solutions. It can be expected that offspring fall in or close to a promising area in the search space. The EDA mutation perturbs the current solution $\mathbf{v}$ and guides the HNN to search in binary 01 solution space in the following way:

## Perturb the current solution using EDA mutation

for $i=1$ to $n$ do
If $\operatorname{rand}()<\beta$ /"Sample from probability vector"/
if $\operatorname{rand}()<p_{n}$ set $v_{i}(t+1)=1$, otherwise set $v_{i}(t+1)=0$;
Otherwise, $v_{i}(t+1)=v_{i}(t)$ /"Copy from current solution $\mathbf{v}$ "/
end for
where rand() produces a random number distributed uniformly on $[0,1]$. In the EDA mutation, a bit is sampled from the probability vector $P$ randomly or directly copied from the current solution $\mathbf{v}$, which is controlled or balanced by the parameter $\beta$. The larger $\beta$ is, the more elements of the new starting point are sampled from the vector $P$. Since some elements of offspring are sample from the probability vector $P$, it can be expected that they fall in or close to the promising area. The random sampling mechanism can also provide diversity for the search afterwards.

The parameter $\beta$ controls the strength of the perturbation or mutation. The mutation (kick-move) implemented by the EDA mutation should be chosen adequately strong to allow to leave the current local minimum and to enable the HNN to find new,
possibly better solutions. If the kick-move is too weak, the HNN may return after very few steps to the local minimum to which the kick-move has been applied. On the other hand, the kick-move should be adequately weak to keep characteristics of the current local minimum since part of the solution may already be close to optimal. A major problem for too strong kick-move is that the resulting algorithm would be very similar to repeating the HNN search from randomly generated solutions. Applying only rather small mutations has an additional advantage that the HNN requires only a few steps to reach the next local optimum, i.e. new local optima can be identified very fast - typically much faster than when starting from a randomly generated solution. Hence, for the same given computation time more HNN searches can be performed than when starting from randomly generated solutions.

In the DHNN-EDA, the probability vector $P$ is initialized as $P=(0.5, \ldots, 0.5, \ldots, 0.5)$. The probability vector can be learned and updated at each descent of the HNN for modeling the distribution of promising solutions in the same way as in the PBIL algorithm (Baluja, 1994):
$p_{i}(t+1)=(1-\lambda) p_{i}(t)+\lambda v_{i}(t)$;
where $\lambda \in(0,1]$ is the learning rate.
The main loop of the framework of EDA consists of three principal stages, selection, estimation and sampling. In the DHNNEDA, current locally optimal solution $\mathbf{v}$ generated by the HNN descent procedure is selected, then $\mathbf{v}$ is used in the estimation stage in which the probability model $P$ is updated according to the rule defined by Eq. (6). The sampling process is described in the EDA mutation operator. However, there are several differences between the DHNN-EDA and the most usual population-based EDA algorithms. Firstly, in the sampling process of the DHNN-EDA, the probability model is not sampled directly as in the pure or original EDA, but rather used as part of the EDA mutation. Secondly, although the DHNN-EDA uses a univariate probability model in the style of the PBIL, only one solution is sampled from the probability model and only one solution is used to update the model (that is, the population size is equal to 1). Thus, the DHNN-EDA is more akin to the EDA hybrid, the guided mutation (Zhang et al., 2004, 2005; Zhang et al., 2007; Zhang \& Sun, 2006). In contrast to that the guided mutation acts on the best-so-far solution gb, the EDA in the DHNN-EDA mutates the current solution $\mathbf{v}$ in order to increase the diversification level and thus exploration ability in the search process. Furthermore, the main novelty of the DHNNEDA consists in applying the probabilistic modeling/EDA idea to train HNN and thus help the network escape from local minima.

Guided by a probability model which characterizes the distribution of promising solutions in the search space, the EDA mutation mutates the current solution to generate a new starting point. The EDA mutation operators provide a mechanism for combining global statistical information about the search space and the information of the current solution found during the previous search, and thus generate new starting points for further search.

### 3.3. Complexity analysis

The DHNN-EDA repeatedly invokes two procedures-HNN search and EDA mutation-to construct a good starting solution for further HNN search. Parameter descents can be seen as an upper bound on the number of HNN invocation and then can be seen as a stopping criterion. One updating iteration is defined as one complete update of all $n$ neurons according to Eqs. (4) and (5). The maximum iteration number of the DHNN-EDA is descents $\times$ iterations.

For the UBQP with a symmetric rational $n \times n$ matrix $Q=\left(q_{0}\right)$, the HNN uses $n$ neurons. According to Eq. (4), the calculation in each neuron takes time $O(n)$. Therefore, a sequential traversal of all $n$ neurons takes time $O\left(n^{2}\right)$ in the DHNN-EDA. Updating of

the probability model takes time $O(n)$. Therefore, the whole complexity of the DHNN-EDA is $O\left(n^{2}\right)$.

## 4. Simulation results and discussion

In order to assess the performance of the DHNN-EDA, simulations were implemented in C on a PC (Pentium 42.80 GHz ). In this section we describe the benchmark datasets, the parameter setting, and present the results of the DHNN-EDA on the benchmark datasets. We also compare the results with those DHNN algorithms with different modifications to demonstrate the effect of the EDA perturbation, and compare the results with other metaheuristics such as SA, TS, GA, and MA.

### 4.1. Benchmark datasets

In this paper, we test the DHNN-EDA on 56 benchmark problems which are also used in numerous other studies of the UBQP (Beasley, 1998; Merz \& Katayama, 2004; Palubeckis, 2006). These benchmark problems include two groups. The first group has 35 problems and the second group has 21 randomly generated problems of larger size and higher density. The size of these benchmark problems ranges from 500 (small scale) to 7000 (large scale).

The basic parameters and the best-known solutions of first group including 35 problems are shown in Table 1. In Table 1, density of the problems means the ratio of the number of nonzero coefficients of quadratic terms in Eq. (2). Minimum and maximum of the coefficients of the linear and quadratic terms are also provided. The glov500 set in the first group is studied by Glover
et al. (1998). The glov500 set has five instances of size $n=500$ with a matrix density varying between 0.1 and 1.0. The second set kbg1000 is kindly provided by Kochenberger and has been used to test the performance of 55 (Amini et al., 1999). The kb-g1000 set has 10 instances of size $n=1000$ with a matrix density varying between 0.1 and 1.0. The bqp1000 ( $n=1000$ ) and bqp2500 ( $n=2500$ ) were first studied by Beasley (1998) and each set has 10 instances with a matrix density 0.1 .

The glove500, bqp1000 and bqp2500 set in Table 1 were taken from the OR-Library website (Beasley, 2008), and the bqp2500 set is the largest UBQP test set in the OR-Library. The kb-g1000 set was kindly provided by Merz \& Katayama (2004). There are several small-scale test instances ( $n<500$ with varying densities) contained in the OR-Library website. These instances are not considered in our experiments, since they are solved easily by heuristics in very short time and thus no good comparisons among algorithms can be provided. Note that the UBQP is formulated as a minimum problem in Glover et al. (2002), while the UBQP is formulated as a maximum problem in this paper just like in Beasley (1998), Merz \& Katayama (2004), Kochenberger et al. (2004), Boros et al. (2007).

In order to further show the performance of the DHNN-EDA, the DHNN-EDA is tested on the second group including 21 randomly generated problems of larger size and higher density which is first produced and used in the Palubeckis (2006). These 21 problems have density from $50 \%$ to $100 \%$ and vary in size from 3000 to 7000 variables. All nonzero coefficients of the objective function are drawn uniformly at random from the interval $[-100,100]$. The basic parameters and the best-known solutions of 21 problems are shown in Table 2. The sources of the generator and input files

Table 1
Main characteristics of 35 benchmark test problems in the first group for UBQP.
Table 2
Main characteristics of 21 benchmark test problems with larger size and higher density in the second group for UBQP.
to replicate these problem instances can be found at http//:www.softer.ktu.lt/ gintaras/ubqop_its.html.

### 4.2. Parameter setting

The DHNN-EDA has two main parameters, parameter $\beta$ and $\lambda$, to be tuned. The parameter $\beta$ controls the strength of the mutation, and the learning rate $\lambda$ balances the contributions between the old statistical information extracted from historical local minima and the information of the current local minimum to the new probability vector. The bigger $\lambda$ is, the greater the contribution of current local minimum is.

To assess the effects of these parameters, the DHNN-EDA is tested as a pre-experimental tuning on a representative subset of problems with different size and density from Tables 1 and 2. These selected problems include glow500-5, kb-gb1000-10, bqp1000-1, bqp2500-1, p3000-1, p4000-2, p5000-3, p5000-4, p6000-3 and p7000-3.

Firstly, $\beta$ and $\lambda$ are defined to take values within the following discrete range $(0.1,0.2, \ldots, 0.9)$, respectively. In the preliminary tests, we found that the parameter combinations $\beta \in(0.1,0.2,0.3)$ and $\lambda \in(0.1)$ can obtain good results, and there is no significant difference in results using these parameter combinations. This suggests that relatively small mutation strength and relatively small contribution of the current local minimum is adequate for the UBQP.

Secondly, in order to further investigate the effect or sensitivity of parameter $\lambda$, we fix the parameter $\beta=0.2$, and then vary parameter $\lambda$ within the range $(0.01,0.02, \ldots, 0.09)$. We find no significant difference in the results using different values of the parameter $\lambda$ within the range, which suggests that the range of reasonable values of the parameter $\lambda$ is rather large only if $\lambda$ is set to a very small value. The problem for too strong mutation strength and too big contribution of the current solution is that the resulting algorithm is very similar to repeating the HNN search from randomly generated or initialized starting point like the multi-start HNN (He et al., 2006). On the other hand, since PBIL described by Eq. (6) is an incremental learning method, the learning rate should be set to a very small value, or else
the probability model will "forget" the old information extracted from the historical local minima quickly.

Finally, $\beta$ is randomly drawn from the interval $[0.1,0.3]$ and $\lambda$ is randomly drawn from the interval $[0.01,0.1]$, we also find no significant difference in the results.

Based on the preliminary computational experiments and analysis in theory on the parameters, we select a parameter combination, $\beta=0.2$ and $\lambda=0.04$, for all test benchmark problems shown in Tables 1 and 2 in the whole simulation. Certainly, the parameters are chosen experimentally, and tuning of these parameters may be necessary when solving different optimization problems. In the future, we will research self-adaptive control strategy for these parameters.

The DHNN for the UBQP works hardest and most productively, measured by a rapidly decreasing energy, during the first eight iterations. Therefore, the maximum iteration number of each descent in the DHNN-EDA is set to 10 iterations, and each test run is set to invoke 500 times HNN search, that is, descents $=500$. The maximum iteration number of the DHNN-EDA is $10^{*} 500=5000$. This is a trade-off between solution quality and computation time. If given more computation time, the DHNN-EDA can implement or invoke more times HNN search and therefore, can be expected to produce better results.

### 4.3. Comparison with HNN algorithms

In this section, we first describe two modified DHNN algorithms proposed for combinatorial optimization problems recently (He et al., 2006; He \& Sykora, 2006; Smitha et al., 2003), and then we compare the DHNN-EDA with them to show how the EDA process can improve the performance of the DHNN.

He et al. (2006) proposed an improved HNN which repeats the random initial solution construction and HNN search a number of times and returns the best solution. Therefore, the improved HNN is called multi-start DHNN algorithm in this paper. He et al. applied the multi-start DHNN to two-page crossing number problem (TPCNP) and outerplanar drawing problem and obtained better results than other NNs (He et al., 2006; He \& Sykora, 2006). The structure of the multi-start DHNN algorithm is as follows:

## Multi-Start DHNN for UBQP

initialize the best-so-far solution $\mathbf{g b}$;
for $k=1$ to descents do
initialize $\mathbf{u}$ (randomly around zero);
calculate $\mathbf{v}$ using Eq. (5);
$t=0$;
repeat
copy the state array of neurons $\mathbf{v}$ to lastv;
for $i=1$ to $n$ do/*HNN descent procedure*/
compute $u_{i}(t+1)$ with motion Eq. (4);
update $v_{i}$ using Eq. (5);
end for
$t=t+1$;
until ( $t>$ iterations or stability criteria is satisfied);
update and keep track for the best-so-far solution gb;
end for

In the multi-start DHNN, HNN descent procedure is restarted with different initial states of the neurons for several times, and the best solution is output. In other words, the best local minimum among the local minima produced by several different descents of the HNN is selected as the best solution.

Smitha et al. (2003) proposed a modified HNN where random perturbation (random flip mutation) is used to help the network escape from local minima, and therefore, the HNN is called DHNN with random flips in this paper. The simulation results on timetabling problems show that the DHNN with random flips is comparable to or better than the SA, TS and greedy search methods (Smitha et al., 2003). To avoid losing good solution during the evolution of the network, we add an additional step, update and keep track for the best-so-far solution gb, to the original DHNN with random flips. DHNN with random flips can thus be summarized as follows:

## DHNN with random flips for UBQP

initialize $\mathbf{u}$ (randomly around zero);
calculate $\mathbf{v}$ using Eq. (5);
initialize best-so-far solution $\mathbf{g b}$;
for $k=1$ to descents do
$t=0$;
repeat
copy the state array of neurons $\mathbf{v}$ to lastv;
for $i=1$ to $n$ do/*HNN descent procedure*/
compute $u_{i}(t+1)$ with motion Eq. (4);
update $v_{i}$ using Eq. (5);
end for
$t=t+1$;
until ( $t>$ iterations or stability criteria is satisfied);
update and keep track for the best-so-far solution gb;
randomly choose a neuron, and flip according to threshold;
end for

In the DHNN with random flips, the stochasticity at the end of each iteration is created by randomly choosing a neuron and assigning its state value of 0 or 1 . A threshold is used to control the stochasticity, so that if the threshold is 0.5 , then there is an equal chance of a neuron state becoming 0 or 1 . However, if the threshold is increased to say 0.7 , then there is only a $30 \%$ chance that the neuron will be assigned a value of 1 . Thus, the modifications to the network dynamics described above contribute to an efficient wandering of the search space in short bursts of gradient descent, using random perturbations to escape local minima. In
this paper, the threshold to control the stochasticity is set to 0.85 as in Smitha et al. (2003). Note that the DHNN with random flips in this paper uses the sequential updating, while the original DHNN with random flips uses the parallel updating.

The two modified HNNs mentioned above all invoke several times HNN search, which is similar to the DHNN-EDA. Therefore, we compare the DHNN-EDA with them in order to determine how much the EDA process contributes to the search.

Table 3 shows the best, average and standard deviation values produced by the multi-start DHNN, DHNN with random flips, and the DHNN-EDA, respectively, for the 35 test problem instances over 30 independent runs. The best-known values of these test problem instances are also shown in Table 3. The last two rows show the average solution values and the average percent deviation of the solutions found by each algorithm from the best-known values shown in the second column of Table 3. From Table 3, we find that the DHNN with random flips gets slightly better best results than the multi-start DHNN. But the DHNN with random flips is worse than the multi-start DHNN in terms of average solutions and standard deviation. It is apparent that the DHNN-EDA performs better than the multi-start DHNN and DHNN with random flips in all instances in terms of best, average and standard deviation values. The average results of the DHNN-EDA are even better than the best results of the multi-start DHNN and DHNN with random flips.

The multi-start DHNN and DHNN with random flips find only one best-known value for small size instance, respectively. The DHNN-EDA can obtain the best-known value in 27 out of 35 instances. Bold figures indicate the best-known value obtained by all the algorithms. The average percent deviation of the best solutions found by the multi-start DHNN, DHNN with random flips, and the DHNN-EDA from the best-known values for 35 instances are $0.25858 \%, 0.25051 \%$, and $0.00580 \%$, respectively. The average percent deviation of the average solutions found by the multi-start DHNN, DHNN with random flips, and the DHNN-EDA from the best known values for 35 instances are $0.47952 \%, 0.66452 \%$, and 0.05096\%, respectively. The average standard deviation of the mul-ti-start DHNN, DHNN with random flips, and the DHNN-EDA for 35 instances are $597.48,1831.32$ and 138.57 , respectively. The low standard deviation of the DHNN-EDA reveals that the DHNNEDA guided by the EDA model has high stability.

In the multi-start DHNN, random initialization is a random sampling mechanism in the search space. That is, the starting solutions are generated completely randomly and thus each HNN search is independently invoked. It does not take into consideration any information from the previous HNN search and can be seen as a memory-less method. If it is lucky enough to start from a good initial point, the multi-start HNN can converge to a good solution. In contrast, the DHNN with random flips and the DHNN-EDA all alternate between calls to HNN search and solution perturbation procedures. Each time the solution perturbation procedure is applied to the solution coming from the previous HNN search, and thus the HNN descents are not independently invoked. Therefore, the search history of previous HNN search is likely utilized by the subsequent HNN search to help the network escape from local minima. However, there is difference between the DHNN with random flips and the DHNN-EDA. The DHNN with random flips uses random perturbation or mutation on the just last solution to help the next HNN escape from local minima, and thus does not explicitly utilize global statistical information in the previous search. Further, which neuron state is chosen to be flipped is decided by a completely random way, and therefore, it is somewhat "blind", which leads to high standard deviation. The high standard deviation reveals that the method has low stability. In the DHNN-EDA, a probability vector is built to characterize the distribution of promising solutions in the search space. The DHNNEDA is guided by the global search information in EDA model,

Table 3
Comparison of the results obtained by the multi-start DHNN, DHNN with random flipping perturbation, and the DHNN-EDA for the 35 test problem instances.

and therefore, can search better solution in the promising region, which is the main reason that the DHNN-EDA can obtain better results than the multi-start DHNN and the DHNN with random flips. On the other hand, the probability vector extracted from the previous search history can be seen as a long term memory. The use of memory is nowadays recognized as one of the fundamental elements of a powerful heuristic algorithm.

Table 4 shows the computation time of the three algorithms in second. Only one neuron in the DHNN with random flips is chose to be flipped, therefore, the network maybe return to the old local minima after very few iterations. The DHNN-EDA mutates the current local minimum by the EDA mutation and it also can converge to next local minimum quickly. Therefore, the DHNN-EDA is much faster than the multi-start HNN starting from a randomly generated solution. Hence, for the same given computation time, the DHNN-EDA can invoke more HNN descents than multi-start HNN. The DHNN-EDA has good balance between the computation time and solution quality.

In summary, the probabilistic modeling/EDA idea is applied to HNN training and helps the network escape from local minima. Thus, the performance of the DHNN is greatly improved due to the EDA process, which is our main contribution in this paper.

### 4.4. Comparison with metaheuristic algorithms

In order to further show the effectiveness of the DHNN-EDA, we now present a comparative performance against some metaheuristic algorithms including the TS proposed by Beasley (TS-B), the SA proposed by Beasley (SA-B) (Beasley, 1998), the SS proposed by Amini (SS-A) (Amini et al., 1999), the EA proposed by Lodi et al. (1999), MA proposed by and Merz and Freisleben (MA-MF) (Merz \& Freisleben, 1999) and MA proposed by Merz and Ktayama (MA-MK) (Merz \& Katayama, 2004). These algorithms have been proposed as one of the best heuristic approaches to the UBQP in those days.

Table 5 displays the name of the instances, the best-known solution value, the results produced by the metaheuristic algorithms and the DHNN-EDA. The results of the competitors are directly adopted from the original papers of the competitors. For bqp1000 and bqp2500 instances, the last two rows show the average solution values and the average percent deviation of the solutions found by each algorithm from the best known values.

Only the best solution value obtained is provided for the EA for glov500 instances. The EA and the DHNN-EDA also can get the best-known values for all glov500 instances.

For the SS-A, only the best solution value for the sets glov500 and kb-g1000 are available. The DHNN-EDA and SS-A also can get the best known values for all glov500 and kb-g1000 instances.

For the TS-B and SA-B, only the best solution value for each instance of set glov500 and the problem sets bqp1000 and bqp2500 are available. The two sets of bqp1000 and bqp2500 are first provided in Beasley (1998) as new benchmark instances contained in the ORLIB (Beasley, 2008). In those days, the values of the solutions obtained by these algorithms were reported as the bestknown solutions for each instance of the two sets. Comparing with SA-B, the DHNN-EDA can obtain better solution for all instances. Further, the average results of the DHNN-EDA are better than

Table 4
Comparison of average computational time of the multi-start DHNN, DHNN with random flipping perturbation, and the DHNN-EDA for the 35 test problem instances.

the best results of SA-B in the whole. Compare with the TA-B, the DHNN-EDA also can obtain better solutions for all instances except that the DHNN-EDA get the same solutions for glov500-1 and glov500-4 instances, and get worse solution for bqp2500-5, bqp2500-8 and bqp2500-9 instances. Further, the average results of the DHNN-EDA are better than the best results of the TA-B for bqp2500 instances in the whole.

For the MA-MF, the average solution values are provided. Although the DHNN-EDA is slightly worse than the MA-MF for glov500 and bqp1000 instances in terms of average solution value, the DHNN-EDA can obtain better results for all bqp2500 instances except for bqp2500-4 and bqp2500-5 instances.

For the MA-MK, only the average solution value for each instance is given because the MA-MK can obtain all the best-known values for the 35 instances in 30 independent runs. It is not surprising that the DHNN-EDA is outperformed by the MA-MK. The MAMK includes a randomized greedy heuristic to create the initial population, a highly effective randomized $k$-opt LS to obtain a population of locally optimum solutions, and a new recombinationbased variation operator, called innovative variation, to produce good starting points for the LS. The initialization, recombinationbased variation operator, and strong LS are all tailored specifically for the UBQP by taking the properties of the fitness landscape of the UBQP into account. In contrast to the MA-MK, the DHNNEDA does not include any specifically design or consideration for the UBQP.

### 4.5. Comparison of results for larger size and higher density instances

Though the bqp2500 instances are the largest instances in the OR-Library, Palubeckis (2006) pointed out that those problem instances are not sufficiently strong for state-of-the-art algorithms for the UBQP. Therefore, Palubeckis proposed five different MST algorithms (MST1-MST5) (Palubeckis, 2004) and an ITS algorithm (Palubeckis, 2006) and tested these TS based algorithms on a set of randomly generated problems of larger size and higher density. These 21 generated problems have density from $50 \%$ to $100 \%$ and vary in size from 3000 to 7000 variables. In order to further show the performance of the DHNN-EDA, the DHNN-EDA is also tested on these larger size problems and compared with other algorithms.

The ITS and MST2 are the most powerful algorithms for the UBQP so far, therefore, the ITS and MST2 can be used as the benchmark algorithms to evaluate the performance of the DHNN-EDA.

The main ingredients of the ITS include solution perturbation procedures, get start point (GSP), for construction of a starting solution, and simple tabu search (STS) for iterative improvement of this solution. The ITS repeatedly invokes this two procedures. In the ITS for the UBQP, the STS procedure is an adaptation of a simple TS implementation proposed by Beasley (1998). The STS consists of a best improvement LS and a short term memory to escape from local minima and to avoid cycles. The short term memory is implemented as a tabu list that keeps track of the most recently visited solutions and forbids moves toward them, which is a good way of taking advantage of the history of the search. The complexity of the TS procedure described by Beasley (1998) is $O(n^{2})$. But a computational trick, mapping of the current solution to the zero vector, is applied in the STS for the UBQP. Thus, the ITS in fact work with a transformed instances of Eqs. (1) and (2). The trick of transformation or modification designed or tailored specifically for the UBQP, allows to hasten exploration of the neighborhood of the current solution and reduces the computation time significantly. Therefore, the complexity of TS procedure in the ITS decreases to $O(n)$. The computation trick also plays the crucial role in the solution perturbation procedure. The perturbation procedure is to select variables that must undergo a flipping operation. These variables are randomly selected from a candidate list. The

Table 5
Comparison of the results obtained by the five metaheuristic methods and the DHNN-EDA for the 35 test problem instances.

Table 6
Comparison of the results obtained by the five metaheuristic methods and the DHNN-EDA for the 21 test problem instances with larger size and higher density.

![img-0.jpeg](img-0.jpeg)

Dongarra's paper, and estimated the performance for the required processor frequency using interpolation. Table 7 presents the estimated performances interpolated at the required chip frequency, and the Dongarra's factors that will be used to compare the computation times.

Certainly, such factors lead to a crude computation time approximation. Lan \& DePuy (2006) pointed out that the average error associated with using the Dongarra conversion could exceed $50 \%$ in some cases. Further, Johnson \& McGeoch (2002) pointed that it is common that an algorithm may scale up with problem size differently depending on machine types. Thus, Dongarra's factors, often used in Operations Research, have to be considered as a rough normalization method, and considered better than no normalization method at all. In this paper, we report both the actual computation time in different computers and the transformed or normalized time (NT) in second to our PC (Pentium 42.80 GHz ) in Tables 8 and 9 .

From the rough estimation results shown in Table 8, we can find the DHNN-EDA is faster than the SA-B and TS-B, but worse than the MA-MF. The DHNN-EDA is faster than the MA-MK for 500 and 1000 variable instances, but slower for bqp2500.

From Table 9, we can find the DHNN-EDA spends more time than the ITS, MST1-2 and MA for the larger instances. In the ITS and MST1-2 for the UBQP, the complexity of the STS procedure decreases from $O\left(n^{2}\right)$ to $O(n)$ by using the computational trick mentioned above. Therefore, the ITS, MST1-2 algorithms based on the computational trick are all faster than the DHNN-EDA. In the ITS, MST1-2 algorithms, the stopping criterion is based on the CPU clock. Thus, given a fixed execution time for whole program, an open problem of these algorithms is how to get optimal trade-off between the number of TS restarts and the number of iterations of a TS run (Palubeckis, 2006). In the DHNN-EDA, HNN search procedure can quickly reach a stable state within a constant number of iterations, therefore, the DHNN-EDA can get good balance between the number of HNN search and solution quality more easily.

Given more time to the MA-MK, it is expected that the MA-MK can evolve more generations and produce some improvements in its performance. But Palubeckis in Palubeckis (2006) pointed out that increasing the time limit for the MA-MK several times does not help very much for the larger instances. The reason may be that the MA-MK is easily trapped in premature situation and thus can not improve the solution continuously for larger instances.

Note that Martı' (2003) also pointed out that one can not take the normalized results shown in Tables 8 and 9 too literally since those running times obtained on different machines. Small differences in running time should not be used to draw any conclusion regarding the relative effectiveness of the algorithms. Within the same order of magnitude should be regarded as indistinguishable (Marth', 2003).

From all the results mentioned above, we can conclude that the DHNN-EDA can obtain better or competitive results than metaheuristic algorithms within reasonable computation time.

Table 9
Comparison of average computation time for 21 benchmark test problems with larger size and higher density.

### 4.7. Discussion and remarks

In this section, firstly we mention the TCNN and NCNN proposed recently to deal with the local minima of the continuous HNN, and point out similarities and differences between the chaotic neural models and the DHNN-EDA. Then, we explain our previous work of the DHNN based on the EDA and its application to the TPCNP in order to show the robustness of the proposed algorithm in this paper. Further, comparison of the DHNN-EDA with LS algorithms with EDA is also given. Finally, we discuss the DHNN-EDA in a multi-start algorithm framework and clarify the similarities and differences between the DHNN-EDA and other metaheuristic algorithms, which suggests or enlightens several ideas to further improve the performance of the DHNN-EDA.

### 4.7.1. Similarities and differences between chaotic neural models and DHNN-EDA

In order to deal with the local minima of the continuous HNN, Chen \& Aihara (1995) proposed a TCNN by adding a decaying negative self-feedback to continuous HNN and thus introducing chaotic dynamics. Recently, Wang et al. $(2004,2008)$ proposed a NCNN by adding decaying stochastic noise into the TCNN. The chaotic dynamics and stochastic dynamics can prevent the network from getting stuck at local minima. But it is difficult to control and balance the chaotic dynamics, stochastic dynamics and gradient ascent dynamics for converging to a stable equilibrium point corresponding to an acceptably near-optimal solution. There are a lot of parameters to be tuned in these models to control those dynamics and the interaction of control parameters with the model performance is complex in practice.

In contrast to the TCNN and NCNN, the DHNN-EDA does not introduce the stochastic dynamics or chaotic dynamics into the original HNN gradient descent dynamics, and therefore, does not attempt to prevent the system getting stuck at local minima. Rather, once the network converges to a local minimum, it aims to generate a new better starting point by EDA mutation for further HNN search. One advantage of this approach is that it has no effect on the energy minimization or original HNN gradient descent dynamics until the network converges to a stable point. In contrast to the TCNN and NCNN based on continuous HNN, the algorithm is based on DHNN and therefore, is more efficient, fast and simple.

The DHNN-EDA has also deterministic dynamics like in the TCNN and is not guaranteed to converge to a global optimum. But from our simulation, the DHNN-EDA can obtain good solutions within reasonable computation time.

### 4.7.2. Explanation of our previous work of DHNN based on EDA

In our previous brief work (Wang, 2008), a similar DHNN approach based on EDA is proposed for the TPCNP. Simulation results show that the EDA can help the network escape from local minima, and thus the DHNN based on EDA algorithm outperforms the other NN algorithms and heuristics specifically designed for the TPCNP, which shows the robustness of the proposed algorithm in this paper.

However, the DHNN-EDA proposed in this paper has some difference from the previous work (Wang, 2008). In the previous work, the EDA mutates the best-so-far solution $\mathbf{g b}$ to generate a new starting point for HNN search like in the guided mutation (Zhang et al., 2004, 2005; Zhang et al., 2007; Zhang \& Sun, 2006). In the work of this paper, the EDA mutates the current solution $\mathbf{v}$. The current solution $\mathbf{v}$ appears to be rather good and not much worse than the best-so-far solution $\mathbf{g b}$. The strategy to submit current solution $\mathbf{v}$ instead of best-so-far solution $\mathbf{g b}$ to the EDA mutation increase the diversification level in the search process, and the perturbed solution remains to be of sufficiently high quality and can serve as a good starting point for the next HNN search. Since
this strategy increases the diversification in the search process, it can further improve the exploration performance of the DHNN based on EDA and thus find better solution finally, which is confirmed by our preliminary experiment results. Hence, the DHNNEDA in this paper is an improved version of our previous algorithm. Further, more comprehensive comparison with other algorithms and analysis of the DHNN-EDA are provided in this paper.

### 4.7.3. Comparison of DHNN-EDA with LS algorithms with EDA

As mentioned in Introduction, some LS algorithms, including randomized first 1-opt LS, best improvement 1-opt LS and randomized $k$-opt LS, are proposed for the UBQP (Katayama, Yamashita, \& Narihisa, 2007; Merz \& Freisleben, 2002; Merz \& Katayama, 2004). In order to confirm the effectiveness of the DHNN, we compare the DHNN-EDA with these LS algorithms combined with EDA mutation, respectively.

In the 1-opt LS algorithms, the single bit that delivers positive gain or the highest gain in objective function is flipped until the gain becomes negative in each iteration. After each flip, a vector of gains is maintained and updated. The basic idea of the $k$-opt LS is to find a solution by flipping a variable number $k$ bits in the solution vector each iteration. In each step, a sequence of $n$ solutions is generated by flipping the bit with the highest associated gain. After each flip, a vector of gains is also maintained and updated. Further, a candidate set is used to assure that each bit is flipped no more than once. The best solution in the sequence is accepted as the new solution for the next iteration. More specifically, in the randomized $k$-opt LS, the randomized first 1-opt LS is executed before the highest gain found by the best improvement 1opt LS with a tabu fashion, which is to achieve a variable $k$-opt neighbor solution, is negative. Since the best improvement 1-opt with a tabu fashion can lead the randomized $k$-opt LS to temporally move to tentative solutions with negative gains (that is, permitting occasional bad moves), the randomized $k$-opt LS has ability of escaping from local minima, and is thus a more sophisticated LS method. The implementation of the randomized $k$-opt LS is also more sophisticated than that of the DHNN defined by Eqs. (4) and (5).

In the experiments, we used a restricted set of instances including kb-g1000-9, kb-g1000-10, bqp2500-2, bqp2500-3, bqp250010, p7000-1, p7000-2 and p7000-3. These instances are selected because, firstly, they are of different sizes and densities. Secondly, they are the hardest instances and thus can reveal the differences among the algorithms (Merz \& Freisleben, 2002; Merz \& Katayama, 2004; Palubeckis, 2006). In the pre-experimental testing, we find that the LS algorithms with EDA can obtain good performance by setting the same values of parameter $\beta$ and $\lambda$ as in the DHNNEDA. Further, the same running time as in the DHNN-EDA is allotted for the implementation of the LS algorithms with EDA for fair comparison. Table 10 displays the name of the instances, the best-known solution value, the results produced by the randomized first 1-opt LS with EDA, the best improvement 1-opt LS with EDA, the randomized $k$-opt LS with EDA and the DHNN-EDA over 30 independent runs. For large size problems (p7000 instances), the relative values of the solutions are reported like in Table 6.

From Table 10, we can find that the DHNN-EDA is better than the best improvement 1-opt LS with EDA. The DHNN-EDA is also better than the randomized first 1-opt LS with EDA in the whole. For kb-g1000-9 and kb-g1000010 instances, the DHNN-EDA obtains slightly better average results than the randomized $k$-opt LS with EDA. However, for the other instances, the DHNN-EDA is outperformed by the randomized $k$-opt LS with EDA. We remark that it is reasonable because the randomized $k$-opt LS with the tabu fashion permits occasional bad moves to escape from local minima and thus shares some characteristics with complex metaheuristic. We also can find the randomized $k$-opt LS with EDA is better than

Table 10
Comparison of the results obtained by several LS methods combined with EDA and the DHNN-EDA.
the MA-MK for p7000 instances. As pointed out earlier, the reason may be due to that the crossover in the MA-MK is designed by taking the properties of the fitness landscape into account for only the first group benchmark instances, and may be not suitable for the second group benchmark instances with larger size and higher density. Thus, the MA-MK is easily trapped in premature situation. In contrast, EDA can effectively guide the randomized $k$-opt LS to search better results.

Katayama et al. (2007) pointed out that the performance of LS highly depends on neighborhood definitions and replacement ways and thus problem-specific neighborhood operator (flip, swap, or add and drop operator) should be designed carefully for specific problem. For HNNs, only the problem-specific objective function is embedded in the energy function that the network evolution tries to minimize. For a specific problem, simple effective LS can also be incorporated into standard HNNs. For example, an efficient multivalued HNN was proposed for the traveling salesman problem (TSP) (Mérida-Casermeiro, Galán-Marín, \& Muñoz-Peréz, 2001). The dynamics or updating rule for the multivalued HNN guaranteeing the energy decrease are derived from the efficient $k$-opt (2-opt and 3-opt) moves. Simulation results show that the multivalued HNN is superior to the best NN for the TSP at that time. Thus, it is concluded in Mérida-Casermeiro et al. (2001) that for NNs the hybrids with classical optimization techniques are one of the best ways to go if one wants to handle larger instances and obtain reasonably good results. More recently, a construc-tive-optimizer neural network (CONN) was proposed for the TSP (Saadatmand-Tarzjan, Khademi, Akbarzadeh-T, \& Moghaddam, 2007). The basic optimizer NN (BONN) in the CONN is algorithmically similar to the family of 2.5 -opt LS for the TSP. The BONN uses a feedback configuration similar to HNNs and is presented in the context of NNs. The energy function decreases monotonically during BONN training. Simulation results show that the CONN provides the best compromise between computation time and accuracy among currently reported NNs for the TSP. Hence, the randomized $k$-opt LS can also be incorporated into the DHNNEDA, which is just our future research work.

### 4.7.4. Similarities and differences between DHNN-EDA and

metaheuristic algorithms

The ITS, MA-MK, MST1-2, and the DHNN-EDA all can be seen as multi-start based methods. In general, these methods have two
phases: the solution construction phase in which the solution is generated and the solution improvement phase in which the solution is improved. Then, each global iteration produces a solution (usually local optima) and the best solution overall is the output of these algorithms (Marti', 2003). In the solution construction phase, a simple strategy, for example, random generation of start solution can be used. Similarly, a simple solution improvement method can be applied, for example, simple LS. Further, the solution improvement phase can be performed with a complex metaheuristic, for example, SA and TS.

In order to better understand the inner instrument of these algorithms concluding the ITS, MA-MK, MST1-2, and the DHNNEDA and the commonalities and differences among them, we first introduce a three-dimensional categorizing framework. Solution construction and solution improvement are considered as two dimensions in the framework. Under solution construction strategies, algorithms are categorized into constructive and perturbation based methods. Under solution improvement strategies, algorithms are categorized into simple LS and complex metaheuristic. We consider population or single point based strategy as a third dimension. This categorizing framework in this paper serves two roles. First, it reveals relationships among different algorithms. Second, it also reveals what are missing in the current combinations of different strategies and thus indicates potential new or improved algorithms with suitable combinations of different strategies in different dimension.

The ITS uses the computational trick designed for the UBQP in both solution perturbation (construction) and solution improvement phases. It is a single point, perturbation (perturbation GSP) and complex metaheuristic (metaheuristic STS) based algorithm. The MST1 and MST2 also use the computation trick in solution improvement phases. Further, the MST2 uses a constructive procedure to a projected problem in the solution construction phase. Therefore, the MST1 and MST2 are all single point, constructive method and complex metaheuristic-based algorithms. The MAMK uses an innovative variation (crossover operator) to construct or generate a population of offspring solutions, a diversification/restart strategy (mutation operator) to mutate or perturb each offspring, and the randomized $k$-opt LS to improve the offspring solutions at each generation. Obviously, the MA-MK is a popula-tion-based algorithm. The crossover operator can be seen as a constructive method and the mutation operator is obviously a

perturbation based method. Though randomized $k$-opt LS is not a metaheuristic methods, it is a more sophisticated LS. The innovative variation and randomized $k$-opt LS are all tailed for the UBQP. Thus, the MA-MK can be seen as a hybrid method. If the population size of the MA-MK is set to 1 , the MA-MK has no crossover operator and the mutation operator and randomized $k$-opt LS are fully used to generate new offspring. Thus it becomes to a single point, perturbation and LS based algorithm.

All the metaheuristic algorithms mentioned above use more sophisticated procedures specifically tailored for the UBQP. Misevcius, Smolinskas, \& Tomkevičius (2005) pointed out that such "tailored" algorithms, like the ITS, MSTI-2 and MA-MK, succeed in search if only they involve the specific problem knowledge. The algorithm designer must be very careful by implementing both the improvement and perturbation (construction) procedures. These procedures should be as much problem-oriented as possible. That is, these multi-started based algorithms are problem-dependent and the ideas and strategies implemented are difficult to apply directly to different problems.

In the DHNN-EDA, the solution construction phase is based on EDA, and the solution improvement phase is based on HNN, a kind of simple and general LS. It is a single point, perturbation and simple LS based algorithm. Thus, the DHNN-EDA is based on a simple and efficient framework that can be used directly to design solving methods for other combinatorial optimization problems, for example, the TPCNP in our previous work (Wang, 2008). In summary, the DHNN-EDA is based on a much simpler and more general-purpose approach. Note that it may be argued that the HNN is based on gradient descent and thus also uses the information from the problem structure implicitly. However, the network derives the gradient information of the problem in a general way described by the motion Eq. (4), which is not necessary to be designed specifically for different problems.

On the other hand, the motion equation of HNNs is based on gradient descent, but HNNs should not be viewed as naive gradient descent machines. They can be view as a machine which consist of large number of simple interconnected processing units and therefore, can implement complex computation task. Thus, the advantage of HNNs for combinatorial optimization problems is their inherently parallel structure and simple computational requirements and therefore, HNNs are suitable for direct hardware implementation using analogue or digital integrated circuit or optical computers (Dominguez \& Munoz, 2008; Huang \& Wang, 2003; Resende \& Werneck, 2004; Smitha et al., 2003). Considering the speed advantage, it is foreseeable that NNs will soon become a rapid solution technique for large and complex combinatorial optimization problems (Smitha et al., 2003).

Therefore, the DHNN-EDA has the advantages of inherently parallel structure and simple computational requirements. In some cases, the DHNN-EDA is not competitive with designer algorithms such as the ITS. Nevertheless, the above experimental results show that the DHNN-EDA can obtain good results within reasonable computation time.

### 4.7.5. Future research lines for further improvement of DHNN-EDA

From the experiments, it is clear that the DHNN-EDA is not the best algorithm for the UBQP. According to the three-dimensional categorizing framework discussed above, we can borrow some ideas from the competitors or other metaheuristic algorithms and invest more intellectual effort by the following ways to further improve the performance of the DHNN-EDA.

Firstly, adaptive perturbations. One possible method is to adopt the idea of the reactive search, which advocates the use of simple subsymbolic machine learning to automate the parameter tuning process and make it an integral part of the algorithm (Battiti \& Brunato, 2007). Another way of adapting the perturbation is to change
deterministically its strength during the search, just as done in variable neighborhood search (VNS) (Hansen \& Mladenovic, 2003).

Secondly, population-based DHNN-EDA extensions. In the population-based DHNN-EDA, EDA guides the search and a population of starting points are kept and used to run the HNN search. Thus, the population-based DHNN-EDA extensions share similarities to the MA. In general, population-based algorithms are more complex to use than single point based algorithms, and require mechanisms to manage a population of solutions. More importantly in the MA, it is necessary to design effective "crossover" operator for the combination of solutions in the population and effective "mutation" operator or other mechanisms to keep the diversity of the population, which, more often, is a challenge and key task. For example, a crossover operator, innovative variation, and a diversification/restart strategy in the MA-MK is specifically designed or tailored to obtain that performance of the algorithm for the first group benchmark instances. Further, one question arises is whether using a population of solutions is really helpful. At least, it is pointed out that the single point based search algorithm leads to good results for some problems such as TSP with high cost-distance correlations, and thus the advantage of population-based method is small or nil (Lourenço, Martin, \& Stützle, 2003). For some other problems, the population-based algorithms can achieve diversification in search process and thus are desirable if their complexity is not overwhelming. These problems can be carefully studied in detail in future research.

Finally, adaptive memory or mechanism to escape from local minima in the HNN descent. In the DHNN-EDA, the solution improvement phase is based on a simple HNN search. Inspired by the ITS and the randomized $k$-opt LS, the tabu mechanism (tabu list) explicitly using the history of the search can be incorporated into the HNN to further improve the performance of the DHNNEDA. Specifically, a tabu search rule, instead of the original updating rule described by Eqs. (4) and (5) in the DHNN, is used to govern the state transition of neurons to search for the global minimum of the energy function, and thus can help the network escape from local minima. It is a promising approach to introduce the tabu mechanism into the DHNN and propose a tabu NN with EDA algorithm. Thus, the short term memory of the tabu mechanism in the tabu NN cooperates with the long term memory mechanism in the EDA to improve the performance of the DHNN-EDA, which is just our ongoing work.

Note that ideas mentioned above can further improve the performance of the DHNN-EDA, but the modified DHNN-EDA with those ideas may become more and more sophisticated and thus run the risk of losing simplicity.

## 5. Conclusions

In this paper, we have presented a novel DHNN-EDA as a competitive approach for the UBQP. In the DHNN-EDA, the idea of EDA is incorporated into the DHNN in order to overcome the local minima problem of the DHNN. The perturbation based on the EDA in the DHNN-EDA can generate a new starting point for the DHNN for further search. Therefore, the DHNN-EDA can escape from local minima and further search better results. Simulation results on the UBQP show that the DHNN-EDA is better than the other improved HNN algorithms such as multi-start DHNN and DHNN with random flips, and is better or competitive with metaheuristic algorithms such as SA, TS, SS and MA. Further, we discuss the DHNN-EDA in the multi-start algorithm framework and clarify the similarities and differences between the DHNN-EDA and other metaheuristic algorithms. We also mention the TCNN and NCNN, and discuss the similarities and differences between the chaotic neural models and the DHNN-EDA. Based on these discussions,

we highlight the characteristics of the DHNN-EDA and propose some ways to further improve the performance of the DHNN-EDA.

In the future, several research lines can be followed. Firstly, the simulation results for the UBQP, together with the results for the TPChP (Wang, 2008), show that the DHNN-EDA is an efficient and robust combinatorial optimization framework and therefore, can be applied to other combinatorial optimization problems. Secondly, the perturbation based on EDA in the DHNN-EDA can be incorporated into other DHNN models, for example, competitive HNN (Galán-Marín, Mérida-Casermeiro, \& Muñoz-Pérez, 2003; Galán-Marín \& Muñoz-Pérez, 2001), hysteretic HNN (Xia, Tang, Li, \& Wang, 2005), and quantized HNN (Nourelfath \& Nahas, 2003), for solving different kinds of combinatorial optimization problems. Finally and most importantly, we will borrow some ideas from the competitors or other metaheuristic algorithms following the ways mentioned in the discussion section to further improve the performance of the DHNN-EDA.

## Acknowledgments

This work was supported in part by the National Natural Science Foundation of China (60805026, 60905038, 60873162), the Specialized Research Fund for the Doctoral Program of Higher Education (20070558052), and the Scientific Research Foundation for the Returned Overseas Chinese Scholars, State Education Ministry (2007-1108).
