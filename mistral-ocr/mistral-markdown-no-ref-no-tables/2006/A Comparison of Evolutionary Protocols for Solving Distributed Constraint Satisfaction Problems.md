# A Comparison of Evolutionary Protocols for Solving Distributed Constraint Satisfaction Problems 

Winard R. Britt, Hurley D. Cunningham, and Gerry V. Dozier


#### Abstract

Evolutionary Computation (EC) is the field of study devoted to problem solving using simulated evolution. In this paper, evolutionary operators are applied and a number of societies of hill-climbers (SoHCs), such as a genetic SoHC (GSoHC) and an evolutionary SoHC (ESoHC) are employed for solving randomly generated distributed asymmetric constraint satisfaction problems (DisACSPs). Further, we develop an Estimation of Distribution Algorithm SoHC (EDA-SoHC) variant using a uniform mutation operator. This variant produces offspring by drawing genetic material from a distribution of above-average individuals in the population.

In this paper, we compare GSoHCs using distributed restricted forms of single-point, two-point, modified two-point, and uniform crossover. The GSoHCs are also compared with an ESoHC that uses a distributed restricted form of uniform mutation and a simple SoHC which does not use any evolutionary operators. Finally, we compare the SoHC, GSoHCs, and ESoHC to the EDA-SoHC.


## I. INTRODUCTION

Evolutionary Computation [1]-[11] is the field of study devoted towards the design, development, and analysis of problem solvers based on simulated genetic and/or social evolution. Evolutionary computations (ECs) have been successfully used to solve a wide variety of problems in the areas of robotics, engineering, scheduling, planning, machine learning, constrained optimization, and constraint satisfaction just to name a few [8]-[10],[12]-[15].

In the Evolutionary Constraint Satisfaction community, we have been a migration away from pure evolutionary computations for constraint satisfaction [16] towards the hybridization of ECs with traditional CSP techniques [17][23] and /or the incorporation of heuristics and problem specific knowledge [18]-[20] ,[24]-[28] in an effort to solve CSPs more efficiently. To date, much of this research has focused on centralized CSPs. Little research has been conducted by the evolutionary constraint satisfaction community on the development of ECs for solving

Manuscript received January 31, 2006. This research was supported by the National Science Foundation under grant \#IIS-9907377.

[^0]distributed constraint satisfaction problems (DisCSPs) [29][33].

A DisCSP [29]-[37] can be viewed as a 4-tuple (X, D, C, A), where X is a set of n variables, D is a set of n domains (one domain for each of the n variables), C is a set of constraints that constrain the values that can be assigned to the n variables, and A is a set of agents for which the variables and constraints are distributed. Constraints between variables belonging to the same agent are referred to as intra-agent constraints while constraints between the variables of more than one agent are referred to as interagent constraints. The objective in solving a DisCSP is to allow the agents in A to develop a consistent distributed solution by means of message passing. The constraints are considered private and are not allowed to be communicated to fellow agents due to privacy, security, or representational reasons [34], [38]. When comparing the effectiveness of DisCSP-solvers the number of communication cycles (through the distributed algorithm) needed to solve the DisCSP at hand is more important than the number of constraint checks [34].

Many real world problems have been modeled and solved using DisCSPs [38]-[44]; however, many of these approaches use mirrored (symmetric) inter-agent constraints. Since these inter-agent constraints are known by the agents involved in the constraint, they can not be regarded as private. If these constraints were truly private then the interagent constraints of one agent would be unknown to the other agents involved in those constraints. In this case the DisCSP would be composed of asymmetric constraints. To date, with the exception of [42] and [44], little research has been done on distributed asymmetric CSPs (DisACSPs).

A simple example of a DisACSP might be attempting to schedule a meeting where a large number of the participants did not wish to reveal their personal time obligations (for security reasons, perhaps). Groups of individuals might try to resolve their time constraints with their coleagues (or "neighbors") until an actual meeting time could be determined. A similar idea is illustrated in [42].

In this paper, we demonstrate how distributed restricted forms of uniform, single-point and two-point crossover can be used for solving DisACSPs known as a society of hillclimbers (SoHC) [29]-[33]. We refer to these algorithms as genetic SoHCs (GSoHCs). We also demonstrate how distributed restricted form of mutation can be used for solving DisACSPs, we refer to this algorithm as evolutionary SoHCs (ESoHC). Further, we show how an Estimation of Distribution Algorithm based SoHC can be utilized, we refer to it as an EDA-SoHC. Our results show


[^0]:    Winard R. Britt is with the Computer Science and Software Engineering Department of Auburn University, Auburn, AL 36849. Phone: 334-5468273; e-mail: brittwr@auburn.edu).

    Hurley D. Cunningham is with the Computer Science and Software Engineering Department of Auburn University, Auburn, AL 36849; e-mail: cunnihu@auburn.edu).

    Gerry V. Dozier is with the Computer Science and Software Engineering Department of Auburn University, Auburn, AL 36849; e-mail: doziegv@auburn.edu).

the three forms of GSoHCs have similar performance. ESoHC and EDA-SoHC both have better performance than GSoHC and SoHC in our test suite.

The reminder of this paper is organized as follows. In section II, we present an overview of constraint processing which includes an introduction to the concept of asymmetric constraints and present a formula for predicting where the most difficult randomly generated asymmetric CSPs are located. In section III, we introduce the SoHC concept and explain how GSoHCs, ESoHCs, and EDA-SoHCs operate. In section IV, we present the results of applying SoHC, GSoHC, ESoHC, and EDA-SoHC on 400 randomly generated distributed DisACSPs. In this section, we also compare the three SoHCs on an additional 400 randomly generated distributed DisACSPs. In section V, we provide conclusions and some guidance for future work.

## II. Asymmetric Constraint Satisfaction

A CSP [6],[19],[30],[45]-[48] can be viewed as triple $\langle X, D, C\rangle_{\text {where }} \mathrm{X}$ is set of variables, D is set of domains where each $\mathrm{xie} \mathrm{X}$ takes its value from the corresponding domain die D , and where C is a set of r constraints. Consider a binary constraint network (one where each constraint constrains the value of exactly two variables) ${ }^{1}$ $\langle X, D, C\rangle_{\text {where }} \mathrm{X}=\{\mathrm{E}, \mathrm{F}, \mathrm{G}\}, \mathrm{D}=\{\mathrm{dE}=\{\mathrm{e} 1, \mathrm{e} 2, \mathrm{e} 3\}, \mathrm{dF}=$ $\{\mathrm{f} 1, \mathrm{f} 2, \mathrm{f} 3\}, \mathrm{dG}=\{\mathrm{g} 1, \mathrm{~g} 2, \mathrm{~g} 3\}\}$, and $\mathrm{C}=\{\mathrm{cEF}, \mathrm{cEG}, \mathrm{cFG}\}$. Suppose that the constraints $\mathrm{cEF}, \mathrm{cEG}, \mathrm{cFG}$ are as follows:
$c_{E F}=\{\langle\mathrm{el}, \mathrm{f} 2\rangle,\langle\mathrm{el}, \mathrm{f} 3\rangle,\langle\mathrm{e} 2, \mathrm{f} 2\rangle,\langle\mathrm{e} 3, \mathrm{f} 2\rangle\}$
$c_{E G}=\{\langle\mathrm{e} 2, \mathrm{~g} 3\rangle,\langle\mathrm{e} 3, \mathrm{gl}\rangle\}$
$c_{F G}=\{\langle\mathrm{f} 2, \mathrm{~g} 1\rangle,\langle\mathrm{f} 2, \mathrm{~g} 3\rangle\}$
Constraint networks possess two additional attributes: tightness and density. The tightness of a constraint is the ratio of the number of tuples disallowed by the constraint to the total number of tuples in di x dj. The average constraint tightness of a binary constraint network is the sum of the tightness of each constraint divided by the number of constraints in the network. The density of a constraint network is the ratio of the number of constraints in the network to the total number of constraints possible.

Constraints in a binary constraint network may also be represented as two directional constraints referred to as arcs [46],[48]. For example, the symmetric constraint $C_{E F}$ can be represented as
$c_{E F}=\left\{\begin{array}{l}c_{E F}, c_{E F} \\ c_{E G}=c_{D}\end{array}\right\}$ where
$c_{D}=c_{D}=\{\langle\mathrm{e} 1, \mathrm{f} 2\rangle,\langle\mathrm{e} 1, \mathrm{f} 3\rangle,\langle\mathrm{e} 2, \mathrm{f} 2\rangle,\langle\mathrm{e} 3, \mathrm{f} 2\rangle\}$,
where $c_{E F}$ represents the directional constraint imposed on variable F by variable E , and where $c_{E F}$ represents the directional constraint imposed on variable E by variable F .

[^0]This view of a symmetric binary constraint admits the possibility of an asymmetric binary constraint between variables E and F as one where $c_{E F} \neq c_{E F}$.

## III. SOCIETY OF Hill-ClimBERS

A society of hill-climbers (SoHC) [5],[6],[29]-[32], [34], [49] is a collection of hill-climbers that search in parallel and communicate promising (or futile) directions of search to one another through some type of external collective structure. In the society of hill-climbers that we present in this paper, the external collective structure which records futile directions of search comes in the form of a distributed list of breakout elements, where each breakout element corresponds to a previously discovered nogood ${ }^{2}$ of a local minimum [50]. Before presenting the SoHC, we must first discuss the distributed hill-climber that makes up the algorithm. In this section, we first introduce a modified version of Yokoo's distributed breakout algorithm with broadcasting [34] (mDBA) which is based on Morris' Breakout Algorithm [50]. After introducing mDBA we will describe the framework of a SoHC.

For the mDBA , each agent $a_{i} \in A$ is responsible for the value assignment of exactly one variable. Therefore, agent $a_{i}$ is responsible for variable $s_{i} \in X$, can assign variable $s_{i}$ one value from domain $d_{i} \in D$, and has as constraints $C_{s_{i}, s_{j}}$ where $i \neq j$. The objective of agent $a_{i}$ is to satisfy all of its constraints $C_{s_{i}, s_{j}}$. Each agent also maintains a breakout management mechanism (BMM) [29]-[32] that records and updates the weights of all of the breakout elements corresponding to the nogoods of discovered local minima. This distributed hill-climber seeks to minimize the number of conflicts plus the sum of all of the weights of the violated breakout elements.

## A. The mDBA

The mDBA (shown in Figure 3) used in our SoHCs is very similar to Yokoo's DBA+BC with the major exceptions being that each agent broadcasts to every other agent the number of conflicts that its current value assignment is involved in. This allows the agents to calculate the total number of conflicts (fitness) of the current best distributed candidate solution (dCS) and to know when a solution has been found (when the fitness is equal to zero).

[^1]
[^0]:    ${ }^{1}$ In this paper, we only consider binary constraint networks because any constraint involving more than one variable can be transformed into a set of binary constraints [45]

[^1]:    ${ }^{2}$ A nogood is a tuple that causes a conflict.

## Procedure mDBA(Agent $a_{i}$ )

\{
Step 0: randomly assign $v_{i} \in d_{i}$ to $x_{i}$;
do $\{$
Step 1: broadcast $\left(x_{i}=v_{i}\right)$ to other agents;
Step 2: receive assignments from other agents, agent_view;
Step 3: assign conflicts $c_{i}$ the number conflicts + breakout_elements $\left(x_{i}=v_{i}, x_{i}=j_{i}\right)$ that $\left(x_{i}=v_{i}\right)$ is involved in;
Step 4: randomly search $d_{i}$ for a value $b_{i}$ that minimizes the number of conflicts + breakout_elements $\left(x_{i}=v_{i}, x_{i}=v_{i}\right)$ of $x_{i}$ (ties broken randomly).
Step 5: let $r_{i}$ equal the number of conflicts resolved by $\left(x_{i}=b_{i}\right)$;
Step 6: broadcast conflicts $c_{i}$ and $r_{i}$ to other agents;
Step 7: receive conflicts $c_{i}$ and $r_{i}$ from other agents, let $f=\Sigma$ conflicts $_{i}$;
Step 8: if ( $\max \left(r_{k}\right)==\mathbf{0}$ )
for each conflict, $\left(x_{i}=v_{i}, x_{i}=w_{i}\right)$
update_breakout_elements $\left(\operatorname{BMM} M_{i}\right.$,
$\left.\left(x_{i}=v_{i}, x_{i}=w_{i}\right)\right)$;
Step 9: if $\left(r_{i}=\infty \max \left(r_{k}\right)\right)^{\dagger}$ $v_{i}=b_{i} ;$
\} while $\left(f_{i}>\mathbf{0}\right)$
\}
$\dagger$ Ties are broken with randomly with a synchronized tie-breaker.

Fig.3. mDBA Agent Protocol
Initially, each agent $a_{i}$, randomly generates a value $v_{i} \in d_{i}$ and assigns it to variable $x_{i}$. Next, each agent broadcasts its assignment, $x_{i}=v_{i}$, to its neighbors $a_{i} \in$ Neighbor $_{i}$ where Neighbor ${ }^{3}$ is the set of agents that $a_{i}$ is connected with via some constraint. Each agent then receives the value assignments of every neighbor. This collection of value assignments is known as the agent_view of an agent $a_{i}$ [34]. Given the agent_view, agent $a_{i}$ computes the number of conflicts that the assignment $\left(x_{i}=v_{i}\right)$ is involved in. This value is denoted as conflicts.

Once the number of conflicts, conflicts $_{i}$, has been calculated, each agent $a_{i}$ randomly searches through its domain, $d_{i}$ for a value $b_{i} \in d_{i}$ that resolves the greatest number of conflicts (ties broken randomly). The number of conflicts that an agent can resolve by assigning $x_{i}=b_{i}$ is denoted as $r_{i}$. Once conflicts $_{i}$ and $r_{i}$ have been computed, agent $a_{i}$ broadcasts these values to each of its neighbors.

When an agent receives the conflicts $_{i}$ and $r_{i}$ values from each of its neighbors, it sums up all conflicts, including conflicts, and assigns this sum to $f_{i}$ where $f_{i}$ represents the fitness of the current dCS. If agent $a_{i}$ has the highest $r_{i}$ value of its neighborhood then agent $a_{i}$ sets $v_{i}=b_{i}$, otherwise agent $a_{i}$ leaves $v_{i}$ unchanged. Ties are broken randomly using the

[^0]commonly seeded tie-breaker ${ }^{4}$ that works as follows: if $t(j)>t(j)$ then $a_{i}$ is allowed to change otherwise $a_{j}$ is allowed to change where $\mathrm{t}(\mathrm{k})=(\mathrm{k}+r n d()) \bmod |A|$, and where $r n d()$ is a commonly seeded random number generator used exclusively for breaking ties.

If $r_{i}$ for each agent is equal to zero, i.e. if none of the agents can resolve any of their conflicts, then the current best solution is a local minimum and all agents $a_{i}$ send the nogoods that violate their constraints to their $B M M_{i}$. An agent's BMM will create a breakout element for all nogoods that are sent to it. If a nogood has been encountered before in a previous local minimum, then the weight of its corresponding breakout element is incremented by one. All weights of newly created breakout elements are assigned an initial value of one. Therefore, the task for mDBA is to reduce the total number of conflicts plus the sum of all breakout elements violated.

After the agents have decided who will be allowed to change their value and invoked their BMMs (if necessary), the agents check their $f_{i}$ value. If $f_{i}>0$ the agents begin a new cycle by broadcasting their value assignments to each other. If $f_{i}=0$ the algorithm terminates with a distributed solution.

## B. The Genetic and Evolutionary Protocols

The SoHCs reported in this paper are based on the mDBA. Each SoHC runs $s$ mDBA hill-climbers in parallel, where $s$ is the society size. Each of the $s$ hill-climbers communicates with each other indirectly throught a distributed BMM [6].

A GSoHC [31], [33] is a SoHC that applies a genetic operator [1], [5], [7]-[11], [33], [51]-[54] on each cycle. The genetic operator could be any kind of crossover, such as single-point, two-point, multi-point and uniform crossover.

## 1) Distributed Restricted Uniform Crossover

The operator of the GSoHC that Dozier employed in [31] is a distributed restricted uniform crossover. We denote a GSoHC that uses this kind of crossover as $\mathrm{GSoHC}_{\mathrm{xx}}$. On each cycle, $\mathrm{GSoHC}_{\mathrm{xx}}$ applies a distributed restricted uniform crossover operator, as follows. Each distributed candidate solution with an above average number of conflicts, $\mathrm{dCS}_{i}$, is replaced with an offspring that is a recombination of the best individual, $\mathrm{dCS}_{\text {best }}$, and $\mathrm{dCS}_{i}$. An agent $a_{i}$ will assign $v_{i j}$ the value from $v_{i j}$, with probability $(1-\mu) / 2$ and will leave $v_{i j}$ unchanged with probability $(1-\mu) / 2$, with $\mu$ being a mutation probability. With probability $\mu$ agent $a_{i}$ will randomly assign $v_{i j}$ a value from $\mathrm{d}_{i}$, the domain of values for variable $x_{i}$.

[^1]
[^0]:    ${ }^{3}$ In this paper, Neighbor $_{i}=A-[a)_{i}$. This effectively implies that there are effective constraints among all agents.

[^1]:    ${ }^{4}$ In case of a tie between two agents $a_{i}$ and $a_{i}$, Yokoo's DBA+BC will allow the agent with the lower agent address number is allowed to change its current value assignment. We refer to this as the deterministic tiebreaker (DTB) method

## 2) Distributed Restricted Two-Point Crossover and Distributed Restricted Modified Two-Point Crossover

Similarly, when a distributed restricted two-point crossover [33] is applied on each cycle, each $\mathrm{dCS}_{i}$ that has an above average number of conflicts is also replaced with an offspring. To create the offspring, the first part is the same as single point crossover. With probability $\mu$, the offspring will randomly select a value from the domain of the values. Then, with probability $1-\mu$, two cut points are randomly chosen with duplicates from 1 to $\mathrm{N}-1$, where N is the number of agents of an individual, and the cut points are sorted. The $\mathrm{dCS}_{i}$ and $\mathrm{dCS}_{\text {best }}$ are cut into parts at these two points. With probability $(1-\mu) / 2$, agents with addresses less than or equal to the first cut point or greater than the second one will take the values of $\mathrm{dCS}_{\text {best }}$, others will keep their values. With probability of the other $(1-\mu) / 2$, agents with addresses greater than the first cut point and less than or equal to the second one will take the values of $\mathrm{dCS}_{\text {best }}$, while others will remain unchanged. We call this kind of recombination a distributed restricted two-point crossover and refer it as $\mathrm{GSoHC}_{\text {tpx }}[33]$.

In order to improve the performance of two-point crossover, we increase the probability for taking genes from the $\mathrm{dCS}_{\text {best }}$. The difference between the GSoHC using the improved two-point crossover with $\mathrm{GSoHC}_{\mathrm{tpx}}$ is as follows. With probability $1-\mu$, agents with addresses less than or equal to the first cut point or greater than the second cut point will take the values of $\mathrm{dCS}_{\text {best }}$, others will keep their values. This way approximately $67 \%$ of an offspring's genes will come from $\mathrm{dCS}_{\text {best }}$. The distributed restricted version of two-point crossover takes approximately $50 \%$ of the genes from $\mathrm{dCS}_{\text {best }}$. We denote the GSoHC that uses this modifed two-point crossover $\mathrm{GSoHC}_{\text {mtpx }}$.

## 3) Evolutionary SoHC

The Evolutionary SoHC [32] is similar to GSoHC mentioned earlier except it relies on mutation exclusively. We denote this as ESoHC. On each cycle, the distributed restricted mutation operator is applied as follows. Each distributed candidate solution that has an above average number of conflicts, $\mathrm{dCS}_{i}$, is replaced with an offspring that is a mutated version of the best individual, $\mathrm{dCS}_{\text {best }}$, as follows. With probability $\mu$, agent $a_{i}$ will randomly assign $v_{i j}$ a value from $\mathrm{d}_{\mathrm{i}}$ and with probability $1-\mu$ agent $a_{\mathrm{i}}$ will set $v_{i j}$ $=v_{\mathrm{iq}}$.

## 4) Estimation of Distribution Algorithm SoHC

The EDA-SoHC uses a distributed restricted estimation of distribution operator (dREDO) which is commonly used in Estimation of Distribution Algorithms (EDA)[55]. In order to create a gene $\mathrm{dCS}_{i}$, the dREDO first applies a distributed uniform mutation operator with probability $\mu$ to a random parent. Alternatively, with probability $(1-\mu) \varepsilon$ (where a higher $\varepsilon$ variation operator value produces a higher variation rate) an agent will select a value for $\mathrm{dCS}_{i}$ from a probability distribution function based on the above average individuals $\left(\mathrm{dCS}_{i}\right)$. The generated offspring, $\mathrm{dCS}_{i}$, will possess attributes that most often appear in above-average
individuals. With probability $(1-\mu)(1-\varepsilon)$ the agent leaves the associated value of $\mathrm{dCS}_{i}$ unchanged. In this manner, all of the below-average individuals in the population are replaced with offspring.

## IV. RESULTS AND DISCUSSION

## A. Experiment Settings

In this experiment, we compared five forms of SoHCs (SoHC, $\mathrm{GSoHC}_{\text {tpx }}, \mathrm{GSoHC}_{\text {mtpx }}$, ESoHC, EDA-SoHC). For the SoHC (running the Society of Hill-Climbers described in Section III without any genetic protocols), experimentation showed that the population size 32 yielded the best results (with respect to success rate and communication cycles) out of $\{1,2,4,8,16,32\}$. We chose our mutation rate $\mu$ to be 0.06 , as it proved to be the best performer from $\{0.03,0.06$, $0.12,0.25\}$. The above best values were obtained from the experiments described in [6]. For our experiments, we tested the algorithms once each on a test suite of 400 instances of randomly generated DisACSPs of the form $n=30$ variables, number of domain values $m=6$, arc density $p 1_{\mathrm{st}}=1.0$, and varying tightness p 2 from $\{0.03,0.04,0.05,0.06\}$. For the EDA-SoHC, we explored values of $\varepsilon$ between 0 and .936. For the purposes of comparison, a value of $\varepsilon=0.125$ was utilized; this value proved to have the best performance at the phase transition ( $\mathrm{p} 2=0.06$ ), which is the most difficult class of problems [30]. For problems beyond the phase transition (more tightly constrainted), various techniques such as arc revision and arc consistency can be used to demonstrate the lack of a solution [23].

## B. Results

In each of the tables 1-4, the first column represents the algorithms (Alg.); the second is Success Rate for the algorithm when given a maximum of 2000 cycles to solve each problem in the class (SR); the third is Average Cycles needed to discover a solution, and the last column shows the results of a single point ANOVA test between the cycles of the algorithm and the cycles of the EDA-SoHC (where a p value less than or equal to 0.05 will be considered statistically significant difference).

As shown in Table I with $\mathrm{p} 2=0.03$, all of the algorithms had a $100 \%$ success rate and the EDA-SoHC slightly outperforms all of the algorithms with respect to average

Table I
Comparison of SoHC, GSoHC, ESoHC, and EDA-SoHC for $\mu=.06,<.30,6,1.0,0.03>$
number of cycles. There is statistically significant distinction between the cycles of the EDA-SoHC and the other

algorithms. The average number of cycles per run of all the algorithms is 14.104 , an indication of the relative ease of these particular problems.

In Table II with $\mathrm{p} 2=0.04$, all of the algorithms had a $100 \%$ success rate and EDA-SoHC performs slightly worse than ESoHC, but better than SoHC and the GSoHCs. Only the comparisons with SoHC and $\mathrm{GSoHC}_{\text {aps }}$ show statistically significant differences. The average number of cycles per run of all the algorithms is 33.406 , which is still fairly low. Of particular interest is the disparity between the SoHC and the ESoHC and EDA-SoHC. The number of cycles required to reach the same success rate is nearly halved in the later two.

TABLE II
COMPARISON OF SoHC, GSoHC, ESoHC, AND EDA-SoHC FOR $\mu=0.06,<30,6,1.0,0.04>$

In Table III with $\mathrm{p} 2=0.05$, the SoHC discovered a relatively low SR of $60 \%$, the GSoHCs and ESoCH had a $98 \%$ success rate, but EDA-SoHC falls to a $97 \%$ SR. Requiring 377.48 cycles, EDA-SoHC performs noticeably worse than all algorithms, excepting the SoHC which takes 1180.34. Based on the results of the ANOVA test, only the comparison with SoHC shows statistical distinction.

Table III
Comparison of SoHC, GSoHC, ESoHC, and EDA-SoHC for $\mu=0.06,<30,6,1.0,0.05>$
Table IV shows the performance at the phase transition ( $\mathrm{p} 2=0.06$ ). The SoHC manages only a $1 \%$ success rate, the $\mathrm{GSoHC}_{\text {aps }}$ discovers a SR of $8 \%$, while all the other algorithms achieve an $11 \%$ SR. With respect to cycles, EDA-SoHC outperforms the other three algorithms (although only slightly). It is worth noting that since many of the problems could not be solved, the average cycle values tend towards 2000 (the number averaged in if no solution is found by that point). Only the SoHC shows statistical distinction, but ESoHC and EDA-SoHC show extremely high statistical correlation.

TABLE IV
COMPARISON OF SoHC, GSoHC, ESoHC, AND EDA-SoHC FOR
$\mu=.06,<30,6,1.0,0.06>$

## V. CONCLUSIONS AND FUTURE WORK

The applied evolutionary operators, known as crossover and mutation, on randomly generated distributed asymmetric CSPs are studied in the work presented in this paper. The SoHCs, GSoHCs, EDA-SoHC and ESoHC are described and a series of experimental results and comparisons are presented. In particular, GSoHCs using distributed restricted forms uniform crossover, and modified two-point crossover, are studied with respect to SR, Cycles and their statistical correlation to the EDA-SoHC $(\varepsilon=0.125)$.

From experimental results and a series of comparisons, we can draw the following conclusions:
In general, we note that SoHC performs noticeably worse than all the other algorithms, save for the easiest instances when $\mathrm{p} 2=0.03$.
Generally speaking, GSoHCmtpx has better performance than GSoHCupx due to the fact that it takes more genes from the best dCS.

The GSoHCs and ESoHC have better performance than the simple SoHC. The EDA-SoHC protocol performs roughly on par with ESoHC under most conditions. Further, the differences between the number of cycles for EDA-SoHC and for the other algorithms are generally not statistically significant, except for the easier instances ( $\mathrm{p} 2=0.03$ and 0.04 ). In general, we attribute the success of the EDA-SoHC to its application of selection pressure through taking genetic material from the above average members of the population. At the same time, the algorithm preserves a level of population diversity by granting the opportunity for a child to obtain attributes from any of the above-average individuals (not merely the best).

Comparing the results between GSoHC, ESoHC, and EDA-SoHC suggests that the variation of the above-average dCS's plays the most important role in the genetic and evolutionary SoHC search. The specific type of operator creating this variation is only of secondary importance [32]. Our future work will be devoted to discovering a form of recombination that is has a performance equal to or better than the distributed restricted uniform mutation operator and the EDA-SoHC.
