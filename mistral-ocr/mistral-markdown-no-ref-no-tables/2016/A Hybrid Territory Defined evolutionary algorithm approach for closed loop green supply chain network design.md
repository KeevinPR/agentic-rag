# A Hybrid Territory Defined evolutionary algorithm approach for closed loop green supply chain network design 

Anurag Tiwari ${ }^{\text {a }}$, Pei-Chann Chang ${ }^{\text {a,b,c, }}$, M.K. Tiwari ${ }^{\text {c }}$, Rishabh Kandhway ${ }^{\text {c }}$<br>${ }^{a}$ Department of Information Management, Yuan Ze University, No. 135, Yuan-Tung Road, Chungli, Taoyuan 32003, Taiwan<br>${ }^{b}$ Innovation Center for Big Data Er Digital Convergence, Yuan Ze University, No. 135, Yuan-Tung Road, Chungli, Taoyuan 32003, Taiwan<br>${ }^{c}$ Department of Industrial Engineering and Management, Indian Institute of Technology, Kharagpur, Kharagpur 721302, India

## A R T I C L E I N F O

Article history:
Available online 18 May 2016

Keywords:
SCM
GCLSP
EDA
NSGAII
EDATDEA

## A B S T R A C T

The Closed loop Supply chain network distribution is one of the most important problems with much real world application in supply chain management area. Presently climate change problem is one of the major concerns for Researchers. Closed loop green supply chain (GCLSC) problem is the extension of closed loop supply chain problem. Semiconductor industries are one of the major industries and a number of waste products in semiconductor industries are quite high. We have considered reducing the waste in semiconductor by recycling the useful waste electronic equipment. In GCLSC, we consider to maximize the profit in forward supply chain whereas we attempt to minimize the Carbon footprints at the same time. In this paper we used a hybrid of Estimation of distribution algorithm (EDA) and Territory Defined multi-objective algorithm to select the optimum number of facilities in the closed loop supply chain network. To examine the effectiveness of our Hybrid Territory Defined algorithm (EDATDEA), we compare the results with those obtained by NSGA II on a same GCLSC problem with different problem sizes and the same data sets.
(c) 2016 Elsevier Ltd. All rights reserved.

## 1. Introduction

Climate change problem have become one of the major threats on earth. Many toxic gases such as Carbon dioxide, carbon mono oxide and many greenhouse gases are one of the biggest contributors to the threats. Dumb products are another major contribution to environment pollution. Today people, government, and business organization are more concerned about the climate change and reducing pollution and global warming.

In today's competitive and global market, the success of an industry is reliant upon the management of its supply chains. Supply chain network design includes all the internal and external components of supply chain management (SCM). Nowadays, customers want the products at the minimum possible cost, whereas firm has many objectives such as maximization of profit, reducing the carbon footprint and recycling the products. So it is important that a firm organizes the plants; retailer, supplier, distribution center and customer zone in such a manner that customer obtains the product at minimum cost and the firm should maintain their profit and minimize carbon footprint. Under these competitive missions,

[^0]firms are using different ways for environment protection. Few firms are considering satisfying the customer by development of green product which can be environmental friendly. Another way is to reduce the raw material by recycling the product. To reduce the environment damage, waste products, use the green raw material and reduce the carbon dioxide emission and push the firm to adopt the Green Supply chain. From this perspective, green supply chain can help companies to reach a more competitive position, higher profitability, and better performance by satisfying their customers more effectively Sarkis (2003). The reverse supply chain has been continually developed not only as a result of the associated economic profit but also because of the ecological motivation, Georgiadis and Vlachos (2004). Nakamura and Kondo (2006) proposed a waste input-output life-cycle cost analysis of the recycling of end-of-life electrical home appliances. Pohlen and Farris (1992) have investigated the reverse distribution channel structure in plastic recycling and analyzed the compaction and routing issues related to transportation in the RL process. The most important objectives of green supply chain management were reducing cost, increasing profit as well as protecting the environment by recycling, reusing, reworking, remanufacturing, refurbishing, reclaiming, and reducing to design reverse logistics by using closed loop supply chain management (Srivastava, 2007). Mutha and Pokharel (2009) proposed a Strategic network design for reverse


[^0]:    a Corresponding author at: Department of Information Management, Yuan Ze University, No. 135, Yuan-Tung Road, Chungli, Taoyuan 32003, Taiwan.

    E-mail address: iepchang@uztorn.yzu.edu.tw (P.-C. Chang).

logistics and remanufacturing using new and old product modules. Closed-loop supply chain (CLSC) focuses on recycling the products by taking them back from the customers. Faccio, Persona, Sgarbossa, and Zanin (2011) apply different supply chain (SC) design approaches in the presence of reverse flows, analyzing the network structure where they considered flows are forward flow exclusively, or forward and reverse flows, or integral closed-loop flows. Last few years closed loop supply chain gained considerable attention of researchers as well as many companies. The definition of closed loop supply chain is the design, control, and operation of a system to maximize value creation over the entire life cycle of a product, with dynamic recovery of value from different types and volumes of returns over time Guide and Van (2009). Koh, Hwang, Sohn, and Ko (2002) proposed an optimal ordering and recovery policy for reusable items. The remanufacturing poses an interesting question with respect to the design and management of closed loop supply chain, Canan, Bhattacharya, Luk, and Wassenhove (2004). Traditional supply chains have been designed in single direction network, called forward logistic with the need of recycling products and decrease the waste products at the end of cycle. However, reverse and closed loop supply chain become as a most important tools for companies which is based on environmental concerns and regulations. The main application of reverse supply chain is to improve reclamation of the products at the end of their life cycle, Meade and Sarkis (2007). Past few years, the closed loop supply chain problem gains more attention. Many researchers have been proposed different closed loop supply chain models in different conditions. Abdolhossein et al. (2012) proposed an overview about closed loop supply chain, and authors discuss different aspects of closed loop supply chain and how it can help to protect the environment. Most of the researchers' concerns are about use of the few raw materials by using the recovery products. To collect the end-of-cycle product from the customers is a big problem. Canan et al. (2004) developed a closed loop supply chain model with product remanufacturing and proposed an idea about collecting recycle product in three different ways. They suggested that firms can collect product by themselves, or firms can provide a suitable incentives to an existing retailer, or firms can subcontract the collection activity to a third party. Lee and Lee (2013) proposed a modeling and optimization of closed-loop supply chain considering order or next arrival of goods.

Presently semiconductor manufacturing industries are one of the major industries. In 2010 Semiconductor market exceeded more than 300 billion USD worldwide. Semiconductor industries are one of the most energy intensive. Therefore it needs to be more environmental friendly and energy efficient. In Semiconductor Company the most important challenge is the complexity of the manufacture of integrated circuits and the role of globalization in their production. Due to the globalization and new inventions, industries need to manufacture the new products and replace their old products, which increase the number of dumb electronic products. In this paper we have considered the recycling the electronic waste equipments, which can minimize the total cost of closed loop supply chain as well as reduce the dumb electronic equipment. Author proposed a model that integrates forward and reverse logistic to satisfy the demand in case of limited recovery electronic materials. Özkir and Basligil (2013) proposed a multiobjective optimization of closed-loop supply chain in uncertain environment. Author examined the problem through product recovery chain regarding the consumer sourced returns, end-ofuse products and end-of-life products. A multi-objective model for a closed loop supply chain network design with uncertain parameters, such as cost coefficient and customer demands was proposed by Fallah, Sahraeian, Tavakkoli, and Moeinipour (2012).

Author proposed an interactive possibilities approach to solve the multi-objective mixed integer linear programming model. Kannan, Sasikumar, and Devika (2010) proposed a genetic algorithm approach for solving a closed loop supply chain a case study of battery recycling. The Closed loop green supply chain is the extension of closed loop supply chain. Last few year researchers concern more on Green supply chain. Yang, Lu, Haider, and Marlow (2013) proposed the effect of green supply chain management on green performance and firm competitiveness in the context of container shipping in Taiwan. Sustainable SC through the complete reprocessing of end-of-life products by manufacturers: A traditional versus social responsibility company perspective proposed by Faccio, Persona, Sgarbossa, and Zanin (2014). In this study, author introduced a linear programming model to minimize the total cost in forward supply chain with Environmental sustainability by the complete reprocessing of the re-use of components, an end-of life product, the disposal of unusable parts sent directly from the manufacturers, with a closed loop transportation system that maximizes transportation efficiency. Kannan and Popiuc (2014) proposed reverse supply chain coordination by revenue sharing contract; author discussed a case study of personal computer industry. Brandenburga, Kannan, Sarkis, and Seuring (2014) proposed quantitative models for sustainable supply chain management: Developments and directions. Lu, Qi, and Liu (2014) addressed about two important issues of recycling; they proposed that the industry contains small-scale and inefficient recycling firms and the output from recycling a multi-components wasted product has multiple recycling products that cannot be recycled efficiently by a single firm. Giovanni (2014) proposed Environmental collaboration in a closed-loop supply chain with a reverse revenue sharing contract. Author considered a closed-loop supply chain (CLSC) with a single manufacturer and a single retailer who invest in green advertising to build up the goodwill dynamic. To address these issue author proposed on the cooperation of recycling operation. In this paper we have proposed a new model for closed loop green supply chain in semiconductor industries, and we used nine echelons, five are in forward direction and four in reverse direction for carrying back used products and extracting value from it. We used a new approach EDATDEA to solve the 9 different closed loop green supply chain problems. EDA is a probabilistic based know evolutionary approach. Initial population generation is based on the EDA, which provides better chromosome from the starting of the procedure. After generating the initial population we have used territory defined evolutionary approach (TDEA) to solve the proposed model. Territory defined evolutionary approach selects the best solution during the nondominated sorting. We compared our result with the well know multi-objective algorithm NSGA II.

The paper is organized as follows: In Section 2 we have proposed the model and its mathematical formulation. Solution methodology is described in Section 3. Computation results are described in Section 4. Conclusion is described in Section 5.

## 2. Model descriptions

We have considered a closed loop supply chain with nine echelons, five are in forward direction and four in reverse direction for carrying back used products and extracting value from it (see Fig. 1). Case of coordinate supply chain was considered as it minimizes the supply chain cost. The costs that are considered in our analysis are, cost of raw material supplied by Supplier, cost of production by Manufacturer, repairing and recycling cost at Repairing Center, cost of disposing at Disposal Center, returns cost given by the Return Center to the customer as perk for returning the pro-

![img-0.jpeg](img-0.jpeg)

Fig. 1. Closed loop green supply chain.
duct and inventory holding cost for Distributor, Wholesaler and Centralized Collection Center. Suppliers supply multiple raw materials and Manufacturer produces multiple products, and each has different costs and material requirement. As shown in Fig. 2, at Recycling Center all the products coming from Centralized collection center are first inspected, and then they are divided in three categories, (1) products that are repairable, (2) products that are recyclable, and (3) products that have to be disposed. Repairable product are repaired, repacked and sent back to distribution center and supplied to the market as new products. Products that are recyclable are recycled and sent to manufacturing center where these are used as raw material along with those coming from Supplier, for manufacturing new products. The products that can neither be repaired nor be recycled are sent to Disposal Center and disposed of.

In past years many researcher have done sufficient work for product recovery. Gupta and Isaacs (1997) and Gungor and Gupta $(1998,1999)$ proposed a model for product recovery. Author has discussed about sequence planning for product with defective parts in product recovery and disposal strategies. Lambert (2002) proposed a model to determine optimum disassembly sequences in electronic equipment. The above described model is useful for a semiconductor manufacturing company; products such as RAM, Hard Disk, Processor, Screws, television, mobile phone, notebook are manufactures using different IC and different electronic material. Suppliers deliver different kinds of semiconductor material to manufacturing company and using this semiconductor material
company develops the final product. The material requirements can be specified with the help of bill of material for products. Similarly, when at Recycling Center the product is inspected, if some parts are damaged then those parts are replaced by new ones, repacking is done and the product is sent to Distributor. If many parts are damaged then the usable components are extracted and sent to Manufacturer where it is reused as raw materials for new Products. If the above two cases are not possible then the Product is sent to Disposal center where it is disposed of.

### 2.1. Assumptions

Various assumptions involved in the model are described below:

- Demand is deterministic i.e. demand for a period is known beforehand and the planning is done accordingly.
- Time taken to transfer a product is negligible.
- Inventory is not allowed at Supplier, Manufacturer, Disposal Center.
- Selling price of the product is inclusive of the inventory holding cost at the retailer.
- Inspection cost is negligible as compared to repairing, recycling and disposal cost.
- The supply chain model considered is a coordinated supply chain.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Recycling center model.

- Emission is majorly caused by the production of raw materials by the Supplier, manufacturing process by Manufacturer, recycling of products at Recycling Center and Disposal.


### 2.2. Notations

### 2.2.1. Indices

### 2.2.2. Parameters


Manufacturer $j$
$c_{i b} v_{k b} \quad$ Per unit inventory holding cost of product $b$ at Distributor $k$
$c_{i n v_{l b}} \quad$ Per unit inventory holding cost of product $b$ at Wholesaler $l$
$c_{e t} t_{p b} \quad$ Per unit return cost of product $b$ at Return Center $p$ Per unit inventory holding cost of product $b$ at Centralized Return Center $o$
$c_{e t p_{n b}} \quad$ Per unit repairing cost of product $b$ at Recycling Center $n$
$c_{e c_{n b}} \quad$ Per unit recycling cost of product $b$ at Recycling Center $n$
$c_{d i s_{q b}} \quad$ Per unit disposing cost of product $b$ at Disposing Center $q$
$c_{a b} \quad$ Number of units of raw material $a$ required to make one unit of product $b$
$\propto \quad$ Proportion of returned products that go for repairing
$j i \quad$ Proportion of returned product that go for recycling
$c f p_{t a} \quad$ Per unit carbon emission for manufacturing of raw material $a$ at Supplier $i$
$c f p_{j b} \quad$ Per unit carbon emission for manufacturing of product $b$ at Manufacturer $j$
$c f p_{n b} \quad$ Per unit carbon emission for recycling of product $b$ at Recycling Center $n$
$c f p_{q b} \quad$ Per unit carbon emission for disposal of product $b$ at Disposal Center $q$
$k \quad$ Proportionality constant for converting transportation cost to carbon emission
supcap $_{n a} \quad$ Capacity of Supplier $i$ to supply raw material $a$
$m f g c a p_{j b} \quad$ Capacity of Manufacturer $j$ to manufacture product $b$
invcap $_{k b} \quad$ Inventory holding capacity of Distributer $j$ for product $b$
invcap $_{l b} \quad$ Inventory holding capacity of Wholesaler $i$ for product $b$
invcap $_{n b} \quad$ Inventory holding capacity of Centralized Collection Center $o$ for product $b$
repcap $_{n b} \quad$ Repairing capacity of Recycling Center $n$ for product $b$
reccap $_{n a} \quad$ Recycling capacity of Recycling Center $n$ for raw material $a$
discap $_{q b} \quad$ Disposing capacity of Disposal Center $q$ for product $b$

### 2.2.3. Decision variables

(continued on next page)

Return Center $o$ to Recycling Center $n$ in period $t$
$q r_{n j b t} \quad$ Units of product $b$ transported from Recycling Center
$n$ to Manufacturer $j$ after Recycling in period $t$
$q r_{n k b t} \quad$ Units of product $b$ transported from Recycling Center
$n$ to Distribution Center $k$ after Repairing in period $t$
$q r_{n q b t} \quad$ Units of product $b$ transported from Recycling Center
$n$ to Disposal Center $q$ after in period $t$
$q i n v_{k b t}$ Number of units of product $b$ stored at Distribution Center $k$ during period $t$
$q i n v_{l b t} \quad$ Number of units of product $b$ stored at Wholesaler $l$ during period $t$
$q i n v_{o b t} \quad$ Number of units of product $b$ stored at Distribution Center $o$ during period $t$

### 2.3. Objective function

The objective of analysis was to determine the combination of quantities of a product or raw material to be transferred between two stages such that total cost of the supply chain and carbon emissions in the supply chain is minimized. In Eq. (1) we use the forecasted value of demand which is assumed to be constant, so the revenue is calculated by multiplying the demand of a product to its price at a particular retailer. In Eq. (2) we calculate total transportation cost in the supply chain by multiplying quantity transferred from a particular route to per unit transportation cost for that route. In Eq. (3) we calculate the cost of raw material by multiplying per unit cost of raw material for a particular supplier with the number of units of raw material it provides. In Eq. (4) manufacturing cost is calculated in a similar manner as raw material cost. In Eq. (5) average inventory for a time period is calculated by adding the amount of inventory with a stakeholder to the amount of products that arrived in that period and subtracting the quantity that leaves. From Eqs. (6)-(9) the costs are calculated by multiplying the quantities on which the action is taken with the cost of taking that action. In a similar fashion in Eqs. (10)-(13), emissions are calculated by multiplying per unit carbon emission with the quantities supplied by Supplier, manufactured at Manufacturer, recycled in Recycling Center, and disposed in Disposal center. Eastern Research Group (1999, chap. 6) proposes alternative methods for estimating air emission from semiconductor manufacturing. EPA (United States Environmental Protection Agency (2005) discuss about emission facts. They have discussed the calculation of the carbon dioxide emission based on transport and fuel consumption.

The two objectives of analysis were formulated as follows:

1. Max Profit $=$ Revenue - Transportation Cost - Raw Material Cost - Manufacturing Cost - Inventory Holding Cost - Return Cost - Recycling Cost - Repairing Cost - Disposal Cost.
2. Min Emissions $=$ Emission of Supplier + Emission of Manufacturer + Emission of Recycling Center + Emission of Disposal Center.

The costs mentioned in the first objective function are defined below:
Revenue $=\sum_{i n=1}^{M} \sum_{b=1}^{B}\left(P_{o n b} * \sum_{t=1}^{T} D_{o n b t}\right)$

$$
\begin{aligned}
& \text { Transportation Cost }=\sum_{i=1}^{I} \sum_{j=1}^{J} \sum_{a=1}^{A}\left(c t r a_{j a} * \sum_{t=1}^{T} q_{j a t}\right) \\
& +\sum_{j=1}^{J} \sum_{k=1}^{K} \sum_{b=1}^{B}\left(c t r a_{j k b} * \sum_{t=1}^{T} q_{j k b t}\right) \\
& +\sum_{k=1}^{K} \sum_{b=1}^{I} \sum_{t=1}^{B}\left(c t r a_{k t b} * \sum_{t=1}^{T} q_{k t b t}\right) \\
& +\sum_{i=1}^{I} \sum_{a=1}^{M} \sum_{b=1}^{B}\left(c t r a_{a n b} * \sum_{t=1}^{T} q_{a n b t}\right) \\
& +\sum_{p=1}^{O} \sum_{n=1}^{B} \sum_{b=1}^{B}\left(c t r a_{p n b} * \sum_{t=1}^{T} q r_{p n b t}\right) \\
& +\sum_{n=1}^{O} \sum_{q=1}^{N} \sum_{b=1}^{B}\left(c t r a_{n q b} * \sum_{t=1}^{T} q r_{n q b t}\right) \\
& +\sum_{n=1}^{N} \sum_{k=1}^{K} \sum_{b=1}^{B}\left(c t r a_{n q b} * \sum_{t=1}^{T} q r_{n k b t}\right) \\
& +\sum_{n=1}^{N} \sum_{j=1}^{J} \sum_{b=1}^{B}\left(c t r a_{n j b} * \sum_{t=1}^{T} q r_{n j b t}\right) \\
& \text { Raw Material Cost }=\sum_{a=1}^{A} \sum_{i=1}^{I}\left(c r m_{i a} * \sum_{j=1}^{J} \sum_{t=1}^{T} q_{j a t}\right)
\end{aligned}
$$

Manufacturing Cost $=\sum_{b=1}^{B} \sum_{j=1}^{J}\left(c m f g_{j b} * \sum_{k=1}^{K} \sum_{t=1}^{T} q_{j k t t}\right)$
Inventory Holding Cost $=\frac{1}{2} *\left(\sum_{b=1}^{B} \sum_{i=1}^{I}\left(c i n v_{l b} * \sum_{t=1}^{T} q i n v_{l b t}\right)\right.$

$$
\begin{aligned}
& +\sum_{b=1}^{B} \sum_{t=1}^{B}\left(c i n v_{k b} * \sum_{t=1}^{T} q i n v_{k b t}\right) \\
& \left.+\sum_{b=1}^{B} \sum_{a=1}^{O}\left(c i n v_{o b} * \sum_{t=1}^{T} q i n v_{o b t}\right)\right)
\end{aligned}
$$

$$
\begin{aligned}
q i n v_{k b t} & =q i n v_{k b(t-1)}+\sum_{j=1}^{J} q_{j k b t}+\sum_{n=1}^{N} q r_{n k b t}-\sum_{l=1}^{L} q_{k l b t} . \quad q i n v_{l b t} \\
& =q i n v_{l b(t-1)}+\sum_{k=1}^{K} q_{k b t}-\sum_{m=1}^{M} q_{l m b t}
\end{aligned}
$$

$$
q i n v_{o b t}=q i n v_{o b(t-1)}+\sum_{p=1}^{P} q_{p n b t}-\sum_{n=1}^{N} q_{o n b t}
$$

Return Cost $=\sum_{b=1}^{B} \sum_{j=1}^{P}\left(\operatorname{cret}_{j b t} * \sum_{t=1}^{T} R_{j b t}\right)$
Recycling Cost $=\sum_{b=1}^{B} \sum_{a=1}^{N}\left(\operatorname{cret}_{o b} * \sum_{b=1}^{B} \sum_{t=1}^{T} q r_{o k b t}\right)$

Repairing Cost $=\sum_{b=1}^{B} \sum_{n=1}^{N}\left(c r e p_{n b}+\sum_{j=1}^{J} \sum_{t=1}^{T} q r_{n j b t}\right)$
Disposal Cost $=\sum_{b=1}^{B} \sum_{q=1}^{Q}\left(c d i s_{q b}+\sum_{n=1}^{N} \sum_{t=1}^{T} q r_{n j b t}\right)$
Emission of Supplier $=\sum_{b=1}^{B} \sum_{t=1}^{J}\left(c f p_{t b}+\sum_{j=1}^{J} \sum_{t=1}^{T} q_{t j b t}\right)$
Emission of Manufacturer $=\sum_{b=1}^{B} \sum_{j=1}^{J}\left(c f p_{j b}+\sum_{k=1}^{K} \sum_{t=1}^{T} q_{j k b t}\right)$
Emission of Recycling Center $=\sum_{b=1}^{B} \sum_{n=1}^{N}\left(c f p_{n b}+\sum_{k=1}^{K} \sum_{t=1}^{T} q_{n k b t}\right)$
Emission of Disposal Center $=\sum_{b=1}^{B} \sum_{q=1}^{Q}\left(c f p_{q b}+\sum_{n=1}^{N} \sum_{t=1}^{T} q_{n j b t}\right)$

## Subject to

### 2.4. Constraints

$\sum_{t=1}^{J} q_{\text {index }}=D_{\text {index }} \quad \forall m, b, t$
$\sum_{a=1}^{Q} q_{\text {index }}=R_{\text {jakt }} \quad \forall m, b, t$
$\sum_{j=1}^{J} q_{j a t} \leqslant \sup _{a p_{t a}} \quad \forall i, a, t$
$\sum_{k=1}^{K} q_{j k b t} \leqslant m f g c a p_{j b} \quad \forall j, b, t$
$\sum_{k=1}^{K} q r_{\text {nikht }} \leqslant r e p c a p_{n b} \quad \forall n, b, t$
$\sum_{j=1}^{J} q r_{\text {njat }} \leqslant r e c c a p_{n a} \quad \forall n, a, t$
$\sum_{n=1}^{N} q r_{\text {njat }} \leqslant \operatorname{discap}_{q b} \quad \forall q, b, t$
$q i n v_{\text {lekt }} \leqslant i n v c a p_{k b} \quad \forall k, b, t$
$q i n v_{\text {ikt }} \leqslant i n v c a p_{t b} \quad \forall l, b, t$
$q i n v_{\text {sikt }} \leqslant i n v c a p_{n b} \quad \forall o, b, t$
$\sum_{b=1}^{B}\left(c_{b u}+\sum_{k=1}^{K} q_{j k b t}\right)=\sum_{t=1}^{J} q_{j a t}+\sum_{n=1}^{N} q r_{n j b t} \quad \forall j, a, t$
$\sum_{k=1}^{K} q r_{\text {nikht }}=\alpha \sum_{a=1}^{Q} q r_{\text {onut }} \quad \forall n, b, t$
$\sum_{b=1}^{B}\left(c_{b u}+\beta \sum_{a=1}^{Q} q r_{\text {onkt }}\right)=\sum_{j=1}^{J} q r_{\text {njat }} \quad \forall n, a, t$
$\sum_{q=1}^{Q} q r_{\text {njkt }}=(1-\alpha-\beta) \sum_{a=1}^{Q} q r_{\text {onut }} \quad \forall n, b, t$
Constraint (14) shows that quantity of product delivered to retailer is equal to the demand of customer, (15) shows that quantity of product shipped from a retailer is equal to units returned. Constraints (16)-(20) are capacity constraints for supplier, manufacturer, recycling, repairing and disposal of products respectively. Constraints (21)-(23) show that inventory at distributor, wholesaler and centralized collection center respectively does not exceed inventory holding capacity. The flow conservation of products at manufacturer, distributor and recycling center is shown in constraints (24)-(27).

## 3. Solution methodology

The above described problem can be classified as a NP hard problem, so we have used meta-heuristics algorithm to solve the problem statement. Two multi-objective evolutionary algorithms were used, (1) Non-Dominated Sorting Genetic Algorithm II, Deb, Pratap, Agarwal, and Meyarivan (2002) and (2) Estimation of Distribution Algorithm, Larrañaga and Lozano (2002) with Territory Defining Evolutionary Algorithm, Karahan and Oksalan (2010), Shim, Tan, and Chia (2013) proposed a multi-objective Optimization with Estimation of Distribution Algorithm in a Noisy Environment. Sun, Zhang, and Edward (2005) developed EDA: A new evolutionary algorithm for global optimization. NSGA II is one of the oldest and robust multi-objective evolutionary algorithms, so we have used it as a benchmarking algorithm to compare the results of the algorithm developed by US. Both algorithms generate Pareto optimal solutions. In the following section we describe how the algorithms were used to solve the proposed problem.

### 3.1. Non-Dominated Sorting Genetic Algorithm II

### 3.1.1. Chromosome representation and initialization

The decision variables in the problem statement are in the form of a four dimensional matrix, so it was converted in a form of array with length equal to number of elements in the matrix. The initial population was generated by randomly selecting a value between upper and lower limit for each element.

### 3.1.2. Non-dominated sorting

Non-dominated set is in which a solution is not dominated by any other solution in that set. Non-dominated sorting is used to obtain different non-dominated sets, called as fronts within the given population for multi-objective problems. At first, the parent population $\left(P_{t}\right)$ and the offspring population $\left(Q_{t}\right)$ are united to form a temporary population, $\left(R_{t}\right)$ of size $2 N$. ' $t$ ' denotes the number of current generations.

For each individual pin $R_{t}$, we calculate $n_{p}$, number of solutions which dominate the solution $p$ and $S_{p}$, a set of solutions that the solution $p$ dominates. Now all the individuals whose $n_{p}$ value is zero (no solution dominates $p$ ) are added to the first nondominated front ( 1 is the best level). Now, for each solution $p$ with $n_{p}=0$, we visit each member of its set $S_{p}$ and reduce its domination count by one. In doing so, if for any member of the set $S_{p}$ domination count becomes zero, we put it in a separate list $Q$. These members are added to the second non-dominated front. Now, the above procedure is continued with each member of $Q$ and the third front is identified. This process continues until all fronts are identified. Thus the population $R_{t}$ of size $2 N$ is then sorted into nondominated Pareto fronts, $F_{1}$ being the best non-dominated front,

![img-2.jpeg](img-2.jpeg)

Fig. 3. NSGA II flow diagram.
$F_{2}$ the second one, and so on. An iteration of non-dominated sorting is as shown in Fig. 3.

### 3.1.3. Crowding distance

Crowding distance is the density estimator of the solutions surrounding a particular solution in the population. To estimate the crowding distance of a particular point (solution), we calculate the average distance of two points on either side of this point along each of the objectives. This quantity $I_{\text {distance }}$ serves as an estimate of the perimeter of the largest cuboid formed by the nearest neighbor's as the vertices enclosing the point $i$ without including any other point in the population. In Fig. 3 Deb et al. (2002), the crowding distance of the $i$ th solution in its front (marked with solid circles) is the average side length of the cuboid (with a dashed box) in the objective space.

The crowding-distance computation requires sorting the population according to each objective function value in ascending order of magnitude. Thereafter, for each objective function, the boundary solutions (solutions with smallest and largest function values) are assigned an infinite distance value. All other intermediate solutions are assigned a distance value equal to the absolute normalized difference in the function values of two adjacent solutions. This calculation is continued with other objective functions. The overall crowding distance value is calculated as the sum of individual distance values corresponding to each objective. Each objective function is normalized before calculating the crowding distance. For each front $F_{i}, n$ is the number of individuals.

### 3.1.4. Selection

Once the individuals are sorted based on non-domination and with crowding distance assigned, the selection is carried out using a crowded comparison-operator $\left(\prec_{n}\right)$. The comparison is carried out as below based on
(1) Non-domination rank $p_{\text {rank }}$ i.e. individuals in front $F_{i}$ will have their rank as $p_{\text {rank }} \neq i$.
(2) Crowding distance $F_{i}\left(d_{j}\right)$
$p \prec_{n} q$ if, prank $<$ qrank or if $p$ and $q$ belong to the same front $F_{i}$ then $F_{i}\left(d_{p}\right) \times F_{i}\left(d_{q}\right)$ i.e. the crowing distance should be more. The individuals are selected using a binary tournament selection with crowded comparison operator.

### 3.1.5. Genetic operators

Genetic operators are used in genetic algorithms to generate diversity (mutation-like operators) and to combine existing solutions into others (crossover-like operators). The main difference among them is that the former operate on one chromosome, that is, they are unary, while the latter are binary operators. To solve the described problem we have used Simulated Binary Crossover operator for crossover and Polynomial Mutation operator for mutation.
3.1.5.1. Simulated binary crossover. Simulated Binary Crossover simulates the binary crossover observed in nature as given below.
$c_{1, k}=\frac{1}{2}\left[\left(1-\beta_{k}\right) p_{1, k}+\left(1+\beta_{k}\right) p_{2, k}\right]$
$c_{2, k}=\frac{1}{2}\left[\left(1+\beta_{k}\right) p_{1, k}+\left(1-\beta_{k}\right) p_{2, k}\right]$
where $c_{i, k}$ is the $i$ th child with $k$ th component, $p_{i, k}$ is the selected parent and $\beta_{k}(\geqslant 0)$ is a sample from a random number generated having the density
$p(\beta)=\frac{1}{2}\left(\eta_{c}+1\right) \beta^{\eta_{c}}, \quad$ if $0 \leqslant \beta \leqslant 1$
$p(\beta)=\frac{1}{2}\left(\eta_{c}+1\right) \frac{1}{\beta^{\beta_{c}+2}}, \quad$ if $\beta>1$.
This distribution can be obtained from a uniformly sampled random number $u$ between $(0,1) . \eta_{c}$ is the distribution index for crossover. That is
$\beta(u)=(2 u)^{\left(\frac{1}{2} \gamma_{1}\right)}$
$\beta(u)=\frac{1}{\left[2(1-u)\right]^{\left(\frac{1}{2} \gamma_{1}\right)}}$

![img-3.jpeg](img-3.jpeg)

Fig. 4. EDATDEA flow diagram.
3.1.5.2. Polynomial mutation. The equations for the polynomial mutation are as described in the following equations, here $c_{k}$ is the child and $p_{k}$ is the parent with $p_{k}^{0}$ being the upper bound on the parent component, $p_{k}^{l}$ is the lower bound and $\delta_{k}$ is small variation which is calculated from a polynomial distribution, and in this equation $r_{k}$ is an uniformly sampled random number between $(0,1)$ and $\eta_{m}$ is mutation distribution index.
$c_{k}=p_{k}+\left(p_{k}^{0}-p_{k}^{l}\right) \delta_{k}$
$\delta_{k}=\left(2 r_{k}\right)^{\frac{1}{m_{k}-1}}-1, \quad$ if $r_{k}<0.5$
$\delta_{k}=\left[2\left(1-r_{k}\right)\right]^{\frac{1}{m_{k}-1}}$ if $r_{k} \geqslant 0.5$

### 3.1.6. Recombination and selection

The offspring population is combined with the current generation population and selection is performed to set the individuals of the next generation. Since all the previous and current best individuals are added in the population, elitism is ensured. Population is now sorted based on non-domination. The new generation is filled by each front subsequently until the population size exceeds the current population size. If by adding all the individuals in front $F_{j}$ the population exceeds $N$ then individuals in front $F_{j}$ are selected based on their crowding distance in the descending order until the population size is $N$. And hence the process repeats to generate the subsequent generations.

Table 1
NSGA II algorithm result on various crossover probability, mutation probability.
Table 2
EDATDEA result on various crossover probability, PEDA.
Table 3
NSGA II algorithm result crossover probability 0.6, mutation probability 0.1 .

Table 4
NSGA II algorithm result crossover probability 0.7 mutation probability 0.2 .

# 3.2. EDATDEA 

In Estimation of Distribution based Territory Defining Evolutionary Algorithm we use the estimation of the distribution of various decision variable using the information from the best of chromosomes in the solution. Larrañaga and Lozano (2002) developed Estimation of distribution algorithms for evolutionary com-
putation. Pan and Ruiz (2012) proposed an estimation of distribution algorithm for lot-streaming flow shop problems with setup times. It is assumed that the decision variables are independent and normally distributed. The parameters of the distribution are estimated by using the information in the top MX of chromosomes in the population. Now these distributions are used to generate a proportion of high quality solutions. After this step

Table 5
SGA II algorithm result crossover probability 0.8 mutation probability 0.3 .

Table 6
NSGA II algorithm result crossover probability 0.9 mutation probability 0.4 .

Territory Defining Evolutionary Algorithm is applied to get the pareto-optimal front. A Territory Defining Multi objective Evolutionary Algorithms and Preference Incorporation was proposed by Karahan and Oksalan (2010). In subsequent section we define each step of the algorithm in detail (see Fig. 4).

## Pseudo Code:

Initialize Population $P(0)$ generated randomly, by selecting a value between upper and lower limit
Non-Dominated Sorting of $P(0)$
Initialize Archive Population A(0) set of initial population $P(0)$ lying in first non-dominated front
Repeat until stopping condition is reached
Generate a random number R1 between 0 and 1
If R1 is less than PEDA (probability of using EDA algorithm)

Generate offspring using EDA Algorithm Else
Generate a random number R2 between 0 and 1
If R2 is less than PC (probability of crossover)
Generate offspring using Simulated Binary crossover algorithm

## Else

Generate offspring using Polynomial Mutation algorithm

## End

End
Mark all chromosomes in $P(t)$ that dominates the generated offspring
If Offspring is dominated by any chromosome in $P(t)$ Reject offspring
Check stopping condition
Else
Mark all chromosomes in $A(t)$ dominated by offspring Remove all marked chromosomes from $A(t)$ Calculate scaled rectilinear distance of Offspring from each chromosome in $A(t)$

Calculate maximum scaled absolute objective difference between offspring and chromosome in $A(t)$ having minimum scaled rectilinear distance

If maximum scaled absolute objective difference is greater than territory size Accept offspring in $A(t)$ Else

## Reject Offspring

Check stopping condition
End

Territory Defining Evolutionary Algorithm is applied to get the pareto-optimal front. A Territory Defining Multi objective Evolutionary Algorithms and Preference Incorporation was proposed by Karahan and Oksalan (2010). In subsequent section we define each step of the algorithm in detail (see Fig. 4).

![img-4.jpeg](img-4.jpeg)

Fig. 5. NSGA II algorithm result crossover probability and mutation probability.
have used EDA, Simulated Binary Crossover and polynomial mutation operator to generate the offspring based on the probability

Table 7
Different cases for closed loop green supply chain problem.
and stopping criterion. The selection of offspring is first tested into regular population $(P(t))$ and then it is tested into archive population $(A(t))$. The entire individuals that are dominated by offspring are marked if offspring is dominated by at least one chromosome in $P(t)$, it rejected and a new offspring generated. For offspring to be accepted in archive population should not lie in the territory of any of the existing chromosome in the archive population. The chromosome with the minimum scaled rectilinear distance is selected and maximum scaled absolute objective difference is calculated between offspring and the selected chromosome for all the objectives. The detailed procedure of EDATDEA is as follows.
![img-5.jpeg](img-5.jpeg)

Fig. 6. EDATDEA result crossover probability and mutation probability.

Table 8
Performance comparison of EDATDEA and NSGA II algorithm for different cases.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Pareto optimal front comparison for case 1.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Pareto optimal front comparison for case 4.

### 3.2.1. Initialization, non-dominated sorting $\mathcal{E}$ ranking

The steps used are same as that used in NSGA II. The main difference is that here we have two population instead of one. The size of one population is fixed whereas the other population varies depending upon the number of solutions we have in the first front. The first population i.e. $P(0)$ is initialized, sorted and ranked in the same way as NSGA II. The second population also known as archive population, $A(0)$ is the set of non-dominated individuals. They are initialized by selecting the solutions from $P(0)$ that lie in the first front.

### 3.2.2. Offspring generation

Three different procedures are used for offspring generation in the algorithm. With a probability of PEDA offspring is generated
![img-8.jpeg](img-8.jpeg)

Fig. 9. Pareto optimal front comparison for case 5.
![img-9.jpeg](img-9.jpeg)

Fig. 10. Pareto optimal front comparison for case 8.
using Estimation of Distribution. The procedure used for generation is, top $\mathrm{M} \%$ of the chromosomes from population are selected. Since using these values of the decision variable we get solutions of good quality, the mean of these values is used as estimates of the mean of normal distribution. The standard deviation of the normal distribution is assumed to be one tenth of the difference of limits for each decision variable. With probability $(1-P E D A) * P C$ offspring is generated using Simulated Binary Crossover operator as described in the NSGA II. With probability $(1-P E D A) *$ $(1-P C)$ offspring were generated using polynomial mutation operator.

### 3.2.3. Criteria for acceptance in $P(t)$

The offspring is first tested for acceptance into regular population, and then it is tested for acceptance into archive population.

![img-10.jpeg](img-10.jpeg)

Fig. 11. Pareto optimal front comparison for case 9.
The evaluation procedure is as follows, first the offspring is tested for dominance. All the individuals that are dominated by offspring are marked, if offspring is dominated by at least one chromosome in $P(t)$, it is rejected and a new offspring is generated, otherwise
offspring is accepted and a marked individual is randomly selected and removed from $P(t)$. If none of the individual is marked then a chromosome is randomly selected and removed.

### 3.2.4. Criteria for acceptance in $A(t)$

For offspring to be accepted in archive population, it should not lie in the territory of any of the existing chromosomes in the archive population. The procedure is as follows, the offspring is tested for dominance, all the individuals dominated by offspring are marked, if it is dominated by any individual in $A(t)$ then it is rejected. If it is not dominated by any individual then all the marked individuals are removed from $A(t)$ and we calculate the scaled rectilinear distance of offspring from each chromosome. The chromosome with the minimum scaled rectilinear distance is selected and maximum scaled absolute objective difference is calculated between offspring and the selected chromosome for all the objectives. If it is more than the territory size the offspring is accepted in archive population else it is rejected and a new offspring is generated.

Scaled Rectilinear Distance : $d_{i c}=\sum_{j=1}^{m}\left|f_{i j}-f_{i j}\right|$

Table 9
Result comparison for case 1.
Case 1 Results

Table 10
Result comparison for case 4.

Table 11
Result comparison for case 5.
$m=$ number of objective, $i=$ chromosome number varies from 1 to number of chromosomes in archive population, $f=$ normalized value of the objective function, $c=$ offspring chromosome.

Maximum Scaled Absolute Objective Difference : $\delta$
$=\max \left|f_{i j}-f_{i j}\right|$
$i^{\circ}=$ chromosome with minimum scaled rectilinear distance, $f=$ normalized value of the objective function, $c=$ offspring chromosome.

# 4. Simulation result 

In this paper, we used a hybrid TDEA algorithm to solve the closed loop green supply chain problem. The proposed model

Table 12
Result comparison for case 8 .
was evaluated for robustness on nine test problems. The data were randomly chosen and modification in the design of supply chain was done. To check the performance of the proposed algorithm, comparison was made with NSGA II. First we tune the parameters for both the algorithms by selecting different values of a parameter and selecting the one with the best results. Then results for same problem at optimal parameter setting were compared for both the algorithms to check the performance of both algorithms. Time of run for both the algorithms was kept as 600 s and an initial population of 50 was selected for both the algorithms The performance of hybrid TDEA algorithm is tested on different problem sets. It should be noted that same number of generations and same population sizes are used for both algorithms. For the fare comparison
we test the result of NSGA II on different parameters and select the best parameter. To select the best parameter we have run both algorithms on different parameter and after comparison we select the best parameter. Tables 1 and 2 show the parameter result comparison.

Tables 3-6 show the NSGA II results on different parameters. Fig. 5 shows the Pareto optimal front of NSGA II algorithm for different crossover and mutation probability. From the following table and figure we have selected the best parameter values for NSGA II algorithm.

Fig. 6 shows the Pareto optimal front of EDATDEA for different crossover and mutation probability. From the following table and

Table 13
Result comparison for case 9 .

figure we have selected the best parameter values for NSGA II algorithm.

In this paper we have select 9 cases to test our results. Following Table 7 shows the cases under we run both the algorithms. For fare comparison we have run the algorithm for same time. We have run both the algorithms for 600 s and calculate the profit and carbon dioxide emission.

Table 8 shows the performance comparison for different cases. A comparison of maximum profit, minimum carbon dioxide emission, average profit and average emission obtaining from EDATDEA and NSGAII algorithm is as shown in following table. We have used small size, minimum size and large size problem to compare the result of EDATDEA and NSGAII. As shown in table EDATDEA has performed better than NSGAII for all cases.

Following Figs. 7-11 and Tables 9-13 show the Pareto front comparison of EDATDEA and NSHGA II algorithm for different cases. For different cases Figures shows that the EDATDEA has better Pareto front than the NSGA II algorithm. EDATDEA can get the near optimal value in limited number of iteration. From figure we can say that EDATDEA performs better than NSGAII in all cases and has the better results.

## 5. Conclusions

Closed loop green supply chain management in semiconductor industries has received much attention in last few years as it allows reducing the carbon dioxide emission and increasing the profit of total supply chain. We have considered a closed loop supply chain with nine echelons, five are in forward direction and four are in reverse direction for carrying back used products and extracting value from it. To solve our model we proposed a new approach named EDATDEA. In order to verify our proposed approach, we have applied EDATDEA on different cases of supply chain and compare with well know approach NSGA II. From the result we can say that this model can be used for the real life problem. The results clearly show that the EDATDEA approach performs better than NSGA II algorithm. EDATDEA can get the near optimal results in limited number of time. In future we can implement some new techniques and model to solve the Green supply chain problem in semiconductor industries. This model can be useful for any industry. In future we can use the real data set or industry to check the applicability of the proposed model.
