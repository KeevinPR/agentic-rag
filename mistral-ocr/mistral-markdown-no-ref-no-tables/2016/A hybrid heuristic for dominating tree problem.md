# A hybrid heuristic for dominating tree problem 

Sachchida Nand Chaurasia $\cdot$ Alok Singh

(DTP) is concerned with finding a tree $D T$ of minimum total edge weight on $G$ in such a way that each node $v \in V$ either belongs to $D T$ or is adjacent to a node belonging to $D T$. Nodes in $D T$ are said to be dominating nodes, whereas nodes which do not belong to $D T$ are said to be non-dominating nodes. DTP is $\mathcal{N} \mathscr{P}$-hard in general (Shin et al. 2010; Zhang et al. 2008). However in some special cases DTP can be solved in polynomial time, e.g. cases where the underlying graph is complete or is a tree. In case of a complete graph, each node is a minimum dominating tree in itself with cost 0 . In case the underlying graph $G$ is a tree, the minimum dominating tree is the subgraph (subtree) of $G$ induced by non-leaf nodes.

The DTP, a relatively new problem, finds applications in the area of wireless sensor networks (WSNs). One such application of the DTP is to provide a virtual backbone for routing (Wu and Hailan 1999). In this scheme, routing information are stored only on the dominating nodes after computing a $D T$. Since non-dominating nodes are one hop away from nodes of the $D T$, in order to forward a message from one node (sender) to another node (receiver), the message can always be first forwarded to the nearest dominating node of the sender, then routed to the nearest dominating node of the receiver with the help of the $D T$, and finally forwarded to the receiver. Non-dominating nodes only need to know the nearest dominating node. The advantage of this scheme is that the number of dominating nodes is small in comparison to the total nodes (Wu and Hailan 1999), thereby significantly reducing the size of the routing tables. Such a scheme is more resilient to faults also as these tables need to be recalculated only when topological changes in the network affect one of the dominating nodes.

In the literature, the connected dominating set concept has been widely used for constructing a routing backbone in WSNs with minimum energy consumption (Thai et al.

Fig. 1 Illustration of a disk graph and a dominating tree. a Edges in a disk graph. b A WSN with 15 nodes. c Disk graph corresponding to WSN of b. d A dominating tree on disk graph of $\mathbf{c}$
![img-0.jpeg](img-0.jpeg)
(a)
![img-1.jpeg](img-1.jpeg)
(c)
![img-2.jpeg](img-2.jpeg)
(b)
![img-3.jpeg](img-3.jpeg)
(d)

2007; Wan et al. 2002; Guha and Khuller 1998; Park et al. 2007; Thaiand et al. 2008). However, these approaches focus on the nodes instead of the edges in order to minimize the energy consumption. Actually, the energy consumption at each edge directly affects the energy consumption of routing. Therefore, one has to consider the energy consumption by each edge to minimize the energy consumption of routing. With this intention, the DTP was formulated (Shin et al. 2010; Zhang et al. 2008). There exists another related problem called the tree cover problem that has been studied in the literature (Arkin et al. 1993; Fujito 2001, 2006), but this problem is different from the DTP. A tree in the tree cover problem is defined as an edge dominating set, whereas a tree in the DTP is defined as a node dominating set.

Actually, communication in wireless sensor networks can be modelled using disk graphs where each disk around a sensor node represents the transmission range of that node. There exists an edge between a pair of nodes if these two nodes lie in the intersection area of their respective disks. In other words, an edge exists between a pair of nodes only when these two nodes are within the transmission range of each other. Obviously, only those nodes which are connected by an edge can communicate directly with each other. Figure

1a explains this concept where three nodes $\mathrm{A}, \mathrm{B}$ and C are placed randomly in a $50 \times 50 \mathrm{~m}$ area. The transmission range of each node is assumed to be $10 \mathrm{~m} . \mathrm{A}_{\mathrm{D}}, \mathrm{B}_{\mathrm{D}}$ and $\mathrm{C}_{\mathrm{D}}$ are the disks associated with nodes $\mathrm{A}, \mathrm{B}$ and C , respectively. In this figure, for the sake of clarity, each node and its associated disk is represented with the same colour which is different from the colours assigned to other nodes and their associated disks. Nodes A and B lie in the intersection area of disks $\mathrm{A}_{\mathrm{D}}$ and $B_{D}$. Similarly, nodes $B$ and $C$ lie in the intersection area of disks $B_{D}$ and $C_{D}$. Hence, an edge exist between $A$ and $B$ and another edge exists between $B$ and $C$. On the other hand, nodes A and C do not lie in the intersection area of their respective disks, viz. $\mathrm{A}_{\mathrm{D}}$ and $\mathrm{C}_{\mathrm{D}}$, and hence there exists no edge between A and C. From this figure, it can also be observed that if the radius of the disks increases, the number of edges can increase.

Figure 1b shows a wireless sensor network consisting of 15 nodes, each with a transmission range of 20 m , placed randomly in a $50 \times 50 \mathrm{~m}$ area. The disks associated with each nodes are also shown. This figure uses the same colouring scheme as used in Fig. 1a. The corresponding disk graph is shown in the Fig. 1c. A possible dominating tree on this disk graph is shown in Fig. 1d with thick red colour edges.

Shin et al. (2010) and Zhang et al. (2008) both proved the $\mathscr{N} \mathscr{P}$-hardness of the DTP, provided the inapproximability results and introduced an approximation framework for solving the DTP. Since approximation algorithm is quasipolynomial $\left(|V|^{O(|g| V|)}\right.$ ), each of them developed a polynomial time heuristic for the DTP. Later, Sundar and Singh (2013) proposed one more heuristic and two metaheuristic techniques, viz. artificial bee colony (ABC) algorithm and ant colony optimization (ACO) algorithm for the DTP. To the best of our knowledge, only these two metaheuristic approaches have been proposed in the literature for the DTP. The heuristic of Sundar and Singh (2013) outperformed the heuristics proposed by Shin et al. (2010) and Zhang et al. (2008).

In this paper, we present a heuristic and an evolutionary algorithm with guided mutation (EA/G) for the DTP. Our heuristic is derived from the heuristic proposed by Sundar and Singh (2013). EA/G is a relatively new evolutionary technique that employs a guided mutation operator to create offsprings (solutions). EA/G was developed by Zhang et al. (2005). The guided mutation operator makes use of global statistical information about the search space and location information of the solutions found so far to generate the offsprings. We have compared our approaches with the previously proposed approaches. Computational results show the effectiveness of our approaches.

The organization of the remaining part of the paper is as follows: Sect. 2 presents the formal problem formulation and introduces the notational conventions used in this paper. Section 3 describes the modifications proposed in the heuristic of Sundar and Singh (2013). Overview of EA/G is provided in Sect. 4, whereas Section 5 describes our EA/G approach for the dominating tree problem. Computational results are presented in Sect. 6. Finally, Sect. 7 presents some concluding remarks and directions for future research.

## 2 Problem formulation

Let $G=(V, E)$ be an undirected connected graph, where $V$ is the set of vertices or nodes and $E$ is the set of edges. Two nodes $u$ and $v$ are called neighbors of each other or adjacent to each other, iff, there exists an edge between them, i.e., $(u, v) \in E$. Similarly, two edges $e_{i, j}$ and $e_{k, l}$ are called neighbors of each other or adjacent to each other, iff, they have a node in common. Given a non-negative weight function $w: E \rightarrow \mathfrak{R}^{+}$associated with the edges of $G$, the dominating tree problem (DTP) seeks on $G$ a tree $D T$ such that for each node $v \in V, v$ is either in $D T$ or adjacent to a node in $D T$ and has minimum total edge weight among all such trees, i.e., $\sum_{e_{i, j} \in D T} w\left(e_{i, j}\right)$ is minimum. Nodes in $D T$ are called dominating nodes, whereas nodes not in $D T$ are called non-dominating or dominatee nodes. In this paper, we will

Table 1 Notational convention
also call any edge belonging to $D T$ dominating edge, and, any edge not in $D T$ non-dominating or dominatee edge.

Throughout this paper, while constructing a dominating tree, we will follow the convention that a node which is neither in the tree nor adjacent to a node in the tree is assumed to have colour WHITE, a node which does not belong to the tree, but is adjacent to a node in the tree is assumed to have colour GREY, and a node belonging to the tree is assumed to have colour BLACK. Initially, all nodes are assumed to have colour WHITE. When construction of dominating tree is complete then nodes belonging to the tree will have BLACK colour and all other (non-dominating) nodes will have GREY colour.

Important notational conventions used throughout this paper are given in the Table 1. Additional notational conventions will be introduced wherever those will be used.

## 3 Heuristic

This section describes our heuristic, which is an improved version of the heuristic H_DT proposed in Sundar and Singh (2013). We will refer to our heuristic as M_DT hereafter. Similar to the H_DT, the M_DT consists of two phases. The first phase is the initialization phase in which the shortest path between all pairs of nodes in graph $G$ are computed. The second phase consists of an iterative procedure to construct a dominating tree. At the beginning of the second phase of the M_DT, all nodes are assumed to have colour WHITE, and, we start with an empty tree $D T$. During each iteration, an edge $e_{i, j}$ is selected using the following expression:
$e_{i, j} \leftarrow \underset{e_{u, v} \in E}{\arg \max } \frac{W\left(e_{u, v}\right) \times n c\left(e_{u, v}\right)}{w\left(e_{u, v}\right)}$
where $W\left(e_{u, v}\right)$ is $\left(\sum_{x \in O N(u)} w\left(e_{u, x}\right) \times c(u, x)+\sum_{y \in O N(v)}\right.$ $\left.w\left(e_{v, y}\right) \times c(v, y)-w\left(e_{u, v}\right) \times c(u, v)\right)$, i.e., $W\left(e_{u, v}\right)$ is the sum of the weights of all those edges which can potentially be

avoided in $D T$ in case the edge $e_{u, v}$ is selected and $n c\left(e_{u, v}\right)$ is $|w d(u) \cup w d(v)|$, i.e., $n c\left(e_{u, v}\right)$ gives the number of white nodes in the closed neighborhood of nodes $u$ and $v$. Therefore, Expression 1 selects an edge considering not only its own characteristics but also the characteristics of its adjacent edges. The characteristics that are considered are the weight of an edge and the colour of its end points. Further processing in the iteration depends on the colour of the nodes $i$ and $j$. Depending on the colour of the nodes $i$ and $j$, following cases can occur:

Case A : If both the nodes $i$ and $j$ are WHITE. A shortest path $S P$ between nodes $\{i, j\}$ and the partially constructed dominating tree $D T$ is searched in $G$. If two or more than two shortest paths exist then the tie is broken by selecting a path which has the maximum number of WHITE nodes. If a tie occurs in case of the number of WHITE nodes on the paths as well, then arbitrarily one such path is selected. All edges belonging to $S P$ are added to $D T$ and all nodes belonging to $S P$ are recoloured BLACK (if not already) and all WHITE neighbors of such nodes are recoloured GREY. The edge $e_{i, j}$ will be added to $D T$ only if one of the nodes among $i$ and $j$ which does not lie on the shortest path $S P$ has at least one WHITE neighbor. Otherwise, there is no point in adding the edge $e_{i, j}$ as both its endpoint nodes are non WHITE after adding the nodes of $S P$ to $D T$. If the edge $e_{i, j}$ got added to $D T$ then nodes $i$ and $j$ are recoloured BLACK (if not already) and all their WHITE neighbors are recoloured GREY.
Case B : If one node is WHITE and the other is GREY. Check which one is WHITE node. Suppose node $j$ is WHITE. Now, find a shortest path $S P$ between partially constructed dominating tree $D T$ and node $j$ (ties are broken in the same manner as previous case). Let $k$ be the node which lies one hop away from node $j$ on $S P$. All edges belonging to $S P$ except $e_{k, j}$ are added to $D T$ and all nodes belonging to $S P$ except $j$ are recoloured BLACK (if not already) and all WHITE neighbors of such nodes are recoloured GREY. Now check whether node $j$ has any WHITE neighboring nodes, if yes, then add the edge $e_{k, j}$ into $D T$ and recolour node $j$ BLACK and also recolour GREY, all the WHITE neighboring nodes of node $j$.
Case C : If both the nodes $i$ and $j$ are GREY.
C1: If both the nodes have WHITE neighboring nodes. Find, which one among $i$ and $j$ has shortest path $S P$ from $D T$ (ties are broken arbitrarily). Suppose $S P$ connects $i$ to $D T$. Add all the edges on the shortest
path $S P$ into $D T$ and recolour all the nodes lying on $S P$ BLACK and all the WHITE neighboring nodes of such nodes GREY. Again recheck that node $j$ still has WHITE neighboring nodes, if yes, then proceed as in case C2.
C2 : If only one has WHITE neighboring nodes. Suppose node $j$ has WHITE neighboring nodes. Now, find the shortest path $S P$ between partially constructed dominating tree $D T$ and node $j$. Add all the edges on the shortest path $S P$ into $D T$ and recolour all the nodes lying on $S P$ BLACK and all the WHITE neighboring nodes of such nodes GREY.

Case D : If one node is BLACK and the other is GREY with at least one WHITE neighbor. Add the edge $e_{i, j}$ into partially constructed dominating tree $D T$ and recolour BLACK the node whose colour is GREY and also recolour GREY all its WHITE neighboring nodes.

After this another iteration begins. This process continues till the construction of the dominating tree is complete, i.e., till no WHITE node remains.

After the completion of the second phase of the heuristic, all nodes in $D T$ are reconnected by computing a minimum spanning tree (MST) (Prim 1957) on the subgraph of $G$ induced by these nodes, thereby possibly reducing the cost further as MST is a spanning tree of least cost among all spanning trees over a graph with given set of nodes. After computing MST, a pruning operator is called to remove all the redundant nodes from $D T$. A redundant node is a node such that if we remove that node from $D T, D T$ still satisfy the property of a dominating tree. Detail of pruning operator can be found in Sect. 3.2.

The following points highlight the differences between the H_DT of Sundar and Singh (2013) and our heuristic M_DT.

1. The determination of next edge $e_{i, j}$ to be added into $D T$ differs for the $\mathrm{H}_{-} \mathrm{DT}$ and the $\mathrm{M}_{-} \mathrm{DT}$. In the $\mathrm{H}_{-} \mathrm{DT}$, next edge to be added is an edge whose edge weight is least among all available edges, whereas in $\mathrm{M}_{-} \mathrm{DT}$, next edge is selected with the help of Expression 1.
2. In the heuristic $\mathrm{H}_{-} \mathrm{DT}$, the edge $e_{i, j}$ is always included into $D T$, but in case of heuristic $\mathrm{M}_{-} \mathrm{DT}$, the edge $e_{i, j}$ will be added to $D T$ only when absolutely necessary as explained already.
3. The heuristic $\mathrm{H}_{-} \mathrm{DT}$ applies two times pruning and two times reconnection by computing a minimum spanning tree (MST) in the following order: pruning $\rightarrow$ MST $\rightarrow$ pruning $\rightarrow$ MST, whereas in our heuristic $\mathrm{M}_{-} \mathrm{DT}$, we applied only once the pruning and MST in the order of MST followed by pruning. Actually, if we apply MST first then we may get a dominating tree of lesser cost

in comparison to applying the pruning first because we may lose some nodes in pruning which are vital for reducing the cost of the dominating tree. Empirical observations also favoured this strategy. It is computationally less expensive, as well.

Algorithm 1 provides the pseudo-code of M_DT.

```
Algorithm 1: The pseudo-code for heuristic M_DT
    //Initially all nodes in \(V\) are coloured WHITE
    \(W_{n} \leftarrow V ; \quad D T \leftarrow \emptyset ; \quad E_{r} \leftarrow E ; \quad n d \leftarrow \emptyset ;\)
    Compute shortest path between all pairs of nodes in G;
    \(e_{i, j} \leftarrow \arg \max _{e_{k, i} \in E_{r}} \frac{W\left(e_{k, j}\right)+\mathrm{no}\left(e_{k, j}\right)}{\mathrm{se}\left(e_{k, j}\right)} ;\)
    \(n d \leftarrow\left\{p: p \in O N(i) \cup O N(j) \cap W_{n}\right\} ;\)
    make \(i\) and \(j\) BLACK;
    make all nodes \(\in n d\) GREY;
    \(W_{n} \leftarrow W_{n} \backslash(n d \cup\{i, j\})\);
    \(D T \leftarrow D T \cup\left\{e_{i, j}\right\}\)
    while \(W_{n} \neq \emptyset\) do
        \(e_{i, j} \leftarrow \arg \max _{e_{k, i} \in E_{r}} \frac{W\left(e_{k, j}\right)+\mathrm{no}\left(e_{k, j}\right)}{\mathrm{se}\left(e_{k, j}\right)} ;\)
        if Both the nodes \(i\) and \(j\) are WHITE then
        \(\square\) Apply Case \(A\);
        else if One is WHITE and the other is GREY then
        \(\square\) Apply Case \(B\);
        else if Both the nodes \(i\) and \(j\) are GREY then
        \(\square\) Apply Case \(C\);
        else if One is BLACK and the other is GREY then
        \(\square\) Apply Case \(D\);
        Remove all BLACK and GREY nodes from \(W_{n}\);
```

Reconnect nodes in $D T$ via a minimum spanning tree;
Apply Pruning operator on nodes in $D T$;
return $D T$;

### 3.1 Illustrating H_DT and M_DT with an example

With the help of the Fig. 2, we demonstrate the process of construction of a dominating tree using the heuristic H_DT of Sundar and Singh (2013). In the Fig. 2a, initially all the nodes are assumed to have colour WHITE. The edge $e_{1,5}$, which has least weight among all the edges, is selected and added into dominating tree $D T$. Now, the nodes $\{1,5\}$ are recoloured BLACK and also their neighboring nodes $\{0,2$, 4 ] are recoloured GREY. This situation is shown in the Fig. 2b. In the next iteration, the edge $e_{9,10}$ is added into $D T$. As a result, the nodes $\{9,10\}$ are recoloured BLACK and their WHITE neighboring nodes $\{6,12,13\}$ are recoloured GREY. The two sub-trees $\left\{e_{1,5}\right\}$ and $\left\{e_{9,10}\right\}$ are connected via the shortest path between nodes 5 and 9 . The node 4 which is on this shortest path is recoloured BLACK and the edges $\left\{e_{5,4}, e_{4,9}\right\}$ are included into $D T$. This situation is depicted in the Fig. 2c where the shortest path between two sub-trees is shown with thick and dotted line. Now, the edge $e_{7,11}$ is selected and included into $D T$ which leads to the
recolouring of the nodes $\{7,11\}$ with BLACK colour and their WHITE neighboring nodes $\{8,14\}$ with GREY colour. The two resulting sub-trees, viz. $\left\{e_{1,5}, e_{5,4}, e_{4,9}, e_{9,10}\right\}$ and $\left\{e_{7,11}\right\}$ are connected via the shortest path between nodes 10 and 11. The node 6 which is on this shortest path is recoloured BLACK and the edges $e_{11,6}$ and $e_{6,10}$ are added into $D T$. This situation is shown in the Fig. 2d. In the last iteration, the edge $e_{2,3}$ is selected and included into $D T$ and the nodes $\{2,3\}$ are recoloured BLACK. The edge $e_{2,6}$ which constitutes the shortest path between the two subtrees $\left\{e_{1,5}, e_{5,4}, e_{4,9}, e_{9,10}, e_{10,6}, e_{6,11}, e_{11,7}\right\}$ and $\left\{e_{2,3}\right\}$ is included into $D T$ yielding a total weight of 36 for $D T$ (Fig. 2e). Now, no WHITE node remains, and as a result, the second phase of heuristic H_DT stops. Hereafter, a pruning procedure (Sect. 3.2) is applied to remove all the redundant edges as well as the redundant nodes. In the dominating tree $D T\left\{e_{1,5}, e_{5,4}, e_{4,9}, e_{9,10}, e_{10,6}, e_{6,11}, e_{11,7}, e_{2,6}\right.$, $\left.e_{2,3}\right\}$, the nodes $\{3,7\}$ are redundant. After the removal of these two redundant nodes and their corresponding redundant edges $\left\{e_{2,3}, e_{11,7}\right\}, D T$ becomes $\left\{e_{1,5}, e_{5,4}, e_{4,9}\right.$, $\left.e_{9,10}, e_{10,6}, e_{6,11}, e_{6,2}\right\}$ with total weight 25 . After the pruning procedure, a minimum spanning tree (MST) is constructed on the subgraph induced by the set of nodes in $D T$ to explore the possibility of reconnecting these nodes via this MST in case it leads to reduction in cost. In this example, nodes in $D T$ are already connected via a MST, so MST procedure fails to reduce the cost of $D T$ any further. Once again the pruning procedure is applied, but in vain as there are no redundant nodes. Finally, MST procedure is also applied unsuccessfully on the nodes of $D T$ and then the heuristic H_DT stops. The final dominating tree with weight 25 is shown in the Fig. 2f.

To illustrate the M_DT, the same input graph with 15 nodes as used for the H_DT is taken. Initially, all nodes are assumed to have colour WHITE as shown in the Fig. 3a. At the first iteration, the edge $e_{7,11}$ is selected by the Expression 1 as this edge has the maximum ratio. Now, the edge $e_{7,11}$ is included into empty dominating tree DT. The nodes $\{7,11\}$ are coloured BLACK and also all the WHITE neighboring nodes $\{2,6,8,13,14\}$ of the nodes $\{7,11\}$ are coloured GREY. This situation is shown in the Fig. 3b. In the next iteration, Expression 1 returns the edge $e_{9,10}$. Here both the nodes, viz. 9 and 10 are WHITE, and therefore, the Case A is applicable. Now, to connect the sub-trees $\left\{e_{7,11}\right\}$ and $\left\{e_{9,10}\right\}$ a shortest path between these two sub-trees is searched. Here the shortest path is between the nodes 11 and 10 with node 6 as the only intermediate node. The edges lying on the shortest path, viz. $e_{11,6}$ and $e_{6,10}$ are added into $D T$. The nodes 6 and 10 are recoloured BLACK. Now, the $w d(9)$ is calculated and $w d(9) \geq 1$, therefore, the edge $e_{10,9}$ is added into $D T$ and the node 9 is recoloured BLACK and also all the WHITE neighboring nodes of the node 9 , viz. 4 and 12 are recoloured GREY. This situation is shown in Fig. 3c.

![img-4.jpeg](img-4.jpeg)

Fig. 2 Illustrating H_DT heuristic. a Initially, all nodes are coloured WHITE and weight $=0$. b Edge $e_{1,5}$ is selected by heuristics $\mathrm{H}_{-} \mathrm{DT}$ and weight $=1$. c Edge $e_{9,10}$ is selected by heuristics $\mathrm{H}_{-}$DT and
weight $=7$. d Edge $e_{7,11}$ is selected by heuristics $\mathrm{H}_{-}$DT and weight $=$ 19. e Edge $e_{2,3}$ is selected by heuristics $\mathrm{H}_{-}$DT and weight $=36$. f After pruning, MST, pruning and MST weight $=25$
![img-5.jpeg](img-5.jpeg)

Fig. 3 Illustrating M_DT heuristic. a Initially, all nodes are coloured WHITE and weight $=0$. b Edge $e_{7,11}$ is selected by heuristics M_DT and weight $=2$. c Edge $e_{9,10}$ is selected by heuristics M_DT
and weight $=13$. d Edge $e_{1,5}$ is selected by heuristics M_DT and weight $=19$. e Edge $e_{2,3}$ is selected by heuristics M_DT and weight $=24$. f After MST and pruning weight $=22$

Next, the edge $e_{1,5}$ is returned by the Expression 1 leading to the Case $A$ again. The edges $e_{9,4}, e_{4,5}, e_{5,1}$ are added into the partially constructed dominating tree DT, the nodes 4 , 5 and 1 are coloured BLACK and their WHITE neighbors GREY (in this case only the node 0 ). This is shown in the Fig. 3d.

In the last iteration, the edge $e_{2,3}$ is returned by the Expression 1, because the ratio of edges $e_{2,3}, e_{8,11}, e_{3,8}, e_{2,6}, e_{1,2}$ and $e_{2,7}$ are $2.11,2,1.9,1.12,0.81$ and 0.75 respectively and the remaining edges have ratio zero. Here the node 2 is GREY and the node 3 is WHITE. So the Case $B$ is applicable. As a result, the shortest path between neighbor-

ing nodes $\{2,8\}$ of node 3 and the partially constructed tree $\left\{e_{1,5}, e_{5,4}, e_{4,9}, e_{9,10}, e_{10,6}, e_{6,11}, e_{11,7}\right\}$ is computed. This shortest path is between the nodes 11 and 8 without any intermediate node. The edge $e_{11,8}$ is included into DT, and, the node 3 , which is the only WHITE neighbor of the node 8 is recoloured GREY. Here $w d(3)$ is zero; therefore the edge $e_{8,3}$ is not included into DT. At this point M_DT stops as no WHITE node remained, and, the construction of the dominating tree $D T$ is complete. This dominating tree has cost 24 (Fig. 3e). Comparing Fig. 2e with Fig. 3e, we can see that the cost of the dominating tree returned by the heuristic H_DT is 36 , whereas the M_DT returns a dominating tree with cost 24 on the same graph. Thus, we can say that our heuristic M_DT can perform better than the heuristic H_DT of Sundar and Singh (2013). Hereafter, we compute a minimum spanning tree (MST) on the set of nodes in $D T$ to reconnect these nodes via this MST in a bid to reduce the cost of DT further. As the nodes of $D T$ are already connected via a MST so cost of $D T$ remains the same. Next the pruning operator is applied to remove the redundant nodes as well as redundant edges which removes the node 7 and the edge $e_{11,7}$ leading to the final $D T$ with cost 22 as shown in Fig. 3f.

### 3.2 Pruning operator

Our Pruning operator is similar to the pruning procedure of Sundar and Singh (2013). Pruning operator removes the redundant nodes of dominating tree DT. Let $D N$ be the set of nodes belonging to $D T$. A node $v \in D N$ is redundant if $|O N(v) \cap D N|=1$ and $C N(v) \subseteq\left(\cup_{u \in D N \backslash\{v\}} O N(u)\right)$, i.e., the degree of the node $v$ in $D N$ must be one and all the non-dominating neighboring nodes of the node $v$ are covered by some other dominating nodes (other than the node $v$ ) in $D N$. If the node $v$ is redundant then it can be removed from $D N$ without affecting the dominating tree characteristic of $D T$. Our pruning operator begins by computing the set $R_{n}$ of redundant nodes and then an iterative process starts where during each iteration a node is selected and removed from $D N$ and the set $R_{n}$ is recomputed. We have selected a node for removal from $R_{n}$ according to the order in which it is added into $D N$. We have also tried selecting a node from $R_{n}$ according to the non-increasing order of the cost of their sole incident edge or according to the non-decreasing order of the number of non-dominating nodes covered by each node in $R_{n}$. Experimentally, we observed that solutions obtained through different ordering schemes did not differ much in quality and no ordering scheme has an ultimate advantage over others. Therefore, we settled for a simpler ordering scheme. Iterative process stops when the set $R_{n}$ becomes empty. The pseudo-code of the pruning operator is presented in Algorithm 2 where Select_Node $\left(R_{n}\right)$ is a function that returns a node from $R_{n}$ which was added first into $D N$ among all the nodes currently present in $R_{n}$.

```
Algorithm 2: The pseudo-code of Pruning operator
    \(R_{n} \leftarrow\left\{v: v \in D N\right.\) and \(\left.|O N(v) \cap D N|=1\right.\) and \(\left.C N(v) \subseteq\right.\)
    \(\left(\cup_{u \in D N \backslash\{v\}} O N(u)\right)\);
    while \(\left(R_{n} \neq \emptyset\right)\) do
        \(v \leftarrow\) Select_Node \(\left(R_{n}\right)\);
        \(D N \leftarrow D N \backslash\{v\}\)
        \(R_{n} \leftarrow\left\{v: v \in D N\right.\) and \(\left.|O N(v) \cap D N|=1\right.\) and \(\left.C N(v) \subseteq\right.\)
    \(\left(\cup_{u \in D N \backslash\{v\}} O N(u)\right)\);
    return \(D N\);
```


## 4 Overview of the EA/G

The evolutionary algorithm with guided mutation (EA/G) is a relatively new member in the class of evolutionary algorithms. It was developed by Zhang et al. (2005) with a motivation to overcome, as far as possible, the drawbacks of two evolutionary algorithms, viz. genetic algorithms (GAs) and estimation of distribution algorithms (EDAs).

The EA/G has the features of both GAs and EDAs. Conventionally, GAs use genetic operators such as crossover and mutation to generate an offspring from the selected parents. GAs directly utilize only the location information of the solutions and do not make use of global information about the search space which can be collected by keeping track of all the solutions generated since the beginning of the algorithm. On the other hand, EDAs rely only on a probability model to generate an offspring. The probability model characterizes the distribution of the promising solutions in the search space and is updated at each generation using the global statistical information about the search space extracted from the population members present at that generation. An offspring is generated by sampling this probability model. Contrary to GAs, EDAs do not directly utilize the location information of solutions. Here, by the location information of a solution, we mean the information that can uniquely identify a solution in the search space of all solutions. For example, in case of the DTP, the set of edges present in a dominating tree constitutes its location information as this information can uniquely identify a dominating tree.

Taking into the account this complementary aspect of GAs and EDs, Zhang et al. (2005) developed an ideal algorithm that utilizes the location information of the solutions like GAs and the global statistical information about the search space like EDAs while generating an offspring. This algorithm was named evolutionary algorithm with guided mutation (EA/G). EA/G uses a mutation operator, called guided mutation (GM), to generate offsprings. Guided mutation generates a new solution considering both the location information about the parent solution as well as the global statistical information about the search space, i.e., a solution is generated partly by sampling a probability model characterizing the global statistical information and partly by copying elements from its parent.

## 5 Hybrid EA/G approach for DTP

Our proposed hybrid approach for the dominating tree problem (DTP) is inspired by the approach of Zhang et al. (2005) for the maximum clique problem (MCP). Success of the EA/G in solving the MCP over standard benchmark instances have motivated us to develop an EA/G approach for the DTP. Solutions obtained through the EA/G approach are further improved through the use of the same two procedures as used in M_DT, i.e., reconnecting the nodes of the solution via minimum spanning tree (MST) and pruning operator. However, each of these procedures are applied twice in the order MST $\rightarrow$ pruning $\rightarrow$ MST $\rightarrow$ pruning. Hereafter, our hybrid EA/G approach with MST and pruning operator will be referred to as EA/G-MP (EA/G with MST and pruning operator).

Before starting our EA/G-MP approach, we pre-compute the set of neighboring nodes for each node $v \in V$ and the shortest paths between all pairs of nodes in $V$. Subsequent subsections describe other salient features of EA/GMP approach.

### 5.1 Solution encoding

Edge-set encoding has been used to represent a solution, i.e., each dominating tree is represented directly be the set of the edges it contains. The edge-set encoding was introduced by Raidl and Julstrom (2003) for representing a spanning tree. It is to be noted that a spanning tree always has $|V|-1$ edges, whereas the number of edges in a dominating tree varies.

### 5.2 Initial solutions

Our initial solution generation method is derived from the initial solution generation method used in Sundar and Singh (2013). First we will describe the initial solution generation method of Sundar and Singh (2013) and then introduce our modifications. Let $W_{n}$ be the set of WHITE nodes which is initialized to $V\left(W_{n}=V\right.$ initially). Let $I_{n}$ be the set of nondominating nodes, $D N$ be the set of dominating nodes and $D T$ be the partially constructed dominating tree. Initially, these three sets, viz. $I_{n}, D N$ and $D T$ are empty. Randomly, a node say $v$ is selected from $W_{n}$ and added into $D N$ and recoloured BLACK and node $v$ is removed from set $W_{n}$. Now, consider a set $n_{b}$ of WHITE neighboring nodes of node $v$, i.e., $n_{b}=O N(v) \cap W_{n}$. Remove the nodes in $n_{b}$ also from $W_{n}$. After that all the nodes in $n_{b}$ are recoloured GREY and added into the set $I_{n}$. From here onwards, at each step, an edge is selected by following one of the two strategies. With probability $\varphi$, first strategy is followed where a least cost edge $e_{v, u}$, connecting a node $v$ in $D N$ and a node $u$ in $I_{n}$ is selected. Otherwise second strategy is followed where an edge $e_{v, u}$ connecting a node $v$ in $D N$ to a node $u$ in $I_{n}$ is selected randomly. Here $\varphi$ is a parameter to be determined

Algorithm 3: The pseudo-code for initial solution
//Initially all nodes in $V$ are coloured WHITE
$W_{n} \leftarrow V ; \quad D T \leftarrow \emptyset ; \quad D N \leftarrow \emptyset ; \quad I_{n} \leftarrow \emptyset ;$
$v \leftarrow \operatorname{random}\left(W_{n}\right) ;$
$D N \leftarrow D N \cup\{v\}$;
make $v$ BLACK;
$n_{b} \leftarrow O N(v) \cap W_{n}$
$W_{n} \leftarrow W_{n} \backslash\left(n_{b} \cup\{v\}\right)$;
make all nodes $\in n_{b}$ GREY;
$I_{n} \leftarrow n_{b}$;
while $W_{n} \neq \emptyset$ do
Generate a random number $u_{01}$ such that $0 \leq u_{01} \leq 1$;
if $u_{01}<\varphi$ then
$(v, u) \leftarrow \arg \min _{v \in D N,\left\{u \in I_{n},\left|O N(u) \cap W_{n}\right| \geq 1\right\}} w(v, u)$;
else
$v \leftarrow \operatorname{random}(D N)$;
$u \leftarrow\left\{u: \operatorname{random}\left(I_{n}\right)\right.$ and $\left|O N(u) \cap W_{n}\right| \geq 1\}$;
$D T \leftarrow D T \cup\left\{e_{v, u}\right\}$;
$D N \leftarrow D N \cup\{u\}$;
make $u$ BLACK;
$I_{n} \leftarrow I_{n} \backslash\{u\} ;$
$n_{b} \leftarrow\left\{u: u \in O N(u) \cap W_{n}\right\} ;$
make all nodes $\in n_{b}$ GREY;
$I_{n} \leftarrow I_{n} \cup n_{b}$;
$W_{n} \leftarrow W_{n} \backslash n_{b}$
Apply pruning operator on nodes in $D T$;
Reconnect nodes in $D T$ via a minimum spanning tree;
return $D T$;
empirically. Clearly, first strategy aims at quality, whereas the latter strategy aims at diversity. Therefore, $\varphi$ governs the delicate balance between the quality and the diversity of initial solutions. We have made two modifications in the initial solution generation method of Sundar and Singh (2013). Our first modification here is that only those edges $e_{v, u}$ are considered where $u \in I_{n}$ has at least one WHITE neighboring node, i.e., where $\left|O N(u) \cap W_{n}\right| \geq 1$. Whereas in Sundar and Singh (2013), those nodes in $I_{n}$ are also considered which have no WHITE neighboring node and as a result some edges might be unnecessarily inserted into $D T$. In addition, with probability $1-\varphi$, we are selecting the edges uniformly at random instead of using roulette wheel selection method like Sundar and Singh (2013). Now, the node $u$ is added into set $D N$ and removed from $I_{n}$ and an edge $e_{v, u}$ is added into the set $D T$. Nodes in $n_{b}=O N(u) \cap W_{n}$ are added into $I_{n}$ and nodes in $n_{b}$ are removed from $W_{n}$. After that all the WHITE neighboring nodes of the node $u$ are recoloured GREY. This whole process is repeated until the set $W_{n}$ becomes empty. After construction of a feasible dominating tree $D T$, a pruning operator (as described in Sect. 3.2) is applied to remove the redundant nodes from $D N$ and the redundant edges from $D T$. After an application of the pruning operator, a MST is constructed on the set of nodes in $D N$ and these nodes are reconnected via this MST. Pseudo-code of the construction of an initial solution is presented in the Algorithm 3. Here, we have applied pruning first

and then MST with the intention of generating more diverse solutions.

### 5.3 Initialization and update of the probability vector

Our EA/G-MP, as in Zhang et al. (2005), models the distribution of promising solutions in the search space through the use of univariate marginal distribution (UMD) model. In this model, a probability vector $p=\left\{p_{1}, p_{2}, \ldots, p_{|V|}\right\} \in$ $[0,1]^{|V|}$ is used to characterize the distribution of the promising solutions in the search space, where $|V|$ is the cardinality of the set $V$, i.e., the number of nodes in the graph $G . p_{v}$ is the probability of the node $v \in V$ to be present in a dominating tree. The probability vector is initialized using $N_{p}$ initial solutions. The probability of each node is initialized to the ratio of the number of initial solutions containing that node to the total number of initial solutions. The pseudo-code for initializing the probability vector $p$ for the DTP is presented in Algorithm 4.

```
Algorithm 4: The pseudo-code for initializing a proba-
    bility vector p
    Compute \(n_{v} \leftarrow\) number of initial solutions containing
    node \(v, \forall v \in V\);
    Compute \(p_{v} \leftarrow \frac{n_{v}}{N_{p}}, \forall v \in V\);
```

At each generation $g$, a parent set parent $(g)$ is formed by selecting the best $L$ solutions from current population $\operatorname{pop}(g)$. Once parent $(g)$ is formed, it is used for updating the probability vector $p$. The pseudo-code for updating the probability vector is given in Algorithm 5, where $\lambda \in(0,1]$ is the learning rate and it governs the contribution of solutions in parent $(g)$ to the updated probability vector $p$, i.e., higher the value of $\lambda$, more is the contribution of solutions in parent $(g)$. The probability of a node increases after update if the ratio of solutions containing this node in parent $(g)$ to the total number of solutions in parent $(g)$ is more than its current probability. The probability decreases in case this ratio is less than its current value. The probability remains the same in case this ratio is exactly equal to its current value.

```
Algorithm 5: The pseudo-code for updating the proba-
    bility vector \(p\) in generation \(g\)
    Compute \(n_{v} \leftarrow\) number of solutions in parent \((g)\)
    containing node \(v, \forall v \in V\);
    Compute \(p_{v} \leftarrow(1-\lambda) p_{v}+\lambda \frac{n_{v}}{L}, \forall v \in V\);
```


### 5.4 Guided mutation (GM) operator

As we have already discussed in Sect. 4, the GM operator uses both the global statistical information stored in

```
Algorithm 6: The pseudo-code of generating a solution
through GM operator
Set the colour of all nodes in V to WHITE;
\(D T \leftarrow \emptyset\);
foreach node \(v \in V\) in some random order do
    Generate a random number \(r_{1}\) such that \(0 \leq r_{1} \leq 1\);
    if \(r_{1}<\beta\) then
        Generate a random number \(r_{2}\) such that \(0 \leq r_{2} \leq 1\);
        if \(\left(r_{2}<p_{v}\right)\) and \(((v\) is WHITE) or \((v\) is GREY with at
        least one WHITE neighbor)) then
            Find the shortest path \(S P\) between node \(v\) and a node
            \(u\) in \(D T\);
            Add all the edges of \(S P\) into \(D T\);
            Colour BLACK all the nodes on the path \(S P\);
            Colour GREY all the WHITE neighboring nodes of
            nodes on the path \(S P\);
else
        if \(v\) is a dominating node in \(m_{i}\) and \(v\) is GREY with at
        least one WHITE neighbor then
            Find the shortest path \(S P\) between node \(v\) and a node
            \(u\) in \(D T\);
            Add all the edges of \(S P\) into \(D T\);
            Colour BLACK all the nodes on the path \(S P\);
            Colour GREY all the WHITE neighboring nodes of
                nodes on the path \(S P\);
return \(D T\);
```

the form of probability vector $p$ and the location information of the parent solution for generating new offsprings. Zhang et al. (2005) applied GM operator $M$ times on the best solution of the current population to generate $M$ offsprings. On the other hand, our $G M$ operator is applied on $M$ best solutions of current population $\operatorname{pop}(g)$ to generate $M$ new offsprings. In other words, on the set of $M$ best solutions $\left\{m_{1}, m_{2}, \ldots, m_{M}\right\}, G M$ is applied once on each $m_{i}, i=1,2 \ldots, M$ to generate $\left\{o_{1}, o_{2}, \ldots, o_{M}\right\}$ offsprings. The pseudo-code of our $G M$ operator is presented in Algorithm 6 where $\beta \in[0,1]$ is an adjustable parameter and $D T$ is a new offspring constructed through $G M$ operator whose nodes are either sampled randomly from the probability vector $p$ or directly copied from the solution $m_{i}$ in $\operatorname{pop}(g)$. In case of sampling from probability vector $p$, a node is copied only when either its colour is WHITE according to partially constructed $D T$ or its colour is GREY and it has at least one WHITE neighbor. Whereas in case a node is to be directly copied from the solution $m_{i}$, it is copied only when it is a dominating node in $m_{i}$, its colour is GREY according to partially constructed $D T$ and it has at least one WHITE neighbor. The reason behind such a policy lies in the fact that by copying a node from $m_{i}$ only when its colour is GREY according to $D T$ will help in getting some more edges in $D T$ from $m_{i}$. As $m_{i}$ is among the best $M$ solutions, this may help in improving the solution quality. There is no guarantee of the feasibility of the offspring generated through $G M$ operator, i.e., it may

not be a dominating tree. Therefore, each infeasible offspring generated through $G M$ operator is passed through a repair operator (Sect. 5.5) so that it can be made feasible.

### 5.5 Repair operator

Repair operator is applied only on an infeasible offspring generated through $G M$ operator. After the application of $G M$ operator, there is a possibility that some WHITE nodes remain, i.e., some nodes may remain uncovered. Let $U_{c n}$ be the set of such WHITE nodes. Such WHITE nodes are covered by making use of the repair operator which follows an iterative procedure. During each iteration, a node with the highest number of WHITE neighboring nodes is selected from $U_{c n}$ (ties are broken in favour of the node having lower index). If none of the nodes in the set $U_{c n}$ has WHITE neighboring nodes, then the node with lowest index is selected from $U_{c n}$. After selecting the node $i$ from the set $U_{c n}$, a shortest path between the node $i$ and the partially constructed tree $D T$ is found, and, all the edges on this path are added into $D T$. All the nodes on this path are recoloured BLACK (if not already) and their neighboring nodes GREY. Then all BLACK and GREY nodes are removed from the set $U_{c n}$. After this another iteration begins. This whole process is repeated until set $U_{c n}$ becomes empty. The pseudo-code of the repair operator is given in Algorithm 7.

```
Algorithm 7: The pseudo-code of repair operator
    while \(U_{c n} \neq \emptyset\) do
        \(v \leftarrow \arg \max _{u \in U_{c n}}(w d(u)>0)\);
        if \(v=\emptyset\) then
            Select a node \(v\) with lowest index from \(U_{c n}\);
            Find a shortest path \(S P\) between node \(v\) and a node
            \(u\) in \(D T\);
            Add all the edges on the path \(S P\) into \(D T\);
            Make BLACK all nodes \(\in S P\);
            Make GREY all WHITE neighboring nodes of
            nodes \(\in S P\);
            Remove all BLACK and GREY nodes from \(U_{c n}\);
    return DT;
```


### 5.6 Others features

Zhang et al. (2005) kept best $\frac{N_{p}}{2}$ solutions of $\operatorname{pop}(g)$ into parent $(g)$ and generated $\frac{N_{p}}{2}$ new offsprings through $G M$ operator in each generation (iteration). The population of the next generation is formed by using $\frac{N_{p}}{2}$ newly created offsprings through $G M$ operator and best $\frac{N_{p}}{2}$ solutions of $\operatorname{pop}(g)$. Therefore, in each next generation the population size remains the same as in previous generation. On the other hand, in our approach parent $(g)$ is formed by using best $L$ solutions of $\operatorname{pop}(g)$ and $M$ new offsprings are gen-
erated through $G M$ operator in each generation. The best $N_{p}-M$ solutions of $\operatorname{pop}(g)$ along with $M$ newly generated offsprings constitute $\operatorname{pop}(g+1)$. Therefore, also in this case population size remains the same throughout the execution of the algorithm.

Unlike Zhang et al. (2005), we never found all the solutions of the population to be same. We also observed that the best solution does not improve for a large number of generations. Therefore, to avoid getting stuck into a local optimum, if the best solution does not improve over $S_{c}$ generations, then, except for the best solution, we reinitialize the entire population in the same manner as described in Sect. 5.2. So, in a way, we have followed the 1-elitism policy as best solution is retained always.

The pseudo-code of our EA/G-MP approach for DTP is given in Algorithm 8.

```
Algorithm 8: EA/G-MP Approach for DTP
1 At generation \(g \leftarrow 0\), an initial population \(\operatorname{pop}(g)\) consisting of
    \(N_{p}\) solutions, is generated randomly;
2 Initialize the probability vector \(p\) for all nodes using Algorithm 4;
3 Select best \(L\) solutions from \(\operatorname{pop}(g)\) to form a parent set parent \((g)\).
    and then update the probability vector \(p\) using Algorithm 5;
4 Apply the \(G M\) operator once on each of the \(M\) best solutions in
    pop(g) in order to generate \(M\) new solutions. A repair operator is
    applied to each generated solution, if necessary, and then MST,
    pruning operator, MST and pruning operator are applied to each
    generated solution to improve its fitness. Add all \(M\) newly
    generated solutions along with \(N_{p}-M\) best solutions in pop(g)
    to form \(\operatorname{pop}(g+1)\). If the stopping condition is met, return the
    dominating tree with minimum weight found so far ;
\(5 g \leftarrow g+1\);
6 If the best solution of the population did not improve over \(S_{c}\)
    generations, then reinitialize entire pop(g) except for the best
    solution, and then go to step 2 ;
7 Go to step 3 ;
```


## 6 Computational results

Our approaches, viz. M_DT and EA/G-MP have been implemented in C and executed on an Intel Core 2 Duo processor based system with 2 GB RAM running under Fedora 12 at 3.0 GHz which is exactly the same system as used for executing the approaches of Sundar and Singh (2013). Likewise gcc 4.4.4-10 compiler with 03 flag has been used to compile the C programs of our approaches. We have used a super set of test instances used in Sundar and Singh (2013) to test our approaches. Due to unavailability of the test instances used in Zhang et al. (2008) and Shin et al. (2010), Sundar and Singh (2013) generated a set of 18 test instances in the same manner as in Zhang et al. (2008) and Shin et al. (2010). These instances were generated considering a disk graph $G=(V, E)$, where each disk around a

node represents the transmission range of that node. There exists an edge between a pair of nodes if these two nodes are within the transmission range of each other. The weight on each edge $e_{i, j}$ in $E$ is assigned through a weight function $w: E \rightarrow \Re^{+} \xrightarrow{\sim}$ which is defined as $w\left(e_{i, j}\right)=d_{i, j}^{2}$, where $d_{i, j}$ is the Euclidean distance between the nodes $i$ and $j$. It was assumed that nodes in $|V|$ are randomly deployed in a $500 \mathrm{~m} \times 500 \mathrm{~m}$ area and transmission range of each node is 100 m . For each value of $|V|$ in $\{50,100,200,300,400$, 500\}, three different test instances were generated leading to a total of 18 instances. In addition to the transmission range of 100 m , we consider two more values for transmission range of each node, viz. 125 and 150 m and generated three different test instances for each combination of values of $V$ mentioned above and one of these two values of transmission range. This results in generation of 36 additional instances leading to a grand total of 54 instances. All these 54 test instances can be downloaded from http://dcis.uohyd.ernet.in/ alokcs/dtp.zip. Actually, density of a disk graph depends on the transmission range of its constituent nodes. The longer the transmission range of nodes, the higher will be the density of the corresponding disk graph. Therefore, to show that effectiveness of our proposed approaches is not limited to graphs with a particular density, it is necessary to consider different values of transmission range. The values of transmission range that we have considered leads to difficult randomly generated feasible DTP instances. We have also considered the transmission range of 75 and 200 m . At the transmission range of 75 m , not all instances with 50 nodes were connected. At the transmission range of 200 m , generated instances were highly dense, and therefore, all dominating trees on these instances had few edges only, and as a result, finding a minimum dominating tree among them was not that difficult. As the C programs for the approaches considered in Sundar and Singh (2013) were available, we have executed them on these additional 36 instances under the same setup as used for our approaches.

For EA/G-MP, we have used a population size of 60 , i.e., $N_{p}=60$, generated $M=25$ new solutions through guided mutation and used $L=15$ best solutions of current population to update probability vector. The value of $\beta$ is set to 0.50 in the guided mutation. The value $\lambda=0.50$ is used in the update of probability vector and the value $\varphi=0.20$ is used in the initial solution generation. If the best solution does not improve over $S_{c}=400$ generations, entire population minus the best solution and the probability vector are reinitialized. We have allowed our EA/G-MP approaches to execute till the best solution does not improve over 3,000 generations and it has executed at least for a total of 10,000 generations. All these parameters are set empirically after a large number of trials. These parameter values provide good results on all instances, though they may not be optimal for all instances. Like ABC_DT and ACO_DT approaches of

Sundar and Singh (2013), EA/G-MP has been executed 20 independent times on each test instance.

We first present the results of M_DT and other problem specific heuristics. Tables 2, 3 and 4 report the results of M_DT on instances with transmission range 100, 125 and 150 m respectively and compare them with previously proposed heuristic approaches, viz. heuristics of Zhang et al. (2008), Shin et al. (2010) and Sundar and Singh (2013), which will be referred to as Heu_DT1, Heu_DT2 and H_DT respectively. In addition, we have also included a simple heuristic which computes a MST on the input graph and then removes leaf nodes from the computed MST to obtain a dominating tree. This heuristic, which will be referred to as MST-L was used in Zhang et al. (2008) and Shin et al. (2010) for comparison against their respective heuristics. For each heuristic, these tables report the cost of the dominating tree obtained (column labelled Value) and the number of nodes in the dominating tree (column labelled NDN) on each instance. In Table 2, data for Heu_DT1, Heu_DT2, H_DT and MSTL are taken from Sundar and Singh (2013). Whereas Tables 3 and 4 contain the results obtained after executing various approaches on 36 new instances. These three tables also report the \% improvement in cost of the dominating tree obtained by M_DT over other approaches. Though not the objective of DTP, we have reported the number of nodes in the dominating tree due to past precedences. Zhang et al. (2008), Shin et al. (2010) and Sundar and Singh (2013), all reported the number of nodes in the dominating tree obtained by various approaches. These tables clearly show the superiority of M_DT over other approaches in terms of the cost of the dominating tree obtained. Except for 8 instances (3 with transmission range $100 \mathrm{~m}, 4$ with transmission range 125 m and 1 with transmission range 150 m ) where $\mathrm{H} \_\mathrm{DT}$ has slightly better cost (as indicated by negative value for \% improvement of M_DT over H_DT in Tables 2, 3 and 4), cost of the dominating tree obtained by M_DT is always better than all the other approaches. As far as number of dominating nodes in a solution is concerned, performance of M_DT is far superior in comparison to Heu_DT1, Heu_DT2 and MST-L on all instances. However, H_DT performs slightly better on this count on most of the instances. Execution times of various heuristics are not reported as all of them hardly need a second on any instance.

Tables 5, 6 and 7 report the results of EA/G-MP on instances with transmission range 100, 125 and 150 m respectively and compare them with ABC_DT and ACO_DT approaches of Sundar and Singh (2013). For each test instance, these tables report the best solution (column Best), average solution quality (column Avg), standard deviation of solution values (column SD), average number of dominating nodes (column ANDN) and average total execution time in seconds (column ATET) obtained over 20 runs for EA/G-MP, ABC_DT and ACO_DT. Data for ABC_DT

Table 2 Results of MST_L, Heu_DT1, Heu_DT2, H_DT and M_DT on the instances with transmission range 100 m
Table 3 Results of MST_L, Heu_DT1, Heu_DT2, H_DT and M_DT on the instances with transmission range 125 m
and ACO_DT is taken from Sundar and Singh (2013) for Table 5. On the other hand, Tables 6 and 7 report the results obtained after executing ABC_DT and ACO_DT on

36 new instances. These three tables also report the results of Mann-Whitney $U$ test between EA/G-MP and ABC_DT (column ABC_EA/G) and between EA/G-MP and ACO_DT

Table 4 Results of MST_L, Heu_DT1, Heu_DT2, H_DT and M_DT on the instances with transmission range 150 m
(column $\mathrm{ACO} \_$EA/G) on each instance as best and average solution quality of these approaches are close to each other. For Mann-Whitney $U$ test, we have used the online calculator available at http://www.socscistatistics.com/tests/ mannwhitney/Default2.aspx. For this test, we have used twotailed hypothesis and $5 \%$ significance criterion ( $p$ value $\leq 0.05$ ) leading to a critical $U$ value of 127 .

### 6.1 Comparison of EA/G-MP, ABC_DT and ACO_DT approaches on instances with transmission range 100 m

Out of 18 test instances with transmission range 100 m , EA/G-MP is better than ABC_DT on 10 test instances and equal to ABC_DT on 8 test instances in terms of quality of the best solution found. Whereas in terms of average solution quality, EA/G-MP is better than ABC_DT on 12 test instances and worse than ABC_DT on 3 test instances and on the remaining 3 test instances EA/G-MP is equal to ABC_DT. Results of Mann-Whitney $U$ test between EA/G-MP and ABC_DT indicate that out of 18 test instances, results of EA/G-MP is statistically significant on 12 test instances in comparison to ABC_DT, whereas on 3 test instances (100_2, 200_1 and 200_2) results are not significant. On the remaining three instances, results of Mann-Whitney $U$ test are not meaningful as both the approaches obtained the same results in all 20 runs. As far as comparison in terms of average number of dominating nodes is concerned, EA/G-MP is better than ABC_DT on 5 test instances, worse than ABC_DT on 9
test instances and equal to ABC_DT on 4 test instances. Our EA/G-MP approach is much faster than ABC_DT approach. On all 18 test instances the average total execution time (ATET) of EA/G-MP is better than ABC_DT. From Table 5, it can be observed that as the size of the input graph increases, the gap in terms of computational time between ABC_DT and EA/G-MP increases as well. On an average, EA/G-MP is 3 times faster than ABC_DT on the instances with 50 nodes, 3 times faster than ABC_DT on the instances with 100 nodes, 4 times faster than ABC_DT on the instances with 200 nodes, 5 times faster than ABC_DT on the instances with 300 nodes, 6 times faster than ABC_DT on the instances with 400 nodes and 8 times faster than ABC_DT on the instance with 500 nodes.

Now, we compare EA/G-MP with ACO_DT. Out of 18 test instances, the best solution of EA/G-MP is better than ACO_DT on 11 test instances, worse than ACO_DT on 2 test instances and on the remaining 5 test instances both approaches obtained the same best solution. In terms of average solution quality, EA/G-MP is better than ACO_DT on 10 test instances, worse than ACO_DT on 5 test instances and on the remaining 3 test instances both the approaches have the same average solution quality. Results of Mann-Whitney $U$ test between EA/G-MP and ACO_DT show that out of 18 test instances, results of EA/G-MP is statistically significant in comparison to ACO_DT on 12 test instances whereas on 3 test instances (100_1, 400_3 and 500_3) results are not significant. On the remaining three instances, results of Mann-

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)

Whitney $U$ test are not meaningful as both the approaches obtained the same results in all 20 independent runs. As far as comparison in terms of average number of dominating nodes is concerned, EA/G-MP is better than ACO_DT on 10 test instances, worse than ACO_DT on 4 test instances and equal to ACO_DT on 4 test instances. From Table 5, it can be observed that as the size of the input graph increases, the gap in terms of computational time between ACO_DT and EA/G-MP increases as well. On an average, EA/G-MP is 4 times faster than ACO_DT on the instances with 200 nodes, 10 times faster than ACO_DT on the instances with 300 nodes, 14 times faster than ACO_DT on the instances with 400 nodes and 22 times faster than ACO_DT on the instance with 500 nodes. On the other hand, EA/G-MP is 3 times slower than ACO_DT on the instances with 50 nodes and slightly slower than ACO_DT on the instances with 100 nodes.

### 6.2 Comparison of EA/G-MP, ABC_DT and ACO_DT approaches on instances with transmission range 125 m

Out of 18 test instances with transmission range 125 m , the best solution obtained by EA/G-MP is better than ABC_DT on 10 test instances, worse than ABC_DT on 1 test instances and equal to ABC_DT on 7 test instances. Whereas in terms of average solution quality, EA/G-MP is better than ABC_DT on 11 test instances and worse than ABC_DT on 3 test instances and on the remaining 4 test instances EA/GMP is equal to ABC_DT. Results of Mann-Whitney $U$ test between EA/G-MP and ABC_DT indicate that out of 18 test instances, results of EA/G-MP is statistically significant on 12 test instances in comparison to ABC_DT, whereas on 2 test instances (200_2 and 300_3) results are not significant. On the remaining four instances, results of Mann-Whitney $U$ test are meaningless as both the approaches obtained the same results in all 20 independent runs. As far as comparison in terms of average number of dominating nodes is concerned, EA/G-MP is better than ABC_DT on 6 test instances, worse than ABC_DT on 6 test instances and equal to ABC_DT on 6 test instances. Our EA/G-MP approach is much faster than ABC_DT approach. On all 18 test instances the average total execution time (ATET) of EA/G-MP is better than ABC_DT. From Table 6, it can be observed that as the size of the input graph increases, execution time of ABC_DT increases at a faster pace than EA/G-MP. On an average, EA/G-MP is 2 times faster than ABC_DT on the instances with 50 and 100 nodes, 4 times faster than ABC_DT on the instances with 200 nodes, 5 times faster than ABC_DT on the instances with 300 nodes, 7 times faster than ABC_DT on the instances with 400 nodes and 8 times faster than ABC_DT on the instance with 500 nodes.

As far as comparison between EA/G-MP and ACO_DT is concerned, out of 18 test instances, the best solution obtained
by EA/G-MP is better than ACO_DT on 11 test instances, worse than ACO_DT on 1 test instances and on the remaining 6 test instances both approaches obtained the same best solution. In terms of average solution quality, EA/G-MP is better than ACO_DT on 16 test instances, worse than ACO_DT on 1 test instance and on the remaining 1 test instance both the approaches have the same average solution quality. Results of Mann-Whitney $U$ test between EA/G-MP and ACO_DT show that out of 18 test instances, results of EA/G-MP is statistically significant in comparison to ACO_DT on 15 test instances whereas on 2 test instances (50_1 and 200_1) results are not significant. On the remaining one instances, result of Mann-Whitney $U$ test is not meaningful as both the approaches obtained the same results in all 20 independent runs. As far as comparison in terms of average number of dominating nodes is concerned, EA/G-MP is better than ACO_DT on 10 test instances, worse than ACO_DT on 5 test instances and equal to ACO_DT on 3 test instances. From Table 6, it can be observed that as the size of the input graph increases, execution time of ACO_DT increases at a faster pace in comparison to EA/G-MP. On an average, EA/G-MP is 3 times faster than ACO_DT on the instances with 200 nodes, 6 times faster than ACO_DT on the instances with 300 nodes, 9 times faster than ACO_DT on the instances with 400 nodes and 10 times faster than ACO_DT on the instance with 500 nodes. On smallest instances with 50 nodes, EA/G-MP is 3 times slower than ACO_DT. On instances with 100 nodes, EA/G-MP is slightly slower than ACO_DT.

### 6.3 Comparison of EA/G-MP, ABC_DT and ACO_DT approaches on instances with transmission range 150 m

On 18 test instances with transmission range $150 \mathrm{~m}, \mathrm{EA} / \mathrm{G}-$ MP is better than ABC_DT on 7 test instances, worse than ABC_DT on 1 test instance and equal to ABC_DT on 10 test instances in terms of quality of the best solution obtained. On the other hand, average solution quality of EA/G-MP is better than ABC_DT on 10 test instances, worse than ABC_DT on 4 test instances and same as ABC_DT on the remaining 4 instances. Results of Mann-Whitney $U$ test between EA/G-MP and ABC_DT indicate that out of 18 test instances, results of EA/G-MP is statistically significant on 6 test instances in comparison to ABC_DT, whereas on 8 test instances (100_1, 100_2, 200_1, 200_2, 200_3, 300_1, 300_2 and 400_2) results are not significant. On the remaining four instances, results of Mann-Whitney $U$ test are not meaningful as both the approaches obtained the same results in all 20 independent runs. As far as comparison in terms of average number of dominating nodes is concerned, EA/GMP is better than ABC_DT on 7 test instances, worse than ABC_DT on 5 test instances and equal to ABC_DT on 6 test instances. Our EA/G-MP approach is much faster than ABC_DT approach. On all 18 test instances the average total

![img-9.jpeg](img-9.jpeg)

Fig. 4 Average solution quality of various heuristics over all the instances of each size for different transmission ranges. a Transmission range 100 m . b Transmission range 125 m . c Transmission range 150 m
execution time (ATET) of EA/G-MP is better than ABC_DT. From Table 7, it can be observed that as the size of the input graph increases, the gap in terms of computational time between ABC_DT and EA/G-MP increases as well. On an average, EA/G-MP is 2 times faster than ABC_DT on the instances with 50 nodes, 3 times faster than ABC_DT on the instances with 100 nodes, 5 times faster than ABC_DT on the instances with 200 nodes, 8 times faster than ABC_DT on the instances with 300 nodes, 11 times faster than ABC_DT on the instances with 400 nodes and 16 times faster than ABC_DT on the instance with 500 nodes.

Next, we compare EA/G-MP with ACO_DT. Out of 18 test instances, the best solution of EA/G-MP is better than ACO_DT on 8 test instances and on the remaining 10 test instances both approaches obtained the same best solution. In terms of average solution quality, EA/GMP is better than ACO_DT on 8 test instances, worse than ACO_DT on 5 test instances and on the remaining 5 test instances both the approaches have the same average solution quality. Results of Mann-Whitney $U$ test
between EA/G-MP and ACO_DT show that out of 18 test instances, results of EA/G-MP is statistically significant in comparison to ACO_DT on 9 test instances whereas on 5 test instances (100_2, 200_2, 300_1, 400_1 and 500_3) results are not significant. On the remaining four instances, results of Mann-Whitney $U$ test are meaningless as both the approaches obtained the same results in all 20 independent runs. As far as comparison in terms of average number of dominating nodes is concerned, EA/G-MP is better than ACO_DT on 10 test instances, worse than ACO_DT on 3 test instances and equal to ACO_DT on remaining 5 test instances.

ACO_DT is also slower than EA/G-MP. From Table 7, it can also be observed that as the size of the graph increases, execution time of ACO_DT increases at a much faster rate compared to EA/G-MP. On an average, EA/G-MP is 3 times faster than ACO_DT on the instances with 200 nodes, 5 times faster than ACO_DT on the instances with 300 nodes, 7 times faster than ACO_DT on the instances with 400 nodes and 10 times faster than ACO_DT on the instance with 500

![img-10.jpeg](img-10.jpeg)

Fig. 5 Average solution quality of ABC_DT, ACO_DT and EA/G-MP over all the instances of each size for different transmission ranges. a Transmission range 100 m . b Transmission range 125 m . c Transmission range 150 m
nodes. On the other hand, EA/G-MP is 3 times slower than ACO_DT on the instances with 50 nodes and slightly slower than ACO_DT on the instances with 100 nodes.

### 6.4 The overall picture

Figures 4 and 5 graphically compare the average solution quality of various approaches over all the instances of each size viz. 50, 100, 200, 300, 400 and 500 for different transmission ranges. Figure 4 compares different problem specific heuristics, viz. MST-L, Heu_DT1, Heu_DT2, H_DT and M_DT, whereas Fig. 5 compares various metaheuristic approaches, viz. ABC_DT, ACO_DT and EA/G-MP. Figure 4 clearly shows that as the problem size increase, the cost of the dominating tree grows rapidly for MST-L, Heu_DT1 and Heu_DT2, thereby restricting the utility of these three heuristics to small size instances only. Like M_DT, H_DT also scales well, but its results are always inferior on an average to those of M_DT. If we look at Fig. 4a-c together, it can be observed that with the increase in transmission range, the average cost of dominating tree returned by H_DT and M_DT decreases for the same node size, which is also expected theoretically. On the other hand, average cost of the dominating tree returned by other heuristics seem to remain unaffected by the increase in transmission range.

Figure 5 shows that all the metaheuristic approaches scale well with regard to average solution quality as size of the problem increases. Except for instances of size 200 and range 100 m , average solution quality of EA/G-MP is better than ABC_DT and ACO_DT on all other sizes and transmission ranges. Looking at the Fig. 5a-c together, we can observe that the average cost of the dominating tree returned by all the three metaheuristic approaches decreases with increase in transmission range.

Figure 6 graphically compares the average total execution time of ABC_DT, ACO_DT and EA/G-MP over all the instances of each size for the transmission range 100, 125 and 150 m . The average total execution time of ABC_DT and ACO_DT grows rapidly with increase in instance size. Only EA/G-MP scales well with increase in instance size in terms

![img-11.jpeg](img-11.jpeg)

Fig. 6 Average total execution time of ABC_DT, ACO_DT and EA/G-MP over all the instances of each size for different transmission ranges. a Transmission range 100 m . b Transmission range 125 m . c Transmission range 150 m
of average total execution time. Some interesting observations can be made if we look at Fig. 6a-c together. Average total execution time of ABC_DT increases with increase in transmission range. On the other hand, average total execution time of ACO_DT decreases with increase in transmission range. For EA/G-MP also average total execution time decreases, but only slightly when compared to ACO_DT.

To get an idea about the effect of increase in transmission range on number of dominating nodes, we have found the best value among average number of dominating nodes returned by ABC_DT, ACO_DT and EA/G-MP on each size for different transmission ranges. We have plotted these best values for each transmission range against node sizes. Resulting plot is shown in Fig. 7. This figure clearly shows that the number of dominating nodes decreases on an average with increase in transmission range. This is also expected theoretically as with increase in transmission range, degree of underlying disk graphs increases, leading to dominating trees with lesser number of nodes.

Though better than other approaches in their respective classes in terms of solution quality, both of our approaches obtain dominating tree with slightly more number of nodes on some instances when we compare M_DT to H_DT, and, EA/G-MP to ABC_DT and ACO_DT. Actually, sometimes even when a pair of node is connected directly by an edge, it may not be the shortest path between them. Instead a shortest path may involve one or more intermediate nodes. As a result, a dominating tree which has lesser cost than another may not have a lesser number of nodes as well. As our approaches favour shortest paths over direct edges more often in comparison to corresponding previous approaches, dominating trees obtained through our approaches are more likely to have more nodes.

## 7 Conclusions

In this paper we have presented two approaches, viz. a problem specific heuristic called M_DT and a hybrid approach

![img-12.jpeg](img-12.jpeg)

Fig. 7 Best ANDN among ABC_DT, ACO_DT and EA/G-MP on each problem size for different transmission ranges
called EA/G-MP that combines evolutionary algorithm with guided mutation with two improvement procedures for the dominating tree problem (DTP). On 54 benchmark instances of various sizes and transmission ranges, M_DT produced better results in comparison to state-of-the-art problem specific heuristic approaches available in the literature. Similarly, EA/G-MP is able to find better solutions on most of the test instances when compared to two state-of-the-art metaheuristic approaches, viz. ABC_DT and ACO_DT in a much shorter time.

As a future work, we intend to extend our approach to other related $\mathcal{N} / \mathcal{P}$-hard problems like the connected minimum weight dominating set problem and the capacitated minimum weight dominating set problem. Analogous approaches can be developed for the set covering problem, the minimum weight vertex cover problem and various target coverage problems in wireless sensor networks etc.

Acknowledgments Authors are grateful to two anonymous reviewers for their valuable comments and suggestions which has helped in improving the quality of this paper.
