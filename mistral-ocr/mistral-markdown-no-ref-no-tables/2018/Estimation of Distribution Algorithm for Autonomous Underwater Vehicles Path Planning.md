# Estimation of Distribution Algorithm for Autonomous Underwater Vehicles Path Planning 

Run-Dong Liu, Zhi-Hui Zhan ${ }^{(\boxtimes)}$, Wei-Neng Chen, Zhiwen Yu, and Jun Zhang ${ }^{(\boxtimes)}$<br>Guangdong Provincial Key Lab of Computational Intelligence and Cyberspace<br>Information, School of Computer Science and Engineering,<br>South China University of Technology, Guangzhou 510006, China<br>zhanapollo@163.com


#### Abstract

Path planning is that given the start point and target point, finding out a shortest or smallest cost path. In recent years, more and more researchers use evolutionary algorithms (EAs) to solve path planning problems, such as genetic algorithms (GAs) and particle swarm optimization (PSO). Estimation of distribution algorithms (EDAs) belong to a kind of EAs that can make good use of global statistic information of the population. However, EDAs are seldom used to solve path planning problems. In this paper, we propose an EDA variant named adaptive fixed-height histogram (AFHH) algorithm to make path planning for autonomous underwater vehicles (AUVs). The proposed AFHH algorithm can adaptively shrink its search space to make good use of computational resource. We use a regenerate approach to avoid getting stuck in local optimum. We also measure the ability of fixed-height histogram (FHH) algorithm for path planning. We simulate a 3-D environment to measure the ability of the proposed AFHH algorithm. The results show that AFHH has a good convergence rate and can also get better performance.


Keywords: Estimation of distribution algorithm (EDA)
Autonomous underwater vehicles (AUVs) $\cdot$ Path planning
Adaptive fixed-height histogram (AFHH)

## 1 Introduction

Path planning is one of the most significant methods to make some robots more intelligent such as unmanned vehicles. Autonomous underwater vehicles (AUVs) are a kind of underwater robots [1]. They can work underwater according to humans' predefined commands. During the working period, they don't need to communicate with humans. Therefore, in some dangerous underwater environment such as contaminated areas, they can complete missions instead of humans [2]. Due to the widely application of AUVs, path planning for AUVs has become a very significant research topic. Although path planning problems (PPP) have been widely studied in the literatures, many of them don't need to consider too many conditions. For example, the traveling

salesman problem (TSP) which is also a kind of PPPs, just needs to find a shortest path without considering complex environment [3].

According to study in [4], path planning algorithm can be divided into two groups. One is the resolution complete algorithms, and the other one is the probabilistic resolution complete algorithms. The A* approach is resolution complete algorithm. Garau et al. [5] used A* approach to make path planning for AUVs in complex environment. EAs are a kind of probabilistic resolution complete algorithms. In recent years, many researchers use EAs to solve some kinds of PPPs. Shih et al. [6] proposed a genetic-based effective approach to solve the PPP for AUVs. Zhang et al. [7] used an adaptive differential evolution (ADE) algorithm to make path planning for AUVs.

In this paper, we propose an adaptive fixed-height histogram (AFHH) algorithm to make path planning for AUVs in 3-D environment. The fixed-height histogram $(\mathrm{FHH})$ algorithm is a kind of EDAs. It is also a kind of EAs. The proposed AFHH algorithm can adaptively shrink search space in the course of evolution. We randomly generate new individuals with the current search space every $T$ generations to make the algorithm avoid getting stuck in local optimum. Furthermore, we use a 3-D environment model to check out whether AFHH has a good path planning ability.

The rest of this paper is organized as follows. Section 2 introduces the background knowledge of EDAs and environment modeling of AUVs path planning. Section 3 describes the proposed AFHH algorithm for path planning in detail. Section 4 presents results of experiments. Section 5 makes a conclusion of this paper.

# 2 Background Knowledge 

### 2.1 Environment Modeling for AUVs Path Planning

To make path planning for AUVs, the first step is constructing an environment model. Environment underwater in some area is very complex. The shape of seabed is not smooth. It maybe changes sharply in different areas. Besides, some floating obstacles make the environment more complex. In this paper, we use a 3-D static environment which is constructed in [7] to model the PPP for AUVs.

Herein, we consider the path planning in 3-D space with length, width, and depth. As shown in Fig. 1(a), the $X$ axis, $Y$ axis, and $Z$ axis represent the environment's length, width and depth respectively. In Fig. 1(a), spheres represent floating obstacles, and the others represent seabed.

The 3-D environment model is split to 40 parallel sections along the $y$ axis. The section is a profile of the 3-D environment. The section is shown in Fig. 1(b). The red areas represent obstacles. Each section is formed with a $20 \times 20$ grid. Besides, a $40 \times 20 \times 20$ array is used to save all sections. If there are obstacles in some areas, then the corresponding grids will be set as 1 . Otherwise, they will be set as 0 .

In each section, a feasible waypoint will be found. The trajectory is formed with 40 waypoints which are respectively generated in 40 sections. After that, we use a cost function to evaluate the path's quality according to its length, variation of depth, turning radius, and safety. The cost function is defined as:

![img-0.jpeg](img-0.jpeg)

Fig. 1. The environment models of path planning for AUVs.

$$
F_{\text {cost }}=C_{\text {length }}+C_{\text {depth }}+C_{\text {smooth }}+C_{\text {block }}
$$

where $C_{\text {length }}$ represents the length of a path. $C_{\text {depth }}$ represents the variation of a path's depth. $C_{\text {smooth }}$ represents a path's smooth degree. $C_{\text {block }}$ represents the safety of a path. $C_{\text {length }}$ is defined as:

$$
C_{\text {length }}=1-\frac{L_{P s P t}}{L_{\text {path }}}, C_{\text {length }} \in(0,1)
$$

where $L_{P s P t}$ is the Euclidean distance between start point and stop point. $L_{\text {path }}$ is the length of the whole path. $C_{\text {depth }}$ is defined as:

$$
C_{\text {depth }}=\frac{D_{\max }-D_{\min }}{D}, C_{\text {depth }} \in(0,1)
$$

where $D_{\max }$ is the max depth of the path, and $D_{\min }$ is the min depth of the path. $D$ is the max depth of the 3-D environment model. $C_{\text {smooth }}$ is defined as:

$$
C_{\text {smooth }}=\left\{\begin{array}{cl}
2+\frac{N_{\text {unable }}}{N_{\text {segment }}}, & N_{\text {unable }}>0 \\
0, & N_{\text {unable }}=0
\end{array}, C_{\text {smooth }} \in 0 \cup(2,3)\right.
$$

where $N_{\text {unable }}$ is the number of path segments whose turning radius beyond the motion ability of AUVs. If the length of one path segment larger than a predefined value $\theta$, then $N_{\text {unable }}$ will increase. We set $\theta$ as 1.75. $N_{\text {segment }}$ is the number of all path segments. $C_{\text {block }}$ is defined as:

$$
C_{\text {block }}=\left\{\begin{array}{cl}
2+\frac{N_{\text {block }}}{N_{\text {space }}}, & N_{\text {block }}>0 \\
0, & N_{\text {block }}=0
\end{array}, C_{\text {block }} \in 0 \cup(2,3)\right.
$$

where $N_{\text {block }}$ is the number of unfeasible waypoints. $N_{\text {space }}$ is the number of sections.

# 2.2 Estimation of Distribution Algorithm 

EDA is a kind of stochastic algorithms which belongs to EAs. It performs better than GA in most case because EDA makes a good use of the global statistics. EDA's procedure is similar to GA. However, EDA doesn't have mutation and crossover procedures. Tsutsui et al. [8] proposed two histogram based EDAs, one is the fixed-width histogram (FWH) algorithm, and the other one is the FHH algorithm. Xiao et al. [10] proposed a histogram-based EDA which is used for processing continuous optimization problems. Yang et al. [11] proposed an improved EDA which can process multimodal problems.

## 3 Proposed AFHH Algorithm

In this section, we describe the proposed AFHH algorithm for path planning in detail. We first choose the organization of individual's structure, which is proposed in [7]. As shown in Eq. (6), the individual's structure is made of waypoints. Each waypoint is a tuple which contains 3-D positional information. The $X$ axis and $Z$ axis values are generated in each section. The $Y$ axis values are known. That is, $y_{j}=j$, where $j$ is the index of sections. The $x$ and $z$ values are updated with the same procedure.

$$
\text { individual }=\left[\begin{array}{l}
x_{1}, x_{2}, \ldots, x_{D i m} \\
y_{1}, y_{2}, \ldots, y_{D i m} \\
z_{1}, z_{2}, \ldots, z_{D i m}
\end{array}\right]
$$

In traditional FHH algorithm's model building step, search space of each variable is divided into $K$ bins. All bins have the same height. Each bin's width will change in each generation. Let $X_{i}=\left\{x_{1}, x_{2}, \ldots, x_{D i m}\right\}$, where Dim is the number of variables, $i$ is the index of individuals. First, select $S$ best individuals and sort them according to the value of the $j^{\text {th }}$ variable. Then, use Eqs. (7) and (8) to update bins.

$$
\begin{aligned}
& \text { Bin_lower }_{m}=\left\{\begin{array}{cc}
\text { lower, } & \text { if } m=0 \\
\left(x_{m \cdot S / K}+x_{m \cdot S / K-1}\right) / 2, & \text { otherwise }
\end{array}\right. \\
& \text { Bin_upper }_{m}=\left\{\begin{array}{cc}
\text { Bin_lower }_{m+1}, & \text { if } m<K-1 \\
\text { upper, } & \text { otherwise }
\end{array}\right.
\end{aligned}
$$

where Bin_lower $_{m}$ is the lower value of the $m^{\text {th }}$ bin, Bin_upper ${ }_{m}$ is the upper value of the $m^{\text {th }}$ bin, lower and upper represent search space's lower bound and upper bound respectively.

When sampling new individuals, each variable will select a bin randomly. Then use the bin's lower bound and upper bound to generate a value randomly. As shown in Fig. 2, during evolution, the bin's width is continuously changing. Figure 2(b) shows that the first bin and the last bin have larger width than others. It is little help for finding global optimum when using them to generate new individuals.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Bin's distribution in search space of one variable in different generations

In AFHH's model building step, all individuals are sorted according to the value of the $j^{\text {th }}$ variable. Then record the smallest value and the largest value of the $j^{\text {th }}$ variable with intervalLower[j] and intervalUpper[j] respectively, where intervalLower and intervalUpper are arrays whose length is Dim. After that, if AFHH finds a feasible path, which means the cost function's value is less than 2.0, parameter $p_{m}$ which is defined as Eq. (9) will be used to control whether to change search space's size of the $j^{\text {th }}$ variable [9]. Then, AFHH will use Eqs. (7) and (8) to update current bins.

$$
p_{m}=0.01+0.99 \cdot \frac{\exp \left(\frac{10 . g}{G}\right)-1}{\exp (10)-1} \in[0.01,1.00]
$$

where $g$ is the current generation, $G$ is the maximum iteration. $p_{m}$ is a nonlinear parameter. When change the search space's size, we use the mean of intervalLower [j] and Bin_lower $_{0}$ as search space's lower bound, and use the mean of intervalUpper [j] and Bin_upper $_{k-1}$ as search space's upper bound. The procedure of updating bins and sampling are the same as traditional FHH algorithm. It is illustrated in Fig. 3.

# 4 Experiments and Results 

### 4.1 Experiments Setup

The real underwater environment is simulated like the ones in Fig. 4. The area is 20 m long, 40 m width and 20 m depth. Four scenarios are used to measure AFHH's performance. AFHH, FHH, PSO, enhance differential evolution with random walk (RWDE) [12], and ADE [7] are used to make a comparison of their ability on path planning [7]. For the FHH and AFHH algorithms, bins size $K$ is set as 50 , and $S$ is set as 100. The PSO is a conventional global topology PSO variant, whose $w$ is set as 0.5 . $c_{1}$ and $c_{2}$ are both set as 2.0. For the RWDE algorithm, two pairs of fixed parameters are used $(F=0.5, C R=0.1 ; F=0.1, C R=0.5)$. All algorithms use the same maximum function evaluations (FEs) 5000000, and the same population's size 200. All results are got after 30 times independently run. All algorithms are implemented on a PC with Intel core i7 processor running 3.6 GHz , RAM of 8 GB .

```
Procedure of AFHH's Model Building
    01 Begin
    02 Load current scenario's map;
    03 Initialize the population;
    04 While (Not Stop)
        //model building
        While \((j<\operatorname{Dim})\)
        Find the biggest and smallest values from \(j^{16}\) variables;
        intervalUpper \([j]=\) biggest value; \(\quad\) intervalLower \([j]=\) smallest value;
        Sort \(S\) best individuals' \(j^{16}\) variable from small to large;
        //Decide whether to shrink the search space of \(j^{16}\) variable
        If ((current best fitness value \(<2.0\) ) and \(\left(\operatorname{random}(0,1)<p_{w}\right)\) )
            lower \([j]=\) intervalLower \([j] ; \quad\) upper \([j]=\) intervalUpper \([j]\);
        End of If
        Use Eq. (7) and Eq. (8) to update \(j^{16}\) variable's bins;
        End of While
        //generate New Individuals
        If \(\left((g e n \% T==0\right)\) and \((g e n!=0)\)
        Use current search space randomly generate new individuals;
        Else
            While \((i<N P)\)
            Randomly select a bin for each variable to generate new variable;
            Use new variables to form the \(i^{16}\) individual;
            Calculate the \(i^{16}\) individual's cost function's value;
            End of While
        End of If
        Select \(N P\) best individuals to form new population;
    27 End of While
    28 End
```

Fig. 3. Procedure of the proposed AFHH algorithm for path planning
![img-4.jpeg](img-4.jpeg)
(a) Scenario 1
![img-5.jpeg](img-5.jpeg)
(b) Scenario 2
![img-4.jpeg](img-4.jpeg)
(c) Scenario 3
![img-5.jpeg](img-5.jpeg)
(d) Scenario 4

Fig. 4. The 3-D static environment models we simulate.

# 4.2 Results Comparisons 

In Table 1, the first column represents different scenario, the second column fills with start points and target points. The mean and standard deviation of 30 independently runs of a path are calculated. Values in brackets are standard deviation. Results in Table 1 show that the proposed AFHH algorithm performs better than other algorithms in most cases. Besides, it is steadier in all independent runs. If a path is feasible, the value of cost function will be less than 2.0 , and the smaller the better. As shown in

Table 2, although the AFHH algorithm can obtain high quality paths, it runs slowest in all scenarios. Because AFHH needs more time to construct probability model. PSO runs fastest in all scenarios, but it can't obtain feasible paths.

As shown in Fig. 5, AFHH converge faster than other algorithms in all scenarios. It has steady performance in all scenarios. Besides, AFHH not only converges faster, but also gets better results. The FHH can also get feasible paths, but it needs more iterations. Moreover, it is not steady sometimes. PSO performs worst, it can't find feasible path in all scenarios. The ADE can find feasible path. However, it needs more generations. Moreover, it is not steady sometimes. The RWDE with different parameters can also get good results in all scenarios, but it needs more iterations.

Table 1. Experimental results on AFHH, FHH, PSO, RWDE, and ADE with different scenarios
Table 2. Computation time of AFHH, FHH, PSO, RWDE, and ADE in different scenarios
![img-6.jpeg](img-6.jpeg)

Fig. 5. All algorithms' convergence property in different scenarios

# 5 Conclusions 

In this paper, we propose the AFHH algorithm, which has good convergence rate and better performance. Many earlier works used GA, DE and PSO to make path planning. We find that EDAs can also complete this mission well. Maybe when use EDAs to solve path planning problems, parameters or properties of EDAs should change corresponding to problems. As the results shown in Sect. 4, AFHH needs more computation time to obtain high quality paths. This weakness is to be optimized in future works. Besides, the ability of EDAs to make path planning in dynamic environment should be checked.

Acknowledgments. This work was partially supported by the National Natural Science Foundations of China (NSFC) with Nos. 61772207 and 61332002, the Natural Science Foundations of Guangzhou Province for Distinguished Young Scholars with No. 2014A030306038, the Project for Pearl River New Star in Science and Technology with No. 201506010047, the GDUPS (2016), and the Fundamental Research Funds for the Central Universities.
