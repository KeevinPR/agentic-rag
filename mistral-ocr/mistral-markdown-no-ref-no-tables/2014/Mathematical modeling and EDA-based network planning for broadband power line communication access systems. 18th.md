# Mathematical Modeling and EDA-based Network Planning for Broadband Power Line Communication Access Systems 

J. S. Oberoi, D. C. Lee, Senior Member, IEEE<br>School of Engineering Science<br>Simon Fraser University<br>Burnaby, Canada<br>(joberoi, dchlee)@sfu.ca


#### Abstract

In this paper, we present a mathematical model of power line communication access systems and a technique for an efficient network deployment. We focus on the problem of designing an infrastructure network model which fits the power line communication needs and installing an apt number of base stations and repeaters at adequate locations suited to serve all the subscribers to the required level at a low cost to the utility company. The computational complexity of determining an optimal deployment by using exhaustive search grows exponentially with the number of base stations, repeaters and the users. We propose a heuristic method combined with an Estimation-of-Distribution Algorithm (EDA) for this assignment problem. EDA is a probabilistic evolutionary algorithm which updates its population at each iteration on the basis of the probability densities obtained from the population of superior candidates evaluated and chosen at the previous iteration.


Keywords- Base station placement, Repeater deployment, Power line communication, Network planning.

## I. INTRODUCTION

The power line communication (PLC) paradigm can utilize the low-voltage electrical supply cable network for consumer communication purposes. With this technology, the electrical lines already installed for supplying electric power to the consumers act as a physical medium for carrying communication signals too. Thus the usage of this access solution results in significant savings in the installation investment costs of communication network infrastructure like optical cables. PLC can be used for various services like internet, telephony, smart metering etc. With the development of the PLC system hardware and technology in recent times, bit rates of up to 500 Mbps have been achieved [1][4] and the standardization process has undergone through different stages under the Open PLC European Research Alliance (OPERA) Project [2], HOMEPLUG Power line Alliance [3] and IEEE [4]. Much work has been invested in the development of PLC systems and understanding the power line communication channel, but relatively little has been discussed concerning the planning of these networks. Installation of some special equipment in the low voltage grid is necessary in order to
connect the users to the service providers over the wide area network (WAN) and to make the communication over this infrastructure possible as illustrated in Fig.1. A part of this equipment is the base station (BS), which connects the PLC access network to commercially available communication networks such as the internet or PSTN called the backhaul networks (BN). A base station (BS) extracts/injects the information signal from/into the low-voltage cable. In some cases, a BS needs one or more repeaters to reach the user(s) if the distance between a BS and the destination (user) is longer than the BS line coverage [5].

The network planning for PLC thus consists of placing an adequate number of BSs and repeaters at apt locations in the low-voltage network (LVN). It is desired that the number and geographical placement of BSs and repeaters be optimal in the sense that they serve all the subscribers to the required quality of service at the minimum cost to the service provider. The cost of the BS installation is higher than a repeater installation due to a higher equipment cost and also the needed back haul network connection. This BS and repeater planning problem is similar to one for wireless communication and is categorized as an NP-hard problem [7][8]. We present a heuristic algorithm to solve this problem for our proposed model.
![img-0.jpeg](img-0.jpeg)

For PLC planning, we have to first understand the infrastructure of low voltage networks (LVNs), for example, their structure, their dimension and the user distribution. An extensive investigation of the LVN structures and characteristics has been presented in [6]. BS planning for PLC has been presented in [7] but the planning is limited to LVNs with a tree physical topology. The present paper addresses

data network planning in LVNs with a general topology, including non-tree topology. Our model is also designed to incorporate branching and interconnectivity, which is highly prevalent in practical electrical supply infrastructure networks. Exhaustive search algorithm can be used for this BS and repeater deployment, but its computational complexity and time-cost increases with the number of BSs, repeaters and the subscribers. We have developed a heuristic algorithm and then combined it with an Estimation-of-Distribution Algorithm (EDA) [9]. The rest of the paper is organized as the following. Section 2 presents our system model and problem formulation. Section 3 presents our algorithms, and simulation results are presented in section 4.

## II. SYSTEM MODEL AND PROBLEM FORMULATION

Fig. 2 illustrates a part of an LVN. The part of the network shown has a transformer and electric poles connected with the electric wires delivering power in low voltage network beyond the transformer.
![img-2.jpeg](img-2.jpeg)

Fig. 2
Note that the PLC coverage range, which is the distance limit above which reliable information transfer cannot take place, is 800 meters to 1 km [5]. In a usual LVN the distance between two consecutive electric poles is 100 meters (urban) to 400 meters (rural). Unlike wireless communication we cannot go with a very high capacity BS and serve all the users through it alone as the PLC coverage range becomes an issue with such a setup. Even if we want to install just one BS, we would need repeaters to help it serve all the subscribers. Thus we need installation sites at appropriate distance apart that can keep the communication link intact and also keep every subscriber within the PLC coverage area. Electric poles in the LVN are considered as the potential sites for a BS/repeater installation [5].

The physical topology of an LVN is represented by two parameters $D_{i, j}$ and $N_{i, j}$ for $i, j=1,2,3 \ldots n, i \neq j$, where $n$ denotes the total number of electric poles. The parameter $N_{i, j}$ indicates whether two poles are neighbors or not and is defined as:
$N_{i, j}=\left\{\begin{array}{cl}1, \text { if pole } i \text { is directly connected to pole } j, & \text { having no pole } \\ & \text { in between ; } \\ & 0, \text { otherwise. }\end{array}\right.$
$D_{i, j}$ is the distance (eg. in meters) between two electric poles numbered $i$ and $j$. The distance is measured along the physical communication medium, which is the electrical power line connecting two electric poles. We now define other input parameters for problem formulation of the PLC network planning. We denote by $R$ the PLC coverage range; that is the maximum distance the communication signal can travel through a power line in LVN reliably.
$U L_{i, j}=U L_{j, i}=$ number of users connected to the electric line between the poles $i$ and $j$.
$W_{i}=$ cost of connecting the BN to the BS installed at pole $i$.
Note that every installed BS has to be connected to BN.
$C_{B i}=$ equipment cost of installing a BS at pole $i$.
$C_{B i}=$ equipment cost of installing a repeater at pole $i$.
$C P_{i}=$ capacity of the BS installed at pole $i$, where we define the capacity as the maximum number of users that can subscribe to a BS for data service with a fixed maximum bandwidth allowed to each user.

In this paper, we assume that the system establishes only one route between a user and the BN. In our network planning method, we establish one or more PLC cells, where each PLC cell comprises one BS and a set of repeaters and has a logical tree topology with the BS as the root as illustrated in Fig.3.
![img-2.jpeg](img-2.jpeg)

Solid lines in Fig. 3 represent the power line connections which form the edges of the logical tree topology. In our planning method, the users tapped on these power lines, which are represented by the edges of the tree topology, have their data flow to and from the parent node of the particular edge. Dotted lines in Fig. 3 represent power line connections which are not a part of the logical tree. Each user tapped on these power lines can have its data network connection through either of the two nodes connected by the particular dotted line but not both. Now we define four sets of optimization variables for $i, j=1,2,3 \ldots n$ and $i \neq j$.
$B_{i}=\left\{\begin{array}{c}1, \text { if a BS is installed at pole } i ; \\ 0, \text { otherwise. }\end{array}\right.$
$R_{i}=\left\{\begin{array}{c}1, \text { if a repeater is installed at pole } i ; \\ 0, \text { otherwise. }\end{array}\right.$
$B S_{i, j}=\left\{\begin{array}{c}1, \text { if the repeater at pole } i \in \text { PLC cell of the BS at pole } j ; \\ 0, \text { otherwise. }\end{array}\right.$
$R S_{i, j}=\left\{\begin{array}{c}1, \text { if the repeater at pole } i \text { is a child of the repeater at } \\ \text { pole } j \text { in the logic tree of a PLC cell; } \\ 0, \text { otherwise. }\end{array}\right.$

Determination of these variables determines the logical topology of a PLC cell or PLC cells in the LVN. For our modeling, two poles with a BS or repeater installation are said to be linked, if they are connected by a power line and have no pole with an installed BS/repeater present on the electric line connecting them.
$L_{i, j}=L_{j, i}=\left\{\begin{array}{c}1, \text { if pole } i \text { is connected with pole } j \text { via power line } \\ \text { with no pole with an installation in between; } \\ 0, \text { otherwise. }\end{array}\right.$
Pole $i$ (with a BS or a repeater) is said to have a link with pole $j$ if $L_{i, j}=1$. We define another optimization variable which deals with user allocation to the installed BSs and repeaters.
$U_{i}^{j}=\left\{\begin{array}{c}\left(\text { if } B_{i}=1\right) \text { number of users directly subscribed to the BS at } \\ \text { pole } i \text { out of the total users present on its link with pole } j ; \\ \text { (if } R_{i}=1 \text { ) number of users subscribed to the BS through } \\ \text { the repeater node } i \text { out of the total users present on its } \\ \text { link with pole } j ; \\ 0, \text { otherwise. }\end{array}\right.$
Using these variables and parameters we present our optimization problem with the constraints below defining our mathematical model.
Objective - Minimize the cost, where the cost is defined as:

$$
\sum_{i=1}^{n} B_{i}\left(C_{B i}+W_{i}\right)+R_{i} \cdot C_{B i}
$$

The constraints that need to be fulfilled while minimizing this cost are:

$$
\begin{array}{lll}
B_{i} \in\{0,1\} & \forall i=1 \text { to } n & -(1) \\
R_{i} \in\{0,1\} & \forall i=1 \text { to } n & -(2) \\
B S_{i, j} \in\{0,1\} & \forall i, j=1 \text { to } n, i \neq j & -(3) \\
R S_{i, j} \in\{0,1\} & \forall i, j=1 \text { to } n, i \neq j & -(4) \\
B_{i}+R_{i} \leq 1 & \forall i=1 \text { to } n & -(5) \\
\hline \sum_{i=1}^{n} B_{i} \geq 1 & & -(6) \\
B S_{i, j}=0 \text { if } R_{i}=0 \text { or } B_{i}=0 & \forall i, j=1 \text { to } n, i \neq j & -(7) \\
R S_{i, j}=0 \text { if } R_{i}=0 \text { or } R_{j}=0 \text { or } L_{i, j}=0 & \forall i, j=1 \text { to } n, i \neq j & -(8) \\
{\left[\left(\sum_{j=1}^{n} B S_{i, j}, L_{i, j}=1\right) \oplus\left(\sum_{j=1}^{n} R S_{i, j}, L_{i, j}=1\right)\right]=1} & \text { if } R_{i}=1 \\
\forall i=1 \text { to } n & & -(9) \\
U_{i}^{j}+U_{j}^{j}=U L_{i, j} & \forall i, j=1 \text { to } n, i \neq j & -(10) \\
U_{j}^{j}=U L_{i, j} \text { if }\left(B S_{i, j}=1 \text { or } R S_{i, j}=1\right) \text { and } L_{i, j}=1 & \\
\forall i, j=1 \text { to } n, i \neq j & & -(11) \\
C P_{i} \geq \sum_{j=1}^{n}\left\{L_{i, j}, U_{i}^{j}+B S_{j, i}, \sum_{k=1}^{n}\left(L_{j, k}, U_{j}^{k}\right)\right\} & & \\
\forall i \text { such that } B_{i}=1, i \neq j, j \neq k, k \neq i & & -(12) \\
L_{i, j} D_{i, j}, B S_{i, j} \leq R & \forall i, j=1 \text { to } n, i \neq j & -(13) \\
D_{i, j}, R S_{i, j} \leq R & \forall i, j=1 \text { to } n, i \neq j & -(14) \\
B_{i}+R_{i}=1 \text { if } \sum_{j=1}^{n} N_{i, j} \geq 3 & \forall i=1 \text { to } n, i \neq j & -(15)
\end{array}
$$

Constraints (1) to (4) restrict $B_{i}, R_{i}, B S_{i, j}$ and $R S_{i, j}$ to be binary variables. Constraint (5) states that a pole can have either a BS installed or a repeater or none. Constraint (6) makes sure that at-least one BS is installed which with a connection to BN serves data to the whole LVN. For $B S_{i, j}$ to take value 1 it is necessary but not sufficient that a repeater is installed at $i$ and a BS at $j$. Likewise for variable $R S_{i, j}$, the necessary condition is that repeaters are installed at both $i$ and
$j$ and the two poles are linked. This is stated in constraints (7) and (8). Constraint (9) guarantees that a repeater either has a link with the BS of its PLC cell or is a child of another repeater of a PLC cell. The XOR operator maintains the exclusivity of the above two choices between a BS and a parent repeater thus ensuring and also restricting every repeater to be a part of exactly one PLC cell. It also ensures that data flow within a PLC cell has a single allowed path. Constraint (10) says that a user present on a link between two poles with installations is either connected to the network through pole $i$ or pole $j$, thus, all the users are guaranteed network service. Constraint (11) states that the users present on the link between a parent and a child are always connected to the BN through the parent node. Constraint (12) is the BS capacity constraint. It states that the total number of users in the PLC cell of a BS located in site (pole) $i$ should not exceed the maximum serving capacity, $C P_{i}$, of the BS at location $i$. The PLC coverage range has to be respected while placing the BSs and repeaters and this is taken care of by constraints (13) and (14). Every pole with 3 or more neighbors must be selected as a site for installation because an intelligent device (BS or repeater) is needed to route signals at such a junction, and constraint (15) guarantees that.

A large number of decision variables and constraints, along with a large domain of electric poles being the potential candidate sites for installation, pose a computational challenge. We propose an efficient preliminary heuristic algorithm that converts our problem (A) to a simpler problem and we solve the resultant simpler problem by using an EDA.

## III. ALGORITHMS: CSSA AND EDA

The aim of our Candidate Site Selection Algorithm (CSSA) is to simplify the problem by restricting it to be a problem of selecting whether to install a BS or a repeater at a given site rather than choosing between installing a BS, a repeater or none on a pole. Not all electric poles need to accommodate a BS or a repeater, so rather than formulating a problem of deciding whether each electric pole will host a BS or a repeater or none, we suggest a preliminary algorithm that selects sites amongst all the electric poles for the BS/repeater installation. We call these selected poles as installation sites. We aim for all installation sites to be exactly distance $R$ apart for making the setup most efficient, leaving all the poles in between unselected.

CSSA (given in Table.1) chooses and declares a selective number of poles as the installation sites amongst all the available electric poles while maintaining the feasibility of power line communication. Variable $S_{i}$ in CSSA states whether the pole has been selected as an installation site or not.

$$
S_{i}=\left\{\begin{array}{r}
1, \text { if pole } i \text { is selected as an installation site; } \\
0, \text { otherwise. }
\end{array}\right.
$$

Parameter $T_{i}$ in $C S S A$ is used to determine a terminal point present in the network. These are the electric poles which have just one neighbor. Such terminal point electric poles are not considered for BS/repeater installation.

$$
T_{i}=\left\{\begin{array}{r}
1, \text { if pole } i \text { is stated as a terminal point; } \\
0, \text { otherwise. }
\end{array}\right.
$$

This algorithm makes sure that no two candidate sites are more than $R$ distance apart while also trying to keep the distance as close to R as possible. This algorithm selects every pole with three or more neighbors as an installation site. Variable $S_{i}$ carries the installation site selection information from CSSA to next stage. We show how our sample network shown before in Fig. 2 looks like after passing through CSSA with $R=900$ meters below in Fig.4.
![img-3.jpeg](img-3.jpeg)

Fig. 4
This is one of the possible results because of the random selection in step 4 of CSSA but still the total number of installation sites selected remains the same for a particular input network. The selected poles, called sites here after, are represented by the same symbol and the non-selected ones are replaced by dots in Fig.4.

Table. 1 - Candidate Site Selection Algorithm (CSSA)

Step 1: Set $S_{i}, T_{i}=0 \forall i=1$ to $n$
: Set $S C=\}$ (empty set)
Step 2: Set $S_{i}=1 \forall$ poles with 3 or more neighbors
: Set $T_{i}=1 \forall$ poles with 1 neighbor $\forall i=1$ to $n$
Step 3: Add poles with $S_{i}=1$ and $T_{i}=1$ in $S C \forall i=1$ to $n$
Step 4: Randomly choose a pole $j \in S C$.
Step 5: $S C=S C-\{j\}$
Step 6: Set $K=\}$ (empty set)
Step 7: for $k=1$ to $n, k \neq j$
: if $N_{j, k}=1$
:Add $k$ to set $K$
Step 8: Randomly choose a pole $k \in K$
Step 9: $K=K-\{k\}$
Step 10: scan the electric line from j , pole by pole in the direction of $k$ till distance $R$
: if no pole with $S_{i}=1$ or $T_{i}=1$ is encountered : mark the last scanned pole $m$ as $S_{m}=1$ : $S C=S C+\{m\}$
: if a pole with $S_{i}=1$ or $T_{i}=1$ is encountered : continue
Step 11: if $K \neq\{ \}$, go to step 8
: if $K=\}$, continue
Step 12: if $S C \neq\{ \}$, go to step 4 ;
: if $S C=\}$, exit.

After a pole has been selected as an installation site, a BS or a repeater has to be installed on that site; otherwise the communication link would break due to out of coverage reasons. Thus, the sum of the number of BSs and repeaters to be installed is determined by CSSA. This sum is denoted by $z$. After CSSA execution, we are left with the task of placing optimal number of BSs and repeaters on these selected sites ensuring service for every subscriber at the minimum cost to the service provider. The more BSs installed, the less repeaters installed. Different combinations of BSs and repeaters result in different costs of setting up the communication network. CSSA reduces our original problem into a less complex problem as shown below. We use the CSSA output, $S_{i}, i=1,2, \ldots, \mathrm{n}$, to derive the input parameters of our reduced problem. The selected $z$ installation sites from the available $n$ electric poles are renumbered from 1 to $z$. The input parameters for $i, j=1$, $2,3 \ldots z$ and $i \neq j$ are given below.

$$
L S_{i, j}=L S_{j, i}=\left\{\begin{aligned}
1, \text { if site } \mathrm{i} \text { is connected with } \mathrm{j} \text { via power line } \\
\text { with no site in between; } \\
0, \text { otherwise. }
\end{aligned}\right.
$$

Sites are said to be linked if $L S_{i, j}=L S_{j, i}=1$.
$U L_{i, j}=U L_{j, i}=$ number of users connected to the link between the sites $i$ and $j$.
$W_{i}=$ cost of connecting BN to the BS installed at site $i$.
$C_{B i}=$ equipment cost of installing BS at site $i$.
$C_{B i}=$ equipment cost of installing repeater at site $i$.
$C P_{i}=$ capacity of the BS installed at site $i$.
Our optimization variables for $i, j=1,2,3 \ldots z$ and $i \neq j$ are:

$$
\begin{aligned}
& B R_{i}=\left\{\begin{array}{l}
1, \text { if a BS is installed at site } i ; \\
0, \text { if a repeater is installed at site } i .
\end{array}\right. \\
& B S_{i, j}=\left\{\begin{array}{l}
1, \text { if the repeater at site } i \in \text { PLC cell of the BS at site } j ; \\
0, \text { otherwise. }
\end{array}\right. \\
& R S_{i, j}=\left\{\begin{array}{l}
1, \text { if the repeater at site } \mathrm{i} \text { is a child of the repeater at } \\
\text { site } \mathrm{j} \text { in the logic tree of a PLC cell; } \\
0, \text { otherwise. }
\end{array}\right.
\end{aligned}
$$

We also define optimization variables $U_{i}^{j}$ where $i$ and $j$ are linked $\left(L S_{i, j}=1\right)$

The reduced optimization problem with modified constraints is given below.

Objective - Minimize the cost and the cost is given by:

$$
\sum_{i=1}^{Z} B R_{i}\left(C_{B i}+W_{i}\right)+\left(1-B R_{i}\right) C_{B i}
$$

The constraints to be followed while minimizing the cost are:

$$
\begin{array}{ll}
B R_{i} \in\{0,1\} & \forall i=1 \text { to } z-(16) \\
B S_{i, j} \in\{0,1\} & \forall i, j=1 \text { to } z, i \neq j-(17) \\
R S_{i, j} \in\{0,1\} & \forall i, j=1 \text { to } z, i \neq j-(18)
\end{array}
$$

$\sum_{i=1}^{e} B R_{i} \geq 1$
$B S_{i, j}=0$ if $B R_{i}=1$ or $B R_{j}=0 \quad \forall i, j=1$ to $z, i \neq j-(20)$
$R S_{i, j}=0$ if $B R_{i}=1$ or $B R_{j}=1$ or $L S_{i, j}=0 \forall i, j=1$ to $z, i \neq j-(21)$
$\left[\left(\sum_{j=1}^{e} B S_{i, j}, L S_{i, j}=1\right) \oplus\left(\sum_{j=1}^{e} R S_{i, j}, L S_{i, j}=1\right)\right]=1$ if $B R_{i}=0$
$\forall i=1$ to $z$
$U_{i}^{l}+U_{j}^{l}=U L_{i, j} \quad \forall i, j=1$ to $z, i \neq j-(23)$
$U_{j}^{l}=U L_{i, j}$ if $\left(B S_{i, j}=1\right.$ or $\left.R S_{i, j}=1\right)$ and $L S_{i, j}=1$
$\forall i, j=1$ to $z, i \neq j$
$C P_{i} \geq \sum_{j=1}^{e}\left\{L_{i, j}, U_{j}^{l}+B S_{j, i}, \sum_{k=1}^{e}\left(L_{j, k}, U_{j}^{k}\right)\right\}$
$\forall i$ such that $B R_{i}=1, i \neq j, j \neq k, k \neq i$
Now we present our use of the Estimation-ofDistribution Algorithm (EDA), which belongs to the class of the Evolutionary Algorithms (EAs), for solving optimization problem (B). In EA, the candidate solutions of an optimization problem are represented as individuals of the population. The fitness of each individual (a particular candidate solution) in the population is evaluated in the first phase of each iteration. In the selection phase, the individuals with higher fitness values are chosen as the parents of the individuals for the next population. Then, a new population of individuals is randomly generated from the probability distribution estimated from the previous iteration. In EDA the probability distribution is estimated from the selected individuals of the previous population rather than mutation or cross over, as done in other evolutionary algorithms [9]. In general, EDA is characterized and described by the parameters $\left(I_{s}, F, \Delta_{l}, \eta_{l}, \beta_{l}, p_{s}, \Gamma, I_{T e r}\right)[9]$, where-

1. $I_{s}$ is the space of all potential solutions (entire search space of individuals).
2. $F$ denotes the fitness function.
3. $\Delta_{l}$ is the population (the set of individuals) at the $l_{\text {th }}$ iteration and $\left|\Delta_{l}\right|$ denotes its cardinality.
4. $\eta_{l}$ is the set of best candidate solutions selected from the set $\Delta_{l}$ at the $l_{\text {th }}$ iteration.
5. We denote $\beta_{l} \equiv \Delta_{l}-\eta_{l} \equiv \Delta_{l} \cap{ }^{c} \eta_{l}$ where ${ }^{c} \eta_{l}$ denotes the complement of $\eta_{l}$.
6. $p_{s}$ is the selection probability. The EDA algorithm selects $p_{s}\left|\Delta_{l}\right|$ individuals from the set $\Delta_{l}$ to make up the set $\eta_{l}$.
7. We denote by $\Gamma$ the distribution estimated from $\eta_{l}$ (the set of selected candidate solutions) at each iteration.
8. $I_{T e r}$ is the maximum number of iterations.

For EDA each individual can be represented by a binary string of a fixed length. Let us denote by $n$ the length of the binary string. The binary string can be also viewed as an $n$ dimensional binary vector. For example, an individual can be denoted by a binary row vector $\mathbf{X}=\left(x_{1}, x_{2}, \cdots, x_{r}\right), x_{i} \in\{0,1\}$. For each iteration $l$, the EDA maintains a population of individuals, and we denote by $\Delta_{l}$ the population at iteration (generation) $l$. Population, $\Delta_{l}$ can be specified by the following matrix (26). Here the superscript indexes an individual and the subscript indexes the component of the binary vector representing an individual.

$$
A=\left(\begin{array}{c}
X^{1} \\
X^{2} \\
\vdots \\
X^{\left.\right|_{\mathrm{s}, \mathrm{l}}^{1}}
\end{array}\right)=\left(\begin{array}{cccccc}
x_{1}^{1} & x_{2}^{1} & \vdots & x_{r}^{1} \\
x_{r}^{2} & x_{2}^{2} & \vdots & x_{s}^{2} \\
\ldots & \ldots & \ldots & \ldots \\
x_{i}^{\left.\right|_{\mathrm{s}, \mathrm{l}}} & x_{i}^{\left.\right|_{\mathrm{s}, \mathrm{l}}} & \vdots & x_{s}^{\left.\right|_{\mathrm{s}, \mathrm{l}}}
\end{array}\right)
$$

The EDA scheme can be described as the following:
Step 1: Generate initial population $\Delta_{0}$. This is done by random sampling according to the uniform distribution, i.e. probability of setting 1 and 0 on any bit position in an individual being equal to 0.5 which means:

$$
p_{i}\left(x_{i}=1\right)=p_{i}\left(x_{i}=0\right)=0.5, i=1,2, \ldots, n
$$

The resultant generated population is passed through various defined constraints from (16) to (25); if they are not satisfied the population is modified to do so. For iterations $1=1,2, \ldots$, $I_{T e r}$ steps 2-7 are followed:

Step 2: Rate the individuals of the current population $\Delta_{l-1}$ by evaluating the fitness function at each particular individual.

Step 3: If $I_{T e r}$ number of iterations have been processed then terminate, else proceed.

Step 4: Select the best $p_{s} \Delta_{l-1}$ individuals.
Step 5: Estimate the probability density distribution on the basis of $\eta_{l-1}$ best individuals which is (28),

$$
\Gamma_{l}=P\left(x_{1}, x_{2}, \cdots, x_{n} \mid \eta_{l-1}\right)
$$

Step 6: Generate new $\left|\Delta_{l}\right|$ individuals on the basis of the new probability distribution (28) and again pass it through all the mentioned constraints to get modified individuals which satisfy all constraints.

Step 7: Go to step 2 and repeat.
The easiest way to calculate an estimate of the required probability distribution is to treat all the variables of the binary vector as if they were statistically independent from each other. Then, the joint probability distribution becomes the product of the marginal distributions. This particular method in EDA is called UMDA (univariate marginal distribution algorithm) [9]. After selection, the probability vector is updated and it stores the proportion of 1 's in each position of the selected population. Then, each bit of a new candidate solution is set to 1 with the probability equal to the proportion of 1 's in that particular position. Thus $\Gamma_{l}$ is estimated by taking the product of individually estimated univariate marginal distributions (UMDA) which is mathematically expressed as,

$$
\Gamma_{l-1}=p\left(x_{1}, x_{2}, \cdots, x_{n} \mid \eta_{l-1}\right)=\prod_{i=1}^{n}\left(\frac{\sum_{j=1}^{\left|n_{i}\right|} \delta\left(X_{i}^{j}=x_{i} \mid \eta_{l-1}\right)}{\left|\eta_{l-1}\right|}\right)
$$

Where, $\delta$ is an indicator function for the individual indexed by $j$ in the set $\eta_{l-1}$

$$
\delta\left(X_{i}^{j}=x_{i} \mid \eta_{l-1}\right)=\left\{\begin{array}{ll}
1 & \text { if } X_{i}^{j}=x_{i} \\
0 & \text { otherwise }
\end{array}\right.
$$

In applying the EDA for our optimization problem (B), we add another layer of heuristics. Among all optimization variables only $B R_{i}, i=1,2, \ldots, z$ appear in the objective function. In order to speed up computation, we only use the z -

dimensional $B R$ vector, with elements indexed as $B R_{i}$ is represented as an individual of the population. Thus installation of BSs and repeaters is governed by the indices of the individual taking value 0 or 1 . We pass this vector to a heuristic module that checks if a feasible candidate solution to problem (B) exists with the associated value of the $B R$ vector. Our objective function in (B) serves as the fitness cost function.

## IV. SIMULATION RESULTS

In this section we present the simulation results for a sample Low Voltage Network. We apply CSSA and EDA sequentially to it and show the result in stages. The network over which we intend to deploy the power line communication infrastructure is shown in Fig.5.
![img-4.jpeg](img-4.jpeg)

Fig. 5
The circles in the figure represent the electric poles, which are numbered and the line connections represent the electric supply connections. The users are connected to the network on these lines but are not shown in the figure. For simulation we use the following data: The distance between the poles is 100 m and the PLC range, R is 400 m . The total number of users is 560 , with each line connecting any pair of adjacent poles having 20 users connected to it. The BS capacity is 200 users. First we run CSSA over this LVN and it results in Fig.6.
![img-5.jpeg](img-5.jpeg)

Fig. 6
The red circles are the selected candidate sites for BS/repeater installation. Next we pass this CSSA resulting network through our EDA scheme which results in Fig.7. The green circles are the sites where BS is installed and reds are the sites with repeater installation. The dotted boundaries represent the PLC cells of each installed BS. In this particular simulation we had 560 users, with each BS having a capacity of 200 users; thus
we ended up with the optimal number of installed BSs, which is 3 in this case.
![img-6.jpeg](img-6.jpeg)

Fig. 7

## V. CONCLUSION

In this paper we presenter network modeling and an EDAbased network planning algorithm for power line communication access systems. It can be used for network deployment in various fields of interest like broadband internet, telephony and smart grid applications. We plan to carry this work forward and include extra parameters in power line communication network modeling and planning.
