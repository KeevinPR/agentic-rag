# Power Aware Data Center Placement in WDM Optical Networks 

Sanwal Zeb*, Arsalan Ahmad ${ }^{\dagger}$, Ashfaq Ahmed ${ }^{\ddagger}$, Andrea Bianco ${ }^{\S}$<br>*1School of Electrical Engineering \& Computer Sciences (SEECS), NUST, Islamabad, Pakistan<br>${ }^{\ddagger}$ Dept. of Electrical Engineering \& Computer Science, Khalifa University, Abu Dhabi, UAE<br>${ }^{\S}$ Dept. of Electronics and Telecommunication, Politecnico di Torino, Torino, Italy<br>*14mseeszeb@seecs.edu.pk, ${ }^{\dagger}$ arsalan.ahmad@seecs.edu.pk, ${ }^{\ddagger}$ ashfaq.ahmed@ku.ac.ae, ${ }^{\S}$ andrea.bianco@polito.it


#### Abstract

Due to the increasing trend in IP traffic, the placement of Data Centers (DCs) at network nodes has become a hot research topic. A proper DCs placement translates in reduced power consumption of overall network. The paper scope is to find the best placement of " $\hat{v}$ " DCs nodes out of " $N$ " total nodes to reduce power consumption. To solve the problem, we propose two heuristics: EoDCP, based on Estimation of Distribution Algorithm (EDA), and MaxN-MinL. An exhaustive search based ESDCP algorithm is used as a lower bound to compare the performance of EoDCP and MaxN-MinL. Moreover, electronic traffic grooming technique is employed to further reduce the total network power consumption. A 20 -Node Random network and a $\mathbf{1 7}$ Node German network are used to perform comparison of proposed heuristics. Performance of EoDCP algorithm is far better than those of MaxN-MinL, and is similar to the optimal solution obtained via ESDCP. Finally, using electronic traffic grooming improves power savings up-to $15 \%$ in the two considered topologies.

Index Terms—Data Center placement, Estimation of Distribution Algorithm, Traffic Grooming.


## I. INTRODUCTION

The increase in network power consumption derived by the need to sustain bandwidth hungry applications has made network energy efficiency an important research topic for several years now. Today, many content and service providers provide services to users by relying on various Data Centers (DCs), installed either in their own private or on third party networks. DCs require hundreds of servers, cooling and energy resources as well as the support of networking infrastructures [1]. To facilitate services and multimedia applications, content delivery networks (CDNs) play a key role. The CDNs replicate data at various geographically distributed DCs. The content hosting through multiple geographical distributed DCs reduces network latency and congestion.

The most viable solution to connect DCs is through the optical transport network. At present, the core wavelength division multiplexing (WDM) network follows the International Telecommunication Union (ITU) frequencies for the allotment of wavelengths, exploiting a fixed range of frequency distribution over the entire C-band of 4 THz , where each channel is of 50 GHz bandwidth.

The power consumption of Information and Communication Technology (ICT) devices have become a major power usage stakeholder. The current forecasting trends show that the internet will consume $50 \%$ of the total world power in the next decade [2]. The Internet high power consumption is mainly due to network devices such as IP routers, transponders, amplifiers, optical cross connects
(OXCs) and to servers and storage devices. The energy usage grew from 1.7 KW to 50 KW [3], also because router capabilities increassed from 100 Gbps to 10 Tbps.

Data Centers (DCs) are a centralized infrastructure, running Information Technology (IT) equipments, typically deployed on network nodes in an IP over WDM topology. The presence of DCs on a particular node creates a hot spot scenario due to the huge amount of traffic going through this node. This can significantly increase IP over WDM power conspumption, as the number of ports and slots of different modules vary with the amount of traffic. In cloud networks, traffic is categorized into two types: DC-to-user traffic and DC-to-DC traffic. In DC-to-user traffic, the flow of traffic is from DCs to the end users. This traffic accounts for $2 / 3$ of the total cloud traffic [4]. The flow of traffic between two DCs (Inter DC), such as virtual machine migration and content distribution, accounts to roughly $1 / 3$ of total cloud traffic. Both types of traffic are considered in our DCs placement schemes, in comparison to earlier work that only focused on DC-to-user traffic [5].

## A. Related Work

This section covers the recent contributions on the DC placement in IP over WDM networks. Because the placement has a direct impact on the power consumption, it plays a vital role in optimizing the power consumption. In inter DCs, major contributors in terms of power consumption are network communication devices such as routers, transponders, OXCs, optical multiplexers and Erbium Doped Fiber Amplifier (EDFA). With advancement in technology, applications are hosted to serve particular regions. Thus, there is a continuous migration of applications and data from one DC to another DC. Therefore, the communication between DC to edge nodes and DC-to-DC has increased. However, the DCs are constrained to geographical locations, thus, become a main concern of global warming due to its high power consumption [6].

Green Routing is another energy minimization routing scheme implemented by considering several approaches such as line card, chassis configuration, the proximity of the equipment to the renewable energy resources and traffic grooming on high capacity links [7] [8]. [9] targeted the green areas, i.e. renewable energy resources such as solar, wind, tidal etc. The author proposed that the network energy can be minimized by placing the high-performance servers, core routers and DCs in a proximity to Green Areas and route the traffic towards these areas in order to

reduce the network power as well as carbon footprint and global warming.

The DC placement problem in IP over WDM network has been studied considering different aspects, such as disaster tolerance [10], energy efficient DCs placement on the basis of proximity to renewable sources [11], network cost minimization [12], efficient bandwidth utilization [13]. Limited contributions exist on energy aware DCs placement problem in IP over WDM. In [14] [15], the authors provide linear programming (LP) for optimized DCs placement in an IP over WDM network to minimize the non-renewable power consumption. This work proposes a heuristic approach for optimizing DCs placement in an IP over WDM network considering both Inter-DC and IntraDC traffic.

## B. Our Approach and Contributions

In this paper, we rely on a type of evolutionary optimization algorithms to map DC placement problem in IP over WDM networks. The followings are the main paper contributions:

- We formulate a power model for IP over WDM networks incorporating DCs.
- We proposed Estimation of Data Center Placement Algorithm EoDCP, based on Estimation of Distribution Algorithm (EDA), to optimize DC location in a given network.
- A greedy Maximum Node Degree with Minimum Average Optical Reach MaxN-MinL heuristic is also proposed to efficiently place DCs in IP over WDM network scenario.
- An Exhaustive Search ESDCP algorithm is used as a performance lower bound.
- Furthermore, two techniques for finding the best set of lightpath are studied: 1) exploiting electronic traffic grooming, and 2) setting up direct lightpath for each traffic demand.

The remaining part of this paper is organized as follows. Section II describes our system and power models. DC placement algorithms ESDCP, EoDCP and MaxN-MinL are explained in Section III. The performance evaluation is shown in Section IV. We conclude the paper in Section V.

## II. SYSTEM MODEL

We consider an IP over WDM optical network, as shown in Fig. 1. The network physical topology is represented by a directed graph, where edges are the physical links that connect the network nodes. Every node in the network is equipped with an OXC. In addition, each node is capable of serving as a DC candidate location [14]. In this network, each source node s to destination node d is separated through a physical link having a length $L_{s d}$ in km . All physical links are assumed to be symmetrical such that $L_{s d}=L_{d s}$.
![img-0.jpeg](img-0.jpeg)

Fig. 1: IP over WDM Network
A three tier DC architecture is used which consists of core, aggregation and access layer [16]. The Core layer delivers high-speed switching, aggregation layer provides functionality such as service module integration, servers load balancing and firewall protecting whereas, the access layer is directly connected to the various types of servers providing services such as content storage and utility computing.

The traffic from each source node to the destination is transmitted using lightpaths, an end-to-end optical channel that starts at the source and terminates at the destination while traversing through multiple physical links. Each lightpath is created using a transponder that can operate at different available modulation levels $m_{i}$ as described in [17].

## A. Power Model

Each node in the network is equipped with an IP router and an OXC. We assume that the IP router is a Cisco CRS-3 series router which comprises of Line Card Shelf (LCS), Line Cards (LCs) and Fabric Card Shelf (FCS). CRS-3 LCS has 16 slots and each slot holds a single LC. The LCs are responsible for the traffic flow between the nodes of the backbone network. In the context of the optical network, each line card can generate and terminate a lightpath and send data directly to optical layer. Multiple LCS can be joined in a multiple chassis configurations to help in load balancing [18]. The power of IP layer is equal to the total power consumption of all IP routers modules as evaluated in 1 . To model the power consumption of the IP layer, the power usage of individual router module is calculated instead of evaluating the power usage from a generic Watt/Gbps expression.

$$
\mathbf{P}_{I P}=\mathbf{P}_{L C S}+\mathbf{P}_{L C s}+\mathbf{P}_{F C S}
$$

In the optical layer, we consider two main power elements: Optical Cross Connects (OXCs) and Optical Line Amplifiers (OLAs). The number of OLAs varies according to length of physical link. We represent the power consumption of OXCs and OLAs by $P_{O X C}$ and $P_{O L A}$ respectively. The total power consumption for any lightpath would thus be the combined power consumption of all IP routers and the power consumption in the optical domain that can be modeled in 2.

$$
\mathbf{P}_{T O T A L}=\sum_{i=1}^{N}\left(\mathbf{P}_{O L A}+\mathbf{P}_{O X C}\right)_{i}+\sum_{j=1}^{M}\left(\mathbf{P}_{I P}\right)_{j}
$$

where $N$ represents the total number of Routers/OXC involved in the lightpath and $M$ denotes the total number of OLAs installed to support lightpath provisioning. We follow the power dissipation statistics of IP routers, OXCs and OLAs derived from [19], [20], [21].

## III. Data Center Placement Schemes

In this section, we describe three different schemes for the DC placement problem in IP over WDM network scenario. The objective of each schemes is to minimize the power consumption to support distributed DCs.

## A. Exhaustive Search DC Placement (ESDCP)

The ESDCP algorithm analyze every possible combination for DC placements, calculates the corresponding IP over WDM power, and selects the combination that minimizes the power consumption. ESDCP gives the optimal power value as it considers each and every combination of DC placement inside the network. Clearly, as the network size increases, the computational time of ESDCP increases exponentially, making this algorithm useless in a realistic context. Therefore, a meta-heuristic named ( $E o D C P$ ), and a greedy heuristic named $(\operatorname{Max} N-\operatorname{Min} L)$ are further proposed.

## B. Estimation of Data center Placement (EoDCP) Algorithm

The EoDCP algorithm is based on the EDA (Estimation of Distribution Algorithm) approach, a recently added optimization technique in the family of evolutionary algorithms (EAs). EoDCP works on iterative probabilistic approach to find an optimal solution of a function where it explores the most promising candidates of an evolving population [22] [23]. For this reason, a new population is generated in each iteration, where the promising candidate offsprings have a higher chance to be an optimal solution. A population with strong fitness value, defined as the total network power in our case, is selected in each generation, so as to reproduces a healthier child population. Keeping in view the above discussion, EoDCP executes the following steps to find an optimal solution [24] and EoDCP flow diagram is shown in Figure 2

1) Generate initial population on the basis of uniform distribution. As the DC placement problem is a binary problem, the population will also be binary where each ' 1 ' will represent the placement of a DC at a particular node and every ' 0 ' represent a non DC node.
2) Evaluate the current population on the basis of fitness function. For said problem, the fitness function is the total network power, as shown in Fig. 4.
3) If the best individual (the one with minimum power in DC placement problem) satisfy the stopping criteria, then abort the simulation. Otherwise, make a stopping criteria i.e. no. of generation. In this case, simulation run for fix number of generations.
![img-1.jpeg](img-1.jpeg)

Fig. 2: Flow Diagram Estimation of Data center Placement (EoDCP) Algorithm
4) Select the best individuals from the current population on the basis of fitness function which is minimization function in DC placement scenario. Selection of best individuals will done on the basis of selection probability which is an input to function. In our case, selection probability is set to 0.5 i.e. $50 \%$ individuals with best fitness are selected form current population.
5) From the set of best selected individuals of current population, estimate the feature probability i.e. probability of ' 1 ' or ' 0 ' in each column.
6) Apply thresholding if the fitness value does not converge for $N$ number of generations. It is applied by cutting the probability of feature(columnn) $k$ to 0.75 if it is greater than 0.85 and similarly increase the probability of feature $k$ to 0.25 if it is below 0.15 . Thresholding is an important step to avoid premature convergence.
7) Generate a new population or child on the basis of the feature probability obtained from the best individuals of the current population. Calculate the fitness of new population and replace the best candidate solutions of current population with the best candidate solutions of newly generated population.

## C. Maximum Node Degree with Minimum Average Optical Length (MaxN-MinL) Heuristic for DC Placement

The MaxN-MinL heuristic is proposed to place DCs in an IP over WDM network with least complexity. This heuristic is based on a critical node selection. For example a DC node should be the most critical node of the network i.e. a DC node should have the highest node degree in the network, which makes it the most connected node of the network. Secondly, we calculate the Minimum average optical length of a node to all other nodes in the network.

The reason we are accounting the minimum average length is because to place a DC at a specific node, its average optical distance to all other nodes should be minimized. By incorporating the above mentioned parameters, the node where DC is to be placed is the most connected node in the network, to obtain a sub-optimal solution.

The MaxN-MinL heuristic places DC on the node having maximum node degree and having minimum average optical length. First, node degree is calculated by adding the number of links associated with a particular node. Then, the average optical length $L_{a v g_{i}}$ of node $i$ is calculated using the equation 3 .

$$
L_{a v g_{i}}=\frac{\sum_{j=1}^{N}\left(L_{i, j+k}\right)}{N-1}\left\{\begin{array}{cc}
k=1 ; & j \neq 1 \\
0 ; & \text { otherwise }
\end{array}\right.
$$

where $N$ is the total number of nodes and $L_{i j}$ is the length of the optical path from $i$ to $j$, computed for all other network nodes $j$. After placing DCs on particular nodes, lightpaths are generated according to the traffic demands of DC-to-node and DC-to-DC traffic. Finally, the power of the IP over WDM solution is calculated. The pseudo-code of MaxN-MinL heuristic is shown in Algorithm 1.

```
Algorithm 1: Max \(N\) - Min \(L\) Heuristic for DC
Placement
    1 Initialization: Start from a Physical Topology Graph with
        \(N\) number of nodes;
    2 Array: Node_Degree \(\leftarrow\) Degree of all nodes;
    3 MAX NUM DC \(\leftarrow\) Maximum number of DCs to be
        placed;
    \(N \leftarrow\) Total Number of Nodes;
    8 Sort :(Node Degree, Descending);
    \(6 \operatorname{temp} \leftarrow\) Node Degree(1);
    \(j \leftarrow 1\);
    foreach \(i=1\) to \(N\) do
        if temp \(=\) Node Degree(i) then
            temp \(\leftarrow\) Node Degree(i);
            foreach \(k \leftarrow j\) to \(M\) do
                Array avg optical length \((k) \leftarrow\) avg optical
                length of \(k t h\) node;
            end
            Sort :(Node Degree( \(j\) to \(M\) ),Ascending order to
                Avg Optical length);
            end
            else
            \(M \leftarrow i-1\);
        end
    end
    build topology();
    create DC(Node Degree(1 to MAX NUM DC));
    Calculate Optical Length();
    find Modulation level();
    24 Lightpath Establishment();
    Calculate Total Network Power(2);
```


## IV. PERFORMANCE EVALUATION

In this section, we present the performance evaluation results of the proposed heuristics. A detailed power model for IP-layer and optical-layer is implemented in the simulator. Additionally, the simulator supports the 3-Tier DC architecture to compute the power consumption within each DC. We study two different network scenarios in our simulations. The first network topology is a 20-node

Random Network, the second one is a 17-node German network topology, depicted in Fig. 3 (a and b) respectively.

For both Random and German network scenario, we consider an aggregated traffic of 10 TB between datacenters-to-users and 5 TB of intra datacenter traffic. The traffic is uniformly distributed among nodes and datacenters. In case of random network, we consider a DC placement set i.e. $k=\{3,4,5,6\}$. For each value of $k$ in a set, results are generated. For same traffic demand between node-to-node and DC-to-DC, we obtained the results by varying the number of DCs $k$. Fig. 4 shows the power consumption stats by varying the number of DCs $k$ for both Random and German network respectively. Here the traffic considered is between DCs-to-Nodes. On the x -axis, the graph represents number of DCs $k$ to be placed in a network, while the total power consumption of IP over WDM network is plotted on the y-axis. Trend in graph shows that for each DC placement scheme, power consumption of the network decreases with the increasing value of DCs $k$. This power reduction with the increasing value of $k$ is due to the reason that with more number of data centers in a given network, optical reach between a node and a DC or intra DC decreases. Similarly this reduction in optical reach permits the frequent use of higher rate modulation levels which leads to the reduction of number of router ports and LCs which ultimately decreases total IP over WDM network power.

Moreover, Fig. 4 shows another important trend in minimizing the power consumption of IP over WDM network: Placing a DCs on a most appropriate nodes in the network permit to decrease the power. It can be clearly seen in Fig. 4 that (ESDCP) finds the most optimal location for DC placement providing the best power minimization. The drawback of using (ESDCP) scheme is the computation complexity and very large simulation time. To overcome this issue, we proposed a MaxN-MinL heuristic for DC placement. MaxN-MinL heuristic performs in reasonable shorter time then (ESDCP) but it does not gives the ultimate DC placement locations to minimize power as compared to (ESDCP). While an optimization approach (EoDCP) outperforms both (ESDCP) and MaxN-MinL heuristic. (EoDCP) performs very close or almost equal to (ESDCP) with its low computational complexity and execution time.

Fig. 5 shows the power consumption using traffic grooming and no grooming scenarios. To test our results, we have considered node-to-node traffic and choose low (1000 Gbps), medium (5000 Gbps) and high (10000 Gpbs) traffic per node as shown on X-axis. Secondly we choose (EoDCP) for both traffic grooming and no grooming technique as we expect that trends are same for other techniques also. As the traffic increases, the power consumption of network also increases but the significance of this result is that power consumption using grooming technique decreases as compared to no grooming technique at given traffic demand. Traffic grooming technique generates small number of lightpaths resulting in lesser utilization of router ports and LCs. This further results in the decrease of network total power consumption.

Fig. 6 shows the power saving [\%] using traffic grooming approach for Random and German network respec-

![img-4.jpeg](img-4.jpeg)

Fig. 3: The (a) 20 Node Random (b) 17 Node German Topology
![img-3.jpeg](img-3.jpeg)

Fig. 4: The (a) Random and (b) German Network DC Placement Analysis
![img-4.jpeg](img-4.jpeg)

Fig. 5: The (a) Random and (b) German Network Power Consumption Analysis (Grooming vs No Grooming)

![img-5.jpeg](img-5.jpeg)

Fig. 6: Power Saving \% using Traffic Grooming
tively. Trends in Fig. 6 show that as the node-to-node traffic increases, there is a significant increase in the power saving. For example, for the 20 -nodes Random network and the 17-node German network with high traffic demand of 10000 Gbps per node, there is roughly a $13 \%$ and $16 \%$ power saving using traffic grooming technique.

## V. CONCLUSION

This work shows that the data traffic can be managed to minimize power consumption with the placement of DCs on suitable nodes or locations. The ESDCP algorithm provides an optimal lower bound in small size topologies. However, it becomes un-tractable for realistic network sizes. Hence, an iterative probabilistic optimization approach EoDCP is proposed to reduce complexity and computational time. Furthermore, the results of Max N-Min L heuristic for German network and $k=\{3,4,5,6\}$ shows that placing DCs in accordance with maximum node degree and minimum average length wastes $15 \%, 17 \%, 19 \%$ and $21 \%$ respectively more power in comparison with ESDCP and EoDCP. Similar trend hold for the Random network too. Thus, a very fast and simple heuristic provides performance very close to those of more complex and time consuming solutions. Finally, electronic traffic grooming is shown to further reduce power consumption.

## REFERENCES

[1] I. Goiri, K. Le, J. Guitart, J. Torres, and R. Bianchini, "Intelligent placement of datacenters for internet services," in Distributed Computing Systems (ICDCS), 2011 31st International Conference on. IEEE, 2011, pp. 131-142.
[2] B. GeSI, "2020: Enabling the low carbon economy in the information age,[london, uk, 2008."
[3] M. Yamada, T. Yazaki, N. Matsuyama, and T. Hayashi, "Power efficient approach and performance control for routers," in Communications Workshops, 2009. ICC Workshops 2009. IEEE International Conference on. IEEE, 2009, pp. 1-5.
[4] C. V. Networking, "Cisco global cloud index: Forecast and methodology, 2014-2019," White Paper), Cisco, 2013.
[5] M. Klinkowski, K. Walkowiak, and R. Goścień, "Optimization algorithms for data center location problem in elastic optical networks," in Transparent Optical Networks (ICTON), 2013 15th International Conference on. IEEE, 2013, pp. 1-5.
[6] Y. Zhang, P. Chowdhury, M. Tornatore, and B. Mukherjee, "Energy efficiency in telecom optical networks," IEEE Communications Surveys \& Tutorials, vol. 12, no. 4, pp. 441-458, 2010.
[7] A. Ahmad, A. Bianco, and E. Bonetto, "Traffic grooming and energy-efficiency in flexible-grid networks," in Communications (ICC), 2014 IEEE International Conference on. IEEE, 2014, pp. $3264-3269$.
[8] K. Dev, R. Nebuloni, C. Capsoni, O. Fiser, and V. Brazda, "Estimation of optical attenuation in reduced visibility conditions in different environments across free space optics link," IET Microwaves, Antennas \& Propagation, vol. 11, no. 12, pp. 1708-1713, 2017.
[9] B. Heller, "Saving energy in data center networks," NSDI'10, Apr, 2010.
[10] J. Xiao, B. Wu, X. Jiang, P.-H. Ho, and S. Fu, "Data center network placement and service protection in all-optical mesh networks," in Design of Reliable Communication Networks (DRCN), 2013 9th International Conference on the. IEEE, 2013, pp. 88-94.
[11] S. Ferdousi, F. Dikbiyik, M. F. Habib, M. Tornatore, and B. Mukherjee, "Disaster-aware datacenter placement and dynamic content management in cloud networks," IEEE/OSA Journal of Optical Communications and Networking, vol. 7, no. 7, pp. 681694, 2015.
[12] Y. Wu, M. Tornatore, S. Ferdousi, and B. Mukherjee, "Green data center placement in optical cloud networks," IEEE Transactions on Green Communications and Networking, vol. 1, no. 3, pp. 347-357, 2017.
[13] K. Guan, "Evaluating the impact of data center locations and distance-adaptive transmission on the wavelength resources for serving cloud traffic," in Optical Fiber Communication Conference. Optical Society of America, 2017, pp. W3D-3.
[14] X. Dong, T. El-Gorashi, and J. M. Elmirghani, "Green ip over wdm networks with data centers," Journal of Lightwave Technology, vol. 29, no. 12, pp. 1861-1880, 2011.
[15] I. Khan, A. Ahmad, M. U. Masood, A. W. Malik, N. Ahmed, and V. Curri, "Impact of data center placement on the power consumption of flexible-grid optical networks," Optical Engineering, vol. 59, no. 1, p. 016115, 2020.
[16] D. Khazovich, P. Boavry, and S. U. Khan, "Greencloud: a packetlevel simulator of energy-aware cloud computing data centers," The Journal of Supercomputing, vol. 62, no. 3, pp. 1263-1283, 2012.
[17] A. Ahmad, A. Bianco, H. Chouman, G. Marchetto, S. Tahir, and V. Curri, "Exploiting the transmission layer in logical topology design of flexible-grid optical networks," in Communications (ICC), 2016 IEEE International Conference on. IEEE, 2016, pp. 1-6.
[18] A. Ahmad, A. Bianco, H. Chouman, D. DeTommas, G. Marchetto, S. Tahir, and V. Curri, "Merit of hybrid edfa/raman amplification in fixed-grid all-optical network exploiting multirate transponders," International Journal of Communication Systems, vol. 31, no. 1, p. e3383, 2018.
[19] A. Ahmad, A. Bianco, E. Bonetto, L. Chiaraviglio, and F. Idzikowski, "Energy-aware design of multilayer core networks," Journal of Optical Communications and Networking, vol. 5, no. 10, pp. A127-A143, 2013.
[20] W. Van Heddeghem, F. Idzikowski, W. Vereecken, D. Colle, M. Pickavet, and P. Demeester, "Power consumption modeling in optical multilayer networks," Photonic Network Communications, vol. 24, no. 2, pp. 86-102, 2012.
[21] J. L. Vizcaíno, Y. Ye, and I. T. Monroy, "Energy efficiency analysis for flexible-grid ofdm-based optical networks," Computer Networks, vol. 56, no. 10, pp. 2400-2419, 2012.
[22] M. Hauschild and M. Pelikan, "An introduction and survey of estimation of distribution algorithms," Swarm and evolutionary computation, vol. 1, no. 3, pp. 111-128, 2011.
[23] D. Simon, Evolutionary optimization algorithms. John Wiley \& Sons, 2013.
[24] A. Ahmed, Q. Khan, M. Naeem, M. Iqbal, A. Anpalagan, and M. Awais, "An insight to the performance of estimation of distribution algorithm for multiple line outage identification," Swarm and Evolutionary Computation, 2017.