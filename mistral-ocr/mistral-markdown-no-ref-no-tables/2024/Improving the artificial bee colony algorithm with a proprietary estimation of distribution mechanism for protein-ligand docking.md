# Improving the artificial bee colony algorithm with a proprietary estimation of distribution mechanism for protein-ligand docking 

Shuangbao Song ${ }^{\mathrm{a}}$, Cheng Tang ${ }^{\mathrm{b}}$, Zhenyu Song ${ }^{\mathrm{c}}$, Jia Qu ${ }^{\mathrm{a}}$, Xingqian Chen ${ }^{\mathrm{d}, *}$<br>${ }^{a}$ School of Computer Science and Artificial Intelligence, Changzhou University, Changzhou 213164, China<br>${ }^{b}$ Faculty of Information Science and Electrical Engineering, Kyushu University, Fukuoka 819-0395, Japan<br>${ }^{c}$ College of Information Engineering, Taizhou University, Taizhou 225300, China<br>${ }^{d}$ School of Computer Engineering, Jiangsu University of Technology, Changzhou 213001, China

## A R TICLE INFO

Keywords:
Protein-ligand docking
Artificial bee colony
Estimation of distribution algorithm
Structure-based drug design
Optimization

## A B STR A C T

The protein-ligand docking problem plays an essential role in structure-based drug design. The challenge for a protein-ligand docking method is how to execute an efficient conformational search to explore a well-designed scoring function. In this study, we improved the artificial bee colony (ABC) algorithm and proposed an approach called ABC-EDM to solve the protein-ligand docking problem. ABC-EDM employs the scoring function of the classical AutoDock Vina to evaluate a solution during docking simulation. ABCEDM adopts the search framework of the canonical ABC algorithm to execute conformational search. By further investigating the characteristics of the protein-ligand docking problem, a proprietary search mechanism inspired by estimation of distribution algorithm, i.e., estimation of distribution mechanism (EDM), is designed to enhance the performance of ABC-EDM. To verify the effectiveness of the proposed ABC-EDM, we compare it with three variants of the ABC algorithm, three evolutionary computation algorithms, and AutoDock Vina. The experimental results show that ABC-EDM can effectively solve the protein-ligand docking problem, and it can achieve a success rate $5 \%$ higher than AutoDock Vina on the GOLD dataset. This study reveals that taking advantage of problem-specific information about the protein-ligand docking problem to enhance a docking method contributes to solving this problem.

## 1. Introduction

Proteins are large macromolecules and perform many fundamental biological functions in organisms. Since many diseases are associated with specific proteins, these proteins can serve as therapeutic targets in structure-based drug design. Usually, small molecules (e.g., ligands) that activate or inhibit the function of a target protein and produce a therapeutic benefit can be seen as drugs. Determining how the target proteins interact with small molecules is an important issue in structure-based drug design [1]. Owing to the rapid development of computer science, computational methods have greatly advanced the research of structure-based drug design in recent years [2,3]. Specifically, the protein-ligand docking method has emerged as one of the most typical techniques in drug design. This technique is commonly used in the process of lead discovery and medicinal chemistry optimization, and consequently, it improves the efficiency of drug design and discovery [4].

Protein-ligand docking is based on the assumption that a small molecule (ligand) exerts its biological activity by specific binding to the
protein receptor. The principles of protein-ligand docking are usually explained as the 'lock and key' mechanism and 'hand and glove' concept [5]. The protein-ligand docking problem is conceptually defined as follows: given the three-dimensional structure of a protein receptor, its prespecified binding site, and a ligand, predict the pose of the ligand bound to the binding site. The aim of docking methods is to predict the protein-ligand binding mode and estimate the corresponding binding affinity. Usually, docking methods are based on single-objective optimization techniques. A docking method reaches the native-like protein-ligand binding mode by optimizing a well-designed scoring function. Thus, an accurate scoring function and an efficient search strategy constitute the core components of a successful protein-ligand docking method.

The scoring functions are used to evaluate the protein-ligand interactions during a docking simulation. A sophisticated scoring function can achieve great performance regarding accuracy and speed. Numerous scoring functions have been proposed for molecule docking, and

[^0]
[^0]:    * Corresponding author.

    E-mail addresses: leadingsong@outlook.com, leadingsong@cczu.edu.cn (S. Song), tang@ait.kyushu-u.ac.jp (C. Tang), songzhenyu@tzu.edu.cn (Z. Song), uj199232@cczu.edu.cn (J. Qu), xingzai@jsut.edu.cn (X. Chen).

these functions can be roughly classified into four groups [6]: force-field-based, empirical, knowledge-based, and machine-learning-based scoring functions. Force-field-based scoring functions are derived from the laws of physics and calculate the noncovalent energy terms within protein-ligand interactions [7]. Empirical scoring functions, e.g., the scoring function of AutoDock Vina [8], accumulate the contributions of energetic factors in protein-ligand binding. Knowledge-based scoring functions sum up pairwise statistical potentials between protein and ligand [9]. Machine-learning-based scoring functions employ machine learning techniques to construct statistical models of scoring functions [10]. Overall, it is well accepted that the performance of all of these groups of scoring functions is not very satisfactory [6]. A specific scoring function has a unique theoretical basis and unique applicable condition.

Evolutionary computation (EC) [11] is a family of populationbased metaheuristic optimization algorithms that are inspired by natural evolution and mimic biological phenomena. The classic EC algorithms include the genetic algorithm (GA), particle swarm optimization (PSO), differential evolution (DE). In addition, in recent years, considerable achievements have been witnessed in two typical EC algorithms, i.e., ABC and estimation of distribution algorithm (EDA). ABC is a swarm-based stochastic optimization algorithm and is mainly inspired by the foraging behavior of bee colonies. Since ABC was originally proposed by Karaboga in 2005 [12], unremitting efforts have been made to improve the performance of ABC, and numerous ABC variants have been proposed in the literature [13], [14], [15], [16]. Owing to the powerful performance and ease of ABC, ABC and its variants have been applied to solve many real-world problems, such as medical-image processing [17] and robot path planning [18]. On the other hand, EDA [19] is a special class of EC algorithms. In contrast to conventional EC algorithms, EDA explores the search space by sampling explicit probabilistic models, which are built from the promising candidate solutions in the current population. In recent years, significant improvements [20] have been made in EDA research, and the effectiveness of EDA is verified on many complex problems [21], [22]. In general, ABC and EDA have emerged as important options among EC algorithms in the face of complex problems.

Due to the importance of the protein-ligand docking problem in structure-based drug design, several classic docking approaches have been developed in the literature, such as Glide [23], GOLD [24], DOCK [25], and AutoDock [26]. Among these docking approaches, AutoDock Vina (Vina for short) [8], [27] is arguably one of the most widely used docking approaches owing to its excellent performance and open source. Since the search space of the protein-ligand docking problem is very large, an exhaustive search strategy is impractical. There are two main categories of optimization techniques to execute conformational search in docking methods: the Monte Carlo method and EC. Vina employs a modified Monte Carlo simulation method coupled with a local search. Zhang et al. proposed a blind proteinligand docking method called EDock [28], where a replica-exchange Monte Carlo simulation is used to perform rigid-body docking. On the other hand, considerable success in applying the EC technique to bioinformatics [29], [30] has been achieved. Many protein-ligand docking methods have also employed the EC technique as the search strategy. GOLD and AutoDock use the canonical GA to constitute the core of their search strategies. Leonhart et al. proposed a BRKGADOCK method based on a biased random key GA for the protein-ligand docking problem [31]. Prentis et al. improved DOCK by employing a new 3D GA as the search strategy [32]. Ng et al. attempted to adopt PSO to enhance the performance of Vina, and a modified method called PSOVina was proposed [33]. PSOVina combines PSO with BFGS local search to perform conformational search. Later, they improved PSOVina by incorporating chaos-embedded local search into the search strategy [34]. In addition, a random drift PSO was proven effective for protein-ligand docking [35], [36]. Song et al. used an adaptive DE algorithm to improve the search efficiency of a docking method [37].

Ji et al. adopted a gradient boosting DE as the search strategy [38]. Moreover, several docking methods based on ABCs have also been proposed in the literature. Uehara et al. employed a special ABC, i.e., a fitness learning-based ABC with proximity stimuli, to perform proteinligand docking [39]. Guan et al. attempted to integrate ABC and DE as a hybrid algorithm for protein-ligand docking [40].

These aforementioned works have shown the advantage of the employed EC technique when solving the protein-ligand docking problem. However, the researchers in these works have attempted to improve the EC-based search strategy from the perspective of optimization. Although numerous search mechanisms to enhance docking performance have been proposed, little attention has been paid to the characteristics of the protein-ligand docking problem. As suggested in the work [41], taking full advantage of problem-specific information and incorporating a proprietary search mechanism into EC to improve docking performance is considered a promising research direction. This motivates us to develop a problem-specific EC technique for solving the protein-ligand docking problem.

In this study, considering the superior performance of ABCs, we propose an approach called ABC-EDM to solve the protein-ligand docking problem. The scoring function of Vina is incorporated into ABC-EDM to evaluate a protein-ligand complex during docking simulation. ABCEDM adopts the general framework of the canonical ABC to execute conformational search. By further investigating the characteristics of the protein-ligand docking problem, a proprietary search mechanism inspired by EDA is proposed to enhance the performance of ABCEDM. Finally, a set of fifty benchmark docking instances and the GOLD dataset are used to evaluate ABC-EDM. The experimental results show the superiority of ABC-EDM in comparison with the other seven methods. The contribution of this paper is fourfold. First, we propose an improved ABC algorithm called ABC-EDM for protein-ligand docking. Second, we further investigate the characteristics of the protein-ligand docking problem and propose a proprietary search mechanism inspired by EDA to enhance the performance of ABC-EDM. Third, we conduct integral experiments to verify the performance of ABC-EDM. Fourth, a new perspective for solving the protein-ligand docking problem by means of designing a problem-specific search strategy is provided in this paper.

The remainder of this paper is organized as follows. Section 2 presents the description of three important concepts used in this study. Section 3 presents the details of the proposed ABC-EDM approach. The experimental studies are provided in Section 4. Finally, Section 5 draws the conclusion of this paper.

## 2. Materials

In this section, we introduce three important concepts used in this study: the protein-ligand docking problem, ABC, and EDA.

### 2.1. The formulation of the protein-ligand docking problem

Given a protein receptor and its binding site, the goal of proteinligand docking methods is to predict the pose of the ligand at the binding site and to give a score estimating the binding affinity. Normally, the protein receptor is regarded as a rigid object, while the ligand has flexibility and is seen as an articulated object. Given a ligand with $n$ active rotatable bonds, a solution is represented as a real-value vector with $n+7$ variables in common docking methods. This vector provides the geometric description of the ligand bound to the binding site, including the conformation, orientation, and position of the ligand.

Fig. 1 exhibits the strategy of solution encoding in the proposed approach. The first $n$ variables of the vector $\mathbf{s}$ represent the torsion angles $\left(t_{1}, t_{2}, \ldots, t_{n}\right)$, which describe the flexibility of the ligand and uniquely determine the conformation of the ligand. The middle four variables $\left(v_{x}, v_{y}, v_{z}, \theta\right)$ of the vector $\mathbf{s}$ form a unit vector $\mathbf{u}=\left(u_{x}, u_{y}, u_{z}\right)$ and a rotation angle $\theta$ that determine the orientation of the ligand.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The strategy of solution encoding in the proposed approach. The designated binding site is marked as the green cube.

Given a rotation around the unit vector $\mathbf{u}$ through the angle $\theta$ on any point $\mathbf{p}=\left(p_{x}, p_{y}, p_{z}\right)$ in the ligand, the new point $\mathbf{p}^{\prime}=\left(p_{x}^{\prime}, p_{y}^{\prime}, p_{z}^{\prime}\right)$ is calculated using the Hamilton product:

$$
\begin{aligned}
\mathbf{p}^{\prime} & =\mathbf{q p q}^{-1} \\
\mathbf{q} & =\cos \frac{\theta}{2}+\left(u_{x} \mathbf{i}+u_{y} \mathbf{j}+u_{z} \mathbf{k}\right) \sin \frac{\theta}{2} \\
\mathbf{q}^{-1} & =\cos \frac{\theta}{2}-\left(u_{x} \mathbf{i}+u_{y} \mathbf{j}+u_{z} \mathbf{k}\right) \sin \frac{\theta}{2}
\end{aligned}
$$

where $\mathbf{q}$ and $\mathbf{q}^{-1}$ are two conjugate unit quaternions formed by $\mathbf{u}$ and $\theta, \mathbf{i}, \mathbf{j}$, and $\mathbf{k}$ are the unit quaternions along three spatial axes. The last three variables of the vector $\mathbf{s}$ compose a translation vector $\mathbf{m}=\left(m_{x}, m_{y}, m_{z}\right)$ to move the ligand into the binding site. In addition, all of the torsion angles $\left(\tau_{1}, \tau_{2}, \ldots, \tau_{n}\right)$ and the rotation angle $\theta$ range in $[-\pi, \pi]$. The variables $\left(v_{x}, v_{y}, v_{z}\right)$ representing the orientation of the ligand are limited to $[-1,1]$. Then, they are normalized as the unit vector $\mathbf{u}$. The variables $\left(m_{x}, m_{y}, m_{z}\right)$ dominating the position of the ligand are restricted to suitable scopes, ensuring that the ligand is within the three-dimensional search space of the binding site.

### 2.2. Canonical ABC

The artificial bee colony algorithm is a powerful stochastic optimization algorithm and is mainly inspired by the foraging behavior of bee colonies [12]. In the ABC algorithm, a candidate solution of an optimization problem is represented as the position of a food source. The bee colony in ABC is composed of three types of bees: employed bee, onlooker bee and scout bee. ABC solves the optimization problem by driving the bee colony to continually seek a better food source within the search space.

A candidate solution (the position of a food source) in ABC is represented as a vector $\mathbf{x}^{(i)}=\left(x_{1}^{(i)}, x_{2}^{(i)}, \ldots, x_{D}^{(i)}\right)$, where $D$ is the number of dimensions of the optimization problem. $\mathbf{x}^{(i)}$ represents the $i$ th individual in the $S N$-size food sources. The minimum and maximum bounds of these candidate solutions are set to $\mathbf{x}^{\min }=\left(x_{1}^{\min }, x_{2}^{\min }, \ldots, x_{D}^{\min }\right)$ and $\mathbf{x}^{\max }=\left(x_{1}^{\max }, x_{2}^{\max }, \ldots, x_{D}^{\max }\right)$, respectively. The framework of the canonical ABC consists of four main phases: the initialization phase, employed bee phase, onlooker bee phase, and scout bee phase. The details of the four phases are described as follows.

Initialization phase: The positions of the food sources in ABC are uniformly initialized in the problem-specific search space as:
$x_{j}^{(i)}=x_{j}^{\min }+r_{1}\left(x_{j}^{\max }-x_{j}^{\min }\right), j \in\{1,2, \ldots, D\}$
where $x_{j}^{(i)}$ is the $j$ th component of $\mathbf{x}^{(i)}$. $r_{1}$ is a random number that is uniformly distributed in $[0,1]$. For a minimization problem, the fitness value of each individual $\mathbf{x}^{(i)}$ is calculated as follows:
$f i t\left(\mathbf{x}^{(i)}\right)= \begin{cases}1 /\left(1+f\left(\mathbf{x}^{(i)}\right)\right) & \text { if } f\left(\mathbf{x}^{(i)}\right) \geq 0 \\ 1+\left|f\left(\mathbf{x}^{(i)}\right)\right| & \text { otherwise }\end{cases}$
where $f i t\left(\mathbf{x}^{(i)}\right)$ and $f\left(\mathbf{x}^{(i)}\right)$ represent the fitness value and objective function value of $\mathbf{x}^{(i)}$, respectively. Then, ABC starts its main loop and executes the following three phases iteratively until the stopping criterion is met.

Employed bee phase: There are $S N$ employed bees in ABC, and each employed bee is associated with a food source. The $i$ th employed bee searches the surrounding area of its associated food source. The position of the candidate food source $\mathbf{v}^{(i)}=\left(v_{1}^{(i)}, v_{2}^{(i)}, \ldots, v_{D}^{(i)}\right)$ inherits from $\mathbf{x}^{(i)}$ except the $j$ th component. This component is calculated as follows:
$v_{j}^{(i)}=x_{j}^{(i)}+r_{2}\left(x_{j}^{(i)}-x_{j}^{(k)}\right)$
where $j$ is randomly selected from $\{1,2, \ldots, D\}$ and $\mathbf{x}^{(k)}$ donates another food source in the population. $r_{2}$ is a random number and ranges in $[-1,1]$. The $i$ th employed bee will compare the fitness values of $\mathbf{x}^{(i)}$ and $\mathbf{v}^{(i)}$. If $\mathbf{v}^{(i)}$ is better than $\mathbf{x}^{(i)}, \mathbf{v}^{(i)}$ replaces $\mathbf{x}^{(i)}$ and is memorized as the new food source; otherwise, $\mathbf{x}^{(i)}$ is retained in the next generation. Then, the employed bees go back to share the information about the food sources with the onlooker bees.

Onlooker bee phase: There are also $S N$ onlooker bees in ABC. Every onlooker bee will first determine a food source in the population and then search its surrounding area. Based on the information brought by the employed bees, an onlooker bee tends to select a food source with a larger fitness value. The selection probability of a food source is calculated as follows:
$p_{i}=f i t\left(\mathbf{x}^{(i)}\right) / \sum_{i=1}^{S N} f i t\left(\mathbf{x}^{(i)}\right)$
After selecting a food source, the onlooker bee adapts the same method used by the employed bees to seek a better food source.

Scout bee phase: Since the nectar amount of a food source is limited, a food source will be abandoned if it cannot be improved during predetermined trials (denoted as the parameter 'limit'). The associated employed bee becomes a scout bee and relocates to a new food source within the search space by using Eq. (2).

### 2.3. Estimation of distribution algorithm

EDA solves a problem by evolving a set of candidate solutions through a cycle of computational steps. Compared with traditional EC algorithms, EDA generates offspring by sampling an explicit probabilistic model that is built from promising candidate solutions. The flowchart of a typical EDA is exhibited in Algorithm 1.

## 3. Methodology

This section presents the details of the proposed ABC-EDM approach, including the scoring function, EDM, and the overview of ABC-EDM.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Figure (a) shows how to offset the native ligand uniformly along the x -axis, y -axis, and z -axis. Correspondingly, the variations of the scoring function are exhibited in Figure (b).

Algorithm 1: The pseudocode of a typical EDA.
Input: Objective function, algorithm parameters.
Output: The best solution visited by the optimization algorithm.

## begin

Initialize the $N$-size population $P=\left\{\mathbf{x}^{(1)}, \mathbf{x}^{(2)}, \ldots, \mathbf{x}^{(N)}\right\}$.
/* A solution is encoded as $\mathbf{x}^{(i)}=\left(x_{1}^{(i)}, x_{2}^{(i)}, \ldots, x_{D}^{(i)}\right)$. $* /$
Calculate the fitness value of each individual by using the objective function.
while Stopping criterion is not met do
Select $M(0<M<N)$ promising solutions from $P$.
Build probabilistic model $p\left(x_{1}, x_{2}, \ldots, x_{D}\right)$ according to the $M$ promising solutions.
Sample $p\left(x_{1}, x_{2}, \ldots, x_{D}\right)$ to generate a set of new candidate solutions $P^{\prime}$.
Calculate the fitness value of each individual in $P^{\prime}$ by using the objective function.
Merge $P$ and $P^{\prime}$, then create new $P$ based on survival of the fittest.
Output result.

### 3.1. Scoring function

Protein-ligand docking methods are usually based on singleobjective optimization techniques, where the conformational search is
performed under the guidance of the single-objective scoring function. The Vina function is a classic scoring function, and its effectiveness has been widely verified in the literature [33,35,37,42]. In this study, the Vina function is employed to evaluate the conformation of a proteinligand complex during docking simulation. A lower value of the Vina function corresponds to a better conformation when two protein-ligand complexes are compared.

The conformation-dependent part of the Vina function is taken into consideration in this study, and the conformation-independent part, i.e., the penalty term about ligand flexibility, is omitted. The conformation-dependent part is a sum consisting of intermolecular and intramolecular contributions. The total scoring function $c$ can be calculated as follows:
$c=\sum_{i<j} c_{i j}$
where $c_{i j}$ is the scoring value of the pair of atoms $i$ and $j$ in the proteinligand complex. $c_{i j}$ can be calculated by the following equation:

$$
\begin{aligned}
c_{i j}= & w_{1} G a u s s_{1}\left(d_{i j}\right)+w_{2} G a u s s_{2}\left(d_{i j}\right)+w_{3} \operatorname{Repulsion}\left(d_{i j}\right) \\
& +w_{4} H y d r o p h o b i c\left(d_{i j}\right)+w_{5} H \operatorname{Bonding}\left(d_{i j}\right)
\end{aligned}
$$

where $d_{i j}$ is the surface distance between the atoms $i$ and $j . w_{1} \sim w_{5}$ are five weighting parameters of different items that are optimized based on the PDBbind dataset [43]. The first three items in Eq. (7) describe the steric interaction between atom $i$ and atom $j$. The fourth item reflects the hydrophobic interaction, and the fifth item reflects the effect of hydrogen bonding. These two items are calculated only when

the two types of interaction are identified. In detail, the five items in Eq. (7) can be calculated as follows:

$$
\begin{aligned}
& \operatorname{Gauss}_{1}\left(d_{i j}\right)=e^{-\left(d_{i j} / 0.5\right)^{2}} \\
& \operatorname{Gauss}_{2}\left(d_{i j}\right)=e^{-\left(\left(d_{i j}-3 / 2\right)^{2}\right.} \\
& \operatorname{Repulsion}\left(d_{i j}\right)= \begin{cases}d_{i j}^{2} & \text { if } d_{i j}<0 \\
0 & \text { if } d_{i j} \geq 0\end{cases} \\
& H_{y d r o g h o b i c}\left(d_{i j}\right)= \begin{cases}1 & \text { if } d_{i j} \leq 0.5 \\
1.5-d_{i j} & \text { if } 0.5<d_{i j}<1.5 \\
0 & \text { if } d_{i j} \geq 1.5\end{cases} \\
& H \operatorname{Bonding}\left(d_{i j}\right)= \begin{cases}1 & \text { if } d_{i j} \leq-0.7 \\
d_{i j} /(-0.7) & \text { if }-0.7<d_{i j}<0 \\
0 & \text { if } d_{i j} \geq 0\end{cases}
\end{aligned}
$$

### 3.2. Estimation of distribution mechanism

As mentioned above, the scoring function used in this study consists of intermolecular and intramolecular contributions. The intermolecular contributions score the interactions of the heavy atom pairs between the receptor and the ligand, and the intramolecular contributions score the non-1-4 heavy atom pairs in the ligand structure. From Eq. (8), it is easy to conclude that the Euclidean distances of the heavy atom pairs between the receptor and the ligand are essential for computing the intermolecular contributions. Compared with the conformation and orientation of a ligand, the position of the ligand can have a macro effect on the calculation of the scoring function. Taking advantage of this problem-specific information and then designing proprietary search mechanisms are considered to be helpful to improving the performance of docking methods.

In the scout bee phase of the canonical ABC, when a food source is abandoned, the associated employed bee will become a scout bee and relocate to a new food source within the search space. However, this scout bee hardly uses information about the current status of the food sources and randomly locates a solution in the search space. In this study, inspired by EDA, a mechanism called EDM is designed to assign the scout bee to a promising food source (candidate solution).

Differing from a common EDA that estimates the probability distribution on the whole variables, the proposed EDM estimates the probability distribution only on the variables $m_{x}, m_{y}$, and $m_{z}$ that are related to the position of the ligand. This is because these three variables are considered to play a more important role in the docking process, as discussed above, and are delimited to the other variables in solution coding. Moreover, the probabilistic model is a key component of an EDA. Since the variables $m_{x}, m_{y}$, and $m_{z}$ are the three components of a translation vector, it is obvious that they are independent from each other. Thus, the type of univariate probabilistic models [19] can be used in the proposed EDM. We empirically investigate the relation between the scoring function and the variables $m_{x}, m_{y}$, and $m_{z}$. Fig. 2(a) exhibits a typical protein-ligand complex where a ligand is bound to the binding site in the native state. We offset the ligand uniformly along the x -axis (i.e., modify the variable $m_{x}$ ), y -axis, and z -axis. The variations of the scoring function are exhibited in Fig. 2(b). From Fig. 2(b), we can see that the function graphs of the scoring function have funnel-shaped landscapes. This implies that the normal distribution is suitable for building probabilistic models for the variables $m_{x}, m_{y}$, and $m_{z}$. This is because the samples of a variable obeying a normal distribution can center around a single point. On the other hand, it is not easy to determine probabilistic models for the rest variables $\left(x_{1}, x_{2}, \ldots, x_{n}, c_{1}, c_{2}, \theta\right)$. Intuitively, the normal distribution is not suitable for building probabilistic models for these variables. It is considered arbitrary to casually select probabilistic models for these variables. Since these variables are related to the conformation and orientation of the ligand, a promising solution is considered to have
suitable conformation and orientation. As a result, it is a wise method to set these variables of a candidate solution by directly inheriting from a promising solution.

In the scout bee phase of the proposed ABC-EDM approach, EDM works in three steps to relocate a new food source. First, $M$ promising solutions that have better fitness values are selected from the current population of food sources. Second, for each variable of $m_{x}, m_{y}$, and $m_{z}$, the means $\left(\mu_{m_{x}}, \mu_{m_{y}}, \mu_{m_{z}}\right)$ and the standard deviations $\left(\delta_{m_{x}}, \delta_{m_{y}}, \delta_{m_{z}}\right)$ are calculated based on these $M$ promising solutions. Consequently, three normal distribution models, i.e., $N\left(\mu_{m_{x}}, \delta_{m_{x}}^{2}\right), N\left(\mu_{m_{y}}, \delta_{m_{y}}^{2}\right)$, and $N\left(\mu_{m_{x}}, \delta_{m_{x}}^{2}\right)$, are built. Finally, a new food source is initialized as follows:

$$
x_{j}^{(i)}= \begin{cases}x_{j}^{(\text {best })} & \text { if } j \in\{1,2, \ldots, n+4\} \\ \text { sampled from } N\left(\mu_{m_{x}}, \delta_{m_{x}}^{2}\right) & \text { if } j=n+5 \\ \text { sampled from } N\left(\mu_{m_{y}}, \delta_{m_{y}}^{2}\right) & \text { if } j=n+6 \\ \text { sampled from } N\left(\mu_{m_{z}}, \delta_{m_{z}}^{2}\right) & \text { if } j=n+7\end{cases}
$$

where $n$ is the number of active rotatable bonds. $x_{j}^{(\text {best })}$ is the $j$ th component of the best individual in the current population. In this way, a new candidate solution with a promising conformation and orientation can be relocated to a promising region in the binding site.

### 3.3. Overview of the proposed ABC-EDM approach

To implement the proposed ABC-EDM approach to solve the proteinligand docking problem, the scoring function is incorporated as the objective function of ABC-EDM. A solution s for the protein-ligand docking problem is encoded as the individual $\mathbf{x}^{(i)}$ in ABC-EDM. Consequently, the number of dimensions of $\mathbf{x}^{(i)}$, i.e., $D_{i}$ is equal to $n+7$. In addition, the minimum and maximum bounds of each variable, i.e., $\mathbf{x}^{\text {min }}$ and $\mathbf{x}^{\text {max }}$, are set to appropriate values, as described in Section 2.1.

Dealing with an infeasible solution in a docking simulation is an important issue in the implementation of ABC-EDM. The unsuitable values of the variables in a solution can cause the ligand to exceed the boundary of the binding site and lead to steric clashing between atoms. To avoid this issue, two simple strategies are proposed in ABC-EDM. In the initialization phase and the scout bee phase of ABC-EDM, the initialization of a new solution is repeated until this solution is checked as a feasible solution. In the employed bee phase and the onlooker bee phase of ABC-EDM, a candidate solution $\mathbf{v}^{(i)}$ is generated based on $\mathbf{x}^{(i)}$, as described in Section 2.2. Since the solution $\mathbf{v}^{(i)}$ may represent an infeasible solution, $\mathbf{v}^{(i)}$ replaces $\mathbf{x}^{(i)}$ and is memorized as the new food source only when $\mathbf{v}^{(i)}$ is checked as a feasible solution and its fitness value is better. Otherwise, $\mathbf{x}^{(i)}$ is retained to the next generation.

The pseudocode of the proposed ABC-EDM is presented in Algorithm 2. ABC-EDM follows the general framework of the canonical ABC but has a proprietary EDM. Before optimization, the docking environment is initialized according to the ligand and the protein receptor. Then, the ABC-EDM algorithm is employed to execute conformational search. Finally, the best solution visited by the bee colony is outputted as the docking result.

## 4. Experimental study

In this section, we present the experiments to evaluate the performance of the proposed ABC-EDM approach. We compare ABC-EDM with three variants of the ABC algorithm, three EC algorithms, and AutoDock Vina. Moreover, some algorithm analysis of ABC-EDM is also provided.

### 4.1. Experimental setup

All algorithms in this study are implemented in C++ and Python language. They are executed on the Linux 64-bit system with an Intel Core i5 CPU and 16 G memory.

Algorithm 2: The pseudocode of the proposed ABC-EDM.
Input: A protein receptor and its binding site, a ligand, algorithm parameters.
Output: The best solution visited by ABC-EDM.
begin
/* Initialization phase. */
Initialize the docking environment.
Obtain the minimum and maximum bounds, i.e., $\mathbf{x}^{\text {min }}$ and $\mathbf{x}^{\text {max }}$. Initialize the population $\left\{\mathbf{x}^{(i)}\right\} i \in\{1,2, \ldots, S N\}$ \} and ensure that they are feasible.
Calculate the fitness value of each $\mathbf{x}^{(i)}$, i.e., $f i t\left(\mathbf{x}^{(i)}\right)$.
while Stopping criterion is not met do
/* Employed bee phase. */
for $i$ in $\{1,2, \ldots, S N\}$ do
The $i$ th employed bee searches the neighbor food source $\mathbf{v}^{(i)}$ of $\mathbf{x}^{(i)}$ using Eq. (4).
Check whether $\mathbf{v}^{(i)}$ is feasible; if so, calculate $f i t\left(\mathbf{v}^{(i)}\right)$.
if $\mathbf{v}^{(i)}$ is feasible and $f i t\left(\mathbf{v}^{(i)}\right)>f i t\left(\mathbf{x}^{(i)}\right)$ then
$\mathbf{x}^{(i)} \leftarrow \mathbf{v}^{(i)}$
else
$\mathbf{x}^{(i)} \leftarrow \mathbf{x}^{(i)}$
/* Onlooker bee phase. */
Calculate the selection probability of each food source $p_{i}$ using Eq. (5).
for $k$ in $\{1,2, \ldots, S N\}$ do
The $k$ th onlooker bee selects a food source $\mathbf{x}^{(i)}$ according to the selection probability.
The $k$ th onlooker bee searches the neighbor food source $\mathbf{v}^{(i)}$ of $\mathbf{x}^{(i)}$ using Eq. (4).
Check whether $\mathbf{v}^{(i)}$ is feasible; if so, calculate $f i t\left(\mathbf{v}^{(i)}\right)$.
if $\mathbf{v}^{(i)}$ is feasible and $f i t\left(\mathbf{v}^{(i)}\right)>f i t\left(\mathbf{x}^{(i)}\right)$ then
$\mathbf{x}^{(i)} \leftarrow \mathbf{v}^{(i)}$
else
$\mathbf{x}^{(i)} \leftarrow \mathbf{x}^{(i)}$
/* Scout bee phase. */
for $i$ in $\{1,2, \ldots, S N\}$ do
if $\mathbf{x}^{(i)}$ cannot be improved during predetermined trials
'limit' then
/* Estimation of distribution mechanism. */
Select $M$ promising solutions from the current population.
Build normal distribution $N\left(\mu_{\mathrm{nt}}, \delta_{\mathrm{nt}}^{2}\right), N\left(\mu_{\mathrm{nt}}, \delta_{\mathrm{nt}}^{2}\right)$, and $N\left(\mu_{\mathrm{nt}}, \delta_{\mathrm{nt}}^{2}\right)$.
Repeat locating a new food source $\mathbf{x}^{(i)}$ by Eq. (9) until it is feasible.
Calculate $f i t\left(\mathbf{x}^{(i)}\right)$.
Output result.

A set of 50 protein-ligand complexes with a wide range of ligand sizes is used as the test docking instances, as shown in Table 1. The number of active rotatable bonds in these ligands varies from 1 to 21. The corresponding native structure of each complex was downloaded from the PDB database [44] and was properly prepared before docking simulation. In detail, for the structure of a complex, all water molecules are removed from it, and all missing hydrogens are appended into it. Then, the processed complex is separated into a ligand structure and a receptor structure. Next, AutoDockTools [26,27] is used to assign partial charges to the corresponding atoms in the ligand structure and the receptor structure. Finally, the information about the binding site is configured as a supplementary file.

Table 1
Fifty protein-ligand complexes are selected as the test docking instances.

${ }^{a}$ Size: Number of active rotatable bonds in the ligand.

To measure the performance of different docking methods, three metrics are employed to evaluate the docking result.
(1) Scoring value: This metric evaluates the optimization performance of a docking method. In addition, it estimates the binding affinity of a docked protein-ligand complex. A lower scoring value corresponds to a better docking result.
(2) Root mean square deviation (RMSD): RMSD measures the geometric similarity between the predicted ligand pose and the native ligand pose. Given a ligand with $n$ heavy atoms, RMSD is used to calculate the average distance between the matched heavy atoms of two poses:
$\operatorname{RMSD}_{(a, b)}=\sqrt{\frac{\sum_{i=1}^{n} d_{i}^{2}}{n}}$
where $a, b$ are the two poses of a ligand. $d_{i}$ is the distance between two corresponding heavy atoms. A smaller RMSD value indicates higher similarity between two poses of the ligand.
(3) Success rate: The docking process is considered successful when the RMSD value of the predicted ligand pose is less than a threshold (e.g. $2 \AA$ ). The success rate is defined as the percentage of the successful docking instances.

To verify the performance of the proposed ABC-EDM approach, we compare ABC-EDM with three types of methods, including three ABC variants, three common EC algorithms, and a classic docking program. Usually, a docking method is executed multiple times for an instance, e.g., 30 times, and the ligand pose with the lowest scoring value is outputted as the final docking result. In the experiment, we follow this practice and compare the docking result with the lowest scoring value. To make a fair comparison, the common parameters of these algorithms are set as follows. The population size (or colony size) is set to 100 , the maximum number of fitness function evaluations is set to 100000 , and the number of docking simulations for a docking instance is set to 30.

### 4.2. Comparing ABC-EDM with ABC variants

To evaluate the performance of the proposed ABC-EDM approach, we compare it with three classic ABC variants, including the canonical ABC [12], GABC [13], and qABC [14]. The user-defined parameters of these ABC algorithms are set as listed in Table 2. We execute the four ABC algorithms on the 50 test docking instances. As mentioned above, for each instance, the ligand pose with the lowest scoring value during 30 docking simulations is outputted as the final docking result.

Table 3 reports the optimization results of ABC-EDM versus the three ABC variants on the 50 docking instances. From Table 3, we can observe that ABC-EDM demonstrates the best performance on 40 docking instances. ABC-EDM is considered to have better optimization performance than the other three algorithms because ABC, GABC, and qABC yield the best performance on 1,6 , and 3 docking instances, respectively. Moreover, to determine the significant differences between ABC-EDM and the three algorithms, we perform the Friedman test as

Table 2
The user-defined parameters of the seven algorithms.
Table 3
The optimization results of ABC-EDM versus the three ABC variants on the 50 docking instances. The scoring value of the ligand pose with the lowest scoring value (among 30 independent docking simulations) is reported for each instance.
shown in Table 4. The Friedman test ranks the four ABC variants, and a smaller ranking value indicates a better performance. We can see that ABC-EDM achieves the smallest ranking of 1.38 . To avoid a Type I error [45], the Holm's method is employed to adjust the $\rho$ values to $p_{\text {Holm }}$ values. The $p_{\text {Holm }}$ values of ABC, GABC, and qABC are smaller

Table 4
Statistical results obtained by the Friedman test on the optimization results (in Table 3).

than the significance level of 0.05 . This indicates that ABC-EDM is significantly better than the three ABC variants in terms of optimization performance.

We compare the convergence performance of ABC-EDM and ABC. The average ( 30 times) convergence curves of ABC-EDM and ABC for six typical instances are illustrated in Fig. 3. These convergence curves reflect the exploration and exploitation ability of ABC-EDM and ABC [46]. Obviously, ABC converges close to ABC-EDM in the early search process. This finding indicates that ABC and ABC-EDM have similar exploration abilities. Moreover, in the late search process, ABC-EDM can more effectively improve the quality of the visited best solution than ABC. This observation implies that ABC-EDM have a stronger exploration ability. Since ABC-EDM is mainly different from ABC in that it has a proprietary EDM, the stronger exploration ability of ABC-EDM is considered to benefit from this mechanism. Overall, the effectiveness of the proposed EDM is empirically demonstrated.

We also compare the docking accuracy of the four ABC algorithms for the 50 docking instances. The RMSD values of the predicted ligand poses (reported in Table 3) are summarized in Table 5. From Table 5, we can see that ABC-EDM achieves the best RMSD values on 19 docking instances among the four algorithms. ABC, GABC, and qABC achieve the best RMSD values on 7, 11, and 13 docking instances, respectively. It is obvious that ABC-EDM achieves the best docking performance in terms of RMSD values. Moreover, the success rates of the four ABC algorithms are also reported in Table 5. ABC-EDM achieves the best performance among the four algorithms because ABC-EDM obtains the highest success rate. Overall, we can conclude that the proposed ABCEDM can provide a competitive result compared with the three ABC variants in terms of docking accuracy.

### 4.3. Comparing ABC-EDM with EC algorithms

To further evaluate the performance of the proposed ABC-EDM, three classical EC algorithms are used as the test baseline to show the performance of ABC-EDM. The three EC algorithms are PSO, DE, and GA. To make a fair comparison, their common parameters are set as mentioned above. In addition, they share the same initialization method, and their user-defined parameters are properly set based on the works in the literature [33,47], as listed in Table 2. We perform the four algorithms 30 times on the 50 test docking instances. For each instance, the ligand pose with the lowest scoring value is outputted as the final docking result.

The optimization results of the four algorithms on the 50 docking instances are summarized in Table 6. From Table 6, we can observe that ABC-EDM and DE achieve the best result on 25 and 24 docking

Table 5
The docking results of ABC-EDM versus the three ABC variants on the 50 docking instances. The RMSD $(\AA)$ of the predicted ligand pose is reported for each instance.

instances, respectively. ABC-EDM and DE are considered to have better optimization performance than the other two algorithms because PSO and GA obtain the best optimization performance on 0 and 1 docking instances, respectively. The Friedman test is employed to determine the significance, and Table 7 reports the statistical results. ABC-EDM achieves the smallest ranking of 1.52 , and ABC-EDM is considered to be significantly better than GA and PSO because the $p_{\text {Holm }}$ values are less than 0.05 . However, ABC-EDM is not significantly better than DE because the $p_{\text {Holm }}$ value is larger than 0.05 . Overall, ABC-EDM can provide a better or a competitive result compared with three classical EC algorithms in terms of optimization performance.

The RMSD values of the predicted ligand poses (reported in Table 6) are summarized in Table 8. For the 50 docking instances, we find that ABC-EDM, PSO, DE, and GA achieve the best result on $25,12,6$, and 7 docking instances, respectively. This indicates that ABC-EDM can achieve the most accurate docking results on half of the 50 docking

Table 6
The optimization results of ABC-EDM versus the three EC algorithms on the 50 docking instances. The scoring value of the ligand pose with the lowest scoring value (among 30 independent docking simulations) is reported for each instance.
Table 7
Statistical results obtained by the Friedman test on the optimization results (in Table 6).
instances. The success rates of the four algorithms are reported in Table 8. ABC-EDM achieves the highest success rate of $66 \%$, implying that ABC-EDM has the best performance compared with the other three EC algorithms. Therefore, we can conclude that, compared with three classical EC algorithms, ABC-EDM provides the most powerful performance for the protein-ligand docking problem in terms of docking accuracy.

![img-2.jpeg](img-2.jpeg)

Fig. 3. The convergence curves of ABC-EDM and ABC for six typical instances.

Table 8
The docking results of ABC-EDM versus the three EC algorithms on the 50 docking instances. The RMSD $(\AA)$ of the predicted ligand pose is reported for each instance.
Table 8 (continued).
### 4.4. Analysis of docking results

An accurate scoring function is essential for solving the proteinligand docking problem because it guides the conformational search of a docking method to obtain a native-like ligand pose. The proposed ABC-EDM incorporates the Vina function as the scoring function. The relationship between the docking accuracy (RMSD) and the scoring function is investigated in this section. Figs. 4 and 5 display the relationship between the scoring value and the RMSD value for the 50 docking instances. For each instance, a total of 210 docking results (each one of the seven algorithms performs 30 independent runs) are scatter plotted. In addition, the Spearman's correlation coefficient ( $r$ ) between the scoring value and the RMSD value is also calculated, as shown in Figs. 4 and 5. It can be observed that the scoring value has a positive correlation with the RMSD value, except 1ETA, 2CHT and 2GBP. This finding meets our expectation that a ligand pose with a lower scoring value generally has a higher docking accuracy (i.e., a smaller RMSD value).

Figs. 4 and 5 also show that the scoring function is not very precise, because the positive correlation between the scoring value and

![img-3.jpeg](img-3.jpeg)

Fig. 4. The scoring value (horizontal axis) versus RMSD value (vertical axis) of 210 docking results are scatter plotted for the 25 docking instances. The Spearman's correlation coefficient ( $\nu$ ) is also calculated.
the RMSD value is not considered strong in some cases, e.g., 1FKG, 1GLP, 1HSL, 1SLT, 1TMN, and 2MCP. This exhibition suggests that the landscape of the scoring function contains many local minima. A docking algorithm can be easily trapped in local minima during the search process. This is a main reason why the solutions in Figs. 4 and 5 are grouped into different numbers of clusters, especially for 1HYT, 1LAH, 1LST, 2ADA, 3CPA, and 3TPI. This finding implies that a successful docking method should not only pay attention to improving its optimization ability but also take advantage of the characteristics of the protein-ligand docking problem during the docking process. In fact, as shown in Table 6, DE produces a competitive optimization result compared with ABC-EDM. However, as exhibited in Table 8, DE produces worse docking results, and ABC-EDM is significantly better than DE in terms of docking accuracy. This finding indicates that a docking algorithm should not merely pursue optimization performance during the conformational search. Taking advantage of the characteristics of the protein-ligand docking problem contributes to solving this problem.

Moreover, we provide a three-dimensional visualization of the docking results to show how the predicted ligands are bound to the protein receptors. The docking results (the ligand poses with the lowest scoring values) of three typical instances, i.e., 1BMA, 1HYT, and 2CGR, are plotted in Fig. 6. Obviously, ABC-EDM provides more suitable solutions compared with the other algorithms because the ligand poses predicted by ABC-EDM are more similar to the native ligand poses. ABC-EDM can locate the ligand in the closer position of the native ligand than the other algorithms. Specifically, the ligand of 1BMA has a larger size (12 active rotatable bonds). ABC-EDM has an overwhelming advantage over the other algorithms for 1BMA, as shown in Fig. 6(a). In general, it can be concluded that ABC-EDM can provide a suitable solution for the protein-ligand docking problem.

### 4.5. Comparing ABC-EDM with AutoDock vina

We compare the docking results obtained by the proposed ABC-EDM approach with the state-of-the-art AutoDock Vina [8]. Vina is a classic molecular docking program and has been recognized as one of the most

![img-4.jpeg](img-4.jpeg)

Fig. 5. The scoring value (horizontal axis) versus RMSD value (vertical axis) of 210 docking results are scatter plotted for the other 25 docking instances. The Spearman's correlation coefficient ( $\nu$ ) is also calculated.

Table 9
Comparison of the success rates of ABC-EDM and Vina on the GOLD dataset (containing 113 docking instances) at three typical RMSD thresholds.
popular protein-ligand docking approaches in the literature [27,48]. Vina shares the same scoring function as ABC-EDM but has a different search method. In Vina, a modified Monte Carlo simulation method coupled with a local search based on BFGS algorithm is employed as the search method. The GOLD dataset is used to evaluate the docking performance of ABC-EDM and Vina. The protein-ligand complexes with structural errors have been removed, and a set of 113 protein-ligand complexes are retained as the benchmark dataset.

The parameters of Vina are set according to the recommendation [8], and the experimental setup is set to be same as ABC-EDM.

We execute Vina on the 113 docking instances. The docking simulation of Vina is performed 30 times on an instance, and the ligand pose with the lowest scoring value is outputted as the final docking result. Table 9 summarizes the success rates of ABC-EDM and Vina on the benchmark dataset. ABC-EDM achieves the better success rates of $30.09 \%$ (RMSD $<1 \AA$ ), $61.06 \%$ (RMSD $<2 \AA$ ), and $86.73 \%$ (RMSD $<5 \AA$ ) in comparison with Vina. Fig. 7 gives the detailed comparison of the success rates at different RMSD thresholds. This comparison result illustrates that the proposed ABC-EDM approach can provide better docking results in comparison with Vina.

Finally, we note that the BFGS-based local search in Vina is a quasi-Newton optimization method. This means that the gradient of the scoring function needs to be calculated. Consequently, more computational resources are required during docking simulation. The success of Vina is partly due to the sophisticated gradient calculation method. Compared with Vina, ABC-EDM does not require gradient calculation but takes advantage of the characteristics of the protein-ligand docking problem. A proprietary search mechanism based on EDA is designed to

![img-5.jpeg](img-5.jpeg)

Fig. 6. Three-dimensional visualizations of the docking results for the three docking instances. For each instance, the rugged surface of the protein receptor is displayed in the left figure, and the green cuboid exhibits the three-dimensional search space of the binding sites. The native ligand poses are labeled in red, and the predicted ligand poses obtained by the different algorithms are labeled in blue.
improve the performance of ABC-EDM. Therefore, the proposed search strategy in ABC-EDM is considered more straightforward and concise.

## 5. Conclusions and future work

In this study, we proposed an approach called ABC-EDM to solve the protein-ligand docking problem. ABC-EDM employed the empirical scoring function of AutoDock Vina as the scoring function. Considering the powerful performance of ABC algorithms, we used a modified ABC to constitute the core search strategy of ABC-EDM. By further analyzing the characteristics of the protein-ligand docking problem, we proposed a proprietary search mechanism inspired by EDA to enhance the search performance. Later, the effectiveness of ABC-EDM was verified on many docking instances. The experimental results demonstrated the superiority of ABC-EDM in comparison with the other seven methods, and ABC-EDM achieved a success rate 5\% higher than AutoDock Vina on the GOLD dataset. Different from previous works that developed a new search strategy starting from the view of optimization, we took full advantage of problem-specific information and designed a proprietary
search mechanism to enhance the search performance. The experimental results suggested that incorporating the prior knowledge of the protein-ligand docking problem contributes to solving this problem. In fact, the analysis of experimental results indicated that merely pursuing optimization performance while overlooking the characteristics of the protein-ligand docking problem could lead to the degradation of the docking accuracy. The development of proprietary search strategies in protein-ligand docking methods deserves the efforts of researchers.

In the future, we intend to pay continuous attention to the search strategy and the scoring function to develop more effective proteinligand docking methods. The adoption of more powerful evolutionary computation techniques in protein-ligand docking is worth investigating. Specifically, taking advantage of more prior knowledge and designing problem-specific mechanisms in docking methods deserve future efforts. Moreover, it is reasonable to incorporate other categories of scoring functions to enhance docking methods, such as knowledge-based scoring functions and machine-learning-based scoring functions.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Comparison of the success rates of ABC-EDM and Vina on the GOLD dataset (containing 113 docking instances).

## CRediT authorship contribution statement

Shuangbao Song: Writing - original draft, Visualization, Software, Methodology, Funding acquisition, Conceptualization. Cheng Tang: Writing - review \& editing, Visualization, Validation, Methodology, Investigation, Formal analysis. Zhenyu Song: Writing - review \& editing, Visualization, Validation, Resources, Investigation, Formal analysis. Jia Qu: Writing - review \& editing, Supervision, Software, Project administration, Investigation, Funding acquisition. Xingqian Chen: Writing - review \& editing, Writing - original draft, Supervision, Resources, Methodology, Formal analysis, Data curation, Conceptualization.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Acknowledgments

This work was supported by the Natural Science Foundation of Jiangsu Province of China (Grant No. BK20220619), and the National Natural Science Foundation of China (Grant No. 62203069).
