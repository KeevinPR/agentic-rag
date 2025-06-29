# An improved Estimation of Distribution Algorithm for Solving Constrained Mixed-Integer Nonlinear Programming Problems 

$1^{\text {st }}$ Daniel Molina Pérez CIDETEC<br>Instituto Politécnico Nacional<br>Ciudad de México, México<br>dmolinap1800@alumno.ipn.mx

$2^{\text {nd }}$ Edgar Alfredo Portilla-Flores
UPIIT
Instituto Politécnico Nacional
Tlaxcala, México
aportilla@ipn.mx

3 ${ }^{\text {rd }}$ Efrén Mezura-Montes<br>Artificial Intelligence Research Center<br>University of Veracruz<br>Veracruz, México<br>emezura@uv.mx

$4^{\text {th }}$ Eduardo Vega-Alvarado CIDETEC<br>Instituto Politécnico Nacional<br>Ciudad de México, México<br>evega@ipn.mx


#### Abstract

In a mixed-integer nonlinear programming problem, integer restrictions divide the feasible region into discontinuous feasible parts with different sizes. Evolutionary Algorithms (EAs) are usually vulnerable to being trapped in larger discontinuous feasible parts. In this work, an improved version of an Estimation of Distribution Algorithm (EDA) is developed, where two new operations are proposed. The first one establishes a link between the learning-based histogram model and the $\varepsilon$-constrained method. Here, the constraint violation level of the $\varepsilon$-constrained method is used to explore the smaller discontinuous parts and form a better statistical model. The second operation is the hybridization of the EDA with a mutation operator to generate offspring from both the global distribution information and the parent information. A benchmark is used to test the performance of the improved proposal. The results indicated that the proposed approach shows a better performance against other tested EAs. This new proposal solves to a great extent the influence of the larger discontinuous feasible parts, and improve the local refinement of the real variables.

Index Terms-estimation of distribution algorithm, evolutionary algorithms, integer restriction handling, mixed integer nonlinear programming.


## I. INTRODUCTION

A large number of engineering optimization problems fall into the category of Mixed-Integer Nonlinear Programming (MINLP) [1], that addresses nonlinear problems including continuous, integer and/or discrete variables. The mathematical model of a MINLP problem can be defined by (1):

$$
\begin{array}{ll}
\operatorname{minimize} & f(\mathbf{x}, \mathbf{y}) \\
\text { subject to: } & g_{i}(\mathbf{x}, \mathbf{y}) \leq 0, \quad i=1, \ldots, n \\
h_{j}(\mathbf{x}, \mathbf{y})=0, & j=1, \ldots, m \\
x_{k}^{l b} \leq x_{k} \leq x_{k}^{u b}, & k=1, \ldots, n_{1} \\
y_{q}^{l b} \leq y_{q} \leq y_{q}^{u b}: & \text { integer, } q=1, \ldots, m_{1} \\
{[\mathbf{x}, \mathbf{y}] \in \Omega} & \\
&
\end{array}
$$

where $f(\mathbf{x}, \mathbf{y})$ is the objective function, $\mathbf{x}$ is a vector of continuous variables, $\mathbf{y}$ is a vector of integer variables, $x_{k}^{l b}$ and $x_{k}^{u b}$ are the lower and upper bounds of $x_{k}$, respectively, $y_{q}^{l b}$ and $y_{q}^{u b}$ are the lower and upper bounds of $y_{q}$, respectively, $\Omega$ is the decision variable space, $g_{i}(\mathbf{x}, \mathbf{y})$ is the $i$ th inequality constraint, and $h_{j}(\mathbf{x}, \mathbf{y})$ is the $j$ th equality constraint.

In a MINLP problem, the constraints define the feasible region, whereas the integer restrictions divide the feasible region into discontinuous feasible parts with different sizes [2]. This fact is shown in Fig. 1, where $x$ is a continuous variable, and $y$ is an integer variable. The shaded area is the feasible region defined by the constraints, and the red lines are the discontinuous feasible parts that also satisfy the integer restrictions.

Diverse classical methods (branch and bound, cutting planes, outer approximation, among others) have been widely used to solve MINLP problems [3]. However, in the case of non-convex problems, these techniques may cut-off the global optima. Even for large-scale problems the generated tree may be arbitrarily large and the solution time particularly high. [4]. Consequently, stochastic methods such as Evolutionary Algorithms (EAs) have been modified to solve MINLP problems. For this purpose, several integer-handling strategies have been implemented in EAs [5]-[10]. However, these extended algorithms are usually vulnerable to the size of the discontinuous feasible parts. That is, the population tends to enter into the larger discontinuous parts, because the algorithm finds feasible solutions more easily in such regions [2]. As a consequence, the small parts remain poorly explored or ignored. Therefore, if the best known solution is located in a smaller part, the algorithm may converge to the wrong part and get trapped in a local optimal solution.

Estimation of Distribution Algorithms (EDAs) are stochastic optimization techniques that explore the search space by

![img-0.jpeg](img-0.jpeg)

Fig. 1. The shaded area represents the feasible region defined by constraints, the red lines are the discontinuous feasible parts that also satisfy the integer restrictions.
sampling probabilistic models. The new offspring is generated from the most promising regions detected by the model. EDAs have been proposed for solving MINLP problems [11], [12]. According to [13], EDAs are considered EAs paradigms, because they do not use crossover and mutation operators as in traditional EAs. In [10], [14], EDA operators have been used in the Particle Swarm Optimization algorithm (PSO) and a surrogate model to solve MINLP problems.

However, the operators used by EDAs to handle discrete variables may also be vulnerable to being trapped in the larger discontinuous feasible parts, as is demonstrated in this work. On the other hand, it is important to note that the offspring generated by the crossover or mutation operators may be close to the parents, whereas EDAs use global statistical information and cannot directly control the similarity between offspring and parents. For such reason, EDAs are very effective in finding promising areas, but not in the local refinement of real values. In order to cover this deficiency, many real-valued EDAs have been combined with classical EAs, local search algorithms, and even with crossover and mutation operators [13], [15].
$E D A_{\text {mon }}$ was initially proposed to solve a Mixed-Variable Newsvendor problem [12]. This work presents an improved version of $E D A_{\text {mon }}$, namely $E D A_{m v}$. The objective is to achieve a better performance when solving MINLP problems, considering the quality of the solution and the computational cost of the algorithm. Two modifications of the original algorithm are proposed, aimed at solving (i) the influence of the larger discontinuous feasible parts in the algorithm (ii) the drawbacks of EDAs in the local refinement of the real values. A benchmark was used to compare the performance between the improved proposal and two other EAs reported in the literature (including the original algorithm). The results show that the performance of $E D A_{m v}$ is better than the other tested EAs. This new proposal solves to a great extent the influence of the larger discontinuous feasible parts in algorithm behavior, and the drawbacks of $E D A_{\text {mon }}$ in the local refinement in the continuous search space.

## II. Estimation of Distribution Algorithm

$E D A_{\text {mon }}$ uses an Adaptive-Width Histogram (AWH) model for handling continuous variables, and a LearningBased Histogram (LBH) model for handling discrete variables. New variable values are generated from the statistical population (statistical sample). The best $N$ solutions selected from the offspring and the parent solutions compose the population of the next iteration. Despite the fact that in [12] the authors propose a strategy to generate the feasible initial population, in this work both $E D A_{\text {mon }}$ and the proposed $E D A_{m v}$ generate the initial population randomly between the bounded ranges. Discrete variables begin with random discrete values.

## A. Adaptive-width histogram model

The AWH model promotes promising areas by assigning them high probabilities, while the rest of them are assigned very low probability to prevent premature convergence. One AWH is developed for each decision variable independently (univariate models). The search space $\left[a_{i}, b_{i}\right]$ of the $i$ th variable $x_{i}$ is divided into $(W+2)$ bins (regions), to built the distribution model $P r_{i}^{c}$ for the AWH model. Points $\left[p_{i, 0}, p_{i, 1}, \ldots, p_{i, w+1}, p_{i, w+2}\right]$ are the limits of the bins (Fig. 2), where $p_{i, 0}=a_{i}$ and $p_{i, w+2}=b_{i}$ ( $x_{i}$ lower and upper bounds, respectively). The total number of bins is $(W+2)$ but the input parameter for $E D A_{\text {mon }}$ is $W$. However, the algorithm creates two more bins: one between the lower boundary $a_{i}$ and the point $p_{i, 1}$, and another between the point $p_{i, w+1}$ and the upper boundary $b_{i}$, to avoid premature convergence. Considering that $x_{i, \min }^{1}$ and $x_{i, \min }^{2}$ are the smallest and the second smallest existing values of variable $x_{i}$, respectively, and $x_{i, \max }^{1}$ and $x_{i, \max }^{2}$ are the highest and the second highest existing values of variable $x_{i}$, respectively, points $p_{i, 1}$ and $p_{i, w+1}$ are defined in (2) and (3):

$$
\begin{aligned}
p_{i, 1} & =\max \left\{x_{i, \min }^{1}-0.5\left(x_{i, \min }^{2}-x_{i, \min }^{1}\right), p_{i, 0}\right\} \\
p_{i, w+1} & =\min \left\{x_{i, \max }^{1}+0.5\left(x_{i, \max }^{1}-x_{i, \max }^{2}\right), p_{i, w+2}\right\}
\end{aligned}
$$

The $W$ bins of the promising areas are located in the range $\left[p_{i, 1}, p_{i, w+1}\right]$, and have the same width $b$, given by (4):

$$
b=\frac{\left(p_{i, w+1}-p_{i, 1}\right)}{W}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. Progression of the AWH model for $W=3$. (a) first generations, (b) later generations.

Let $A_{i, j}$ be the count of individuals for the $i$ th variable located in the $j$ th bin. As can be seen in Fig. 2, the end bins do not contain points (unpromising areas), then the values $A_{i, 1}=A_{i, W+2}=0$. However, a small value will be assigned through the input parameter $e_{b}$ to avoid premature convergence. Therefore, $A_{i, j}$ is obtained from (5):

$$
A_{i, j}= \begin{cases}A_{i, j}, & \text { if } 2 \leq j \leq(W+1) \\ e_{b}, & \text { if } j=1,(W+2), \text { and } p_{i, j}>p_{i, j-1} \\ 0, & \text { if } j=1,(W+2), \text { and } p_{i, j}=p_{i, j-1}\end{cases}
$$

Note that the first case in (5) is the bins count of the promising areas $\left[p_{i, 1}, p_{i, w+1}\right]$. The second case assigns the value $e_{b}$ to the end bins. The third case assigns zero to the end bins with empty range. Finally, the probability of the $i$ th variable in the $j$ th bin, could be approximated by (6):

$$
\operatorname{Pr}_{i, j}^{c}=\frac{A_{i, j}}{\sum_{k=1}^{W+2} A_{i, k}}
$$

Fig. 2 shows how the promising area becomes very small in advanced stages of the search process. In that case, the algorithm focuses on exploitation. However, the end bins guarantee that the rest of the search space maintains an exploration behavior, which helps to avoiding premature convergence.

## B. Learning-based histogram model

In [12], the LBH model is proposed for handling integer variables. The variable $x_{m}$ has $v$ available integer values, with $v \in\left\{l b_{m}, l b_{m}+1, l b_{m}+2, \ldots, u b_{m}\right\}$. Regarding discrete values the same process is applied, but encoding the variables indexes instead of their values. In this model, the probability of the $n$th available value of $v$ is defined as $\operatorname{Pr}_{m, v}^{d}$ (Fig. 3). The probability in the first iteration is set by (7) to ensure that each $v$ value can be selected from the beginning:

$$
\operatorname{Pr}_{m, v}^{d}(0)=\frac{1}{\left(u b_{m}-l b_{m}\right)+1}
$$

The probability is updated in subsequent generations by (8):

$$
\operatorname{Pr}_{m, v}^{d}(t)=(1-\gamma) \cdot \operatorname{Pr}_{m, v}^{d}(t-1)+\gamma \cdot \frac{\text { Count }_{v}}{N}
$$

where $N$ is the population size, $t$ is the current generation, $\gamma$ is the population learning rate, and $\operatorname{Count}_{v}$ is the number of
![img-2.jpeg](img-2.jpeg)

Fig. 3. Progression of the LBH model for $W=3$. (a) first generations, (b) later generations.
individuals with value equal to $v$. Let $t_{\max }$ be the maximum number of generations, then the parameter $\gamma$ is set in (9):

$$
\gamma=\frac{t}{t_{\max }}
$$

Therefore, as the number of generations increases, $\gamma$ gradually increases as well, which implies that the model uses more information from individuals in those promising areas.

## C. Sampling

After the histograms have been developed, the offspring is obtained by sampling from the models. In case of a continuous variable $x_{i}$, a bin $j$ is firstly selected according to a randomly generated probability, then $x_{i}$ is uniformly sampled from the points that limit the bin selected $\left[p_{i, j-1}, p_{i, j}\right)$. For a discrete variable $x_{m}$, an available value of $v \in\left\{l b_{m}, u b_{m}\right\}$ is selected by a randomly generated probability.

## D. Constraint handling

$E D A_{m v n}$ uses a penalty method as a constraint-handling technique. The fitness values of each individual is divided in two parts: (i) objective function value $U$ and (ii) sum of constraint violation $C V$. This fitness value is defined in (10):

$$
f(\mathbf{x}, \mathbf{y})=U(\mathbf{x}, \mathbf{y})+C V(\mathbf{x}, \mathbf{y})
$$

The constraint violation is obtained from (11):
$C V(\mathbf{x}, \mathbf{y})=k_{1} \sum_{i=1}^{n} \max \left(g_{i}(\mathbf{x}, \mathbf{y}), 0\right)+k_{2} \sum_{j=1}^{m} \max \left(\left|h_{j}(\mathbf{x}, \mathbf{y})\right|, E\right)$
where $E$ is the tolerance parameter for equality constraints, $k_{1}$ and $k_{2}$ are the penalty factors for inequality constraints and equality constraints, respectively.

## III. Vulnerability to the Size of Discontinuous FEASIBLE PARTS

In [2], the authors showed the influence of the larger discontinuous feasible parts in the truncation and rounding techniques in MINLP problems. Unlike previous techniques, $E D A_{m v n}$ uses a direct integer-restriction-handling technique, since the LBH model directly generates integer values. In this section, we disclose the influence of those discontinuous parts on the LBH model. For that, the example in (12) is presented.

$$
\begin{gathered}
\operatorname{minimize} f(x, y)=2(x-1)^{2}+(y-3)^{2} \\
\text { subject to: } g(x, y)=x^{2}+y^{2}-4 \leq 0 \\
x \in[-3,3] \\
y \in\{-3,3\}
\end{gathered}
$$

In the MINLP problem in (12), $x$ is a continuous variable and $y$ is a integer variable, both in the range between -3 and 3. The optimal solution is $f(0,2)=3$, as shown in Fig. 4(a). The shaded area represents the feasible region defined by the constraints, and the red zones are the discontinuous feasible parts that also satisfy the integer restrictions. Note in Fig. 4(b), the global optimal solution is located in a small discontinuous

feasible part (upper red point). Local optimal solutions can be found in the larger discontinuous feasible parts.

The MINLP problem in (12) was solved by $E D A_{m v n}$ and PSO for mixed-variable $\left(P S O_{m v}\right)$, to illustrate the vulnerability of the LBH model to being trapped in larger discontinuous feasible parts. $P S O_{m v}$ [10] is a hybrid approach that uses the LBH model as integer restrictions handler. The parameter values used by both algorithms were obtained by the calibration process explained in Section V-C.

Fig. 5 shows the execution of $E D A_{m v n}$. In the 2 nd generation the population is in the exploration phase. However, in the 5th generation the entire population is located in the largest discontinuous feasible parts, as shown in Fig. 5(b). Therefore, the probability of the LBH model for the available value $y=2$ is zero. This inhibits any possibility of exploring the global optimum feasible region. In the later generations, the population tends to the best local optimum in the large discontinuous feasible parts, as shown in Figs. 5(c), 5(d). In $E D A_{m v n}$, the search in small discontinuous feasible parts improves when the penalty factor values decrease, since in regions close to feasibility parts low $C V(\mathbf{x}, \mathbf{y})$ are obtained. However, since the precision to the feasibility is affected by the penalization values, in many cases the algorithm does not get a real feasible solution.
$P S O_{m v}$ (see Fig. 6) also starts with a randomly generated population. It can be observed in Fig. 6(c) that, even in the 10th generation there are individuals exploring the region close to the global optimum. However, the population tends towards the best local optimal solution of the larger discontinuous feasible parts, as shown in Fig. 6(d).

In summary, the LBH model finds good candidates in large areas with relative ease, but it only finds infeasible points around small areas. This behavior increases the probability of available values in larger parts, and quickly discards small parts that remain unexplored or poorly explored. Once the entire population enters the wrong part, the loss of diversity causes the population to be trapped in a local optimum.

## IV. IMPROVEMENT PROPOSAL

In this section, two modifications for the original $E D A_{m v n}$ are proposed. The new variant $E D A_{m v}$ is aimed at solving
![img-3.jpeg](img-3.jpeg)

Fig. 4. MINLP problem in Eq. (12) (a) Feasible region and feasible parts, (b) global optimal solution and local optimal solutions.
![img-4.jpeg](img-4.jpeg)

Fig. 5. $E D A_{m v n}$ execution for the MINLP problem in (12): (a) 2nd generation; (b) 5th generation; (c) 10th generation; (d) 60th generation.
![img-5.jpeg](img-5.jpeg)

Fig. 6. $P S O_{m v}$ execution for the MINLP problem in (12): (a) 2nd generation; (b) 5th generation; (c) 10th generation; (d) 60th generation.
(i) the influence of the larger discontinuous feasible parts in the algorithm and (ii) the drawbacks of EDAs in the local refinement of the real values. In the first modification, the $\varepsilon$-constrained method is implemented in a special link with the LBH model, for exploring from non-feasible regions, and then improve the searching in small feasible parts. The second modification is the hybridization of EDA with a mutation operator to generate offspring from both the global distribution information and the parent information.

## A. $\varepsilon$-constrained method

The $\varepsilon$-constrained method was proposed by Takahama and Sakai [16] as a constraint-handling technique. Given two function values $f\left(x_{1}\right), f\left(x_{2}\right)$, and two constraint violations

$\phi\left(x_{1}\right), \phi\left(x_{2}\right)$ for two points $x_{1}$ and $x_{2}$, the $\varepsilon$-constrained method uses the $\varepsilon$-level comparisons described in (13):

$$
\left(f_{1}, \phi_{1}\right) \leq_{\varepsilon}\left(f_{2}, \phi_{2}\right)= \begin{cases}f_{1} \leq f_{2}, & \text { if } \phi_{1}, \phi_{2} \leq \varepsilon \\ f_{1} \leq f_{2}, & \text { if } \phi_{1}=\phi_{2} \\ \phi_{1}<\phi_{2}, & \text { otherwise }\end{cases}
$$

where $\varepsilon$-level comparisons are defined as an order relation on a pair of objective function and constraint violation values $(f(x), \phi(x))$.This means that the candidates with violation sum lower than $\varepsilon$ are considered as feasible solutions and are ordered according to their fitness function values. In the case of $\varepsilon=0, \phi(x)$ always precedes $f(x)$. Therefore, this method favors the approach to the feasible region by keeping slightly infeasible solutions with promising objective function value.

The $\varepsilon$-level decreases at each iteration $G$ until the predefined iteration number $T c$ is reached, after that $\varepsilon=0$, see (14):

$$
\begin{array}{ll}
\varepsilon(0)=\phi\left(x_{\theta}\right) & \text { if } 0<G<T_{c} \\
\varepsilon(G)= \begin{cases}\varepsilon(0)\left(1-\frac{G}{T_{c}}\right)^{c p}, & \text { otherwise }\end{cases}
$$

where $c p$ is a parameter to control the speed of constraint relaxation, $\varepsilon(0)$ is the initial value of $\varepsilon$, and $x_{\theta}$ is the top $\theta$ th in an array sorted by total constraint violation $(\theta=0.2 N)$.
B. Link between the LBH model and the $\varepsilon$-constrained method

The first modification is to use the $\varepsilon$-constrained method as a constraint-handling technique. Then, the selection mechanism to get the next population is carried out through parentoffspring competition using the $\varepsilon$-constrained method. The main idea is to improve exploration in small discontinuous feasible parts, approaching from the infeasible contours, i.e., infeasible candidates are not necessarily discarded, with the aim to reach feasible parts by using such solutions.

This modification fulfills the goal only for some runs, as will be shown in the results section. In other runs, the feasible region could not be reached. The problem occurs mainly when the LBH model converges while the $\varepsilon$ value is still high. If the entire population covers a region with constraint violation lower than the $\varepsilon$-level, the algorithm may be trapped in such infeasible region due to loss of diversity.

To overcome this drawback, a link between the LBH model and the $\varepsilon$-constrained method is established. The LBH model maintains equal probability for all available integer values until $\varepsilon$ reaches a predefined value $\varepsilon_{p}$. In this point, the LBH model begins to operate considering the statistical information (learning). If the $\varepsilon$-constrained method has been effective, for values of $\varepsilon$ sufficiently small, the solutions must be close to those parts of the feasible region with promising objective function values. Therefore, if the histogram begins the learning process at that point, it has a better chance of converging to good solutions.

The AWH and LBH histogram models for the new proposal $E D A_{m v}$ are shown in Algorithms 1, 2, respectively. The AWH is unchanged from the original $E D A_{m v n}$. However, the LBH model (now called LBH $\varepsilon$ ) works linked with the $\varepsilon$-level, as shown in line 2 of Algorithm 2.

```
Algorithm \(1 P R^{c} \leftarrow \mathrm{AWH}\left(p, W, e_{b}\right)\)
Input: the population \(p\), the number of bins \(W\), end bins
    parameter \(e_{b}\).
Output: the probability model \(P R^{c}\)
    for \(i \leftarrow 1\) to \(N v a r^{c}\) do
        Get \(x_{i, \min }^{1}, x_{i, \min }^{2}, x_{i, \max }^{1}, x_{i, \max }^{2}\)
        Calculate the boundaries of the promising area \(p_{i, 1}\) and
        \(p_{i, w-1}\) by (2) and (3)
        Calculate the bin width \(b\) by (4)
        for \(j \leftarrow 1\) to \(W+2\) do
            Count the candidates that fall into the \(j\) th bin and set
            \(A_{i, j}\) by (5)
            Update the probability model \(P R_{i, j}^{c}\) by (6)
            end for
    end for
Algorithm \(2 P R^{d} \leftarrow \mathrm{LBH} \varepsilon\left(p, t, \varepsilon, \varepsilon_{p}\right)\)
Input: the population \(p\), the current generation t , level \(\varepsilon\), link
    parameter \(\varepsilon_{p}\).
Output: the probability model \(P R^{d}\)
    for \(m \leftarrow 1\) to \(N v a r^{d}\) do
        if \(\mathrm{t}=1\) or \(\varepsilon>\varepsilon_{p}\) then
            Update \(P R_{m, v}^{d}\) by (7)
        else
            for \(v \leftarrow l b_{m}\) to \(u b_{m}\) do
                Count the individuals with values \(x_{m}\) equals to \(v\)
                and set as \(\operatorname{count}_{v}\)
                Update \(P R_{m, v}^{d}\) by (8)
            end for
        end if
    end for
```


## C. Hybridization with a mutation operator

The second modification is aimed at improving the search process in the space of real variables. EDAs work with probabilistic models, since the global distribution of the population is used to generate new solutions. In contrast, in conventional EAs, crossover and mutation operators are used to generate new solutions. Both types have their pros and cons, the solutions generated by crossover and mutation operators may be close to the parents, but far from other promising areas, while the EDAs cannot directly control the similarities between the new solutions and the parents. In this work, the mutation operation is added to generate the real variables. This operation is alternated with the original sampling operation taking into account the predefined mutation probability $r_{M}$. In this way, if this probability is satisfied for a solution vector, its real variables are computed as shown in (15) and (16):

$$
\begin{aligned}
& x_{i, j}^{g+1}=x_{\text {best }, j}^{g}+\beta \cdot\left(x_{\text {best }, j}^{g}-x_{i, j}^{g}\right) \\
& \beta=\beta_{\text {min }}+\operatorname{rand}_{i, j} \cdot\left(\beta_{\text {max }}-\beta_{\text {min }}\right)
\end{aligned}
$$

where $i, j$ are the index of the current solution vector and current variable, respectively, $g$ is the current generation,

$x_{b e s t, j}^{g}$ is the $j$ th variable of the best solution vector found so far, $r a n d_{i, j}$ is a random number between 0 and 1 , and $\beta_{\text {min }}$ and $\beta_{\text {max }}$ are the lower and upper bounds of $\beta$ predefined by the user, with values between 0 and 1 .

Consequently, the real variables of solution vectors could be generated by either sampling or mutation. Algorithm 3 shows the generation of real variables in both ways (lines 1-12), as well as the sampling of the integer variables (lines 13-16) without any change from the original algorithm. The overall procedure of $E D A_{m v}$ is presented in Algorithm 4.

```
Algorithm 3 Offs \(\leftarrow \mathrm{S} / \mathrm{M}\left(P R^{c}, P R^{d}, r_{M}, \beta_{\min }, \beta_{\max }, x_{\text {best }}\right)\)
Input: the probability models \(P R^{c}\) and \(P R^{d}\); mutation pa-
    rameters \(r_{M}, \beta_{\text {min }}, \beta_{\text {max }}\)
Output: a new candidate offspring \(\left[x_{i}, x_{m}\right]\)
    \(r_{1} \leftarrow \operatorname{Uniform}(0,1)\)
    if \(r_{1} \leq r_{M}\) then
        for \(i \leftarrow 1\) to \(N v a r^{c}\) do
            calculate variable \(x_{i}\) by (15)
        end for
    else
        for \(i \leftarrow 1\) to \(N v a r^{c}\) do
            \(r_{2} \leftarrow \operatorname{Uniform}(0,1)\)
            Select a bin j according \(P R^{c}\) and \(r_{2}\)
            \(x_{i} \leftarrow \operatorname{Uniform}\left[p_{i, j-1}, p_{i, j}\right)\)
        end for
    end if
    for \(m \leftarrow 1\) to \(N v a r^{d}\) do
        \(r_{3} \leftarrow \operatorname{Uniform}(0,1)\)
        Select a value \(v\) from \(\left\{l_{b}, u_{b}\right\}\) according \(P R^{d}\) and \(r_{3}\)
    end for
Algorithm \(4 E D A_{m v}\) framework
Input: \(N, W, e_{b}, G, r_{M}, T_{c}, c p, \beta_{\min }, \beta_{\max }, \varepsilon_{p}\)
Output: The best solution
    Initialize population \(p\)
    for \(t \leftarrow 1\) to \(G\) do
        Get the best solution so far \(x_{\text {best }}\)
        temporal \(\leftarrow \varnothing\)
        \(P R^{c} \leftarrow \operatorname{AWH}\left(p, W, e_{b}\right)\)
        \(P R^{d} \leftarrow \operatorname{LBHz}\left(p, t, \varepsilon, \varepsilon_{p}\right)\)
        for \(i \leftarrow 1\) to \(N\) do
            Offs \(\leftarrow \mathrm{S} / \mathrm{M}\left(P R^{c}, P R^{d}, r_{M}, \beta_{\text {min }}, \beta_{\text {max }}, x_{\text {best }}\right)\)
            temporal \(\leftarrow\) temporal \(\cup\) Offs
        end for
        temporal \(\leftarrow\) temporal \(\cup \mathrm{p}\); and clear p
        Select the best N individuals from temporal by the \(\varepsilon\) constrained method and set to p
    end for
```

V. EXPERIMENTATION AND RESULTS
A. How $E D A_{m v}$ works?

The problem described in (12) is solved by $E D A_{m v}$. The parameters used will be described in the Section V-C. The
progress of the algorithm along generations is observed in Fig. 7. In the early stages, the $\varepsilon$-level comparison allows the algorithm to explore smaller parts from the infeasible contours, as shown in Figs. 7(a), 7(b). At that moment, the LBH $\varepsilon$ model maintains a uniform probability for all available integer values in order to avoid premature convergence towards infeasible parts. This procedure contributes to the placement of solutions in various discontinuous parts and, as a consequence, the exploration of each part by means of the sampling/mutation operation of real variables operators. Fig. 7(c) shows how the solutions are located very close to the optimal solutions of those discontinuous parts. Once the value of $\varepsilon$ reaches $\varepsilon_{p}$, the LBH $\varepsilon$ begins the learning process. At that point, the statistical information is comprised of solutions located in feasible or almost feasible regions, with promising values of the objective function. As a consequence, the LBH $\varepsilon$ model has a better chance of converging to good solutions, as shown in Fig. 7(d).

## B. Benchmark problems

Twelve MINLP problems (F1-F12) proposed in [2] were used to evaluate and compare the performance of the proposed $E D A_{m v}$. Problems F1-F4 have many discontinuous feasible parts with different sizes and the optimal solution is located in a feasible part with a small size. Both F5 and F7 are problems with equality constraints. F8-F12 are problems with at least eight decision variables. Details of F1-F12 are presented in the Supplementary File in [2].

For the experimentation, the maximum number of the objective function evaluations was set at $1.8 \mathrm{E}+05$, and 25 independent runs were carried out for each problem. The tolerance value $E$ for the equality constraints was set at 1.0E-04. A run is considered as successful if: $\left|f\left(x_{\text {best }}\right)-f\left(x^{*}\right)\right| \leq 1.0 \mathrm{E}-4$, where $x^{*}$ is the best known solution and $x_{\text {best }}$ is the best feasible solution provided by the tested algorithm.
![img-6.jpeg](img-6.jpeg)

Fig. 7. $E D A_{m v}$ execution for the MINLP problem in (12): (a) 2nd generation; (b) 5th generation; (c) 10th generation; (d) 60th generation.

TABLE I
$P S O_{m v}, E D A_{m v n}, E D A-I$, AND $E D A-I I$ RESULTS OVER 25 INDEPENDENT RUNS.

## C. Algorithms

The test problems were solved by the $P S O_{m v}, E D A_{m v n}$, and $E D A_{m v}$ algorithms. However, to evaluate the individual contribution of each modification, the variants $E D A-I$ (only with the $\varepsilon$-constrained method), and $E D A-I I$ (with a link between the $\varepsilon$-constrained and the LBH model) are also included. The algorithms were tuned using the iRace parameter tuning tool [17]. The instances used for tuning were the F1F12 problems. For each algorithm, 2000 experiments were carried out in iRace, using the Friedman test for the selection of parameter sets.
$P S O_{m v}$ used a swarm size $N=300$, acceleration coefficient $c=1.5299$, learning rate $\alpha=0.0125 . E D A_{m v n}$ used $N=300$, numbers of bins $W=10$, end bins parameter $e_{b}=5.9058$, penalty parameters $k_{1}=500,000$ and $k_{2}=1,000 . E D A-I$ used $N=50, W=2, e_{b}=2.0192$, control generation $T_{c}=3,000$ and control speed parameter $c p=5 . E D A-I I$ used $N=50, W=2, e_{b}=2.0192$,
$T_{c}=3,000, c p=5$, link parameter $\varepsilon_{p}=0.01 . E D A_{m v}$ used $N=50, W=4, e_{b}=2.3959, T_{c}=3000, c p=8$, mutation parameters: $r_{M}=0.6, \varepsilon_{p}=0.2399, \beta_{\min }=0.3, \beta_{\max }=0.9$.

## D. Analysis of results

Table I summarizes the results of the test problems solved by $P S O_{m v}, E D A_{m v n}, E D A-I, E D A-I I$, and $E D A_{m v}$. The results are assessed in terms of the Feasible Rate (FR), Successful Rate (SR), Average (Ave), and Standard Deviation (Std Dev), over 25 independent runs. "NA" means that an algorithm cannot achieve $100 \%$ FR.

Firstly, the focus is on the progressive advancement of the original $E D A_{m v n}$. The $\varepsilon$-constrained method implementation ( $E D A-I$ ) aims to explore the smallest discontinuous feasible parts. However, it gave the worst results for the test problems. As can be seen in Table I, $E D A-I$ improved few results, since in many cases no feasible solutions were found. As mentioned above, this drawback mainly occurs when the LBH model

converges while the $\varepsilon$ value is still high. At that point, the whole population enters into a permissible infeasible region, and the algorithm can be trapped due to loss of diversity.

In $E D A-I I$, a link between the LBH model and the $\varepsilon$ constrained method was established ( $\mathrm{LBH} \varepsilon$ ). The learning process of $\mathrm{LBH} \varepsilon$ begins when $\varepsilon \leq 0.01$, then statistical information is comprised by better solutions. $E D A-I I$ is better than $E D A_{m v n}$ in seven problems, F1, F3, F4, F5, F6, F9 and F10. The FR and SR indicators are substantially improved over previous proposals. However, it was detected that the failed solutions were often very close to the best known solution.

In the final proposal $E D A_{m v}$, the mutation operator is also added to improve the search process for real variables. The Wilcoxon's rank-sum test at a 0.05 significance level was carried out between $E D A_{m v}$ and the other four algorithms. In Table I, $[-],[\approx]$ and $[+]$ means that the performance of the algorithm under test is worse, equal, or better than the corresponding to $E D A_{m v}$, respectively.

As can be seen in the last row of Table I, the results of $E D A_{m v}$ are significantly better than the original $E D A_{m v n}$ in eight problems: F1, F3, F4-F7, F11, F12, and similar in four other problems: F2, F8, F9, F10. Therefore, in no case $E D A_{m v n}$ improves the results of the new proposal. Significantly better $E D A_{m v}$ results can also be observed with regard to the $E D A-I$ and $E D A-I I$ algorithms, indicating the effectiveness of the proposed modifications.

Finally, $E D A_{m v}$ is compared with the hybrid $P S O_{m v}$. From Table I, $E D A_{m v}$ is significantly better than $P S O_{m v}$ in five test problems: F1, F3, F5, F7, F12, no difference in four problems: F2, F4, F6, F11, while $P S O_{m v}$ outperformed $E D A_{m v}$ in three problems: F8, F9, F10. For problems F9 and F10 the mutation operator of $E D A_{m v}$ produces premature convergence, which causes the population to be trapped in infeasible zones for some runs. It is notable that the original $E D A_{m v n}$ shows a worse performance than $P S O_{m v}$. In contrast, after the proposed modifications $E D A_{m v}$ provided a better performance than those of the four compared algorithms.

## VI. Conclusions

$E D A_{m v n}$ was initially proposed to solve a mixed-variable newsvendor problem. In this work, the vulnerability of $E D A_{m v n}$ of being trapped in larger discontinuous feasible parts has been proven, as well as its drawbacks in the local refinement of real variables. To overcome such disadvantages, $E D A_{m v}$ was proposed with two modifications to the original algorithm (i) a link between the LBH model and the $\varepsilon$ constrained method, and (ii) the hybridization with a mutation operator. This new proposal solves to a great extent the influence of the larger discontinuous feasible parts, and the disadvantages of EDAs in the local refinement of the real values.

A benchmark from the related literature was used to test and compare the performance of the improved proposal against the original $E D A_{m v n}$ and hybrid $P S O_{m v}$ algorithms. According to the Wilcoxon's rank-sum tests applied to the results obtained
in the experimental stage, the performance of $E D A_{m v}$ was better than those of the other algorithms tested. Different instances were also executed considering each proposed modification separately, and their effectiveness was verified.

## ACKNOWLEDGMENT

The first author acknowledges support from the Mexican National Council of Science and Technology (CONACyT) through a scholarship to pursue graduate studies at the CIDETEC-IPN. Second and fourth author acknowledge support from SIP-IPN through project No. 20221928 and No. 20221960, respectively.
