# An estimation of distribution algorithm and new computational results for the stochastic resourceconstrained project scheduling problem 

Chen Fang $\cdot$ Rainer Kolisch $\cdot$ Ling Wang $\cdot$ Chundi Mu

Published online: 13 January 2015
(c) Springer Science+Business Media New York 2015


#### Abstract

In this paper we propose an estimation of distribution algorithm (EDA) to solve the stochastic resource-constrained project scheduling problem. The algorithm employs a novel probability model as well as a permutation-based local search. In a comprehensive computational study, we scrutinize the performance of EDA on a set of widely used benchmark instances. Thereby, we analyze the impact of different problem parameters as well as the variance of activity durations. By benchmarking EDA with state-of-the-art algorithms, we can show that its performance compares very favorably to the latter, with a clear dominance in instances with medium to high variance of activity duration.


Keywords Stochastic resource-constrained project scheduling $\cdot$ Estimation of distribution algorithm $\cdot$ Permutation-based local search $\cdot$ Impact of problem parameters

## 1 Introduction

The stochastic resource-constrained project scheduling problem (SRCPSP) is concerned with scheduling a set of precedence related activities with stochastic durations subject to scarce resources, such that the expected duration of the project (makespan) is minimized (see, e.g., Herroelen and Leus 2005). In case of deterministic activity durations the SRCPSP reduces to the RCPSP. The latter has

[^0]
[^0]:    C. Fang $\cdot$ L. Wang $\cdot$ C. Mu

    Tsinghua National Laboratory for Information Science and Technology (TNList), Department of Automation, Tsinghua University, Beijing 100084, China
    R. Kolisch ( $\square$ )

    TUM School of Management, Technische Universität München, Arcisstr. 21, 80333 Munich, Germany
    e-mail: rainer.kolisch@tum.de

been shown by Blazewicz et al. (1983) to be NP-hard. Research on the RCPSP has long been employed and its outcome is comprehensive (see for example Brucker et al. 1999; Neumann et al. 2003; Kolisch and Hartmann 2006 as well as Hartmann and Briskorn 2010). However, solving the RCPSP is of limited use for the SRCPSP due to the following reasons. Firstly, a schedule which provides a start time for each activity cannot be employed in the case of stochastic activity durations. Secondly, Heller (1981) shows that project duration is systematically underestimated if the RCPSP is solved for expected activity durations instead of obtaining the expected project duration, subject to the distribution of the activity durations, i.e. $C_{\max }\left(E\left(d_{1}\right), \ldots, E\left(d_{J}\right)\right) \leq E\left(C_{\max }\left(d_{1}, \ldots, d_{J}\right)\right)$. The difference between $C_{\max }$ $\left(E\left(d_{1}\right), \ldots, E\left(d_{J}\right)\right)$ and $E\left(C_{\max }\left(d_{1}, \ldots, d_{J}\right)\right)$ may become arbitrarily large with increasing number $J$ of activities and increasing variances of activity durations. Thirdly, project planners are not only interested in the expected project makespan but in more informative measures such as the entire distribution of the project makespan or value at risk measures. Hence, there is a legitimate interest in conducting research on the SRCPSP. Nevertheless, research on this topic is still limited.

For solving the SRCPSP, one has to resort to so-called scheduling policies (see Möhring et al. 1984) to which we will also refer simply as policies in the following. The latter transforms a scenario, which for each activity yields a duration drawn from the distribution function of that activity into a schedule, i.e. a start time for each activity. Stork (2000) provides a survey of different classes of policies including information on dominance relationships. For heuristics, two policy classes-neither of which predominates-are most common: Activity-based policies and resource-based policies. Stork (2001) has shown that when interpreted as a function which maps a vector of activity durations into a vector of activity start times resource-based policies are neither monotone nor continuous. As a consequence, the majority of researchers have refrained from employing resource-based policies.

Tsai and Gemmill (1998) proposed a tabu search algorithm for solving the RCPSP and the SRCPSP using resource-based policies, although the latter are not explicitly mentioned by the authors. Stork (2000) developed an exact branch-andbound algorithm for solving the SRCPSP employing three different classes of policies, amongst them activity-based policies. Ballestin (2007) proposed a genetic algorithm (GA) for the SRCPSP which employs activity-based policies. His computational results show that there is a considerable gap between the deterministic makespan $C_{\max }\left(E\left(d_{1}\right), \ldots, E\left(d_{J}\right)\right)$ and the expected makespan $E\left(C_{\max }\left(d_{1}, \ldots, d_{J}\right)\right)$ for the RCPSP which is increasing with increasing variance of the activity durations. These findings are in line with the results of Heller (1981). Ballestin and Leus (2009) developed a greedy randomized adaptive search procedure (GRASP) which employs activity-based policies. They examined various objective functions related to timely project completion as well as their correlation. They also studied the distribution of the makespan as obtained by GRASP showing that in most cases, all activity distributions, except the exponential distribution, lead to a normal distributed project makespan. Ashtiani et al. (2011) propose a new class of policies, so-called pre-processor policies, a variant of the class of resource-based

policies. They employed pre-processor policies within a genetic algorithm. Preprocessor policies make a number of prior sequencing decisions and thus add some extra precedence relations to the existing ones in order to resolve potential resource conflicts. The remaining resource conflicts are dynamically resolved by employing a resource-based policy.

The estimation of distribution algorithm (EDA) is a newly proposed algorithm framework for stochastic optimization (see Larranaga and Lozano 2002). As such it is in general suited for solving the SRCPSP. Unlike GA, which explicitly applies genetic operators such as crossover and mutation to produce a new generation, EDA reproduces a new generation implicitly by sampling from a probability distribution, which captures features of good solutions. The best solutions derived are then taken in order to further improve the probability distribution towards its ability to sample superior solutions. Thus far, EDA has been applied to a variety of optimization problems, amongst others flow-shop scheduling (see Jarboui et al. 2009), multimode resource-constrained project scheduling (see Wang and Fang 2012) and rostering (see Aickelin et al. 2007). EDA shares some common characteristics with the cross-entropy method (see Rubinstein and Kroese 2004), which has been used by Bendavid and Golany (2009) to solve a stochastic project scheduling problem different from the SRCPSP. In this paper we propose EDA to solve the SRCPSP employing the resource-based scheduling policy. The choice of the latter has been inspired by the promising results recently obtained by Ashtiani et al. (2011). Our algorithm is characterized by a novel way of defining and updating the probability distribution. Furthermore, a permutation-based local search method is applied to the best individuals to exploit their neighborhood. Computational results and comparisons with existing algorithms demonstrate the effectiveness of our EDA approach.

The remainder of the paper is organized as follows: In Sect. 2, the SRCPSP is described, and in Sect. 3, the proposed EDA is introduced. Computational results and comparisons are provided in Sect. 4. Finally, we end the paper with some conclusions in Sect. 5.

# 2 Definitions and problem statement 

### 2.1 The stochastic RCPSP

The (deterministic) RCPSP is concerned with the scheduling of project activities to minimize the project's makespan. The RCPSP can be stated as follows. A project consists of $J$ activities labeled $j=1, \ldots, J$, where the deterministic duration of activity $j$ is denoted by $d d_{j}$. There exist precedence relationships between some activities of the project. This relationship is given by sets of immediate predecessors $P_{j}$ indicating that an activity $j$ may not be started before any of its predecessors $i \in P_{j}$ is completed, which can be denoted as $i \prec j$. The set of renewable resources is referred to as $K$. For each resource $k \in K$, the per-period-availability $R_{k}$ is assumed to be constant. Activity $j$ requires $r_{j k}$ units of resource $k$ in each period of its nonpreemptable duration. The activities $j=0$ and $j=J+1$ are dummy activities,

which represent the start and end of the project, respectively. It is assumed that the dummy activities do not require any resources and their durations are equal to zero. The set of all activities including the dummy activities is denoted as $J^{+}=\{0, \ldots, J+1\}$. The most common objective is to minimize the makespan of the project; this objective is also considered in our paper. The RCPSP can also be represented by a directed acyclic graph $G(N, A)$, where the set of nodes $N$ denotes the activities of the project and the set of $\operatorname{arcs} A$ contains all the $\operatorname{arcs}(i, j)$ where $i, j \in J^{+}, i \prec j$. A solution for the deterministic RCPSP is a schedule $s=$ $\left(s_{0}, s_{1}, \ldots, s_{J+1}\right)$ which is a vector of start times of activities. A schedule is feasible if the precedence constraint and resource constraint are guaranteed.

Heuristics for RCPSP usually encode the schedule with some representation, for example an activity list. A schedule generation scheme (SGS) is then used to transform the representation to a schedule. Two SGS procedures are used in literature: the parallel SGS and the serial SGS (see Kolisch 1996 as well as Kolisch and Hartmann 1999 for details).

In the Stochastic RCPSP (SRCPSP), the duration $D_{j}$ of each activity $j \in J^{+}$is a random value which follows a known probability distribution. The vector $\left(D_{0}, D_{1}, \ldots, D_{J+1}\right)$ is denoted by $D$. For the activities $j=0, J+1, P\left[D_{j}=0\right]=1$; for the activities $j=1, \ldots, P\left[D_{j}<0\right]=0$ (where $P[e]$ represents the probability of event $e$ ), we use vector $d=\left(d_{0}, d_{1}, \ldots, d_{J+1}\right)$ to represent one particular scenario (also termed sample or realization).

# 2.2 Scheduling policies 

In the stochastic RCPSP, we can no longer use a vector of start times of activities to represent a solution because we do not know the exact duration of each activity before it has been finished. As a result, a scheduling policy is needed to decide which activity to choose at each decision time. Decision times are $t=0$ (the start time of the project) and the finishing times of activities. For each decision time $t$, only information which has become available up to $t$ can be used to make the decision (non-anticipativity constraint, see e.g. Stork 2001). That means we can only know the durations of activities which have been finished up to time $t$. After all activities are completed, we obtain a scenario $d$ from the random duration vector $D$. Consequently, every policy $\pi$ may alternatively be interpreted as a function $\pi$ : $R_{J+2}^{+} \rightarrow R_{J+2}^{+}$that maps a given scenario $d$ to start times of activities (schedules) $s(d, \pi)$ (Stork 2000). For a given sample $d$ and scheduling policy $\pi, s_{J+1}(d, \pi)$ denotes the makespan of the project. The objective for the SRCPSP is to select a policy $\pi^{*}$ which minimizes the expected makespan $E\left[s_{J+1}\left(D, \pi^{*}\right)\right]$.

Various classes of policies have been proposed for the SRCPSP. Some wellknown classes of policies are earliest-start policies ( $\Pi^{E S}$ ), preselective policies $\left(\Pi^{P S}\right)$, linear preselective policies $\left(\Pi^{L P S}\right)$, resource-based policies $\left(\Pi^{R B}\right)$, activitybased policies $\left(\Pi^{A B}\right)$, and pre-processor policies $\left(\Pi^{P P}\right)$, (see Stork 2001; Ashtiani et al. 2011).

The policy classes $\Pi^{E S}, \Pi^{P S}$ and $\Pi^{L P S}$ are based on the so-called minimal forbidden sets (see Stork 2000 for details). Since the number of minimal forbidden

sets grows exponentially with the number of activities, the computational time becomes unacceptable when dealing with practical project scheduling problems. As a result, policies which do not need the calculation of minimal forbidden sets should be adopted when dealing with real size projects. These are resource-based policies, activity-based policies and pre-processor policies. As will be shown, each of these policies operates in a specific way with an activity list. Hence, with $\pi$ we denote activity list and policy interchangeably.

A resource-based policy $\pi \in \Pi^{R B}$ considers at any decision time $t$ the not yet started activities in the order of activity list $\pi$. At $t$, some activities will have finished, some activities will be active (that is, they have started but are not yet finished), and some activities will not yet have started. The policy selects the first activity on the list which has not started, whose predecessors in the activity network have already been completed, and for which there is enough capacity left in order to be processed at $t$. This activity is started at $t$. Further activities are selected to start at $t$ until no activity is available any more. Then, the new decision time $t^{\prime}$ is increased to the next finish time of one of the activities which have been active or started at $t<t^{\prime}$. The counterpart of a resource-based policy for the RCPSP is the parallel SGS. Stork (2001) has shown that policies from the class $\Pi^{R B}$, when viewed as function which maps a vector of activity durations into a vector of activity start times, are not always monotone or continuous. That is, the makespan may increase although activity durations are decreasing (so-called Graham anomalies, see Graham 1966).

An activity-based policy $\pi \in \Pi^{A B}$ schedules activities as early as possible in the order of an activity list $\pi$ but adds the side constraint that $s_{i}(d) \leq s_{j}(d)$ if $i \prec_{\pi} j$ for each scenario $d . i \prec_{\pi} j$ denotes that activity $i$ precedes activity $j$ in activity list $\pi$. The side constraint is necessary to prevent activity $j$ from delaying activity $i$, although there is $i \prec_{\pi} j$. Ballestin (2007) speaks of activity-based policies as "stochastic serial SGS" which equals the deterministic serial SGS with the additional side constraints. Sprecher (2000) shows that when employing the activity-based policy to the (deterministic) RCPSP there will always be one activity list which leads to the minimum makespan.

Pre-processor policies $\Pi^{P P}$ (see Ashtiani et al. 2011) combine unconditional sequencing decisions as made by earliest-start policies $\Pi^{E S}$ with the real-time dispatching features of resource-based policies $\Pi^{R B}$. For this, a pre-process is employed to define extra arcs which are added to the original directed acyclic graph $G(N, A)$.

Since the aim of this paper is to develop an algorithm to solve real size projects, we cannot employ policies from the classes $\Pi^{E S}, \Pi^{P S}$ and $\Pi^{L P S}$ which are based on the minimal forbidden sets. Thus we have to resort to one of the policy classes $\Pi^{R B}$, $\Pi^{A B}$ or $\Pi^{P P}$. Based on the observation of Ashtiani et al. (2011) and Fliedner (2011), which showed that policies from the class of resource-based policies performed on average better than policies from the class of activity-based policies, we employ the class of resource-based policies.

# 3 Estimation of distribution algorithm for the SRCPSP 

The estimation of distribution algorithm (EDA) is an evolutionary metaheuristic which has its theoretical foundation in probability theory. For foundations of EDA see Larranaga and Lozano (2002). EDA has been used for a variety of different problems (see Larranaga and Lozano 2002). A number of papers employ estimation of distribution algorithms for scheduling problems. Jarboui et al. (2009) and Zhang and $\mathrm{Li}(2011)$ consider the permutation flow shop problem with a minimizing total flow time objective, and Aickelin and Li (2007) as well as Aickelin et al. (2007) treat nurse scheduling and nurse rostering, respectively. Pan and Ruiz (2012) consider makespan minimization for the lot-streaming flow shop problem with setup times. Finally, Wang and Fang (2012) address makespan minimization for multimode resource-constrained project scheduling.

In contrast to the genetic algorithm (GA), EDA does not directly generate new solutions by crossover of parent solutions and mutations but by sampling from a probability distribution. The latter depicts the features of a selected set of feasible solutions of the problem. The probability distribution is the core of EDA and termed there as a probability model. In case of an optimization problem with unrelated variables, where each variable can take on a value independently of the value of the other variables, the probability distribution can be immediately derived from the solution itself. For example, the probability distribution for an unconstrained binary optimization problem $\max f(x)$ subject to $x \in\{1,0\}$ could be a vector $p$ of the size of $x$ where $p_{i}$ is the parameter of the Bernoulli distribution of variable $x_{i}$. However, when variables are interrelated by constraints, the probability distribution is defined for an encoding of the solution instead of the solution itself. An encoding for the RCPSP can be, for example, an activity list. The probability distribution of a list could then be a $J \times J$ matrix which gives for each element $(i, j)$ the probability that activity $i$ is placed at position $j$ of the list (see Wang and Fang 2012). In this paper we define the probability distribution for a matrix $X$ which states for each pair of activities $(i, j)$ whether activity $i$ is placed before activity $j$ on the list or not. Details of the definition of the probability distribution are provided in Sect. 3.2. Using the probability distribution for matrix $X$, we can sample activity lists and thus solutions. Now, starting with some initial probability distribution for matrix $X$, in each generation EDA samples a number of activity lists and selects an elite set of lists with the best objective function value. The lists in this set are further improved by applying a simple local search procedure. The resulting elite set of lists is then employed in order to update the probability distribution of the next generation. The aim is to improve the estimate of the probability distribution over the generations in terms of its ability to breed high quality solutions. We will now provide the details for the procedure in Sects. 3.1-3.7.

### 3.1 Representation and fitness function

As a generalization of RCPSP, SRCPSP also shares most of the characteristics of RCPSP. Kolisch and Hartmann (1999) concluded from experimental tests that

procedures for solving the RCPSP based on the activity list representation yield good results. Inspired by this observation, we adopted the activity list representation to encode individuals. Let us denote the activity list as $\pi=\left[a_{0}, a_{1}, \ldots, a_{J+1}\right]$ where $a_{j}$ is the activity on position $j$ of the list.

As fitness value of an activity list $\pi$ we use the expected makespan which we approximate by the average makespan of $n$ scen scenarios

$$
\operatorname{fitness}(\pi)=\frac{1}{n \operatorname{scen}} \sum_{n=1}^{n \operatorname{scen}} s_{J+1}\left(d^{n}, \pi\right)
$$

Ballestin (2007) showed that for a fixed number of generated schedules $s\left(d^{n}, \pi\right)$ using less scenarios $n$ scen is beneficial because more individuals can be evaluated. Following Ballestin and Leus (2009) we choose $n$ scen $=10$ to evaluate an activity list during the search procedure.

# 3.2 Probability model 

As stated at the beginning of Sect. 3, we use an activity list solution representation in order to build the probability model. Let $X$ be a $J \times J$ binary random variable matrix which can be defined as

$$
X=\left(\begin{array}{ccc}
X_{11} & \cdots & X_{1 J} \\
\vdots & \ddots & \vdots \\
X_{J 1} & \cdots & X_{J J}
\end{array}\right)
$$

with

$$
X_{i j}= \begin{cases}1, & \text { if activity } i \text { is placed before activity } j \text { in activity list } \pi \\ 0, & \text { else }\end{cases}
$$

Accordingly, we can map an activity list $\pi$ to $X$ with a function $\{0,1, \ldots, J+1\}^{J+2} \mapsto\{0,1\}^{J \times J}:$

$$
X=f(\pi)
$$

Let us illustrate $X=f(\pi)$ by mapping activity list $\pi=[2,1,3]$ into matrix $X=\left(\begin{array}{lll}0 & 0 & 1 \\ 1 & 0 & 1 \\ 0 & 0 & 0\end{array}\right)$. Since for a feasible activity list, activity $i$ is placed before activity $j$ or vice versa, $X_{i, j}+X_{j, i}=1$ holds for any two activities $i, j, i \neq j$. Furthermore, $X$ contains the transitive closure obtained from a graph which depicts the linear order of the activities in $\pi$ and thus has $\frac{J \cdot(J-1)}{2}$ non-zero entries, whereas $\pi$ requires $J+2$ entries only. Since the entries in $X$ are in $\{0,1\}$, it follows immediately that the sum of all entries in $X$ is $\frac{J \cdot(J-1)}{2}$.

We can now define the probability matrix

$$
\phi=\left(\begin{array}{ccc}
p\left(X_{11}=1\right) & \ldots & p\left(X_{13}=1\right) \\
\vdots & \ddots & \vdots \\
p\left(X_{J 1}=1\right) & \ldots & p\left(X_{J J}=1\right)
\end{array}\right)
$$

where element $p\left(X_{i j}=1\right) \in[0,1]$ represents the probability that activity $i$ is placed before $j$ in the list. Since the probability matrix will change during the iteration of the EDA we denote with $\varphi_{g}$ and with $p_{g}=\left(X_{i j}\right)$ the probability matrix and element $(i, j)$ of the matrix in iteration $g$, respectively.

# 3.3 Distribution-based offspring sampling 

We can now use probability matrix $\varphi$ in order to sample activity lists and thus solutions. For this we employ a variant of the parallel SGS (see Kolisch and Hartmann 1999). Starting with the partial list $\pi=\left[\mathrm{a}_{0}=0\right]$ with activity 0 being in the first position $\mathrm{a}_{0}$, the set of eligible activities $E$ is defined. An activity $j$ is in $E$ if it is not on the list and each of its predecessors in the activity network is on the list. For each activity $j \in E$ the probability of extending the list with $j$ is calculated according to

$$
\operatorname{Prob}_{i}=\frac{\sum_{j \in E} p_{g}\left(X_{i j}=1\right)}{\sum_{i \in E} \sum_{j \in E} p_{g}\left(X_{i j}=1\right)}
$$

```
Algorithm \(\operatorname{DBOS}\left(\varphi_{g}\right)\)
\(a_{0}=0\);
for \(j=0\) to \(J\)
    for \(i=0\) to \(J+1\)
        if \(i \in E\)
            Calculate the selecting probability \(\operatorname{Prob}_{i}\) of activity \(i\) according to Eq. (6);
        else
            \(\operatorname{Prob}_{i}=0\);
    end for
    Select an activity \(m\) according to the selecting probabilities;
    \(a_{j+1}=m\);
end for
Return \(\pi=\left[a_{0}, a_{1}, \ldots, a_{J+1}\right]\)
```

Fig. 1 Procedure DBOS

and the next activity on the list is randomly selected based on Prob. To illustrate the approach let us consider a project with 3 non-dummy activities and single precedence constraint $2 \rightarrow 3$ as well as the probability matrix $\varphi=\left(\begin{array}{ccc}0 & .3 & .7 \\ .7 & 0 & .7 \\ .3 & .3 & 0\end{array}\right)$. For determining activity $a_{1}$ we have $E=\{1,2\}, \quad \operatorname{Prob}_{1}=\frac{0.3}{0.3+0.7}=0.3$ and $\operatorname{Prob}_{1}=\frac{0.7}{0.3+0.7}=0.7$. Figure 1 provides the pseudocode of distribution-based offspring sampling (DBOS).

# 3.4 Local search strategy 

In order to improve solutions we employ a permutation-based local search strategy (PBLS) which is described in Fig. 2. It employs the swap operator proposed by Hartmann (1998) by swapping the position of the $i$-th and the $(i+1)$ th activity in the list with probability Pper, if the two activities are not precedence related.

### 3.5 Updating mechanism

A population-based updating mechanism is proposed to update the probabilistic matrix $\varphi_{g}$. Firstly, in iteration $g$ the population $\Omega_{g}:\left\{\pi_{g}(1), \pi_{g}(2), \ldots, \pi_{g}(M)\right\}$ of size $M$ is generated according to the matrix $\varphi_{g}$. After evaluating the population, $Q<M$ best individuals are selected from $\Omega_{g}$ to form the elite set $\Omega_{g}^{\text {Elite }}:\left\{\pi_{g}^{E}(1), \pi_{g}^{E}(2), \ldots, \pi_{g}^{E}(Q)\right\}$. Secondly, the PBLS is employed to improve each individual of the elite set. Then, the elite set is chosen to update $\varphi_{g}$ according to equation

```
Algorithm PBLS \(\left(\pi=\left[a_{0}, a_{1}, \ldots, a_{J+1}\right]\right)\)
for \((i=1,2, \ldots, J-I)\)
    Randomly generate value rand where \(0<r a n d<1\);
    if (rand<Pper)
        if \(\left(a_{i}\right.\) is not the predecessor of \(\left.a_{i+1}\right)\)
            Swap \(a_{i}\) and \(a_{i+1}\);
            Evaluate the new \(\pi\);
            if (fitness value is improved)
                Record current \(\pi\) and fitness value;
            end if
            end if
        end if
    end for
return \(\pi\)
```

Fig. 2 Procedure of PBLS

$$
\varphi_{g+1}=(1-\beta) \cdot \varphi_{g}+\beta \cdot \frac{1}{Q} \sum_{q \in \Omega_{g}^{\text {Elite }}} I_{g}(q)
$$

where $\beta$ is the learning speed and $I_{g}(q)$ is the frequency matrix of the $q^{\text {th }}$ individual of $\Omega_{g}^{\text {Elite }}$ in generation $g$ which is defined as

$$
I_{g}(q)=\left(\begin{array}{ccc}
\delta_{11 g}(q) & \cdots & \delta_{1 J g}(q) \\
\vdots & \ddots & \vdots \\
\delta_{J 1 g}(q) & \cdots & \delta_{J J g}(q)
\end{array}\right)
$$

employing the frequency function $\delta_{i j g}(q)$ according to:
$\delta_{i j g}(q)=\left\{\begin{array}{l}1, \text { if activity } i \text { is placed before activity } j \text { in the } q^{\text {th }} \text { individual of } \Omega_{g}^{\text {Elite }} \text { in generation } g ; \\ 0, \text { else. }\end{array}\right.$
Note that the updating mechanism always maintains the characteristic $p\left(X_{i j}=1\right)+p\left(X_{j i}=1\right)=1$ of $\varphi$. In contrast to $X$, the number of non-zero entries is not limited to $\frac{J \cdot(J-1)}{2}$ but typically is $J \cdot(J-1)$.

# 3.6 Initial population 

Hartmann $(1998,2002)$ has shown that it is advantageous to generate an initial population with the regret-based biased random sampling method of Kolisch (1996) using the latest finish time (LFT) priority rule. Following this advice, we generate an initial population $\Omega_{\text {Init }}$. For each of the $q=1, \ldots, M$ activity lists $\pi_{\text {Init }}(q)$ we obtain the frequency matrix $I_{\text {Init }}(q)$ according to Eqs. (8)-(9). In order to balance quality and diversity for the initial probability matrix $\varphi_{0}$ we blend these frequency matrices with the uniform probability matrix

$$
\varphi_{\text {uniform }}=\left(\begin{array}{ccccc}
0 & 0.5 & \cdots & 0.5 \\
0.5 & \ddots & \ddots & \vdots \\
\vdots & \ddots & \ddots & 0.5 \\
0.5 & \cdots & 0.5 & 0
\end{array}\right)
$$

by employing Eq. (7) with parameter $\beta$

$$
\varphi_{0}=(1-\beta) \cdot \varphi_{\text {uniform }}+\beta \cdot \frac{1}{M} \sum_{q \in \Omega_{0}} I_{\text {Init }}(q)
$$

Note that for the probability matrix of each generation the sum of all entries of $\varphi$ is $\frac{J \cdot(J-1)}{2}$.

# 3.7 EDA-procedure for the SRCPSP 

Employing the building blocks presented above, we can now give the overall description of EDA for solving the SRCPSP in Fig. 3.

## 4 Computational results

### 4.1 Problem instances

We coded the proposed algorithm in C++ using Microsoft Visual Studio 2005. All the experiments were performed on an IBM Thinkpad T61 with a Core 2 T7500 2.2 GHz processor. We used the standard RCPSP dataset J120 from the PSPLIB (see Kolisch and Sprecher 1996) for testing. The problem set J120 contains 600 instances with 120 activities each.

We follow Stork (2001), Ballestin and Leus (2009) and Ashtiani et al. (2011) in the choice of the probability distribution types, means, and variances. The deterministic processing times $d^{*} \in \mathrm{~N}^{J}$ that appear in J 120 are taken as the expected values for the stochastic duration. We work with five distributions: two continuous

```
Algorithm EDA
Generate the initial population \(\Omega_{\text {init }}:\left\{\pi_{\text {init }}(1), \pi_{\text {init }}(2), \ldots, \pi_{\text {init }}(M)\right\}\)
Generate the initial probability matrix \(\varphi_{0}\) according to Eq. (11);
\(\pi^{\text {best }}=\pi_{\text {init }}(1)\);
\(g=0\);
do
    for \(i\) to \(M\)
        \(\pi_{g}(i)=D B O S\left(\varphi_{g}\right) ;\)
    end for
    Evaluate the population \(\Omega_{g}:\left\{\pi_{g}(1), \pi_{g}(2), \ldots, \pi_{g}(M)\right\}\) according to Eq. (1);
    Select the Q best individuals to form the elite set \(\Omega_{g}^{\text {Elite }}:\left\{\pi_{g}^{E}(1), \pi_{g}^{E}(2), \ldots, \pi_{g}^{E}(Q)\right\}\);
    for \(i\) to \(Q\)
        \(\pi_{g}^{E}(i)=P B L S\left(\pi_{g}^{E}(i)\right)\);
        if fitness \(\left(\pi_{g}^{E}(i)\right)<\) fitness \(\left(\pi^{\text {best }}\right)\)
            \(\pi^{\text {best }}=\pi_{g}^{E}(i)\)
        end if
    end for
    Generate the probability matrix \(\varphi_{g+1}\) according to Eqs. (7)-(9);
    \(g++\)
while (Stopping condition is not met)
return \(\pi^{\text {best }}\)
```

Fig. 3 EDA for the SRCPSP

uniform distributions with intervals $\left[d_{i}^{*}-\sqrt{d_{i}^{*}} ; d_{i}^{*}+\sqrt{d_{i}^{*}}\right]$ and $\left[0 ; 2 d_{i}^{*}\right]$; one exponential distribution with mean $d_{i}^{*}$; and two beta distributions with variance $d_{i}^{*} / 3$ and $d_{i}^{* 2} / 3$, both with support $\left[d_{i}^{*} / 2 ; 2 d_{i}^{*}\right]$. In the following, we will refer to these five distributions as U1, U2, Exp, B1, and B2, respectively. The variance of these distributions is $d_{i}^{*} / 3, d_{i}^{* 2} / 3, d_{i}^{* 2} d_{i}^{*} / 3$, and $d_{i}^{* 2} / 3$, respectively. That means that U1 and B1 have relatively little variability, U2 and B2 have medium variability, and Exp has large variability. The parameters $(\alpha, \beta)$ of the beta distribution are $\left(d_{i}^{*} / 2-1 / 3, d_{i}^{*}-2 / 3\right)$ and $(1 / 6,1 / 3)$ for B 1 and B 2 , respectively.

We evaluate the quality of the algorithm by the average percentage deviation of $E\left[s_{J+1}(D, \pi)\right]$ from the critical path length with the deterministic durations $d^{*}$. The expected makespan is obtained by mean of a simulation with 1,000 replications. In order to compare different algorithms fairly, computational effort is measured by the number of generated schedules, which is 5,000 and 25,000 (see Kolisch and Hartmann 2006). Solving one scenario with a resource-based policy will be counted as one generated schedule.

# 4.2 Setting the parameters of the EDA 

We used the Taguchi method of design of experiment (see Montgomery 2009) to determine a set of suitable parameters for the EDA. From the J120 dataset we chose 60 instances according to $\mathrm{X} p \_q$.RCP, where $p=1,2, \ldots, 60$ and $q=p-\left\lfloor\frac{p-1}{10}\right\rfloor \times 10$. For each of these instances we chose the U2 distribution since it has a medium level of variability.

The EDA contains four key parameters: the population size of each generation $(M)$, the size of the elite set $(Q)$, the PBLS acceptance rate (Pper), and the learning speed $(\beta)$. With the five levels for each parameter given in Table 1 and using an orthogonal array $L_{25}\left(5^{4}\right)$, we obtain 25 parameter combinations. Each of the 60 instances is solved with each parameter combination and a maximum number of 5,000 and 25,000 schedules as stopping condition. The response $R$ for each parameter combination and stopping criterion is the average deviation of the makespan obtained by the thus parameterized EDA from the critical path based lower bound LB of the instance with deterministic activity durations $d^{*}$.

$$
R=\frac{1}{60} \sum_{i=1}^{60} \frac{\left(\text { Makespan }_{i}-L B_{i}\right)}{L B_{i}}
$$

Table 1 Combinations of parameter values
Figures 4 and 5 present the main effect of the parameter variations on the solution quality. It can be seen that the main effect is rather moderate. Based on the results we set the parameter to $M=150, Q=1 \% \mathrm{M}, \operatorname{Pper}=0.5$ and $\beta=0.3$ for the following experiments.

# 4.3 The impact of the project characteristics and distribution types 

In this section, we analyze the impact of project characteristics on the performance of the proposed EDA. According to Kolisch and Hartmann (1999), a full factorial design of the variable parameters including network complexity ( $N C$ ) (3 levels), resource factor $(R F)$ (4 levels), and resource strength $(R S)$ (5 levels) with 10 replications per cell is adopted to generate a total of $3 \times 4 \times 5 \times 10=600$ benchmark problems for J120. NC is the average number of non-redundant arcs per node, including the dummy start and finish activity. $R F \in[0,1]$ gives the average percentage of resources requested per activity, while $R S \in[0,1]$ measures the strength of the resource constraints, where low values indicate that resource constraints are tight. Besides the distributions U1, U2, Exp, B1, and B2 we also adopt the deterministic case (Deter) for comparison. Only 1 scenario (nscen $=1$ ) is needed for calculating the fitness value of an activity list for the deterministic case, whereas 10 scenarios (nscen $=10$ ) are used for calculating each fitness value for U1, U2, Exp, B1, and B, respectively. For a fair comparison, 500 schedules and 2,500 schedules are adopted as the stopping conditions for Deter. Tables 2 and 3 as well as Fig. 6 provide information on the average percentage deviation of EDA from the deterministic critical path based lower bound with deterministic durations with respect to the levels of problem parameters and the distribution functions. There are a number of observations which can be made. Firstly, the average
![img-0.jpeg](img-0.jpeg)

Fig. 4 Factor level trend with 5,000 schedules

![img-1.jpeg](img-1.jpeg)

Fig. 5 Factor level trend with 25,000 schedules

Table 2 Average percentage deviation for different project parameters and distributions (5,000 schedules)
deviation from the lower bound (Ave.LB.Dev) increases with increasing variance of the distribution function. This effect is consistent for all problem parameters and parameter levels and confirms the results of Heller (1981) and Ballestin (2007). Secondly, the type of distribution function does not have an impact but the variance of the distribution does. This can be observed for the uniform distribution U1 and

Table 3 Average percentage deviation for different project parameters and distributions (25,000 schedules)
![img-2.jpeg](img-2.jpeg)

Fig. 6 Average percentage deviation for different project parameters and distributions

the beta distribution B1 which have the same variance of $d_{i}^{*} / 3$. Thirdly, the average deviation from the lower bound increases for increasing resource factor $R F$, i.e. more resources are requested by an activity, and decreasing resource strength $R S$, i.e. scarcer resources. These findings are basically in line with observations on the impact of the problem parameters on the RCPSP (see Kolisch 1995). The impact of the network complexity $N C$ is not as clear. While there is no impact when increasing $N C$ from 1.5 to 1.8 , there is a decrease of the average deviation from the lower bound when $N C$ is increased from 1.8 to 2.1 . This effect deviates from previous findings for the deterministic case where Kolisch (1995) did not observe a significant impact from the $N C$ on the performance of priority rule based heuristics. However, Kolisch (1995) measured the deviation from the optimal solution while, due to the size of the problems, we are measuring the deviation from the critical path based lower bound. In order to analyze the impact of the lower bound in more detail, Table 4 provides the critical path based lower bound (LB) and the upper bound (UB) generated by the proposed EDA for different project parameters for the deterministic case. Based on the results listed in Table 4, the impacts of different project parameters are illustrated in Figs. 7, 8 and 9. Figure 7 shows that the $N C$ has an impact on both the LB and the UB. When $N C$ increases, LB and UB increase as well. The reason is that additional (non-redundant) precedence relations lead to an increase in the length of the critical path of the project (LB) as well as a resourcefeasible project makespan (UB). Interestingly, the slope of LB decreases for increasing $N C$, while the slope of UB increases. That is, from a medium level of $N C$ on, the impact of additional precedence relations on the critical path decreases noticeably, while the impact on the resource feasible makespan increases mildly.

Table 4 LB and UB for different project parameters (deterministic case)
Fig. 7 The impact of NC on LB and UB
![img-3.jpeg](img-3.jpeg)

Fig. 8 The impact of RF on LB and UB
![img-4.jpeg](img-4.jpeg)

Fig. 9 The impact of RS on LB and UB
![img-5.jpeg](img-5.jpeg)

This gives evidence for the assumption that the increase in Ave.LB.Dev when increasing $N C$ from 1.8 to 2.1 does not primarily stem from a poor performance of EDA, but from the decreasing impact on the critical path based lower bound. Figures 8 and 9 show that the effect of the two resource parameters $R F$ and $R S$ on

the critical path based lower bound is null, which is as expected. The impact of $R F$ and $R S$ on the upper bound is considerable.

# 4.4 Performance comparison with other heuristics 

In this section, we compare the EDA with the state-of-the-art algorithms for the SRCPSP. The algorithms compared include the genetic algorithm of Ballestin (2007), denoted as ABGA, the greedy randomized adaptive search procedure proposed by Ballestin and Leus (2009), denoted as ABGR, and the two-phase genetic algorithm of Ashtiani et al. (2011), denoted as PPGA. The comparison results are depicted in Tables 5 and 6 where the best performance for each distribution is set in bold.

Tables 5 and 6 reveal that the EDA outperforms the ABGA and PPGA in all cases. Like the PPGA, the EDA outperforms the ABGR in the medium and highvariability cases (U2, Exp and B2). However, the ABGR is slightly better than the EDA for low variability (U1 and B1). Since ABGR employs an activity-based policy and EDA employs a resource-based policy this might be an indication for the superiority of activity-based policies for problems with small variability of activity durations. This conjecture is backed up by theoretical and experimental results for the deterministic case, i.e. the extreme case of the SRCPSP where variability converges to zero. There, Sprecher (2000) has proven that when scheduling activity lists according to the serial scheduling scheme with side constraints $s_{i}(d) \leq s_{j}(d)$ if $i \prec_{\pi} j$, which is the deterministic counterpart of the activity-based scheduling policy, there is always one activity list with minimum makespan. Kolisch (1996) has proven that the parallel schedule generation scheme, the deterministic counterpart of the resource-based policy, searches in the set of nondelay schedules which does not

Table 5 Comparison with other algorithms (5,000 schedules)
Table 6 Comparison with other algorithms (25,000 schedules)
always include an optimal solution. Kolisch and Hartmann (2006) have experimentally shown that heuristics which employ the serial schedule generation scheme perform better than heuristics which use the the parallel schedule generation scheme, if the runtime and thus the number of generated schedules is sufficiently large.

# 5 Conclusion and future work 

In this paper, we proposed the estimation of distribution algorithm (EDA) for the stochastic resource-constrained project scheduling problem (SRCPSP). The EDA utilizes the statistic information obtained from the elite individuals of the former generation to predict the promising area in the searching space. By adopting a novel probability model and an updating mechanism, the promising area could be tracked effectively. By adopting the permutation-based local search strategy (PBLS), the exploitation ability is further enhanced. Using an experimental design with orthogonal array, suitable parameter settings for the EDA were determined. Simulation results based on the PSPLIB benchmarks and comparisons with some existing algorithms demonstrated the effectiveness of the proposed EDA and the impact of problem parameters and the activity distributions on its performance. Comparing EDA to state-of-the-art heuristics for the SRCPSP, we could show that the proposed procedure is quite competitive and, indeed, yields the best performance if the variance of the activity duration is medium to large. Possible future work is to develop an adaptive EDA with a parameter learning mechanism and to develop a new class scheduling policy for the SRCPSP.

Acknowledgments This paper was written during Chen Fang's one year research stay at the TUM School of Management. The authors thank two anonymous reviewers for their valuable comments. This research has been partially supported by National Key Basic Research and Development Program of China (Grant No. 2013CB329503), National Science Foundation of China (Grant No. 61174189), and Doctoral Program Foundation of Institutions of Higher Education of China (Grant No. 20130002110057).
