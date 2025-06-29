# Improved Compact Genetic Algorithm for EM Complex System Design 

Bui Van Ha*, R.E. Zich*, M. Mussetta*, Paola Pirinoli*, Chien Ngoc Dao ${ }^{\#}$<br>*Politecnico di Milano, Dipartimento di Energia, Milano, Italy<br>Email: ha.bui@mail.polimi.it, riccardo.zich@polimi.it, marco.mussetta@polimi.it<br>${ }^{*}$ Politecnico di Torino, Dipartimento di Elettronica e Telecomunicazioni, Torino, Italy<br>Email: paola.pirinoli@polito.it<br>${ }^{\#}$ Hanoi University of Science and Technology, Ha Noi, Viet Nam<br>Email: chiendn-fet@mail.hut.edu.vn


#### Abstract

Nowadays the design of complex real electrical, electronic or electromagnetic systems may effectively exploit the characteristics of population based global optimizers. One of the main drawbacks of the adoption of these optimizers in the design of a real system is the difficulty in the introduction, in the optimized design algorithm, of all the heuristic knowledge already available in the field. In order to overcome this problem compact genetic algorithms, classified as estimation of distribution algorithm, could be very effective, since they apply and manipulate a suitable probability vector to represent the distribution of good solutions. Unfortunately, their straightforward implementations usually lack of exploration, and they are easily trapped in local maxima. In order to overcome even this drawback and to develop a compact genetic algorithm with both the required exploitation, of the heuristic knowledge, and the exploration, for avoiding local maxima, in this paper a modified cGA is proposed by implementing more probability vectors and adding a suitable learning scheme to the traditional one in order to ensure the effectiveness of the algorithm. The here proposed new algorithm has been tested on some mathematical test functions and on a typical EM design problem, a microwave microstrip filter synthesis.


Keywords-compact genetic algorithm

## I. INTRODUCTION

Nowadays the design of complex real electrical, electronic or electromagnetic systems may effectively exploit the characteristics of population based global optimizers, such as the classic Genetic Algorithms (GA) or Particle Swarm Optimization (PSO) and all the more recent developed ones such as MetaPSO, GSO, MetaLamarckians and so on. One of the main drawbacks of the adoption of these optimizers in the design of a real system is the difficulty in the introduction, in the optimized design algorithm, of all the heuristic knowledge already available in the field, and this is usually a big problem since the heuristic knowledge is often the core itself of the design team value. By the way, this is one of the main limits in the spread of population based algorithm for complex system optimizations.

In order to overcome this problem, compact genetic algorithm, classified as estimation of distribution algorithm, could be very effective, since they are based on the definition
of the distribution of promising solutions. Compact genetic algorithms have been suitably developed for overcoming this problem, since they introduce a suitable probability vector to represent the population, aiming exactly to exploit at best all the heuristic knowledge that has been achieved on a particular problem.

Unfortunately, their straightforward implementations usually lack of exploration, since they attempt to manipulate a probabilistic vector from the available knowledge, and may be easily trapped in local maxima lacking of what is usually called high level design prospective. In order to overcome even this drawback and to develop a compact genetic algorithm with both the required exploitation, of the heuristic knowledge, and the exploration, for avoiding local maxima, in this paper a modified cGA is proposed by implementing more than one probability vector and adding a suitable learning scheme to the traditional one in order to ensure the effectiveness and the convergence of algorithm. The new algorithm in the following will be presented, discussed and tested both on purely mathematical and on an EM design problem, e.g. a microwave microstrip filter synthesis.

## II. COMPACT GENETIC ALGORITHM - CGA

## A. Compact Genetic Algorithm

Compact Genetic Algorithm - cGA, first presented in [1], uses probability vector (PV) to represent a possible solution. In cGA, instead of using real population as in traditional Genetic Algorithm, it manages PV to get the distribution of good solutions. The length of PV corresponds to the number of variables of problem, and the value of PV measures the probability of one variable to get particular value e.g. the proportion of " 1 " in case of binary problem. A full treatment of the method can be found in [1-2], but for the sake of clarity and uniformity of notation it is briefly summarized in the following section.

The pseudo code of cGA is described in Fig.1. Initially, the PV is assigned a value of 0.5 i.e. assuming uniform distribution for every position. In each generation, two individuals are generated from current PV. They are left to compete, and the winner will be responsible for updating the PV. The updating rule will increase or decrease probability vector by a factor $1 / n$ (n-population size) according to the value of the winner. The

cGA will stop when PV has value of 0 or 1 at all positions i.e. finding optimal solution.

1) Initialize probability vector for $\mathrm{i}:=1$ to 1 do $\mathrm{p}[\mathrm{i}]:=0.5$;
2) Generate two individual from the vector
$\mathrm{a}:=$ generate(p);
$\mathrm{b}:=$ generate(p);
3) Let them compete
winner, loser: = evaluate(a,b);
4) Update the probability vector towards the better one for $\mathrm{i}:=1$ to 1 do
if winner[i] \# loser[i] then
if winner $[\mathrm{i}]=1$ then $\mathrm{p}[\mathrm{i}]:=\mathrm{p}[\mathrm{i}]+1 / \mathrm{n}$;
else $\mathrm{p}[\mathrm{i}]:=\mathrm{p}[\mathrm{i}]-1 / \mathrm{n}$;
5) Check if the vector has converged for $\mathrm{i}:=1$ to 1 do
if $\mathrm{p}[\mathrm{i}]=0$ and $\mathrm{p}[\mathrm{i}]<1$ then
return to step 2;
6) $p$ presents the final solution
cGA parameter:
n : population size
1 : chromosome length

Fig. 1: pseudo code of cGA

## B. Improved performance of Compact Genetic Algorithm

The cGA works well when problems consist of nonoverlapping Building Blocks ( BBs ), or low order behavior, but it fails when dealing with higher order BBs. To overcome this limitation, Harik [1] introduced a modification of cGA by increasing the number of generated offspring and applying tournament competition i.e. simulating higher selection pressure. This allows the cGA to solve the problem with higher order BBs. However, the modification has a drawback of computational cost since it needs to store and evaluate a considerable number of individuals.

In [2], Chang Wook Ahn proposed new versions of cGA introducing elitism. He created two different mechanisms: persistent elitism cGA (pe-cGA) and non-persistent elitism cGA (ne-cGA). The elitism-based cGAs outperform the original cGA in term of function evaluations. The reason for this is that the elitism can prevent the loss of low salience genes of chromosomes which is equivalent to increase the selection pressure. Unfortunately, pe-cGA and ne-cGA couldn't perform better in term of solution quality, while they have only the advantage of consuming less memory than all cGAs.

In all above mentioned modifications, the authors attempted to manipulate one probability vector in different ways in order to speed up the algorithm convergence. However, their performances decrease when the order of complexity of the problem increases.

In this paper, we propose a further effort to improve the cGA algorithm effectiveness by simultaneously dealing with more probability vectors. The idea is that using more than one PV enhances the exploration properties of the algorithm, and this will increase the ability to avoid local trapping dealing
with high-order BBs. Moreover, the incorporation mechanism of the information from different PVs may also enhance the exploitation itself of the algorithm speeding up the convergence.

The proposed algorithm, since deals with more PVs, needs a completely new updating rule in order to manage effectively all the PVs. The new rules are described in Fig.2, where a suitable learning scheme that allows PVs to learn from each other is introduced. Therefore, in this way, in the updating process, the PVs will be not only updated by their generated individuals, but also by the best PV at current iteration. Furthermore, the non-persistent elitism cGA has been introduced in our algorithm.

```
Initialize probability vectors
    for \(\mathrm{i}:=1\) to P
    for \(\mathrm{j}:=1\) to 1 do \(\mathrm{p}[i][\mathrm{j}]:=0.5\);
    Generate two individual from each vector
    for \(\mathrm{i}:=1\) to P
    if the first generation
        \(\operatorname{coun}[\mathrm{i}]:=0 ;{ }^{*}\) control parameter*/
            \(\mathrm{E} \_\)chrom[i]: = generate(p[i]);
    N_chrom[i]: = generate(p[i]);
3) Let them compete in small group
    for \(\mathrm{i}:=1\) to P
    winner[i], loser[i]: = evaluate(E_chrom[i], N_chrom[i]);
        if \(\operatorname{coun}[\mathrm{i}] \leq \eta \& \operatorname{winner}[\mathrm{i}]=\mathrm{E} \_\)chrom[i]
            \(\operatorname{coun}[\mathrm{i}]++;\)
            E_chrom[i] = winner $[\mathrm{i}] ;$
        else
            E_chrom[i]: = generate(prob[i] \(=0.5\) )
4) Update the probability vectors towards the better one
    \% local update
    for \(\mathrm{i}:=1\) to P
    for \(\mathrm{j}:=1\) to 1 do
    if winner[i][j] \# loser[i][j] then
        if winner[i][j] \(=1\) then \(\mathrm{p}[i][\mathrm{j}]:=\mathrm{p}[i][\mathrm{j}]+1 / \mathrm{n}\);
                else \(\mathrm{p}[i][\mathrm{j}]:=\mathrm{p}[i][\mathrm{j}]-1 / \mathrm{n}\);
            \% global update
            global_best = compete(winner[1:P]);
        for \(\mathrm{i}:=1\) to P
        \(\mathrm{p}[\mathrm{i}]=\mathrm{p}[\mathrm{i}]+\mathrm{c}^{*}\) (global_best \(=\mathrm{p}[\mathrm{i}]\) );
        \(* \mathrm{c}:\) learning factor \(* /\)
```

Parameter:
n : population size
P: number of PVs
$\mathrm{l}:$ chromosome length
$\eta$ : length of inheritance

Fig. 2: Modification of cGA implementing more PVs

## III. NUMERICAL RESULTS

In this section the numerical results obtained with the proposed algorithm are reported. The results are compared with the one obtained on the same problem with different cGAs ancestors both in terms of the obtained solution quality and in terms of the required numerical effort. In order to consider a reasonable statistics over the intrinsic stochasticity of these approaches, all the numerical results have been averaged over 50 runs. The proposed algorithm, denoted as "new", in the here presented results uses two probability vectors, while the length of inheritance of non-persistent elitism is equal to $10 \%$ of population size.

## A. Results for the problems involving high order BBs

The first mathematical test function with high order BBs that has been considered is the Minimum Deceptive Problem, MDP, consisting in concatenating ten copies of minimum deceptive function i.e. 2 bits. A MDP is defined by:
$f_{M D P}=\sum_{1}^{10} f\left(x_{2 i}\right)$ where $f\left(x_{2 i}\right)=\left\{\begin{array}{l}0.7 \text { if } x_{2 i}=00 \\ 0.4 \text { if } x_{2 i}=01 \\ 0.0 \text { if } x_{2 i}=10 \\ 1.0 \text { if } x_{2 i}=11\end{array}\right.$
Here, $x_{2 i}$ presents the values of a 2-bit long substring i.e. BBs.
![img-0.jpeg](img-0.jpeg)

Fig.3. Performance of the algorithms on MDP problem. (a) Number of correct BBs versus population size. (b) Number of correct BBs versus number of function evaluations.

Fig. 3 (a) and (b) report the quality of solution and speed of convergence of all cGAs the MDP with 10 BBs is considered. With low order problems the new algorithm is close to the cGA performances in terms of population size, while, as shown in Fig. 3(b) reporting the comparison of the quality of the solution in terms of the number of function evaluations, the new algorithm outperforms cGA, pe-cGA, and ne-cGA.

Fully deceptive problems [3] have been then considered for testing the proposed algorithm. The problems involving trap functions are ideal cases for testing the capability to deal with high order BBs. A simple 3-deceptive problem, formed by concatenating ten copies of the three bits trap function has been considered, each three bits trap function has deceptive to optimal ratio of 0.7 as defined below:

$$
\begin{gathered}
f_{3-b i t}=\sum_{1}^{10} f\left(x_{3-b i t}\right) \\
\text { where } f\left(x_{3-b i t}\right)=\left\{\begin{array}{l}
0.7 \text { if sum }(3 b i t)=0 \\
0.4 \text { if sum }(3 b i t)=1 \\
0.0 \text { if sum }(3 b i t)=2 \\
1.0 \text { if sum }(3 b i t)=3
\end{array}\right.
\end{gathered}
$$

![img-1.jpeg](img-1.jpeg)

Fig.4. Performance of different algorithms on 3-deceptive problem. (a) Number of correct BBs vs. population size. (b) Number of correct BBs vs. number of function evaluations.

In Fig. 4(a), the cGA fail to solve the problem, while the performance of pe-cGA and ne-cGA can be considered close to the one of cGA with high selection pressure $\mathrm{s}=8$ and $\mathrm{s}=16$

respectively. The proposed algorithm generally shows better performances to achieve best solutions both in term of quality of solution vs. population size and vs. function evaluations.

## B. Results for continuous real problem

The proposed algorithm has been applied to design a symmetric micro strip band-pass filter, consisting in a cascade of $2 P-1$ lines, each of which with electrical length equal to $\lambda_{g} / 2$ at the central frequency (being $\lambda_{g}$ the guided wavelength, given by $\lambda_{h} / \varepsilon_{o f f}$, where $\varepsilon_{o f f}$ is the effective permittivity, related to the relative permittivity of the substrate $\varepsilon_{s}$ and $\lambda_{h}$ is the free-space wavelength), but different width. In the present case, the layout of the filter, an example of which is shown in Fig. 5 for $P=2$, is printed on a single layer dielectric characterized by the relative dielectric constant of $\varepsilon_{r}=3.5$, and thickness $h=1.58 \mathrm{~mm}$. The lines are disposed symmetrically with respect to the central one.
![img-2.jpeg](img-2.jpeg)

Figure 5: Geometry of a $\mathrm{N}=2$ filter
The filter can be easily modeled with its transmission line equivalent model, i.e. with a cascade of $2 P-1$ transmission lines, having all the same electrical length ( $\lambda_{g} / 2$ ), but different characteristic impedance $Z_{i}$, since this latter quantity depends on the line width $w_{i}$. The filter can be therefore seen as a sequence of two-port networks, each of which can be represented by its chain matrix [4], whose entries depend only on the characteristic impedance and on the electric length. The chain matrix of the entire structure is given by the product of $2 P-1$ single chain matrices and the transmission coefficient (i.e. the transfer function) of the filter is expressed in terms of the entries of the chain matrix of the whole structure:

$$
S_{21}=\frac{2 \sqrt{Z_{\text {out }} / Z_{\text {in }}}}{A_{n o t}+B_{n o t} / Z_{\text {in }}+\left(Z_{\text {out }} / Z_{\text {in }}\right)\left(C_{n o t} Z_{\text {in }}+D_{n o t}\right)}
$$

where $Z_{\text {out }}, Z_{\text {in }}$ are the reference impedances at the output and input ports of the filter, respectively.

The performances of the filter depend on the number of lines used for its realization (the greater is $P$, the larger is the bandwidth, but also the longer the filter is), and on the values of the characteristic impedance of the equivalent transmission
lines. Here $P$ is fixed and the filter widths $w_{i}$ are optimized with the modified cGA. The design constraints are:

- the bandwidth, that has to be equal or greater than a fixed value;
- minimization of the in-band ripple;
- $\quad$ maximization of the out of band rejection.

Even if the model does not take into account the interactions between the different lines, it represents a good compromise between the accuracy in modeling the filter and the low computational cost that is a very important aspect when optimization tools as the modified cGA is used.

Fig. 6 shows the transfer function of the microwave filter consisting in 17 piece lines $(\mathrm{P}=9)$. The design satisfies $60 \%$ 3 dB bandwidth required, with in-band ripple less than -3 dB .
![img-3.jpeg](img-3.jpeg)

Fig.6. Transfer function for 17 cells filters

## IV. CONCLUSION

The preliminary results reveal good performances of proposed algorithm both with high order BBs and continuous optimization problem. The results also promise a wide application of modified cGA into real difficult EM problems.
