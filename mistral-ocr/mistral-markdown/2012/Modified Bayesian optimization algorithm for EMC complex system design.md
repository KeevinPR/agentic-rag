# Modified Bayesian Optimization Algorithm for EMC Complex System Design 

Bui Van Ha ${ }^{01}$, M. M. Maglio ${ }^{\dagger 2}$, M. Mussetta ${ }^{03}$, P. Pirinoli ${ }^{* 4}$, R.E. Zich ${ }^{* 5}$<br>${ }^{1}$ Politecnico di Milano, Dipartimento di Energia<br>Via La Masa 34, 20156 Milano, Italy.<br>${ }^{1}$ ha.bui@mail.polimi.it<br>${ }^{2}$ marco.mussetta@polimi.it<br>${ }^{3}$ riccardo.zich@polimi.it<br>${ }^{4}$ Politecnico di Milano, Dipartimento di Elettrotecnica<br>Piazza L. da Vinci, 32 - 20133 Milano - Italy<br>${ }^{5}$ matteo.maglio@mail.polimi.it<br>* Politecnico di Torino, Dipartimento di Elettronica e Telecomunicazioni<br>C. Duca degli Abruzzi 24, 10129 Torino, Italy.<br>${ }^{6}$ paola.pirinoli@polito.it


#### Abstract

The design of real electrical, electronic or electromagnetic complex systems fulfilling EMC constrains often exploits the performances of population based global optimizers. One of the main drawbacks of the adoption of these optimizers in the design of a real system is the difficulty in the introduction, in the optimized design algorithm, of all the heuristic knowledge already available in the field. In order to overcome this problem Bayesian optimization algorithms, classified as estimation of distribution algorithm, could be very effective, since they are based on the definition of the distribution of promising solutions by using the information extracted from the entire set of currently good solutions. Unfortunately, their straightforward implementations usually lack of exploration, and are easily trapped in local maxima. In order to overcome even this drawback and to develop a Bayesian optimization algorithm with both the required exploitation, of the heuristic knowledge, and the exploration, for avoiding local maxima, for system or subsystem design fulfilling EMC constrains, in this paper a modified BOA is proposed by adding a suitable mutation scheme to the traditional one in order to ensure the effectiveness of the algorithm. The here proposed new algorithm has been tested on some mathematical test functions and on a typical EM design problem, a microwave microstrip filter synthesis, to show its capability.


## I. INTRODUCTION

The design of real electrical, electronic or electromagnetic complex systems fulfilling EMC constrains often exploits the performances of population based global optimizers, such as the classic Genetic Algorithms (GA) or Particle Swarm Optimization (PSO) and all the more recent developed ones such as MetaPSO, GSO, MetaLamarckians and so on. One of the main drawbacks of the adoption of these optimizers in the design of a real system is the difficulty in the introduction, in the optimized design algorithm, of all the heuristic knowledge already available in the field, and this is usually a big problem since the heuristic knowledge is often the core itself of the design team value. By the way, this is one of the main limits
in the spread of population based algorithm for complex system optimizations.

In order to overcome this problem, Bayesian optimization algorithms, classified as estimation of distribution algorithm, could be very effective, since they are based on the definition of the distribution of promising solutions by using the information exacted from the entire set of currently good solutions. Bayesian algorithms have been suitably developed exactly for overcoming this problem, since they are based on the "inductive" logical process, instead of the usual "deductive" one, aiming exactly to exploit at best all the heuristic knowledge that has been achieved on a particular problem.

Unfortunately, their straightforward implementations usually lack of exploration, since they attempt to build up a probabilistic model from the available knowledge, and may be easily trapped in local maxima lacking of what is usually called high level design prospective.

In order to overcome even this drawback and to develop a Bayesian optimization algorithm with both the required exploitation, of the heuristic knowledge, and the exploration, for avoiding local maxima, for system or subsystem design fulfilling EMC constrains, in this paper a modified BOA is proposed by adding a suitable mutation scheme, a typical GA operator, to the traditional one in order to ensure the effectiveness and the convergence of algorithm. The new algorithm in the following will be presented, discussed and tested both on purely mathematical and on EM design problem, e.g. a microwave microstrip filter synthesis.

## II. MODIFIED BAYESIAN OPTIMIZATION ALGORITHM

Bayesian Optimization Algorithm (BOA), first published in [1], uses Bayesian Networks (BN) to estimate the joint distribution of promising solutions. In the BOA, interaction between parameters (i.e. variables) are covered to build probabilistic model i.e. BN, also prior information and the set of promising solution are combined for estimating the

distribution. This estimation is then used to generate new candidates by sampling. A full treatment of the method can be found in [1-2], but for the sake of clarity and uniformity of notation it is briefly summarized in the following section.

The BOA starts with randomly generating a set of population i.e. set of strings. The current population is evaluated, and the best solutions are selected using selection method e.g. truncation selection or tournament selection. A Bayesian Network is then constructed to fit the selected set of strings. In building network process, a metric and a search method are used to measure and maximize the quality of network. New offspring is generated by sampling the distribution of best population modelled by BN. Finally, new population is added to the original population by replacement some worst ones. The next iteration proceeds again until stoping criteria are satisfied. The pseudo-code of the BOA follows:
(1) Randomly generate initial population $(\mathbf{P})$
(2) Select a set of promising solutions $(\mathbf{S})$ from $(\mathbf{P})$
(3) Construct the network $(\mathbf{B})$ using the chosen metric and constraints
(4) Generate a set of new offspring $(\mathbf{O})$ according to the joint distribution encoded by $\mathbf{B}$
(5) Create a new population $\left(\mathbf{P}^{*}\right)$ by replacing some instances from $(\mathbf{P})$ with $(\mathbf{O})$
(6) If the termination criteria are not met, go to (2)

In the BOA, creating Bayesian Networks and generating offspring are the two most important steps, which will be described detail in this section.

## A. Bayesian Networks

Bayesian Networks - BNs [3] are graphical models that combine probabilistic theory with graph theory to encode the relationship between variables contained in the modelled data. BNs are described by their structures i.e. directed acyclic graph and corresponding parameters. In the graph, each node represents one variable of modelled data, and the edges between these nodes correspond to conditional dependencies. The parameters are represented by the conditional probabilities for each variable given any instance of variables that this variable depends on. Mathematically, a BN encodes the joint probabilistic distribution:

$$
p(\mathbf{C})=\prod_{i=1}^{n} p\left(X_{i} \mid \pi_{i}\right)
$$

Where $\mathrm{X}=\left(X_{0}, X_{0}, \ldots, X_{k}\right)$ is the vector of variable of problem, $\pi_{i}$ is the set of parents of variable $X_{i}$, and $p\left(X_{i} \mid \pi_{i}\right)$ is the conditional probability of $X_{i}$ conditioned on the variables $\pi_{i}$.

In BOA, both structure and parameters of BN are learned in order to best fit the promising solution. There are two basic components of the algorithm for learning BN: scoring metric and search procedure. The scoring metric quantifies the quality of the given network. Prior knowledge about the problem can be incorporated into the metric as well. The
search engine is used to explore the space of all possible networks in order to maximize the value of scoring metric as high as possible. The exploration is usually restricted by problem constraints i.e. maximum number of incoming edge to one node. This number directly influences the complexity of algorithm for constructing network, and generating offspring. In this work, we use K2 as scoring metric [4] and greedy algorithm as search procedure. The next section will explain how to generate new offspring using distribution extracted from constructed network.

## B. Generating offspring

Once the structure and parameters of BN have been learned, new offspring will be generated by sampling the learned network. The procedure proceeds in two steps: ordering nodes and sampling variable according to the order.

In the first step, an order of nodes, where each node is preceded by it parents, is computed. The purpose of this order is to generate variable in a certain sequence so that the value of parents of one node are generated prior to the generation of the node itself. The second step samples all variables according to the computed ordering. Following the ancestral ordering, given values of parents of a variable, the distribution of this variable is computed by the corresponding conditional probability, and new value is generated according to this distribution.

## C. Modified BOA

As described above, BOA performance greatly depends on distribution of current good solutions. However, initial population for BOA is randomly generated; there would be some cases when all best solutions would not provide good enough distribution about problem, thus the algorithm hardly converges. To overcome this difficulty, one possibility is to increase the population size; therefore it will increase the quality of distribution of good solution. However, this solution will be time consuming, i.e. evaluating all population and offspring. In this paper, we propose a new approach by adding mutation to traditional BOA.

By adding mutation, some individual will be used to discover space out of distribution of good ones; therefore, the algorithm will avoid being trapped at local optimum. This is similar to Genetic Algorithms (GA) [5], Population Based Incremental Learning (PBIL) [6], and Compact Genetic Algorithm (CGA) [7], which use mutation as one of most important operator for exploring problem space. However, in proposed algorithm, we use Bayesian Network to represent probability model and generate new offspring. Moreover, we work with variable vector, which is more preferred for realvariable problem as microwave, instead of probability vector as PBIL and CGA. In our work, we implement BOA with tournament selection and individual mutation for design microwave filters.

## III. TEST PROBLEMS

In this paper, we present result of modified BOA for Onemax problem as mathematical test function and then apply

for filter synthesis. For all test problems, 30 independent runs are performed and the results showed here are averaged values.

## A. Onemax problem

Onemax problem is defined as sum of bits in the input binary string. The optimal solution of Onemax is the string of all ones.

## B. Microwave filter design

The described algorithm is applied to design of a symmetric micro strip band-pass filter, consisting in a cascade of $2 P-1$ lines, each of which with electrical length equal to $\lambda_{e} / 2$ at the central frequency (being $\lambda_{c}$ the guided wavelength, given by $\lambda_{n} / \varepsilon_{c p}$, where $\varepsilon_{c p}$ is the effective permittivity, related to the relative permittivity of the substrate $\varepsilon_{r}$ and $\lambda_{n}$ is the freespace wavelength), but different width. In the present case, the layout of the filter, an example of which is shown in Fig. 1 for $P=2$, is printed on a single layer dielectric characterized by the relative dielectric constant of $\varepsilon_{r}=3.5$, and thickness $h=1.58 \mathrm{~mm}$. The lines are disposed symmetrically with respect to the central one.
![img-0.jpeg](img-0.jpeg)

Fig.1. Geometry of a $\mathrm{N}=2$ filter
The filter can be easily modeled with its transmission line equivalent model, i.e. with a cascade of $2 P-1$ transmission lines, having all the same electrical length ( $\lambda_{e} / 2$ ), but different characteristic impedance $Z_{i}$, since this latter quantity depends on the line width $w_{i}$. The filter can be therefore seen as a sequence of two-port networks, each of which can be represented by its chain matrix [8], whose entries depend only on the characteristic impedance and on the electric length. The chain matrix of the entire structure is given by the product of $2 P-1$ single chain matrices and the transmission coefficient (i.e. the transfer function) of the filter is expressed in terms of the entries of the chain matrix of the whole structure:

$$
S_{21}=\frac{2 \sqrt{Z_{o u t} / Z_{i n}}}{A_{e n}+B_{e n} / Z_{i n}+\left(Z_{o u t} / Z_{i n}\right)\left(C_{e n} Z_{i n}+D_{e n}\right)}
$$

where $Z_{\text {out }}, Z_{\text {in }}$ are the reference impedances at the output and input ports of the filter, respectively.

The performances of the filter depend on the number of lines used for its realization (the greater is $P$, the larger is the bandwidth, but also the longer the filter is), and on the values
of the characteristic impedance of the equivalent transmission lines. Here $P$ is fixed and the filter widths $w_{i}$ are optimized, with the BOA. The design constraints are:

- the bandwidth, that has to be equal or greater than a fixed value;
- minimization of the in-band ripple;
- $\quad$ maximization of the out of band rejection.


## IV. NUMERICAL RESULTS

In this section, we present results of modified BOA for above mentioned problems. Figure 2 shows the behaviour of MBOA for Onemax with the problem's size varying from 100 to 500 bits. It reports the number of fitness evaluations until MBOA finds the optimum solution. The number of evaluated functions can be approximated by $O(n \log (n))$. The results indicate that Modified BOA can solve Onemax with an almost linear number of evaluations.
![img-1.jpeg](img-1.jpeg)

Fig.2. Number of fitness evaluation of Modified BOA for Onemax problem
![img-2.jpeg](img-2.jpeg)

Fig.3. Transfer function for 17 cells filter
In the design microwave filter, we consider all variables are independent. Even if this model does not take into account the interactions between the different lines, it represents a good compromise between the accuracy in modelling the filter and

the low computational cost that is a very important aspect when optimization tools as the BOA is used. Figure 3 shows transfer function of microwave filter consisting 17 piece lines $(\mathrm{P}=9)$. The design satisfies $60 \%-3 \mathrm{~dB}$ bandwidth required, with in-band ripple less than $-3 \mathrm{~dB}$.

The preliminary result indicates good performance of proposed algorithm. The results promise a wide application of Modified BOA into real difficult EMC designs.

## REFERENCES

[1] M. Pelikan, D. E. Goldberg, and E. Cant-Paz, "BOA: The Bayesian Optimization Algorithm", proceedings of Genetics and Evolutionary Computation Conferences GECCO-99, W. Banzhaf et al., Eds. San Francisco, CA: Morgan Kaufmann, 1999, pp. 525-532.
[2] M. Pelikan, Hierarchical Bayesian Optimization Algorithm: Toward a New Generation of Evolutionary Algorithms, Springer, 2005.
[3] J.Pearl, Probabilistic reasoning in intelligent systems: Networks of Plausible inference. San matoo, CA: Morgan Kaufmann, 1988.
[4] D. Heckerman, D. Geiger, and D. M. Chickering, "Learning Bayesian networks: The combination of knowledge and statistical data," Microsoft Research, Redmond, WA, Technical Report MSR-TR-9409,1994.
[5] Goldberg D. E. "Genetic Algorithms in search, optimization and machine learning", Addison-Wiley, 1989.
[6] Bluja, S. "Population base incremental learning: A method for integrating genetic search based function optimization and competitive learning", Carnegie Mellon University, Pittsburgh, Pennsylvania, Technical Report No. CMUCS-94-163, 1994.
[7] Harik, G. R., Lobo, F.G. and Goldberg D. E. "the compact genetic algorithm", proceedings of the IEEE Conference on Evolutionary Computation, 1998, pp. 523-528.
[8] P.C. Magnusson, G.C. Alexander, V.K. Tripathi, Transmission lines and wave propagation, 3rd ed., Boca Raton : CRC Press, 1992