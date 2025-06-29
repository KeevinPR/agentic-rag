# An Improved Ant Colony Algorithm based on Distribution Estimation 

Fang Bei<br>SuZhou Polytechnic Institute of Agriculture, JiangSu SuZhou 215008, China<br>houshuai2014_cn@163.com


#### Abstract

In last two decades, Ant colony algorithm got extensive application in combinatorial optimization, function optimization and other fields. Ant colony algorithm is easy to fall into local optimum. A novel estimation of distribution algorithm by fusion improvement on ant colony algorithm and PBIL estimation of distribution algorithm is proposed. The algorithm introduce probability distribution model of PBIL algorithm to guide route choice, which greatly improves the faults that positive feedback mechanism of pheromone. Although the hybrid ant colony algorithm has achieved good results, this is just the preliminary attempt of distributed estimation algorithm combined with ant colony algorithm. Probability distribution model of other distribution estimation algorithm can also be used to guide the choice of ant colony optimal path.


Keywords-Ant colony algorithm; distribution estimation; the binary ant colony algorithm

## I. INTRODUCTION

During the 1990s, the Italian scholar M.Dorigo, V.Maniezzo proposed a heuristic evolutionary bionic algorithm based on population by simulation the collective behavior of ant routing, and found the whole ant colony make use of pheromone to collaborate with each other to form a positive feedback that each ant follow the shortest path[1-2]. In last two decades, Ant colony algorithm got extensive application in combinatorial optimization, function optimization, system identification, network route, robot path planning, data mining and cabling design of large scale integrated circuit[3-8]. But many scholars realized the limitation of traditional ant colony algorithm to improve. The improvement of ant colony algorithm have two handles, one aspect is the improvement of itself, such as improvement mode of pheromone release, probability of selection method, and the other is fusion improvement on ant colony algorithm and other intelligent optimization algorithms $[9,10]$.

Because the ant colony algorithm itself is a kind of optimization algorithm based on pheromone positive feedback mechanism, large pheromone accumulation is easy to fall into local optimum, and application effect of the basic ant colony algorithm in the continuous domain is not obvious. In order to solve this problem, people explore other evolutionary algorithms[11,12], which are introduced to solve the problem of pheromone accumulation of positive feedback, such as the ant colony algorithm and artificial immune algorithm, ant colony algorithm with neural network fusion, the fusion of ant colony algorithm and particle swarm algorithm, the mutation operator of genetic algorithm introduced into ant colony algorithm, etc. The
hybrid algorithms relieve local optimal problem of the ant colony algorithm to some extent, but there is still space for further research. This paper introduced distribution estimation algorithm into ant colony algorithm. Distribution estimation algorithm is a kind of evolutionary algorithm based on probability model, which is based on statistical feature. The paper is organized as follows. In the next section, the binary ant colony algorithm is given. In Section 3, a novel ant colony algorithm based on distribution estimation algorithm and traditional ant colony algorithm is presented In Section 4, experiments are done. Finally, we conclude our paper in section 5.

## II. THE BINARY ANT COLONY ALGORITHM

The pheromone matrix of binary ant colony algorithm is Ant_phero of $2 \times M$ dimension. The first row vector of Ant_phero represents pheromone, the position of which is 1 . The sencond row vector of Ant_phero represents pheromone, the position of which is 0 . Due to the early stage of ant pheromone distribution is very important, the layout of the pheromone will directly affect the choice of direction of ants. Therefore, the former let pheromone sent out with small unit, with the increase of evolution, pheromone distribution quantity increase gradually for the pheromone update.
Ant_pheromne $(i, j)=(1-\rho) \cdot$ Ant_pheromne $0(i, j)+$
$\rho \frac{1}{1+e^{-10\left(\frac{n}{n_{-} \max }-0.5\right)}} \cdot$ Ant_pheromne $(i, j)$
Ant_pheromone0 represents pheromone matrix of the last generation, Ant_pheromonel represents contemporary increased pheromone matrix, Ant_pheromone represents the pheromone matrix after update, $\rho$ represents pheromone volatilization coefficient, $n c$ represents the current evolution generation, $n c \_$max represents maximum evolution generation. The transmitting probability matrix Ant_ $\operatorname{pro}(2, m)$ adopts the following formula.
Ant_ $\operatorname{pro}(i, j)=1-$ Ant_ $\operatorname{pro}(1, j)$
when $i=2, j=1,2, \cdots, m$. When $i=1, j=1,2, \cdots, m$. The process of binary ant colony algorithm is as follows.
Step1. Randomly generate the initial solution, and set the initial pheromone value 0.5 .
Step2. Calculate each ant path length, and introduce elite

reserved strategy at the same time.
Step3.Determine whether meet the algorithm end condition, if it meets, the algorithm stops. Otherwise go on.
Step4. According to the path distribution of ants, update pheromone.
Step5. Calculate transition probability according to the formula.
Step6. According to the transition probability, redistribute ant paths, turn to step 2 .
Ant_pro $(i, j)=\frac{\text { Ant_pheromone }(1, j)}{\text { Ant_pheromone }(1, j)+\text { Ant_pheromone }(2, j)}$
III. AN IMPROVED ANT COLONY ALGORITHM BASED ON DISTRIBUTION ESTIMATION

## A. Distribution estimation algorithm

The process of distribution estimation algorithm is as follows.
Step1. Generate the initial probability vector $P_{0}$.
Step2. Generate $M$ number of individuals through probability vector $P$ and calculate fitness value of $M$ number of individuals. Introduce elite reservation strategy to determine whether it meets the terminal condition. Otherwise go on.
Step3. Choose the optimal $N$ number of individuals, $N=u \cdot M . u$ is percentage of choosing the optimal individuals, $N \leq M$.
Step4. Update probability vector $P$, and the update rule is Heb rule.
$P=(1-r) \cdot P_{1}+r \cdot P_{2}$.
$P$ represents probability vector after update, $P$ represents probability vector of the last generation, $P_{2}$ represents probability vector of $N$ number of individuals, the bit value of which is 1 , and $r$ represents learning factor. Turn to step2.

## B. An improved ant colony algorithm based on distribution estimation algorithm

In this paper, the parameters of the algorithm mainly includes the pheromone evaporation rate $\rho$, the number of ants $m$, learning rate $r$, sample percentage of distribution model $u$, learning guidance factor $\lambda$. Choose the following five functions as parameters test function.
$E S\left(x_{1}, x_{2}\right)=-\cos \left(x_{1}\right) \cos \left(x_{2}\right) \exp \left(-\left(\left(x_{1}-\pi\right)^{2}+\left(x_{2}-\pi\right)^{2}\right)\right)$.
The domain of variable is $-100 \leq x_{j} \leq 100, j=1,2$. It has a global minimal value $\left(x_{1}, x_{2}\right)^{*}=(\pi, \pi)$.
$E S\left(\left(x_{1}, x_{2}\right)^{*}\right)=-1$
$G P\left(x_{1}, x_{2}\right)=\left[1+\left(x_{1}+x_{2}+1\right)^{2} \cdot\left(19-14 x_{1}+13 x_{1}^{2}\right.\right.$
$\left.-14 x_{2}+6 x_{1} x_{2}+3 x_{2}^{2}\right)\left[\left.30+\left(2 x_{1}-3 x_{2}\right)^{2} \cdot\left(18-32 x_{1}\right.\right.\right.$
$\left.\left.+12 x_{1}^{2}-48 x_{2}-36 x_{1} x_{2}+27 x_{2}^{2}\right)\right]$
The domain of variable is $-2 \leq x_{j} \leq 2, j=1,2$.
$D J\left(x_{1}, x_{2}, x_{3}\right)=x_{1}^{2}+x_{2}^{2}+x_{3}^{2}$.
The domain of variable is $-5.12 \leq x_{j} \leq 5.12$, $j=1,2,3$.
$M G(x)=\left(x_{1}-x_{2}\right)^{2}+\left(\left(x_{1}+x_{2}-10\right) / 3\right)^{2}$. The domain of variable is $-20 \leq x_{j} \leq 20, j=1,2$.
$G r(x)=\sum_{i=1}^{n}\left(x_{j}^{2} / 4000\right)-\prod_{j=1}^{n} \cos \left(x_{j} / \sqrt{j}\right)+1 \quad$. The domain of variable is $-600 \leq x_{j} \leq 600, j=1,2, \ldots 10$.
$\operatorname{Value}(r)=E S(r)+G P(r)+D J(r)+M G(r)+G r(r)$.
$\operatorname{Value}(u)=E S(u)+G P(u)+D J(u)+M G(u)+G r(u)$.
$\operatorname{Value}(\rho)=E S(\rho)+G P(\rho)+D J(\rho)+M G(\rho)+G r(\rho)$.
$\operatorname{Value}(m)=E S(m)+G P(m)+D J(m)+M G(m)+G r(m)$
$\operatorname{Value}(\lambda)=E S(\lambda)+G P(\lambda)+D J(\lambda)+M G(\lambda)+G r(\lambda)$.
Relation between $r, u, \rho, m, \lambda$ and Value is shown in Figure.1, Figure.2, Figure.3, Figure. 4 and Figure. 5 respectively.
![img-0.jpeg](img-0.jpeg)

Figure 1. Relation between $r$ and Value

## IV. SIMULATIONS

In order to illustrate the effectiveness of the improved hybrid ant colony algorithm, the other three standard test functions are selected to test the performance of them. The result of MG function is shown in Figure.6, the result of matyas function is shown in Figure. 7 and the result of sum function is shown in Figure. 8.

![img-6.jpeg](img-6.jpeg)

Figure 2. Relation between $\boldsymbol{H}$ and Value
![img-6.jpeg](img-6.jpeg)

Figure 3. Relation between $\boldsymbol{\rho}$ and Value
![img-6.jpeg](img-6.jpeg)

Figure 4. Relation between $\boldsymbol{m}$ and Value
![img-6.jpeg](img-6.jpeg)

Figure 5. Relation between $\lambda$ and Value
![img-6.jpeg](img-6.jpeg)

Figure 6. MG function
![img-6.jpeg](img-6.jpeg)

Figure 7. matyas function

![img-7.jpeg](img-7.jpeg)

Figure 8. sum function
Ant colony algorithm and distribution estimation algorithm are easy to fall into local optimum, causing premature. By the way of fusion of distribution estimation algorithm and the ant colony algorithm, the search ability and speed of global optimal solution can effectively be improved.

## V. CONCLUSIONS

We propose a novel estimation of distribution algorithm by fusion improvement on ant colony algorithm and PBIL estimation of distribution algorithm. The algorithm introduce probability distribution model of PBIL algorithm to guide route choice, which greatly improves the faults that positive feedback mechanism of pheromone.
