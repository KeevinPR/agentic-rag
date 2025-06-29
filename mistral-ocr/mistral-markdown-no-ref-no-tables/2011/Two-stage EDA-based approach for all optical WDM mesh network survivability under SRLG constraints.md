# Two-stage EDA-based approach for all optical WDM mesh network survivability under SRLG constraints 

Jianyong Sun*<br>CPJB, School of Bioscience, The University of Nottingham, Nottingham, UK

## A R T I C L E I N F O

Article history:
Received 22 August 2008
Received in revised form 6 January 2010
Accepted 17 January 2010
Available online 25 January 2010

Keywords:
Shared-risk-link-group
Routing and wavelength assignment problem
Greedy heuristic
Estimation of distribution algorithm

## A B S T R A C T

In this paper, a two-stage evolutionary algorithm is proposed to solve an $\lambda 7^{2}$-complete telecommunication problem-all optical wavelength-division multiplexing (WDM) mesh network survivability under shared-risk-link-group (SRLG) constraints. First of all, a novel greedy heuristic with two control parameters is developed to construct feasible solutions of the telecommunication problem. An estimation of distribution algorithm (EDA) with guided mutation is applied to search for optimum settings of the two control parameters in respective two stages. Given the found best control parameters, an optimal solution of the considered problem can be constructed by the greedy heuristic. Experimental results show that the proposed approach compares favorably against the best-known evolutionary-based algorithm in 26 out of 30 test instances in terms of solution quality within given time limit.
(c) 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Wavelength-division multiplexing (WDM) technology greatly increases the network capacities. It is generally believed that the new generation Internet will be mainly based on WDM technology [30]. The network capacity is greatly increased, survivability of an optical WDM mesh network becomes more and more crucial both for customers and providers since a link or node failure could cause huge damages. Therefore, network providers are eager to design a survivable network to minimize the loss of data.

Many protection schemes have been developed for network survivability. Among these schemes, the shared path-protection scheme has been found that can use less network sources [35]. In the path-based protection scheme, a lightpath ${ }^{1}$ that transports connection requests by wavelengths from the source node to the destination node is called as a primary or working path. ${ }^{2}$ To protect the working path against single link failure, ${ }^{3}$ a protection or

[^0]backup path disjointed with the working path is routed between the source and destination nodes. Wavelength channels should be assigned on links involved in the working and backup paths. Hence, the network survivability problem is also known as the routing and wavelength assignment problem (RWAP).

A number of heuristics have been proposed for the routing and wavelength assignment problem, for examples in [1,29,28,45] to just name a few, based on different protection schemes. But most of them do not consider the shared-risk-link-group (SRLG) constraints. In a WDM mesh network, fibers containing in the same duct, or cable, belong to the same SRLG. Fibers in the same SRLG could fail simultaneously because of destructive events, such as earthquake. These fibers share the same "risk". Due to the existence of SRLG, the RWAP becomes much more complicated. Actually, it has been proved to be $\lambda 7^{2}$-complete [19]. Fig. 1 shows a simple example of WDM network under SRLG constraints.

In the figure, the example WDM network has five nodes and seven ducts in the duct-layer. In Fig. 1(a), the grey rectangles represent the ducts used to wrap the fibers (the solid lines in the plots). Fig. 1(b) shows the network in the link-layer. In the plot, two fibers $(1,2)$ and $(2,3)$ are bundled together by the same duct. In Fig. 1(c), the protection scheme is shown for two connection requests, which are represented by solid and dashed arrow lines respectively. To transmit the request from node 2 to node 3 , in case that we do not consider the duct topology, the two paths $2 \rightarrow 3$ and $2 \rightarrow 0 \rightarrow 1 \rightarrow 3$ can be used as the working path and the protection path, respectively considering single-link-failure protection. Alternative protection path is $2 \rightarrow 1 \rightarrow 2$. In case that the duct between node 2 and 3 fails, the alternative path cannot be used as the pro-


[^0]:    * Corresponding author at: CPJB, School of Bioscience, The University of Nottingham, Sutton Bonington, UK.

    E-mail address: j.sun@cpib.ac.uk.
    ${ }^{1}$ In a WDM network without wavelength converter, a lightpath is a connection between a source node and a destination node occupying the same wavelength. Many fiber links may be involved in a lightpath to provide an all-optical connection between the source and destination nodes.
    ${ }^{2}$ We do not differentiate the two terms in the paper.
    ${ }^{3}$ Since the optical cross-connect (OXC), a device to switch an optical signal from an incoming fiber to an outgoing fiber on the same wavelength, in an all-optical WDM mesh network is seldom broke, we only consider link failure in this paper.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Example of a duct-layer WDM network.
tection path. Moreover, in assigning wavelength for the paths, the duct-layer topology should also be considered. For example, to protect the requests from node 2 to node 3 , and from node 2 to node 4 , we use the paths $2 \rightarrow 0 \rightarrow 1 \rightarrow 3$ and $2 \rightarrow 0 \rightarrow 1$ as shown in Fig. 1(c), respectively. We may want to use the same wavelength on links $\langle 2,0\rangle$ and $\langle 2,1\rangle$ for the protection of the primary paths $2 \rightarrow 3$ and $2 \rightarrow 1$ because they are fiber-disjoint. However, notice that the two primary paths go through the same duct ( 2,3 ), the two paths may fail at the same time. Therefore, we should use different wavelengths for the two protection paths.

From the simple example, one can see that the routing and wavelength assignment under the SRLG constraints is much more difficult than the problem without considering the SRLG constraints. More problems should be considered when carrying out routing and wavelength assignment. Zang and Mukherjee [46] used integer linear programming (ILP) to model the RWAP in WDM mesh network under SRLG constraints with various protection schemes. According to their analysis, the complexity of integer linear programming (ILP) formulation for the shared-path protection of the RWAP under SRLG constrains is $C\left(N^{4} W D\right)$ in terms of the number of decision variables, where $N$ is the number of nodes, $W$ is the number of wavelengths available on each link and $D$ is the number of ducts. For the simple example, if we set $W=10$, the number of variables is in the magnitude of 777,600 . Therefore, it is not practical to use exact algorithms (such as branch and bound algorithm) for even a small-size network RWAP due to the inhibitive computational cost to be used.

Fortunately, the development of nature-inspired optimization algorithms, such as genetic algorithm [11], estimation of distribution algorithm [24], and many others, provides us a possibility to find a near global optimum in a reasonable short time for the $\lambda 7^{2}$-complete problems. We could follow the ILP formulation of the considered problem to represent a solution as a vector of integer variables. However, the size of the solution vector will be as many as millions even for a medium-sized network instance. This will cause low-efficiency of the nature-inspired algorithm if the integer solution representation is adopted. In light of this, to make the
nature-inspired algorithm efficient on the considered problem, we have to design suitable solution representation.

In this paper, we propose an evolutionary-based approach with deliberate solution representations for the RWAP under SRLG constraints. First of all, a parameterized greedy heuristic is developed to construct solutions of the problem. The greedy heuristic includes mainly three parts, i.e. the working paths routing procedure, the protection path routing procedure and the wavelength assignment procedure since a solution of the RWAP includes the routing paths (the working paths and protection paths) for the connection requests and the wavelengths assigned on these paths. In the greedy heuristic, to route the working paths, a set of candidate paths (called PathList) for each connection request is firstly constructed. The working path routing procedure selects paths from the prepared PathList as the working paths. The protection path routing procedure constructs protection paths iteratively in an order of the connection requests. The wavelength assignment procedure assigns wavelengths for the working and protection paths, and returns a network cost as a measure of the solution.

There are two control parameters, i.e. the combination of the available working paths for the connection requests and the order of connection requests for protection paths, in the greedy heuristic. Given a pair of control parameters, a feasible solution of the considered problem can be uniquely constructed. Therefore, we can optimize the considered problem through searching optimal control parameters. In this paper, the estimation of distribution algorithm [24] with guided mutation [49] is applied to find optimal parameters of the heuristic. The proposed algorithm includes two stages. The first stage searches for the optimal combination of the candidate working paths for the connection requests. The second stage searches for the optimal order of the connection requests for the protection paths routing.

The proposed algorithm was compared with the best-known EA-based algorithm (called BH/EA/G) [49] and a pure random algorithm based on the proposed greedy heuristic, on a suite of test networks with different network topologies. The comparison results showed that the proposed algorithm outperforms BH/EA/G in 26 out of 30 test instances, and the pure random algorithm on all the test instances, in terms of solution quality with the same computational cost.

The rest of the paper is organized as follows. Section 2 gives a review on the related heuristics/meta-heuristics work to the telecommunication optimization problems. The main contribution of the paper is also presented. Section 3 defines the considered shared-path protection RWAP under SRLG constraints. Section 4 presents the proposed greedy heuristic. The EDA-based algorithm for optimizing the problem w.r.t. the control parameters is introduced in Section 5. Computational results are given in Section 6. Section 7 concludes the paper.

## 2. Related work

Optimization problems in telecommunication have been extensively studied in the literature from different perspectives. Readers are referred to [37] for details about the problems including planning and design of telecommunication networks, routing, network protection, grooming, restoration, wireless communications, network location and assignment problems, Internet protocol, world wide web, stochastic issues and many others. In this paper, we focused on the application of heuristics/meta-heuristics to the routing and wavelength assignment problem. For a comprehensive review, readers are referred to [6].

Heuristic algorithms have been applied for dynamic RWAP considering different objectives, or based on different protection schemes. For examples, Oki et al. [32] proposed a weighted-SRLG selection algorithm (WSRLG) for finding a given number of disjoint

paths between the source and destination nodes with the smallest cost. Xiao et al. [41] presented a simple heuristic as well for finding the maximum disjoint paths. Lee et al. [26] developed a hierarchical scheme for handling multiple simultaneous failures under SRLG constraints. In the papers of [42,43], the multiple segment protection scheme is proposed for the SRLG protection. Heuristics have also been proposed for the static RWAP [33,34,38,40,50].

Additionally to these heuristics, many meta-heuristics including genetic algorithms, particle swarm optimization (PSO), artificial immune systems (AIS), ant colony optimization (ACO), and viral systems (VS) and many others have also been applied for the telecommunication optimization problems.

The artificial immune systems, firstly introduced by Farmer et al. [10] have continued being applied to several network problems. For examples, an AIS developed in [4] is applied to find a set of $k$ Spanning trees; the AIS in [22,25] is applied to the routing problem. The viral system (VS) [7] has been applied to a library of medium-to-large-sized cases of the Steiner problem.

Particle swarm optimization (PSO), firstly introduced by Kennedy et al. [9,23], has been applied to the static and dynamic routing and wavelength problems in [17,36] and [15,16,18], respectively. An adaptive PSO has been applied to the RWA [5], a discrete PSO has been applied to the multiple destination routing problem [47]. Branch-and-bound and PSO have been hybridized to the peer-to-peer optimization in large unreliable networks [3]. The multiple constrained QoS multicast routing has been addressed by the PSO as in [21]. Algorithms based on other swarm intelligence including ant colony [8] and bee colony [31] have been applied to the network optimization problems, such as dynamic server allocation problem in Internet hosting centers [31], the RWAP [27], the multicast Routing problem [20], and so on.

However, few efforts have been devoted to the shared-path protection scheme for the static RWAP with SRLG-constraints. Among these efforts, [39] modeled the survivable network problems as an integer linear programming to maximize the revenue and proposed a tabu search heuristic considering different path protection schemes including dedicated, shared and unprotected. Zang and Mukherjee [46] proposed an off-line heuristic to minimize the total number of wavelengths used on links in the network. Zhou and Mouftah [50] proposed a genetic algorithm for long-haul WDM mesh network sparse capacity planning with SRLG constraints to minimize the cost and load balancing. In their algorithm, a solution (configuration) of the static RWAP under SRLG is encoded to be a binary string. The classical GA is applied. However, as we stated in Section 1 that even for a small-size network, the length of the binary string will be prohibitively large in their algorithm. It is wellknown that for such a large binary encoding, GAs would be very time-consuming and low-efficiency. In our previous work [49], a two-stage EDA-based approach has been proposed for the problem in order to make the application of EAs efficient. The developed algorithm has been experimentally justified to be more effective than the heuristic developed by [46] in terms of solution quality. The proposed algorithm is currently the best evolutionary-based algorithm for the RWAP under SRLG constraints.

In this paper, the problem we studied the same problem as in [49]. Also, the same two-stage algorithmic framework is applied. The most important difference to the constructive heuristic developed in [49] is that a simple yet natural heuristic is proposed for the working and protection paths routing. The novel working path construction scheme makes the working path routing process easy to be understood. Moreover, when applying EDA to find the optimal routing and wavelength assignment solution, the solution representation in the EDA will be totally different to the one in [49]. And hereafter new EDA components should be developed to adapt to the new solution representation. Moreover, a new repair heuristic and an intelligent initialization heuristic can be developed thanks
to the new working path routing heuristic. As well known in the evolutionary computation community, the solution representation defines the fitness landscape of the problem to be searched by the EA. Actually, it is the ruggedness of the fitness landscape that affects the performance of an evolutionary algorithm at most. Based on the new routing and wavelength assignment heuristic, the developed EDA is expected to perform better than the EDA in [49] in terms of solution quality, and faster than that in terms of computational time. These claims will be justified in the experimental studies.

## 3. Problem definition

The static RWAP under SRLG constraints can be modeled as an optimization problem on a simple directed graph. The same as in [49], the problem can be described as follows. Given:

1. $V$ : the set of nodes in the graph under consideration.
2. $E$ : the set of directed links (edges) in the graph.
3. $W$ : the number of wavelengths available on each link. The wavelengths are numbered from 1 to $W$.
4. $D$ : the set of ducts.
5. $R$ : the set of connection requests. $M=|R|$. The requests are numbered from 1 to $M$. Each connection request has a source node and a destination node. ${ }^{4}$ It requires a working lightpath and a backup lightpath from its source to its destination. In this paper, a lightpath is a directed path in which all the links use the same wavelength.
6. $G$ : the set of SRLGs. If two links are in the same SRLG, we say that they are SRLG-joint. Otherwise, we call them SRLG-disjoint.

The goal is to determine a working lightpath and a backup lightpath for each connection request in $R$. The constraints are:

C1 The number of wavelengths used on each link cannot excess $W$, or in mathematical form:

$$
\sum_{k=1}^{D_{0}}\left[W_{w}(i, j)+W_{p}(i, j)\right] \leq W, \quad \forall(i, j) \in E
$$

where $W_{w}(i, j)$ and $W_{p}(i, j)$ are the wavelength used by the working lightpath and backup lightpath that pass through the link $(i, j)$.
C2 The working lightpath and its backup lightpath for each connection request must be SRLG-disjoint. If link $e_{1}$ is used in the working lightpath and $e_{2}$ in its protect lightpath, then $e_{1}$ and $e_{2}$ are SRLG-disjoint. Otherwise, we call them SRLG-joint. In mathematical form, the constraints on SRLG can be written as follows:

$$
\sum_{1 \leq i, d \leq N} \delta_{i, j, w}^{i, d, w} \leq 1 \forall \kappa \in D, \quad 1 \leq w \leq W
$$

where $\delta_{i, j, w}^{i, d, w}$ takes 1 if wavelength $w$ is used on the link $(i, j)$ by some back lightpath from node $s$ to node $d$ when duct $x$ fails; 0 otherwise.
C3 Two working lightpaths cannot use the same wavelength on the same link, or in mathematical form:

$$
m_{i j}^{w}+\sum_{1 \leq i, d \leq N} F_{i j}^{i, d, w} \leq 1
$$

[^0]
[^0]:    ${ }^{4}$ Two different requests in $R$ may have the same source and destination.

for all link $\langle i, j\rangle$ where $m_{i j}^{w}$ takes 1 if wavelength $w$ is used by some backup lightpath that occupies link $\langle i, j\rangle ; 0$ otherwise, and $F_{i j}^{s, d, w}$ is 1 if wavelength $w$ on link $\langle i, j\rangle$ is carrying traffic from source $s$ to destination $d, 0$ otherwise.
C4 A protection lightpath cannot share the same wavelength on the same link with any working lightpaths, or in mathematical form:
$m_{i j}^{w} \times t_{i j}^{s, d, w}=0, \quad \forall\langle i, j\rangle,\langle s, d\rangle \in E$
where $t_{i j}^{s, d, w}$ takes 1 if wavelength $w$ is used for the working path of the request $\langle s, d\rangle$ that traverse link $\langle i, j\rangle, 0$ otherwise.
C5 If two working lightpaths are SRLG-joint, their protection lightpaths cannot use the same wavelength on the same link, or in mathematical form:
$G_{i j}^{s, d, w} \times G_{i j}^{u, e, w}=0, \quad \forall\langle i, j\rangle \in E \quad$ and $\quad W P_{s d} \bigcap W P_{u v}=\varnothing$
where $G_{i j}^{s, d, w}$ takes 1 if wavelength $w$ on link $\langle i, j\rangle$ is used as protection for connection request from source $s$ to destination $d$, and $W P_{s d}$ is the working path for connection request from $s$ to $d$.

The objective is to minimize the cost:
$\sum_{e \in E}\left(F_{e}+S_{e}\right)$
where $F_{e}$ is the number of wavelengths on link $e$ used in working lightpaths and $S_{e}$ the number of wavelengths on link $e$ used in backup lightpaths.

## 4. Greedy heuristic

Since the objective of this problem is to minimize the total number of wavelengths used in a routing scheme, a heuristic for the above problem should have the following properties:

1. The wavelength sharing in the backup lightpaths should be maximized.
2. SRLG-disjointness among the working lightpaths should be encouraged such that backup lightpaths have a good chance to share wavelengths.
3. The lightpaths should be as short as possible, since a wavelength needs to be assigned to each link traversed by these lightpaths.

The proposed greedy heuristic consists of four phases taking the constraints $\mathbf{C 1}-\mathbf{C 5}$ into account. The four phases are the working path routing, the protection path routing, the repair heuristic, and the wavelength assignment heuristic. In the following sections, we will use the example described in Section 1 to demonstrate the greedy heuristic. In the example, we assume that two connection requests from node 2 to node 3 and from node 2 to node 4 need to be routed and protected.

First of all, to route the working paths for each connection request $i \in R$, we construct a set of paths using Yen's K-shortest path routing algorithm [44] as the candidate paths without taking the SRLG constraints into consideration, and denote the set of candidate paths as PathList $\left(=P_{l 1}, \ldots, P_{u_{l}}\right), 1 \leq i \leq M$, where $u_{l}$ is the number of the available paths for connection request $i$. The $u_{l}$ 's, $1 \leq i \leq M$ are not necessary to be equal. It is worth pointing out that these candidate paths need to be computed only once. The underlying rationale is that no matter what routing algorithms are to be applied, the working paths have to be among these candidate paths.
![img-1.jpeg](img-1.jpeg)

Fig. 2. The routing paths of the connection requests of the example network.

Example: Recall the example network, we see that the candidate paths for connection request $(2,3)$ are $P_{11}=2 \rightarrow 3, P_{12}=2 \rightarrow$ $1 \rightarrow 3, P_{14}=2 \rightarrow 0 \rightarrow 3$, and $P_{14}=2 \rightarrow 0 \rightarrow 1 \rightarrow 3$, while for $(2,4)$, the paths are $P_{21}=2 \rightarrow 3 \rightarrow 4^{(1)}, P_{22}=2 \rightarrow 3 \rightarrow 4^{(2)},{ }^{5} P_{23}=2 \rightarrow$ $1 \rightarrow 3 \rightarrow 4, P_{24}=2 \rightarrow 0 \rightarrow 3 \rightarrow 4$ and $P_{25}=2 \rightarrow 0 \rightarrow 1 \rightarrow 3 \rightarrow 4$. It can be noted that $u_{1}=4$ and $u_{2}=5$.

In the first phase of our greedy heuristic, we choose a combination of the candidate paths PathList $1,1 \leq i \leq M$ as the working paths for the connection requests in $R$. In the second phase, a heuristic is presented to compute backup paths for all the working paths established in the first stage. Since there is no guarantee that the constructed solution to the RWAP under SRLG constraints in the first two stages is feasible, a heuristic is proposed in the third phase to repair the infeasible solutions if necessary. In the fourth phase, we adopted the same heuristic used in [49] to assign a wavelength to each path constructed in the previous three phases and returns a network cost.

### 4.1. The working and protection path routing scheme

The working path routing procedure is fairly easy. We only need to chooses a combination of the constructed candidate working paths. Specifically, given a combination $\mathbf{x}=\left(x_{1}, \ldots, x_{M}\right)$ where $x_{i} \in\left\{1,2, \ldots, u_{i}\right\}$, we can interpret the combination to be a set of working paths. That is, for the $i$ th connection request, its working path is selected as the $x_{i}$ th path in PathList. The working path routing procedure returns a set of working paths WP. It can be seen that the set of working paths $W P$ is uniquely defined given $\mathbf{x}$. Moreover, it is guaranteed that all the connection requests are routed so long as $\forall i, u_{i} \neq 0$.

Example: For the example network, if a solution is represented as $\mathbf{x}=(2,5)$, the working path routed for the connection requests are then $P_{12}$ and $P_{25}$, respectively. The working paths set $W P$ is then $\langle 2 \rightarrow 1 \rightarrow 3 ; 2 \rightarrow 0 \rightarrow 1 \rightarrow 3 \rightarrow 4\rangle$ as shown in Fig. 2.

Given a set of working lightpaths $W P=\left\{w p_{1}, w p_{2}, \ldots, w p_{M}\right\}$ for all the connection requests in $R$ (where $w p_{r}$ is for request $r$ ). The goal of the protection path routing is to route $b p_{r}$ for each connection request $w p_{r}$. The routing is based on a permutation $\sigma=\left(\sigma_{1}, \ldots, \sigma_{M}\right)$ of the working paths. Suppose that for the first $K$ working paths, a set of protection paths $B P^{K}=\left\{b p_{o_{1}}, \ldots, b p_{o_{K}}\right\}$ have been routed (in the case of $K=0$, no backup lightpath has been established). The protection path $\sigma_{K+1}$ for the corresponding working path is as follows:

[^0]
[^0]:    ${ }^{5}$ Since there are two links between node 3 and node 4 , we use superscripts (1) and (2) to describe the resultant different paths. In the experiments, we introduce a new node between the nodes 3 and 4 to differentiate the paths.

![img-2.jpeg](img-2.jpeg)

Fig. 3. The routing paths of the connection requests of the example network.
Step 1 Let $H$ be the set of links that
(a) have been used by working lightpath $w p_{\sigma_{K+1}}$, or
(b) are SRLG-joint with links in working path $w p_{\sigma_{K+1}}$.

Step 2 Applying Dijkstra algorithm to the graph $(V, E \backslash H)$ with the equal link length to find the shortest path from the source to the destination in connection request $\pi_{K+1}$ as backup lightpath $b p_{\sigma_{K+1}}$. If Dijkstra algorithm fails in finding a path, set $b p_{\sigma_{K+1}}=\varnothing$.

The algorithmic parameters $\sigma=\left(\sigma_{1}, \sigma_{2}, \ldots, \sigma_{M}\right)$ and the set of working lightpaths WP can be regarded as the input to the protection path routing scheme, and the backup lightpaths $B P=$ $\left(b p_{1}, b p_{2}, \ldots, b p_{M}\right)$ are its output.
Remark 1. If lightpath $b p_{\sigma_{K+1}}$ uses any links in $H$ defined in Step 1 , it will lead to an infeasible routing. For this reason, the protection path routing scheme prevents $b p_{\sigma_{K+1}}$ from using these links.
Remark 2. If there is no path from the source node to the destination node for request $\sigma_{K+1}$ in graph $(V, E \backslash H)$ or $w p_{\sigma_{K+1}}$, the protection path routing scheme will set $b p_{\sigma_{K+1}}=\varnothing$. In this case, the set of source-destination pairs with no protection-paths assigned is returned as $I$, the set of the corresponding indices of the working paths is returned as $J$.

Example: For the example network, if the order $\sigma=(2,1)$, according to the protection routing heuristic, firstly we need to route for the second connection request, i.e. the request from node 2 to node 4 , and then the first request from node 2 to node 3 . Fig. 3 shows the routing for the second request. In the figure, the working path is denoted by the arrow solid line. Moreover, the links that are contained in the set $H$ are shown by red cross according to Step 1 in the heuristic. The red crosses show the links specified by Step 1(b), i.e. the links that have been used by the working path $W P_{2}$, while the blue cross shows the link specified by Step 1(c). It can be seen that when the Dijkstra algorithm is applied, no path can be found. This means that $b p_{\sigma_{J}}=\varnothing$. In other words, the routing defined by $(\mathbf{x}, \sigma)$ is infeasible.

### 4.2. The repair heuristic

It can be seen that a solution generated by means of the protection path routing procedure may be infeasible. We propose the following heuristic to repair the infeasible solution. Suppose a solution is returned with a working path set WP, a protection path set $B P$, and an unassigned set of source-destination pairs $I$ and corresponding indices $J$. The repair heuristic for the $k$ th source-destination pair in $I(\ell=I(k)$ the index of the connection request) is shown as follows.

Step 1 Set $j=0, i:=J(k)$ (i.e. $i$ is the index of the candidate working path in PathList $_{f}$ ) and $P l:=\varnothing$.
Step 2 If $P_{l J} \neq W P_{f}$, perform the protection path routing scheme for the connection request $\ell$ (cf. Section 4.1) to find a protection path $p ; P l:=P l \bigcup p ;$ Set $j:=j+1$.

Step 3 If $j$ is larger than the number of available path in PathList $_{\ell}$, stop. Calculate the lengths of the paths in $P l$ (if some path $p$ is $\varnothing$, simply set its length to be $\infty$ ) and take the path with minimum length as the protection path for the connection request $\ell$. Otherwise, go to Step 2.

Remark 1. To make the infeasible solution feasible, the repair heuristic works on the source-destination pairs whose protection path is not assigned. The heuristic replaces the working path of a source-destination pair with another potential path in the path list. The path with the minimal length is chosen to be the protection path. This can most likely decrease the wavelength used.
Remark 2. It should be pointed out that the repair heuristic can still not guarantee that all the protection paths can be routed since the found protection path $p$ in Step 2 could be $\varnothing$. However, since we iterate over all the candidate working paths, if no protection path can be found at all, the only reason is that there are no two SRLGdisjoint paths in the network topology. In our experiment, we will ignore these kind of network instances.

Example: In the example network, the protection path for the request $\sigma_{1}$ cannot be routed. When applying the repair operation, we need to check one by one the paths in PathList $_{\sigma_{1}}$ other than the used working path to find the working path that (1) its corresponding protection path can be routed; and (2) its protection path has the minimum number of length. In the example, from Fig. 3(b), we see that if we choose $P_{11}=2 \rightarrow 3 \rightarrow 4$ as the working path, its protection path can be routed as $2 \rightarrow 0 \rightarrow 1 \rightarrow 3 \rightarrow 4$. For request $\sigma_{2}$, it can be routed as $2 \rightarrow 0 \rightarrow 3$. Fig. 3(c) shows the working and protection path routing results.

### 4.3. The wavelength assignment scheme

Given the set of working lightpath $W P$ and the set of backup lightpath $B P$ for all the connection requests in $R$, the task of wavelength assignment scheme is to assign wavelengths to each working lightpath and backup lightpath such that the total number of wavelengths used is minimized under the following constraints:

CW1 two working lightpaths must be assigned different wavelengths if they traverse the same link,
CW2 a working path and a backup lightpath must be assigned different wavelengths if they traverse the same link, and
CW3 two backup lightpaths have to be assigned different wavelengths, if they traverse the same link and their corresponding working lightpaths are SRLG-joint.

Viewing each lightpath as a node in a graph and each wavelength as a color, two nodes (lightpaths) are defined to be adjacent if they must be assigned different wavelengths. Then, the above problem becomes the well-known $\lambda \mathcal{P}$-hard graph coloring problem. We use a first-fit heuristic for this problem. We assume in the heuristic that the number of the wavelengths available are infinite,

the wavelengths are indexed by $1,2, \ldots$. The heuristic works as follows:

Step 1 Set $P=B P \cup W P$. Remove all the empty paths from $P$.
Step 2 Assign wavelength.
Step 2.1 Remove a lightpath $p$ from $P$.
Step 2.2 Assign the allowable wavelength with the smallest index to $p$. A wavelength is allowable if assigning it to $p$ does not violate CW1-CW3.
Step 3 If $P=\varnothing$, stop. Otherwise, go to Step 1.
There are several ways in Step 1 to select from $P$ a lightpath to remove. In our implementation, we randomly pick a lightpath from $P$ in Step 1. WP and $B P$ are inputs to the wavelength assignment heuristic while the output is a wavelength assignment to each lightpath in $P=B P \cup W P, a: P \rightarrow\{1,2, \ldots\}$.
Remark 1. The wavelength assignment $a$ generated in the working path procedure will satisfy the constraints CW1-CW3. However, if the number of wavelengths used in $a$ is more than $W$, it may violate the constraint $\mathbf{C 1}$ (i.e., the number of wavelengths used on some links may be more than $W$ ). This is prohibited in the following search procedure, we will set the network cost of these violated solutions as $\infty$.

Example: Fig. 3(c) shows the wavelength assignment on these links used for the working and protection paths. In the figure, the numbers in each link is of the ' $a / b$ ' form, where ' $a$ ' is the number of wavelengths used for the working path, and ' $b$ ' is the number for the protection path.

### 4.4. Brief summary of the greedy heuristic

According to the previous subsections, the proposed greedy heuristic for the routing and wavelength assignment can be summarized as follows.

- For each connection request $r \in R$ with source node $s$ and destination node $d$, Yen's algorithm is applied to find all the paths from $s$ to $d$, denote the paths as PathList. We associate each path in the list an integer number from 1 to $u_{i}$.
- To route the working paths for the connection requests, we generate a vector of $M$ integers $\mathbf{x}=\left(x_{1}, \ldots, x_{M}\right)$, while $x_{i}$ variable is randomly generated from $\left(1, \ldots, u_{i}\right)$. The solution $\mathbf{x}$ can be easily interpreted as a set of working paths for the connection requests.
- The protection path routing for a connection request is carried out by using the Dijkstra algorithm to find the shortest path of a graph induced from the original graph by discarding the prohibited links as defined in Section 4.1. The routing order is a permutation $\sigma=$ $\left(\sigma_{1}, \ldots, \sigma_{M}\right)$ of the connection requests.
- If there are some protection paths that are $\varnothing$, the repair heuristic is applied to make the routing feasible.
- If all the working and protection paths are feasible, the wavelengths can be assigned on the used links as described in Section 4.3.

It can be seen that the routing is solely determined by a categorical vector $\mathbf{x}$ and a permutation $\sigma$. After the routing and wavelength assignment procedure, if the routings are successful, the number of wavelengths assigned on the links for the working paths and protection paths will be returned. The cost of the routed network, or the objective value of the decision variables $(\mathbf{x}, \sigma)$, can be computed according to Eq. (1).

Any solutions generated by GH will satisfy constraints C2-C5. An inappropriate setting of $\mathbf{x}$ and $\sigma$ may generate a solution which is incomplete (there are no backup lightpaths for some requests) or/and violates constraint C1. In these cases, the network cost of the parameter settings is set to be $\infty$.

It is not easy to develop a simple mathematical model for the relationship between the algorithmic parameter settings and the quality of the solution obtained. Finding an optimal parameter settings turns out to be a black box optimization problem. In this paper, we propose to use estimation of distribution algorithm (EDA) as a tool for tuning the algorithmic parameters. The proposed EDA and the whole algorithm will be described in the following.

## 5. The algorithm

### 5.1. Estimation of distribution algorithm

EDAs are a type of model-based evolutionary algorithm (EA). Like general EAs [13], EDAs also maintain and evolve a population of solutions until stop criteria are met. Different from general EAs, EDAs generate offspring by sampling from a previously constructed probabilistic model instead of by applying the genetic operators such as crossover and mutation operators. A number of EDAs have been proposed both for global continuous optimization problems and combinatorial optimization problems and achieved great success [14]. The framework of the EDA can be summarized in Alg. EDA.

## Algorithm $E D A\left(\Theta_{1}\right)$

Input: parameters $\Theta_{1}$.
Output: The best solution found $\mathbf{x}^{*}$.

1. Parameter Settings. Set appropriate algorithmic parameters, such as population size, selection size, initial probability model $\mathcal{P}(0)$, etc.
2. while computational budget has not been exceeded,
3. Initialization. Set $t:=0$. Generate the initial population $S(0)$. Evaluate the fitness of the population.
Selection. Select promising solutions from $S(t)$.
4. Modeling. Construct a probability model $\mathcal{P}(t)$ based on the selected solutions.
5. Sampling. Sample $N$ offspring from $\mathcal{P}(t)$. Evaluate the sampled offspring.
6. Replacement. Partially or fully replace $S(t)$ by the sampled solutions to form $S(t+1)$. Set $t:=t+1$.
7. end while;
8. Find the best solution $\mathbf{x}^{*}$ with the lowest objective value from $S(t)$ and return it.

From the framework, one can see that the generation of new offspring is through sampling from a probability model which is constructed from some selected promising solutions. On the contrary, in traditional genetic algorithms (GAs), new offspring is created by using crossover and mutation operations. No explicit model is applied in traditional GAs. The advantage of EDA is that the evolutionary search is explicitly (rather than implicitly as in GAs) guided by the probability model. The most important components of the EDAs include the model construction, and the sampling procedure.

For the considered static RWAP with SRLG-constraints, EDA works on top of the proposed greedy heuristic to tune the control parameters in respective two stages. In the following, we first describe the main components, including initialization, selection, probability model construction and new offspring sampling, of the EDA with category (for working path routing) and permutation (for protection path routing) representations. Then the whole twostage evolutionary approach for the optimization of the RWAP is proposed.

### 5.2. Initialization of population and probability model

To apply EDA to an optimization problem with permutation representation, we use a probability matrix $\mathcal{P}=\left(p_{i j}\right), 1 \leq i, j \leq M$ to represent the probability model, where $p_{i j}$ denotes the probability of assigning element $i$ to location $j$. It is initialized to be
$\mathcal{P}_{0}=\left(\begin{array}{cccc}\frac{1}{n} & \ldots & \frac{1}{n} \\ \vdots & \ddots & \vdots \\ \frac{1}{n} & \ldots & \frac{1}{n}\end{array}\right)$
The search space is the set of all possible permutations $\Pi$. EDA randomly chooses $N$ permutations from $\Pi$ to constitute the initial population $S(0)$.

To apply EDA to problem with a categorical representation, a probability matrix $\mathcal{Q}=\left(q_{i j}\right)$ is adopted, where $q_{i j}$ represents the probability of using the candidate path $j$ to route the $i$ th connection request. It is initialized to be
$\mathcal{Q}_{0}=\left(\begin{array}{ccc}\frac{1}{u_{1}} & \ldots & \frac{1}{u_{M}} \\ \vdots & \ddots & \vdots \\ \frac{1}{u_{1}} & \ldots & \frac{1}{u_{M}}\end{array}\right)$
The search space is the set of all the combinations of the constructed candidate paths.

To initialize the population for problems with categorical representation, we could generate a set of random solutions. In this paper, we initialize the population based on the principles mentioned in Section 4 for routing the working paths. Specifically, each combination is constructed as follows. The selection of potential working paths for the connection requests follows a random order $\pi=\left(\pi_{1}, \ldots, \pi_{M}\right)$ of the connection requests. Suppose that for the connection requests $\pi_{1}, \ldots, \pi_{K}(1 \leq K<M)$, a set of working paths $W P^{K}=\left(w p_{\pi_{1}}, \ldots, w p_{\pi_{K}}\right)$ have been selected from the candidate paths (in the case of $K=0$, a path is randomly selected from PathList $_{\pi_{1}}$ ). The working path $w p_{\pi_{K+1}}$ for connection request $\pi_{K+1}$ is as follows:

Step 1 For each potential path $p_{i} \in$ PathList $_{\pi_{K+1}}$, calculate its similarity degree as follows: first set the degree value $s_{i}$ to zero, then for each link $\ell$ in $p_{i}$, if $\ell$ exists in any one of $P_{\pi_{k}}, 1 \leq k \leq K$, set $s_{i}:=s_{i}+1$;

Step 2 Select the path with the minimal similarity degree, say $p_{\min }:=\operatorname{argmin}_{1 \leq i \leq u_{K+1}} s_{i} \cdot P:=P \bigcup p_{\min } ;$

The similarity degree of a path $p$ to a path set $P$ in Step 1 is computed as the sum of the number of links in $p$ which are the same as to the links in the path set $P$. To increase the SRLG-disjoint degree of the set of working paths, the working path routing procedure encourages the use of the candidate paths with small similarity degree to previously routed paths. The reason is that a path with small similarity degree is very likely to be SRLG-disjoint with the other paths. The working path routing procedure tries to establish a set of working paths which are as small similarity degree as possible.

The purpose of the construction is to make the initial population as informative as possible. The high-quality initial population can make the following search for optimal solutions more effective than random initial population.

### 5.3. Selection and update of probability matrix

Assume that the population at generation $t$ is $S(t)=$ $\left(\pi^{1}, \pi^{2}, \ldots, \pi^{N}\right)$ with cost $\mathcal{C}=\left(c_{1}, c_{2}, \ldots, c_{N}\right)$ and the probability matrix at generation $t-1$ is $\mathcal{P}_{t-1}\left(\right.$ or $\left.\mathcal{Q}_{t-1}\right)$. The best $N / 2$ individuals are selected as $\mathcal{H}(t)=\left(\sigma^{1}, \ldots, \sigma^{N / 2}\right)$ for the aim of probability matrix construction. That is, the probability matrix $\mathcal{P}_{t}=\left(p_{i j}(t)\right)$ (or $\left.\mathcal{Q}_{t}\right)$ is updated by PBIL [2] as follows:
$p_{i j}(t)[$ or $\left.q_{i j}(t)\right)=(1-\beta) \cdot \sum_{k=1}^{N / 2} I_{i j}\left(\sigma^{k}\right)+\beta \cdot p_{i j}(t-1)\left(\right.$ or $\left.q_{i j}(t-1)\right)$,
$1 \leq i, j \leq M$.
where $I_{i j}\left(\sigma^{k}\right)$ is the indicator function and defined as follows:
$I_{i j}\left(\sigma^{k}\right)= \begin{cases}1, & \text { if } \quad \sigma^{k}(i)=j ; \\ 0, & \text { otherwise }\end{cases}$
and $0 \leq \beta \leq 1$ is the learning rate, which controls the contribution of the present promising solutions to the probability matrix $\mathcal{P}(t)$ (or $\mathcal{Q}(t)$ ). The larger $\beta$ value indicates more contribution of the information learned from the history.

### 5.4. Sampling and replacement

An offspring $\pi$ is sampling from the probability matrix $\mathcal{P}(t)$ (or $\mathcal{Q}(t)$ ) at generation $t$ iteratively. Here we use the guided mutation operator [49] to sample new offspring. The guided mutation constructs a new offspring based on the probability matrix and the best solution found so far. Its underlying assumption is the socalled proximate optimality principle (POP), which is proposed by [12]. The POP states that good solutions have similar structure. It is widely adopted, implicitly or explicitly, in most, if not all, meta-heuristics. Previous study on the guided mutation [48,49] has shown its superiority over the other recombination operators.

The procedure to sample a permutation $\pi$ by guided mutation can be described as follows. Suppose that the best solution found so far is $\mathbf{x}$, and current probability matrix is $\mathcal{P}$. To sample a new offspring, first a set $I=\left(i_{1}, \ldots, i_{i}\right)$, where $s=|\alpha M\rangle$ is randomly selected, $\alpha$ is a parameter of the guided mutation and $\lceil x\rceil$ rounds the element of $x$ to the nearest integer towards infinity. The elements for the new offspring $\sigma$ in $I$ are copied from $\mathbf{x}$, that is, $\sigma_{i}=\mathbf{x}_{i}, i \in I$. The selection for elements in the rest unfilled components, i.e. $\{1,2, \ldots, M\} \backslash I$ is proportional to the probability matrix $\mathcal{P}$.

Specifically, the following procedure can be used to select an element for a location $k$ in $\{1,2, \ldots, M\} \backslash I$. To begin with, we denote

$U=I$ the already-assigned components, and $V=\left(\mathbf{x}_{i_{1}}, \ldots, \mathbf{x}_{i_{t}}\right)$ the already-used elements.

Step 1 Reset the $k$ th column of the probability matrix $\mathcal{P}(t)$ by setting $p_{i, k}(t), i \in V$ as zero, since these elements are forbidden to be $\sigma_{k}$ for constructing a feasible permutation.
Step 2 Sum the $k$ th column of the probability matrix $\mathcal{P}(t)$,

$$
\begin{aligned}
& h=\sum_{i=1}^{M} p_{i, k} \\
& \operatorname{set} \mathbf{h}_{k}(t)=\left(\frac{p_{i}(t)}{h}, \cdots, \frac{p_{i k}(t)}{h}\right)^{T}
\end{aligned}
$$

Step 3 Select an element, e.g. $v$, by using the roulette wheel method based on $\mathbf{h}_{k}(t)$, set $\sigma_{k}:=v$.
Step 4 Set $U=U \bigcup_{k} k$ and $V=V \backslash\{v\}$.
The iteration continues until all components in $\{1,2, \ldots, M\} \backslash I$ are filled, i.e. $U=\{1,2, \ldots, M\}$ or $V=\varnothing$. In our algorithm, we sample $N$ offsprings from the probability matrix $\mathcal{P}(t)$.

To sample a category solution $\mathbf{y}=\left(y_{1}, \ldots, y_{M}\right)$ by using the guided mutation based on the probability matrix $\mathcal{Q}(t)$ and the best solution found so far $\mathbf{x}$. The same as the above sampling of permutation, we select a set of indices $I$ in which the elements in those locations are copied to $\mathbf{y}$, that is $y_{i}=x_{i}, i \in I$. The rest of the components are filled according to $\mathrm{Q}(t)$. Specifically, to fill the $j$ th component, $j \in\{1,2, \ldots, M\} \backslash I$, the following procedure is given:

Step 1 Normalize the probability element $q_{i j}, 1 \leq i \leq u_{j}$, that is,

$$
q_{i j}=\frac{q_{i j}}{\sum_{k=1}^{u_{j}} q_{k j}}
$$

Step 2 Select an element, say $v$, by roulette wheel method based on the normalized $q_{i j}, 1 \leq i \leq u_{j}$. Set $y_{j}=v$.

The solution construction procedure terminates when all unfilled components are filled.

The replacement is performed after sampling. To perform replacement, the generated offspring are partially replaced with solutions in the current population. The best $N$ individuals are selected from the combined set of the current population and the sampled offspring. Note that in order to preserve the diversity of the population, duplicates are not allowed in the new population.

### 5.5. Structure of the EDA with guided mutation

The following Alg. EDAP (EDAC) summarizes the algorithmic framework of the proposed EDA with guided mutation for permutation-based solution representation, called EDAP, and category-based solution representation (EDAC).

## Algorithm EDAP $(E D A C)(N, \alpha, \beta)$

Input: population size $N$, the control parameter in the guided mutation operator $\alpha$ and the learning rate $\beta$.
Output: The best solution found $\mathbf{x}^{*}$.

1. while computational budget has not been exceeded,

Initialization. Set $t:=0$. Generate the initial population $S(0)$ for EDAP randomly, and for EDAC heuristically (cf. subsection 5.2). Evaluate the fitness of the population by the greedy heuristic. Set the initial probability matrix $\mathcal{P}(0)$ using Eq. 2 for EDAP and Eq. 3 for EDAC.
3. Selection. Select half the best solutions in $S(t)$.
4. Modeling. Construct $\mathcal{P}(t)$, the probability model, using Eq. (4) based on the selected solutions.
5. Sampling. Sample $N$ offspring $\left\{v^{1}, \cdots, v^{N}\right\}$ by guided mutation as described in Section 5.4. Evaluate the sampled offspring by the greedy heuristic.
6. Replacement. Choose the best $N$ solutions from $\left\{v^{1}, \cdots, v^{M}\right\} \cup$ $S(t)$ to form $S(t+1)$ without duplication. Set $t:=t+1$.
7. end while;
8. Return the best solution $\mathbf{x}^{*}$ found in $S(t)$.

In the paper, the above EDA with guided mutation terminates when the algorithms cannot find a better solution within 30 generations, or the execution time excesses over a given time limit.

### 5.6. Tuning the control parameters of the greedy heuristic

The proposed procedure for tuning these parameters works in the following with EDAP (EDAC) as input.

Step 1 Tuning $x$ for the working path routing procedure.
Step 1.1 Randomly generate a permutation $\delta$ as the input parameter for the protection path routing procedure.
Step 1.2 Use $\operatorname{EDAC}\left(N, \alpha_{1}, \beta_{1}\right)$ to tune the working path routing, where the cost of a working path routing vector $\mathbf{x}$ is set as $f(\mathbf{x}, \delta)$. Set $\mathbf{x}^{*}$ to be the found best working path routing vector.
Step 2 Tuning $\sigma$ for the protection path routing procedure.
Step 2.1 Use EDAP $\left(\alpha_{2}, \beta_{2}\right)$ to tune $\sigma$ where the cost of $\sigma$ is set as $f\left(\mathbf{x}^{*}, \sigma\right)$. Set $\sigma^{*}$ to be the best setting of $\sigma$ found.

Return the best solution found to the static RWAP under SRLGconstraints is the solution generated by GH with parameter setting $\left(\mathbf{x}^{*}, \sigma^{*}\right)$.

Table 1
The characteristics of test network instances.
## 6. Computational results

### 6.1. Test problems

The network topology used is similar to the network topology in [46]. Parameters of a certain network topology include the number of nodes $n=|V|$, the number of SRLGs $S=|G|$, the number of links $L=|E|$, the maximum number of wavelength $W$ and the number of demands to be routed $M=|R|$.

Two kinds of network topology $T_{1}$ and $T_{2}$ are tested in the paper. In $T_{1}$, links in a same SRLG have the same input or output node. In $T_{2}$, links in a SRLG are set randomly. Parameters of the used test network topologies are listed in Table 1. The first eight networks have the same parameter settings as used in [46]. In the following simulation, 9 networks from each network topology are taken as examples. The example instances are named with its topology name plus an index. For example, $T_{1}-01$ means the instance is sampled from topology $T_{1}$ with parameters from Network1.

Note that in a generated test networks, there maybe no two linkand SRLG-disjoint paths between some source-destination pairs. In order to avoid such cases, the source-destination pairs are selected from all of the source-destination pairs who have at least two linkand SRLG-disjoint paths. For fair comparison, firstly the heuristic algorithm proposed in [46] is performed on a certain test network, then $M$ source-destination pairs which can be routed are picked and used as the test network for the new proposed algorithms.

### 6.2. Comparison results

To test the performance of the proposed algorithm, three algorithms are employed including a random algorithm, the EDA-based approach proposed in [49] and the proposed algorithm. The resultant algorithms are called R/GH, BH/EA/G and EDA/GH, respectively.

R/GA searches the search space by running GH on randomly generated control parameters. In the proposed EDA/GH, we need to set the algorithmic parameters, including the population size, the sampling population size, the guided mutation parameter $\alpha$, and probability updating parameter $\beta$. In all the experiments, the population size is set to 100 , the size of selected solutions is 50 , and the size of the sampled solutions is 100 .

To decide the proper parameters for $\alpha$ and $\beta$, we used $T_{1}-01$ as an example instance. For each algorithmic parameter combination, i.e. $\left\{\alpha_{1}, \beta_{1}\right\}$ and $\left\{\alpha_{2}, \beta_{2}\right\}$, the proposed algorithm was carried out 10 times on $T_{1}-01$, where $\alpha_{1}, \alpha_{2}=0.0,0.1,0.2, \ldots, 0.9$ and $\beta_{1}, \beta_{2}=$ $0.0,0.1,0.2, \ldots, 0.9$. The combination of the algorithmic parameters with the best average fitness value is picked as the proper parameter for the proposed algorithm. As a result, the parameter settings for EDA/GH are $\alpha_{1}=0.2, \beta_{1}=0.2, \alpha_{2}=0.3, \beta_{2}=0.2$ though these settings may be not suitable for the other network instances.

To fairly compare the mentioned three algorithms, we carried out them 30 times with their proper parameter for each test network instance within the given time limit $T$. The parameter setting

The comparison of EDA/GH, BH/EA/G and R/GH on test network instances.

![img-3.jpeg](img-3.jpeg)

Fig. 4. The evolution procedures of the compared algorithms.
for $\mathrm{EDA} / \mathrm{GH}$ is copied from [49]. The time limit $T$ for the instances from Network1 to Network7 is 120 s , while for Network8 is 300 s , 1200 s for Network9-Network11, 3600 for Network12-14 and 7200 for Network15. Table 2 lists the comparison results among the three algorithms on the test network instances with topologies $7_{1}$ and $7_{2}$.

In Table 2, "worst", "best", "avg." and "std." columns list the average worst, best, average network costs, and the standard deviation over the 30 runs. In the table, the values in " $t$-test" column show the t -values between the results of EDA/GH and BH/EA/G $\left(t_{2}\right)$, EDA/GH and $\mathrm{R} / \mathrm{GH}\left(t_{1}\right)$ by using two-tailed $t$-test. The null hypothesis used here is that the average cost obtained by $\mathrm{BH} / \mathrm{EA} / \mathrm{G}$ is the same as that obtained by BH/EA/G. The values $t_{1}<2.6$ suggests that EDA/GH can find better network routing and wavelength assignment schemes than BH/EA/G. From the tables, we can see that in 26 out of 30 test problems, the solution quality found by the EDA/GH is significantly better than that of BH/EA/G. The $t$-test between EDA/GH and $\mathrm{R} / \mathrm{GH}$ indicates that the proposed algorithm performs better than the random algorithm on all the test problems in terms of solution quality.

In Fig. 4, on the $x$-axis is the number of greedy function calls, on the $y$-axis is the average cost of the best solutions found over 30 runs. From the figure, we can see that the average quality of the initial population in BH/GA/G is superior to that in EDA/GH. However, the proposed algorithm can find high quality solutions very quick. One possible explanation to this is that the search space of EDA/GH in stage 1 is not as rugged as that of BH/GA/G which is rooted from the different solution representations.

The average times (in seconds) to evaluate per 100 solutions by using EDA/GH and BH/EA/G are shown in columns 'time' of Table 2. From the table, one can see that the time used for constructing a solution by the proposed algorithm is at least 1.5 time less than the time used by BH/EA/G. Note that in the heuristic developed in [49], the Dijsktra algorithm has to be applied to route the working path for each connection request. Since it is obvious that the working paths routed for the connection requests can only fall into the candidate path set PathList, it is therefore a waste of time to route the connection request at each routing procedure. The experimental results shown in Table 2 also indicate that the solution quality found by the proposed algorithm compensates the overhead of constructing the shortest paths.

From the comparison, we can draw the following conclusions:

1. The usage of the population-based algorithm is beneficial to the search since the population-based algorithm (EDA/GH) clearly outperforms the random algorithm R/GH.
2. The selection of proper solution representation has significant influence to the performance of the population-based algorithm. Since the solution representation reflects the fitness landscape of the optimization problem, a good solution representation will
make the evolutionary search much easier than a bad solution representation.

## 7. Conclusion

In the paper, a two-stage EDA-based approach was proposed for the static routing and wavelength assignment problem (RWAP) for all optical WDM mesh network survivability under SRLG constraints. A greedy heuristic (GH) with two control parameters was proposed to construct a feasible solution of the considered problem. The estimation of distribution algorithm with guided mutation works on top of the heuristic to find optimal control parameter settings of the heuristic in respective two stages.

The proposed algorithm, called EDA/GH, was empirically compared with the best-known EA-based algorithm for the static RWAP under SRLG constraints, and a pure random algorithm based on the proposed greedy heuristic on a set of 30 test network instances within given time limit. The comparison results favor the proposed algorithm against the best-known EA-based algorithm in 26 out of 30 test network instances, and against the random algorithm in all the instances in terms of solution quality within a given time limit.

The comparison results also indicate that the search for optimal solutions benefits from the population approach. The experiments also show the solution representation has a significant effect to the performance of population-based approach.

## Acknowledgements

JS is funded by BBSRC/EPSRC grant BB/D019613/1, UK. The author also would like to thank anonymous reviewers for their constructive comments and suggestions.
